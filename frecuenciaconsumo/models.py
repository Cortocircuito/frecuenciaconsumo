from __future__ import unicode_literals

from django.db import models

class Unidad(models.Model):
    nombre = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre.encode('utf-8').strip()
        
class Racion(models.Model):
    nombre = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    peso = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre.encode('utf-8').strip()
    
