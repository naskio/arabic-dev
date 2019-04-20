from django.db import models
from star_ratings import get_star_ratings_rating_model_name
from django.contrib.contenttypes.fields import GenericRelation


# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    github_account_link  =  models.CharField(max_length=255)
    website = models.CharField(max_length=255)

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

    class Meta:
        ordering = ['name']

    def __str__(self):
       return self.display_name


# Review Model
class Review(models.Model):
    stemmer = models.ForeignKey(Stemmer, on_delete=models.CASCADE)
    ratings = GenericRelation(get_star_ratings_rating_model_name(), related_query_name='stemmers')
    user_email_address = models.EmailField()
    user_github_account_link = models.CharField(max_length=255, null=True)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
