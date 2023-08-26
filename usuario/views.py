from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as login_django,
    logout as logout_django,
)
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Usuário já existe")

        user = User.objects.create_user(username, email, senha)
        user.save()

        return HttpResponse("Usuário criado com sucesso")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return render(request, "index.html")

        return HttpResponse("Usuário ou senha inválidos")


def logout(request):
    logout_django(request)
    return HttpResponseRedirect("/")


@login_required(login_url="/auth/login/")
def gerar_chaves(request):
    return render(request, "gerar_chaves.html")
