---
- GuiCommand   */it
   Name   *Arch PipeConnector
   Name/it   *Raccordo
   MenuLocation   *Arch → Tubazioni → Raccordo
   Workbenches   *[Arch](Arch_Workbench/it.md)
   Shortcut   ***P** **C**
   Version   *0.17
   SeeAlso   *[Tubo](Arch_Pipe/it.md), [Arredo](Arch_Equipment/it.md)
---

# Arch PipeConnector/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea una connessione a angolo o un tee (raccordo) tra 2 o 3 [Tubi](Arch_Pipe/it.md) selezionati .


</div>

## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare 2 o 3 [Tubi Arch](Arch_Pipe/it.md). Se si selezionano 3 tubi, due di loro devono essere perfettamente allineati.
2.  Premere il pulsante **<img src="images/Arch_PipeConnector.svg" width=16px> [Raccordo](Arch_PipeConnector/it.md)**, o premere **P** e poi **C**.


</div>

## Proprietà

-    {{PropertyData/it|Radius}}   * Il raggio di curvatura del raccordo

## Flusso di lavoro tipico 


<div class="mw-translate-fuzzy">

Vedere in [Tubo](Arch_Pipe/it.md) le informazioni per il flusso di lavoro sull\'uso dei tubi e la creazione di raccordi.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche   ***

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Pipe Connector può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione   *


</div>


```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Connector` dai `pipes` dati, che sono una lista di [Tubi](Arch_Pipe/it.md), e facoltativamente un `radius` di curvatura.
    -   Gli oggetti di base [Wire](Draft_Wire/it.md) dei [Tubi](Arch_Pipe/it.md) dovrebbero condividere un punto finale per creare un raccordo corretto e regolare.


</div>

Esempio   * 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(-1000, 0, 0)
p2 = FreeCAD.Vector(-2000, 0, 0)
p3 = FreeCAD.Vector(-2000, 0, 0)
p4 = FreeCAD.Vector(-2000, -1000, 0)
p5 = FreeCAD.Vector(-2000, -1000, 0)
p6 = FreeCAD.Vector(-4000, -1000, 0)
Line1 = Draft.makeWire([p1, p2])
Line2 = Draft.makeWire([p3, p4])
Line3 = Draft.makeWire([p5, p6])

Pipe1 = Arch.makePipe(Line1, 150)
Pipe2 = Arch.makePipe(Line2, 150)
Pipe3 = Arch.makePipe(Line3, 150)
FreeCAD.ActiveDocument.recompute()

Conn = Arch.makePipeConnector([Pipe1, Pipe2])
Conn2 = Arch.makePipeConnector([Pipe2, Pipe3])
FreeCAD.ActiveDocument.recompute()

Line4 = Draft.move(Line1, FreeCAD.Vector(-500, 1000, 0), copy=True)
Line5 = Draft.move(Line2, FreeCAD.Vector(-500, 1000, 0), copy=True)
Pipe4 = Arch.makePipe(Line4, 100)
Pipe5 = Arch.makePipe(Line5, 100)
FreeCAD.ActiveDocument.recompute()

Conn3 = Arch.makePipeConnector([Pipe4, Pipe5], radius=400)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/it
|[Tubo](Arch_Pipe/it.md)
|[Materiali](Arch_CompSetMaterial/it.md)
|[Arch](Arch_Workbench/it.md)
|IconL=Arch_Pipe.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_CompSetMaterial.png
}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/it
