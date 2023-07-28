# Macro FlattenWire/de
{{Macro/de
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=Dieses Makro glättet Draft-Drähte, die nicht planar bezüglich ihrer mittlere Z-Koordinate ausgerichtet sind
|Author=Yorik
|Version=1.1
|Date=2021-10-27
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}



## Beschreibung

Dieses Makro glättet Draft-Drähte, die nicht planar bezüglich ihrer mittleren Z-Koordinate ausgerichtet sind



## Skript

Werkzeugleisten-Symbol ![](images/Macro_FlattenWire.png )

**Macro_FlattenWire.FCMacro**


{{MacroCode|code=
import FreeCAD
obj = FreeCAD.ActiveDocument.ActiveObject
z = 0
for p in obj.Points: z += p.z
z = z/len(obj.Points)
newpoints = []
for p in obj.Points: newpoints.append(FreeCAD.Vector(p.x, p.y, z))
obj.Points = newpoints
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FlattenWire/de
