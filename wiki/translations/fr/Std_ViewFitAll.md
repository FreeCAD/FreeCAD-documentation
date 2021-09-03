---
- GuiCommand:/fr
   Name:Std ViewFitAll
   Name/fr:Std Tout afficher
   MenuLocation:Affichage → Vues standards‏‎ → Tout afficher
   Workbenches:Tous
   Shortcut:**V** **F**
   SeeAlso:[Std Affichage de la sélection](Std_ViewFitSelection/fr.md)
---

## Description

La commande **Std Tout afficher** effectue un zoom et un panoramique afin que tous les objets visibles tiennent dans la [vue 3D](3D_view/fr.md) active.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_ViewFitAll.svg" width=16px> [Affiche l'ensemble...](Std_ViewFitAll/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Affichage → Vues standards → <img src="images/Std_ViewFitAll.svg" width=16px> Tout afficher}} dans le menu.
    -   Sélectionnez l\'option {{MenuCommand|<img src="images/Std_ViewFitAll.svg" width=16px> Affiche l'ensemble...}} dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **V** puis **F**.

## Remarques

-   Il est également possible de passer en mode \'affichage total\' via le menu Mini-cube du [Cube de navigation](Navigation_Cube/fr.md).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'affichage total\', utilisez la méthode `fitAll` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Alternativement, la méthode `SendMsgToActiveView` de l\'objet FreeCADGui peut être utilisée. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}  
