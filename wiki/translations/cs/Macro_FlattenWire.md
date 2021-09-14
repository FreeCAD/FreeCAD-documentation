# Macro FlattenWire/cs

 {{Macro/cs
|Name=FlattenWire
|Translate=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=Toto makro vyrovnává vodiče průvanu, které nejsou rovinné k jejich středové souřadnici Z
|Author=Yorik
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Deskriptivní

Toto makro vyrovná nakreslený drát, který není vyrovnán (není v jedné rovině), do roviny, která odpovídá střední výšce nevyrovnaných drátů.

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
for p in obj.Points: newppoints.append(FreeCAD.Vector(p.x,p.y,z))
obj.Points = newppoints

}}




