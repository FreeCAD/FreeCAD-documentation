---
- GuiCommand:
   Name:TechDraw Dimension Landmark
   MenuLocation:TechDraw → Dimension Landmark
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Dimension Horizontal](TechDraw_Dimension_Horizontal.md), [TechDraw Dimension Vertical](TechDraw_Dimension_Vertical.md)
---

## Description

The Dimension Landmark tool adds a linear dimension to a View. The dimension is based on two Point **feature** (Draft.Point or Part.Vertex) from the 3D model. Note that the points must be **feature** objects that appear in the model [tree view](Tree_view.md). Random vertexes from a shape will not work.

The purpose of this tool is to provide a workaround to the corruption of dimension caused by \"[topological naming](topological_naming_problem.md)\" issues. The source points should use [Expressions](Expressions.md) or other containing mechanism to establish their position. Since the points are [Document Objects](App_DocumentObject.md), and not shape components, their name does not change with recomputes, and hence they are easily found.

See the Limitation and WorkAround sections of [TechDraw Dimension Length](TechDraw_Dimension_Length.md) for more on dimensions and topological naming.

The Landmark Dimension generally behaves like any other Dimension

## Usage

1.  Select 2 Point objects in the [tree view](Tree_view.md) or the [3D view](3D_view.md).
2.  Select also the View to which the dimension is to be added.
3.  Press the **<img src="images/Techdraw-landmarkdistance.svg" width=20px> [Dimension Landmark](TechDraw_Dimension_Landmark.md)
** button or **TechDraw → Dimension Landmark**
4.  A dimension will be added to the View. The dimension text may be dragged to the desired position.

## Limitations

The Landmark Dimension tool is initially limited to \"Distance\" dimensions. Other types may be added if demand warrants.

## Properties

Landmark Dimension does not introduce any new properties.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Landmark tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::LandmarkDimension','Landmark')
dim1.Type = "Distance"
dim1.References2D=[(TDView, 'Vertex1')]
dim1.References3D=[(Point3d1, 'Vertex1')]
dim1.References3D=[(Point3d2, 'Vertex1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
