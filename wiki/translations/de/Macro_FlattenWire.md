# Macro FlattenWire/de
<div class="mw-translate-fuzzy">


{{Macro/de
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=Dieses Makro glättet Zugdrähte, die nicht auf ihre mittlere Z-Koordinate ausgerichtet sind
|Author=Yorik
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Desorption

Dieser Makroentwurf ist nicht bindend für den Median


</div>

## Skript

ToolBar Icon ![](images/Macro_FlattenWire.png )

**Macro\_FlattenWire.FCMacro**


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
