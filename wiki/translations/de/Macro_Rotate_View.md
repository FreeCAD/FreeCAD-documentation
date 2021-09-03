 {{Macro/de
|Name=Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Translate=Rotate View by 90°
|Description=Dieses Makro dreht die aktuelle Ansicht um 90 ° nach links. Funktioniert nur, wenn Sie sich in der [Draufsicht](Top_view/de.md) befinden
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/a/a0/Macro_Rotate_View_view_90_Degrees.png Macro_Rotate_View_view_90_Degrees]
|SeeAlso=<img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width:Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric/de.md) [24px"> <img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width:24px"><br />[Macro Rotate View Free](Macro_Rotate_View_Free/de.md)
}}

## Beschreibung

Dieses Makro dreht die aktuelle Ansicht um 90° nach links.

## Beschränkungen

Funktioniert nur in der Draufsicht: ![Std\_ViewTop\|16px\|link=Std\_ViewTop](images/View-top.svg ) [Draufsicht](Std_ViewTop/de.md)

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




