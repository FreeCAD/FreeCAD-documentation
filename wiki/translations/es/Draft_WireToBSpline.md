---
- GuiCommand:
   Name: Draft_WireToBSpline
   Name/es: Draft_WireToBSpline
   MenuLocation: Boceto -> Contorno a BSpline
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
---

# Draft WireToBSpline/es

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta convierte [Contornos](Draft_Wire/es.md) en [BSplines](Draft_BSpline/es.md), y viceversa.


</div>

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;"> 
*Converting a Draft Wire to a Draft BSpline, and a closed Draft BSpline to a closed Draft Wire*


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Selecciona un [contorno](Draft_Wire/es.md) o una [BSpline](Draft_BSpline/es.md)
2.  Presiona el botón **<img src="images/Draft_WireToBSpline.png" width=16px> [Contorno a BSpline](Draft_WireToBSpline/es.md)
**


</div>

## Notes

-   The command may result in a closed, self-intersecting [Draft Wire](Draft_Wire.md) or [Draft BSpline](Draft_BSpline.md) with a face. Such an object will not display properly in the [3D view](3D_view.md). Its **Make Face** property, or its **Closed** property, must be set to `False`.

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

No disponible, pero crear un nuevo objeto con los puntos de otro es sencillo, por ejemplo:


</div>


<div class="mw-translate-fuzzy">

-   if the active object is a wire


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(1000, 1000, 0)
p2 = App.Vector(2000, 1000, 0)
p3 = App.Vector(2500, -1000, 0)
p4 = App.Vector(3500, -500, 0)

base_wire = Draft.make_wire([p1, p2, p3, p4])
base_spline = Draft.make_bspline([-p1, -1.3*p2, -1.2*p3, -2.1*p4])

points1 = base_wire.Points
spline_from_wire = Draft.make_bspline(points1)

points2 = base_spline.Points
wire_from_spline = Draft.make_wire(points2)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/es
