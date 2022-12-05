---
- GuiCommand:/fr
   Name:Std AxisCross
   Name/fr:Std Axes du repère
   MenuLocation:Affichage → Afficher les axes des coordonnées
   Workbenches:Tous
   Shortcut:**A** **C**
---

# Std AxisCross/fr

## Description

La commande **Std Axes** bascule les axes du repère dans la [vue 3D](3D_view/fr.md) active.

Les axes du repère se composent de trois flèches représentant les axes positifs X, Y et Z du système de coordonnées global. Leur point de départ commun est l\'origine du système de coordonnées global.

![](images/Std_AxisCross_example.svg ) 
*Les axes du repère (les lettres ne font pas partie du repère)*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_AxisCross.svg" width=16px> Afficher les axes des coordonnées** dans le menu.
    -   Utilisez le raccourci clavier: **A** puis **C**.

## Remarques

-   FreeCAD peut afficher un indicateur de système de coordonnées plus petit dans le coin inférieur droit des vues 3D: **Edition → Préférences ... → Affichage → Vue 3D → Afficher le système de coordonnées dans le coin**. Voir [Editeur de préférences](Preferences_Editor/fr#Vue_3D.md).
-   Le [Cube de navigation](Navigation_Cube/fr.md) comprend également un indicateur de système de coordonnées.

## Préférences

-   La valeur par défaut des axes du repère peut être modifiée dans les préférences: **Edition → Préférences... → Affichage → Vue 3D → Afficher la croix de l'axe par défaut**. Voir [Réglage des préférences](Preferences_Editor/fr#Vue_3D.md). {{Version/fr|0.19}}

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour faire apparaitre les axes du repère, utilisez la méthode `setAxisCross` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)
FreeCADGui.ActiveDocument.ActiveView.hasAxisCross()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AxisCross/fr
