# Macro FlattenWire
{{Macro
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=This macro flattens draft wires that are not planar to their median Z coordinate
|Author=Yorik
|Version=1.1
|Date=2021-10-27
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Description

This macro flattens draft wires that are not planar to their median Z coordinate.

## Script

ToolBar Icon  ![](images/Macro_FlattenWire.png )

**Macro\_FlattenWire.FCMacro**


```python
import FreeCAD
obj = FreeCAD.ActiveDocument.ActiveObject
z = 0
for p in obj.Points: z += p.z
z = z/len(obj.Points)
newpoints = []
for p in obj.Points: newpoints.append(FreeCAD.Vector(p.x, p.y, z))
obj.Points = newpoints
```

---
[documentation index](../README.md) > Macro FlattenWire
