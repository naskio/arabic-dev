"""ARABIC_DEV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.stemmers_comparer import views
from rest_framework import routers
from django.conf.urls import include, url


router = routers.DefaultRouter()
router.register(r'admin/requirements', views.RequirementViewSet)
router.register(r'admin/feautures', views.FeatureViewSet)
router.register(r'admin/authors', views.AuthorViewSet)
router.register(r'admin/languages', views.ProgrammingLanguageViewSet)
router.register(r'admin/stemmers', views.StemmerViewSet)
router.register(r'admin/userratings', views.UserRatingViewSet)
router.register(r'admin/ratings', views.RatingViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path('stem-words/<stemmer_name>', views.stem_view, name='stem_words'),
    path('get-stemmer/<stemmer_name>', views.get_stemmer, name='get_stemmer'),
    path('get-stemmers', views.get_stemmers, name='get_stemmers'),
    path('get-stemmers/<programming_language>', views.get_stemmers, name='filter_stemmers'),
    path('rate', views.rate, name='post_rate'),
    path('get-rates/<stemmer_name>', views.rate, name='get_rates'),


]
