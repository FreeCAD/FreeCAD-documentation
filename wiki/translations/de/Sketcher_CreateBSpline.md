---
 GuiCommand:
   Name: Sketcher CreateBSpline
   Name/de: Sketcher B-SplineErstellen
   MenuLocation: Sketch , Skizzengeometrien , B-Spline erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **B** **B**
   Version: 0.17
   SeeAlso: Sketcher_CreatePeriodicBSpline/de
---

# Sketcher CreateBSpline/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:24px;"> [Sketcher B-SplineErstellen](Sketcher_CreateBSpline/de.md) erstellt eine offene [B-Spline](B-Splines.md)-Kurve durch Kontrollpunkte. {{Version/de|1.0}}: Oder wahlweise durch Knotenpunkte.

![](images/Sketcher_CreateBSpline_Example.png ) 
*Eine B-Spline-Kurve (weiß), festgelegt durch 4 Kontrollpunkte.<br>
Das Kontrollpolygon (grün) verbindet die Kontrollpunkte (markiert mit dunkelgelben Gewichtskreisen).<br>
Die Zahl 3 (grün, ohne Klammern) in der Mitte repräsentiert den [Grad](Sketcher_BSplineIncreaseDegree/de#Beschreibung.md) des B-Splines.<br>
Die Zahlen (1) und (4) (grün, in runden Klammern) repräsentieren die [Vielachheit](Sketcher_BSplineDecreaseKnotMultiplicity/de#Beschreibung.md) der Knotenpunkte.<br>
Die Zahlen [1.00] (grün, in eckigen Klammern) repräsentieren die Gewichte der Kontrollpunkte.*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateBSpline.svg" width=16px> [B-Spline durch Kontrollpunkte](Sketcher_CreateBSpline/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateBSpline.svg" width=16px> B-Spline erstellen** auswählen.
    -   Ein Rechtsklick in der [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreateBSpline.svg" width=16px> B-Spline erstellen** im Kontextmenü auswählen. {{Version/de|1.0}}
    -   Das Tastaturkürzel **G** dann **B** dann **B**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  DerAbschnitt **B-Spline-Parameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
4.  Wahlweise die **M**-Taste drücken oder eine der Möglichkeiten im Auswahlfeld Modus des Abschnitts Parameter auswählen, um den Werkzeugmodus zu ändern:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> **Durch Kontrollpunkte**:
        1.  Wahlweise den **Grad** anpassen (kann auch nach dem Auswählen der Punkte erfolgen):
            -   Eine Zahl größer als null eingeben.
            -   Die **U**-Taste drücken, um den Grad zu erhöhen.
            -   Die **J**-Taste drücken, um den Grad zu verringern.
    -   <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:16px;"> **Durch Knoten**: {{Version/de|1.0}}
        1.  B-Splines durch Knoten werden immer mit Grad 3 erstellt, aber der Grad kann nachträglich angepasst werden. Siehe [Hinweise](#Hinweise.md).
5.  Wahlweise die **R**-Taste drücken oder die CheckBox **Periodisch** aktivieren, um einen geschlosenen B-Spline zu erstellen (kann auch nach dem Auswählen der Punkte erfolgen). {{Version/de|1.0}}
6.  Mehrere Punkte auswählen.
7.  Wahlweise vor dem Beenden die **F**-Taste drücken, um den letzten Punkt zu löschen.
8.  Die rechte Maustaste oder **Esc** drücken, um die Eingabe abzuschließen.
9.  Der B-Spline wird erstellt, einschließlich der zugehörigen internen Geometrie (Gewichtskreise und Knotenpunkte).
10. Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) läuft:
    1.  Wahlweise weitere B-Splines erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Elemente der internen Geometry können gelöscht werden. Sie können jederzeit neu erstellt werden mit [Sketcher InterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry/de.md).
-   Nachdem ein B-Spline erstellt wurde, ist es möglich, die Gewichte der Kontrollpunkte festzulegen, indem die Radien der Gewichtskreise geändert werden. Die Gleichheitsbedingungen der Kreise müssen zuerst gelöscht werden. Die Randbedingung Radius ist frei wählbar, das Gewicht der Kontrollpunkte wird durch die relativen Radien der Kreise definiert. Es funktioniert ähnlich wie die Schwerkraft: Je größer ein Kreis im Verhältnis zu den anderen ist, desto stärker wird die Kurve von diesem Kontrollpunkt angezogen.
-   Der Grad eines erstellten B-Splines kann [erhöht](Sketcher_BSplineIncreaseDegree/de.md) oder [verringert](Sketcher_BSplineDecreaseDegree/de.md) werden und auch die Vielfachheit seiner Knoten kann [erhöht](Sketcher_BSplineIncreaseKnotMultiplicity/de.md) oder [verringert](Sketcher_BSplineIncreaseKnotMultiplicity/de.md) werden.
-   Die Sichtbarkeit des [Grades](Sketcher_BSplineDegree/de.md), des [Kontrollpolygons](Sketcher_BSplinePolygon/de.md), des [Krümmungskamms](Sketcher_BSplineComb/de.md), der [Knotenvielfachheit](Sketcher_BSplineKnotMultiplicity/de.md) und des [Kontrollpunktgewichts](Sketcher_BSplinePoleWeight/de.md) können in der Symbolleiste [Sketcher visuell](Sketcher_Workbench/de#Sketcher_visuell.md) ein- bzw. ausgeschaltet werden.



## Einschränkungen

-   Einige Arten von Randbedingungen werden derzeit nicht unterstützt.
-   Die festgelegte Vielfachheit der Knoten wird eventuell nicht immer berücksichtigt:
    -   Für einen geschlossenen Spline hat der erste Knoten (deckungsgleich mit dem letzten) immer eine Vielfachheit von 2.
    -   Für einen offenen Spline haben der erste und der letzte Knoten immer eine Vilefachheit von 4.
    -   Besitzen die Punkte unmittelber davor und danach eine Vielfachheit \>= 3, ist das Stück zwischen den beiden vollständig stetig, und dieser (Mittel-) Punkt wird nur mit einer Randbedingung Punkt auf Objekt festgelegt. Wird ein Knoten benötigt, sollte das Werkzeug [BSplineKnotenEinfügen](Sketcher_BSplineInsertKnot/de.md) in Erwägung gezogen werden.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/de
