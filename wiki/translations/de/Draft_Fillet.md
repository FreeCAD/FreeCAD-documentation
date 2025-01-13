---
 GuiCommand:
   Name: Draft Fillet
   Name/de: Draft Verrundung
   MenuLocation: Zeichnen , Verrundung<br>2D-Entwurf , Verrundung
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **F** **I**
   Version: 0.19
   SeeAlso: Draft_Line/de, Draft_Wire/de
---

# Draft Fillet/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Fillet.svg  style="width:24px;"> **Draft Verrundung** erstellt eine Verrundung (eine abgerundete Ecke) oder eine Fase (eine gerade Kante) zwischen zwei ausgewählten Kanten.

In {{VersionMinus/de|0.21}} funktioniert der Befehl nur dann richtig, wenn beide ausgewählte Kanten gerade sind.

In {{VersionMinus/de|1.0}}, wenn die ausgewählten Objekte mehrere Kanten besitzen, wird ihre erste Kante verwendet. Dies muss nicht die Kante sein, die in der [3D-Ansicht](3D_view/de.md) ausgewählt wurde.

<img alt="" src=images/Draft_Fillet_example.png  style="width:400px;"> 
*Mehrere Verrundungen und Fasen, die zwischen zwei Kanten erstellt wurden*



## Anwendung

1.  Zwei Kanten auswählen, die sich in einem einzelnen Punkt treffen. Siehe [Hinweise](#Hinweise.md).

2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Fillet.svg" width=16px> [Verrundung](Draft_Fillet/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → <img src="images/Draft_Fillet.svg" width=16px> Verrundung** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_Fillet.svg" width=16px> Verrundung** auswählen.
    -   Das Tastaturkürzel **F** dann **I**.

3.  Den **Fillet radius** (Abrundungsradius) eingeben. Achtung, der Befehl kann nicht erfolgreich abgeschlossen werden, wenn der Radius bzw. die Fase zu groß für die ausgewählten Kantenobjekte ist.

4.  Wahlweise die Option **Originalobjekte löschen** aktivieren.

5.  Wahlweise die Option **Fase erstellen** aktivieren.

6.  Wurden eine oder beide der vorherigen Optionen ausgewählt: In das Eingabefeld **Abrundungsradius** klicken.

7.  
    **Enter**drücken.



## Optionen

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Eine Draft-Verrundung kann nicht bearbeitet werden und ist auch nicht mit den Kanten verknüpft, die zu ihrer Erstellung verwendet wurden.
-   Ein [Draft-Linienzug](Draft_Wire/de.md), der mindestens drei Punkte besitzt, kann verrundet oder angefast werden, indem seine {{PropertyData/de|Fillet Radius}} bzw. {{PropertyData/de|Chamfer Size}} geändert wird. Da [Draft-Linien](Draft_Line/de.md) und [Draft-Linienzüge](Draft_Wire/de.md) mit den Befehlen [Draft Linienzug](Draft_Wire/de.md), [Draft Verbinden](Draft_Join/de.md) oder [Draft Hochstufen](Draft_Upgrade/de.md) verbunden werden können, stellt dies eine alternative Methode zur Erstellung von Verrundungen und Fasen dar.



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

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Verrundung wird die Methode `make_fillet` des Draft-Moduls verwendet:


```python
fillet = make_fillet([edge1, edge2], radius=100, chamfer=False, delete=False)
```

-   Erzeugt ein `Fillet` Objekt zwischen den Kantenobjekten `edge1` und `edge2`, wobei `radius` die Krümmung festlegt.
-   Ist `chamfer` `True`, wird eine gerade Kante mit der Länge von `radius` erstellt, anstatt einer abgerundeten Kante.
-   Ist `delete` `True`, werden die angegebenen `edge1` und `edge2` gelöscht, und nur das neue Objekt bleibt übrig.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

edge1 = Draft.make_line(p1, p2)
edge2 = Draft.make_line(p2, p3)

doc.recompute()

fillet = Draft.make_fillet([edge1, edge2], radius=500)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Fillet/de
