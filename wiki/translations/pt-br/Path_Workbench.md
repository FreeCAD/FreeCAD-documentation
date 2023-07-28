# <img alt="ícone da bancada de trabalho Path" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/pt-br


{{TOCright}}



## Introdução


<div class="mw-translate-fuzzy">

A <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [bancada de trabalho Path](Path_Workbench/pt-br.md) é utilizada para produzir instruções de máquina para [máquinas CNC](https://en.wikipedia.org/wiki/CNC_router) a partir de um modelo 3D do FreeCAD. Elas produzem objetos 3D do mundo real em máquinas CNC, como moinhos, tornos, lascadores ou similares. Normalmente, as instruções são um dialeto [G-Code](https://en.wikipedia.org/wiki/G-Code).


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

O fluxo de trabalho da bancada Path do FreeCAD Path cria essas instruções de máquina da seguinte maneira:

-   Um modelo 3D é o objeto base, normalmente criado usando uma ou mais das Bancadas de trabalho [ Part Design](PartDesign_Workbench/pt-br.md), [ Part](Part_Workbench/pt-br.md) ou [ Draft](Draft_Workbench/pt-br.md).
-   Um [ Trabalho](Path_Job/pt-br.md) é criado na bancada Path. Este contém todas as informações necessárias para gerar o G-Code necessário para processar o trabalho em uma fresadora CNC: há material de estoque, a fresadora possui um determinado [ conjunto de ferramentas](Path_ToolLibraryEdit/pt-br.md) e segue certos comandos controlando a velocidade e os movimentos (geralmente G-Code).
-   As ferramentas são selecionadas conforme exigido pelas operações do trabalho.
-   Os caminhos de fresagem são criados usando, por exemplo, operações [ Contorno](Path_Profile/pt-br.md) e [ Corte](Path_Pocket_3D/pt-br.md). Estes Objetos de caminho usam o dialeto interno do G-Code do FreeCAD, independente da máquina CNC.
-   Exporte o trabalho com um G-Code, correspondente à sua máquina. Essa etapa é chamada de \"pós-processamento\"; existem diferentes pós-processadores disponíveis.


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## Conceitos gerais 

A bancada gera o G-Code que define os caminhos necessários para usinar o projeto representado pelo modelo 3D na fresadora alvo em [o caminho Tarefas de trabalho FreeCAD G- Dialeto de código](Path_scripting/pt-br#The_FreeCAD_Internal_GCode_Format.md), que é posteriormente traduzido para o dialeto apropriado para o controlador CNC de destino, selecionando o pós-processador apropriado.

O G-Code é gerado a partir de diretivas e operações contidas em um trabalho de caminho. O Fluxo de Trabalho das listas na ordem em que serão executados. A lista é preenchida com a adição de Operações de Caminho, Dressups de Caminho, Comandos Parciais de Caminho e Modificações de Caminho do Menu de Caminho ou botões da GUI.


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


<div class="mw-translate-fuzzy">

A bancada Path fornece ferramentas de Gerenciador de Ferramentas (Biblioteca, Tabela de Ferramentas), Inspeção de Código G e Simulação. Ela vincula o pós-processador e permite importar e exportar modelos de trabalho.


</div>


<div class="mw-translate-fuzzy">

A bancada de trabalho Path tem dependências externas, incluindo:

1.  As unidades do modelo FreeCAD 3D são definidas nas configurações de {{MenuCommand | Editar → Preferências → Geral → Unidades da unidade}}. A configuração do pós-processador define as unidades finais do G-Code.
2.  O caminho do arquivo de macro e as tolerâncias geométricas são definidas na guia {{MenuCommand | Editar → Preferências → Caminho → Preferências de trabalho}}.
3.  As cores são definidas na guia {{MenuCommand | Editar → Preferências → Caminho → Cores do caminho}}.
4.  Os parâmetros da tag de retenção são definidos na guia {{MenuCommand | Editar → Preferências → Caminho → Dressups}}.
5.  Essa qualidade do modelo Base 3D suporta os requisitos da bancada de trabalho Path, passa a verificar geometria.


</div>



## Limitações


<div class="mw-translate-fuzzy">

Algumas das limitações atuais das quais você deve estar ciente são: A maioria das ferramentas Path Tools não são verdadeiras ferramentas 3D, mas apenas 2.5D capazes. Isto significa que elas assumem uma forma 2D fixa e podem cortá-lo até uma determinada profundidade. Entretanto, existem duas ferramentas que produzem verdadeiros caminhos em 3D:**<img src="images/Path_3DPocket.svg" width=24px> [Fenda 3D](Path_Pocket_3D/pt-br.md)** e **<img src="images/Path_Surface.svg" width=24px> [Superfície 3D](Path_Surface/pt-br.md)** (que ainda é um [recurso experimental](Path_experimental/pt-br.md) a partir de novembro 2020).

-   A maior parte da bancada de trabalho Path foi projetada para uma fresa/router CNC de 3 eixos (xyz) simples e padrão, mas as ferramentas de torno estão em desenvolvimento em 0,19_pre.
-   A maioria das operações na bancada de trabalho Path retornará caminhos baseados apenas em uma ferramenta padrão de fresa/bit, independentemente do tipo de ferramenta/bit atribuído em um determinado controlador de ferramentas, com exceção dos **<img src="images/Path_Engrave.svg" width=24px> [Gravação](Path_Engrave/pt-br.md)** e **<img src="images/Path_Surface.svg" width=24px> [Superfície 3D](Path_Surface/pt-br.md)** operações.
-   As operações dentro da bancada de trabalho Path não estão conscientes dos mecanismos de fixação em uso para fixar o modelo à sua máquina. Consequentemente, por favor, revise e simule os caminhos que você gera antes de enviar o código para sua máquina. Se necessário, modele seus mecanismos de fixação no FreeCAD a fim de inspecionar melhor os caminhos gerados. Procure por possíveis colisões com grampos ou outros obstáculos ao longo dos caminhos.


</div>



## Unidades

A manipulação de unidades no Path pode ser confusa. Existem vários pontos para entender:

1.  As unidades base do FreeCAD para comprimento e hora são \'mm\' e \'s\' respectivamente. A velocidade é, portanto, \'mm / s\'. Isto é o que o FreeCAD armazena internamente, independentemente de qualquer outra coisa.
2.  O esquema unitário padrão usa as unidades padrão. Se você estiver usando o esquema padrão e inserir uma velocidade de avanço sem uma string de unidade, ela será inserida como \'mm / s\'.
3.  A maioria das máquinas CNC espera uma velocidade de avanço na forma de \'mm / min\' ou \'in / min\'. A maioria dos pós-processadores converterá automaticamente a unidade ao gerar o G-Code.

Esquemas:

1.  Alterar esquema nas preferências altera a sequência de unidades padrão para os campos de entrada. Se você é um usuário do Path e prefere projetar em métrica, é altamente recomendável usar o esquema \"Metric Small Parts & CNC\". Se você projetar em unidades dos EUA, o Imperial Decimal e o Building US funcionarão.
2.  Alterar seu esquema de unidade preferencial não afetará a saída, mas ajudará a evitar erros de entrada.

Saída:

1.  Gerar a unidade correta na saída é de responsabilidade do pós-processador e é feito somente naquele momento.
2.  A unidade de saída da máquina não tem relação alguma com o esquema de unidade selecionado.
3.  Os pós-processadores produzem uma saída métrica (G21), uma saída Imperial (G20) ou são configuráveis.
4.  Configuráveis pós-processadores padrão para métrica (G21).
5.  Se você quiser que seu pós-processador configurável gere o código imperial (G20), defina o argumento correto na configuração de saída do trabalho (ou seja, inches para linuxcnc). Isso pode ser armazenado em um modelo de trabalho e definido como seu modelo padrão para torná-lo automático para todos os trabalhos futuros.

Inspeção de caminho:

1.  Se você usar a ferramenta Inspecionar Caminho para ver o G-Code, verá em \'mm/s\' porque não está sendo pós-processado.

## Heights and depths 


<div class="mw-translate-fuzzy">

## Comandos do Path 

Muitos dos comandos têm várias alturas e profundidades: <img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Referência visual para propriedades de profundidade (configurações)*


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Trabalho](Path_Job/pt-br.md): Cria um novo trabalho CNC.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Post.svg  style="width:32px;"> [Pós-processar](Path_Post/pt-br.md): Exporta um projeto para o G-Code.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Erros do Path](Path_Sanity/pt-br.md): Verifica valores ausentes para os trabalhos (Job) selecionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Exportar Template](Path_ExportTemplate/pt-br.md): Exporta o trabalho atual como um modelo (template).


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Inspecionar G-Code](Path_Inspect/pt-br.md): Mostra o G-Code para verificação.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Simulador](Path_Simulator/pt-br.md): Mostra a operação de fresagem como é feita na maquina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Completar volta](Path_SelectLoop/pt-br.md): Completa uma volta a partir de duas arestas selecionadas.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Operação ativar](Path_OpActiveToggle/pt-br.md): Utilizada para ativar ou desativar uma operação de caminho.


</div>

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock.




<div class="mw-translate-fuzzy">

### Operações de Caminho Básico 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Perfil](Path_Profile/pt-br.md) (New in 0.19): Cria uma operação de perfil de todo o modelo, ou a partir de uma ou mais faces ou bordas selecionadas. Esta operação combina o Contorno, Faces de Perfil e Arestas de Perfil pré-existentes.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Corte](Path_Pocket_Shape/pt-br.md): Cria uma operação de corte (furo) a partir de um ou mais cortes selecionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Perfuração](Path_Drilling/pt-br.md): Executa um ciclo de perfuração.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Face.svg  style="width:32px;"> [Fresar face](Path_MillFace/pt-br.md): Cria um caminho de superfície.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Helix.svg  style="width:32px;"> [Hélice](Path_Helix/pt-br.md): Cria um caminho helicoidal.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptativo](Path_Adaptive/pt-br.md): Cria uma operação de limpeza e perfilagem adaptativa


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Fenda](Path_Slot/pt-br.md) (New in 0.19): Cria uma operação de slotting a partir de características selecionadas ou pontos personalizados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Engrave.svg  style="width:32px;"> [Gravação](Path_Engrave/pt-br.md): Cria um caminho de gravação.


</div>

-   <img alt="" src=images/Path_Deburr.svg  style="width:32px;"> [Deburr](Path_Deburr.md): Creates a deburr path.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Fenda V](Path_Vcarve/pt-br.md): Cria um caminho para uma cavidade 3D


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DPocket.svg  style="width:32px;"> [Fenda 3D](Path_Pocket_3D/pt-br.md): Cria um caminho para o corte 3D.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [Superfície 3D](Path_Surface/pt-br.md): Cria um caminho para uma superfície 3D.(experimental, 0.19)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Contorno por linhas de nível](Path_Waterline/pt-br.md): Cria uma trama de linha de nível para uma superfície 3D (experimental, 0.19)


</div>




<div class="mw-translate-fuzzy">

### Otimização de percurso 


</div>

-   <img alt="" src=images/Path_DressupAxisMap.svg  style="width:32px;"> [Axis Map](Path_DressupAxisMap.md): Remaps one axis to another.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Limitação de contorno](Path_DressupPathBoundary/pt-br.md): acrescenta um contorno de restrição de rota a uma rota selecionada.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Trabalhando os cantos](Path_DressupDogbone/pt-br.md): Adiciona uma modificação para usinagem de cantos a uma trajetória de usinagem selecionada


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Usinage com estilete](Path_DressupDragKnife/pt-br.md): Adiciona uma modificação de usinage com estilete ao caminho selecionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [Ponto de entrada ou saída](Path_DressupLeadInOut/pt-br.md): Adiciona um ponto de entrada ou saída ao caminho selecionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [ Rampa de entrada](Path_DressupRampEntry/pt-br.md): Adiciona uma rampa de entrada de usinagem a uma trajetória de usinagem selecionada.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Baliza de fixação](Path_DressupTag/pt-br.md): Adiciona uma modificação de baliza de fixação a um caminho selecionado.


</div>

-   <img alt="" src=images/Path_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](Path_DressupZCorrect.md): Corrects the Z depth using Probe Map.




<div class="mw-translate-fuzzy">

### Comandos Parciais 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Fixação](Path_Fixture/pt-br.md): Modifica a posição da fixação.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Comentário](Path_Comment/pt-br.md): Insere um comentário no G-Code de um caminho.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Parada](Path_Stop/pt-br.md): Insere um ponto final da máquina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Customização](Path_Custom/pt-br.md): Insere um G-Code customizado.


</div>

-   <img alt="" src=images/Path_Probe.svg  style="width:32px;"> [Probe](Path_Probe.md): Creates a Probing Grid from a job stock.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_GcodeFromShape.svg  style="width:32px;"> [G-Code para um contorno](Path_Shape/pt-br.md): Cria um objeto de caminho de um objeto Part selecionado.


</div>




<div class="mw-translate-fuzzy">

### Modificações do Path 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Cópia](Path_Copy/pt-br.md): Cria uma cópia paramétrica de um objeto Path selecionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Matriz](Path_Array/pt-br.md): Cria uma matriz ao duplicar um caminho selecionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Cópia simples](Path_SimpleCopy/pt-br.md): Cria uma cópia não paramétrica de um objeto Path selecionado.


</div>

### Specialty Operations 

-   <img alt="" src=images/Path_ThreadMilling.svg  style="width:32px;"> [Thread Milling](Path_ThreadMilling.md): Creates a Path Thread Milling operation from features of a base object. [**Experimental**](Path_experimental.md).

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Feature area](Path_Area/pt-br.md): Cria uma área de recurso a partir de objetos selecionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Plano de trabalho da área de recursos](Path_Area_Workplane/pt-br.md): Cria um plano de trabalho da área de recursos.


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Gerenciador de ferramentas](Path_ToolLibraryEdit/pt-br.md): Edita o Gerenciador de ferramentas.


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

A bancada Path compartilha muitos conceitos com outros pacotes de software CAM, mas possui suas próprias peculiaridades. Se algo parece errado, isso pode ser um bom lugar para começar.


</div>




<div class="mw-translate-fuzzy">

### Preferências


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferências\...](Path_Preferences/pt-br.md): Preferências disponíveis nas ferramentas do Path.


</div>

## Scripting


<div class="mw-translate-fuzzy">

Confira a página [Path scripting](Path_scripting.md).


</div>

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.

## Roadmap

-   [Path Development Roadmap](Path_Development_Roadmap.md): Read this if you are a developer and want to contribute to Path.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/pt-br
