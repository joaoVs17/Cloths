from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
            return render(request, 'login.html')
    def post(self, request):
        
        redirectURL = request.GET.get('next')

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if request.user.is_authenticated == False: #basicamente, isso só deixa o usuário logar se ele estiver deslogado antes
            user = authenticate(request, email=email, password=senha)
            login(request, user)
            return redirect(redirectURL)
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
        print(request.user.pk)
        return render(request, 'perfil_usuario.html')
    def post(self, request):
        pass

    #eu queria exibir a foto de perfil do usuário