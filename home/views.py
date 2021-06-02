from django.shortcuts import render
from .models import Movies


def index(request):
    movies = Movies.objects.all()
    return render(request, 'home/index.html', {
        'movies': movies
    })
