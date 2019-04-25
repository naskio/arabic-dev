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
# from django.conf.urls.static import serve
from django.contrib import admin
from django.urls import path
from apps.stemmers_comparer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='HOME_URL'),
    path('stemmers/', views.stemmers_view, name='STEMMERS_URL'),
    path('stemmer/<display_name>/', views.StemmerView.as_view(), name='STEMMER_URL'),
    path('stemmer/review/<display_name>/', views.post_review_view, name='POST_REVIEW_URL'),
    path('api/stemmer/<display_name>/', views.stem_view, name='STEMMER_API'),
    path('api/stemmers/', views.stems_view, name='STEMMERS_API'),
]
