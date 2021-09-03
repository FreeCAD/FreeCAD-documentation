---
- GuiCommand:/fr
   Name:Part ElementCopy
   Name/fr:Part Copie d'un élément
   MenuLocation:Pièce → Créer une copie → Create shape element copy
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Part Copie simple](Part_SimpleCopy/fr.md), [Part Copie transformée](Part_TransformedCopy/fr.md), [Part Affiner la forme](Part_RefineShape/fr.md)
---

## Description

[Part Copie d\'un élément](Part_ElementCopy/fr.md) produit une copie non paramétrique d\'un sous-élément d\'un objet particulier, c\'est-à-dire d\'un sommet, d\'une arête ou d\'une face.

Pour produire des copies non paramétriques complètes des objets, utilisez **<img src="images/Part_SimpleCopy.svg" width=16px> [Part Créer une copie simple](Part_SimpleCopy/fr.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px> [Part Créer une copie transformée](Part_TransformedCopy/fr.md)** ou **<img src="images/Part_RefineShape.svg" width=16px> [Part Affiner la forme](Part_RefineShape/fr.md)**

## Utilisation

1.  Sélectionnez un sommet, une arête ou une face d\'un objet pour lequel vous souhaitez effectuer une copie.
2.  Allez au menu **Pièce → Create a copy → <img src=images/Part_ElementCopy.svg style="width:16px"> [Create shape element copy](Part_ElementCopy/fr.md)**.

## Propriétés

### Données

La copie a une simple propriété {{PropertyData/fr|Placement}} comme n\'importe quel autre [Part Feature](Part_Feature/fr.md).

### Vue

La copie a des propriétés de vue comme toutes les autres [Part Features](Part_Feature/fr.md).

## Script

La commande **Part Copie d\'un élément** peut être appliquée après avoir sélectionné un ou plusieurs objets dans la [Vue en arborescence](Tree_view/fr.md):


```python
FreeCADGui.runCommand('Part_ElementCopy')
```

La sélection peut être manuelle (en utilisant la souris) ou via la [Console Python](Python_console/fr.md).
Pour en savoir plus sur la sélection d\'objets de manière programmatique, reportez-vous à [Méthodes de sélection](Selection_methods/fr.md).





 
