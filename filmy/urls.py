from django.contrib import admin
from django.urls import path
from filmy.views import HomeScreen
from mostrarinfo.views import MostrarFilmeInfo
from autenticacao.views import Login

urlpatterns = [
    path('login/', Login.as_view(), name="Login"),
    path('filme/', MostrarFilmeInfo, name="MostrarFilmeInfo"),
    path('', HomeScreen, name="HomeScreen"),
    path('admin/', admin.site.urls)
]
