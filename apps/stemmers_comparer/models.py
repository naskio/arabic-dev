from django.db import models
from decimal import Decimal
from django.db.models import Avg, Count, Sum
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator


# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    github_account_link = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ProgrammingLanguage Model
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    website = models.URLField(null=True, blank=True)

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
    count = models.IntegerField(default=0)
    average = models.DecimalField(max_digits=6, decimal_places=5, default=Decimal(0.0))

    @property
    def rank(self):
        sts = Stemmer.objects.filter(is_enabled=True)
        index = 1
        for st in sts:
            if st.name == self.name:
                return index
            index += 1
        return None

    class Meta:
        ordering = ['-average', '-count', 'display_name']

    def update_rating(self):
        """
        Recalculate the totals, and save.
        """
        aggregates = self.user_ratings.aggregate(average=Avg('score'), count=Count('score'))
        self.count = aggregates.get('count')
        self.average = aggregates.get('average')
        self.save()

    def __str__(self):
        return self.display_name


# UserRating Model
class UserRating(TimeStampedModel):
    """
    An individual rating of a user against a model.
    """
    user_email_address = models.EmailField()
    user_github_account_link = models.URLField(null=True, blank=True)
    comment = models.TextField()
    score = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    stemmer = models.ForeignKey(Stemmer, related_name='user_ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f"by {self.user_email_address} at {self.created}"
