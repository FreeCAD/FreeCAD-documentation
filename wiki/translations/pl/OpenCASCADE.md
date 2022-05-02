# OpenCASCADE/pl
{{TOCright}}

## Opis

**OpenCASCADE Technology**, w skrócie **OCC** lub **OCCT**, jest zbiorem bibliotek C++, które razem tworzą profesjonalne jądro komputerowego wspomagania projektowania *(CAD)* do modelowania obiektów 2D i 3D oraz budowania specjalistycznych narzędzi do produkcji, symulacji lub wizualizacji. OpenCASCADE jest sercem geometrycznych możliwości programu FreeCAD.

Klasy geometryczne OCCT są w większości zaimplementowane i udostępnione w programie FreeCAD za pośrednictwem środowiska pracy [Część](Part_Workbench/pl.md), od którego zależy większość innych [środowisk pracy](Workbenches/pl.md). Udostępnia on także wewnętrzne funkcje odczytu i zapisu różnych formatów plików, takich jak STEP i IGES, oraz wykonywania rzutów 2D, które mogą być używane do tworzenia rysunków technicznych w środowisku pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*OpenCASCADE dostarcza podstawowe klasy geometryczne i funkcje rysunkowe do środowiska pracy [Część](Part_Workbench/pl.md), które są następnie wykorzystywane przez wszystkie grupy robocze w programie FreeCAD.*

OpenCASCADE nie powinien być mylony z [OpenSCAD](https://www.openscad.org/), który jest innym projektem open source do budowy modeli 3D, dostępnym poprzez środowisko pracy [OpenSCAD](OpenSCAD_Workbench/pl.md).

OpenCASCADE jest wolnym oprogramowaniem podlegającym warunkom licencji GNU Lesser General Public License *(LGPL)* w wersji 2.1 z dodatkowym wyjątkiem.

## Instalacja

OpenCASCADE is a core component of FreeCAD, so if you get FreeCAD from one of the links in the [Download](Download.md) page, you will have it installed, and no further installation is necessary.

However, if you would like to develop applications that use OCCT, or would like to contribute C++ code to FreeCAD, then you need to install the development files of OCCT. In this case, the procedure is explained in [Compiling](Compiling.md) for each of the main systems, Linux, Windows, and MacOS.

## Edycja społecznościowa 

A \"community edition\" of OpenCASCADE, abbreviated OCE, was released in 2011, based on the official OpenCASCADE sources (OCCT) of version 6.5. In theory the community edition OCE should be compatible with the main version OCCT in most aspects, while having some additional code contributed by the community.

However, this alternative distribution stopped active development around 2017, and lagged behind the main version in terms of features and bug fixes. For this reason, since FreeCAD v0.17, FreeCAD is compiled exclusively with OCCT, and OCE is not tested.

In some older Linux distributions, FreeCAD is compiled against OCE 0.18, equivalent to OCCT 6.9.x, causing various issues that have been solved already in the main OCCT 7.x releases. If this is the case, try removing OCE, and installing OCCT instead. If this is not possible, use the [AppImage](AppImage.md) to get a modern FreeCAD with an updated OCCT version.

## Historia

The Cas.CADE geometric kernel was originally closed source, but it became open source under its current name around the year 2000. Shortly after, the FreeCAD project was started, with the oldest files being dated to January 2001. Read more in [History](History.md).

OpenCASCADE version 6.6 and earlier were governed by its own \"OCCT public license\", which made it not entirely \"free software\". This was solved with the release of OCCT 6.7 (2013), when it adopted the LGPL2 license.

## Koncepcje geometryczne OCCT 

In OpenCascade terminology, we distinguish between geometric primitives and topological shapes. A geometric primitive can be a point, a line, a circle, a plane, etc. or even some more complex types like a B-Spline curve or a surface. A shape can be a vertex, an edge, a wire, a face, a solid or a compound of other shapes. The geometric primitives are not made to be directly displayed on the 3D scene, but rather to be used as building geometry for shapes. For example, an edge can be constructed from a line or from a portion of a circle.

In summary, geometry primitives are \"shapeless\" building blocks, while [topological shapes](Part_TopoShape.md) are the real objects built on them.

A complete list of all primitives and shapes refer to the [OCC documentation](http://www.opencascade.org/org/doc/) (Alternative: [sourcearchive.com](https://www.opencascade.com/doc/occt-7.4.0/refman/html/)) and search for **Geom\_\*** (for geometric primitives) and **TopoDS\_\*** (for shapes). There you can also read more about the differences between them. Please note that the official OCC documentation is not available online (you must download an archive) and is mostly aimed at programmers, not at end-users. But hopefully you\'ll find enough information to get started here. Also see [Modeling Data User\'s Guide](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html).

> *At a very high level, topology tells what pieces an object is made of, and the logical relationships between them. A shape is made of a certain set of faces. A face is bounded by a certain set of edges. Two faces are adjacent if they share a common edge.*

> *Topology alone does not tell you the size, curvature, or 3D locations of any of those pieces. However, each piece of topology does knows about it\'s underlying geometry. A face knows what surface it lies on. An edge knows what curve it lies on. The geometry knows about curvature and location in space.* - [Source](https://www.opencascade.com/content/geometry-and-topology)


<hr />

> *Thus, Topology defines the relationship between simple geometric entities, which can be linked together to represent complex shapes.* - [Modeling Data User\'s Guide](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html)

![](images/ClassTopoDS_Shape_inherit_graph.png )

**Note:** Only 3 types of topological objects have geometric representations -- vertex, edge, and face ([Source](https://opencascade.blogspot.com/2009/02/topology-and-geometry-in-open-cascade.html)).

The geometric types actually can be divided into two major groups: curves and surfaces. Out of the curves (line, circle, \...) you can directly build an edge, out of the surfaces (plane, cylinder, \...) a face can be built. For example, the geometric primitive line is unlimited, i.e. it is defined by a base vector and a direction vector while its shape representation must be something limited by a start and end point. And a box \-- a solid \-- can be created by six limited planes.

From an edge or face you can also go back to its geometric primitive counterpart.

Thus, out of shapes you can build very complex parts or, the other way round, extract all sub-shapes a more complex shape is made of.

<img alt="" src=images/Part_TopoShape_relationships.svg  style="width:600px;">



*The `Part::TopoShape* class is the geometrical object that is seen on screen. Essentially all workbenches use these [TopoShapes](Part_TopoShape.md) internally to build and display edges, faces, and solids.`

## Powiązane

-   OpenCASCADE Technology (OCCT) [main website](http://www.opencascade.com)
-   OCCT [development portal](https://dev.opencascade.org/)
-   OCCT [latest release](https://www.opencascade.com/content/latest-release)
-   OCCT [git repository](https://git.dev.opencascade.org/gitweb/?p=occt.git)
-   OpenCASCADE Community Edition (OCE) [git repository](https://github.com/tpaviot/oce)
-   [Open Cascade Technology OCCT](http://en.wikipedia.org/wiki/Open_Cascade_Technology) on Wikipedia
-   Glossary, [Open CASCADE](Glossary#Open_CASCADE.md)
-   Tracking OCCT bugs in the FreeCAD bugtracker [(thread)](https://forum.freecadweb.org/viewtopic.php?f=10&t=20264)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > OpenCASCADE/pl
