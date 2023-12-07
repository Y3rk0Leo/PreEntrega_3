## Configuración inicial del proyecto
Crear carpeta para nuestro repositorio, "proyecto3"
1.	Se crea archivo README.md
2.	Mediante una terminal, se instala `django`:  pip install django
3.	Crear proyecto:  django-admin startproject proyecto3  (Este comando creará varios archivos dentro una nueva carpeta que se crea “proyecto3”, lo cual dará inicio a nuestro proyecto)
4.	Crear aplicación, python manage.py startapp AppCoder (Con este comando creamos nuestra aplicación “AppCoder”.
5.	Registrar la aplicación, dentro del archivo settings.py que se encuentra en “proyecto3”, se agrega al final la aplicación “AppCoder” 

```python
 

INSTALLED_APPS = [
'AppCoder',  #aca se agrega
]

```

## Rutas
	
6.	Crear rutas principales, dentro de proyecto3/urls.py:
```python
 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),	(Ruta principal creada).
]
```

Copiar archivo proyecto3/urls.py en AppCoder
Se crea ruta “” vacía, dentro de AppCoder/urls.py: 


```python


from django.urls import path
from . import views

urlpatterns = [
    path("", views.views_base, name=’index’),
    
]

```

Creamos las rutas:
```python

from django.urls import path

urlpatterns = [    
    path('', views.views_base, name='index'),
    path('buscar_producto/', views.views_buscar_producto, name='buscar_producto'),
    path('buscar_catalogo/', views.views_buscar_catalogo, name='buscar_catalogo'),
    path('buscar_accesorio/', views.views_buscar_accesorio, name='buscar_accesorio'),
    path('crear_producto/', views.views_crear_producto, name='crear_producto'),
    path('crear_catalogo/', views.views_crear_catalogo, name='crear_catalogo'),
    path('crear_accesorio/', views.views_crear_accesorio, name='crear_accesorio'),
    path('listar_producto/', views.views_listar_producto, name='listar_producto'),
    path('listar_catalogo/', views.views_listar_catalogo, name='listar_catalogo'),
    path('listar_accesorio/', views.views_listar_accesorio, name='listar_accesorio'),
   
]

```

8. Creando los templates y herencia
Se crea una carpeta llamada “templates” dentro de la carpeta “AppCoder”, ahora se crea dentro de “templates” otra carpeta con el nombre “AppCoder” y dentro de esta el archivo “padre.html”.
Se crea ruta “” vacía dentro de urls.py AppCoder 
```python
path('', views.views_base, name='index'),

```
```python

def padre_view(request):
    return render(request, 'AppCoder/padre.html')
```

```python
Agregamos por ejemplo en la ruta `producto_***.html`
    ```html
    {% extends "AppCoder/padre.html" %}
    ```
 Agregamos en `padre.html`
    ```html
    {% block contenido %}
    {% endblock %}
    ```
    y en `producto.html`

    ```html
    {% block contenido %}
 
    {% endblock %}
```
Renderizar: 

```python
def producto_view(request):
   # return HttpResponse("producto")
    return render(request, "AppCoder/padre.html")
```

Crear carpeta `static` en nuestra app: `AppCoder/static/AppCoder`
Le agregamos 1 línea y modificamos otra:
{% load static %}
<!-- Core theme CSS (includes Bootstrap)-->
<link href="{% static 'AppCoder/css/styles.css'  %}" rel="stylesheet" />


8. Creamos los modelos:
```python


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
```

Registramos los modelos en archive /admin.py  
```python

from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Catalogo)
admin.site.register(models.Accesorio)
admin.site.register(models.Producto)
```

9. Crear tablas en bd:
python manage.py makemigrations
python manage.py migrate

Se crea admin y password 123, para administración de nuestro sitio
python manage.py createsuperuser

Creamos archive forms.py en AppCoder
```python

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
   
```


En las páginas .html por ejemplo,  se agrega el siguiente código por ejemplo: (se debe crear con antelación la carpeta templates  (/AppCoder/Templates/AppCoder/xxx.html
```python
{% extends "AppCoder/padre.html" %}

{% block title %}
<h2>Crear Productos</h2>
{% endblock %}

{% block context %}
<div class="containser">
 
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="mb-5 btn btn-success">guardar</button>
</form>
</div>
 
{% endblock %}
```

En listar*** html por ejemplo
```python
{% extends 'AppCoder/padre.html' %}

{% block contenido %}
<div class="row">  
    <div class="col-8 mx-auto mt-5 mb-5">      
      {% if productos.count > 0 %}
        <table class="table">
            <tr>
                <th scope="col">id</th>
                <th scope="col">Nombre</th>
                <th scope="col">Tipo</th>
                <th scope="col">Catalogo</th>
                <th scope="col">Accesorio</th>
                
              </tr>
            </thead>
            <tbody>
                {% for pro in productos  %}
              <tr>
                
                <td>{{pro.id}}</td>
                <td>{{pro.nombre}}</td>
                <td>{{pro.tipo}}</td>
                <td>{{pro.catalogo_origen}}</td>
                <td>{{pro.accesorio_origen}}</td>
                
              </tr>
              {% endfor %}
            
            </tbody>
          </table>      
      {% endif %} 
    </div>
  </div>
  
  {% endblock %}
```
En buscar*** html por ejemplo
```python
{% extends 'AppCoder/padre.html' %}

{% block contenido %}
<div class="row">  
    <div class="col-8 mx-auto mt-5 mb-5">
      <div class="card">
        
        <div class="card-body mx-auto">  
          <form class="row g-3" method="POST" action="../buscar_producto/" > 
            {% csrf_token %}
            <div class="col-auto mt-4" >Buscar:</div>        
            <div class="col-auto" >
                       
              <input type="text" class="form-control" name="nombre" id="nombre" placeholder="">
            </div>
            <div class="col-auto">
              <button type="submit" class="btn btn-primary mb-3">Aceptar</button>
            </div>
          </form>  
        </div>
      </div>
      {% if productos.count > 0 %}
        <table class="table">
            <thead>
              <tr>
                <th scope="col">id</th>
                <th scope="col">Nombre</th>
                <th scope="col">Tipo</th>
                <th scope="col">Catalogo</th>
                <th scope="col">Accesorio</th>
                
              </tr>
            </thead>
            <tbody>
                {% for pro in productos  %}
              <tr>
                
                <td>{{pro.id}}</td>
                <td>{{pro.nombre}}</td>
                <td>{{pro.tipo}}</td>
                <td>{{pro.catalogo_origen}}</td>
                <td>{{pro.accesorio_origen}}</td>
                
              </tr>
              {% endfor %}
            
            </tbody>
          </table>      
      {% endif %}
  
      {% if productos.count == 0 %}
      <div class="alert alert-warning mt-3" role="alert">
          {{valida}} 
      </div>
      {% endif %}
    </div>
  </div>
  
  {% endblock %}
```
Creamos las nuevas vistas:
```python
 
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
    
    

```



