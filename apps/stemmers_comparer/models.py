from django.db import models
from decimal import Decimal
from django.db.models import Avg, Count, Sum
from model_utils.models import TimeStampedModel

# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    github_account_link = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name


# ProgrammingLanguage Model
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Requirement Model
class Requirement(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


# Feature Model
class Feature(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


# Stemmer Model
class Stemmer(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    display_name = models.CharField(max_length=50)
    is_enabled = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author)
    license = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    documentation_link = models.CharField(max_length=255, null=True)
    download_link = models.CharField(max_length=255, null=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    requirements = models.ManyToManyField(Requirement)
    features = models.ManyToManyField(Feature)
    how_to_use = models.TextField(null=True)

    def __str__(self):
       return self.display_name

    class Meta:
        ordering = ['name']


class RatingManager(models.Manager):
    # instance = stemmer

    def for_instance(self, instance):

        ratings, created = self.get_or_create(stemmer=instance)

        return ratings

    def rate(self, instance, score, user_email_address, user_github_account_link=None, comment=''):

        existing_rating = UserRating.objects.for_instance_by_user(instance=instance, user_email_address=user_email_address)

        if existing_rating:
            for existing_rating_ in existing_rating:
                existing_rating_.score = score
                existing_rating_.save()
            return existing_rating_.rating

        else:

            rating, created = self.get_or_create(stemmer=instance)
            return UserRating.objects.create(user_email_address=user_email_address, user_github_account_link=user_github_account_link, comment=comment, score=score, rating=rating).rating


# Rate Model
class Rate(models.Model):
    count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
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
            'percentage': self.percentage
        }

    def __str__(self):
        return str(self.id)

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

    def __str__(self):
        return str(self.id)



class UserRatingManager(models.Manager):

    def for_instance_by_user(self, instance, user_email_address):

        rating = self.filter(user_email_address=user_email_address, rating__stemmer=instance)
        return rating

# UserRating Model
class UserRating(TimeStampedModel):

    """
    An individual rating of a user against a model.
    """
    user_email_address = models.EmailField()
    user_github_account_link = models.CharField(max_length=255, null=True)
    comment = models.TextField()
    score = models.CharField(max_length=5)
    rating = models.ForeignKey('rating', related_name='user_ratings', on_delete=models.CASCADE)

    objects = UserRatingManager()

    class Meta:
        unique_together = ['user_email_address', 'rating']

    def __str__(self):
        return self.user_email_address


