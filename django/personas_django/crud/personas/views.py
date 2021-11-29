from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona


def detallePersonas(request, id):
    #persona=Persona.objects.get(pk=id)
    persona= get_object_or_404(Persona, pk=id)
    return render (request,'personas/detalle.html' , {'persona': persona})
