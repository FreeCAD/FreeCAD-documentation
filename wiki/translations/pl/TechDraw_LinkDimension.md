---
- GuiCommand:
   Name:TechDraw LinkDimension
   MenuLocation:TechDraw → Dimensions → Link Dimension to 3D Geometry
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw View](TechDraw_View.md), [TechDraw ProjectionGroup](TechDraw_ProjectionGroup.md)
---

# TechDraw LinkDimension/pl

## Description

The Link Dimension tool creates a link between 3D geometry and one or more existing projected Dimensions on a Page. This link allows the Dimension to use actual 3D values instead of 2D projected values.

The Link Dimension tool\'s most common use is in dimensioning isometric views in a ProjectionGroup. The projected length of an Edge in an isometric view will, of course, not necessarily equal the actual length of the Edge. In an orthogonal view the projected and actual lengths will be equal.

The link instructs the Dimension to compute it\'s value directly from the 3D geometry.

## Usage

1.  Create an appropriate dimension on the drawing page using any of [TechDraw LengthDimensionh](TechDraw_LengthDimension.md), [TechDraw HorizontalDimension](TechDraw_HorizontalDimension.md), etc. This dimension will be in the right place on the Page, but will show the projected dimension value.
2.  Select the geometry in the 3D view, for example, an edge, that corresponds to the projected geometry of your dimension.
3.  Press the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link Dimension](TechDraw_LinkDimension.md)** button.
4.  A dialog will open. Select one or more Dimensions to be linked to the selected 3D geometry.
5.  Press **OK**.

After the link operation is completed the **MeasureType** property of the dimension changes from `Projected` to `True`.

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that linking dimensions be one of the last steps in your drawing process.

The link tool will not stop you from making illogical links, so you need to choose the correct edge from the 3D view when creating the link.

There is currently no way to break a link; you can change the **MeasureType** back to `Projected` so that the dimension will use the projected value instead of the linked value.

Note that if the Dimension to be linked is based on two vertices, you should select two vertices in the 3D view. Similarly if the Dimension is based on an edge, you should select an edge in the 3D view.

## Properties

1.  The MeasureType property of a linked Dimension will be changed from \"Projected\" to \"True\".

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Link Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
to be defined
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/pl
