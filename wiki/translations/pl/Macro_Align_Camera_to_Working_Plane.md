# Macro Align Camera to Working Plane/pl
{{Macro/pl
|Name=Makrodefinicja: Wyrównaj ujęcie widoku do płaszczyzny roboczej
|Icon=Macro_Align_Camera_to_Working_Plane.png
|Description=Za pomocą tej makrodefinicji ujęcie widoku jest wyrównywane do bieżącej [Płaszczyzny roboczej](Draft_SelectPlane.md).
|Author=yorik
|Version=0.1
|Date=2017-03-16
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Align_Camera_to_Working_Plane.png ToolBar Icon]
|FCVersion=Wszystkie
|SeeAlso=[Makrodefinicja: Wyrównaj płaszczyznę roboczą do ujęcia widoku](Macro_Align_Working_Plane_to_Camera/pl.md) [<img src=images/Macro_Align_Working_Plane_to_Camera.png style="width:24px"> 
}}

## Opis

Za pomocą tej makrodefinicji ujęcie widoku jest wyrównywane do bieżącej [Płaszczyzny roboczej](Draft_SelectPlane/pl.md).

## Użycie

-   Ustaw [Płaszczyznę roboczą](Draft_SelectPlane/pl.md) według własnych upodobań
-   Uruchom makrodefinicję

## Skrypt

Ikonka paska narzędzi ![](images/Macro_Align_Camera_to_Working_Plane.png )

**Macro_Align_Camera_to_Working_Plane.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
c = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
r = FreeCAD.DraftWorkingPlane.getRotation().Rotation.Q
c.orientation.setValue(r)
}}



---
⏵ [documentation index](../README.md) > Macro Align Camera to Working Plane/pl
