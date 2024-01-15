# Mi_Primer_Entrega_Rafael_Ivan_Acevedo


## Nombre : Rafael Ivan Acevedo

## Comision: 56060

## Resumen del proyecto

-

## Pasos para ejecutar el proyecto

-Creamos un repositorio de Git Hub

-Copiamos el link 

-Creamos un entorno virtual
  -python -m venv .venv

  -.\.venv\Scripts\activate

-Creamos un archivo requirements

-Instalar las dependencias con pip requirements:
  -Django


-Creamos las aplicaciones

-creamos los models 

-importamos los modelos con:   (python manage.py makemigrations)  ## Este comando analiza los modelos en tu aplicación y compara la estructura actual de la base de datos con las definiciones de tus modelos. Luego, genera archivos de migración que describen cómo la base de datos debe cambiar para reflejar esos modelos.

-Usamos  (python manage.py migrate)  para aplicar las migraciones pendientes en la base de datos

     Importante 

    Repite estos pasos cada vez que realices cambios en tus modelos. Esto asegura que tu base de datos esté siempre en sincronía con la estructura actual de tu aplicación.


-Creamos un super usuario



-registramos el super usuario en la carpeta admin


-creamos 2 carpetas en nuestra aplicacion :
     -template que contendra otra carpeta con el nombre de la aplicacion y dentro de esta carpeta un archivo html que sera el base o padre y otro archivo que heredara  del padre gracias a {% extends 'direccion de la carpeta/la plantilla padre' %}


-creamos las vistas


-Ejecutamos el servidor



