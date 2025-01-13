# Workbenches/pt
O FreeCAD, como outros programas como o [Revit](wikipedia_Revit.md) ou [Catia](wikipedia_CATIA.md), é baseado no conceito de bancadas. Uma bancada pode ser considerada como um conjunto de ferramentas agrupadas para fazer uma certa tarefa. Numa oficina de carpintaria tradicional, haveria uma mesa para a pessoa que trabalha com madeira, outra para peças metálicas, e talvez uma terceira para a pessoa que faz a montagem das várias peças.

No FreeCAD aplica-se o mesmo conceito. As ferramentas são agrupadas em bancadas de acordo com as tarefas em que são usadas.

Quando muda de uma bancada para a outra, as ferramentas disponíveis no interface mudam. As barras de ferramentas, barras de comandos e eventualmente outras partes do interface mudam com a nova bancada, mas os conteúdos do seu trabalho não mudam. Poderia, por exemplo, começar a desenhar formas em 2D com a Bancada de Desenho, e depois fazer mais trabalho na Bancada de Peças.

Perceba que algumas vezes um Bancada é referida como um *Módulo*. Entretanto, Bancadas e Módulos são entidades diferentes. Um Módulo é qualquer extensão do FreeCAD, enquanto uma Bancada é um tipo especial de Módulo com uma configuração de GUI (barras de ferramentas e menus)



## Bancadas de Trabalho Pré-instaladas 



### Atual

As seguintes Bancadas são disponibilizadas com qualquer instalação do FreeCAD

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). Essa não é realmente uma bancada, mas sim uma categoria de comandos e ferramentas \"padrões\" que podem ser usadas em todas bancadas.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> A [Bancada Assembly](Assembly_Workbench.md) para construção e resolução de montagens mecânicas. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> A [Bancada BIM](BIM_Workbench.md) para trabalho com elementos e criação de modelos arquiteturais [BIM](https://en.wikipedia.org/wiki/Building_information_modeling). Ela combina a Bancada Arch e a antiga Bancada externa BIM disponível em {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> The [CAM Workbench](CAM_Workbench.md) is used to produce G-Code instructions. This workbench was called \"Path Workbench\" in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. Still in the early stages of development.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> The [Material Workbench](Material_Workbench.md) handles the FreeCAD material system. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with geometric primitives and boolean operations.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements. Currently unmaintained.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.



### Obsoleto

As seguintes bancadas de trabalho não estão mais incluídos após a versão 0.21:

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

The following workbenches are no longer included after version 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) was used for working with bitmap images. Its functionality has been integrated in [Std Base](Std_Base.md). See [Std Import](Std_Import.md) and [Std ViewLoadImage](Std_ViewLoadImage.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) was used for ray-tracing (rendering). The external [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) should be used instead.

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main development area.

The [external workbenches](External_workbenches.md) page lists all that are known to this community. Most are easily installable from within FreeCAD, using the [Addon Manager](Std_AddonMgr.md), found under menu **Tools → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/pt
