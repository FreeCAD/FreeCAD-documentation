---
- GuiCommand:/ro
   Name:Arch PipeConnector
   MenuLocation:Arch → Pipe Tools → Pipe Connector
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:**P** **C**
   SeeAlso:[Arch Equipment/ro](Arch_Pipe/ro]],_[[Arch_Equipment.md)
   Version:0.17
---

# Arch PipeConnector/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">


<small>(v0.17)</small> 

Acest instrument permite crearea unui conector de colț sau T între două sau trei [ Arc Pipes](Arch_Pipe.md) selectate.


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați 2 sau 3 [Arch Pipes](Arch_Pipe.md). Dacă selectați 3 pipes, două dintr ele trebuiesc aliniate exact.
2.  apăsați butonul **<img src="images/Arch_PipeConnector.png" width=16px> [[Arch PipeConnector]]
** , sau în ordine tastele **P** apoi **C**


</div>

## Proprietăți

-    **Radius**: Raza curburii acestui conector

## Fluxul de lucru tipic 


<div class="mw-translate-fuzzy">

See [Arch Pipe#Typical_workflow](Arch_Pipe#Typical_workflow.md)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Pipe Connector poate fi utilizat în [macros](macros.md) și de la consola Python folosind următoarea funcție:


</div>


```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```

-   Creates a `Connector` object from the given `pipes`, which is a list of [Arch Pipes](Arch_Pipe.md), and optionally a `radius` of curvature.
    -   The base objects ([Draft Wires](Draft_Wire.md)) of the [Arch Pipes](Arch_Pipe.md) should share an endpoint so they create a proper, smooth connector.

Example: 
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


{{docnav/ro|[Pipe](Arch_Pipe.md)|[Arch CompSetMaterial](Arch_CompSetMaterial.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Pipe.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompSetMaterial.png}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/ro
