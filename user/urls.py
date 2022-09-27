from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('login/', views.Login.as_view(), name='login'),
]
