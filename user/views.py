from django.shortcuts import render
from django.views import View
from .models import User

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
        emailConfirmar = request.POST.get('senhaConfirmar')



class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        pass

    #eu ia fazer o cadastro de usuários