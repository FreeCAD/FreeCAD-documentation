---
 GuiCommand:
   Name: Sketcher ConstrainHorizontal
   Name/ja: Sketcher ConstrainHorizontal
   Workbenches: Sketcher Workbench/ja, PartDesign Workbench/ja
   MenuLocation: Sketch , Sketcher constraints , Constrain horizontally
   SeeAlso: Constraint Vertical/ja
---

# Sketcher ConstrainHorizontal/ja


</div>



## 説明


<div class="mw-translate-fuzzy">

HorizontalConstraintは選択された線または画像の辺がスケッチの水平軸と平行なるように拘束を行います。


</div>


<small>(v1.0)</small> 

: In most cases it is advisable to use the combined [Sketcher ConstrainHorVer](Sketcher_ConstrainHorVer.md) tool instead.




<div class="mw-translate-fuzzy">

## 使用方法


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint1.png  style="width:256px;"> スケッチ上の線をクリックして選択します。
<img alt="" src=images/HorizontalConstraint2.png  style="width:256px;"> 線が暗緑色に変わります。
<img alt="" src=images/HorizontalConstraint3.png  style="width:256px;"> Sketcher ConstraintsツールバーのHorizontalConstraintアイコン<img alt="" src=images/Constraint_Horizontal.png  style="width:16px;">をクリックするか、スケッチャーワークベンチのSketcherメニューアイテム（あるいはパートデザインワークベンチのPart Designメニューアイテム）にあるSketcher constraintsサブメニューのConstrain horizontallyメニューアイテムを選択してHorizontalConstraintを適用します。すると選択された線がスケッチの水平軸に平行になるように拘束されます。
<img alt="" src=images/HorizontalConstraint4.png  style="width:256px;"> 複数の線を選択することもできます。
<img alt="" src=images/HorizontalConstraint5.png  style="width:256px;"> 上で示したように線を選択して拘束を適用すると、それらがスケッチの水平軸に平行になるように拘束されます。


</div>

### Run-once mode 

1.  Do one of the following:
    -   Select two or more points.
    -   Select one or more lines. Points can be included in the selection, but will be ignored.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Constrain horizontal** option from the context menu.
3.  Depending on the selection one or more constraints are added.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/ja
