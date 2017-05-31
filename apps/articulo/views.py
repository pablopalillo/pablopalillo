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
                metaArticle = getMetaData(article.id_articulo)

                return render(request, "articulo/index.html",
                    {"article":article, 'meta':metaArticle}
                )

        except Articulo.DoesNotExist:
            raise Http404("Error 404, Articulo no encontrado")


def getMetaData(idPost):

    metaHtml = ''

    if( not idPost is None ):
        metaArticle = Meta.objects.filter(id_articulo = idPost)

        for itemMeta in metaArticle:
            metaText = ('<meta name="{name}" content="{content}" />').format(
            name = itemMeta.metatype,
            content = itemMeta.metadata.encode('utf8')
            )
            metaHtml = metaHtml+" "+metaText

    return metaHtml




class index(TemplateView):

    template_name = "articulo/index-perfil.html"
