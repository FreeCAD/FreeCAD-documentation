# Workbenches/pt-br
O FreeCAD, como muitos aplicativos de design modernos, como [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit) ou [CATIA](https://en.wikipedia.org/wiki/CATIA), baseia-se no conceito de [Workbench](https://en.wikipedia.org/wiki/Workbench) (Bancada de trabalho). Uma bancada de trabalho pode ser considerada um conjunto de ferramentas especialmente agrupadas para uma determinada tarefa. Em uma oficina de móveis tradicional, você teria uma mesa de trabalho para quem trabalha com madeira, outra para quem trabalha com peças de metal e talvez uma terceira para quem monta todas as peças.

No FreeCAD aplica-se o mesmo conceito. As ferramentas são agrupadas em bancadas, segundo as tarefas em que são utilizadas.

Quando você muda de uma bancada para outra, as ferramentas disponíveis na interface mudam. Barras de ferramentas, barras de comando e possivelmente outras partes da interface mudam para a nova bancada de trabalho, mas o conteúdo de sua cena não muda. Você poderia, por exemplo, começar a desenhar formas 2D com a Bancada Draft e, em seguida, trabalhar mais neles com a Bancada Part.

Perceba que algumas vezes um Bancada é referida como um *Módulo*. Entretanto, Bancadas e Módulos são entidades diferentes. Um Módulo é qualquer extensão do FreeCAD, enquanto uma Bancada é um tipo especial de Módulo com uma configuração de GUI (barras de ferramentas e menus)



## Bancadas de Trabalho Pré-instaladas 



### Atual

As seguintes bancadas de trabalho estão disponíveis em todas as instalações do FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). Essa não é realmente uma bancada, mas sim uma categoria de comandos e ferramentas \"padrões\" que podem ser usadas em todas bancadas.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> A [Bancada Assembly](Assembly_Workbench.md) para construção e resolução de montagens mecânicas. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> A [Bancada BIM](BIM_Workbench.md) para trabalho com elementos e criação de modelos arquiteturais [BIM](https://en.wikipedia.org/wiki/Building_information_modeling). Ela combina a Bancada Arch e a antiga Bancada externa BIM disponível em {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> A [Bancada CAM](CAM_Workbench.md) é usada para produzir instruções G-Code. Essa Bancada era chamada \"Bancada Path\" na {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> A [Bancada Draft](Draft_Workbench/pt-br.md) contém ferramentas 2D e operações básicas CAD 2D e 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> A [Bancada FEM](FEM_Workbench/pt-br.md) fornece um fluxo de trabalho de Análise de Elementos Finitos (em inglês, FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> A [Bancada Inspection](Inspection_Workbench/pt-br.md) é feita para disponibilizar ferramentas específicas para o exame das formas. Ela está nos estágios iniciais de desenvolvimento.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> A [Bancada Material](Material_Workbench.md) manipula o sistema de material do FreeCAD. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> A [bancada de trabalho Mesh](Mesh_Workbench/pt-br.md) é usada para trabalhar com malhas trianguladas.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> A [Bancada de trabalho OpenSCAD](OpenSCAD_Workbench/pt-br.md) como interoperabilidade com OpenSCAD e reparo da história do modelo [ geometria sólida construtiva](constructive_solid_geometry/pt-br.md)(CSG) história do modelo.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> A [Bancada Part](Part_Workbench.md) é para trabalhar com primitivas geométricas e operações booleanas.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> A [Bancada Part Design](PartDesign_Workbench/pt-br.md) usada para a construção de formas de peças a partir de esboços.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> A [bancada Points](Points_Workbench/pt-br.md) usada para trabalhar com nuvens de pontos.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> A [Bancada Reverse Engineering ](Reverse_Engineering_Workbench/pt-br.md) destina-se a fornecer ferramentas específicas para converter formas/sólidos/malhas em características paramétricas compatíveis com o FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> A [Bancada Robot](Robot_Workbench/pt-br.md) serve para o estudo dos movimentos dos robôs. Atualmente está sem manutenção.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> A [Bancada Sketcher](Sketcher_Workbench/pt-br.md) serve para trabalhar com esboços com restrições geométricas.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> A [Bancada Spreadsheet](Spreadsheet_Workbench/pt-br.md) serve para a criação e manipulação de dados de planilhas.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> A [Bancada Surface](Surface_Workbench/pt-br.md) fornece ferramentas para criar e modificar superfícies. É similar a opção [Construtor de formas](Part_Builder/pt-br.md) da face a partir das bordas.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> A [Bancada TechDraw](TechDraw_Workbench/pt-br.md) é usada para a produção de desenhos técnicos a partir de modelos 3D. É o sucessor da [Bancada Drawing](Drawing_Workbench/pt-br.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> A [Bancada Test Framework](Testing/pt-br.md) é para a depuração do FreeCAD.



### Obsoleto

As seguintes bancadas de trabalho não estão mais incluídos após a versão 0.21:

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> A [Bancada Start Center](Start_Workbench/pt-br.md) permite saltar rapidamente para uma das bancadas de trabalho mais comuns.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> A [Bancada Web](Web_Workbench/pt-br.md) fornece a você uma janela do navegador em vez da [vista 3D](3D_view/pt-br.md) dentro do FreeCAD.

As seguintes bancadas de trabalho não estão mais incluídos após a versão 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> A [Bancada Drawing](Drawing_Workbench.md) era utilizada para produção de desenhos técnicos. A [Bancada TechDraw](TechDraw_Workbench.md) é a substituta mais avançada.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> A [Bancada Image](Image_Workbench.md) era utilizada para trabalhar com imagens bitmap. Suas funcionalidades foram integradas na [Std Base](Std_Base.md). Veja [Std Import](Std_Import.md) e [Std ViewLoadImage](Std_ViewLoadImage.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> A [Bancada Raytracing](Raytracing_Workbench.md) era utilizada para ray-tracing (renderização). A Bancada externa [ Render](https://github.com/FreeCAD/FreeCAD-render.md) deve ser utilizada no seu lugar.



## Bancadas de Trabalho Externas 

As bancadas de trabalho do FreeCAD são fáceis de programar em [Python](Python/pt-br.md), portanto há muitas pessoas desenvolvendo bancadas de trabalho adicionais fora da área de desenvolvimento principal do FreeCAD.

A página de bancadas de trabalho externas ([Bancadas de trabalho externas](external_workbenches/pt-br.md)) lista todas as que são conhecidas por esta comunidade. A maioria é facilmente instalável de dentro do FreeCAD, usando o [Gerenciador de Extensões](Std_AddonMgr/pt-br.md), encontrado no menu **Ferramentas → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/pt-br
