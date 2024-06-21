from django.http import HttpRequest
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.conf import settings
import requests

def MostrarFilmeInfo(request):
    FilmeID = request.GET["id"]
    url = f"{settings.API_SHOW_MOVIE_INFO_URL}"
    ondeInserirOID = url.find("/movie/") + len("/movie/")
    enderecoParaBuscarFilme = url[:ondeInserirOID] + FilmeID + url[ondeInserirOID:]
    filme = requests.get(enderecoParaBuscarFilme).json()

    context = {
        'FilmeID': FilmeID,
        'filme': filme,
    }

    return render(request, 'showinfo.html', context)