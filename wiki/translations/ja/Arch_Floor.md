---
- GuiCommand:
   Name: Arch Floor   Name/ja: Arch Floor
   MenuLocation: Arch - Floor
   Workbenches: [Arch](Arch_Workbench/ja.md)
   Shortcut: **F** **L**
   SeeAlso: [[Arch Building]], [[Arch BuildingPart]], [[Arch Site]]
---

# Arch Floor/ja


</div>

## 説明


<div class="mw-translate-fuzzy">

Arch Floorは床を作成するのに特に便利な追加プロパティを持った特殊なタイプのです。特徴的なのがheightプロパティを持っていることで、その子オブジェクト（[壁や](Arch_Wall.md)[骨組み](Arch_Structure.md)）ではそれを使ってその高さを自動で設定することができます。


</div>

As of <small>(v0.18)</small>  the Arch Floor is derived entirely from the [Arch BuildingPart](Arch_BuildingPart.md) object, which is a general container to organize a building model not limited to floors or storeys. Older Floor objects can be converted to the new type by right clicking on them and choosing `Convert to BuildingPart`.

## 使用方法


<div class="mw-translate-fuzzy">

＃オプションで、新しいフロアに含める1つ以上のオブジェクトを選択します ＃{{KEY | <img src="images/Arch_Floor.svg" width=16px> '''Arch Floor'''}}ボタンを押すか、{{KEY | F}}、その後{{KEY | L}}キーを押します


</div>

## オプション

-   After creating a floor, you can add more objects to it by drag and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a floor by drag and dropping them out of it the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

## プロパティ

An Arch Floor object shares all properties from an [Arch BuildingPart](Arch_BuildingPart.md), with the **Ifc Type** set to `"Building Storey"`.


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

Floorツールは、[マクロやPythonコンソールから次の関数を使って使うことができます](macros.md)：


</div>


```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```

-   Creates a `Floor` object from `objectslist`, which is a list of objects.

例題:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Floor/ja
