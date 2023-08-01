# Macro FaceToSketch/it
{{Macro/it
|Name=FaceToSketch
|Translate=Da Faccia a Schizzo
|Icon=Macro_FaceToSketch.png
|Description=Converte la faccia selezionata in uno Sketch senza vincoli.
|Author=Jreinhardt
|Version=1.0
|Date=2013-12-23
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/6e/Macro_FaceToSketch.png ToolBar Icon]
}}

## Descrizione

Questa macro rompe la forma con la funzione **<img src="images/Draft_Downgrade.svg" width=16px> [Draft Downgrade](Draft_Downgrade/it.md)** e trasforma la faccia selezionata in uno schizzo senza vincoli e pronto per essere modificato.

## Script

Icona barra strumenti ![](images/Macro_FaceToSketch.png )

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
![](images/Button_right.svg) [documentation index](../README.md) > Macro FaceToSketch/it
