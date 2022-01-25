# Macro SuperWire/cs
{{Macro/cs
|Name=SuperWire
|Translate=SuperWire
|Icon=Macro_SuperWire.png
|Description=Toto makro vytváří drát (lomenou čáru) z vybraných objektů (přímek a oblouků) i v případech kdy běžné metody pro vytváření drátů (např. nástroj pro aktualizaci) selžou
|Author=Yorik
|Version=0.1
|Date=2012-05-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/e3/Macro_SuperWire.png ToolBar Icon]
}}

## Description


<div class="mw-translate-fuzzy">

## Deskriptivní

Toto makro vytváří drát (lomenou čáru) z vybraných objektů (přímek a oblouků) i v případech kdy běžné metody pro vytváření drátů (např. nástroj pro aktualizaci) selžou.


</div>

Pozor, aby to fungovalo, potřebujete nejnovější verzi FreeCADu.

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro SuperWire/cs
