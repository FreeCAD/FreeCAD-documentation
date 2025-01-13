---
 GuiCommand:
   Name: Draft Polygon
   Name/de: Draft Vieleck
   MenuLocation: Zeichnen , Vieleck<br>2D-Entwurf , Vieleck
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
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
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen→ <img src="images/Draft_Polygon.svg" width=16px> Vieleck** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_Polygon.svg" width=16px> Vieleck
**
    -   Das Tastaturkürzel **P** dann **G**.
2.  Der Aufgabenbereich **Polygon** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Die gewünschte Anzahl von Seiten (**Sides**) eingeben.
4.  Den ersten Punkt, den Mittelpunkt des Vielecks, in der [3D-Ansicht](3D_view/de.md) auswählen, oder Die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
5.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder einen **Radius** eingeben.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

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

-    {{PropertyData/de|Area|Area}}: (nur Lesezugriff) gibt den Flächeninhalt der Fläche des Vielecks an. Der Wert ist {{value|0.0}}, wenn die {{PropertyData/de|Make Face}} `False` ist.

-    {{PropertyData/de|Chamfer Size|Length}}: gibt die Länge der Fasen an den Ecken des Vielecks an.

-    {{PropertyData/de|Draw Mode|Enumeration}}: gibt an, ob das Vieleck einen Umkreis einbeschrieben ist ({{value|inscribed}}) oder ob ein Inkreis von ihm umschrieben wird ({{value|circumscribed}}).

-    {{PropertyData/de|Faces Number|Integer}}: gibt die Anzahl der Seiten des Vielecks an.

-    {{PropertyData/de|Fillet Radius|Length}}: gibt den Radius der Verrundungen an den Ecken des Vielecks an.

-    {{PropertyData/de|Make Face|Bool}}: gibt an, ob das Vieleck eine Fläche erzeugt oder nicht. Wenn `True`, wird eine Fläche erstellt, andernfalls wird nur der Umriss als Teil des Objekts betrachtet.

-    {{PropertyData/de|Radius|Length}}: gibt den Radius des Kreises an, der das Vieleck definiert.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Pattern|Enumeration}}: Legt das [Draft-Muster](Draft_Pattern/de.md) fest, mit dem die Fläche des Vielecks gefüllt wird. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Make Face}} auf `True` und die {{PropertyView/de|Display Mode}} auf {{value|Flat Lines}} gesetzt ist.

-    {{PropertyView/de|Pattern Size|Float}}: Legt die Größe des [Draft-Musters](Draft_Pattern/de.md) fest.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um ein Draft-Vieleck zu erstellen, wird die Methode `make_polygon` ({{Version/de|0.19}}) des Draft-Moduls verwendet. Diese Methode ersetzt die veraltete Methode `makePolygon`.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Erzeugt ein `polygon`-Objekt mit der angegebenen Anzahl von Flächen (`nfaces`) und basierend auf einem Kreis mit einem `radius` in Millimetern.
-   Ist `inscribed` `True`, wird das Vieleck in einem Umkreis einbeschrieben, andernfalls umschreibt es einen Inkreis.
-   Wenn `placement` `None` ist, wird das Vieleck im Ursprung erstellt und einer seiner Eckpunkte liegt auf der X-Achse.
-   Wenn `face` `True` ist, bildet das Vieleck eine Fläche, d. h. es wird ausgefüllt.

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
