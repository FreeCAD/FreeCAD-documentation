# Macro Toggle Visibility2 2-2/pl
{{Macro
|Name=Macro Toggle Visibility2 2-2
|translate=Macro Toggle Visibility2 2-2
|Icon=Macro_VisibleAlls2.png
|Description={{ColoredParagraph|DarkRed|Yellow|This macro must be used with '''Macro_Toggle_Visibility2_1-2'''}}<br/>This macro makes all objects visible respecting the original visible and hidden objects after use the [Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2.md)
|Author=openfablab
|Version=00.02b
|Date=2017-07-27
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ec/Macro_VisibleAlls2.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2.md)<br/>[Macro Toggle Visibility](Macro_Toggle_Visibility.md)
}}

## Description


{{ColoredText|This macro must be used with '''[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2.md)'''}}

This macro makes all objects visible respecting the original visible and hidden objects after use the [Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2.md)

## How To Use 

Copy the macros and the icons in your folder macros and run (see [How to install macros](How_to_install_macros.md))

## Script

This macro makes all objects visible respecting the original visible and hidden objects after use the [Macro_Toggle_Visibility2_1-2](Macro_Toggle_Visibility2_1-2.md) macro.

ToolBar Icon <img alt="" src=images/Macro_VisibleAlls2.png  style="width:64px;">

**Macro_DisplayAllObjects2_2-2.FCMacro**


{{MacroCode|code=

import FreeCAD
#original name "Macro_VisibleAlls" pratical name "Macro_Toggle_Visibility2_2-2" "Macro_Toggle_Visibility2_1-2" associate with "Macro_Toggle_Visibility2_2-2"
__title__="Macro_DisplayAllObjects2_2-2"
__author__ = "openfablab"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00b"
__date__    = "27/07/2017"

try:
    for ShapeNameObj in FreeCAD.actual:   # displyed alls objects
        #print ShapeNameObj
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj).Visibility = True
except Exception:
    None }}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Toggle Visibility2 2-2/pl
