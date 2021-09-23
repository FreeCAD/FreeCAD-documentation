---
- GuiCommand:
   Name:Part Extrude
   MenuLocation:Part → Extrude
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Draft Trimex](Draft_Trimex.md)
---

# Part Extrude/zh-cn

![600px](images/Part_Extrude_demo.png)

## 描述

**零件挤型**工具根据用户指定的距离以特定方向将一个形状挤压成型。根据输入的形状类型与可选项的具体选择，输出的形状类型会有所不同。


<div class="mw-translate-fuzzy">

下列内容为：在大多常见的情景中，根据指定的输入形状类型可能输出的形状类型，

-   对一个顶点（点）进行挤型操作，将生成一个线性的边（线）
-   对一个开放的边（例如，线、弧）进行挤型操作，将生成一个开放的面（如，平面）
-   对一个闭合的边（例如，圆）进行挤型操作，将生成一个闭合面（如，一个开放端面的圆柱体），或者，如果如果参数\"solid\"为\"true\"将生成一个实体（如，一个闭合的实心圆柱体）
-   对一个开放的连线（例如，一条底图连线）进行挤型操作，将生成一个开放的壳（若干互连的面）
-   对一个闭合的连线（例如，一条底图连线）进行挤型操作，将根据可选项生成一个壳（若干连接的面），如果参数\"solid\"为\"true\"将生成一个实体
-   对一个面（例如，平面）进行挤型操作，将生成一个实体（例如，长方体）
-   对一个[Draft Shape String进行挤型操作](Draft_ShapeString.md)，将生成一个复合实体（生成的字符串是由多个字母实体复合而成）
-   对壳中的多个面进行挤型操作，将生成一个复合实体。


</div>


<div class="mw-translate-fuzzy">

## 如何使用

1.  在3D视图或模型树中选中待挤型的（多个）形状
2.  点击工具栏中的**<img src="images/Part_Extrude.png" width=16px> '''Extrude'''** 图标，或前往Part → Extrude菜单
3.  设置挤型的方向与长度，以及其他可选参数（参见后面的[参数部分获得更多详情](#Parameters.md)）。
4.  单击OK。


</div>


<div class="mw-translate-fuzzy">

或者，可以先加载工具，而后再通过任务面板中的列表来选择待挤型的一个或多个形状。


</div>

操作完成后，模型树将列出与被选形状一样多的挤型对象。而每一个输入形状都将被置于其挤型对象之下。

## 参数

挤型对象由下列参数定义而成，可在创建挤型对象后于数据选项卡中对其参数进行编辑调整。

-   **Base**: 输入的形状（挤型工具工作时要用到的基本形状）

-   **Dir**: 挤型方向。如果**Dir Mode**为\'Custom\'，您就可以编辑**Dir**。 否则，**Dir**仅为只读，且根据连接形状（linked shape）开始计算。

-   **Dir Link**: 以参数化的方式连接至一条边（线），从而设置挤型方向。自v0.17版起，属性编辑器中不在支持此属性。

-   **Dir Mode**: 设置如何控制**Dir**参数。\'Custom\'选项意味着**Dir**是可编辑的。\'Edge\'表示Dir要通过**Dir Link**根据一条待连接的边（线）来确定。而\'Normal\'则表示Dir正交于输入形状的所在平面。

-   **Length Fwd**: 挤型的距离。如果**Length Fwd**与**Length Rev**皆为0，则采用**Dir**向量的长度。

-   **Length Rev**: 另一种与**Dir**方向相反的挤型长度。

-   **Solid**: 如果此项为True，对一条闭合边或一条闭合连线进行挤型，将生成一个对应实体。如果此项为False，则生成一个对应的壳。

-   **Reversed**: 将挤型对象调转至**Dir**的相反方向。

-   **Symmetric**: 如果此项为True，则以输入形状为中心向指定方向及其相反方向进行挤型，且挤型总长度为**Length Fwd**。并忽略**Length Rev**。

-   **Taper Angle** and **Taper Angle Rev**: applies an angle to the extrusion, so that sides of the extrusion are drafted by the specified angle. Positive angle means the cross-section expands. **Taper Angle Rev** sets the taper for the reversed part of the extrusion (the part from **Length Rev**). As of v0.17, tapered extrusion is only supported for wires with no holes. Taper does not work well if the extruded shape contains B-splines.

-   **Face Maker Class**: sets C++ class name of face making code, which is used when making solids from wires. This property is here mainly for maintaining backward compatibility. Do not touch, unless you know what you are doing.

-   **Placement**: 标准的[定位参数集](Placement.md)


<div class="mw-translate-fuzzy">

-   **Label**: 显示在模型树中的标签（创建挤型对象后方可使用）


</div>

## Task对话框

![](images/Part_Extrude_dialog.png )


<div class="mw-translate-fuzzy">

-   OK: 创建挤型对象，并关闭对话框。


</div>


<div class="mw-translate-fuzzy">

-   Close: 关闭对话框，神马也不做。


</div>


<div class="mw-translate-fuzzy">

-   Apply: 创建挤型对象，却并不关闭此对话框。您可以继续在下侧的列表中选择另一个形状，以此创建更多的挤型对象。点击Apply可以多次创建多个挤型对象。


</div>

-   \'Direction\' 单选按钮：设置计算挤型方向的方式。

-    **Select**button: click it, and then pick an edge in [3D view](3D_view.md). That edge will appear in text field next to the button, in format \"ObjectName:EdgeN\". You can also type the link manually. Values X,Y,Z will be filled according to the edge direction.


<div class="mw-translate-fuzzy">

-   X, Y, Z 按钮：点击X按钮来设置+X轴上的挤型方向。再次点击则设置-X轴上的挤型方向。


</div>

-    **X**, **Y**, **Z** input fields: set or display the direction vector of extrusion. If both lengths are zero, the length of this vector sets the length of extrusion, and values are always in mm, regardless of unit preferences.

-   Length fields: 设置挤型的长度。此输入框支持用户输入的单位。

-   Symmetric: 以对称的方式向指定方向及其反向进行挤型，因此输入形状将位于生成挤型对象的中部。

-   Taper Outward Angle: positive angle means profile is expanded at other end of extrusion.

-   Create Solid checkbox: 如果选中此项，对一条闭合的连线或边进行挤型将生成一个对应实体。如果在调用挤型工具之前便提前选中了一条闭合连线，则此项是默认选中的。

-   Shape list: 在此选择待挤型的形状。如果选中了多个形状，则将创建多个挤型对象。

## Notes

-   The task dialog does not offer a preview, yet. **Apply** will create an extrusion object every time you click it, which can be useful as preview; however, they will remain and yet another one will be created as you click **OK**. [Undo](Std_Undo.md) can be useful to clean them up before clicking **OK**.

-    <small>(v0.17)</small> A sketch created from within PartDesign cannot be used for Part Extrude, if it is within a Body (\"Links go out of allowed scope\" error). In order to Part-Extrude a sketch, you should create the sketch from Sketcher workbench. Or you can just drag a PartDesign one out of a Body.

-   Extrusion with taper angle does not support holes. It also may give bogus results if the number of segments in the profile changes as a result of taper.


<div class="mw-translate-fuzzy">

## 与[PartDesign Pad的比较](PartDesign_Pad.md) 


</div>

PartDesign Pad也是一种挤型功能，但是与本页描述的挤型工具大有不同。

零件挤型工具总是创建孤立的形状。而PartDesign Pad则把挤压成型的独立形状与其余体对象融合在一起。


<div class="mw-translate-fuzzy">

零件挤型工具并不关心对象在模型树中的具体位置。而PartDesign Pad却只能存在于[PartDesign Body中](PartDesign_Body.md)。


</div>

除了实体与复合实体（compsolid）以外，零件挤型工具能够对任意有着零件几何体（OCC形状）的对象执行挤压成型操作。另外，此工具还不能对其他对象上的单体面（individual face）进行挤型。而PartDesign Pad则只能接受草图Sketch（以及其他对象类型中的一小部分）或者实体上的单个面作为轮廓。

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Extrude/zh-cn
