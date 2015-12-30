from django.db import models


class Producto(models.Model):
    nombre      = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=300)
    precio      = models.PositiveSmallIntegerField()
    imagen      = models.FileField(upload_to="image/productos", max_length=100)

    def __unicode__(self):
        return self.nombre
