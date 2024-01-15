---
 GuiCommand:
   Name: Draft Mirror
   Name/de: Draft Spiegeln
   MenuLocation: Änderung , Spiegeln
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **M** **I**
   SeeAlso: Draft_Clone/de
---

# Draft Mirror/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Mirror.svg  style="width:24px;"> **Draft Spiegeln** erstellt gespiegelte Kopien, [Part-Mirror](Part_Mirror/de.md)-Objekte, von ausgewählten Objekten. Ein [Part-Mirror](Part_Mirror/de.md)-Objekt ist parametrisch, d.h. es aktualisiert sich, wenn sich sein Quellobjekt ändert.

Der Befehl kann auf 2D-Objekte angewendet werden, die im Arbeitsbereich [Draft](Draft_Workbench/de.md) oder im Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch auf viele 3D-Objekte, wie jene, die in den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;"> 
* Ein Objekt Spiegeln*



## Anwendung

Siehe auch: [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Mirror.svg" width=16px> [Spiegeln](Draft_Mirror/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Mirror.svg" width=16px> Spiegeln** auswählen.
    -   Das Tastaturkürzel **M** dann **I**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgaben-Bereich **Spiegeln** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Den ersten Punkt der Spiegelebene in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
6.  Den zweiten Punkt der Spiegelebene in der [3D Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
7.  Die Spiegelebene wird durch die ausgewählten Punkte und die Normale der [Draft-Arbeitsebene](Draft_SelectPlane/de.md) definiert.



## Optionen

Die im Aufgaben-Bereich verfügbaren Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, the coordinates of the second point are relative to the first point, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.



## Hinweise

-   Mirrored copies of [Draft Lines](Draft_Line.md), [Draft Wires](Draft_Wire.md), [Draft Arcs](Draft_Arc.md) and [Draft Circles](Draft_Circle.md) can be turned into independent editable Draft objects by using [Draft Downgrade](Draft_Downgrade.md) and then [Draft Upgrade](Draft_Upgrade.md).
-   The [Part SimpleCopy](Part_SimpleCopy.md) command can be used to create a copy of a mirrored object that is not linked to its source object.



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

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Spiegeln von Objekten wird die Methode `mirror` des Draft-Moduls verwendet.


```python
mirrored_list = mirror(objlist, p1, p2)
```

-    `objlist`contains the objects to be mirrored. It is either a single object or a list of objects.

-    `p1`is the first point of the mirror plane.

-    `p2`is the second point of the mirror plane.

-   If the [Draft working plane](Draft_SelectPlane.md) is available the alignment of the mirror plane is determined by its normal, else the view direction of the camera in the active [3D view](3D_view.md) is used. If the graphical interface is not available the Z axis is used.

-    `mirrored_list`is returned with the new `Part::Mirroring` objects. It is either a single object or a list of objects, depending on `objlist`.

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
