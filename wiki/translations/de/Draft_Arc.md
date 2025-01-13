---
 GuiCommand:
   Name: Draft Arc
   Name/de: Draft Bogen
   MenuLocation: Zeichnen , Bogenwerkzeuge , Kreisbogen<br>2D-Entwurf , Kreisbogen
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.7
   Shortcut: **A** **R**
   SeeAlso: Draft_Arc_3Points/de, Draft_Circle/de
---

# Draft Arc/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> **Draft Bogen** erstellt einen Kreisbogen auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) aus Mittelpunkt, Radius, Anfangswinkel und Öffnungswinkel. Der Radius und die Winkel können durch Indizieren der Punkte festgelegt werden.

Ein Draft-Bogen ist eigentlich ein [Draft-Kreis](Draft_Circle/de.md) mit einer {{PropertyData/de|First Angle}} die nicht identisch ist mir der {{PropertyData/de|Last Angle}}.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;"> 
*Ein durch vier Punkte festgelegter Bogen aus Mittelpunkt, Radius, Startpunkt und letztem Punkt des Bogens*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
2.  Die Schaltfläche **<img src="images/Draft_Arc.svg" width=16px> [Kreisbogen](Draft_Arc/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → Bogenwerkzeuge → <img src="images/Draft_Arc.svg" width=16px> Kreisbogen** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_Arc.svg" width=16px> Kreisbogen** auswählen.
    -   Das Tastaturkürzel **A** dann **R**.
3.  Der Aufgaben-Bereich **Kreisbogen** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
4.  Den ersten Punkt, den Mittelpunkt des Kreisbogens, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt  eingeben** drücken.
5.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder den **Radius** eingeben.
6.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder den **Startwinkel** eingeben.
7.  Den vierten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder den **Öffnungswinkel** eingeben.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Zum manuellen Eingeben der Koordinaten des Mittelpunktes werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam den Mauszeiger aus der [3D-Ansicht](3D_view.md) heraus zu bewegen, bevor die Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **N**drücken oder die Checkbox **Continue** aktivieren, um den Fortsetzen-Modus umzuschalten. Wenn der Fortsetzen-Modus aktiviert ist, wird der Befehl nach dem Beenden erneut gestartet, und ermöglicht so mit dem Erstellen von Bögen fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Ein Draft-Bogen kann mit dem Befehl [Draft-Bearbeiten](Draft_Edit/de.md) geändert werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft-Einstellungen](Draft_Preferences/de.md).

-   Wenn die Option **Bearbeiten → Einstellungen... → Draft → Allgemein → Create Part primitives if possible** aktiviert ist, wird ein [Part-Kreis](Part_Circle/de.md) anstelle eines Draft-Kreises erstellt.



## Eigenschaften

Siehe [Draft-Kreis](Draft_Circle/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Bogens wird die Methode `make_circle` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeCircle`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/de
