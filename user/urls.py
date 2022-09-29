from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('login/', views.Login.as_view(), name='login'),
    path('sair/', views.sair, name='sair'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)