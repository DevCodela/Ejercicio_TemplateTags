#encoding:utf-8
from django.db import models


class Articulo(models.Model):

    """
    Este modelo almacena los artículos pidiendo que cada 
    una tenga un nombre, votos y un estado para saber 
    si está publicado o no.
    """
    nombre = models.CharField(max_length=140)
    votos = models.PositiveSmallIntegerField(default=0)
    usuario = models.CharField(max_length=50)
    publicado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre
