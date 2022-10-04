from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage, default_storage
import os
from pathlib import Path

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
#views

class Cadastro(View):
    def get(self, request):
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
            return redirect ('home')                #estiver logado, ele vai ser redirecionado para home
        elif request.user.is_authenticated == False:
            
            print('batata')
            return render(request, 'login.html')
    def post(self, request):
        redirectURL = request.GET.get('next')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if request.user.is_authenticated == False: #basicamente, isso só deixa o usuário logar se ele estiver deslogado antes
            user = authenticate(request, email=email, password=senha)
            login(request, user)
            if redirectURL != None:
                return redirect(redirectURL)
            else:
                return redirect('home')
        elif request.user.is_authenticated == True:
            return redirect('home') #Talvez mudar isso
        


@login_required(login_url='/usuario/login/')
def sair(request):
    logout(request)
    return redirect('home')


class Perfil(LoginRequiredMixin, View):
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def get(self, request):
        return render(request, 'perfil_usuario.html')
    def post(self, request):
        pass

class EditarPerfil(LoginRequiredMixin, View):
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def get(self, request):
        return render(request, 'perfil_usuario_editar.html')
    def post(self, request):
        db = get_user_model()
        user = db.objects.get(pk=request.user.pk)

        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')

        if request.FILES:
            fs = FileSystemStorage(location='media/fotos_usuarios/', base_url='/fotos_usuarios/')
            upload = request.FILES['foto_usuario']
            nome = upload.name
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


class AtualizarConta(LoginRequiredMixin,View):
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
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
        pass

class PlanosLojas(LoginRequiredMixin, View):
    login_url = '/usuario/login/'
    redirect_field_name = 'next'
    def get(self, request):
        return render(request, 'planos_precos_loja.html')
    def post(self, request):
        pass