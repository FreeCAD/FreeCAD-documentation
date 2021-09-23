# Macro Align View to Face
{{Macro
|Name=Macro Align View to Face
|Icone=Macro_Align_View_to_Face.png
|Description=This macro aligns the current view to a selected face
|Author=Rockn
|Version=2.0
|Date=2016-03-06
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d7/Macro_Align_View_to_Face.png ToolBar Icon]
}}

## Description

This macro rotates the current view to point perpendicularly at a selected face of an existing object.

## Usage

1.  Select a face on an object
2.  Run the macro

## Script

 ToolBar Icon ![](images/Macro_Align_View_to_Face.png )

**Macro\_Align\_View\_to\_Face.FCMacro** {{MacroCode|code=

# -*- coding: utf-8 -*-
# Set the current view perpendicular to the selected face
# Place la vue perpendiculairement a la face selectionnee
# 2013 Jonathan Wiedemann, 2016 Werner Mayer

from pivy import coin

def pointAt(normal, up):
    z = normal
    y = up
    x = y.cross(z)
    y = z.cross(x)
   
    rot = App.Matrix()
    rot.A11 = x.x
    rot.A21 = x.y
    rot.A31 = x.z
   
    rot.A12 = y.x
    rot.A22 = y.y
    rot.A32 = y.z
   
    rot.A13 = z.x
    rot.A23 = z.y
    rot.A33 = z.z

    return App.Placement(rot).Rotation

s=Gui.Selection.getSelectionEx()
obj=s[0]
faceSel = obj.SubObjects[0]
dir = faceSel.normalAt(0,0)
cam = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()

if dir.z == 1 :
    rot = pointAt(dir, App.Vector(0.0,1.0,0.0))
elif dir.z == -1 :
    rot = pointAt(dir, App.Vector(0.0,1.0,0.0))
else :
    rot = pointAt(dir, App.Vector(0.0,0.0,1.0))

cam.orientation.setValue(rot.Q)
Gui.SendMsgToActiveView("ViewSelection")

}}

---
[documentation index](../README.md) > Macro Align View to Face
