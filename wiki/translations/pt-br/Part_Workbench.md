# <img alt="Ícone da bancada de trabalho Part" src=images/Workbench_Part.svg  style="width:64px;"> Part Workbench/pt-br






## Introdução


<div class="mw-translate-fuzzy">

As capacidades de modelagem sólida do FreeCAD são baseadas em [OpenCASCADE Technology](OpenCASCADE/pt-br.md)(OCCT) kernel, um sistema de CAD de nível profissional que caracteriza a criação e a manipulação avançadas da geometria 3D. A <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Bancada de trabalho Part](Part_Workbench/pt-br.md) é uma camada situada em cima das bibliotecas OCCT, que dá ao usuário acesso às primitivas e funções geométricas da OCCT. Essencialmente todas as funções de desenho 2D e 3D em cada bancada de trabalho (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/pt-br.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/pt-br.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/pt-br.md), etc.), são baseadas nestas funções expostas pela Bancada de trabalho Part. Portanto, a Bancada de trabalho Part é considerada o componente central das capacidades de modelagem do FreeCAD.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The Part Workbench can also create objects that are not solids, such as faces, shells, and objects with only edges or vertices. It also provides a variety of general purpose tools for geometry manipulation, geometry validation, and making copies.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses an alternative workflow for creating solids. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).


</div>

![](images/Part_Workbench_Example.jpg )



## Ferramentas


<div lang="en" dir="ltr" class="mw-content-ltr">

### Solids toolbar 


</div>

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/pt-br.md): Cria um cubo sólido especificando suas dimensões.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/pt-br.md): Cria um cilindro sólido especificando suas dimensões.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Part_Sphere/pt-br.md): Cria uma esfera sólida especificando suas dimensões.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone/pt-br.md): Cria um cone sólido especificando suas dimensões.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus.md): Cria um toro.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tubo](Part_Tube.md): Cria um tubo.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Criar primitivas\...](Part_Primitives.md): Uma ferramenta para criar uma das seguintes primitivas:

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plano](Part_Plane.md): Cria um plano.

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Caixa](Part_Box.md): Cria uma caixa. Este objeto também pode ser criado com a ferramenta [Cubo](Part_Box.md).

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder.md): Cria um cilindro. Este objeto também pode ser criado com a ferramenta [Cilindro](Part_Cylinder.md).

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Cria um cone. Este objeto também pode ser criado com a ferramenta [Cone](Part_Cone.md).

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Part_Sphere.md): Cria uma esfera. Este objeto também pode ser criado com a ferramenta [Esfera](Part_Sphere.md).

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Elipsóide](Part_Ellipsoid.md): Cria um elipsóide.

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus.md): Cria um toro. Este objeto também pode ser criado com a ferramenta [Toro](Part_Torus.md).

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism.md): Cria um prisma.

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cunha](Part_Wedge.md): Cria uma cunha.

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Cria uma hélice.

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Espiral](Part_Spiral.md): Cria uma espiral.

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Círculo](Part_Circle.md): Cria um arco circular.

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Elipse](Part_Ellipse.md): Cria um arco elíptico.

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Ponto](Part_Point.md): Cria um ponto.

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linha](Part_Line.md): Cria uma linha.

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polígono regular](Part_RegularPolygon.md): Cria um polígono regular.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Construtor de formas\...](Part_Builder.md): Cria formas a partir de vários formas primitivas.


<div lang="en" dir="ltr" class="mw-content-ltr">

### Part tools toolbar 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.


</div>

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusão](Part_Extrude/pt-br.md): Faz a extrusão de faces planas de um objeto.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolver](Part_Revolve/pt-br.md): Cria um sólido através da revolução de outro objeto (não sólido) ao redor de um eixo.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Espelho](Part_Mirror/pt-br.md): Cria uma peça simétrica de uma selecionada através de um plano de simetria.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v1.0)</small> 


</div>

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Filete](Part_Fillet/pt-br.md): Arredonda as arestas de um objeto.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chanfro](Part_Chamfer/pt-br.md): Cria um chanfro nas arestas de um objeto.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Fazer face a partir de fios](Part_MakeFace/pt-br.md): Faz uma face a partir de um conjunto de fios (contornos).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Superfície regrada](Part_RuledSurface/pt-br.md): Cria uma superfície a partir de duas arestas ou dois arames.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft/pt-br.md): Cria uma superfície (ou sólido) de um perfil a outro.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Varredura](Part_Sweep/pt-br.md): Varre um ou mais perfis ao longo de um caminho.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Seção](Part_Section/pt-br.md): Cria uma seção cruzando um objeto com um plano de seção.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cruzamentos\...](Part_CrossSections/pt-br.md): Cria uma ou mais seções transversais através de um objeto.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Deslocamento:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [Deslocamento 3D](Part_Offset/pt-br.md): Constrói uma forma paralela a uma certa distância da forma original.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Deslocamento 2D](Part_Offset2D/pt-br.md): Constrói um arame paralelo a uma certa distância do arame original ou amplia/encolhe uma face plana.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Espessura](Part_Thickness/pt-br.md): Utilitário para gerar uma espessura em um sólido ao selecionar faces.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projeção na superfície](Part_ProjectionOnSurface/pt-br.md): Projeta um logotipo, texto ou qualquer face, fio ou borda em uma superfície.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Cores definidas](Part_FaceColors/pt-br.md): Atribui cores a faces individuais de objetos.


</div>




<div class="mw-translate-fuzzy">

### Booleano


</div>

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Composição:

  - <img alt="32px" src=images/Part_Compound.svg  style="width:32px;"> [Criar composição](Part_Compound/pt-br.md): Cria uma composição a partir dos objetos selecionados.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explodir composição](Part_ExplodeCompound/pt-br.md): Ferramenta para dividir composição de formas.


</div>

  - <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Filtro de composição](Part_Compound‏‎Filter/pt-br.md): O filtro de composição pode ser utilizado para extrair peças individuais.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Operações booleanas](Part_Boolean/pt-br.md): Realiza operações Booleanas sobre os objetos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Recortar](Part_Cut/pt-br.md): Corta (subtrai) um objeto de outro.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [União](Part_Fuse/pt-br.md): Faz a união de dois objetos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Interseção](Part_Common/pt-br.md): Extrai a parte comum de dois objetos.


</div>

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Juntar:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Conectar](Part_JoinConnect/pt-br.md): Conecta interiores de paredes de objetos.

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embutir](Part_JoinEmbed/pt-br.md): Incorpora um objeto murado dentro de outro objeto murado.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Corte](Part_JoinCutout/pt-br.md): Cria um corte em uma parede de um objeto para outro objeto murado.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Divisão:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Fragmentos booleanos](Part_BooleanFragments/pt-br.md): Cria todas as peças que podem ser obtidas por meio das operações booleanas entre objetos. Divide os objetos onde eles se interceptam.

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Fatiar uma peça](Part_SliceApart/pt-br.md): Ferramenta para dividir formas através da intersecção com outras formas.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Fatiar](Part_Slice/pt-br.md): Divide um objeto em pedaços através da interseção com outro objeto.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR](Part_XOR/pt-br.md): Remove o espaço compartilhado por um número par de objetos (versão simétrica da [Recortar](Part_Cut/pt-br.md)).

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Verificar geometria](Part_CheckGeometry/pt-br.md): Verifica a geometria dos objetos selecionados em busca de erros.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Desnaturalização](Part_Defeaturing/pt-br.md): Remove recursos de um objeto.



### Outras ferramentas 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importar](Part_Import/pt-br.md): Esta ferramenta te permite adicionar um arquivo \*.IGES, \*.STEP, \*.BREP ao documento.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Exportar](Part_Export/pt-br.md): Esta ferramenta te permite exportar um objeto como arquivo \*.IGES, \*.STEP ou \*.BREP.


</div>

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Caixa de seleção](Part_BoxSelection/pt-br.md): Seleciona faces a partir de uma área retangular.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ShapeFromMesh.png  style="width:32px;"> [Forma a partir de malha](Part_ShapeFromMesh/pt-br.md): Cria uma forma a partir de um objeto de malha.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Pontos da malha](Part_PointsFromMesh/pt-br.md): Cria um objeto feito de pontos a partir de um objeto geométrico.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Converter em sólido](Part_MakeSolid/pt-br.md): Converte uma forma em um sólido.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Inverter formas](Part_ReverseShape/pt-br.md): Inverte as normais de todas as faces do objeto selecionado.


</div>

-   Criar uma cópia:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Criar uma cópia simples](Part_SimpleCopy/pt-br.md): Cria uma cópia simples de um objeto selecionado.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Criar cópia transformada](Part_TransformedCopy/pt-br.md): Cria uma cópia transformada de um objeto selecionado.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Criar uma cópia do elemento forma](Part_ElementCopy/pt-br.md): Cria uma cópia a partir de um elemento (vértice, borda, face) de um objeto selecionado.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refinar a forma](Part_RefineShape/pt-br.md): Limpa as faces removendo linhas desnecessárias.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Anexo](Part_EditAttachment/pt-br.md): Prende um objeto a outro objeto.


</div>



## Ferramentas obsoletas 



### Medida


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure.md) tool replaces the tools listed below. <small>(v1.0)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Medida Linear](Part_Measure_Linear/pt-br.md): Cria uma medição linear.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Medida Angular](Part_Measure_Angular/pt-br.md): Cria uma medição angular.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Medida Atualização](Part_Measure_Refresh/pt-br.md): Atualiza todas as medidas.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Limpar tudo](Part_Measure_Clear_All/pt-br.md): Limpa todas as medidas.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Alternar tudo](Part_Measure_Toggle_All/pt-br.md): Mostra ou oculta todas as medidas.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Alternar 3D](Part_Measure_Toggle_3D/pt-br.md): Mostra ou oculta medidas 3D.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Alternar o Delta](Part_Measure_Toggle_Delta/pt-br.md): Mostra ou esconde medidas delta.


</div>



## Preferências


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferências](PartDesign_Preferences/pt-br.md): Preferências disponíveis para as Ferramentas da Part (a bancada de trabalho da Part também usa as Preferências do PartDesign).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferências de exportação de importação](Import_Export_Preferences/pt-br.md): Preferências disponíveis para importação e exportação de e para diferentes formatos de arquivo.
-   [Ajuste fino](Fine-tuning/pt-br.md): Alguns parâmetros extras para afinar o comportamento das peças.


</div>

## Scripting

Veja [Script(roteiro) da peça](Part_scripting/pt-br.md).



## Tutoriais

-   [Importação de STL ou OBJ](Import_from_STL_or_OBJ/pt-br.md) : Como importar arquivos STL/OBJ no FreeCAD
-   [Exportação para STL ou OBJ](Export_to_STL_or_OBJ/pt-br.md) : Como exportar arquivos STL/OBJ do FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial/pt-br.md) : Como usar o módulo de peças



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/pt-br
