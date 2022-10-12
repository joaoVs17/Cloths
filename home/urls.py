from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('roupas/', include('roupas.urls')),
    path('lojasCadastradas/', views.LojasCadastradas.as_view(), name='lojas_cadastradas'),
    path('pesquisa/', views.Pesquisa.as_view(), name='pesquisa'),
    path('lojasCadastradas/<int:pk>/', views.LojaVer.as_view(), name='lojaver'),
    path('pesquisa/<str:query>/', views.pesquisaFiltro, name='filtro')
]
