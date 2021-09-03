---
- GuiCommand:/fr
   Name:Std ViewIvStereoInterleavedColumns
   Name/fr:Std Colonnes stéréo entrelacées
   MenuLocation:Affichage → Stéréo → Colonnes stéréo entrelacées
   Workbenches:Tous
   SeeAlso:[Std Stéréo rouge cyan](Std_ViewIvStereoRedGreen/fr.md), [Std Tampon stéréo quadruple](Std_ViewIvStereoQuadBuff/fr.md), [Std Lignes stéréo entrelacées](Std_ViewIvStereoInterleavedRows/fr.md), [Std Stéréo désactivée](Std_ViewIvStereoOff/fr.md)
---

## Description

La commande **Std Colonnes stéréo entrelacées** change le mode actif de la [vue 3D](3D_view/fr.md) en mode d\'affichage stéréo des colonnes entrelacées. Pour utiliser ce mode stéréo, une carte graphique spéciale, un écran spécial et des lunettes [avec verres polarisés](https://en.wikipedia.org/wiki/Polarized_3D_system) sont nécessaires.

## Utilisation

1.  Sélectionnez l\'option {{MenuCommand|Affichage → Stéréo → <img src="images/Std_ViewIvStereoInterleavedColumns.svg" width=16px> Colonnes stéréo entrelacées}} dans le menu.

## Préférences

-   La distance entre les yeux peut être modifiée dans les préférences: {{MenuCommand|Édition → Préférences... → Affichage → Vue 3D → Eye to eye distance for stereo modes}}. Voir l\'[Editeur de préférences](Preferences_Editor#3D_View/fr.md).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour modifier la vue en colonnes entrelacées stéréo, utilisez la méthode `setStereoType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedColumns')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}  
