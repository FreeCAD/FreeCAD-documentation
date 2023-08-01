---
- GuiCommand:
   Name:Draft Edit
   Name/de:Draft Bearbeiten
   MenuLocation:Modification → Bearbeiten
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**D** **E**
   SeeAlso:[Std Bearbeiten](Std_Edit/de.md)
---

# Draft Edit/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Edit.svg  style="width:16px;"> **Bearbeiten** versetzt ausgewählte Objekte in den Draft-Modus Bearbeiten. In diesem Modus können die Eigenschaften von Objekten grafisch bearbeitet werden. Typischerweise können Knoten verschoben werden und in einigen Fällen können Optionen im Kontextmenü ausgewählt werden. Der Befehl kann die meisten Draft-Objekte, aber auch einige andere Objekte bearbeiten. Siehe [Unterstützte Objekte](#Unterstützte_Objekte.md). Unterstützte Draft-Objekte können auch mit dem Befehl [Std Berabeiten](Std_Edit/de.md) in den Draft-Modus Bearbeiten versetzt werden.

![](images/Draft_Edit_example.png ) 
*4 Objekte im Draft-Modus Bearbeiten: ein Draft-Draht (rot), ein Draft-Bogen (schwarz), ein Draft-BSpline (grün) und ein Draft-BezKurve (magenta)*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen. Es ist zu beachte, dass sich zwar mehrere Objekte im Draft-Modus Bearbeiten befinden können, aber immer nur ein Objekt zu Zeit bearbeitet werden kann.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wenn noch kein Objekt ausgewählt wurde: Ein Doppelklick auf ein Objekt in der [Baumansicht](Tree_view/de.md). Dies funktioniert nur bei unterstützten Draft-Objekten.
    -   Die Schaltfläche **<img src="images/Draft_Edit.svg" width=16px> [Bearbeiten](Draft_Edit/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Edit.svg" width=16px> Bearbeiten** auswählen.
    -   Das Tastaturkürzel: **D** und dann **E**.
    -   Für ein einzelnes Objekt: Den Eintrag **Edit** im MKontextmenü der [Baumansicht](Tree_view/de.md) auswählen. Dies funktioniert nur mit unterstützten Draft-Objekten. {{Version/de|0.21}}
3.  Wenn noch kein Objekt ausgewählt wurde: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Die ausgewählten Objekte werden mit temporären Knoten markiert, und der [Haupt-Aufgabenbereich](#Haupt_Aufgabenfeld.md) wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Wahlweise das Kontextmenü eines Knotens oder einer Kante verwenden. Diese Kontextmenüs sind nur für einige Draft-Objekte verfügbar. Weitere Informationen finden sich unter [Unterstützte Objekte](#Unterstützte_Objekte.md).
    -   Einen der folgenden Schritte ausführen:
        -   Auf allen Betriebssystemen: **E** gedrückt halten und auf den Knoten oder die Kante klicken. Um **E** zu verwenden, muss man eventuell einmal in die [3D-Ansicht](3D_view/de.md) klicken, um sicherzustellen, dass diese den Fokus hat.
        -   Unter Windows: **Alt** gedrückt halten und auf den Knoten oder die Kante klicken.
        -   Unter Linux: **Shift**+**Alt**, **Strg**+**Alt** oder **Alt** gedrückt halten und auf den Knoten oder die Kante klicken.
        -   Unter macOS: **Option** gedrückt halten und auf den Knoten oder die Kante klicken.
    -   Einen Eintrag im Kontextmenü auswählen.
    -   Wenn die ausgewählte Option eine Punkteingabe erfordert:
        -   Der [Aufgabenbereich Knoten bearbeiten](#Knoten_Aufgabenpaneel.md) wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
        -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) anwählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
6.  Wahlweise einen Knoten verschieben:
    -   Den Knoten in der [3D-Ansicht](3D_view/de.md) anklicken.

    -   Der [Aufgabenbereich Knoten bearbeiten](#Knoten_Aufgabenpaneel.md) wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.

    -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) anwählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

    -   Das Ergebnis hängt vom Objekt und dem ausgewählten Knoten ab.

    -   
        **Esc**
        
        oder die Schaltfläche **Schließen** drücken, um den Befehl zu beenden.



## Optionen

Die hier genannten Tastaturkürzel für einzelne Zeichen können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md).



### Haupt-Aufgabenbereich 

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl zu beenden.



### Aufgabenbereich Knoten bearbeiten 

-   Um die Koordinaten manuell einzugeben, werden die X-, Y- und Z-Komponente eingegeben und jedesmal mit **Enter** bestätigt. Oder die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken, wenn die gewünschten Werte angezeigt werden. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-   Um Polarkoordinaten zu verwenden, werden die Werte für **Länge** und **Winkel** eingegeben und jeweils mit **Enter** bestätigt.

-   Das Kontrollkästchen **Winkel** aktivieren, um den Zeiger auf den angegebenen Winkel festzulegen.

-    **G**drücken oder auf das Kontrollkästchen **Global** klicken, um den globalen Modus zu aktivieren. Wenn der globale Modus eingeschaltet ist, sind die Koordinaten relativ zum globalen Koordinatensystem, andernfalls sind sie relativ zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **S**drücken, um [Draft Fangen](Draft_Snap/de.md) ein- oder auszuschalten.



## Unterstützte Objekte 



### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Draft Linie](Draft_Line/de.md) und <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Draht](Draft_Wire/de.md) 

-   Wenn der Anfangs- oder Endknoten eines offenen Drahtes so verschoben wird, dass sie zusammenfallen, wird der Draht geschlossen.
-   Kontextmenü des Knotens: {{Value|Punkt löschen}}. Es müssen mindestens zwei Punkte verbleiben.
-   Kontextmenü der Kante: {{Value|Punkt hinzufügen}}, {{Value|Draht schließen/öffnen}} ({{Version/de|0.21}}) und {{Value|Draht umkehren}} ({{Version/de|0.20}}).



### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Draft Bogen](Draft_Arc/de.md) und <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Draft BogenDurch3Punkte](Draft_Arc_3Points/de.md) 

-   Kontextmenü des Mittelpunkts: {{Value|Bogen verschieben}}.
-   Kontextmenü des Anfangsknotens: {{Value|Startwinkel setzen}}.
-   Kontextmenü des Endknotens: {{Value|Endwinkel setzen}}.
-   Kontextmenü des mittleren Knotens: {{Value|Radius setzen}}.
-   Kontextmenü der Kante: {{Value|Bogen umkehren}}.



### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Draft Kreis](Draft_Circle/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Draft Ellipse](Draft_Ellipse/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rechteck](Draft_Rectangle/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Draft Polygon](Draft_Polygon/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Draft BSpline](Draft_BSpline/de.md) 

-   Wenn der Anfangs- oder Endknoten eines offenen Splines so verschoben wird, dass sie zusammenfallen, wird der Spline geschlossen.
-   Kontextmenü des Knotens: {{Value|Punkt löschen}}. Für einen offenen Spline müssen mindestens zwei Punkte übrig bleiben. Bei einem geschlossenen Spline sind es mindestens drei Punkte.
-   Kontextmenü der Kante: {{Value|Punkt hinzufügen}}., {{Value|Spline schließen/öffnen}} ({{Version/de|0.21}}) and {{Value|Spline umkehren}} ({{Version/de|0.21}}).



### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Draft KubischeBezKurve](Draft_CubicBezCurve/de.md) und <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Draft BezKurve](Draft_BezCurve/de.md) 

-   Wenn der Anfangs- oder Endknoten einer offenen Kurve so verschoben wird, dass sie zusammenfallen, wird die Kurve geschlossen.
-   Kontextmenü des Knotens: {{Value|Punkt löschen}}, {{Value|Scharf machen}}, {{Value|Tangente machen}} und {{Value|Symmetrisch machen}}.
-   Kontextmenü der Kante: {{Value|Punkt hinzufügen}}, {{Value|Kurve schließen/öffnen}} ({{Version/de|0.21}}) and {{Value|Kurve umkehren}} ({{Version/de|0.21}}).



### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Bemaßen](Draft_Dimension/de.md) 

-   Winkelmaße können nicht bearbeitet werden.
-   Die Anfangs- und Endknoten von parametrischen Bemaßungen können nicht verschoben werden.
-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Wand](Arch_Wall/es.md) 

-   Ein einzelner Knoten zur Steuerung der Höhe der Wand wird über der {{PropertyData/de|Placement}} der Wand angezeigt.
-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Arch Structure](Arch_Structure.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Window](Arch_Window.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Arch Space](Arch_Space.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Arch Panel Cut](Arch_Panel_Cut.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Arch Panel Sheet](Arch_Panel_Sheet.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Würfel](Part_Box/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Zylinder](Part_Cylinder/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Kugel](Part_Sphere/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Kegel](Part_Cone/de.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Line](Part_Line.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Skizze](Sketcher_NewSketch/de.md) 

-   Nur Skizzen, die eine einzelne unbestimmte Linie enthalten, können bearbeitet werden.
-   Keine Kontextmenüs für dieses Objekt.



## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Die Farbe der temporären Knoten ist dieselbe wie die Farbe der Fangsymbole. Diese Farbe kann in den Voreinstellungen geändert werden: **Bearbeiten → Voreinstellungen... → Entwurf → Visuelle Einstellungen → Visuelle Einstellungen → Farbe**. Beachte, dass diese Farbe nicht für die temporären Knoten verwendet wird, die für [Draft BezKurven](Draft_BezCurve/de.md) angezeigt werden. Diese Knoten verwenden stattdessen die {{PropertyView/de|Linienfarbe}} der Kurve.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python-Methode, um Draft Bearbeiten auf Objekte anzuwenden. Um die Ergebnisse des Befehls zu emulieren, müssen die geometrische Eigenschaften der Objekte geändert werden.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/de
