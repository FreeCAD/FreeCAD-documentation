# Macro FlattenWire/pl
{{Macro/pl
|Name=FlattenWire
|Icon=Macro_FlattenWire.png
|Description=To makro dokonuje spłaszczenia projektów polilinii, które nie są płaskie względem ich środkowej współrzędnej Z.
|Author=Yorik
|Version=1.0
|Date=2011-08-01
|FCVersion=Wszystkie
|Download=[https://www.freecadweb.org/wiki/images/2/2f/Macro_FlattenWire.png ToolBar Icon]
}}

## Opis

To makro dokonuje spłaszczenia projektów polilinii, które nie są płaskie względem ich środkowej współrzędnej Z.

## Tworzenie skryptów 

Ikonka paska narzędzi ![](images/Macro_FlattenWire.png )

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
[documentation index](../README.md) > Macro FlattenWire/pl
