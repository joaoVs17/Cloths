import email
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model, authenticate, login, logout
from lojas.models import Loja
from .models import Roupa
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
#Funções e utilitários
#
# Create your views here.

class RoupaVer(View):
    def get(self, request, pk):
        roupa = Roupa.objects.get(pk=pk)
        context = {
            'roupa': roupa,
        }
        if request.user.is_authenticated:
            loja = Loja.objects.get(loja_admin=request.user)
            context['loja'] = loja
        return render(request, 'ropa.html', context)
    def post(self, request):
        pass