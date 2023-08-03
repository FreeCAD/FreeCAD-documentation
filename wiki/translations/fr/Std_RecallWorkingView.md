---
 GuiCommand:
   Name: Std RecallWorkingView
   Name/fr: Std Rappel de la vue de travail
   MenuLocation: Affichage , Vues standards , Rappeler la vue de travail
   Workbenches: Tous
   Shortcut: **Fin**
   Version: 0.21
   SeeAlso: Std_StoreWorkingView/fr, Std_FreezeViews/fr
---

# Std RecallWorkingView/fr

## Description

La fonction **Std Rappel de vue de travail** rappelle la vue de travail stockée de la [vue_3D](3D_view/fr.md) active. Pour plus d\'informations, voir [Std Stocker la vue de travail](Std_StoreWorkingView/fr.md).



## Utilisation

1.  Assurez-vous qu\'une [vue_3D](3D_view/fr.md) est active et que la commande [Std Stocker la vue de travail](Std_StoreWorkingView/fr.md) a été utilisée au moins une fois.
2.  Il existe plusieurs façons de lancer la commande :
    -   Sélectionnez l\'option **Affichage → Vues standards → Rappeler la vue de travail** dans le menu.
    -   Utilisez le raccourci clavier : **Fin**.



## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour rappeler la vue de travail enregistrée de la vue 3D active :


```python
import FreeCADGui

FreeCADGui.runCommand("Std_RecallWorkingView", 0)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std RecallWorkingView/fr
