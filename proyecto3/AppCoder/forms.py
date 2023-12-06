from django import forms

from . import models

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = models.Catalogo
        fields = "__all__"
        
class AccesorioForm(forms.ModelForm):
    class Meta:
        model = models.Accesorio
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"