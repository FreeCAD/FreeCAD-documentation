---
- GuiCommand:
   Name:TechDraw CosmeticVertex
   MenuLocation:TechDraw → Add Vertices → Add Cosmetic Vertex 
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Midpoint](TechDraw_Midpoints.md), [TechDraw Quadrant](TechDraw_Quadrants.md)
---

## Description

The Cosmetic Vertex tool adds a [Vertex](Glossary#V.md), which is not part of the source geometry, to a View. This Vertex behaves like any other vertex and can be used for dimensioning.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Cosmetic Vertex used to create an otherwise impossible Dimension*

## Usage

1.  Select a view in the drawing.
2.  Press the **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> Add Cosmetic Vertex** button
3.  A task dialog will open. It allows to set location of the Cosmetic Vertex either by picking a point or by entering an x,y-offset from the center of the selected view.
4.  To pick a position, press the button **Point Picker**. Click to a position in the view and subsequently press **OK** to create the point. To exit the point picking without creating a Cosmetic Vertex, press the **Escape picking** button in the dialog.

To delete a Cosmetic Vertex, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

**Note:** You cannot change the location of the Cosmetic Vertex after it has been created. At the moment there is no other way than to delete it and creating a new one.

## Properties

Cosmetic Vertices have no properties of their own, as they are no document objects. They share color and size settings with regular geometry vertices.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Cosmetic Vertices are available to [macros](Macros.md) or the [Python](Python.md) console.


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```





{{TechDraw Tools navi

}}  
