# Part Module/pt-br
<div class="mw-translate-fuzzy">





</div>

<img alt="Ícone da bancada de trabalho Part" src=images/Workbench_Part.svg  style="width:128px;">


{{TOCright}}

## Introdução

As capacidades de modelagem sólida do FreeCAD são baseadas em _ é uma camada situada em cima das bibliotecas OCCT, que dá ao usuário acesso às primitivas e funções geométricas da OCCT. Essencialmente todas as funções de desenho 2D e 3D em cada bancada de trabalho (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _, <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/pt-br.md), etc.), são baseadas nestas funções expostas pela Bancada de trabalho Part. Portanto, a Bancada de trabalho Part é considerada o componente central das capacidades de modelagem do FreeCAD.

Uma discussão mais detalhada da bancada de trabalho Part comparada à bancada de trabalho Part Design pode ser encontrada aqui: [Part e Part Design](Part_and_PartDesign/pt-br.md).

Os objetos criados com a bancada de trabalho são relativamente simples; destinam-se a ser utilizados com operações booleanas (uniões e cortes) a fim de construir formas mais complexas. **Este paradigma de modelagem é conhecido como _), até que o objeto final seja obtido.

Os objetos das peças são mais complexos que os objetos de malha criados com a [bancada de trabalho Mesh](Mesh_Workbench/pt-br.md), pois permitem operações mais avançadas como operações booleanas coerentes, histórico de modificações e comportamento paramétrico.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">


*A bancada de trabalho é a camada básica que expõe as funções de desenho do OCCT a todas as bancadas de trabalho do FreeCAD.*

## Ferramentas

As ferramentas estão localizadas no menu **Part** ou no menu **Medida**.

### Primitivas

Essas são ferramentas para criar objetos primitivos.

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/pt-br.md): Cria um cubo sólido especificando suas dimensões.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/pt-br.md): Cria um cilindro sólido especificando suas dimensões.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Part_Sphere/pt-br.md): Cria uma esfera sólida especificando suas dimensões.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone/pt-br.md): Cria um cone sólido especificando suas dimensões.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus/pt-br.md): Cria um toro (anel) sólido especificando suas dimensiones.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tubo](Part_Tube/pt-br.md): Cria um tubo. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Criar primitivas](Part_Primitives/pt-br.md): Uma ferramenta para criar diversas primitivas geométricas paramétricas.
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plano](Part_Plane/pt-br.md): Cria um plano.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> _.
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> _.
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> _.
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> _.
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Elipsóide](Part_Ellipsoid/pt-br.md): Cria uma elipsóide.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> _.
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/pt-br.md): Cria um prisma.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cunha](Part_Wedge/pt-br.md): Cria uma cunha.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/pt-br.md): Cria uma hélice.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Espiral](Part_Spiral/pt-br.md): Cria uma espiral.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Círculo](Part_Circle/pt-br.md): Cria uma borda circular.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Elipse](Part_Ellipse/pt-br.md): Cria uma borda elíptica.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Ponto](Part_Point/pt-br.md): Cria um ponto (vértice).
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linha](Part_Line/pt-br.md): Cria uma linha (borda).
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polígono regular](Part_RegularPolygon/pt-br.md): Cria um polígono regular.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Construtor de formas](Part_Builder/pt-br.md): Uma ferramenta para criar formas mais complexas a partir de diversas primitivas geométricas paramétricas.

### Criação e modificação 

Estas são ferramentas para criar novos objetos e modificar os existentes.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusão](Part_Extrude/pt-br.md): Faz a extrusão de faces planas de um objeto.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolução](Part_Revolve/pt-br.md): Cria um sólido ao revolver outro objeto (não sólido) ao redor do eixo.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Simetria](Part_Mirror/pt-br.md): Cria uma simetria dos objetos selecionados ao redor de um plano de simetria dado.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Filete](Part_Fillet/pt-br.md): Arredonda as arestas de um objeto.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chanfro](Part_Chamfer/pt-br.md): Cria um chanfro nas arestas selecionadas de um objeto.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Fazer face a partir de fios](Part_MakeFace/pt-br.md): Faz uma face a partir de um conjunto de fios (contornos). <small>(v0.19)</small> 

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Superfície regrada](Part_RuledSurface/pt-br.md): Cria uma superfície regrada a partir de duas arestas ou dois arames.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft/pt-br.md): Cria uma superfície (ou sólido) de um perfil a outro.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Varredura](Part_Sweep/pt-br.md): Varre um ou mais perfis ao longo de um caminho.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Seção](Part_Section/pt-br.md): Cria uma seção cruzando um objeto com um plano de seção.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cruzamentos\...](Part_CrossSections/pt-br.md): Cria uma ou mais seções transversais através de um objeto.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Ferramentas de deslocamento](Part_CompOffsetTools/pt-br.md): Ferramentas para deslocamento de formas. Este é um ícone-menu na barra de ferramentas da bancada Part que contém os seguintes comandos:
    -   <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [Deslocamento 3D](Part_Offset/pt-br.md): Constrói uma forma paralela a uma certa distância da forma original.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Deslocamento 2D](Part_Offset2D/pt-br.md): Constrói um arame paralelo a uma certa distância do arame original ou amplia/encolhe uma face plana.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Espessura](Part_Thickness/pt-br.md): Utilitário para gerar uma espessura em um sólido ao selecionar faces.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projeção na superfície](Part_ProjectionOnSurface/pt-br.md): Projeta um logotipo, texto ou qualquer face, fio ou borda em uma superfície. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Attachment.svg  style="width:32px;"> [Anexo](Part_Attachment/pt-br.md): Prende um objeto a outro objeto.


</div>

### Booleano

Estas ferramentas realizam operações booleanas.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Ferramentas de composição](Part_CompCompoundTools/pt-br.md): Este é um ícone-menu na barra de ferramentas Part que contém os seguintes comandos:
    -   <img alt="32px" src=images/Part_Compound.svg  style="width:32px;"> [Criar composição](Part_Compound/pt-br.md): Cria uma composição a partir dos objetos selecionados.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explodir composição](Part_ExplodeCompound/pt-br.md): Ferramenta para dividir composição de formas.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Filtro de composição](Part_Compound‏‎Filter/pt-br.md): O filtro de composição pode ser utilizado para extrair peças individuais.

-   <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Operações booleanas](Part_Boolean/pt-br.md): Realiza operações Booleanas sobre os objetos.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Diferença](Part_Cut/pt-br.md): Corta (subtrai) um objeto de outro.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [União](Part_Fuse/pt-br.md): Faz a união de dois objetos.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Interseção](Part_Common/pt-br.md): Extrai a parte comum de dois objetos.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Juntar atributos](Part_CompJoinFeatures/pt-br.md): Operações booleanas para objetos murados (ex. tubos). Este é um ícone-menu na barra de ferramentas da bancada Part que contém os seguintes comandos:
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Conectar](Part_JoinConnect/pt-br.md): Conecta interiores de paredes de objetos.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embutir](Part_JoinEmbed/pt-br.md): Incorpora um objeto murado dentro de outro objeto murado.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Corte](Part_JoinCutout/pt-br.md): Cria um corte em uma parede de um objeto para outro objeto murado.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Ferramentas de divisão](Part_CompSplittingTools/pt-br.md):Este é um ícone-menu na barra de ferramentas da bancada Part que contém os seguintes comandos:
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Fragmentos booleanos](Part_BooleanFragments/pt-br.md): Cria todas as peças que podem ser obtidas por meio das operações booleanas entre objetos. Divide os objetos onde eles se interceptam.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Fatiar uma peça](Part_SliceApart/pt-br.md): Ferramenta para dividir formas através da intersecção com outras formas.
    -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Fatiar](Part_Slice/pt-br.md): Divide um objeto em pedaços através da interseção com outro objeto.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> _).

### Medida

<img alt="" src=images/Part_Measure_Menu.png  style="width:64px;"> [Medida](Part_Measure_Menu/pt-br.md): Ferramentas para medições lineares e angulares.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Medida Linear](Part_Measure_Linear/pt-br.md): Cria uma medição linear.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Medida Angular](Part_Measure_Angular/pt-br.md): Cria uma medição angular.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Medida Atualização](Part_Measure_Refresh/pt-br.md): Atualiza todas as medidas.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Limpar tudo](Part_Measure_Clear_All/pt-br.md): Limpa todas as medidas.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Alternar tudo](Part_Measure_Toggle_All/pt-br.md): Mostra ou oculta todas as medidas.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width:32px;"> [Alternar 3D](Part_Measure_Toggle_3d/pt-br.md): Mostra ou oculta medidas 3D.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Alternar o Delta](Part_Measure_Toggle_Delta/pt-br.md): Mostra ou esconde medidas delta.

### Outras ferramentas 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importar](Part_Import/pt-br.md): Esta ferramenta te permite adicionar um arquivo \*.IGES, \*.STEP, \*.BREP ao documento.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Exportar](Part_Export/pt-br.md): Esta ferramenta te permite exportar um objeto como arquivo \*.IGES, \*.STEP ou \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [CaixaSeleção](Part_BoxSelection/pt-br.md): Seleciona faces a partir de uma área retangular.

-   <img alt="" src=images/Part_ShapeFromMesh.png  style="width:32px;"> [Forma a partir de uma malha](Part_ShapeFromMesh/pt-br.md): Cria uma forma a partir de um objeto de malha.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Pontos da malha](Part_PointsFromMesh/pt-br.md): Cria um objeto de forma feito de pontos a partir de um objeto de malha. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Converter em sólido](Part_MakeSolid/pt-br.md): Converte uma forma em um sólido.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Inverter formas](Part_ReverseShapes/pt-br.md): Inverte as normais de todas as faces do objeto selecionado.

-   Criar uma cópia:
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Criar uma cópia simples](Part_SimpleCopy/pt-br.md): Cria uma cópia simples de um objeto selecionado.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Criar cópia transformada](Part_TransformedCopy/pt-br.md): Cria uma cópia transformada de um objeto selecionado. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Criar uma cópia do elemento forma](Part_ElementCopy/pt-br.md): Cria uma cópia a partir de um elemento (vértice, borda, face) de um objeto selecionado. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refinar a forma](Part_RefineShape/pt-br.md): Limpa as faces removendo linhas desnecessárias.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Verificar geometria](Part_CheckGeometry/pt-br.md): Verifica a geometria dos objetos selecionados em busca de erros.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Desnaturalização](Part_Defeaturing/pt-br.md): Remove recursos de um objeto.

### Itens do menu de contexto 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Aparência](Std_SetAppearance/pt-br.md): Determina a aparência de um objeto inteiro (cor, transparência, etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Cores definidas](Part_FaceColors/pt-br.md): Atribui cores a faces individuais de objetos.

## Preferências

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferências](PartDesign_Preferences/pt-br.md): Preferências disponíveis para as Ferramentas da Part (a bancada de trabalho da Part também usa as Preferências do PartDesign).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferências de exportação de importação](Import_Export_Preferences/pt-br.md): Preferências disponíveis para importação e exportação de e para diferentes formatos de arquivo.
-   [Ajuste fino](Fine-tuning/pt-br.md): Alguns parâmetros extras para afinar o comportamento das peças.

## Scripting

Veja [Script(roteiro) da peça](Part_scripting/pt-br.md).

## Tutoriais

-   [Importação de STL ou OBJ](Import_from_STL_or_OBJ/pt-br.md) : Como importar arquivos STL/OBJ no FreeCAD
-   [Exportação para STL ou OBJ](Export_to_STL_or_OBJ/pt-br.md) : Como exportar arquivos STL/OBJ do FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial/pt-br.md) : Como usar o módulo de peças


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/pt-br
