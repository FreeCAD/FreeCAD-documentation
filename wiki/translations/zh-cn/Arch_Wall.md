---
- GuiCommand:/zh-cn
   Name:Arch Wall
   Name/zh-cn:建筑墙体
   MenuLocation:Arch → Wall
   Workbenches:[Arch](Arch_Workbench.md)
   Shortcut:**W** **A**
   SeeAlso:[Arch Structure](Arch_Structure.md)
---

# Arch Wall/zh-cn


</div>



## 描述


<div class="mw-translate-fuzzy">

利用此工具可从头或基于其他[几何图形（shape）或](Part_Workbench.md)[网格（mesh）对象来构建墙体](Mesh_Workbench.md)。构建墙体并非一定要基于其他对象，仅需长、宽、高三种属性来描述其长方体外观即可。在利用存在的几何图形构建墙体时，可以以下列对象为基础：


</div>

-   **线性2D对象**，例如线段、连线、弧线或草图，在利用这些对象绘制墙体时，您可以改变墙体的厚度，对齐方式(右对齐、左对齐或居中对齐)及其高度。唯独长度属性不可更改。
-   **平面**，在利用此对象绘制墙体时，您只能改变高度属性。而无法更改长度与宽度属性。如果所基于的平面是一个顶点，however, the wall will use the width property instead of height, allowing you to build walls from space-like objects or mass studies.
-   **实体**，在利用此对象绘制墙体时，长、宽、高三种属性皆不可改变。墙体简单地用此实体作为其外观形状。
-   **网格**，在利用此对象绘制墙体时，所基于的网格必须为一个闭合、manifold的实体。

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*基于线段、连线、平面、实体与草图来构建墙体*


<div class="mw-translate-fuzzy">

我们也可以对的墙体执行添加或移除操作。在执行添加操作时，将令其他对象的形状与墙体相融；移除则是从墙体中去除目标对象。利用[Arch Add与](Arch_Add.md)[Arch Remove工具即可实现墙体的增减操作](Arch_Remove.md)。Additions and subtractions have no influence over wall parameters such as height and width, which can still be changed. Walls can also have their height automatic, if they are included into a higher-level object such as [floors](Arch_Floor.md). The height must be kept at 0, then the wall will adopt the height specified in the parent object.


</div>

当若干墙体相交的时候，您需要将它们置于同一[楼层（floor）上](Arch_Floor.md)，再实现它们在几何方面上的相交。




<div class="mw-translate-fuzzy">

## 如何使用


</div>



### 从头绘制墙体


<div class="mw-translate-fuzzy">

1.  按下**<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall/zh-cn.md)**按钮，或先后依次按下**W**与 **A**键
2.  在3D视图中点选第一个点，或输入一个 坐标
3.  在3D视图中点选第二个点，或输入一个 坐标


</div>



### 在所选对象的基础之上绘制墙体


<div class="mw-translate-fuzzy">

1.  选择一个或多个基础几何对象(底图对象、草图等等)
2.  按下**<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall/zh-cn.md)**按钮，或先后依次按下**W**与**A**键
3.  调整需要修改的属性，如高度或宽度。


</div>



## 选项

-   Walls share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The height, width and alignment of a wall can be set during drawing, via the task panel
-   When snapping a wall to an existing wall, both walls will be joined into one. The way the two walls are joined depends on their properties: If they have the same width, height and alignment, and if the option \"join base sketches\" is enabled in the Arch preferences, the resulting wall will be one object based on a sketch made of several segments. Otherwise, the latter wall will be added to the first one as addition.
-   Press **X**, **Y** or **Z** after the first point to constrain the second point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **Enter** between each X, Y and Z component.
-   Press **R** or click the checkbox to check/uncheck the **Relative** button. If relative mode is on, the coordinates of the second point are relative to the first one. If not, they are absolute, taken from the (0,0,0) origin point.
-   Press **Shift** while drawing to [constrain](Draft_Constrain.md) your second point horizontally or vertically in relation to the first one.
-   Press **Esc** or the **Cancel** button to abort the current command.
-   Double-clicking on the wall in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions
-   Multi-layer walls can be easily created by building several walls from the same baseline. By setting their Align property to either left or right, and specifying an Offset value, you can effectively construct several wall layers. Placing a window in such a wall layer will propagate the opening to the other wall layers based on the same baseline.
-   Walls can also make use of [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the wall will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Wall\'s Width value, after subtracting the other layers.
-   Walls can be made to display blocks, instead of one single solid, by turning their **Make Blocks** property on. The size and offset of blocks can be configured with different properties, and the amount of blocks is automatically calculated.

## Snapping

Snapping works a bit differently with Arch walls than other Arch and Draft objects. If a wall has a baseline object, snapping will anchor to the base object, instead of the wall geometry, allowing to easily align walls by their baseline. If, however, you specifically want to snap to the wall geometry, pressing **Ctrl** will switch snapping to the wall object.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Second wall snapping perpendicularly to the first one*



## 属性

Wall objects inherit the properties of [Part](Part_Workbench.md) objects, and also have the following extra properties:

### Data


{{TitleProperty|Blocks}}

-    **Block Height**: The height of each block

-    **Block Length**: The length of each block

-    **Count Broken**: The number of broken blocks (read-only)

-    **Count Entire**: The number of entire blocks (read-only)

-    **Joint**: The size of the joints between each block

-    **Make Blocks**: Enable this to make the wall generate blocks

-    **Offset First**: The horizontal offset of the first line of blocks

-    **Offset Second**: The horizontal offset of the second line of blocks


{{TitleProperty|Component}}

-    **Base**: The base object this wall is built on


{{TitleProperty|Wall}}

-    **Align**: The alignment of the wall on its baseline: Left, Right or Center

-    **Area**:

-    **Face**: The index of the face from the base object to use. If the value is not set or 0, the whole object is used

-    **Height**: The height of the wall (not used when the wall is based on a solid). If no height is given, and the wall is inside a [floor](Arch_Floor.md) object with its height defined, the wall will automatically take the value of the floor height.

-    **Length**: The length of the wall (not used when the wall is based on an object)

-    **Normal**: An extrusion direction for the wall. If set to (0,0,0), the extrusion direction is automatic.

-    **Offset**: This specifies the distance between the wall and its baseline. Works only if the Align property is set to Right or Left.

-    **Override Align**:

-    **Override Width**:

-    **Width**: The width of the wall (not used when the wall is based on a face)

## Scripting


<div class="mw-translate-fuzzy">

## 脚本


**参见:**

[Arch API](Arch_API.md) 与 [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


</div>


<div class="mw-translate-fuzzy">

借助下列函数即可在[宏与](macros.md)[Python控制台中使用墙体工具](Python.md)：


</div>


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Creates a `Wall` object from the given `baseobj`, which can be a [Draft object](Draft_Workbench.md), a [Sketch](Sketcher_Workbench.md), a face, or a solid.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width` (thickness), and `height`.
    -   If given, `face` can be used to give the index of a face from the underlying object, to build this wall on, instead of using the whole object.

-    `align`can be `"Center"`, `"Left"` or `"Right"`.

-   It returns `None` if the operation fails.

示例:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Wall/zh-cn
