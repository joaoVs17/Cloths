from django.shortcuts import render
from django.views import View
from user.models import User
from lojas.models import Loja

# Create your views here.
class Home(View):
    def get(self, request):
        context = {
        }
        if request.user.is_authenticated:
            if request.user.is_loja_admin:
                loja = Loja.objects.get(loja_admin=request.user)
                context['loja'] = loja
        return render (request, 'index.html', context)
    def post(self, request):
        pass