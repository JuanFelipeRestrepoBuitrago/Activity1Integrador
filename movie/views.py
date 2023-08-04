from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.
def home(request):
    # return render(request, "home.html", {
    #     "name": "Juan Felipe Restrepo"
    # })
    search_term = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    if search_term:
        movies = movies.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    return render(request, "home.html", {
        "search_term": search_term,
        "movies": movies
    })

def about(request):
    return render(request, "about.html")
