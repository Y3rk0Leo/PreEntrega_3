
from django.urls import path, include
from . import views

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
