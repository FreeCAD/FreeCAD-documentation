---
- GuiCommand:
   Name:Arch Pipe
   Name/ja:Arch Pipe
   Workbenches:[Arch](Arch_Module.md)
   MenuLocation:Arch - Pipe Tools - Pipe
   Shortcut:**P** **I**
   SeeAlso:[Arch PipeConnector](Arch_PipeConnector/ja.md)
   Version:0.17
---

# Arch Pipe/ja


</div>

## 説明


<div class="mw-translate-fuzzy">


<small>(v0.17)</small> 

このツールを使用すると、最初から、または選択したオブジェクトからパイプを作成できます。選択されたオブジェクトは、パーツベース（Draft/ドラフト、Sketch/スケッチなど）でなければならず、開いているWire/ワイヤが1つだけです。


</div>


<div class="mw-translate-fuzzy">

## 使用方法


</div>

1.  Optionally, select a linear [Part](Part_Workbench.md) shape such as a [Draft Line](Draft_Line.md), a [Draft Wire](Draft_Wire.md) or an open [Sketch](Sketcher_NewSketch.md).
2.  Invoke this command using several methods:
    -   Pressing the **<img src="images/Arch_Pipe.svg" width=16px> [Arch Pipe](Arch_Pipe.md)** button on the toolbar.
    -   Pressing the **P** then **I** keyboard shortcut.
    -   Pressing the **Arch → Pipe Tools → Pipe** entry from the top menu.

## オプション

-   Pipes share the common properties and behaviours of all [Arch Components](Arch_Component.md)

## プロパティ

-    **Length**: Sets the length of this pipe, when it is not based on a wire

-    **Diameter**: The diameter of this pipe, when it is not based on a profile

-    **Base**: The base wire of this pipe, if any

-    **Profile**: The base profile of this pipe. If not given, the pipe is cylindrical.

## 典型的なワークフロー

-   Start by placing sanitary/hydraulic appliance items (below is an imported step file). You turn these objects into Arch Equipments by selecting them, and pressing the [Arch Equipment](Arch_Equipment.md) button.

![](images/Arch_pipe_example_01.jpg )

-   Arch Equipments now have a new **SnapPoints** property, which is a list of 3D vectors. This allows you to add custom snap points, to which you can snap when the new [Draft Special](Draft_Snap_Special.md) snap button is turned on. Currently that property is only available to Python, though. In the case above I added a new snap point at the exit of the WC appliance. The vectors inside SnapPoints appear on the model as white dots:

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

## Scripting


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

Pipeツールは、[マクロやPythonコンソールから次の関数を使って使うことができます](macros.md)：


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


{{docnav/ja|[Arch CompPipe](Arch_CompPipe/ja.md)|[Pipe Connector](Arch_PipeConnector/ja.md)|[Arch](Arch_Workbench/ja.md)|IconL=Arch_CompPipe.png |IconC=Workbench_Arch.svg |IconR=Arch_PipeConnector.svg}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Pipe/ja
