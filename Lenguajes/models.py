# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
 class Lenguaje(models.Model):
     name = models.CharField(max_length=255)
     tipo = models.CharField(max_length=255)
     aplicacion = models.CharField(max_length=255)
     puntaje = mo dels.DecimalField(max_digits=2,decimal_places=2)
