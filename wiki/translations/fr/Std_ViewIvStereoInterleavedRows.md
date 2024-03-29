---
 GuiCommand:
   Name: Std ViewIvStereoInterleavedRows
   Name/fr: Std Lignes stéréo entrelacées
   MenuLocation: Affichage , Stéréo , Lignes stéréo entrelacées
   Workbenches: Tous
   SeeAlso: Std_ViewIvStereoRedGreen/fr, Std_ViewIvStereoQuadBuff/fr, Std_ViewIvStereoInterleavedColumns/fr, Std_ViewIvStereoOff/fr
---

# Std ViewIvStereoInterleavedRows/fr

## Description

La commande **Std Lignes stéréo entrelacées** change le mode actif de la [vue 3D](3D_view/fr.md) en mode d\'affichage stéréo des lignes entrelacées. Pour utiliser ce mode stéréo, une carte graphique spéciale, un écran spécial et des lunettes [avec verres polarisés](https://en.wikipedia.org/wiki/Polarized_3D_system) sont nécessaires.



## Utilisation

1.  Sélectionnez l\'option **Affichage → Stéréo → <img src="images/Std_ViewIvStereoInterleavedRows.svg" width=16px> Lignes stéréo entrelacées** dans le menu.



## Préférences

-   La distance entre les yeux peut être modifiée dans les préférences : **Édition → Préférences... → Affichage → Vue 3D → Distance entre les yeux pour les modes stéréo**. Voir l\'[Éditeur de préférences](Preferences_Editor#3D_View/fr.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour modifier la vue en lignes entrelacées stéréo, utilisez la méthode `setStereoType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedRows')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoInterleavedRows/fr
