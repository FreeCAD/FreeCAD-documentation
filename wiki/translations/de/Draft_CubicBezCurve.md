---
- GuiCommand:
   Name:Draft CubicBezCurve
   Name/de:Entwurf KubischeBézKurve
   MenuLocation:Entwurf → Bézier Werkzeuge → Kubische Bézier Kurve
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Version:0.19
   SeeAlso:[Entwurf BézKurve](Draft_BezCurve/de.md), [Entwurf BSpline](Draft_BSpline/de.md), 
---

# Draft CubicBezCurve/de

## Beschreibung

Der <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> **Draft_CubicBezCurve/de\|Entwurf KubischeBézKurve**-Befehl erstellt eine [Bézierkurve](https://de.wikipedia.org/wiki/B%C3%A9zierkurve) dritten Grades (vier Punkte erforderlich).

Die Bézierkurve ist eine der am häufigsten verwendeten Kurven bei Computergrafiken. Dieser Befehl erlaubt dir eine kontinuierliche Spline aus mehreren Béziersegmenten 3. Grades zu erstellen, ähnlich dem Bézierwerkzeug in [Inkscape](https://inkscape.org/). Eine allgemeine Bézier Kurve beliebigen Grades kann mit dem [Entwurf BézKurve](Draft_BezCurve/de.md) Befehl erstellt werden.

Der [Entwurf BézKurve](Draft_BezCurve/de.md) und der [Entwurf KubischeBézKurve](Draft_CubicBezCurve/de.md) Befehl verwenden **Kontrollpunkte**, um die Position und Krümmung der Spline zu definieren. Der [Entwurf BSpline](Draft_BSpline/de.md) Befehl andererseits legt die **genauen Punkte**, durch die die Kurve verläuft fest.

<img alt="" src=images/Draft_CubicBezCurve_example.png  style="width:500px;"> 
*Spline, definiert durch drei kubische Béziersegmente. Das erste Segment wird durch vier Punkte definiert. Nachfolgende Segmente verwenden zwei Punkte aus dem vorherigen Segment wieder und benötigen daher nur zwei zusätzliche Punkte.*

## Anwendung

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

1.  Drücke die Taste **<img src="images/Draft_CubicBezCurve.svg" width=16px> [Entwurf KubischeBezKurve](Draft_CubicBezCurve/de.md)
**
2.  Klicke auf einen ersten Punkt in der 3D Ansicht und halte die Maustaste (1) gedrückt; dies ist der erste Endpunkt.
3.  Ziehe den Mauszeiger an einen anderen Punkt in der 3D Ansicht und lasse die Maustaste los (2); dies ist der erste Kontrollpunkt.
4.  Bewege den Zeiger auf einen anderen Punkt in der 3D Ansicht und klicke und halte die Maustaste auf diesen Punkt (3); dies ist der zweite Endpunkt.
5.  Bewege den Zeiger auf einen anderen Punkt in der 3D-Ansicht, um die endgültige Krümmung der Spline anzupassen, und lasse dann die Maustaste (4) los.
6.  In diesem Moment hast du bereits eine Bezier-Kurve von 3. Grad. Der Befehl kann durch Drücken von **Esc** oder der Taste **Close** abgeschlossen werden, oder Du kannst den Prozess des Klickens und Haltens (5) und des Ziehens und Loslassens (6) wiederholen, um weitere Bezier-Segmente dritten Grades hinzuzufügen.


</div>

## Optionen

Siehe [Entwurf BezKurve](Draft_BezCurve/de#Optionen.md).

## Hinweise

-   Eine Entwurf KubischeBezKurve kann mit dem Befehl [Entwurf Bearbeiten](Draft_Edit/de.md) bearbeitet werden.

## Einstellungen

Siehe [Entwurf BezKurve](Draft_BezCurve/de#Eigenschaften.md).

## Eigenschaften

Siehe [Entwurf BezKurve](Draft_BezCurve/de#Eigenschaften.md).

## Skripten


<div class="mw-translate-fuzzy">

Siehe auch: [Autogenerierte API Dokumentation](https://www.freecadweb.org/api) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>

Siehe [Entwurf BezKurve](Draft_BezCurve/de.md) für allgemeine Information. Ein kubischer Bézier wird durch Übergabe der Option Grad=3 an `makeBezCurve()` erzeugt.

Für jedes kubische Bézier-Segment müssen vier Punkte verwendet werden, von denen die beiden Extrempunkte angeben, wo der Spline durchläuft, und die beiden Zwischenpunkte Kontrollpunkte sind.

-   Wenn nur 3 Punkte gegeben sind, wird stattdessen ein quadratischer Bezier mit nur einem Kontrollpunkt erzeugt.
-   Wenn nur 2 Punkte gegeben sind, wird ein linearer Bézier, d. h. eine gerade Linie, erzeugt.
-   Wenn 5 Punkte gegeben sind, erzeugen die ersten 4 ein kubisches Bézier-Segment; der vierte und der fünfte Punkt werden verwendet, um eine gerade Linie zu erzeugen.
-   Wenn 6 Punkte gegeben sind, erzeugen die ersten 4 ein kubisches Bézier-Segment; der 4. und die beiden anderen Punkte werden verwendet, um ein quadratisches Bézier Segment zu erzeugen.
-   Wenn 7 Punkte gegeben sind, erzeugen die ersten 4 ein kubisches Bézier-Segment; der 4. und die anderen drei Punkte werden verwendet, um ein zweites kubisches Bézier Segment zu erzeugen.
-   Im Allgemeinen wird der letzte Punkt in einer Vierergruppe mit den folgenden drei Punkten maximal geteilt, um ein weiteres Bézier-Segment zu erzeugen.
-   Um glatte Kurven ohne gerade Segmente zu erhalten, sollte die Anzahl der Punkte `3n + 1` oder `3n` sein, wobei `n` die Anzahl der Segmente ist, für n >= 1.

<img alt="" src=images/Draft_CubicBezCurve_API_example.png  style="width:600px;">



*Beispiele für Bézierkurven, die unter Verwendung von 2, 3, 4, 5, 6, 7 und 8 Punkten erstellt wurden. Die durchgezogenen Linien stellen kubische Béziersegmente dar; die anderen Linien sind quadratisch oder linear.*

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(-3500, 0, 0)
p2 = App.Vector(-3000, 2000, 0)
p3 = App.Vector(-1100, 2000, 0)
p4 = App.Vector(0, 0, 0)

p5 = App.Vector(1500, -2000, 0)
p6 = App.Vector(3000, -1500, 0)
p7 = App.Vector(5000, 0, 0)
p8 = App.Vector(6000, 1500, 0)
rot = App.Rotation()

c1 = Draft.make_circle(100, placement=App.Placement(p1, rot), face=False)
c1.Label = "B1_E1"
c2 = Draft.make_circle(50, placement=App.Placement(p2, rot), face=True)
c2.Label = "B1_c1"
c3 = Draft.make_circle(50, placement=App.Placement(p3, rot), face=True)
c3.Label = "B1_c2"
c4 = Draft.make_circle(100, placement=App.Placement(p4, rot), face=False)
c4.Label = "B1_E2"
c5 = Draft.make_circle(50, placement=App.Placement(p5, rot), face=True)
c5.Label = "B2_c3"
c6 = Draft.make_circle(50, placement=App.Placement(p6, rot), face=True)
c6.Label = "B2_c4"
c7 = Draft.make_circle(100, placement=App.Placement(p7, rot), face=False)
c7.Label = "B2_E3"
c8 = Draft.make_circle(50, placement=App.Placement(p8, rot), face=True)
c8.Label = "B3_c5"

doc.recompute()

B1 = Draft.make_bezcurve([p1, p2], degree=3)
B1.Label = "B_lin"
B1.ViewObject.DrawStyle = "Dashed"

B2 = Draft.make_bezcurve([p1, p2, p3], degree=3)
B2.Label = "B_quad"
B2.ViewObject.DrawStyle = "Dotted"

B3 = Draft.make_bezcurve([p1, p2, p3, p4], degree=3)
B3.Label = "B_cub"
B3.ViewObject.LineWidth = 4

B4 = Draft.make_bezcurve([p1, p2, p3, p4, p5], degree=3)
B4.Label = "B_cub+lin"
B4.ViewObject.DrawStyle = "Dashed"

B5 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6], degree=3)
B5.Label = "B_cub+quad"
B5.ViewObject.DrawStyle = "Dotted"

B6 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7], degree=3)
B6.Label = "B_cub+cub"
B6.ViewObject.LineWidth = 2

B7 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7, p8], degree=3)
B7.Label = "B_cub+cub+lin"
B7.ViewObject.DrawStyle = "Dashed"

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CubicBezCurve/de
