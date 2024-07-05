"""
URL configuration for portfolioproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
# Importa la función 'path' de django.urls y las vistas del módulo actual.

urlpatterns = [
    # Define una lista de rutas URL para la aplicación.
    
    path('', views.home, name='home'),
    # Ruta para la página de inicio que muestra los proyectos. 
    # URL: '' (vacía), vista: 'index', nombre: 'index'.

    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    # Ruta para crear un nuevo contacto. 
    # URL: 'contacto/nuevo/', vista: 'contacto_nuevo', nombre: 'contacto_nuevo'.

    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    # Ruta para ver el detalle de un contacto específico.
    # URL: 'contacto/<int:pk>/', vista: 'contacto_detalle', nombre: 'contacto_detalle'.
    # '<int:pk>' es un parámetro que captura un entero (clave primaria).

    path('contacto/<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    # Ruta para editar un contacto específico.
    # URL: 'contacto/<int:pk>/editar/', vista: 'contacto_editar', nombre: 'contacto_editar'.

    path('contacto/<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
    # Ruta para eliminar un contacto específico.
    # URL: 'contacto/<int:pk>/eliminar/', vista: 'contacto_eliminar', nombre: 'contacto_eliminar'.

    path('contactos/', views.contacto_lista, name='contacto_lista'),
    # Ruta para listar todos los contactos.
    # URL: 'contactos/', vista: 'contacto_lista', nombre: 'contacto_lista'.

    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),
    # Ruta para mostrar la confirmación de creación de contacto.
    # URL: 'contacto/confirmacion/', vista: 'contacto_confirmacion', nombre: 'contacto_confirmacion'.

 
    path('vista_protegida/', views.vista_protegida, name='vista_protegida'),  # Nueva URL protegida
   
    path('proyecto/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),  # Nueva URL para el detalle del proyecto
]
