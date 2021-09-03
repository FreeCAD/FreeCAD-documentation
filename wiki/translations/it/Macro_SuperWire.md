 {{Macro/it
|Name=SuperWire
|Icon=Macro_SuperWire.png
|Translate=Forza Wire
|Description=Questa macro crea una polilinea da oggetti selezionati (linee e archi), anche quando i normali metodi di creazione delle polilinee, per esempio lo strumento di aggiornamento, non funzionano
|Author=Yorik
|Version=0.1
|Date=2012-05-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/e3/Macro_SuperWire.png ToolBar Icon]
}}

## Descrizione

Questa macro crea una polilinea da oggetti selezionati (linee e archi), anche quando i normali metodi di creazione delle polilinee, per esempio lo strumento di aggiornamento, non funzionano.

Attenzione, funziona solo con le versioni recenti di FreeCAD

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




