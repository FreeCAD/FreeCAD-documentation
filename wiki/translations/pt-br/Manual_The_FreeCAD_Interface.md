# Manual:The FreeCAD Interface/pt-br
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

O FreeCAD usa o [framework Qt](https://pt.wikipedia.org/wiki/Qt_(software)) para desenhar e gerenciar sua interface. Este framework é utilizado em uma ampla gama de aplicativos, o que faz com que a interface do FreeCAD seja bastante clássica e não apresente dificuldades para ser entendida. A maioria dos botões são padrão e podem ser encontrados onde você espera **Arquivo → Abrir, Editar → Colar, etc**. Aqui está a aparência do FreeCAD quando você o abre pela primeira vez, logo após a instalação, mostrando o centro de início:


</div>


<div class="mw-translate-fuzzy">

![](images/FreeCAD-v0-18-FirstStart.png )


</div>


<div class="mw-translate-fuzzy">

O centro de início é uma \"tela de boas-vindas\" conveniente, que exibe informações úteis para iniciantes, como os arquivos mais recentes com os quais você esteve trabalhando, as novidades no mundo do FreeCAD ou informações rápidas sobre as bancadas de trabalho mais comuns. Ele também notificará você se uma nova versão estável do FreeCAD estiver disponível.


</div>


<div class="mw-translate-fuzzy">

Com o tempo, à medida que você se familiariza mais com o FreeCAD, pode ter feito alterações nas preferências para que, quando o FreeCAD iniciar, você seja direcionado diretamente para uma das bancadas de trabalho com um novo documento aberto. Ou, simplesmente, feche a aba da página inicial e crie um novo documento:


</div>


<div class="mw-translate-fuzzy">

![nenhum](images/FreeCAD-v0-18-NewProject.png )


</div>



### \"Workbenches\" (Bancadas de trabalho) 


<div class="mw-translate-fuzzy">

As Bancadas de Trabalho são grupos de ferramentas (botões de barra de ferramentas, menus e outros controles da interface) que são agrupadas por especialidade. Pense em uma oficina onde diferentes pessoas trabalham juntas: uma pessoa que trabalha com metal, outra com madeira. Cada uma delas tem, em sua oficina, uma mesa separada com ferramentas específicas para o seu trabalho. No entanto, todas podem trabalhar nos mesmos objetos. O mesmo acontece no FreeCAD.


</div>

In the context of FreeCAD, each Workbench is tailored to a particular type of task, organizing all the necessary tools for that activity in one interface. When switching between Workbenches, the set of tools and controls visible in the user interface adjusts to reflect the needs of the selected task, though the actual project contents or \"scene\" you are working on does not change. This allows for seamless transitions in workflow, such as beginning a design with basic 2D shapes in the Draft Workbench and then elaborating on these designs with advanced modeling tools in the Part Workbench.

The terms \"Workbench\" and \"Module\" are sometimes used interchangeably, but they have distinct meanings within FreeCAD. A Module is any extension that adds functionality to FreeCAD, while a Workbench is a specific kind of Module equipped with its own user interface components such as toolbars and menus, designed to facilitate specific types of tasks. Thus, every Workbench is a Module, but not every Module qualifies as a Workbench.

O controle mais importante da interface do FreeCAD é o seletor de Bancada de Trabalho, que você usa para alternar de uma bancada de trabalho para outra:


<div class="mw-translate-fuzzy">

![nenhum](images/FreeCAD-v0-18-WorkbenchMenu.png )


</div>

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> The [Assembly Workbench](Assembly_Workbench.md) for building and solving mechanical assemblies. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> The [BIM Workbench](BIM_Workbench.md) for working with architectural elements and creating [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) models. It combines the Arch Workbench and the formerly external BIM Workbench available in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> The [CAM Workbench](CAM_Workbench.md) is used to produce G-Code instructions. This workbench was called \"Path Workbench\" in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for the examination of shapes. Still in the early stages of development.

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


<div class="mw-translate-fuzzy">

As Bancadas de Trabalho costumam confundir os novos usuários, pois nem sempre é fácil saber em qual bancada procurar uma ferramenta específica. Mas elas são rápidas de aprender, e após um curto período, isso se tornará natural --- percebendo que é uma maneira conveniente de organizar a grande quantidade de ferramentas que o FreeCAD oferece. As Bancadas de Trabalho também são totalmente personalizáveis (veja abaixo). A mesma ferramenta pode aparecer em mais de uma bancada de trabalho. O ícone do botão de uma ferramenta específica será sempre o mesmo, independentemente da bancada em que ela aparecer.


</div>



### A interface 

Vamos dar uma olhada mais detalhada nas diferentes partes da interface:


<div class="mw-translate-fuzzy">

![nenhum](images/FreeCAD-v0-18-Cube.png )


</div>

The main window of the application can be roughly divided into 11 sections:

1.  The [Main view area](Main_view_area.md), which can contain different tabbed windows.
2.  The [3D view](3D_view.md), normally embedded in the [main view area](Main_view_area.md). The 3D view is the central element of the interface, displaying and allowing manipulation of the objects you are working on. It is possible to have multiple views of the same document (or objects) or to have several documents open simultaneously. Additionally, each view can be detached from the main window separately.
3.  The Model and and the [Tasks](Task_panel.md) tab.
    1.  The Model tab shows you the contents and structure of your document.
    2.  The Tasks tab is where FreeCAD will prompt you for values specific to the workbench and tool you are currently using (for example dimensions of an object).
4.  The [Property editor](Property_editor.md) which appears when the Model tab is active in the interface. It allows managing the publicly exposed properties of the objects in the document. It consists of the Data and View sections, showing the visualization properties and the parametric properties of the objects respectively.
5.  The [Selection view](Selection_view.md) which indicates the objects or sub-elements of objects (vertices, edges, faces) that are selected.
6.  The [Report view](Report_view.md) where messages, warnings and errors are shown.
7.  The [Python console](Python_console.md).The Python console, where all the commands executed are printed, and where you can enter Python code.
8.  The [Status bar](Status_bar.md) where some messages and tooltips appear.
9.  The toolbar area, where the toolbars are docked.
10. The [workbench selector](Std_Workbench.md), where you select the active [workbench](Workbenches.md).
11. The [standard menu](Standard_Menu.md), which holds basic operations of the program.

Most of the above panels can be hidden or revealed using the **View → Panels menu**



### Personalizando a interface 


<div class="mw-translate-fuzzy">

A interface do FreeCAD é altamente personalizável. Todos os painéis e barras de ferramentas podem ser movidos para diferentes locais ou empilhados um sobre o outro. Eles também podem ser fechados e reabertos conforme necessário, a partir do menu Visualizar ou clicando com o botão direito em uma área vazia da interface. Existem, no entanto, muitas outras opções disponíveis, como criar barras de ferramentas personalizadas com ferramentas de qualquer uma das bancadas de trabalho, ou atribuir e alterar atalhos de teclado.


</div>

Essas opções avançadas de personalização estão disponíveis no menu **Ferramentas → Personalizar**:


<div class="mw-translate-fuzzy">

![nenhum](images/FreeCAD-v0-18-CustomizeInterface.png )


</div>

**Leia mais**

-   [Introdução ao FreeCAD](Getting_started/pt-br.md)
-   [Personalizando a interface](Interface_Customization/pt-br.md)
-   [Bancadas (Workbenches)](Workbenches/pt-br.md)
-   [Mais sobre Python](https://www.python.org)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD Interface/pt-br
