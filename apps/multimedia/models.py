from django.db import models

class Multimedia(models.Model):
    id_multimedia = models.IntegerField(primary_key=True)
    tipo = models.ForeignKey('TipoMultimedia', db_column='tipo')
    titulo = models.CharField(max_length=80, blank=True)
    descripcion = models.TextField(blank=True)
    url = models.CharField(max_length=1000, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'multimedia'

class TipoMultimedia(models.Model):
    id_tipo_multimedia = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'tipo_multimedia'


class Articuloxmultimedia(models.Model):
    id_axm = models.IntegerField(primary_key=True)
    articulo = models.ForeignKey(Arcticulo, db_column='articulo', blank=True, null=True)
    multimedia = models.ForeignKey('Multimedia', db_column='multimedia', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'articuloxmultimedia'
