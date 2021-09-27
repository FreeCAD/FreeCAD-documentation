# Macro Align Object to View/en
{{Macro
|Name=Macro Align Object to View
|Icon=Macro_Align_Object_to_View.png
|Description=This macro aligns the selected object to the current View.
|Author=Mario52
|Version=0.1
|Date=2015-01-16
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/f/f4/Macro_Align_Object_to_View.png ToolBar Icon]
|SeeAlso=_ [Macro_FCCamera](Macro_FCCamera.md)
}}

## Description

This macro aligns and Position the selected object to the current View.

## Usage

-   Direct your view, select your object and run the macro
-   Your object will be the placement of the camera coordinates

## Script

ToolBar Icon ![](images/Macro_Align_Object_to_View.png )

**Macro\_Align\_Object\_to\_View.FCMacro**


{{MacroCode|code=
# This macro place your object selected to the position ActiveView (camera)
# extact FCCamera
# 16/01/2015

__title__  ="Align Object to View"
__author__ = "Mario52"
__date__   = "16/01/2015"
__version__= "0.1"

import pivy
from pivy import coin

sel = FreeCADGui.Selection.getSelection()
Nameelement = sel[0].Name
App.Console.PrintMessage(str(Nameelement)+"\n")

pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)

App.ActiveDocument.getObject(Nameelement).Placement=pl

}}

## Example


<center>

Image:Macro Align Object to View 01.png\|Your object in its original position XY. Image:Macro Align Object to View 02.png\|Rotate the screen X? Y? Z? or use this macro [Macro\_Rotate\_View](Macro_Rotate_View.md) for precise rotation.


</center>


<center>

Image:Macro Align Object to View 03.png\|Select the object and run the macro (the object face the screen). Image:Macro Align Object to View 04.png\|Your object return in the XY display and in its new coordinates position (Placement,Angle)


</center>

## Credits

Tanks Simplified code to rentlau\_64

---
[documentation index](../README.md) > Macro Align Object to View/en
