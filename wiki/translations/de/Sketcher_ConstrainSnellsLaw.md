---
- GuiCommand:/de
   Name:Sketcher ConstrainSnellsLaw
   Name/de:Skizzierer BeschränkeSnelliusschesGesetz
   MenuLocation:Sketch → Skizzen-Beschränkungen → Lichtbrechung (nach Snellius-Gesetz) festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **W**
   Version:0.15
---

# Sketcher ConstrainSnellsLaw/de

## Beschreibung

Beschränkt zwei Linien, um dem Gesetz der Lichtbrechung zu folgen, wenn es durch eine Grenzfläche dringt, in der sich zwei Materialien mit unterschiedlichen Brechungsindizes treffen. Siehe [1](https://de.wikipedia.org/wiki/Snelliussches_Brechungsgesetz) auf Wikipedia für weitere Informationen.

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;">



*Snelliussches Gesetz*

## Anwendung

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt. n1, n2 sind nur Bezeichnungen, die zeigen, wo sich die Brechungsindizes befinden.*

-   Du brauchst zwei Linien, die einem Lichtstrahl folgen sollen, und eine Kurve, die als Schnittfläche dient. Die Linien sollten sich auf verschiedenen Seiten der Schnittfläche befinden.
-   Wähle den Endpunkt einer Linie, einen Endpunkt einer anderen Linie und die Schnittflächenkante. Die Schnittfläche kann eine [Linie](Sketcher_CreateLine/de.md), ein [Bogen](Sketcher_CompCreateArc/de.md), ein [Kreis](Sketcher_CompCreateCircle/de.md) oder ein [Kegel](Sketcher_CompCreateConic/de.md).

sein. Beachte die Reihenfolge, in der du die Endpunkte ausgewählt hast.

-   Rufe die Zwangsbeschränkung auf. Es erscheint ein Dialog, in dem nach einem Verhältnis der Brechungsindizes n2/n1 gefragt wird. n2 entspricht dem Medium, in dem sich die Linie des zweiten ausgewählten Endpunkts befindet, n1 ist für die erste Linie.
-   Die Endpunkte werden zur Deckung gebracht (falls erforderlich), auf die Schnittstelle beschränkt (falls erforderlich) und das Snelliussche Gesetz wird beschränkt.

Beachte, dass mehrere [Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) automatisch (Punkt-auf-Objekt, deckungsgleich) hinzugefügt werden. Sie können gelöscht werden, wenn sie eine Redundanz verursachen oder manuell hinzugefügt werden, wenn sie nicht automatisch hinzugefügt wurden. Für die tatsächliche Beschränkung des Snelliusschen Brechungsgesetzes müssen die Endpunkte der Linien deckungsgleich sein und auf der Schnittfläche liegen, sonst ist das Verhalten undefiniert.

Durch Verwenden der **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Polylinie](Sketcher_CreatePolyline/de.md)** ist es möglich, die Zeichnung von Lichtstrahlen zu beschleunigen. In diesem Fall kann man zwei deckungsgleiche Endpunkte durch Kastenauswahl auswählen.

## Anmerkungen

-   Die eigentliche Beschränkung nach Snelliussches Brechungsgesetz erzwingt die einfachgesetzliche Gleichung n1\*sin(theta1) = n2\*sin(theta2). Es ist notwendig, dass die Linienenden durch andere Zwangsbeschränkungen zufällig und auf der Schnittfläche gemacht werden. Die notwendigen Hilfsbeschränkungen werden automatisch auf der Grundlage der aktuellen Koordinaten der Elemente hinzugefügt.
-   Die Pythonroutine fügt die Hilfsbeschränkungen nicht hinzu. Diese müssen vom Skript manuell hinzugefügt werden (siehe Beispiel im Abschnitt Skripten).
-   Diese Hilfsbeschränkungen können vorübergehend gelöscht und die Endpunkte auseinandergezogen werden, was nützlich sein kann, wenn man einen reflektierten Strahl oder Doppelbrechungsstrahl konstruieren möchte.
-   Im Gegensatz zur Realität sind Brechungsindizes mit Lichtstrahlen verknüpft, aber nicht entsprechend der Grenzseiten. Dies ist nützlich, um die Doppelbrechung zu emulieren, Pfade verschiedener Wellenlängen aufgrund der Brechung zu konstruieren und den Winkel des Auftretens der Totalreflexion leicht zu konstruieren.
-   Beide Strahlen können sich auf der gleichen Seite der Grenzfläche befinden und erfüllen damit die Randbedingung. Dies ist physikalischer Unfug, es sei denn, das Verhältnis n2/n1 ist 1,0, in diesem Fall emuliert die Einschränkung eine Reflexion.
-   Kreis- und Ellipsenbögen werden auch als Strahlen (physikalischer Unfug) akzeptiert.

## Skripten

Die Beschränkungen können aus [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole durch folgende Funktion verwendet werden:


```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```

wobei:

:\* {{Incode|Sketch}} ist ein Skizzenobjekt

:\* {{Incode|line1}} und {{Incode|pointpos1}} sind zwei ganze Zahlen, die den Endpunkt der Linie im Medium mit dem Brechungsindex von *n1* identifizieren. {{Incode|line1}} ist der Index der Linie in der Skizze (der Wert, der von Sketch.addGeometry zurückgegeben wird), und {{Incode|pointpos1}} sollte 1 für Startpunkt und 2 für Endpunkt sein.

:\* {{Incode|line2}} und {{Incode|pointpos2}} sind die Indizes, die den Endpunkt der zweiten Zeile angeben (in Medium *n2*)

:\* `interface` ist der Index, der die Linie angibt, die auf die Position des Interface zwischen Medium *n1* und Medium *n2* hinweist

:\* {{Incode|n2byn1}} ist eine Gleitkommazahl, die dem Verhältnis der Brechungsindizes *n2*/*n1* entspricht

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `iline1`, `iline2`, `pointpos2` und `interface` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.

Beispiel:


```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2
MiddlePoint = 3

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





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/de
