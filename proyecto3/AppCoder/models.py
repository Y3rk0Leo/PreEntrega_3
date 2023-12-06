from django.db import models

# Create your models here.
class Catalogo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Accesorio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=120)
    catalogo_origen = models.ForeignKey(Catalogo, on_delete=models.SET_NULL, null=True, blank=True)
    accesorio_origen = models.ForeignKey(Accesorio, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    