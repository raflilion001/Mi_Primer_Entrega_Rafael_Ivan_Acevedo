
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Clientes.urls")), #include("Clientes.urls") permite delegar la gestión de las rutas a otro archivo urls.py dentro de la aplicación "Clientes"
   
]