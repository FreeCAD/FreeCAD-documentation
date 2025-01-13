---
 GuiCommand:
   Name: Draft Mirror
   Name/de: Draft Spiegeln
   MenuLocation: Änderung , Spiegeln<br>Bearbeiten , Spiegeln
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **M** **I**
   SeeAlso: Draft_Clone/de
---

# Draft Mirror/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Mirror.svg  style="width:24px;"> **Draft Spiegeln** erstellt gespiegelte Kopien, [Part-Mirror](Part_Mirror/de.md)-Objekte, von ausgewählten Objekten. Ein [Part-Mirror](Part_Mirror/de.md)-Objekt ist parametrisch, d.h. es aktualisiert sich, wenn sich sein Quellobjekt ändert.

Der Befehl kann auf 2D-Objekte angewendet werden, die im Arbeitsbereich [Draft](Draft_Workbench/de.md) oder im Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch auf viele 3D-Objekte, wie jene, die in den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;"> 
* Ein Objekt Spiegeln*



## Anwendung

Siehe auch: [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Mirror.svg" width=16px> [Spiegeln](Draft_Mirror/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → <img src="images/Draft_Mirror.svg" width=16px> Spiegeln** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_Mirror.svg" width=16px> Spiegeln** auswählen.
    -   Das Tastaturkürzel **M** dann **I**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgaben-Bereich **Spiegeln** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Den ersten Punkt der Spiegelebene in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
6.  Den zweiten Punkt der Spiegelebene in der [3D Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
7.  Die Spiegelebene wird durch die ausgewählten Punkte und die Normale der [Draft-Arbeitsebene](Draft_SelectPlane/de.md) definiert.



## Optionen

Die im Aufgaben-Bereich verfügbaren Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.

-   Um die Koordinaten des Basispunktes von Hand einzugeben, gib die X, Y und Z Komponenten ein und drücke nach jeder **Enter**. Oder du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** Schaltfläche betätigen sobald du die gewünschten Werte hast. Es ist ratsam den Zeiger vor der Eingabe der Koordinaten aus der [3D Ansicht](3D_view/de.md) heraus zu bewegen.
-   Drücke **R** oder wähle das **Relative** Optionsfeld um in den relativ Modus umzuschalten. Wenn der relativ Modus aktiv ist, dann sind die Koordinaten des zweiten Punktes relativ zu denen des ersten Punktes, sonst sind sie relativ zum Ursprung des Koordinatensystems
-   Drücke **G** oder wähle das **Global** Optionsfeld um den globalen Modus umzuschalten. Wenn der Global Modus aktiv ist, dann sind die Koordinaten relativ zum globalen Koordinatensystem, sonst sind sie relativ zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).
-   Drücke **S** um [Draft Einrasten](Draft_Snap/de.md) ein oder auszuschalten.
-   Drücke **Esc** oder die **Abbrechen** Schaltfläche um den Befehl abzubrechen.



## Hinweise

-   Gespiegelte Kopien von [Draft Linie](Draft_Line/de.md), [Draft Linienzug](Draft_Wire/de.md), [Draft Bogen](Draft_Arc/de.md) und [Draft Kreis](Draft_Circle/de.md) können durch Verwenden von [ Herabstufen](Draft_Downgrade/de.md) in unabhängig editierbare Draft Objekte verwandelt werden und dann [Draft Hochstufen](Draft_Upgrade/de.md).
-   Der Befehl [Part EinfacheKopie](Part_SimpleCopy/de.md) kann verwendet werden, um eine Kopie eines gespiegelten Objektes zu erzeugen, die nicht mit dem Ursprungsobjekt verbunden ist



## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Ein [Part Mirror](Part_Mirror.md)-Objekt ist von einem [Part Feature](Part_Feature.md)-Objekt abgeleitet und erbt alle Eigenschaften. Es besitzt zusätzlich folgende Eigenschaften:



### Daten


{{TitleProperty|Base}}

-    **Source|Link**: nennt das gespiegelte Objekt.


{{TitleProperty|Plane}}

-    **Base|Vector**: bezeichnet den Ursprung der Spiegelfläche.

-    **Normal|Vector**: bezeichnet die Normale auf die Spiegelfläche.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Spiegeln von Objekten wird die Methode `mirror` des Draft-Moduls verwendet.


```python
mirrored_list = mirror(objlist, p1, p2)
```

-    `objlist`enthält die Objekte die gespiegelt werden sollen. Entweder ein einzelnes Objekt oder eine Liste von Objekten.

-    `p1`ist der erste Punkt der Spiegelebene.

-    `p2`ist der zweite Punkt der Spiegelebene.

-   Wenn [Draft EbeneAuswählen](Draft_SelectPlane/de.md) vorhanden ist, dann wird der Anschluss der Spiegelebene durch ihre Normale festgelegt, sonst wird die Blickrichtung der Kamera in der aktiven [3D Ansicht](3D_view/de.md) verwendet. Wenn keine graphische Schnittstelle vorhanden ist, dann wird die Z Achse verwendet.

-    `mirrored_list`wird mit den neuen `Part::Mirroring` Objekten zurückgegeben. Ist abhängig von `objlist` entweder ein einzelnes Objekt oder eine Liste von Objekten.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(FreeCAD.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

p1 = App.Vector(2000, -1000, 0)
p2 = App.Vector(2000, 1000, 0)

line1 = Draft.make_line(p1, p2)
mirrored1 = Draft.mirror(polygon1, p1, p2)

Line2 = Draft.make_line(-p1, -p2)
mirrored2 = Draft.mirror([polygon1, polygon2], -p1, -p2)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Mirror/de
