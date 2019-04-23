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
from django.urls import path  # include
from apps.stemmers_comparer import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.conf.urls import include, url

# from ARABIC_DEV.settings import STATIC_ROOT, DEBUG

router = routers.DefaultRouter()
router.register(r'admin/requirements', views.RequirementViewSet)
router.register(r'admin/feautures', views.FeatureViewSet)
router.register(r'admin/authors', views.AuthorViewSet)
router.register(r'admin/languages', views.ProgrammingLanguageViewSet)
router.register(r'admin/stemmers', views.StemmerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/docs', include_docs_urls(title='ARABIC.DEV API')),
    # path(r'', include(router.urls)),
    path('', views.HomeView.as_view(), name='HOME_URL'),
    path('stemmers/', views.get_stemmers, name='STEMMERS_URL'),
    # path('^static/<str:path>', serve, {'document_root': STATIC_ROOT}),
    # path('stem-words/<stemmer_name>', views.stem_view, name='stem_words'),
    # path('get-stemmer/<stemmer_name>', views.get_stemmer, name='get_stemmer'),
    # path('get-stemmers/<programming_language>', views.get_stemmers, name='filter_stemmers'),
    # path('rate/', views.rate, name='post_rate'),
]
