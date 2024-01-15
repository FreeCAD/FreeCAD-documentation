---
 GuiCommand:
   Name: Draft Polygon
   Name/de: Draft Vieleck
   MenuLocation: Entwurf , Vieleck
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **P** **G**
   Version: 0.7
---

# Draft Polygon/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> **Draft Vieleck** erstellt ein regelmäßiges Vieleck (Polygon) auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) aus einem Mittelpunkt und einem Radius. Der Radius kann durch Indizieren eines Punktes festgelegt werden.

Ein Draft-Vieleck kann mit der {{PropertyData/de|Draw Mode}} von inscribed (mit Umkreis) auf circumscribed (mit Inkreis) umgeschaltet werden. Die Ecken eines Draft-Vielecks können mit Rundung (Fillet) oder Fase (Chamfer) versehen werden, indem seine {{PropertyData/de|Fillet Radius}} oder {{PropertyData/de|Chamfer Size}} geändert werden.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;"> 
*Ein durch zwei Punkte, den Mittelpunkt und den Radius, festgelegtes regelmäßiges Vieleck*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Polygon.svg" width=16px> [Vieleck](Draft_Polygon/de.md)** drücken.
    -   Den Menüeintrag **Drafting → <img src="images/Draft_Polygon.svg" width=16px> Vieleck** auswählen.
    -   Das Tastaturkürzel **P** dann **G**.
2.  Der Aufgabenbereich **Polygon** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Die gewünschte Anzahl von Seiten (**Sides**) eingeben.
4.  Den ersten Punkt, den Mittelpunkt des Vielecks, in der [3D-Ansicht](3D_view/de.md) auswählen, oder Die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** drücken.
5.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder einen **Radius** eingeben.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **F**drücken oder die Checkbox **Füllen** aktivieren, um den Füllen-Modus umzuschalten. Ist der Füllen-Modus aktiviert, wird die {{PropertyData/de|Make Face}} des erstellten Vielecks auf `True` gesetzt und es erhält eine gefüllte Fläche.

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Vielecken fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Ein Draft-Vieleck kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Ist die Option **Bearbeiten → Einstellungen... → Draft → Allgemein → Part-Grundkörper erstellen, wenn möglich** aktiviert, wird ein [Part-Regelmäßiges-Polygon](Part_Circle/de.md) anstelle eines Draft-Vielecks erstellt.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Vieleck (Polygon-Objekt) wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the polygon. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the polygon.

-    **Draw Mode|Enumeration**: specifies if the polygon is {{value|inscribed}} in a circle or {{value|circumscribed}} around a circle.

-    **Faces Number|Integer**: specifies the number of sides of the polygon.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the polygon.

-    **Make Face|Bool**: specifies if the polygon makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Radius|Length**: specifies the radius of the circle that defines the polygon.



### Ansicht


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the polygon. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

To create a Draft Polygon use the `make_polygon` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePolygon` method.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Creates a `polygon` object with the given number of faces (`nfaces`), and based on a circle of `radius` in millimeters.
-   If `inscribed` is `True`, the polygon is inscribed in the circle, otherwise it will be circumscribed.
-   If `placement` is `None` the polygon is created at the origin and one of its vertices will lie on the X axis.
-   If `face` is `True`, the polygon will make a face, that is, it will appear filled.

Beispiel: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/de
