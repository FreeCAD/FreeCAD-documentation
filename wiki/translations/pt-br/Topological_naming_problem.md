# Topological naming problem/pt-br
## Introdução




O **Problema de Nomeação Topológica** no FreeCAD refere-se a uma questão em que partes internas de um modelo, como faces, arestas ou vértices, tinham seus nomes internos alterados após operações de modelagem (como extrusão, corte, união, chanfro, arredondamento, etc.). Essas alterações causavam falhas ou cálculos incorretos em recursos paramétricos que dependiam dessas partes.

Esse problema era especialmente evidente em duas situações principais:

-   Na <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Bancada PartDesign](PartDesign_Workbench/pt-br.md)\*\*: Se um recurso dependia de uma face (ou aresta ou vértice) de um sólido, ele poderia se romper ou apresentar falhas caso o sólido tivesse seu tamanho ou orientação alterados, já que os nomes internos das partes usadas poderiam mudar.

-   Na <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Bancada TechDraw](TechDraw_Workbench/pt-br.md)\*\*: Dimensões aplicadas em arestas ou outras características projetadas de um modelo 3D poderiam perder a referência ou se tornar inválidas caso o modelo fosse modificado, devido à alteração nos nomes internos das partes.

**Solução para o problema na versão 1.0:**

Esse problema, de longa data, foi abordado e parcialmente resolvido graças ao esforço conjunto de vários desenvolvedores. O algoritmo desenvolvido por Realthunder foi implementado e aprimorado na versão principal do FreeCAD. Embora ainda existam melhorias planejadas para futuras versões, a versão 1.0 trouxe uma solução inicial sólida, tornando o trabalho com modelagem paramétrica muito mais confiável e eficiente.

O problema de nomeação topológica é uma questão complexa na modelagem CAD, originada pela forma como as rotinas internas do FreeCAD lidam com as atualizações das formas geométricas criadas usando o núcleo [OCCT](OpenCASCADE/pt-br.md). Esse problema não é exclusivo do FreeCAD; ele está presente em softwares CAD em geral. No entanto, a maioria dos outros softwares CAD utiliza heurísticas para minimizar o impacto desse problema na experiência dos usuários.

No caso do FreeCAD, o esforço na versão 1.0 introduziu uma solução baseada no algoritmo de Realthunder, que melhora significativamente a confiabilidade na edição e atualização de modelos paramétricos.


<div class="mw-translate-fuzzy">

A partir do FreeCAD 0.19, esforços de desenvolvimento contínuos foram realizados para melhorar o gerenciamento central de formas, reduzindo o impacto dos problemas de nomeação topológica. O algoritmo de nomeação, detalhado no tópico do fórum [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278), foi projetado para diminuir o esforço manual. Ele pode corrigir automaticamente alguns problemas, sugerir soluções prováveis ou, pelo menos, indicar claramente a origem do problema.

A primeira versão estável do FreeCAD a incorporar esse novo algoritmo de nomeação é a 1.0. Com o tempo, esse algoritmo será expandido para mais áreas do software, adicionando mais ferramentas de reparo automático e assistido em versões futuras. Isso marca um avanço significativo para usuários que dependem de modelos paramétricos robustos e confiáveis.


</div>

O problema de nomeação topológica geralmente afeta e confunde os novos usuários do FreeCAD. No PartDesign, o usuário é aconselhado a seguir as práticas recomendadas discutidas na página [edição de recursos](feature_editing/pt-br.md). O uso de objetos de dados de suporte como [plano de referência](PartDesign_Plane/pt-br.md) e [criar um sistema de coordenadas local](PartDesign_CoordinateSystem.md) é altamente recomendado para produzir modelos que não estejam facilmente sujeitos a esses erros topológicos. No TechDraw, o usuário é aconselhado a adicionar dimensões somente quando o modelo 3D estiver completo e não for modificado posteriormente.



## Exemplo

1\. Na <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md), crie um <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo](PartDesign_Body/pt-br.md) e, em seguida, use <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [criar esboço](PartDesign_NewSketch/pt-br.md) e selecione o plano XY para desenhar; em seguida, execute um <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [preencher](PartDesign_Pad/pt-br.md) para criar o primeiro sólido.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Selecione a face superior do sólido anterior e, em seguida, use <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [criar esboço](PartDesign_NewSketch.md) para desenhar outro esboço; em seguida, execute um segundo preencher.

+++
| <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;"> |
+++

3\. Selecione a face superior da extrusão anterior e, mais uma vez, crie um esboço e um bloco com preencher.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Agora, clique duas vezes no segundo esboço e modifique-o de modo que seu comprimento esteja ao longo da direção X; isso recriará o segundo preencher. O terceiro esboço e o bloco permanecerão no mesmo lugar.

+++
| <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;"> |
+++

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Agora, clique duas vezes no segundo (Sketch001) esboço novamente e ajuste seus pontos de modo que uma parte dele fique fora dos limites definidos pelo primeiro bloco. Ao fazer isso, o segundo bloco será recomputado corretamente; no entanto, ao examinar a [vista em árvore](Tree_view/pt-br.md), será indicado um erro no terceiro bloco.

+++
| <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;"> |
+++

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. Ao tornar visíveis o terceiro esboço e o bloco, fica claro que o cálculo do novo sólido não foi feito corretamente. O terceiro esboço, em vez de ser apoiado pela face superior do segundo bloco, aparece em um local estranho, com sua normal orientada para a direção X. Isso resulta em um bloco inválido, já que esse bloco seria desconectado do restante do <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [corpo](PartDesign_Body/pt-br.md), o que não é permitido.

O problema parece ser que, quando o segundo esboço foi modificado, a face superior do segundo bloco foi renomeada de `Face13` para `Face14`. O terceiro esboço está anexado a `Face13` como estava originalmente, mas como essa face agora está na lateral (e não no topo), o esboço segue sua orientação e agora está posicionado incorretamente.

+++
| <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;"> |
+++

7\. Para corrigir o problema, o terceiro esboço deve ser mapeado novamente para a face superior. Selecione o esboço (Sketch002), clique nas reticências (três pontos) ao lado da propriedade **Map Mode** e escolha novamente a face superior do segundo bloco. Em seguida, o esboço se move para a parte superior do sólido existente e o terceiro bloco é gerado sem problemas.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

+++
| <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;"> |
+++

O remapeamento de um esboço dessa forma pode ser feito sempre que houver um erro de nomeação topológica; no entanto, isso pode ser tedioso se o modelo for complicado e houver muitos esboços que precisem ser ajustados.



## Solução

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

O [gráfico de dependência](Std_DependencyGraph.md) é uma ferramenta útil para observar as relações entre os diferentes corpos do documento. O uso do fluxo de trabalho de modelagem original revela a relação direta que existe entre os esboços e os blocos. Como em uma cadeia, é fácil ver que essa dependência direta estará sujeita a problemas de nomeação topológica se algum dos links da sequência for alterado.

Conforme explicado na página [edição de recursos](Feature_editing/pt-br.md), uma solução para esse problema é oferecer suporte a esboços não em faces, mas nos planos principais da [PartDesign Corpo](PartDesign_Body/pt-br.md) Origin, ou em planos de referência anexados a esses planos principais. O uso de planos de referência para suportar um único esboço, conforme descrito abaixo, não é realmente necessário, pois o próprio esboço pode ser anexado diretamente a um plano principal e tem as mesmas opções de deslocamento que um plano de referência. Mas o uso de planos de referência pode fazer sentido ao posicionar vários esboços.

1\. Select the origin of the [PartDesign Body](PartDesign_Body.md) and make sure that it is visible. Then select the XY plane, and click on [PartDesign Plane](PartDesign_Plane.md). In the attachment offset dialog, give it an offset in the Z direction so that the datum plane is coplanar with the top face of the first pad.

2\. Repita o processo, mas, desta vez, adicione um deslocamento maior para que o segundo plano de referência fique coplanar com a face superior do segundo bloco.




+++
| <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;"> |
+++

3\. Select the second sketch, click on the ellipsis next to the **Map Mode** property, and then select the first datum plane. The datum plane is already offset from the body\'s XY plane, so no further Z offset is required for the sketch.

4\. Repeat the process with the third sketch, and select the second datum plane as support. Again, no further Z offset is necessary.

5\. The dependency graph now shows that the sketches and pads are supported by the datum planes. This model is more stable as each sketch can be modified essentially independently from each other.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Double click the second sketch and modify the shape. The second pad should update immediately without causing topological problems with the third sketch and the third pad.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. In fact, every sketch can be modified without interfering with each other\'s pads. As long as the pads have sufficient extrusion length, so that they touch and form a contiguous solid, the entire body will be valid.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">



## Vantagens e desvantagens 

Adicionar objetos de datum é mais trabalhoso para o usuário, mas, em última análise, produz modelos mais estáveis que estão menos sujeitos ao problema de nomeação topológica.

Naturalmente, os objetos de referência podem ser criados antes de qualquer esboço ser desenhado e os blocos serem produzidos. Isso pode ser útil para visualizar a forma e as dimensões aproximadas do corpo final.

Datum planes can also be based on other datum planes. This creates a chain of dependencies that could also result in topological problems; however, since datum planes are very simple objects, the risks of having these issues is less than if the face of a solid object is used as support.

Datum objects, [points](PartDesign_Point.md), [lines](PartDesign_Line.md), [planes](PartDesign_Plane.md), and [coordinate systems](PartDesign_CoordinateSystem.md), may also be useful as reference geometry, that is, as visual aids to show the important features in the model, even if no sketch is directly attached to them.



## Algoritmo de nomeação topológica 


<div class="mw-translate-fuzzy">

O algoritmo de nomeação topológica do Realthunder, selecionado para reduzir o impacto desse problema, foi amplamente descrito como "consertando o problema de nomeação topológica", o que induziu involuntariamente muitos usuários a pensar que não será mais útil usar técnicas como datums, posicionamento explícito de esboços e [Edição de recursos](Feature_editing#Advice_for_creating_stable_models.md) para tornar os modelos mais estáveis. O algoritmo não se destina a corrigir todas as falhas introduzidas pela ambiguidade de nomes topológicos. Em vez disso, ele tem três objetivos.


</div>

1.  O primeiro e mais importante objetivo é, sempre que possível, **identificar** referências quebradas de alterações topológicas e exibir um erro para o usuário. Em vez de ter de trabalhar em uma série de operações para encontrar a primeira operação que diverge da intenção do projeto, a operação que altera os nomes normalmente será sinalizada com um erro, o que facilita muito a correção manual de problemas de modelo introduzidos por alterações em operações ou parâmetros.
2.  Às vezes, o FreeCAD poderá identificar uma "provável" correção para uma referência quebrada, de modo que, quando o usuário estiver corrigindo manualmente a referência quebrada sinalizada, um candidato será apresentado para que ele aceite ou altere. Um exemplo comum disso são as operações de acabamento, como filetes e chanfros, em que o usuário pode ter de editar a operação e aceitar a seleção do recurso de substituição proposto ou alterá-lo para corrigi-lo.
3.  Em alguns casos, o FreeCAD poderá resolver **automaticamente** a referência quebrada, pois há informações suficientes sobre a referência armazenadas para que se tenha alta confiança de que a substituição está correta. Por exemplo, ao esboçar diretamente em uma face, o algoritmo frequentemente (mas nem sempre) reparará corretamente a referência à face quando a geometria subjacente for alterada parametricamente. (Ao alterar a estrutura, por exemplo, adicionando ou excluindo operações no meio de um corpo de desenho de peça, esse tipo de reparo automático será menos provável). No entanto, o FreeCAD fará isso somente com alta confiança na exatidão do reparo, pois um reparo automático incorreto pode reintroduzir o problema de ter de procurar onde o problema foi introduzido para reparar um modelo após uma modificação. "Primeiro, não cause danos".


<div class="mw-translate-fuzzy">

A meta para o FreeCAD 1.0 é que a implementação desse algoritmo na versão oficial do FreeCAD tenha atingido a paridade de recursos com a bifurcação "Linkstage 3" de Realthunder, onde ele originalmente desenvolveu o algoritmo, no momento em que o trabalho de integração foi iniciado. Há novos recursos do FreeCAD que poderiam usar o algoritmo, mas ainda não o fazem, e sempre haverá mais oportunidades de adicionar correções candidatas e reparos automáticos. O trabalho inicial forneceu uma "estrutura" a ser usada para esses aprimoramentos adicionais ao longo do tempo, tanto no FreeCAD principal quanto nos Addons.


</div>

## Links

-   [PartDesign Fillet - Topological naming](PartDesign_Fillet#Topological_naming.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278): a possible solution, by realthunder.
-   [Topological Naming Project](Topological_Naming_Project.md): idea to solve the problem, by ickby.
-   [Topological data scripting](Topological_data_scripting.md)
-   [Feature editing](Feature_editing.md): contains alternate advice for stable modelling techniques.
-   [Clarifying and expanding \"Topological Naming Problem\" documentation](https://forum.freecad.org/viewtopic.php?p=770360): Clarifying expectations for Realthunder\'s topological naming algorithm selected for FreeCAD 1.0.



## Vídeos

-   [Why do my FreeCAD models break? - \"Topological Naming Problem\"](https://youtu.be/6p2vqEEmWq4): A Video explanation of the underlying issues of [Topological naming problem](Topological_naming_problem.md)
-   [FreeCAD Is Fundamentally Broken! - Now what\... Help Me Decide\...](https://www.youtube.com/watch?v=QSsVFu929jo): A Maker Tales Video


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common%20Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/pt-br
