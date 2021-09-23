# <img alt="El icono del Ambiente de trabajo Mesh" src=images/Workbench_Mesh.svg  style="width:64px;"> Mesh Workbench/es


{{TOCright}}

## Introducción

El <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Ambiente de trabajo Mallas](Mesh_Workbench.md) maneja [triangle mesh](http://en.wikipedia.org/wiki/Triangle_mesh). Mallas son un tipo especial de objeto 3D, compuesto por areas triangulares conectadas por sus vértices y aristas.

Muchas aplicaciones 3D, como [Sketchup](https://es.wikipedia.org/wiki/SketchUp), [Blender](http://es.wikipedia.org/wiki/Blender), [Autodesk Maya](http://es.wikipedia.org/wiki/Autodesk_Maya) y [Autodesk 3ds Max](http://es.wikipedia.org/wiki/Autodesk_3ds_Max) utilizan mallas como tipo principal de objeto 3D. Dado que las mallas son objetos muy sencillos, que sólo contienen vértices (puntos), aristas y caras triangulares, son muy fáciles de crear, modificar, subdividir y estirar, y pueden pasarse fácilmente de una aplicación a otra sin pérdida de detalles. Además, como las mallas contienen datos muy simples, las aplicaciones 3D suelen poder gestionar cantidades muy grandes de ellas sin utilizar muchos recursos. Por estas razones, las mallas suelen ser el tipo de objeto 3D preferido para las aplicaciones que se ocupan de las películas, la animación y la creación de imágenes.

Sin embargo, en el campo de la ingeniería las mallas presentan una gran limitación: no pueden definir con precisión las superficies curvas. Por eso FreeCAD se basa en [Brep](wikipedia:Boundary_representation.md) en su lugar. El Mesh Workbench ofrece algunos comandos para manipular directamente las mallas, pero se utiliza más a menudo para importar datos de malla 3D y convertirlos en un sólido para su uso con el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo Piezas](Part_Workbench/es.md) o <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md).

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">

## Herramientas

Todas las herramientas del ambiente de trabajo Malla se puede acceder a desde el menú **Mallas**. Casi todas están también disponibles en una de las barras de herramientas de malla.

-   ![ 32px](images/_Mesh_ImportMesh.png ) [Import Mesh](Mesh_Import/es.md): Importar mallas en varios formatos de archivo

-   ![ 32px](images/_Mesh_ExportMesh.png ) [ Export Mesh](Mesh_Export/es.md): exporta mallas en varios formatos de archivo

-   ![ 32px](images/_Mesh_MeshFromShape.png ) [ Create Mesh from shape](Mesh_MeshFromShape.md): convierte objetos [ Part](Part_Workbench/es.md) en mallas

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Refinamiento\...](Mesh_RemeshGmsh/rs.md): Refina un objeto de malla. {{Version/es|0.19}}

-   Analizar
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width:32px;"> [Evaluar y reparar malla\...](Mesh_Evaluation/es.md): Evalúa y repara un objeto de malla.
    -   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width:32px;"> [ Face Info](Mesh_EvaluateFacet/es.md): Da información sobre las caras
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width:32px;"> [ Curvature Info](Mesh_CurvatureInfo/es.md): proporciona información sobre la curvatura
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width:32px;"> [ Check solid mesh](Mesh_EvaluateSolid/es.md): Comprueba si el sólido se puede convertir a una malla
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [ Boundings info \...](Mesh_BoundingBox/es.md): Muestra las coordenadas del cuadro delimitador de un objeto de malla.

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

-   Booleano
    -   <img alt="" src=images/Mesh_Union.svg  style="width:32px;"> [Unión](Mesh_Union/es.md): Crea un objeto de malla que es la unión de dos objetos de malla.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width:32px;"> [Intersección](Mesh_Intersection/es.md): Crea un objeto de malla que es la intersección de dos objetos de malla.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width:32px;"> [Diferencia](Mesh_Difference/es.md): Crea un objeto de malla que es la diferencia de dos objetos de malla.

-   Cutting
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width:32px;"> [Cut mesh](Mesh_PolyCut.md): Cuts whole faces from mesh objects.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width:32px;"> [Trim mesh](Mesh_PolyTrim.md): Trims faces and parts of faces from mesh objects.
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width:32px;"> [Trim mesh with a plane](Mesh_TrimByPlane.md): Trims faces and parts of faces on one side of a plane from a mesh object.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width:32px;"> [Create section from mesh and plane](Mesh_SectionByPlane.md): Creates a cross section across a mesh object.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width:32px;"> [Cross-sections\...](Mesh_CrossSections.md): Creates multiple cross sections across mesh objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Merge](Mesh_Merge.md): Creates a mesh object by combining the meshes of two or more mesh objects.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Split by components](Mesh_SplitComponents.md): Splits a mesh object into its components. <small>(v0.19)</small> 

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Unwrap Mesh](MeshPart_CreateFlatMesh.md): Creates a flat representation of a mesh object. <small>(v0.19)</small> 

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Unwrap Face](MeshPart_CreateFlatFace.md): Creates a flat representation of a face of a shape object. <small>(v0.19)</small> 

## Preferencias

Hay algunas [preferencias de exportación relacionadas con los formatos de malla](Import_Export_Preferences/es#Formatos_de_malla.md) pero no son utilizadas por los comandos pertenecientes a este ambiente de trabajo. Son utilizadas por el comando [Std Exportar](Std_Export/es.md).

Mesh Workbench preferences can be found in the following categories of the [Preferences Editor](Preferences_Editor.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Display](Preferences_Editor#Display_settings.md): On the [Mesh view](Preferences_Editor#Mesh_view.md) tab several preferences can be set.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences.md): The [Mesh Union](Mesh_Union.md), [Mesh Intersection](Mesh_Intersection.md) and [Mesh Difference](Mesh_Difference.md) commands require [OpenSCAD](http://www.openscad.org/) and use the **OpenSCAD executable** preference to find its executable.

## Notas

-   Hay más herramientas de malla disponibles en el <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [Ambiente de trabajo OpenSCAD](OpenSCAD_Workbench/es.md).
-   Ver [Mallas guiones](Mesh_Scripting/es.md) para manipular y crear mallas usando [Python](Python/es.md).
-   Ver también: [FreeCAD e Mesh Importación](FreeCAD_and_Mesh_Import/es.md)
-   Ver [Asymptote](Asymptote/es.md) para exportar mallas al formato Asymptote.





{{Mesh Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Mesh Workbench/es
