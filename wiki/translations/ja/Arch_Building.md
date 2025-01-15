---
 GuiCommand:
   Name: Std_Edit
   Name/ja: Std_Edit
   MenuLocation: Edit -> Toggle Editmode
   Workbenches: All
   SeeAlso: 
---

# Arch Building/ja


</div>



## 概要

このコマンドを使うと選択されているオブジェクトの編集モードの有効/無効を切り替えることができます。 このコマンドが動作するにはオブジェクトが選択されているか（編集モードを有効にする場合）、編集モードになっているか（編集モードを無効にする場合）どちらかである必要があります。




<div class="mw-translate-fuzzy">

## 使用方法


</div>


<div class="mw-translate-fuzzy">

編集モードが有効になった場合の動作はオブジェクトの型によって変わります。 一部のオブジェクト型では編集モード時の動作が定義されていません。その場合は標準の動作（変形ウィジット）が使用されます。

ツリービューにあるオブジェクトをダブルクリックすることでも同じ動作を行うことができます。


</div>



## オプション

-   Starting from FreeCAD version 0.18, the Building object is actually a [BuildingPart](Arch_BuildingPart.md) with its **IFC Type** property set to \"Building\". You can convert any BuildingPart to a Building simply by changing its IFC Type.
-   After creating a building, you can add more objects to it by drag and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a building by drag and dropping them out of it the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.



## プロパティ

-    **Building Type**: The type of this building, to choose from a list

## Scripting


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

以下では特定のオブジェクトの編集モードを有効にしています：

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)

以下では編集モードを終了しています：

FreeCADGui.ActiveDocument.resetEdit()


</div>


```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Creates a `Building` object from `objectslist`, which is a list of objects, or `baseobj`, which is a `Shape`.

Example:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Building/ja
