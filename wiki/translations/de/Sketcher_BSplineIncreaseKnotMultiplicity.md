---
 GuiCommand:
   Name: Sketcher BSplineIncreaseKnotMultiplicity
   Name/de: Sketcher BSplineKnotenVielfachheitErhöhen
   MenuLocation: Skizze , B-Spline-Werkzeuge , Vielfachheit eines Knotens erhöhen
   Workbenches: Sketcher_Workbench/de
   Version: 0.17
   SeeAlso: Sketcher_BSplineDecreaseKnotMultiplicity/de
---

# Sketcher BSplineIncreaseKnotMultiplicity/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:24px;"> [Sketcher BSplineKnotenVielfachheitErhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md) erhöht die Vielfachheit eines [B-Spline](B-Splines/de.md)-Knotens.



## Anwendung

1.  Einen B-Spline-Knoten auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px">  [Vielfachheit eines Knotens erhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md)** drücken.
    -   Den Menüeintrag **Skizze → B-Spline-Werkzeuge → [<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Vielfachheit eines Knotens erhöhen** auswählen.



## Beispiel

B-Splines sind grundsätzlich eine Kombination von [Bézier-Kurven](B-Splines/de#B.C3.A9zierKurven.md) (schön erklärt in [diesem](https://www.youtube.com/watch?v=bE1MrrqBAl8) und [diesem](https://www.youtube.com/watch?v=xXJylM2S72s) (engl.) Video). Die Punkte an denen zwei Teile einer Bézier-Kurve verbunden sind, werden Knoten genannt. Ein Knoten mit der Vielfachheit *m* auf einem B-spline vom Grad *d* (degree) bedeutet, dass die Kurve links und der rechts des Knotens mindestens eine Ableitung \"n\"-ter Ordnung besitzt (*C^n^*-Stetigkeit genannt) wobei gilt *n = d - m*.

In diesem kubischen B-Spline (Grad 3) gibt es 3 Abschnitte, d.h. 3 Kurven sind an 2 Knoten verbunden. Die Knoten haben die Vielfachheit 1.

Die Vielfachheit wird durch die Zahlen in runden Klammern dargestellt. Siehe <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:16px;"> [Sketcher BSplineKnotenVielfachheit](Sketcher_BSplineKnotMultiplicity/de.md).

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*B-Spline dessen Knoten beide die Vielfachheit 1 besitzen.*

Eine Vielfachheit von 3 ändert diesen B-Spline so, dass sogar die ersten Ableitungen nicht gleich sind (*C*^0^-Stetigkeit). Hier ist derselbe B-Spline mit einer auf 3 erhöhten Vielfachheit des linken Knotens:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*Derselbe B-Spline mit einer Vielfachheit 3 der Knoten. Ein Kontrollpunkt wurde bewegt, um zu zeigen, dass der Knoten eine ''C<sup>0</sup>''-Stetigkeit besitzt.*

Eine Folge aus einer höheren Vielfachheit ist, dass auf Kosten verlorener Stetigkeit eine örtliche Einstellbarkeit erzielt wurde. Das bedeutet, dass die Änderung eines Kontrollpunktes den B-Spline nur örtlich beeinflusst.

Dies erkennt man in diesem Beispiel, in dem der B-Spline mit Vielfachheit 1 der Knoten aus dem ersten Beispiel genommen wurde und in dem der zweite Kontrollpunkt von rechts nach oben verschoben wurde. Als Ergebnis hat sich die komplette Form des B-Splines geändert:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality1.png  style="width:400px;">

Nach dem Erhöhen der Vielfachheit der Knoten auf 2 ergibt das Bewegen des zweiten Kontrollpunktes von rechts nur signifikante Änderungen auf der rechten Seite der Form:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality2.png  style="width:400px;">



## Hinweise

-   Die Vielfachheit der Knoten kann auch mit [Sketcher BSplineKnotenEinfügen](Sketcher_BSplineInsertKnot/de.md) erhöht werden.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/de
