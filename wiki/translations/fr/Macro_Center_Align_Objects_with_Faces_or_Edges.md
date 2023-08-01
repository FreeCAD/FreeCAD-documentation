# Macro Center Align Objects with Faces or Edges/fr
**Cet outil est maintenant inclus dans l'atelier [Manipulator Workbench](Manipulator_Workbench/fr.md). Installez cet atelier pour bénéficier des dernières mises à ajours.**


{{Macro/fr
|Name=Center Faces of Parts
|Icon=Macro_Center_Align_Objects_with_Faces_or_Edges.svg
|Description=Cette macro aligne et contraint un objet sur la face ou le bord d'un autre objet. Cet outil est maintenant inclus dans l'atelier [Manipulator Workbench](Manipulator_Workbench/fr.md)
|Author=easyw-fc
|Version=1.5.3
|Date=2017-10-01
|FCVersion=Tous
|Download=[https://www.freecadweb.org/wiki/images/e/ee/Macro_Center_Align_Objects_with_Faces_or_Edges.svg ToolBar Icon]<br/>[https://www.freecadweb.org/wiki/images/3/3d/Manipulator_Mover.svg Mover-icon]<br/>[https://www.freecadweb.org/wiki/images/1/10/Manipulator_Caliper.svg Caliper-icon]
}}

## Description

Cette macro contraint et aligne des objets sur les faces ou les bords


{{Codeextralink|https://raw.githubusercontent.com/easyw/FreeCAD_Macros/master/Align%20Objects/CenterAlignObjectswFacesEdges.py}}

## Tools

**Aligner** <img alt="" src=images/Macro_Center_Align_Objects_with_Faces_or_Edges.svg  style="width:32px;">: un ensemble d\'outils pour déplacer et aligner des parties 3D

**Mover** <img alt="" src=images/Manipulator_Mover.svg  style="width:32px;">: un ensemble d\'outils pour déplacer et faire pivoter des pièces 3D sur différents axes

**Measure** <img alt="" src=images/Manipulator_Caliper.svg  style="width:32px;">: un ensemble d\'outils pour mesurer des pièces 3D, avec une fonction d\'accrochage et des mesures de rayon, de longueur et d\'angle.

Ces aides fonctionnent avec les objets **Part, App :: Part et Body**. Chaque outil peut être **Flottant** ou **Docké à Gauche ou à Droite**.



## Anciennes Références 

Cette macro couvre les contraintes suivantes:

-   Contrainte concentrique parmi les parties non cylindriques;
-   Contrainte sur les faces centrales et/ou les bords.
-   Il fonctionne aussi avec les nouveaux conteneurs Body et App::Part, ainsi qu\'avec la hiérarchie STEP.

![](images/Center-align-faces.png )

![](images/center-align-faces-in-action.gif )

![](images/center-align-Body-objects.gif )

![](images/utube-alignment-tool-tutorial.png )

[Aligning tool video tutorial](https://youtu.be/qzixT157jJU)

![](images/utube-alignment-STEP-models.png )

[Aligning STEP models video tutorial](https://youtu.be/aQcPqhlgHBU)

## Utilisation

Contraint un objet sur la face ou bord d\'un autre objet non cylindrique: Ouvrez un document, lancez la Macro et sélectionnez deux ou plusieurs faces/bords pour les aligner. Cliquez sur le bouton **Align** et c\'est tout!

## Script

L\' icône pour votre barre d\'outils <img alt="" src=images/Macro_Center_Align_Objects_with_Faces_or_Edges.png  style="width:50px;">

**CenterAlignObjectswFacesEdges.py**

Après avoir copié la macro sur la page
GitHub
<https://github.com/easyw/FreeCAD_Macros/blob/master/Align%20Objects/CenterAlignObjectswFacesEdges.py>
code:
<https://github.com/easyw/FreeCAD_Macros/raw/master/Align%20Objects/CenterAlignObjectswFacesEdges.py>
vous devez la coller dans votre répertoire de macros
[Comment installer une macro](How_to_install_macros.md)

## Lien

Forum : [Faces or Edges constraint among non cylindrical parts Macro](http://forum.freecadweb.org/viewtopic.php?f=22&t=18655)



---
⏵ [documentation index](../README.md) > Macro Center Align Objects with Faces or Edges/fr
