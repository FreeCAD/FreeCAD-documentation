# Macro Rotate View/fr
 {{Macro/fr
|Name=Rotate View by 90°
|Translate=Vue Rotation à 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Description=Cette macro fait pivoter l'affichage actuel de 90 ° vers la gauche. Ne fonctionne que si vous êtes en [vue de dessus](Std_ViewTop/fr.md).
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/a/a0/Macro_Rotate_View_view_90_Degrees.png Macro_Rotate_View_view_90_Degrees]
|SeeAlso=<img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width:Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric/fr.md) [24px"> <img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width:24px"><br />[Macro Rotate View Free](Macro_Rotate_View_Free/fr.md)
}}

## Description

Cette macro fait pivoter l\'affichage actuel de 90 ° vers la gauche.

## Limitations

Ne fonctionne que si vous êtes en vue de dessus: ![Std\_ViewTop\|16px\|link=Std\_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop/fr.md)

## Script

ToolBar Icon ![](images/Macro_Rotate_View_view_90_Degrees.png )

**Macro\_Rotate\_View\_90\_Degrees.FCMacro**


{{MacroCode|code=
import math
from pivy import coin
cam = Gui.ActiveDocument.ActiveView.getCameraNode()
rot = coin.SbRotation()
rot.setValue(coin.SbVec3f(0,0,1),math.pi/2)
nrot = cam.orientation.getValue() * rot
cam.orientation = nrot
}}




