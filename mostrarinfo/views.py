from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from mostrarinfo.models import ToWatchList
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from datetime import datetime

def show_movie_info(request, movie_id):
    if 'Add' in request.GET:
        return add_to_watchlist(request, movie_id)
    
    url = f"{settings.API_SHOW_MOVIE_INFO_URL}"
    ondeInserirOID = url.find("/movie/") + len("/movie/")
    enderecoParaBuscarFilme = url[:ondeInserirOID] + str(movie_id) + url[ondeInserirOID:]
    filme = requests.get(enderecoParaBuscarFilme).json()
    
    # Convert release date to desired format
    release_date = filme['release_date']
    release_date_obj = datetime.strptime(release_date, '%Y-%m-%d')
    filme['release_date'] = release_date_obj.strftime('%B %-d, %Y')
    
    context = {
        'filme': filme
    }
    return render(request, 'showinfo.html', context)


def add_to_watchlist(request, filme_id):
    if request.user.is_authenticated:
        if not ToWatchList.objects.filter(user=request.user, movie_id=filme_id).exists():
            ToWatchList.objects.create(user=request.user, movie_id=filme_id)
        return redirect(reverse('show_movie_info', args=[filme_id]))
    else:
        return redirect('Login')
