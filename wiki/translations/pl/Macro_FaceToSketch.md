# Macro FaceToSketch/pl
 {{Macro/pl
|Name=FaceToSketch
|Name/pl=Makrodefinicja FaceToSketch
|Icon=Macro_FaceToSketch.png
|Description=To makro rozbija twoją formę za pomocą funkcji Rozbij kształt środowiska Rysunek Roboczy i przekształca ścianę wybraną w szkicu bez ograniczeń, gotową do modyfikacji.
|Author=Jreinhardt
|Version=1.0
|Date=2013-12-23
|FCVersion=Wszystkie
|Download=[https://www.freecadweb.org/wiki/images/6/6e/Macro_FaceToSketch.png Ikonka paska narzędzi]
}}

## Opis

To makro rozbija twoją formę za pomocą funkcji **<img src="images/Draft_Downgrade.svg" width=16px> [Rozbij kształt](Draft_Downgrade/pl.md)** środowiska Rysunek Roboczy i przekształca ścianę wybraną w szkicu bez ograniczeń, gotową do modyfikacji.

## Tworzenie skryptów 

Ikonka paska narzędzi [mage:Macro\_FaceToSketch.png](mage:Macro_FaceToSketch.png.md)

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




