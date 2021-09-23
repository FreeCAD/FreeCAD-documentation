# Macro Rotate ViewAxonometric/ru
 {{Macro
|Name=Macro Rotate ViewAxonometric
|Icon=Macro_Rotate_View_with_Y_pointing_upwards_.png
|Description=This macro rotates the current view in ViewAxonometric.
|Author=Yorik
|Version=01.00
|FCVersion=All
|Download= [https://www.freecadweb.org/wiki/images/2/2e/Macro_Rotate_View_with_Y_pointing_upwards_.png Macro_Rotate_View_with_Y_pointing_upwards_]<br />[https://www.freecadweb.org/wiki/images/a/a2/Macro_Rotate_View_with_Z_pointing_upwards_.png Macro_Rotate_View_with_Z_pointing_upwards_]
|Date=2010-11-17
|SeeAlso=<img src=images/Macro_Rotate_View_view_90_Degrees.png style="width:Macro_Rotate_View](Macro_Rotate_View.md) [24px">
}}

## Описание

This macro rotates the current view in ViewAxonometric (as is: Y).

You have two options:

-   mode 1 : axonometric view with Y pointing upwards ![axonometric view with Y pointing upwards](images/Macro_Rotate_View_with_Y_pointing_upwards_.png ) mode 1
-   mode 2 : axonometric view with Z pointing upwards ![axonometric view with Z pointing upwards](images/Macro_Rotate_View_with_Z_pointing_upwards_.png ) mode 2 (uncomment for use)

## Применение

For use the two macros, copy the first macro and name it \"**Macro\_Rotate\_ViewAxonometric\_Y**\" (mode 1) without change the code and use this icon ![axonometric view with Y pointing upwards](images/Macro_Rotate_View_with_Y_pointing_upwards_.png )

Copy the second macro and name it \"**Macro\_Rotate\_ViewAxonometric\_Z**\" (mode 2) and:

comment the line


{{ColoredText|'''11''' **#rot.setValue(coin.SbVec3f(1,0,0),-math.pi/2) # Y pointing upwards (mode 1)** }}

and uncomment the line


{{ColoredText|'''12''' **rot.setValue(coin.SbVec3f(0,0,1),math.pi/2) # Z pointing upwards (mode 2 uncomment for use)** }}

and use this icon ![axonometric view with Z pointing upwards](images/Macro_Rotate_View_with_Z_pointing_upwards_.png )

## Скрипт

-   mode 1 : ToolBar Icon ![](images/Macro_Rotate_View_with_Y_pointing_upwards_.png )
-   mode 2 : ToolBar Icon ![](images/Macro_Rotate_View_with_Z_pointing_upwards_.png ) (uncomment for use)

**Macro\_Rotate\_ViewAxonometric.FCMacro**


{{MacroCode|code=
import math
import pivy
from pivy import coin

Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")

cam = Gui.ActiveDocument.ActiveView.getCameraNode()
rot = coin.SbRotation()

rot.setValue(coin.SbVec3f(1,0,0),-math.pi/2) # Y pointing upwards (mode 1)
#rot.setValue(coin.SbVec3f(0,0,1),math.pi/2) # Z pointing upwards (mode 2 uncomment for use)
nrot = cam.orientation.getValue() * rot
cam.orientation = nrot
Gui.SendMsgToActiveView("ViewFit")
}}




