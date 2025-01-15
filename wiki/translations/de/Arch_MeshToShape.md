---
 GuiCommand:
   Name: Arch MeshToShape
   Name/de: Arch NetzZuForm
   MenuLocation: Utils , Netz in Form umwandeln
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_SplitMesh/de, Arch_RemoveShape/de
---

# Arch MeshToShape/de



## Beschreibung

Das Werkzeug [Arch NetzZuForm](Arch_MeshToShape/de.md) wandelt ein gewähltes [Netz](Mesh/de.md)-Objekt ([Mesh Formelement](Mesh_Feature/de.md)) in ein [Form](Shape/de.md)-Objekt ([Part Formelement](Part_Feature/de.md)) um.

Dieses Werkzeug ist für Objekte mit ebenen Flächen (keine Kurven) optimiert. Das entsprechende Werkzeug **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part FormAusNetz](Part_ShapeFromMesh.md)** aus dem Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/de.md) ist möglicherweise besser für Objekte geeignet, die gekrümmte Oberflächen enthalten.



## Anwendung

1.  Ein Netzobjekt auswählen.
2.  Den Menüeintrag **Utils → <img src="images/Arch_MeshToShape.svg" width=16px> Netz in Form umwandeln** auswählen.



## Eigenschaften



## Einschränkungen



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden:


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

Der obige Codeschnipsel wandelt das gegebene `obj` (ein Netz) in eine Form um und verbindet dabei komplanare Facetten.

-   Wenn `mark` `True` ist, werden nicht-mannigfaltige Objekte rot markiert (z.B. nicht geschlossene Netze, aus denen keine Festkörper erstellt werden können).

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
⏵ [documentation index](../README.md) > Arch MeshToShape/de
