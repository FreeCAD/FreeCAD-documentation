---
- GuiCommand   *
   Name   *Arch PipeConnector
   MenuLocation   *Arch → Pipe Tools → Pipe Connector
   Workbenches   *[Arch](Arch_Workbench.md)
   Shortcut   ***P** **C**
   Version   *0.17
   SeeAlso   *[Arch Pipe](Arch_Pipe.md), [Arch Equipment](Arch_Equipment.md)
---

# Arch PipeConnector/pt-br

## Descrição

This tool allows to create corner or tee connection between two or three selected [Arch Pipes](Arch_Pipe.md).

## Utilização

1.  Select 2 or 3 [Arch Pipes](Arch_Pipe.md). If you are selecting 3 pipes, two of them must be exactly aligned.
2.  Press the **<img src="images/Arch_PipeConnector.svg" width=16px> [Arch PipeConnector](Arch_PipeConnector.md)** button, or press **P** then **C** keys.

## Propriedades

-    **Radius**   * The curvature radius of this connector

## Typical workflow 

See the information on [Arch Pipe](Arch_Pipe.md) for the workflow on using pipes and creating connectors.

## Scripting


**See also   ***

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Pipe Connector tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function   * 
```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```

-   Creates a `Connector` object from the given `pipes`, which is a list of [Arch Pipes](Arch_Pipe.md), and optionally a `radius` of curvature.
    -   The base objects ([Draft Wires](Draft_Wire.md)) of the [Arch Pipes](Arch_Pipe.md) should share an endpoint so they create a proper, smooth connector.

Example   * 
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





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/pt-br
