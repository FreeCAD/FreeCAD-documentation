# Macro FlattenWire/pl
{{Macro/pl
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=To makro dokonuje spłaszczenia projektów polilinii, które nie są planarne względem ich środkowej współrzędnej Z.
|Author=Yorik
|Version=1.1
|Date=2021-10-27
|FCVersion=Wszystkie
|Download=[https   *//www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Opis

To makro dokonuje spłaszczenia projektów polilinii, które nie są planarne względem ich środkowej współrzędnej Z.

## Tworzenie skryptów 

Ikonka paska narzędzi ![](images/Macro_FlattenWire.png )

**Macro\_FlattenWire.FCMacro**


{{MacroCode|code=
import FreeCAD
obj = FreeCAD.ActiveDocument.ActiveObject
z = 0
for p in obj.Points   * z += p.z
z = z/len(obj.Points)
newpoints = []
for p in obj.Points   * newpoints.append(FreeCAD.Vector(p.x, p.y, z))
obj.Points = newpoints
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FlattenWire/pl
