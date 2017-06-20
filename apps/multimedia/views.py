from django.shortcuts import render
from .models import Articuloxmultimedia

class ArticleMultimedia() :

    idPost = None

    def getAllImages():

        images        = []

        if( not self.idPost is None ):
            imagesPost = Articuloxmultimedia.objects.filter(articulo = idPost)

            for image in imagePost:

                info = { 'title': image.multimedia.titulo,
                         'href': image.multimedia.url,
                         'desc': image.multimedia.descripcion
                        }
                images.append(info)

        return images

    def getThumbnail():

        images        = []

        if( not self.idPost is None ):
            imagePost = Articuloxmultimedia.objects.filter(articulo = idPost)

            for image in imagePost:

                info = { 'title': image.multimedia.titulo,
                         'href': image.multimedia.url,
                         'desc': image.multimedia.descripcion
                        }
                images.append(info)

        return images

    def getImagesByType(self, type):

        images        = []
        imagePost     = None

        if( not self.idPost is None and not type is None ):

            imagePost = Articuloxmultimedia.objects.filter(articulo = self.idPost)

            for image in imagePost:

                info = { 'title': image.multimedia.titulo,'href': image.multimedia.url,'desc': image.multimedia.descripcion }
                images.append(info)
        
        return images
