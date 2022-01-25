# Macro Align View to Face/es
{{Macro/es
|Name=Macro Align View to Face
|Icone=Macro_Align_View_to_Face.png
|Translate=Vista de alineación de macro a cara
|Description=Esta macro alinea la vista actual a una cara seleccionada
|Author=Rockn
|Version=1.0
|Date=2014-03-12
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d7/Macro_Align_View_to_Face.png ToolBar Icon]
}}

## Descripción

Esta macro gira la vista actual para apuntar perpendicularmente a una cara seleccionada de un objeto existente.


<div class="mw-translate-fuzzy">

## Cómo usar 

1.  Seleccionar una cara en un objeto
2.  Ejecutar la macro


</div>

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
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align View to Face/es
