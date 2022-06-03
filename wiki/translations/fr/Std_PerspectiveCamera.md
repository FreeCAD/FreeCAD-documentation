---
- GuiCommand   */fr
   Name   *Std PerspectiveCamera
   Name/fr   *Std Vue en perspective
   MenuLocation   *Affichage → Vue en perspective
   Workbenches   *Tous
   Shortcut   ***V** **P**
   SeeAlso   *[Std Vue orthographique](Std_OrthographicCamera/fr.md)
---

# Std PerspectiveCamera/fr

## Description

La commande **Std Vue en perspective** fait passer la vision du mode actif [vue 3D](3D_view/fr.md) en mode de vue en perspective. Dans ce mode, les objets qui sont plus éloignés de l\'appareil photo apparaissent plus petits que ceux qui sont plus proches.

![](images/Std_PerspectiveCamera_example.svg ) 
*Deux cubes de mêmes dimensions vus en perspective*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_PerspectiveCamera.svg" width=16px> Vue en perspective** dans le menu.
    -   Utilisez le raccourci clavier   * **V** then **P**.

## Remarques

-   Il est également possible de passer en mode d\'affichage perspective via le menu Mini-cube du [Cube de navigation](Navigation_Cube/fr.md).

## Préférences

-   Le type de vue peut être modifié dans les préférences   * **Edition → Préférences... → Affichage → Vue 3D → Type de caméra**. Le type sélectionné sera utilisé pour toutes les vues 3D de tous les documents ouverts et également pour les nouveaux documents. Voir [Editeur de préférences](Preferences_Editor/fr#Vue_3D.md).

## Script


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en perspective, utilisez la méthode `setCameraType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std PerspectiveCamera/fr
