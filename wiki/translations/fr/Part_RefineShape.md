---
 GuiCommand:
   Name: Part RefineShape
   Name/fr: Part Affiner la forme
   MenuLocation: Part , Créer une copie , Affiner la forme
   Workbenches: Part_Workbench/fr
   SeeAlso: 
---

# Part RefineShape/fr

## Description

La commande <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> **Part Affiner la forme** crée des copies paramétriques avec une forme affinée à partir d\'objets sélectionnés. Elle supprime les arêtes inutiles des faces planes et cylindriques.

![](images/PartRefineShape_it.png ) 
*L'objet original avec 11 faces (à gauche) et sa copie affinée avec 7 faces (à droite).*



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option **Part → Créer une copie → <img src="images/Part_RefineShape.svg" width=16px> Affiner la forme** du menu.
3.  Pour chaque objet, une copie paramétrique nettoyée est créée.
4.  Les objets originaux sont cachés.



## Remarques

-   Cette commande peut être utilisée comme dernière étape d\'un flux de travail traditionnel d\'une [géométrie solide constructive](constructive_solid_geometry/fr.md).
-   Elle peut aider à nettoyer le modèle avant d\'appliquer d\'autres fonctions, telles que des [congés](Part_Fillet/fr.md).
-   Le nettoyage d\'un objet peut empêcher les imprimantes 3D d\'imprimer des bords indésirables une fois que l\'objet est exporté dans un format de maillage.
-   Cette commande peut également être utilisée après avoir converti un maillage en une forme ([Part Forme à partir du maillage](Part_ShapeFromMesh/fr.md)).
-   Par défaut, cette commande crée des copies paramétriques (liées). Il existe un paramètre de [réglage fin](Fine-tuning/fr.md) pour passer à des copies non paramétriques. Plus d\'informations sur le comportement des copies paramétriques/non-paramétriques peuvent être trouvées dans ce [fil du forum](https://forum.freecad.org/viewtopic.php?t=42993).
-   Quelques informations intéressantes sur ce qui se passe avec le placement et comment y accéder par Python peuvent être trouvées dans ce [fil du forum](https://forum.freecad.org/viewtopic.php?t=77568#p675456).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Part RefineShape est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Refine}}

-    **Source|Link**: spécifie la forme source liée.



## Script

La commande Python pour affiner une forme est la suivante :


```python
shape.removeSplitter()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/fr
