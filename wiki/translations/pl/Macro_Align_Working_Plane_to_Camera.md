# Macro Align Working Plane to Camera/pl
{{Macro/pl
|Name=Makrodefinicja: Wyrównaj płaszczyznę roboczą do ujęcia widoku
|Icon=Macro_Align_Working_Plane_to_Camera.png
|Description=To makro przesuwa bieżącą [Plaszczyzne roboczą](Draft_SelectPlane/pl.md) na środek bieżącego widoku. Jest to przydatne, gdy pracujesz daleko od środka siatki.
|Author=yorik
|Version=1.0
|Date=2017-05-10
|Download=[https://www.freecadweb.org/wiki/images/0/01/Macro_Align_Working_Plane_to_Camera.png ToolBar Icon]
|FCVersion=All
|SeeAlso=_
}}

## Opis

To makro przesuwa bieżącą [Plaszczyzne roboczą](Draft_SelectPlane/pl.md) na środek bieżącego widoku. Jest to przydatne, gdy pracujesz daleko od środka siatki.

## Użycie

-   Przesuń widok do miejsca, na które chcesz spojrzeć
-   Uruchom makrodefinicję

## Skrypt

Ikonka paska narzędzi ![](images/Macro_Align_Working_Plane_to_Camera.png )

**Macro\_Align\_Working\_Plane\_to\_Camera.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
cam = FreeCAD.Vector(FreeCADGui.ActiveDocument.ActiveView.getCameraNode().position.getValue().getValue())
pos = FreeCAD.DraftWorkingPlane.projectPoint(cam)
FreeCAD.DraftWorkingPlane.position = pos
FreeCADGui.Snapper.setGrid()
}}

---
[documentation index](../README.md) > Macro Align Working Plane to Camera/pl
