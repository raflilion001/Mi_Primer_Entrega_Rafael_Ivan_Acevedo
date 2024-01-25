
from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.index,name ="index"),
    path('profesor/list',views.profesor_list,name='profesor_list'), #el name es el nombre que tenemos que usar 
    #en el html <button><a href="{% url 'profesor_list' %}">Ver  Profesores</a></button>
    path('profesor/creat', views.profesor_creat, name ="profesor_creat"),
    path('alumnos/list',views.alumnos_list,name='alumnos_list'),
    path('alumnos/creat',views.alumnos_creat,name='alumnos_creat'),
    path('eliminarProfesores/<profesor_nombre>',views.eliminar_profesor,name='EliminarProfesor'),
    path('eliminarProfesores/<estudiante_nombre>',views.eliminar_estudiante,name='EliminarEstudiante'),
]
    



