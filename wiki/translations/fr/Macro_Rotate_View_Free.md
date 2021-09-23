# Macro Rotate View Free/fr
 {{Macro
|Name=Rotate View Free
|Translate=Rotation Libre
|Icon=Text_console_python.png
|Description=Cette Commande collée dans la console Python FreeCAD vous permet de faire pivoter la vue en 3 axes et l'angle (en degrés) et permet de créer un plan à la position souhaitée
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|SeeAlso=<img src=images/Macro_Rotate_View_view_90_Degrees.png style="width:Macro Rotate View](Macro_Rotate_View/fr.md) [24px"><br /><img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width:Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric/fr.md) [24px"> <img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width:24px">
}}

## Description

Cette définition collée dans la console Python FreeCAD (ou votre macro) vous permet de faire pivoter la vue en 3 axes et l\'angle (en degrés) permet de créer un plan à la position souhaitée

## Utilisation

Collez le code dans la console Python, tapez **Enter** → **Enter** (pour valider la commande) puis tapez ex: {{ColoredText|**RotateView(0,1,0,45)** }}

## Script

**Macro\_Rotate\_View\_Free.FCMacro**


{{MacroCode|code=
#Paste in the Python console and tip ex:
#RotateView(0,1,0,45)
def RotateView(axisX=1.0,axisY=0.0,axisZ=0.0,angle=45.0):
    import math
    from pivy import coin
    try:
        cam = Gui.ActiveDocument.ActiveView.getCameraNode()
        rot = coin.SbRotation()
        rot.setValue(coin.SbVec3f(axisX,axisY,axisZ),math.radians(angle))
        nrot = cam.orientation.getValue() * rot
        cam.orientation = nrot
        print( axisX," ",axisY," ",axisZ," ",angle)
    except Exception:
        print( "Not ActiveView ")


}}

Dans la console Python tapez par exemple:


{{MacroCode|code=
RotateView(0,1,0,45)
}}

si aucun document n\'est ouvert une erreur est retournée




