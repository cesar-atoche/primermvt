from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from familia.models import Persona
# Create your views here.
# def borrar(request):
#     for x in range(80,83):
#         aux = Persona.objects.get(id=x)
#         aux.delete()
#     return HttpResponse("Eliminando")

def inicio(request):
    lista = [
        {"nombre":"carlos","apellido":"balladares paredes","nacimiento":"1984-10-04","edad":38},
        {"nombre":"juan","apellido":"perez ruiz","nacimiento":"2015-07-27","edad":7},
        {"nombre":"jose","apellido":"vasco ruiz","nacimiento":"2011-08-04","edad":11}]

    for i in range(len(lista)):
        personita = Persona(nombre=lista[i]["nombre"],apellido=lista[i]["apellido"],nacimiento=lista[i]["nacimiento"],edad=lista[i]["edad"])
        personita.save()
    
    persona=Persona.objects.all()
    template=loader.get_template("inicio.html")
    contenido={"personas":persona}
    return HttpResponse(template.render(contenido))
