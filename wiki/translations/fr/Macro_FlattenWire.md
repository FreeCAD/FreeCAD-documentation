# Macro FlattenWire/fr
 {{Macro/fr
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=Cette macro aplatit les fils (Wire) du projet qui ne sont pas plan à la médiane de leurs coordonnées z
|Author=Yorik|Version=1.0
|Date=2011-08-01
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Description

Cette macro aplatit les fils (Wire) du projet qui ne sont pas plan à la médiane de leurs coordonnées z

## Script

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




