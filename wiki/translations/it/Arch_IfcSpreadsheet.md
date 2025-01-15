---
 GuiCommand:
   Name: Arch IfcSpreadsheet
   Name/it: Crea foglio di calcolo Ifc
   MenuLocation: Arch , Utilità , Crea foglio di calcolo Ifc...
   Workbenches: Arch_Workbench/it
   Shortcut: **I** **P**
   SeeAlso: Arch_IFC/it, Arch_IfcExplorer/it
---

# Arch IfcSpreadsheet/it


</div>



## Descrizione

Questo strumento crea un foglio di calcolo per memorizzare le proprietà [IFC](Arch_IFC/it.md) di un oggetto.



## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto.
2.  Richiamare il comando utilizzando uno di questi metodi:
    -   Premereil pulsante **<img src="images/Arch_IfcSpreadsheet.svg" width=16px> Crea un foglio di calcolo IFC** nella barra degli strumenti.
    -   Usare la scorciatoia da tastiera **I** **P**.
    -   Usare la voce **Arch → Utilità → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Crea un foglio di calcolo IFC** del menu principale.


</div>



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
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





</div>



---
⏵ [documentation index](../README.md) > Arch IfcSpreadsheet/it
