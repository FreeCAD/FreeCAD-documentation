# Macro Rotate View/ru
{{Macro
|Name=Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Description=This macro rotates the current view by 90° to the left. Only works if you are in [Top view](Std_ViewTop.md).
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/a/a0/Macro_Rotate_View_view_90_Degrees.png Macro_Rotate_View_view_90_Degrees]
|SeeAlso=[Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric.md) [<img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width   *24px"> [<img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width   *24px"><br />[Macro Rotate View Free](Macro_Rotate_View_Free.md)
}}

## Описание

This macro rotates the current view by 90° to the left.

## Ограничения

Only works if you are in Top view   * ![Std\_ViewTop\|16px\|link=Std\_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop.md)

## Скрипт

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Rotate View/ru
