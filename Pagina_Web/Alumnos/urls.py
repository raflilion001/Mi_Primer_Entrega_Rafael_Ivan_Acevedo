
from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.index,name ="index"),
    path('alumno/list',views.alumnos_list,name='alumnos_list'),
    path('alumno/creat', views.alumnos_creat, name ="alumnos_creat"),
]

