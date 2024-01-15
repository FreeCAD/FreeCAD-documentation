---
 GuiCommand:
   Name: Draft Point
   Name/de: Draft Punkt
   MenuLocation: Zeichnen , Punkt
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Version: 0.7
---

# Draft Point/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Point.svg  style="width:24px;"> **Draft Punkt** erstellt einen einfachen Punkt. Draft-Punkte können nützlich sein als Referenz für die Positionierung von Linien, Polylinien oder anderen Objekten.

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">



## Anwendung

Siehe auch: [Draft-Ablage](Draft_Tray/de.md), [Draft-Einrasten](Draft_Snap/de.md) und [Draft-Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
2.  Die Schaltfläche **<img src="images/Draft_Point.svg" width=16px> [Punkt](Draft_Point/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Point.svg" width=16px> Punkt** auswählen.
    -   Der Aufgaben-Bereich **Punkt** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Punkten fortzufahren.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft EinrastenInDerNähe](Draft_Snap_Near/de.md) verwenden ({{VersionMinus/de|0.20}}) oder <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> [Draft EinrastenAufEndpunkt](Draft_Snap_Endpoint.md) ({{VersionPlus/de|0.21}}), um an Draft-Punkten einzurasten.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Punkt-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|X|Abstand}}: gibt die X Koordinate des Punktes an.

-    {{PropertyData/de|Y|Abstand}}: gibt die Y Koordinate des Punktes an.

-    {{PropertyData/de|Z|Abstand}}: gibt die Z Koordinate des Punktes an.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Pattern|Enumeration}}: nicht verwendet.

-    {{PropertyView/de|Pattern Size|Float}}: nicht verwendet.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um einen Draft-Punkt zu erstellen, wird die Methode `make_point` ({{Version/de|0.19}}) des Draft-Moduls verwendet. Diese Methode ersetzt die veraltete Methode `makePoint`.


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```

-   Erstellt ein `Punkt`-Objekt an den angegebenen `X`-, `Y`- und `Z`-Koordinaten mit Einheiten in mm. Falls keine Koordinaten angegeben werden, wird der Punkt bei (0,0,0) angelegt.
    -   Falls `X` ein durch einen `FreeCAD.Vector` definierter `Punkt` ist, wird dieser verwendet.

-    `color`ist ein Tupel `(R, G, B)`, das die Farbe des Punktes in der RGB-Farbskala angibt; jeder Wert des Tupels sollte im Bereich von `0` bis `1` liegen.

-    `name`ist der Name des Objekts.

-    `point_size`ist die Größe des Objekt in Pixeln, falls die grafische Benutzeroberfläche geladen ist

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

point1 = Draft.make_point(1600, 1400, 0)

p2 = App.Vector(-3200, 1800, 0)
point2 = Draft.make_point(p2, color=(0.5, 0.3, 0.6), point_size=10)

doc.recompute()
```

Beispiel:

Dieser Code erzeugt `N` zufällige Punkte innerhalb eines Quadrats der Seitenlänge `2L`. Er macht eine Schleife, die `N` Punkte erzeugt, die überall von `-L` bis `+L` auf X und Y erscheinen können. Er wählt auch eine zufällige Farbe und Größe für jeden Punkt. Ändere `N`, um die Anzahl der Punkte zu ändern, und ändere `L`, um den von den Punkten abgedeckten Bereich zu ändern.


```python
import random
import FreeCAD as App
import Draft

doc = App.newDocument()

L = 1000
centered = App.Placement(App.Vector(-L, -L, 0), App.Rotation())
rectangle = Draft.make_rectangle(2*L, 2*L, placement=centered)

N = 10
for i in range(N):
    x = 2*L*random.random() - L
    y = 2*L*random.random() - L
    z = 0
    r = random.random()
    g = random.random()
    b = random.random()
    size = 15*random.random() + 5
    Draft.make_point(x, y, z, color=(r, g, b), point_size=size)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Point/de
