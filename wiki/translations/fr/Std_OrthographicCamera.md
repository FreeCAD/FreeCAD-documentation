---
- GuiCommand:/fr
   Name:Std OrthographicCamera
   Name/fr:Std Vue orthographique
   MenuLocation:Affichage → Vue orthographique
   Workbenches:Tous
   Shortcut:**V** **O**
   SeeAlso:[Std Vue en perspective](Std_PerspectiveCamera/fr.md)
---

## Description

La commande **Std Vue orthographique** fait passer la vision du mode actif [vue 3D](3D_view/fr.md) en mode de vue orthographique. Dans ce mode, les objets qui sont plus éloignés de l\'appareil photo n\'apparaissent pas plus petits que ceux qui sont plus proches.

![](images/Std_OrthographicCamera_example.svg ) *Deux cubes de mêmes dimensions en vue orthographique*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_OrthographicCamera.svg" width=16px> Vue orthographique** dans le menu.
    -   Utilisez le raccourci clavier: **V** puis **O**.

## Remarques

-   Il est également possible de passer en mode d\'affichage orthographique via le menu Mini-cube du [Cube de navigation](Navigation_Cube/fr.md).

## Préférences

-   Le type de vue peut être modifié dans les préférences: **Edition → Préférences... → Affichage → Vue 3D → Type de caméra**. Le type sélectionné sera utilisé pour toutes les vues 3D de tous les documents ouverts et également pour les nouveaux documents. Voir [Editeur de préférences](Preferences_Editor/fr#Vue_3D.md).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en orthographique, utilisez la méthode `setCameraType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Orthographic')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}  
