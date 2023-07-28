# <img alt="Mesh workbench icon" src=images/Workbench_Mesh.svg  style="width:64px;"> Mesh Workbench/sv


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

**Nät arbetsbänken** hanterar [triangelnät](http://en.wikipedia.org/wiki/Triangle_mesh). Nät är en speciell typ av 3D objekt, sammansatt av trianglar som är ihopkopplade via deras kanter och hörn.


</div>


<div class="mw-translate-fuzzy">

Många 3D applikationer använder nät som deras primära 3D objektstyp, som [sketchup](http://sv.wikipedia.org/wiki/Sketchup), [blender](http://sv.wikipedia.org/wiki/Blender), [maya](http://sv.wikipedia.org/wiki/Maya_(datorprogram)) eller [3d studio max](http://sv.wikipedia.org/wiki/3ds_Max). Eftersom nät är mycket simpla objekt, som endast innehåller hörn (punkter), kanter och (triangulära) ytor, så är de mycket lätta att skapa, förändra, dela upp, sträcka ut, och kan lätt flyttas från en applikation till en annan utan några förluster. Eftersom de dessutom innehåller mycket simpel data, så kan 3D applikationer vanligtvis hantera mycket stora kvantiteter av dem utan några problem. Av dessa anledningar, så är nät ofta den valda 3D objekttypen i applikationer för filmer, animeringar, och bildbehandling.


</div>


<div class="mw-translate-fuzzy">

Emellertid har nät en stor begränsning inom konstruktionsfältet: De är mycket \'dumma\' objekt, som endast består av punkter, linjer och ytor. De består endast av ytor, och har ingen informationom dess massa, så de beter sig inte som solider. I ett nät så finns det inget automatiskt sätt att avgöra om en punkt är inuti eller utanför objektet. Detta innebär att alla solidbaserade operationer, som addition eller subtraktion, alltid är svåra att utföra på nät, och ofta orsakar fel.


</div>

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">




<div class="mw-translate-fuzzy">

### Använda nätmodulen 


</div>


<div class="mw-translate-fuzzy">

Nätmodulen har för närvarande ett mycket enkelt gränssnitt, alla dess funktioner är grupperade i **Nät** menyn. De viktigaste operationerna som du för närvarande kan göra med nät är:

-   Importera nät i flera filformat
-   Exportera nät i flera filformat
-   Konvertera [Del](Part_Workbench/sv.md) objekt till nät
-   Analysera kurvatur, ytor, och kontrollera om ett nät kan konverteras till en solid på ett säkert sätt
-   Vända nät [normaler](http://sv.wikipedia.org/wiki/normalvektor)
-   Stänga hål i nät
-   Ta bort ytor i nät
-   Förena, subtrahera och skära nät
-   Skapa nätprimitiver, som kuber, sfärer, Koner eller cylindrar
-   Klippa nät längs en linje


</div>

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Import mesh\...](Mesh_Import.md): Imports a mesh object from a file.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Export mesh\...](Mesh_Export.md): Exports a mesh object to a file.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> [Create mesh from shape\...](Mesh_FromPartShape.md): Creates mesh objects from shape objects.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Refinement\...](Mesh_RemeshGmsh.md): Remeshes a mesh object.

-   Analyze
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width:32px;"> [Evaluate and repair mesh\...](Mesh_Evaluation.md): Evaluates and repairs a mesh object.
    -   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width:32px;"> [Face info](Mesh_EvaluateFacet.md): Shows information about faces of mesh objects.
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width:32px;"> [Curvature info](Mesh_CurvatureInfo.md): Shows the absolute curvature of [curvature objects](Mesh_VertexCurvature.md) at selected points.
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width:32px;"> [Check solid mesh](Mesh_EvaluateSolid.md): Checks if a mesh object is solid.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [Boundings info\...](Mesh_BoundingBox.md): Shows the bounding box coordinates of a mesh object.

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width:32px;"> [Curvature plot](Mesh_VertexCurvature.md): Creates Mesh Curvature objects for mesh objects.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width:32px;"> [Harmonize normals](Mesh_HarmonizeNormals.md): Harmonizes the normals of mesh objects.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width:32px;"> [Flip normals](Mesh_FlipNormals.md): Flips the normals of mesh objects.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width:32px;"> [Fill holes\...](Mesh_FillupHoles.md): Fills holes in mesh objects.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width:32px;"> [Close hole](Mesh_FillInteractiveHole.md): Fills selected holes in mesh objects.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width:32px;"> [Add triangle](Mesh_AddFacet.md): Adds faces along a boundary of an open mesh object.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width:32px;"> [Remove components\...](Mesh_RemoveComponents.md): Removes faces from mesh objects.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width:32px;"> [Remove components by hand\...](Mesh_RemoveCompByHand.md): Removes components from mesh objects.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width:32px;"> [Create mesh segments\...](Mesh_Segmentation.md): Creates separate mesh segments for specified surface types of a mesh object.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width:32px;"> [Create mesh segments from best-fit surfaces\...](Mesh_SegmentationBestFit.md): Creates separate mesh segments for specified surface types of a mesh object, and can identify their parameters.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width:32px;"> [Smooth\...](Mesh_Smoothing.md): Smooths mesh objects.

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Decimation\...](Mesh_Decimating.md): Reduces the number of faces in mesh objects.

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Scale\...](Mesh_Scale.md): Scales mesh objects.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Regular solid\...](Mesh_BuildRegularSolid.md): Creates a regular parametric solid mesh object.

-   Boolean
    -   <img alt="" src=images/Mesh_Union.svg  style="width:32px;"> [Union](Mesh_Union.md): Creates a mesh object that is the union of two mesh objects.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width:32px;"> [Intersection](Mesh_Intersection.md): Creates a mesh object that is the intersection of two mesh objects.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width:32px;"> [Difference](Mesh_Difference.md): Creates a mesh object that is the difference of two mesh objects.

-   Cutting
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width:32px;"> [Cut mesh](Mesh_PolyCut.md): Cuts whole faces from mesh objects.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width:32px;"> [Trim mesh](Mesh_PolyTrim.md): Trims faces and parts of faces from mesh objects.
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width:32px;"> [Trim mesh with a plane](Mesh_TrimByPlane.md): Trims faces and parts of faces on one side of a plane from a mesh object.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width:32px;"> [Create section from mesh and plane](Mesh_SectionByPlane.md): Creates a cross section across a mesh object.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width:32px;"> [Cross-sections\...](Mesh_CrossSections.md): Creates multiple cross sections across mesh objects.

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Merge](Mesh_Merge.md): Creates a mesh object by combining the meshes of two or more mesh objects.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Split by components](Mesh_SplitComponents.md): Splits a mesh object into its components.

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Unwrap Mesh](MeshPart_CreateFlatMesh.md): Creates a flat representation of a mesh object.

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Unwrap Face](MeshPart_CreateFlatFace.md): Creates a flat representation of a face of a shape object.

## Preferences

There are some [export preferences related to Mesh Formats](Import_Export_Preferences#Mesh_Formats.md) but these are not used by commands belonging to this workbench. They are used by the [Std Export](Std_Export.md) command.

Mesh Workbench preferences can be found in the following categories of the [Preferences Editor](Preferences_Editor.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Display](Preferences_Editor#Display.md): On the [Mesh view](Preferences_Editor#Mesh_view.md) tab several preferences can be set.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences.md): The [Mesh Union](Mesh_Union.md), [Mesh Intersection](Mesh_Intersection.md) and [Mesh Difference](Mesh_Difference.md) commands require [OpenSCAD](http://www.openscad.org/) and use the **OpenSCAD executable** preference to find its executable.

## Notes

-   More mesh tools are available in the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md).
-   See [Mesh Scripting](Mesh_Scripting.md) to manipulate and create meshes using [Python](Python.md).
-   See also [FreeCAD and Mesh Import](FreeCAD_and_Mesh_Import.md)
-   See [Asymptote](Asymptote.md) to export meshes to the Asymptote format.


<div class="mw-translate-fuzzy">


{{docnav/sv|Workbenches/sv|Part Workbench/sv}}


</div>


{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Mesh](Category_Mesh.md) > Mesh Workbench/sv
