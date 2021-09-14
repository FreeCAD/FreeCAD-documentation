# Shape/de



## Einleitung

In FreeCAD wird das Wort \"[Form](Shape/de.md)\" normalerweise verwendet, um sich auf eine [Part TopoForm](Part_TopoShape/de.md) (`Part::TopoShape` Klasse) zu beziehen , ein Objekttyp, der einem Element seine 3D geometrische und parametrische Darstellung gibt (Würfel, Pyramide, Kugel, Zylinder, Vereinigung usw.).

Im Wesentlichen haben alle Objekte, die in der [3D Ansicht](3D_view/de.md) angezeigt werden, eine [TopoForm](Part_TopoShape/de.md), mit Ausnahme von \"[Polygonnetze](Mesh/de.md)\", die eine [PolygonnetzObjekt](Mesh_MeshObject/de.md) (`Mesh::MeshObject` Klasse) haben.

Siehe [Part TopoForm](Part_TopoShape/de.md) für weitere Information über diesen Objekttyp.

![](images/Shape_and_mesh.svg )


*Links: parametrische [Form](Shape/de.md), definiert durch Eigenschaften. Rechts: [Polygonnetz](Mesh/de.md), definiert durch Knoten und Dreiecksflächen.*

## Anwendung

Formen werden normalerweise durch interne Funktionen des [Part Arbeitsbereichs](Part_Workbench/de.md) erstellt und werden letztlich durch den [OpenCASCADE Technologie](OpenCASCADE/de.md) Kernel (OCCT) definiert.

Sobald eine Form erstellt wurde, kann sie von allen [Arbeitsbereichen](Workbenches/de.md) verwendet und geändert werden, indem [Skriptgenerierte Objekte](scripted_objects/de.md) um diese Form herum erstellt werden.

Im Wesentlichen wird jedes Objekt, das von einer [Part Formelement](Part_Feature/de.md) (`Part::Feature` Klasse) abgeleitet ist, wird erwartet, eine Form zu halten und zu verändern.

## Hinweise

Im informellen Gebrauch kann eine \"Form\" jede geometrische Figur sein, die in der [3D Ansicht](3D_view/de.md) sichtbar ist, und daher kann ihr Konzept mit dem von \"[Körper](Body/de.md)\" oder \"[Part](Part/de.md)\" verwechselt werden.

Wenn jedoch mehr Präzision erforderlich ist, muss eine Unterscheidung getroffen werden.

-   Ein \"[Körper](Body/de.md)\" ist ein Objekt, das von einem [Part Formelement](Part_Feature/de.md) abgeleitet ist. (`Part::Feature` Klasse), erstellt mit der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md).
-   Eine \"Form\" ist ein internes Objekt, eingebettet in die Klasse \"[Körper](Body/de.md)\".
-   Ein \"[Part](Part/de.md)\" wird verwendet, um mehrere \"[Körper](Body/de.md)\" zu gruppieren, um eine [Baugruppe](assembly/de.md) zu bilden. Ein \"Part\" hat eine Sammlung von \"Formen\", hat aber keine eigenständige \"Form\".


 {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
