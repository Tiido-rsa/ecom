from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

def movie_list(request):
    movies = Movies.objects.all()

    # SEARCH
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains=movie_name)

    # PAGINATION
    paginator   = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    context = {
        'movies': movies,
        'page_obj': page_obj
    }

    return render(request, 'newapp/movie_list.html', context)

