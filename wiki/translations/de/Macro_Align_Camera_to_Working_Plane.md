# Macro Align Camera to Working Plane/de
{{Macro
|Name=Macro Align Camera to Working Plane
|Icon=Macro_Align_Camera_to_Working_Plane.png
|Description=This macro aligns the camera to the current [Draft Working Plane](Draft_SelectPlane.md)
|Author=yorik
|Version=0.1
|Date=2017-03-16
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Align_Camera_to_Working_Plane.png ToolBar Icon]
|FCVersion=All
|SeeAlso=[Macro Align Working Plane to Camera](Macro_Align_Working_Plane_to_Camera.md) [<img src=images/Macro_Align_Working_Plane_to_Camera.png style="width:24px"> 
}}



## Beschreibung

Dieses Makro richtet die Kamera auf die aktuelle [Draft Arbeitsebene](Draft_SelectPlane/de.md) aus.



## Anwendung

-   Lege die [Draft Arbeitsebene](Draft_SelectPlane/de.md) entsprechend deiner Vorlieben fest.
-   Starte das Makro.



## Skript

Werkzeugleisten-Symbol ![](images/Macro_Align_Camera_to_Working_Plane.png )

**Macro_Align_Camera_to_Working_Plane.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
c = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
r = FreeCAD.DraftWorkingPlane.getRotation().Rotation.Q
c.orientation.setValue(r)
}}



---
⏵ [documentation index](../README.md) > Macro Align Camera to Working Plane/de
