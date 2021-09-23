# FreeCAD Docker CLI mode/fr
 





{{TOCright}}

## Présentation

Image Docker de FreeCAD compilée sans GUI. Cette image de Docker est spécialement destinée aux développeurs qui ne souhaitent utiliser FreeCAD que dans l\'interface de ligne de commande (CLI).

### Bénéfices

Toutes les dépendances de FreeCAD sont déjà installées, compatibles les unes avec les autres et configurées de manière appropriée, ce qui vous permet de commencer à développer très rapidement.

-   Facile à utiliser et léger.
-   Il donne de meilleures performances en termes de vitesse.
-   Pas besoin d\'ajouter des chemins FreeCAD pour l\'importer dans Python.

## Dépôt Docker 

-   Docker Hub : <https://hub.docker.com/r/amrit3701/freecad-cli>
-   Dépôt Github : <https://github.com/amrit3701/docker-freecad-cli>

## Prérequis

-   3 GB de mémoire libre
-   Docker

## Installation

1.  Récupérez l\'image Docker.{{Code|lang=bash|code=
    docker pull amrit3701/freecad-cli:latest
    }}
2.  Quand vous avez réussi à extraire l\'image du docker, vous pouvez maintenant lancer l\'image.{{Code|lang=bash|code=
    docker run -it amrit3701/freecad-cli:lastest bash
    }}

## Information Supplémentaire 

### Extension de l\'image de Docker 

Vous pouvez également étendre ces images Docker pour ajouter des dépendances supplémentaires pour votre projet. Par exemple {{Code|lang=docker|code=

# Dockerfile

FROM amrit3701/freecad-cli:lastest

# Add additional dependencies

# pip3.8 install <some_package>
}}

### Importer FreeCAD en Python 

Après avoir exécuté l\'image du Docker, il suffit de lancer Python.


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

### Lancer FreeCADCmd 

Pour lancer FreeCAD dans l\'image de Docker, exécutez simplement la commande FreeCADCmd .

## Discussion

-   Fil du forum FreeCAD : <https://forum.freecadweb.org/viewtopic.php?f=8&t=45877>




