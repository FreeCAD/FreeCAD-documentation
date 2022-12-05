# Macro FaceToSketch/cs
{{Macro/cs
|Name=FaceToSketch
|Translate=FaceToSketch
|Icon=Macro_FaceToSketch.png
|Description=Konvertuje povrch do náčrtu bez vazeb.
|Author=Jreinhardt
|Version=1.0
|Date=2013-12-23
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/6e/Macro_FaceToSketch.png ToolBar Icon]
}}


<div class="mw-translate-fuzzy">

## Description

Toto makro rozloží tvar funkcí **<img src="images/Draft_Downgrade.png" width=16px> [[Draft Downgrade]]** a transformuje povrch vybraný v náčrtu bez vazeb s možností dalších úprav.


</div>

## Script

ToolBar Icon ![](images/Macro_FaceToSketch.png )

**Macro_FaceToSketch.FCMacro**


{{MacroCode|code=

import Draft
  
wires,_faces = Draft.downgrade(FreeCADGui.Selection.getSelection(),delete=True)
  
sketch = Draft.makeSketch(wires[0:1])
for wire in wires[1:]:
    Draft.makeSketch([wire],addTo=sketch)
  
for wire in wires:
    FreeCAD.ActiveDocument.removeObject(wire.Name)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FaceToSketch/cs
