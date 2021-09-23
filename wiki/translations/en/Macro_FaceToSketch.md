# Macro FaceToSketch/en
 {{Macro
|Name=FaceToSketch
|Icon=Macro_FaceToSketch.png
|Description=This macro breaks down your form with function Draft Downgrade and transforms the face selected in a sketch without constraints, and ready to be modified.
|Author=Jreinhardt
|Version=1.0
|Date=2013-12-23
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/6e/Macro_FaceToSketch.png ToolBar Icon]
}}

## Description

This macro breaks down your form with function **<img src="images/Draft_Downgrade.svg" width=16px> [[Draft Downgrade]]** and transforms the face selected in a sketch without constraints, and ready to be modified.

## Script

ToolBar Icon ![](images/Macro_FaceToSketch.png )

**Macro\_FaceToSketch.FCMacro**


{{MacroCode|code=

import Draft
  
wires,_faces = Draft.downgrade(FreeCADGui.Selection.getSelection(),delete=True)
  
sketch = Draft.makeSketch(wires[0:1])
for wire in wires[1:]:
    Draft.makeSketch([wire],addTo=sketch)
  
for wire in wires:
    FreeCAD.ActiveDocument.removeObject(wire.Name)
}}




