---
- GuiCommand:/ru
   Name/ru:Связать размер с 3D геометрией
   Name:TechDraw_LinkDimension
   MenuLocation:TechDraw → Размеры → Связать размер с 3D геометрией
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Вставить Вид](TechDraw_View/ru.md), [Вставить группу проекций](TechDraw_ProjectionGroup/ru.md)
---

# TechDraw LinkDimension/ru

The **TechDraw LinkDimension** tool is expected to be deprecated in the future. The [TechDraw DimensionRepair](TechDraw_DimensionRepair.md) tool can be used to change both 2D and 3D references.



## Описание

The **TechDraw LinkDimension** tool creates a link between 3D geometry and one or more existing projected Dimensions on a Page. This link allows the Dimension to use actual 3D values instead of 2D projected values.

The Link Dimension tool\'s most common use is in dimensioning isometric views in a ProjectionGroup. The projected length of an Edge in an isometric view will, of course, not necessarily equal the actual length of the Edge. In an orthogonal view the projected and actual lengths will be equal.

The link instructs the Dimension to compute it\'s value directly from the 3D geometry.



## Применение

1.  Create an appropriate dimension on the drawing page using any of [TechDraw LengthDimension](TechDraw_LengthDimension.md), [TechDraw HorizontalDimension](TechDraw_HorizontalDimension.md), etc. This dimension will be in the right place on the Page, but will show the projected dimension value.
2.  Select the geometry in the 3D view, for example, an edge, that corresponds to the projected geometry of your dimension.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link Dimension to 3D Geometry](TechDraw_LinkDimension.md)** button.
    -   Select the **TechDraw → Dimensions → <img src="images/TechDraw_LinkDimension.svg" width=16px> Link Dimension to 3D Geometry** option from the menu.
4.  A task panel opens.
5.  Select one or more Dimensions to be linked to the selected 3D geometry.
6.  Press **OK**.

The link operation changes the **MeasureType** property of the dimension from `Projected` to `True`.



## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that linking dimensions be one of the last steps in your drawing process.

The link tool will not stop you from making illogical links, so you need to choose the correct edge from the 3D view when creating the link.

There is currently no way to break a link; you can change the **MeasureType** back to `Projected` so that the dimension will use the projected value instead of the linked value.

Note that if the Dimension to be linked is based on two vertices, you should select two vertices in the 3D view. Similarly if the Dimension is based on an edge, you should select an edge in the 3D view.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The TechDraw LinkDimension tool is not directly usable in macros, but changing the **References 3D** property can accomplish the same result.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/ru
