---
- GuiCommand:/es
   Name:Arch Pipe
   Name/es:Arch Pipe
   Workbenches:[Arch](Arch_Workbench/es.md)
   MenuLocation:Arch → Pipe Tools → Pipe
   Shortcut:P I
   SeeAlso:[Arch PipeConnector](Arch_PipeConnector.md)
   Version:0.17
---

# Arch Pipe/es


</div>

## Descripción


<div class="mw-translate-fuzzy">


<small>(v0.17)</small> 

Esta herramienta permite crear tuberías desde cero, o desde objetos seleccionados. Los objetos seleccionados deben estar basados en partes (borrador, boceto, etc.) y contener uno y solo un cable abierto.


</div>


<div class="mw-translate-fuzzy">

## Como utilizar 


</div>


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccione una forma lineal de [ Part](Part_Workbench.md) como [ Draft Line](Draft_Line.md), [ Draft Wire](Draft_Wire.md) o un [ Sketch](Sketcher_NewSketch.md)
2.  Presione el botón {{KEY | <img src="images/_Arch_Pipe.png_" width= 16px> [ Arch Pipe](Arch_Pipe_.md)}}, o presione {{KEY | P}} luego las teclas {{KEY | I}}


</div>

## Opciones

-   Pipes share the common properties and behaviours of all [Arch Components](Arch_Component.md)

## Properties

-    **Length**: Sets the length of this pipe, when it is not based on a wire

-    **Diameter**: The diameter of this pipe, when it is not based on a profile

-    **Base**: The base wire of this pipe, if any

-    **Profile**: The base profile of this pipe. If not given, the pipe is cylindrical.

## Typical workflow 

-   Start by placing sanitary/hydraulic appliance items (below is an imported step file). You turn these objects into Arch Equipments by selecting them, and pressing the [Arch Equipment](Arch_Equipment.md) button.

![](images/Arch_pipe_example_01.jpg )

-   Arch Equipments now have a new **SnapPoints** property, which is a list of 3D vectors. This allows you to add custom snap points, to which you can snap when the new [Draft Special](Draft_Snap_Special.md) snap button is turned on. Currently that property is only available to python, though. In the case above I added a new snap point at the exit of the wc appliance. The vectors inside SnapPoints appear on the model as white dots:

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   With the new [\"Snap Special\"](Draft_Snap_Special.md) Draft Snap, you can now snap to these custom points:

![](images/Arch_pipe_example_03.jpg )

-   Now we can draw our piping using Draft Lines, Draft Wires, or Sketches. The best way, though, is using only Draft Lines:

![](images/Arch_pipe_example_04.jpg )

-   There is now a new [Draft Slope](Draft_Slope.md) tool that allows to change the slope of Draft lines, to, for example, 5% (0.05). So we can quickly give our waste lines a correct slope. Only z coordinates are change by this tool, so we only need to snap them back to each other, the top projection will stay unchanged.

![](images/Arch_pipe_example_05.jpg )

-   We now only have to select all our lines, and press the [Arch Pipe](Arch_Pipe.md) button. Arch Pipe works with any Part-based object that contains one and only one open wire.

![](images/Arch_pipe_example_06.jpg )

-   We can now create connections by selecting 2 or 3 coincident tubes, and press the [Arch PipeConnector](Arch_PipeConnector.md) button. If 3 pipes are selected, two of them must be aligned in order to create a tee element:

![](images/Arch_pipe_example_07.jpg )

-   Changing the connectors radius doesn\'t change the length of the underlying base line, only the resulting tube (by changing their OffsetStart or OffsetEnd property). So you can still draw your line layout with only straight lines, without the need to care about curves and radius.

It is also possible to create Arch Pipes without a base line, in this case use its \"Length\" property to define the length.


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta de Tubería/Pipe se puede utilizar en [macros](macros/es.md) y desde la consola de Python mediante la utilización de las siguientes funciones:


</div>


```python
Pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `Pipe` object from the given `baseobj` and `diameter`.
    -   
        `baseobj`
        
        is a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).

    -   If `baseobj` is omitted, a straight pipe can be created with just the `diameter` and the `length` in the Z direction.
-   If a `placement` is given, it is used.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
Line = Draft.makeWire([p1, p2, p3, p4])

Pipe = Arch.makePipe(Line, 200)
FreeCAD.ActiveDocument.recompute()

Pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/es
|[Arch CompPipe](Arch_CompPipe/es.md)
|[Pipe Connector](Arch_PipeConnector/es.md)
|[Arch](Arch_Workbench/es.md)
|IconL=Arch_CompPipe.png
|IconC=Workbench_Arch.svg
|IconR=Arch_PipeConnector.svg
}}


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Pipe/es
