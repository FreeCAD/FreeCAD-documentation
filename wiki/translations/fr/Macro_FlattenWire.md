# Macro FlattenWire/fr
{{Macro/fr
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=Cette macro aplatit les Draft fils qui ne sont pas planaires à leur coordonnée Z médiane.
|Author=Yorik
|Version=1.1
|Date=2021-10-27
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png Icône de la barre d'outils]
}}

## Description

Cette macro aplatit les Draft fils qui ne sont pas planaires à leur coordonnée Z médiane.

## Script

Icône de la barre d\'outils ![](images/Macro_FlattenWire.png )

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
⏵ [documentation index](../README.md) > Macro FlattenWire/fr
