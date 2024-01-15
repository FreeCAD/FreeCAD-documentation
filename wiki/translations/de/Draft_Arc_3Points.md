---
 GuiCommand:
   Name: Draft Arc 3Points
   Name/de: Draft Bogen 3Punkte
   MenuLocation: Zeichnen , Bogenwerkzeuge , Bogen aus 3 Punkten
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **A** **T**
   Version: 0.19
   SeeAlso: Draft_Arc/de, Draft_Circle/de
---

# Draft Arc 3Points/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> **Draft Bogen 3Punkte** erstellt einen Kreisbogen auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) durch Eingabe von drei Punkten, die auf dem Umfang liegen; aus diesen drei Punkten werden Mittelpunkt und Radius bestimmt.

Ein Draft-Bogen ist eigentlich ein [Draft-Kreis](Draft_Circle/de.md) mit einer {{PropertyData/de|First Angle}} die nicht identisch ist mir der {{PropertyData/de|Last Angle}}.

<img alt="" src=images/Draft_Arc_3Points_example.png  style="width:400px;"> 
*Ein durch drei auf dem Umfang liegende Punkte festgelegter Bogen*



## Anwendung

Siehe auch: [Draft-Ablage](Draft_Tray/de.md), [Draft-Einrasten](Draft_Snap/de.md) und [Draft-Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Arc_3Points.svg" width=16px> [Bogen aus 3 Punkten](Draft_Arc_3Points/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → Bogenwerkzeuge → <img src="images/Draft_Arc_3Points.svg" width=16px> Bogen aus 3 Punkten** auswählen.
    -   Das Tastaturkürzel **A** dann **T**. {{Version/de|0.20}}
2.  Der Aufgaben-Bereich **Bogen aus 3 Punkten** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
4.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
5.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Zum manuellen Eingeben der Koordinaten des Mittelpunktes werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam den Mauszeiger aus der [3D-Ansicht](3D_view.md) heraus zu bewegen, bevor die Koordinaten eingegeben werden.

-    **R**drücken oder die Checkbox **Relative** aktivieren, um den Relativ-Modus umzuschalten. Wenn der Relativ-Modus aktiviert ist, beziehen sich Koordinaten auf den zuletzt eingegebenen Punkt, falls vorhanden, andernfalls auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **N**drücken oder die Checkbox **Continue** aktivieren, um den Fortsetzen-Modus umzuschalten. Wenn der Fortsetzen-Modus aktiviert ist, wird der Befehl nach dem Beenden erneut gestartet, und ermöglicht so mit dem Erstellen von Bögen fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Ein Draft-Bogen kann mit dem Befehl [Draft-Bearbeiten](Draft_Edit/de.md) geändert werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Wenn die Option **Bearbeiten → Einstellungen... → Draft → Allgemein → Create Part primitives if possible** aktiviert ist, erstellt der Befehl ein nicht editierbares [Part-Formelement](Part_Feature/de.md) anstelle eines Draft-Kreises.



## Eigenschaften

Siehe [Draft Kreis](Draft_Circle/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Bogens durch 3 Punkte wird die Methode `make_arc_3points` des Draft-Moduls verwendet:


```python
arc = make_arc_3points(points, placement=None, face=False, support=None, map_mode="Deactivated", primitive=False)
```

-   Erstellt ein `arc`-Objekt aus der gegebenen `points`-Liste.
-   Ist ein `placement` angegeben, wird der Mittelpunkt eines Kreisbogens auf diese Position verschoben. Siehe [Positionierung](Placement/de.md) für weitere Informationen.
-   Ist `face` auf `True` gesetzt, wird aus dem Kreisbogen eine Fläche erstellt, d.h. er wird gefüllt dargestellt.
-   Ist ein `support` angegeben, handelt es sich um eine `LinkSubList`, d.h. eine Liste, die ein Objekt und ein Unterelement dieses Objekts enthält. Dies wird verwendet, um das Objekt auf diesen Support zu referenzieren.

:   Zum Beispiel: support=[(obj, ("Face1"))].

-   Ist ein `map_mode` angegeben, handelt es sich um eine Zeichenkette, die die Art der Zuordnung festlegen, z.B.: map_mode='FlatFace', map_mode='ThreePointsPlane', usw. Siehe [Part-Befestigen](Part_EditAttachment/de.md) für weitere Informationen.
-   Ist `primitive` auf `True` gesetzt, wird der Bogen als einfaches [Part-Formelement](Part_Feature/de.md) erstellt, nicht als komplexes Draft-Objekt.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points = [App.Vector(0, 0, 0),
          App.Vector(5, 10, 0),
          App.Vector(10, 0, 0)]

arc = Draft.make_arc_3points(points)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc 3Points/de
