---
- GuiCommand:
   Name:TechDraw FaceCenterLine
   Name/fr:TechDraw Ligne centrale à une face
   MenuLocation:TechDraw → Ajouter des lignes → Ajouter une ligne centrale à des faces
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Point cosmétique](TechDraw_CosmeticVertex/fr.md), [TechDrawAdd Ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md), [TechDraw Ligne centrale entre 2 sommets](TechDraw_2PointCenterLine/fr.md), [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)
---

# TechDraw FaceCenterLine/fr


</div>

## Description

L\'outil **TechDraw Ligne centrale à une face** ajoute une ligne médiane à une ou plusieurs faces.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Ligne centrale ajoutée a une face*


</div>

## Usage create 


<div class="mw-translate-fuzzy">

1.  Sélectionnez une ou plusieurs faces dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Ajouter une ligne centrale à des faces](TechDraw_FaceCenterLine/fr.md)**.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez spécifier les attributs de la nouvelle ligne centrale.
4.  Une ligne centrale sera ajoutée au milieu de la boîte englobante la ou les faces sélectionnées.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

N\'importe quel bouton de commande de ligne centrale (**<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 pointss](TechDraw_2PointCenterLine/fr.md)**) peut être utilisé pour éditer n\'importe quelle ligne centrale.


</div>


<div class="mw-translate-fuzzy">

1.  Sélectionnez une ligne centrale.
2.  Appuyez sur n'importe quel bouton de commande de ligne centrale.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez modifier les attributs de la ligne centrale.
4.  Appuyez sur **OK** pour voir vos modifications.


</div>




<div class="mw-translate-fuzzy">

## Propriétés


</div>


<div class="mw-translate-fuzzy">

1.  Mode (boutons radio):
    -   **Vertical** : force la ligne médiane à être verticale
    -   **Horizontal**: force la ligne médiane à être horizontale
    -   ***Aligned** : cette option n\'est pas possible pour la ligne médiane par rapport aux faces*
2.  **Shift Horiz** : déplace la ligne médiane à gauche ou à droite de sa position normale
3.  **Shift Vert** : déplace la ligne médiane de sa position normale vers le haut ou le bas
4.  **Rotation** : fait pivoter la ligne médiane autour de son centre (degrés. + Dans le sens antihoraire, - dans le sens horaire)
5.  **Extend** : allonge la ligne médiane de ce montant
6.  **Color** : couleur de la ligne médiane
7.  **Weight** : épaisseur de la ligne médiane
8.  **Style** : <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continu, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Tiret, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Point, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tiret Point, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Tiret Point Point


</div>



## Remarques


<div class="mw-translate-fuzzy">

-   Ligne centrale à une face remplacera éventuellement deux propriétés d\'affichage:
    -   
        {{PropertyView/fr|HorizCenterLine}}
        
        : affiche un trait d\'axe horizontal dans la vue.

    -   
        {{PropertyView/fr|VertCenterLine}}
        
        : affiche un trait d\'axe vertical dans la vue.


</div>

## Properties

Centerlines have no properties of their own, as they are not document objects.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/fr
