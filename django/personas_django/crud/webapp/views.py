from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    return render(request,'Bienvenido.html')

def despedirse(request):
    return HttpResponse('Adiós mundo desde django')
