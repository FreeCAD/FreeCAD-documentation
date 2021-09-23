---
- GuiCommand:/fr
   Name:TechDraw FaceCenterLine
   Name/fr:TechDraw Ligne centrale à une face
   MenuLocation:TechDraw → Ajouter des lignes → Ajouter une ligne centrale à des faces
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Point cosmétique](TechDraw_CosmeticVertex/fr.md), [TechDrawAdd Ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md), [TechDraw Ligne centrale entre 2 sommets](TechDraw_2PointCenterLine/fr.md), [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)
---

# TechDraw FaceCenterLine/fr

## Description

L\'outil FaceCenterLine ajoute une ligne médiane à une ou plusieurs faces.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Ligne centrale ajoutée a une face*

## Utilisation

1.  Sélectionnez une ou plusieurs faces dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Ajouter une ligne centrale à des faces](TechDraw_FaceCenterLine/fr.md)**.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez spécifier les attributs de la nouvelle ligne centrale.
4.  Une ligne centrale sera ajoutée au milieu de la boîte englobante la ou les faces sélectionnées.

Pour supprimer une ligne médiane, sélectionnez-la et utilisez le bouton de la barre d\'outils **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)**.

## Modification des lignes centrales 

N\'importe quel bouton de commande de ligne centrale (**<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 pointss](TechDraw_2PointCenterLine/fr.md)**) peut être utilisé pour éditer n\'importe quelle ligne centrale.

1.  Sélectionnez une ligne centrale.
2.  Appuyez sur n'importe quel bouton de commande de ligne centrale.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez modifier les attributs de la ligne centrale.
4.  Appuyez sur **OK** pour voir vos modifications.

## Propriétés

Les lignes centrales n\'ont pas de propriétés propres, car elles ne sont pas des objets de document. Elles possèdent des attributs qui peuvent être modifiés dans la boîte de dialogue d\'édition des lignes centrales.

1.  Mode (boutons radio):
    -   **Vertical**: force la ligne médiane à être verticale
    -   **Horizontal**: force la ligne médiane à être horizontale
    -   **Aligned**: cette option n\'est pas possible pour la ligne médiane par rapport aux faces\'\'
2.  **Shift Horiz**: déplace la ligne médiane à gauche ou à droite de sa position normale
3.  **Shift Vert**: déplace la ligne médiane de sa position normale vers le haut ou le bas
4.  **Rotation**: fait pivoter la ligne médiane autour de son centre (degrés. + Dans le sens antihoraire, - dans le sens horaire)
5.  **Extend**: allonge la ligne médiane de ce montant
6.  **Color**: couleur de la ligne médiane
7.  **Weight**: épaisseur de la ligne médiane
8.  **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continu, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Tiret, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Point, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tiret Point, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Tiret Point Point

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les lignes centrales ne sont pas accessibles à partir de [macro](Macros/fr.md) ou de la console [Python](Python/fr.md) pour le moment.

## Remarques

-   Ligne centrale à une face remplacera éventuellement deux propriétés d\'affichage:
    -   
        {{PropertyView/fr|HorizCenterLine}}
        
        : affiche un trait d\'axe horizontal dans la vue.

    -   
        {{PropertyView/fr|VertCenterLine}}
        
        : affiche un trait d\'axe vertical dans la vue.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/fr
