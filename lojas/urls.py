from django.urls import path
from .import views

urlpatterns = [
    path('perfil_loja/', views.PerfilLoja.as_view(), name='perfil_loja'),
    path('perfil_loja/editar/', views.EditarPerfilLoja.as_view(), name='editar_perfil_loja'),
    path('perfil_admin/', views.PerfilAdmin.as_view(), name="perfil_admin")
]
