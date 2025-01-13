---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/fr: Sketcher Arc d'ellipse
   MenuLocation: Esquisse , Géométries d'esquisse , Créer un arc d'ellipse
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/fr
---

# Sketcher CreateArcOfEllipse/fr



## Description

L\'outil <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:24px;"> [Sketcher Arc d\'ellipse](Sketcher_CreateArcOfEllipse/fr.md) crée un arc d\'ellipse.

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Arc d'ellipse (en blanc) avec géométrie interne (en jaune foncé)*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> [Arc d'ellipse par son centre, son rayon, des extrémités](Sketcher_CreateArcOfEllipse/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> Créer un arc d'ellipse** du menu.
    -   Utilisez le raccourci clavier : **G** puis **E**, puis **A**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  Choisissez le centre de l\'arc.
4.  Choisissez un point d\'extrémité de l\'un des axes de l\'arc, ce qui définit également l\'un de ses rayons.
5.  Choisissez le point de départ de l\'arc, qui définit également l\'autre rayon de l\'arc.
6.  Choisissez le point d\'arrivée de l\'arc.
7.  L\'arc d\'ellipse est créé, y compris un ensemble de géométrie interne (grand axe, petit axe et deux foyers).
8.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des arcs d\'ellipse.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Les éléments de la géométrie interne peuvent être supprimés. Ils peuvent être recréés à tout moment avec [Sketcher Géométrie interne d\'alignement](Sketcher_RestoreInternalAlignmentGeometry/fr.md).
-   Une fois créé, les axes majeurs et mineurs d\'un arc ou d\'une ellipse sont figés et ne peuvent plus être redimensionnés. Ceci est une conséquence de la paramétrisation du solveur et du même comportement strict d\'[OpenCASCADE](OpenCASCADE/fr.md). Un arc d\'ellipse doit être tourné pour intervertir ses axes.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/fr
