# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/zh-cn


{{TOCright}}

## 简介


<div class="mw-translate-fuzzy">

[ 草图工作台用于创建用于](Sketcher_Workbench.md)[ 零件工作台](PartDesign_Workbench/zh-cn.md)、[ 建筑工作台和其他工作台的二维几何图形](Arch_Workbench/zh-cn.md)。 通常，二维绘图被视为大多数CAD模型的起点，因为二维草图可以"拉伸"以创建三维形状；进一步的二维草图可以用于在先前构建的三维形状的基础上创建其他特征，如开槽"Pocket"、隆起"ridges"或拉伸。 草图绘制器与在[零件设计工作台中定义的布尔操作一起构成了构建实体的](PartDesign_Workbench/zh-cn.md)[构造实体几何方法的基础](constructive_solid_geometry/zh-cn.md)。此外，草图绘制器还与[零件设计工作台操作一起构成了创建实体的](PartDesign_Workbench/zh-cn.md)[特征编辑方法的基础](feature_editing/zh-cn.md)。


</div>

草图工作台本身具有约束条件 - 允许将2D形状约束到精确的几何定义。以及一个约束求解器，它计算二维几何约束范围，并允许对草图自由度的交互式探索。

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*一个全约束草图*

## Basics of constraint sketching 


<div class="mw-translate-fuzzy">

## 约束草图的基础

为了解释草图编辑器的工作原理，将其与"传统的"起草方式进行比较可能是有用的。


</div>

#### Traditional Drafting 


<div class="mw-translate-fuzzy">

#### 传统起草

CAD绘图的传统方式继承于旧的[绘图板](http://en.wikipedia.org/wiki/Drawing_board). [正交（2D）视图](http://en.wikipedia.org/wiki/Multiview_orthographic_projection) 手动绘制，用于生产技术图纸（也称为蓝图）。对象被精确地绘制到预期的尺寸或尺寸上。如果要从（0,0）开始绘制长度为100mm的水平线，您可以激活线条工具，点击屏幕或输入第一个点的（0,0）坐标，然后再次点击或在（100,0）处输入第二点坐标。或者你会画你的线，而不考虑它的位置，然后移动它。绘制几何图形后，可以向其添加尺寸。


</div>

#### Constraint Sketching 


<div class="mw-translate-fuzzy">

#### 约束草图

**草图**远离这个逻辑。对象不需要完全按照您的意图进行绘制，因为它们将在稍后被约束定义。对象可以松散绘制，只要不受约束，就可以进行修改。它们实际上是"浮动"，可以移动，拉伸，旋转，缩放等等。这在设计过程中给予了很大的灵活性。


</div>

#### What are constraints? 


<div class="mw-translate-fuzzy">

#### 什么是约束？

使用约束来限制对象的自由度。例如，没有约束的线条具有4 [自由度](#Degrees_Of_Freedom.md)（简写为"DOF"）：可以水平或垂直移动，可以被拉伸，并且可以旋转。


</div>

应用水平或垂直约束或角度约束（相对于另一条线或与其中一条轴）将限制其旋转能力，从而使其具有3个自由度。锁定其原点之一的点将消除另外2个自由度。并且应用维度约束将消除最后的自由度。然后，该行被认为是"完全受限制的"。


<div class="mw-translate-fuzzy">

多个对象可以彼此约束。可以通过其中一个点与重合点约束连接两条线。可以在它们之间设置一个角度，或者它们可以垂直设置。一条线可以与弧或圆相切，依此类推。具有多个对象的复杂草图将具有多种不同的解决方案，并使其"完全受约束"，这意味着基于所应用的约束只能达到其中一种可能的解决方案。


</div>


<div class="mw-translate-fuzzy">

有两种约束：几何和尺寸。它们在下面的[\'工具\'部分中详细介绍](#The_tools.md)。


</div>

#### What the Sketcher is not good for 


<div class="mw-translate-fuzzy">

## 草图编辑器不擅长于

草图编辑器不打算制作2D蓝图。草图一旦用于生成实体特征后，会自动隐藏。约束仅在草图编辑模式下可见。


</div>


<div class="mw-translate-fuzzy">

如果您仅需要生成2D视图进行打印，并不想创建3D模型，请查看[底图工作台](Draft_Workbench/zh-cn.md)（请注意，底图工作台也可用于创建此时草图编辑器中不可用的2D几何，如B-Splines。）


</div>

## Sketching Workflow 

## 草图工作流程

草图总是二维（2D）。要创建一个实体，创建单个封闭区域的2D草图，然后垫高或旋转以添加第三维，从2D草图创建3D实体。

如果草图具有彼此交叉的段，其中一个点不直接位于段上的位置，或相邻段的端点之间存在间隙的位置，垫高或旋转将不会创建一个实体。这个规则的例外是它不适用于构造（蓝色）几何对象。

在封闭区域内，我们可以有较小的非重叠区域。当创建3D实体时，这些将变为空白。

Once a Sketch is fully constrained, the Sketch features will turn green; Construction Geometry will remain blue. It is usually \"finished\" at this point and suitable for use in creating a 3D solid. However, once the Sketch dialog is closed it may be worthwhile going to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and running **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Check geometry](Part_CheckGeometry.md)** to ensure there are no features in the Sketch which may cause later problems.

## Tools


<div class="mw-translate-fuzzy">

## 工具

草图工作台工具都位于加载草图工作台时出现的草图菜单中。


</div>

### General

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [创建草图](Sketcher_NewSketch/zh-cn.md): 在所选的面或平面上创建新的草图。如果在执行此工具时未选择任何面, 则系统将提示用户从弹出窗口中选择一个平面。

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [编辑草绘](Sketcher_EditSketch/zh-cn.md): 编辑已选择的草图。这会开启[草图对话框](Sketcher_Dialog.md)。

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [离开草图](Sketcher_LeaveSketch/zh-cn.md): 离开草图编辑模式。

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [查看草图](Sketcher_ViewSketch/zh-cn.md): 设置垂直于草图平面的模型视图。

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [查看截面](Sketcher_ViewSection/zh-cn.md): 创建一个截面，并暂时隐藏此草图平面前侧的所有内容。

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [映射草图至面](Sketcher_MapSketch/zh-cn.md): 将草图映射到以前选定的实心面。

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [调整草图方向](Sketcher_ReorientSketch/zh-cn.md): 允许您更改草图的位置

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [校验草图...](Sketcher_ValidateSketch/zh-cn.md): 它允许你检查是否有不同点的公差和匹配。

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [合并草图](Sketcher_MergeSketches/zh-cn.md): 合并两个或多个草图。

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [镜像草图](Sketcher_MirrorSketch/zh-cn.md): 沿 x 轴、y轴或原点镜像草图。

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): When in edit mode, stop the current operation, whether that is drawing, setting constraints, etc.

#### 草图编辑器几何工具

这是创建对象的工具。

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint.md): 绘制一个点.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Line by 2 point](Sketcher_CreateLine.md): 从2点绘制线段。对于特定的约束而言，此工具绘制的是无限长的直线。


</div>

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Create an arc](Sketcher_CompCreateArc.md): 这是一个位于草图工作台中的图标菜单，其中列有下列命令：

:\* <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arc](Sketcher_CreateArc.md): 从中心，半径，起始角度和最终角度绘制弧段。


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [Arc by 3 Point](Sketcher_Create3PointArc.md): 根据圆周上的两个端点以及圆周上的另一个点来绘制弧段。


</div>

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Create a circle](Sketcher_CompCreateCircle.md): 这是一个位于草图工具栏中的图标菜单，其中列有下列命令：

:\* <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Circle](Sketcher_CreateCircle.md): 从中心和半径画一个圆。

:\* <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Circle by 3 point](Sketcher_Create3PointCircle.md) : 从圆周上的三个点画一个圆。


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Conics.png  style="width:32px;"> [Conic sections](Sketcher_CompCreateConic.md): 草图工作台提供了以下圆锥曲线工具。与B样条不同的是，可对这些圆锥曲线使用各种约束，如切线、对象上的点或正交。
    -   <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md) : 通过中心点，大半径点和小半径点绘制椭圆。 <small>(v0.15)</small> 
    -   <img alt="" src=images/Sketcher_CreateEllipse_3points.png  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md) : 用大直径（2点）和小半径点绘制椭圆。 <small>(v0.15)</small> 
    -   <img alt="" src=images/Sketcher_Elliptical_Arc.png  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md) : 通过中心点，主要半径点，起点和终点绘制椭圆弧。 <small>(v0.15)</small> 
    -   <img alt="" src=images/Sketcher_Hyperbolic_Arc.png  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): 绘制双曲线弧。 <small>(v0.17)</small> 
    -   <img alt="" src=images/Sketcher_Parabolic_Arc.png  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): 画出抛物线弧。 <small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [Create a B-spline](Sketcher_CompCreateBSpline.md): 这是一个位于草图工作台中的图标菜单，其中列有下列命令：
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Create B-spline](Sketcher_CreateBSpline.md): 利用控制点来绘制一条B样条曲线。<small>(v0.17)</small> 
    -   <img alt="" src=images/Sketcher_Create_Periodic_BSpline.svg  style="width:32px;"> [Create periodic B-spline](Sketcher_CreatePeriodicBSpline.md): 利用控制点来绘制一条周期性（periodic，此处为闭合closed之意）的B样条曲线。<small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline (multiple-point line)](Sketcher_CreatePolyline.md): 绘制由多个线段组成的线。绘制折线时，按M键可在不同的折线模式之间切换。


</div>

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Create rectangles](Sketcher_CompCreateRectangles.md): This is an icon menu in the Sketcher toolbar that holds the following commands: <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md): 从两个相反的点绘制一个矩形。


</div>

:\* <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered Rectangle](Sketcher_CreateRectangle_Center.md): Draws a rectangle from a central point and an edge point. <small>(v0.20)</small> 

:\* <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded Rectangle](Sketcher_CreateOblong.md): Draws a rounded rectangle from 2 opposite points. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Create regular polygon](Sketcher_CompCreateRegularPolygon.md): 这是一个位于草图工具栏中的图标菜单，其中列有下列命令：

-   <img alt="" src=images/Sketcher_CreateTriangle.png  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md): 在几何圆草图中绘制一个正三角形。

-   <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> [Square](Sketcher_CreateSquare.md): 在几何圆草图中绘制一个正方形。

-   <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md): 在几何圆草图中绘制一个正五面。

-   <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md): 在几何圆草图中绘制一个正六边形。

-   <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md): 在几何圆草图中绘制一个正七边形。

-   <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md): 在几何圆草图中绘制一个正八边形。

:\* <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Create Regular Polygon](Sketcher_CreateRegularPolygon.md) : 根据指定的边数与拾取的两个点：中点与一个角点来绘制一个正多边形。

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Slot](Sketcher_CreateSlot.md): 通过选择一个半圆的中心和另一个半圆的终点绘制椭圆。

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md): 在一条线之间加入两条线之间的圆角。选择两行或单击角点，然后激活该工具。


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Trimming](Sketcher_Trimming.md): 相对于点击的点修剪线，圆或圆弧。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extend](Sketcher_Extend.md): 将一条线或一条弧延长至一条边界线、弧、椭圆形、椭圆形上的弧或空间中的一个点处。 <small>(v0.17)</small> 


</div>

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits a line or an arc into two, converts a circle into an arc while keeping most of the constraints. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [External Geometry](Sketcher_External.md): 创建与外部几何相关联的边。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [CarbonCopy](Sketcher_CarbonCopy.md): 复制另一张草图中的几何体图形。 <small>(v0.17)</small> 


</div>

-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md): 将元素切换 到/从 草图模式。对象草图不会在3D几何操作中使用，并且仅在编辑包含它的草图时可见。这是 v0.15 中使用的图标。直到FreeCAD v0.16，用户必须先在草图编辑器中创建常规（白色）几何对象，然后使用此工具将其更改为"几何草图"（蓝色）。
-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md): 在FreeCAD v0.16中，添加了在构造模式下直接创建几何的能力，因此图标已更改为该图形。选择现有的草图编辑器几何图形，然后单击此工具可以在常规和构造模式之间切换几何图形，就像以前的FreeCAD版本一样。从FreeCAD v0.16开始，当没有选择草图编辑器几何图形时，选择此工具会更改将要创建将来的对象的模式（常规与构造）。

### 草图编辑器约束

约束用于定义长度、在草图元素之间设置规则以及沿垂直和水平轴锁定草图。某些约束要求 [辅助约束](Sketcher_helper_constraint.md)

#### Geometric constraints 


<div class="mw-translate-fuzzy">

#### 几何约束

不与数值数据关联


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident.md): 在一个或多个点上(同时)附加一个点。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Point On Object](Sketcher_ConstrainPointOnObject.md): 将点附加到另一对象上, 如直线、圆弧或轴。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical.md): 将所选线条或折线元素约束为真正的垂直方向。在应用此约束之前, 可以选择多个对象。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Horizontal.png  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md): 将所选线条或折线元素约束为真正的水平方向。在应用此约束之前, 可以选择多个对象。


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

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Block](Sketcher_ConstrainBlock.md): it blocks an edge from moving, that is, it prevents its vertices from changing their current positions. It should be particularly useful to fix the position of B-Splines. See the [Block Constraint forum topic](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Dimensional constraints 


<div class="mw-translate-fuzzy">

#### 尺寸約束

**与数值数据关联**

对于这些约束, 可以使用[表达式](Expressions/zh-cn.md)。数据可能取自 [电子表格](Spreadsheet_Workbench/zh-cn.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.png‎  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md): 通过设置相对于原点的垂直和水平距离来约束选定项, 从而锁定该项的位置。这些约束距离可以在以后进行编辑。


</div>

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md): Fixes the horizontal distance between two points or line endpoints. If only one item is selected, the distance is set to the origin.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Vertical Distance](Sketcher_ConstrainDistanceY.md): 修复两点或线端点之间的水平距离。如果只选择一项, 则将距离设置为原点。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md): 通过限制选定行的长度来定义其距离, 或通过限制两点之间的距离来定义它们之间的距离。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md): 通过限制半径来定义所选圆弧或圆的半径。
-   <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal Angle](Sketcher_ConstrainAngle.md): 定义两个选定行之间的内部角度。


</div>

#### Special constraints 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell\'s Law](Sketcher_ConstrainSnellsLaw.md): 约束两条线服从折射定律来模拟通过界面的光。<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> [Internal Alignment](Sketcher_ConstrainInternalAlignment.md): 将所选元素与所选形状对齐 (例如, 一条线成为椭圆的主轴)。


</div>

#### Constraint tools 

The following tools can be used the change the effect of constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstraint.png  style="width:32px;"> [Toggle Constraint](Sketcher_ToggleDrivingConstraint.md): 将工具栏或所选约束切换到/从参照模式。<small>(v0.16)</small> 


</div>

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/Deactivate constraint](Sketcher_ToggleActiveConstraint.md): Enable or disable an already placed constraint. <small>(v0.19)</small> 

### 草图工具

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Select solver DOFs](Sketcher_SelectElementsWithDoFs.md): Highlights in green the geometry with degrees of freedom (DOFs), i.e. not fully constrained.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.png‎  style="width:32px;"> [Close Shape](Sketcher_CloseShape.md): 通过对端点应用重合约束创建闭合形状 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.png‎  style="width:32px;"> [Connect Edges](Sketcher_ConnectLines.md): 通过对端点应用重合约束来连接草图编辑器器元素 <small>(v0.15)</small> 


</div>


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

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Show/Hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md): Recreates missing/deletes unneeded internal geometry of a selected ellipse, arc of ellipse/hyperbola/parabola or B-spline.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.png‎  style="width:32px;"> [Select Origin](Sketcher_SelectOrigin.md): 选择草图的原点 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.png‎  style="width:32px;"> [Select Vertical Axis](Sketcher_SelectVerticalAxis.md): 选择草图的垂直轴 <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.png‎  style="width:32px;"> [Select Horizontal Axis](Sketcher_SelectHorizontalAxis.md): 选择草图的水平轴 <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetry](Sketcher_Symmetry.md): Copies a sketcher element symmetrical to a chosen line.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clone](Sketcher_Clone.md): Clones a sketcher element.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copy](Sketcher_Copy.md): Copies a sketcher element.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Move](Sketcher_Move.md): Moves the selected geometry taking as reference the last selected point.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rectangular Array](Sketcher_RectangularArray.md): Creates an array of selected sketcher elements.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove Axes Alignment](Sketcher_RemoveAxesAlignment.md): Remove axes alignment while trying to preserve the constraint relationship of the selection. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Delete All Geometry](Sketcher_DeleteAllGeometry.md): Deletes all geometry from the sketch.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Delete All Constraints](Sketcher_DeleteAllConstraints.md): Deletes all constraints from the sketch.

### Sketcher B-spline tools 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Show/hide B-spline control polygon](Sketcher_BSplinePolygon.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Convert geometry to B-spline](Sketcher_BSplineApproximate.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md), <small>(v0.20)</small> 

### Sketcher virtual space 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Switch Virtual Space](Sketcher_SwitchVirtualSpace.md): Allows you to hide all constraints of a sketch and make them visible again.

## Preferences

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Preferences](Sketcher_Preferences.md): Preferences for the **Sketcher** workbench.

## Best Practices 


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

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a 70-page long PDF document that serves as a detailed manual for the sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) for beginners
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimum requirement for a sketch and Complete determination of a sketch

## Scripting

The [Sketcher scripting](Sketcher_scripting.md) page contains examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}} 

[分类:用户文档](Category:User_Documentation/zh-cn.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/zh-cn
