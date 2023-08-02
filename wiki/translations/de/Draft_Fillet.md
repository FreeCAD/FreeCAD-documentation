---
- GuiCommand:
   Name: Draft Fillet
   Name/de: Draft Verrundung
   MenuLocation: Entwurf -> Verrundung
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **F** **I**
   Version: 0.19
   SeeAlso: Draft_Line/de, Draft_Wire/de
---

# Draft Fillet/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Fillet.svg  style="width:24px;"> **Draft Verrundung** erstellt eine Verrundung (eine abgerundete Ecke) oder eine Fase (eine gerade Kante zwischen zwei [Draft Linien](Draft_Line/de.md)).

<img alt="" src=images/Draft_Fillet_example.png  style="width:400px;"> 
*Mehrere Verrundungen und Fasen, die zwischen zwei Linien erstellt wurden*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle zwei [Entwurf Linie](Draft_Line/de.md), die bereits auf dem Dokument platziert sind und sich an einem Punkt treffen.
2.  Drücke die Taste **<img src="images/Draft_Fillet.svg" width=16px> [Entwurf Verrundung](Draft_Fillet/de.md)** Taste.
3.  Wähle den Radius der Verrundung und drücke dann **Enter**.


</div>



## Optionen

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Anmerkungen


<div class="mw-translate-fuzzy">

-   Das resultierende Verrundungsobjekt ist nicht editierbar.
-   Wenn der Radius zu groß ist, als dass der erzeugte Bogen nicht zu einer der Linien tangiert wäre, wird der Vorgang nicht erfolgreich sein.
-   Im Moment werden nur einzelne Linien unterstützt; [Draft Wires](Draft_Wire/de.md), d.h. Linien mit mehreren Punkten, führen möglicherweise nicht zum gewünschten Ergebnis.


</div>



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Verrundungs-Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



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

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Verrundung wird die Methode `make_fillet` des Draft-Moduls verwendet:


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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Fillet/de
