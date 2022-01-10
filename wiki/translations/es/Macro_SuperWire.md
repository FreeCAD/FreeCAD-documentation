# Macro SuperWire/es
{{Macro/es
|Name=SuperWire
|Translate=SuperWire
|Icon=Macro_SuperWire.png
|Description=Esta macro crea una polilínea a partir de los objetos seleccionados (líneas y arcos) incluso si los métodos habituales de creación de polilíneas fallan (por ejemplo la herramienta Promocionar)
|Author=Yorik
|Version=0.1
|Date=2012-05-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/e3/Macro_SuperWire.png ToolBar Icon]
}}

## Description


<div class="mw-translate-fuzzy">

## Descriptivo

Esta macro crea una polilínea a partir de los objetos seleccionados (líneas y arcos) incluso si los métodos habituales de creación de polilíneas fallan (por ejemplo la herramienta Promocionar)


</div>

Atención, necesitas una versión reciente de FreeCAD para que esto funcione

## Rescripto

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
[documentation index](../README.md) > Macro SuperWire/es
