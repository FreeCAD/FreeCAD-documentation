---
- GuiCommand:/fr
   Name:Part SimpleCopy‏‎
   Name/fr:Part Copie simple
   MenuLocation:Pièce → Créer une copie → Créer une copie simple
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Std Copie](Std_Copy/fr.md), [Std Dupliquer la Sélection](Std_DuplicateSelection/fr.md), [Part Copie transformée](Part_TransformedCopy/fr.md), [Part Copie de l’élément](Part_ElementCopy/fr.md), [Part Affiner la forme](Part_RefineShape/fr.md)
---


</div>

## Description


**![](images/)_[Part_Copie_simple](Part_SimpleCopy‎/fr.md)**

génère une copie sans l\'historique paramétrique. Les étapes et opérations nécessaires à sa création ne sont plus accessibles.

**Alternativement**, pour produire d\'autres copies non-paramétriques utilisez <img alt="" src=images/Part_TransformedCopy.svg  style="width:16px;"> [Part Copie transformée](Part_TransformedCopy/fr.md), <img alt="" src=images/Part_ElementCopy.svg  style="width:16px;"> [Part Copie élément](Part_ElementCopy/fr.md) et <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Part Affiner la forme](Part_RefineShape/fr.md)

## Utilisation

1.  Sélectionnez un objet pour lequel vous souhaitez faire une copie.
2.  Aller au menu **Part → Create a copy → ![](images/)__[Créer_une_simple_copie](Part_SimpleCopy/fr.md)**.

## Propriétés

### Données

La copie a une seule propriété {{PropertyData/fr|Placement}} comme n\'importe quel autre [objet Part](Part_Feature/fr.md).

### Vue

La copie a des propriétés de vue simples comme toutes les autres [Objet Part](Part_Feature/fr.md).

## Script

La commande **Part Copie simple** peut être appliquée après avoir sélectionné un ou plusieurs objets dans la [Vue en arborescence](Tree_view/fr.md):


```python
FreeCADGui.runCommand('Part_SimpleCopy')
```

La sélection peut être manuelle (en utilisant la souris) ou via la [Console Python](Python_console/fr.md).
Pour en savoir plus sur la sélection d\'objets de manière programmatique, reportez-vous à [Méthodes de sélection](Selection_methods/fr.md).


<div class="mw-translate-fuzzy">





</div>


  
