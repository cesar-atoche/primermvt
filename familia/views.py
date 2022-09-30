from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from familia.models import Persona
# Create your views here.
def borrar(request):
    for x in range(80,83):
        aux = Persona.objects.get(id=x)
        aux.delete()
    return HttpResponse("Eliminando")

def inicio(request):
    lista = [
        {"nombre":"cesarin","apellido":"atoche paredes","nacimiento":"1984-09-04","edad":38},
        {"nombre":"dereck","apellido":"atoche ruiz","nacimiento":"2015-06-27","edad":7},
        {"nombre":"alexis","apellido":"atoche ruiz","nacimiento":"2011-09-04","edad":11}]

    for i in range(len(lista)):
        personita = Persona(nombre=lista[i]["nombre"],apellido=lista[i]["apellido"],nacimiento=lista[i]["nacimiento"],edad=lista[i]["edad"])
        personita.save()
    
    persona=Persona.objects.all()
    template=loader.get_template("inicio.html")
    contenido={"personas":persona}
    return HttpResponse(template.render(contenido))
