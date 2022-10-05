from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from .models import Loja
from user.models import User
# Create your views here.
#Funções e utilitários
def check_is_loja(request):
    return request.user.is_loja

#

class Loja(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin
    def handle_no_permission(self):
        return redirect('home')
    
    def get(self, request):
        return render(request, 'perfil_adimin_lojas.html')
    def post(self, request):
        pass