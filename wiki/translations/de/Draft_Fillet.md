---
 GuiCommand:
   Name: Draft Fillet
   Name/de: Draft Verrundung
   MenuLocation: Zeichnen , Verrundung
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

1.  Zwei [Draft Linien](Draft_Line/de.md) auswählen, die sich in einem einzelnen Punkt treffen.

2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Fillet.svg" width=16px> [Verrundung](Draft_Fillet/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Fillet.svg" width=16px> Verrundung** auswählen.
    -   Das Tastaturkürzel **F** dann **I**.

3.  Den **Abrundungsradius** eingeben. Ist die Option **Fase erstellen** ausgewählt, wird er als Größe der Fase verwendet (die Länge der geraden Kante). Achtung, der Befehl kann nicht erfolgreich abgeschlossen werden, wenn der Radius bzw. die Fase zu groß für die ausgewählten Linien ist.

4.  Wahlweise die Option **Originalobjekte löschen** aktivieren.

5.  Wahlweise die Option **Fase erstellen** aktivieren.

6.  Wurden eine oder beide der vorherigen Optionen ausgewählt: In das Eingabefeld **Abrundungsradius** klicken.

7.  
    **Enter**drücken.



## Optionen

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Eine Draft Verrundung kann nicht bearbeitet werden und ist auch nicht mit den Linien verknüpft, die zu ihrer Erstellung verwendet wurden.
-   Nur Draft-Linien, also [Draft Polylinien](Draft_Wire/de.md) mit nur zwei Punkten werden zurzeit unterstützt.
-   Eine [Draft Polylinie](Draft_Wire/de.md), die mindestens drei Punkte hat, kann verrundet oder angefast werden, indem ihre {{PropertyData/de|Fillet Radius}} bzw. {{PropertyData/de|Chamfer Size}} geändert wird. Da [Draft Linien](Draft_Line/de.md) und [Draft Polylinien](Draft_Wire/de.md) mit den Befehlen [Draft Polylinie](Draft_Wire/de.md), [Draft Verbinden](Draft_Join/de.md) oder [Draft Hochstufen](Draft_Upgrade/de.md) verbunden werden können, stellt dies eine alternative Methode zur Erstellung von Verrundungen und Fasen dar.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Verrundungs-Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|End|VectorDistance}}: (schreibgeschützt) gibt den Endpunkt der Verrundung an.

-    {{PropertyData/de|Fillet Radius|Length}}: (schreibgeschützt) Radius, mit dem die Verrundung erstellt wurde.

-    {{PropertyData/de|Length|Length}}: (schreibgeschützt) gibt die Gesamtlänge der Verrundung an.

-    {{PropertyData/de|Start|VectorDistance}}: (schreibgeschützt) gibt den Startpunkt der Verrundung an.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Arrow Size|Length}}: Gibt die Größe des Symbols an, das am Ende der Verrundung angezeigt wird.

-    {{PropertyView/de|Arrow Type|Enumeration}}: Gibt den Typ des Symbols an, das am Ende der Verrundung angezeigt wird und die Werte {{value|Punkt}} (Dot), {{value|Kreis}} (Circle), {{value|Pfeil}} (Arrow), {{value|Schrägstrich}} (Tick) oder {{value|Schrägstrich-2}} annehmen kann.

-    {{PropertyView/de|End Arrow|Bool}}: Gibt an, ob am Ende der Verrundung ein Symbol angezeigt wird, damit es als Maßlinie verwendet werden kann.

-    {{PropertyView/de|Pattern|Enumeration}}: wird nicht verwendet.

-    {{PropertyView/de|Pattern Size|Float}}: wird nicht verwendet.



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
