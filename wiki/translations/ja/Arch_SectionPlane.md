# Arch SectionPlane/ja
---
- GuiCommand   */ja   Name   *Arch SectionPlane   Name/ja   *Arch SectionPlane   Workbenches   *[[Arch Workbench/ja   建築]]|MenuLocation   *Arch -> Section Plane   Shortcut   *S P---


</div>

## 説明


<div class="mw-translate-fuzzy">

このツールは現在のドキュメントに断面表示のためのギズモ（仕組み）を配置します。これよって断面または表示面が定義されます。ギズモは移動と回転によって位置や方向を変えることができ、取得したい2D表示を表示できます。他のオブジェクトを選択しない状態でこのツールが使用された場合、シーンにある全てのオブジェクトが2D表示に含まれます。何かオブジェクトを選択している場合、2D表示にはそのオブジェクトのみ表示されます。[Arch Addツールと](Arch_Add/jp.md)[Arch Removeツールを使用することで後からSectionPlaneオブジェクトにオブジェクトを追加したり](Arch_Remove/jp.md)、削除したりすることができます。


</div>


<div class="mw-translate-fuzzy">

現在のところ作成時にSectionPlaneオブジェクトはSectionPlaneの対象とみなされるオブジェクトの2D写像が設定された[Drawing Pageオブジェクトを作成します](Drawing_Workbench.md)。上の図の左側はシーン内に置かれたSectionPlaneオブジェクトを表し、右側はSVGの2D出力を表しています。面のソートの実装はまだ不完全です。


</div>

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width   *600px;">


<div class="mw-translate-fuzzy">

## 使用方法


</div>


<div class="mw-translate-fuzzy">

1.  Optionally, set the [Draft Working Plane](Draft_SelectPlane.md) to reflect the plane where you want to place the Section Plane
2.  Select objects you want to be included in your section view
3.  Press the **<img src="images/Arch_SectionPlane.png" width=16px> '''SectionPlane'''** button or press **S** then **P** keys
4.  [Move](Draft_Move.md)/[rotate](Draft_Rotate.md) the Section Plane into correct position if needed
5.  Select the Section Plane if not selected already
6.  Use either [Drawing DraftView](Draft_Drawing.md), [Draft Shape2DView](Draft_Shape2DView.md) or [TechDraw ArchView](TechDraw_ArchView.md) to create a view

-   オブジェクトを選択します
-   <img alt="" src=images/Arch_SectionPlane.png  style="width   *16px;"> **SectionPlane**ボタンを押してください
-   断面を適切な位置に移動/回転させてください
-   表示を更新のために<img alt="" src=images/Std_Recompute.png  style="width   *16px;"> **Recompute**ボタンを押してください


</div>

## Options

-   The Section plane object will only consider a certain set of objects, not all the objects of the document. Objects can be added or removed from a SectionPlane object by using the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools, or by double-clicking the Section Plane in the tree view, selecting objects either in the list of in the 3D scene, and pressing the **add** or remove **buttons**.

-   With a section plane object selected, use the [Draft Shape2DView](Draft_Shape2DView.md) tool to create a shape object representing the section view in the document

<img alt="" src=images/Arch_Section_example2.jpg  style="width   *600px;">

-   Create [Drawing DraftViews](Draft_Drawing.md) if you are working with the [Drawing Workbench](Drawing_Workbench.md), or [TechDraw ArchView](TechDraw_ArchView.md) if you are using the [TechDraw Workbench](TechDraw_Workbench.md).

<img alt="" src=images/Arch_Section_example3.jpg  style="width   *600px;">

-   The Section Plane can also be used to show the entire 3D view cut by an infinite plane. This is only visual, and won\'t affect the geometry of the objects being cut.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width   *600px;">

## プロパティ

-    **Only Solids**   * If this is True, non-solid objects in the set will be disregarded

-    **Display Length**   * The length of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Display Height**   * The height of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Arrow Size**   * The size of the arrows of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Cut View**   * If this is `True`, the whole 3D view will be cut at the location of this section plane.

-    **Clip view**   * if this is `True`, it will clip the view to the display height and length of the section plane. This effectively turns the section plane into an orthographic camera, limiting the field of view. <small>(v0.19)</small> 

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width   *600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App   *   *PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

## スクリプト処理


</div>


<div class="mw-translate-fuzzy">

Section Planeツールは[macros内で](macros.md)、そしてPythonコンソールから次の関数を使って使うことができます：


</div>


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Creates a `Section` object from `objectslist`, which is a list of objects.

例題   *


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav
|[Window](Arch_Window.md)
|[Arch CompAxis](Arch_CompAxis.md)
|[Arch](Arch_Workbench.md)
|IconL=Arch_Window.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_CompAxis.png
}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SectionPlane/ja
