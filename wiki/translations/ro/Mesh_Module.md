


<div class="mw-translate-fuzzy">





</div>

<img alt="Mesh workbench icon" src=images/Workbench_Mesh.svg  style="width:128px;">


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

## Introducere

Atelierul Plase [Mesh Workbench](Mesh_Workbench.md) se ocupă de [mesh triangle](http://en.wikipedia.org/wiki/Triangle_mesh). Plasele/Mesh-urile sunt un tip special de obiect 3D, compuse din fațete triunghiulare legate de marginile lor și de colțurile lor (numite și vârfuri).


</div>

Multe aplicații 3D utilizează ochiurile de plasă ca tip principal de obiect 3D, cum ar fi [sketchup](http://en.wikipedia.org/wiki/Sketchup), [Blender](http://en.wikipedia.org/wiki/Blender_(software)) , [Maya](http://en.wikipedia.org/wiki/Maya_(software)) sau [3D Studio Max](http://en.wikipedia.org/wiki/3d_max), utilizează plase ca primă alegere de elecție. Deoarece plasele sunt obiecte foarte simple, conținând numai vârfuri (puncte), muchii și fațete (triunghiulare), ele sunt foarte ușor de creat, modificat, subdivizat, întins și ușor de trecut de la o aplicație la alta fără nici o pierdere. În plus, deoarece conțin date foarte simple, aplicațiile 3D pot gestiona, de obicei, cantități foarte mari din acestea fără nici o problemă. Din aceste motive, plasele sunt adesea tipul de obiect 3D preferat pentru aplicații care se ocupă cu filmele, animația și crearea imaginilor.


<div class="mw-translate-fuzzy">

Cu toate acestea, în domeniul rețelelor de inginerie există o mare limitare: ele sunt doar realizate din suprafețe și nu au informații despre masă, deci nu se comportă ca solide. Aceasta înseamnă că toate operațiunile de bază pentru solide, cum ar fi adunarea sau scăderea, sunt dificil de realizat pe ochiuri de plasă. Mesh Workbench este util să importați date 3D în format de plase, să le analizați, să detectați erorile și, în final, să le convertiți într-un solid, pentru a fi utilizate cu [Part Workbench](Part_Workbench.md).


</div>

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">


<div class="mw-translate-fuzzy">

## Instrumente


</div>


<div class="mw-translate-fuzzy">

Modulul de plase are în prezent o interfață foarte simplă, toate funcțiile sale fiind grupate în intrarea din meniul {{MenuCommand|Mesh}}


</div>

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Import mesh\...](Mesh_Import.md): Imports a mesh object from a file.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Export mesh\...](Mesh_Export.md): Exports a mesh object to a file.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> [Create mesh from shape\...](Mesh_FromPartShape.md): Creates mesh objects from shape objects.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Refinement\...](Mesh_RemeshGmsh.md): Remeshes a mesh object. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

### Analiza

-   Analizează curbura, fațetele și verifică dacă o plasă poate fi convertită într-un solid
    -   [Evaluate & Repair mesh\...](Mesh_EvaluateRepair.md): Evaluează și repară plase
    -   <img alt="" src=images/Mesh_EvaluateFacet.png  style="width:32px;"> [Face Info](Mesh_EvaluateFacet.md): Dă informații despre fațete
    -   [Curvature Info](Mesh_EvaluateCurvature.md): Dă informații despre curbură
    -   [Check solid mesh](Mesh_EvaluateSolid.md): Verifică dacă un solid poate fi convertit într-o plasă
    -   [Boundings info\...](Mesh_BoundingBox.md): Evaluează paralelipipedul de încadrare al unei plase


</div>

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

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Decimation\...](Mesh_Decimating.md): Reduces the number of faces in mesh objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Scale\...](Mesh_Scale.md): Scales mesh objects.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Regular solid\...](Mesh_BuildRegularSolid.md): Creates a regular parametric solid mesh object.


<div class="mw-translate-fuzzy">

### Boolean

-   [Union](Mesh_Union.md): Realizează o uniune/fuziun e cu plase
-   [Intersection](Mesh_Intersection.md): Realizează o intersecție/common de plase
    -   [Difference](Mesh_Difference.md): Realizează o diferență/cut de plase


</div>


<div class="mw-translate-fuzzy">

### Cutting

-   <img alt="" src=images/Mesh_Cut.png  style="width:32px;"> [Cut mesh](Mesh_Cut.md): Taie/Cut plase de-a lungul unei linii
-   [Trim mesh](Mesh_TrimMesh.md): Trims plase
-   [Trim mesh with a plane](Mesh_TrimMeshWithPlane.md): Trims plase cu un plan
-   Creează o secțiune dintr-o plasă și un plan


</div>

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Merge](Mesh_Merge.md): Creates a mesh object by combining the meshes of two or more mesh objects.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Split by components](Mesh_SplitComponents.md): Splits a mesh object into its components. <small>(v0.19)</small> 

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Unwrap Mesh](MeshPart_CreateFlatMesh.md): Creates a flat representation of a mesh object. <small>(v0.19)</small> 

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Unwrap Face](MeshPart_CreateFlatFace.md): Creates a flat representation of a face of a shape object. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

## Preferences

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preference](Import_Export_Preference.md) Import-Export


</div>

There are some [export preferences related to Mesh Formats](Import_Export_Preferences#Mesh_Formats.md) but these are not used by commands belonging to this workbench. They are used by the [Std Export](Std_Export.md) command.

Mesh Workbench preferences can be found in the following categories of the [Preferences Editor](Preferences_Editor.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Display](Preferences_Editor#Display_settings.md): On the [Mesh view](Preferences_Editor#Mesh_view.md) tab several preferences can be set.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences.md): The [Mesh Union](Mesh_Union.md), [Mesh Intersection](Mesh_Intersection.md) and [Mesh Difference](Mesh_Difference.md) commands require [OpenSCAD](http://www.openscad.org/) and use the **OpenSCAD executable** preference to find its executable.


<div class="mw-translate-fuzzy">

## Legături


</div>


<div class="mw-translate-fuzzy">

-   [FreeCAD and Mesh Import](FreeCAD_and_Mesh_Import.md)


</div>


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
