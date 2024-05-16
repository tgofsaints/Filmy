from django.http import HttpRequest
from django.http import HttpResponse
import datetime
from django.shortcuts import render
import requests

def HomeScreen(request):
    api_key = "e06d43b09426bf8ef8c1b0748ebf262d"
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=pt-BR&page=1"

    response = requests.get(url)
    upcomingMovies = response.json()

    movies = upcomingMovies['results']
    for movie in movies:
        movie['release_date'] = datetime.datetime.strptime(movie['release_date'], "%Y-%m-%d").date()

    context = {
        'data_atual': datetime.datetime.now().date(),
        'dates': upcomingMovies['dates'],
        'movies': movies
    }

    return render(request, 'telainicial.html', context)


