from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Catalogo)
admin.site.register(models.Accesorio)
admin.site.register(models.Producto)