# Mesh/de
## Einleitung

In FreeCAD wird das Wort \"[Polygonnetz](Mesh/de.md)\" (kurz Netz) normalerweise verwendet, um sich auf ein [Mesh Netzobjekt](Mesh_MeshObject/de.md) (`Mesh::MeshObject`-Klasse) zu beziehen, eine Objektart, die 3D-Daten darstellt, aber keine Festkörper-\"[Form](Shape/de.md)\" ist.

Polygonnetze sind sehr einfache Objekte, die nur Knoten (Punkte), Kanten und dreieckige Flächen enthalten. Im Allgemeinen sind sie leicht zu erstellen, bearbeiten, unterteilen und zu dehnen und können ohne Detailverlust von einer Anwendung zu einer anderen übertragen werden. Da die Netze sehr einfache Daten enthalten, können 3D-Anwendungen wie Animationssoftware und Videospiele sehr große Mengen von ihnen (Millionen von Dreiecken) ohne großen Rechenaufwand verwalten.

Im Bereich der technischen Netze gibt es jedoch eine große Einschränkung: Sie bestehen nur aus Flächen und haben keine \"Masse\"-Informationen, so dass sie sich nicht wie \"Festkörper\" verhalten. Das bedeutet, dass festkörperbasierte Verknüpfungen wie [boolesche Vereinigung oder Differenz](Part_Boolean/de.md) mit Polygonnetzen schwer durchführbar sind. Da sie außerdem durch einzelne Punkte definiert sind, lassen sie sich nur schwer auf parametrische Art beschreiben.

Siehe [Mesh Netzobjekt](Mesh_MeshObject/de.md) für weitere Informationen zu diesem Objekttyp und siehe [Polygonnetz](https://de.wikipedia.org/wiki/Polygonnetz) für allgemeine Informationen im Bereich Computersysteme.

![](images/Shape_and_mesh.svg )



*Links: parametrische [Form](Shape/de.md), definiert durch Eigenschaften. Rechts: [Polygonnetz](Mesh/de.md), definiert durch Knoten und dreieckige Oberflächen.*



## Anwendung

Polygonnetze werden normalerweise durch interne Funktionen des Arbeitsbereichs [Mesh](Mesh_Workbench/de.md) erstellt oder durch den Import von Dateien in einem Netzformat wie STL oder OBJ.

Im Wesentlichen wird von jedem Objekt, das von einem [Mesh Formelement](Mesh_Feature/de.md) (`Mesh::Feature`-Klasse) abgeleitet ist, erwartet, ein Polygonnetz zu enthalten und zu verändern.

Da FreeCAD in erster Linie als Konstruktionsprogramm für Festkörper konzipiert ist, ist es besser geeignet, mit Festkörper- [Formen](Shape/de.md) zu bearbeiten. Es kann Netze in die [3D-Ansicht](3D_view.md) importieren und der Arbeitsbereich [Mesh](Mesh_Workbench/de.md) enthält einige Befehle um sie direkt zu bearbeiten. In vielen Fällen muss das Netz aber zuerst in eine [Form](Shape/de.md) konvertiert werden (siehe [Part FormAusNetz](Part_ShapeFromMesh/de.md)) oder die Geometrie muss nachkonstruiert werden, mit Modellierungstechniken für Festkörper der Arbeitsbereiche [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md).



## Finite Element Netze 

In FreeCAD kann sich das Wort \"[Polygonnetz](Mesh/de.md)\" auch auf ein bestimmtes Objekt beziehen, das in der Finite Elemente Analyse (FEA) verwendet wird.

Wenn ein Objekt mit einer Festkörper-[Form](Shape/de.md) im Arbeitsbereich [FEM](FEM_Workbench/de.md) verwendet wird, wird es in ein Netz aus Dreiecken Netz umgewandelt. In diesem Fall ist das resultierende Objekt ein [FEM-Netzobjekt](FEM_Mesh/de.md) (`Fem::FemMeshObject`-Klasse) und ist nicht von einem [Mesh Formelement](Mesh_Feature/de.md) (`Mesh::Feature`-Klasse) abgeleitet.

Für weitere Informationen siehe Arbeitsbereich [FEM](FEM_Workbench/de.md) und [FEM Polygonnetz](FEM_Mesh/de.md).



## Weitere Informationen 

-   [Polygonale (Netz)-Geometrie](https://forum.freecadweb.org/viewtopic.php?f=8&t=47493)


{{Mesh Tools navi

}} {{FEM Tools navi}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Category_Mesh.md) > [FEM](Category_FEM.md) > Mesh/de
