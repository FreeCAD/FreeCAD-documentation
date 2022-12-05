# Macro Align View to Face/fr
{{Macro/fr
|Name=Macro Align View to Face
|Icone=Macro_Align_View_to_Face.png
|Description=Cette macro aligne la vue en cours sur la face sélectionnée
|Author=Rockn
|Version=3.0
|Date=2022-10-08
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/d/d7/Macro_Align_View_to_Face.png Icône de la barre d'outils]
}}

## Description

Cette macro fait pivoter la vue en courspour la faire pointer perpendiculairement sur une face sélectionnée d\'un objet existant.

## Utilisation

1.  Sélectionnez la face d\'un objet
2.  Lancez la macro

## Script

Icône de la barre d\'outils ![](images/Macro_Align_View_to_Face.png )

**Macro_Align_View_to_Face.FCMacro** {{MacroCode|code=

# -*- coding: utf-8 -*-
# Set the current view perpendicular to the selected face
# Place la vue perpendiculairement a la face selectionnee
# 2013 Jonathan Wiedemann,
# 2016 Werner Mayer, 
# 2022 tchernomax, https://forum.freecadweb.org/viewtopic.php?p=630019#p630019
#
__title__   = "Align_View_to_Face"
__author__  = "Jonathan Wiedemann (Rockn)"
__url__     = "https://www.freecadweb.org/"
__Wiki__    = "https://wiki.freecadweb.org/Macro_Align_View_to_Face"
__version__ = "3.0"
__date__    = "2022/10/08"  #YYYY/MM/DD
#
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

sel=Gui.Selection.getSelectionEx()[0]
obj=sel.Object
face=sel.SubObjects[0]
dir = face.normalAt(0,0)
cam = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()

if dir.z == 1 :
    rot = pointAt(dir, App.Vector(0.0,1.0,0.0))
elif dir.z == -1 :
    rot = pointAt(dir, App.Vector(0.0,1.0,0.0))
else :
    rot = pointAt(dir, App.Vector(0.0,0.0,1.0))

def computeRotation(obj):
    if not obj.Parents:
        # the object has no parent
        return obj.Placement.Rotation
    # the object has parent
    # we compute the rotation of it's parent and multiply it with it's rotation
    return parentRotate(obj.Parents[0][0]).multiply(obj.Placement.Rotation)

if obj.Parents:
    obj_par = obj.Parents[0][0]
    rot_par = computeRotation(obj_par)
    cam.orientation.setValue(rot_par.multiply(rot).Q)
else:
    cam.orientation.setValue(rot.Q)

Gui.SendMsgToActiveView("ViewSelection")

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align View to Face/fr
