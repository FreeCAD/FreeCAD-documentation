# <img alt="Ícone da bancada de trabalho Mesh" src=images/Workbench_Mesh.svg  style="width:64px;"> Mesh Workbench/pt-br






## Introdução

A <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [ Bancada de Malhas](Mesh_Workbench/pt-br.md) manipula [malhas triangulares](http://en.wikipedia.org/wiki/Triangle_mesh). As malhas são um tipo especial de objeto 3D, composto de faces triangulares conectadas por seus vértices e arestas.

Muitos aplicativos 3D, como [Sketchup](http://en.wikipedia.org/wiki/Sketchup), [Blender](http://en.wikipedia.org/wiki/Blender_(software)), [.org / wiki / Maya\_ (software) Maya](http://en.wikipedia/) e [3D Studio Max](http://en.wikipedia.org/wiki/3d_max), usam malhas como seu tipo principal de objeto 3D. Como as malhas são objetos muito simples, contendo apenas vértices (pontos), arestas e faces triangulares, elas são muito fáceis de criar, modificar, subdividir, estender e podem ser facilmente passadas de um aplicativo para outro sem qualquer perda de detalhes. Além disso, como as malhas contêm dados muito simples, os aplicativos 3D geralmente podem gerenciar grandes quantidades deles sem usar muitos recursos. Por esses motivos, as malhas são geralmente o tipo de objeto 3D escolhido para aplicativos que lidam com filmes, animações e criação de imagens.

Entretanto, no campo da engenharia, as malhas apresentam uma grande limitação: não podem definir com precisão superfícies curvas. É por isso que o FreeCAD conta com [Brep](wikipedia_Boundary_representation.md) em vez disso. A Bancada de Trabalho Mesh oferece alguns comandos para manipular diretamente as malhas, mas é mais freqüentemente usada para importar dados de malhas 3D e convertê-los em um sólido para uso com o <img alt="" src=images/Workbench_Part.svg  style="width:24px;">. [Bancada de Trabalho Part](Part_Workbench/pt-br.md) ou <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Bancada de Trabalho PartDesign](PartDesign_Workbench/pt-br.md).

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">



## Ferramentas

Todas as ferramentas da Bancada de Trabalho Mesh podem ser acessadas a partir do menu **Meshes**. Quase todas também estão disponíveis em uma das barras de ferramentas Mesh.

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Malha de importação\...](Mesh_Import/pt-br.md): Importação de um objeto de malha de um arquivo.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Malha de exportação\...](Mesh_Export/pt-br.md): Exporta um objeto de malha para um arquivo.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> [Criar malha a partir da forma\...](Mesh_FromPartShape/pt-br.md): Cria objetos de malha a partir de objetos de forma.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Refinamento\...](Mesh_RemeshGmsh/pt-br.md): Remova um objeto de malha. <small>(v0.19)</small> 


</div>

-   Analisar
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width:32px;"> [Avaliar e Repapar malha](Mesh_Evaluation/pt-br.md): Avalia e repara um objeto de malha.
    -   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width:32px;"> [Face Info](Mesh_EvaluateFacet/pt-br.md): Dá informações sobre as faces.
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width:32px;"> [Curvatura Info](Mesh_CurvatureInfo/pt-br.md): Mostra a curvatura absoluta de [objetos de curvatura](Mesh_VertexCurvature/pt-br.md) em pontos selecionados.
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width:32px;"> [Checar malha sólido](Mesh_EvaluateSolid/pt-br.md): Verifica se um objeto de malha é sólido.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [Delimitações info](Mesh_BoundingBox/pt-br.md): Mostra as coordenadas da caixa de delimitação de um objeto de malha.

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width:32px;"> [Traçar curvatura](Mesh_VertexCurvature/pt-br.md): Cria objetos de curvatura de malha para objetos de malha.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width:32px;"> [Harmonizar as normas](Mesh_HarmonizeNormals/pt-br.md): Harmoniza as normas dos objetos de malha.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width:32px;"> [Mudança de direção de normas](Mesh_FlipNormals/pt-br.md): Vira as normas dos objetos de malha.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width:32px;"> [Preencher furos\...](Mesh_FillupHoles/pt-br.md): Preenche buracos em objetos de malha.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width:32px;"> [Fechar buraco](Mesh_FillInteractiveHole/pt-br.md): Preenche furos selecionados em objetos de malha.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width:32px;"> [Adicionar triângulo](Mesh_AddFacet/pt-br.md): Adiciona as faces ao longo de um limite de um objeto de malha aberta.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width:32px;"> [Remover componentes\...](Mesh_RemoveComponents/pt-br.md): Remove faces de objetos de malha.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width:32px;"> [Remover componentes à mão\...](Mesh_RemoveCompByHand/pt-br.md): Remove componentes de objetos de malha.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width:32px;"> [Criar segmentos de malha\...](Mesh_Segmentation/pt-br.md): Cria segmentos de malha separados para tipos de superfície especificados de um objeto de malha.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width:32px;"> [Criar segmentos de malha a partir das melhores superfícies\...](Mesh_SegmentationBestFit/pt-br.md): Cria segmentos de malha separados para tipos de superfície especificados de um objeto de malha, e pode identificar seus parâmetros.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width:32px;"> [Suavizar\...](Mesh_Smoothing/pt-br.md): Suaviza os objetos de malha.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Dizimar\...](Mesh_Decimating/pt-br.md): Reduz o número de faces em objetos de malha. <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Escala\...](Mesh_Scale/pt-br.md): Objetos de malha de escala.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Regularmente sólido\...](Mesh_BuildRegularSolid/pt-br.md): Cria um objeto de malha sólida paramétrica regular.

-   Booleanos
    -   <img alt="" src=images/Mesh_Union.svg  style="width:32px;"> [União](Mesh_Union/pt-br.md):Cria um objeto de malha que é a união de dois objetos de malha.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width:32px;"> [Intersecção](Mesh_Intersection/pt-br.md): Cria um objeto de malha que é a interseção de dois objetos de malha.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width:32px;"> [Diferença](Mesh_Difference/pt-br.md): Cria um objeto de malha que é a diferença de dois objetos de malha.


<div class="mw-translate-fuzzy">

-   Corte
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width:32px;"> [Policorte em malhas](Mesh_PolyCut/pt-br.md): Corta faces inteiras de objetos de malha.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width:32px;"> [Corte curto em malhas](Mesh_PolyTrim/pt-br.md): Apara faces e partes de faces em um lado de um plano a partir de um objeto de malha.
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width:32px;"> [Corte em malhas com um plano](Mesh_TrimByPlane/pt-br.md): Apara faces e partes de faces em um lado de um plano a partir de um objeto de malha.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width:32px;"> [Criar seção a partir de malha e plano](Mesh_SectionByPlane/pt-br.md): Cria uma seção transversal através de um objeto de malha.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width:32px;"> [Cortes transversais\...](Mesh_CrossSections/pt-br.md): Cria múltiplas seções transversais através de objetos de malha. <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Fundir](Mesh_Merge/pt-br.md): Cria um objeto de malha combinando as malhas de dois ou mais objetos de malha.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Dividido por componentes](Mesh_SplitComponents/pt-br.md): Divide um objeto de malha em seus componentes. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Desembrulhar malha](MeshPart_CreateFlatMesh/pt-br.md): Cria uma representação plana de um objeto de malha. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Face desembrulhada](MeshPart_CreateFlatFace/pt-br.md): Cria uma representação plana de uma face de um objeto de forma. <small>(v0.19)</small> 


</div>



## Preferências

Existem algumas [preferências de exportação relacionadas aos formatos de malha](Import_Export_Preferences/pt-br#Mesh_Formats.md), mas estas não são utilizadas pelos comandos pertencentes a esta bancada de trabalho. Eles são usados pelo comando [Std Export](Std_Export/pt-br.md).

As preferências da Bancada de Trabalho Mesh podem ser encontradas nas seguintes categorias do [ Editor de Preferências](Preferences_Editor/pt-br.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Display](Preferences_Editor/pt-br#Display.md): Na aba [Mesh view](Preferences_Editor/pt-br#Mesh_view.md), várias preferências podem ser definidas.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences/pt-br.md): Os comandos [Mesh União](Mesh_Union/pt-br.md), [Mesh Intersecção](Mesh_Intersection/pt-br.md) e [Mesh Diferença](Mesh_Difference/pt-br.md) requerem [OpenSCAD](http://www.openscad.org/) e usam a preferência **OpenSCAD executável** para encontrar seu executável.



## Notas

-   Mais ferramentas de malha estão disponíveis no <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [Bancada de trabalho OpenSCAD](OpenSCAD_Workbench/pt-br.md).
-   Veja [Mesh Scripting](Mesh_Scripting/pt-br.md) para manipular e criar malhas usando [Python](Python/pt-br.md).
-   Veja também [FreeCAD e importação de malha](FreeCAD_and_Mesh_Import/pt-br.md)
-   Veja [Assímptota](Asymptote/pt-br.md) para exportar malhas para o formato assintoto.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Mesh](Category_Mesh.md) > Mesh Workbench/pt-br
