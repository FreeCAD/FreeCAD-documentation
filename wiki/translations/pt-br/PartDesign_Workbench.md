# PartDesign Workbench/pt-br
 

<img alt="ícone da bancada de trabalho PartDesign" src=images/Workbench_PartDesign.svg  style="width:128px;">


{{TOCright}}

## Introdução


<div class="mw-translate-fuzzy">

A <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md) fornece ferramentas avançadas para modelagem de peças sólidas complexas. O seu foco principal é a criação de peças mecânicas que podem ser fabricadas e montadas em um produto acabado. Entretanto, os sólidos criados podem ser usados em geral para qualquer outra finalidade, como [projeto arquitetônico](Arch_Workbench/pt-br.md), [análise de elementos finitos](FEM_Workbench/pt-br.md), ou [usinagem e impressão 3D](Path_Workbench/pt-br.md).


</div>

A bancada de trabalho PartDesign está intrinsecamente relacionada ao [bancada de trabalho Sketcher](Sketcher_Workbench.md). O usuário normalmente cria um Sketch(Esboço), depois utiliza a ferramenta [Protrusão](PartDesign_Pad.md) para extrudá-lo e criar um sólido básico, e então este sólido é modificado posteriormente.


<div class="mw-translate-fuzzy">

Enquanto a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Bancada de trabalho Part](Part_Workbench/pt-br.md) é baseado em uma [geometria construtiva sólida](constructive_solid_geometry/pt-br.md)(CSG) para construir formas, a Bancada de trabalho PartDesign utiliza uma metodologia paramétrica de edição de características, o que significa que um sólido básico é transformado sequencialmente pela adição de características no topo até que a forma final seja obtida. Veja a página [edição de recursos](feature_editing/pt-br.md) para uma explicação mais completa deste processo, e depois veja [Criando uma peça simples com PartDesign](Creating_a_simple_part_with_PartDesign/pt-br.md) para começar a criar sólidos.


</div>

Uma discussão mais detalhada da bancada de trabalho Part workbench comparada à bancada de trabalho Part Design pode ser encontrada aqui: [Part e Part Design](Part_and_PartDesign/pt-br.md).

Os corpos criados com PartDesign estão freqüentemente sujeitos ao [problema de nomenclatura topológica](Topological_naming_problem/pt-br.md) que faz com que as características internas sejam renomeadas quando as operações paramétricas são modificadas. Este problema pode ser minimizado seguindo as melhores práticas descritas na página [edição de recursos](feature_editing/pt-br.md), e aproveitando os objetos de dados como suporte para esboços e recursos.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Ferramentas

As ferramentas de Projeto da Peça estão todas localizadas no menu **Part Design** e na barra de ferramentas PartDesign que aparece quando você carrega a bancada de trabalho Part Design.

### Ferramentas de estrutura 

Essas ferramentas, de fato, não fazem parte da bancada de trabalho PartDesign. Elas pertencem à [Base Padrão](Std_Base/pt-br.md) do sistema. Elas foram desenvolvidas na v0.17 com a intenção de serem úteis para organizar um modelo, e criar [montagens](Assembly/pt-br.md); como tal, elas são muito úteis quando se trabalha com corpos criados com esta bancada de trabalho.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Peça](Std_Part/pt-br.md): adiciona um novo recipiente de peças no documento ativo e o torna ativo.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Grupo](Std_Group/pt-br.md): adiciona um recipiente de Grupo no documento ativo, o que permite organizar os objetos no [vista em árvore](Tree_view/pt-br.md).

### Ferramentas auxiliares de projeto de peças 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Criar corpo](PartDesign_Body/pt-br.md): cria um objeto [Corpo](Body/pt-br.md) no documento ativo e o torna ativo.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Criar esboço](PartDesign_NewSketch/pt-br.md): cria um novo esboço em um rosto ou plano selecionado. Se nenhuma face for selecionada enquanto esta ferramenta é executada, o usuário é solicitado a selecionar um plano do painel Tarefas. A interface então muda para o [Bancada de trabalho Sketcher](Sketcher_Workbench/pt-br.md) em modo de edição de esboço.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar esboço](Sketcher_EditSketch/pt-br.md): Edite o Esboço selecionado.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [ Aplique um esboço de um lado](Sketcher_MapSketch/pt-br.md): Mapeia um esboço para um plano previamente selecionado ou para uma face do corpo ativo.

### Ferramentas de modelagem de projeto de peças 

#### Ferramentas de referência 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Criar um ponto de referência](PartDesign_Point/pt-br.md): cria um ponto de referência no corpo ativo.

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Criar uma linha de referência](PartDesign_Line/pt-br.md): cria uma linha de referência no corpo ativo.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Criar um plano de referência](PartDesign_Plane/pt-br.md): cria um plano de referência no corpo ativo.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Criar um sistema de coordenadas local](PartDesign_CoordinateSystem/pt-br.md): cria um sistema de coordenadas local anexado à geometria do datum no corpo ativo.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Criar um aglutinante de forma](PartDesign_ShapeBinder/pt-br.md): cria um aglutinante de forma no corpo ativo.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Criar um aglutinante em forma de subobjetos](PartDesign_SubShapeBinder/pt-br.md): cria um aglutinante de forma para um subelemento, como borda ou face de outro corpo, enquanto mantém a posição relativa desse elemento. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Criar um clone](PartDesign_Clone/pt-br.md): cria um clone do corpo selecionado.

#### Ferramentas aditivas 

Estas são ferramentas para criar características básicas ou adicionar material a um corpo sólido existente.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Protrusão](PartDesign_Pad/pt-br.md): extruda um sólido de um esboço selecionado.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolução](PartDesign_Revolution/pt-br.md): cria um sólido ao girar um esboço em torno de um eixo. O esboço deve formar um perfil fechado.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Loft aditivo](PartDesign_AdditiveLoft/pt-br.md): cria um sólido, fazendo uma transição entre dois ou mais esboços.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Aditivo de varredura](PartDesign_AdditivePipe/pt-br.md): cria um sólido ao varrer um ou mais esboços ao longo de um caminho aberto ou fechado.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Hélice aditiva](PartDesign_AdditiveHelix/pt-br.md): cria um sólido ao varrer um esboço ao longo de uma hélice. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Criar um aditivo primitivo](PartDesign_CompPrimitiveAdditive/pt-br.md): adiciona um aditivo primitivo ao corpo ativo.

:\*<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Cubo aditivo](PartDesign_AdditiveBox/pt-br.md): cria um cubo aditivo.

:\*<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Cone aditivo](PartDesign_AdditiveCone/pt-br.md): cria um cone aditivo.

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Cilindro aditivo](PartDesign_AdditiveCylinder/pt-br.md): cria um cilindro aditivo.

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Elipsóide aditiva](PartDesign_AdditiveEllipsoid/pt-br.md): cria uma elipsóide aditiva.

:\*<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Prisma aditivo](PartDesign_AdditivePrism/pt-br.md): cria um prisma aditivo.

:\*<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Esfera aditiva](PartDesign_AdditiveSphere/pt-br.md): cria uma esfera aditiva.

:\*<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Toro aditivo](PartDesign_AdditiveTorus/pt-br.md): cria um toro aditivo.

:\*<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Cunha aditiva](PartDesign_AdditiveWedge/pt-br.md): cria uma cunha aditiva.

#### Ferramentas subtrativas 

Estas são ferramentas para subtrair material de um corpo existente.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Cavidade](PartDesign_Pocket/pt-br.md): cria uma cavidade a partir do esboço selecionado.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Perfuração](PartDesign_Hole/pt-br.md): cria uma função de perfuração a partir do esboço selecionado. O esboço deve conter um ou mais círculos.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Sulco](PartDesign_Groove/pt-br.md): cria uma ranhura ao girar um esboço em torno de um eixo.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Loft subtrativo](PartDesign_SubtractiveLoft/pt-br.md): cria um sólido, fazendo uma transição entre pelo menos dois esboços e depois o subtrai do corpo ativo.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Escaneamento subtrativo](PartDesign_SubtractivePipe/pt-br.md): cria uma forma sólida ao varrer um ou mais esboços ao longo de um caminho aberto ou fechado e o subtrai do corpo ativo.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Hélice subtrativa](PartDesign_SubtractiveHelix/pt-br.md): cria uma forma sólida ao varrer um esboço ao longo de uma hélice e o subtrai do corpo ativo. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Criar um primitivo subtrativo](PartDesign_CompPrimitiveSubtractive/pt-br.md): adiciona um primitivo subtrativo ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Cubo subtrativa](PartDesign_SubtractiveBox/pt-br.md): adiciona um cubo subtrativa ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Cone subtrativo](PartDesign_SubtractiveCone/pt-br.md): adiciona um cone subtrativo ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Cilindro subtrativo](PartDesign_SubtractiveCylinder/pt-br.md): adiciona um cilindro subtrativo ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Elipsóide subtrativa](PartDesign_SubtractiveEllipsoid/pt-br.md): adiciona uma elipsóide subtrativa ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisma subtrativo](PartDesign_SubtractivePrism/pt-br.md): adiciona um prisma subtrativo ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Esfera subtrativa](PartDesign_SubtractiveSphere/pt-br.md): adiciona uma esfera subtrativa ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Toro subtrativo](PartDesign_SubtractiveTorus/pt-br.md): adiciona um toro subtrativo ao corpo ativo.

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Cunha subtrativa](PartDesign_SubtractiveWedge/pt-br.md): adiciona uma cunha subtrativa ao corpo ativo.

#### Ferramentas de transformação 

Estas são ferramentas para transformar as características existentes. Elas permitirão que você escolha quais características transformar.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Simetria](PartDesign_Mirrored/pt-br.md): espelha uma ou mais características em um plano ou face.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Padrão Linear](PartDesign_LinearPattern/pt-br.md): cria um padrão linear baseado em uma ou mais características.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Padrão Polar](PartDesign_PolarPattern/pt-br.md): cria um padrão polar de uma ou mais características.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Transformação múltipla](PartDesign_MultiTransform/pt-br.md): cria um padrão com qualquer combinação das outras transformações.

#### Ferramentas de embelezamento 

Estas ferramentas aplicam um tratamento às bordas ou faces selecionadas.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Filete](PartDesign_Fillet/pt-br.md): filetes (redondos) bordas do corpo ativo.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chanfro](PartDesign_Chamfer/pt-br.md): chanfraduras das bordas do corpo ativo.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Rascunho](PartDesign_Draft/pt-br.md): aplica um esboço angular a rostos selecionados do corpo ativo.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Espessura](PartDesign_Thickness/pt-br.md): cria uma concha grossa a partir do corpo ativo e abre a(s) face(s) selecionada(s).

#### Booleano

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Operação booleana](PartDesign_Boolean/pt-br.md): importa um ou mais Corpos ou Clones PartDesign para o corpo ativo e aplica uma operação booleana.

#### Extras

Algumas funcionalidades adicionais encontradas no menu Design da peça:

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrar](PartDesign_Migrate/pt-br.md): migra arquivos criados com versões mais antigas do FreeCAD. Se o arquivo for baseado exclusivamente no PartDesign, a migração deve ser bem sucedida. Se o arquivo contiver objetos mistos Part/Part Design/Draft, a conversão muito provavelmente falhará.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Assistente de projeto da roda dentada](PartDesign_Sprocket/pt-br.md): cria um perfil de empena que pode ser extrudido. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Assistente de projeto de engrenagem envolvente](PartDesign_InvoluteGear/pt-br.md): cria um perfil de engrenagem involutivo que pode ser extrudado.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Assistente de projeto do eixo](PartDesign_WizardShaft/pt-br.md): Gera um eixo a partir de uma tabela de valores e permite analisar forças e momentos. O eixo é feito com um esboço giratório que pode ser editado.

### Itens do menu de contexto 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Designar como uma função resultante](PartDesign_MoveTip/pt-br.md): redefine a ponta, que é a característica exposta fora do Corpo.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Mover objeto para outro corpo](PartDesign_MoveFeature/pt-br.md): move o esboço selecionado, a geometria do datum ou a característica para outro Corpo.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Mover objeto após outro objeto](PartDesign_MoveFeatureInTree/pt-br.md): permite reordenar a árvore do corpo movendo o esboço, a geometria dos dados ou a característica selecionada para outra posição na lista de características.

#### Itens compartilhados com a bancada de trabalho da peça 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Aparência](Std_SetAppearance/pt-br.md): determina a aparência de toda a peça (transparência de cores, etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Cores definidas](Part_FaceColors/pt-br.md): atribui cores aos rostos das peças.

### Preferências

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferências](PartDesign_Preferences/pt-br.md): preferências disponíveis para as Ferramentas PartDesign.
-   [Sintonia fina](Fine-tuning/pt-br.md): alguns parâmetros extras para afinar o comportamento do PartDesign.

## Tutoriais

-   [Como usar o FreeCAD](http://help-freecad-jpg87.fr/), um website descrevendo o fluxo de trabalho para o projeto mecânico. (inglês e francês)
-   [Criando uma peça simples com o PartDesign](Creating_a_simple_part_with_PartDesign/pt-br.md)
-   [Tutorial de Projeto Básico de Peças](Basic_Part_Design_Tutorial/pt-br.md)
-   [Tutorial de Projeto de Mancais de Apoio I](PartDesign_Bearingholder_Tutorial_I/pt-br.md) (precisa de atualização)
-   [Tutorial de Projeto de Mancais de Apoio II](PartDesign_Bearingholder_Tutorial_II/pt-br.md) (precisa de atualização)





 {{PartDesign Tools navi}}

[Category:Workbenches](Category:Workbenches.md)
