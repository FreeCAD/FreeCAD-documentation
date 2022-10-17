# Macro FaceToSketch/fr
{{Macro/fr
|Name=FaceToSketch
|Icon=Macro_FaceToSketch.png
|Description=Convertit une face en un sketch sans contraintes.
|Author=Jreinhardt
|Version=1.0
|Date=2013-12-23
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/6/6e/Macro_FaceToSketch.png ToolBar Icon]
}}

## Description

Cette macro décompose votre forme avec la fonction **<img src="images/Draft_Downgrade.svg" width=16px> [Draft Downgrade](Draft_Downgrade/fr.md)** et transforme la face sélectionnée en une esquisse sans contraintes et prête à être modifiée.

## Script

Icône de la barre d\'outils ![](images/Macro_FaceToSketch.png )

**Macro_FaceToSketch.FCMacro**


{{MacroCode|code=

import Draft
  
wires,_faces = Draft.downgrade(FreeCADGui.Selection.getSelection(),delete=True)
  
sketch = Draft.makeSketch(wires[0   *1])
for wire in wires[1   *]   *
    Draft.makeSketch([wire],addTo=sketch)
  
for wire in wires   *
    FreeCAD.ActiveDocument.removeObject(wire.Name)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FaceToSketch/fr
