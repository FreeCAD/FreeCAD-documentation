---
- GuiCommand:/de
   Name:Draft WireToBSpline
   Name/de:Entwurf DrahtZuBSpline
   MenuLocation:Änderung → Draht zu BSpline
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   SeeAlso:[Entwurf Draht](Draft_Wire/de.md), [Entwurf BSpline](Draft_BSpline/de.md)
---

# Draft WireToBSpline/de

## Beschreibung

Der <img alt="" src=images/Draft_WireToBSpline.svg  style="width:24px;"> **Entwurf DrahtZuBSpline** Befehl konvertiert [Entwurf Drähte](Draft_Wire/de.md) in [Entwurf BSplines](Draft_BSpline/de.md) und umgekehrt.

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;"> 
*Umwandlung eines Entwurf Drahtes in eine Entwurf BSpline und einer geschlossenen Entwurf BSpline in einen geschlossenen Entwurf Draht*

## Anwendung

1.  Wähle einen [Entwurf Draht](Draft_Wire/de.md) oder einen [Entwurf BSpline](Draft_BSpline/de.md).
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_WireToBSpline.svg" width=16px> [Entwurf DrahtZuBSpline](Draft_WireToBSpline/de.md)** Schaltfläche.
    -   Wähle den **Änderung → <img src="images/Draft_WireToBSpline.svg" width=16px> Draht zu Bspline** aus dem Menü.
3.  Ein neues Objekt wird erstellt.

## Hinweise

-   Der Befehl kann zu einem geschlossenen, sich selbst durchdringenden [Entwurf Draht](Draft_Wire/de.md) oder [Entwurf BSpline](Draft_BSpline/de.md) mit einer Fläche führen. Ein solches Objekt wird in der [3D Ansicht](3D_view/de.md) nicht korrekt dargestellt. Seine **Erstelle Fläche** Eigenschaft oder seine **Geschlossen** Eigenschaft muss auf `False` gesetzt werden.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um einen Draht in einen Bspline umzuwandeln oder umgekehrt, übergib die Eigenschaft `Points` des Quellobjekts an die Methode `[make_bspline](Draft_BSpline/de#Skripten.md)` bzw. die Methode `[make_wire](Draft_Wire/de#Skripten.md)` des Entwurf Moduls.

Beispiel:


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
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/de
