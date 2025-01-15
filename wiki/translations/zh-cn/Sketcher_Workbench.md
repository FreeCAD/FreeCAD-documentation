# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/zh-cn






## 简介


<div class="mw-translate-fuzzy">

[ 草图工作台](Sketcher_Workbench.md)用于创建用于[ 零件工作台](PartDesign_Workbench/zh-cn.md)、[ 建筑工作台](Arch_Workbench/zh-cn.md)和其他工作台的二维几何图形。 通常，二维绘图被视为大多数CAD模型的起点，因为二维草图可以"拉伸"以创建三维形状；进一步的二维草图可以用于在先前构建的三维形状的基础上创建其他特征，如开槽"Pocket"、隆起"ridges"或拉伸。 草图绘制器与在[零件设计工作台](PartDesign_Workbench/zh-cn.md)中定义的布尔操作一起构成了构建实体的[构造实体几何](constructive_solid_geometry/zh-cn.md)方法的基础。此外，草图绘制器还与[零件设计工作台](PartDesign_Workbench/zh-cn.md)操作一起构成了创建实体的[特征编辑](feature_editing/zh-cn.md)方法的基础。


</div>

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.


<div class="mw-translate-fuzzy">

草图工作台本身具有约束条件 - 允许将2D形状约束到精确的几何定义。以及一个约束求解器，它计算二维几何约束范围，并允许对草图自由度的交互式探索。


</div>


<div class="mw-translate-fuzzy">

## 草图编辑器不擅长于

草图编辑器不打算制作2D蓝图。草图一旦用于生成实体特征后，会自动隐藏。约束仅在草图编辑模式下可见。


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*一个全约束草图*

## Constraints


<div class="mw-translate-fuzzy">

#### 什么是约束？

使用约束来限制对象的自由度。例如，没有约束的线条具有4 [自由度](#Degrees_Of_Freedom.md)（简写为"DOF"）：可以水平或垂直移动，可以被拉伸，并且可以旋转。


</div>

应用水平或垂直约束或角度约束（相对于另一条线或与其中一条轴）将限制其旋转能力，从而使其具有3个自由度。锁定其原点之一的点将消除另外2个自由度。并且应用维度约束将消除最后的自由度。然后，该行被认为是"完全受限制的"。


<div class="mw-translate-fuzzy">

多个对象可以彼此约束。可以通过其中一个点与重合点约束连接两条线。可以在它们之间设置一个角度，或者它们可以垂直设置。一条线可以与弧或圆相切，依此类推。具有多个对象的复杂草图将具有多种不同的解决方案，并使其"完全受约束"，这意味着基于所应用的约束只能达到其中一种可能的解决方案。


</div>


<div class="mw-translate-fuzzy">

有两种约束：几何和尺寸。它们在下面的[\'工具\'](#The_tools.md)部分中详细介绍。


</div>

### Edit constraints 

When a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, and if the **Ask for value after creating a dimensional constraint** [preference](Sketcher_Preferences#Display.md) is selected (default), a dialog opens to edit its value.

![](images/Sketcher_Edit_Constraint.png )

You can enter a numerical value or an [expression](Expressions.md), and it is possible to name the constraint to facilitate its use in other expressions. You can also check the **Reference** checkbox to switch the constrain to [reference mode](Sketcher_ToggleDrivingConstraint.md).

To edit the value of an existing dimensional constraint do one of the following:

-   Double-click the constraint value in the [3D view](3D_view.md).
-   Double-click the constraint in the [Sketcher Dialog](Sketcher_Dialog.md).
-   Right-click the constraint in the Sketcher Dialog and select the **Change value** option from the context menu.

### Reposition constraints 

Dimensional constraints can be repositioned in the 3D view by dragging. Hold down the left mouse button over the constraint value and move the mouse. The symbols of geometric constraints are positioned automatically and cannot be moved.

## Profile sketches 

To create a sketch that can be used as a profile for generating solids certain rules must be followed:

-   The sketch must contain only closed contours. Gaps between endpoints, however small, are not allowed.
-   Contours can be nested, to create voids, but should not self-intersect or intersect other contours.
-   Contours cannot share edges with other contours. Duplicate edges must be avoided.
-   T-connections, that is more than two edges sharing a common point, or a point touching an edge, are not allowed.

These rules do not apply to construction geometry (default color blue), which is not shown outside edit mode, or if the sketch is used for a different purpose. Depending on the workbench and the tool that will use the profile sketch, additional restrictions may apply.

## Drawing aids 

The Sketcher Workbench has several drawing aids and other features that can help when creating geometry and applying constraints.

### Continue modes 

There are two continue modes: **Geometry creation \"Continue Mode\"** and **Constraint creation \"Continue Mode\"**. If these are checked (default) in the [preferences](Sketcher_Preferences#Display.md), related tools will restart after finishing. To exit a continuous tool press **Esc** or the right mouse button. This must be repeated if a continuous geometry tool has already received input. You can also exit a continuous tool by starting another geometry or constraint creation tool. Note that pressing **Esc** if no tool is active will exit sketch edit mode. Uncheck the **Esc can leave sketch edit mode** [preference](Sketcher_Preferences#General.md) if you often inadvertently press **Esc** too many times.

### Auto constraints 

In sketches that have **Auto constraints** checked (default) several constraints are applied automatically. The icon of a proposed automatic constraint is shown next to the cursor when it is placed correctly. Left-Clicking will then apply that constraint. This is a per-sketch setting that can be changed in the [Sketcher Dialog](Sketcher_Dialog#Constraints.md) or by changing the **Autoconstraints** [property](Property_editor.md) of the sketch.

The following constraints are applied automatically:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident](Sketcher_ConstrainCoincident.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) (line midpoint)

### Snapping


<small>(v0.21)</small> 

It is possible to [snap](Sketcher_Snap.md) to grid lines and grid intersection, to edges of geometry and midpoints of lines and arcs, and to certain angles. Please note that snapping does not produce constraints in and of itself. For example, only if [Auto constraints](#Auto_constraints.md) is switched on will snapping to an edge produce a [Point on object constraint](Sketcher_ConstrainPointOnObject.md). But just picking a point on the edge would then have the same result.

### On-View-Parameters 


<small>(v1.0)</small> 

Depending on the selected option in the [preferences](Sketcher_Preferences#General.md) only the dimensional On-View-Parameters or both the dimensional and the positional On-View-Parameters can be enabled. Positional parameters allow the input of exact coordinates, for example the center of a circle, or the start point of a line. Dimensional parameters allow the input of exact dimensions, for example the radius of a circle, or the length and angle of a line. On-View-Parameters are not available for all tools.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determining the center point of a circle with the positional parameters enabled*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determining the radius of a circle with the dimensional parameters enabled*

If values are entered and confirmed by pressing **Enter** or **Tab**, related constraints are added automatically. If two parameters are displayed at the same time, for example the X and Y coordinate of a point, it is possible to enter one value and pick a point to define the other. Depending on the object additional constraints may be required to fully constrain it. Constraints resulting from On-View-Parameters take precedence over those that may result from [Auto constraints](Sketcher_Dialog#Constraints.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc created by entering all On-View-Parameters with resulting automatically created constraints*

### Coordinate display 

If the **Show coordinates beside cursor while editing** [preference](Sketcher_Preferences#Display.md) is checked (default), the parameters of the current geometry tool (coordinates, radius, or length and angle) are displayed next to the cursor. This is deactivated while On-View-Parameters are shown.

## Selection methods 

While a sketch is in edit mode the following selection methods can be used:

### 3D view element selection 

As elsewhere in FreeCAD, an element can be selected in the [3D view](3D_view.md) with a single left mouse click. But there is no need to hold down the **Ctrl** key when selecting multiple elements. Holding down that key is possible though and has the advantage that you can miss-click without losing the selection. Edges, points and constraints can be selected in this manner.

### 3D view box selection 

Box selection in the 3D view works without using [Std BoxSelection](Std_BoxSelection.md) or [Std BoxElementSelection](Std_BoxElementSelection.md):

1.  Make sure that no tool is active.
2.  Do one of the following:
    -   Click in an empty area and drag a rectangle from left to right to select elements that lie completely inside the rectangle.
    -   Click in an empty area and drag a rectangle from right to left to also select elements that touch or cross the rectangle.

You can box-select edges and points, constraints cannot be box-selected.

### 3D view connected geometry selection 


<small>(v1.0)</small> 

Double-clicking an edge in the 3D view will select all edges directly and indirectly connected with that edge via endpoints. There is no need for the edges to be connected with [Coincident constraints](Sketcher_ConstrainCoincident.md), endpoints need only have the same coordinates.

### Sketcher Dialog selection 

Edges and points can also be selected from the Elements section of the [Sketcher Dialog](Sketcher_Dialog.md), and constraints from the Constraints section of that dialog.

## Copy, cut and paste 


<small>(v1.0)</small> 

The standard keyboard shortcuts, **Ctrl**+**C**, **Ctrl**+**X** and **Ctrl**+**V**, can be used to copy, cut and paste selected Sketcher geometry including related constraints. But these tools are also available from the **Sketch → Sketcher tools** menu. They can be used within the same sketch but also between different sketches or separate instances of FreeCAD. Since the data is copied to the clipboard in the form of Python code, it can be used in other ways too (e.g. shared on the forum).

## Tools


<div class="mw-translate-fuzzy">

## 工具

草图工作台工具都位于加载草图工作台时出现的草图菜单中。


</div>

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.

### General

#### Sketcher toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [创建草图](Sketcher_NewSketch/zh-cn.md): 在所选的面或平面上创建新的草图。如果在执行此工具时未选择任何面, 则系统将提示用户从弹出窗口中选择一个平面。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [编辑草绘](Sketcher_EditSketch/zh-cn.md): 编辑已选择的草图。这会开启[草图对话框](Sketcher_Dialog.md)。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [映射草图至面](Sketcher_MapSketch/zh-cn.md): 将草图映射到以前选定的实心面。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [调整草图方向](Sketcher_ReorientSketch/zh-cn.md): 允许您更改草图的位置


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [校验草图...](Sketcher_ValidateSketch/zh-cn.md): 它允许你检查是否有不同点的公差和匹配。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [合并草图](Sketcher_MergeSketches/zh-cn.md): 合并两个或多个草图。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [镜像草图](Sketcher_MirrorSketch/zh-cn.md): 沿 x 轴、y轴或原点镜像草图。


</div>

#### Sketcher Edit Mode toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [离开草图](Sketcher_LeaveSketch/zh-cn.md): 离开草图编辑模式。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [查看草图](Sketcher_ViewSketch/zh-cn.md): 设置垂直于草图平面的模型视图。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [查看截面](Sketcher_ViewSection/zh-cn.md): 创建一个截面，并暂时隐藏此草图平面前侧的所有内容。


</div>

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): Stops any currently running geometry or constraint creation tool.



#### 草图编辑器几何工具

这是创建对象的工具。


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint.md): 绘制一个点.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline (multiple-point line)](Sketcher_CreatePolyline.md): 绘制由多个线段组成的线。绘制折线时，按M键可在不同的折线模式之间切换。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Line by 2 point](Sketcher_CreateLine.md): 从2点绘制线段。对于特定的约束而言，此工具绘制的是无限长的直线。


</div>

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arc](Sketcher_CreateArc.md): 从中心，半径，起始角度和最终角度绘制弧段。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [Arc by 3 Point](Sketcher_Create3PointArc.md): 根据圆周上的两个端点以及圆周上的另一个点来绘制弧段。


</div>

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Creates an arc of ellipse.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Creates an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Creates an arc of parabola.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Circle](Sketcher_CreateCircle.md): 从中心和半径画一个圆。


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Circle by 3 point](Sketcher_Create3PointCircle.md) : 从圆周上的三个点画一个圆。


</div>

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Creates an ellipse by its center, an endpoint of one of its axes, and a point along the ellipse. <small>(v1.0)</small> : Or by both endpoints of one of its axes and a point along the ellipse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Creates an ellipse by the endpoints of one of its axes and a point along the ellipse. <small>(v1.0)</small> : This is the same tool as [Ellipse by center](Sketcher_CreateEllipseByCenter.md) but with a different initial mode.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md): 从两个相反的点绘制一个矩形。


</div>

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md): Creates a centered rectangle. <small>(v1.0)</small> : This is the same tool as [Rectangle](Sketcher_CreateRectangle.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded rectangle](Sketcher_CreateOblong.md): Creates a rounded rectangle. Idem.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateTriangle.png  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md): 在几何圆草图中绘制一个正三角形。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> [Square](Sketcher_CreateSquare.md): 在几何圆草图中绘制一个正方形。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md): 在几何圆草图中绘制一个正五面。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md): 在几何圆草图中绘制一个正六边形。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md): 在几何圆草图中绘制一个正七边形。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md): 在几何圆草图中绘制一个正八边形。


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Create Regular Polygon](Sketcher_CreateRegularPolygon.md) : 根据指定的边数与拾取的两个点：中点与一个角点来绘制一个正多边形。


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Slot](Sketcher_CreateSlot.md): 通过选择一个半圆的中心和另一个半圆的终点绘制椭圆。


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Creates a B-spline curve by control points. <small>(v1.0)</small> : Or by knot points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Creates a periodic (closed) B-spline curve by control points. <small>(v1.0)</small> : This is the same tool as [B-spline by control points](Sketcher_CreateBSpline.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md): 将元素切换 到/从 草图模式。对象草图不会在3D几何操作中使用，并且仅在编辑包含它的草图时可见。这是 v0.15 中使用的图标。直到FreeCAD v0.16，用户必须先在草图编辑器中创建常规（白色）几何对象，然后使用此工具将其更改为"几何草图"（蓝色）。
-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md): 在FreeCAD v0.16中，添加了在构造模式下直接创建几何的能力，因此图标已更改为该图形。选择现有的草图编辑器几何图形，然后单击此工具可以在常规和构造模式之间切换几何图形，就像以前的FreeCAD版本一样。从FreeCAD v0.16开始，当没有选择草图编辑器几何图形时，选择此工具会更改将要创建将来的对象的模式（常规与构造）。


</div>



### 草图编辑器约束


<div class="mw-translate-fuzzy">

约束用于定义长度、在草图元素之间设置规则以及沿垂直和水平轴锁定草图。某些约束要求 [辅助约束](Sketcher_helper_constraint.md)


</div>

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md): Fixes the horizontal distance between two points or the endpoints of a line. If a single point is pre-selected, the distance is relative to the origin of the sketch.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Vertical Distance](Sketcher_ConstrainDistanceY.md): 修复两点或线端点之间的水平距离。如果只选择一项, 则将距离设置为原点。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md): 通过限制选定行的长度来定义其距离, 或通过限制两点之间的距离来定义它们之间的距离。


</div>

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Fixes the radius of arcs and B-spline weight circles, and the diameter of circles.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md): 通过限制半径来定义所选圆弧或圆的半径。
-   <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal Angle](Sketcher_ConstrainAngle.md): 定义两个选定行之间的内部角度。


</div>

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Fixes the diameter of circles and arcs.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Fixes the angle between two edges, the angle of a line with the horizontal axis of the sketch, or the aperture angle of a circular arc.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.png‎  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md): 通过设置相对于原点的垂直和水平距离来约束选定项, 从而锁定该项的位置。这些约束距离可以在以后进行编辑。


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident.md): 在一个或多个点上(同时)附加一个点。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Point On Object](Sketcher_ConstrainPointOnObject.md): 将点附加到另一对象上, 如直线、圆弧或轴。


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Horizontal.png  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md): 将所选线条或折线元素约束为真正的水平方向。在应用此约束之前, 可以选择多个对象。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical.md): 将所选线条或折线元素约束为真正的垂直方向。在应用此约束之前, 可以选择多个对象。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel.md): 约束两条或多行平行于彼此。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Perpendicular.png  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md): 约束两条垂直于彼此的线, 或约束垂直于弧线端点的直线。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent.md): 在两个所选实体之间创建切线约束, 或在两个线段之间建立共线约束。 直线段不必直接位于圆弧或圆上, 而将其与圆弧或圆相切。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Equal Length](Sketcher_ConstrainEqual.md): 约束两个选定的实体彼此相等。 如果在圆或弧形上使用它们的半径将被设置为相等。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md): 将两个点对称地约束在一条直线上, 或者将前两个点对称地限制在第三个选定点上。


</div>

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Block](Sketcher_ConstrainBlock.md): Blocks edges in place with a single constraint. It is mainly intended for B-splines.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell\'s Law](Sketcher_ConstrainSnellsLaw.md): 约束两条线服从折射定律来模拟通过界面的光。<small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstraint.png  style="width:32px;"> [Toggle Constraint](Sketcher_ToggleDrivingConstraint.md): 将工具栏或所选约束切换到/从参照模式。<small>(v0.16)</small> 


</div>

  - <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md): Activates or deactivates selected constraints.



### 草图工具

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md): 在一条线之间加入两条线之间的圆角。选择两行或单击角点，然后激活该工具。


</div>

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Trimming](Sketcher_Trimming.md): 相对于点击的点修剪线，圆或圆弧。


</div>

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits an edge while transferring most constraints.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extend](Sketcher_Extend.md): 将一条线或一条弧延长至一条边界线、弧、椭圆形、椭圆形上的弧或空间中的一个点处。 <small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [External Geometry](Sketcher_External.md): 创建与外部几何相关联的边。


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [CarbonCopy](Sketcher_CarbonCopy.md): 复制另一张草图中的几何体图形。 <small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.png‎  style="width:32px;"> [Select Origin](Sketcher_SelectOrigin.md): 选择草图的原点 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.png‎  style="width:32px;"> [Select Horizontal Axis](Sketcher_SelectHorizontalAxis.md): 选择草图的水平轴 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.png‎  style="width:32px;"> [Select Vertical Axis](Sketcher_SelectVerticalAxis.md): 选择草图的垂直轴 <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetry](Sketcher_Symmetry.md): Creates mirrored copies of selected elements.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md): Removes the axes alignment of selected edges by replacing [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) constraints with [Parallel](Sketcher_ConstrainParallel.md) and [Perpendicular](Sketcher_ConstrainPerpendicular.md) constraints.

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Delete all geometry](Sketcher_DeleteAllGeometry.md): Deletes all geometry and all constraints from the sketch.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Delete all constraints](Sketcher_DeleteAllConstraints.md): Deletes all constraints from the sketch.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

### Sketcher B-spline tools 

-   <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:32px;"> [Convert geometry to B-spline](Sketcher_BSplineConvertToNURBS.md): Converts edges to B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md): Increases the degree (order) of B-splines.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md): Increases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md): Decreases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Select unconstrained DoF](Sketcher_SelectElementsWithDoFs.md): Selects the not fully constrained elements in the sketch.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.png‎  style="width:32px;"> [Select Constraints](Sketcher_SelectConstraints.md): 选择草图编辑器元素的约束 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.png‎  style="width:32px;"> [Select Elements Associated with constraints](Sketcher_SelectElementsAssociatedWithConstraints.md): 选择与约束关联的草图编辑器元素 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.png‎  style="width:32px;"> [Select Redundant Constraints](Sketcher_SelectRedundantConstraints.md): 选择草图的冗余约束 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.png‎  style="width:32px;"> [Select Conflicting Constraints](Sketcher_SelectConflictingConstraints.md): 选择草图的冲突约束 <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:

  - <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md): Shows or hides the B-spline degree in all sketches.

  - <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Show/hide B-spline control polygon](Sketcher_BSplinePolygon.md): Shows or hides the B-spline control polygon in all sketches.

  - <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md): Shows or hides the B-spline curvature comb in all sketches.

  - <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md): Shows or hides the B-spline knot multiplicity in all sketches.

  - <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md): Shows or hides the B-spline control point weight in all sketches.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md): Deletes the internal geometry of elements, or recreates missing internal geometry.

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Switch virtual space](Sketcher_SwitchVirtualSpace.md): (un)hides constraints or switches the visible virtual space.

### Obsolete tools 

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clone](Sketcher_Clone.md): Clones a Sketcher element. Not available in <small>(v1.0)</small> .


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.png‎  style="width:32px;"> [Close Shape](Sketcher_CloseShape.md): 通过对端点应用重合约束创建闭合形状 <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.png‎  style="width:32px;"> [Connect Edges](Sketcher_ConnectLines.md): 通过对端点应用重合约束来连接草图编辑器器元素 <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copy](Sketcher_Copy.md): Copies a Sketcher element. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Move](Sketcher_Move.md): Moves the selected geometry taking as reference the last selected point. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rectangular array](Sketcher_RectangularArray.md): Creates an array of selected Sketcher elements. Not available in <small>(v1.0)</small> .

## Preferences

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferences](Sketcher_Preferences.md): Preferences for the Sketcher Workbench.

## Best practices 


<div class="mw-translate-fuzzy">

## 最佳做法

每个CAD用户随着时间的推移发展自己的工作方式，但跟随一些有用的一般原则。


</div>


<div class="mw-translate-fuzzy">

-   一系列简单的草图比单个复杂的草图更容易管理。例如，可以为基础3D特征（衬垫或旋转）创建第一个草图，而第二个可以包含孔或切口（凹坑）。一些细节可以省略，稍后将作为3D功能实现。如果太多，你可以选择避免草图中的圆角，并将其添加为3D功能。
-   始终创建一个封闭的配置文件，或者你的草图不会产生实体，而是一组开放的面。如果你不希望将某些对象包含在实体创建中，请使用"构造模式"工具将其转换为构造元素。
-   使用自动约束特性来限制你必须手动添加的约束数量。
-   作为一般规则，首先应用几何约束，然后应用尺寸约束，并最后锁定草图。但请记住：规则被破坏。如果你在操作草图时遇到问题，在完成配置文件之前先限制几个对象可能很有用。
-   如果可能，将草图中心定位到具有锁定约束的原点（0,0）。如果你的草图不对称，请将其中一个点定位到原点，或者为锁定距离选择好的圆角参数。在v0.12中，外部约束（将草图约束到现有3D几何像边缘或其他草图）未实现。这意味着要将以下草图定位到你的第一个草图中，你需要手动设置相对于你的第一个草图的距离。一个基于原点的（25,75）的锁定约束比（23.47,73.02）更容易记住。
-   如果你有可能在长度约束和水平或垂直距离约束之间进行选择，则选择后者。水平和垂直距离约束在计算上更便宜。
-   一般来说，最好使用的约束是：水平和垂直约束;水平和垂直长度约束;点对点相切。如果可能，限制使用这些：一般长度约束;边缘到边缘相切;固定点到线约束;对称约束


</div>




<div class="mw-translate-fuzzy">

### 教程


</div>

-   [Sketcher Lecture](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a more than 80 page PDF document that serves as a detailed manual for the Sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) for beginners
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimum requirement for a sketch and Complete determination of a sketch

## Scripting

The [Sketcher scripting](Sketcher_scripting.md) page contains examples on how to create constraints from Python scripts.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">


<div class="mw-translate-fuzzy">


</div>


{{Sketcher_Tools_navi

}} 

[分类:用户文档](Category:User_Documentation/zh-cn.md)



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/zh-cn
