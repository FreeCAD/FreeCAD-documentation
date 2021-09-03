

## Einleitung

In FreeCAD wird das Wort \"[Polygonnetz](Mesh/de.md)\" normalerweise verwendet, um sich auf ein [Polygonnetz PolygonnetzObjekt](Mesh_MeshObject/de.md) (`Mesh::MeshObject` Klasse) zu beziehen, ein Objekttyp, der 3D Daten definiert, aber kein Volumenkörper \"[Form](Shape/de.md)\" ist.

Polygonnetze sind sehr einfache Objekte, die nur Knoten (Punkte), Kanten und dreieckige Flächen enthalten. Im Allgemeinen sind sie leicht zu erstellen, zu modifizieren, zu unterteilen und zu dehnen und können ohne Detailverlust von einer Anwendung zur anderen übertragen werden. Da die Netze sehr einfache Daten enthalten, können 3D Anwendungen wie Animationssoftware und Videospiele sehr große Mengen von ihnen (Millionen von Dreiecken) ohne großen Rechenaufwand verwalten.

Im Bereich der technischen Netze gibt es jedoch eine große Einschränkung: Sie bestehen nur aus Flächen und haben keine \"Masse\" Informationen, so dass sie sich nicht wie \"Volumenkörper\" verhalten. Das bedeutet, dass festkörperbasierte Operationen, wie [boolesche Addition oder Subtraktion](Part_Boolean/de.md), auf Polygonnetzen schwer durchführbar sind. Da sie außerdem durch einzelne Punkte definiert sind, lassen sie sich nur schwer parametrisch beschreiben.

Siehe [Polygonnetz PolygonnetzObjekt](Mesh_MeshObject/de.md) für weitere Informationen über diesen Objekttyp und siehe [Polygonnetz](https://de.wikipedia.org/wiki/Polygonnetz) für generelle Informationen in Computersystemen.

![](images/Shape_and_mesh.svg )


*Links: parametrische [Form](Shape/de.md), definiert durch Eigenschaften. Rechts: [Polygonnetz](Mesh/de.md), definiert durch Eckpunkte und Dreiecksflächen.*

## Anwendung

Polygonnetze werden normalerweise durch interne Funktionen der [Polygonnetz Arbeitsbereich](Mesh_Workbench/de.md) oder durch den Import von Polygonnetzformatdateien, wie STL und OBJ, erstellt.

Im Wesentlichen wird jedes Objekt, das von einer [Polygonnetz Formelement](Mesh_Feature/de.md) (`Mesh::Feature` Klasse) abgeleitet ist, wird erwartet, ein Polygonnetz zu halten und zu verändern.

Da FreeCAD in erster Linie als Volumenmodellierer konzipiert ist, ist es besser geeignet, mit Volumenkörpern [Formen](Shape/de.md) zu arbeiten. Es kann Netze in der [3D Ansicht](3D_view.md) importieren und anzeigen, aber um sie zu transformieren oder neue Geometrie zu erzeugen, muss das Netz zuerst in eine [Form](Shape/de.md) konvertiert werden (siehe [Part FormAusPolygonnetz](Part_ShapeFromMesh/de.md)). In vielen Fällen erfolgt diese Konvertierung nicht automatisch und erfordert die Neuerstellung der Geometrie mit Volumenkörpermodellierungstechniken unter Verwendung der [Part](Part_Workbench/de.md) und [PartDesign](PartDesign_Workbench/de.md) Werkzeuge.

## Finite Element Netze {#finite_element_netze}

In FreeCAD kann sich das Wort \"[Polygonnetz](Mesh/de.md)\" auch auf ein bestimmtes Objekt beziehen, das in der Finite Elemente Analyse (FEA) verwendet wird.

Wenn ein Objekt mit einem Volumenkörper [Form](Shape/de.md) in der [FEM Arbeitsbereich](FEM_Workbench/de.md) verwendet wird, wird es zu einem dreieckigen Netz diskretisiert. In diesem Fall ist das resultierende Objekt ein [Fem FemPolygonnetzObjekt](Fem_FemMeshObject/de.md) (`Fem::FemMeshObject` Klasse) und ist nicht von einer [Polygonnetz Merkmal](Mesh_Feature/de.md) (`Mesh::Feature` Klasse) abgeleitet.

Für weitere Informationen siehe [FEM Arbeitsbereich](FEM_Workbench/de.md) und [FEM Polygonnetz](FEM_Mesh/de.md).

## Weitere Informationen {#weitere_informationen}

-   [Polygonale (Netz)-Geometrie](https://forum.freecadweb.org/viewtopic.php?f=8&t=47493)


{{Mesh Tools navi

}} {{FEM Tools navi}} {{Document objects navi}} 

[Category:Glossary{{\#translation:}}](Category:Glossary.md)
