# Arch Remove/ja
---
 GuiCommand:
   Name: Arch Remove
   Name/ja: Removeツール
   MenuLocation: Arch -> Remove
   Workbenches: Arch Workbench/ja
   SeeAlso: Arch Add/ja---


</div>



## 説明


<div class="mw-translate-fuzzy">

Removeツールは2種類の操作を提供します：

-   Archオブジェクトからサブコンポーネントを取り除きます。例えば[Arch Addの](Arch_Add/jp.md)例のような壁に追加されていた直方体を壁から取り除きます。
-   [シェイプベースのオブジェクトを](Part_Module/jp.md)[壁や](Arch_Wall/jp.md)[骨組みといった](Arch_Structure/jp.md) Archコンポーネントから減算します。


</div>

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

上の図では壁から直方体を減算しています


</div>




<div class="mw-translate-fuzzy">

## 使用方法


</div>


<div class="mw-translate-fuzzy">

-   Archオブジェクト内のサブコンポーネントを選択してください。**あるいは**
-   減算されるオブジェクト（複数可）を選択してからそれらを減算するArchコンポーネントを選択してください（Archコンポーネントは最後に選択しなければなりません）
-   <img alt="" src=images/Arch_Remove.png  style="width:16px;"> **Remove**ボタンを押してください


</div>

Or

1.  Select objects to be subtracted, the last object selected must the Arch object from which the other objects will be subtracted.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px> [Remove component](Arch_Remove.md)** button, or **Modify → <img src="images/Arch_Remove.svg" width=16px> Remove component** from the top menu.

## Scripting


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>

The Remove tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
removeComponents(objectsList, host=None)
```

-   Removes the given objects in `objectsList` from their parents.
-   If a `host` object is specified, this function will try adding the objects in `objectsList` as holes to the `host`.

Example:


```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/ja|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Remove/ja
