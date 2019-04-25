from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import FilterLanguagesForm, PostReviewForm
from .models import Stemmer, ProgrammingLanguage, UserRating
from libs.stemmers import service


class HomeView(TemplateView):
    template_name = "home.html"


@method_decorator(csrf_exempt)
def stemmers_view(request):
    if request.method != 'POST' and request.method != 'GET':
        return render(request, 'errors.html', status=404)
    pl = None
    stemmers = None
    languages = ProgrammingLanguage.objects.all()
    if request.method == 'POST':
        filter_form = FilterLanguagesForm(request.POST)
        if filter_form.is_valid():
            pl = filter_form.get_languages()
            if pl and len(pl):
                stemmers = Stemmer.objects.filter(is_enabled=True, programming_languages__in=pl).distinct()
    if not stemmers:
        stemmers = Stemmer.objects.filter(is_enabled=True)
    return render(request, 'stemmers.html', status=200,
                  context={'languages': languages, 'stemmers': stemmers, 'languages_checked': pl})


class StemmerView(View):
    def get(self, request, *args, **kwargs):
        stemmer = get_object_or_404(Stemmer, display_name=kwargs['display_name'], is_enabled=True)
        context = {'stemmer': stemmer}
        return render(request, 'stemmer.html', context)


@method_decorator(csrf_exempt)
def post_review_view(request, display_name):
    if request.method == 'GET':
        stemmer = get_object_or_404(Stemmer, display_name=display_name, is_enabled=True)
        context = {'stemmer': stemmer}
        return render(request, 'post_review.html', context)
    elif request.method == 'POST':
        stemmer = get_object_or_404(Stemmer, display_name=display_name, is_enabled=True)
        form = PostReviewForm(request.POST)
        if form.is_valid():
            UserRating.objects.create(**form.cleaned_data, stemmer=stemmer)
            stemmer.update_rating()
            return render(request, 'thanks.html', {'stemmer': stemmer})
    return render(None, 'errors.html', status=404)


@api_view(['POST'])
def stem_view(request, display_name):
    stemmer = get_object_or_404(Stemmer, display_name=display_name, is_enabled=True)
    string = request.data['value']
    stem = " ".join(service.stem(string, stemmer.name))
    return Response({"original": string, "stemmed": stem})


@api_view(['POST'])
def stems_view(request):
    stemmers = get_list_or_404(Stemmer, is_enabled=True)
    string = request.data['value']
    res = []
    for stemmer in stemmers:
        stem = " ".join(service.stem(string, stemmer.name))
        res.append({'name': stemmer.name, 'stemmed': stem, 'display_name': stemmer.display_name,
                    'rate_it': f'/stemmer/review/{stemmer.display_name}/',
                    'url': f'/stemmer/{stemmer.display_name}/'})  # 'rank': stemmer.rank})
    return Response({"original": string, "stemmers": res})
