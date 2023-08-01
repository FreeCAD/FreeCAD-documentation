# <img alt="Icône de l\'atelier externe Manipulator" src=images/Manipulator_workbench_icon.svg  style="width:64px;"> Manipulator Workbench/fr

## Introduction


{{TOCright}}

L\'[Atelier Manipulator](Manipulator_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) destiné à aider les utilisateurs de FreeCAD à aligner, déplacer, faire pivoter et mesurer des objets 3D via une interface graphique conviviale. Ces séries d\'outils aident à transformer les objets de placement et de mesure et les modèles STEP dans FreeCAD.

## Fonctionnalités

![](images/Aligner-ico.png ) **Aligner :** ensemble d\'outils permettant de déplacer et d\'aligner des pièces 3D ; il peut également aligner un objet (face, arête, point) sur l\'origine dans FreeCAD.

![](images/Manipulator_Mover.svg ) **Mover :** ensemble d\'outils pour déplacer et faire pivoter des pièces 3D sur différents axes.

![](images/Manipulator_Caliper.svg ) **Caliper :** ensemble d\'outils permettant de mesurer des pièces 3D, avec une fonction d\'aimantation et des mesures de rayon, de longueur et d\'angle.

Ces aides fonctionnent avec les objets **Part, App::Part et Body**.

Les outils peuvent être **flottants** ou **dockés à gauche ou à droite**.

Chaque outil a un **bouton d\'aide** ![](images/_Help-btn.png ) pour obtenir des conseils utiles.

## Références

-   Auteur sur github : [\@easyw](https://github.com/easyw)
-   Forums FreeCAD : [easyw-fc](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=6387)
-   Code source sur github: <https://github.com/easyw/Manipulator>
-   Annonces/discussion du forum : <https://forum.freecadweb.org/viewtopic.php?t=24742>

## Tutoriel

<img alt="Title Manipulator-WB-@Work" src=images/Manipulator-WB-@Work.png  style="width:1024px;">



*Tutoriel sur YouTube [https://youtu.be/owGzsd1fyZc Manipulator WorkBench @Work]*

## Outils

![](images/Manipulator-WB-Tools.png ) 
*Ci-dessus : boîte de dialogue de l'atelier Manipulator. Pour une description plus détaillée, voir [https://github.com/easyw/Manipulator/blob/master/README.md README.md] sur Github.*

### Aligner

![](images/Manipulator-WB-Aligner.gif ) 
*Aligner : ensemble d'outils permettant de déplacer et d'aligner des pièces 3D ; il peut également aligner un objet (face, arête, point) sur l'origine dans FreeCAD.*

### Mover

![](images/Manipulator-WB-Mover.gif ) 
*Mover : ensemble d'outils pour déplacer et faire pivoter des pièces 3D sur différents axes*

![](images/Manipulator-WB-Mover-with-App_Part&Body.gif ) 
*Mover : Utilisation de App:Part et d'un corps*

![](images/Manipulator-WB-Mover-with-External-Reference.gif ) 
*Mover : avec une référence externe*

### Caliper

![](images/Manipulator-WB-Measure-Radius.gif ) 
*Caliper : mesure de rayon*

![](images/Manipulator-WB-Measure-Angles.gif ) 
*Caliper: mesure d'angles*

![](images/Manipulator-WB-Dimension.gif ) 
*Caliper : mesure de dimensions*

![](images/Manipulator-WB-Dimension-2.gif ) 
*Caliper : mesure de dimensions (suite)*

![](images/Manipulator-WB-Parallel-Planes-Distance.gif ) 
*Caliper : distance entre deux plans parallèles*

### Manipulator

![](images/Manipulator-WB-Assembly-Parts.gif )

## Installation

### Installation automatique 

La méthode recommandée pour installer l\'atelier Manipulator est via le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) dans le menu **Outils → Gestionnaire des extensions**.


<div class="mw-collapsible mw-collapsed toccolours" style="width:600px">

### Installation manuelle 

Si une installation manuelle est nécessaire, veuillez suivre les instructions suivantes:


<div class="mw-collapsible-content">

-   Copier les sources de Manipulator dans le sous-répertoire **Mod** de l\'application FreeCAD.


```python
cd ~/.FreeCAD/Mod 
git clone https://github.com/easyw/Manipulator Manipulator
```

-   Redémarrer FreeCAD


</div>


</div>

### Supports

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 11707
-   FreeCAD v0.18+
-   FreeCAD v0.19+

## Histoire

L\'atelier a évolué à partir de la macro [Center Align Objects with Faces or Edges](Macro_Center_Align_Objects_with_Faces_or_Edges/fr.md).

## Ateliers extérieurs 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), il y a donc beaucoup de gens qui développent des établis supplémentaires en dehors des développeurs principaux de FreeCAD.

La page des [ateliers externes](External_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, tenez vous au courant!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Manipulator Workbench/fr
