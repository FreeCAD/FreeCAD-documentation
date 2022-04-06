# Macro Rotate ViewAxonometric/fr
{{Macro/fr
|Name=Macro Rotate ViewAxonometric
|Icon=Macro_Rotate_View_with_Y_pointing_upwards_.png
|Description=Cette macro pivote la vue dans la position axonométrique (2 posibilités, Y et Z).
|Author=Yorik
|Version=01.00
|FCVersion=Toutes
|Download= [https://www.freecadweb.org/wiki/images/2/2e/Macro_Rotate_View_with_Y_pointing_upwards_.png Macro_Rotate_View_with_Y_pointing_upwards_]<br />[https://www.freecadweb.org/wiki/images/a/a2/Macro_Rotate_View_with_Z_pointing_upwards_.png Macro_Rotate_View_with_Z_pointing_upwards_]
|Date=2010-11-17
|SeeAlso=[Macro Rotate View](Macro_Rotate_View/fr.md) [<img src=images/Macro_Rotate_View_view_90_Degrees.png style="width:24px">
}}

## Description

Cette macro pivote la vue dans la position axonométrique (tel quel: Y).

Vous avez deux options:

-   mode 1 : axonometric vue Y ![axonometric view with Y pointing upwards](images/Macro_Rotate_View_with_Y_pointing_upwards_.png ) mode 1
-   mode 2 : axonometric vue Z ![axonometric view with Z pointing upwards](images/Macro_Rotate_View_with_Z_pointing_upwards_.png ) mode 2 (dé-commenter pour utiliser)

## Utilisation

Pour utiliser les deux macros, copiez la première macro et nommez-la \"**Macro\_Rotate\_ViewAxonometric\_Y**\" (mode 1) sans changer le code et utilisez cette icône ![axonometric view with Y pointing upwards](images/Macro_Rotate_View_with_Y_pointing_upwards_.png ).

Copiez la seconde macro et namez la \"**Macro\_Rotate\_ViewAxonometric\_Z**\" (mode 2) and:

commentez la ligne


{{ColoredText|'''11''' **#rot.setValue(coin.SbVec3f(1,0,0),-math.pi/2) # Y pointing upwards (mode 1)** }}

et décommettez la ligne


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
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Rotate ViewAxonometric/fr
