---
 GuiCommand:
   Name: Draft Facebinder
   Name/de: Draft Flächenbinder
   MenuLocation: Zeichnen , Flächenverbinder
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **F** **F**
   Version: 0.14
---

# Draft Facebinder/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Facebinder.svg  style="width:24px;"> **Draft Flächenbinder** erstellt ein Oberflächenobjekt aus ausgewählten Flächen. Ein Draft-Flächenbinder ist parametrisch, er wird aktualisiert, wenn seine Quellobjekte geändert werden.

Er kann verwendet werden, um eine Extrusion aus einer Sammlung von Flächen aus anderen Objekten zu erstellen. Diese Extrusion kann zum Beispiel einen Wandabschluss in der architektonischen Gestaltung verkörpern.

<img alt="" src=images/Draft_facebinder_example.jpg  style="width:400px;"> 
*Flächenbinder erstellt aus den Wandflächen*



## Anwendung

1.  Eine oder mehrere Flächen auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Facebinder.svg" width=16px> [Flächenverbinder](Draft_Facebinder/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Facebinder.svg" width=16px> Flächenverbinder** auswählen.
    -   Das Tastaturkürzel **F** dann **F**.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Flächenbinder (Facebinder-Objekt) wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Entwurf}}

-    {{PropertyData/de|Area|Area}}: (nur-lesen) Gibt den gesamten Bereich der verbundenen Flächen des Flächenbinders an.

-    {{PropertyData/de|Extrusion|Distance}}: Gibt die Extrusionsdicke des Flächenbinders an.

-    {{PropertyData/de|Faces|LinkSubList}}: Gibt die verbundenen Flächen des Flächenbinders an.

-    {{PropertyData/de|Offset|Distance}}: Gibt eine Abstandsentfernung an, die vor der Extrusion zwischen den ursprünglichen Flächen und dem Flächenbinder bestehen soll.

-    {{PropertyData/de|Remove Splitter|Bool}}: Gibt an, ob Trennlinien (\"splitter lines\" ?) entfernt werden sollen, die auf gleicher Ebene liegende Flächen vom Flächenbinder trennen oder nicht.

-    {{PropertyData/de|Sew|Bool}}: Gibt an, ob ein topolischer Nähvorgang am Flächenbinder durchgeführt werden soll oder nicht.



### Ansicht


{{TitleProperty|Entwurf}}

-    {{PropertyView/de|Muster}}: spezifiziert ein [Entwurfs Muster](Draft_Pattern/de.md), mit dem die Fläche der Form ausgefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn {{PropertyView/de|Display Mode}} \"Flat Lines\" ist.

-    {{PropertyView/de|Muster Grösse}}: gibt die Größe des [Muster Grösse](Draft_Pattern/de.md) an.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).

Um einen Entwurf Flächenbinder zu erstellen, verwende die Methode `make_facebinder` (<small>(v0.19)</small> ) des Entwurfsmoduls. Diese Methode ersetzt die veraltete Methode `makeFacebinder`.


```python
facebinder = make_facebinder(selectionset)
```

-   Erstellt ein `facebinder` Objekt aus dem angegebenen `selectionset`, das eine Liste von `SelectionObject`en ist, wie sie von `FreeCADGui.Selection.getSelectionEx()` zurückgegeben wird. Es werden nur ausgewählte Flächen berücksichtigt.
    -   
        `selectionset`
        
        kann auch ein `PropertyLinkSubList` sein.

Eine `PropertyLinkSubList` ist eine Liste von Tupeln; jedes Tupel enthält als erstes Element ein `object`, und als zweites Element eine Liste (oder Tupel) von Zeichenketten; diese Zeichenketten zeigen die Namen der Unterelemente (Flächen) dieses Objekts an.


```python
PropertyLinkSubList = [tuple1, tuple2, tuple3, ...]
PropertyLinkSubList = [(object1, list1), (object2, list2), (object3, list3), ...]
PropertyLinkSubList = [(object1, ['Face1', 'Face4', 'Face6']), ...]
PropertyLinkSubList = [(object1, ('Face1', 'Face4', 'Face6')), ...]
```

Die Dicke des Flächenverbinders kann durch Überschreiben des Attributs `Extrusion` hinzugefügt werden; der Wert wird in Millimetern eingegeben.

Die Platzierung des Flächenverbinders kann durch Überschreiben des Attributs `Placement` oder durch individuelles Überschreiben der Attribute `Placement.Base` und `Placement.Rotation` geändert werden.

Beispiel:


```python
import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

# Insert a solid box
box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

# selection = Gui.Selection.getSelectionEx()
selection = [(box, ("Face1", "Face6"))]
facebinder = Draft.make_facebinder(selection)
facebinder.Extrusion = 50

doc.recompute()

facebinder.Placement.Base = App.Vector(1000, -1000, 100)
facebinder.ViewObject.ShapeColor = (0.99, 0.99, 0.4)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Facebinder/de
