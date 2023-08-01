# Macro FlattenWire/sv
<div class="mw-translate-fuzzy">


{{Macro/sv
|Name=FlattenWire
|Translate=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=Detta makro flattar utkaststrådar som inte är planerade till sin median Z-koordinat
|Author=Yorik
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Deskription

Detta makro plattar ut ritlinjer som inte är parallella (i Z-axeln) till deras median Z koordinat.


</div>

## Script

ToolBar Icon ![](images/Macro_FlattenWire.png )

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
![](images/Button_right.svg) [documentation index](../README.md) > Macro FlattenWire/sv
