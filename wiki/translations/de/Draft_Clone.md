---
- GuiCommand:/de
   Name:Draft Clone
   Name/de:Entwurf Klonen
   MenuLocation:Änderung → Klonen
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Shortcut:**C** **L**
   SeeAlso:[Entwurf Skalieren](Draft_Scale/de.md)
---

# Draft Clone/de

## Beschreibung

Das <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> **Entwurf Klonen** Werkzeug erstellt verbundene Kopien, Klone von ausgewählten Objekten. Die Form eines Klons ist parametrisch, er wird aktualisiert, wenn sich sein Quellobjekt ändert. Aber ein Klon hat seine eigene Position, Rotation und Skalierung und seine eigenen [Ansichtseigenschaften](Property_editor/de.md). Für [Architektur](Arch_Workbench/de.md) Objekte erzeugt der Befehl einen speziellen Typ von Klon: einen Architektur Klon.

Der Befehl kann auf 2D Objekte angewendet werden, die mit dem [Arbeitsbereich Entwurf](Draft_Workbench/de.md) oder [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) erzeugt wurden, aber auch auf viele 3D Objekte, wie sie mit dem [Arbeitsbereich Part](Part_Workbench/de.md), [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md) oder [Arbeitsbereich Architektur](Arch_Workbench/de.md) erzeugt wurden. Klone von 2D Objekten können in [PartDesign Körpern](PartDesign_Body/de.md) verwendet werden.

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;"> 
*Entwurf Klon neben dem Quellobjekt*

## Anwendung

1.  Wähle optional ein oder mehrere Objekte aus.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_Clone.svg" width=16px> [Entwurf klonen](Draft_Clone/de.md)**.
    -   Wähle die Option **Änderung → <img src="images/Draft_Clone.svg" width=16px> Klonen** aus dem Menü.
    -   Verwende den Tastaturkürzel: **C** und dann **L**.
3.  Wenn du noch kein Objekt ausgewählt hadt: Wähle ein Objekt in der [3D Ansicht](3D_view/de.md).

## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Ein mit dem Befehl Entwurfsklon erzeugtes Objekt wird von einem [Part Part2DObjekt](Part_Part2DObject/de.md), einem [Part Formelement](Part_Feature/de.md) Objekt oder, wenn ein Architekturklon erzeugt wird, vom Objekttyp des Quellobjekts abgeleitet. Er erbt alle Eigenschaften von diesem Objekt. Ein Klon, der von einem der ersten beiden Objekte abgeleitet ist, hat außerdem die folgenden zusätzlichen Eigenschaften:

### Daten


{{TitleProperty|Entwurf}}

-    **Fuse|Bool**: gibt an, ob überlappende Formen im Klon verschmolzen werden oder nicht.

-    **Objects|LinkListGlobal**: legt die Objekte fest, die geklont werden.

-    **Scale|Vector**: Legt die X, Y und Z Skalierungsfaktoren fest.

## Skripten

Siehe auch: _.

Um einen Klon zu erstellen, verwende die Methode `make_clone` ({{Version/de|0.19}}) des Moduls Entwurf. Diese Methode ersetzt die veraltete Methode `clone`.


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```

-    `obj`enthält die zu klonenden Objekte. Es ist entweder ein einzelnes Objekt oder eine Liste von Objekten.

-    `delta`ist der Verschiebungsvektor, der auf den Klon angewendet werden soll.

-   Wenn `forcedraft` `False` ist und `obj` ein einzelnes [Architektur Objekt](Arch_Workbench/de.md) enthält, wird ein Architektur-Klon erzeugt. Setzen Sie `forcedraft` auf `True`, um stattdessen einen Entwurf-Klon zu erzeugen.

-    `cloned_object`wird mit dem Klonobjekt zurückgegeben.

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
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/de
