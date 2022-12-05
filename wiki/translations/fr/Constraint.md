# Constraint/fr
## Introduction


{{TOCright}}

Dans FreeCAD, le mot \"[Contrainte](Constraint/fr.md)\" est normalement utilisé pour désigner une \"règle\" pour dessiner des formes géométriques à l\'intérieur d\'une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Esquisse](Sketch/fr.md) (classe `Sketcher::SketchObject`). Une contrainte limite la position d\'un certain élément géométrique de différentes manières, par exemple, elle peut spécifier si l\'élément est horizontal, vertical, tangent, parallèle, perpendiculaire, coïncidant avec un point, concentrique à un autre objet, etc.

Il existe deux principaux types de contraintes:

-    **Geometric constraints**définit les caractéristiques des formes sans spécifier les dimensions exactes, par exemple, l\'horizontalité, la verticalité, le parallélisme, la perpendicularité et la tangence.

-    **Datum constraints**ou **dimensional constraints** définissent les caractéristiques des formes en spécifiant les dimensions, par exemple, une longueur numérique ou un angle.

Reportez-vous aux informations dans l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md) pour une liste de toutes les contraintes qui peuvent être appliquées. Certains d\'entre eux s\'appliquent aux lignes, certains aux courbes et certains aux sommets. Voir aussi le [tutoriel de base sur les croquis](Basic_Sketcher_Tutorial/fr.md).

## Utilisation

1.  Créez une esquisse depuis l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md) ou via l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).
2.  Presse
    -   
        **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)**
        
        , ou

    -   
        **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**
        
        suivi de **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse ](PartDesign_NewSketch/fr.md)**.
3.  Double-cliquez sur l\'esquisse créée pour entrer dans son mode d\'édition.
4.  Dessinez une série de lignes en utilisant **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Polyligne](Sketcher_CreatePolyline/fr.md)**.
5.  Choisissez l\'une des lignes et utilisez **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Contrainte verticale](Sketcher_ConstrainVertical/fr.md)**.
6.  Choisissez l\'une des lignes et utilisez **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md)**.
7.  Choisissez la ligne verticale et utilisez **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Contrainte distance Y](Sketcher_ConstrainDistanceY/fr.md)**; attribuer une distance.
8.  Choisissez la ligne horizontale et utilisez **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Contrainte distance X](Sketcher_ConstrainDistanceX/fr.md)**; attribuer une distance.

## Remarques

-   Les contraintes sont utiles pour créer des profils très précis qui peuvent être transformés en extrusions solides en utilisant le **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)** ou **[<img src=images/Part_Extrude.svg style="width:16px"> [Part Extrusion](Part_Extrude/fr.md)** opérations.
-   Les contraintes ne sont utilisées que dans les [Esquisses](Sketch/fr.md); d\'autres objets 2D tels que ceux créés avec l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) ne comprennent pas de contraintes; ces derniers sont simplement placés dans l\'espace 3D et leurs propriétés définissent leur forme et leur position.


{{Sketcher Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Sketcher](Category_Sketcher.md) > Constraint/fr
