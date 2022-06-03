---
- GuiCommand   */fr
   Name   *Std ShowObjects
   Name/fr   *Std Afficher tous les objets
   MenuLocation   *Affichage → Visibilité → Afficher tous les objets
   Workbenches   *Tous
   SeeAlso   *[Std Basculer visibilité](Std_ToggleVisibility/fr.md), [Std Afficher la sélection](Std_ShowSelection/fr.md), [Std Masquer la sélection](Std_HideSelection/fr.md), [Std Basculer tous les objets](Std_ToggleObjects/fr.md), [Std Masquer tous les objets](Std_HideObjects/fr.md)
---

# Std ShowObjects/fr

## Description

La commande **Std Afficher les objets** affiche tous les objets appartenant au document actif dans la [vue 3D](3D_view/fr.md). Soyez prudent lorsque vous utilisez cette commande car elle affichera également des sous-éléments du [PartDesign Corps](PartDesign_Body/fr.md) et des objets utilisés par les [Part Opérations booléennes](Part_Boolean/fr.md). Dans la plupart des cas, ceux-ci doivent rester invisibles.

## Utilisation

1.  Sélectionnez l\'option **Affichage → Visibilité → <img src="images/Std_ShowObjects.svg" width=16px> Afficher tous les objets** dans le menu.

## Remarques

-   L\'action de cette commande ne peut pas être annulée avec [Std Annuler](Std_Undo/fr.md).
-   La visibilité d\'un objet peut également être modifiée via sa propriété {{PropertyData/fr|Visibility}} associée dans l\'[Éditeur de propriétés](Property_editor/fr.md) ou la [Vue Combinée](Combo_view/fr.md).

## Script


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour un exemple de script, voir [Std Basculer la visibilité](Std_ToggleVisibility/fr.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ShowObjects/fr
