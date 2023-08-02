---
- GuiCommand:
   Name: Arch PipeConnector   Name/ja: Arch PipeConnector
   MenuLocation: Arch -> Pipe Tools -> Pipe Connector
   Workbenches: Arch Workbench/ja
   Shortcut: **P** **C**
   SeeAlso: Arch Pipe/ja, Arch Equipment/ja
   Version: 0.17
---

# Arch PipeConnector/ja


</div>

## 説明


<div class="mw-translate-fuzzy">


<small>(v0.17)</small> 

このツールを使用すると、[ Arch Pipesで選択された](Arch_Pipe.md)2つまたは3つのパイプの間にコーナー接続または \"T\"接続を作成できます。


</div>

## 使用方法


<div class="mw-translate-fuzzy">

＃2本または3本のパイプ[アーチパイプを選択します](Arch_Pipe.md)。 3本のパイプを選択する場合は、2本を正確に位置合わせする必要があります。 ＃**<img src="images/Arch_PipeConnector.png" width=16px> [[Arch PipeConnector]]**ボタンを押すか、{{KEY | P}}キーを押してから{{KEY | C}}キーを押します。


</div>

## プロパティ

-    **Radius**: このコネクタの曲率半径

## 典型的なワークフロー


<div class="mw-translate-fuzzy">

[Arch Pipe#Typical_workflow](Arch_Pipe#Typical_workflow.md) を参照してください。


</div>

## Scripting


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

Pipe Connectorツールは、[マクロやPythonコンソールから次の関数を使って使うことができます](macros.md)：


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


{{docnav/ja|[Pipe](Arch_Pipe.md)|[Arch CompSetMaterial](Arch_CompSetMaterial.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Pipe.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompSetMaterial.png}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/ja
