from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import Http404
from .models import Articulo
from .models import Meta

def getArticle(request, slug):

    if( slug is None ):
        raise Http404("Articulo no valido")
    else :

        try:
            article = Articulo.objects.get(slug=slug)

            if article.estado.id_estado != 1 :
                raise Http404("Error 404, Articulo no encontrado")
            else:
                metaArticle = Meta.objects.filter(id_articulo = article.id_articulo)
                print(metaArticle)

                return render(request, "articulo/index.html",{"article":article, 'foo':'bar'})

        except Articulo.DoesNotExist:
            raise Http404("Error 404, Articulo no encontrado")



class index(TemplateView):

    template_name = "articulo/index-perfil.html"
