import email
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model, authenticate, login, logout

from colecoes.models import Colecao
from roupas.models import Categoria, Roupa, TipoTamanho
from .models import Loja
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
#Funções e utilitários
def GetFileURL(caminho, uploadFoto, request):
    if request.FILES:
            fs = FileSystemStorage(location='media/'+caminho+'/', base_url='/'+caminho+'/')
            upload = request.FILES[uploadFoto]
            filename = fs.save(upload.name.replace(" ",""), upload)
            url = fs.url(filename)
            return url
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

class EditarPerfilAdmin(LoginRequiredMixin, UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin 
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        loja = Loja.objects.get(loja_admin = request.user)
        return render(request, 'perfil_adimin_editar.html', {'loja':loja})
    def post(self, request):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')

        db = get_user_model()
        user = db.objects.get(pk=request.user.pk)

        if request.FILES:
            fs = FileSystemStorage(location='media/fotos_usuarios/', base_url='/fotos_usuarios/')
            upload = request.FILES['foto_usuario']
            filename = fs.save(upload.name.replace(" ",""), upload)
            url = fs.url(filename)
            if url:
                if user.foto_usuario: 
                    currentDirectory=os.getcwd()
                    fs.delete(currentDirectory+user.foto_usuario.url)
                user.foto_usuario = url
        
        if nome and not nome.isspace():
            user.nome = nome
        if telefone and not telefone.isspace():
            user.telefone = telefone
        if cep and not cep.isspace():
            user.cep = cep
        if estado and not estado.isspace():
            user.estado = estado
        if cidade and not cidade.isspace():
            user.cidade = cidade
        if rua and not rua.isspace():
            user.rua = rua
        if bairro and not bairro.isspace():
            user.bairro = bairro

        user.save()

        return redirect('perfil_admin')

class MinhasColecoes(LoginRequiredMixin,UserPassesTestMixin,View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        context = {}
        loja = Loja.objects.get(loja_admin = request.user)
        colecao = Colecao.objects.get(loja=loja)
        roupas = Roupa.objects.filter(colecao=colecao)

        context['loja'] = loja
        context['colecao'] = colecao
        context['roupas'] = roupas
        
        return render(request, 'minhas_colecoes.html', context)
    def post(self, request):
        loja = Loja.objects.get(loja_admin=request.user)
        colecao = Colecao.objects.get(loja = loja)
        tipo_tamanho = TipoTamanho.objects.all()

        categoria_nome = request.POST.get('categoria')
        categoria = Categoria.objects.get(nome_categoria=categoria_nome)

        nome_roupa = request.POST.get('nome_roupa')
        preco_roupa = request.POST.get('preco_roupa')

        t1 = request.POST.get('t1')
        t2 = request.POST.get('t2')
        t3 = request.POST.get('t3')
        t4 = request.POST.get('t4')
        t5 = request.POST.get('t5')
        t6 = request.POST.get('t6')

        url = GetFileURL(caminho='fotos_roupas', uploadFoto='foto_roupa', request=request)   

        roupa = Roupa(colecao=colecao, categoria=categoria, nome_roupa=nome_roupa, preco=preco_roupa)
        roupa.foto=url
        roupa.save()
        if categoria.tipo_tamanho == tipo_tamanho[0]:
            roupa.pp=t1
            roupa.p=t2
            roupa.m=t3
            roupa.g=t4
            roupa.gg=t5
            roupa.xg=t6
        elif categoria.tipo_tamanho == tipo_tamanho[1]:
            roupa.t1=t1
            roupa.t2=t2
            roupa.t3=t3
            roupa.t4=t4
            roupa.t5=t5
            roupa.t6=t6

        
        
            

        return redirect('minhas_colecoes')

class PedidosLoja(LoginRequiredMixin, UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        loja  = Loja.objects.get(loja_admin = request.user)
        return render(request, 'pedidos.html', {'loja': loja})
    def post(self, request):
        pass

class Pedido(LoginRequiredMixin, UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        loja = Loja.objects.get(loja_admin = request.user)
        return render(request, 'pedido.html', {'loja':loja})
    def post(self, request):
        pass