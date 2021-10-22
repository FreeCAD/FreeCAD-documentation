# Macro FlattenWire/it
{{Macro/it
|Name=FlattenWire
|Translate=Wire appiattita su piano mediano
|Description=Questa macro appiattisce i contorni che non sono su un unico piano al valore mediano della loro coordinata Z
|Author=Yorik
|Version=1.0
|Date=2011-08-01
|FCVersion=Tutte
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Questa macro appiattisce i contorni che non sono su un unico piano al valore mediano della loro coordinata Z


</div>

## Script

ToolBar Icon ![](images/Macro_FlattenWire.png )

**Macro\_FlattenWire.FCMacro**


```python
import FreeCAD
obj = FreeCAD.ActiveDocument.ActiveObject
z = 0
for p in obj.Points: z += p.z
z = z/len(obj.Points)
newpoints = []
for p in obj.Points: newppoints.append(FreeCAD.Vector(p.x,p.y,z))
obj.Points = newppoints
```

---
[documentation index](../README.md) > Macro FlattenWire/it
