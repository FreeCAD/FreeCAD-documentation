# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/pt-br



Esta é a principal área de ajuda para os recém chegados ao FreeCAD.

O FreeCAD está em desenvolvimento contínuo, portanto, pode haver informações ausentes ou desatualizadas. Se você não encontrar as informações que precisa, não hesite em perguntar no [fórum do FreeCAD](https://forum.freecad.org).

Se você gostaria de contribuir com o FreeCAD, por favor, [faça uma doação](donate/pt-br.md), e veja a página [Ajude o FreeCAD](Help_FreeCAD/pt-br.md) para outras formas de contribuição. Se você gostaria de editar esta wiki, solicite uma conta de wiki com permissões de editor [no fórum](https://forum.freecad.org/viewtopic.php?f=21&t=6830), e leia as [WikiPages](WikiPages/pt-br.md) para as diretrizes gerais que você deve seguir.

Se você gostaria de saber como o FreeCAD começou anos atrás, visite a página [História](History/pt-br.md).



## Usando o FreeCAD 



### Introdução

-   [Visão geral do aplicativo](About_FreeCAD/pt-br.md): Uma visão geral do FreeCAD
-   Instalando: Como instalar o FreeCAD no [Windows](Installing_on_Windows/pt-br.md), [Linux](Installing_on_Linux/pt-br.md) e [Mac](Installing_on_Mac/pt-br.md)
-   [Instalando arquivos de ajuda](Installing_Helpfile/pt-br.md): como instalar a documentação offline baseada nesta wiki.
-   [Instalando componentes adicionais](Installing_additional_components/pt-br.md): como instalar componentes de terceiros adicionais que podem funcionar com o FreeCAD.
-   [Primeiros passos](Getting_started/pt-br.md): Uma visão geral rápida das ferramentas disponíveis
-   [Perguntas frequentes](Frequently_asked_questions/pt-br.md): Perguntas frequentemente feitas
-   [Tutoriais](Tutorials/pt-br.md) cobrindo diferentes partes do FreeCAD

#### Migrating from other software? 

-   [Soluções alternativas](Workarounds/pt-br.md)
-   [Migrando para o FreeCAD a partir do Fusion360](Migrating_to_FreeCAD_from_Fusion360/pt-br.md)
-   [Migrando para o FreeCAD a partir do OnShape](Migrating_to_FreeCAD_from_OnShape/pt-br.md)
-   [Migrando para o FreeCAD a partir do SolidWorks](Migrating_to_FreeCAD_from_SolidWorks/pt-br.md)
-   [Migrando para o FreeCAD a partir do Revit](Migrating_to_FreeCAD_from_Revit/pt-br.md)
-   [Guia de migração do FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [Tabela de compatibilidade de aplicativos BIM](BIM_application_compatibility_table/pt-br.md)



### Conceitos Básicos do Software 

-   [Interface](Interface/pt-br.md): a interface do FreeCAD é composta por vários elementos gráficos na tela, incluindo a [visão 3D](3D_view/pt-br.md), a [vista de árvore](Tree_view/pt-br.md), o [editor de propriedades](Property_editor/pt-br.md), o [painel de tarefas](Task_panel/pt-br.md) e o [console Python](Python_console/pt-br.md).
-   [Navegação com o mouse](Mouse_navigation/pt-br.md): os diferentes tipos de uso do mouse ou trackpad para navegar na visão 3D.
-   [Métodos de seleção](Selection_methods/pt-br.md): os diferentes métodos de seleção de objetos no software.
-   [Nomeação de objetos](Object_name/pt-br.md): os objetos do FreeCAD possuem um `Nome` somente leitura que os identifica de forma única, e um `Label` que é editável pelo usuário.
-   [Editor de Preferências](Preferences_Editor/pt-br.md): o sistema que permite controlar várias propriedades do sistema base e dos workbenches individuais.
-   [Formatos de arquivo](Import_Export/pt-br.md): os diferentes formatos de arquivo que o FreeCAD pode ler e escrever.



### \"Workbenches\" (Bancadas de trabalho) 

[Bancadas de trabalho](Workbenches/pt-br.md) são coleções de ferramentas usadas para tarefas específicas. Imagine que você está em seu espaço de trabalho, e nesse espaço há várias bancadas de trabalho, cada uma equipada com as ferramentas necessárias para realizar um tipo específico de tarefa. Por exemplo, uma bancada pode ser destinada à marcenaria, outra à pintura e outra à soldagem. Da mesma forma, no FreeCAD, cada workbench é uma bancada especializada com ferramentas para diferentes tipos de tarefas, como modelagem, desenho técnico, análise e mais. Esses workbenches são essenciais para otimizar seu fluxo de trabalho, oferecendo as ferramentas mais adequadas para cada tarefa específica.

<img alt="" src=images/Freecad.svg  style="width:32px;"> [Ferramentas padrão](Std_Base/pt-br.md). Esta não é uma bancada de trabalho propriamente dita, mas sim uma categoria de comandos e ferramentas \"padrão\" que podem ser utilizadas em todas as bancadas de trabalho. Essas ferramentas estão disponíveis em qualquer workbench e oferecem funcionalidades básicas e comuns, facilitando o trabalho em diversas tarefas, independentemente da bancada especializada que você esteja utilizando.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> O [Workbench de Montagem](Assembly_Workbench/pt-br.md) para a construção e resolução de montagens mecânicas. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> A [Bancada BIM](BIM_Workbench/pt-br.md) para trabalhar com elementos arquitetônicos e criar modelos de [BIM](https://en.wikipedia.org/wiki/Building_information_modeling). Ela combina a Bancada Arch e a antiga Bancada BIM que estava disponível na versão {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> A [Bancada CAM](CAM_Workbench/pt-br.md) é utilizada para produzir instruções em G-Code. Essa bancada era chamada de \"Bancada Path\" na versão {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> A [Bancada Draft](Draft_Workbench/pt-br.md) contém ferramentas 2D e operações básicas de CAD 2D e 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> A [Bancada FEM](FEM_Workbench/pt-br.md) fornece o fluxo de trabalho de Análise por Elementos Finitos (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> A [Bancada Inspection](Inspection_Workbench/pt-br.md) foi criada para fornecer ferramentas específicas para a análise de formas. Ainda está em estágios iniciais de desenvolvimento.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> A [Bancada Material](Material_Workbench/pt-br.md) gerencia o sistema de materiais do FreeCAD. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> A [Bancada Mesh](Mesh_Workbench/pt-br.md) para trabalhar com malhas trianguladas.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> A [Bancada OpenSCAD](OpenSCAD_Workbench/pt-br.md) para interoperabilidade com o OpenSCAD e reparo do histórico de modelos de [geometria sólida construtiva](Constructive_solid_geometry/pt-br.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> A [Bancada Part](Part_Workbench/pt-br.md) para trabalhar com primitivas geométricas e operações booleanas.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> A [Bancada Part Design](PartDesign_Workbench/pt-br.md) para criar formas de peças a partir de esboços.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> A [Bancada Points](Points_Workbench/pt-br.md) para trabalhar com nuvens de pontos.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> A [Bancada Reverse Engineering](Reverse_Engineering_Workbench/pt-br.md) é destinada a fornecer ferramentas específicas para converter formas/sólidos/malhas em recursos paramétricos compatíveis com o FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> A [Bancada Robot](Robot_Workbench/pt-br.md) para estudar os movimentos de robôs. Atualmente não está sendo mantida.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> A [Bancada Sketcher](Sketcher_Workbench/pt-br.md) para trabalhar com esboços restritos por geometria.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> A [Bancada Spreadsheet](Spreadsheet_Workbench/pt-br.md) para criar e manipular dados de planilhas.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> A [Bancada Surface](Surface_Workbench/pt-br.md) fornece ferramentas para criar e modificar superfícies. Ela é semelhante à opção \"Face from edges\" da [Bancada Part Builder](Part_Builder/pt-br.md), opção de face a partir das bordas.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> A [Bancada TechDraw](TechDraw_Workbench/pt-br.md) para produzir desenhos técnicos a partir de modelos 3D.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> A [Bancada Test Framework](Testing/pt-br.md) é para depuração do FreeCAD.

### Macros

[Macros](Macros/pt-br.md) são trechos relativamente pequenos de código [Python](Python/pt-br.md) que realizam tarefas simples ou complexas que não estão disponíveis no sistema base do FreeCAD.

Usuários avançados escreveram diversas [macros](macros/pt-br.md) para aprimorar o FreeCAD com mais funcionalidades.

Desde o FreeCAD 0.17, muitas macros podem ser instaladas usando o [Gerenciador de Addons](Std_AddonMgr/pt-br.md). Para uma lista das macros, consulte a página [Receitas de Macros](Macros_recipes/pt-br.md). Para instalação manual, veja [Como instalar macros](How_to_install_macros/pt-br.md).



### Bancadas de Trabalho Externas 

Quando muitas macros ou funções são desenvolvidas juntas e organizadas em barras de ferramentas e menus, elas podem se tornar uma nova bancada.

[Bancadas externas](External_workbenches/pt-br.md) são coleções de funções que não fazem parte do sistema base do FreeCAD, geralmente desenvolvidas por usuários experientes, e voltadas para uma necessidade específica.

Desde o FreeCAD 0.17, muitas bancadas podem ser instaladas usando o [Gerenciador de Addons](Std_AddonMgr/pt-br.md). Para instalação manual, veja [Como instalar bancadas adicionais](How_to_install_additional_workbenches/pt-br.md).



## Referências

-   [Referência de Comandos](List_of_Commands/pt-br.md): Uma lista completa dos comandos disponíveis no FreeCAD.



## Ajuda Online 

Esta é a ajuda online oficial do FreeCAD. Observe que todo o sistema de ajuda online está atualmente sendo reformulado. Ele será utilizado para gerar um arquivo .CHM, que será distribuído com os pacotes binários do FreeCAD. No momento, a ajuda online resume algumas das seções mais completas deste wiki.

-   [Sistema de ajuda online - Índice](Online_Help_Toc/pt-br.md)



## Mais Informações 

-   O [Hub de Usuários Avançados](Power_users_hub/pt-br.md) é o lugar para acessar exemplos de uso mais avançado do FreeCAD.
-   O [Portal da Comunidade FreeCAD](FreeCAD_Community_Portal/pt-br.md) lista projetos feitos por membros da comunidade em torno do FreeCAD.
-   Não entende um termo ou expressão usada no FreeCAD? Consulte a página [Glossário](Glossary/pt-br.md).



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/pt-br
