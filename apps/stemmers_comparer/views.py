"""ARABIC_DEV Stemmers name
those names are used to choose which stemmer to execute
    0 --> alkhalilMorphoSys ---> alkhalilMorphoSysStemmer
    1 --> arabicProcessingCog --> arabicProcessingCogStemmer
    2 --> AST1 --> arabic_stemming_toolkit_Algo1
    3 --> AST2 --> arabic_stemming_toolkit_Algo2
    4 --> AST3 --> arabic_stemming_toolkit_Algo3
    5 --> assemsArabic --> assems_arabic_light_stemmer
    6 --> farasa --> farasa_stemmer
    7 --> luceneArabicAnalyzer --> luceneArabicAnalyzerStemmer
    8 --> ntlk --> ntlk_isri_stemmer
    9 --> qutuf --> qutuf_stemmer
    10 --> shereenekhoja --> shereen_kohja_stemmer
    11 --> tashaphyne --> tashaphyne_stemmer
"""
from django.views.generic import View, TemplateView
import json
from django.shortcuts import render
from apps.stemmers_comparer import models
from rest_framework import viewsets
from ARABIC_DEV import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from libs.stemmers.services.alkhalil_morph_sys_stemmer import alkhalilMorphoSysStemmer
from libs.stemmers.services.arabic_processing_cog_stemmer import arabicProcessingCogStemmer
from libs.stemmers.services.arabic_stemming_toolkit.ast_algo1.arabicStemmingToolkitAlgo1 import \
    ArabicStemmingToolkitStemmerAlgo1 as ast_algo1_stemmer
from libs.stemmers.services.arabic_stemming_toolkit.ast_algo2.arabicStemmingToolkitAlgo2 import \
    ArabicStemmingToolkitStemmerAlgo2 as ast_algo2_stemmer
from libs.stemmers.services.arabic_stemming_toolkit.ast_algo3.arabicStemmingToolkitAlgo3 import \
    ArabicStemmingToolkitStemmerAlgo3 as ast_algo3_stemmer
from libs.stemmers.services.farasa_stemmer.farasaStemmer import FarasaStemmer as farasa_stemmer_
from libs.stemmers.services.assems_arabic_light_stemmer import assemsArabicLightStemmer
from libs.stemmers.services.ntlk_stemmer import ntlkIsriStemmer
from libs.stemmers.services.qutuf_stemmer import qutufStemmer
from libs.stemmers.services.shereen_khoja_stemmer.shereenKhojaStemmer import \
    ShereenKhojaStemmer as shereen_khoja_stemmer_
from libs.stemmers.services.tashaphyne_stemmer import tashaphyneStemmer

from libs.stemmers.services.lucene_arabic_analyzer.luceneArabicAnalyzerStemmer import \
    LuceneArabicAnalyzerStemmer as lucene_arabic_analyzer_stemmer_

from django.http import HttpResponse


# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


@api_view(['GET'])
def get_stemmers(request, programming_language=''):
    if programming_language == '':
        stemmers = models.Stemmer.objects.all()

    else:
        stemmers = models.Stemmer.objects.filter(programming_languages__name__iexact=programming_language)
        # substring search
        # stemmers = models.Stemmer.objects.filter(programming_languages__name__icontains=programming_language)

    stemmers_dict = []
    for stemmer in stemmers:

        requirements = stemmer.requirements.all()
        requirements_dict = []
        for requirement in requirements:
            requirement_dict = dict(
                id=requirement.id,
                name=requirement.name
            )
            requirements_dict.append(requirement_dict)

        features = stemmer.features.all()
        features_dict = []
        for feature in features:
            feature_dict = dict(
                id=feature.id,
                name=feature.name
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

        rating = models.Rating.objects.filter(stemmer__name=stemmer.name).first()

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
            features=features_dict,
            rating=rating.to_dict()
        )
        stemmers_dict.append(stemmer_dict)

    #print(stemmers_dict)
    return Response({"stem_words": stemmers_dict})
    #return render(request, 'stemmers.html', {'stemmers': stemmers_dict})


@api_view(['GET'])
def get_stemmer(request, stemmer_name):
    stemmer = models.Stemmer.objects.get(name=stemmer_name)

    requirements = stemmer.requirements.all()
    requirements_dict = []
    for requirement in requirements:
        requirement_dict = dict(
            id=requirement.id,
            name=requirement.name
        )
        requirements_dict.append(requirement_dict)

    features = stemmer.features.all()
    features_dict = []
    for feature in features:
        feature_dict = dict(
            id=feature.id,
            name=feature.name
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

    rating = models.Rating.objects.filter(stemmer__name=stemmer_name).first()

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
        features=features_dict,
        rating=rating.to_dict()
    )

    # print(stemmers_dict)
    # return Response({"stemmer_dict": stemmer_dict})
    return render(request, 'stemmer.html', {'stemmer': stemmer_dict})


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

class UserRatingViewSet(viewsets.ModelViewSet):

    queryset = models.UserRating.objects.all()
    serializer_class = serializers.UserRatingSerializer

class StemmerViewSet(viewsets.ModelViewSet):
    queryset = models.Stemmer.objects.all()
    serializer_class = serializers.StemmerSerializer


class RatingViewSet(viewsets.ModelViewSet):

    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer


def alkhalil_morpho_sys_stemmer(string):
    return alkhalilMorphoSysStemmer.stem(string)


def arabic_processing_cog_stemmer(string):
    return arabicProcessingCogStemmer.stem(string)


def ast1(string):
    return ast_algo1_stemmer.stem(ast_algo1_stemmer, string)


def ast2(string):
    return ast_algo2_stemmer.stem(ast_algo2_stemmer, string)


def ast3(string):
    return ast_algo3_stemmer.stem(ast_algo3_stemmer, string)


def assems_arabic_light_stemmer(string):
    return assemsArabicLightStemmer.stem(string.encode().decode())


def farasa_stemmer(string):
    return farasa_stemmer_.stem(farasa_stemmer_, string.encode().decode())


def lucene_arabic_analyzer_stemmer(string):
    return lucene_arabic_analyzer_stemmer_.stem(lucene_arabic_analyzer_stemmer_, string.encode().decode())


def ntlk_stemmer(string):
    return ntlkIsriStemmer.stem(string.encode().decode())


def qutuf_stemmer(string):
    return qutufStemmer.stem(string)


def shereen_khoja_stemmer(string):
    return shereen_khoja_stemmer_.stem(shereen_khoja_stemmer_, string)


def tashaphyne_stemmer(string):
    return tashaphyneStemmer.stem(string.encode().decode())


def all_stemmers(string):
    alkhalilMorphoSys_dict = alkhalil_morpho_sys_stemmer(string)
    arabicProcessingCog_dict = arabic_processing_cog_stemmer(string)
    AST1_dict = ast1(string)
    AST2_dict = ast2(string)
    AST3_dict = ast3(string)
    assemsArabic_dict = assems_arabic_light_stemmer(string)
    farasa_dict = farasa_stemmer(string)
    luceneArabicAnalyzer_dict = lucene_arabic_analyzer_stemmer(string)
    ntlk_dict = ntlk_stemmer(string)
    qutuf_dict = qutuf_stemmer(string)
    shereenekhoja_dict = shereen_khoja_stemmer(string)
    tashaphyne_dict = tashaphyne_stemmer(string)

    stem_result = [{
        "alkhalilMorphoSys": alkhalilMorphoSys_dict,
        "arabicProcessingCog": arabicProcessingCog_dict,
        "AST1": AST1_dict,
        "AST2": AST2_dict,
        "AST3": AST3_dict,
        "assemsArabic": assemsArabic_dict,
        "farasa": farasa_dict,
        "luceneArabicAnalyzer": luceneArabicAnalyzer_dict,
        "ntlk": ntlk_dict,
        "qutuf": qutuf_dict,
        "shereenekhoja": shereenekhoja_dict,
        "tashaphyne": tashaphyne_dict
    }]
    return stem_result


def pass_string(string):
    return string


def switch(case):
    return {
        "alkhalilMorphoSys": alkhalil_morpho_sys_stemmer,
        "arabicProcessingCog": arabic_processing_cog_stemmer,
        "AST1": ast1,
        "AST2": ast2,
        "AST3": ast3,
        "assemsArabic": assems_arabic_light_stemmer,
        "farasa": farasa_stemmer,
        "luceneArabicAnalyzer": lucene_arabic_analyzer_stemmer,
        "ntlk": ntlk_stemmer,
        "qutuf": qutuf_stemmer,
        "shereenekhoja": shereen_khoja_stemmer,
        "tashaphyne": tashaphyne_stemmer,
        "all": all_stemmers
    }.get(case, pass_string)


@api_view(['GET', 'POST'])
def stem_view(request, stemmer_name):
    string_dict = request.data.dict()
    stem_words = switch(stemmer_name)(string_dict["string"])
    return Response({"stem_words": stem_words})
    # return render(request, 'template.html', {'stem_words': stem_words})


@api_view(['GET', 'POST'])
def rate(request, stemmer_name=None):

    if request.method == 'POST':
        string_dict = request.data.dict()

        stemmer = models.Stemmer.objects.get(name=string_dict['stemmer_name'])

        rating = models.Rating.objects.rate(
                            instance=stemmer,
                            score=int(string_dict['score']),
                            user_email_address=string_dict['user_email_address'],
                            user_github_account_link=string_dict['user_github_account_link'],
                            comment=string_dict['comment'])

        rating.calculate()
        rating_dict = rating.to_dict()
        return Response({"rating": rating_dict})

    else:#request.method == 'GET'

        ratings = models.Rating.objects.filter(stemmer__name=stemmer_name)
        for rating in ratings:
            users_ratings = models.UserRating.objects.filter(rating=rating.pk)
        users_ratings_dict = []

        for user_ratings in users_ratings:
            user_ratings_dict = dict(
                user_email_address=user_ratings.user_email_address,
                user_github_account_link=user_ratings.user_github_account_link,
                comment=user_ratings.comment,
                score=int(user_ratings.score),
                created=user_ratings.created,
                modified=user_ratings.modified
            )
            users_ratings_dict.append(user_ratings_dict)

        return Response({"users_ratings": users_ratings_dict})
