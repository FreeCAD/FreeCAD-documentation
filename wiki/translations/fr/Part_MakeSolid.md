---
 GuiCommand:
   Name: Part MakeSolid
   Name/fr: Part Convertir en solid‏‎e
   MenuLocation: Part , Convertir en solide
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_ShapeFromMesh/fr
---

# Part MakeSolid/fr

## Description

La commande <img alt="" src=images/Part_MakeSolid.svg  style="width:24px;"> **Part Convertir en solid‏‎e** crée des solides à partir d\'objets forme.

Cette commande est généralement utilisée comme l\'une des étapes de la création d\'un solide à partir d\'un maillage. Voir [Part Forme à partir d\'un maillage](Part_ShapeFromMesh/fr#Utilisation.md) pour plus d\'informations.



## Utilisation

1.  Sélectionnez un ou plusieurs objets de forme.
2.  Choisissez l\'option **Part → <img src="images/Part_MakeSolid.svg" width=16px> Convertir en solide** du menu.
3.  Pour chaque objet sélectionné, un solide est créé en tant que nouvel objet distinct.



## Remarques

-   Les objets forme sélectionnés n\'ont pas été analysés ou validés.
-   Il est recommandé d\'utiliser [Part Affiner la forme](Part_RefineShape/fr.md) avant de convertir en solide.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Les objets créés sont des objets [Part Feature](Part_Feature/fr.md) sans propriétés supplémentaires.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part MakeSolid/fr
