
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet, ThrillerViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('action', ActionViewSet, basename='action-movies')
router.register('comedy', ComedyViewSet, basename='comedy-movies')
router.register('thriller', ThrillerViewSet, basename='thriller-movies')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
