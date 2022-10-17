# Macro Rotate View Free/ru
{{Macro
|Name=Rotate View Free
|Icon=Text_console_python.png
|Description=This def pasted in the Python console FreeCAD (or your macro) allows you to rotate the view in 3-axis and the angle (in degrees) give interesting to create a plan to a desired position
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|SeeAlso=[Macro Rotate View](Macro_Rotate_View.md) [<img src=images/Macro_Rotate_View_view_90_Degrees.png style="width   *24px"><br />[Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric.md) [<img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width   *24px"> [<img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width   *24px">
}}

## Описание

This def pasted in the Python console FreeCAD (or your macro) allows you to rotate the view in 3-axis and the angle (in degrees) give interesting to create a plan to a desired position

## Применение

Paste the code in the Python console FreeCAD and type **Enter** → **Enter** (for validate) and tip ex   * {{ColoredText|**RotateView(0,1,0,45)** }}

## Скрипт

**Macro_Rotate_View_Free.FCMacro**


{{MacroCode|code=
#Paste in the Python console and tip ex   *
#RotateView(0,1,0,45)
def RotateView(axisX=1.0,axisY=0.0,axisZ=0.0,angle=45.0)   *
    import math
    from pivy import coin
    try   *
        cam = Gui.ActiveDocument.ActiveView.getCameraNode()
        rot = coin.SbRotation()
        rot.setValue(coin.SbVec3f(axisX,axisY,axisZ),math.radians(angle))
        nrot = cam.orientation.getValue() * rot
        cam.orientation = nrot
        print( axisX," ",axisY," ",axisZ," ",angle)
    except Exception   *
        print( "Not ActiveView ")


}}

tip in the console ex    *


{{MacroCode|code=
RotateView(0,1,0,45)
}}

If there is not open document an error is returned



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Rotate View Free/ru
