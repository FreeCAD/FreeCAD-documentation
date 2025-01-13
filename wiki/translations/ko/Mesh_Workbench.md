# Mesh Workbench/ko
<div class="mw-translate-fuzzy">





</div>

<img alt="메쉬 작업대 아이콘" src=images/Workbench_Mesh.svg  style="width:128px;">






## 소개

<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> **메쉬 작업대**에서는 [삼각형 메쉬](http://en.wikipedia.org/wiki/Triangle_mesh)를 처리합니다.메쉬는 꼭지점과 가장자리로 연결된 삼각형 면으로 구성된 특별한 유형의 3D 개체입니다.

[Sketchup](http://en.wikipedia.org/wiki/Sketchup), [Blender](http://en.wikipedia.org/wiki/Blender_(software)), [Maya](http://en.wikipedia.org/wiki/Maya_(software)) 및 [3D Studio Max](http://en.wikipedia.org/wiki/3d_max)와 같은 많은 3D 응용 프로그램은 메쉬를 기본 유형의 3D 개체로 사용합니다. 메쉬는 꼭지점(점), 모서리 및 삼각형 면만 포함하는 매우 단순한 개체이므로 생성, 수정, 세분화, 늘리기가 매우 쉽고 세부 정보 손실 없이 한 응용 프로그램에서 다른 응용 프로그램으로 쉽게 전달할 수 있습니다. 이러한 이유로 메쉬는 영화, 애니메이션 및 이미지 생성을 다루는 응용 프로그램에서 선택되는 3D 객체 유형인 경우가 많습니다.

그러나 엔지니어링 메쉬 분야에서는 다음과 같은 큰 한계가 있습니다: 곡면을 정확하게 정의할 수 없습니다. 이것이 FreeCAD가 대신 [Brep에](wikipedia_Boundary_Representation.md) 의존하는 이유입니다. 메쉬 워크벤치는 메쉬를 직접 조작하는 몇 가지 명령을 제공하지만, 3D 메쉬 데이터를 가져와 솔리드로 변환하여 <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [부품 작업대또는](Part_Workbench/ko.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [부품설계 작업대와](PartDesign_Workbench/ko.md) 함께 사용하는 데 가장 많이 사용됩니다.

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">



## 도구

All Mesh Workbench tools can be accessed from the **Meshes** menu. Almost all are also available in one of the Mesh toolbars.

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

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Unwrap mesh](MeshPart_CreateFlatMesh.md): Creates a flat representation of a mesh object.

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Unwrap face](MeshPart_CreateFlatFace.md): Creates a flat representation of a face of a shape object.

## Preferences

There are some [export preferences related to Mesh Formats](Import_Export_Preferences#Mesh_Formats.md) but these are not used by commands belonging to this workbench. They are used by the [Std Export](Std_Export.md) command.

Mesh Workbench preferences can be found in the following groups in the [Preferences Editor](Preferences_Editor.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Display](Preferences_Editor#Display.md): On the [Mesh view](Preferences_Editor#Mesh_view.md) page several preferences can be set.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences.md): The [Mesh Union](Mesh_Union.md), [Mesh Intersection](Mesh_Intersection.md) and [Mesh Difference](Mesh_Difference.md) commands require [OpenSCAD](http://www.openscad.org/) and use the **OpenSCAD executable** preference to find its executable.

## Notes

-   More mesh tools are available in the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md).
-   See [Mesh Scripting](Mesh_Scripting.md) to manipulate and create meshes using [Python](Python.md).
-   See also [FreeCAD and Mesh Import](FreeCAD_and_Mesh_Import.md)
-   See [Asymptote](Asymptote.md) to export meshes to the Asymptote format.


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Mesh](Category_Mesh.md) > Mesh Workbench/ko
