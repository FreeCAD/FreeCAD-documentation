# Macro Normal Vector
{{Macro
|Name=Normal Vector Macro
|Icon=Macro_Normal_Vector.png
|Description=Get normal vector of preselected face
|Author=ulrich1a
|Version=1.0
|Date=2016-09-26
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/8/8b/Macro_Normal_Vector.png ToolBar Icon]
}}

## Description

Simple macro to extract normal vector of previously within the 3D-View chosen face and give the output to the python console

## Usage

-   Choose Face in 3D View.
-   Copy Macro code to python console.
-   FreeCAD will then display normal vector information in python console.
-   Use these values for setting up direction when creating a drawing view.

## Script

ToolBar Icon  ![](images/Macro_Normal_Vector.png )

**Macro\_Normal\_Vector.FCMacro**


{{MacroCode|code=
Gui.Selection.getSelectionEx()[0].SubObjects[0].Faces[0].normalAt(0,0)
}}



## Link

[Link to dicussion thread (german)](http://forum.freecadweb.org/viewtopic.php?f=13&t=10959)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Normal Vector
