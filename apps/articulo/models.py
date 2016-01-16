from django.db import models

class Arcticulo(models.Model):
    id_articulo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    contenido = models.TextField(blank=True)
    slug = models.CharField(max_length=300, blank=True)
    tipo = models.ForeignKey('TipoArticulo', db_column='tipo')
    estado = models.ForeignKey('EstadoArticulo', db_column='estado')
    class Meta:
        managed = False
        db_table = 'arcticulo'

class EstadoArticulo(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'estado_articulo'

class Meta(models.Model):
    id_meta = models.IntegerField(primary_key=True)
    id_articulo = models.ForeignKey(Arcticulo, db_column='id_articulo')
    metatype = models.CharField(max_length=35, blank=True)
    metadata = models.CharField(max_length=300, blank=True)
    class Meta:
        managed = False
        db_table = 'meta'

class TipoArticulo(models.Model):
    id_tipo_articulo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'tipo_articulo'
