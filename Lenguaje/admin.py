# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Lenguaje

#admin.site.register(Lenguaje)

@admin.register(Lenguaje)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name','tipo','aplicacion',)
    list_filter = ('name','id')
# Register your models here.
