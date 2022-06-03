---
- GuiCommand   */ja
   Name   *Arch Rebar
   Name/ja   *Arch Rebar
   MenuLocation   *Arch → Rebar
   Workbenches   *[Arch](Arch_Module.md)
   Shortcut   *R B
   SeeAlso   *[Arch Structure](Arch_Structure.md), [Reinforcement Addon](Reinforcement_Addon.md)
---

# Arch Rebar/ja


</div>

## 説明


<div class="mw-translate-fuzzy">

Rebarツールを使用すると、[Arch Structureオブジェクトの中に](Arch_Structure.md) [reinforcing bars](http   *//en.wikipedia.org/wiki/Rebar) を配置することができます。 Rebarオブジェクトは、[sketches](Sketcher_Workbench.md) /[スケッチや](Sketcher_Workbench.md)[draft objects](Draft_Workbench.md)/[ドラフトオブジェクトなどの](Draft_Workbench.md)2Dプロファイルに基づいており、構造オブジェクトの面に描画する必要があります。バーの数や直径、または構造要素の両端のオフセット距離など、リバーの構成を調整することができます。


</div>

The [Arch Rebar](Arch_Rebar.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

Rebar objects are based on 2D profiles such as [Draft objects](Draft_Workbench.md) and [Sketches](Sketcher_Workbench.md), that must be drawn on a face of the structural object. After creation you can adjust the properties of the rebar, including the number and diameter of the bars, and the offset distance between them and the faces of the structural element.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">

上の図は、2つの棒グラフを定義する2つのスケッチが描かれている構造オブジェクトを示しています。これらの2つのスケッチは、鉄筋オブジェクトに変換されます。


</div>

## 利用可能なエクステンション

The Rebar tool is enhanced by the [Reinforcement Workbench](Reinforcement_Workbench.md), which is installed by the [Addon Manager](Std_AddonMgr.md). The additional rebar types available with the addon are   *

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width   *32px;"> [Straight Rebar](Arch_Rebar_Straight.md)
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width   *32px;"> [UShape Rebar](Arch_Rebar_UShape.md)
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width   *32px;"> [LShape Rebar](Arch_Rebar_LShape.md)
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width   *32px;"> [Bent Shape Rebar](Arch_Rebar_BentShape.md)
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width   *32px;"> [Stirrup Rebar](Arch_Rebar_Stirrup.md)
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width   *32px;"> [Helical Rebar](Arch_Rebar_Helical.md)


<div class="mw-translate-fuzzy">

## 使用方法


</div>

1.  Switch to the <img alt="" src=images/Workbench_Arch.svg  style="width   *16px;"> [Arch Workbench](Arch_Workbench.md)
2.  Create an **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** element.
3.  Switch to the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher Workbench](Sketcher_Workbench.md).
4.  Select one face of the structural element.
5.  Press the **<img src="images/Sketcher_NewSketch.svg" width=16px> [New Sketch](Sketcher_NewSketch.md)** button to start a new sketch on the selected face.
6.  Draw the diagram of your bar.
7.  Press the **<img src="images/Sketcher_LeaveSketch.svg" width=16px> [Leave Sketch](Sketcher_LeaveSketch.md)** button to finish.
8.  Switch back to the <img alt="" src=images/Workbench_Arch.svg  style="width   *16px;"> [Arch Workbench](Arch_Workbench.md).
9.  Select the sketch you just drew.
10. Press the **<img src="images/Arch_Rebar.svg" width=16px> [Arch Rebar](Arch_Rebar.md)** button, or press **R** then **B** keys.
11. Adjust the desired properties (your rebar might not appear immediately, if some of the properties create an impossible situation, such as the bar diameter being 0, or the offset distances being bigger than the length of the structural element).

Although normally a rebar is used inside an Arch Structure, since FreeCAD 0.19 the rebar can be created outside of any host object. To host a rebar inside an object, you just need to set its **Host**.

## オプション

-   Rebars share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The rounding value is expressed in times the diameter. If your bar has a diameter of 5mm, a rounding value of 3 will create rounding at angles with a radius of 15mm.
-   Default values for new rebars can be set in the Arch preferences settings.
-   If a direction vector is not specified, the direction and distance along which the bars will spread is calculated automatically from the host structural object, by taking the normal direction of the base sketch, and taking its intersection with the structural object. If you specify a direction vector, the length of that vector will also be taken into account.
-   The spacing value is calculated from the current amount of bars, and represents the distance between the axes of each bar. You must therefore subtract the bar diameter to obtain the size of the free space between bars.

## プロパティ

-    **Amount**   * The amount of bars.

-    **Diameter**   * The diameter of the bars.

-    **Direction**   * The direction (and length) along which the bars must spread. If the value is (0,0,0), the direction is calculated automatically from the host structural object.

-    **Offset Start**   * The offset distance between the border of the structural object and the first bar.

-    **Offset End**   * The offset distance between the border of the structural object and the last bar.

-    **Rounding**   * A rounding value to be applied to the corners of the bars, expressed in times the diameter.

-    **Spacing**   * The distance between the axes of each bar.


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

Rebarツールは、[マクロやPythonコンソールから次の関数を使って使うことができます](macros.md)：


</div>


```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```

-   Creates a `Rebar` object from the given `baseobj`, which is an [Arch Structure](Arch_Structure.md), and a `sketch` as profile.
    -   
        `diameter`
        
        , `amount`, and `offset` are used to define the characteristics of the bars.

    -   If no `diameter`, `amount`, or `offset` values are given, the default values from the [Arch Preferences](Arch_Preferences.md) are used.

例題   *


```python
import FreeCAD, Arch, Part

Structure = Arch.makeStructure(None, length=1000, width=1000, height=3000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

p1 = FreeCAD.Vector(-400, 400, 0)
p2 = FreeCAD.Vector(400, 400, 0)
Sketch = FreeCAD.ActiveDocument.addObject('Sketcher   *   *SketchObject', 'Sketch')
Sketch.MapMode = "FlatFace"
Sketch.Support = [(Structure, "Face6")]
Sketch.addGeometry(Part.LineSegment(p1, p2))
FreeCAD.ActiveDocument.recompute()

Rebar = Arch.makeRebar(Structure, Sketch, diameter=80, amount=7, offset=50)
Rebar.OffsetStart = 100
Rebar.OffsetEnd = 100
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav|[BeamReinforcement](Arch_Rebar_BeamReinforcement.md)|[Floor](Arch_Floor.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Rebar_BeamReinforcement.svg |IconC=Workbench_Arch.svg |IconR=Arch_Floor.svg}}


</div>


 

[Category   *External Command Reference](Category_External_Command_Reference.md) [Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar/ja
