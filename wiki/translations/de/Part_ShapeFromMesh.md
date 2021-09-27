---
- GuiCommand:/de
   Name:Part ShapeFromMesh‏‎
   Name/de:Part FormAusNetz
   MenuLocation:Part → Erzeuge Form aus Netz...
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part UmwandelnInFestkörper](Part_MakeSolid/de.md), [Part FormVerfeinern](Part_RefineShape/de.md), [Part PunkteAusNetz](Part_PointsFromMesh/de.md)
---

# Part ShapeFromMesh/de

## Einführung

Der **<img src="images/Part_ShapeFromMesh.svg" width=16px> [Part FormAusNetz](Part_ShapeFromMesh/de.md)** Befehl erzeugt eine Form aus einem [Netzobjekt](Mesh/de.md). Netzobjekte haben in FreeCAD nur begrenzte Bearbeitungsmöglichkeiten, ihre Konvertierung in [Formen](Shape/de.md) ermöglicht ihre Verwendung mit vielen weiteren Booleschen und Modifikationswerkzeugen.

Die Umkehroperation ist **<img src=images/Mesh_FromPartShape.svg style="width:16px"> _.

## Anwendung

1.  Wähle das Netzobjekt in der [Baumansicht](tree_view/de.md) aus.
2.  Gehe zum Menü, **Part → <img src=images/Part_ShapeFromMesh.svg style="width:16px"> Erzeuge Form aus Netz**.
3.  Ein Aufklappmenü fragt nach der Toleranz für das Nähen der Form; der Standardwert ist {{Value|0.1}}.
4.  Eine [Form](Shape/de.md) aus dem Netzobjekt wird als separates neues Objekt erstellt.

Die Analyse und Reparatur des Netzes sollte, falls erforderlich, vor dem Start manuell durchgeführt werden **<img src=images/Part_ShapeFromMesh.svg style="width:16px"> _ verfügbar.

Nach der Erstellung einer <img src=images/Part_RefineShape.svg style="width:Form](Shape/de.md), kann es nützlich sein, **[Umwandeln in Festkörper](Part_MakeSolid/de.md)** (erforderlich für [boolesche Operationen](Part_Boolean/de.md)) und **[16px"> [Form verfeinern](Part_RefineShape/de.md)**.

## Verweise

-   [Bearbeite STL Dateien in FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) Video von AllVisuals4U.

## Skripten

Das Erstellen einer [Form](Shape/de.md) aus einem [Netz](Mesh/de.md) kann mit der Methode `makeShapeFromMesh` aus einem [Part TopoForm](Part_TopoShape/de.md) erfolgen; Du musst das Quellnetz und die Toleranz angeben und das Ergebnis einem neuen [Part Formelement](Part_Feature/de.md) Objekt zuweisen.

Beachte, dass das Netz neu berechnet werden muss, bevor es in eine Form umgewandelt wird, da es sonst keine Topologieinformationen gibt und die Umwandlung nicht erfolgreich ist.


```python
import FreeCAD as App
import Part

doc = App.newDocument()
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

solid = doc.addObject("Part::Feature", "Shape")
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid.Shape = shape
solid.Placement.Base = App.Vector(15, 0, 0)
solid.purgeTouched()
doc.recompute()
```

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/de
