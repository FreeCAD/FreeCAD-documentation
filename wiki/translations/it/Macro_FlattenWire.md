# Macro FlattenWire/it
{{Macro/it
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Translate=Wire appiattita su piano mediano
|Description=Questa macro appiattisce i contorni che non sono su un unico piano al valore mediano della loro coordinata Z
|Author=Yorik
|Version=1.1
|Date=2021-10-27
|FCVersion=Tutte
|Download=[https   *//www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Descrizione

Questa macro appiattisce i contorni che non sono su un unico piano al valore mediano della loro coordinata Z

## Script

Icona barra strumenti ![](images/Macro_FlattenWire.png )

**Macro_FlattenWire.FCMacro**


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
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FlattenWire/it
