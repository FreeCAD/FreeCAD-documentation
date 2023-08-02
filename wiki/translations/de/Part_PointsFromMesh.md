---
- GuiCommand:
   Name: Part PointsFromMesh‎
   Name/de: Part PunkteAusGeometrie
   MenuLocation: Part -> Punktobjekt aus Geometrie erstellen
   Workbenches: Part_Workbench/de
   Version: 0.19
   SeeAlso: Part_ShapeFromMesh/de, Part_MakeSolid/de, Part_RefineShape/de
---

# Part PointsFromMesh/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Part_PointsFromMesh.svg  style="width:24px;"> [Part PunkteAusGeometrie](Part_PointsFromMesh/de.md) erzeugt ein Punktobjekt aus einem geometrischen Objekt. In {{VersionMinus/de|0.20}} muss das Basisobjekt ein Netzobjekt sein, in späteren Versionen kann jedes geometrische Objekt ausgewählt werden.

Die resultierende Form ist ein Verbund aus Knoten, der als Referenz verwendet werden kann für das weitere Erstellen von Linien, Skizzen und Flächen mit anderen Werkzeugen, wie denen aus den Arbeitsbereichen <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md) oder <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/de.md).



## Anwendung

1.  Ein Netzobjekt auswählen.
2.  Den Menüeintrag **Part → <img src="images/Part_PointsFromMesh.svg" width=24px> Punktobjekt aus Geometrie erstellen** auswählen.
3.  Der Dialog **Distance in parameter space** wird geöffnet.
4.  Einen Wert für den Abstand eingeben.
5.  Die Schaltfläche **OK** drücken.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part PointsFromMesh/de
