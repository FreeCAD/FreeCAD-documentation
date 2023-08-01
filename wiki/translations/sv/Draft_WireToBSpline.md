# Draft WireToBSpline/sv
---
- GuiCommand:   Name: Draft WireToBSpline   Name/sv: Draft WireToBSpline   Workbenches: [Arch](Draft_Workbench/sv___Draft]],_[[Arch_Workbench/sv.md)|MenuLocation: Drafting -> Wire to BSpline---


</div>

## Beskrivning

The <img alt="" src=images/Draft_WireToBSpline.svg  style="width:24px;"> **Draft WireToBSpline** command converts [Draft Wires](Draft_Wire.md) to [Draft BSplines](Draft_BSpline.md) and vice versa.

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;"> 
*Converting a Draft Wire to a Draft BSpline, and a closed Draft BSpline to a closed Draft Wire*


<div class="mw-translate-fuzzy">

## Bruk


</div>

1.  Select a [Draft Wire](Draft_Wire.md) or a [Draft BSpline](Draft_BSpline.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_WireToBSpline.svg" width=16px> [Draft WireToBSpline](Draft_WireToBSpline.md)** button.
    -   Select the **Modification → <img src="images/Draft_WireToBSpline.svg" width=16px> Wire to B-spline** option from the menu.
3.  A new object is created.

## Notes

-   The command may result in a closed, self-intersecting [Draft Wire](Draft_Wire.md) or [Draft BSpline](Draft_BSpline.md) with a face. Such an object will not display properly in the [3D view](3D_view.md). Its **Make Face** property, or its **Closed** property, must be set to `False`.

## Scripting


<div class="mw-translate-fuzzy">

## Skript


</div>

To convert a wire to a bspline, or vice versa, pass the `Points` property of the source object to the `[make_bspline](Draft_BSpline#Scripting.md)` method, or respectively the `[make_wire](Draft_Wire#Scripting.md)` method, of the Draft module.

Example:


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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/sv
