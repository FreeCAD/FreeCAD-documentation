---
 GuiCommand:
   Name: FreeGrid StorageGrid
   Name/fr: FreeGrid Grille de rangement
   MenuLocation: FreeeGrid , Storage grid
   Workbenches: FreeGrid_Workbench/fr
   Version: 
   SeeAlso: 
---

# FreeGrid StorageGrid/fr

## Description

L\'outil [FreeGrid Grille de rangement](FreeGrid_StorageGrid/fr.md) crée une grille de rangement.

Cet outil fait partie de l\'[atelier FreeGrid](FreeGrid_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/FreeGrid_StorageGrid.svg" width=16px> [Storage grid](FreeGrid_StorageGrid/fr.md)**.
    -   Sélectionnez l\'option **FreeGrid → <img src="images/FreeGrid_StorageGrid.svg" width=16px> Storage grid** du menu.
2.  Une grille de rangement est créée avec des propriétés basées sur les préférences en cours.
3.  Vous pouvez sélectionner l\'objet et modifier ses propriétés dans l\'[éditeur de propriétés](Property_editor/fr.md)



## Propriétés

Un objet FreeGrid StorageBox est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Grid features}}

-    **Corner Connectors|Bool**: par défaut `True`. Ajoute des cavités pour les connecteurs d\'angle.

-    **Extra Bottom Material|Length**: par défaut {{Value|16 mm}}. Épaisseur supplémentaire sous la grille.

-    **Is Subtractive|Bool**: par défaut `False`. Crée une grille adaptée à la fabrication soustractive.


{{Properties_Title|Magnet mount}}

-    **Include Magnets|Bool**: par défaut `True`. Inclut les réceptacles à aimants.

-    **Magnet Diameter|Length**: par défaut {{Value|6 mm}}. Diamètre des aimants.

-    **Magnet Height|Length**: par défaut {{Value|2 mm}}. Hauteur des aimants.


{{Properties_Title|Size}}

-    **Depth|IntegerConstraint**: par défaut {{Value|2}}. Nombre d\'unités de 50 mm dans la direction Y de l\'objet.

-    **Width|IntegerConstraint**: par défaut {{Value|3}}. Nombre d\'unités de 50 mm dans la direction X de l\'objet.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [FreeGrid](Category_FreeGrid.md) > FreeGrid StorageGrid/fr
