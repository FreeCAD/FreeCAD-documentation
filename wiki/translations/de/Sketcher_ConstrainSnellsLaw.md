---
 GuiCommand:
   Name: Sketcher ConstrainSnellsLaw
   Name/de: Sketcher ConstrainSnellsLaw
   MenuLocation: Sketch , Skizzen-Beschränkungen , Lichtbrechung  festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **W**
   Version: 0.15
---

# Sketcher ConstrainSnellsLaw/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Sketcher ConstrainSnellsLaw](Sketcher_ConstrainSnellsLaw/de.md) Legt zwei Linien so fest, dass sie der Lichtbrechung entsprechen, die beim Passieren einer Grenzfläche auftritt, an der zwei Werkstoffe mit unterschiedlichen Brechungsindizes aufeinander treffen. Siehe [Snelliussches_Brechungsgesetz](https://de.wikipedia.org/wiki/Snelliussches_Brechungsgesetz).

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;"> 
*Snelliussches Gesetz*



## Anwendung

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt. n1, n2 zeigen, wo sich die Brechungsindizes befinden.*

1.  Zwei Linien, die einen Lichtstrahl darstellen, und eine Kante, die eine Grenzschicht darstellt, vorbereiten. Die Linien sollten sich auf unterschiedlichen Seiten der Grenzschichtkante befinden, die eine [Linie](Sketcher_CreateLine/de.md), ein [Kreisbogen](Sketcher_CreateArc/de.md), ein [Kreis](Sketcher_CreateCircle/de.md) oder ein [Kegelschnitt](Sketcher_CompCreateConic/de.md) sein kann.
2.  Einen Endpunkt der ersten Linie, einen Endpunkt der zweiten Linie und die Grenzschichtkante auswählen. Bei der Auswahl ist die Reihenfolge zu beachten.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainSnellsLaw.svg" width=16px> Lichtbrechung (nach Snellius-Gesetz) festlegen** auswählen.
    -   Das Tastaturkürzel **K** dann **W**.




1.  Der Dialog **Brechungsindex-Verhältnis** wird geöffnet.
2.  einen Wert für **Verhältnis n2/n1** eingeben, wobei **n2** für das Medium gilt, in dem sich die zweite ausgewählte Linie befindet, und **n1** für das Medium der ersten Linie gilt.
3.  Eine Randbedingung Lichtbrechung (nach Snellius-Gesetz) festlegen wird hinzugefügt. Wenn nötig, werden die Endpunkte mit den Randbedingungen [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) und [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) mit der Grenzschichtkante verbunden. Diese zusätzlichen Randbedingungen werden [Helferrandbedingungen](Sketcher_helper_constraint/de.md) genannt.



## Hinweise

-   Die eigentliche Randbedingung nach Snellius-Gesetz verwendet die einfache Gleichung n1 \* sin(theta1) = n2 \* sin(theta2). Es erfordert, dass die Linienenden durch andere Randbedingungen deckungsgleich (koinzident) und auf der Grenzlinie liegend festgelegt werden, andernfalls ist ihr Verhalten nicht definiert. Die notwendigen Helferrandbedingungen werden automatisch auf Grundlage der aktuellen Koordinaten der Elemente hinzugefügt.
-   In Python müssen die Helferrandbedingungen manuell hinzugefügt werden (siehe [Skripten](#Skripten.md)).
-   Diese Helferrandbedingungen können vorübergehend gelöscht und die Endpunkte auseinandergezogen werden, was nützlich sein kann, wenn man einen reflektierten Strahl oder einen Doppelbrechungsstrahl konstruieren möchte.
-   Im Gegensatz zur Realität sind Brechungsindizes mit Lichtstrahlen verknüpft, aber nicht den Seiten der Grenze entsprechend. Dies ist nützlich, um die Doppelbrechung zu emulieren, Pfade verschiedener Wellenlängen aufgrund der Brechung zu konstruieren und den Winkel des Auftretens der Totalreflexion leicht zu konstruieren.
-   Beide Strahlen können sich auf der gleichen Seite der Grenzfläche befinden und gleichzeitig die Gleichung der Randbedingung erfüllen. Dies ist physikalischer Unfug, es sei denn, das Verhältnis n2 / n1 ist 1,0; in diesem Fall emuliert die Randbedingung eine Reflexion.
-   Kreis- und Ellipsenbögen werden auch als Strahlen akzeptiert. Aber auch dies ist physikalischer Unfug.



## Skripten

Die Randbedingungen können in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit dem folgenden Befehl erstellt werden:


```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```

wobei

  - {{Incode|Sketch}} ein Skizzenobjekt ist.

  - {{Incode|line1}} und {{Incode|pointpos1}} zwei ganze Zahlen sind, die den Endpunkt der Linie im Medium mit dem Brechungsindex von *n1* identifizieren. {{Incode|line1}} ist der Index der Linie in der Skizze (der Rückgabewert von Sketch.addGeometry), und {{Incode|pointpos1}} sollte 1 für den Startpunkt und 2 für den Endpunkt sein.

  - {{Incode|line2}} und {{Incode|pointpos2}} die Indizes sind, die den Endpunkt der zweiten Linie angeben (in Medium *n2*)

  - `interface` der Index der Linie ist, die die Position der Grenzfläche zwischen Medium *n1* und Medium *n2* darstellt.

  - {{Incode|n2byn1}} eine Gleitkommazahl ist, die dem Verhältnis der Brechungsindizes *n2*/*n1* entspricht.

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `line1`, `pointpos1`, `line2`, `pointpos2` und `interface` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.

Beispiel:


```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2

f = App.activeDocument().addObject("Sketcher::SketchObject","Sketch")

# add geometry to the sketch
icir = f.addGeometry(Part.Circle(App.Vector(-547.612366,227.479736,0),App.Vector(0,0,1),68.161979))
iline1 = f.addGeometry(Part.LineSegment(App.Vector(-667.331726,244.127090,0),App.Vector(-604.284241,269.275238,0)))
iline2 = f.addGeometry(Part.LineSegment(App.Vector(-604.284241,269.275238,0),App.Vector(-490.940491,256.878265,0)))
# add constraints
# helper constraints:
f.addConstraint(Sketcher.Constraint('Coincident',iline1,EndPoint,iline2,StartPoint)) 
f.addConstraint(Sketcher.Constraint('PointOnObject',iline1,EndPoint,icir)) 
# the Snell's law:
f.addConstraint(Sketcher.Constraint('SnellsLaw',iline1,EndPoint,iline2,StartPoint,icir,1.47))

App.ActiveDocument.recompute() 
```



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/de
