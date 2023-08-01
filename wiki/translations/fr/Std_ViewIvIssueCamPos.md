---
- GuiCommand:
   Name: Std ViewIvIssueCamPos
   Name/fr: Std Position de la caméra
   MenuLocation: Affichage - Stéréo - Récupérer la position de la caméra
   Workbenches: Tous
   SeeAlso: [Std Figer l'affichage](Std_FreezeViews/fr.md)
---

# Std ViewIvIssueCamPos/fr



## Description

La commande **Std Position de la caméra** affiche les paramètres de la caméra de la [vue 3D](3D_view/fr.md) active dans la [Vue rapport](Report_view/fr.md) et la [console Python](Python_console/fr.md).


```python   OrthographicCamera {   viewportMapping ADJUST_CAMERA   position 57.73505 -57.73502 57.735027   orientation 0.74290609 0.30772209 0.59447283  1.2171158   nearDistance 81.588844   farDistance 109.60551   aspectRatio 1   focalDistance 100   height 100  } 
```



*Exemple de sortie : paramètres de la caméra après être passé à [vue isométrique](Std_ViewIsometric/fr.md) dans un nouveau document*



## Utilisation

1.  Sélectionnez l\'option **Affichage → Stéréo → <img src="images/Std_ViewIvIssueCamPos.svg" width=16px> Récupérer la position de la caméra** dans le menu.



## Remarques

-   Les paramètres de la caméra peuvent être utilisés pour ajouter des vues figées à un fichier \*.cam. Voir [Std Figer l\'affichage](Std_FreezeViews/fr.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

La méthode `getCamera` de l\'objet ActiveView renvoie les mêmes paramètres de caméra dans une seule chaîne. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.getCamera()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvIssueCamPos/fr
