# FreeCAD Docker CLI mode/it
}





{{TOCright}}



## Panoramica

L\'immagine Docker di FreeCAD compilata senza GUI. Questa immagine Docker è specifica per gli sviluppatori che desiderano utilizzare FreeCAD solo da riga di comando (CLI).



### Vantaggi

Tutte le dipendenze di FreeCAD sono già installate, compatibili tra loro e configurate in modo appropriato, consentendo di iniziare a sviluppare molto rapidamente.

-   Facile da usare e leggero.
-   Offre prestazioni migliori in termini di velocità.
-   Non è necessario aggiungere percorsi a FreeCAD per importarlo in Python.



## Repository Docker 

-   Docker Hub: <https://hub.docker.com/r/amrit3701/freecad-cli>
-   Github repository: <https://github.com/amrit3701/docker-freecad-cli>



## Prerequisiti

-   3 GB di spazio libero
-   Docker



## Installazione

1.  Prelevare l\'immagine Docker.{{Code|lang=bash|code=
    docker pull amrit3701/freecad-cli:latest
    }}
2.  Quando hai scaricato correttamente l\'immagine Docker, si può eseguire l\'immagine.{{Code|lang=bash|code=
    docker run -it amrit3701/freecad-cli:lastest bash
    }}



## Informazioni aggiuntive 



### Estendere l\'immagine Docker 

Si può anche estendere queste immagini Docker per aggiungere ulteriori dipendenze per il progetto. Per esempio: {{Code|lang=docker|code=

# Dockerfile

FROM amrit3701/freecad-cli:lastest

# Add additional dependencies

# pip3.8 install <some_package>
}}



### Importare FreeCAD in Python 

Dopo aver eseguito l\'immagine Docker, eseguire semplicemente Python.


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



### Avviare FreeCADCmd 

Per avviare FreeCAD all\'interno dell\'immagine Docker, basta eseguire il comando FreeCADCmd.



## Discussione

FreeCAD forum thread: <https://forum.freecadweb.org/viewtopic.php?f=8&t=45877>



---
![](images/Button_right.svg) [documentation index](../README.md) > FreeCAD Docker CLI mode/it
