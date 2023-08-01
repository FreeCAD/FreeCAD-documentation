---
- GuiCommand:
   Name: Arch PipeConnector
   Name/es: Arch PipeConnector
   MenuLocation: Arch - Pipe Tools - Pipe Connector
   Workbenches: [Arch](Arch_Workbench/es.md)
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: [Arch Pipe](Arch_Pipe/es.md), [Arch Equipment](Arch_Equipment/es.md)
---

# Arch PipeConnector/es

## Descripción


<div class="mw-translate-fuzzy">


{{Version/es|0.17}}

Esta herramienta permite crear una conexión de esquina o de salida en T entre dos o tres [Arch Pipes](Arch_Pipe/es.md) seleccionados.


</div>

## Como utilizar 


<div class="mw-translate-fuzzy">

1.  Seleccione 2 o 3 [Arch Pipes](Arch_Pipe/es.md). Si selecciona 3 tubos, dos de ellos deben estar exactamente alineados.
2.  Presione el botón **<img src="images/_Arch_PipeConnector.png" width=16px> [Arch PipeConnector](Arch_PipeConnector/es.md)
**, o presione **P** y luego la tecla **C**


</div>

### Propiedades

-    {{PropertyData/es|Radius}}: El radio de curvatura de este conector

## Flujo de trabajo típico 


<div class="mw-translate-fuzzy">

Ver [Arch Pipe#Typical_workflow](Arch_Pipe#Typical_workflow.md)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta conector de tubería se puede usar en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


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


{{docnav/es|[Pipe](Arch_Pipe.md)|[Arch CompSetMaterial](Arch_CompSetMaterial.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Pipe.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompSetMaterial.png}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/es
