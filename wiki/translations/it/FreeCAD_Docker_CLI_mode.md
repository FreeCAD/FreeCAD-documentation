# FreeCAD Docker CLI mode/it
}





{{TOCright}}



## Panoramica

L\'immagine Docker di FreeCAD compilata senza GUI. Questa immagine Docker è specifica per gli sviluppatori che desiderano utilizzare FreeCAD solo da riga di comando (CLI).



### Vantaggi

All of FreeCAD\'s dependencies are already installed, compatible with each other, and configured appropriately, allowing you to get started developing very quickly.

-   Easy to use and lightweight.
-   It gives better performance in terms of speed.
-   No need to add FreeCAD paths to import it into Python.



## Repository Docker 

-   Docker Hub: <https://hub.docker.com/r/amrit3701/freecad-cli>
-   Github repository: <https://github.com/amrit3701/docker-freecad-cli>



## Prerequisiti

-   3 GB di spazio libero
-   Docker



## Installazione

1.  Pull the Docker image.{{Code|lang=bash|code=
    docker pull amrit3701/freecad-cli:latest
    }}
2.  When you successfully pulled Docker image, now you can run image.{{Code|lang=bash|code=
    docker run -it amrit3701/freecad-cli:lastest bash
    }}



## Informazioni aggiuntive 

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



## Discussione

FreeCAD forum thread: <https://forum.freecadweb.org/viewtopic.php?f=8&t=45877>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > FreeCAD Docker CLI mode/it
