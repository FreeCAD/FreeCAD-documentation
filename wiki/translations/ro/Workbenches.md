# Workbenches/ro
<div class="mw-translate-fuzzy">


{{docnav/ro|[Property editor](Property_editor/ro.md)|[PartDesign Workbench](PartDesign_Workbench/ro.md)}}


</div>


<div class="mw-translate-fuzzy">

FreeCAD, la fel ca multe aplicații de design moderne, precum [ Revit](wikipedia__Revit.md) sau [ CATIA](wikipedia__CATIA.md), se bazează pe conceptul de [ Workbench](wikipedia__Workbench.md). Un atelier poate fi considerat un set de instrumente special grupate pentru o anumită sarcină. Într-un atelier de mobilier tradițional, veți avea o masă de lucru pentru persoana care lucrează cu lemn, un altul pentru cel care lucrează cu piese de metal și poate un al treilea pentru tipul care montează toate piesele împreună.


</div>

În FreeCAD, se aplică același concept. Instrumentele sunt grupate în ateliere în funcție de sarcinile cu care sunt legate.

Când treceți de la un atelier la altul, se schimbă instrumentele disponibile pe interfață. Barele de instrumente, barele de comandă și, eventual, alte părți ale interfeței comută la noul tabel de lucru, dar conținutul scenei dvs. nu se schimbă. Ați putea, de exemplu, să începeți desenarea unor forme 2D cu Workbench Draft, apoi să lucrați mai departe pe ele cu Workbench Part.


<div class="mw-translate-fuzzy">

Rețineți că uneori un Workbench este denumit \"Modul\". Cu toate acestea, atelierele de lucru și modulele sunt entități diferite. Un modul este orice extensie a FreeCAD, în timp ce un Workbench este o configurație GUI specială care grupează câteva bare de instrumente și meniuri. De obicei, fiecare modul conține propriul său Workbench, de unde și utilizarea încrucișată a numelui.


</div>



## Ateliere încorporate 

### Current


<div class="mw-translate-fuzzy">

Următoarele ateliere sunt disponibile pentru fiecare instalare FreeCAD:


</div>

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. Still in the early stages of development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with geometric primitives and boolean operations.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements. Currently unmaintained.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Obsolete

The following workbenches are no longer included after version 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) was used for working with bitmap images. It functionality has been integrated in [Std Base](Std_Base.md). See [Std Import](Std_Import.md) and [Std ViewLoadImage](Std_ViewLoadImage.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) was used for ray-tracing (rendering). The external [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) should be used instead.



## Ateliere externe 


<div class="mw-translate-fuzzy">

Atelierele de lucru FreeCAD sunt ușor de programat în [Python](Python.md), prin urmare, mulți oameni dezvoltă ateliere suplimentare în afara grupului principal de dezvoltatori FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Pagina [external workbenches](external_workbenches.md) conține câteva informații și tutoriale despre unele dintre ele, iar proiectul [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) are ca scop colectarea acestora și facilitarea instalării acestora în cadrul FreeCAD .


</div>


<div class="mw-translate-fuzzy">


{{docnav/ro|Property editor/ro|PartDesign Workbench/ro}}


</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/ro
