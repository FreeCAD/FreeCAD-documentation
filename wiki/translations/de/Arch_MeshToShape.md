---
- GuiCommand:/de
   Name:Arch MeshToShape
   Name/de:Arch NetzZuForm
   MenuLocation:Arch → Dienstprogramme → Netz zu Form
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch NetzAufteilen](Arch_SplitMesh/de.md), [Arch EntferneForm](Arch_RemoveShape/de.md)
---

# Arch MeshToShape/de

## Beschreibung

[Arch NetzZuForm](Arch_MeshToShape/de.md) wandelt ein gewähltes [Polygonnetz](Mesh/de.md) ([Polygonnetz Formteil](Mesh_Feature/de.md)) Objekt in eine [Form](Shape/de.md) ([Part Formteil](Part_Feature/de.md)) Objekt.

Dieses Werkzeug ist für Objekte mit flachen Flächen (keine Kurven) optimiert. Das entsprechende Werkzeug **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part FormAusNetz](Part_ShapeFromMesh.md)** aus dem <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Arbeitsbereich](Part_Workbench/de.md) ist möglicherweise besser für Objekte geeignet, die gekrümmte Oberflächen enthalten.

## Anwendung

1.  Wähle ein Netzobjekt
2.  Drücke den **<img src="images/Arch_MeshToShape.svg" width=16px> [Netz zu Form](Arch_MeshToShape/de.md)** Eintrag in {{MenuCommand/de|Arch → Dienstprogramme → Netz zu Form}}

## Eigenschaften

## Begrenzungen

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden: 
```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

Der obige Codeschnipsel wandelt den gegebenen `obj` (ein Netz) in eine Form um, die koplanare Facetten verbindet.

-   Wenn `mark` `True` ist, werden nicht-feste Objekte rot markiert.

-   Wenn `fast` `True` ist, wird ein schnellerer Algorithmus verwendet, indem aus den Facetten eine Schale aufgebaut und dann der Splitter entfernt wird.

-    `tol`ist die Toleranz, die bei der Umwandlung von Netzsegmenten in Drähte verwendet wird.

-   Wenn `flat` `True` ist, werden die Drähte gezwungen, perfekt planar zu sein, um sicher zu sein, dass sie in Flächen umgewandelt werden können, aber dies könnte Lücken in der endgültigen Schale hinterlassen.

-   Wenn `cut` `True` ist, werden Löcher in Flächen durch Subtraktion erzeugt.

Beispiel: 
```python
import Arch, Mesh, BuildRegularGeoms

Box = FreeCAD.ActiveDocument.addObject("Mesh::Cube", "Cube")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

new_obj = Arch.meshToShape(Box)
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MeshToShape/de
