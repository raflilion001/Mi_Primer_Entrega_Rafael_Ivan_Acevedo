from django.shortcuts import render


from . import models   # me permite consultar a la base de datos


def index(request):
    
    return render(request,"Clientes/index.html")#carpeta de la app + direccion html


def profesor_list(request):
    consulta = models.Profesor.objects.all() #la variable consulta accede a la base de datos
    
    contexto = {"profesores": consulta} # contexto es un diccionario que toma como clave valor a profesores y lo tomado en consulta
    
    return render (request, "Clientes/profesor_list.html", contexto) #renderiza  la pagina html con el contexto
#que seria el diccionario   con el nombre profesor/s