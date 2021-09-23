---
- GuiCommand:/de
   Name:Draft Edit
   Name/de:Entwurf Bearbeiten
   MenuLocation:Änderung → Bearbeiten<br>Hilfsprogramme → Bearbeiten
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Shortcut:**D** **E**
   SeeAlso:[Std Bearbeiten](Std_Edit/de.md)
---

# Draft Edit/de


</div>

## Beschreibung

Der <img alt="" src=images/Draft_Edit.svg  style="width:16px;"> **Entwurf Bearbeiten** Befehl versetzt ausgewählte Objekte in den Entwurf bearbeiten Modus. In diesem Modus können die Eigenschaften von Objekten grafisch bearbeitet werden. Typischerweise können Knoten verschoben werden und in einigen Fällen können Kontextmenüoptionen ausgewählt werden. Der Befehl kann die meisten Entwurfsobjekte, aber auch einige andere Objekte bearbeiten. Siehe [Unterstützte Objekte](#Unterstützte_Objekte.md). Unterstützte Entwurfsobjekte können auch mit dem Befehl [Std Berabeiten](Std_Edit/de.md) in den Entwurf Bearbeitungsmodus versetzt werden.

![](images/Draft_Edit_example.png ) *4 Objekte im Entwurfsbearbeitungsmodus: ein Entwurf Draht (rot), ein Entwurf Bogen (schwarz), ein Entwurf BSpline (grün) und ein Entwurf BezKurve (magenta)*

## Anwendung

Siehe auch: [Entwurf Fang](Draft_Snap/de.md) und [Entwurf Beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

1.  Wähle optional ein oder mehrere Objekte aus. Beachte, dass sich zwar mehrere Objekte im Entwurf Bearbeitungsmodus befinden können, aber immer nur ein Objekt auf einmal bearbeitet werden kann.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wenn du noch kein Objekt ausgewählt hast: Doppelklicke auf ein Objekt in der [Baumansicht](Tree_view/de.md). Dies funktioniert nur bei unterstützten Entwurfsobjekten.
    -   Drücke die **<img src="images/Draft_Edit.svg" width=16px> [Entwurf Bearbeiten](Draft_Edit/de.md)** Schaltfläche.
    -   Wähle die Option **Änderung → <img src="images/Draft_Edit.svg" width=16px> Bearbeiten** aus dem Menü.
    -   Wähle die Option **Hilfsprogramme → <img src="images/Draft_Edit.svg" width=16px> Bearbeiten** aus dem Menü.
    -   Verwende die Tastaturkürzel: **D** und dann **E**.
3.  Wenn du noch kein Objekt ausgewählt hast: Wähle ein Objekt in der [3D Ansicht](3D_view/de.md) aus.
4.  Die ausgewählten Objekte werden mit temporären Knoten markiert, und das [Hauptaufgabenfeld](#Haupt_Aufgabenfeld.md) öffnet sich. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Verwende optional ein Knoten- oder Kantenkontextmenü. Diese Kontextmenüs sind nur für einige Entwurfsobjekte verfügbar. Weitere Informationen findest du unter [Unterstützte Objekte](#Unterstützte_Objekte.md).
    -   Führe einen der folgenden Schritte aus:
        -   Auf allen Betriebssystemen: Halte **E** gedrückt und klicke auf den Knoten oder die Kante. Um **E** zu verwenden, musst du eventuell einmal in die [3D Ansicht](3D_view/de.md) klicken, um sicherzustellen, dass diese den Fokus hat.
        -   Unter Windows: Halte **Alt** gedrückt und klicke auf den Knoten oder die Kante.
        -   Unter Linux: Halte **Shift**+**Alt**, **Strg**+**Alt** oder **Alt** gedrückt und klicke auf den Knoten oder die Kante.
        -   Unter macOS: Halte **Option** gedrückt und klicke auf den Knoten oder die Kante.
    -   Wähle eine Option aus dem Kontextmenü.
    -   Wenn die ausgewählte Option eine Punkteingabe erfordert:
        -   Das [Knoten Aufgabenpaneel](#Knoten_Aufgabenpaneel.md) wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
        -   Greife einen Punkt in der [3D Ansicht](3D_view/de.md), oder gib Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
6.  Optional Verschiebe einen Knoten:
    -   Klicke den Knoten in der [3D Ansicht](3D_view/de.md) an.
    -   Das [Knoten Aufgabenpaneel](#Knoten_Aufgabenpaneel.md) öffnet sich. Siehe [Optionen](#Optionen.md) für weitere Informationen.
    -   Greife einen Punkt in der [3D Ansicht](3D_view/de.md), oder gib Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
    -   Das Ergebnis hängt vom Objekt und dem ausgewählten Knoten ab.
    -   Drücke **Esc** oder die **Schliessen** Schaltfläche, um den Befehl zu beenden.


</div>

## Optionen

Die hier genannten Tastaturkürzel für einzelne Zeichen können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md).

### Hauptaufgabenpaneel

-   Drücke **O** oder die **[16px](Bild:Draft_CloseLine.svg.md) Schließen** Schaltfläche, um den Befehl zu beenden. Wenn ein einzelner [Entwurf Draht](Draft_Wire/de.md) ausgewählt wurde, wird der Draht geschlossen.
-   Drücke **Esc** oder die **Schliessen** Schaltfläche, um den Befehl zu beenden.

### Knoten Aufgabenpaneel 

-   Um die Koordinaten manuell einzugeben, gib die X, Y und Z Komponente ein und drücke nach jeder Eingabe die **Eingabe**. Oder drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche, wenn du die gewünschten Werte hast. Es ist ratsam, den Mauszeiger aus der [3D Ansicht](3D_view/de.md) zu bewegen, bevor du Koordinaten eingibst.
-   Um Polarkoordinaten zu verwenden, gib einen Wert für die **Länge** und einen Wert für den **Winkel** ein, und drücke jeweils **Eingabe**.
-   Hake das **Winkel** Kontrollkästchen, um den Zeiger auf den angegebenen Winkel zu beschränken.
-   Das **Relativ** Kontrollkästchen hat bei diesem Befehl keine Bedeutung.
-   Drücke **G** oder klicke auf das **Global** Kontrollkästchen, um den globalen Modus zu aktivieren. Wenn der globale Modus eingeschaltet ist, sind die Koordinaten relativ zum globalen Koordinatensystem, andernfalls sind sie relativ zur [Arbeitsebene](Draft_SelectPlane/de.md) des Koordinatensystems. {{Version/de|0.20}}
-   Das **Weiter** Kontrollkästchen hat bei diesem Befehl keine Bedeutung.
-   Drücke **S**, um [Entwurf Fangen](Draft_Snap/de.md) ein- oder auszuschalten.
-   Die **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig** Schaltfläche hat für diesen Befehl keine Bedeutung.

## Unterstützte Objekte 

### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Entwurf Linie](Draft_Line/de.md) und <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Entwurf Draht](Draft_Wire/de.md) 

-   Wenn der Anfangs- oder Endknoten eines offenen Drahtes so verschoben wird, dass sie zusammenfallen, wird der Draht geschlossen.
-   Kontextmenü des Knotens: {{Value|Punkt löschen}}. Es müssen mindestens zwei Punkte verbleiben.
-   Kante Kontextmenü: {{Value|Punkt hinzufügen}}, {{Value|Draht umkehren}} ({{Version/de|0.20}}).

### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Entwurf Bogen](Draft_Arc/de.md) und <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Entwurf Bogen 3Punkte](Draft_Arc_3Points/de.md) 

-   Knotenkontextmenü Zentrum: {{Value|Bogen verschieben}}.
-   Knotenkontextmenü Anfang: {{Value|Ersten Winkel setzen}}.
-   Knotenkontextmenü Ende: {{Value|letzten Winkel setzen}}.
-   Kontextmenü des mittleren Knotens: {{Value|Radius setzen}}.
-   Kante Kontextmenü: {{Value|Bogen invertieren}}. Derzeit funktioniert dies nicht.

### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Entwurf Kreis](Draft_Circle/de.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Entwurf Ellipse](Draft_Ellipse/de.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Entwurf Rechteck](Draft_Rectangle/de.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Entwurf Polygon](Draft_Polygon/de.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Entwurf BSpline](Draft_BSpline/de.md) 

-   Wenn der Anfangs- oder Endknoten eines offenen Splines so verschoben wird, dass sie zusammenfallen, wird der Spline geschlossen.
-   Kontextmenü Knoten: {{Value|Punkt löschen}}. Für einen offenen Spline müssen mindestens zwei Punkte übrig bleiben. Bei einem geschlossenen Spline sind es mindestens drei Punkte.
-   Kontextmenü Kante: {{Value|Punkt hinzufügen}}.

### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Entwurf KubischeBezKurve](Draft_CubicBezCurve/de.md) und <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Entwurf BezKurve](Draft_BezCurve/de.md) 

-   Wenn der Anfangs- oder Endknoten einer offenen Kurve so verschoben wird, dass sie zusammenfallen, wird die Kurve geschlossen.
-   Kontextmenü Knoten: {{Value|Scharf machen}}, {{Value|Tangente machen}}, {{Value|Symmetrisch machen}} und {{Value|Punkt löschen}}.
-   Kontextmenü Kante: {{Value|Punkt hinzufügen}}.

### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Entwurf Bemaßen](Draft_Dimension/de.md) 

-   Winkelbemaßungen können nicht bearbeitet werden.
-   Die Start- und Endknoten von parametrischen Bemaßungen können nicht verschoben werden.
-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Architektur Wand](Arch_Wall/es.md) 

-   Ein einzelner Knoten zur Steuerung der Höhe der Wand wird über den **Placement** der Wand angezeigt.
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

### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Box](Part_Box.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Cylinder](Part_Cylinder.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Sphere](Part_Sphere.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cone](Part_Cone.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Line](Part_Line.md) 

-   Keine Kontextmenüs für dieses Objekt.

### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Skizzierer Skizze](Sketcher_NewSketch/de.md) 

-   Nur Skizzen, die eine einzelne unbeschränkte Linie enthalten können bearbeitet werden. Derzeit funktioniert dies nicht richtig.
-   Keine Kontextmenüs für dieses Objekt.

## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Die Farbe der temporären Knoten ist dieselbe wie die Farbe der Fangsymbole. Diese Farbe kann in den Voreinstellungen geändert werden: **Bearbeiten → Voreinstellungen... → Entwurf → Visuelle Einstellungen → Visuelle Einstellungen → Farbe**. Beachte, dass diese Farbe nicht für die temporären Knoten verwendet wird, die für [Entwurf BezKurven](Draft_BezCurve/de.md) angezeigt werden. Diese Knoten verwenden stattdessen die **Linienfarbe** der Kurve.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python Methode für Entwurf Editieren Objekte. Um die Ergebnisse des Befehls zu emulieren, müssen geometrische Eigenschaften von Objekten geändert werden.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/de
