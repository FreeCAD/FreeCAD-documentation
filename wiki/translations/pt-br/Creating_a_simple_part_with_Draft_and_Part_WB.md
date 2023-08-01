---
- TutorialInfo:   Topic:Modeling
   Level:Beginner
   Author:heda
   Time:1.5 hours
   FCVersion:0.19 or above
   Files:
   SeeAlso:[Criando uma peça simples com a bancada Part](Creating_a_simple_part_with_Part_WB/pt-br.md), [Criando uma peça simples com a bancada Part Design](Creating_a_simple_part_with_PartDesign/pt-br.md)
---

# Creating a simple part with Draft and Part WB/pt-br







## Introdução

Este tutorial pretende ser usado como uma primeira introdução à bancada [Draft](Draft_Workbench.md) ![](images/Switch_DraftWorkbench.JPG ) no FreeCAD. O tutorial usa uma *forma 2D* para criar um *sólido 3D*, o último é realizado através da bancada [Part](Part_Workbench.md). Recomenda-se que o leitor trabalhe primeiro com o tutorial irmão *[Criando uma peça simples com a bancada Part](Creating_a_simple_part_with_Part_WB/pt-br.md)*, que cria o mesmo modelo com uma técnica diferente e ao mesmo tempo cobre mais do básico da interface de usuário do FreeCAD. Este tutorial espera que o usuário esteja brevemente familiarizado com a interface do usuário e alguns fluxos de trabalho disponíveis no FreeCAD. O objetivo do tutorial não é necessariamente mostrar a forma mais eficiente de usar o programa, mas sim conscientizar o leitor sobre as diferentes funcionalidades disponíveis no FreeCAD, como utilizá-las e onde encontrá-las.



### O que o tutorial aborda 

-   O modelo a ser feito
-   Criando o perfil 2D
-   Por que a extrusão pode falhar
-   Fazendo a extrusão do perfil
-   Criando o buraco vazado
-   Fazendo um esboço do perfil 2D
-   Qualidade de modelos
-   Finalizando



## O modelo a ser feito 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width:372px;">

![](images/T101pwb01-02_dims.png )



## Criando o perfil 2D 

Crie um novo documento e salve-o diretamente com um novo nome. Altere a visualização para <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [Topo](Std_ViewTop.md) e alterne para a visualização <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Bancada Draft](Draft_Workbench/pt-br.md). Sua tela deve ficar como abaixo. Se a grade não aparecer, ative/desative-a com <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> [Ligar/desligar grade](Draft_ToggleGrid/pt-br.md).

![](images/T101dwb01-01draftgrid.png )

Para iniciar o perfil, desenhe um <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Retângulo](Draft_Rectangle/pt-br.md) aleatório no plano xy clicando em 2 pontos na [Visualização 3D](3D_view/pt-br.md) formando qualquer diagonal de um retângulo. Uma aba de *Dados* se abrirá assim que o retângulo for traçado. Desta vez não vamos usá-la, mas é claro que você pode inserir as coordenadas do retângulo diretamente. Sua visualização 3D agora deve ter um retângulo desenhado, semelhante à imagem abaixo.

![](images/T101dwb01-02rectangleraw.png )

Ao trabalhar na bancada **Draft** quase sempre se desenha em um plano 2D. Esse plano 2D é chamado de *[Plano de trabalho](Draft_SelectPlane/pt-br.md)* e, se as configurações padrão forem usadas, ele sempre se alinhará automaticamente à visão 3D atual. Portanto, até que o perfil 2D seja concluído, é melhor simplesmente manter a visualização *Topo* (posição da câmera) e não brincar com a rotação da visualização. Se por acaso você o alterou, basta voltar para a visualização *Topo* antes de iniciar qualquer novo comando na bancada **Draft**.

A vista lateral do nosso modelo final tem o contorno externo de 100 x 50 mm, e seria bom se o canto inferior esquerdo fosse colocado na posição zero global. Isso pode ser feito através das *Propriedades*. Certifique-se de que o objeto **Rectangle** criado está selecionado na árvore e, em seguida, altere a *Posição* do retângulo para **(0, 0, 0)**, modifique a *Altura* (Height) para **50**mm e o *Comprimento* (Lenght) para **100**mm conforme as imagens abaixo.

![](images/T101dwb01-03rectangleprops.png )

O **Rectangle** está finalizado e deve ficar assim depois de aplicar <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Enquadrar tudo](Std_ViewFitAll.md) na visualização.

![](images/T101dwb01-04rectangledone.png )

Em seguida, vamos dividir o retângulo em suas quatro bordas, isso é feito selecionando primeiro o **Rectangle** e então o comando <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Regredir](Draft_Downgrade/pt-br.md) (ou rebaixar), a face preenchida desaparecerá e o objeto na árvore agora é um **Wire** (arame) ao invés de um **Rectangle**, mostrado na figura abaixo à esquerda. Usar **Regredir** mais uma vez quebrará o *Wire* em suas *bordas* (edges), mostradas na figura do meio abaixo.

![](images/T101dwb01-05rectangledowngrade.png )

Quem for observador notará que o ícone do objeto na árvore já mudou do *Wire* para uma *caixa azul*. Esta caixa azul é o ícone usado para objetos geométricos genéricos (objetos geométricos da bancada Part mais especificamente, mas isso é para leitores avançados). Selecione a borda vertical esquerda e clique em <img alt="" src=images/Draft_Upgrade.svg  style="width:24px;"> [Promover](Draft_Upgrade.md). O objeto *Edge* agora terá um ícone diferente e mudou o nome para **Line**. Agora é um objeto da bancada **Draft** onde se pode editar, por exemplo, o *ponto inicial* (Start) e o *ponto final* (End) na aba *Propriedades*. Isso não é possível com o *objetos de borda*.



### Criando o arredondamento (Filete) 

Comece selecionando as laterais superior e direita. Use o menu **Editar → Caixa de seleção** <img alt="" src=images/Std_BoxSelection.svg  style="width:24px;"> [Seleção de caixa](Std_BoxSelection/pt-br.md), clique no [24px](Image:Mouse_LMB.svg.md) **botão esquerdo do mouse**, arraste da direita pra esquerda, passando a caixa de seleção sobre as laterais e solte-o. Ao arrastar *da direita para a esquerda*, a seleção resultante inclui tudo total ou parcialmente dentro da área de seleção. Se arrastar *da esquerda para a direita*, apenas os objetos totalmente incluídos na área de seleção serão incluídos na seleção resultante. A seleção propriamente dita acontece quando o botão esquerdo do mouse é solto, não sendo mostrada previsão do que será selecionado.

![](images/T101dwb02-01filletboxselection.png )

Com as bordas do canto superior direito selecionadas, dê o comando <img alt="" src=images/Draft_Fillet.svg  style="width:24px;"> [Filete](Draft_Fillet/pt-br.md) na bancada **Draft**. Marque *Excluir objetos originais*, altere o *raio* para 20mm e pressione **enter**.

![](images/T101dwb02-02fillettaskpanel.png )

O objeto **Fillet** é criado e seu modelo agora deve ficar como abaixo.

![](images/T101dwb02-03filletdone.png )



### Criando o chanfro 

Para fazer o *chanfro* precisamos ter uma linha com a inclinação correta e também saber posicioná-la corretamente. Comecemos pela posição, que está na coordenada *(50, 50, 0)*. No perfil atual não temos um ponto lá, então vamos criar um fazendo uma *linha de ajuda temporária*. Primeiro selecione a **Linha** vertical esquerda, então crie a linha de ajuda com <img alt="" src=images/Std_DuplicateSelection.svg  style="width:24px;"> [Duplicar seleção](Std_DuplicateSelection.md) em **Editar → Duplicar seleção**, **Line001** é criada. Use as *Propriedades* e mova **Line001** 50 mm na direção x usando a propriedade *Placement*. Em seguida, duplique a *borda horizontal inferior*, e altere o *ângulo* da aresta para 30 graus, mais uma vez usando a propriedade *Placement*. O modelo agora deve se parecer com a imagem abaixo.

![](images/T101dwb03-01chamferhelp.png )

Em seguida, mova a *linha inclinada* para a posição. Para isso, usamos <img alt="" src=images/Draft_Move.svg  style="width:24px;"> [Draft Move](Draft_Move/pt-br.md) juntamente com a funcionalidade *snap* na bancada **Draft**, mais especificamente \"ponto final\" (Adquirir ponto final). Primeiro, certifique-se de que sua barra de ferramentas de encaixe seja semelhante à abaixo.

![](images/T101pwb03-02_snap.png )

Em seguida, selecione a linha inclinada, **Edge001**, pressione **Mover** e um painel *Tarefas* se abrirá.

![](images/T101dwb03-03_movetaskpanel.png )

Certifique-se de que *Copiar* esteja desmarcado. Passe o mouse sobre o *quarto superior* da *linha inclinada*, uma vez que o *ponto branco* é exibido no ponto certo e o símbolo do *ponto final* aparece, clique no botão [24px](Imagem:Mouse_LMB.svg.md) esquerdo do mouse. Mova o mouse para o quarto superior da linha auxiliar, assim que o ponto branco e o símbolo do ponto final aparecerem, clique no botão esquerdo do mouse. A sequência é ilustrada abaixo.

![](images/T101dwb03-04_moveline.png )

A linha agora está na posição correta, mas é muito longa. Para ajustar o comprimento <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> [Trimex](Draft_Trimex/pt-br.md) será usado. Selecione a *linha inclinada*, **Edge001**, pressione Trimex e depois clique na parte inferior da *linha vertical mais à esquerda*, **Line**, para usá-la como a aresta de corte. A projeção do ponto onde a aresta de corte é selecionada na aresta a ser cortada, determina o resultado. Se você selecionar a linha vertical mais à esquerda perto de sua extremidade superior, a parte errada da linha angular será aparada. A imagem abaixo mostra o comando **Trim**, a linha vertical pré-selecionada e o cursor pairando sobre o lado errado dessa linha. Se você olhar com atenção, poderá ver a visualização do resultado.

![](images/T101dwb03-05_trimline.png )

Apare também a linha vertical mais à esquerda para formar o canto inferior do chanfro. Selecione a *linha inclinada*, **Edge001**, perto de seu ponto final superior direito para obter um resultado correto. Se você cometer um erro ao aparar, basta usar <img alt="" src=images/Std_Undo.svg  style="width:24px;"> [Undo](Std_Undo.md) e <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Refresh](Std_Refresh.md) (o último geralmente chamado *atualizar*) e tente novamente.

![](images/T101dwb03-06_chamferlowercornerdone.png )

Para aparar a *linha superior*, o **Fillet** precisa ser *Rebaixado* para que a linha superior seja seu próprio objeto na visualização em árvore. Se você tentar apará-lo sem primeiro ter feito o rebaixamento, a função de aparo tentará aparar o arco no filete. Como a borda de corte, a *linha vertical do meio*, é perpendicular à borda a ser cortada, você não pode controlar o resultado do corte escolhendo um ponto correto na borda de corte. Aqui você precisa inverter a solução padrão mantendo pressionada a tecla **Alt** enquanto seleciona a aresta de corte.

O perfil está pronto e mostrado abaixo com as bordas organizadas em um <img alt="" src=images/Std_Group.svg  style="width:24px;"> [Grupo](Std_Group/pt-br.md) chamado **Profile** (ou *rotulado* para ser preciso no jargão do FreeCAD), juntamente com a linha de ajuda excluída. Os grupos podem ser usados para organizar os recursos em seus *documentos FreeCAD*, seu uso é semelhante a uma estrutura de pastas no sistema de arquivos de um computador. Para mover itens para dentro e para fora do grupo, basta *arrastar e soltar* na árvore.

![](images/T101dwb03-07_profiledone.png )



## Por que a extrusão pode falhar 

Salve o documento. Vamos experimentar neste parágrafo e queremos poder voltar ao modelo atual.

Vamos direto ao assunto: selecione todas as arestas no *grupo* **Profile**, e na bancada <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/pt-br.md) chame o comando <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Extrusão](Part_Extrude/pt-br.md). Um painel *Tarefas* se abre, aceite todos os padrões e clique em **OK**.

![](images/T101dwb04-01_extrudelineserror.png )

Isso não funcionou, mas parece fácil corrigir o erro, só precisamos especificar uma direção. Clique em **OK** para voltar ao painel de *Tarefas* e selecione *Direção personalizada*.

![](images/T101dwb04-02_extrudelineszaxis.png )

Aceite o eixo z padrão e mais uma vez clique em **OK**.

![](images/T101dwb04-03_extrudelinessheets.png )

Conseguimos fazer uma estrutura semelhante a uma cerca, a julgar pela visualização em árvore, cada aresta é tratada separadamente. Não é o sólido preenchido que queremos. Clique em [Undo](Std_Undo.md) e vamos tentar outra coisa.

Rolando até a parte inferior do painel *Tarefas* da **Extrusão** há uma opção *Criar um sólido*, marque essa opção e clique em **OK**.

![](images/T101dwb04-04_extrudelinesfilled.png )

Tudo desapareceu, claro que também não funcionou. Vamos ver por que nenhuma dessas maneiras está funcionando. No primeiro caso, recebemos um erro de que a direção não pôde ser determinada. Uma face plana tem uma normal, ou seja, uma direção, uma linha não. Pela nossa segunda tentativa, sabemos que funcionou quando fornecemos uma direção, então esse erro veio da tentativa de extrudar uma linha sem saber a direção. Alguém pode pensar que um arco tem uma (direção) normal, isso é verdade. Se você selecionar apenas a aresta que é o arco, o FreeCAD fará a extrusão, também com as configurações padrão.

No segundo caso funcionou, mas também conseguimos uma extrusão para cada borda que tínhamos em nossa seleção. Os objetos resultantes, entretanto, não são o que queremos, ou seja, um sólido.

No terceiro caso marcamos *Criar um sólido*, e acabamos com tudo desaparecendo. Os objetos na árvore também têm um ícone diferente, há um *ponto de exclamação* branco em um fundo vermelho, esse *ícone de sobreposição* específico significa que o objeto tem um erro que precisa ser corrigido. Pode-se ler sobre os diferentes tipos de [ícones de sobreposição](Tree_view/pt-br#Overlay_icons.md) no wiki.

Ao passar o mouse sobre qualquer um dos objetos da árvore com o ícone de sobreposição, uma dica de ferramenta é exibida, dizendo *Wire is not closed* (O fio não está fechado).

![](images/T101dwb04-05_extrudelineserrortooltip.png )

No nosso caso, o erro não pode ser corrigido. É *geometricamente impossível* criar um sólido a partir de uma única linha extrudada. Uma linha extrudada simplesmente se torna uma folha, ou *casca* no jargão do FreeCAD. Em outras palavras, esta não é uma limitação do FreeCAD, é um resultado fundamental da teoria geométrica. A razão pela qual a visualização 3D fica completamente em branco é que os recursos criados, ou objetos na visualização em árvore, têm erros na *forma* produzida e, portanto, não contêm nada para renderizar. No entanto, o FreeCAD cria os novos objetos do documento (neste caso, extrusões) e, portanto, oculta qualquer geometria/objeto usado para criar os novos objetos do documento. É por isso que a tela fica em branco ao tentar fazer um sólido a partir de uma linha ou linhas.

A dica da ferramenta diz tudo, para fazer a extrusão em um sólido é necessário um *fio fechado* ou *uma face*. Uma face é, por definição, simplesmente um fio fechado que é preenchido. Uma maneira de criar um fio fechado a partir das bordas de nosso perfil é selecionar todas elas e aplicar <img alt="" src=images/Draft_Upgrade.svg  style="width:24px;"> [Promover](Draft_Upgrade/pt-br.md). Se aplicado uma vez, torna-se um fio, enquanto ao mesmo tempo consome as arestas individuais da visualização em árvore. Se aplicado duas vezes, torna-se uma face, qualquer uma delas permite uma extrusão sólida bem-sucedida.

Antes de passar para o próximo parágrafo: abra a versão anterior do documento.



## Extrudando o perfil 

Outra maneira de criar o fio fechado é com o comando <img alt="" src=images/Part_Builder.svg  style="width:24px;"> [Construtor de forma](Part_Builder.md) da bancada Part, que permite fazer um fio sem consumir as arestas individuais . O **Construtor de forma** do *Part* é uma ferramenta poderosa para criar qualquer geometria no FreeCAD que pode ser usada posteriormente para criar sólidos complexos. O exemplo mais simples é criar uma linha entre dois vértices. Clique em **Construtor de forma** para abrir o painel *Tarefas*.

![](images/T101dwb05-01_shapebuildertaskpanel.png )

Podemos usar *Arame a partir de arestas* ou *Uma face a partir de arestas*. Várias seleções devem ser feitas com a tecla **Ctrl** pressionada. Vamos usar *Uma face a partir de arestas*. Uma vez que essa opção é selecionada, também pode-se selecionar *Planar*, faça isso também. Em seguida, selecione todas as arestas no perfil, a ordem não importa (neste caso) e clique em **Criar**, e depois em **Close** para voltar à Tree View. A *face* foi criada.

![](images/T101dwb05-02_shapebuilderfacedone.png )

Selecione **Face** na árvore e use a ferramenta **Extrusão**, defina o *comprimento* da extrusão para **30mm** e clique em **OK**.

![](images/T101dwb05-03_extrusiondone.png )



## Criando o furo passante 

Para fazer o furo precisamos de um cilíndro corretamente posicionado para fazer um corte booleano.

Crie um cilindro e posicione-o corretamente. Neste caso, o *raio* é de 5mm, a altura (*Height*) é definida para 60mm. Para o posicionamento, primeiro ele é *girado* -90 graus ao redor do eixo x, então posicionado em *(65, -5, 15)*. O 5 negativo na direção y ocorre porque a altura é 10mm maior do que o necessário.

![](images/T101dwb05-04_cylinderplaced.png )

Não faz mal aumentar a altura do cilindro mais do que o necessário. Para um modelo simples como este, não importa se o cilindro tem a altura exata do perfil. No entanto, é uma boa prática evitar faces coplanares para evitar erros numéricos no núcleo geométrico que podem, às vezes, resultar em efeitos estranhos ou falhas em operações subsequentes.

Com um corte booleano final, e depois de mudar a aparência do objeto resultante, o modelo é concluído.

![](images/T101dwb05-05_modelcomplete.png )



## Fazendo um esboço (Sketch) a partir do perfil 2D 

Usar a bancada **Draft** é uma maneira de criar um perfil 2D. Na bancada **Draft** uma linha pode ser feito no espaço 3D. O FreeCAD fornece outra ferramenta para fazer perfis 2D -- a <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> bancada [Sketcher](Sketcher_Workbench/pt-br.md). Usar um *esboço* é uma maneira mais versátil de criar um perfil 2D. Qualquer perfil 2D feito na bancada **Draft** pode ser convertido em um esboço *sem restrições*.

Comece escondendo o recurso **Cortar** e deixe as arestas do perfil visíveis. Selecione as bordas e na bancada **Draft** pressione o botão da barra de ferramentas <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> [Traço para esboço](Draft_Draft2Sketch/pt-br.md). Você deve ver o mesmo que na imagem abaixo.

![](images/T101dwb06-01_draft2sketch.png )

Em seguida, oculte as bordas originais e clique duas vezes no objeto **Sketch** na árvore. Isso vai abrir o esboço na visão 3D e a aba *Tarefas* na Tela combinada.

![](images/T101dwb06-02_sketchedit.png )

É assim que fica quando se *edita um esboço*. Como este não é um tutorial para usar o Sketcher, vá em frente e feche-o. Se você deseja uma introdução ao processo, que é um fluxo de trabalho básico em qualquer CAD paramétrico 3D, siga o tutorial irmão *[Criando uma peça simples com Part Design](Creating_a_simple_part_with_PartDesign/pt-br.md)*.

Com o **Sketch** fechado e selecionado, na bancada **Part** use Extrude da mesma forma que antes. O bloco básico do modelo simples está pronto mais uma vez.

![](images/T101dwb06-03_sketchextruded.png )



## Qualidade dos modelos 

Mais cedo ou mais tarde, ao trabalhar com CAD paramétrico 3D, você encontrará um modelo quebrado, seja um que você mesmo criou ou um modelo que você importou. Um modelo quebrado pode funcionar para seu propósito, mas na maioria das vezes, há operações subsequentes que simplesmente não funcionarão. Para reparar um modelo quebrado, é preciso saber o que reparar, é aqui que entram as ferramentas de verificação de qualidade integradas no FreeCAD.

Primeiro, vamos verificar a qualidade do recém-criado **Extrude001**. Com a bancada **Part** ativa, primeiro selecione **Extrude001** e depois use o comando <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Verificar a geometria](Part_CheckGeometry/pt-br.md). Marque todas as caixas de seleção de configurações, exceto a superior, e clique no botão **Executar verificação**.

![](images/T101dwb07-01_geocheck.png )

Nosso modelo está OK, nenhum erro é relatado. Há também uma listagem do conteúdo dos modelos, ou no jargão do FreeCAD, o conteúdo da *forma*, ou seja, como ela é montada desde o início. Aqui pode-se ver que, aparentemente, para fazer um *sólido* é necessário também uma *casca*, e a casca é feita de *faces*, e assim por diante. Em outras palavras, você pode criar qualquer sólido simplesmente começando por fazer pontos, ou *vértices*, a partir desses se faz *arestas*, e a partir dessas se criam *fios*, e a partir dos fios faz-se *faces* que são costuradas em uma *concha*, da qual se chega finalmente a um *sólido*. Um sólido só pode ser feito de uma casca estanque. Uma casca não estanque é uma fonte comum de modelos CAD problemáticos, pode acontecer, por exemplo, com a geometria importada criada em um software diferente, especialmente ao usar os formatos de arquivo neutros comumente disponíveis.

Outra verificação que se pode fazer é relacionada ao **Sketch**. Feche o painel *Tarefas* para verificar a geometria. Selecione **Sketch**, expanda **Extrude001** na árvore, se necessário, para ver o objeto do esboço. Mude para <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> bancada [Sketcher](Sketcher_Workbench/pt-br.md), use o comando <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [Validar um esboço](Sketcher_ValidateSketch.md), abre-se um painel *Tarefas*. Clique no botão **Procurar** em *Coincidências faltantes*. Ele destaca e relata *6* delas, ou seja, todos os pontos onde as arestas se encontram.

![](images/T101dwb07-02_sketchvalidate.png )

Clique em **OK** na caixa de diálogo pop-up e, em seguida, clique no botão **Consertar** para corrigir as *Coincidências faltantes*. Se você fechar o painel *Tarefas* e entrar no *modo de edição* do **Esboço**, ele reportará *12 graus de liberdade*, ao contrário do *24* anterior \'. Isso foi conseguido adicionando *restrições coincidentes* aos pontos finais das linhas.

O leitor atento percebe que ao usar as arestas do *Draft*, essas tiveram que ser unidas em uma linha fechada para fazer uma extrusão sólida, enquanto no Sketcher isso aparentemente não era necessário. A lógica aqui é que o esboço é um objeto, e a extrusão de um objeto o trata como se ele fosse uma linha fechada (neste caso).

Finalmente, deve-se ressaltar que, embora a criação de objetos subsequentes a partir de esboços com vértices abertos possa funcionar, é melhor prática não ter nenhum, bem como ter um totalmente esboço restrito (ao invés de um com graus de liberdade). A razão pela qual funciona aqui é que o esboço é criado a partir de um perfil *Draft* construído de forma que os pontos finais das arestas coincidam sem nenhuma lacuna. Se você desenhar à mão em um esboço e também tentar combinar os pontos finais manualmente, é praticamente garantido que os pontos finais não coincidirão, ou seja, as lacunas (embora não sejam realmente visíveis na tela) serão grandes o suficiente para que o processo não possa considerar as arestas passíveis de serem unidas geometricamente.



## Finalizando

Depois de passar pelo tutorial, você se familiarizou um pouco com a funcionalidade básica do FreeCAD, junto com as bancadas principais **Part** e **Draft**. Você também está ciente da existência da bancada **Sketcher**, que para muitos usuários experientes é a única ferramenta usada para criar perfis 2D posteriormente utilizados em operações de sólidos. O uso de *esboços* é um conceito central na bancada **Part Design**. Sugere-se que você aprenda as bancadas *Sketcher* e **Part Design** se seu foco for criar sólidos. O tutorial irmão *[Criando uma peça simples com Part Design](Creating_a_simple_part_with_Part_Design/pt-br.md)* cria o mesmo modelo deste tutorial. Se seu foco é modelar edifícios, seu próximo aprendizado deve ser as bancadas **Draft** e **Arch**.

Por fim, o FreeCAD é feito por voluntários em seu tempo livre. Se você quiser que os recursos do FreeCAD avancem ainda mais, considere [contribuir](Help_FreeCAD.md) para o FreeCAD, por exemplo, melhorando a documentação.



---
⏵ [documentation index](../README.md) > Creating a simple part with Draft and Part WB/pt-br
