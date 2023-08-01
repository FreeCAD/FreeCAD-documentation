---
- GuiCommand:
   Name: Std ToggleSelectability
   Name/fr: Std Basculer la sélectivité
   MenuLocation: Affichage - Visibilité - Basculer la sélectivité
   Workbenches: Tous
---

# Std ToggleSelectability/fr

## Description

La commande **Std Basculer la sélectivité** bascule la sélectionnabilité des objets dans la [Vues 3D](3D_view/fr.md).



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Affichage → Visibilité → <img src="images/Std_ToggleSelectability.svg" width=16px> Basculer la sélectivité** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_ToggleSelectability.svg" width=16px> Basculer la sélectivité** dans le menu contextuel de la [vue en arborescence](tree_view/fr.md). Cette option n\'est pas disponible dans l\'[Atelier PartDesign](PartDesign_Workbench.md).
    -   Sélectionnez l\'option **<img src="images/Std_ToggleSelectability.svg" width=16px> Basculer la sélectivité** dans le menu contextuel de la vue 3D.



## Remarques

-   La sélectibilité d\'un objet peut également être modifiée via sa propriété **Selectable** associée dans l\'[Editeur de propriétés](Property_editor/fr.md) ou la [Vue Combinée](Combo_view/fr.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

La propriété `Selectable` d\'un objet détermine sa sélectibilité.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Selectable == True:
  obj.Selectable = False
else:
  obj.Selectable = True
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleSelectability/fr
