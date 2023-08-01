# <img alt="Ícone da Sketcher workbench" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/pt-br






## Introdução

A bancada de trabalho <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [bancada de trabalho Sketcher](Sketcher_Workbench/pt-br.md) do FreeCAD é usada para criar Sketches 2D destinadas ao uso na <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [bancada de trabalho Arch](Arch_Workbench/pt-br.md), e outras bancadas de trabalho. Geralmente, um desenho 2D é considerado o ponto de partida para a maioria dos modelos CAD, pois um esboço 2D pode ser \"extrudado\" para criar uma forma 3D; outros esboços 2D podem ser usados para criar outros recursos como bolsos, saliências ou extrusões no topo das formas 3D previamente construídas. Junto com as operações booleanas definidas na <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [bancada de trabalho Part](Part_Workbench/pt-br.md), o Sketcher forma a base do método de [Geometria Sólida Construtiva](constructive_solid_geometry/pt-br.md)(constructive solid geometry - CSG) de construção de sólidos. Além disso, junto com as operações da <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md), o Sketcher também forma a base da metodologia de [edição de recursos](feature_editing/pt-br.md) de criação de sólidos .

A bancada do Sketcher apresenta restrições (\"constraints\"), permitindo que formas 2D sigam definições geométricas precisas em termos de comprimento, ângulos e relações (horizontalidade, verticalidade, perpendicularidade, etc.). Um solucionador de restrições calcula a extensão do efeito das restrições sobre a geometria 2D e permite a exploração interativa dos graus de liberdade do esboço.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*''Um esboço básico totalmente restrito''*



## Noções Básicas de Esboçagem por Restrições 

Para explicar como o Sketcher funciona, pode ser útil compará-lo com a forma \"tradicional\" de desenho.



#### Desenho Tradicional 

A forma tradicional de elaboração do CAD é herdada da antiga [prancheta de desenho](http://en.wikipedia.org/wiki/Drawing_board). As [vistas ortogonais (2D)](http://en.wikipedia.org/wiki/Multiview_orthographic_projection) são desenhadas manualmente e destinadas à produção de desenhos técnicos (também conhecidos como plantas). Os objetos são desenhados precisamente no tamanho ou dimensão/cota pretendidos. Se você deseja desenhar uma linha horizontal de 100 mm de comprimento começando em (0,0), ative a ferramenta de linha, clique na tela ou insira as coordenadas (0,0) para o primeiro ponto e, em seguida, dê um segundo clique ou insira as coordenadas do segundo ponto em (100,0). Você também pode traçar sua linha em uma posição qualquer e movê-la depois. Quando terminar de desenhar as geometrias, basta adicionar as cotas.



#### Esboçagem por Restrições 

O **Sketcher** afasta-se dessa lógica. Os objetos não precisam ser desenhados exatamente como se pretende, porque eles serão definidos posteriormente por restrições. Os objetos podem ser desenhados livremente e, desde que ainda não tenham restrições, podem ser modificados. Na verdade, eles estão \"flutuando\" e podem ser movidos, esticados, girados, redimensionados e assim por diante. Isso proporciona grande flexibilidade no processo de design.



#### O Que São Restrições? 

Em vez de cotas, restrições são usadas para limitar os graus de liberdade de um objeto. Por exemplo, uma linha sem restrições tem 4 graus de liberdade - (em inglês, Degrees Of Freedom - abreviado como \" DOF \"): ela pode ser movida horizontal e verticalmente, pode ser estendida/encurtada, e pode ser rotacionada.

Aplicar uma restrição horizontal ou vertical, ou uma restrição angular (em relação a outra linha ou a um dos eixos), limitará sua capacidade de rotação, deixando-a com 3 graus de liberdade. Travar um de seus pontos em relação à origem removerá outros 2 graus de liberdade, e a aplicação de uma restrição de tamanho (dimensão) removerá o último grau de liberdade. A linha é então considerada **totalmente restrita**.

Vários objetos podem ser restringidos entre si. Duas linhas podem ser unidas por meio de um de seus pontos com a restrição de ponto coincidente. Um ângulo pode ser definido entre elas, ou elas podem ser postas como perpendiculares. Uma linha pode ser tangente a um arco ou círculo e assim por diante. Um esboço complexo com vários objetos terá uma série de soluções diferentes e torná-lo **totalmente restrito** significa que apenas uma dessas soluções possíveis foi alcançada com base nas restrições aplicadas.

Existem dois tipos de restrições: geométricas e dimensionais. Eles são detalhados na seção [\'Ferramentas\'](#Ferramentas/pt-br.md) abaixo.



#### Para que o Sketcher não Serve 

O Sketcher não se destina à produção de plantas 2D. Depois que os esboços são usados para gerar um sólido, eles são automaticamente ocultados. As restrições são visíveis apenas no modo de edição de esboço.

Se você só precisa produzir visualizações 2D para impressão e não deseja criar modelos 3D, verifique a [Draft workbench](Draft_Workbench/pt-br.md). Ao contrário dos elementos do Sketcher, os objetos Draft não usam restrições; estes são formas simples definidas no momento da sua criação. Tanto o Draft quanto o Sketcher podem ser usados para desenho de geometria 2D e criação de sólidos 3D, embora suas preferências de uso sejam diferentes:

-   **Sketcher** é normalmente usado junto com as bancadas [Part](Part_Workbench/pt-br.md) e [PartDesign](PartDesign_Workbench/pt-br.md) para criar sólidos.
-   **Draft** é normalmente usado para desenhos planos simples sobre uma grade, como ao desenhar uma planta baixa arquitetônica; nessas situações, o Draft é usado principalmente em conjunto com a [bancada de trabalho Arch](Arch_Workbench/pt-br.md).

A ferramenta [Draft2Sketch](Draft_Draft2Sketch/pt-br.md) converte um objeto Draft em um objeto Sketch e vice-versa; muitas ferramentas que requerem um elemento 2D como entrada funcionam com qualquer desses objetos, já que uma conversão interna é feita automaticamente.



## Fluxo de Trabalho da Esboçagem 

Um esboço é sempre bidimensional (2D). Para criar um sólido, um esboço 2D de uma única área fechada é criado e, a seguir, preenchido ou revolvido para adicionar a 3ª dimensão, criando um sólido 3D a partir do esboço 2D.

Se um esboço tem segmentos que se cruzam, lugares onde um ponto não está diretamente em um segmento, ou lugares onde há lacunas entre as extremidades de segmentos adjacentes, as ferramentas Pad ou Revolution não criarão um sólido. Às vezes, um esboço que contém linhas que se cruzam funcionará para uma operação simples, como Pad, mas operações posteriores como Linear Pattern falharão. É melhor evitar cruzar linhas. A exceção a esta regra é que ela não se aplica à geometria de construção (azul).

Dentro da área fechada, podemos ter áreas menores não sobrepostas. Eles se tornarão vazios quando o sólido 3D for criado.

Depois que um esboço está totalmente restrito, seu contorno ficará verde; a geometria de construção permanecerá azul. Neste ponto, ele é considerado \"acabado\" e adequado para uso na criação de um sólido 3D. No entanto, uma vez que a caixa de diálogo do esboço é fechada, pode valer a pena acessar a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [bancada de trabalho Part](Part_Workbench/pt-br.md) e executar o botão **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Verificar geometria](Part_CheckGeometry/pt-br.md)** para garantir que não haja partes no esboço que possam causar problemas posteriores.



## Ferramentas

As ferramentas do Sketcher Workbench estão localizadas no menu Sketch e/ou em várias barras de ferramentas. {{Version/pt-br|0.21}}: Quase todas as barras de ferramentas do Sketcher são exibidas apenas enquanto um esboço está no modo de edição. A única exceção é o [Barra de ferramentas do Sketcher](#Barra_de_ferramentas_do_Sketcher.md) que só é exibida se nenhum esboço estiver no modo de edição.


{{Version/pt-br|0.21}}

: Se um esboço estiver no modo de edição, a barra de ferramentas Estrutura ficará oculta, pois nenhuma de suas ferramentas poderá ser usada.



### Gerais



#### Barra de ferramentas do Sketcher 

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Criar um novo esboço](Sketcher_NewSketch/pt-br.md): Cria um novo esboço em uma face ou plano selecionado. Se nenhuma face estiver selecionada enquanto esta ferramenta é executada, o usuário é solicitado a selecionar um plano em uma janela pop-up.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar o esboço selecionado](Sketcher_EditSketch/pt-br.md): Abre a edição do esboço selecionado. Isso abrirá a [caixa de diálogo do Sketcher](Sketcher_Dialog/pt-br.md).

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Mapear um esboço para uma face](Sketcher_MapSketch/pt-br.md): Mapeia um esboço para a face previamente selecionada de um sólido.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Reorientação](Sketcher_ReorientSketch/pt-br.md): Permite anexar o esboço a um dos planos principais.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validar](Sketcher_ValidateSketch/pt-br.md): Verifica a tolerância de diferentes pontos e as ajusta.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Fundir](Sketcher_MergeSketches/pt-br.md): Mescla dois ou mais esboços.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Espelhar](Sketcher_MirrorSketch/pt-br.md): Espelha um esboço em relação ao eixo x, ao eixo y ou à origem.



#### Barra de ferramentas do Sketcher Modo de Edição 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Fechar a edição do esboço](Sketcher_LeaveSketch/pt-br.md): Sai do modo de edição do esboço.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Olhar perpendicularmente ao plano do esboço](Sketcher_ViewSketch/pt-br.md): Configura a vista do modelo como perpendicular ao plano do esboço.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Alternar entre a seção e a exibição completa](Sketcher_ViewSection/pt-br.md): Cria um plano de seção que oculta temporariamente qualquer coisa na frente do plano do esboço.



#### Barra de ferramentas de edição do Sketcher 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 



#### Outros

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Parar a operação](Sketcher_StopOperation/pt-br.md): Quando no modo de edição, para a operação atual, seja desenho, configuração de restrições, etc.



### Geometrias do Sketcher 

Estas são ferramentas para criar objetos.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Criar um ponto no esboço](Sketcher_CreatePoint/pt-br.md): Desenha um ponto.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Criar uma linha no esboço](Sketcher_CreateLine/pt-br.md): Desenha um segmento de reta entre 2 pontos. As linhas são infinitas em relação a certas restrições.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Criar um arco na bancada de esboços](Sketcher_CompCreateArc/pt-br.md): Este é um menu de ícones na barra de ferramentas do Sketcher, contendo os seguintes comandos:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Pontos de centro e extremidades](Sketcher_CreateArc/pt-br.md): Desenha um segmento de arco a partir do centro, raio, ângulo inicial e ângulo final.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Pontos de extremidade e ponto de borda](Sketcher_Create3PointArc/pt-br.md): Desenha um segmento de arco a partir dos dois pontos finais e outro ponto na circunferência.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Criar um círculo no esboço](Sketcher_CompCreateCircle/pt-br.md): Este é um menu de ícones na barra de ferramentas do Sketcher, contendo os seguintes comandos:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Ponto de centro e borda](Sketcher_CreateCircle/pt-br.md): Desenha um círculo a partir do centro e do raio.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [3 pontos de borda](Sketcher_Create3PointCircle/pt-br.md): Desenha um círculo a partir de três pontos na circunferência.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:48px;"> [Criar uma cônica no esboço](Sketcher_CompCreateConic/pt-br.md): O Sketcher fornece as seguintes seções cônicas que, ao contrário das B-splines, podem ser usadas com todos os tipos de restrições, como [Tangente](Sketcher_ConstrainTangent/pt-br.md), [Ponto sobre o objeto](Sketcher_ConstrainPointOnObject/pt-br.md), ou [Perpendicular](Sketcher_ConstrainPerpendicular/pt-br.md)..

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Elipse centro](Sketcher_CreateEllipseByCenter/pt-br.md): Desenha uma elipse pelo ponto central, ponto do raio maior e ponto do raio menor.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Elipse 3 pontos](Sketcher_CreateEllipseBy3Points/pt-br.md): Desenha uma elipse pelo diâmetro maior (2 pontos) e ponto do raio menor.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arco de elipse](Sketcher_CreateArcOfEllipse/pt-br.md): Desenha um arco de elipse pelo ponto central, ponto do raio maior, ponto inicial e ponto final.

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arco de hipérbole](Sketcher_CreateArcOfHyperbola/pt-br.md): Desenha um arco de hipérbole.

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arco de parábola](Sketcher_CreateArcOfParabola/pt-br.md): Desenha um arco de parábola.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [Criar uma B-spline](Sketcher_CompCreateBSpline/pt-br.md): Este é um menu de ícones na barra de ferramentas do Sketcher, contendo os seguintes comandos:

\*: <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Criar B-spline](Sketcher_CreateBSpline/pt-br.md): Desenha uma curva B-spline por seus pontos de controle.

\*: <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Criar B-spline periódica](Sketcher_CreatePeriodicBSpline/pt-br.md): Desenha uma curva B-spline periódica (fechada) por seus pontos de controle.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Draws a B-spline curve by its knots. <small>(v0.21)</small> 

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Draws a periodic (closed) B-spline curve by its knots. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilinha (linha de múltiplos pontos)](Sketcher_CreatePolyline/pt-br.md): Desenha uma linha composta de vários segmentos de linha. Pressionar a tecla M enquanto se desenha uma polilinha alterna entre os diferentes modos de polilinha.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Criar retângulos](Sketcher_CompCreateRectangles/pt-br.md): Este é um menu de ícones na barra de ferramentas Sketcher que contém os seguintes comandos: <small>(v0.20)</small> 


</div>

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectângulo](Sketcher_CreateRectangle/pt-br.md): Desenha um retângulo a partir de dois vértices opostos.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rectângulo Centrado](Sketcher_CreateRectangle_Center/pt-br.md): Desenha um retângulo a partir de um ponto central e de um ponto de borda. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rectângulo Arredondado](Sketcher_CreateOblong/pt-br.md): Traça um retângulo arredondado a partir de 2 pontos opostos. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Criar polígonos regulares](Sketcher_CompCreateRegularPolygon/pt-br.md): Este é um menu de ícones na barra de ferramentas do Sketcher, contendo os seguintes comandos:


</div>

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangulo](Sketcher_CreateTriangle/pt-br.md): Desenha um triângulo regular inscrito em um círculo de geometria de construção.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Quadrado](Sketcher_CreateSquare/pt-br.md): Desenha um quadrado regular inscrito em um círculo de geometria de construção.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentágono](Sketcher_CreatePentagon/pt-br.md): Desenha um pentágono regular inscrito em um círculo de geometria de construção.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexágono](Sketcher_CreateHexagon/pt-br.md): Desenha um hexágono regular inscrito em um círculo de geometria de construção.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptágono](Sketcher_CreateHeptagon/pt-br.md): Desenha um heptágono regular inscrito em um círculo de geometria de construção.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octágono](Sketcher_CreateOctagon/pt-br.md): Desenha um octógono regular inscrito em um círculo de geometria de construção.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Criar Polígono Regular](Sketcher_CreateRegularPolygon/pt-br.md) : Desenha um polígono regular selecionando o número de lados e escolhendo dois pontos: o centro e um canto.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Oblongo](Sketcher_CreateSlot/pt-br.md): Desenha uma forma oval selecionando o centro de um semicírculo e a extremidade do outro semicírculo.

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width:48px;"> [Create fillet](Sketcher_CompCreateFillets.md): This is an icon menu in the Sketcher toolbar that holds the following commands:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Filete](Sketcher_CreateFillet/pt-br.md): Faz um filete entre duas linhas unidas em um ponto. Selecione as duas linhas ou clique no ponto de canto e ative a ferramenta.


</div>

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their (virtual) intersection.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Ajustar](Sketcher_Trimming/pt-br.md): Corta uma linha, círculo ou arco em relação ao ponto clicado.


</div>

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Ampliar](Sketcher_Extend/pt-br.md): Estende uma linha ou um arco a uma linha limite, arco, elipse, arco de elipse ou um ponto no espaço.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Dividir](Sketcher_Split/pt-br.md): Divide uma linha ou um arco em dois, converte um círculo em um arco, mantendo a maior parte das restrições. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometria externa](Sketcher_External/pt-br.md): Cria uma aresta vinculada à geometria externa.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Cópia em carbono](Sketcher_CarbonCopy/pt-br.md): Copia a geometria de outro esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Modo de construção](Sketcher_ToggleConstruction/pt-br.md): Alterna a geometria do esboço de/para o modo de construção. A geometria de construção é mostrada em azul e é descartada fora do modo de edição do esboço.


</div>



### Restrições do Sketcher 

As restrições são usadas para definir comprimentos, definir regras entre os elementos do esboço e para bloquear o esboço ao longo dos eixos vertical e horizontal. Algumas restrições requerem o uso de [Restrições de ajuda](Sketcher_helper_constraint/pt-br.md).



#### Restrições Geométricas 

Tais restrições não estão associadas a dados numéricos.

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/pt-br.md): Afixa um ponto em (coincidente com) um ou mais outros pontos. Atua como uma restrição concêntrica se dois ou mais círculos, arcos, elipses ou arcos de elipses forem selecionados.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Ponto sobre o objeto](Sketcher_ConstrainPointOnObject/pt-br.md): Afixa um ponto em outro objeto, como uma linha, arco ou eixo.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical/pt-br.md): Restringe as linhas selecionadas ou elementos de polilinha a uma orientação vertical verdadeira. Mais de um objeto pode ser selecionado antes de aplicar esta restrição.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/pt-br.md): Restringe as linhas selecionadas ou elementos de polilinha a uma orientação horizontal verdadeira. Mais de um objeto pode ser selecionado antes de aplicar esta restrição.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Paralela](Sketcher_ConstrainParallel/pt-br.md): Restringe duas ou mais linhas, fazendo-as paralelas entre si.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular/pt-br.md): Restringe duas linhas, fazendo-as perpendiculares uma à outra, ou restringe uma linha perpendicular à extremidade de um arco.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/pt-br.md): Cria uma restrição tangente entre duas entidades selecionadas ou uma restrição colinear entre dois segmentos de linha. Um segmento de linha não precisa estar diretamente sobre um arco ou círculo para ser restrito tangente a esse arco ou círculo.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Iguadade](Sketcher_ConstrainEqual/pt-br.md): Restringe duas entidades selecionadas, fazendo-as iguais uma à outra. Se usado em círculos ou arcos, seus raios resultarão iguais.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Simetria](Sketcher_ConstrainSymmetric/pt-br.md): Restringe dois pontos simetricamente em relação a uma linha, ou restringe os dois primeiros pontos selecionados simetricamente em relação a um terceiro ponto selecionado.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Bloquear](Sketcher_ConstrainBlock/pt-br.md): Impede que uma aresta se mova, ou seja, impede que seus vértices mudem suas posições atuais. Deve ser particularmente útil para corrigir a posição de B-Splines. Veja o tópico [Block Constraint](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572) no fórum.



#### Restrições Dimensionais 

Estas são restrições associadas a dados numéricos, para os quais você pode usar [expressões](Expressions/pt-br.md). Os dados podem ser retirados de uma [planilha](Spreadsheet_Workbench/pt-br.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Restringir](Sketcher_ConstrainLock/pt-br.md): Restringe o item selecionado definindo distâncias verticais e horizontais em relação à origem, travando assim a localização desse item. Essas distâncias podem ser editadas posteriormente.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distancia Horizontal](Sketcher_ConstrainDistanceX/pt-br.md): Fixa a distância horizontal entre dois pontos quaisquer, ou pontos extremos de uma linha. Se apenas um item for selecionado, a distância é definida para a origem.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Distancia Vertical](Sketcher_ConstrainDistanceY/pt-br.md): Fixa a distância vertical entre dois pontos quaisquer, ou pontos extremos de uma linha. Se apenas um item for selecionado, a distância é definida para a origem.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distancia](Sketcher_ConstrainDistance/pt-br.md): Define o comprimento de uma linha, a distância perpendicular entre um ponto e uma linha, a distância entre dois pontos, ou, <small>(v0.21)</small> , a distância entre as arestas de dois círculos.

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width:48px;"> [Constrain radius or diameter](Sketcher_CompConstrainRadDia.md): This is an icon menu in the Sketcher constraints toolbar that holds the following commands:

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Raio ou peso](Sketcher_ConstrainRadius/pt-br.md): Define o raio de um arco ou círculo ou o peso de um pólo B-spline.

-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diâmetro](Sketcher_ConstrainDiameter/pt-br.md): Define o diâmetro de um arco ou círculo.

-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Radiano](Sketcher_ConstrainRadiam/pt-br.md): Define o raio de um arco, o diâmetro de um círculo ou o peso de um pólo B-spline.<small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angulo](Sketcher_ConstrainAngle/pt-br.md): Define o ângulo interno entre duas linhas selecionadas.



#### Restrições Especiais 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [A Lei de Snell](Sketcher_ConstrainSnellsLaw/pt-br.md): Restringe duas linhas à obediência a uma lei de refração, para simular a luz que passa por uma interface.


</div>

#### Constraint tools 


<div class="mw-translate-fuzzy">

#### Ferramentas de Restrição 

As seguintes ferramentas podem ser usadas para modificar o efeito das restrições:


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Alternar restrição de direção/referência](Sketcher_ToggleDrivingConstraint/pt-br.md): Alterna a barra de ferramentas ou as restrições selecionadas de/para o modo de referência.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Ativar/Desativar restrição](Sketcher_ToggleActiveConstraint/pt-br.md): Habilita ou desabilita uma restrição já colocada. <small>(v0.19)</small> 


</div>



### Ferramentas do Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [ Exibindo os graus de liberdade](Sketcher_SelectElementsWithDoFs/pt-br.md): Destaca em verde a geometria com graus de liberdade (GDLs), isto é, não toalmente restrita.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Selecione Restrições](Sketcher_SelectConstraints/pt-br.md): Seleciona as restrições de um elemento do Sketcher.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Selecione Elementos Associados a Restrições](Sketcher_SelectElementsAssociatedWithConstraints/pt-br.md): Seleciona elementos do Sketcher associados com restrições.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Selecione Restrições Redundantes](Sketcher_SelectRedundantConstraints/pt-br.md): Seleciona restrições redundantes de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Selecione Restrições Conflitantes](Sketcher_SelectConflictingConstraints/pt-br.md): Seleciona restrições conflitantes de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Mostrar/ocultar geometria interna](Sketcher_RestoreInternalAlignmentGeometry/pt-br.md): Recria o que falta ou deleta geometria interna desnecessária em uma elipse, arco de elipse, hipérbole, parábola ou B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Selecionar Origem](Sketcher_SelectOrigin/pt-br.md): Seleciona a origem de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Selecionar Eixo Horizontal](Sketcher_SelectHorizontalAxis/pt-br.md): Seleciona o eixo horizontal de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Selecionar Eixo Vertical](Sketcher_SelectVerticalAxis/pt-br.md): Seleciona o eixo vertical de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Simetria](Sketcher_Symmetry/pt-br.md): Copia um elemento do sketcher simétrico a uma linha escolhida.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clonar](Sketcher_Clone/pt-br.md): Clona um elemento do Sketcher.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copiar](Sketcher_Copy/pt-br.md): Copia um elemento do Sketcher.


</div>

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Mover](Sketcher_Move/pt-br.md): Move a geometria selecionada tomando como referência o último ponto selecionado.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Matriz Retangular](Sketcher_RectangularArray/pt-br.md): Cria uma matriz de elementos do Sketcher selecionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Retirar o alinhamento dos eixos](Sketcher_RemoveAxesAlignment/pt-br.md): Remover o alinhamento dos eixos enquanto tenta preservar a relação de restrição da seleção <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Eliminar toda a geometria](Sketcher_DeleteAllGeometry/pt-br.md): Deleta todas as geometrias do esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Eliminar todas as restrições](Sketcher_DeleteAllConstraints/pt-br.md): Deleta todas as restrições do esboço.


</div>



### Ferramentas de B-spline do Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Mostra/esconde o grau da B-spline](Sketcher_BSplineDegree/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Mostra/esconde o polígono de controle da B-spline](Sketcher_BSplinePolygon/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Mostra/esconde o pente de curvatura da B-spline](Sketcher_BSplineComb/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Mostra/esconde o nó de multiplicidade da B-spline](Sketcher_BSplineKnotMultiplicity/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Mostra/esconde o peso dos pontos de controle da B-spline](Sketcher_BSplinePoleWeight/pt-br.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Converte geometria para B-spline](Sketcher_BSplineApproximate/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Aumenta o grau da B-spline](Sketcher_BSplineIncreaseDegree/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Diminui o grau da B-spline](Sketcher_BSplineDecreaseDegree/pt-br.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Aumenta a multiplicidade do nó](Sketcher_BSplineIncreaseKnotMultiplicity/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Diminui a multiplicidade do nó](Sketcher_BSplineDecreaseKnotMultiplicity/pt-br.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into an existing B-spline. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Joins two curves at selected end points. <small>(v0.21)</small> 



### Espaço Virtual do Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Trocar espaço virtual](Sketcher_SwitchVirtualSpace/pt-br.md): Permite esconder todas as restrições de um esboço e fazê-las visíveis novamente.


</div>



### Ferramentas obsoletas 

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Forma fechada](Sketcher_CloseShape/pt-br.md): Cria uma forma fechada aplicando restrições coincidentes a exremidades. Não disponível em <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Conectar bordas](Sketcher_ConnectLines/pt-br.md): Conecta elementos do Sketcher aplicando restrições de coincidência nas extremidades. Não disponível em <small>(v0.21)</small> .



## Preferências

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferências](Sketcher_Preferences/pt-br.md): Preferências para a bancada de trabalho **Sketcher**.



## Boas Práticas 

Cada usuário CAD desenvolve sua própria maneira de trabalhar ao longo do tempo, mas existem alguns princípios gerais úteis a seguir.


<div class="mw-translate-fuzzy">

-   Uma série de esboços simples é mais fácil de gerenciar do que um único e complexo. Por exemplo, um primeiro esboço pode ser criado para o recurso 3D base (um "pad" ou um "revolve"), enquanto um segundo pode conter furos ou recortes ("pockets"). Alguns detalhes podem ser omitidos, para serem adicionados posteriormente como elementos 3D. Você pode escolher evitar filetes em seu esboço se houver muitos e adicioná-los como um elemento 3D.
-   Sempre crie um perfil fechado, ou seu esboço não produzirá um sólido, mas sim um conjunto de faces abertas. Se você não quiser que alguns dos objetos sejam incluídos na criação do sólido, transforme-os em elementos de construção com a ferramenta Construction Mode.
-   Use o recurso de restrições automáticas para limitar o número de restrições que você terá que adicionar manualmente.
-   Como regra geral, aplique primeiro as restrições geométricas, depois as restrições dimensionais e bloqueie o esboço por último. Mas lembre-se: as regras são feitas para serem quebradas. Se você estiver tendo problemas para manipular seu esboço, pode ser útil restringir alguns objetos antes de completar seu perfil.
-   Se possível, centralize seu esboço na origem (0,0) com a restrição de bloqueio (\"Lock\"). Se o seu esboço não for simétrico, localize um de seus pontos na origem ou escolha bons números redondos para as distâncias de bloqueio -- Uma restrição de bloqueio de (25,75) da origem é mais facilmente lembrada do que (23,47 , 73,02). Na v0.12, as restrições externas (restringindo o esboço à geometria 3D existente, como arestas ou outros esboços) não estão implementadas. Isso significa que, para localizar a geometria de esboços subsequentes em seu primeiro esboço, você precisará definir manualmente as distâncias relativas ao primeiro esboço.
-   Se você tiver a possibilidade de escolher entre a restrição Length e as restrições de distância Horizontal Distance ou Vertical Distance, prefira as últimas. Elas consomem menos recursos computacionais.
-   Em geral, as melhores restrições a serem usadas são: Restrições horizontais e verticais; restrições de comprimento horizontal e vertical; tangência ponto a ponto. Se possível, limite o uso destes: a restrição geral de comprimento; tangência borda a borda; restrição de fixar o ponto em uma linha; restrição de simetria.
-   Se estiver em dúvida sobre a validade de um esboço depois de concluído (os elementos ficam verdes), feche a caixa de diálogo do Sketcher, mude para a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Bancada de trabalho Part](Part_Workbench/pt-br.md) e execute **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Verificar geometria](Part_CheckGeometry/pt-br.md)**.


</div>



## Tutoriais


<div class="mw-translate-fuzzy">

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) por chrisb. Este é um documento PDF de 70 páginas que serve como um manual detalhado para o desenhista. Ele explica os fundamentos do uso do Sketcher e dá muitos detalhes sobre a criação de formas geométricas e cada uma das restrições.
-   [Tutorial Básico de Sketcher](Basic_Sketcher_Tutorial/pt-br.md) para iniciantes.
-   [Sketcher Micro Tutorial - Práticas de Restrição](Sketcher_Micro_Tutorial_-_Constraint_Practices/pt-br.md).
-   [Requisitos de esboço para um esboço](Sketcher_requirement_for_a_sketch/pt-br.md) Requisito Mínimo para um Esboço e Determinação Completa de um Esboço.


</div>

## Scripting

A página [Sketcher scripting](Sketcher_scripting/pt-br.md) contém exemplos de como criar restrições a partir de scripts Python.



## Exemplos

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/pt-br
