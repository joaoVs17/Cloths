from django.contrib import admin
from .models import Roupa, Categoria, TipoTamanho

# Register your models here.
admin.site.register(Roupa)
admin.site.register(Categoria)
admin.site.register(TipoTamanho)