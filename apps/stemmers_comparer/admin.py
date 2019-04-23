from django.contrib import admin
from .models import Author, ProgrammingLanguage, Requirement, Feature, Stemmer, UserRating

admin.site.register(Author)
admin.site.register(ProgrammingLanguage)
admin.site.register(Requirement)
admin.site.register(Feature)
admin.site.register(Stemmer)
admin.site.register(UserRating)
