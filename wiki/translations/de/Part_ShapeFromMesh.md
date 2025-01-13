---
 GuiCommand:
   Name: Part ShapeFromMesh‏‎
   Name/de: Part FormAusNetz
   MenuLocation: Part , Form aus Dreiecksnetz erstellen...
   Workbenches: Part_Workbench/de
   SeeAlso: Part_MakeSolid/de, Part_RefineShape/de, Part_PointsFromMesh/de
---

# Part ShapeFromMesh/de



## Einleitung

Der Befehl **<img src="images/Part_ShapeFromMesh.svg" width=24px> [Part FormAusNetz](Part_ShapeFromMesh/de.md)** erzeugt eine Form aus einem [Netzobjekt](Mesh/de.md). Netzobjekte haben in FreeCAD nur begrenzte Bearbeitungsmöglichkeiten, ihre Konvertierung in [Formen](Shape/de.md) ermöglicht ihre Verwendung mit booleschen Verknüpfungen und vielen weiteren Bearbeitungsbefehlen.

Der umgekehrte Vorgang wird mit <img alt="" src=images/Mesh_FromPartShape.svg  style="width:16px;"> [Mesh NetzAusPartForm](Mesh_FromPartShape/de.md) aus dem Arbeitsbereich <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh](Mesh_Workbench/de.md) ausgeführt.



## Anwendung

1.  Das Analysieren und Reparieren der Netzobjekte sollte, wenn erforderlich, bevor dieser Befehl gestartet wird. Geeignete Werkzeuge für diese Aufgabe findet man im Arbeitsbereich <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh](Mesh_Workbench/de.md).
2.  Ein oder mehrere Netzobjekte auswählen.
3.  Den Menüeintrag **Part → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Form aus Dreiecksnetz erstellen** auswählen.
4.  Das Dialogfenster **Form aus Netz** wird geöffnet.
5.  Wahlweise die Checkbox **Form nähen** aktivieren und eine Toleranz festlegen:
    -   Diese Option wird normalerweise nicht gebraucht. Sie ist für Netzobjekte vorgesehen, die nicht wasserdicht sind und kleine Lücken zwischen Kanten aufweisen.
    -   Ist die Option ausgewählt, wird ein Verbund von Hüllen anstatt eines Verbundes von Flächen erstellt.
    -   Der Vorgang des Vernähens kann eine hohe Rechenleistung erfordern.
6.  Die Schaltfläche **OK** drücken.
7.  Zu jedem ausgewählten Netzobjekt wird eine [Form](Shape/de.md) (Shape object) als separates neues Objekt erstellt.
8.  Wahlweise <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Part FormAufbereiten](Part_RefineShape/de.md) auf diese Objekte anwenden.
9.  Wahlweise die endgültigen Objekte mit <img alt="" src=images/Part_MakeSolid.svg  style="width:16px;"> [Part FestkörperErstellen](Part_MakeSolid/de.md) in Festkörper umwandeln.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Der Befehl Part ShapeFromMesh erstellt [Part Formelemente](Part_Feature/de.md) ohne weitere Eigenschaften.



## Skripten

Das Erstellen einer [Form](Shape/de.md) aus einem [Netz](Mesh/de.md) kann mit der Methode `makeShapeFromMesh` aus einem [Part TopoShape](Part_TopoShape/de.md)-Objekt erfolgen; es muss das Quellnetz und die Toleranz angegeben sowie das Ergebnis einem neuen [Part Formelement](Part_Feature/de.md) (Feature object) zuweisen werde.

Man beachte, dass das Netz neu berechnet werden muss, bevor es in eine Form umgewandelt wird, andernfalls würden die Topologieinformationen fehlen und die Umwandlung könnte nicht erfolgreich durchgeführt werden.


```python
import FreeCAD as App
import Part

doc = App.ActiveDocument
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid = doc.addObject("Part::Feature", "Solid")
solid.Shape = Part.Solid(shape.removeSplitter())
solid.Placement.Base = App.Vector(15, 0, 0)
doc.recompute()
```



## Verweise

-   [Bearbeite STL Dateien in FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) Video von AllVisuals4U.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/de
