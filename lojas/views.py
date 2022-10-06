import email
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Loja
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
#Funções e utilitários
#

class PerfilLoja(LoginRequiredMixin,UserPassesTestMixin,View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin
    def handle_no_permission(self):
        return redirect('home')
    #fim filtros
    def get(self, request):
        loja = Loja.objects.get(loja_admin=request.user)
        context = {
            'loja': loja,
        }
        return render(request, 'perfil_adimin_lojas.html', context)
    def post(self, request):
        pass

class EditarPerfilLoja(LoginRequiredMixin, UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin
    def handle_no_permission(self):
        return redirect('home')
    #fim filtros


    def get(self, request):
        loja = Loja.objects.get(loja_admin=request.user)
        context = {
            'loja': loja, 
        }
        return render(request, 'perfil_adimin_editar_loja.html', context)
    def post(self, request):
        nome_loja = request.POST.get('nome_loja')
        telefone_loja = request.POST.get('telefone_loja')
        email_loja = request.POST.get('email_loja')
        cep_loja = request.POST.get('cep_loja')
        estado_loja = request.POST.get('estado_loja')
        cidade_loja = request.POST.get('cidade_loja')
        rua_loja = request.POST.get('rua_loja')
        bairro_loja = request.POST.get('bairro_loja')

        loja = Loja.objects.get(loja_admin = request.user)
        
        if nome_loja and not nome_loja.isspace():
            loja.nome_loja = nome_loja
        if telefone_loja and not telefone_loja.isspace():
            loja.telefone_loja = telefone_loja
        if email_loja and not email_loja.isspace():
            loja.email_loja = email_loja
        if cep_loja and not cep_loja.isspace():
            loja.cep_loja = cep_loja
        if estado_loja and not estado_loja.isspace():
            loja.estado_loja = estado_loja
        if cidade_loja and not cidade_loja.isspace():
            loja.cidade_loja = cidade_loja
        if rua_loja and not rua_loja.isspace():
            loja.rua_loja = rua_loja
        if bairro_loja and not bairro_loja.isspace():
            loja.bairro_loja = bairro_loja
        
        if request.FILES:
            fs = FileSystemStorage(location='media/logos_lojas/', base_url="/logos_lojas/")
            upload = request.FILES['logo']
            filename = fs.save(upload.name.replace(" ",""), upload)
            url = fs.url(filename)
            if url:
                if loja.logo_loja:
                    currentDirectory=os.getcwd()
                    fs.delete(currentDirectory+loja.logo_loja.url)
                loja.logo_loja = url
        
        loja.save()
        return redirect('perfil_loja')
    
class PerfilAdmin(LoginRequiredMixin, UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin
    def handle_no_permission(self):
        return redirect('home')
    #fim filtros

    def get(self, request):
        loja = Loja.objects.get(loja_admin = request.user)
        context = {
            'loja': loja,
        }
        return render(request, 'perfil_adimin .html', context)    