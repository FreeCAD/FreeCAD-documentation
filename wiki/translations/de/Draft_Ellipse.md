---
 GuiCommand:
   Name: Draft Ellipse
   Name/de: Entwurf Ellipse
   MenuLocation: Entwurf , Ellipse
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **E** **L**
   Version: 0.7
   SeeAlso: Draft_Circle/de, Draft_Arc/de
---

# Draft Ellipse/de

## Beschreibung


<div class="mw-translate-fuzzy">

Das Ellipsen Werkzeug erzeugt eine Ellipse in der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) durch Eingabe von zwei Punkten zur Definition der Eckpunkte eines Rechtecks, in das die Ellipse passt. Es verwendet den [Entwurf Linienstil](Draft_Linestyle/de.md) festgelegt auf die [Entwurf Ablage](Draft_Tray/de.md)


</div>


<div class="mw-translate-fuzzy">

Dieses Werkzeug kann auch zur Erstellung von elliptischen Bögen verwendet werden, indem der Start und Endwinkel angegeben wird. Zum Erstellen von Kreisen und Kreisbögen verwende die Werkzeuge [Entwurf Kreis](Draft_Circle/de.md) und [Entwurf Bogen](Draft_Arc/de.md). Du kannst auch eine Ellipsen oder Kreisbogen mit den Werkzeugen [Entwurf BSpline](Draft_BSpline/de.md) und [Entwurf BezKurve](Draft_BezCurve/de.md) annähern.


</div>

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Ellipse definiert durch die Ecken eines Rechtecks*


</div>

## Anwendung

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Draft_Ellipse.svg" width=16px> [Entwurf Ellipse](Draft_Ellipse/de.md)** Taste oder drücke **E** dann **L** Tasten.
2.  Klicke einen ersten Punkt in der 3D Ansicht oder

gib eine Koordinate ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste.

1.  Klicke einen zweiten Punkt in der 3D Ansicht oder

gib eine Koordinate ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste.


</div>

## Optionen

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Um Koordinaten manuell einzugeben, gib einfach die Ziffern ein, drücke dann **Enter** zwischen den X, Y und Z Komponenten. YDu kannst die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Schaltfläche drücken wenn Du die gewünschten Werte zum Einfügen des Punktes hast.
-   Drücke **R** oder klicke auf das Kontrollkästchen, um den *relativen* Modus umzuschalten. Wenn der Relativmodus eingeschaltet ist, sind die Koordinaten des zweiten Punktes relativ zum ersten Punkt; wenn nicht, sind sie absolut, ausgehend vom Ursprung (0,0,0).
-   Drücke **T** oder klicke das Kontrollkästchen an, um den Modus *fortsetzen* zu aktivieren. Wenn der Fortsetzungsmodus eingeschaltet ist, wird das Ellipsenwerkzeug nach dem Beenden der Form neu gestartet, so dass Du eine weitere Form zeichnen kannst, ohne die Werkzeugschaltfläche erneut zu drücken.
-   Drücke **L** oder klicke auf das Kontrollkästchen, um den Modus \"gefüllt\" zu aktivieren. Wenn der Modus \"gefüllt\" aktiviert ist, erzeugt die Ellipse eine gefüllte Fläche ({{PropertyData/de|Erstelle Fläche}} `True`); wenn nicht, erzeugt die Ellipse keine Fläche ({{PropertyData/de|Erstelle Fläche}} `False`).
-   Halte **STRG** während des Zeichnens gedrückt, um [Fangen](Draft_Snap/de.md) deinen Punkt unabhängig von der Entfernung zur nächsten Fangposition zu zwingen.
-   Halte **Umschalten**, während du auf [Beschränken](Draft_Constrain/de.md) deinen zweiten Punkt horizontal oder vertikal in Bezug auf den ersten zeichnest.
-   Drücke **Esc** oder die **Schließen** Taste, um den aktuellen Befehl abzubrechen.


</div>

## Notes

-   A Draft Ellipse can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Ellipse](Part_Ellipse.md) instead of a Draft Ellipse.

## Eigenschaften

See also: [Property editor](Property_editor.md).

A Draft Ellipse object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Daten

-    {{PropertyData/de|Erster Winkel}}: gibt den Winkel des ersten Punktes der Ellipse an; normalerweise 0°.

-    {{PropertyData/de|Letzter Winkel}}: gibt den Winkel des letzten Punktes der Ellipse an; normalerweise 0°.

-    {{PropertyData/de|Hauptradius}}: gibt den Hauptradius der Ellipse an; normalerweise 0°.

-    {{PropertyData/de|Nebenradius}}: gibt den kleinen Radius der Ellipse an.

:   Wenn beide Radien den gleichen Wert haben, sieht die Ellipse wie ein [Entwurf Kreis](Draft_Circle/de.md) aus.

-    {{PropertyData/de|Fläche erzeugen}}: gibt an, ob die Ellipse eine Fläche erzeugt oder nicht. Ist sie `True`, wird eine Fläche erzeugt, andernfalls wird nur der Umfang als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn die Form eine Vollellipse ist.

Damit es eine Vollellipse ist, müssen {{PropertyData/de|Erster Winkel}} und {{PropertyData/de|Letzter Winkel}} den gleichen Wert haben; andernfalls wird ein elliptischer Bogen angezeigt. Die Werte 0° und 360° werden als gleich betrachtet.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Ansicht

-    {{PropertyView/de|Muster}}: definiert ein [Entwurf Muster](Draft_Pattern/de.md), mit dem die Fläche der Form gefüllt wird. Diese Eigenschaft funktioniert nur, wenn {{PropertyData/de|Fläche erstellen}} `True` ist und {{PropertyView/de|Anzeigemodus}} auf \"Ebene Linien\" gesetzt ist.

-    {{PropertyView/de|Mustergröße}}: gibt die Größe des [Entwurf Muster](Draft_Pattern/de.md) an.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Entwurf API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Ellipsenwerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch folgende Funktion verwendet werden:


</div>


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```


<div class="mw-translate-fuzzy">

-   Erzeugt ein `Ellipse` Objekt mit gegebenem Haupt- ({incode\|majradius}) und Nebenradius (`minradius`) in Millimetern.
    -   Der größere Wert wird für den Hauptradius (X Achse) verwendet, wenn keine andere Platzierung angegeben ist.
-   Wenn ein `placement` angegeben wird, wird er verwendet; andernfalls wird die Form am Ursprung erzeugt.
-   Wenn `Fläche` `True` ist, wird die Ellipse eine Fläche bilden, d.h. sie wird gefüllt erscheinen.


</div>

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/de
