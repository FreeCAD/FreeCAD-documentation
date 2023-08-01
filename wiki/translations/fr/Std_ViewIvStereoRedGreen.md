---
- GuiCommand:
   Name:Std ViewIvStereoRedGreen
   Name/fr:Std Stéréo rouge cyan
   MenuLocation:Affichage → Stéréo → Stéréo rouge/cyan
   Workbenches:Tous
   SeeAlso:[Std Tampon stéréo quadruple](Std_ViewIvStereoQuadBuff/fr.md), [Std Lignes stéréo entrelacées](Std_ViewIvStereoInterleavedRows/fr.md), [Std Colonnes stéréo entrelacées](Std_ViewIvStereoInterleavedColumns/fr.md), [Std Stéréo désactivée](Std_ViewIvStereoOff/fr.md)
---

# Std ViewIvStereoRedGreen/fr

## Description

La commande **Std Stéréo rouge cyan** change la [vue 3D](3D_view/fr.md) active en rouge/cyan, [Anaglyphe](https://fr.wikipedia.org/wiki/Anaglyphe), mode d\'affichage stéréo. Pour utiliser ce mode stéréo, des lunettes avec des lentilles colorées sont nécessaires.



## Utilisation

1.  Sélectionnez l\'option **Affichage → Stéréo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stéréo rouge cyan** dans le menu.



## Préférences

-   La distance entre les yeux peut être modifiée dans les préférences : **Édition → Préférences... → Affichage → Vue 3D → Distance entre les yeux pour les modes stéréo**. Voir l\'[Éditeur de préférences](Preferences_Editor#3D_View/fr.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en rouge/cyan, utilisez la méthode `setStereoType` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewIvStereoRedGreen/fr
