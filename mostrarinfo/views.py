from django.shortcuts import render
from django.http import request

# Create your views here.

def MostrarFilmeInfo():
       return render(request, 'mostrarinfo.html')