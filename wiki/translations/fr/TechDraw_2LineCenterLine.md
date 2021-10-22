---
- GuiCommand:/fr
   Name:TechDraw 2LineCenterLine
   Name/fr:TechDraw Ligne centrale entre 2 lignes
   MenuLocation:TechDraw → Ajouter des lignes → Ajouter une ligne centrale entre 2 lignes
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Ligne centrale à une surface](TechDraw_FaceCenterLine/fr.md), [TechDraw Ligne centrale entre 2 sommets](TechDraw_2PointCenterLine.md)
---

# TechDraw 2LineCenterLine/fr

## Description

L\'outil Ligne centrale entre 2 lignes ajoute une ligne centrale entre deux arêtes.

<img alt="" src=images/CL2LinesSample.png  style="width:350px;">



*Ligne centrale alignée entre 2 arêtes*

## Utilisation

1.  Sélectionnez 2 bords dans une vue. Les bords devraient être plus ou moins parallèles.
2.  Appuyez sur le bouton **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md)**.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez spécifier les attributs de la nouvelle ligne centrale.
4.  Une ligne centrale sera ajoutée entre les 2 arêtes sélectionnées. **Si la ligne générée semble étrange ou n\'est pas crée du tout, vous devrez peut-être utiliser l\'option** [**Flip Ends**](#Flip_Ends.md).

Pour supprimer une ligne centrale, sélectionnez-la et utilisez le bouton de la barre d\'outils **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)**.

## Modification des lignes centrales 

N\'importe quel bouton de commande de la ligne centrale ( **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Ajouter une ligne centrale à des faces](TechDraw_FaceCenterLine/fr.md)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> Ajouter une ligne centrale entre 2 lignes**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Ajouter une ligne centrale entre 2 points](TechDraw_2PointCenterLine/fr.md)**) peut être utilisé pour éditer n\'importe quelle ligne centrale.

1.  Sélectionnez une ligne centrale.
2.  Appuyez sur n'importe quel bouton de commande de ligne centrale.
3.  Une boîte de dialogue s\'ouvrira où vous pourrez modifier les attributs de la ligne centrale.
4.  Appuyez sur **OK** pour voir vos modifications.

## Propriétés

Les lignes centrales n\'ont pas de propriétés propres car elles ne sont pas des objets de document. Elles ont des attributs qui peuvent être modifiés via la boîte de dialogue.

-   **Orientation**:
    -   **Vertical**: force la ligne centrale à être verticale
    -   **Horizontal**: force la ligne centrale à être horizontale
    -   **Aligned**: fait suivre la direction générale du bord pour le centre de 2 bords
-   **Shift Horizontal**: déplace la ligne centrale à gauche ou à droite de sa position normale
-   **Shift Vertical**: déplace la ligne centrale de sa position normale vers le haut ou le bas
-   **Rotation**: Fait pivoter la ligne centrale autour de son centre (degrés. + Dans le sens antihoraire, - dans le sens horaire)
-   **Extend By**: allonger la ligne centrale de ce montant
-   **Color**: couleur de la ligne centrale
-   **Weight**: épaisseur de la ligne centrale
-   **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continu, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Tiret, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Point, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tiret Point, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Tiret Point Point
-   **Flip ends**: inverse les points de terminaison pour le cas comme décrit ci-dessous. (attribut supprimé avec FreeCAD 0.20)

## Flip Ends 

<img alt="Croquis de la construction de la ligne médiane" src=images/TD-CenterLineFlip.png  style="width:350px;"> La ligne centrale entre 2 lignes est tracée entre les points médians (m0 et m1) des lignes qui relient les extrémités des lignes sélectionnées (p0 et p1), voir l\'esquisse. Selon l\'ordre des points, il existe 2 possibilités pour tracer les lignes de connexion. L\'attribut **Flip Ends** inverse la façon dont les lignes de connexion sont dessinées. Dans FreeCAD 0.20, l\'ordre des points est automatiquement déterminé de sorte que l\'attribut **Flip Ends** n\'est plus nécessaire.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les lignes centrales ne sont pas accessibles à partir des [macros](Macros/fr.md) ou de la console [Python](Python/fr.md) pour le moment.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2LineCenterLine/fr
