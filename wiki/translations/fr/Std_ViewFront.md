---
- GuiCommand:
   Name:Std ViewFront
   Name/fr:Std Vue de face
   MenuLocation:Affichage - Vues standards - Face
   Workbenches:Tous
   Shortcut:**1**
   SeeAlso:[Std Vue de dessus](Std_ViewTop/fr.md), [Std Vue droite](Std_ViewRight/fr.md)
---

# Std ViewFront/fr

## Description

La **Std Vue de face** place la caméra dans la [vue 3D](3D_view/fr.md) dans la direction de l\'axe des Y positifs.

![](images/FreeCAD_views_front.svg ) 
*La flèche 1 pointe dans le sens de la vue de face*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewFront.svg" width=16px> [Face](Std_ViewFront/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand |Affichage → Vues standards → <img src="images/Std_ViewFront.svg" width=16px> Face}} dans le menu.
    -   Sélectionnez l\'option {{MenuCommand |Vues standards → <img src="images/Std_ViewFront.svg" width=16px> Face}} dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **1**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue de face\', utilisez la méthode `viewFront` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewFront()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewFront/fr
