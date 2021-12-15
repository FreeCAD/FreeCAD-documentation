---
- GuiCommand:/it
   Name:Draft WireToBSpline
   Name/it:Polilinea in B-spline
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Polilinea in B-spline
   SeeAlso:[Polilinea](Draft_Wire/it.md), [B-spline](Draft_BSpline/it.md)
---

# Draft WireToBSpline/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento converte i segmenti di una linea spezzata, qui definita [Polilinea](Draft_Wire/it.md), in curve di tipo [B-spline](Draft_BSpline/it.md), e viceversa.


</div>

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Conversione di una polilinea in una B-Spline e di una B-spline chiusa in un contorno chiuso*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una linea [Polilinea](Draft_Wire/it.md) o una [BSpline](Draft_BSpline/it.md). Lo strumento è disabilitato se nessun oggetto è selezionato.
2.  Premere il pulsante **<img src="images/Draft_WireToBSpline.svg" width=16px> Polilinea in BSpline
**


</div>

## Notes

-   The command may result in a closed, self-intersecting [Draft Wire](Draft_Wire.md) or [Draft BSpline](Draft_BSpline.md) with a face. Such an object will not display properly in the [3D view](3D_view.md). Its **Make Face** property, or its **Closed** property, must be set to `False`.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Per lo strumento WireToBSpline non è disponibile un\'interfaccia di programmazione; tuttavia, creare un nuovo oggetto dai punti di un altro è semplice.


</div>

Esempio:


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
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/it
