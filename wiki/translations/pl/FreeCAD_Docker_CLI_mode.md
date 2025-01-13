# FreeCAD Docker CLI mode/pl
}









## Informacje ogólne 

Obraz Docker programu FreeCAD skompilowanego bez GUI. Ten obraz Dockera jest przeznaczony dla programistów, którzy chcą używać programu FreeCAD tylko w interfejsie wiersza poleceń *(CLI)*.



### Korzyści

Wszystkie zależności FreeCAD są już zainstalowane, kompatybilne ze sobą i odpowiednio skonfigurowane, co pozwala na bardzo szybkie rozpoczęcie programowania.

-   Łatwy w użyciu i lekki.
-   Zapewnia lepszą wydajność pod względem szybkości.
-   Nie ma potrzeby dodawania ścieżek FreeCAD, aby zaimportować go do środowiska Python.



## Repozytorium Docker 

-   Docker Hub: <https://hub.docker.com/r/amrit3701/freecad-cli>
-   Repozytorium Github: <https://github.com/amrit3701/docker-freecad-cli>



## Wymagania wstępne 

-   3 GB wolnej przestrzeni dyskowej.
-   Docker.



## Instalacja

1.  Uruchom obraz Docker.{{Code|lang=bash|code=
    docker pull amrit3701/freecad-cli:latest
    }}
2.  Po pomyślnym pobraniu obrazu Docker można go teraz uruchomić.{{Code|lang=bash|code=
    docker run -it amrit3701/freecad-cli:lastest bash
    }}



## Informacje dodatkowe 



### Rozszerz obraz Docker 

Możesz również rozszerzyć te obrazy Docker, aby dodać dodatkowe zależności dla swojego projektu. Na przykład: {{Code|lang=docker|code=

# Dockerfile

FROM amrit3701/freecad-cli:lastest

# Add additional dependencies

# pip3.8 install <some_package>
}}



### Import FreeCAD w środowisku Python 

Po uruchomieniu obrazu Docker wystarczy uruchomić Python.


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



### Uruchom FreeCADCmd 

Aby uruchomić FreeCAD wewnątrz obrazu Docker, wystarczy wykonać polecenie FreeCADCmd.



## Dyskusja

Wątek na forum FreeCAD: <https://forum.freecadweb.org/viewtopic.php?f=8&t=45877>



---
⏵ [documentation index](../README.md) > FreeCAD Docker CLI mode/pl
