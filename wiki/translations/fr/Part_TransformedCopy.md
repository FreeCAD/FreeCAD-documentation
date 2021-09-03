---
- GuiCommand:/fr
   Name:Part TransformedCopy
   Name/fr:Part Copie transformée
   MenuLocation:Pièce → Créer une copie → Créer une copie modifiée
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Part Copie simple](Part_SimpleCopy/fr.md), [Part Copie élément](Part_ElementCopy/fr.md), [Part Affiner la forme](Part_RefineShape/fr.md)
---


</div>

## Description

[Part Copie transformée](Part_TransformedCopy/fr.md) produit une copie non paramétrique d\'un objet qui a été déplacé de sa position d\'origine.

Pour produire d'autres copies non paramétriques, utilisez **<img src="images/Part_SimpleCopy.svg" width=16px> [Part Créer une copie simple](Part_SimpleCopy/fr.md)**, **<img src="images/Part_ElementCopy.svg" width=16px>[Part Copie élément](Part_ElementCopy/fr.md)** ou **<img src="images/Part_RefineShape.svg" width=16px> [Part Affiner la forme](Part_RefineShape/fr.md)**.

## Utilisation

1.  Sélectionnez un objet que vous souhaitez copier.
2.  Aller au menu **Pièce → Créer une copie → <img src=images/Part_TransformedCopy.svg style="width:16px"> [Create transformed copy](Part_TransformedCopy/fr.md)**.

## Propriétés

### Données

La copie a une simple propriété {{PropertyData/fr|Placement}} comme n\'importe quel autre [Part Feature](Part_Feature/fr.md).

### Vue

La copie a des propriétés de vue simples comme toutes les autres [Part Feature](Part_Feature/fr.md).

## Script

La commande **Part Copie transformée** peut être appliquée après avoir sélectionné un ou plusieurs objets dans la [Vue en arborescence](Tree_view/fr.md):


```python
FreeCADGui.runCommand('Part_TransformedCopy')
```

La sélection peut être manuelle (en utilisant la souris) ou via la [Console Python](Python_console/fr.md).
Pour en savoir plus sur la sélection d\'objets de manière programmatique, reportez-vous à [Méthodes de sélection](Selection_methods/fr.md).


<div class="mw-translate-fuzzy">





</div>


 
