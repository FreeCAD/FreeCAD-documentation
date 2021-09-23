# TechDraw AngleDimension/ro
---
- GuiCommand:   Name:TechDraw  Dimension Angle   Workbenches:[[TechDraw_Workbench   TechDraw]]|MenuLocation:TechDraw → Dimension Angle   Shortcut:   SeeAlso:---


</div>

## Descriere

Instrumentul pentru cote unghiulare adaugă o cotă unghiulară unei imagini. Cota poate fi unghi interior, și între oricare două segment ede line draptă care formează muchii. Unghiul va fi inițial unghiul proiectat(adică așa cum este reprezentată în desen), dar aceast unghi poate fi înlocuit prin unghiul 3D real utilizând instrumentul Link Dimension <img alt="" src=images/LinkDimension.png  style="width:24px;">. <img alt="" src=images/AngleSample.png  style="width:200px;">

The Angle Dimension tool adds a angular dimension to a View. The dimension may be the interior angle between any two straight line edges. The angle will initially be the projected angle (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Measuring the angle between two straight lines*

## Cum se folosește 

1.  Selectați punctele sau muchiile care definesc măsurarea dvs.
2.  Apăsați butonul **<img src="images/Dimension_Angle.png" width=24px> [Dimension Angle](TechDraw_Dimension_Angle.md)
**
3.  O cotă va fi adăugată la View. Cota poate fi glisată în poziția dorită.




1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Angle Dimension](TechDraw_AngleDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Proprietăți

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length/ro.md) tool. See that tool for details.

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md).

## Script

Cotele tip unghi pot fi adăugate la Pages utilizând Python.


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Angle Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/ro
