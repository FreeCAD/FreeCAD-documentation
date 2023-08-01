# Macro If Selected Stay If Not Then Delete/ru
{{Macro
|Name=Macro If Selected Stay If Not Then Delete
|Icon=Macro_If_Selected_Stay_If_Not_Then_Delete.png
|Description=This macro delete all objects not selected.
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/62/Macro_If_Selected_Stay_If_Not_Then_Delete.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2.md)<br>[Macro_Toggle_Visibility](Macro_Toggle_Visibility.md)<br>[Macro HiddenAlls](Macro_HiddenAlls.md)<br>[Macro_VisibleAlls](Macro_VisibleAlls.md)
}}

## Описание

Данный макрос удаляет все объекты кроме тех, что выбраны пользователем!!!

## Скрипт

ToolBar Icon <img alt="" src=images/Macro_If_Selected_Stay_If_Not_Then_Delete.png  style="width:64px;">

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
⏵ [documentation index](../README.md) > Macro If Selected Stay If Not Then Delete/ru
