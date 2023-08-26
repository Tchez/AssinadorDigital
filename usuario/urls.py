from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/cadastro/", views.cadastro, name="cadastro"),
    path("auth/login/", views.login, name="login"),
    path("auth/logout/", views.logout, name="logout"),
    path("gerar_chaves/", views.gerar_chaves, name="gerar-chaves"),    
]
