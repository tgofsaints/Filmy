# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class Login(View):
    """
    Class Based View para autenticação de usuários.
    """
    
    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return HttpResponse('Usuário já está autenticacao!')
            # return redirect("/veiculos")
        else:
            return render(request, 'login.html', contexto)

    def post(self, request):
        # Obtém as credenciais de autenticação do formulário
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # Verifica as credenciais de autenticação fornecidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            # Verifica se o usuário ainda está ativo no sistema
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuário autenticacao com sucesso!')

            return render(request, 'login.html', {'mensagem': 'Usuário inativo.'})

        return render(request, 'login.html', {'mensagem': 'Usuário ou senha inválidos.'})

class Logout(View):
    """
    Class Based View para realizar logout de usuários.
    """
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
