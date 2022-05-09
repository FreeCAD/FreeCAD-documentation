# Arch Wall/ru
---
- GuiCommand   */ru
   Name   *Arch_Wall
   Name/ru   *Стена
   Workbenches   *[Arch](Arch_Workbench/ru.md)
   MenuLocation   *Архитектура → Стена
   Shortcut   ***W** **A**
   SeeAlso   *[Структура](Arch_Structure/ru.md)---

## Описание


<div class="mw-translate-fuzzy">

Этот инструмент создает объект Wall с нуля или поверх любого другого объекта [ shape](Part_Workbench.md) или [ mesh](Mesh_Workbench.md). Стена может быть построена без какого-либо базового объекта, и в этом случае она ведет себя как кубический том, используя свойства длины, ширины и высоты. При построении поверх существующей формы стена может основываться на   *


</div>

-   A **linear 2D object**, such as lines, wires, arcs or sketches, in which case you can change thickness, alignment (right, left or centered) and height. The length property has no effect.
-   A **flat face**, in which case you can only change the height. Length and width properties have no effect. If the base face is vertical, however, the wall will use the width property instead of height, allowing you to build walls from space-like objects or mass studies.
-   A **solid**, in which case length, width and height properties have no effect. The wall simply uses the underlying solid as its shape.
-   A **mesh**, in which case the underlying mesh must be a closed, manifold solid.

<img alt="" src=images/Arch_Wall_example.jpg  style="width   *780px;"> 
*Walls built from a line, a wire, a face, a solid, and a sketch*

Walls can also have additions or subtractions. Additions are other objects whose shapes are joined in this Wall\'s shape, while subtractions are subtracted. Additions and subtractions can be added with the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools. Additions and subtractions have no influence over wall parameters such as height and width, which can still be changed. Walls can also have their height automatic, if they are included into a higher-level object such as [floors](Arch_Floor.md). The height must be kept at 0, then the wall will adopt the height specified in the parent object.

When several walls should intersect, you need to place them into a [floor](Arch_Floor.md) to have their geometry intersected.

## Применение

### Рисование стены с нуля 

1.  Нажмите кнопку **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall/ru.md)**, или нажмите **W**, затем **A**.
2.  Щелкните первую точку на трехмерном изображении или введите первую координату.
3.  Нажмите вторую точку на трехмерном представлении или введите вторую координату.

### Drawing a wall on top of a selected object 

1.  Select one or more base geometry objects (Draft object, sketch, etc)
2.  Press the **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall.md)** button, or press the **W** then **A** keys
3.  Adjust needed properties such as height or width.

## Опции

-   Walls share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The height, width and alignment of a wall can be set during drawing, via the task panel
-   When snapping a wall to an existing wall, both walls will be joined into one. The way the two walls are joined depends on their properties   * If they have the same width, height and alignment, and if the option \"join base sketches\" is enabled in the Arch preferences, the resulting wall will be one object based on a sketch made of several segments. Otherwise, the latter wall will be added to the first one as addition.
-   Press **X**, **Y** or **Z** after the first point to constrain the second point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **Enter** between each X, Y and Z component.
-   Press **R** or click the checkbox to check/uncheck the **Relative** button. If relative mode is on, the coordinates of the second point are relative to the first one. If not, they are absolute, taken from the (0,0,0) origin point.
-   Press **Shift** while drawing to [constrain](Draft_Constrain.md) your second point horizontally or vertically in relation to the first one.
-   Press **Esc** or the **Cancel** button to abort the current command.
-   Double-clicking on the wall in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions
-   Multi-layer walls can be easily created by building several walls from the same baseline. By setting their Align property to either left or right, and specifying an Offset value, you can effectively construct several wall layers. Placing a window in such a wall layer will propagate the opening to the other wall layers based on the same baseline.
-   Walls can also make use of [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the wall will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Wall\'s Width value, after subtracting the other layers.
-   Walls can be made to display blocks, instead of one single solid, by turning their **Make Blocks** property on. The size and offset of blocks can be configured with different properties, and the amount of blocks is automatically calculated. <small>(v0.18)</small> 

## Привязки

Привязка к стенам Arch работает немного иначе, чем с другими объектами Arch и Draft. Если стена имеет базовый объект, привязка будет привязана к базовому объекту, а не к геометрии стены, что позволит легко выровнять стены по их базовой линии. Однако, если вы специально хотите привязаться к геометрии стены, нажатие **Ctrl** переключит привязку на объект стены.

<img alt="" src=images/Arch_wall_snap.jpg  style="width   *780px;"> 
*Second wall snapping perpendicularly to the first one*

## Свойства

Wall objects inherit the properties of [Part](Part_Workbench.md) objects, and also have the following extra properties   *

-    **Align**   * The alignment of the wall on its baseline   * Left, Right or Center

-    **Base**   * The base object this wall is built on

-    **Face**   * The index of the face from the base object to use. If the value is not set or 0, the whole object is used

-    **Force Wire**   * If True, and the wall is based on a face, only the border wire of the face is used, resulting in a wall bordering the face

-    **Length**   * The length of the wall (not used when the wall is based on an object)

-    **Width**   * The width of the wall (not used when the wall is based on a face)

-    **Height**   * The height of the wall (not used when the wall is based on a solid). If no height is given, and the wall is inside a [floor](Arch_Floor.md) object with its height defined, the wall will automatically take the value of the floor height.

-    **Normal**   * An extrusion direction for the wall. If set to (0,0,0), the extrusion direction is automatic.

-    **Offset**   * This specifies the distance between the wall and its baseline. Works only if the Align property is set to Right or Left.


{{Version/ru|0.18}}

-    **Make Blocks**   * Enable this to make the wall generate blocks

-    **Block Length**   * The length of each block

-    **Block Height**   * The height of each block

-    **Offset First**   * The horizontal offset of the first line of blocks

-    **Offset Second**   * The horizontal offset of the second line of blocks

-    **Joint**   * The size of the joints between each block

-    **Count Entire**   * The number of entire blocks (read-only)

-    **Count Broken**   * The number of broken blocks (read-only)

## Scripting


<div class="mw-translate-fuzzy">

## Программирование


**См. так же   ***

[Arch API](Arch_API/ru.md) и [Основы написания скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Инструмент «Стена» может использоваться в [макросах](Macros/ru.md) и на консоли [Python](Python.md) с помощью следующей функции   *


</div>


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Creates a `Wall` object from the given `baseobj`, which can be a [Draft object](Draft_Workbench.md), a [Sketch](Sketcher_Workbench.md), a face, or a solid.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width` (thickness), and `height`.
    -   If given, `face` can be used to give the index of a face from the underlying object, to build this wall on, instead of using the whole object.

-    `align`can be `"Center"`, `"Left"` or `"Right"`.

-   It returns `None` if the operation fails.

Пример   *


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Wall/ru
