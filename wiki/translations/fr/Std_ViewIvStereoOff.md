---
- GuiCommand:/fr
   Name:Std ViewIvStereoOff
   Name/fr:Std Stéréo désactivée
   MenuLocation:Affichage → Stéréo → Désactiver la stéréo
   Workbenches:Tous
   SeeAlso:[Std Stéréo rouge cyan](Std_ViewIvStereoRedGreen/fr.md), [Std Tampon stéréo quadruple](Std_ViewIvStereoQuadBuff/fr.md), [Std Lignes stéréo entrelacées](Std_ViewIvStereoInterleavedRows/fr.md), [Std Colonnes stéréo entrelacées](Std_ViewIvStereoInterleavedColumns/fr.md)
---

# Std ViewIvStereoOff/fr

## Description

La commande **Std Stéréo désactivée** désactive le mode stéréo dans la [vue 3D](3D_view/fr.md) active.



## Utilisation

1.  Sélectionnez l\'option **Affichage → Stéréo → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Désactiver la stéréo** dans le menu.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en non-stéréo, utilisez la méthode `setStereoType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoOff/fr
