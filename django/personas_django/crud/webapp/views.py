from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):

    mensajes={ 'msj1': 'valor mensaje1', 'msj2': 'valor mensaje2' }
    return render(request,'Bienvenido.html',mensajes)

#def despedirse(request):
 #   return HttpResponse('Adiós mundo desde django')
