---
- GuiCommand:
   Name:Arch MultiMaterial
   Name/fr:Arch Matériaux multiples
   MenuLocation:Arch - Outils pour les matériaux - Matériaux multiples
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Arch Matériau](Arch_SetMaterial/fr.md), [Arch Outils matériaux](Arch_CompSetMaterial/fr.md)
---

# Arch MultiMaterial/fr

## Description

L\'outil Matériaux multiples définit une liste de [materiaux](Material/fr.md) avec, pour chaque matériau, un nom et une valeur d\'épaisseur. Cette liste multi-matériaux peut ensuite être ajoutée à un objet [Arch](Arch_Workbench/fr.md) à la place d\'un seul [Arch Matériau](Arch_SetMaterial/fr.md).

![](images/Arch_multimaterial_example.png )

Tous les objets Arch ne peuvent pas actuellement utiliser des matériaux multiples, et l\'utilisation qu\'ils en font diffère. Actuellement:

-   <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Mur](Arch_Wall/fr.md) avec des matériaux multiples utilisera les définitions de matériaux et les épaisseurs pour créer un mur multicouche
-   <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Fenêtre](Arch_Window/fr.md) avec des matériaux multiples va attribuer des matériaux avec un nom donné défini dans le Multi-Matériau aux composants de fenêtre avec un même nom ou type (voir ci-dessous). L\'épaisseur du matériau n\'est pas prise en compte.
-   <img alt="" src=images/Arch_Panel.svg  style="width:24px;"> [Arch Panneaux](Arch_Panel/fr.md) avec des matériaux multiples utilisera les définitions et les épaisseurs de matériaux pour créer un panneau multicouche.



## Utilisation

1.  Créez d\'abord une série de **<img src="images/Arch_SetMaterial.svg" width=16px> [Arch Matériaux](Arch_SetMaterial/fr.md)** dont vous aurez besoin dans vos matériaux multiples.
2.  Sélectionnez un objet Arch que vous souhaitez attribuer aux nouveaux matériaux multiples.
3.  Appuyez sur le bouton **<img src="images/Arch_MultiMaterial.svg" width=16px> [Matériaux multiples](Arch_MultiMaterial/fr.md)**.
4.  Définir les couches de matériaux souhaitées.

## Options

![](images/Arch_multimaterial_panel.png )

Lors de la création ou de l\'édition d\'un Matériaux multiples en double-cliquant dessus dans l\'arborescence, les options suivantes sont disponibles:

-   **Dupliquer** un autre Matériaux multiples existant du même document. Cela ne fait que copier les valeurs et ne lie en aucun cas les deux multi-matériaux.
-   Le champ **Nom** définira également l\'étiquette de l\'objet matériau
-   La liste **Composition** est la liste des différentes couches de matériaux qui composent ce multi-matériaux. Chaque couche a un nom, un matériau et une valeur d\'épaisseur.
-   Cliquez sur **Ajouter** pour ajouter un nouveau calque, **Haut** pour déplacer un calque sélectionné vers le haut, **Bas** pour déplacer un calque sélectionné vers le bas ou **Sup** pour supprimer un calque sélectionné.
-   Double-cliquez sur le **nom** d\'un calque pour le modifier; le matériau vous proposera une liste déroulante des [Arch Matériaux](Arch_SetMaterial/fr.md) disponibles dans le même document, et l\'épaisseur peut être définie à n\'importe quelle valeur dans n\'importe quelle unité
-   Les champs Nom et Matériau sont obligatoires. L\'épaisseur peut être laissée vide (elle prendra alors une valeur de 0).
-   Lorsqu\'un multi-matériaux contient des couches d\'épaisseur nulle, cette épaisseur est considérée comme variable. Les objets d\'Arch qui utilisent le multi-matériaux, tels que les murs et les panneaux, traiteront cela en conséquence, et donneront à cette couche l\'espace restant disponible compte tenu de sa propre largeur ou épaisseur.
-   Si vous nommez les différents composants d\'un \"Cadre\" multi-matériaux, \"Panneau plein\", \"Panneau de verre\" ou \"Louvre\" et appliquez ce matériau à une fenêtre, les matériaux donnés seront appliqués aux composants de fenêtre correspondants.



## Relation avec IFC 

Cela correspond à peu près à une combinaison de [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) et [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).

## Limitations



## Script



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MultiMaterial/fr
