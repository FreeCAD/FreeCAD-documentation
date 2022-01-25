---
- GuiCommand:/fr
   Name:Std ViewZoomOut
   Name/fr:Std Zoom arrière
   MenuLocation:Affichage → Zoom‏‎ → Zoom arrière
   Workbenches:Tous
   Shortcut:**Ctrl**+**-**
   SeeAlso:[Std Zoom avant](Std_ViewZoomIn/fr.md), [Std Zoom de sélection](Std_ViewBoxZoom/fr.md)
---

# Std ViewZoomOut/fr

## Description

La commande **Std Zoom arrière** effectue un zoom arrière dans la [vue 3D](3D_view/fr.md) active.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option **Affichage → Zoom → <img src="images/Std_ViewZoomOut.svg" width=16px> Zoom arrière** dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**-**.

## Remarques

-   Il est également possible de dézoomer avec la molette de défilement de la souris.

## Préférences

-   Le facteur de zoom peut être modifié dans les préférences: **Edition → Préférences... → Affichage → Navigation → Zoom step**. Ce paramètre affecte également le zoom de la molette de défilement. Voir [Editeur de préférences](Preferences_Editor/fr#Navigation.md).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour dézoomer, utilisez la méthode `zoomOut` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomOut()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomOut/fr
