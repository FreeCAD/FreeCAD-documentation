---
 GuiCommand:
   Name: Draft CubicBezCurve
   Name/de: Draft KubischeBézierkurve
   MenuLocation: Zeichnen , Bézierwerkzeuge , Kubische Bézierkurve<br>2D-Entwurf , Kubische Bézierkurve
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.19
   SeeAlso: Draft_BezCurve/de, Draft_BSpline/de, 
---

# Draft CubicBezCurve/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> **Draft KubischeBézierkurve** erstellt eine [Bézierkurve](https://de.wikipedia.org/wiki/B%C3%A9zierkurve) dritten Grades (vier Punkte erforderlich).

Die Bézierkurve ist eine der am häufigsten verwendeten Kurven für Computergrafiken. Dieser Befehl erlaubt es, einen zusammenhängenden Spline aus mehreren Bézier-Abschnitten 3. Grades zu erstellen, ähnlich dem Bézierwerkzeug in [Inkscape](https://inkscape.org/). Eine allgemeine Bézierkurve beliebigen Grades kann mit dem Befehl [Draft Bézierkurve](Draft_BezCurve/de.md) erstellt werden.

Die Befehle [Draft Bézierkurve](Draft_BezCurve/de.md) und [Draft KubischeBézierkurve](Draft_CubicBezCurve/de.md) verwenden **Kontrollpunkte**, um die Position und Krümmung der Splines festzulegen. Der Befehl [Draft BSpline](Draft_BSpline/de.md) legt andererseits die **genauen Punkte**, durch die die Kurve verläuft fest.

<img alt="" src=images/Draft_CubicBezCurve_example.png  style="width:500px;"> 
*Spline, definiert durch drei kubische Bézier-Abschnitte. Der erste Abschnitt wird durch vier Punkte definiert. Nachfolgende Abschnitte verwenden zwei Punkte aus dem vorherigen Abschnitt wieder und benötigen daher nur zwei weitere Punkte.*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_CubicBezCurve.svg" width=16px> [Kubische Bézierkurve](Draft_CubicBezCurve/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → Bézierwerkzeuge → <img src="images/Draft_CubicBezCurve.svg" width=16px> Kubische Bézierkurve** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_CubicBezCurve.svg" width=16px> Kubische Bézierkurve** auswählen.

2.  Der Aufgaben-Bereich **Kubische Bézierkurve** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.

3.  Es ist nicht möglich die Punkte im Aufgaben-Bereich einzugeben.

4.  Für die folgenden Varianten der [ Mausnavigation](Mouse_navigation/de.md) muss eine Taste auf der Tastatur gedrückt gehalten werden:
    -   Wird [OpenInventor-Navigation](Mouse_navigation/de#OpenInventor_Navigation.md) verwendet, muss die **Strg**-Taste (Ctrl) während der Ausführung des Befehls durchgängig gedrückt gehalten werden.
    -   Wird [Gesten-Navigation](Mouse_navigation/de#Gesture_Navigation.md) verwendet, muss die **Alt**-Taste für jede Abfolge von klicken, halten, loslassen gedrückt gehalten werden, es ist aber auch möglich diese Taste während der Ausführung des Befehls durchgängig gedrückt zu halten.

5.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen und die Maustaste gedrückt halten (1). Dies ist der erste Endpunkt.

6.  Den Mauszeiger auf einen anderen Punkt in der [3D-Ansicht](3D_view.md) ziehen und die Maustaste loslasen (2). Dies ist der erste Kontrollpunkt.

7.  Den Mauszeiger auf einen weiteren Punkt in der [3D-Ansicht](3D_view.md) bewegen, diesen Punkt auswählen und die Maustaste gedrückt halten (3). Dies ist der zweite Endpunkt.

8.  Den Mauszeiger auf einen weiteren Punkt in der [3D-Ansicht](3D_view.md) ziehen, um die endgültige Krümmung des Abschnitts anzupassen und die Maustaste loslasen (4). Dies ist der zweite Kontrollpunkt.

9.  Eine Bézierkurve 3. Grades wurde hinzugefügt.

10. Wahlweise kann der Ablauf von klicken und halten (5) sowie ziehen und loslassen (6) wiederholt werden, um weitere Abschnitte hinzuzufügen.

11. Jeder Folgeabschnitt verwendet entsprechend den zweiten Endpunkt und den Zweiten Kontrollpunkt des vorherigen Abschnitts als seinen ersten Endpunkt und ersten Kontrollpunktach.

12. 
    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl zu beenden.



## Optionen

Siehe [Draft Bézierkurve](Draft_BezCurve/de#Optionen.md).



## Hinweise

-   Eine kubische Draft-Bézierkurve (CubicBezCurve-Objekt) kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.



## Eigenschaften

Siehe [Draft Bézierkurve](Draft_BezCurve/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Siehe [Draft Bézierkurve](Draft_BezCurve/de.md) für allgemeine Informationen. Eine kubische Bézierkurve wird durch Übergabe der Option Grad=3 an `makeBezCurve()` erzeugt.

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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CubicBezCurve/de
