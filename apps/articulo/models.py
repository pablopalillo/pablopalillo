from django.db import models

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    contenido = models.TextField(blank=True)
    slug = models.CharField(max_length=300, blank=True)
    tipo = models.ForeignKey('TipoArticulo', db_column='tipo')
    estado = models.ForeignKey('EstadoArticulo', db_column='estado')

    def __unicode__(self):
        return self.nombre

    """
     Sobreescribir el delete, por que en mi caso es un borrado logico.
    """
    def delete (self, *args, **kwargs):

        Articulo.objects.filter(id_articulo = self.id_articulo).update(estado = "3")

        """newArticulo = Articulo.objects.get(pk = self.id_articulo)
        newArticulo.estado.id_estado = "3"
        newArticulo.save(*args, **kwargs) """

    class Meta:
        db_table = 'articulo'



class EstadoArticulo(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=40)

    def __unicode__(self):
        return self.estado

    class Meta:
        managed = False
        db_table = 'estado_articulo'

class Meta(models.Model):
    id_meta = models.IntegerField(primary_key=True)
    id_articulo = models.ForeignKey(Articulo, db_column='id_articulo')
    metatype = models.CharField(max_length=35, blank=True)
    metadata = models.CharField(max_length=300, blank=True)
    class Meta:
        managed = False
        db_table = 'meta'

class TipoArticulo(models.Model):
    id_tipo_articulo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=40)

    def __unicode__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'tipo_articulo'
