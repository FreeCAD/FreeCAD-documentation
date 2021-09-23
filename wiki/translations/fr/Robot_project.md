# Robot project/fr



**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

Cet [projet d\'article](project/fr.md) est pour le projet Robot. Il suit les règles de la \[<http://fr.wikipedia.org/wiki/Getting_Things_Done>\| Getting things done\] processus. Les projets sont collectées dans la [feuille de route de développement](Development_roadmap/fr.md).

## Buts et principles 

Ce projet devrait fixer les principales technologiques, pour une simulation réaliste de robot dans FreeCAD. Dans la première étape, il vise la norme robot industriel 6-axis.

## Résultats

Simulation de robot

![](images/Robot.jpg )

## Réflexions

### Librairies disponibles 

-   [OROCOS](http://www.orocos.org/) bibliothèques C ++ portables pour un contrôle avancé des machines et des robots
-   [ROBOOP](http://roboop.sourceforge.net/) Un package orienté objet robotique en C ++
-   [Beremiz](http://www.beremiz.org/) un automate OpenSource PLC.

### Standards de communications 

-   [OPC UA](http://en.wikipedia.org/wiki/OPC_Unified_Architecture) un protocole de communication machine à machine pour l\'automatisation industrielle (PLC)
-   [1](https://www.ipk.fraunhofer.de/de/referenzen/realistic-robot-simulation.html) Initiative allemande pour améliorer la précision des contrôleurs de robots et optimiser la programmation des robots hors ligne
-   [Realistic Robot Simulation (RRS)](http://www.realistic-robot-simulation.org/) RRS-2, interface de contrôleur de robot virtuel (VRC)

### Middleware pour comunications 

-   [D-Bus](http://en.wikipedia.org/wiki/D-Bus) un bus logiciel, une communication inter-processus (IPC) et un mécanisme d\'appel de procédure à distance (RPC) qui permet la communication entre plusieurs programmes informatiques
-   [CORBA](http://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture) permet la collaboration entre des systèmes sur différents systèmes d\'exploitation, langages de programmation et matériel informatique

### Les produits Commerciaux dans le domaine 

-   [Visual Components](http://www.visualcomponents.com/Solutions/Robot-Simulation)
-   [Delmia](http://www.3ds.com/products/delmia/welcome/)
-   [KUKA Sim](http://www.kuka-robotics.com/france/fr/products/software/simulation/start.htm)

### Connaissance

-   [Définition cinématique](http://prt.fernuni-hagen.de/lehre/KURSE/PRT001/course_main/node15.html) -\> lien obsolète !!!
-   [Denavit -- Hartenberg parameters](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters) paramètres associés à une convention particulière pour attacher des référentiels aux liens du robot manipulateur
-   [Roboter VRML modele](http://www.iha.tut.fi/education/IHA-3500/robotlib/) -\> lien obsolète !!!

## Organisation

-   La représentation visuelle des robots 6 axes (fait).
-   Le calcul cinématique de robots directe et inverse, arbitraires (fait).
-   RobotLib, types dynamique lisible de robots (travail en cours).
-   Simulation de la trajectoire (travail en cours).
    -   simulation de collision.
    -   détection des changements de configuration, et, de singularités.
    -   estimation du temps.
    -   volume utilisé (raboté).
-   Post processeur pour robots [Kuka](http://www.kuka-robotics.com/fr/) (travail en cours).
-   Processus et contrôle de cellule de travail (raboté).
-   La réalisation de films sur la simulation (raboté).

## Actions suivantes 

-   Trajectoire, et gestion des points de cheminement.



[Category:Roadmap](Category:Roadmap.md)
