---
 GuiCommand:
   Name: Std ViewIvStereoOff
   Name/fr: Std Stéréo désactivée
   MenuLocation: Affichage , Stéréo , Désactiver la stéréo
   Workbenches: Tous
   SeeAlso: Std_ViewIvStereoRedGreen/fr, Std_ViewIvStereoQuadBuff/fr, Std_ViewIvStereoInterleavedRows/fr, Std_ViewIvStereoInterleavedColumns/fr
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
⏵ [documentation index](../README.md) > Std ViewIvStereoOff/fr
