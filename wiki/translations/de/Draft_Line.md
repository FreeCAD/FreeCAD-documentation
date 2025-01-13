---
 GuiCommand:
   Name: Draft Line
   Name/de: Draft Linie
   MenuLocation: Zeichnen , Linie<br>2D-Entwurf , Linie
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **L** **I**
   Version: 0.7
   SeeAlso: Draft_Wire/de
---

# Draft Line/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Line.svg  style="width:24px;"> **Draft Linie** erstellt eine gerade Linie.

Eine Draft-Linie ist eigentlich eine [Draft-Polylinie](Draft_Wire/de.md) mit nur zwei Punkten.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;"> 
*Eine durch zwei Punkte festgelegte Linie*



## Anwendung

Siehe auch: [Draft-Ablage](Draft_Tray/de.md), [Draft-Einrasten](Draft_Snap/de.md) und [Draft-Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Line.svg" width=16px> [Linie](Draft_Line.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → <img src="images/Draft_Line.svg" width=16px> Linie** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_Line.svg" width=16px> Linie** auswählen.
    -   Das Tastaturkürzel **L** dann **I**.
2.  Der Aufgaben-Bereich **Linie** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
4.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam den Mauszeiger außerhalb der [3D-Ansicht](3D_view/de.md) zu plazieren, bevor man Koordinaten eingibt.

-   Um PolarKoordinaten zu veränden, werden Werte für die **Länge** und den **Winkel** jeweils mit abschließendem **Enter** eingegeben.

-   Die Check-Box **Angle** aktivieren, um den Zeiger auf den eingegebenen Winkel festzulegen.

-    **L**drücken, um den Fokus vom Eingabefeld **X** auf das Eingabefeld **Länge** und zurück zu setzen. Abhängig davon, auf welchem Eingabefeld der Fokus liegt ist das Häkchen in der Check-Box **Winkel** aktiviert oder nicht.

-    **R**drücken oder die Check-Box **Relativ** anklicken, um den Relativ-Modus umzuschalten. Ist der Relativ-Modus aktiviert, beziehen sich die Koordinaten des zweiten Punktes auf den ersten. Andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Check-Box **Global** anklicken, um den Global-Modus umzuschalten. ist der Global-Modus aktiviert, beziehen sich die Koordinaten auf das globale Koordinatensystem. Andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **N**drücken oder die Check-Box **Fortsetzen** anklicken, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Linien fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. ausgeschaltet.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Eine Draft-Linie kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.
-   Draft-Linien und [Draft Polylinien](Draft_Wire/de.md) können mit den Befehlen [Draft Polylinie](Draft_Wire/de.md), [Draft Verbinden](Draft_Join/de.md) oder [Draft Hochstufen](Draft_Upgrade/de.md) verbunden werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft-Einstellungen](Draft_Preferences/de.md).

-   So ändern Sie den anfänglichen Fokus des Aufgabenbereichs auf das Eingabefeld **Länge**: **Bearbeiten → Einstellungen... → Draft → Allgemein → Fokussierung auf Länge statt auf X-Koordinate setzen**. Beachten Sie, dass Sie den Zeiger in der [3D-Ansicht](3D_view/de.md) bewegen müssen, damit die Änderung wirksam wird.
-   Wenn die Option **Bearbeiten → Einstellungen... → Draft → Allgemein → Part-Grundkörper erstellen, wenn möglich** aktiviert ist, erzeugt der Befehl eine [Part Linie](Part_Line/de.md) anstelle einer Draft Linie.



## Eigenschaften

Siehe [Draft-Polylinie](Draft_Wire/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Linie wird die Methode `make_line` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeLine`.


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   Erzeugt ein `Line` Objekt zwischen den Punkten `p1` und `p2`, jeweils definiert durch ihren `FreeCAD.Vector`, mit Einheiten in Millimetern.
-   Erstellt ein `Line` Objekt aus einem `Part.LineSegment`.
-   Erzeugt ein `Line` Objekt vom ersten Knoten bis zum letzten Knoten der angegebenen `Shape`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/de
