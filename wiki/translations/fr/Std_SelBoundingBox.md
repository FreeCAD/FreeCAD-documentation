---
- GuiCommand:/fr
   Name:Std SelBoundingBox
   Name/fr:Std SelBoundingBox
   MenuLocation:Affichage → Bounding box
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Style de représentation](Std_DrawStyle/fr.md)
---

## Description

La commande **Std Boîte de délimitation** bascule le mode de surbrillance du cadre de sélection global. Si ce mode est activé, les objets sélectionnés sont marqués dans une [vue 3D](3D_view/fr.md) avec un cadre de sélection en surbrillance même si leur **Selection Style** est défini sur \'Shape\' (Forme).

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_SelBoundingBox.svg" width=16px> [Std SelBoundingBox](Std_SelBoundingBox.md)**.
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_SelBoundingBox.svg" width=16px> Bounding box** dans le menu.

## Préférences

Le mode en question est stocké: **Outils → Editer paramètres... → BaseApp → Preferences → View → ShowSelectionBoundingBox**. Il s\'agit d\'une valeur booléenne, la valeur par défaut est `False`.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour modifier le paramètre ShowSelectionBoundingBox, utilisez la méthode `SetBool` du ParameterGrp approprié. L\'exemple de code ne fonctionne pas si FreeCAD est en mode console.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/View')
if grp.GetBool('ShowSelectionBoundingBox'):
  grp.SetBool('ShowSelectionBoundingBox',False)
else:
  grp.SetBool('ShowSelectionBoundingBox',True)

FreeCADGui.updateCommands()
```





{{Std Base navi

}}  
