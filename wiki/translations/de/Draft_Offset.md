---
 GuiCommand:
   Name: Draft Offset
   Name/de: Draft Versatz
   MenuLocation: Änderung , Versatz<br>Bearbeiten , Versatz
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **O** **S**
   SeeAlso: Part_Offset2D/de
---

# Draft Offset/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Offset.svg  style="width:24px;"> **Draft Versatz** verschiebt jedes Teilstück eines ausgewählten Objekts um einen gegebenen Abstand oder erstellt eine versetzte Kopie des ausgewählten Objekts.

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;"> 
*Versetzen eines Draft-Drahtes*



## Anwendung

Siehe auch: [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein Objekt auswählen. Das Objekt muß auf der aktuellen [Draft Arbeitsebene](Draft_SelectPlane/de.md) liegen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Offset.svg" width=16px> [Versetzen](Draft_Offset/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → <img src="images/Draft_Offset.svg" width=16px> Versetzen** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_Offset.svg" width=16px> Versetzen** auswählen.
    -   Das Tastaturkürzel **O** dann **S**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgaben-Bereich **Versatz** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informtionen.
5.  Zum Festlegen des Versatzabstands gibt es folgende Möglichkeiten:
    -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Eine Zahl eingeben:
        1.  Der Zeiger muß sich auf der richtigen Seite des Objektes in der [3D-Ansicht](3D_view/de.md) befinden.
        2.  Der Zeiger darf nicht aus der [3D-Ansicht](3D_view/de.md) heraus bewegt werden.
        3.  Einen **Abstand** eingeben.
        4.  Die Taste **Enter** drücken, um die Anweisung abzuschließen.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Ist die Checkbox **OCC-style offset** aktiviert, wird ein besonderer Versatzstil verwendet: Offene [Draft Polylinien](Draft_Wire/de.md) werden zu beiden Seiten versetzt und die neuen Kanten werden mit gerundeten Ecken verbunden. Dies funktioniert nur mit ebenen Objekten mit mindestens zwei Kanten. Dabei ist zu beachten, dass mit diesem Stil ein neues nicht parametrisches Objekt erstellt wird und, wenn der Modus Kopieren deaktiviert ist, das Originalobjekt entfernt wird.

-    **C**drücken oder die Checkbox **Kopieren** aktivieren, um den Kopieren-Modus umzuschalten. Ist der Kopieren-Modus aktiviert, erstellt der Befehl eine versetzte Kopie anstatt das Originalobjekt zu (v)ersetzen.

-   Wird **Alt** gedrückt gehalten, bevor Punkte in der [3D-Ansicht](3D_view/de.md) ausgewählt werden, wird auch der Kopieren-Modus umgeschaltet. Während **Alt** gedrückt gehalten wird, können mehrere Versatzpunkte ausgewählt werden. **Alt** loslassen, um den Befehl zu beenden und die erstellten Kopien anzuzeigen.

-    **Shift**gedrückt halten, um den Versatzabstand mit dem aktuellen Abschnitt verknüpft zu lassen.

-    **S**Drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Close** drücken, um den Befehl abzubrechen.



## Hinweise

-   Zum Erstellen einer Versetzte Version eines [Draft B-Splines](Draft_BSpline/de.md) werden seine Punkte einzeln versetzt und durch die neuen Punkte wird ein neuer Spline berechnet. Dieser neue Spline ist nicht parallel zum originalen Spline. Für eine exakt parallele Versatzkurve eines [Draft B-Splines](Draft_BSpline/de.md) sollte der Befehl [Part 2DVersatz](Part_Offset2D/de.md) eingesetzt werden.
-   Der Befehl Draft Offset kann [Draft Bézierkurve](Draft_BezCurve/de.md) nicht bearbeiten. Dafür kann der Befehl [Part 2DVersatz](Part_Offset2D/de.md) verwendet werden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Versetzen von Objekten wird die Methode `offset` des Draft-Moduls verwendet. Die Methode kann nur [Draft Wires](Draft_Wire/de.md), [Draft Circles](Draft_Circle/de.md), [Draft Rectangles](Draft_Rectangle/de.md), [Draft Polygons](Draft_Polygon/de.md) und [Draft BSplines](Draft_BSpline/de.md) verarbeiten.


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```

-    `obj`ist das zu versetzende Objekt.

-    `delta`enthält die Versatzinformationen:

    -   Für [Draft-Polylinien](Draft_Wire/de.md), [Draft-Rechtecke](Draft_Rectangle/de.md) und [Draft-Vielecke](Draft_Polygon/de.md) ist es ein Versatzvektor, der rechtwinklig auf dem ersten Abschnitt des Objekts steht.
    -   Für [Draft Circles](Draft_Circle/de.md) ist es der neue Radius.
    -   Für [Draft BSplines](Draft_BSpline/de.md) ist es eine Liste von neuen Punkten.

-   Ist `copy` auf `True` gesetzt, wird das Originalobjekt behalten und ein neues Objekt erstellt.

-   Ist `bind` auf `True` gesetzt, wird eine Fläche erstellt, indem die Form des Originalobjekts mit der Form seines Versatzobjekts verbunden wird. Dies funktioniert nur mit offenen [Draft-Polylinien](Draft_Wire/de.md).

-   Sind `sym` auf `True` und auch `bind` auf `True` gesetzt, wird das Originalobjekt zu beiden Seiten versetzt; die Gesamtbreite entspricht der Länge des gegebenen Vektors. Dies funktioniert nur mit offenen [Draft-Polylinien](Draft_Wire/de.md).

-   Ist `occ` auf `True` gesetzt, wird ein OCC-Style-Versatz verwendet. Siehe [Optionen](#Optionen.md). Ist `occ` auf `True` gesetzt, werden die Argumente `bind` und `sym` ignoriert.

-    `offset_obj`wird mit dem originalen versetzten Objekt zurückgegeben oder mit dem neuen Objekt. Ist `bind` auf `True` gesetzt oder `occ` auf `True` gesetzt, wird das neue Objekt ein `[Part::Feature](Part_Feature.md)`-Object.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Offset/de
