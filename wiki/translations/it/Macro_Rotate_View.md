# Macro Rotate View/it
{{Macro/it
|Name=Macro Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Translate=Ruota la vista di 90°
|Description=Questa macro ruota la vista corrente di 90° a sinistra. Funziona solo se si è in vista dall'alto
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=Tutte
|Download=[https://wiki.freecad.org/images/a/a0/Macro_Rotate_View_view_90_Degrees.png ToolBar Icon]
|SeeAlso=[Macro Rotate ViewAxonometric](Macro_Rotate_ViewAxonometric.md), [Macro Rotate View Free](Macro_Rotate_View_Free.md)
}}



## Descrizione

Questa macro ruota la vista corrente di 90° a sinistra.



## Limitazioni

Funziona solo se si è in vista dall\'alto ![Std_ViewTop\|16px\|link=Std_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop/it.md)

## Script

Icona barra strumenti ![](images/Macro_Rotate_View_view_90_Degrees.png )

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
⏵ [documentation index](../README.md) > Macro Rotate View/it
