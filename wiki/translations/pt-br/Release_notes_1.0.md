# Release notes 1.0/pt-br
**FreeCAD 1.0** foi lançado em **18 de novembro de 2024**, e pode ser baixado na página [Download](Download/pt-br.md). Esta página lista todos os novos recursos e mudanças.

As notas de versão das versões anteriores do FreeCAD podem ser encontradas na [Lista de recursos](Feature_list/pt-br#Release_notes.md).



## Em memória: Bradley McLean (bgbsww) 

Embora estejamos felizes em apresentar esta nova versão, também estamos tristes em anunciar que nosso amigo e prolífico desenvolvedor do FreeCAD [bgbsww](https://github.com/bgbsww) faleceu algumas semanas antes do lançamento desta versão. Ele foi um dos principais arquitetos do esforço de correção do nomeamento topológico, escreveu muito código adicional e testes, e se tornou o especialista do FreeCAD em TNP. Ele também ajudou praticamente todos os outros desenvolvedores a se adaptarem ao novo algoritmo. Esta versão é dedicada a ele.



### Geral

+++
| <img alt="" src=images/TNP_fix_relnotes_1.0.PNG  style="width:320px;"> | O antigo [Problema de Nomeação Topológica](Topological_naming_problem/pt-br.md) finalmente foi resolvido graças ao esforço conjunto e ao trabalho árduo de vários desenvolvedores. O [algoritmo de Realthunder](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) foi cuidadosamente implementado e melhorado para funcionar na versão principal do FreeCAD. O projeto levou mais de um ano, e a implementação inicial foi finalizada com o seguinte PR que possibilitou as melhorias. O problema do TNP não está completamente resolvido, e melhorias adicionais virão na próxima versão. [Pull request #13705](https://github.com/FreeCAD/FreeCAD/pull/13705) |
+++

+++
| <img alt="" src=images/AssemblyExample_relnotes_1.0.png  style="width:320px;"> | O FreeCAD agora possui uma nova [Bancada de Montagem](Assembly_Workbench/pt-br.md), baseada no trabalho original feito para o que costumávamos chamar de \"[o outro FreeCAD](https://www.askoh.com/freecad/what_is_freecad/index.html)\", outro software, também chamado FreeCAD, com capacidades de simulação de movimento criadas ao mesmo tempo que o nosso. A portabilidade foi realizada pelo próprio autor do outro FreeCAD, [Dr. Aik-Siong Koh](https://www.askoh.com), e com essa mudança significativa, ambos os FreeCADs agora finalmente estão unidos. Leia abaixo para [mais informações](#Assembly_Workbench/pt-br.md). [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427) |
+++

+++
| <img alt="" src=images/Freecad.svg  style="width:320px;"> | O FreeCAD tem um novo logo. Ele foi selecionado entre os 5 vencedores do concurso público. As diretrizes de uso e um kit de logo estão disponíveis na página [Diretrizes de Marca do FreeCAD](https://fpa.freecad.org/handbook/process/logo.html). [Pull request #14284](https://github.com/FreeCAD/FreeCAD/pull/14284) |
+++



## Interface do Usuário 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_1.0.gif  style="width:320px;"> | Foi adicionado um indicador de centro de rotação. Este indicador é exibido quando a visão é rotacionada arrastando o mouse. Ele pode ser opcionalmente desabilitado nas preferências. Também há configurações para sua cor, transparência e tamanho. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) e [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_1.0.gif  style="width:320px;">Clique na imagem se a animação não começar.   Filtros de seleção [Selection filters](Part_SelectFilter.md) foram adicionados, facilitando a seleção de vértices, arestas e faces. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_1.0.png  style="width:320px;"> | Para maior flexibilidade, o painel de tarefas agora é um widget independente. Ele pode ser [ancorado](Combo_view/pt-br#Dock_Task_panel_on_top_of_Combo_view/pt-br.md) no topo da visualização Combo para obter o layout compacto das versões anteriores. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) e [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_1.0.png  style="width:320px;"> | A aparência do manipulador da ferramenta [Transform](Std_TransformManip/pt-br.md) foi aprimorada. Agora, ela também possui um conjunto de manipuladores planos para mover objetos ao longo dos 3 planos padrão. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_1.0.png  style="width:320px;"> | A funcionalidade de Realthunder que permite sobrepor widgets ancorados (transparência da árvore e do painel de tarefas) foi adicionada. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_1.0.png  style="width:320px;"> | A posição da fonte de luz agora pode ser configurada nas preferências (*Preferências → Exibição*). [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) e [Pull request #15877](https://github.com/FreeCAD/FreeCAD/pull/15877) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_1.0.png  style="width:320px;"> | A janela de Preferências foi redesenhada para substituir as abas por uma visualização em árvore. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++

+++
| <img alt="" src=images/TabBar_relnotes_1.0.png  style="width:320px;"> | O seletor de bancada de trabalho do TabBar foi adicionado. Ele pode ser habilitado e configurado em *Preferências → Bancadas de trabalho*. [Pull request #12270](https://github.com/FreeCAD/FreeCAD/pull/12270) |
+++

+++
| <img alt="" src=images/Unified_measurement_relnotes_1.0.PNG  style="width:320px;"> | Uma nova [ferramenta de medição universal](Std_Measure/pt-br.md) foi adicionada, substituindo as antigas [ferramentas de medição da bancada Part](Part_Workbench/pt-br#Measure.md). [Pull request #9750](https://github.com/FreeCAD/FreeCAD/pull/9750) e seguintes |
+++

   
  <img alt="" src=images/Normal_view_relnotes_1.0.gif  style="width:320px;">Clique na imagem se a animação não começar.   A ferramenta [Alinhar à seleção](Std_AlignToSelection/pt-br.md) foi adicionada, tornando possível entrar em vistas normais às faces ou seguindo as direções das arestas. [Pull request #13906](https://github.com/FreeCAD/FreeCAD/pull/13906)
   



### Outras melhorias na interface do usuário 

-   Um sistema de unidades de projeto foi introduzido. [Pull request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   A ferramenta [Section Cut](Part_SectionCut/pt-br.md) agora também funciona em uma visualização em perspectiva. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   Uma opção para classificar os workbenches em ordem alfabética (disponível após clicar com o botão direito em *Preferences → Workbenches*) foi adicionada. [Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
-   Um filtro **Find file** e um filtro **Find in files** foram adicionados ao diálogo [Std DlgMacroExecute](Std_DlgMacroExecute/pt-br.md). [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   O menu [View](Std_View_Menu/pt-br.md) e a barra de ferramentas View foram revisados. [Pull request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   O botão de parada foi removido da [Macro toolbar](Macros/pt-br.md). O [botão de gravação](Std_DlgMacroRecord/pt-br.md) agora se transforma em um botão de parada quando a gravação está em andamento. [Pull request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   O botão de reset nas Preferências agora exibe um menu com opções para redefinir as configurações em diferentes níveis: todas, no grupo atual ou na guia atual. [Pull request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) e [Pull request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   O Módulo de Ajuda foi integrado, de modo que não é mais necessário baixar um complemento para utilizá-lo. [Pull request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Preferências para personalizar o tema atual foram adicionadas. [Pull request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   As configurações padrão de seleção foram alteradas para tornar mais fácil a seleção de objetos na janela 3D. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   Um sistema de unidades denominado **Meter decimal** foi adicionado. O sistema MKS (m/kg/s/grau) não exibe sempre as dimensões em metros --- os milímetros ainda são usados para valores abaixo de 0,1 m. No entanto, para algumas aplicações (ex: engenharia civil), um sistema que exibe todas as dimensões em metros é útil. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Tamanhos adicionais de marcador (20, 25 e 30 px) foram adicionados a *Preferences → Display → 3D View → Marker size* para ajudar usuários de telas 4K. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   Uma opção *Toggle transparency* foi adicionada aos menus View e de contexto para alternar rapidamente a transparência de objetos selecionados. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)
-   Foi adicionada uma opção para bloquear as barras de ferramentas. Com ela, é possível bloquear ou desbloquear as posições das barras de ferramentas. Está disponível no menu View e no menu de contexto da área da barra de ferramentas. [Pull request #11596](https://github.com/FreeCAD/FreeCAD/pull/11596)
-   A cor padrão das formas foi ajustada para melhorar a aparência dos modelos. [Pull request #12380](https://github.com/FreeCAD/FreeCAD/pull/12380) e [Pull request #12488](https://github.com/FreeCAD/FreeCAD/pull/12488)
-   Itens dentro de contêineres de Part e Group agora podem ser ordenados por arrastar e soltar. [Pull request #12293](https://github.com/FreeCAD/FreeCAD/pull/12293)
-   Ícones de visibilidade (símbolo de olho) foram adicionados a objetos na árvore se a opção Mostrar ícone de visibilidade estiver marcada em *Preferences → Display → UI*. [Pull request #12298](https://github.com/FreeCAD/FreeCAD/pull/12298)
-   Um status [congelado](Std_ToggleFreeze/pt-br.md) (opção *Toggle freeze* no menu de contexto da [árvore](Tree_view/pt-br.md)) foi adicionado, tornando possível desativar o comportamento paramétrico de um objeto (para que ele não mude mesmo se os objetos dos quais depende forem alterados). [Pull request #12580](https://github.com/FreeCAD/FreeCAD/pull/12580)
-   As animações de navegação foram melhoradas. As animações agora utilizam uma função de suavização e têm uma duração fixa, que pode ser alterada em *Preferences → Display → Navigation*. [Pull request #10881](https://github.com/FreeCAD/FreeCAD/pull/10881) e [Pull request #12205](https://github.com/FreeCAD/FreeCAD/pull/12205)
-   Os botões para as visualizações padrão agora estão agrupados sob um único botão. Os botões individuais ainda estão disponíveis na barra de ferramentas adicional *Individual views*. [Pull request #12878](https://github.com/FreeCAD/FreeCAD/pull/12878)
-   O nome do documento ativo agora também é exibido na barra de título da janela. [Pull request #12035](https://github.com/FreeCAD/FreeCAD/pull/12035)
-   Foi adicionada um comando para exibir o painel [Property View](Property_editor/pt-br.md). [Pull request #12024](https://github.com/FreeCAD/FreeCAD/pull/12024)
-   A integração de dispositivos 3Dconnexion com o FreeCAD no Windows foi melhorada. [Pull request #12929](https://github.com/FreeCAD/FreeCAD/pull/12929)
-   Uma função de Medição Rápida foi adicionada. Ela utiliza a [barra de status](Status_bar/pt-br.md) para exibir informações-chave sobre a medição (comprimento de aresta, área da face, distância/ângulo entre pontos/arestas e raio de arestas circulares/faces cilíndricas) sobre a seleção atual na visualização 3D. [Pull request #12217](https://github.com/FreeCAD/FreeCAD/pull/12217)
-   As barras de ferramentas agora podem ser arrastadas e soltas nas barras de status e de menu. [Pull request #13571](https://github.com/FreeCAD/FreeCAD/pull/13571)
-   Um botão *Reload stylesheet* foi adicionado para ajudar no desenvolvimento de estilos. Ele não pertence a nenhuma barra de ferramentas por padrão, sendo necessário adicioná-lo manualmente em *Tools → Customize → Toolbars → View*. [Pull request #13982](https://github.com/FreeCAD/FreeCAD/pull/13982)
-   Ícones de documentos (incluindo os de [Abrir](Std_Open/pt-br.md) e [Salvar](Std_Save/pt-br.md), entre outros) foram melhorados e unificados. [Pull request #13865](https://github.com/FreeCAD/FreeCAD/pull/13865)
-   O ícone [Fit all](Std_ViewFitAll/pt-br.md) foi substituído para maior clareza. [Pull request #14180](https://github.com/FreeCAD/FreeCAD/pull/14180)
-   Vários ícones principais (como [Novo](Std_New/pt-br.md)) foram aprimorados. [Pull request #14278](https://github.com/FreeCAD/FreeCAD/pull/14278), [Pull request #14434](https://github.com/FreeCAD/FreeCAD/pull/14434) e [Pull request #14154](https://github.com/FreeCAD/FreeCAD/pull/14154)
-   Os ícones dos painéis de tarefas do Sketcher e do Part Design foram aprimorados. [Pull request #13968](https://github.com/FreeCAD/FreeCAD/pull/13968)
-   No [modo sem cabeça](Headless_FreeCAD/pt-br.md), o console Python interativo agora oferece autocompletar, desde que o módulo [readline](https://docs.python.org/3/library/readline.html) esteja disponível. [Pull request #14213](https://github.com/FreeCAD/FreeCAD/pull/14213)
-   Uma opção para exibir nomes internos na árvore de objetos foi adicionada. Ela está desativada por padrão e pode ser ativada em *Preferences → Display → UI → Hide Internal Names*. [Pull request #14237](https://github.com/FreeCAD/FreeCAD/pull/14237)
-   O botão de Ajuda foi removido das Preferências porque não estava funcionando. [Pull request #14695](https://github.com/FreeCAD/FreeCAD/pull/14695)
-   Os estilos de planilhas padrão foram significativamente aprimorados e agora são oferecidos em duas variantes além da clássica: claro e escuro. [Pull request #13772](https://github.com/FreeCAD/FreeCAD/pull/13772)
-   As páginas de Tema e Interface do usuário no grupo Exibição das Preferências foram reorganizadas e combinadas. Algumas preferências foram movidas para a nova página Avançado. [Pull request #14974](https://github.com/FreeCAD/FreeCAD/pull/14974)
-   As preferências de verificação e refinamento do Part/Part Design agora estão ativadas por padrão. [Pull request #14406](https://github.com/FreeCAD/FreeCAD/pull/14406)
-   Foi adicionado um novo parâmetro - **BaseApp/Preferences/Bitmaps/Theme/UseIconTheme** (booleano): Defina como verdadeiro para forçar o Qt a usar ícones do tema de ícones do sistema. O padrão é falso, então o FreeCAD usará seus próprios ícones. Isso não afeta outros mecanismos de tema de ícones do Qt, como diálogos de sistema, botões e outros. Esses sempre devem usar os ícones do tema do sistema. [Pull request #16018](https://github.com/FreeCAD/FreeCAD/pull/16018)
-   Informações sobre estilos de planilha, tema e QtStyle agora estão incluídas em *Ajuda → Sobre o FreeCAD*. [Pull request #16281](https://github.com/FreeCAD/FreeCAD/pull/16281)
-   A tela de introdução agora é selecionada aleatoriamente na inicialização a partir de várias imagens, incluindo modelos de usuário e apresentações de algumas das bancadas adicionais. [Pull request #16071](https://github.com/FreeCAD/FreeCAD/pull/16071)
-   Um modo seguro foi adicionado e pode ser ativado através de *Ajuda → Reiniciar em modo seguro*. Ele desativa temporariamente as configurações do usuário, complementos, temas e outras personalizações para executar o FreeCAD em um estado de \"restauração de fábrica\" para depuração. [Pull request #16858](https://github.com/FreeCAD/FreeCAD/pull/16858)



## Alterações no formato de arquivo 

Embora precauções tenham sido tomadas para garantir que arquivos criados com a nova versão 1.0 possam ainda ser abertos em versões anteriores do FreeCAD, algumas novas funcionalidades introduzidas na versão 1.0 não podem ser entendidas por versões anteriores, o que pode fazer com que modelos salvos com a versão 1.0 apresentem falhas ou problemas ao serem abertos em versões mais antigas do FreeCAD. Aqui está um resumo dos possíveis problemas que você pode encontrar e suas soluções. A comunidade do fórum também pode fornecer ajuda na correção de problemas de compatibilidade.

-   A propriedade **Attachment** foi renomeada para **AttachmentSupport**. Isso significa que recursos que dependem dessa propriedade (principalmente modelos que utilizam o complemento Assembly4) precisarão ser ajustados para serem abertos em uma versão anterior do FreeCAD. Uma [macro está disponível aqui](Macro_Convert_021/pt-br.md) para corrigir esses arquivos.



## Sistema central e API 



### Núcleo

-   As funções de vetor da [API de Vetores](Vector_API.md) agora podem ser usadas em [Expressões](Expressions/pt-br.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   O editor Python agora ajusta a indentação da linha anterior ao pressionar a tecla Enter. [Pull request #11356](https://github.com/FreeCAD/FreeCAD/pull/11356).
-   O nome da propriedade que mantém o(s) objeto(s) de referência de um anexo foi alterado de **Support** para **AttachmentSupport**. [Pull request #12714](https://github.com/FreeCAD/FreeCAD/pull/12714).
-   Um contêiner de propriedades, App::VarSet, foi introduzido como um recurso central. Um VarSet permite que os usuários definam propriedades que podem ser usadas em modelos, assim como aliases de planilha e outros contêineres de propriedades anteriores (Dados Dinâmicos, Path PropertyBags e Variáveis do Assembly 4). [Pull Request #12135](https://github.com/FreeCAD/FreeCAD/pull/12135)

### API



#### Nova API Python 

-    {{Incode|getUpDirection}}: Obtém a direção para cima de uma visão View3DInventor. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### API Python Alterada 

-   Para salvar/restaurar dados personalizados de um recurso Python, os métodos anteriormente chamados {{Incode|__getstate__}}/{{Incode|__setstate__}} foram renomeados para {{Incode|dumps}}/{{Incode|loads}}. Isso se deve a alterações internas no Python 3.11. [Pull request #10769](https://github.com/FreeCAD/FreeCAD/pull/10769) e [Pull request #12243](https://github.com/FreeCAD/FreeCAD/pull/12243).



## Início

A bancada Start foi substituída por uma página inicial, um aplicativo baseado em QtWidgets. Ela pode ser exibida utilizando a opção *Ajuda → Iniciar*. [Pull request #13134](https://github.com/FreeCAD/FreeCAD/pull/13134)

Os dois primeiros pull requests mencionados abaixo pertencem à bancada Start, mas influenciaram o design da página inicial.

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_1.0.png  style="width:384px;"> | Uma seção **Novo arquivo**, que inclui vários botões de acesso rápido, foi adicionada à Página Inicial. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_1.0.png  style="width:384px;"> | O design visual da Página Inicial foi reformulado. Agora, ela apresenta uma aparência mais moderna e consistente. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++

+++
| <img alt="" src=images/First_start_relnotes_1.0.png  style="width:384px;"> | Um widget simples para o primeiro início foi adicionado e será expandido em breve. [Pull request #13650](https://github.com/FreeCAD/FreeCAD/pull/13650) |
+++



## Bancada de Montagem (Assembly Workbench) 

+++
| <img alt="" src=images/Assembly_relnotes_1.0.png  style="width:384px;"> | Uma bancada de [Montagem](Assembly_Workbench/pt-br.md) integrada foi finalmente adicionada ao FreeCAD. Ela utiliza o solver open-source [Ondsel](https://github.com/Ondsel-Development/OndselSolver). Funcionalidades básicas (juntas) já estão disponíveis. O desenvolvimento adicional está em andamento. [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427), [Pull request #10764](https://github.com/FreeCAD/FreeCAD/pull/10764), [Pull request #12406](https://github.com/FreeCAD/FreeCAD/pull/12406) e mais |
+++



### Mais melhorias na Montagem 

-   Uma [Vista Explodida](Assembly_CreateView/pt-br.md) foi adicionada. [Pull request #12419](https://github.com/FreeCAD/FreeCAD/issues/12419)
-   Os ícones da montagem foram atualizados e as funcionalidades experimentais foram expostas. [Pull request #13866](https://github.com/FreeCAD/FreeCAD/pull/13866)
-   Juntas de Ângulo, Perpendicular e Paralela foram adicionadas. [Pull request #14008](https://github.com/FreeCAD/FreeCAD/pull/14008)
-   Uma funcionalidade de [Lista de Materiais](Assembly_CreateBom/pt-br.md) foi adicionada. [Pull request #14198](https://github.com/FreeCAD/FreeCAD/pull/14198)
-   O código de mitigação do [TNP](Topological_naming_problem/pt-br.md) foi adicionado. [Pull request #14674](https://github.com/FreeCAD/FreeCAD/pull/14674)
-   Suporte para submontagens flexíveis foi adicionado. Submontagens adicionadas a uma montagem principal podem ser definidas como rígidas (uma unidade sólida) ou flexíveis (permitindo movimento de seus componentes individuais). Passos manuais são necessários para as submontagens adicionadas durante o ciclo de desenvolvimento antes da integração desta funcionalidade. Essas montagens precisarão ser removidas e readicionadas à sua montagem principal. [Pull request #15629](https://github.com/FreeCAD/FreeCAD/pull/15629)



## Bancada de Trabalho BIM 

+++
| <img alt="" src=images/bim_relnotes_1.0.png  style="width:384px;"> | A bancada Arch foi finalmente mesclada com a [BIM](BIM_Workbench/pt-br.md), tornando-se a nova bancada BIM. A nova bancada BIM mantém todas as ferramentas da Arch, adiciona algumas novas e traz muitos aprimoramentos para todo o fluxo de trabalho BIM e de design arquitetônico, além de melhores ferramentas de configuração e gerenciamento, e um suporte aprimorado ao IFC. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783) |
+++



### Mais melhorias na BIM 

-   Vindo da Workbench BIM, algumas ferramentas \"tudo-em-um\" do Arch foram divididas em diferentes casos de uso: A ferramenta [Arch BuildingPart](Arch_BuildingPart/pt-br.md) foi dividida nas ferramentas [BIM Building](Arch_Building/pt-br.md) e [BIM Level](Arch_Floor/pt-br.md), a ferramenta [Arch Structure](Arch_Structure/pt-br.md) foi dividida em [BIM Column](BIM_Column/pt-br.md), [BIM Beam](BIM_Beam/pt-br.md) e [BIM Slab](BIM_Slab/pt-br.md), e a ferramenta [Arch Window](Arch_Window.md) foi dividida nas ferramentas [BIM Window](Arch_Window/pt-br.md) e [BIM Door](BIM_Door/pt-br.md). Internamente, essas ferramentas ainda produzem o mesmo objeto, apenas com tipos IFC diferentes e presets aplicados. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   O [Arch CutPlane](Arch_CutPlane/pt-br.md) foi aprimorado. Agora, ele é ciente de aninhamento e links, e a seleção está mais flexível. Também é possível selecionar as bordas, tornando o comando Arch CutLine obsoleto. [Pull request #11254](https://github.com/FreeCAD/FreeCAD/pull/11254) e [Pull request #11792](https://github.com/FreeCAD/FreeCAD/pull/11792)
-   As preferências BIM foram verificadas e aprimoradas. As páginas no [Preferences Editor](Preferences_Editor/pt-br.md) receberam um novo layout. [Pull request #11940](https://github.com/FreeCAD/FreeCAD/pull/11940) e [Pull request #12038](https://github.com/FreeCAD/FreeCAD/pull/12038)
-   Um preset *Apenas Abertura* foi adicionado ao comando [Arch Window](Arch_Window/pt-br.md). [Pull request #12209](https://github.com/FreeCAD/FreeCAD/pull/12209)
-   O objeto [Arch Roof](Arch_Roof/pt-br.md) agora possui uma propriedade *Subvolume*. Isso permite usar um objeto sólido personalizado como volume de subtração para um telhado. [Pull request #12346](https://github.com/FreeCAD/FreeCAD/pull/12346)
-   Além disso, para um objeto [Arch Roof](Arch_Roof/pt-br.md) que usa um objeto sólido como sua *Base*, um volume de subtração apropriado é agora gerado automaticamente. Assim como um telhado baseado em fios, esse tipo de telhado pode ser subtraído das paredes de um edifício com [Arch Remove](Arch_Remove.md). [Pull request #13221](https://github.com/FreeCAD/FreeCAD/pull/13221)
-   A ferramenta [Arch Reference](Arch_Reference.md) foi aprimorada: os objetos de referência agora podem usar o conteúdo completo do arquivo em vez de precisar escolher uma parte; suporte para arquivos DXF e IFC foi adicionado. [Pull request #13287](https://github.com/FreeCAD/FreeCAD/pull/13287)
-   FreeCAD agora possui um novo arquivo de exemplo BIM. [Pull request #14937](https://github.com/FreeCAD/FreeCAD/pull/14937)
-   A nova Workbench BIM também oferece uma série de novas ferramentas de gerenciamento para ajudar a configurar seu projeto ou gerenciar em massa as propriedades IFC dos seus objetos. Saiba mais na página [BIM Workbench](BIM_Workbench/pt-br.md).
-   [IfcOpenShell](IfcOpenShell/pt-br.md), outro software de código aberto necessário para trabalhar com arquivos IFC no FreeCAD, agora está incluído em todos os pacotes de instaladores oficiais oferecidos pela equipe do FreeCAD. Se você obter o FreeCAD de um provedor terceirizado, como sua distribuição Linux, onde o IfcOpenShell ainda não foi oficialmente incluído, a Workbench BIM oferece uma ferramenta de utilitário para baixar e instalar o IfcOpenShell. E, se você não tiver uso para o IFC, a Workbench BIM ainda funciona 100% sem o IfcOpenShell.
-   As barras de ferramentas e menus da Workbench BIM foram reformuladas. [Pull request #14087](https://github.com/FreeCAD/FreeCAD/pull/14087)



## Bancada de Trabalho CAM 

-   A Workbench Path agora é chamada de CAM. [Pull request #12665](https://github.com/FreeCAD/FreeCAD/pull/12665)



### Melhorias adicionais no CAM 

-   A usinagem de acabamento foi reimplementada para obter entradas a partir do G-code das operações anteriores (em vez de usar os parâmetros internos das operações [Área](CAM_Area/pt-br.md)). Isso permite o suporte para usinagem de acabamento em operações de Área após operações não-Área (mais notavelmente o processo Adaptativo). [Pull request #11939](https://github.com/FreeCAD/FreeCAD/pull/11939)
-   A compensação da altura da ferramenta G43 foi adicionada ao pós-processador CAM de centróide. [Pull request #12652](https://github.com/FreeCAD/FreeCAD/pull/12652)
-   Uma opção de *Retração de avanço* foi adicionada às configurações de operação de perfuração para alargamento e escareamento. [Pull request #13254](https://github.com/FreeCAD/FreeCAD/pull/13254)
-   Um novo simulador CAM baseado em funções OpenGL de baixo nível (mais rápido e mais preciso) foi adicionado. [Pull request #13884](https://github.com/FreeCAD/FreeCAD/pull/13884) e [Pull request #15597](https://github.com/FreeCAD/FreeCAD/pull/15597)
-   A operação [Vcarve](CAM_Vcarve/pt-br.md) foi reformulada para incluir recursos comumente disponíveis em outros softwares CAM (Desnível de passo, Passagem de acabamento, Otimização do movimento da ferramenta e método debugVoronoi), possibilitando melhorar drasticamente a qualidade da superfície usinada, enquanto aumenta a velocidade de usinagem em até 50%. [Pull request #14093](https://github.com/FreeCAD/FreeCAD/pull/14093)
-   Modelos de usinabilidade de materiais foram adicionados juntamente com diversos materiais. [Pull request #14460](https://github.com/FreeCAD/FreeCAD/pull/14460), [Pull request #15910](https://github.com/FreeCAD/FreeCAD/pull/15910) e [Pull request #16021](https://github.com/FreeCAD/FreeCAD/pull/16021)



## Bancada Draft 

-   Uma opção de justificação e várias propriedades relacionadas foram adicionadas ao [Draft ShapeStrings](Draft_ShapeString/pt-br.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Dimensões radiais](Draft_Dimension/pt-br#Usage_radial_dimension.md) agora mostram apenas uma seta. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Uma propriedade de *Ângulo Obliquo* foi adicionada ao [Draft ShapeStrings](Draft_ShapeString/pt-br.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Suporte para hyperlinks foi adicionado. Hyperlinks para arquivos locais e remotos e URLs em [Draft Texts](Draft_Text/pt-br.md) e [Draft Labels](Draft_Label/pt-br.md) podem ser abertos a partir do [Tree view](Tree_view/pt-br.md) ou do menu de contexto [3D view](3D_view/pt-br.md). [Pull request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   O código do [plano de trabalho Draft](Draft_SelectPlane/pt-br.md) foi reestruturado. Agora há um plano de trabalho por visualização 3D. [Pull request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   O recurso de histórico e as opções de alinhamento do comando [Draft SelectPlane](Draft_SelectPlane/pt-br.md) foram melhorados. [Pull request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   O comportamento da [grade](Draft_ToggleGrid/pt-br.md) foi melhorado. Sua visibilidade agora é armazenada por visualização 3D. Ao mudar para outra bancada de trabalho, todas as grades são ocultadas (há um parâmetro de [ajuste fino](Fine-tuning/pt-br.md) disponível para desabilitar isso). [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   As preferências do Draft foram verificadas e melhoradas. Algumas preferências foram adicionadas, e preferências obsoletas foram removidas. As páginas no [Editor de Preferências](Preferences_Editor/pt-br.md) têm um novo layout e mostram unidades onde aplicável. Não é mais necessário reiniciar o FreeCAD após mudar uma preferência do Draft. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) e [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Uma nova configuração de *Atraso do Mouse* foi adicionada às preferências gerais do Draft. Se for diferente de zero (o valor padrão é 1 s), após inserir um número em um dos campos de entrada do painel de tarefas, o movimento do mouse será desativado, e não mudará o valor no campo de entrada, por um tempo determinado em segundos. Configurar um valor muito grande praticamente desativa o movimento do mouse até que o comando termine. [Pull request #12624](https://github.com/FreeCAD/FreeCAD/pull/12624)
-   Um botão para alterar rapidamente a cor da grade foi adicionado ao painel de tarefas do comando [Draft SelectPlane](Draft_SelectPlane/pt-br.md). [Pull request #13051](https://github.com/FreeCAD/FreeCAD/pull/13051)
-   Uma propriedade de *Fusão* foi adicionada aos [Draft PointArrays](Draft_PointArray/pt-br.md), [Draft PathArrays](Draft_PathArray/pt-br.md) e Draft PathTwistedArrays. [Pull request #13172](https://github.com/FreeCAD/FreeCAD/pull/13172) e [Pull request #13191](https://github.com/FreeCAD/FreeCAD/pull/13191)
-   O botão do comando [Toggle grid](Draft_ToggleGrid/pt-br.md) agora se comporta como um botão de alternância, fornecendo um feedback visual do status da grade (visível ou oculta). [Pull request #14452](https://github.com/FreeCAD/FreeCAD/pull/14452)



### Outras melhorias no Draft 

-   [Draft Facebinders](Draft_Facebinder/pt-br.md) agora podem lidar com faces pertencentes a links e faces aninhadas em [Std Parts](Std_Part/pt-br.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Várias configurações foram adicionadas ao comando [Draft SetStyle](Draft_SetStyle/pt-br.md). [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) e [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Configurações também foram adicionadas ao comando [Draft ApplyStyle](Draft_ApplyStyle/pt-br.md). [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610) e [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Marcadores de snap, edição e rastreador agora usam a preferência [Tamanho do marcador](Preferences_Editor/pt-br#3D_View.md). [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688) e [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Alguns ícones do Draft foram alterados para melhorar sua aparência. [Pull request #13585](https://github.com/FreeCAD/FreeCAD/pull/13585)
-   O objeto [Draft Layer](Draft_Layer/pt-br.md) foi atualizado para o novo sistema de gerenciamento de materiais. Agora ele possui uma propriedade *Aparência da Forma* e uma propriedade *Substituir Aparência da Forma dos Filhos*. [Pull request #13949](https://github.com/FreeCAD/FreeCAD/pull/13949)
-   [Draft Fillets](Draft_Fillet/pt-br.md) agora também podem ser aplicados a arcos. [Pull request #14774](https://github.com/FreeCAD/FreeCAD/pull/14774)



## Bancada FEM 

+++
| <img alt="" src=images/FEM_better_legend_labels_relnotes_1.0.JPG  style="width:384px;"> | A posição dos rótulos da legenda de cores foi ajustada para que os rótulos superiores sejam menos propensos a serem cobertos pelo cubo de navegação. A fonte e a cor padrão dos rótulos foram alteradas para aumentar a visibilidade, e preferências foram adicionadas para permitir a modificação da cor e tamanho dos rótulos. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_1.0.png  style="width:384px;"> | O comando [FEM PostFilterLinearizedStresses](FEM_PostFilterLinearizedStresses/pt-br.md) agora pode usar os componentes do tensor de tensão para cálculos de tensão linearizada. Anteriormente, apenas as tensões de Von Mises, Tresca e as principais (maior/intermediária/menor) podiam ser usadas para isso. [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++

+++
| <img alt="" src=images/Cyclic_symmetry_relnotes_1.0.jpg  style="width:384px;"> | Foi adicionado suporte para simetria cíclica via [restrição de amarração](FEM_ConstraintTie/pt-br.md) no CalculiX, tornando possível analisar modelos com simetria periódica rotacional usando um único setor repetitivo. [Pull request #12289](https://github.com/FreeCAD/FreeCAD/pull/12289) |
+++

+++
| <img alt="" src=images/2D_analyses_relnotes_1.0.png  style="width:384px;"> | Foi adicionado suporte para análises 2D (tensão plana, deformação plana e axisimétrica) para o [solucionador CalculiX](FEM_SolverCalculixCxxtools/pt-br.md). Elas são configuradas da mesma forma que as simulações com elementos de casca, mas existem algumas restrições adicionais descritas na página wiki mencionada. A nova opção *Espaço do Modelo* deve ser configurada corretamente. [Pull request #12562](https://github.com/FreeCAD/FreeCAD/pull/12562) |
+++

+++
| <img alt="" src=images/Hex_subdivision_relnotes_1.0.png  style="width:384px;"> | Como o primeiro passo em direção ao suporte para elementos hexaédricos, agora é possível gerar esses elementos usando a técnica de subdivisão do Gmsh, graças à nova propriedade do Gmsh *Algoritmo de Subdivisão*. Ela também pode ser usada para criar elementos quadriláteros. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) |
+++

+++
| <img alt="" src=images/Pipeline_colors_relnotes_1.0.png  style="width:384px;"> | Novas propriedades de visualização foram adicionadas aos objetos do pipeline de resultados. A cor e a largura da borda da malha agora podem ser alteradas para o modo de exibição *Superfície com Bordas*. O tamanho dos nós pode ser modificado para o modo *Nós*. Também foi adicionada uma configuração de transparência para todos os modos. [Pull request #13066](https://github.com/FreeCAD/FreeCAD/pull/13066) |
+++

+++
| <img alt="" src=images/Constraint_suppress_relnotes_1.0.png  style="width:384px;"> | As restrições FEM agora podem ser suprimidas (clique com o botão direito em uma restrição e selecione *Suprimir*) e, assim, ignoradas pelos solucionadores. Dessa forma, é possível modificar a configuração da análise sem precisar excluir as restrições que não são necessárias no momento. [Pull request #12359](https://github.com/FreeCAD/FreeCAD/pull/12359) |
+++

+++
| <img alt="" src=images/Rigid_body_relnotes_1.0.JPG  style="width:384px;"> | O suporte para a [Restrição de Corpo Rígido](FEM_ConstraintRigidBody/pt-br.md) do CalculiX foi adicionado, finalmente tornando possível simular a torção de componentes arbitrários e aplicar cargas remotas, entre outras funcionalidades. [Pull request #13900](https://github.com/FreeCAD/FreeCAD/pull/13900) |
+++



### Melhorias adicionais no FEM 

-   O menu *Modelo → Restrições sem solucionador* foi removido da interface gráfica. As restrições listadas não podiam ser usadas. [Pull request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) e [Pull request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   A palavra \"restrição\" foi removida dos nomes e descrições da maioria das funcionalidades na bancada FEM para garantir a nomenclatura correta. Os nomes foram alterados para atender aos padrões da indústria de FEA e torná-los mais intuitivos para novos usuários. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) e [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)
-   Novos ícones foram adicionados para [Solver CalculiX Standard](FEM_SolverCalculixCxxtools/pt-br.md), [Controle de tarefa do solver](FEM_SolverControl/pt-br.md) e [Executar cálculos do solver](FEM_SolverRun/pt-br.md) para maior intuitividade. [Pull request #10885](https://github.com/FreeCAD/FreeCAD/pull/10885)
-   O Solver CalculiX (novo framework) foi removido da interface gráfica, pois está incompleto e desnecessário no momento. Seus exemplos também foram removidos. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823) e [Pull request #12876](https://github.com/FreeCAD/FreeCAD/pull/12876)
-   O layout de alguns painéis de ferramentas de pós-processamento foi melhorado para reduzir o espaço horizontal ocupado por eles. [Pull request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   O painel de tarefas [FEM ConstraintTemperature](FEM_ConstraintTemperature/pt-br.md) foi reformulado para corrigir problemas ao editar essa funcionalidade. [Pull request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   Um antigo problema com o [FEM PostFilterDataAlongLine](FEM_PostFilterDataAlongLine/pt-br.md), que só permitia plotar magnitude e não componentes vetoriais de uma variável de saída selecionada, foi finalmente corrigido. [Pull request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   As funcionalidades [FEM ConstraintForce](FEM_ConstraintForce/pt-br.md) e [FEM ConstraintPressure](FEM_ConstraintPressure/pt-br.md) foram reformuladas para melhorar seu funcionamento no lado do código-fonte. [Pull request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) e [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   O [FEM PostFilterDataAtPoint](FEM_PostFilterDataAtPoint/pt-br.md) agora possui uma propriedade PointSize para ajustar o tamanho do símbolo do ponto para maior visibilidade. [Pull request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   Para maior clareza, o comando [FEM mesh region](FEM_MeshRegion/pt-br.md) foi renomeado para *Refinamento de malha FEM* na interface gráfica (o nome do comando permanece inalterado). [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)
-   A magnitude da aceleração da gravidade agora pode ser alterada usando as propriedades de [FEM ConstraintSelfWeight](FEM_ConstraintSelfWeight/pt-br.md). [Pull request #12044](https://github.com/FreeCAD/FreeCAD/pull/12044)
-   [Contato](FEM_ConstraintContact/pt-br.md) e [restrição de vínculo](FEM_ConstraintTie/pt-br.md) foram significativamente aprimorados. A rigidez de contato agora usa a unidade correta e o valor da inclinação de aderência pode ser especificado para fricção no contato. Além disso, o ajuste de folga pode ser especificado para o contato, enquanto a restrição de vínculo pode ter o ajuste habilitado ou desabilitado. [Pull request #12133](https://github.com/FreeCAD/FreeCAD/pull/12133)
-   PaStiX e Pardiso foram adicionados aos solvers de matrizes suportados [CalculiX](FEM_SolverCalculixCxxtools/pt-br#Properties.md). Eles são os solvers ccx mais rápidos, mas a possibilidade de usá-los depende da versão do binário CalculiX e das bibliotecas adicionais disponíveis. [Pull request #12478](https://github.com/FreeCAD/FreeCAD/pull/12478)
-   A propriedade *Beam Reduced Integration* (definida como *verdadeiro* por padrão) foi adicionada às configurações do [CalculiX solver](FEM_SolverCalculixCxxtools/pt-br.md). Ela habilita um esquema de integração reduzida para elementos de viga, tornando possível usar a seção de viga de tubo e eliminando problemas de precisão em análises com plasticidade, entre outros. [Pull request #12513](https://github.com/FreeCAD/FreeCAD/pull/12513)
-   A ferramenta [Conjunto de nós](FEM_CreateNodesSet/pt-br.md) incompleta foi removida da interface gráfica. Ela não podia ser usada. [Pull request #12611](https://github.com/FreeCAD/FreeCAD/pull/12611)
-   O procedimento de análise *Check Mesh CalculiX* agora gera corretamente a malha de resultados. [Pull request #12612](https://github.com/FreeCAD/FreeCAD/pull/12612)
-   Foi esclarecido no painel de tarefas que o diâmetro usado pela seção de viga de tubo é o diâmetro externo. [Pull request #12609](https://github.com/FreeCAD/FreeCAD/pull/12609)
-   A propriedade *Beam Shell Result Output 3D* do [CalculiX solver](FEM_SolverCalculixCxxtools/pt-br.md) agora é definida como *verdadeira* por padrão para fornecer resultados para elementos de viga e fornecer resultados significativos para elementos de casca. [Pull request #12493](https://github.com/FreeCAD/FreeCAD/pull/12493)
-   Os símbolos das funcionalidades de análise agora estão corretamente posicionados quando o corpo (ou contêiner de peça) teve a propriedade de posicionamento modificada. [Pull request #12527](https://github.com/FreeCAD/FreeCAD/pull/12527)
-   A [Pressão](FEM_ConstraintPressure/pt-br.md) agora funciona corretamente para cascas, independentemente da configuração de grupos de malha. Essa configuração pode ser alterada nas Preferências. [Pull request #12437](https://github.com/FreeCAD/FreeCAD/pull/12437)
-   A nova opção de endurecimento isotrópico foi renomeada em [Material Mecânico Não Linear](FEM_MaterialMechanicalNonlinear/pt-br.md). Além disso, foi adicionada a opção de endurecimento cinemático. [Pull request #12666](https://github.com/FreeCAD/FreeCAD/pull/12666)
-   Agora, a não linearidade geométrica não é ativada automaticamente nem exigida quando um material não linear é utilizado, pois são formas de não linearidade independentes. [Pull request #12703](https://github.com/FreeCAD/FreeCAD/pull/12703)
-   Malhas mistas, compostas tanto por elementos triangulares quanto quadriláteros, agora são exibidas corretamente na pipeline de resultados. [Pull request #12740](https://github.com/FreeCAD/FreeCAD/pull/12740)
-   A propriedade *Output Frequency* foi adicionada às [Configurações do solver CalculiX](FEM_SolverCalculixCxxtools/pt-br.md). Ela define a frequência de gravação de saídas em incrementos. [Pull request #12672](https://github.com/FreeCAD/FreeCAD/pull/12672)
-   Agora é possível gerar elementos quadriláteros de segunda ordem. Anteriormente, a configuração Gmsh de 2ª ordem gerava elementos quadriláteros de 1ª ordem devido à falta do comando *SecondOrderIncomplete* no Gmsh, que agora é utilizado internamente. Esses elementos também podem ser usados em análises 2D. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) e [Pull request #12774](https://github.com/FreeCAD/FreeCAD/pull/12774)
-   A determinação da orientação da seção transversal da viga foi parcialmente corrigida. Devido a um erro na versão atual do CalculiX, ainda podem ocorrer problemas com algumas orientações. [Pull request #12833](https://github.com/FreeCAD/FreeCAD/pull/12833)
-   Exemplos de FEM de viga engastada na página inicial foram atualizados e um novo exemplo utilizando elementos 1D foi adicionado. [Pull request #12871](https://github.com/FreeCAD/FreeCAD/pull/12871)
-   O formato em que o FreeCAD grava o [constraint de força](FEM_ConstraintForce/pt-br.md) agora é compatível com o formato do CalculiX, eliminando problemas raros com números muito longos. [Pull request #12932](https://github.com/FreeCAD/FreeCAD/pull/12932)
-   Agora é possível exportar a [pipeline de resultados](FEM_PostPipelineFromResult/pt-br.md) para o formato VTK. [Pull request #12987](https://github.com/FreeCAD/FreeCAD/pull/12987)
-   Novas propriedades de controle de incremento foram adicionadas às [Configurações do solver CalculiX](FEM_SolverCalculixCxxtools/pt-br.md). Atualmente, além do tamanho inicial do incremento e do período de tempo do passo, é possível especificar o tamanho mínimo e máximo do incremento. Além disso, a propriedade *Iterations Thermo Mech Maximum* foi renomeada para *Iterations Maximum*, pois agora pode ser usada para análises estáticas (não termomecânicas) também. [Pull request #12662](https://github.com/FreeCAD/FreeCAD/pull/12662)
-   A espessura padrão do [elemento 2D](FEM_ElementGeometry2D.md) foi alterada de 20 mm para 1 mm, pois faz mais sentido na prática. [Pull request #13077](https://github.com/FreeCAD/FreeCAD/pull/13077)
-   Muitos ícones de FEM foram significativamente melhorados para reduzir a semelhança entre eles e tornar mais claro o que as ferramentas fazem. [Pull request #13130](https://github.com/FreeCAD/FreeCAD/pull/13130)
-   A propriedade *Thermo Mech Type* foi adicionada às [Configurações do solver CalculiX](FEM_SolverCalculixCxxtools/pt-br.md). Ela permite alternar uma análise termomecânica regular (acoplada) para uma análise desacoplada ou uma pura análise de transferência de calor. [Pull request #13296](https://github.com/FreeCAD/FreeCAD/pull/13296)
-   A propriedade *Min. Size* foi adicionada ao [gerador de malha Netgen](FEM_MeshNetgenFromShape/pt-br.md) para evitar a geração de elementos muito pequenos ao fazer malhas em geometrias mais complexas. [Pull request #12794](https://github.com/FreeCAD/FreeCAD/pull/12794)
-   Um antigo problema com a propriedade de escala de símbolo não funcionando corretamente para as restrições de FEM foi finalmente corrigido, e a propriedade *Scale* pode agora ser utilizada para ajustar o tamanho dos símbolos de uma restrição selecionada. [Pull request #13274](https://github.com/FreeCAD/FreeCAD/pull/13274)
-   A escala automática das restrições de FEM foi aprimorada para lidar melhor com objetos muito pequenos ou muito grandes. [Pull request #13586](https://github.com/FreeCAD/FreeCAD/pull/13586)
-   O [fluxo de calor](FEM_ConstraintHeatflux/pt-br.md) agora possui um modo de radiação de fluxo de calor para modelar a radiação de superfície para o ambiente. [Pull request #13466](https://github.com/FreeCAD/FreeCAD/pull/13466)
-   Algumas propriedades de visualização de símbolos de restrição não utilizadas foram removidas. [Pull request #13569](https://github.com/FreeCAD/FreeCAD/pull/13569)
-   Novas propriedades de visualização (com a principal sendo *Color Mode*) foram adicionadas aos objetos de malha FEM, permitindo que configurações de cor e transparência personalizadas para malhas sejam salvas e restauradas. [Pull request #13698](https://github.com/FreeCAD/FreeCAD/pull/13698)
-   Agora, por padrão, apenas o último filtro adicionado sob cada objeto de pipeline de resultados é visível. [Pull request #13820](https://github.com/FreeCAD/FreeCAD/pull/13820)
-   As dicas no painel de tarefas de várias restrições foram alteradas para refletir as regras de seleção de geometria para essas restrições. [Pull request #13921](https://github.com/FreeCAD/FreeCAD/pull/13921) e [Pull request #14002](https://github.com/FreeCAD/FreeCAD/pull/14002)
-   O suporte para resultados de fluxo de calor de análises termomecânicas foi adicionado à pipeline de resultados. [Pull request #14019](https://github.com/FreeCAD/FreeCAD/pull/14019)
-   A funcionalidade de [Impressão de seção](FEM_ConstraintSectionPrint/pt-br.md) foi aprimorada, adicionando suporte para resultados de fluxo de calor e tensão de arrasto (ainda não disponíveis, pois as análises fluidodinâmicas 3D com o CalculiX ainda não foram implementadas). [Pull request #14046](https://github.com/FreeCAD/FreeCAD/pull/14046)
-   A [Fonte de calor no corpo](FEM_ConstraintBodyHeatSource/pt-br.md) agora pode ser utilizada com o CalculiX e possui dois modos de entrada: taxa de dissipação \[W/kg\] e potência total \[W\]. [Pull request #14417](https://github.com/FreeCAD/FreeCAD/pull/14417)
-   As propriedades de rotação do [Sistema de coordenadas local](FEM_ConstraintTransform/pt-br.md) foram substituídas por uma única propriedade *Rotação* para maior consistência. [Pull request #14353](https://github.com/FreeCAD/FreeCAD/pull/14353)
-   Foi adicionada a ferramenta [Apagar Elementos](FEM_CreateElementsSet/pt-br.md) para permitir ocultar elementos de uma malha selecionados com um polígono. [Pull request #11492](https://github.com/FreeCAD/FreeCAD/pull/11492)
-   Os três exemplos de FEM na página inicial foram substituídos por um único exemplo, contendo todas as três variantes do modelo de viga em balanço (1D, 2D e 3D) em contêineres [Grupo](Std_Group/pt-br.md). [Pull request #15786](https://github.com/FreeCAD/FreeCAD/pull/15786)
-   As propriedades e caixas de seleção redundantes de *Fixação* do [Deslocamento de Restrição FEM](FEM_ConstraintDisplacement/pt-br.md) foram removidas. [Pull request #15531](https://github.com/FreeCAD/FreeCAD/pull/15531)
-   O comportamento dos botões Cancelar nos painéis de tarefas dos meshing [Gmsh](FEM_MeshGmshFromShape/pt-br.md) e [Netgen](FEM_MeshNetgenFromShape.md) foi corrigido, permitindo que sejam usados para abortar a malhação em andamento, o que é especialmente importante quando uma estimativa inicial do tamanho do elemento é muito baixa. Além disso, o meshing Netgen foi implementado, tornando possível usá-lo em todos os sistemas, incluindo o Linux. [Pull request #16515](https://github.com/FreeCAD/FreeCAD/pull/16515) e [Pull request #16433](https://github.com/FreeCAD/FreeCAD/pull/16433)
-   O algoritmo 2D *Quad quase estruturado* que estava ausente no mesher Gmsh foi adicionado, juntamente com outras correções. [Pull request #15624](https://github.com/FreeCAD/FreeCAD/pull/15624)



## Bancada de Materiais 

+++
| <img alt="" src=images/Materials_relnotes_1.0.png  style="width:384px;"> | O sistema de gerenciamento de materiais, incluindo o editor, foi completamente reformulado. Novas melhorias a esse respeito serão feitas posteriormente. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_1.0.png  style="width:384px;"> | A visualização da aparência foi adicionada para mostrar os materiais da mesma forma que serão exibidos nos documentos. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++

+++
| <img alt="" src=images/Material_appearance_relnotes_1.0.jpg  style="width:384px;"> | O novo sistema de materiais agora é utilizado para as propriedades de aparência. [Pull request #13294](https://github.com/FreeCAD/FreeCAD/pull/13294) |
+++



### Outras melhorias em Materiais 

-   Diálogos para visualizar as propriedades de Aparência e Material de um objeto foram adicionados e estão disponíveis como ferramentas *Inspecionar Aparência* e *Inspecionar Material*. [Pull request #13967](https://github.com/FreeCAD/FreeCAD/pull/13967)



## Bancada de Partes (FEM) 

+++
| <img alt="" src=images/Part_scale_relnotes_1.0.png  style="width:384px;"> | A ferramenta [Escala de Partes](Part_Scale.md) foi adicionada para permitir o dimensionamento fácil de formas sem a necessidade de usar ferramentas da Bancada de Desenho. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_1.0.png  style="width:384px;"> | A ferramenta [Espelho de Partes](Part_Mirror/pt-br.md) agora suporta objetos de referência, como um [Plano de Parte](Part_Plane/pt-br.md), para definir um plano de espelhamento arbitrário, além dos planos padrão XY, XZ e YZ. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Outras melhorias em Partes (FEM) 

-   A propriedade *Frenet* agora está habilitada por padrão para a ferramenta [Varredura de Partes](Part_Sweep/pt-br.md) para evitar um problema comum de renderização. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)
-   Um novo [modo de fixação](Part_EditAttachment/pt-br#Attachment_modes.md) chamado *Interseção* foi adicionado à Linha de Motor. Ele encontra a interseção de duas faces planas. [Pull request #12328](https://github.com/FreeCAD/FreeCAD/pull/12328)
-   A ferramenta [Projeção em Superfície de Parte](Part_ProjectionOnSurface/pt-br.md) agora é paramétrica. [Pull request #13158](https://github.com/FreeCAD/FreeCAD/pull/13158)
-   Agora, todos os ícones de Partes utilizam o tema azul, e as primitivas usam o mesmo ícone para a barra de ferramentas e a árvore de objetos.[Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   O comando [Criar esboço](Sketcher_NewSketch/pt-br.md) foi adicionado à barra de ferramentas e ao menu de Partes, já que operações como extrusão normalmente utilizam esboços como entrada. [Pull request #14318](https://github.com/FreeCAD/FreeCAD/pull/14318)
-   Um novo [modo de fixação](Part_EditAttachment/pt-br#Attachment_modes.md) chamado *XY paralelo ao plano* foi adicionado ao Plano de Motor e ao Motor 3D. Ele resulta em uma fixação semelhante à *XY do Objeto*, mas com o plano XY traduzido para passar por um vértice selecionado. Ao contrário do modo de fixação *Traduzir origem*, ele não move a origem em 2D/Sketcher. Pode ser usado com planos de origem, planos de datum e esboços, mas também com qualquer objeto com a propriedade *Colocação*. [Pull request #14372](https://github.com/FreeCAD/FreeCAD/pull/14372)



## Bancada de PartDesign 

+++
| <img alt="" src=images/Revolve_options_relnotes_1.0.png  style="width:384px;"> | Mais modos foram adicionados aos recursos de [revolução](PartDesign_Revolution/pt-br.md) e [groove](PartDesign_Groove/pt-br.md) - para o primeiro/último, até a face e duas dimensões. [Pull request #7193](https://github.com/FreeCAD/FreeCAD/pull/7193) |
+++

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_1.0.png  style="width:384px;"> | Os painéis de tarefa de [Pad](PartDesign_Pad/pt-br.md) e [pocket](PartDesign_Pocket/pt-br.md) foram aprimorados (itens da interface reorganizados, a opção **Selecionar face** oculta quando desnecessária, entre outros). [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_1.0.png  style="width:384px;"> | O modo de deslocamento foi adicionado para [padrão linear](PartDesign_LinearPattern/pt-br.md) e [padrão polar](PartDesign_PolarPattern/pt-br.md). O modo anterior foi renomeado para **Comprimento total**. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++

+++
| <img alt="" src=images/Single_solid_rule_relnotes_1.0.PNG  style="width:384px;"> | O suporte experimental para múltiplos sólidos dentro de um [Corpo](PartDesign_Body/pt-br.md) foi adicionado. Pode ser ativado nas preferências (para novos Corpos) ou nas propriedades de um Corpo existente. [Pull request #13960](https://github.com/FreeCAD/FreeCAD/pull/13960) |
+++

+++
| <img alt="" src=images/Pad_up_to_shape_relnotes_1.0.PNG  style="width:384px;"> | O modo *Até forma* foi adicionado para Pad e Pocket, permitindo que eles terminem em múltiplas faces, ao contrário do modo *Até face*, que permite a seleção de apenas uma face. [Pull request #11392](https://github.com/FreeCAD/FreeCAD/pull/11392) e [Pull request #14433](https://github.com/FreeCAD/FreeCAD/pull/14433) |
+++



### Melhoria Adicional no PartDesign 

-   A opção *Fazer espessura para dentro* agora está habilitada por padrão para a ferramenta [Espessura](PartDesign_Thickness/pt-br.md). [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)
-   Os pontos de datum agora mudam de cor quando destacados ou selecionados (assim como outros datums). [Pull request #12439](https://github.com/FreeCAD/FreeCAD/pull/12439)
-   Os ícones do Part Design foram ligeiramente aprimorados para maior consistência. [Pull request #13109](https://github.com/FreeCAD/FreeCAD/pull/13109)
-   Uma propriedade *Suprimido* foi adicionada para desabilitar temporariamente uma feature. [Pull request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) e [Pull request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   As barras de ferramentas do Part Design foram atualizadas - datums e ações baseadas em esboços agora estão agrupadas, [Verificação de Geometria da Peça](Part_CheckGeometry/pt-br.md) foi adicionada à barra de ferramentas e ao menu, e as barras de ferramentas foram divididas em individuais para permitir sua reorganização. [Pull request #13833](https://github.com/FreeCAD/FreeCAD/pull/13833)
-   Agora todas as features do Part Design utilizam os mesmos ícones para a barra de ferramentas e a árvore de objetos. [Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   Um novo modo *Transformar corpo* foi adicionado às ferramentas de espelhamento e padronização do Part Design, possibilitando a transformação da forma da feature base inteira, em vez das formas individuais das ferramentas de features aditivas e subtrativas. [Pull request #12589](https://github.com/FreeCAD/FreeCAD/pull/12589)
-   O layout da janela de diálogo da ferramenta [Furo](PartDesign_Hole/pt-br.md) foi aprimorado. [Pull request #14031](https://github.com/FreeCAD/FreeCAD/pull/14031)
-   A ferramenta [Migrar](PartDesign_Migrate/pt-br.md) foi removida da interface gráfica, pois era útil apenas para migrações entre versões agora altamente desatualizadas. [Pull request #15196](https://github.com/FreeCAD/FreeCAD/pull/15196)



## Bancada do Esboço 

+++
| <img alt="" src=images/Arc_helper_relnotes_1.0.png  style="width:384px;"> | A implementação de uma sobreposição de círculo para arcos (para resolver o problema de restrições aparecendo longe deles) foi concluída com um [comando para alterná-las](Sketcher_ArcOverlay/pt-br.md). [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_1.0.gif  style="width:384px;">Clique na imagem se a animação não começar.   Uma ferramenta de restrição [Dimensão](Sketcher_Dimension/pt-br.md) contextual foi adicionada para permitir a dimensionamento rápido e intuitivo com uma única ferramenta versátil. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_1.0.gif  style="width:384px;">Clique na imagem se a animação não começar.   [Parâmetros da ferramenta](Sketcher_Workbench#On-View-Parameters/pt-br.md) foram adicionados para permitir a dimensionamento durante a criação de formas. Dependendo da configuração de preferência \"On-View-Parameters\", eles podem ser desabilitados, reduzidos apenas às dimensões (sem as coordenadas iniciais) ou totalmente habilitados. Além disso, modos foram adicionados para as ferramentas de forma. Eles podem ser selecionados usando a tecla M ou uma lista suspensa no painel de tarefas. Algumas ferramentas possuem configurações adicionais na forma de caixas de seleção no painel de tarefas e atalhos de teclado adicionais. Atualmente, os novos recursos estão disponíveis para pontos, linhas, arcos, elipses, retângulos, polígonos, slots e B-splines. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) e seguintes
   

+++
| <img alt="" src=images/Offset_relnotes_1.0.png  style="width:384px;"> | Uma ferramenta [Deslocamento](Sketcher_Offset/pt-br.md) foi adicionada para permitir o deslocamento de curvas. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_1.0.png  style="width:384px;"> | O modo de [retângulo](Sketcher_CompCreateRectangles/pt-br.md) de três pontos foi adicionado em duas versões - 3 cantos ou centro e 2 cantos. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_1.0.png  style="width:384px;"> | Uma ferramenta [Slot com arco](Sketcher_CreateArcSlo/pt-brt.md) foi adicionada com dois modos (extremos de arco e extremos retos) para permitir a criação de slots curvados. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_1.0.gif  style="width:384px;">Clique na imagem se a animação não começar.   Uma restrição [Horizontal/Vertical](Sketcher_ConstrainHorVer/pt-br.md) foi adicionada. Ela aplica automaticamente a restrição horizontal se uma linha estiver mais próxima da orientação horizontal ou a restrição vertical se estiver mais próxima da orientação vertical. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_1.0.png  style="width:384px;"> | O renderizador das restrições de ângulo e raio foi aprimorado. As restrições de ângulo agora possuem linhas de extensão completas. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_1.0.png  style="width:384px;"> | Uma ferramenta [Transformação polar](Sketcher_Rotate/pt-br.md) foi adicionada para permitir a rotação e padrões circulares de geometrias de esboço. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++

   
  [384px](Arquivo:Sketcher_copy-cut-paste_relnotes_1.0.gif.md)Clique na imagem se a animação não iniciar.   Agora é possível copiar/cortar e colar geometria de esboço (com restrições) usando atalhos de teclado comuns: Ctrl+C, Ctrl+X e Ctrl+V. Não apenas dentro de um único esboço, mas também entre esboços diferentes ou até mesmo entre instâncias diferentes do FreeCAD. A geometria é copiada em forma de comandos Python, permitindo usos adicionais (ex.: compartilhamento em fóruns). [Solicitação de Pull #11537](https://github.com/FreeCAD/FreeCAD/pull/11537)
   

   
  [384px](Arquivo:Scale_transform_relnotes_1.0.png.md)   Uma ferramenta de [Transformação de Escala](Sketcher_Scale/pt-br.md) foi adicionada, permitindo escalar a geometria no esboço usando um ponto central selecionado e um fator de escala ou dois pontos de referência. [Solicitação de Pull #11265](https://github.com/FreeCAD/FreeCAD/pull/11265)
   

   
  [384px](Arquivo:B-spline_tangency_relnotes_1.0.gif.md)Clique na imagem se a animação não iniciar.   Foi adicionada a tangência às bordas B-spline, eliminando a necessidade de usar pontos finais e soluções alternativas. [Solicitação de Pull #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

   
  [384px](Arquivo:Sketcher_translate_relnotes_1.0.png.md)   As ferramentas [Array Retangular](Sketcher_RectangularArray/pt-br.md), [Mover](Sketcher_Move/pt-br.md), [Copiar](Sketcher_Copy/pt-br.md) e [Clonar](Sketcher_Clone/pt-br.md) foram substituídas por uma única ferramenta [Transformação de Array](Sketcher_Translate/pt-br.md). [Solicitação de Pull #11267](https://github.com/FreeCAD/FreeCAD/pull/11267)
   

   
  [384px](Arquivo:Sketcher_chamfer_relnotes_1.0.png.md)   Uma ferramenta [Chamfer](Sketcher_CreateChamfer/pt-br.md) foi adicionada com opção para alternar para o modo [Arredondamento](Sketcher_CreateFillet/pt-br.md). Além disso, não existe mais uma ferramenta de Arredondamento de Canto separada. A opção *Preservar Canto* (marcada por padrão) foi adicionada à ferramenta [Crie Arredondamento](Sketcher_CreateFillet/pt-br.md). [Pull request #12898](https://github.com/FreeCAD/FreeCAD/pull/12898)
   

   
  [384px](Arquivo:New_symmetry_relnotes_1.0.gif.md)Clique na imagem se a animação não iniciar.   A ferramenta [Simetria](Sketcher_Symmetry/pt-br.md) foi reformulada. Agora, ela funciona selecionando previamente a geometria e escolhendo uma linha ou ponto para refletir a geometria. Uma prévia é exibida e o comportamento da ferramenta pode ser controlado por meio das configurações da ferramenta. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

   
  [384px](Arquivo:Auto_midpoint_relnotes_1.0.gif.md)Clique na imagem se a animação não iniciar.   A restrição [Simétrica](Sketcher_ConstrainSymmetric/pt-br.md) agora é aplicada automaticamente quando o ponto médio de uma linha é selecionado. [Pull request #13147](https://github.com/FreeCAD/FreeCAD/pull/13147)
   

   
  [384px](Arquivo:Sketcher_arc_length_relnotes_1.0.png.md)   A restrição de dimensão de distância [Distância](Sketcher_ConstrainDistance/pt-br.md) agora pode ser usada para restrições de comprimento de arco (o arco circular deve ser pré-selecionado). [Pull request #12602](https://github.com/FreeCAD/FreeCAD/pull/12602)
   

   
  [384px](Arquivo:Point_color_relnotes_1.0.png.md)   A cor de renderização dos pontos agora varia conforme o tipo: Ponto/Extremidade normal (branco, criado por padrão com a ferramenta [CriarPonto](Sketcher_CreatePoint/pt-br.md)), Ponto de construção/Ponto central (azul), Ponto coincidente com outro (vermelho). [Pull request #13098](https://github.com/FreeCAD/FreeCAD/pull/13098)
   

   
  [384px](Arquivo:Trim_drag_relnotes_1.0.gif.md)Clique na imagem se a animação não iniciar.   A ferramenta [Recortar Borda](Sketcher_Trimming/pt-br.md) agora suporta modo arrastar e soltar. [Pull request #13188](https://github.com/FreeCAD/FreeCAD/pull/13188)
   



### Outras melhorias no Sketcher 

-   O modo \"Frame\" foi adicionado à ferramenta Retângulo. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Dois novos modos foram adicionados à ferramenta Linha: *Ponto, comprimento, ângulo* e *Ponto, largura, altura*. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Os ícones de [AlternarConstrução](Sketcher_ToggleConstruction/pt-br.md) e [AlternarRestriçãoDirigida](Sketcher_ToggleDrivingConstraint/pt-br.md) foram alterados. Agora o primeiro não é mais tão semelhante ao [Cópia de Carbono](Sketcher_CarbonCopy/pt-br.md) e ambos os ícones de alternância mudam ao serem clicados. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Os ícones do Sketcher foram reformulados para unificar sua aparência (largura de traços, cores e tamanhos de pontos). [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   Uma nova ferramenta opcional de [restrição Coincidente unificada](Sketcher_ConstrainCoincidentUnified/pt-br.md) foi introduzida. Esta ferramenta combina as ferramentas de restrição [Coincidente](Sketcher_ConstrainCoincident/pt-br.md) e [PontoNoObjeto](Sketcher_ConstrainPointOnObject/pt-br.md). [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)
-   O renderizador das restrições de ângulo de arco, ângulo de linha e distância de arco foi melhorado. [Pull request #12012](https://github.com/FreeCAD/FreeCAD/pull/12012)
-   Agora os tipos de borda podem ser personalizados não apenas pela cor, mas também pelo padrão e tamanho. Isso permite, por exemplo, linhas de construção tracejadas. [Pull request #11996](https://github.com/FreeCAD/FreeCAD/pull/11996)
-   O menu de clique direito agora é contextual e também inclui comandos de B-spline. [Pull request #11884](https://github.com/FreeCAD/FreeCAD/pull/11884) e [Pull request #11973](https://github.com/FreeCAD/FreeCAD/pull/11973)
-   Agora, ao clicar duas vezes em uma borda, toda a geometria conectada a ela é selecionada. [Pull request #11925](https://github.com/FreeCAD/FreeCAD/pull/11925)
-   As barras de ferramentas do Sketcher foram ligeiramente reorganizadas para maior clareza e consistência. [Pull request #13407](https://github.com/FreeCAD/FreeCAD/pull/13407) e [Pull request #13763](https://github.com/FreeCAD/FreeCAD/pull/13763)
-   Os ícones da ferramenta [Cópia de Carbono](Sketcher_CarbonCopy/pt-br.md) foram melhorados para melhor visibilidade. [Pull request #15074](https://github.com/FreeCAD/FreeCAD/pull/15074)



## Bancada de Trabalho Spreadsheet (Planilha) 



### Outras melhorias no Sketcher 

-   Agora, ao clicar duas vezes em uma planilha na visualização de Árvore, a bancada é alterada para esta. [Pull request #13137](https://github.com/FreeCAD/FreeCAD/pull/13137)
-   Os ícones da Planilha foram melhorados. [Pull request #13996](https://github.com/FreeCAD/FreeCAD/pull/13996)



## Bancada TechDraw 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_1.0.png  style="width:250px;"> | A ferramenta [CosmeticCircle](TechDraw_CosmeticCircle/pt-br.md) foi adicionada para permitir a criação de círculos cosméticos, selecionando o centro e inserindo o raio. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_1.0.png  style="width:250px;"> | A ferramenta [ArcLengthAnnotation](TechDraw_ExtensionArcLengthAnnotation/pt-br.md) foi adicionada para criar anotações semelhantes a dimensões do comprimento de arco de arestas selecionadas. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_1.0.png  style="width:250px;"> | A ferramenta [AddOffsetVertex](TechDraw_CommandAddOffsetVertex/pt-br.md) foi adicionada para criar vértices cosméticos como deslocamentos a partir de vértices selecionados. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++

+++
| <img alt="" src=images/Broken_view_relnotes_1.0.png  style="width:250px;"> | A ferramenta [BrokenView](TechDraw_BrokenView/pt-br.md) foi adicionada para representar objetos longos de maneira fácil. [Pull request #13331](https://github.com/FreeCAD/FreeCAD/pull/13331) |
+++

   
  <img alt="" src=images/Techdraw_smart_dimension_relnotes_1.0.gif  style="width:320px;">Clique na imagem se a animação não começar.   Uma nova ferramenta de dimensão contextual foi adicionada, baseada em [aquela introduzida no Sketcher](Sketcher_Dimension/pt-br.md). [Pull request #13525](https://github.com/FreeCAD/FreeCAD/pull/13525)
   



### Outras melhorias no TechDraw 

-   Seções baseadas em outras seções agora usam a forma original (não cortada) por padrão. Isso pode ser alterado nas configurações da seção para usar a seção anterior. [Pull request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281)
-   Objetos cosméticos e linhas centrais agora podem ser excluídos selecionando-os e pressionando a tecla Delete. Anteriormente, isso resultava na exclusão de toda a vista. [Pull request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) e [Pull request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   Um novo ícone mais intuitivo foi adicionado para a ferramenta [WeldSymbol](TechDraw_WeldSymbol/pt-br.md). [Pull request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   O comportamento do modo ponto + aresta da [LengthDimension](TechDraw_LengthDimension/pt-br.md) foi corrigido. [Pull request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   Um estado marcado foi adicionado para o botão [ToggleFrame](TechDraw_ToggleFrame/pt-br.md), para que o usuário possa ver se o botão está ativado ou não. [Pull request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   O comportamento da ferramenta [DecorateLine](TechDraw_DecorateLine/pt-br.md) foi melhorado. Agora, o clique duplo em uma linha invoca essa ferramenta. E os estilos de linha são corretamente restaurados se o usuário pressionar *Cancelar*. Anteriormente, não havia diferença entre pressionar *OK* e *Cancelar*. [Pull request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188)
-   A cor e a transparência das faces agora podem ser definidas por vista. [Pull request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   O modo de multisseleção foi adicionado e pode ser ativado nas Preferências. Nesse modo, múltiplos vértices, arestas e faces podem ser selecionados clicando neles, sem precisar manter pressionada a tecla Ctrl. [Pull request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   O [ExtensionAreaAnnotation](TechDraw_ExtensionAreaAnnotation.md) agora pode calcular áreas de faces arbitrárias. [Pull request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Linhas não contínuas agora seguirão os padrões ISO/ANSI em vez do estilo de linha Qt. Uma nova preferência foi adicionada para selecionar o padrão. [Pull request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   O comportamento da ferramenta [AxoLengthDimension](TechDraw_AxoLengthDimension.md) foi melhorado. Agora, ao dimensionar arestas paralelas aos eixos do sistema de coordenadas global, o valor real (3D) é calculado automaticamente e inserido na propriedade Format Spec (como texto). [Pull request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   A ferramenta [ExtensionPositionSectionView](TechDraw_ExtensionPositionSectionView.md) agora pode ser usada selecionando uma aresta em uma vista de seção e um vértice na vista de origem. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)
-   A ferramenta [ExtensionInsertRepetition](TechDraw_ExtensionInsertRepetition/pt-br.md), para inserir uma contagem repetida de características, foi adicionada. [Pull request #12509](https://github.com/FreeCAD/FreeCAD/pull/12509)
-   Pequenas, mas importantes melhorias de usabilidade foram feitas - clicar duas vezes na página do TechDraw agora entra nesse ambiente de trabalho e a ferramenta TechDraw MoveView foi substituída por simples arrastar e soltar na [árvore](Tree_view/pt-br.md). As ferramentas TechDraw ClipGroupAdd e TechDraw ClipGroupRemove também foram substituídas por esse comportamento de arrastar e soltar. [Pull request #13063](https://github.com/FreeCAD/FreeCAD/pull/13063)
-   Os modelos de desenho agora são automaticamente preenchidos com informações disponíveis (como data e título). [Pull request #13005](https://github.com/FreeCAD/FreeCAD/pull/13005)
-   A ferramenta [Project shape](TechDraw_ProjectShape/pt-br.md) foi removida do TechDraw, pois é herdada do antigo ambiente de desenho e não tem relação com uma página do TechDraw. [Pull request #13655](https://github.com/FreeCAD/FreeCAD/pull/13655)
-   A ferramenta [Insert View](TechDraw_View/pt-br.md) foi aprimorada para que possa lidar com mais tipos de objetos e configurações. Isso permitiu remover as seguintes ferramentas da barra de ferramentas: [SpreadsheetView](TechDraw_SpreadsheetView/pt-br.md), [ArchView](TechDraw_ArchView/pt-br.md), [Symbol](TechDraw_Symbol/pt-br.md), [Image](TechDraw_Image/pt-br.md) e [ProjectionGroup](TechDraw_ProjectionGroup/pt-br.md). [Pull request #13219](https://github.com/FreeCAD/FreeCAD/pull/13219)
-   A função de \"snapping\" foi adicionada para permitir o alinhamento automático de vistas e dimensões. O \"snapping\" pode ser temporariamente desativado com a tecla Alt. [Pull request #13659](https://github.com/FreeCAD/FreeCAD/pull/13659)
-   O manuseio de objetos cosméticos foi melhorado de várias maneiras. [Pull request #14216](https://github.com/FreeCAD/FreeCAD/pull/14216)
-   Muitos ícones do TechDraw foram melhorados. [Pull request #14873](https://github.com/FreeCAD/FreeCAD/pull/14873) e seguintes
-   O painel de tarefas da ferramenta [SurfaceFinishSymbols](TechDraw_SurfaceFinishSymbols/pt-br.md) foi significativamente melhorado visualmente. [Pull request #16147](https://github.com/FreeCAD/FreeCAD/pull/16147)



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/pt-br
