---
- TutorialInfo:   Topic:Modeling
   Level:Beginner
   Author:GlouGlou
   Time:1 hour
   FCVersion:0.17 or above
   Files:
   SeeAlso:[Creating a simple part with Part WB](Creating_a_simple_part_with_Part_WB/pt-br.md), [Creating a simple part with Draft and Part WB](Creating_a_simple_part_with_Draft_and_Part_WB/pt-br.md)
---

# Creating a simple part with PartDesign/pt-br





![](images/GGTuto1_Vue.PNG )

Este tutorial visa ensinar aos iniciantes do FreeCAD alguns recursos básicos por meio de um exemplo. Depois de ver o básico na [Central do Usuário](User_hub/pt-br.md), você poderá modelar uma primeira peça passo a passo.

**Abordaremos neste tutorial em particular:**

-   Usando a bancada [Part Design](PartDesign_Workbench.md), traçando o esboço.
-   Usando os recursos Pad e Pocket.
-   Mudança de cor e transparência.
-   Mover a peça manualmente.
-   Exibindo dimensões de referência no esboço.
-   Editando uma ou mais dimensões.
-   Usando recurso de geometria externa e usando um plano de referência para centralizar um furo.



### Usando a [Bancada Part Design](PartDesign_Workbench.md), traçando o esboço 

Crie um novo documento e mude para o **[<img src=images/Workbench_PartDesign.svg style="width:24px"> a '''bancada Part Design'''** usando o [workbench selector](Getting_started/pt-br#Exploring_the_interface.md) (rotulado 10 na imagem vinculada) ou acessando o menu *Vista → Bancada*. O FreeCAD começará com as barras de ferramentas na parte superior, a tela combinada à esquerda e a visualização 3D à direita.

**Crie um corpo:**

Clique em <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Criar corpo](PartDesign_Body.md). ***Nota:** não confunda o Corpo, cujo ícone é azul, com a Parte, cujo ícone é amarelo.* Na aba Modelo, na barra lateral da Tela combinada, um novo objeto chamado \"Body\" (corpo em português) aparece sob o rótulo do documento, que atualmente é \"Unnamed\" (ou \"sem nome\", em português), pois ainda não salvamos nosso documento. O Corpo é um contêiner no qual os recursos da Part Design são organizados sequencialmente para formar um único sólido. Ele contém seus próprios eixos e planos de referência. Ele será destacado em azul claro na árvore na aba Modelo, o que significa que está ativo, ou seja, podemos editar os elementos que ele contém, bem como adicionar novos elementos a ele. Se não estiver realçado, clique duas vezes ou clique com o botão direito do mouse e selecione *Alternar o corpo ativo* no menu que se abre. À frente da etiqueta Body, existe um ícone azul idêntico ao anterior, e uma seta ou um sinal de mais, dependendo do seu sistema operacional. Clicar na seta ou no sinal de adição na frente de Corpo expande seu conteúdo. Neste ponto, ele contém apenas um elemento chamado *Origin*. Na frente de *Origin* também há uma seta ou sinal de mais. Clique nele para expandir seu conteúdo. Isso revela os eixos e planos de referência acima mencionados, conforme mostrado na imagem abaixo:

![](images/PartDesign_Body_tree_Unnamed.png ) *O corpo ativo recém-criado com seu conteúdo expandido.*

A *Origin* está acinzentada, o que indica que seu conteúdo não é visível na visualização 3D. Você pode tornar o conteúdo de *Origin* visível na visualização 3D selecionando *Origin* e pressionando a barra de espaço em seu teclado. *Origem* agora aparecerá em preto na árvore. Pressione a barra de espaço novamente para ocultar seu conteúdo na visualização 3D. Clique novamente na seta ou no sinal de mais na frente de *Origin* para recolher seu conteúdo na árvore.

Antes de continuarmos, vamos aproveitar para renomear o Corpo.

**Renomeando Body:**

Na árvore da aba Modelo, clique em *Body* com o botão direito do mouse. Selecione Renomear e digite um nome, por exemplo \"Body part1\" e pressione **Enter** para validar.

**Criando um esboço:**

Vamos agora traçar o esboço que define a forma geral da peça. Um esboço é um diagrama que descreve um perfil a ser aplicado a um recurso para produzir uma forma. Pode ser \"positivo\" ou \"aditivo\", como um bloco, por exemplo; ou \"negativo\" ou \"subtrativo\", como um bolso.

Aqui, como a forma geral da peça é regular ao longo do eixo Y, criaremos o bloco ao longo deste eixo.

Pressione <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Criar um esboço](Sketcher_NewSketch.md). A tela combinada agora muda para a aba **Tarefas** e exibe a caixa de diálogo *Selecione um objeto*. Esta caixa de diálogo espera a seleção de um plano ao qual anexar nosso esboço e lista os planos disponíveis. Selecione *XZ_Plane (Plano de base)* e clique em **OK**. A interface agora muda, o Sketcher (ferramenta de desenho) agora assume e suas barras de ferramentas aparecem acima da visualização 3D. Estamos no plano XZ do corpo para traçar o esboço.

Para ajudar no esboço, defina as seguintes opções em \"Controles de edição\" na aba Tarefas à esquerda:

-   Mostrar grade: marcado
-   Tamanho da grade: 10 mm
-   Restrições automáticas: marcado

Traçaremos o seguinte esboço:

![](images/GGTuto1_0.PNG )

**Vamos começar com os primeiros segmentos:**

Selecione a ferramenta <img alt="" src=images/Sketcher_Line.svg  style="width:24px;"> [Criar linha](Sketcher_CreateLine.md). Clique no ponto de origem, primeiro certificando-se de que um pequeno ponto vermelho apareça ao lado e à direita do ponteiro do mouse. Clique em seguida no eixo X cerca de 10 quadrados à direita ou cerca de 100 mm. Se o segmento não tiver exatamente 100 mm neste ponto, não importa, depois daremos a ele uma dimensão fixa que garantirá esse comprimento.

Faça o mesmo para os outros segmentos, tente mirar nos pontos que você criou que devem acender em amarelo. O que significa que esses pontos serão coincidentes. Você deve obter algo assim:

![](images/GGTuto1_1.PNG )

Observe as pequenas linhas vermelhas acima e ao lado dos segmentos que você desenhou: são restrições horizontais e verticais. Suas linhas são forçadas a ficar na horizontal ou na vertical. Observe também o símbolo em forma de um pequeno arco à esquerda: significa que o ponto está fixo no eixo Z.

Agora escolha diferentes segmentos de linha com o botão esquerdo do mouse e, mantendo o botão esquerdo pressionado, arraste o mouse para tentar movê-los: alguns são livres, outros não.

**Aplicando restrições:**

Na parte superior da Tela combinada, nas Mensagens no painel Tarefas, você pode ler o número de graus de liberdade (DoF - do inglês \"Degrees of Freedom\") dos elementos já esboçados: deve ser cerca de 6. O objetivo das restrições é reduzir o número de graus de liberdade para 0.

A linha inclinada deve estar livre para girar neste momento: daremos a ela uma restrição de ângulo para corrigi-la.

Clique na linha inclinada e depois na linha inferior; uma vez selecionadas, essas linhas ficarão verdes escuras; então clique no ícone <img alt="" src=images/Constraint_InternalAngle.svg  style="width:24px;"> [Ângulo de restrição](Sketcher_ConstrainAngle.md).

![](images/GGTuto1_2.PNG )

Insira um valor de 30°. As linhas têm um ângulo fixo agora. A restrição foi criada à esquerda do esboço; com o mouse, mova-a para dentro do perfil.

Vamos agora restringir o tamanho da linha inferior: selecione-a e clique em <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:24px;"> [Restrição de distância horizontal](Sketcher_ConstrainDistanceX.md).

Digite um valor de 100 mm. A linha vertical à direita agora se alinha exatamente com o 10º quadrado da grade à direita da origem.

Vamos definir a altura geral do perfil selecionando o ponto mais alto à esquerda e depois o ponto de origem. Clique em <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:24px;"> [Restrição a distância vertical](Sketcher_ConstrainDistanceY.md) e insira um valor de 50 mm.

Faça o mesmo para o comprimento horizontal da linha inclinada com outra restrição de distância horizontal de 50 mm.

Afaste as dimensões do perfil para melhor visibilidade. Deve ficar parecido com isso:

![](images/GGTuto1_3.PNG )

Observe que o número de graus de liberdade foi reduzido para 2. São as extremidades ainda abertas.

**Traçando o arco**

Clique em <img alt="" src=images/Sketcher_Arc.svg  style="width:24px;"> [Criar arco](Sketcher_CreateArc.md), posicione o centro em aproximadamente x = 80 y = 30; em seguida, clique para definir o primeiro ponto inicial do arco no ponto final direito da linha horizontal superior; em seguida, clique para definir o final do arco para o ponto final superior da linha vertical direita (certifique-se de que os pontos estejam destacados em amarelo antes de clicar).

Dê ao raio uma restrição de raio: selecione o arco, então clique em <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Restrição de raio](Sketcher_ConstrainRadius.md) e então insira um valor de 20 mm.

Agora vamos fazer o arco tangente às linhas às quais ele está conectado: selecione o arco, a linha superior e clique em <img alt="" src=images/Constraint_Tangent.svg  style="width:24px;"> [Restrição tangente](Sketcher_ConstrainTangent.md). Uma mensagem *Substituição de restrição* aparece, clique em **OK**. Faça o mesmo para a restrição de tangente no outro lado do arco.

Procedemos em duas etapas para criar o esboço, mas também poderíamos ter traçado o perfil completamente antes de restringi-lo totalmente.

**Esboço totalmente restrito:**

Se você trabalhou direitinho, deve ter algo assim:

![](images/GGTuto1_4.PNG )

O esboço ficou verde, o que significa que está totalmente restrito. Não há mais ambiguidade, tudo está perfeitamente definido. Isso se confirma pela mensagem do solucionador no canto superior esquerdo. Observe também que o centro do arco se moveu ligeiramente, de fato. Devido a essas três últimas restrições, o FreeCAD calculou a verdadeira posição do centro.

Se o seu esboço ainda não estiver verde, um ou mais pontos não são coincidentes (2 pontos podem ser sobrepostos, mas não coincidentes). Faça uma pequena janela (janela de captura) ao redor de um ponto para selecionar e crie uma [24px](Arquivo:Constraint_PointOnPoint.svg.md) [Restrição de coincidência](u200eSketcher_ConstrainCoincident.md). *Observação: não confunda a restrição de coincidência com Criar ponto; embora seus ícones sejam semelhantes, o último tem um ícone maior; adiciona um ponto solitário no esboço.*

Proceda da mesma forma com todos os pontos.

Se o seu esboço ainda não estiver verde, verifique se todas as linhas (exceto a inclinada) têm restrição <img alt="" src=images/Constraint_Horizontal.svg  style="width:24px;"> [Horizontal](Sketcher_ConstrainHorizontal.md) ou [24px ](File:Constraint_Vertical.svg.md) [Vertical](Sketcher_ConstrainVertical.md) e adicione se necessário.



### Usando os recursos Preencher e Perfuração 

Clique em **Close** (fechar) na guia Tarefas, no canto superior esquerdo. Saímos automaticamente da bancada Sketcher e a bancada Part Design é ativada novamente. A Tela combinada volta para a aba Modelo. Se você deixou seu *Body part1* expandido, você verá um novo elemento **Sketch** abaixo de *Origin* e aninhado sob o *Body part1*.

Neste ponto, vamos salvar nosso documento. Dê um nome a ele (por exemplo, \"tutorial1\" ou qualquer nome que você ache interessante). É uma boa prática salvar seu documento com frequência, por exemplo, depois de concluir um esboço ou um recurso.

Clique em <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> **Isométrico** e depois em <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Enquadrar tudo](Std_ViewFitAll.md) e ficamos com uma visão 3D isométrica centralizada.

Clique em <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Preencher](PartDesign_Pad.md), insira um comprimento de 30 mm. Clique em **OK**. A forma está completa. Na árvore, um objeto **Pad** (que chamamos de recurso) aparece no lugar do *Sketch*. Na verdade, reivindicou o *Sketch*, já que é baseado nele; clicar na seta ou no sinal de mais na frente de *Pad* para expandi-lo revelará o *Sketch* abaixo, que foi automaticamente ocultado (seu rótulo fica esmaecido).

Observe que a forma criada forma um sólido.

![](images/GGTuto1_5.PNG )

**Criando o buraco**

Clique no lado superior (quadrado) da peça e clique no ícone <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> para criar um novo esboço. O FreeCAD cria um novo esboço anexado a esta face. Portanto, estamos em um plano paralelo ao plano absoluto XY, mas deslocado em altura da altura da peça, ou seja, 50 mm.

Você pode mudar a visualização 3D para uma vista isométrica <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> ou ficar na vista superior <img alt="" src=images/Std_ViewTop.svg  style="width:24px;">. A qualquer momento, você pode retornar à visualização Sketch (a visualização é orientada para enfrentar o plano do sketch) usando o ícone <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:24px;"> [Ver esboço](Sketcher_ViewSketch/pt-br.md).

Observe que a origem desse novo esboço é a do corpo. Podem ser diferentes, mas aqui se confundem com a origem absoluta.

Com a ferramenta <img alt="" src=images/Sketcher_Circle.svg  style="width:24px;"> [Criar círculo](Sketcher_CreateCircle.md), clique mais ou menos no centro da face e faça um círculo de qualquer raio.

Selecione o círculo e crie uma <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Restrição de raio](Sketcher_ConstrainRadius.md), insira um valor de 5 mm.

Selecione o centro do círculo e crie uma <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Restrição de bloqueio](Sketcher_ConstrainLock.md); clique duas vezes na dimensão horizontal e insira -65 mm (aqui indicamos uma posição relativa à origem do esboço). Faça o mesmo para a dimensão vertical (15 mm). O círculo assume sua posição correta e o esboço fica verde, indicando que está totalmente restrito:

![](images/GGTuto1_6.PNG )

Feche o esboço; na árvore um novo objeto **Sketch001** apareceu abaixo de *Pad*. Enquanto *Sketch001* ainda estiver selecionado, clique em <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Perfuração](PartDesign_Pocket.md).

Perfuração é um recurso chamado \"subtrativo\", ele retira material da nossa peça, aqui na forma de um cilindro já que o esboço é um círculo. No \"Tipo\" defina \"Atravessando de tudo\" para cortar completamente a peça. Pressione **OK** para concluir. Na árvore um novo elemento rotulado **Pocket** aparece na parte inferior do *Body part1* e reivindica *Sketch001*.



### Mudando cor e transparência 

É possível alterar a cor da peça, muitas vezes é útil distinguir uma peça entre outras. A transparência da peça também pode ser modificada, o que é útil para visualizar seu interior.

Selecione o corpo **Body part1**; certifique-se de que a aba Modelo da Tela combinada esteja selecionada e, na parte inferior dela, clique na aba *Vista*; localize a propriedade *Shape Color*; pode ser necessário usar a barra de rolagem vertical à direita para encontrá-la. Você também pode ampliar a coluna *Propriedade*: passe o mouse sobre a linha de separação entre os cabeçalhos *Propriedade* e *Valor*; quando o ponteiro se transformar em uma seta de dois lados, pressione e segure o botão esquerdo do mouse, arraste para o lado e solte. Na coluna da direita, clique no quadrado cinza, que abre a caixa de diálogo **Select color** . Escolha outra cor e clique em OK. Em seguida, novamente na aba *Vista*, altere o valor de *Transparency*, por exemplo para 50 e pressione **Enter** para concluir (0 = totalmente opaco, 100 = totalmente transparente).

O furo agora está visível dentro da peça. Isso geralmente é útil para ver as faces ocultas ou internas do modelo.

Você também pode variar \"Line Color\" e \"Line Width\" para alterar a espessura da linha e a cor do contorno da peça.

### Mova a peça manualmente 

Vá para o menu *Vista* e selecione *Ligar/desligar símbolo de eixos*. Estes são os eixos absolutos. Você deve ver na visualização 3D os 3 eixos X, Y, Z em vermelho, verde e azul. Este marco nos ajudará a nos orientar no espaço. Este marco é fixo e imutável, ou é a vista que gira ou o objeto que gira neste espaço.

Selecione **Body part1**. Na parte inferior da Tela combinada à esquerda, você verá isso (a guia *Dados* precisa estar selecionada, talvez seja necessário clicar nela):

![](images/GGTuto1_10.PNG )

Clique nos três pontinhos, ou seja, nas reticências (caso não apareçam, clique no *Valor* do campo **Posicionamento**). Isso abre uma nova caixa de diálogo na aba *Tarefas*. Usando as setas você pode variar a posição e os ângulos da peça. Na verdade, é a posição do corpo (portanto, sua origem) que se move no espaço, a orientação da visualização 3D não muda.

Outro método: na Tela combinada, selecione o **Body part1** e clique com o botão direito do mouse, depois selecione *Transformar*. Uma visão como esta aparece:

![](images/GGTuto1_11.PNG )

Segure e arraste os cones ao longo dos eixos ou das esferas para mover o corpo em todas as direções.

Verifique, em seguida, redefina os ângulos e as coordenadas para 0.



### Exibindo dimensões de referência no esboço 

Pode ser útil conhecer as dimensões de algumas partes do desenho a partir do cálculo interno do FreeCAD. Isso pode ser usado apenas para referência, ou posteriormente para definir outras dimensões, por exemplo.

Na árvore da aba *Modelo*, se necessário, expanda *Body part1* e depois *Pad* para mostrar o primeiro *Sketch*. Clique duas vezes nele (ou clique com o botão direito do mouse e selecione *Editar esboço* no menu que se abre). Clique em <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:24px;"> [Ativar/desativar restrição atuante ou de referência](Sketcher_ToggleDrivingConstraint.md). (**Nota:** dependendo da resolução do seu monitor, este ícone pode não estar visível. Na extremidade direita da barra de ferramentas *Restrições*, você pode encontrar um botão **»**. Clique nele para expandir e acessar os ícones recolhidos.) A partir de agora, podemos criar dimensões de referência em vez de restrições dimensionais: elas serão azuis e não terão influência nas formas do esboço de onde vêm, elas são calculadas automaticamente.

Note que as ferramentas de restrição (de distância horizontal, etc) mudaram para cor azul. Proceda como na criação de restrições normais, mas agora as informações serão apenas apresentadas e não estarão restringindo a peça de verdade. Você pode exibir essas dimensões, por exemplo:

![](images/GGTuto1_7.PNG )

Podemos ver, por exemplo, que o arco tem um comprimento de 20, pois é tangente às arestas.

Também podemos ver que o FreeCAD calcula a face esquerda (50-50xTAN(30°)), bem como a dimensão da distância do eixo do arco com a origem.



### Editando uma ou mais dimensões 

Durante a modelagem, você pode variar as dimensões do modelo. É muito simples: para a espessura da peça, clique duas vezes em *Pad* e insira um novo valor, 40 mm, por exemplo. Na parte inferior da *Tela combinada* você também pode alterar esse valor. Verifique que a forma do objeto mudou.

Faça o mesmo para o comprimento total da peça: clique duas vezes em Sketch, depois clique duas vezes na restrição dimensional de 100 mm, altere para 110 mm e confirme.

Podemos ver que a peça foi ampliada, mas o furo não está mais centrado no meio da face superior. Isso ocorre porque ele foi restrito à origem do esboço. O que não corresponde necessariamente ao que se gostaria. O buraco deve ficar no centro, seja qual for o tamanho da face.

### Centralizando o buraco 

**Primeiro método usando geometria externa**

Edite novamente o esboço do furo e apague suas restrições de distância horizontal e vertical.

Em seguida, clique em <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Geometria externa](Sketcher_External.md).

Vamos agora criar duas linhas no esboço, mas extraídas de uma forma (ou recurso) externa a esta e previamente definida: a do Pad.

Clique em uma aresta vertical na parte superior da peça. Por exemplo, o lado da inclinação da borda.

Uma nova linha magenta aparecerá acima da aresta. Repita para a outra borda, no lado arredondado.

Agora podemos usar essas linhas (especialmente os pontos em suas extremidades) para centralizar o círculo, porém devemos adicionar duas linhas de construção: por exemplo, as diagonais.

Clique em <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Ativa/desativa geometria de construção](Sketcher_ToggleConstruction.md). Mudamos para o modo de construção: as linhas ficarão azuis e serão descartadas fora do modo de edição do esboço. Eles permitirão fixar o centro do círculo. Note que a cor dos ícones nas ferramentas também ficam azuis, indicando que estamos nesse modo. Crie as diagonais da mesma forma que desenhou as primeiras linhas. Certifique-se de que todos os pontos são coincidentes.

Em seguida, selecione o centro do círculo, depois as duas linhas diagonais azuis e clique em <img alt="" src=images/Constraint_PointOnObject.svg  style="width:24px;"> [Restringir um ponto sobre um objeto](Sketcher_ConstrainPointOnObject.md), o círculo deve ser centralizado na interseção das diagonais, que está no centro da face. O croqui deve ser verde, totalmente restringido (é essencial). Observe que além do raio do círculo, não é mais necessário criar restrições dimensionais.

Observe que, além de alternar a barra de ferramentas para o modo de construção, o botão <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Ativa/desativa geometria de construção](Sketcher_ToggleConstruction.md) também pode alternar elementos individuais do Sketcher para o modo de construção, caso tenham sido selecionados. Se você acidentalmente alternar um elemento para o modo de construção, poderá obter um erro ao sair do esboço.

![](images/GGTuto1_8.PNG )

Saindo do esboço, vemos que o círculo está bem centrado. (O recurso de bolso não foi excluído, mas modificado). Se você alterar novamente as dimensões da peça, a espessura ou o comprimento, o círculo permanecerá centralizado na face.

**Evite linhas de construção:**

Muitas vezes é possível evitar a criação de linhas de construção. Você pode editar o esboço novamente, apagar as linhas de construção e usar um <img alt="" src=images/Constraint_Symmetric.svg  style="width:24px;"> [Restrição simétrica](Sketcher_ConstrainSymmetric.md) entre os dois vértices opostos das linhas geométricas externas e o centro do círculo (selecione os pontos nesta ordem):

![](images/GGTuto1_12.PNG )

Obtemos exatamente o mesmo resultado para a posição do furo. De fato, graças às restrições disponíveis no ambiente de trabalho do Sketcher, existem muitos métodos possíveis. Este exemplo mostra que muitas vezes é melhor escolher o método mais simples, limitando assim o número de objetos criados, bem como os erros que podem surgir.

**Segundo método usando um plano de referência.**

Aqui está outro método mais rápido, possível desde a versão 0.17: o uso de um plano de referência e sua conexão.

Comece apagando o \"Pocket\", bem como o esboço do furo. Selecione a face superior e clique em <img alt="" src=images/PartDesign_Point.svg  style="width:24px;"> [Criar um ponto de partida](PartDesign_Point.md): crie um ponto de referência no corpo ativo. O modo de fixação escolhido deve ser \"Centro de massa\".

Selecione a face superior novamente e enquanto mantém pressionada a tecla CTRL, selecione o ponto que você acabou de criar na árvore Modelo, solte CTRL e clique em [24px](Arquivo:PartDesign_Plane.svg.md) [Criar um plano de referência](PartDesign_Plane.md). Um plano de referência é criado com a origem do ponto. Clique OK.

Agora é muito fácil centralizar o círculo! Selecione na árvore ou na visualizaçao 3D o plano que você criou e clique em <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Criar um esboço](Sketcher_NewSketch.md), um esboço (Sketch) é criado tendo, como origem, a origem do plano. Depois é só traçar o círculo de 5 mm de raio nessa origem, depois validar (o esboço deve estar obrigatoriamente verde).

Você obtém o furo com a \"Perfuração\", conforme criado anteriormente e ele sempre estará centralizado.

![](images/GGTuto1_9.PNG )

Este tutorial está concluído, salve este arquivo. Você pode se divertir explorando vários recursos. Mudar outras dimensões, fazer outras formas, colocar outros buracos em outras faces. É errando que a gente evolui!

Você também pode continuar com este outro tutorial de uma peça um pouco mais complicada:

[Tutorial de Projeto Básico de Peças](Basic_Part_Design_Tutorial/pt-br.md)


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Creating a simple part with PartDesign/pt-br
