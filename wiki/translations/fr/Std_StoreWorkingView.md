---
- GuiCommand:
   Name: Std StoreWorkingView
   Name/fr: Std Stocker la vue de travail
   MenuLocation: Affichage -> Vues standards -> Stocker la vue de travail
   Workbenches: Tous
   Shortcut: **Maj**+**Fin**
   Version: 0.21
   SeeAlso: Std_RecallWorkingView/fr, Std_FreezeViews/fr
---

# Std StoreWorkingView/fr

## Description

La commande **Std Stocker la vue de travail** stocke les paramètres de la caméra de la [vue 3D](3D_view/fr.md) active dans sa vue de travail temporaire. Cette vue peut être rappelée avec la commande [Std Rappel de vue de travail](Std_RecallWorkingView/fr.md).

Chaque vue 3D possède sa propre vue de travail. L\'enregistrement d\'une nouvelle vue de travail écrasera la vue de travail existante de la vue 3D active. Lorsqu\'une vue 3D est fermée, sa vue de travail est perdue.



## Utilisation

1.  Assurez-vous qu\'une [vue 3D](3D_view/fr.md) est active.
2.  Il existe plusieurs façons d\'invoquer la commande :
    -   Sélectionnez l\'option **Affichage → Vues standards → Stocker la vue de travail** dans le menu.
    -   Utilisez le raccourci clavier : **Maj**+**Fin**.



## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour stocker les paramètres actuels de la caméra de la vue 3D active dans une vue de travail :


```python
import FreeCADGui

FreeCADGui.runCommand("Std_StoreWorkingView", 0)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std StoreWorkingView/fr
