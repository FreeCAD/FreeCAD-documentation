---
- GuiCommand   *
   Name   *Draft Wire
   MenuLocation   *Drafting → Polyline
   Workbenches   *[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut   ***P** **L**
   Version   *0.7
   SeeAlso   *[Draft Line](Draft_Line.md), [Draft BSpline](Draft_BSpline.md)
---

# Draft Wire/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描绘

利用连线工具可创建一条折线(一系列互连的线段)。本工具利用[底图工具栏中的](Draft_Tray.md)[底图线条样式进行绘制](Draft_Linestyle.md)。除了允许用户输入2个以上的点之外，连线工具与[底图线段工具的行为完全相同](Draft_Line.md)。


</div>

The corners of a Draft Wire can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide the edges of a Draft Wire by changing its **Subdivisions** property.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width   *400px;"> 
*多点定一连线*

## Create

### Usage

See also   * [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## 如何使用

1.  按下**<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire/zh-cn.md)**按钮，或先按**W**键再按**I**键。
2.  在3D视图中点击第一个点，或输入一个坐标再按**<img src="images/Draft_AddPoint.svg" width=16px> add point**按钮。
3.  在3D视图中单击另一个点，或输入一个坐标再按**<img src="images/Draft_AddPoint.svg" width=16px> add point**按钮。
4.  按**Esc**键或**Close**按钮来结束本次编辑。


</div>

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## 选项

-   按**A**键或**<img src="images/Draft_FinishLine.png" width=12px> Finish**按钮来结束当前连线的绘制，并关闭对此连线的编辑。
-   按**O**键或**<img src="images/Draft_CloseLine.png" width=12px> Close**按钮令当前连线闭合，即一条线段将连接当前连线首尾两点，从而构成一个面。而构成一个面则最少需要三个点。
-   按**W**键或**<img src="images/Draft_Wipe.svg" width=12px> Wipe**按钮来移除刚画好的线段，但是将继续保持从前一个点的位置继续编辑连线。
-   按**U**键或**<img src="images/Draft_SelectPlane.svg" width=12px> [Set WP](Draft_SelectPlane.md)**按钮根据前一个点的方位来调整当前的工作平面。
-   在创建一个点后，按**X**、**Y**或 **Z**键来在对应轴上约束下一个点。
-   为了手动输入坐标，每当设置好X、Y、Z分量后都要按下**Enter**键。当您需要以特定坐标值插入一个点时，可点击**<img src="images/Draft_AddPoint.svg" width=16px> |add point**按钮。
-   按**R**键或点击relative多选框切换至*相对* 模式。若开启了相对模式，则后一个相对于前一个的坐标而定；否则采用绝对坐标，即相对原点(0,0,0)定后一个点的坐标。
-   按**T**键或点击continue多选框切换至*连续（绘制）*模式。若开启了连续模式，则连线工具在绘制一条连线后会自动重启，即允许您在不用点击连线工具的情况下，继续绘制下一条连线。
-   按**L**键或点击filled多选框切换至*填充*模式。若开启了填充模式，则一条闭合的连线将创建出一个填充面(**Make Face** `True`); 否则，闭合的连线将不会创建出一个面(**Make Face** `False`)。

   *   
    **请注意   ***若连线存在自相交的情况，便不能对其进行填充存在，因为它将无法创建对应真面（proper face）。如果对连线填充后却无法看到它本身的形状，就手动将**Make Face**设置为`False`来查看连线。

-   按住**Ctrl**键，将当前所绘点强制放在与之最近的[捕捉位置处](Draft_Snap.md)。
-   按住**Shift**键，将下一个点的位置[约束于上一个的水平方向或垂直方向上](Draft_Constrain.md)。
-   按**Ctrl**+**Z**组合键或点击{{button|<img src="images/Draft_UndoLine.png" width=12px> Undo}}按钮来撤销当前操作，返回上一个操作点。
-   按**Esc**键或{{button|Close}}按钮来终止当前连线命令；但此前绘制好的线段仍会保留。


</div>

## Join

### Usage 

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut   * **P** then **L**.

## Notes


<div class="mw-translate-fuzzy">

双击树状视图中的元素或点击**<img src="images/Draft_Edit.svg" width=16px> [[Draft Edit]]**按钮即可编辑连线。接下来，您可以将其中的点移到一个新位置，或点击**<img src="images/Draft_AddPoint.svg" width=16px> add point**或**<img src="images/Draft_DelPoint.svg" width=16px> remove point**按钮再点选连线来增添其中的点。


</div>

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode   * **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Properties

See also   * [Property editor](Property_editor.md).

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### 数据

-    **Start**   * 指定连线中的第一个点。

-    **End**   * 指定连线中的最后一个点，如果是闭合连线则不计入初始点。

-    **Closed**   * 指定连线是否闭合。如果连线原本是开放的，此值为`False`；将其设置为`True`则为会原连线再绘制一条线段使之闭合。如果连线原本就是闭合的，此值为`True`；将其设置为`False`则会从连线中去掉最后一条线段，令其变为开放连线。

-    **Chamfer Size**   * specifies the size of the chamfers (straight segments) created on the corners of the wire.

-    **Fillet Radius**   * specifies the radius of the fillets (arc segments) created on the corners of the wire.

-    **Make Face**   * 指定是否令连线构成一个面。如果为`True`则创建一个面，否则仅绘制本对象中的边。如果**Closed**为`True`时，本属性才会生效。

   *   
    **请注意   ***如果连线自相交，则不要将**Make Face**设置为`True`，因为在这种情况下不能用它来创建一个真面（proper face）。

-    **Subdivisions**   * 指定连线中每条线段内的内部节点数量。<small>(v0.16)</small> 

-    **Length**   * 指定整条连线的长度（只读属性）。


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### 视图

-    **End Arrow**   * 如果此项为`True`，将在连线最后一点上显示一个符号，因此可将其用作一条注解线（annotation line）。

-    **Arrow Size**   * 指定连线末尾处所示符号的大小。

-    **Arrow Type**   * 指定连线末尾处所示的符号类型，可以为\"Dot（点）\", \"Circle（圈）\", \"Arrow（箭头）\", 或\"Tick\"。

-    **Pattern**   * 指定一种[图案来填写闭合连线所构成的面](Draft_Pattern.md)。只有在**Make Face**为`True`且**Display Mode**为\"Flat Lines\"时，此属性才会生效。

-    **Pattern Size**   * 指定[图案的大小](Draft_Pattern.md)。


</div>

## 脚本


<div class="mw-translate-fuzzy">


**参见   ***

[Draft API与](Draft_API.md)[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)。


</div>


<div class="mw-translate-fuzzy">

借助下列函数即可在[宏与](macros.md)[Python控制台中使用连线绘制工具](Python.md)：


</div>


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   利用指定的一个点列表`pointslist`来创建一个`Wire`对象。
    -   列表中的每个点都被定义为`FreeCAD.Vector`，单位为毫米。
    -   或者, 输入也可以是一个`Part.Wire`，从中提取各点。
-   如果`closed`为`True`，或者如果连线中的第一个点与最后一个点为同一点，则连线是闭合的。
-   如果指定了`placement`，则在此位置创建连线；否则在原点处创建连线。
-   如果`face`为`True`，且连线是闭合的，则连线将构成一个面，即表现为一个填充图形。


</div>

示例：


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/zh-cn
