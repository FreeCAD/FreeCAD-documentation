# Macro Rotate View/de
{{Macro/de
|Name=Macro Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Translate=Rotate View by 90°
|Description=Dieses Makro dreht die aktuelle Ansicht um 90 ° nach links. Funktioniert nur, wenn Sie sich in der [Draufsicht](Std_ViewTop/de.md) befinden
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|Download=[https://wiki.freecad.org/wiki/images/a/a0/Macro_Rotate_View_view_90_Degrees.png Werkzeugleistensymbol]
|SeeAlso=[Macro Rotate ViewAxonometric](Macro_Rotate_ViewAxonometric/de.md), [Macro Rotate View Free](Macro_Rotate_View_Free/de.md)
}}



## Beschreibung

Dieses Makro dreht die aktuelle Ansicht um 90° nach links.



## Beschränkungen

Funktioniert nur in der Draufsicht: ![Std_ViewTop\|16px\|link=Std_ViewTop](images/View-top.svg ) [Draufsicht](Std_ViewTop/de.md)

## Script

Werkzeugleistensymbol ![](images/Macro_Rotate_View_view_90_Degrees.png )

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
⏵ [documentation index](../README.md) > Macro Rotate View/de
