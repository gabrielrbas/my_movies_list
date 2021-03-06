from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Movies
from .forms import MovieForm


def index(request):
    movies = Movies.objects.all()
    return render(request, "home/index.html", {"movies": movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    return render(request, "home/detail.html", {"movie": movie})


def new_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return redirect("index")
    else:
        form = MovieForm()
    return render(request, "home/new_movie.html", {"form": form})


def update(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            # file is saved
            form.save()
            return redirect("index")
    else:
        form = MovieForm()
    return render(request, "home/update.html", {"movie": movie})


def delete(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    if request.method == "DELETE":
        form = Movies.objects.get(id=movie_id)
        form.delete()
        return redirect("index")
    return render(request, "home/delete.html", {"movie": movie})


def secure_delete(request, movie_id):
    form = Movies.objects.get(id=movie_id)
    form.delete()
    return redirect("index")
