---
- GuiCommand   */es
   Name   *TechDraw Dimension Radius
   Name/es   *TechDraw Dimensión Radio
   MenuLocation   *TechDraw → Dimensión Radio
   Workbenches   *[TechDraw](TechDraw_Workbench/es.md)
   SeeAlso   *[TechDraw Dimensión Diámetro](TechDraw_DiameterDimension/es.md)
---

# TechDraw RadiusDimension/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Dimensión Radio añade una dimensión de radio a una Vista. La dimensión puede aplicarse a cualquier Borde del dibujo que sea un círculo o un arco circular. La distancia será inicialmente la distancia proyectada (es decir, como se muestra en el dibujo), pero puede cambiarse a la distancia real en 3D usando el **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Enlace Dimensión](TechDraw_LinkDimension/es.md)** herramienta.


</div>

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width   *130px;"> 
*Measuring a circle, indicating the radius*

## Utilización

1.  Select a circle or circular arc in the drawing. (Note some arcs which appear to be circular are actually ellipses or BSplines. You cannot make a radius dimension in these cases)
2.  Press the **<img src="images/TechDraw_RadiusDimension.svg" width=16px> [Radius Dimension](TechDraw_RadiusDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitaciones

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Propiedades

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md).

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Radius Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/es
