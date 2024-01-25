from django.shortcuts import render,redirect, get_object_or_404
from . import models,forms   # me permite consultar a la base de datos
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

def index(request):
     return render(request,"Clientes/index.html")#carpeta de la app + direccion html

def profesor_list(request):
    consulta = models.Profesor.objects.all() #la variable consulta accede a la base de datos
    contexto = {"profesores": consulta} # contexto es un diccionario que toma como clave valor a profesores y lo tomado en consulta
    return render (request, "Clientes/profesor_list.html", contexto) #renderiza  la pagina html con el contexto
#que seria el diccionario   con el nombre profesor/s

def profesor_creat(request):
    if request.method =="POST":
        form =forms.ProfesorForm(request.POST)# aqui nos llega la informacion del html
        if form.is_valid():
            form.save()
            return redirect("profesor_list")#nombre de la url
    else:
        form= forms.ProfesorForm()    
    return render(request,"Clientes/profesor_creat.html",{"form":form})#el contexto es un diccionario
#la calve es un string y el valor es una instancia          




def alumnos_list(request):
    consulta = models.Estudiante.objects.all() 
    contexto = {"alumnos": consulta} 
    return render (request, "Clientes/alumnos_list.html", contexto) 

def alumnos_creat(request):
    if request.method =="POST":
        form =forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumnos_list")
    else:
        form= forms.EstudianteForm()    
    return render(request,"Clientes/alumnos_creat.html",{"form":form})


def eliminar_profesor(request,profesor_nombre):
    profesor = models.Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesores =models.Profesor.objects.all() 
    contexto = {"profesores":profesores}
    return render (request, "Clientes/profesor_list.html",contexto)

#en todo lo que implique crear o modificar la base de datos utilizaremos obligatoriamente el if 

def eliminar_estudiante(request,estudiante_nombre):
    estudiante = models.Profesor.objects.get(nombre=estudiante_nombre)
    estudiante.delete()
    
    estudiantes =models.Profesor.objects.all() 
    contexto = {"estudiantes":estudiantes}
    return render (request, "Clientes/estudiantes_list.html",contexto)

    
    