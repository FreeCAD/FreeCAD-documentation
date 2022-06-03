# Macro Align Working Plane to Camera
{{Macro
|Name=Macro Align Working Plane to Camera
|Icon=Macro_Align_Working_Plane_to_Camera.png
|Description=This macro moves the current [Draft Working Plane](Draft_SelectPlane.md) to the center of the current view
|Author=yorik
|Version=1.0
|Date=2017-05-10
|Download=[https   *//www.freecadweb.org/wiki/images/0/01/Macro_Align_Working_Plane_to_Camera.png ToolBar Icon]
|FCVersion=All
|SeeAlso=[Macro Align Camera to Working Plane](Macro_Align_Camera_to_Working_Plane.md) [24px|Macro Align Camera to Working Plane](File   *Macro_Align_Camera_to_Working_Plane.png.md)
}}

## Description

This macro moves the current [Draft Working Plane](Draft_SelectPlane.md) to the center of the current view. It is useful when you are working quite far from the grid center.

## Usage

-   Move the view to the zone where you want to look at.
-   Run the macro.

## Script

ToolBar Icon  ![](images/Macro_Align_Working_Plane_to_Camera.png )

**Macro\_Align\_Working\_Plane\_to\_Camera.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
cam = FreeCAD.Vector(FreeCADGui.ActiveDocument.ActiveView.getCameraNode().position.getValue().getValue())
pos = FreeCAD.DraftWorkingPlane.projectPoint(cam)
FreeCAD.DraftWorkingPlane.position = pos
FreeCADGui.Snapper.setGrid()
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align Working Plane to Camera
