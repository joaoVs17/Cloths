from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('roupas/', include('roupas.urls')),
]
