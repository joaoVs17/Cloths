from django.urls import path
from .import views

urlpatterns = [
    path('perfil_loja/', views.Loja.as_view(), name='perfil_loja'),
]
