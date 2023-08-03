---
 GuiCommand:
   Name: Draft Offset
   Name/de: Draft Versatz
   MenuLocation: Änderung , Versatz
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **O** **S**
   SeeAlso: Part_Offset2D/de
---

# Draft Offset/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Offset.svg  style="width:24px;"> **Draft Versatz** verschiebt jedes Teilstück eines ausgewählten Objekts um einen gegebenen Abstand oder erstellt eine versetzte Kopie des ausgewählten Objekts.

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;"> 
*Versetzen eines Draft-Drahtes*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Ein Objekt auswählen. Das Objekt muß auf der aktuellen [EntwurfWähleEbene](Draft_SelectPlane/de.md) liegen.
2.  Es gibt mehrere Wege die Anweisung zu geben:
    -   Die **<img src="images/Draft_Offset.svg" width=16px> [Entwurf Versetzen](Draft_Offset/de.md)** Schaltfläche anklicken oder die Taste **O** und dann die Taste**S** drücken.

    -   
        **Änderung → <img src="images/Draft_Offset.svg" width=16px> Versetzen
**
        
        aus dem Menü wählen.

    -   Tastenkürzel: **O** dann **S** drücken.
3.  Wenn kein Objekt ausgewählt ist: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Die **Offset** Aufgabenansicht öffnet sich. Siehe auch [Options](#Options.md).
5.  Der Versatz wird wie folgt angegeben:
    -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) wählen
    -   Eine Zahl eingeben:
        1.  Der Zeiger muß auf die richtigen Seite des Objektes in der [3D-Ansicht](3D_view/de.md) zeigen.
        2.  Der Zeiger darf nicht aus der [3D-Ansicht](3D_view/de.md) bewegt werden.
        3.  Einen **Abstand** eingeben.
        4.  Die Taste **Enter** drücken, um die Anweisung abzuschließen.



## Optionen

Die hier genannten Tastaturkürzel für einzelne Zeichen und die hier beschriebenen Auswahltasten können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md).


<div class="mw-translate-fuzzy">

-   Drücke **P** oder klicke auf das Kontrollkästchen, um den Kopiermodus umzuschalten. Wenn der Kopiermodus eingeschaltet ist, behält das Versatzwerkzeug die ursprüngliche Form an ihrer Stelle, erstellt aber eine skalierte Kopie an der gewählten Stelle.
-   Halte **Alt** gedrückt, während du den Punkt auswählst, um ebenfalls den Kopiermodus umzuschalten. Die **Alt** gedrückt halten, erlaubt dir versetzte Kopien platzieren; loslassen **Alt**, um den Vorgang abzuschließen und alle versetzten Formen zu sehen.
-   Klicke auf das \"OCC-Stil\" Kontrollkästchen, um den Modus \"OCC\" umzuschalten. Dadurch wird ein Versatz von beiden Seiten eines Liniensegments erzeugt, wodurch eine besonders geschlossene Form mit abgerundeten Kanten an den Enden der Segmente entsteht.

:   
    **Hinweis:**Bei diesem Stil werden die Originalsegmente entfernt, verwende also den Kopiermodus, um die Originalkanten zu erhalten.

-   Halte **Ctrl** während des Versatzes gedrückt, um [Fangen](Draft_Snap/de.md) deinen Punkt unabhängig vom Abstand an die nächstgelegene Fangposition zu zwingen.
-   Halte **Shift** gedrückt, um den Versatzabstand in Bezug auf das aktuelle Segment beizubehalten und zu vermeiden, dass ein anderer Bezug gewählt wird.
-   Drücke **Esc** oder die {{button|Close}} Schaltfläche , um den aktuellen Befehl abzubrechen; bereits platzierte Offset-Kopien bleiben erhalten.


</div>



## Hinweise

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe des Abstands zu ändern: **Bearbeiten → Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen**



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Das Versatzwerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus verwendet werden, indem die folgende Funktion verwendet wird:


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Versetzt den gegebenen `obj` Draht durch Anwendung des gegebenen `delta`, definiert als Vektor, auf seinen ersten Knoten.

-   Wenn `copy` `True` ist, wird ein anderes Objekt erzeugt, anstatt das ursprüngliche Objekt zu versetzen.

-   Wenn `bind` gleich `True` ist und vorausgesetzt, das Drahtobjekt ist offen, werden der ursprüngliche und der versetzte Draht an ihren Endpunkten miteinander verbunden und bilden eine Fläche.
    -   Wenn `sym` `True` ist, muss `bind` ebenfalls `True` sein, und der Versatz wird auf beiden Seiten des Drahtes vorgenommen, wobei die Gesamtbreite die Länge des gegebenen Vektors ist.

-   Wenn `occ` `True` ist, wird ein Versatz im OCC-Stil verwendet: es wird von beiden Seiten versetzt, dann werden die neuen Drähte zusammengebunden und die Ecken abgerundet.

-    `Offsetobj`wird mit dem ursprünglichen Versatzobjekt oder mit der neuen Kopie zurückgegeben.


</div>

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
