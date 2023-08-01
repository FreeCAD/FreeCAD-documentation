# FreeCAD Docker CLI mode/pt-br
}





{{TOCright}}

## Visão geral 

Docker image of FreeCAD compiled without GUI. This Docker image is especially for developers who only want to use FreeCAD in the command-line interface (CLI).

### Benefits

All of FreeCAD\'s dependencies are already installed, compatible with each other, and configured appropriately, allowing you to get started developing very quickly.

-   Easy to use and lightweight.
-   It gives better performance in terms of speed.
-   No need to add FreeCAD paths to import it into Python.

## Docker Repository 

-   Docker Hub: <https://hub.docker.com/r/amrit3701/freecad-cli>
-   Github repository: <https://github.com/amrit3701/docker-freecad-cli>

## Pré-requisitos 

-   3 GB of free storage
-   Docker

## Instalação

1.  Pull the Docker image.{{Code|lang=bash|code=
    docker pull amrit3701/freecad-cli:latest
    }}
2.  When you successfully pulled Docker image, now you can run image.{{Code|lang=bash|code=
    docker run -it amrit3701/freecad-cli:lastest bash
    }}

## Additional information 

### Extend Docker image 

You can also extend this Docker images to add additional dependencies for your project. For eg {{Code|lang=docker|code=

# Dockerfile

FROM amrit3701/freecad-cli:lastest

# Add additional dependencies

# pip3.8 install <some_package>
}}

### Import FreeCAD in Python 

After running Docker image, just run Python.


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

### Launch FreeCADCmd 

To launch FreeCAD inside Docker image, just run FreeCADCmd command.

## Discussão

FreeCAD forum thread: <https://forum.freecadweb.org/viewtopic.php?f=8&t=45877>



---
![](images/Button_right.svg) [documentation index](../README.md) > FreeCAD Docker CLI mode/pt-br
