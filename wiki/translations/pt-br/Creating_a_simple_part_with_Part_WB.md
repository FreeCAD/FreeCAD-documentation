---
- TutorialInfo:   Topic:Modeling
   Level:Beginner
   Author:heda
   Time:2 hours
   FCVersion:0.19 or above
   Files:
   SeeAlso:[Criando uma peça simples com a bancada Part Design](Creating_a_simple_part_with_PartDesign/pt-br.md), [Criando uma peça simples com as bancadas Draft e Part](Creating_a_simple_part_with_Draft_and_Part_WB/pt-br.md)
---

# Creating a simple part with Part WB/pt-br







## Introdução

Esse tutorial tem como propósito ser uma primeira introdução à modelagem 3D usando a [Bancada Part](Part_Workbench/pt-br.md) ![](images/Switch_PartWorkbench.JPG ) do FreeCAD. Ao finalizá-lo você vai conseguir produzir modelos 3D simples usando primitivas como cubos, cilindros, etc, com a técnica de modelagem chamada [Geometria Sólida Construtiva](https://pt.wikipedia.org/wiki/Geometria_s%C3%B3lida_construtiva) (ou Constructive Solid Geometry, CSG, em inglês). Uma outra maneira de criar modelos 3D é usando uma forma 2D, por exemplo, fazendo a extrusão dela ou revolução da forma 2D no espaço 3D. Para uma introdução nessa técnica, por favor acesse o tutorial irmão *[Criando uma peça simples com a bancada Part Design](Creating_a_simple_part_with_PartDesign/pt-br.md)*. Esses dois tutoriais tem, intencionalmente, o mesmo modelo gerado, para apresentar ao iniciante uma experiência com a mão na massa nas duas diferentes técnicas e como são implementadas no FreeCAD. A definição das duas técnicas pode ser vista como estritamente dividida do ponto de vista semântico, no entanto, não há nada impedindo diretamente uma mistura delas ao criar modelos. Há algumas ressalvas a serem observadas ao misturar técnicas de modelagem, principalmente relacionadas a aspectos de como o FreeCAD é programado. Há um [terceiro tutorial](Creating_a_simple_part_with_Draft_and_Part_WB/pt-br.md), feito como uma primeira introdução a um exemplo de modelagem mista. Esse tutorial utiliza a **Bancada Draft** para criar um perfil 2D utilizado para extrudar um sólido na **Bancada Part** para fazer o mesmo modelo deste tutorial.

Antes de começar, dê uma olhada em como **[navegar](Mouse_navigation/pt-br.md)** no espaço 3D. Ao passar o mouse sobre o seletor de modo do mouse no canto inferior direito da janela do FreeCAD, dicas do modo atual de operação do mouse aparecem como na imagem abaixo.

![](images/T101pwb00-01_navi.png )

Muitos novatos em programas CAD travam ao aprender o software. Se isso acontecer com você, por favor, procure mais informações na wiki ou no fórum -- é provável que outras pessoas também tenham travado no mesmo ponto, então já pode existir uma resposta para a sua pergunta. Ou faça um post no fórum com suas perguntas ou descobertas. O fórum possui vários tópicos onde os usuários obtém ajuda para concluir todo tipo de tarefa, esses tópicos muitas vezes são semelhantes a tutoriais e frequentemente incluem ilustrações.



### O que esse tutorial cobre 

-   O modelo a ser criado
-   Usando da Bancada Part para criar e manipular os modelos primitivos
-   Alterando cor e transparência
-   Um modo diferente de posicionar o buraco
-   Tornando o furo um furo escareado (ou rebaixado)
-   Fazendo uma peça oca
-   Uma maneira diferente de posicionar o chanfro
-   Editando dimensões
-   Organizando a árvore ligeiramente diferente
-   Finalizando



## O modelo a ser criado 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width:372px;">

![](images/T101pwb01-02_dims.png )



## Usando da Bancada Part para criar e manipular os modelos primitivos 

Crie um novo documento e salve-o lodo com um novo nome. É uma boa prática garantir que você salve o documento em intervalos regulares ou antes de operações maiores. Em seguida, mude para a **[Bancada Part](Part_Workbench/pt-br.md)** usando o [seletor de bancadas](Getting_started#Exploring_the_interface.md) (rotulado como 10 na imagem vinculada) ou indo para o menu **Vista → Bancada**. O FreeCAD iniciará com as barras de ferramentas na parte superior, a \'Tela combinada\' à esquerda e a vista 3D à direita.



### Crie o bloco sólido principal 

Pressione <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Cubo](Part_Box.md) para criar um cubo sólido padrão. O cubo aparece na [Visualização 3D](3D_view/pt-br.md) e também um novo objeto na [Visualização em árvore](Tree_view/pt-br.md) na barra lateral.

Pressione <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isométrico](Std_ViewIsometric.md) para ver o cubo em 3D.

![](images/T101pwb01-03_cube1.png )

Selecione o cubo na [Visualização em árvore](Tree_view/pt-br.md), ele fica verde na visualização 3D. Abaixo da visualização em árvore você verá agora que o cubo é criado por padrão com as dimensões **Length x Width x Height** (**Comprimento x Largura x Altura**) sendo *10 x 10 x 10mm*. Mude essas dimensões para **100 x 30 x 50**, como no desenho inicial do modelo.

![](images/T101pwb01-04_cubedims.png )

Ao alterar uma propriedade, como *Lenght* (Comprimento), através da caixa de seleção, você pode inserir os valores ou usar a roda de rolagem para aumentar ou diminuir os valores. As setas para aumentar ou diminuir os valores também podem ser usadas. Na figura mais à direita acima, a propriedade *Height* (Altura) está em modo de edição, rolando a roda de rolagem quando o mouse está sobre essa célula, o valor será alterado de um em um para cima ou para baixo.

Clique <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> **[Enquadrar tudo](Std_ViewFitAll.md)** para ver o cubo inteiro.

![](images/T101pwb01-05_cube2.png )



### Criando o arredondamento 

Para criar o canto arredondado, na barra de ferramentas, clique em <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> **[Filete](Part_Fillet/pt-br.md)** (ou \'Fillet\'), o que abre o *painel de tarefas* para arredondamentos na [Tela combinada](Combo_view/pt-br.md) na lateral. Mude a caixa de seleção do raio para 20 mm e, em seguida, na vista 3D, selecione a borda na lateral superior à direita e clique em **OK**.

![](images/T101pwb01-06_filletrad.png )

O *painel de tarefas* se fecha e você está de volta à visualização em árvore, que agora tem um objeto Fillet ao invés do Cubo anterior.



### Visibilidade de filhos 

Clique na seta para direita/sinal \"maior que\" para expandir os filhos do filete, que neste caso é o *cubo* que criamos anteriormente, mas está esmaecido. Selecione o cubo e pressione a barra de espaço - isso alterna a visibilidade para que o cubo fique visível novamente e o ícone não esteja mais esmaecido. Para desmarcar o cubo, clique em uma área em branco na visualização em árvore ou na visualização 3D.

![](images/T101pwb01-07_fillet.png )



### Crie o chanfro 

Em seguida, crie o *chanfro* de 30 graus, comece alternando a visibilidade do cubo filho do filete. Existe uma ferramenta de chanfro em [Bancada Part](Part_Workbench/pt-br.md), mas ao invés de usá-la faremos o chanfro com outro bloco e um corte booleano.

Crie um novo <img alt="" src=images/Part_Box.svg  style="width:24px;"> **[Cubo](Part_Box/pt-br.md)** com dimensões 60 x 30 x 30. Altere o **Ângulo** de colocação em **Placement** para -30 graus.

![](images/T101pwb01-08_chamfer1.png )

O ângulo de posicionamento está usando o **vetor de posicionamento** (Eixo) como eixo de rotação. O padrão é o eixo z, que não corresponde à nossa direção desejada. Alterando o vetor de posicionamento para o **eixo y** produz a orientação necessária da ferramenta de corte para o chanfro.

![](images/T101pwb01-09_chamfer2.png )

O mesmo posicionamento também pode ser obtido com outros valores, o exemplo alternativo mais simples de um posicionamento igual é um ângulo de +30 graus e um eixo y de -1.



#### Console python 

Em seguida, a posição precisa ser ajustada. Observando o desenho da peça acabada, não há dimensão direta a ser usada para a translação pretendida para cima. Como a dimensão para cima é a necessária, temos que calculá-la. Vamos usar a **[Console python](Python_console/pt-br.md)** embutida para esses cálculos, é trigonometria básica. Se a console Python do FreeCAD não estiver visível para você, basta clicar com o botão direito do mouse em um espaço vazio na área da barra de ferramentas e marcar a *Console Python* e ela deve aparecer na área de trabalho. Marque também a **[Tela de relatório](Report_view/pt-br.md)** se ainda não estiver visível. A *tela do relatório* na maioria das vezes fornece informações úteis ou até dicas sobre o que fazer a seguir para diferentes comandos.

![](images/T101pwb01-10_pyconsole.png )

Depois de importar o módulo **[math](https://docs.python.org/3/library/math.html#module-math)** das bibliotecas padrão no python, podemos usar a fórmula *(50 - math.tan(math.radians(30)) \* 50)* para encontrar a distância na direção z que o bloco deve ser movido. Copie o resultado da fórmula da console Python e cole-o na posição z de **Cube001**. A *ferramenta* a ser usada para o *corte* do chanfro agora está orientada e posicionada corretamente.

![](images/T101pwb01-11_chamfer3.png )



#### Expressões

Não é necessário usar a console Python para fazer o cálculo. Na maioria dos casos, ao lidar com valores paramétricos numéricos, o FreeCAD possui um atalho para uma calculadora embutida. Chama-se **[Expressões](Expressions/pt-br.md)** no FreeCAD, você pode entrar no *modo de expressão* clicando primeiro na caixa de seleção para a posição z, um pequeno ícone circular azulado aparecerá no lado direito.

![](images/T101pwb01-12_expression1.png )

Clicar nesse ícone abre a janela *Editor de fórmulas*, onde fórmulas e expressões podem ser inseridas conforme mostrado abaixo. Expressões são um recurso poderoso, pois é possível acessar os parâmetros do modelo. Todos os parâmetros do modelo ficam disponíveis como variáveis a serem usadas na criação de uma expressão. Resumindo, em nossa fórmula, ao invés de inserir o número 50 no editor de fórmulas, poderíamos inserir um *parâmetro referido* contendo o valor 50 do cubo, com a vantagem de que se mudarmos a *altura* do cubo \', a posição do chanfro seguirá automaticamente. O valor de 50 no modelo atual é referido como *Cube.Length*, ou seja, a propriedade *Length* do recurso *Cube*. Mais informações sobre isso podem ser encontradas no wiki.

![](images/T101pwb01-13_expression2.png )

Para fazer o corte, com a tecla **Ctrl** pressionada primeiro selecione o **Fillet** na visualização em Árvore e depois o último cubo criado (chamado **Cube001**) e finalmente na barra de ferramentas pressione o botão <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **[Recortar](Part_Cut/pt-br.md)** (Cut). Sua visualização em Árvore agora deve mostrar novamente um único objeto na raiz chamado **Cut**.

![](images/T101pwb01-14_model1.png )



#### As barras de ferramentas 

Uma observação sobre as barras de ferramentas, já que elas são o caminho típico para invocar comandos. Embora haja uma configuração básica para o layout das barras de ferramentas, o layout que aparece em seu computador pode não ser o ideal. Nesses casos é fácil ajustar. Considere a seção superior da imagem abaixo. Existem duas linhas de barras de ferramentas e apenas um número limitado de botões da barra de ferramentas [Bancada Part](Part_Workbench/pt-br.md) estão visíveis. A maneira mais simples de ver mais botões da barra de ferramentas é maximizar a janela do FreeCAD, a menos que ela já esteja maximizada, é claro.

O mais prático é ajustar o layout das barras de ferramentas para atender às suas necessidades e ao seu computador específico. O reposicionamento é feito com a alça à esquerda de cada barra de ferramentas. Você pode simplesmente clicar e arrastar a alça para um novo local. Na seção inferior da imagem abaixo, as posições da barra de ferramentas foram ajustadas, revelando seu conteúdo completo. As alterações nas posições da barra de ferramentas são permanentes mesmo após fechar e abrir o software.

![](images/T101pwb01-141_toolbars.png )



#### A ferramenta de medição 

A **[ferramenta de medição](Part_Workbench/pt-br#Measure.md)** na **Bancada Part** pode ser usada para verificar se nosso cálculo e posicionamento do chanfro estão corretos. Pressione o botão <img alt="" src=images/Part_Measure_Linear.svg  style="width:24px;"> **[Medida Linear](Part_Measure_Linear/pt-br.md)** e um *painel de tarefas* se abrirá, então selecione 2 pontos extremos de um lado do chanfro.

![](images/T101pwb01-15_model1measure1.png )

Podemos conferir a medida de x de 50 mm. Limpe a medição (Clear all dimensions) e feche o diálogo (Close).



### Criando o buraco 

Para fazer o furo, pressione o botão <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> **[Cilindro](Part_Cylinder/pt-br.md)**, defina o raio (*Radius*) com 5 mm e a altura (*Height*) com 50 mm.

![](images/T101pwb01-16_cyl1.png )

Em seguida, precisamos posicionar o furo de acordo com as dimensões do desenho. Altere a visualização para <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> **[Topo](Std_ViewTop.md)** e clique com o botão direito do mouse em **Cilindro** na visualização em árvore e selecione **Transformar** no menu pop-up.

![](images/T101pwb01-17_cyl1translate.png )

Altere *Incremento de translação* para 5 e use as setas vermelha e verde para posicionar o cilindro na posição correta, movendo-o 15 mm em y e 65 em x, arrastando as pontas das setas com o mouse. Clique em **OK** para fechar a caixa de diálogo *Transformar*. Para fazer o furo pressione a tecla **Ctrl** e selecione **Cut** e **Cilindro** na visualização em Árvore, então pressione a tecla <img alt=" link=Part_Cut" src=images/Part_Cut.svg  style="width:24px;"> **[Recortar](Part_Cut/pt-br.md)** na barra de ferramentas. Sua visualização em árvore deve ter novamente um único objeto na raiz chamado **Cut001**.

Parabéns, o modelo está pronto.

![](images/T101pwb01-18_model1complete.png )

Com o modelo básico pronto, vamos explorar diferentes formas de alterar este modelo, alguns exemplos ajustam a aparência, mostram funcionalidades adicionais, ou simplesmente uma forma diferente de fazer o mesmo.



## Mudando a cor e transparência 

Existem várias maneiras diferentes de alterar a aparência dos objetos. Vamos aqui usar a guia de exibição na parte de propriedades da exibição de combinação. Primeiro, selecione o objeto na visualização em árvore e, em seguida, edite qualquer propriedade como cor da linha, cor da forma ou transparência por meio da aba **Vista** (encontrada na parte inferior da *Tela combinada*).

![](images/T101pwb02-01_appearance1.png )

Infelizmente, quando o objeto é selecionado, é um pouco difícil ver como ele ficará ao ajustar a nova aparência. Para ver o resultado final é preciso desmarcar o objeto. Aqui está o novo visual do modelo, onde agora é possível ver o furo passante também na perspectiva isométrica. Outra forma de editar a aparência é através do menu **Vista → ![](images/)_Aparência...**.

![](images/T101pwb02-02_appearance2.png )



## Uma maneira diferente de posicionar o buraco 

Faça um *salvar como* com um novo nome. Em seguida, exclua o corte que adicionou o furo e mova o cilindro de volta para a posição zero. Seu modelo deve se parecer com a figura abaixo, que é o ponto de partida para usar uma técnica diferente para localizar o orifício no centro da face superior. Observe que a cor voltou ao cinza padrão, a alteração na aparência que fizemos foi no objeto recortado que agora foi excluído.

![](images/T101pwb03-01_cyl.png )

Desta vez, a <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> **[Bancada Draft](Draft_Workbench.md)** será usada para localizar o furo. O furo deve, como antes, estar localizado no centro da face superior, que é o mesmo que o ponto médio da diagonal da face superior.

Comece mudando a bancada para **Draft**. Pode ser que uma *grade* apareça na visualização 3D, a visibilidade da grade pode ser alternada com <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> [Ligar/desligar grade](Draft_ToggleGrid.md) na barra de ferramentas. Ao fazer uso da funcionalidade **[encaixe](Draft_Snap/pt-br.md)** (snap) na **Bancada Draft** é bom ter apenas os *tipos de encaixe* de interesse ativados. Desta vez é suficiente deixar *Snap Endpoint*, *Snap Midpoint* e *Snap Center* ativados, de modo que as configurações de encaixe devem ficar parecidas com as abaixo.

![](images/T101pwb03-02_snap.png )

Encontrar o ponto para colocar o centro do cilindro pode ser feito fazendo uma diagonal como linha de apoio e usar o centro do cilindro e o ponto médio da diagonal para identificar os pontos chave, porém nem precisamos fazer quaisquer linhas auxiliares, podemos encaixar na geometria sólida já existente.

Selecione o **Cilindro** na visualização em Árvore (ele fica verde na visualização 3D) e pressione o botão <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **[Mover](Draft_Move/pt-br.md)** na barra de ferramentas. Um *painel de tarefas* abre para objetos em movimento, certifique-se de que *Copiar* esteja desmarcado.

![](images/T101pwb03-03_move.png )

Em seguida, mova o mouse para a face superior do cilindro de modo que você veja um *ponto branco* no centro do círculo conforme a figura esquerda abaixo, isso junto com o símbolo do centro ao lado do ponteiro do mouse significa que um clique do botão esquerdo do mouse fará o mouse se encaixar com o ponto branco.

![](images/T101pwb03-04_snapselect.png )

Quando você tiver o ponto branco na face superior, clique com o botão esquerdo do mouse e repita para a face quadrada superior do sólido principal, como na imagem à direita acima, e confirme a escolha com um clique com o botão esquerdo do mouse. A função encaixar (snap) faz uso do *centro de massa* para qualquer tipo de face, e neste caso o centro de massa é o mesmo que o centro geométrico que se busca. Você já deve ter notado que o movimento do cilindro é animado, então você sempre vê o que está para acontecer.

Repetir a etapa do **corte booleano** anterior mais uma vez fará o furo passante que completa o modelo. Usando a ferramenta **medida linear** na bancada Part, pode se fazer uma verificação de que o furo está colocado corretamente. A medição só pode ser feita entre *pontos*, então a medição é feita do zero do corpo principal até o ponto de emenda do cilindro, ou seja, a distância correta é 70 mm ao invés de 65 que está no desenho, por conta do raio extra incluído na distância.

![](images/T101pwb03-05_modelmeasure.png )



## Fazendo do furo um furo escareado 

Volte para a [bancada Part](Part_Workbench/pt-br.md) e crie um *cone* pressionando <img alt="" src=images/Part_Cone.svg  style="width:24px;"> *\'[Cone](Part_Cone/pt-br.md)* \' na barra de ferramentas. Altere *radius1* para 0 mm e *radius2* para 7 mm -- isso resultará em um *rebaixamento* de 2 mm no raio no furo escareado. Tornar a *altura* do cone de 7 mm resulta em um ângulo superior com 90 graus do cone ou ângulo de rebaixamento de 45 graus. Vale a pena notar que pode-se alternativamente usar a operação <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Chanfro](Part_Chamfer/pt-br.md).

Ao trabalhar com o FreeCAD, você se deparará continuamente com várias maneiras diferentes de obter resultados semelhantes. Dificilmente existe uma verdade absoluta sobre qual é a maneira certa de alcançar um determinado resultado final - no entanto, ao olhar em um contexto específico, um fluxo de trabalho específico pode ser mais flexível, permitir que recursos posteriores sejam realmente usados, etc. Sua forma de construir modelos 3D vai evoluir ao longo do tempo à medida que você aprende mais e mais sobre os recursos e capacidades do FreeCAD.

![](images/T101pwb04-01_cone.png )

Reposicione o cone de modo que fique *concêntrico* com o furo e *coplanar* com a superfície superior sólida principal. Use qualquer método descrito anteriormente neste tutorial para fazer isso.

Na figura abaixo o movimento é feito com *Transformar* e uma configuração de *incremento* de 1 mm, já que o cone tem uma dimensão característica de 7 mm, o que significa que a configuração de incremento anterior de 5 mm não permitirá posicionamento correto. A renderização do tipo <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> **[Arame](Std_DrawStyle#Wireframe.md)** é usada para facilitar a visualização de que o cone está na posição correta.

![](images/T101pwb04-02_conetranslate.png )

Para completar o modelo, vamos usar o comando <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> **[Booleano](Part_Boolean/pt-br.md)** em vez de primeiro selecionar objetos e aplicar uma operação booleana específica. Pressione o botão da barra de ferramentas e uma aba de *tarefas* se abrirá conforme a imagem abaixo à esquerda.

![](images/T101pwb04-03_boolean.png )

Três itens precisam ser especificados, o *tipo de operação*, a *primeira forma* e a *segunda forma*. O cone deve ser cortado, isso é chamado *Diferença* neste comando, em vez de *Cortar*. A primeira forma é a nossa **Cut001**, ela está listada em *compostos*, pois é construída a partir de vários sólidos. A segunda forma é o **Cone**. Uma vez feitas as configurações corretas para o comando, clique no botão **Apply** (Aplicar) para executar a operação. Tudo isso foi feito na figura à direita, e também pode-se ver que um *composto* **Cut002** agora está listado, esta é a forma final do nosso modelo. Depois de mudar a aparência, o modelo final fica assim.

![](images/T101pwb04-04_modelcomplete.png )



## Fazendo uma peça oca 

Faça um *salvar como* com um novo nome. FreeCAD tem todas as operações típicas de um modelador 3D, uma delas é <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> **[Espessura](Part_Thickness/pt-br.md)**, que é usado para peças *escavadas* ou *ocas*.

Gire a visualização para que a face inferior do modelo fique visível.

![](images/T101pwb05-01_frombottom.png )

Selecione a *face inferior* do modelo, então na [Bancada Part](Part_Workbench/pt-br.md) selecione <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> *\'[Espessura](Part_Thickness/pt-br.md)\'* e a tela deve ficar como abaixo.

![](images/T101pwb05-02_thickness_cmd.png )

Clique em **OK**. Como você pode ver, agora há um *raio* na parte vazada

![](images/T101pwb05-03_thickness_dimension.png )

Além disso, ao fazer uma medição da largura da peça, ela agora é de 32 mm, então a *espessura* foi aplicada *para fora*. Vamos editar isso, clique duas vezes no modelo na visualização em árvore e modifique as configurações de *Tipo de junta* para *Intersecção* e a configuração de *Espessura* para -1.

![](images/T101pwb05-04_thickness_modify.png )

Agora a largura externa da peça é de 30 mm, como antes, e os cantos são todos cantos vivos.

![](images/T101pwb05-05_thickness_modified.png )



## Uma maneira diferente de posicionar o chanfro 

De um *Salvar como* com outro nome. Em seguida, exclua os itens para que o modelo fique como abaixo.

![](images/T101pwb06-01_startingpoint.png )

Faça um **Cubo** com dimensões **30x30x60**, terminando como abaixo.

![](images/T101pwb06-02_with_cube.png )

Altere o **posicionamento** (placement) girando primeiro -120 graus ao redor do eixo Y.

![](images/T101pwb06-03_rotated_cube.png )

Por fim, mude a posição para **X=50** e **Z=50** e faça o corte para produzir o mesmo resultado anterior.

![](images/T101pwb06-04_cube_cut.png )

Isso mais uma vez ressalta que sempre existem várias maneiras de produzir o mesmo resultado, o que é um fato recorrente quando se trata de modelagem 3D. Quando se trata de geometrias básicas ou sólidos, pode-se usar diferentes bancadas no FreeCAD, bem como diferentes comandos e ainda ter o mesmo sólido. Você simplesmente precisa encontrar seu próprio caminho, ferramentas e fluxo de trabalho preferidos com os quais se sinta confortável. A modelagem em 3D paramétrica é um processo de aprendizado constante e requer prática para dominar.



## Editando dimensões, cores de face e PNT 

O FreeCAD é um modelador 3D paramétrico, que permite alterar qualquer *posicionamento* ou *dimensão* e o modelo será atualizado de acordo. Em geral, isso funciona, mas é possível quebrar um modelo quando editado -- por exemplo, quando um filete é baseado em uma aresta que não existe mais devido à edição. Quando um modelo quebra durante a edição, isso é chamado de PNT, **[Problema de Nomenclatura Topológica](Topological_naming_problem/pt-br.md)** (ou TNP, do inglês Topological Naming Problem).

Vá em frente e experimente alterar dimensões e posicionamentos para ver se você pode quebrar o modelo, não se esqueça de recalcular o modelo após as alterações, se necessário. Isso pode ser feito com o botão <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Atualizar](Std_Refresh.md) na barra de ferramentas. Se o ícone estiver acinzentado, não é necessário atualizar o objeto.



### Reposicionando o cilindro 

Aqui está um exemplo do cilindro movido do centro para um lado do corpo principal usando *Transformar* no cilindro. Como pode ser visto na imagem, o cone ainda está na posição original, não sendo afetado pelo movimento do cilindro.

![](images/T101pwb07-01_cylindermoved.png )

Quando você move o cilindro e rompe a superfície externa, na versão 0.19 você está perdendo parte das configurações de cores do seu modelo. O FreeCAD reverte as configurações do usuário para cores de formas e transparência na visualização 3D para padrão, porém a forma **Cut002** ainda mostra as cores e transparência que tinha antes, como visto na figura abaixo.



### Acertando as cores 

![](images/T101pwb07-02_wrongcolor.png )

Aqui está uma maneira de recuperar. Primeiro mude a *transparência* (Transparency) um tique para cima ou para baixo e depois volte, isso traz de volta a transparência. Você pode fazer o mesmo truque em *cor da forma* (Shape color). Outra maneira de obter a cor de volta é clicar com o botão direito em **Cut002** na visualização em árvore e selecionar **Definir cores** no menu de contexto. No *painel de tarefas* que aparece, clique em **Definir como padrão**, e isso traz de volta a cor definida nas propriedades de exibição.

![](images/T101pwb07-03_set_colors.png )

O comando **Definir cores** permite selecionar faces individuais de uma forma e definir uma cor única nas faces selecionadas.



### Sólidos múltiplos 

Outro exemplo em que o cubo que está fazendo o chanfro foi transladado e girado.

![](images/T101pwb07-04_3solids.png )

Como pode ser visto ao reposicionar o chanfro desta forma, o resultado final são *3 sólidos disjuntos*. A [Bancada Part](Part_Workbench/pt-br.md) permite isso, a [Bancada Part Design](PartDesign_Workbench/pt-br.md) não, ou você obterá um *erro de múltiplos sólidos* ou simplesmente não renderizará todos os sólidos.



### PNT

Voltando ao modelo original concluído, vamos explorar como as faces são nomeadas.

Aqui a **[tela de seleção](Selection_view/pt-br.md)** foi ativada (menu Vista / Painéis / Tela de seleção), apenas para mostrar claramente o que está selecionado e o que não está. Também a coloração é ajustada para que a seleção seja mais fácil de ver.

![](images/T101pwb07-05_face2and9.png )

Selecionando uma face lateral e a face interna do cilindro vemos que elas são chamadas internamente de face *2* e *9*, onde a face *2* é a face lateral. A numeração das faces pode ser diferente para você.

Mover o cilindro para que a cavidade termine na face lateral e fazer a seleção das faces agora fornece um número diferente para a face cilíndrica.

![](images/T101pwb07-06_newfacenumbers.png )

A face 2 é o lado direito da face 2 original, o lado esquerdo da antiga face 2 é agora a face 8. A parte cilíndrica era a face 9, mas agora é a face 7. O FreeCAD reatribui a numeração e a ordem não é necessariamente preservada. A contagem total de faces no primeiro modelo é 10. Na versão com a face cilíndrica perfurando a face lateral, a contagem total de faces é 11. Então, obviamente, a numeração das faces tem que mudar quando a chamada *topologia* muda. Isso provavelmente parece um detalhe mínimo, mas acaba sendo muito importante no CAD 3D paramétrico. Imagine que você usou a face cilíndrica como referência para outro recurso, ela costumava ser chamada de face 9, mas agora é chamada de face 8. A referência à superfície cilíndrica pretendida é perdida. Como o FreeCAD, pelo menos nas versões atualmente lançadas, não rastreia a *face pretendida*, ele apenas rastreia a *face numerada*, o modelo quebra quando é feita referência a uma face que posteriormente é renumerada. Isso é chamado **PNT, [Problema de nomenclatura topológica](Topological_naming_problem/pt-br.md)**.

Sinta-se encorajado a aprender como evitar modelos quebrados devido ao PNT. Leituras adicionais podem ser feitas [em outro lugar no wiki](Topological_naming_problem/pt-br.md), que foca principalmente em um fluxo de trabalho *orientado por esboço*, mantendo, porém, o mecanismo subjacente. A renumeração descrita aqui para faces vale para todas as entidades geométricas, faces, arestas e vértices.



## Organizando a árvore um pouquinho diferente 

Faça um *salvar como* com um novo nome. Em seguida, exclua todos os cortes terminando com um modelo parecido com o abaixo.

![](images/T101pwb08-01_primitives.png )

Ao usar a bancada **Part** modelando sólidos complexos, a estrutura em árvore de um sólido pode se tornar difícil de decifrar. Até agora criamos uma primitiva/recurso e aplicamos uma operação booleana. Na bancada **Part**, é possível agrupar primitivas em uma operação booleana. No nosso caso, temos o cilindro, o cone e o cubo que são todos uma operação booleana de corte.

Em vez de fazer um corte para cada primitiva, podemos primeiro aplicar uma união booleana <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> **[União](Part_Fuse/pt-br.md)** nos sólidos primitivos destinados ao corte booleano, depois fazer o *corte* entre o **Fillet** e o **Fusion**.

Usando essa abordagem, a exibição em árvore acaba ficando como abaixo, que é apenas uma maneira diferente de construir o mesmo modelo. Compare isso com a exibição em árvore original, nenhuma é melhor que a outra, no entanto, ao criar modelos mais complexos, uma abordagem sobre a outra pode ter benefícios na facilidade de modificar/reorganizar o modelo, se necessário.

![](images/T101pwb08-02_fused.png )



## Finalizando

Tendo passado pelo tutorial, você agora está relativamente familiarizado com a interface de usuário do FreeCAD e aprendeu o básico sobre como usar a bancada **Part**. Agora você deve ser capaz de construir modelos simples ao seu gosto. A bancada **Part** é uma das bancadas que podem ser usadas para criar sólidos, a **Part Design** é outra. As diferentes bancadas têm diferentes capacidades e fluxos de trabalho. Aprender o FreeCAD por completo, especialmente considerando todos os complementos e macros, leva anos, então continue explorando novas e diferentes formas de fazer modelos -- faça diferentes tutoriais no wiki, o aprendizado nunca para ao trabalhar com o FreeCAD. Sugere-se que você aprenda *esboços* (sketches) e a bancada **Part Design** em seguida, se seu foco estiver na criação de sólidos. Se seu foco é modelar edifícios, seu próximo aprendizado deve ser nas bancadas **Draft** e **Arch**.

Por fim, o FreeCAD é feito por voluntários em seu tempo livre. Se você quiser que os recursos do FreeCAD fiquem ainda mais avançados, considere [contribuir](Help_FreeCAD/pt-br.md) para o FreeCAD, por exemplo, melhorando a documentação.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Creating a simple part with Part WB/pt-br
