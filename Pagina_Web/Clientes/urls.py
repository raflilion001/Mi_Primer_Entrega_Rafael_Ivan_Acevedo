
from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.index,name ="index"),
    path('profesor/list',views.profesor_list,name='profesor_list'), 
    #path('profesor/creat', views.profesor_creat, name ="profesor_creat"),
]

