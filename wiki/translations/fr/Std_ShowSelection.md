---
- GuiCommand   */fr
   Name   *Std ShowSelection
   Name/fr   *Std Afficher la sélection
   MenuLocation   *Affichage → Visibilité → Afficher la sélection
   Workbenches   *Tous
   SeeAlso   *[Std Basculer la visibilité](Std_ToggleVisibility/fr.md), [Std Masquer la sélection](Std_HideSelection/fr.md), [Std Basculer tous les objets](Std_ToggleObjects/fr.md), [Std Afficher tous les objets](Std_ShowObjects/fr.md), [Std Masquer tous les objets](Std_HideObjects/fr.md)
---

# Std ShowSelection/fr

## Description

La commande **Std Afficher la sélection** masque les objets sélectionnés dans la [Vues 3D](3D_view/fr.md).

## Utilisation

1.  Sélectionnez un ou plusieurs objets.
    -   Les objets invisibles peuvent être sélectionnés dans la [vue en arborescence](Tree_view/fr.md).
    -   Soyez prudent lorsque vous utilisez **Ctrl**+**A** pour sélectionner tous les objets dans l\'arborescence. Cela sélectionnera également les sous-éléments du [PartDesign Corps](PartDesign_Body/fr.md) et les objets utilisés par les [Part Opérations booléennes](Part_Boolean/fr.md). Dans la plupart des cas, ceux-ci doivent rester invisibles.
    -   Les objets utilisés par les [Part Opérations booléennes](Part_Boolean/fr.md) sont également sélectionnés lorsque vous utilisez **Ctrl**+**A** dans une vue 3D.
2.  Il existe plusieurs façons d\'appeler la commande   *
    -   Sélectionnez l\'option **Affichage → Visibilité → <img src="images/Std_ShowSelection.svg" width=16px> Afficher la sélection** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_ShowSelection.svg" width=16px> Afficher la sélection** dans le menu contextuel de l\'arborescence. Cette option n\'est pas disponible dans l\'[atelier PartDesign](PartDesign_Workbench/fr.md).

## Remarques

-   Les objets invisibles sont affichés avec une étiquette grisée et une icône grisée dans la [Vue en arborescence](Tree_view/fr.md).
-   Les objets imbriqués dans un [Std Part](Std_Part/fr.md) ou un [Std Lien](Std_LinkMake/fr.md) vers un [Std Groupe](Std_Group/fr.md), ou un LinkGroup, et les [Fonctionnalité](PartDesign_Feature/fr.md) d\'un [PartDesign Corps](PartDesign_Body/fr.md) ne seront visibles dans les [Vues 3D](3D_view/fr.md) que si leur parent est également visible. Cela signifie qu\'une caractéristique dans un PartDesign Corps qui est imbriquée dans une pièce standard ne sera visible dans les vues 3D que si la caractéristique elle-même, le PartDesign Corps et la pièce standard sont tous visibles. Et si la partie standard est à son tour imbriquée dans une autre partie standard, alors ce dernier objet doit également être visible.
-   Si la visibilité d\'un [Std Groupe](Std_Group/fr.md) (ou d\'un objet dérivé de celui-ci tel qu\'une [Arch Partie de bâtiment](Arch_BuildingPart/fr.md)) est modifiée, la visibilité de ses objets imbriqués changera en conséquence. Mais leur visibilité peut également être modifiée de manière indépendante.
-   L\'action de cette commande ne peut pas être annulée avec [Std Annuler](Std_Undo/fr.md).
-   La visibilité d\'un objet peut également être modifiée via sa propriété {{PropertyData/fr|Visibility}} associée dans l\'[Éditeur de propriétés](Property_editor/fr.md) ou la [Vue Combinée](Combo_view/fr.md).

## Script


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour un exemple de script, voir [Std Basculer la visibilité](Std_ToggleVisibility/fr.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ShowSelection/fr
