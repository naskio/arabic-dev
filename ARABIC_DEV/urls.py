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
from rest_framework.documentation import include_docs_urls



router = routers.DefaultRouter()

router.register(r'stemmers-api', views.StemmersView)
router.register(r'admin/requirements', views.RequirementViewSet)
router.register(r'admin/feautures', views.FeatureViewSet)
router.register(r'admin/authors', views.AuthorViewSet)
router.register(r'admin/languages', views.ProgrammingLanguageViewSet)
router.register(r'admin/stemmers', views.StemmerViewSet)




# TODO: add Routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ratings/', include('star_ratings.urls')),
    path(r'', include(router.urls)),
    path(r'api/docs', include_docs_urls(title='Sayara DZ API')),
    path('stem_words/<stemmer_name>', views.stem_view, name='stem_words')


]
