# TechDraw RadiusDimension/ro
---
- GuiCommand:   Name:TechDraw  Dimension Radius   Workbenches:[[TechDraw_Workbench   TechDraw]]|MenuLocation:TechDraw → Dimension Radius   Shortcut:   SeeAlso:---


</div>

## Descriere

Instrumentul Radius Dimension adaugă o dimensiune a unei raze la o View. Cota/dimensiunea poate fi aplicată la orice margine în desenul care este un cerc sau un arc de cerc. <img alt="" src=images/RadiusSample.png  style="width:200px;">

The Radius Dimension tool adds a radius dimension to a View. The dimension may be applied to any Edge in the drawing which is a circle or circular arc. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Measuring a circle, indicating the radius*

## Cum se folosește 

1.  Select a circle or circular arc in the drawing. (Note some arcs which appear to be circular are actually ellipses or BSplines. You cannot make a radius dimension in these cases)
2.  Press the **<img src="images/TechDraw_RadiusDimension.svg" width=16px> [Radius Dimension](TechDraw_RadiusDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Proprietăți

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md).

## Script

Cotele tip rază pot fi adăugate la Pages utilizând Python.


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Radius Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/ro
