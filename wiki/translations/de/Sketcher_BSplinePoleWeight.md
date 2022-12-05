---
- GuiCommand:/de
   Name:Sketcher BSplinePoleWeight
   Name/de:Sketcher BSplinePolGewicht
   MenuLocation:Sketch → B-Spline-Werkzeuge → Gewicht der B-Spline-Kontrollpunkte anzeigen / ausblenden
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Version:0.19
   SeeAlso:[AuswahlB-SplineErstellen](Sketcher_CompCreateBSpline/de.md)
---

# Sketcher BSplinePoleWeight/de

## Beschreibung

Blendet die Darstellung der Kontrollpunkt**gewichte** für die Kontrollpunkte einer B-Spline-Kurve ein oder aus (siehe [unten](#Erklärung_Gewichte.md) für eine Erklärung der Gewichte).

<img alt="" src=images/sketcher_BSplineWeightShow.png  style="width:468px;"> 
*B-Spline mit Kontrollpunktgewichten in eckigen Klammern*

## Anwendung

1.  Eine B-Spline-Kurve auswählen.
2.  Die Schaltfläche **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Gewicht der B-Spline-Kontrollpunkte anzeigen / ausblenden](Sketcher_BSplinePoleWeight/de.md)** drücken.

## Gewicht, kurz erklärt 

B-Splines sind im Grunde eine Kombination aus [Bézierkurven](B-Splines/de#B.C3.A9zierkurven.md) (sehr schön erklärt in [diesem](https://www.youtube.com/watch?v=bE1MrrqBAl8) und [diesem](https://www.youtube.com/watch?v=xXJylM2S72s) Video).

Die Bézierkurve wird mit dieser Formel berechnet:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{Polynomausdruck}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{Polynomausdruck}}\; \underbrace{P_{i}}_{\text{Punktkoordinate}}$

Dabei ist *n* der Grad der Kurve. Eine Bézierkurve vom Grad *n* ist also ein Polygon der Ordnung *n*. Die Faktoren $P_{i}$ sind dabei die Koordinaten der Kontrollpunkte der Bézierkurven. Zur Veranschaulichung siehe [diese Seite](https://pomax.github.io/bezierinfo/#control).

Der Begriff Gewicht ist in FreeCAD etwas irreführend, da in der entsprechenden Literatur die Faktoren $P_{i}$ oft auch Gewichte genannt werden. FreeCADs Gewichte sind etwas anderes. Die Idee dieser Gewichte ist, die Spline-Kurve zu verändern, durch unterschiedlich \"gewichtete\" Kontrollpunkte. Die Idee ist, dass ein Punkt mit dem Gewicht 2 doppelt so viel Einfluss hat, wie ein Punkt mit dem Gewicht 1. Dies wird erreicht, durch Anwendung dieser abgewandelten Formel zur Berechnung der Spline-Kurve:

$\quad
\mathrm{Rational\ Bezier}(n,t)=\cfrac{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}P_{i}}{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}\;\;\;\,}$

wobei $w_{i}$ das Gewicht für den Punkt $P_{i}$ ist.

Dies ist eine neue Klasse von Bézierkurven, da trotz der wie gewünscht gewichteten Punkte die Kurve nicht mehr polynom ist, sondern gebrochen polynom ist. Daher werden diese Kurven rationale Bézier-Kurven genannt und die B-Splines heißen dann rationale B-Splines.

Die Konsequenz ist, dass man eine größere Flexibilität bei der Festlegung der Spline-Form erhält. Sind alle Gewichte gleich, ändert sich die Form des Splines nicht. Das Verhältnis der Gewichte zueinander ist wichtig, nicht nur der Wert alleine. Dieser Spline zum Beispiel hat exakt dieselbe Form, wie der auf dem ersten Bild:

<img alt="" src=images/sketcher_BSplineWeightDouble.png  style="width:468px;"> 
*Derselbe B-Spline wie im ersten Bild aber mit anderen absoluten Werten des Gewichts*

Ein Gewicht von Null wäre eine Definitionslücke der Gleichung zur Berechnung rationaler Bézier-Kurven, daher stellt FreeCAD sicher, dass es nicht Null werden kann. Dennoch haben kleine Werte denselben Effekt, als wären die Kontrollpunkte nicht vorhanden:

<img alt="" src=images/sketcher_BSplineWeightZero.png  style="width:468px;"> 
*Derselbe B-Spline mit einem Kontrollpunkt, dessen Gewicht fast Null ist*

## Gewichte Ändern 

Wie Gewichte geändert werden, ist auf [dieser Wiki-Seite](B-Splines/de#Ändern_des_Gewichts.md) beschrieben.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplinePoleWeight/de
