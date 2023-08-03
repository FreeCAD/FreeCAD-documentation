---
 GuiCommand:
   Name: Std ViewFitAll
   Name/fr: Std Tout afficher
   MenuLocation: Affichage , Vues standards‏‎ , Tout afficher
   Workbenches: Tous
   Shortcut: **V** **F**
   SeeAlso: Std_ViewFitSelection/fr
---

# Std ViewFitAll/fr



## Description

La commande **Std Tout afficher** effectue un zoom et un panoramique afin que tous les objets visibles tiennent dans la [vue 3D](3D_view/fr.md) active.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewFitAll.svg" width=16px> [Tout afficher](Std_ViewFitAll/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standards → <img src="images/Std_ViewFitAll.svg" width=16px> Tout afficher** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_ViewFitAll.svg" width=16px> Tout afficher** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Sélectionnez l\'option **<img src="images/Std_ViewFitAll.svg" width=16px> Tout afficher** dans le menu Mini-cube du [Cube de navigation](Navigation_Cube/fr.md).
    -   Utilisez le raccourci clavier : **V** puis **F**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \"Affichage total\", utilisez la méthode `fitAll` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Autre possibilité, la méthode `SendMsgToActiveView` de l\'objet FreeCADGui peut être utilisée. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitAll/fr
