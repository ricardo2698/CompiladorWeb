# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render , get_object_or_404




from .models import Lenguaje


def hello_world(request):
    #return HttpResponse("<h1>HELLO WORLD</h1>")
    lenguaje = Lenguaje.objects.order_by('id')
    template = loader.get_template('index.html')
    title = ' Compiladores'
    context = {
        'lenguaje': lenguaje,
        'title': title
    }
    return HttpResponse(template.render(context,request))

def saludo(request):
    template = loader.get_template('saludo.html')
    big_title = 'Encabezado de la pagina '
    title = 'Aqui no hay lenguajes'
    hola = {
        'big_title' : big_title ,
        'title' : title
            }
    return HttpResponse (template.render(hola,request))

def detalleLenguaje(request,pk):
    lenguaje = get_object_or_404(Lenguaje, pk=pk)
    template = loader.get_template('lenguajeDetail.html')
    context = {
    'lenguaje': lenguaje
        }
    return HttpResponse(template.render(context, request))
