# Macro Rotate ViewAxonometric/it
{{Macro/it
|Name=Macro Rotate ViewAxonometric
|Icon=Macro_Rotate_View_with_Y_pointing_upwards_.png
|Description=Questa macro ruota la vista corrente in ViewAxonometric (come è: Y).
|Author=Yorik
|Version=01.00
|FCVersion=All
|Download= [https://www.freecadweb.org/wiki/images/2/2e/Macro_Rotate_View_with_Y_pointing_upwards_.png Macro_Rotate_View_with_Y_pointing_upwards_]<br />[https://www.freecadweb.org/wiki/images/a/a2/Macro_Rotate_View_with_Z_pointing_upwards_.png Macro_Rotate_View_with_Z_pointing_upwards_]
|Date=2010-11-17
|SeeAlso=[Macro Rotate View](Macro_Rotate_View/it.md) [<img src=images/Macro_Rotate_View_view_90_Degrees.png style="width:24px">
}}

## Descrizione

Questa macro ruota la vista corrente in ViewAxonometric (come è: Y).

Avete due opzioni:

-   modo 1: vista assonometrica con Y rivolta verso l\'alto ![vista assonometrica con Y rivolta verso l\'alto](images/_Macro_Rotate_View_with_Y_pointing_upwards_.png ) modalità 1
-   modo 2: vista assonometrica con Z rivolta verso l\'alto ![vista assonometrica con Z rivolta verso l\'alto](images/_Macro_Rotate_View_with_Z_pointing_upwards_.png ) modalità 2 (commento per l\'uso)


<div class="mw-translate-fuzzy">

## Utilizzo


</div>

Per utilizzare le due macro, copiare la prima macro e denominarla \"**Macro\_Rotate\_ViewAxonometric\_Y**\" (modo 1) senza modificare il codice e utilizzare questa icona ![vista assonometrica con Y rivolta verso l\'alto](images/_Macro_Rotate_View_with_Y_pointing_upwards_.png )

Copia la seconda macro e chiamala \"**Macro\_Rotate\_ViewAxonometric\_Z**\" (modo 2) e:

commenta la linea


{{ColoredText|'''11''' **#rot.setValue(coin.SbVec3f(1,0,0),-math.pi/2) # Y pointing upwards (mode 1)** }}

e decommenta la linea


{{ColoredText|'''12''' **rot.setValue(coin.SbVec3f(0,0,1),math.pi/2) # Z pointing upwards (mode 2 uncomment for use)** }}

and use this icon ![axonometric view with Z pointing upwards](images/Macro_Rotate_View_with_Z_pointing_upwards_.png )

## Script

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

---
[documentation index](../README.md) > Macro Rotate ViewAxonometric/it
