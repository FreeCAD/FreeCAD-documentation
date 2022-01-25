# TechDraw DiameterDimension/ro
---
- GuiCommand:   Name:TechDraw  Dimension Diameter   Workbenches:[[TechDraw_Workbench   TechDraw]]|MenuLocation:TechDraw → Dimension Diameter   Shortcut:   SeeAlso:---


</div>

## Descriere

Instrumentul pentru cote tip diametrue adaugă o cotă diametru unei imagini. Cota poate fi aplicată la orice cerc din desen. Distanța va fi inițial distanța proiectată(adică așa cum este reprezentată în desen), dar această distanță poate fi înlocuită prin distanța 3D reală utilizând instrumentul Link Dimension <img alt="" src=images/LinkDimension.png  style="width:24px;">. <img alt="" src=images/DiameterSample.png  style="width:200px;">

The Diameter Dimension tool adds a diameter dimension to a View. The dimension may be applied to any circular in the drawing. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Diameter_example.png  style="width:130px;"> 
*Measuring a circle, indicating the diameter*

## Cum se folosește 

1.  Selectați un cerc sau un arc de cerc în desen. (Notați că anumite arce de cerc apar ca fiind circulare dar de fapt sunt elipse sau curbe BSplines. Nu puteți realiza diametru dimension în aceste cazuri)
2.  Apăsați butonul **<img src="images/TechDraw_DiameterDimension.svg" width=24px> [Dimension Diameter](TechDraw_DiameterDimension.md)
**
3.  O cotă/distanță va fi adăugată în View. Cota poate fi glisată până în poziția dorită.




1.  Select a circular edge in the drawing. (Note some arcs which appear to be circular are actually ellipses or BSplines. You cannot make a diameter dimension in these cases)
2.  Press the **<img src="images/TechDraw_DiameterDimension.svg" width=16px> [Diameter Dimension](TechDraw_DiameterDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Proprietăți

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md).

## Script

Cotele tip diametru pot fi adăugate la Pages utilizând Python.


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Diameter Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Diameter"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DiameterDimension/ro
