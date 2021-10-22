---
- GuiCommand:/fr
   Name:Std UserEditMode
   Name/fr:Std Mode d'édition
   MenuLocation:Edition → Mode d'édition → ...
   Workbenches:Tous
   Version:0.20
   SeeAlso:[Std Bascule mode édition](Std_Edit/fr.md)
---

# Std UserEditMode/fr

## Description

La commande **Std Bascule mode édition** définit le mode d\'édition à utiliser lorsqu\'un objet est double-cliqué dans la [Vue en arborescence](Tree_view/fr.md).

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Cliquez sur la flèche noire descendante à droite du bouton **<img src="images/Std_UserEditModeDefault.svg" width=16px> [Mode d'édition](Std_UserEditMode/fr.md)** et sélectionnez un mode d\'édition dans le menu déroulant. Remarque : l\'image du bouton change en fonction de l\'option sélectionnée.
    -   Dans le menu, allez à **Affichage → Mode d'édition** et sélectionnez un mode d\'édition.

## Modes d\'édition disponibles 

### <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> Défault 

L\'objet sera édité en utilisant son mode par défaut. Ce mode d\'édition est défini en interne pour être le plus approprié au type d\'objet. Par exemple, ce sera l\'édition des propriétés de forme pour des [Part Primitives](Part_Primitives/fr.md) et des [PartDesign Fonctionnalités](PartDesign_Feature/fr.md), l\'édition du placement pour des [Part Booléens](Part_Boolean.md) etc\...

### <img alt="" src=images/Std_UserEditModeTransform.svg  style="width:24px;"> Transformer 

L\'objet aura son placement modifiable avec la commande [Std Transformation manipulation](Std_TransformManip/fr.md).

### <img alt="" src=images/Std_UserEditModeCutting.svg  style="width:24px;"> Coupe 

Ce mode d\'édition est implémenté comme étant disponible mais ne semble pas actuellement être utilisé par aucun objet.

### <img alt="" src=images/Std_UserEditModeColor.svg  style="width:24px;"> Couleur 

L\'objet aura la couleur de ses faces indépendantes modifiables avec la commande [Part Définir les couleurs](Part_FaceColors/fr.md).

## Remarques

-   Tous les objets ne supportent pas tous les modes d\'édition. Si le mode sélectionné n\'est pas supporté par l\'objet, son mode d\'édition par défaut sera utilisé à la place.

## Préférences

-   Le dernier mode d\'édition est mémorisé : **Outils → Editer paramètres... → BaseApp → Preferences → General → UserEditMode**. Il s\'agit d\'une valeur entière. Les valeurs possibles sont {{Incode|0}} (Par défaut), {{Incode|1}} (Transformation), {{Incode|2}} (Coupe) ou {{Incode|3}} (Couleur). La valeur par défaut est {{Incode|0}}.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour répertorier les modes d\'édition disponibles :


```python
import FreeCADGui
FreeCADGui.listUserEditModes()
```

Pour obtenir le mode d\'édition actif :


```python
import FreeCADGui
FreeCADGui.getUserEditMode()
```

Pour définir le mode d\'édition actif :


```python
import FreeCADGui
FreeCADGui.setUserEditMode(MODENAME) # Where MODENAME is a string available in the list of edit modes
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std UserEditMode/fr
