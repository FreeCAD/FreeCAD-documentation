# Macro Rotate View/fr
{{Macro/fr
|Name=Macro Rotate View by 90°
|Name/fr=Macro Rotate View by 90°
|Icon=Macro Rotate View view 90 Degrees.png
|Description=Cette macro fait pivoter l'affichage actuel de 90 ° vers la gauche. Ne fonctionne que si vous êtes en [vue de dessus](Std_ViewTop/fr.md).
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=Toutes
|Download=[https://wiki.freecad.org/images/a/a0/Macro_Rotate_View_view_90_Degrees.png Icône de la barre d'outils]
|SeeAlso=[Macro Rotate ViewAxonometric](Macro_Rotate_ViewAxonometric/fr.md), [Macro Rotate View Free](Macro_Rotate_View_Free/fr.md)
}}

## Description

Cette macro fait pivoter l\'affichage actuel de 90 ° vers la gauche.

## Limitations

Ne fonctionne que si vous êtes en vue de dessus: ![Std_ViewTop\|16px\|link=Std_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop/fr.md)

## Script

Icône de la barre d\'outils ![](images/Macro_Rotate_View_view_90_Degrees.png )

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
⏵ [documentation index](../README.md) > Macro Rotate View/fr
