---
 GuiCommand:
   Name: Sketcher BSplineDecreaseKnotMultiplicity
   Name/de: Sketcher BSplineKnotenVielfachheitVerringern
   MenuLocation: Skizze , B-Spline-Werkzeuge , Vielfachheit eines Spline-Knotens verringern
   Workbenches: Sketcher_Workbench/de
   Version: 0.17
   SeeAlso: Sketcher_BSplineIncreaseKnotMultiplicity/de
---

# Sketcher BSplineDecreaseKnotMultiplicity/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:24px;"> [Sketcher BSplineKnotenVielfachheitVerringern](Sketcher_BSplineDecreaseKnotMultiplicity/de.md) verringert die Vielfachheit eines [B-Spline](B-Splines/de.md)-Knotens.



## Anwendung

1.  Einen B-Spline-Knoten auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_BSplineDecreaseKnotMultiplicity.svg" width=16px>  [Vielfachheit eines B-Spline-Knotens verringern](Sketcher_BSplineDecreaseKnotMultiplicity/de.md)** drücken.
    -   Den Menüeintrag **Skizze → B-Spline-Werkzeuge → <img src="images/Sketcher_BSplineDecreaseKnotMultiplicity.svg" width=16px> Vielfachheit eines B-Spline-Knotens verringern** auswählen.



## Beispiel

Siehe [Sketcher BSplineKnotenVielfachheitErhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de#Beispiel.md)



## Hinweise

Wird die Vielfachheit eines Knotens auf null reduziert, wird der Knoten entfernt. Mathematisch betrachtet ist er null Mal im Knotenvektor vorhanden, d.h. es gibt keine Basisfunktion mehr. Um dies zu verstehen, braucht man etwas Mathematik; aber auch ein Blick auf die Vielfachheit verschafft Klarheit. Ein Knoten mit der Vielfachheit 0 heißt z.B., dass an der Position des Knotens zwei Teile einer Bézier-Kurve mit *C^3^*-Stetigkeit verbunden sind. So sollte die dritte Ableitung auf beiden Seiten des Knotens gleich sein. Für eine kubische Bézier-Kurve heißt das, dass beide Seiten ein Teil derselben Kurve sein müssen. Es gibt dann effektiv keinen Knoten mehr, der zwei Bézier-Kurven verbindet.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/de
