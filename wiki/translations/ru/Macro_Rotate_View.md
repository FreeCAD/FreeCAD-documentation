# Macro Rotate View/ru
{{Macro
|Name=Macro Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Description=This macro rotates the current view by 90° to the left. Only works if you are in [Top view](Std_ViewTop.md).
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|Download=[https://wiki.freecad.org/images/a/a0/Macro_Rotate_View_view_90_Degrees.png ToolBar Icon]
|SeeAlso=[Macro Rotate ViewAxonometric](Macro_Rotate_ViewAxonometric.md), [Macro Rotate View Free](Macro_Rotate_View_Free.md)
}}



## Описание

This macro rotates the current view by 90° to the left.



## Ограничения

Only works if you are in Top view: ![Std_ViewTop\|16px\|link=Std_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop.md)



## Скрипт

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
⏵ [documentation index](../README.md) > Macro Rotate View/ru
