---
- GuiCommand:
   Name: Sketcher CreateEllipseBy3Points
   Name/fr: Sketcher Ellipse par 3 points
   MenuLocation: Esquisse - Géométries d'esquisse - Créer une ellipse via 3 points
   Workbenches: [Sketcher](Sketcher_Workbench/fr.md)
   Shortcut: **G** **3** **E**
   Version: 0.15
   SeeAlso: [Sketcher Ellipse par son centre](Sketcher_CreateEllipseByCenter/fr.md), [Sketcher Cercle](Sketcher_CreateCircle/fr.md), [Sketcher Arc d'ellipse](Sketcher_CreateArcOfEllipse/fr.md)
---

# Sketcher CreateEllipseBy3Points/fr

## Description

Cet outil trace une ellipse à partir de trois points : (1) la périapside (premier croisement du plus grand diamètre avec l\'ellipse), (2) l\'apoapside (le second croisement du plus grand diamètre avec l\'ellipse), (3) un point du côté du plus grand diamètres plus long (a) définissant le rayon mineur (b). (c) est le centre résultant et (f) sont les points focaux.

Lors du lancement de l\'outil, le pointeur de la souris change pour une croix blanche avec une icône représentant une ellipse rouge.

![](images/Ellipse_3Point.png‎ ) 
*La séquence de clics est indiquée par des flèches jaunes numérotées.<br>
1 est la périapside, 2 l'apoapside, 3 définit le point du diamètre mineur<br>
Les lignes vertes sont les diamètres majeur et mineur.<br>
Les lignes bleues sont des lignes de construction aléatoires à des fins d'illustration.*



## Utilisation

-   Appuyer sur le bouton **[<img src=images/Sketcher_CreateEllipseBy3Points.svg style="width:16px"> [Créer une ellipse via 3 points](Sketcher_CreateEllipseBy3Points/fr.md)**.
-   Cliquer d\'abord dans la vue 3D pour définir un point de croisement du diamètre majeur avec l\'ellipse (périapside). Le second point dans la vue 3D définit le croisement avec l\'ellipse opposé au centre (apoapside). Le troisième clic définit un point sur l\'ellipse définissant le rayon mineur.

-   Après le troisième clic, l\'ellipse est créée, ainsi qu\'un ensemble de géométrie de construction alignée sur l\'ellipse (diamètres majeur et intérieur, 2 points focaux). La géométrie de construction peut être supprimée manuellement si non requise, et recréée plus tard. Consultez [afficher/basculer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md).
-   Appuyer sur **Echap** ou un clic droit sur la souris annule la fonction.



## Particularités

-   Les axes majeur et mineur de l\'ellipse sont stricts et ne peuvent pas être échangés en redimensionnant l\'ellipse. Il s\'agit d\'une conséquence de la paramétrisation utilisée par le solveur (centre (x,y), focus1 (x,y) et rayon mineur (b)) et le comportement strict d\'Open Cascade. L\'ellipse doit être pivotée pour échanger les axes.
-   L\'ellipse peut faire office de cercle si les axes de diamètre majeur et mineur sont supprimés, et qu\'un des points focaux est contraint pour coïncider avec le centre. Toutefois, la contrainte radiale ne fonctionnera pas.
-   Le déplacement de l\'ellipse par son pourtour a le même effet que par son centre.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseBy3Points/fr
