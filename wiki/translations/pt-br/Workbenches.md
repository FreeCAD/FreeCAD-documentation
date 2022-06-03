# Workbenches/pt-br
O FreeCAD, como muitos aplicativos de design modernos, como [Revit](wikipedia_Revit.md) ou [CATIA](wikipedia_CATIA.md), baseia-se no conceito de [Workbench](wikipedia_Workbench.md) (Bancada de trabalho). Uma bancada de trabalho pode ser considerada um conjunto de ferramentas especialmente agrupadas para uma determinada tarefa. Em uma oficina de móveis tradicional, você teria uma mesa de trabalho para quem trabalha com madeira, outra para quem trabalha com peças de metal e talvez uma terceira para quem monta todas as peças.

No FreeCAD aplica-se o mesmo conceito. As ferramentas são agrupadas em bancadas, de acordo com as tarefas em que são utilizadas.

Quando você muda de uma bancada para outra, as ferramentas disponíveis na interface mudam. Barras de ferramentas, barras de comando e possivelmente outras partes da interface mudam para a nova bancada de trabalho, mas o conteúdo de sua cena não muda. Você poderia, por exemplo, começar a desenhar formas 2D com o Draft Workbench e, em seguida, trabalhar mais neles com o Part Workbench.


<div class="mw-translate-fuzzy">

Observe que às vezes uma bancada de trabalho é referida como sendo um *Módulo*. No entanto, Bancadas de Trabalho e Módulos são entidades diferentes. Um módulo é qualquer extensão do FreeCAD, enquanto uma bancada de trabalho é uma configuração de GUI especial que agrupa algumas barras de ferramentas e menus. Normalmente, cada módulo contém sua própria bancada de trabalho, daí o uso cruzado do nome.


</div>

## Bancadas de Trabalho Pré-instaladas 


<div class="mw-translate-fuzzy">

As seguintes bancadas de trabalho estão disponíveis em todas as instalações do FreeCAD   *


</div>

-   <img alt="" src=images/Freecad.svg  style="width   *32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width   *32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width   *32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width   *32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width   *32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width   *32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width   *32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width   *32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width   *32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width   *32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width   *32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width   *32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width   *32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width   *32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width   *32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width   *32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width   *32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width   *32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width   *32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width   *32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width   *32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width   *32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Descontinuadas


<div class="mw-translate-fuzzy">

As seguintes bancadas de trabalho ainda estão incluídas na instalação básica para fins de compatibilidade, mas não devem mais ser usadas.

-   <img alt="" src=images/Workbench_Complete.svg  style="width   *32px;"> [Complete Workbench](Complete_Workbench.md)   * Contém todos os comandos e recursos de todos os módulos e bancadas que atendem a certos critérios de qualidade. {{Obsolete|0.17}}
-   <img alt="" src=images/Workbench_Drawing.svg  style="width   *32px;"> [Drawing Workbench](Drawing_Workbench.md)   * Era usada para exibir trabalhos 3D em uma folha 2D, mas foi descontinuada; ainda é necessária para ler arquivos antigos do FreeCAD que contêm objetos de desenho originalmente feitos com esta bancada. Veja [TechDraw Workbench](TechDraw_Workbench.md), que é uma substituição mais avançada. {{Obsolete|0.17}}


</div>

-   <img alt="" src=images/Workbench_Complete.svg  style="width   *32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width   *32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## Bancadas de Trabalho Externas 

As bancadas de trabalho do FreeCAD são fáceis de programar em [Python](Python/pt-br.md), portanto há muitas pessoas desenvolvendo bancadas de trabalho adicionais fora da área de desenvolvimento principal do FreeCAD.


<div class="mw-translate-fuzzy">

A página de bancadas de trabalho externas ([Bancadas de trabalho externas](external_workbenches/pt-br.md)) lista todas as que são conhecidas por esta comunidade. A maioria é facilmente instalável de dentro do FreeCAD, usando o [Gerenciador de Extensões](Std_AddonMgr/pt-br.md), encontrado no menu **Ferramentas → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**.


</div>

Novas bancadas de trabalho estão sempre em desenvolvimento. Fique atento!







[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/pt-br
