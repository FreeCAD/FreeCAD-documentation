---
 GuiCommand:
   Name: Draft Line
   Name/de: Draft Linie
   MenuLocation: Entwurf , Linie
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
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
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Line.svg" width=16px> Linie** auswählen.
    -   Das Tastaturkürzel **L** dann **I**.
2.  Der Aufgaben-Bereich **Linie** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
4.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).


<div class="mw-translate-fuzzy">

## Optionen 

-   Drücke **X**, **Y** oder **Z** nach dem ersten Punkt, um den zweiten Punkt auf der angegebenen Achse zu beschränken.
-   Um Koordinaten manuell einzugeben, gib einfach die Zahlen ein und drücken dann **Enter** zwischen den einzelnen X-, Y- und Z-Komponenten.
    -   Du kannst auch die Polarkoordinaten des Punktes definieren, indem du einen Wert für \"Länge\" und \"Winkel\" angibst. Klicke auf das Kontrollkästchen neben \"Winkel\", um den Zeiger auf den angegebenen Winkel zu beschränken.
    -   Du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste drücken wenn Du die gewünschten Werte hast, um den Punkt einzufügen.
-   Drücke {**R** oder klicke auf das Kontrollkästchen, um den *relativen* Modus umzuschalten. Wenn der Relativmodus eingeschaltet ist, sind die Koordinaten des zweiten Punktes relativ zum ersten; wenn nicht, sind sie absolut, bezogen auf den Ursprung (0,0,0).
-   Drücke **T** oder klicke auf das Kontrollkästchen, um den *Weiter*-Modus umzuschalten. Wenn der Fortsetzungsmodus eingeschaltet ist, wird das Linienwerkzeug nach der Eingabe des zweiten Punktes neu gestartet, so dass du ein weiteres Liniensegment zeichnen kannst, ohne die Werkzeugtaste erneut zu drücken.
-   Halte **Ctrl** während des Zeichnens gedrückt, um [Fang](Draft_Snap/de.md) deinen Punkt auf die nächstgelegene Fangposition zu zwingen, unabhängig von der Entfernung.
-   Halte **Shift** während des Zeichnens gedrückt, um deinen zweiten Punkt horizontal oder vertikal in Bezug auf den ersten zu [Beschränkung](Draft_Constrain/de.md).
-   Drücke **Strg**+**Z** oder drücke die {{button|<img src="images/Draft_UndoLine.svg" width=12px> Rückgängig}} Schaltfläche, um den letzten Punkt rückgängig zu machen.
-   Drücke **Esc** oder die Taste **Close**, um den aktuellen Befehl abzubrechen.


</div>



## Hinweise

-   Eine Draft-Linie kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.
-   Draft-Linien und [Draft Polylinien](Draft_Wire/de.md) können mit den Befehlen [Draft Polylinie](Draft_Wire/de.md), [Draft Verbinden](Draft_Join/de.md) oder [Draft Hochstufen](Draft_Upgrade/de.md) verbunden werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft-Einstellungen](Draft_Preferences/de.md).

-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   If the **Edit → Preferences... → Draft → General → Create Part primitives if possible** option is checked, the command will create a [Part Line](Part_Line.md) instead of a Draft Line.



## Eigenschaften

Siehe [Draft-Polylinie](Draft_Wire/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

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
