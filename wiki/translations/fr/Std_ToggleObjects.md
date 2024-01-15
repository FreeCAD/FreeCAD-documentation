---
 GuiCommand:
   Name: Std ToggleObjects
   Name/fr: Std Basculer tous les objets
   MenuLocation: Affichage , Visibilité , Activer/désactiver tous les objets
   Workbenches: Tous
   SeeAlso: Std_ToggleVisibility/fr, Std_ShowSelection/fr, Std_HideSelection/fr, Std_ShowObjects/fr, Std_HideObjects/fr
---

# Std ToggleObjects/fr

## Description

La commande **Std Basculer tous les objets** bascule la visibilité de tous les objets appartenant au document actif dans la [vue 3D](3D_view/fr.md). Soyez prudent lorsque vous utilisez cette commande car elle affichera également des sous-éléments du [PartDesign Corps](PartDesign_Body/fr.md) et des objets utilisés par les [Part Opérations booléennes](Part_Boolean/fr.md). Dans la plupart des cas, ceux-ci doivent rester invisibles.



## Utilisation

1.  Sélectionnez l\'option **Affichage → Visibilité → <img src="images/Std_ToggleObjects.svg" width=16px> Activer/désactiver tous les objets** du menu.



## Remarques

-   Les objets invisibles sont affichés avec une étiquette grisée et une icône grisée dans la [vue en arborescence](Tree_view/fr.md).
-   Les objets imbriqués dans un [Std Part](Std_Part/fr.md) ou un [Std Lien](Std_LinkMake/fr.md) vers un [Std Groupe](Std_Group/fr.md), ou un LinkGroup, et les [fonctions](PartDesign_Feature/fr.md) d\'un [PartDesign Corps](PartDesign_Body/fr.md) ne seront visibles dans les [vues 3D](3D_view/fr.md) que si leur parent est également visible. Cela signifie qu\'une fonction dans un PartDesign Corps qui est imbriquée dans une pièce standard ne sera visible dans les vues 3D que si la fonction elle-même, le PartDesign Corps et la pièce standard sont tous visibles. Et si la partie standard est à son tour imbriquée dans une autre partie standard, alors ce dernier objet doit également être visible.
-   Si la visibilité d\'un [Std Groupe](Std_Group/fr.md) (ou d\'un objet dérivé de celui-ci tel qu\'une [Arch Partie de bâtiment](Arch_BuildingPart/fr.md)) est modifiée, la visibilité de ses objets imbriqués changera en conséquence. Mais leur visibilité peut également être modifiée de manière indépendante.
-   L\'action de cette commande ne peut pas être annulée avec [Std Annuler](Std_Undo/fr.md).
-   La visibilité d\'un objet peut également être modifiée via sa propriété **Visibility** associée dans l\'[éditeur de propriétés](Property_editor/fr.md) ou la [vue combinée](Combo_view/fr.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour un exemple de script, voir [Std Basculer la visibilité](Std_ToggleVisibility/fr.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleObjects/fr
