---
- GuiCommand:/de
   Name:Draft Wire
   Name/de:Entwurf Draht
   MenuLocation:Entwurf → Polylinie
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Shortcut:**P** **L**
   Version:0.7
   SeeAlso:[Entwurf Linie](Draft_Line/de.md), [Entwurf BSpline](Draft_BSpline/de.md)
---

# Draft Wire/de


</div>

## Beschreibung

Der <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Entwurf Draht** Befehl [erzeugt](#Erzeugt.md) eine Polylinie, eine Folge von mehreren Liniensegmenten. Der Befehl kann auch verwendet werden um [Entwurf Linien](Draft_Line/de.md) und Entwurf Drähte zu [verbinden](#verbinden.md).

The corners of a Draft Wire can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide the edges of a Draft Wire by changing its **Subdivisions** property.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Draht definiert durch mehrfache Punkte*

## Erstellen

### Anwendung

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Draft_Wire.svg" width=16px> [Entwurf Draht](Draft_Wire/de.md)** Schaltfläche, oder drücke **P** dann **L** Tasten.
2.  Klicke auf einen ersten Punkt in der 3D Ansicht, oder gib eine [Koordinate](Draft_Coordinates/de.md) ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** Schaltfläche im zugehörigen Aufgabenpaneel Linie.
3.  Klicke auf weitere Punkte in der 3D Ansicht, oder gib eine [Koordinate](Draft_Coordinates/de.md) und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** Schaltfläche im zugehörigen Aufgabenpaneel Linie.
4.  Drücke **Esc** oder die **Close** Schaltfläche, um die Bearbeitung abzuschließen.


</div>

### Optionen

Die im Aufgabenpaneel verfügbaren Einzelzeichen Tastaturkürzel können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.


<div class="mw-translate-fuzzy">

-   Drücke **A** oder die **<img src="images/Draft_FinishLine.svg" width=12px> [Beenden](Draft_FinishLine/de.md)** Taste, um den Draht fertigzustellen, offen hinterlassend.
-   Drücke **O** oder die **<img src="images/Draft_CloseLine.svg" width=12px> [Schliessen](Draft_CloseLine/de.md)** Schaltfläche um den Draht zu schliessen, d.h. es wird ein Segment vom letzten Punkt zum ersten hinzugefügt, um eine Fläche zu bilden. Es sind mindestens drei Punkte erforderlich, um eine Fläche zu bilden.
-   Drücke **W** oder die **<img src="images/Draft_Wipe.svg" width=12px> [Wischen](Draft_Wipe/de.md)** Taste um die bereits platzierten Liniensegmente zu entfernen, aber den Draht vom letzten Punkt aus weiter zu bearbeiten.
-   Drücke **U** oder die **<img src="images/Draft_SelectPlane.svg" width=12px> [Setze WP](Draft_SelectPlane/de.md)** Taste um die aktuelle Arbeitsebene in der Orientierung des letzten Punktes anzupassen.
-   Drücke **X**, **Y** oder **Z** nach einem Punkt, um den nächsten Punkt auf der gegebenen Achse zu beschränken.
-   Um Koordinaten manuell einzugeben, gib einfach die Zahlen ein und drücke dann **Enter** zwischen jeder X, Y und Z Komponente. Du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** Schaltfläche drücken wenn Du die gewünschten Werte zum Einfügen des Punktes hast.
-   Drücke **R** oder klicke auf das Kontrollkästchen, um den *relativen* Modus umzuschalten. Wenn der Modus \"relativ\" eingeschaltet ist, sind die Koordinaten des nächsten Punktes relativ zum letzten; wenn nicht, sind sie absolut, ausgehend vom Ursprung (0,0,0).
-   Drücke **T** oder klicke das Kontrollkästchen an, um den Modus *fortsetzen* zu aktivieren. Wenn der Fortsetzungsmodus eingeschaltet ist, wird das Drahtwerkzeug nach Beendigung des Drahtes neu gestartet, so dass Du einen weiteren Draht zeichnen kannst, ohne den Werkzeugknopf erneut zu drücken.
-   Drücke **L** oder klicke auf das Kontrollkästchen, um den *ausgefüllten* Modus umzuschalten. Wenn der Modus \"ausgefüllt\" eingeschaltet ist, erzeugt ein geschlossener Draht eine ausgefüllte Fläche {{PropertyData/de|Erstelle Fläche}} `True`; wenn nicht, erzeugt der geschlossene Draht keine Fläche {{PropertyData/de|Erstelle Fläche}} `False`

:   
    **Hinweis:**; der Draht sollte nicht gefüllt werden, wenn er sich selbst schneidet, da er keine ordnungsgemäße Fläche erzeugt. Wenn der Draht gefüllt ist, aber keine Form sichtbar ist, setze manuell {{PropertyData/de|Erstelle Fläche}} auf `False`, um den Draht zu sehen.

-   Halte **Ctrl** während des Zeichnens gedrückt, um [Fangen](Draft_Snap/de.md) Deinen Punkt unabhängig vom Abstand zur nächsten Fangposition zu zwingen.
-   Halte **Umschalten**, während Du [Beschränken](Draft_Constrain/de.md) Deinen nächsten Punkt horizontal oder vertikal in Bezug auf den letzten zeichnest.
-   Drücke **Ctrl**+**Z** oder drücke die {{button|<img src="images/Draft_UndoLine.svg" width=12px> [rückgängig](Draft_UndoLine/de.md)}} Schaltfläche um den letzten Punkt rückgängig machen.
-   Drücke **Esc** oder die {{button/de|Schliessen}} Taste, um den aktuellen Befehl abzubrechen; bereits platzierte Liniensegmente bleiben erhalten.


</div>

## Verbinden

### Anwendung 

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.

## Hinweise


<div class="mw-translate-fuzzy">

Der Draht kann nach doppelklicken auf das Element in der Baumansicht oder durch drücken der Taste **<img src="images/Draft_Edit.svg" width=16px> [Entwurf Bearbeiten](Draft_Edit/de.md)** geändert werden. Dann kannst Du die Punkte an eine neue Position verschieben oder **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** oder **<img src="images/Draft_DelPoint.svg" width=16px> [Punkt entfernen](Draft_DelPoint/de.md)** und dann den Draht anklicken, um Punkte hinzuzufügen oder zu entfernen.


</div>

## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen zu ändern, die bei der Eingabe von Koordinaten verwendet werden: **Bearbeiten → Einstellungen... → Allgemein → Einheiten → Einheiteneinstellungen → Anzahl der Dezimalstellen**.
-   Um den Anfangswert des Füllmodus zu ändern: **Bearbeiten → Einstellungen... → Entwurf → Allgemeine Einstellungen → Entwurf Werkzeuge Optionen → Objekte mit Flächen füllen, wann immer möglich**. Ändern des Füllmodus in einem Aufgabenpaneel, wird diese Voreinstellung für die aktuelle FreeCAD Sitzung überschreiben.

## Eigenschaften


<div class="mw-translate-fuzzy">

Siehe auch: [Eigenschafteneditor](property_editor/de.md).


</div>

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Daten


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Start**: spezifiziert den ersten Punkt im Draht.

-    **Ende**: spezifiziert den letzten Punkt im Draht, wobei der Anfangspunkt nicht mitgezählt wird, wenn der Draht geschlossen wird.

-    **Geschlossen**: spezifiziert, ob der Draht geschlossen ist oder nicht. Wenn der Draht ursprünglich offen ist, ist dieser Wert `False`; ihn auf `True` setzen, wird ein Liniensegment zeichnen, um den Draht zu schließen. Wenn der Draht ursprünglich geschlossen ist, ist dieser Wert `True`; ihn auf `False` setzen, wird das letzte Liniensegment entfernen, und der Draht wird geöffnet.

-    **Fasengröße**: gibt die Größe der Fasen (gerade Abschnitte) an, die an den Ecken des Drahtes erzeugt werden.

-    {{PropertyData/de|Verrundungsradius}}: gibt den Radius der Verrundungen (Bogenabschnitte) an, die an den Ecken des Drahtes erzeugt werden.

-    **Erstelle Fläche**: gibt an, ob der Draht eine Fläche bildet oder nicht. Wenn es `True` ist, wird eine Fläche erzeugt, andernfalls werden nur die Kanten als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn **Geschlossen** `True` ist.

:   
    **Hinweis:**setze **Erstelle Fläche** nicht auf `True`, wenn der Draht sich selbst überkreuzt, da er keine ordnungsgemäße Fläche erzeugt.

-    **Unterteilungen**: gibt die Anzahl der innen liegenden Knoten in jedem Abschnitt des Drahtes an. {{version/de|0.16}}

-    **Länge**: (nur-lesen) gibt die Länge des gesamten Drahtes an.


</div>

### Ansicht


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Endpfeil**: wenn es `True` ist, wird ein Symbol am letzten Punkt des Drahtes angezeigt, so dass es als Anmerkungslinie verwendet werden kann.

-    **Pfeilgröße**: gibt die Größe des am Ende des Drahtes angezeigten Symbols an.

-    **Pfeiltyp**: gibt den Typ des am Ende des Drahtes angezeigten Symbols an, der \"Punkt\", \"Kreis\", \"Pfeil\" oder \"Kreuz\" sein kann.

-    **Muster**: spezifiziert ein [Entwurfsmuster](Draft_Pattern.md), mit dem die Fläche des geschlossenen Drahtes ausgefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn **Erstelle Fläche** `True` ist und wenn **Anzeigemodus** \"Ebene Linien\" ist.

-    **Mustergröße**: gibt die Größe des [Entwurfsmuster](Draft_Pattern/de.md) an.


</div>

## Skripten

Siehe auch: _.


<div class="mw-translate-fuzzy">

Das Drahtwerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden:


</div>


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Erzeugt ein `Draht` Objekt mit der angegebenen Liste von Punkten, `Punktliste`.
    -   Jeder Punkt in der Liste wird durch seinen `FreeCAD.Vector` definiert, mit Einheiten in Millimetern.
    -   Alternativ kann die Eingabe ein `Part.Wire` sein, aus dem die Punkte extrahiert werden.
-   Wenn `closed` `True` ist, oder wenn der erste und letzte Punkt identisch sind, wird der Draht geschlossen.
-   Wenn ein `placement` angegeben wird, wird dieser verwendet; andernfalls wird die Form am Ursprung erzeugt.
-   Wenn `Fläche` `True` ist und der Draht geschlossen ist, wird der Draht eine Fläche bilden, d.h. er wird gefüllt erscheinen.


</div>

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/de
