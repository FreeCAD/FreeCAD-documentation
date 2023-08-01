---
- GuiCommand:/fr
   Name:Std SelBoundingBox
   Name/fr:Std Boîte englobante
   MenuLocation:Affichage → Boîte englobante
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Style de représentation](Std_DrawStyle/fr.md)
---

# Std SelBoundingBox/fr

## Description

La commande **Std Boîte englobante** bascule le mode de surbrillance du cadre de sélection global. Si ce mode est activé, les objets sélectionnés sont marqués dans une [vue 3D](3D_view/fr.md) avec un cadre de sélection en surbrillance même si leur **Selection Style** est défini sur \"Shape\" (Forme).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Std_SelBoundingBox.svg" width=16px> [Boîte englobante](Std_SelBoundingBox/fr.md)**.
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_SelBoundingBox.svg" width=16px> Boîte englobante** dans le menu.



## Préférences

Le mode en question est stocké : **Outils → Éditer les paramètres... → BaseApp → Preferences → View → ShowSelectionBoundingBox**. Il s\'agit d\'une valeur booléenne, la valeur par défaut est `False`.



## Script


**Voir aussi :**

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



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SelBoundingBox/fr
