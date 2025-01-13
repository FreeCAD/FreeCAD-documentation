---
 GuiCommand:
   Name: Std ShowSelection
   Name/fr: Std Afficher la sélection
   MenuLocation: Affichage , Visibilité , Afficher la sélection
   Workbenches: Tous
   SeeAlso: Std_ToggleVisibility/fr, Std_HideSelection/fr, Std_ToggleObjects/fr, Std_ShowObjects/fr, Std_HideObjects/fr
---

# Std ShowSelection/fr

## Description

La commande **Std Afficher la sélection** masque les objets sélectionnés dans la [Vues 3D](3D_view/fr.md).



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
    -   Les objets invisibles peuvent être sélectionnés dans la [vue en arborescence](Tree_view/fr.md).
    -   Soyez prudent lorsque vous utilisez **Ctrl**+**A** pour sélectionner tous les objets dans l\'arborescence. Cela sélectionnera également les sous-éléments du [PartDesign Corps](PartDesign_Body/fr.md) et les objets utilisés par les [Part Opérations booléennes](Part_Boolean/fr.md). Dans la plupart des cas, ceux-ci doivent rester invisibles.
    -   Les objets utilisés par les [Part Opérations booléennes](Part_Boolean/fr.md) sont également sélectionnés lorsque vous utilisez **Ctrl**+**A** dans une vue 3D.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Affichage → Visibilité → <img src="images/Std_ShowSelection.svg" width=16px> Afficher la sélection** du menu.
    -   Sélectionnez l\'option **<img src="images/Std_ShowSelection.svg" width=16px> Afficher la sélection** dans le menu contextuel de l\'arborescence.



## Remarques

Voir [Std Basculer la visibilité](Std_ToggleVisibility/fr#Remarques.md)



## Script

Voir [Std Basculer la visibilité](Std_ToggleVisibility/fr#Script.md)





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ShowSelection/fr
