from django.shortcuts import render
from apps.stemmers_comparer import models
from rest_framework.views import APIView
from rest_framework import serializers, viewsets
from ARABIC_DEV import  serializers
# Create your views here.


# TODO: add API for all stemmers
class StemmersView(viewsets.ModelViewSet):

    queryset = models.Stemmer.objects.all()

    def list(self, request, *kwargs):

        stemmers = models.Stemmer.objects.all()

        stemmers_dict =[]
        for stemmer in stemmers:

            requirements = stemmer.requirements.all()
            requirements_dict = []
            for requirement in requirements:
                requirement_dict = dict(
                    id=requirement.id,
                    content=requirement.content
                )
                requirements_dict.append(requirement_dict)

            features = stemmer.features.all()
            features_dict = []
            for feature in features:
                feature_dict = dict(
                    id=feature.id,
                    content=feature.content
                )
                features_dict.append(feature_dict)

            authors = stemmer.authors.all()
            authors_dict = []
            for author in authors:
                author_dict = dict(
                    id=author.id,
                    first_name=author.first_name,
                    last_name=author.last_name,
                    github_account_link=author.github_account_link,
                    website=author.website
                )
                authors_dict.append(author_dict)

            programming_languages = stemmer.programming_languages.all()
            programming_languages_dict = []
            for programming_language in programming_languages:
                programming_language_dict = dict(
                    name=programming_language.name,
                    website=programming_language.website
                )
                programming_languages_dict.append(programming_language_dict)
            stemmer_dict = dict(
                name=stemmer.name,
                display_name=stemmer.display_name,
                is_enabled=stemmer.is_enabled,
                license=stemmer.license,
                description=stemmer.description,
                documentation_link=stemmer.documentation_link,
                download_link=stemmer.download_link,
                how_to_use=stemmer.how_to_use,
                authors=authors_dict,
                programming_languages=programming_languages_dict,
                requirements=requirements_dict,
                features=features_dict
            )
            stemmers_dict.append(stemmer_dict)
        #print(stemmers_dict)
        return render(request, 'template.html', {'stemmers': stemmers_dict})
    


class RequirementViewSet(viewsets.ModelViewSet):

    queryset = models.Requirement.objects.all()
    serializer_class = serializers.RequirementSerializer


class FeatureViewSet(viewsets.ModelViewSet):

    queryset = models.Feature.objects.all()
    serializer_class = serializers.FeaturesSerializer


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):

    queryset = models.ProgrammingLanguage.objects.all()
    serializer_class = serializers.ProgrammingLanguageSerializer


class StemmerViewSet(viewsets.ModelViewSet):

    queryset = models.Stemmer.objects.all()
    serializer_class = serializers.StemmerSerializer



# TODO: add API for specific stemmer

# TODO: add view for home.html page
# TODO: add view for stemmer.html page
