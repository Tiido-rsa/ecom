
from django.contrib import admin
from django.urls import path
from newapp.views import movie_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movie_list, name='movie_list'),
]
