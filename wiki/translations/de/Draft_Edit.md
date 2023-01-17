---
- GuiCommand:/de
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
    -   Für ein einzelnes Objekt: Den Eintrag **Edit** im MKontextmenü der [Baumansicht](Tree_view/de.md) auswählen. Dies funktioniert nur mit unterstützten Draft-Objekten. {{Version/de|1.0}}
3.  Wenn noch kein Objekt ausgewählt wurde: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Die ausgewählten Objekte werden mit temporären Knoten markiert, und der [Haupt-Aufgabenbereich](#Haupt_Aufgabenfeld.md) wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.

Bearbeitung fortsetzen!

1.  Verwende optional ein Knoten- oder Kantenkontextmenü. Diese Kontextmenüs sind nur für einige Entwurfsobjekte verfügbar. Weitere Informationen findest du unter [Unterstützte Objekte](#Unterstützte_Objekte.md).
    -   Führe einen der folgenden Schritte aus:
        -   Auf allen Betriebssystemen: Halte **E** gedrückt und klicke auf den Knoten oder die Kante. Um **E** zu verwenden, musst du eventuell einmal in die [3D Ansicht](3D_view/de.md) klicken, um sicherzustellen, dass diese den Fokus hat.
        -   Unter Windows: Halte **Alt** gedrückt und klicke auf den Knoten oder die Kante.
        -   Unter Linux: Halte **Shift**+**Alt**, **Strg**+**Alt** oder **Alt** gedrückt und klicke auf den Knoten oder die Kante.
        -   Unter macOS: Halte **Option** gedrückt und klicke auf den Knoten oder die Kante.
    -   Wähle eine Option aus dem Kontextmenü.
    -   Wenn die ausgewählte Option eine Punkteingabe erfordert:
        -   Das [Knoten Aufgabenpaneel](#Knoten_Aufgabenpaneel.md) wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
        -   Greife einen Punkt in der [3D Ansicht](3D_view/de.md), oder gib Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
2.  Optional Verschiebe einen Knoten:
    -   Klicke den Knoten in der [3D Ansicht](3D_view/de.md) an.
    -   Das [Knoten Aufgabenpaneel](#Knoten_Aufgabenpaneel.md) öffnet sich. Siehe [Optionen](#Optionen.md) für weitere Informationen.
    -   Greife einen Punkt in der [3D Ansicht](3D_view/de.md), oder gib Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
    -   Das Ergebnis hängt vom Objekt und dem ausgewählten Knoten ab.
    -   Drücke **Esc** oder die **Schliessen** Schaltfläche, um den Befehl zu beenden.



## Optionen

Die hier genannten Tastaturkürzel für einzelne Zeichen können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md).



### Hauptaufgabenpaneel


<div class="mw-translate-fuzzy">

-   Drücke **O** oder die **<img src="images/Draft_CloseLine.svg" width=16px> Schließen** Schaltfläche, um den Befehl zu beenden. Wenn ein einzelner [Entwurf Draht](Draft_Wire/de.md) ausgewählt wurde, wird der Draht geschlossen.
-   Drücke **Esc** oder die **Schliessen** Schaltfläche, um den Befehl zu beenden.


</div>




<div class="mw-translate-fuzzy">

### Knoten Aufgabenpaneel 


</div>


<div class="mw-translate-fuzzy">

-   Um die Koordinaten manuell einzugeben, gib die X, Y und Z Komponente ein und drücke nach jeder Eingabe die **Eingabe**. Oder drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche, wenn du die gewünschten Werte hast. Es ist ratsam, den Mauszeiger aus der [3D Ansicht](3D_view/de.md) zu bewegen, bevor du Koordinaten eingibst.
-   Um Polarkoordinaten zu verwenden, gib einen Wert für die **Länge** und einen Wert für den **Winkel** ein, und drücke jeweils **Eingabe**.
-   Hake das **Winkel** Kontrollkästchen, um den Zeiger auf den angegebenen Winkel zu beschränken.
-   Das **Relativ** Kontrollkästchen hat bei diesem Befehl keine Bedeutung.
-   Drücke **G** oder klicke auf das **Global** Kontrollkästchen, um den globalen Modus zu aktivieren. Wenn der globale Modus eingeschaltet ist, sind die Koordinaten relativ zum globalen Koordinatensystem, andernfalls sind sie relativ zur [Arbeitsebene](Draft_SelectPlane/de.md) des Koordinatensystems. {{Version/de|0.20}}
-   Das **Weiter** Kontrollkästchen hat bei diesem Befehl keine Bedeutung.
-   Drücke **S**, um [Entwurf Fangen](Draft_Snap/de.md) ein- oder auszuschalten.
-   Die **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig** Schaltfläche hat für diesen Befehl keine Bedeutung.


</div>



## Unterstützte Objekte 



### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Entwurf Linie](Draft_Line/de.md) und <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Entwurf Draht](Draft_Wire/de.md) 


<div class="mw-translate-fuzzy">

-   Wenn der Anfangs- oder Endknoten eines offenen Drahtes so verschoben wird, dass sie zusammenfallen, wird der Draht geschlossen.
-   Kontextmenü des Knotens: {{Value|Punkt löschen}}. Es müssen mindestens zwei Punkte verbleiben.
-   Kante Kontextmenü: {{Value|Punkt hinzufügen}}, {{Value|Draht umkehren}} ({{Version/de|0.20}}).


</div>



### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Entwurf Bogen](Draft_Arc/de.md) und <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Entwurf Bogen 3Punkte](Draft_Arc_3Points/de.md) 


<div class="mw-translate-fuzzy">

-   Knotenkontextmenü Zentrum: {{Value|Bogen verschieben}}.
-   Knotenkontextmenü Anfang: {{Value|Ersten Winkel setzen}}.
-   Knotenkontextmenü Ende: {{Value|letzten Winkel setzen}}.
-   Kontextmenü des mittleren Knotens: {{Value|Radius setzen}}.
-   Kante Kontextmenü: {{Value|Bogen invertieren}}. Derzeit funktioniert dies nicht.


</div>



### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Entwurf Kreis](Draft_Circle/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Entwurf Ellipse](Draft_Ellipse/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Entwurf Rechteck](Draft_Rectangle/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Entwurf Polygon](Draft_Polygon/de.md) 

-   Keine Kontextmenüs für dieses Objekt.



### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Entwurf BSpline](Draft_BSpline/de.md) 


<div class="mw-translate-fuzzy">

-   Wenn der Anfangs- oder Endknoten eines offenen Splines so verschoben wird, dass sie zusammenfallen, wird der Spline geschlossen.
-   Kontextmenü Knoten: {{Value|Punkt löschen}}. Für einen offenen Spline müssen mindestens zwei Punkte übrig bleiben. Bei einem geschlossenen Spline sind es mindestens drei Punkte.
-   Kontextmenü Kante: {{Value|Punkt hinzufügen}}.


</div>



### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Entwurf KubischeBezKurve](Draft_CubicBezCurve/de.md) und <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Entwurf BezKurve](Draft_BezCurve/de.md) 


<div class="mw-translate-fuzzy">

-   Wenn der Anfangs- oder Endknoten einer offenen Kurve so verschoben wird, dass sie zusammenfallen, wird die Kurve geschlossen.
-   Kontextmenü Knoten: {{Value|Scharf machen}}, {{Value|Tangente machen}}, {{Value|Symmetrisch machen}} und {{Value|Punkt löschen}}.
-   Kontextmenü Kante: {{Value|Punkt hinzufügen}}.


</div>



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


<div class="mw-translate-fuzzy">

-   Nur Skizzen, die eine einzelne unbeschränkte Linie enthalten können bearbeitet werden. Derzeit funktioniert dies nicht richtig.
-   Keine Kontextmenüs für dieses Objekt.


</div>



## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Die Farbe der temporären Knoten ist dieselbe wie die Farbe der Fangsymbole. Diese Farbe kann in den Voreinstellungen geändert werden: **Bearbeiten → Voreinstellungen... → Entwurf → Visuelle Einstellungen → Visuelle Einstellungen → Farbe**. Beachte, dass diese Farbe nicht für die temporären Knoten verwendet wird, die für [Entwurf BezKurven](Draft_BezCurve/de.md) angezeigt werden. Diese Knoten verwenden stattdessen die **Linienfarbe** der Kurve.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python Methode für Entwurf Editieren Objekte. Um die Ergebnisse des Befehls zu emulieren, müssen geometrische Eigenschaften von Objekten geändert werden.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/de
