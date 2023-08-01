# OpenCASCADE/pt-br
## Descrição

[OpenCASCADE Technology](OpenCASCADE/pt-br.md), **OCC** ou **OCCT** para abreviar, é uma coleção de bibliotecas C++ que juntas constituem um kernel profissional de projeto assistido por computador (CAD) para modelagem de objetos 2D e 3D, e construção de ferramentas especializadas para fabricação, simulação ou visualização. O OpenCASCADE é o coração das capacidades geométricas do FreeCAD.

As classes geométricas do OCCT são principalmente implementadas e disponibilizadas no FreeCAD através do modulo [Part](Part_Workbench/pt-br.md), do qual a maioria das outras [bancadas de trabalho](Workbenches/pt-br.md) dependem. Ele também fornece funções internas para ler e gravar diferentes formatos de arquivo como STEP e IGES, e para executar projeções 2D, que podem ser usadas para criar desenhos técnicos em [TechDraw](TechDraw_Workbench/pt-br.md).

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*OpenCASCADE fornece as classes geométricas básicas e funções de desenho para o módulo[Part](Part_Workbench/pt-br.md), que são então usados por todas as bancadas de trabalho no FreeCAD.*

OpenCASCADE não deve ser confundido com [OpenSCAD](https://www.openscad.org/), que é um projeto de código aberto diferente para construir modelos 3D, e que é acessível através da [bancada de trabalho OpenSCAD](OpenSCAD_Workbench/pt-br.md).

OpenCASCADE é software livre regido pelos termos da GNU Lesser General Public License (LGPL) versão 2.1 com uma exceção adicional.



## Instalação

OpenCASCADE é um componente central do FreeCAD, então se você obter FreeCAD de um dos links na página [Download](Download/pt-br.md), você terá ele instalado, e nenhuma instalação adicional é necessária.

No entanto, se você gostaria de desenvolver aplicativos que usam OCCT, ou gostaria de contribuir com código C++ para FreeCAD, então você precisa instalar os arquivos de desenvolvimento do OCCT. Nesse caso, o procedimento é explicado em [Compilação](Compiling/pt-br.md) para cada um dos principais sistemas, Linux, Windows e MacOS.



## Edição comunitária 

Uma \"edição comunitária\" do OpenCASCADE, abreviada OCE, foi lançada em 2011, com base nos fontes oficiais do OpenCASCADE (OCCT) da versão 6.5. Em teoria, a edição da comunidade OCE deve ser compatível com a versão principal OCCT na maioria dos aspectos, tendo algum código adicional contribuído pela comunidade.

No entanto, essa distribuição alternativa parou o desenvolvimento ativo por volta de 2017 e ficou atrás da versão principal em termos de recursos e correções de bugs. Por esta razão, desde o FreeCAD v0.17, o FreeCAD é compilado exclusivamente com OCCT, e o OCE não é testado.

Em algumas distribuições Linux mais antigas, o FreeCAD é compilado contra OCE 0.18, equivalente ao OCCT 6.9.x, causando vários problemas que já foram resolvidos nas principais versões do OCCT 7.x. Se esse for o caso, tente remover o OCE e instalar o OCCT. Se isso não for possível, use o [AppImage](AppImage/pt-br.md) para obter um FreeCAD moderno com uma versão OCCT atualizada.



## História

O kernel geométrico Cas.CADE era originalmente de código fechado, mas tornou-se open source sob seu nome atual por volta do ano 2000. Pouco depois, o projeto FreeCAD foi iniciado, com os arquivos mais antigos sendo datados de janeiro de 2001. Leia mais em [História](History/pt-br.md).

OpenCASCADE versão 6.6 e anteriores foram governados por sua própria \"licença pública OCCT\", o que fez com que não fosse inteiramente \"software livre\". Isso foi resolvido com o lançamento do OCCT 6.7 (2013), quando adotou a licença LGPL2.



## Conceitos geométricos da OCCT 

Na terminologia OpenCascade, distinguimos entre primitivas geométricas e formas topológicas. Uma primitiva geométrica pode ser um ponto, uma linha, um círculo, um plano, etc. ou mesmo alguns tipos mais complexos, como uma curva B-Spline ou uma superfície. Uma forma pode ser um vértice, uma borda, um fio, um rosto, um sólido ou um composto de outras formas. As primitivas geométricas não são feitas para serem exibidas diretamente na cena 3D, mas sim para serem usadas como geometria de construção de formas. Por exemplo, uma aresta pode ser construída a partir de uma linha ou de uma parte de um círculo.

Em resumo, as primitivas de geometria são blocos de construção \"disformes\", enquanto [formas topológicas](Part_TopoShape/pt-br.md) são os objetos reais construídos sobre eles.

Uma lista completa de todas as primitivas e formas refere-se à [documentação do OCC](https://dev.opencascade.org/resources/documentation) (Alternativa: [sourcearchive.com](https://www.opencascade.com/doc/occt-7.4.0/refman/html/)) e procure por **Geom\_\*** (para primitivas geométricas) e **TopoDS\_\*** (para formas). Lá você também pode ler mais sobre as diferenças entre eles em Inglês. Por favor, note que a documentação oficial do OCC não está disponível on-line (você deve baixar um arquivo) e é principalmente destinada a programadores, não a usuários finais. Mas espero que você encontre informações suficientes para começar aqui. Consulte também [Guia do usuário de dados de modelagem](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html).

> \'\'Em um nível muito alto, a topologia diz de quais peças um objeto é feito e as relações lógicas entre elas. Uma forma é feita de um determinado conjunto de rostos. Um rosto é delimitado por um certo conjunto de arestas. Duas faces são adjacentes se compartilharem uma borda comum.\"

> *A topologia sozinha não informa o tamanho, a curvatura ou os locais 3D de nenhuma dessas peças. No entanto, cada parte da topologia sabe sobre sua geometria subjacente. Um rosto sabe em que superfície se encontra. Uma aresta sabe em que curva se encontra. A geometria sabe sobre curvatura e localização no espaço.* - [Fonte](https://www.opencascade.com/content/geometry-and-topology)


<hr />

> *Assim, a Topologia define a relação entre entidades geométricas simples, que podem ser ligadas entre si para representar formas complexas.* - [Modeling Data User\'s Guide](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html)

![](images/ClassTopoDS_Shape_inherit_graph.png )

**Nota:** Apenas 3 tipos de objetos topológicos têm representações geométricas -- vértice, aresta e face ([Fonte](https://opencascade.blogspot.com/2009/02/topology-and-geometry-in-open-cascade.html)).

Os tipos geométricos, na verdade, podem ser divididos em dois grandes grupos: curvas e superfícies. A partir das curvas (linha, círculo, \...) você pode construir diretamente uma borda, a partir das superfícies (plano, cilindro, \...) uma face pode ser construída. Por exemplo, a linha primitiva geométrica é ilimitada, ou seja, é definida por um vetor base e um vetor de direção, enquanto sua representação de forma deve ser algo limitado por um ponto inicial e final. E uma caixa - um sólido - pode ser criada por seis planos limitados.

De uma borda ou face você também pode voltar à sua contraparte primitiva geométrica.

Assim, a partir de formas, você pode construir peças muito complexas ou, ao contrário, extrair todas as subformas de que uma forma mais complexa é feita.

<img alt="" src=images/Part_TopoShape_relationships.svg  style="width:600px;">



*A classe `Part::TopoShape* é o objeto geométrico que é visto na tela. Essencialmente, todas as bancadas de trabalho usam estas [TopoShapes](Part_TopoShape/pt-br.md) internamente para construir e exibir bordas, faces e sólidos.`



## Relacionado

-   Tecnologia OpenCASCADE (OCCT) [site principal](http://www.opencascade.com)
-   OCCT \[Portal de desenvolvimento <https://dev.opencascade.org/>\]
-   OCCT [versão mais recente](https://www.opencascade.com/content/latest-release)
-   OCCT [repositório git](https://git.dev.opencascade.org/gitweb/?p=occt.git)
-   OpenCASCADE Community Edition (OCE) [repositório git](https://github.com/tpaviot/oce)
-   [Open Cascade Technology OCCT](http://en.wikipedia.org/wiki/Open_Cascade_Technology) na Wikipédia
-   Glossário, [Open CASCADE](Glossary/pt-br#Open_CASCADE.md)
-   Rastreamento de bugs OCCT no bugtracker FreeCAD [(thread)](https://forum.freecadweb.org/viewtopic.php?f=10&t=20264)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > OpenCASCADE/pt-br
