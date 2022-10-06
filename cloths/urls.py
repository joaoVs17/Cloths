from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from cloths.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('usuario/', include('user.urls')),
    path('loja/', include('lojas.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
