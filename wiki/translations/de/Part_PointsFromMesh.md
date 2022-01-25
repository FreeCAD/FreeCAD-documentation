---
- GuiCommand:/de
   Name:Part PointsFromMesh‎
   Name/de:Part PunkteAusNetz
   MenuLocation:Part → Erzeuge Punktobjekt aus Netz
   Workbenches:[Arbeitsbereich Part](Part_Workbench/de.md)
   Version:0.19
   SeeAlso:[Part FormausNetz](Part_ShapeFromMesh/de.md), [Part KonvertiereZuFestkörper](Part_MakeSolid/de.md), [Part FormVerfeinern](Part_RefineShape/de.md)
---

# Part PointsFromMesh/de

## Beschreibung

Das **<img src="images/Part_PointsFromMesh.svg" width=16px>
[Part PunkteAusNetz](Part_PointsFromMesh/de.md)** Werkzeug erzeugt eine Form, die von einem [Netz Objekt](Glossary/de#Mesh.md) ausgeht, das aus der [Netz Arbeitsbereich](Mesh_Workbench/de.md) importiert oder erzeugt wurde.

Die resultierende Form ist eine Sammlung von Knoten oder Punkten, die als Referenz für die weitere Erstellung von Linien, Skizzen und Flächen mit anderen Werkzeugen, wie denen aus der **<img src="images/Workbench_Sketcher.svg" width=16px>
[Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md)** oder der **<img src="images/Workbench_Draft.svg" width=16px> [Entwurf Arbeitsbereich](Draft_Workbench/de.md)** verwendet werden können.

## Anwendung

1.  Wähle das Netzobjekt aus.
2.  Gehe zu **Teil → <img src="images/Part_PointsFromMesh.svg" width=24px> Erzeuge Punktobjekt aus Netz**.
3.  Eine Form aus dem Netzobjekt wird als separates neues Objekt erstellt.

Es wird keine Analyse oder Validierung des Netzobjekts durchgeführt. Die Analyse und Reparatur des Netzes sollte bei Bedarf manuell vor der Konvertierung durchgeführt werden. Entsprechende Werkzeuge sind in der **<img src="images/Workbench_Mesh.svg" width=24px>[Netz Arbeitsbereich](Mesh_Workbench/de.md)** verfügbar.

## Hinweise

## Eigenschaften

## Begrenzungen

## Skripten



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part PointsFromMesh/de
