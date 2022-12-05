# OpenSCAD Workbench/pt-br
<div class="mw-translate-fuzzy">





</div>

<img alt="OpenSCAD workbench icon" src=images/Workbench_OpenSCAD.svg  style="width:128px;">

## Introdução

The <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) is intended to offer interoperability with the open source software [OpenSCAD](http://www.openscad.org/). This program is not distributed as part of FreeCAD, but should be installed to make full use of this workbench. OpenSCAD should not be confused with [OpenCASCADE](OpenCASCADE.md), which is the geometrical kernel that FreeCAD uses to build geometry on screen. The OpenCASCADE libraries are always needed to use FreeCAD, while the OpenSCAD executable is entirely optional.

Ela contém um importador [CSG](OpenSCAD_CSG.md) para abrir arquivos CSG do OpenSCAD e um exportador para a saída de um CSG baseado em árvore. A geometria que não está baseada em operações CSG serão exportadas como uma malha.

Esta bancada de trabalho contém funções para modificar o recurso de árvore CSG e reparar modelos. Também contém ferramentas de propósitos gerais que não necessitam de instalação do OpenSCAD; elas também podem ser utilizadas em conjunto com outras bancadas de trabalho.


{{TOCright}}

![](images/OpenSCADexamaple1.png )

## Dependencies

In FreeCAD 0.19, the Ply (Python-Lex-Yacc) module, which is used to import CSG files, was removed from the FreeCAD source code, as it is a third party library not developed by FreeCAD. As a result, you now need to install Ply before using the OpenSCAD Workbench. When using a pre-packaged, stable version of FreeCAD this dependency should be installed automatically in all platforms; in other cases, for example, when [compiling](Compiling.md) from source, you may have to install it from an online repository.

In openSUSE this is done by:


```python
sudo zypper install python3-ply
```

In Debian/Ubuntu based systems this is done like the following:


```python
sudo apt install python3-ply
```

The general installation in all platforms can be done from the Python package index.


```python
pip3 install --user ply
```

## A linguagem OpenSCAD e formato de arquivo 

A linguagem OpenSCAD permite o uso de variáveis e laços de repetição. Permite que você especifique submódulos para reutilizar geometria e código. Este alto grau de flexibilidade torna a análise muito complexa. Atualmente a bancada OpenSCAD não pode manipular a linguagem OpenSCAD nativamente. Em vez disso, se o OpenSCAD estiver instalado, pode ser usado para converter a entrada em formato CSG, o qual é um subconjunto da linguagem OpenSCAD e pode ser utilizada como entrada para o OpenSCAD para processamento adicional.

## Ferramentas

-   <img alt="" src=images/OpenSCAD_ColorCodeShape.svg  style="width:32px;"> [Cor da Forma](OpenSCAD_ColorCodeShape/pt-br.md): Modifica a cor de todas as formas selecionadas baseado na validade delas.
-   <img alt="" src=images/OpenSCAD_ReplaceObject.svg  style="width:32px;"> [Substituir Objeto](OpenSCAD_ReplaceObject/pt-br.md): Substitui um objeto no recurso de árvore.
-   <img alt="" src=images/OpenSCAD_RemoveSubtree.svg  style="width:32px;"> [Remover Subárvore](OpenSCAD_RemoveSubtree/pt-br.md): Remove os objetos selecionados e todos os filhos que não são referenciados de outros objetos.
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:32px;"> [Função Refinar Formas](OpenSCAD_RefineShapeFeature/pt-br.md): Cria um recurso de refino de forma.
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:32px;"> [Característica de refinar a forma](OpenSCAD_RefineShapeFeature/pt-br.md): Criar característica de refinar a forma.
-   <img alt="" src=images/OpenSCAD_MirrorMeshFeature.svg  style="width:32px;"> [Simétrica](OpenSCAD_MirrorMeshFeature/pt-br.md): Crie simetria na Malha.
-   <img alt="" src=images/OpenSCAD_ScaleMeshFeature.svg  style="width:32px;"> [Escala](OpenSCAD_ScaleMeshFeature/pt-br.md): Escala uma característica de malha.
-   <img alt="" src=images/OpenSCAD_ResizeMeshFeature.svg  style="width:32px;"> [Redimensionar](OpenSCAD_ResizeMeshFeature/pt-br.md): Redimensionar uma malha.
-   <img alt="" src=images/OpenSCAD_IncreaseToleranceFeature.svg  style="width:32px;"> [Função Aumentar Tolerância](OpenSCAD_IncreaseToleranceFeature/pt-br.md): Aumenta a tolerância das arestas/faces/vértices de objetos selecionados.
-   <img alt="" src=images/OpenSCAD_Edgestofaces.svg  style="width:32px;"> [Converter Arestas em Faces](OpenSCAD_Edgestofaces/pt-br.md): Converte arestas em faces. É útil para preparar geometria importada DXF para extrusão.
-   <img alt="" src=images/OpenSCAD_ExpandPlacements.svg  style="width:32px;"> [Expandir Posicionamento](OpenSCAD_ExpandPlacements/pt-br.md): Expanda todas as veiculações para baixo no FeatureTree.
-   <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> [Explodir Grupo](OpenSCAD_ExplodeGroup/pt-br.md): Explode peças fundidas primitivas.
-   <img alt="" src=images/OpenSCAD_AddOpenSCADElement.svg  style="width:32px;"> [Adicionar elemento OpenSCAD](OpenSCAD_AddOpenSCADElement/pt-br.md): Adiciona um elemento OpenSCAD ao inserir um código OpenSCAD no painel de tarefas.
-   <img alt="" src=images/OpenSCAD_MeshBoolean.svg  style="width:32px;"> [Booleano Malha](OpenSCAD_MeshBoolean/pt-br.md): Cria um novo objeto de malha através de operação booleana de formas.
-   <img alt="" src=images/OpenSCAD_Hull.svg  style="width:32px;"> [Casco](OpenSCAD_Hull/pt-br.md): Aplica um casco às formas selecionadas.
-   <img alt="" src=images/OpenSCAD_Minkowski.svg  style="width:32px;"> [Minkowski](OpenSCAD_Minkowski/pt-br.md): Aplica uma soma minkowski às formas selecionadas.

## Preferências

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferências](OpenSCAD_Preferences/pt-br.md): Preferências disponíveis para as ferramentas do OpenSCAD.

## Limitations


<div class="mw-translate-fuzzy">

## Limitações

O OpenSCAD cria geometria sólida construtiva, além de importar arquivos de malha e extrudir a geometria 2D dos arquivos [ DXF](DXF.md). O FreeCAD também permite que você crie CSG com primitivos. A geometria kernel (OCCT) do FreeCAD funciona usando um representação limite.Portanto, a conversão do CSG para o BREP deve, em teoria, ser possível, enquanto a conversão do BREP para o CSG não é, em geral, possível.


</div>


<div class="mw-translate-fuzzy">

O OpenSCAD trabalha internamente nas malhas. Algumas operações que são úteis em malhas não são significativas em um modelo BREP e não podem ser totalmente suportadas. Entre estes estão o casco convexo, soma minkowski, glide e subdiv. Atualmente executamos o binário OpenSCAD para realizar operações de casco e minkwoski e importar o resultado. Isso significa que a geometria envolvida será triangulada. No OpenSCAD, o escalonamento não uniforme é frequentemente usado, o que não impõe nenhum problema ao usar malhas. Em nossa geometria, as primitivas geométricas do kernel (linhas, seções circulares, etc) são convertidas para o BSpline antes de executar tais deformações. Esses BSplines são conhecidas por causar problemas em operações booleanas posteriores. Uma solução automática não está disponível no momento. Por favor, sinta-se livre para postar no fórum se você encontrar tais problemas. Muitas vezes, esses problemas podem ser resolvidos por pequenas peças de remodelação. Uma deformação de um cilindro pode ser substituída por uma extrusão de elipses.


</div>

## Importing text 

Importing OpenSCAD code with texts requires that the fonts that are used are properly installed on your system. You can verify this by opening OpenSCAD as a standalone tool and checking the list in **Help → Font List**. The list will also give you the correct font names. If a font does not appear in the list after installing, you may have to manually copy the font file to the appropriate system directory.

Importing texts is relatively slow. Behind the scenes FreeCAD uses a DXF file created by OpenSCAD. The more contours there are the slower the import.

It can be a good idea to first import a simple test case (replace {{Incode|NameOfFont}} with the correct font name):

    TESTFONT="NameOfFont";
    linear_extrude(0.001) {
      text("A", size=5, font=TESTFONT, script="Latn");
    };

The {{Incode|<nowiki>script="Latn"</nowiki>}} parameter can be left out here, but is required if the text string does not contain any letters, but only punctuation and/or numbers.

Please note that {{Incode|<nowiki>use <FONT>;</nowiki>}} statements in your source files are ignored when importing in FreeCAD. Under OpenSCAD the effect of a {{Incode|use}} statement is that the provided font file is temporarily added to the list of known fonts (although even there the statement does not work when a script is modified interactively).

## Dicas

Ao importar [ DXF](DXF.md), defina a precisão do rascunho para uma quantidade razoável, pois isso afetará a detecção das arestas conectadas.

Se o FreeCAD travar ao importar o CSG, é altamente recomendável que você ative a opção \"verificar automaticamente o modelo após a operação booleana\" em {{MenuCommand | Menu → Editar → Preferências → Desenho da Peça → Configuração do Modelo}}.

## Tutoriais

-   [Importar código OpenSCAD](Import_OpenSCAD_code/pt-br.md)

## Links


<div class="mw-translate-fuzzy">

-   Repositório de código fonte do OpenSCAD em [GitHub](https://github.com/openscad/openscad)
-   [Open tickets tagged \"Openscad\" on the FreeCAD bugtracker](https://freecadweb.org/tracker/search.php?tag_string=OpenSCAD)
-   [Things tagged with \"OpenSCAD\" on Thingiverse](http://www.thingiverse.com/tag:openscad)


</div>


<div class="mw-translate-fuzzy">





</div>


{{OpenSCAD Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [OpenSCAD](Category_OpenSCAD.md) > OpenSCAD Workbench/pt-br
