# Macro VisibleAlls
{{Macro
|Name=Macro VisibleAlls
|Icon=Macro_VisibleAlls.png
|Description=This macro display all objects in the document (Visibility True).
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/1/19/Macro_VisibleAlls.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2.md)<br>[Macro_Toggle_Visibility](Macro_Toggle_Visibility.md)<br>[Macro_HiddenAlls](Macro_HiddenAlls.md)<br>[Macro If Selected Stay If Not Then Delete](Macro_If_Selected_Stay_If_Not_Then_Delete.md)
}}

## Description

This macro display all objects in the document (Visibility True).

## Script

ToolBar Icon  <img alt="" src=images/Macro_VisibleAlls.png  style="width   *64px;">

**Macro_VisibleAlls.FCMacro**


{{MacroCode|code=
import FreeCAD
#Macro_VisibleAlls
__title__="Macro_DisplayAllObjects"
__author__ = "Mario52"
__url__     = "http   *//www.freecadweb.org/index-fr.html"
__version__ = "00.00"
__date__    = "11/11/2015"

try   *
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *   # displyed alls objects
        #print ShapeNameObj.Name
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True
except Exception   *
    None
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro VisibleAlls
