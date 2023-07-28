---
- GuiCommand:/fr
   Name:Std ViewIvStereoQuadBuff
   Name/fr:Std Tampon stéréo quadruple
   MenuLocation:Affichage → Stéréo → Tampon stéréo quadruple
   Workbenches:Tous
   SeeAlso:[Std Stéréo rouge cyan](Std_ViewIvStereoRedGreen/fr.md), [Std Lignes stéréo entrelacées](Std_ViewIvStereoInterleavedRows/fr.md), [Std Colonnes stéréo entrelacées](Std_ViewIvStereoInterleavedColumns/fr.md), [Std Stéréo désactivée](Std_ViewIvStereoOff/fr.md)
---

# Std ViewIvStereoQuadBuff/fr

## Description

La commande **Std Tampon stéréo quadruple** change le mode actif de la [vue 3D](3D_view/fr.md) en mode de visualisation stéréo à quadruple tampon. Pour utiliser ce mode stéréo, une carte graphique spéciale, un écran spécial et des lunettes [avec verres polarisés](https://en.wikipedia.org/wiki/Polarized_3D_system) sont nécessaires.



## Utilisation

1.  Sélectionnez l\'option **Affichage → Stéréo → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Tampon stéréo quadruple** dans le menu.



## Préférences

-   La distance entre les yeux peut être modifiée dans les préférences : **Édition → Préférences... → Affichage → Vue 3D → Distance entre les yeux pour les modes stéréo**. Voir l\'[Éditeur de préférences](Preferences_Editor#3D_View/fr.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en Tampon stéréo quadruple, utilisez la méthode `setStereoType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoQuadBuff/fr
