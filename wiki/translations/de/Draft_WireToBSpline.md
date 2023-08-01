---
- GuiCommand:
   Name:Draft WireToBSpline
   Name/de:Draft DrahtZuBSpline
   MenuLocation:Änderung - Kantenzug zu BSpline
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft Draht](Draft_Wire/de.md), [Draft BSpline](Draft_BSpline/de.md)
---

# Draft WireToBSpline/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_WireToBSpline.svg  style="width:24px;"> **Draft DrahtZuBSpline** wandelt [Draft Kantenzüge](Draft_Wire/de.md) in [Draft B-Splines](Draft_BSpline/de.md) und umgekehrt.

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;"> 
*Umwandlung eines Draft-Kantenzuges in einen Draft-B-Spline und eines geschlossenen Draft-B-Splines in einen geschlossenen Draft-Kantenzug*



## Anwendung

1.  Einen [Draft Kantenzug](Draft_Wire/de.md) oder einen [Draft B-Spline](Draft_BSpline/de.md) auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_WireToBSpline.svg" width=16px> [Kantenzug zu B-Spline](Draft_WireToBSpline/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_WireToBSpline.svg" width=16px> Kantenzug zu B-Spline** auswählen.
3.  Ein neues Objekt wird erstellt.



## Hinweise

-   Der Befehl kann zu einem geschlossenen, sich selbst durchdringenden [Draft Kantenzug](Draft_Wire/de.md) oder [Draft B-Spline](Draft_BSpline/de.md) mit einer Fläche führen. Ein solches Objekt wird in der [3D-Ansicht](3D_view/de.md) nicht korrekt dargestellt. Seine {{PropertyData/de|Make Face}} oder seine {{PropertyData/de|Closed}} muss auf `False` gesetzt werden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um einen Draht in einen B-Spline umzuwandeln oder umgekehrt, wird die Eigenschaft `Points` des Quellobjekts an die Methode `[make_bspline](Draft_BSpline/de#Skripten.md)` bzw. die Methode `[make_wire](Draft_Wire/de#Skripten.md)` des Draft-Moduls übergeben.

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
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/de
