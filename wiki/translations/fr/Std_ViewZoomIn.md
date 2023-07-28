---
- GuiCommand:/fr
   Name:Std ViewZoomIn
   Name/fr:Std Zoom avant
   MenuLocation:Affichage → Zoom‏‎ → Zoom avant
   Workbenches:Tous
   Shortcut:**Ctrl**+**+**
   SeeAlso:[Std Zoom arrière](Std_ViewZoomOut/fr.md), [Std Zoom de sélection](Std_ViewBoxZoom/fr.md)
---

# Std ViewZoomIn/fr

## Description

La commande **Std Zoom avant** effectue un zoom avant dans la [vue 3D](3D_view/fr.md) active.



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Affichage → Zoom → <img src="images/Std_ViewZoomIn.svg" width=16px> Zoom avant** dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**+**.



## Remarques

-   Il est également possible de zoomer avec la molette de défilement de la souris.



## Préférences

-   Le facteur de zoom peut être modifié dans les préférences : **Édition → Préférences... → Affichage → Navigation → Pas du zoom**. Ce paramètre affecte également le zoom de la molette de défilement. Voir [Éditeur de préférences](Preferences_Editor/fr#Navigation.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour zoomer, utilisez la méthode `zoomIn` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomIn/fr
