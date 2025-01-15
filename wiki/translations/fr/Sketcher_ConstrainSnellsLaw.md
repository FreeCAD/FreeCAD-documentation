---
 GuiCommand:
   Name: Sketcher ConstrainSnellsLaw
   Name/fr: Sketcher Contrainte de réfraction
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de réfraction 
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **W**
   Version: 0.15
---

# Sketcher ConstrainSnellsLaw/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Sketcher Contrainte de réfraction](Sketcher_ConstrainSnellsLaw/fr.md) contraint deux lignes à suivre la loi de réfraction de la lumière lorsqu\'elle pénètre à travers une interface où deux matériaux ayant des indices de réfraction différents se rencontrent. Voir [Loi de Snell](http://fr.wikipedia.org/wiki/Loi_de_Snell_Descartes).

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;"> 
*Loi de Snell*



## Utilisation

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*La séquence des clics est indiquée par des flèches jaunes avec des nombres, n1 et n2 indiquent où les indices de réfraction se trouvent.*

1.  Préparez deux lignes pour représenter un faisceau de lumière et une arête pour servir d\'interface. Les lignes doivent être situées de part et d\'autre de l\'interface. L\'interface peut être une [ligne](Sketcher_CreateLine/fr.md), un [arc](Sketcher_CompCreateArc/fr.md), un [cercle](Sketcher_CompCreateCircle/fr.md) ou un [conique](Sketcher_CompCreateConic/fr.md)
2.  Sélectionnez une extrémité de la première ligne, une extrémité de la deuxième ligne et l\'arête de l\'interface. Notez l\'ordre de sélection des extrémités.
3.  Il y a plusieurs façons de lancer l\'outil :
    -   Sélectionnez l\'outil **Esquisse → Contraintes de l'esquisse → <img src="images/Sketcher_ConstrainSnellsLaw.svg" width=16px> Contrainte de réfraction (loi de Snell)** du menu.
    -   Utilisez le raccourci clavier : **K** puis **W**.
4.  La fenêtre de dialogue **Rapport d'indice de réfraction** s\'ouvre.
5.  Saisissez le **Rapport n2/n1**, où **n2** correspond au milieu où se trouve la deuxième ligne sélectionnée et **n1** correspond au milieu de la première ligne.
6.  Une contrainte de la loi de Snell est ajoutée. Si nécessaire, les extrémités sont rendues [coïncidentes](Sketcher_ConstrainCoincident/fr.md) et contraintes [sur l\'interface](Sketcher_ConstrainPointOnObject/fr.md). Ces contraintes supplémentaires sont appelées [contraintes d\'aide](Sketcher_helper_constraint/fr.md).



## Remarques

-   La contrainte de la loi de Snell applique l\'équation de la loi simple n1\*sin(theta1) = n2\*sin(theta2). Elle a besoin que les extrémités des lignes coïncident et soient sur l\'interface par d\'autres contraintes, sinon le comportement n\'est pas défini. Les contraintes d\'aide nécessaires sont ajoutées automatiquement en fonction des coordonnées actuelles des éléments.
-   En Python, les contraintes d\'aide doivent être ajoutées manuellement (voir [Script](#Script.md)).
-   Ces contraintes peuvent être temporairement supprimées et les extrémités déplacées, ce qui peut être utile si l\'on veut construire un rayon réfléchi ou des rayons de biréfringence.
-   Contrairement à la réalité, les indices de réfraction sont associés aux rayons de lumière, mais pas en fonction des côtés de la frontière. Ceci est utile pour émuler la biréfringence, construire des trajectoires de différentes longueurs d\'onde dues à la réfraction, et construire facilement l\'angle d\'apparition de la réflexion interne totale.
-   Les deux rayons peuvent se trouver du même côté de l\'interface, satisfaisant ainsi à l\'équation de contrainte. Il s\'agit d\'un non-sens physique, sauf si le rapport n2/n1 est de 1,0, auquel cas la contrainte émule une réflexion.
-   Les arcs de cercle et les ellipses sont également acceptés comme des rayons. Mais c\'est également un non-sens physique.



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



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/fr
