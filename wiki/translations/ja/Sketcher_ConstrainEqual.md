---
- GuiCommand:
   Name: Constraint EqualLength
   Name/ja: Constraint EqualLength
   Workbenches: [スケッチャー](Sketcher_Workbench/ja.md), [パートデザイン](PartDesign_Workbench/ja.md)
   MenuLocation: Sketch - Sketcher constraints - Constrain equal
   SeeAlso: [Constraint Radius](Constraint_Radius/ja.md)
---

# Sketcher ConstrainEqual/ja


</div>

## 説明


<div class="mw-translate-fuzzy">

ConstrainEqualはライン、ポリライン、長方形に含まれる複数の線分が等しい長さになるように拘束を行います。円弧や円に対して適用した場合はその半径が等しくなるように拘束を行います。異なるタイプの幾何プリミティブ間（例えば線分と円弧）に適用することはできません。


</div>


<div class="mw-translate-fuzzy">

## 操作

下のスケッチの例には複数のスケッチプリミティブ（ライン、ポリライン、長方形、円弧、円）が含まれています。

<img alt="" src=images/EqualConstraint1.png  style="width:256px;">

複数の線分を選択します（例えばラインと長方形の一辺）。

<img alt="" src=images/EqualConstraint2.png  style="width:256px;">

（スケッチャーワークベンチまたはパートデザインワークベンチにある）スケッチャーツールバのConstrainEqualアイコン<img alt="" src=images/Constraint_EqualLength.png  style="width:16px;">をクリックするか、選択されているワークベンチ（スケッチャーまたはパートデザイン）に応じてSketchメニューアイテムまたはPart DesignメニューアイテムにあるSketcher constraintsサブメニューアイテムのConstrain Equaメニューアイテムを選択して選択アイテムに拘束を適用します。

<img alt="" src=images/EqualConstraint3.png  style="width:256px;">

今度はスケッチ上の円弧と円を選択します。

<img alt="" src=images/EqualConstraint4.png  style="width:256px;">

先ほどと同じようにConstrainEqual<img alt="" src=images/Constraint_EqualLength.png  style="width:16px;">拘束を適用します。

<img alt="" src=images/EqualConstraint5.png  style="width:256px;">

今度は線分、ポリラインの全線分、そして長方形の拘束されずに残っている辺の一つを選択します。

<img alt="" src=images/EqualConstraint6.png  style="width:256px;">

先ほどと同じようにConstrainEqual<img alt="" src=images/Constraint_EqualLength.png  style="width:16px;">拘束を適用します。

<img alt="" src=images/EqualConstraint7.png  style="width:256px;">

線分と円弧を選択します。

<img alt="" src=images/EqualConstraint8.png  style="width:256px;">

先ほどと同じようにConstrainEqual<img alt="" src=images/Constraint_EqualLength.png  style="width:16px;">拘束を適用します。すると拘束アイテム同じ形状タイプ（曲線を含まない線分集合または曲線を含む線分集合）でなければならいということを示すポップアップメッセージが表示されます。

<img alt="" src=images/EqualConstraint9.png  style="width:256px;">


</div>

The example sketch below contains a number of sketch primitives (line, poly-line, rectangle, arc and circle).

![](images/EqualConstraint1.png )

Select two or more line segments (e.g. line and one side of the rectangle).

![](images/EqualConstraint2.png )

Click on **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** in the Sketcher toolbar (in either the Sketcher or Part Design workbenches) or select the Constrain Equal menu item from the Sketcher constraints sub menu item in either the Sketch or Part Design menu item depending upon which workbench is selected (Sketcher or Part Design) to apply the constraint to the selected items.

![](images/EqualConstraint3.png )

Now select the arc and the circle in the sketch.

![](images/EqualConstraint4.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint5.png )

Now select the line segment, all segments of the poly-line and one of the remaining unconstrained sides of the rectangle

![](images/EqualConstraint6.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint7.png )

Select the line segment and the arc

![](images/EqualConstraint8.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before. A pop-up message indicates that the constrained items have to be of the same geometrical type (lines of zero curvature or lines of non-zero curvature).

![](images/EqualConstraint9.png )

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/ja
