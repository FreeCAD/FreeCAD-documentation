---
- GuiCommand:
   Name:Draft Clone
   Name/de:Draft Klonen
   MenuLocation:Änderung → Klonen
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**C** **L**
   SeeAlso:[Draft Skalieren](Draft_Scale/de.md)
---

# Draft Clone/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> **Draft Klonen** erstellt verknüpfte Kopien, Klone von ausgewählten Objekten. Die Form eines Klons ist parametrisch; er wird aktualisiert, wenn sich sein Quellobjekt ändert. Aber ein Klon hat seine eigene Position, Ausrichtung und Skalierung sowie seine eigenen [Ansicht-Eigenschaften](Property_editor/de.md). Für [Arch](Arch_Workbench/de.md)-Objekte erstellt der Befehl eine besondere Art von Klon: einen Arch-Klon.

Der Befehl kann auf 2D-Objekte angewendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erzeugt wurden, aber auch auf viele 3D-Objekte, wie solchen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erzeugt wurden. Klone von 2D-Objekten können in [PartDesign-Körpern](PartDesign_Body/de.md) verwendet werden.

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;"> 
*Draft-Klon neben dem Quellobjekt*



## Anwendung

1.  Wahlweise ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Clone.svg" width=16px> [Klonen](Draft_Clone/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Clone.svg" width=16px> Klonen** auswählen.
    -   Das Tastaturkürzel **C** dann **L**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Ein mit dem Befehl Draft Klonen erzeugtes Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md), einem [Part-Formelement](Part_Feature/de.md)-Objekt oder, wenn ein Arch-Klon erstellt wird, vom Objekttyp des Quellobjekts abgeleitet. Er erbt alle Eigenschaften dieses Objekts. Ein Klon, der von einem der ersten beiden Objekte abgeleitet wurde, hat außerdem die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    **Fuse|Bool**: gibt an, ob überlappende Formen im Klon vereinigt werden oder nicht.

-    **Objects|LinkListGlobal**: legt die Objekte fest, die geklont werden.

-    **Scale|Vector**: Legt die Skalierungsfaktoren für X, Y und Z fest.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um einen Klon zu erstellen, wird die Methode `make_clone` ({{Version/de|0.19}}) des Moduls Draft verwendet. Diese Methode ersetzt die veraltete Methode `clone`.


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```

-    `obj`enthält die zu klonenden Objekte. Es ist entweder ein einzelnes Objekt oder eine Liste von Objekten.

-    `delta`ist der Verschiebungsvektor, der auf den Klon angewendet wird.

-   Wenn `forcedraft` `False` ist und `obj` ein einzelnes [Arch- Objekt](Arch_Workbench/de.md) enthält, wird ein Arch-Klon erstellt. `forcedraft` auf `True` setzen, um stattdessen einen Draft-Klon zu erstellen.

-    `cloned_object`wird mit dem Klon-Objekt zurückgegeben.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/de
