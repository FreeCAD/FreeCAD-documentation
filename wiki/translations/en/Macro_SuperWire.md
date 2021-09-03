 {{Macro
|Name=SuperWire
|Icon=Macro_SuperWire.png
|Description=This macro creates a wire from selected objects (lines and arcs) even where normal wire creation methods (for example the upgrade tool) fail. Attention, you need a recent version of FreeCAD for this to work
|Author=Yorik
|Version=0.1
|Date=2012-05-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/e3/Macro_SuperWire.png ToolBar Icon]
}}

## Description

This macro creates a wire from selected objects (lines and arcs) even where normal wire creation methods (for example the upgrade tool) fail.

Attention, you need a recent version of FreeCAD for this to work

## Script

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




