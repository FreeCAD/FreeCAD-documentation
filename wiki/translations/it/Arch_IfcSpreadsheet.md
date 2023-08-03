---
 GuiCommand:
   Name: Arch_MakeIfcSpreadsheet
   Name/it: Crea un foglio di calcolo Ifc
   Icon: Arch_Schedule.svg
   MenuLocation: Arch , Utilità , Crea un foglio di calcolo Ifc...
   Workbenches: Arch_Workbench/it
   Shortcut: **I** **P**
   SeeAlso: Arch IFC/it, Arch IfcExplorer/it
---

# Arch IfcSpreadsheet/it


</div>

## Descrizione

Questo strumento crea un foglio di calcolo per memorizzare le proprietà [IFC](Arch_IFC/it.md) di un oggetto.

## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto.
2.  Richiamare il comando utilizzando uno di questi metodi:
    -   Premereil pulsante **<img src="images/Arch_Schedule.svg" width=16px> Crea un foglio di calcolo IFC** nella barra degli strumenti.
    -   Usare la scorciatoia da tastiera **I** **P**.
    -   Usare la voce **Arch → Utilità → <img src="images/Arch_Schedule.svg" width=16px> Crea un foglio di calcolo IFC** del menu principale.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
spreadsheet = makeIfcSpreadsheet(archobj=None)
```

-   Crea un oggetto `spreadsheet`. Optionalmente può essere dato un `archobj`.

Esempio: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

spreadsheet = Arch.makeIfcSpreadsheet(Wall)
```


<div class="mw-translate-fuzzy">


{{docnav/it
|[3 Viste da mesh](Arch_3Views/it.md)
|[Mostra/Nascondi i sotto-componenti](Arch_ToggleSubs/it.md)
|[Arch](Arch_Workbench/it.md)
|IconL=Arch_3Views.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_ToggleSubs.svg
}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch IfcSpreadsheet/it
