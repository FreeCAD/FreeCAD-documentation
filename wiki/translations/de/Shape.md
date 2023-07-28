# Shape/de
## Einleitung

In FreeCAD wird das Wort \"[Form](Shape/de.md)\" normalerweise verwendet, um sich auf eine [Part TopoForm](Part_TopoShape/de.md) (`Part::TopoShape` Klasse) zu beziehen , ein Objekttyp, der einem Element seine geometrische und parametrische 3D-Darstellung gibt (Würfel, Pyramide, Kugel, Zylinder, Vereinigung usw.).

Im Wesentlichen haben alle Objekte, die in der [3D-Ansicht](3D_view/de.md) angezeigt werden, eine [TopoForm](Part_TopoShape/de.md), mit Ausnahme von \"[Netzen](Mesh/de.md)\", die ein [Netzobjekt](Mesh_MeshObject/de.md) (`Mesh::MeshObject`-Klasse) haben.

Siehe [Part TopoForm](Part_TopoShape/de.md) für weitere Information über diesen Objekttyp.

![](images/Shape_and_mesh.svg )



*Links: parametrische [Form](Shape/de.md), definiert durch Eigenschaften. Rechts: [Polygonnetz](Mesh/de.md), definiert durch Knoten und dreieckigen Oberflächen.*



## Anwendung

Formen werden normalerweise durch interne Funktionen des Arbeitsbereichs [Part](Part_Workbench/de.md) erstellt und werden letztlich durch den [OpenCASCADE-Technology](OpenCASCADE/de.md)-Kernel (OCCT) definiert.

Sobald eine Form erstellt wurde, kann sie von allen [Arbeitsbereichen](Workbenches/de.md) verwendet und geändert werden, indem [skriptgenerierte Objekte](scripted_objects/de.md) um diese Form herum erstellt werden.

Im Wesentlichen wird von jedem Objekt, das von einem [Part Formelement](Part_Feature/de.md) (`Part::Feature` Klasse) abgeleitet ist, erwartet, eine Form zu enthalten und zu verändern.

Jede OpenCascade-Form besitzt eine Netzstruktur für die Darstellung der Form auf dem Bildschirm. Mehr Informationen darüber findet man im [Forumsbeitrag](https://forum.freecad.org/viewtopic.php?t=77521&start=10#p674947) und in der [OpenCascade-Mesh-Documentation](https://dev.opencascade.org/doc/overview/html/occt_user_guides__mesh.html).



## Hinweise

Im informellen Gebrauch kann eine \"Form\" jede geometrische Figur sein, die in der [3D-Ansicht](3D_view/de.md) sichtbar ist, und daher kann ihr Konzept mit dem von \"[Körper](Body/de.md)\" oder \"[Part](Part/de.md)\" verwechselt werden.

Wenn jedoch mehr Präzision erforderlich ist, muss eine Unterscheidung getroffen werden.

-   Ein \"[Körper](Body/de.md)\" ist ein Objekt, das von einem [Part Formelement](Part_Feature/de.md) (`Part::Feature` Klasse) abgeleitet ist, erstellt mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md).
-   Eine \"Form\" ist ein internes Objekt, eingebettet in einem \"[Körper](Body/de.md)\".
-   Ein \"[Part](Part/de.md)\" wird verwendet, um mehrere \"[Körper](Body/de.md)\" zu gruppieren, um eine [Baugruppe](assembly/de.md) zu bilden. Ein \"Part\" hat eine Sammlung von \"Formen\", hat aber keine eigenständige \"Form\".


 {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Part](Category_Part.md) > Shape/de
