# Macro HiddenAlls/it
{{Macro/it
|Name=Macro HiddenAlls
|Icon=Macro_HiddenAlls.png
|Description=Questa macro nasconde tutti gli oggetti de documento (Visibility False).
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=Tutte versione
|Download=[https://www.freecadweb.org/wiki/images/d/d6/Macro_HiddenAlls.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/it.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/it.md)<br>[Macro_Toggle_Visibility](Macro_Toggle_Visibility/it.md)<br>[Macro VisibleAlls](Macro_VisibleAlls/it.md)<br>[Macro If Selected Stay If Not Then Delete](Macro_If_Selected_Stay_If_Not_Then_Delete/it.md)
}}

## Descrizione

Questa macro nasconde tutti gli oggetti de documento (Visibility False).

## Script

Icona barra strumenti <img alt="" src=images/Macro_HiddenAlls.png  style="width:64px;">

**Macro_HidenAlls.FCMacro**


{{MacroCode|code=
import FreeCAD
#Macro_HideAllObjects
__title__="Macro_HideAlls"
__author__ = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00"
__date__    = "11/11/2015"

try:
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects:   # hidden alls objects
        #print ShapeNameObj.Name
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = False
except Exception:
    None
}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro HiddenAlls/it
