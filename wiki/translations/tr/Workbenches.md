# Workbenches/tr



<div class="mw-translate-fuzzy">


{{docnav/tr|[Özellik Penceresi](Property_editor/tr.md)|[Parça Tasarım Tezgahı](PartDesign_Workbench/tr.md)}}

FreeCAD, [Revit](wikipedia:Revit.md) veya [CATIA](wikipedia:CATIA.md) gibi birçok modern tasarım uygulamasına benzer olarak, [Tezgah](wikipedia:Workbench.md) kavramına dayanmaktadır. Bir tezgah, belirli bir görev için özel olarak gruplandırılmış bir takım araçlar olarak düşünülebilir. Geleneksel bir mobilya atölyesinde, ahşapla çalışan için bir çalışma masası, metal parçalarıyla çalışan için başka bir çalışma masası ve montaj yapan kişi için üçüncü bir çalışma masası olacaktır.


</div>

FreeCAD, like many modern design applications such as [Revit](wikipedia:Revit.md) or [CATIA](wikipedia:CATIA.md), is based on the concept of [Workbench](wikipedia:Workbench.md). A workbench can be considered as a set of tools specially grouped for a certain task. In a traditional furniture workshop, you would have a work table for the person who works with wood, another one for the one who works with metal pieces, and maybe a third one for the guy who mounts all the pieces together.

FreeCAD\'de de aynı görüş geçerlidir. Araçlar, ilgili oldukları görevlere göre tezgahlarda gruplanır.

Bir tezgahtan diğerine geçtiğinizde, arayüzde mevcut olan araçlar değişir. Araç çubukları, komut çubukları ve arayüzün muhtemelen diğer kısımları yeni tezgahlara geçer, ancak sahnenizin içeriği değişmez. Örneğin, Taslak Tezgahı ile 2D şekiller çizmeye başlayabilir, daha sonra Parça Tezgahı ile nesne üzerinde daha fazla çalışabilirsiniz.


<div class="mw-translate-fuzzy">

Bazen bir Tezgahın *Modül* olarak adlandırıldığını unutmayın . Ancak, Tezgahlar ve Modüller farklı varlıklardır. Bir Modül, FreeCAD\'in bir uzantısıdır, Tezgah ise bazı araç çubuklarını ve menüleri gruplayan özel bir GUI yapılandırmasıdır. Genellikle her modül kendi tezgahını içerir, bu nedenle ismin çapraz kullanımıdır.


</div>

## Yerleşik tezgahlar 


<div class="mw-translate-fuzzy">

Aşağıdaki tezgahlar bütün FreeCAD kurulumlarında bulunur:


</div>

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar as the Part Shape builder Face from edges.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Deprecated

The following workbenches are still included in the base installation for compatibility purposes, but they should no longer be used.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## Program dışı tezgahlar 


<div class="mw-translate-fuzzy">

FreeCAD çalışma tezgahlarının Python\'da programlanması kolaydır , bu nedenle FreeCAD ana geliştiricilerinin dışında ek çalışma tezgahları geliştiren birçok insan vardır.


</div>


<div class="mw-translate-fuzzy">

[3. Parti tezgahlar](external_workbenches.md) sayfasında, bu tezgahlardan bir kısmı hakkında bilgi bulabilir ve kılavuzlarına ulaşabilirsiniz. Ayrıca [FreeCAD Eklentileri](https://github.com/FreeCAD/FreeCAD-addons) projesi bu çalışmaları FreeCAD içinden kolayca yüklenebilir hale getirmeyi amaçlamaktadır.


</div>


<div class="mw-translate-fuzzy">

Yeni tezgahlar geliştiriliyor, bizi izlemeye devam edin!


</div>


<div class="mw-translate-fuzzy">


{{docnav/tr|[Özellik Penceresi](Property_editor/tr.md)|[Parça Tasarım Tezgahı](PartDesign_Workbench/tr.md)}}


</div>




[Category:Workbenches](Category:Workbenches.md)
