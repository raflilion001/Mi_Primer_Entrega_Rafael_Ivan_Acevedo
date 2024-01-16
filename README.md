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


-Creamos las aplicaciones con : python manage.py startapp nombre de la app

-Agregamos la app a settings en el apartado INSTALLED_APPS 

-Creamos un archivo urls.py

-creamos los models Modelos

Los modelos de Django se utilizan para representar los datos de la aplicación. Los modelos se definen en el archivo models.py.

Cuando un usuario ingresa a una URL que corresponde a una vista que utiliza un modelo, el servidor web carga el modelo correspondiente. El modelo se utiliza para acceder a los datos de la base de datos.

-importamos los modelos con:   (python manage.py makemigrations)  ## Este comando analiza los modelos en tu aplicación y compara la estructura actual de la base de datos con las definiciones de tus modelos. Luego, genera archivos de migración que describen cómo la base de datos debe cambiar para reflejar esos modelos.

-Usamos  (python manage.py migrate)  para aplicar las migraciones pendientes en la base de datos

     Importante 

    Repite estos pasos cada vez que realices cambios en tus modelos. Esto asegura que tu base de datos esté siempre en sincronía con la estructura actual de tu aplicación.

-Creamos un super usuario

-registramos el super usuario en la carpeta admin

-creamos un archivo forms.py Formularios se utilizan para recopilar datos del usuario. Los formularios se definen en el archivo forms.py.

Cuando un usuario envía un formulario, el servidor web valida los datos del formulario. Si los datos son válidos, el servidor web pasa los datos a la vista correspondiente.

-creamos las url: URL se utilizan para mapear las solicitudes del usuario a las vistas. Las URLs se definen en el archivo urls.py.

Cuando un usuario ingresa a una URL, el servidor web busca la URL correspondiente en el archivo urls.py. Si encuentra la URL correspondiente, llama a la vista correspondiente.


-creamos las vistas: se utilizan para procesar las solicitudes del usuario. Las vistas se definen en el archivo views.py.

Las vistas reciben los datos del usuario de la solicitud y los utilizan para generar una respuesta. La respuesta puede ser una página web, un archivo, o cualquier otro tipo de contenido.

-creamos las plantillas: se utilizan para generar el contenido de las páginas web. Las plantillas se definen en el archivo templates/Nombre de la app/NombreDescriptivo.html

Las plantillas utilizan el lenguaje de plantillas de Django para generar el contenido de las páginas web. El lenguaje de plantillas de Django es un lenguaje sencillo que se basa en HTML.

-Ejecutamos el servidor


En resumen 

1ro: creamos un repositorio de Git Hub

2do: copiamos el link de ese proyecto 

3ro: Creamos un entorno virtual

4to: Lo activamos 

5to: Instalar las dependencias con pip requirements(django)

6to: Creamos las aplicaciones con : python manage.py startapp nombre de la app

7tmo: Agregamos la app a settings en el apartado INSTALLED_APPS 

8vo: Creamos los archivos correspondientes: models, forms, urls, views

9no: Migramos los models 

10mo: Checamos que nuestras importaciones esten bien escritas y coincidan 

11vo :Checamos tambien las urls de la parte principal 

12vo: Arrancamos el servidor para comprovar qeu ande correctamente con python manage.py runserver




