---
- GuiCommand:/fr
   Name:Sketcher ConstrainSnellsLaw
   Name/fr:Sketcher Contrainte de réfraction
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte de réfraction (Loi de Snell)
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**K** **W**
   Version:0.15
---

# Sketcher ConstrainSnellsLaw/fr

## Description

Contraint deux lignes à suivre la loi de la réfraction de la lumière qui pénètre à travers une interface, où deux matériaux de différents indices de réfraction se rencontrent. Voir [Loi de Snell](http://fr.wikipedia.org/wiki/Loi_de_Snell_Descartes) sur Wikipedia pour plus d\'info.

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;">



*Loi de Snell*



## Utilisation

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*La séquence des clics est indiquée par des flèches jaunes avec des chiffres. n1, n2 ne sont que des indications pour montrer où se trouvent les indices de réfraction.*

-   Vous aurez besoin de deux lignes qui vont suivre un faisceau de lumière, et une courbe pour agir comme une interface. Les lignes doivent être sur des côtés différents de l\'interface.
-   Sélectionnez l\'extrémité d\'une ligne, un point d\'extrémité d\'une autre ligne, et le bord de l\'interface. L\'interface peut être une [ligne](Sketcher_CreateLine/fr.md), un [arc](Sketcher_CompCreateArc/fr.md), un [cercle](Sketcher_CompCreateCircle/fr.md) ou un [conique](Sketcher_CompCreateConic/fr.md)
-   Lancez la contrainte. Une boîte de dialogue apparaît pour demander un rapport d\'indices de réfraction n2/n1. n2 correspond au milieu où la ligne du deuxième critère sélectionné réside, n1 est pour la première ligne.
-   Les critères d\'évaluation seront mis en coïncidence (si nécessaire), contraint à l\'interface (si nécessaire), et la loi de Snell deviendront contraint.

Notez que plusieurs [Sketcher Aides pour contraindre](Sketcher_helper_constraint/fr.md) seront ajoutées automatiquement (point sur objet, coïncidence). Elles peuvent être supprimées si elles créeent une redondance ou ajoutées manuellement si elles n\'ont pas été ajoutées automatiquement. Pour la contrainte de la loi de Snell, les extrémités des lignes doivent coïncider et reposer sur l\'interface, sinon le comportement n\'est pas défini.

En utilisant l\'outil **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Sketcher Polyligne](Sketcher_CreatePolyline/fr.md)**, il est possible d\'accélérer le tracé des rayons de lumière. Dans ce cas, il est possible de sélectionner deux extrémités coïncidentes par sélection de boîte.



## Remarques

-   La contrainte actuelle de la loi de Snell applique la plaine équation de la loi n1\*sin(theta1) = n2\*sin(theta2). Il a besoin que les extrémités des lignes soient confondues et sur l\'interface par d\'autres contraintes. Les contraintes auxiliaires nécessaires sont ajoutées automatiquement en fonction des coordonnées actuelles des éléments.
-   La routine de Python n\'ajoute pas les contraintes d\'aide. Celles-ci doivent être ajoutées manuellement par le script (voir l\'exemple dans la section Script)
-   Ces contraintes auxiliaires peuvent être supprimées temporairement et les points terminaux traînés dehors, ce qui peut être utile au cas où on veut construire un rayon réfléchi ou des rayons biréfringent.
-   Contrairement à la réalité, les indices de réfraction sont associés à des rayons de lumière, mais non pas selon les côtés de la frontière. C\'est utile pour émuler la biréfringence, construire des chemins de longueurs d\'onde différentes en raison de la réfraction, et construire facilement l\'angle de début de réflexion interne totale.
-   Les deux rayons peuvent être sur le même côté de l\'interface, répondant à l\'équation de contrainte. Cela n\'a aucun sens physique, à moins que le rapport n2/n1 est de 1,0, auquel cas la contrainte émule une réflexion.
-   Arcs de cercle et une ellipse sont également acceptés comme les rayons (non-sens physique).



## Script

Les contraintes peuvent être créées à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) en utilisant la fonction suivante:


```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```

où:

  - `Sketch` est un objet d\'esquisse

  - `line1` et `pointpos1` sont deux entiers identifiant l\'extrémité de la ligne dans le milieu avec un indice de réfraction de *n1*. `line1` est l\'index de la ligne dans l\'esquisse (la valeur, retournée par Sketch.addGeometry), et `pointpos1` doit être 1 pour le point de départ et 2 pour le point final.

  - `line2` et `pointpos2` sont les index spécifiant le point final de la seconde ligne (dans le support *n2*)

  - `interface` est l\'index spécifiant la ligne indiquant la position de l\'interface entre le support *n1* et le support *n2*

  - `n2byn1` est un nombre à virgule flottante égal au rapport des indices de réfraction *n2/n1*

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `line1`, `pointpos1`, `line2`, `pointpos2` et `interface` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.

Exemple :


```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2
MiddlePoint = 3

f = App.activeDocument().addObject("Sketcher::SketchObject","Sketch")

# add geometry to the sketch
icir = f.addGeometry(Part.Circle(App.Vector(-547.612366,227.479736,0),App.Vector(0,0,1),68.161979))
iline1 = f.addGeometry(Part.LineSegment(App.Vector(-667.331726,244.127090,0),App.Vector(-604.284241,269.275238,0)))
iline2 = f.addGeometry(Part.LineSegment(App.Vector(-604.284241,269.275238,0),App.Vector(-490.940491,256.878265,0)))
# add constraints
# helper constraints:
f.addConstraint(Sketcher.Constraint('Coincident',iline1,EndPoint,iline2,StartPoint)) 
f.addConstraint(Sketcher.Constraint('PointOnObject',iline1,EndPoint,icir)) 
# the Snell's law:
f.addConstraint(Sketcher.Constraint('SnellsLaw',iline1,EndPoint,iline2,StartPoint,icir,1.47))

App.ActiveDocument.recompute() 
```





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/fr
