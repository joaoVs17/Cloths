from multiprocessing import context
from re import S
from django.shortcuts import render, redirect
from django.views import View
from .models import User
from colecoes.models import Colecao
from lojas.models import Loja, Plano
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
import os
from pathlib import Path
from hashlib import sha256

# Exceções
class ErrorEmail(Exception):
    pass
class ErrorPassword(Exception):
    pass
class EmailAlreadyExists(Exception):
    pass
class CpfAlreadyExists(Exception):
    pass
class RgAlreadyExists(Exception):
    pass
class TelefoneAlreadyExistes(Exception):
    pass

#funções e utilitários
def custom_encode_Sha(valor):
    valor = sha256(valor.encode()).hexdigest()
    return valor

#views


class Cadastro(View):
    def get(self, request):
        if request.user.is_authenticated == True: # na hora que o usuário acessar a página de cadastro, se ele
            return redirect ('home')                #estiver logado, ele vai ser redirecionado para home
        elif request.user.is_authenticated == False:
            status = request.GET.get('status')
            context = {
                'status': status,
            }
            return render(request, 'creatAcount.html', context)
    def post(self, request):
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')

        senhaConfirmar = request.POST.get('senhaConfirmar')
        emailConfirmar = request.POST.get('emailConfirmar')

        try:
            db = get_user_model()

            #aqui são verificados os possíveis erros
            if senha != senhaConfirmar:
                raise ErrorPassword
            if email != emailConfirmar:
                raise ErrorEmail
            if len(db.objects.filter(cpf=cpf)) > 0 :
                raise CpfAlreadyExists
            if len(db.objects.filter(rg=rg)) > 0 :
                raise RgAlreadyExists
            if len(db.objects.filter(telefone=telefone)) > 0 :
                raise TelefoneAlreadyExistes
            if len(db.objects.filter(email=email)) >0 :
                raise EmailAlreadyExists
            #se nenhum erro rolou, é criado o usuário

            db.objects.create_user(nome=nome, cpf=cpf, rg=rg, telefone=telefone, email=email, password=senha, cep=cep, estado=estado,
            cidade=cidade, rua=rua, bairro=bairro)
            user = authenticate(request, email=email, password=senha)
            login(request, user)
            return redirect('/?status=0')

            #aqui estão as ações conforme o erro
        except CpfAlreadyExists:
            return redirect('/usuario/cadastro/?status=1')
        except RgAlreadyExists:
            return redirect('/usuario/cadastro/?status=2')
        except TelefoneAlreadyExistes:
            return redirect('/usuario/cadastro/?status=3')
        except ErrorEmail:
            return redirect('/usuario/cadastro/?status=4')    
        except ErrorPassword:
            return redirect('/usuario/cadastro/?status=5')
        except EmailAlreadyExists:
            return redirect('/usuario/cadastro/?status=6')
        except Exception:
            return redirect('/usuario/cadastro/?status=9')#status=3 erro do sistema)
        
        

class Login(View):
    def get(self, request):
        if request.user.is_authenticated == True: # na hora que o usuário acessar a página de login, se ele
            return redirect ('login')                #estiver logado, ele vai ser redirecionado para home
        elif request.user.is_authenticated == False:
            status = request.GET.get('status')
            return render(request, 'login.html', {'status':status})
    def post(self, request):
        redirectURL = request.GET.get('next')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if request.user.is_authenticated == False: #basicamente, isso só deixa o usuário logar se ele estiver deslogado antes
            try:
                user = authenticate(request, email=email, password=senha)
                login(request, user)
                if redirectURL != None:
                    return redirect(redirectURL)
                else:
                    return redirect('home')
            except Exception:
                return redirect('/usuario/login/?status=1')
        elif request.user.is_authenticated == True:
            return redirect('home') #Talvez mudar isso
        


@login_required(login_url='/usuario/login/')
def sair(request):
    logout(request)
    return redirect('home')


class Perfil(LoginRequiredMixin,UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return not self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        return render(request, 'perfil_usuario.html')
    def post(self, request):
        pass

class EditarPerfil(LoginRequiredMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return not self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        return render(request, 'perfil_usuario_editar.html')
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

        return redirect('perfil')


#Atualização da conta da

class AtualizarConta(LoginRequiredMixin, UserPassesTestMixin,View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return not self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self,request):
        plano = request.GET.get('plano')
        if plano:
            if plano!='normal' and plano!='plus' and plano!='pro': 
                return redirect('planos')
            else:
                return render(request, 'tranformAccount.html', {'plano':plano})
        else:
            return redirect('planos')
    def post(self,request):
        plano = request.GET.get('plano')
        nome_loja = request.POST.get('nome_loja')
        cnpj = request.POST.get('cnpj')
        cep_loja = request.POST.get('cep_loja')
        estado_loja = request.POST.get('estado_loja')
        cidade_loja = request.POST.get('cidade_loja')
        rua_loja = request.POST.get('rua_loja')
        bairro_loja = request.POST.get('bairro_loja')

        numero_cartao = custom_encode_Sha(request.POST.get('numero_cartao'))
        nome_cartao = custom_encode_Sha(request.POST.get('nome_cartao'))
        cvv = custom_encode_Sha(request.POST.get('cvv'))

        data_expiracao = request.POST.get('data_expiracao')

        db = get_user_model()
        user = db.objects.get(pk=request.user.pk)

        Loja.objects.create(loja_admin=user,nome_loja=nome_loja, cnpj=cnpj, cep_loja=cep_loja,
        estado_loja=estado_loja, cidade_loja=cidade_loja, rua_loja=rua_loja, bairro_loja=bairro_loja,
        numero_cartao=numero_cartao, nome_cartao=nome_cartao, cvv=cvv, data_expiracao=data_expiracao)
        
        user.is_loja_admin = True
        user.save()

        loja = Loja.objects.get(cnpj=cnpj)

        if plano=='normal':
            loja.plano = Plano.objects.get(nome='Normal')
        elif plano=='plus':
            loja.plano = Plano.objects.get(nome='Plus')
        elif plano=='pro':
            loja.plano = Plano.objects.get(nome='Pro')

        loja.save()    
        
        Colecao.objects.create(loja=loja, nome='Main')

        return redirect('perfil_loja')



class PlanosLojas(LoginRequiredMixin,UserPassesTestMixin, View):
    #inicio filtros
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return not self.request.user.is_loja_admin #nesse caso ele dá permissão se o valor for False
    def handle_no_permission(self):
        return redirect('perfil_loja') #se for True, ele te redireciona para 
    #fim filtros
    def get(self, request):
        return render(request, 'planos_precos_loja.html')
    def post(self, request):
        pass