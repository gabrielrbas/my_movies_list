from django.shortcuts import render, get_object_or_404
from .models import Movies
from .forms import MovieForm


def index(request):
    movies = Movies.objects.all()
    return render(request, "home/index.html", {"movies": movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    return render(request, "home/detail.html", {"movie": movie})


def new_movie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "home/new_movie.html", {"form": form})
