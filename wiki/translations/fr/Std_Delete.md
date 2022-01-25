---
- GuiCommand:/fr
   Name:Std_Delete
   Name/fr:Std Effacer
   MenuLocation:Édition → Effacer
   Workbenches:Tous
   Shortcut:**Suppr**
---

# Std Delete/fr

## Description

La commande **Std Effacer** supprime les objets sélectionnés.

## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Édition → <img src="images/Std_Delete.svg" width=16px> Effacer** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_Delete.svg" width=16px> Effacer** dans le menu contextuel [vue en arborescence](tree_view/fr.md) ou le menu contextuel [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **Suppr**.

## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour supprimer un objet, utilisez la méthode `removeObject` de l\'objet document.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Delete/fr
