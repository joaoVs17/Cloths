from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('login/', views.Login.as_view(), name='login'),
    path('sair/', views.sair, name='sair'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),
    path('perfil/editar/', views.EditarPerfil.as_view(), name='editar_perfil'),
    path('planos/atualizar_para_conta_comercial/', views.AtualizarConta.as_view(), name='atualizar'),
    path('planos/', views.PlanosLojas.as_view(), name='planos')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)