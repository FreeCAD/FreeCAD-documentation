---
- GuiCommand:/fr
   Name:TechDraw 2LineCenterLine
   Name/fr:TechDraw Ligne centrale entre 2 points
   MenuLocation:TechDraw → Ajouter des lignes → Ajouter une ligne centrale entre 2 points
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Ligne centrale à une face](TechDraw_FaceCenterLine/fr.md), [TechDraw Ligne centrale entre 2 arêtes](TechDraw_2LineCenterLine/fr.md)
---

# TechDraw 2PointCenterLine/fr

## Description

L\'outil Ligne centrale entre 2 points ajoute une ligne centrale entre deux sommets (points).

<img alt="" src=images/CL2PointsSample.png  style="width:200px;">



*Ligne centrale entre 2 points*

## Utilisation

1.  Sélectionnez 2 sommets dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 points](TechDraw_2PointCenterLine/fr.md)**.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez spécifier les attributs de la nouvelle ligne centrale.
4.  Une ligne centrale sera ajoutée entre les 2 sommets sélectionnés.

Pour supprimer une ligne centrale, sélectionnez-la et utilisez le bouton de la barre d\'outils **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)**.

## Modification des lignes centrales 

N\'importe quel bouton de commande de la ligne centrale (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Ajouter une ligne centrale à des faces](TechDraw_FaceCenterLine/fr.md)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> Ajouter une ligne centrale entre 2 points**) peut être utilisé pour éditer n\'importe quelle ligne centrale.

1.  Sélectionnez une ligne centrale.
2.  Appuyez sur n'importe quel bouton de commande de ligne centrale.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez modifier les attributs de la ligne centrale.
4.  Appuyez sur **OK** pour voir vos modifications.

## Propriétés

Les lignes centrales n\'ont pas de propriétés propres car elles ne sont pas des objets de document. Elles ont des attributs qui peuvent être modifiés.

1.  Mode (boutons radio) :
    -   **Vertical** : force la ligne à être verticale
    -   **Horizontal** : force la ligne à être horizontale
    -   **Aligned** : fait suivre la direction générale du bord pour la ligne centrale à 2 bords
2.  **Shift Horiz** : déplace la ligne centrale à gauche ou à droite de sa position normale
3.  **Shift Vert** : déplace la ligne centrale de sa position normale vers le haut ou le bas
4.  **Rotation** : fait pivoter la ligne centrale autour de son centre (degrés. + Dans le sens antihoraire, - dans le sens horaire)
5.  **Extend** : allonge la ligne centrale de la valeur
6.  **Color** : permet de coloriser la ligne centrale
7.  **Weight** : spécifie l\'épaisseur de la ligne centrale
8.  \'\'\'Style : <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continu, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Tiret, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Point, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tiret Point, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Tiret Point Point

## Script


**Voir aussi :**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les lignes centrales ne sont pas accessibles à partir des [macros](Macros/fr.md) ou de la console [Python](Python/fr.md) pour le moment.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCenterLine/fr
