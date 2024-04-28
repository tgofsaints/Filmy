from django.http import HttpRequest
from django.shortcuts import render

def Login(request):
    return render(request, 'login.html')