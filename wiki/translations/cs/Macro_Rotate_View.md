# Macro Rotate View/cs
<div class="mw-translate-fuzzy">


{{Macro/cs
|Name=Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Translate=Rotate View by 90°
|Description=Toto makro otočí objekt o 90° doleva. Funguje jen pokud jste v pohledu shora
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/a/a0/Macro_Rotate_View_view_90_Degrees.png Macro_Rotate_View_view_90_Degrees]
|SeeAlso=[Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric/cs.md) [<img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width:24px"> [<img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width:24px"><br />[Macro Rotate View Free](Macro_Rotate_View_Free/cs.md)
}}


</div>

## Description


<div class="mw-translate-fuzzy">

Toto makro otočí objekt o 90° doleva. Funguje jen pokud jste v pohledu shora ![rotation 90 degrees](images/Macro_Rotate_View_view_90_Degrees.png )


</div>

## Limitations

Only works if you are in Top view: ![Std_ViewTop\|16px\|link=Std_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop.md)

## Script

ToolBar Icon ![](images/Macro_Rotate_View_view_90_Degrees.png )

**Macro_Rotate_View_90_Degrees.FCMacro**


{{MacroCode|code=
import math
from pivy import coin
cam = Gui.ActiveDocument.ActiveView.getCameraNode()
rot = coin.SbRotation()
rot.setValue(coin.SbVec3f(0,0,1),math.pi/2)
nrot = cam.orientation.getValue() * rot
cam.orientation = nrot
}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Rotate View/cs
