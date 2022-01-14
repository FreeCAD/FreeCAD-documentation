---
- GuiCommand:/de
   Name:Draft Draft2Sketch
   Name/de:Entwurf EntwurfZuSkizze
   MenuLocation:Änderung → Entwurf zu Skizze
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench.md)
---

# Draft Draft2Sketch/de

## Beschreibung


<div class="mw-translate-fuzzy">

Der <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> **Entwurf EntwurfZuSkizze** Befehl wandelt [Entwurfsobjekte](Draft_Workbench/de.md) in [Skizzierer Skizzen](Sketcher_NewSketch/de.md) um und umgekehrt.


</div>

![](images/Draft_Draft2Sketch_example.png ) 
*Konvertieren von Entwurfsobjekten in Skizzierer Skizzen*

## Anwendung

1.  Wähle optional ein oder mehrere Entwurfsobjekte oder [Skizzierer Skizzen](Sketcher_NewSketch/de.md).
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_Draft2Sketch.svg" width=16px> [Entwurf EntwurfZuSkizze](Draft_Draft2Sketch/de.md)**.
    -   Wähle die **Änderung → <img src="images/Draft_Draft2Sketch.svg" width=16px> Entwurf zu Skizze** im Menü.
3.  Wenn du noch kein Objekt ausgewählt hast: Wähle ein Objekt in der [3D Ansicht](3D_view/de.md).
4.  Ein neues Objekt wird erstellt.

## Anmerkungen

-   Nicht-Entwurf Objekte, die vollkommen planar sind, können ebenfalls konvertiert werden.
-   Der Befehl kann nur Objekte verarbeiten, die aus **geraden Linien, Kreisbögen, elliptischen Bögen, B-Splines und Bézier Kurven** bestehen.
-   [Entwurf BezKurven](Draft_BezCurve/de.md) werden durch [Skizzierer BSplines](Sketcher_CreateBSpline/de.md) angenähert.
-   Der externe [KicadStepUp Arbeitsbereich](KicadStepUp_Workbench/de.md) enthält einen Befehl, um eine [Entwurf BSpline](Draft_BSpline/de.md) in eine Reihe von [Skizzierer Bögen](Sketcher_CreateArc/de.md) zu konvertieren. Weitere Informationen findest du im Forumsbeitrag [BSplines to Shape2DView and Sketcher](https://forum.freecadweb.org/viewtopic.php?f=9&t=25082).
-   [Dieser andere Forenbeitrag](https://forum.freecadweb.org/viewtopic.php?f=3&t=58781#p505207) enthält ein Makro für eine solche Konvertierung.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Objekte in eine Skizze zu konvertieren, verwendedie Methode `make_sketch` ({{Version/de|0.19}}) des Moduls Entwurf. Diese Methode ersetzt die veraltete Methode `makeSketch`.


```python
sketch = make_sketch(objects_list, autoconstraints=False, addTo=None, delete=False, name="Sketch", radiusPrecision=-1, tol=1e-3)
```

-    `objects_list`enthält die zu konvertierenden Objekte. Es ist entweder ein einzelnes Objekt oder eine Liste von Objekten. Unterstützt werden `Draft` Objekte, `Part::Feature` Objekte und `Part.Shape` Objekte.

-   Wenn `autoconstraints` `True` ist, werden übereinstimmende Zwangsbedingungen zu Knoten hinzugefügt, die zum selben Quellobjekt gehören.

-    `addTo`ist das vorhandene Skizzenobjekt, zu dem die Geometrie hinzugefügt wird. Wenn nicht angegeben, wird eine neue Skizze erstellt.

-   Wenn `delete` gleich `True` ist, werden die Quellobjekte gelöscht.

-    `name`ist der Name für die neue Skizze.

-    `radiusPrecision`gibt an, wie die Radiusbeschränkungen behandelt werden sollen:

    -   Verwenden Sie `-1`, um Radiuseinschränkungen zu deaktivieren.
    -   Verwenden Sie `0`, um einzelne Radiusbeschränkungen hinzuzufügen.
    -   Verwenden Sie eine positive Zahl, um Radien entsprechend dieser Genauigkeit zu runden und um gleiche Zwangsbedingungen zwischen Kurven mit gleichen Radien hinzuzufügen.

-    `tol`ist die Toleranz, die verwendet wird, um zu prüfen, ob Formen planar und koplanar sind. Verwenden Sie `-1` für eine strenge Prüfung.

-    `sketch`wird mit dem Skizzenobjekt zurückgegeben.

Um eine Skizze in Entwurfsobjekte umzuwandeln, verwende die Methode `draftify` des Entwurf Moduls.


```python
draftify(objectslist, makeblock=False, delete=True)
```

-    `objectslist`enthält die zu konvertierenden Objekte. Es ist entweder ein einzelnes Objekt oder eine Liste von Objekten.

-   Wenn `makeblock` gleich `True` ist, werden die konvertierten Objekte in einem `Part::Part2DObject` gruppiert.

-   Wenn `delete` gleich `True` ist, werden die Quellobjekte gelöscht.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(2000, 1000)
circle = Draft.make_circle(500)
doc.recompute()

sketch_from_draft = Draft.make_sketch([rectangle, circle], autoconstraints=True, delete=False, radiusPrecision=0)
doc.recompute()

draft_from_sketch = Draft.draftify(sketch_from_draft, delete=False)
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Draft2Sketch/de
