# <img alt="Ícone da bancada de trabalho Arch" src=images/Workbench_Arch.svg  style="width:64px;"> Arch Workbench/pt-br


{{TOCright}}

## Introdução

A bancada de trabalho Arch fornece um moderno _.

A bancada Arch importa todas as ferramentas da [Bancada Draft](Draft_Workbench.md), pois usa objetos 2D para construir seus objetos arquitetônicos. No entanto, a Arch também pode usar objetos sólidos criados em outras bancadas, como a [ Bancada Part](Part_Workbench.md) e a [ Bancada PartDesign](PartDesign_Workbench.md).

A funcionalidade BIM do FreeCAD agora está dividida progressivamente nesta Bancada, que contém ferramentas arquitetônicas básicas, e no [BIM Workbench](BIM_Workbench.md), que você pode instalar através do [ Gerenciador de Complementos](Std_AddonMgr.md). Este ambiente de trabalho adiciona uma nova camada de interface às ferramentas do Arch, com o objetivo de tornar o fluxo de trabalho BIM no FreeCAD mais intuitivo e fácil de usar.

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Ferramentas

Estas são as ferramentas para criar objetos arquitetônicos:

-   <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [Parede](Arch_Wall/pt-br.md): cria uma parede usando um esboço ou usando um objeto selecionado como base (arame, face ou sólido).
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Muro cortina](Arch_CurtainWall/pt-br.md): cria uma fachada contínua a partir do zero ou usando um objeto selecionado como base. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [Elemento estrutural](Arch_Structure/pt-br.md): cria um elemento estrutural usando um esboço ou usando um objeto selecionado como base (esboço, arame, face ou sólido).

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Ferramenta de Armadura](Arch_CompRebarStraight/pt-br.md): o complemento Reinforcement aumenta as estruturas de bancada de trabalho do Arch.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Armadura reta](Arch_Rebar_Straight/pt-br.md): cria um armadura reta em um elemento estrutural selecionado.
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [Armadura U](Arch_Rebar_UShape/pt-br.md): cria uma armadura em forma de U em um elemento estrutural selecionado.
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Armadura L](Arch_Rebar_LShape/pt-br.md): cria uma armadura em forma de L em um elemento estrutural selecionado.
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Armadura moldada](Arch_Rebar_BentShape/pt-br.md): cria uma armadura moldada em um elemento estrutural selecionado.
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Estribo de vergalhão](Arch_Rebar_Stirrup/pt-br.md): cria uma barra de reforço em forma de estribo no elemento estrutural selecionado.
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Armadura helicoidal](Arch_Rebar_Helical/pt-br.md): cria uma barra de reforço helicoidal em um elemento estrutural selecionado.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Armadura de pilar](Arch_Rebar_ColumnReinforcement/pt-br.md): cria barras de reforço dentro de uma estrutura de coluna da Arch.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Reforço de pilares com duas braçadeiras e seis barras](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/pt-br.md): cria barras de reforço dentro de um objeto de estrutura de pilar na Arch.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [Armadura de reforço de viga](Arch_Rebar_BeamReinforcement/pt-br.md): cria barras de reforço dentro de um objeto de estrutura de viga na Arch.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Vergalhão](Arch_Rebar/pt-br.md): cria um vergalhão personalizado em um elemento estrutural selecionado utilizando um esboço.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piso](Arch_Floor/pt-br.md): Cria um piso incluindo objetos selecionados.
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Parte de um edifício (nível)](Arch_BuildingPart/pt-br.md): Cria uma parte do edifício que inclui objetos selecionados.
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Edifício ](Arch_Building/pt-br.md): Cria um edifício composto pelos objetos selecionados.
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Terreno](Arch_Site/pt-br.md): Criar um sítio que inclua os objetos selecionados.
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projeto](Arch_Project/pt-br.md): Cria um projeto que inclui objetos selecionados.
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Referência](Arch_Reference/pt-br.md):Liga objetos de outro arquivo do FreeCAD neste documento.
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Janela](Arch_Window/pt-br.md): Cria uma janela usando um objeto selecionado como base.
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Plano de corte](Arch_SectionPlane/pt-br.md): Adiciona um objeto do Plano de Seção ao documento.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Ferramentas de eixo](Arch_CompAxis/pt-br.md): A ferramenta Eixo permite que você coloque uma série de eixos no documento atual.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Eixo](Arch_Axis/pt-br.md): Adiciona ao documento um conjunto de eixos de 1-direção
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Sistema de eixos](Arch_AxisSystem/pt-br.md): Adiciona ao documento um sistema de eixos composto de vários eixos
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grade](Arch_Grid/pt-br.md): Adiciona um objeto em forma de grade ao documento

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Telhado](Arch_Roof/pt-br.md): Cria um teto inclinado a partir de uma face selecionada
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Espaço](Arch_Space/pt-br.md): Cria um objeto espacial no documento
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Escadas](Arch_Stairs/pt-br.md): Cria um objeto escada no documento

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Ferramentas de painel](Arch_CompPanel/pt-br.md): Permite a construção de todos os tipos de elementos semelhantes a painéis.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Painel](Arch_Panel/pt-br.md): Cria um objeto de painel a partir de um objeto 2D selecionado
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Corte do painel](Arch_Panel_Cut/pt-br.md): Cria uma vista de corte 2D a partir de um painel <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Folha de Painel](Arch_Panel_Sheet/pt-br.md): Cria uma folha de corte 2D incluindo cortes de painel ou outros objetos 2D <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Ninho](Arch_Nest/pt-br.md): Permitir aninhar vários objetos planos dentro de uma forma de recipiente <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Estrutura](Arch_Frame/pt-br.md): Cria um objeto de estrutura a partir de um layout selecionado.
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Cerca](Arch_Fence/pt-br.md): Cria um objeto de cerca a partir de um poste e caminho selecionados. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Treliça](Arch_Truss/pt-br.md): Cria uma treliça a partir de uma linha selecionada a partir do zero. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Mobiliário](Arch_Equipment/pt-br.md): Cria um equipamento ou objeto de mobiliário
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Perfil](Arch_Profile/pt-br.md):Cria um perfil 2D paramétrico. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Ferramentas de tubulação](Arch_CompPipe/pt-br.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Tubo](Arch_Pipe/pt-br.md): Cria um tubo <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Conector de tubos](Arch_PipeConnector/pt-br.md): Cria uma conexão de canto ou em t entre 2 ou 3 tubos selecionados <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Ferramentas materiais](Arch_CompSetMaterial/pt-br.md): As ferramentas de Material permitem adicionar materiais ao documento ativo.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial/pt-br.md): Cria um material e o atribui a objetos selecionados, se houver
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Material](Arch_MultiMaterial/pt-br.md): Creata um multimaterial e o atribui a objetos selecionados, se houver <small>(v0.17)</small> 
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Cronograma](Arch_Schedule/pt-br.md): Cria diferentes tipos de cronograma

### Ferramentas de Modificação 

Estas são as ferramentas para modificar objetos arquitetônicos:

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Corte com uma linha](Arch_CutLine/pt-br.md): Cortar um objeto de acordo com uma linha. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Corte com plano](Arch_CutPlane/pt-br.md): Cortar um objeto de acordo com um plano.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Adicionar componente](Arch_Add/pt-br.md): Adiciona objetos a um componente
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remover componente](Arch_Remove/pt-br.md): Subtrai ou remove objetos de um componente
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Levantamento](Arch_Survey/pt-br.md): Entra ou sai do modo de levantamento

### Utilidades

Estas são as ferramentas adicionais para te ajudar em tarefas específicas.

!!FUZZY!!\* <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Componente](Arch_Component/pt-br.md): Cria um componente não paramétrico Arch.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> _).
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Dividir uma malha](Arch_SplitMesh/pt-br.md): Divide uma malha selecionada em componentes separados.
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Malha para uma forma ](Arch_MeshToShape/pt-br.md): Converte uma malha em uma forma, unificando as faces coplanares.
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [ Seleção de malhas não sólidas](Arch_SelectNonSolidMeshes/pt-br.md): Seleciona todas as malhas não sólidas a partir da seleção atual ou do documento.
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remover Forma](Arch_RemoveShape/pt-br.md): Tentativas de transformar um objeto Arch baseado em uma forma cúbica em um objeto totalmente paramétrico.
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Fechar furos](Arch_CloseHoles/pt-br.md): Fecha furos em um objeto baseado em forma selecionada.
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [ Fusão de paredes](Arch_MergeWalls/pt-br.md): Fundir duas ou mais paredes.
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Verifique](Arch_Check/pt-br.md): Verificar se os objetos selecionados são sólidos e não contêm defeitos.
-   <img alt="" src=images/IFC.svg  style="width:32px;"> _.
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Comutar a bandeira Brep do IFC](Arch_ToggleIfcBrepFlag/pt-br.md): Força um objeto selecionado a ser exportado como um [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> _.
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> _ de um objeto.
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Alternar Subcomponentes](Arch_ToggleSubs/pt-br.md): Mostra ou oculta os subcomponentes de um objeto da Arch.

### Preferências

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferências](Arch_Preferences/pt-br.md): preferências em relação à aparência padrão de paredes, estruturas, vergalhões, janelas, escadas, painéis, tubos, grades e eixos.

### Formatos de arquivos 

-   [IFC](Arch_IFC/pt-br.md): classes de fundação da indústria
-   [DAE](Arch_DAE/pt-br.md): Formato de malha Collada
-   [OBJ](Arch_OBJ/pt-br.md): Formato da malha objeto (somente exportação)
-   [JSON](Arch_JSON/pt-br.md): Formato JavaScript Object Notation (somente exportação)
-   [3DS](Arch_3DS/pt-br.md): Formato 3DS (somente importação)
-   [SHP](Arch_SHP/pt-br.md): Arquivos em forma de GIS (somente importação)

## API

A bancada (módulo) Arch pode ser usado em scripts [Python](Python/pt-br.md) e [macros](macros/pt-br.md) usando as funções [Arch Python API](http://www.freecadweb.org/api/Arch.html).

## Tutoriais

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): Um exemplo de como o FreeCAD pode começar a ter seu lugar preliminar em um fluxo de trabalho de arquitetura.
-   [Tutorial Arch](Arch_tutorial/pt-br.md) (v0.14)
-   [Visão geral rápida da Arch no blog de Yorik](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Apresentação em vídeo da bancada de trabalho Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Tutorial do painel da Arch ](Arch_panel_tutorial/pt-br.md) (v0.15)
-   _
-   [Importação de STL ou OBJ](Import_from_STL_or_OBJ/pt-br.md)
-   [Exportação para STL ou OBJ](Export_to_STL_or_OBJ/pt-br.md)





 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Arch Workbench/pt-br
