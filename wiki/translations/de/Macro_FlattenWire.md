# Macro FlattenWire/de
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

## Description


<div class="mw-translate-fuzzy">

## Desorption

Dieser Makroentwurf ist nicht bindend für den Median


</div>

## Skript

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
[documentation index](../README.md) > Macro FlattenWire/de
