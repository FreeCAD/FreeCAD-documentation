---
- GuiCommand:/de
   Name:Draft Fillet
   Name/de:Entwurf Verrundung
   MenuLocation:Entwurf → Verrundung
   Workbenches:[Arbeitsbereich Entwurf](Draft_Workbench/de.md)
   Version:0.19
   SeeAlso:[Entwurf Linie](Draft_Line/de.md), [Entwurf Draht](Draft_Wire/de.md)
---

# Draft Fillet/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das [Entwurf Verrundungswerkzeug](Draft_Fillet/de.md) erstellt eine Verrundung, eine abgerundete Ecke, zwischen zwei [Entwurf Linien](Draft_Line/de.md). Alternativ kann es auch eine Fase, eine gerade Kante, zwischen diesen beiden Linien erzeugen.


</div>

<img alt="" src=images/Draft_Fillet_example.png  style="width:400px;"> 
*Mehrere Verrundungen und Fasen, die zwischen zwei Linien entstehen*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle zwei [Entwurf Linie](Draft_Line/de.md), die bereits auf dem Dokument platziert sind und sich an einem Punkt treffen.
2.  Drücke die Taste **<img src="images/Draft_Fillet.svg" width=16px> [Entwurf Verrundung](Draft_Fillet/de.md)** Taste.
3.  Wähle den Radius der Verrundung und drücke dann **Enter**.


</div>

## Optionen


<div class="mw-translate-fuzzy">

-   Aktivieredas Kontrollkästchen \"Originalobjekte löschen\", wenn du die beiden Originalzeilen löschen möchtest und nur das neue Verrundungsobjekt übrig lässt.
-   Aktivieredas Kontrollkästchen \"Fase erzeugen\", wenn du eine gerade Kante anstelle einer abgerundeten Kante zwischen den beiden Linien erzeugen möchtest.
-   Drücke **Esc** oder die Taste **Close**, um den aktuellen Befehl abzubrechen.


</div>

## Anmerkungen


<div class="mw-translate-fuzzy">

-   Das resultierende Verrundungsobjekt ist nicht editierbar.
-   Wenn der Radius zu groß ist, als dass der erzeugte Bogen nicht zu einer der Linien tangiert wäre, wird der Vorgang nicht erfolgreich sein.
-   Im Moment werden nur einzelne Linien unterstützt; [Draft Wires](Draft_Wire/de.md), d.h. Linien mit mehreren Punkten, führen möglicherweise nicht zum gewünschten Ergebnis.


</div>

## Eigenschaften


<div class="mw-translate-fuzzy">

Siehe auch: [Eigenschaftseditor](property_editor/de.md).


</div>

A Draft Fillet object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Daten


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Start**: (schreibgeschützt) gibt den Startpunkt an.

-    **End**: (schreibgeschützt) gibt den Endpunkt an.

-    **Length**: (schreibgeschützt) gibt die Länge des gesamten Segments an.

-    **Fillet Radius**: (schreibgeschützt) Radius, mit dem die Verrundung erstellt wurde.


</div>

### Ansicht


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Ansicht 

-    {{PropertyView/de|Ende Pfeil}}: Wenn es `True` ist, zeigt es ein Symbol am letzten Punkt der Linie an, so dass es als Anmerkungslinie verwendet werden kann.

-    {{PropertyView/de|Pfeil Größe}}: Gibt die Größe des Symbols an, das am Ende der Zeile angezeigt wird.

-    **Pfeil Typ**: gibt den Typ des am Ende der Zeile angezeigten Symbols an, das \"Punkt\", \"Kreis\", \"Pfeil\", \"Haken\", oder \"Haken-2\" sein kann.


</div>

## Skripten


<div class="mw-translate-fuzzy">


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Kreis Werkzeug kann sowohl in [Makros](Macros/de.md) als auch aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


</div>


```python
fillet = make_fillet([line1, line2], radius=100, chamfer=False, delete=False)
```

-   Erzeugt ein `Fillet` Objekt zwischen den Linien `line1` und `line2`, wobei die Krümmung mit `radius` erfolgt.
-   Wenn `chamfer` `True` ist, erzeugt es eine gerade Kante mit der Länge von `radius`, anstatt einer abgerundeten Kante.
-   Wenn `delete` `True` ist, löscht es die angegebenen `line1` und `line2`, und lässt nur das neue Objekt übrig.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p2, p3)

doc.recompute()

fillet = Draft.make_fillet([line1, line2], radius=500)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Fillet/de
