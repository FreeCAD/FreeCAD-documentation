---
 GuiCommand:
   Name: Arch Add
   Name/ja: Arch Add
   Workbenches: Arch Workbench/ja
   MenuLocation: Arch -> Add
   SeeAlso: Arch Remove/ja
---

# Arch Add/ja


</div>



## 説明


<div class="mw-translate-fuzzy">

Addツールは2種類の操作を提供します：

-   [シェイプベースのオブジェクトを](Part_Workbench/ja.md)[壁や](Arch_Wall/ja.md)[骨組みといった](Arch_Structure/ja.md) Archコンポーネントに追加します。これらのオブジェクトはArchコンポーネントのパーツとなってその高さや厚みといった基本プロパティを保持するだけでなく、その形状を変更する機能を提供します。
-   [壁](Arch_Wall/ja.md)、[骨組みあるいは](Arch_Structure/ja.md)[床などのセルベースのオブジェクトといったArchコンポーネントを](Arch_Floor/ja.md)追加します。
-   [axis systems](Arch_Axis.md) に[structural objectsを](Arch_Structure.md)追加する
-   [ section planesにオブジェクトを](Arch_SectionPlane.md)追加する


</div>

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

上の図では壁に直方体が追加されています。


</div>




<div class="mw-translate-fuzzy">

## 使用方法


</div>


<div class="mw-translate-fuzzy">

-   追加するオブジェクト（複数可）を選択してから\"ホスト\"となるオブジェクトを選択してください（最後に選択したものがホストオブジェクトになります）
-   <img alt="" src=images/Arch_Add.png  style="width:16px;"> **Add**ボタンを押してください


</div>

## Scripting


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

Add ツールは、[マクロやPythonコンソールから](macros.md)次の関数を使って使うことができます：


</div>


:   
    
```python
    addComponents(objectsList, host)
    
```
    


<div class="mw-translate-fuzzy">

-   Adds the given object or the objects from the given list as components to the given host Object. Use this for example to add windows to a wall, or to add walls to a floor.
-   Returns nothing.


</div>

例題:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Add/ja
