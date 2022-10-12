from django.shortcuts import render, redirect
from django.views import View
from colecoes.models import Colecao
from user.models import User
from lojas.models import Loja
from roupas.models import Roupa

# Create your views here.
class Home(View):
    def get(self, request):
        context = {
        }
        if request.user.is_authenticated:
            if request.user.is_loja_admin:
                loja = Loja.objects.get(loja_admin=request.user)
                context['loja'] = loja
        lojas = Loja.objects.all()
        roupas = Roupa.objects.all()
        context['lojas'] = lojas
        context['roupas'] = roupas
        return render (request, 'index.html', context)
    def post(self, request):
        pass

class LojasCadastradas(View):
    def get(self, request):
        context = {
        }
        if request.user.is_authenticated:
            if request.user.is_loja_admin:
                loja = Loja.objects.get(loja_admin=request.user)
                context['loja'] = loja
        todas_lojas = Loja.objects.all().values_list('estado_loja', 'cidade_loja').distinct()
        print(todas_lojas)
        context['todas_lojas'] = todas_lojas
        return render(request, 'lojasCadastradas.html', context)
    def post(self, request):
        pass

class Pesquisa(View):
    def get(self, request):
        query = request.GET.get('query')
        context = {            
        }
        if query != None:
            resultados_roupas = Roupa.objects.filter(nome_roupa__icontains=query)
            context['resultados_roupas'] = resultados_roupas
            resultados_lojas = Loja.objects.filter(nome_loja__icontains=query)
            context['resultados_lojas'] = resultados_lojas
            context['query']=query
        elif query==None:
            resultados_roupas = Roupa.objects.all().order_by('nome_roupa')
            context['resultados_roupas'] = resultados_roupas
            resultados_lojas = Loja.objects.all().order_by('nome_loja')
            context['resultados_lojas'] = resultados_lojas
        if request.user.is_authenticated:
            if request.user.is_loja_admin:
                loja = Loja.objects.get(loja_admin=request.user)
                context['loja'] = loja
        return render(request, 'pesquisa.html', context)
    def post(self, request):
        pass

class LojaVer(View):
    def get(self, request, pk):
        lojaver = Loja.objects.get(pk=pk)
        context = {
            'lojaver':lojaver,
        }
        if request.user.is_authenticated:
            if request.user.is_loja_admin:
                loja = Loja.objects.get(loja_admin=request.user)
                context['loja'] = loja
        colecao = Colecao.objects.get(loja = lojaver)
        roupas = Roupa.objects.filter(colecao=colecao)
        context['roupas'] = roupas
        soma = 0
        for roupa in roupas:
            soma += roupa.pp+roupa.p+roupa.m+roupa.g+roupa.gg+roupa.xg+roupa.t1+roupa.t2+roupa.t3+roupa.t4+roupa.t5+roupa.t6
        context['soma'] = soma
        return render(request, 'lojasC_loja.html', context)
    def post(self, request):
        pass

def pesquisaFiltro(request, query):
    return redirect('/pesquisa/?query='+query)