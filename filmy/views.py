from django.http import HttpRequest
from django.http import HttpResponse

from django.shortcuts import render
import requests

def HomeScreen(request):
    api_key = "e06d43b09426bf8ef8c1b0748ebf262d"
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=pt-BR&page=1"
    
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer e06d43b09426bf8ef8c1b0748ebf262d"
}

    response = requests.get(url)
    upcomingMovies = response.json()
    
    context = {
        'dates': upcomingMovies['dates'],
        'movies': upcomingMovies['results']
    }

    return render(request, 'telainicial.html', context)
    



