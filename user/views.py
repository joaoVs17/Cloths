from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class Cadastro(View):
    def get(self, request):
        return render(request, 'creatAcount.html')
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

        if senha and senhaConfirmar and email and emailConfirmar and senha==senhaConfirmar and email==emailConfirmar:
            try:
                db = get_user_model()
                db.objects.create_user(nome=nome, cpf=cpf, rg=rg, telefone=telefone, email=email, password=senha, cep=cep, estado=estado,
                cidade=cidade, rua=rua, bairro=bairro)
                user = authenticate(cpf=cpf, email=email, telefone=telefone)
                login(request, user)
                return redirect('/?status=0')
            except Exception:
                return redirect('/?status=1')#status=1 é um erro do sistema
        else:
            return redirect('/usuario/cadastro/?status=2') #status=2 é a não correspondência do email e/ou da senha


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if request.user.is_authenticated == False: #basicamente, isso só deixa o usuário logar se ele estiver deslogado antes
            user = authenticate(request, email=email, password=senha)
            print(user)
            print('batata')
            login(request, user)
            return redirect('home')
        elif request.user.is_authenticated == True:
            return redirect('home') #Talvez mudar isso
        


@login_required(login_url='/usuario/login/')
def sair(request):
    logout(request)
    return redirect('home')