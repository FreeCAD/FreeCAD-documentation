# Draft WireToBSpline/cs
---
- GuiCommand:/cs   Name:Draft WireToBSpline   Name/cs:Kreslení Drát do B-křivky   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> Drát do B-křivky---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj konvertuje [Dráty](Draft_Wire/cs.md) do [B-křivek](Draft_BSpline/cs.md) a naopak.


</div>

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;"> 
*Converting a Draft Wire to a Draft BSpline, and a closed Draft BSpline to a closed Draft Wire*


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte [drát](Draft_Wire/cs.md) nebo [B-křivku](Draft_BSpline/cs.md)
2.  Stiskněte tlačítko **<img src="images/Draft_WireToBSpline.png" width=16px> [Kreslení Drát do B-křivky](Draft_WireToBSpline/cs.md)
**


</div>

## Notes

-   The command may result in a closed, self-intersecting [Draft Wire](Draft_Wire.md) or [Draft BSpline](Draft_BSpline.md) with a face. Such an object will not display properly in the [3D view](3D_view.md). Its **Make Face** property, or its **Closed** property, must be set to `False`.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Není dostupné, ale vytvoření nového objektu z bodů jiného objektu je snadné, například:


</div>


<div class="mw-translate-fuzzy">

-   Je-li aktivní objekt drát:


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
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/cs
