# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Lenguaje(models.Model):
    name = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    aplicacion = models.CharField(max_length=255)
    puntaje = models.IntegerField(default =10 )
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
