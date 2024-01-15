from django.shortcuts import render,redirect
from . import models,forms   # me permite consultar a la base de datos

def index(request):
     return render(request,"Alumnos/index.html")#carpeta de la app + direccion html

def alumnos_list(request):
    consulta = models.Estudiante.objects.all() #la variable consulta accede a la base de datos
    contexto = {"alumnos": consulta} # contexto es un diccionario que toma como clave valor a profesores y lo tomado en consulta
    return render (request, "Alumnos/alumnos_list.html", contexto) #renderiza  la pagina html con el contexto
#que seria el diccionario   con el nombre profesor/s

def alumnos_creat(request):
    if request.method =="POST":
        form =forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumnos_list")#nombre de la url
    else:
        form= forms.EstudianteForm()    
    return render(request,"Alumnos/alumnos_creat.html",{"form":form})#el contexto es un diccionario
#la calve es un string y el valor es una instancia 