 {{Macro/de
|Name=SuperWire
|Icon=Macro_SuperWire.png
|Description=Dieses Makro erstellt einen Draht aus ausgewählten Objekten (Linien und Bögen), auch wenn normale Drahtherstellungsmethoden (z. B. das Upgrade-Tool) fehlschlagen
|Author=Yorik
|Version=0.1
|Date=2012-05-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/e3/Macro_SuperWire.png ToolBar Icon]
}}

## Beschreibung

Dieses Makro erstellt einen Draht aus ausgewählten Objekten (Linien und Bögen), in denen normale Draht-Erstellungsverfahren fehlschlagen.
Achtung, Sie benötigen eine aktuelle Version von FreeCAD, damit dies funktioniert.

Achtung, Sie benötigen eine aktuelle Version von FreeCAD, damit dies funktioniert.

## Skript

ToolBar Icon ![](images/Macro_SuperWire.png )

**Macro\_SuperWire.FCMacro**


{{MacroCode|code=

import FreeCAD,FreeCADGui,Part
try:
    import DraftGeomUtils as fcgeo
except:
    from draftlibs import fcgeo

sel = FreeCADGui.Selection.getSelection()
if not sel:
   FreeCAD.Console.PrintWarning("Select something first!")
else:
   elist = []
   for obj in sel:
       if hasattr(obj,"Shape"):
           elist.append(obj.Shape.Edges[0])
   wire = fcgeo.superWire(elist)
   if wire:
       Part.show(wire)
   else:
       FreeCAD.Console.PrintError("SuperWire operation failed!")

}}




