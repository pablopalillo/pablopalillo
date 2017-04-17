from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Articulo

def getArticle(request, article_id):
    idArticle = 12
    print article_id
    return HttpResponse("Hola mama , hola hola", article_id)

class index(TemplateView):

    template_name = "articulo/index-perfil.html"
