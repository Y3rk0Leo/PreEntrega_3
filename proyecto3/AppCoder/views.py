from django.http import HttpResponse
from django.shortcuts import render

from . import forms
from . import models


# Create your views here.

def views_base(request):
    return render(request, 'AppCoder/padre.html')
    

def views_crear_producto(request):
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            msg="guardado conforme"
            return render(request, "AppCoder/padre.html", {'msg': msg})
    else:
        form = forms.ProductoForm()
    return render(request, "AppCoder/crear_producto.html", {'form' : form})


def views_buscar_producto (request):
    
    if request.method == 'POST':
        datos = models.Producto.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'El registro no existen.'
        return render(request, 'AppCoder/buscar_producto.html',{'productos':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscar_producto.html')

def views_listar_producto(request):
    productos = models.Producto.objects.all()    
    return render(request, 'AppCoder/listar_producto.html', {"productos": productos}) 



def views_listar_catalogo(request):
    catalogos = models.Catalogo.objects.all()    
    return render(request, 'AppCoder/listar_catalogo.html', {"catalogos": catalogos}) 


def views_buscar_catalogo (request):
    
    if request.method == 'POST':
        datos = models.Catalogo.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'El registro no existen.'
        return render(request, 'AppCoder/buscar_catalogo.html',{'catalogos':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscar_catalogo.html')
    
    
def views_crear_catalogo(request):
    if request.method == 'POST':
        form = forms.CatalogoForm(request.POST)
        if form.is_valid():
            form.save()
            msg="guardado conforme"
            return render(request, "AppCoder/crear_catalogo.html", {'msg': msg,'form' : forms.CatalogoForm()})
    else:
        form = forms.CatalogoForm()
        return render(request, "AppCoder/crear_catalogo.html", {'form' : form})
   

def views_crear_accesorio(request):
    if request.method == 'POST':
        form = forms.AccesorioForm(request.POST)
        if form.is_valid():
            form.save()
            msg="guardado conforme"
            return render(request, "AppCoder/crear_accesorio.html", {'msg': msg,'form' : forms.AccesorioForm()})
    else:
        form = forms.AccesorioForm()
        return render(request, "AppCoder/crear_accesorio.html", {'form' : form})
                      
                      
def views_listar_accesorio(request):
    accesorios = models.Accesorio.objects.all()    
    return render(request, 'AppCoder/listar_accesorio.html', {"accesorios": accesorios})


def views_buscar_accesorio (request):
    
    if request.method == 'POST':
        datos = models.Accesorio.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'El registro no existen.'
        return render(request, 'AppCoder/buscar_accesorio.html',{'accesorio':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscar_accesorio.html')
    
    
    