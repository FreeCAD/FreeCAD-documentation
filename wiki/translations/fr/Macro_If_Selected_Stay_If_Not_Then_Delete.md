# Macro If Selected Stay If Not Then Delete/fr
{{Macro/fr
|Name=Macro If Selected Stay If Not Then Delete
|Icon=Macro_If_Selected_Stay_If_Not_Then_Delete.png
|Description=Cette macro éfface tous les objets qui ne sont pas sélectionnés.
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/6/62/Macro_If_Selected_Stay_If_Not_Then_Delete.png Icône de la barre d'outils]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/fr.md)<br>[Macro_Toggle_Visibility](Macro_Toggle_Visibility/fr.md)<br>[Macro HiddenAlls](Macro_HiddenAlls.md)<br>[Macro_VisibleAlls](Macro_VisibleAlls/fr.md)
}}

## Description

Cette macro efface tous les objets qui ne sont pas sélectionnés.

## Script

Icône de la barre d\'outils <img alt="" src=images/Macro_If_Selected_Stay_If_Not_Then_Delete.png  style="width:64px;">

**Macro_If_Selected_Stay_If_Not_Then_Delete.FCMacro**


{{MacroCode|code=
import FreeCAD
# Macro_If_Selected_Stay_If_Not_Then_Delete
__title__="Macro_If_Selected_Stay_If_Not_Then_Delete"
__author__ = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00"
__date__    = "16/06/2016"

App = FreeCAD
try:
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects:
        if Gui.Selection.isSelected(ShapeNameObj) == True:
            None
        else:
            App.ActiveDocument.removeObject(ShapeNameObj.Name)        # remove objects not selecteds
except Exception:
    None
}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro If Selected Stay If Not Then Delete/fr
