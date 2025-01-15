# <img alt="ícone da bancada de trabalho PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/pt-br






## Introdução

A <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> **Bancada PartDesign** oferece ferramentas para modelar componentes sólidos. É principalmente voltada para a criação de componentes mecânicos que podem ser fabricados e montados em um produto finalizado. No entanto, os sólidos criados podem ser usados para outras finalidades, como [modelagem BIM](BIM_Workbench/pt-br.md), [análise por elementos finitos](FEM_Workbench/pt-br.md) ou [usinagem e impressão 3D](CAM_Workbench/pt-br.md).

A Bancada PartDesign usa uma abordagem que constrói os objetos passo a passo. Cada peça é representada por um contêiner chamado \"Corpo\" (Body), que organiza as operações realizadas e define um sistema de coordenadas local para a peça.

Dentro do Corpo, você cria \"recursos\" que dão forma ao objeto final. Esses recursos podem ser \*\*aditivos\*\* (adicionam material) ou \*\*subtrativos\*\* (removem material). Por exemplo: - A ferramenta [Pad](PartDesign_Pad/pt-br.md) pega um desenho 2D (esboço) e o transforma em um sólido 3D, como se \"esticasse\" o desenho. - A ferramenta [Pocket](PartDesign_Pocket/pt-br.md) faz o contrário, criando um buraco ao \"cavar\" o sólido usando um desenho 2D.

Cada etapa se acumula sobre a anterior, formando o objeto completo como um processo de \"camadas\". Além disso, você pode usar formas básicas prontas, como [Cilindros](PartDesign_AdditiveCylinder/pt-br.md) e [Esferas](PartDesign_AdditiveSphere/pt-br.md), ou até sólidos criados fora do Corpo, para complementar o modelo.

Consulte a página [Edição de recursos](Feature_editing/pt-br.md) para uma explicação mais detalhada desse processo. Em seguida, veja [Criando um componente simples com PartDesign](Creating_a_simple_part_with_PartDesign/pt-br.md) para começar a criar sólidos.

A <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Bancada Part](Part_Workbench/pt-br.md) é uma alternativa para criar formas usando uma abordagem chamada \*\*geometria sólida construtiva\*\* (CSG). Esse método permite combinar formas simples, como cubos e cilindros, para criar objetos mais complexos.

Se você quiser entender melhor as diferenças entre a Bancada Part e a Bancada PartDesign, confira a página [Part e PartDesign](Part_and_PartDesign/pt-br.md).

![](images/PartDesign_Workbench_Example.jpg )



## Ferramentas

As ferramentas da Bancada PartDesign, também chamadas de ferramentas de Projeto da Peça, estão todas reunidas no menu **Part Design** e na barra de ferramentas PartDesign. Esses recursos aparecem automaticamente assim que você carrega a Bancada PartDesign, facilitando o acesso às funções necessárias para modelagem.



### Ferramentas Auxiliares de Design de Peças 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Criar corpo](PartDesign_Body/pt-br.md): cria um objeto [Corpo](Body/pt-br.md) no documento ativo e o torna ativo.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create Sketch:

  -<img alt="" src=images/PartDesign_NewSketch.svg  style="width:32px;"> [Criar esboço](PartDesign_NewSketch/pt-br.md): cria um novo esboço em uma face ou plano selecionado. Se nenhuma face for selecionada ao executar esta ferramenta, o usuário será solicitado a selecionar um plano no painel de Tarefas. A interface então muda para a [Área de Trabalho do Esboço](Sketcher_Workbench/pt-br.md) no modo de edição de esboço.

  - <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Anexar esboço](Sketcher_MapSketch/pt-br.md): anexa um esboço à geometria selecionada do corpo ativo.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar esboço](Sketcher_EditSketch/pt-br.md): edita o esboço selecionado.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validar esboço](Sketcher_ValidateSketch/pt-br.md): verifica a tolerância de diferentes pontos e ajusta-os.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Verificar geometria](Part_CheckGeometry/pt-br.md): Verifica a geometria dos objetos selecionados em busca de erros.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Criar um vinculo de forma](PartDesign_ShapeBinder/pt-br.md): cria um vinculo de forma referenciando a geometria de um único objeto pai.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Criar um vinculo de forma de sub-objeto(s)](PartDesign_SubShapeBinder/pt-br.md): cria um vinculo de forma referenciando a geometria de um ou mais objetos pais.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Criar um clone](PartDesign_Clone/pt-br.md): cria um clone do objeto selecionado.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Criar um plano de referência:


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Criar um plano de referência](PartDesign_Plane/pt-br.md): cria um plano de referência no objeto ativo.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Criar uma linha de referência](PartDesign_Line/pt-br.md): cria uma linha de referência no objeto ativo.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Criar um ponto de referência](PartDesign_Point/pt-br.md): cria um ponto de referência no objeto ativo.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Criar um sistema de coordenadas local](PartDesign_CoordinateSystem/pt-br.md): cria um sistema de coordenadas local vinculado a uma geometria de referência no corpo ativo.


</div>


:   
    <small>(v1.1)</small> : these tools have been replaced by new [datum tools](Std_Base#Part_Datums.md).



### Ferramentas de Modelagem do Part Design 



#### Ferramentas de Adições 

Essas são ferramentas para criar características básicas ou adicionar material a um corpo existente.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pad](PartDesign_Pad/pt-br.md): extruda (ou empurra) uma peça sólida a partir de um esboço selecionado, ou seja, cria um volume sólido estendendo o contorno do esboço para uma terceira dimensão.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolução](PartDesign_Revolution/pt-br.md): cria uma peça sólida ao girar um esboço em torno de um eixo. O esboço deve formar um perfil fechado.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Loft aditivo](PartDesign_AdditiveLoft/pt-br.md): cria um sólido, fazendo uma transição entre dois ou mais esboços.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Aditivo de varredura](PartDesign_AdditivePipe/pt-br.md): cria um sólido ao varrer um ou mais esboços ao longo de um caminho aberto ou fechado.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Hélice aditiva](PartDesign_AdditiveHelix/pt-br.md): cria um sólido ao varrer um esboço ao longo de uma hélice.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create an additive primitive:

  -<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Cubo aditivo](PartDesign_AdditiveBox/pt-br.md): cria um cubo aditivo.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Cilindro aditivo](PartDesign_AdditiveCylinder/pt-br.md): cria um cilindro aditivo.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Esfera aditiva](PartDesign_AdditiveSphere/pt-br.md): cria uma esfera aditiva.

  -<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Cone aditivo](PartDesign_AdditiveCone/pt-br.md): cria um cone aditivo.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Elipsóide aditiva](PartDesign_AdditiveEllipsoid/pt-br.md): cria uma elipsóide aditiva.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Toro aditivo](PartDesign_AdditiveTorus/pt-br.md): cria um toro aditivo.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Prisma aditivo](PartDesign_AdditivePrism/pt-br.md): cria um prisma aditivo.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Cunha aditiva](PartDesign_AdditiveWedge/pt-br.md): cria uma cunha aditiva.



#### Ferramentas subtrativas 

Estas são ferramentas para subtrair material de um corpo existente.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Cavidade](PartDesign_Pocket/pt-br.md): cria uma cavidade a partir do esboço selecionado.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Perfuração](PartDesign_Hole/pt-br.md): cria uma função de perfuração a partir do esboço selecionado. O esboço deve conter um ou mais círculos.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Sulco](PartDesign_Groove/pt-br.md): cria uma ranhura ao girar um esboço em torno de um eixo.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Loft subtrativo](PartDesign_SubtractiveLoft/pt-br.md): cria um sólido, fazendo uma transição entre pelo menos dois esboços e depois o subtrai do corpo ativo.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Escaneamento subtrativo](PartDesign_SubtractivePipe/pt-br.md): cria uma forma sólida ao varrer um ou mais esboços ao longo de um caminho aberto ou fechado e o subtrai do corpo ativo.

<img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Hélice subtrativa](PartDesign_SubtractiveHelix/pt-br.md): cria uma forma sólida ao deslocar um esboço ao longo de uma hélice e subtrai essa forma do corpo ativo.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create a subtractive primitive:

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Cubo subtrativa](PartDesign_SubtractiveBox/pt-br.md): adiciona um cubo subtrativa ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Cilindro subtrativo](PartDesign_SubtractiveCylinder/pt-br.md): adiciona um cilindro subtrativo ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Esfera subtrativa](PartDesign_SubtractiveSphere/pt-br.md): adiciona uma esfera subtrativa ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Cone subtrativo](PartDesign_SubtractiveCone/pt-br.md): adiciona um cone subtrativo ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Elipsóide subtrativa](PartDesign_SubtractiveEllipsoid/pt-br.md): adiciona uma elipsóide subtrativa ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Toro subtrativo](PartDesign_SubtractiveTorus/pt-br.md): adiciona um toro subtrativo ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisma subtrativo](PartDesign_SubtractivePrism/pt-br.md): adiciona um prisma subtrativo ao corpo ativo.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Cunha subtrativa](PartDesign_SubtractiveWedge/pt-br.md): adiciona uma cunha subtrativa ao corpo ativo.



#### Booleano

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Operação booleana](PartDesign_Boolean/pt-br.md): importa um ou mais Corpos ou Clones PartDesign para o corpo ativo e aplica uma operação booleana.



### Ferramentas de Acabamento 

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolução](PartDesign_Revolution.md): cria uma peça sólida ao girar um esboço em torno de um eixo. O esboço deve formar um perfil fechado.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Filete](PartDesign_Fillet/pt-br.md): filetes (redondos) bordas do corpo ativo.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chanfro](PartDesign_Chamfer/pt-br.md): chanfraduras das bordas do corpo ativo.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Rascunho](PartDesign_Draft/pt-br.md): aplica um esboço angular a rostos selecionados do corpo ativo.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Espessura](PartDesign_Thickness.md): cria uma casca espessa a partir do corpo ativo e abre a face selecionada.



### Ferramentas de Transformação 

Estas são ferramentas para transformar características existentes.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Espelhado](PartDesign_Mirrored.md): espelha uma ou mais características.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Padrão Linear](PartDesign_LinearPattern.md): cria um padrão linear de uma ou mais características.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Padrão Polar](PartDesign_PolarPattern.md): cria um padrão de repetição circular de uma ou mais características ao redor de um ponto central.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Criar MultiTransformação](PartDesign_MultiTransform.md): cria um padrão combinando qualquer uma das transformações mencionadas acima, além da transformação [Escalonada](PartDesign_Scaled.md).
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [Escalonada](PartDesign_Scaled.md): escala uma ou mais características. Esta transformação não está disponível como uma ferramenta separada.

#### Extras

Algumas funcionalidades adicionais encontradas no menu Design da peça:

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Roda dentada](PartDesign_Sprocket/pt-br.md): cria o perfil de uma roda dentada, que pode ser extrudado (transformado em uma peça 3D com espessura). A roda dentada é um componente usado para transmitir movimento rotacional, geralmente em sistemas de corrente.

-   <img alt="" src=images/PartDesign_InvoluteGear.svg  style="width:32px;"> [Engrenagem involuta](PartDesign_InvoluteGear/pt-br.md): cria o perfil de uma engrenagem com formato involuto, que pode ser extrudado (transformado em um objeto 3D com espessura) para criar uma peça sólida. O formato involuto é um tipo de curvatura comumente usado em engrenagens, proporcionando um movimento de transmissão mais suave e eficiente.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Assistente de projeto do eixo](PartDesign_WizardShaft/pt-br.md): Gera um eixo a partir de uma tabela de valores e permite analisar forças e momentos. O eixo é feito com um esboço giratório que pode ser editado.



### Itens do menu de contexto 

-   [Suprimido](PartDesign_Suppressed/pt-br.md): caixa de seleção para desativar um recurso específico sem excluí-lo. <small>(v1.0)</small> 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Definir ponta](PartDesign_MoveTip/pt-br.md): redefine a ponta, que é o recurso exposto fora do Corpo.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Mover objeto para outro corpo](PartDesign_MoveFeature/pt-br.md): move o esboço, geometria de referência ou recurso selecionado para outro Corpo.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Mover objeto após outro objeto](PartDesign_MoveFeatureInTree/pt-br.md): permite reordenar a árvore do Corpo movendo o esboço, geometria de referência ou recurso selecionado para outra posição na lista de recursos. Isso ajuda a controlar a ordem de criação dos recursos no modelo, o que pode influenciar como as operações são aplicadas, já que a ordem dos recursos na árvore afeta o resultado final do modelo. Por exemplo, ao mover um esboço ou recurso para uma posição diferente, você pode alterar a sequência de operações, o que pode modificar a geometria do modelo.



#### Itens compartilhados com a Bancada Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Aparência](Std_SetAppearance/pt-br.md): determina a aparência de toda a peça (cor, transparência, etc.).

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Cor por face](Part_ColorPerFace/pt-br.md): Permite atribuir cores diferentes para as faces individuais dos objetos. Isso significa que, em vez de aplicar uma única cor a todo o objeto, você pode personalizar cada face do objeto com uma cor específica, o que pode ser útil para destacar ou diferenciar partes de um modelo 3D.



### Ferramentas Obsoletas 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrar](PartDesign_Migrate/pt-br.md): migra arquivos de versões do FreeCAD anteriores à 0.17 para a versão 0.17. Esta ferramenta não está disponível na <small>(v1.0)</small> .



### Preferências

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferências](PartDesign_Preferences/pt-br.md): preferências disponíveis para as ferramentas do PartDesign.
-   [Ajustes finos](Fine-tuning/pt-br.md): alguns parâmetros extras para ajustar o comportamento do PartDesign.



## Tutoriais

-   [Como usar o FreeCAD](http://help-freecad-jpg87.fr/), um site que descreve o fluxo de trabalho para o design mecânico.
-   [Criando uma peça simples com o PartDesign](Creating_a_simple_part_with_PartDesign/pt-br.md)
-   [Tutorial Básico de Design de Peças 019](Basic_Part_Design_Tutorial_019/pt-br.md)
-   [Tutorial PartDesign Suporte de Rolamento I](PartDesign_Bearingholder_Tutorial_I/pt-br.md) (precisa de atualização)
-   [Tutorial PartDesign Suporte de Rolamento II](PartDesign_Bearingholder_Tutorial_II/pt-br.md) (precisa de atualização)



## Exemplos

Para algumas ideias do que pode ser alcançado com as ferramentas do PartDesign, confira: [Exemplos do PartDesign](PartDesign_Examples/pt-br.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">





 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [PartDesign](Category_PartDesign.md) > PartDesign Workbench/pt-br
