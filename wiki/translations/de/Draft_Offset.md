---
- GuiCommand   */de
   Name   *Draft Offset
   Name/de   *Entwurf Versetzen
   MenuLocation   *Entwurf → Versetzen
   Workbenches   *[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut   ***O** **S**
   SeeAlso   *[Part 2D Versatz](Part_Offset2D/de.md)
---

# Draft Offset/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Versatzwerkzeug verschiebt das ausgewählte Objekt um einen bestimmten Abstand (Versatz) senkrecht zu sich selbst.


</div>

<img alt="" src=images/Draft_Offset_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">



*Versetzen eines Drahtes um einen bestimmten Abstand von einer seiner Kanten*


</div>

## Anwendung

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Wähle das Objekt aus, das du versetzen möchtest.
2.  Drücke die **<img src="images/Draft_Offset.svg" width=16px> [Entwurf Versetzen](Draft_Offset/de.md)** Schaltfläche oder drücke **O** und dann **S** Tasten. Wenn kein Objekt ausgewählt ist, wirst du aufgefordert, eines auszuwählen.
3.  Klicke auf einen Punkt in der 3D Ansicht, oder gib einen Abstand ein.


</div>

## Optionen

The single character keyboard shortcuts and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Drücke **P** oder klicke auf das Kontrollkästchen, um den Kopiermodus umzuschalten. Wenn der Kopiermodus eingeschaltet ist, behält das Versatzwerkzeug die ursprüngliche Form an ihrer Stelle, erstellt aber eine skalierte Kopie an der gewählten Stelle.
-   Halte **Alt** gedrückt, während du den Punkt auswählst, um ebenfalls den Kopiermodus umzuschalten. Die **Alt** gedrückt halten, erlaubt dir versetzte Kopien platzieren; loslassen **Alt**, um den Vorgang abzuschließen und alle versetzten Formen zu sehen.
-   Klicke auf das \"OCC-Stil\" Kontrollkästchen, um den Modus \"OCC\" umzuschalten. Dadurch wird ein Versatz von beiden Seiten eines Liniensegments erzeugt, wodurch eine besonders geschlossene Form mit abgerundeten Kanten an den Enden der Segmente entsteht.

   *   
    **Hinweis   ***Bei diesem Stil werden die Originalsegmente entfernt, verwende also den Kopiermodus, um die Originalkanten zu erhalten.

-   Halte **Ctrl** während des Versatzes gedrückt, um [Fangen](Draft_Snap/de.md) deinen Punkt unabhängig vom Abstand an die nächstgelegene Fangposition zu zwingen.
-   Halte **Shift** gedrückt, um den Versatzabstand in Bezug auf das aktuelle Segment beizubehalten und zu vermeiden, dass ein anderer Bezug gewählt wird.
-   Drücke **Esc** oder die {{button|Close}} Schaltfläche , um den aktuellen Befehl abzubrechen; bereits platzierte Offset-Kopien bleiben erhalten.


</div>

## Notes

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch   ***

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Versatzwerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus verwendet werden, indem die folgende Funktion verwendet wird   *


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Versetzt den gegebenen `obj` Draht durch Anwendung des gegebenen `delta`, definiert als Vektor, auf seinen ersten Knoten.

-   Wenn `copy` `True` ist, wird ein anderes Objekt erzeugt, anstatt das ursprüngliche Objekt zu versetzen.

-   Wenn `bind` gleich `True` ist und vorausgesetzt, das Drahtobjekt ist offen, werden der ursprüngliche und der versetzte Draht an ihren Endpunkten miteinander verbunden und bilden eine Fläche.
    -   Wenn `sym` `True` ist, muss `bind` ebenfalls `True` sein, und der Versatz wird auf beiden Seiten des Drahtes vorgenommen, wobei die Gesamtbreite die Länge des gegebenen Vektors ist.

-   Wenn `occ` `True` ist, wird ein Versatz im OCC-Stil verwendet   * es wird von beiden Seiten versetzt, dann werden die neuen Drähte zusammengebunden und die Ecken abgerundet.

-    `Offsetobj`wird mit dem ursprünglichen Versatzobjekt oder mit der neuen Kopie zurückgegeben.


</div>

Beispiel   *


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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Offset/de
