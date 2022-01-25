# FreeCAD Docker CLI mode/es
{{TOCright}}

## Vista general 

Imagen Docker de FreeCAD compilada sin GUI. Esta imagen Docker es especialmente para los desarrolladores que sólo quieren utilizar FreeCAD en la interfaz de línea de comandos (CLI).

### Beneficios

Todas las dependencias de FreeCAD ya están instaladas, son compatibles entre sí y están configuradas adecuadamente, lo que te permite empezar a desarrollar muy rápidamente.

-   Es fácil de usar y ligero.
-   Da un mejor rendimiento en términos de velocidad.
-   No es necesario añadir rutas de FreeCAD para importarlo a Python.

## Docker Repositorio 

-   Docker Hub: <https://hub.docker.com/r/amrit3701/freecad-cli>
-   Repositorio Github: <https://github.com/amrit3701/docker-freecad-cli>

## Prerequisitos

-   3 GB de almacenamiento gratuito
-   Docker

## Instalación

1.  Extrae la imagen Docker.{{Code|lang=bash|code=
    docker pull amrit3701/freecad-cli:latest
    }}


<div class="mw-translate-fuzzy">

1.  Cuando haya sacado la imagen docker con éxito, ahora puede ejecutar la imagen.


</div>


{{Code|lang=bash|code=
docker run -it amrit3701/freecad-cli:lastest bash
}}

## Información adicional 

### Extender imagen Docker 

También puedes ampliar estas imágenes Docker para añadir dependencias adicionales para tu proyecto. Por ejemplo {{Code|lang=docker|code=

# Dockerfile

FROM amrit3701/freecad-cli:lastest

# Add additional dependencies

# pip3.8 install <some_package>
}}

### Importar FreeCAD en Python 

Después de ejecutar la imagen Docker, simplemente ejecuta Python.


{{Code|lang=bash|code=
$ docker run -it amrit3701/freecad-cli:lastest bash
root@f0ec904cf9b9:/# python3.8
Python 3.8.5 (default, Jul 20 2020, 19:48:14)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import FreeCAD
>>> import Part
>>> import Draft
>>> import Arch
}}

### Lanzar FreeCADCmd 

Para lanzar FreeCAD dentro de la imagen Docker, simplemente ejecuta el comando FreeCADCmd.

## Discusión

FreeCAD hilo de foro: <https://forum.freecadweb.org/viewtopic.php?f=8&t=45877>



---
![](images/Right_arrow.png) [documentation index](../README.md) > FreeCAD Docker CLI mode/es
