 {{TOCright}}

## Background

This page is intended for users who are interested in migrating to FreeCAD from the Fusion 360 world.

## What do I do? {#what_do_i_do}

1.  The first thing that you want to do is to get your files out of proprietary formats and storage. Start by exporting your models from the cloud to your local machine.
    -   A popular method is using this [Fusion360 total exporter](https://github.com/Jnesselr/fusion-360-total-exporter) script.
2.  We recommend exporting to STEP format.

## Glossary


{{VeryImportantMessage|Please also reference the ongoing work in progress [CAD Rosetta Stone](CAD_Rosetta_Stone.md) project to learn the analogous names that popular proprietary CADs use}}

Reference the [Glossary](Glossary.md) page in general but here is a short list of specific terms that F360 folks may find spefically helpful:

-   Tangent constraint - FreeCAD\'s form of **Collinear Constraint**. See <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Sketcher ConstrainTangent](Sketcher_ConstrainTangent#Between_two_lines_.28collinear.29.md).
-   Pad - The **extrude** function in FreeCAD. Read the <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) documentation to learn more.
-   Toponaming - Short for [Topological naming problem](Topological_naming_problem.md). Covered very well in [Brodie Fairhall\'s youtube clip](https://www.youtube.com/watch?v=6p2vqEEmWq4)\].
--   

## FAQ

1.  What formats do you support in FreeCAD?
    -   The native file format in FreeCAD is BREP, [boundary representation](https://en.wikipedia.org/wiki/Boundary_representation), provided by the internal [OpenCASCADE (OCCT)](OpenCASCADE.md) geometry kernel.
    -   FreeCAD supports all formats that OCCT supports, so STEP and IGES at least.
2.  What formats should I use to migrate to FreeCAD?
    -   STEP is the best format because it is a solid [Shape](Shape.md) format, as opposed to a [Mesh](Mesh.md) (STL, OBJ, DAE). Example, [Importing Step with Colors](https://forum.freecadweb.org/viewtopic.php?f=3&t=50308).
    -   Importing an STL is possible, but this mesh format will be difficult to modify further. We recommend converting imported meshes to solid Shapes using **<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part ShapeFromMesh](Part_ShapeFromMesh.md)**. Remodelling the object in FreeCAD, while using the mesh as reference, is the best advice.

## Tips

-   \@MPetrika ([twitter](https://twitter.com/MPetrikas/status/1362051484704264198)) recommends installing HakanSeven12\'s [ModernUI Workbench](ModernUI_Workbench.md)

## Learning Resources {#learning_resources}

-   [Fusion360 to FreeCAD - Introduction](https://www.youtube.com/watch?v=_GxJkB23ZHM), video by Brodie Fairhall.
-   [Fusion360 to FreeCAD - Part 2](https://www.youtube.com/watch?v=IESZD4QS3P8), video by Brodie Fairhall.
-   [V0.19 Benchmarking\--2019 Monthly Challenges](https://forum.freecadweb.org/viewtopic.php?f=36&t=50492), a series of objects created with Fusion360 are remodelled using FreeCAD, by experienced user ppemawm.
-   [Beginners written tutorial: from first part to technical drawing.](https://github.com/macdroid53/LearningFreeCAD) by macdroid53.
-   [An online resource for us regular FreeCAD users.](https://www.freecad.info/)

## Comparison Videos {#comparison_videos}

-   [Model a compressor turbine in FreeCAD and Fusion360](https://www.youtube.com/watch?v=kirDbZd0dvI&feature=youtu.be)

## Help

Is this wiki page missing something. Please make a request for [wiki permissions](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) on the forum to edit this page.

## Related

-   [Migrating to FreeCAD from OnShape](Migrating_to_FreeCAD_from_OnShape.md)



