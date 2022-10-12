from django.urls import path
from .import views

urlpatterns = [
    path('perfil_loja/', views.PerfilLoja.as_view(), name='perfil_loja'),
    path('perfil_loja/editar/', views.EditarPerfilLoja.as_view(), name='editar_perfil_loja'),
    path('perfil_admin/', views.PerfilAdmin.as_view(), name="perfil_admin"),
    path('perfil_admin/editar/', views.EditarPerfilAdmin.as_view(), name='editar_perfil_admin'),
    path('minhas_colecoes/', views.MinhasColecoes.as_view(), name='minhas_colecoes'),
    path('pedidos/', views.PedidosLoja.as_view(), name='pedidos_loja'),
    path('pedidos/pedido', views.Pedido.as_view(), name='pedido'),
    path('minhas_colecoes/roupa/<int:pk>/', views.delete, name="deletar_roupa"),
]
