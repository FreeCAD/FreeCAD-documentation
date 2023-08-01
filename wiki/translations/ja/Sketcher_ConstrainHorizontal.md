---
- GuiCommand:
   Name:Sketcher ConstrainHorizontal
   Name/ja:Sketcher ConstrainHorizontal
   Workbenches:[スケッチャー](Sketcher_Workbench/ja.md), [パートデザイン](PartDesign_Workbench/ja.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain horizontally
   SeeAlso:[Constraint Vertical](Constraint_Vertical/ja.md)
---

# Sketcher ConstrainHorizontal/ja


</div>

## 説明

HorizontalConstraintは選択された線または画像の辺がスケッチの水平軸と平行なるように拘束を行います。


<div class="mw-translate-fuzzy">

## 使用方法


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint1.png  style="width:256px;"> スケッチ上の線をクリックして選択します。
<img alt="" src=images/HorizontalConstraint2.png  style="width:256px;"> 線が暗緑色に変わります。
<img alt="" src=images/HorizontalConstraint3.png  style="width:256px;"> Sketcher ConstraintsツールバーのHorizontalConstraintアイコン<img alt="" src=images/Constraint_Horizontal.png  style="width:16px;">をクリックするか、スケッチャーワークベンチのSketcherメニューアイテム（あるいはパートデザインワークベンチのPart Designメニューアイテム）にあるSketcher constraintsサブメニューのConstrain horizontallyメニューアイテムを選択してHorizontalConstraintを適用します。すると選択された線がスケッチの水平軸に平行になるように拘束されます。
<img alt="" src=images/HorizontalConstraint4.png  style="width:256px;"> 複数の線を選択することもできます。
<img alt="" src=images/HorizontalConstraint5.png  style="width:256px;"> 上で示したように線を選択して拘束を適用すると、それらがスケッチの水平軸に平行になるように拘束されます。


</div>

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*The line turns dark green.*

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Apply the Horizontal Constraint by clicking on the **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Constraint horizontal](Sketcher_ConstrainHorizontal.md)* in the Sketcher Constraints toolbar or by selecting the Constrain horizontally menu item in the Sketcher constraints sub menu of the Sketch menu item in the Sketcher work bench (or the Part Design menu item of the Part Design work bench). The selected line is constrained to be parallel to the horizontal axis of the sketch.**

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Multiple lines may be selected*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*and then applying the constraint as described above, they are constrained to be parallel to the sketch horizontal axis.*

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/ja
