# <img alt="" src=images/MOOC_workbench_icon.svg  style="width:240px;">  MOOC Workbench/fr
*align=center|L'icône de l'atelier externe MOOC FreeCAD*



## Présentation


{{TOCright}}

L\'atelier MOOC est un [atelier externe](External_workbenches/fr.md) avec lequel vous pouvez suivre des didacticiels interactifs et faire l\'évaluation de votre travail directement dans l\'interface FreeCAD. L\'atelier MOOC propose 2 outils: des tutoriels interactifs et des évaluations.

-   Actuellement uniquement en français (et codé en dur).
-   Compatible uniquement avec FreeCAD Py3 et Qt5 (PySide2)
-   Code LGPLv2 (ou similaire) financé par l\'Europe via IMT et EESAB.
-   Modulaire: cet atelier a été créé dans le but que l\'ajout de tutoriels et d\'évaluations soit modulaire. En d\'autres termes, il faut ajouter un tutoriel dans le dossier **lessons** ou une évaluation dans le dossier **exercises** pour apparaître dans l\'outil respectif.

**Les tutoriels Interactifs** (aussi appelés Player) sont des exercices guidés pas à pas avec des vérifications d\'objectifs. Il se lance directement dans FreeCAD et vous permet d\'avancer pas à pas dans la modélisation d\'un objet. L\'utilisateur dispose d\'un texte, d\'une vidéo et surtout d\'une vérification que les objectifs ont été atteints.

### Interactif

Les tutoriels **interactifs** (aussi appelés <img alt="" src=images/MOOC_Player.svg  style="width:24px;"> Player) sont des exercices guidés étape par étape avec des vérifications objectives. Il se lance directement dans FreeCAD et vous permet d\'avancer une étape à la fois de la modélisation d\'un objet. L\'utilisateur dispose d\'un texte, d\'une vidéo et surtout d\'un contrôle que les objectifs ont bien été atteints.

<img alt="" src=images/MOOC_Player_Dialog_Context.png  style="width:1024px;"> 
*align=center|Boîte de dialogue du lecteur MOOC dans l'interface graphique de FreeCAD* ![](images/MOOC_Player_Dialog.png ) 
*Boîte de dialogue du lecteur MOOC de plus près*

### Evaluations

**Evaluations** (aussi appelé <img alt="" src=images/MOOC_Grader.svg  style="width:24px;"> Grader) consiste en un petit programme qui vérifie certains critères d\'un document FreeCAD, par exemple, la présence d\'une partie du corps, d\'un croquis ou du volume final. <img alt="" src=images/MOOC_Grader_Dialog.png  style="width:1024px;"> 
*align=center|La boîte de dialogue de Grader du MOOC*

## Installation

Cet atelier peut être installé à partir du [Gestionnaire des extensions](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).

## Limitations

Pour l\'instant cet atelier est uniquement disponible en langue française.



## Détails techniques 

D\'un point de vue technique, l\'atelier est composé de:

-   une \"API\" qui contient le code qui analyse le document (**MoocChecker.py**)
-   le code qui exécute les tutoriels dans le dossier \"leçons\" (**MoocPlayer.py**)
-   le code qui exécute les évaluations dans le dossier \"exercices\" (**MoocGrader.py**)

## Feuille de route 

-   internationalisation de l\'établi
-   Intégration de vidéos dans FreeCAD (PySide2.QtWebEngineWidgets?)
-   demander l\'intégration du plan de travail dans la liste du gestionnaire d\'extensions TERMINÉ



## Liens

-   Code source hébergé sur Framagit: [1](https://framagit.org/freecad-france/mooc-workbench)
-   Documentation officielle [2](https://framagit.org/freecad-france/mooc-workbench#mooc-workbench)
-   Fils de discussion: [anglais](https://forum.freecadweb.org/viewtopic.php?f=9&t=37584) / [français](https://forum.freecadweb.org/viewtopic.php?f=12&t=37322)



## Ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), de ce fait, beaucoup de personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page [ateliers externes](External_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux. Le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, tenez vous au courant!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > MOOC Workbench/fr
