---
- GuiCommand:   Name:TechDraw  Dimension Radius   Workbenches:[[TechDraw_Workbench   TechDraw]]|MenuLocation:TechDraw → Dimension Radius   Shortcut:   SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Radius Dimension adaugă o dimensiune a unei raze la o View. Cota/dimensiunea poate fi aplicată la orice margine în desenul care este un cerc sau un arc de cerc. <img alt="" src=images/RadiusSample.png  style="width:200px;">


</div>

The Dimension Radius tool adds a radius dimension to a View. The dimension may be applied to any Edge in the drawing which is a circle or circular arc. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Link Dimension](TechDraw_Dimension_Link.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Measuring a circle, indicating the radius*


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}

1.  Selectați un cerc sau un arc circular în desen. (Notați că anumite arce de cerc apar ca fiind circulare dar de fapt sunt elipse sau curbe BSplines. Nu puteți realiza radius dimension în aceste cazuri)
2.  Apăsați butonul **<img src="images/Dimension_Radius.png" width=24px> [Dimension Radius](TechDraw_Dimension_Radius.md)
**
3.  O cotă/distanță va fi adăugată în View. Cota poate fi glisată până în poziția dorită.


</div>

1.  Select a circle or circular arc in the drawing. (Note some arcs which appear to be circular are actually ellipses or BSplines. You cannot make a radius dimension in these cases)
2.  Press the **<img src="images/TechDraw_Dimension_Radius.svg" width=16px> [Dimension Radius](TechDraw_Dimension_Radius.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_Dimension_Length#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to \"topological naming\" issues. See the information in the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool for more information.


<div class="mw-translate-fuzzy">

## Proprietăți

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length/ro.md) tool. See that tool for details.


</div>

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool. See that tool for details.


<div class="mw-translate-fuzzy">

## Script

Cotele tip rază pot fi adăugate la Pages utilizând Python.


</div>


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Radius tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
