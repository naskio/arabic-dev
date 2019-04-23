from django.db import models
from decimal import Decimal
from django.db.models import Avg, Count, Sum
from model_utils.models import TimeStampedModel
import swapper
from . import get_star_ratings_rating_model_name, get_star_ratings_rating_model


# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    github_account_link = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ProgrammingLanguage Model
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Requirement Model
class Requirement(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


# Feature Model
class Feature(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# Stemmer Model
class Stemmer(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    display_name = models.CharField(max_length=80)
    is_enabled = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author, blank=True)
    license = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    documentation_link = models.URLField(null=True, blank=True)
    download_link = models.URLField(null=True, blank=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, blank=True)
    requirements = models.ManyToManyField(Requirement, blank=True)
    features = models.ManyToManyField(Feature, blank=True)
    how_to_use = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.display_name

    class Meta:
        ordering = ['name']


class RatingManager(models.Manager):
    # instance = stemmer
    def rate(self, instance, score, user_email_address, user_github_account_link=None, comment=''):

        existing_rating = UserRating.objects.for_instance_by_user(instance, user_email_address)

        if existing_rating:

            existing_rating.score = score
            for existing_rating_ in existing_rating:
                existing_rating_.save()
            return existing_rating_.rating

        else:

            rating, created = self.get_or_create(stemmer=instance)
            return UserRating.objects.create(user_email_address=user_email_address,
                                             user_github_account_link=user_github_account_link, comment=comment,
                                             score=score, rating=rating).rating


# Rate Model
class Rate(models.Model):
    count = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    average = models.DecimalField(max_digits=6, decimal_places=3, default=Decimal(0.0))
    stemmer = models.OneToOneField('stemmer', on_delete=models.CASCADE, unique=True)

    objects = RatingManager()

    class Meta:
        abstract = True

    @property
    def percentage(self):
        return (self.average / 5) * 100

    def to_dict(self):
        return {
            'count': self.count,
            'total': self.total,
            'average': self.average,
            'percentage': self.percentage,
            'stemmer': self.stemmer.name,
            'stemmer__display_name': self.stemmer.display_name
        }

    def __str__(self):
        return str(self.count)

    def calculate(self):
        """
        Recalculate the totals, and save.
        """
        aggregates = self.user_ratings.aggregate(total=Sum('score'), average=Avg('score'), count=Count('score'))
        self.count = aggregates.get('count')
        self.total = aggregates.get('total')
        self.average = aggregates.get('average')
        self.save()


class Rating(Rate):
    class Meta(Rate.Meta):
        swappable = swapper.swappable_setting('stemmers_comparer', 'Rating')


class UserRatingManager(models.Manager):

    def for_instance_by_user(self, instance, user_email_address):
        user = self.filter(user_email_address__iexact=user_email_address, rating__stemmer=instance)
        return user

    def bulk_create(self, objs, batch_size=None):
        objs = super(UserRatingManager, self).bulk_create(objs, batch_size=batch_size)
        for rating in set(o.rating for o in objs):
            rating.calculate()

        return objs


# UserRating Model
class UserRating(TimeStampedModel):
    """
    An individual rating of a user against a model.
    """
    user_email_address = models.EmailField(unique=True)
    user_github_account_link = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(max_length=1500)
    comment_date = models.DateTimeField(auto_now=True)
    # TODO: check between 0 and 5
    score = models.PositiveSmallIntegerField()
    rating = models.ForeignKey(get_star_ratings_rating_model_name(), related_name='user_ratings',
                               on_delete=models.CASCADE)

    objects = UserRatingManager()

    class Meta:
        unique_together = ['user_email_address', 'rating']

    def __str__(self):
        return self.user_email_address
