---
 GuiCommand:
   Name: Draft Circle
   Name/de: Draft Kreis
   MenuLocation: Zeichnen , Kreis<br>2D-Entwurf , Kreis
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **C** **I**
   Version: 0.7
   SeeAlso: Draft_Arc/de, Draft_Arc_3Points/de
---

# Draft Circle/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> **Draft Kreis** erstellt einen Kreis auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) aus Mittelpunkt und Radius. Der Radius kann durch Indizieren eines Punktes festgelegt werden.

Ein Draft-Kreis kann in einen Bogen gewandelt werden, indem seine {{PropertyData/de|First Angle}} und {{PropertyData/de|Last Angle}} auf unterschiedliche Werte gesetzt werden

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;"> 
*Ein durch zwei Punkte festgelegter Kreis aus Mittelpunkt und Radius*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Circle.svg" width=16px> [Kreis](Draft_Circle.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → <img src="images/Draft_Circle.svg" width=16px> Kreis** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_Circle.svg" width=16px> Kreis** auswählen.
    -   Das Tastaturkürzel **C** dann **I**.
2.  Der Aufgaben-Bereich **Kreis** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Den ersten Punkt, den Kreismittelpunkt, in der 3DAnsicht auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** drücken.
4.  Den zweiten Punkt in der 3DAnsicht auswählen oder einen **Radius** eingeben.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **F**drücken oder die Checkbox **Füllen** aktivieren, um den Füllen-Modus umzuschalten. Ist der Füllen-Modus aktiviert, wird die {{PropertyData/de|Make Face}} des erstellten Kreises auf `True` gesetzt und er erhält eine gefüllte Fläche.

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Kreisen fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Ein Draft-Kreis kann mit dem Befehl [Draft-Bearbeiten](Draft_Edit/de.md) geändert werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Ist die Option **Bearbeiten → Einstellungen... → Draft → Allgemein → Part-Grundkörper erstellen, wenn möglich** aktiviert, wird ein [Part-Kreis](Part_Circle/de.md) anstelle eines Draft-Kreises erstellt.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Kreis-Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|Area|Area}}(schreibgeschützt): Gibt den Flächeninhalt der Kreisfläche an. Der Wert ist {{value|0.0}}, wenn die {{PropertyData/de|Make Face}} auf `False` gesetzt ist oder die Fläche nicht erstellt werden kann.

-    {{PropertyData/de|First Angle|Angle}}: Legt den Startwinkel des Kreises fest; normalerweise {{value|0&#176;}}.

-    {{PropertyData/de|Last Angle|Angle}}: Legt den Endwinkel des Kreises fest; normalerweise {{value|0&#176;}}.

-    {{PropertyData/de|Make Face|Bool}}: Legt fest, ob die Kreisfläche erstellt wird oder nicht. Auf `True` gesetzt, wird eine Fläche erstellt, andernfalls wird nur der Kreisumfang als Teil des Objekts angesehen. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|First Angle}} und die {{PropertyData/de|Last Angle}} denselben Wert enthalten. Man beachte, dass {{value|0&#176;}} und {{value|360&#176;}} nicht als gleich angesehen werden.

-    {{PropertyData/de|Radius|Length}}: Legt den Radius des Kreises fest.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Pattern|Enumeration}}: Legt das [Draft-Muster](Draft_Pattern/de.md) fest, mit dem die Fläche des Kreises gefüllt wird. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Make Face}} auf `True` und die {{PropertyView/de|Display Mode}} auf {{value|Flat Lines}} gesetzt ist.

-    {{PropertyView/de|Pattern Size|Float}}: Legt die Größe des [Draft-Musters](Draft_Pattern.md) fest.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Kreises wird die Methode `make_circle` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeCircle`.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```

-   Erstellt ein `circle`-Objekt mit gegebenem `radius` in mm.
    -   
        `radius`
        
        kann auch eine `Part.Edge` sein, deren Attribut `Curve` ein `Part.Circle` sein muss.
-   Ist `placement` auf `None` gesetzt, wird der Kreis im Ursprung erstellt.
-   Ist `face` auf `True` gesetzt, erhält der Kreis eine Fläche, d.h. er wird gefüllt erscheinen.
-   Sind `startangle` und `endangle` angegeben (in Grad) und haben unterschiedliche Werte, werden sie verwendet und das Objekt erscheint als [Draft-Bogen](Draft_Arc/de.md).

Beispiel: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/de
