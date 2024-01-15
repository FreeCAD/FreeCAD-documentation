---
 GuiCommand:
   Name: Draft Ellipse
   Name/de: Draft Ellipse
   MenuLocation: Zeichnen , Ellipse
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **E** **L**
   Version: 0.7
   SeeAlso: Draft_Circle/de, Draft_Arc/de
---

# Draft Ellipse/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> **Draft Ellipse** erstellt eine Ellipse in der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) aus zwei Punkten, die ein Rechteck festlegen, in das die Ellipse hineinpasst.

Eine Draft-Ellipse kann in einen Ellipsenbogen gewandelt werden, indem ihre {{PropertyData/de|First Angle}} und {{PropertyData/de|Last Angle}} auf unterschiedliche Werte gesetzt werden

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;"> 
*Eine durch die Ecken eines Rechtecks festgelegte Ellipse*



## Anwendung

Siehe auch: [Draft-Ablage](Draft_Tray/de.md), [Draft-Einrasten](Draft_Snap/de.md) und [Draft-Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Ellipse.svg" width=16px> [Ellipse](Draft_Ellipse/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Ellipse.svg" width=16px> Ellipse** auswählen.
    -   Das Tastaturkürzel **E** dann **L**.
2.  Der Aufgaben-Bereich **Ellipse** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
4.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken. Dieser Punkt darf nicht auf die X-, Y- oder Z-Achse festgelegt werden.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **R**drücken oder die Checkbox **Relativ** aktivieren, um den Relativ-Modus umzuschalten. Ist der Relativ-Modus aktiviert, beziehen sich die Koordinaten des zweiten Punktes auf den ersten Punkt, andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **F**drücken oder die Checkbox **Füllen** aktivieren, um den Füllen-Modus umzuschalten. Ist der Füllen-Modus aktiviert, wird die {{PropertyData/de|Make Face}} der erstellten Ellipse auf `True` gesetzt und sie erhält eine gefüllte Fläche.

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Ellipsen fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Eine Draft-Ellipse kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft-Einstellungen](Draft_Preferences/de.md).

-   Ist die Option **Bearbeiten → Einstellungen... → Draft → Allgemein → Part-Grundkörper erstellen, wenn möglich** aktiviert, wird eine [Part-Ellipse](Part_Circle/de.md) anstelle einer Draft-Ellipse erstellt.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Draft-Ellipse (Ellipse-Objekt) wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    **Area|Area**(schreibgeschützt): Gibt den Flächeninhalt der Ellipsenfläche an. Der Wert ist {{value|0.0}}, wenn die {{PropertyData/de|Make Face}} auf `False` gesetzt ist oder die Fläche nicht erstellt werden kann.

-    **First Angle|Angle**: Legt den Winkel des ersten Punktes auf der Ellipse fest; normalerweise {{value|0&#176;}}.

-    **Last Angle|Angle**: Legt den Winkel des letzten Punktes auf der Ellipse fest; normalerweise {{value|0&#176;}}.

-    **Major Radius|Length**: Legt den Hauptradius der Ellipse fest.

-    **Make Face|Bool**: Legt fest, ob die Ellipsenfläche erstellt wird oder nicht. Auf `True` gesetzt, wird eine Fläche erstellt, andernfalls wird nur der Ellipsenumfang als Teil des Objekts angesehen. Diese Eigenschaft funktioniert nur, wenn die Form eine vollständige Ellipse ist.

-    **Minor Radius|Length**: Legt den Nebenradius der Ellipse fest.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Pattern|Enumeration}}: Legt das [Draft-Muster](Draft_Pattern/de.md) fest, mit dem die Fläche der Ellipse gefüllt wird. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Make Face}} auf `True` und die {{PropertyView/de|Display Mode}} auf {{value|Flat Lines}} gesetzt ist.

-    {{PropertyView/de|Pattern Size|Float}}: Legt die Größe des [Draft-Musters](Draft_Pattern.md) fest.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Ellipse wird die Methode `make_ellipse` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeEllipse`.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```

-   Erstellt ein `ellipse`-Objekt mit gegebenem `majradius` (Hauptradius) und `minradius` (Nebenradius) in Millimetern.
    -   Der größere Wert wird für den Hauptradius (X-Achse) verwendet, wenn keine andere Positionierung angegeben ist.
-   Ist `placement` auf `None` gesetzt, wird die Ellipse im Ursprung erstellt.
-   Ist `Fläche` auf `True` gesetzt, erhält die Ellipse eine Fläche, d.h. sie wird gefüllt erscheinen.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/de
