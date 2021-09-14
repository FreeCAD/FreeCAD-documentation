---
- GuiCommand:/ru
   Name:TechDraw  Dimension Link
   Name/ru:TechDraw  Dimension Link
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   MenuLocation:TechDraw → Dimension Link
   SeeAlso:
---


</div>

## Описание

The Dimension Link tool creates a link between 3D geometry and 1 or more existing projected Dimensions on a Page. This link allows the Dimension to use actual 3D values instead of 2D projected values.

The Dimension Link tool\'s most common use is in dimensioning isometric views in a ProjectionGroup. The projected length of an Edge in an isometric view will, of course, not necessarily equal the actual length of the Edge. In an orthogonal view the projected and actual lengths will be equal.

The Dimension Link instructs the Dimension to compute it\'s value directly from the 3D geometry.

## Применение

1.  Create an appropriate dimension on the drawing page using any of [Dimension Length](TechDraw_Dimension_Length.md), [Dimension Horizontal](TechDraw_Dimension_Horizontal.md), etc. This dimension will be in the right place on the Page, but will show the projected dimension value.
2.  Select the geometry in the 3D view, for example, an edge, that corresponds to the projected geometry of your dimension.
3.  Press the **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Dimension Link](TechDraw_Dimension_Link.md)** button.
4.  A dialog will open. Select one or more Dimensions to be linked to the selected 3D geometry.
5.  Press **OK**.

After the link operation is completed the **MeasureType** property of the dimension changes from `Projected` to `True`.

## Ограничения

Dimension objects are vulnerable to \"topological naming\" issues. See the information in the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool for more information. It is recommended that linking dimensions be one of the last steps in your drawing process.

The link tool will not stop you from making illogical links, so you need to choose the correct edge from the 3D view when creating the link.

There is currently no way to break a link; you can change the **MeasureType** back to `Projected` so that the dimension will use the projected value instead of the linked value.

Note that if the Dimension to be linked is based on two vertices, you should select two vertices in the 3D view. Similarly if the Dimension is based on an edge, you should select an edge in the 3D view.

## Свойства

1.  The MeasureType property of a linked Dimension will be changed from \"Projected\" to \"True\".

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Dimension Link tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
to be defined
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
