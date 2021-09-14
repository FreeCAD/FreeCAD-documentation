# Macro FaceToSketch/de

 {{Macro/de
|Name=FaceToSketch
|Name/de=FlächeZuSkizze
|Icon=Macro_FaceToSketch.png
|Description=Dieses Makro zerlegt Ihre Form mit der Funktion Entwurf Herabstufen und transformiert die in einer Skizze ausgewählte Fläche ohne Beschränkungen und bereit zur Änderung.
|Author=Jreinhardt
|Version=1.0
|Date=2013-12-23
|FCVersion=Alle
|Download=[https://www.freecadweb.org/wiki/images/6/6e/Macro_FaceToSketch.png WerkzeugLeisten Symbol]
}}

## Beschreibung

Dieses Makro zerlegt deine Form mit der Funktion **<img src="images/Draft_Downgrade.svg" width=16px> [Enwurf Herabstufen](Draft_Downgrade/de.md)** und überführt die gewählte Fläche in eine Skizze ohne Beschränkungen, die dann bearbeitet werden kann.

## Skript

Werkzeugleistensymbol ![](images/Macro_FaceToSketch.png )

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




