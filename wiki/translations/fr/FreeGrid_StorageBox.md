---
 GuiCommand:
   Name: FreeGrid StorageBox
   Name/fr: FreeGrid Boîte de rangement
   MenuLocation: FreeeGrid , Storage box
   Workbenches: FreeGrid_Workbench/fr
   Version: 
   SeeAlso: 
---

# FreeGrid StorageBox/fr

## Description

L\'outil [FreeGrid Boîte de rangement](FreeGrid_StorageBox/fr.md) crée une boîte de rangement.

Cet outil fait partie de l\'[atelier FreeGrid](FreeGrid_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/FreeGrid_StorageBox.svg" width=16px> [Storage box](FreeGrid_StorageBox/fr.md)**.
    -   Sélectionnez l\'option **FreeGrid → <img src="images/FreeGrid_StorageBox.svg" width=16px> Storage box** du menu.
2.  Une boîte de rangement est créée avec des propriétés basées sur les préférences en cours.
3.  Vous pouvez sélectionner l\'objet et modifier ses propriétés dans l\'[éditeur de propriétés](Property_editor/fr.md)



## Propriétés

Un objet FreeGrid StorageBox est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Box features}}

-    **Box Grip|Bool**: par défaut `True`. Ajoute une zone pour une poignée/étiquette à l\'arrière de la boîte.

-    **Box Grip Depth|Length**: défaut {{Value|15 mm}}. Profondeur de la poignée.

-    **Box Open Front|Bool**: par défaut `False`. Permet de laisser l\'avant de la boîte ouvert.

-    **Box Ramp|Bool**: par défaut `True`. Ajoute une rampe à l\'intérieur de l\'avant de la boîte.

-    **Floor Support|Bool**: par défaut `True`. Ajoute un support pour le fond.


{{Properties_Title|Internal divisions}}

-    **Hauteur de division|Percent**: par défaut {{Value|100}}. Hauteur des divisions internes par rapport à la hauteur de la boîte.

-    **Divisions X|IntegerConstraint**: par défaut {{Value|1}}. Nombre de divisions le long de l\'axe X.

-    **Divisions Y|IntegerConstraint**: par défaut {{Value|1}}. Nombre de divisions le long de l\'axe Y.


{{Properties_Title|Magnet mount}}

-    **Magnet Diameter|Length**: par défaut {{Value|6 mm}}. Diamètre des aimants.

-    **Magnet Height|Length**: par défaut {{Value|2 mm}}. Hauteur des aimants.

-    **Magnet Option|Enumeration**: par défaut {{Value|allIntersections}}. Positions des aimants. Les autres options sont {{Value|cornersOny}} et {{Value|noMagnets}}.


{{Properties_Title|Position on grid}}

-    **Position X|IntegerConstraint**: par défautt {{Value|0}}. Position de l\'objet sur la grille le long de l\'axe X. Commence à zéro.

-    **Position Y|IntegerConstraint**: par défaut {{Value|0}}. Position de l\'objet sur la grille le long de l\'axe Y. Commence à zéro.


{{Properties_Title|Size}}

-    **Depth|IntegerConstraint**: par défaut {{Value|1}}. Nombre d\'unités de 50 mm dans la direction Y de l\'objet.

-    **Height|Length**: par défaut {{Value|50 mm}}. Hauteur de l\'objet.

-    **Width|IntegerConstraint**: par défaut {{Value|1}}. Nombre d\'unités de 50 mm dans la direction X de l\'objet.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [FreeGrid](Category_FreeGrid.md) > FreeGrid StorageBox/fr
