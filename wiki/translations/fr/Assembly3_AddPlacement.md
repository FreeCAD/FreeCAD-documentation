---
- GuiCommand:/fr
   Name:Assembly3 AddPlacement
   Name/fr:Assembly3 Ajoutez un emplacement
   Icon:Assembly_Add_Placement.svg‎‎
   MenuLocation:Assembly3 → Workplane and origin → Add placement
   Workbenches:[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 AddPlacement/fr

## Description

La commande <img alt="" src=images/Assembly_Add_Placement.svg  style="width:24px;"> [Add placement](Assembly3_AddPlacement/fr.md) ajoute un placement à un assemblage actif.

Un objet Placement sera créé dans le conteneur Parts de l\'arbre d\'assemblage et un élément de placement associé sera placé dans la vue 3D. Il est placé à l\'origine de l\'assemblage et hérite de l\'orientation du système de coordonnées local de l\'assemblage, si l\'objet Assembly a été sélectionné directement.

<img alt="" src=images/Assembly3_AddPlacement-01.png  style="width:250px;"> <img alt="" src=images/Assembly3_AddPlacement-02.png  style="width:350px;"> 
*À gauche : Vue de l'arborescence. À droite : Un placement près de l'origine de l'assemblage (indiqué ici comme origine du fichier)*

L\'assemblage peut également être sélectionné indirectement par un élément appartenant à l\'assemblage. Le placement est alors placé à l\'origine de l\'élément et hérite de l\'orientation du système de coordonnées local de cet élément.

Les éléments valides sont par exemple des éléments, des corps, des sommets, des arêtes, des faces, des origines, des plans de travail et d\'autres placements provenant de la [Vue en arborescence](Tree_view/fr.md) ou de la [Vue 3D](3D_view/fr.md).

## Utilisation

1.  Activez la commande <img alt="" src=images/Assembly_Add_Placement.svg  style="width:16px;"> **Ajoutez un emplacement** en utilisant l\'une des commandes suivantes :
    -   Le bouton **<img src="images/Assembly_Add_Placement.svg_" width=16px> [Add placement](Assembly3_AddPlacement/fr.md)**.
    -   L\'option de menu **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_Placement.svg_" width=16px> Add placement**.



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 AddPlacement/fr
