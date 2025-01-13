---
 GuiCommand:  
   Name: Part SectionCut  
   MenuLocation: Exibir , Corte Seccional Persistente  
   Workbenches: Todas  
   Version: 0.20  
   SeeAlso: Std_ToggleClipPlane/pt-br  
---

# Part SectionCut/pt-br



## Descrição

A funcionalidade **Corte Seccional** está disponível para todas as bancadas, mas funciona apenas para objetos do Part e PartDesign e montagens desses tipos. Ela cria um corte persistente de objetos e montagens. Como o resultado do corte é um objeto <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [Corte de Peça](Part_Cut/pt-br.md) normal, ele pode ser modificado posteriormente ou, por exemplo, impresso em 3D. Veja abaixo possíveis aplicações.

<img alt="" src=images/Part_SectionCut_example.png  style="width:300px;"> 
*Uma montagem cortada. Algumas faces do corte foram coloridas manualmente. A peça amarela não foi cortada porque foi propositalmente movida um mícron para dentro de outra peça.*



## Utilização

![O diálogo de Corte Seccional.](images/Part_SectionCut_Dialog.png )

O diálogo **Corte Seccional** é aberto através do menu **Exibir → <img src="images/Part_SectionCut.svg" width=24px> Corte Seccional Persistente**. Ele é independente da bancada atual e do documento atualmente aberto. Pode ser destacado de sua posição inicial pressionando o botão no canto superior direito do diálogo.

A funcionalidade **Corte Seccional** considera todos os objetos Part atualmente visíveis no documento ativo. Portanto, é possível controlar o que será cortado tornando uma peça visível ou invisível. Ao selecionar uma das opções de **Corte** no diálogo, a funcionalidade é ativada. Você pode então inserir uma posição (em coordenadas do documento) ou usar os deslizadores para definir a posição do corte. Também é possível combinar cortes, por exemplo, para cortar nas direções X e Z. Os botões **Inverter** alternam o lado que será cortado.

Assim que uma opção de **Corte** é selecionada no diálogo, um objeto de corte aparece na [visualização de árvore](Tree_view/pt-br.md). O nome dele é, por exemplo, *SectionCutY* quando o corte é na direção Y.

A opção do diálogo **Manter apenas os cortes visíveis ao fechar** oculta tudo na visualização de árvore, exceto o objeto de corte, quando o botão **Fechar** é clicado para fechar o diálogo.

Para remover o objeto de corte, desmarque todas as opções de **Corte**.

Ao desmarcar todas as opções de **Corte**, o botão **Atualizar visualização** se torna ativo. Quando pressionado, ele captura uma espécie de \"imagem\" dos objetos Part atualmente visíveis. Isso será usado quando você selecionar novamente uma opção de **Corte**. A atualização é necessária quando você troca de documento. Ela também é útil para montagens, onde você pode querer ocultar algumas peças ou adicioná-las posteriormente ao corte. Nesse caso, a atualização recalcula os valores mínimo/máximo dos deslizadores e as posições de corte de acordo com as dimensões dos objetos atualmente visíveis.

Se a opção **Automático** na seção de faces de corte estiver marcada, a cor e a transparência dos objetos cortados serão aplicadas à face do corte. Isso só funciona se todos os objetos cortados tiverem a mesma cor ou transparência.

A opção **Cortar objetos que se intersectam** permite cortar também objetos que se intersectam entre si. Em montagens, as interseções podem ocorrer às vezes com objetos que foram projetados para apenas tocar-se, devido a problemas de precisão numérica. A desvantagem dessa opção é que todos os objetos visíveis receberão a mesma cor. Essa cor pode ser especificada como na seção de faces de corte do diálogo. Se você precisar do corte, por exemplo, para uma boa imagem com várias cores de face, pode alterar as cores das faces usando a ferramenta <img alt="" src=images/Part_ColorPerFace.svg  style="width:24px;"> [Cor por face](Part_ColorPerFace/pt-br.md).

**Nota:** Para montagens, os deslizadores no diálogo são desativados (exceto o para a transparência). A razão é que o movimento de um deslizante resulta em várias operações de corte em um curto espaço de tempo. Para montagens, isso rapidamente consome toda a potência da CPU, e um movimento de deslizante instável não é útil.

Quando você seleciona um objeto de corte na visualização de árvore e, em seguida, abre o diálogo de Corte Seccional, as posições do corte serão lidas para o diálogo.



￼

## Aplicações

-   Um caso de uso importante é que o Corte Seccional cria cortes preenchidos, não vazios, como a funcionalidade <img alt="" src=images/Std_ToggleClipPlane.svg  style="width:24px;"> [Plano de Corte](Std_ToggleClipPlane/pt-br.md).
-   O Corte Seccional é útil para montagens, por exemplo, para visualizar o princípio de funcionamento de um dispositivo. Você pode querer colorir certas faces de corte usando a ferramenta <img alt="" src=images/Part_ColorPerFace.svg  style="width:24px;"> [Cor por face](Part_ColorPerFace/pt-br.md). Para usar a ferramenta, alterne para a bancada Part ou PartDesign, clique com o botão direito no objeto de corte na visualização de árvore e selecione no menu de contexto **Definir cores**.
-   Sem a opção **Cortar objetos que se intersectam**, apenas as peças que não se intersectam com outras serão cortadas. Isso pode ser usado como um teste de colisão.
-   A funcionalidade Corte Seccional pode ser usada para desenhos técnicos, a fim de destacar certas áreas ou para permitir a inclusão de dimensões. A imagem abaixo mostra um exemplo onde as funcionalidades [TechDraw](TechDraw_Workbench/pt-br.md) <img alt="" src=images/TechDraw_ActiveView.svg  style="width:24px;"> [Vista Ativa](TechDraw_ActiveView/pt-br.md) e <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Vista](TechDraw_View/pt-br.md) são usadas.

<img alt="" src=images/Part_SectionCut_TD-example.png  style="width:400px;"> 
*Um desenho técnico onde o resultado de um Corte Seccional é utilizado. (Clique na imagem para visualizar em tamanho completo.)*



## Posições de corte especiais 

<img alt="Um corte inclinado de uma montagem." src=images/Part_SectionCut_slant-cut.png  style="width:200px;">

-   Por exemplo, na primeira imagem desta página, apenas um quarto da montagem é cortado. Isso foi feito criando um corte na direção X. Em seguida, no objeto de corte resultante **SectionCutX**, o [posicionamento](Placement/pt-br.md) do subobjeto **SectionCutBoxX** foi alterado.
-   Para obter um corte em qualquer direção, você pode fazer o seguinte:

1.  Crie um novo contêiner [Std Parte](Std_Part/pt-br.md).
2.  Selecione todos os objetos que deseja cortar na visualização de árvore e mova-os para o contêiner.
3.  Agora, defina o posicionamento do contêiner para uma rotação de sua escolha. Para a imagem à esquerda, o contêiner foi rotacionado em 45° ao redor dos eixos X e Z, e o corte seccional foi realizado na direção X.






## Limitações

<img alt="Uma montagem onde duas peças se intersectam e, portanto, não são cortadas. Observe os artefatos de cor na face do corte." src=images/Part_SectionCut_Color-artifact.png  style="width:200px;">

-   **Importante:** A funcionalidade Corte Seccional funciona de forma inadequada com [OpenCASCADE](OpenCASCADE/pt-br.md) 7.4 e versões anteriores devido a erros. Portanto, é recomendável usar o OpenCASCADE 7.5 ou versões mais recentes (todas as versões do FreeCAD <small>(v0.20)</small>  garantem isso).

-    <small>(v1.0)</small> : A opção **Cortar objetos que se intersectam** colorirá todas as peças visíveis da mesma forma. Isso tecnicamente não pode ser evitado. No entanto, se for necessário o corte persistente para, por exemplo, uma apresentação, veja o método descrito acima sobre como redefinir a cor manualmente.

-    {{VersionMinus/pt-br|0.20}}: Em montagens, **peças que se intersectam não podem ser cortadas**. Normalmente, objetos que se intersectam não serão cortados enquanto os outros serão. No entanto, às vezes o corte pode produzir resultados estranhos, o que é um erro nas bibliotecas do OpenCASCADE. Para obter uma visualização de corte também para objetos que se intersectam, você pode usar a macro [Corte Seccional](Macro_cross_section/pt-br.md).

-    {{VersionMinus|0.20}}: Especialmente ao usar a [bancada A2plus](A2plus_Workbench/pt-br.md), algumas peças montadas podem se sobrepor por apenas um micron devido a erros internos de arredondamento. Para corrigir isso, adicione um micron de espaço nas configurações de restrição.

-   Podem ocorrer artefatos de cor no resultado do corte. Se e como isso ocorre depende da biblioteca OpenCASCADE e também da posição da visualização. Em muitos casos, os artefatos de cor desaparecem quando a visualização 3D é ligeiramente rotacionada.

-   Quando se tem objetos cortados com cores diferentes, não é possível aplicar automaticamente a cor desses objetos nas faces de corte correspondentes. Todas as faces de corte terão a mesma cor selecionada no diálogo.

-   Ao usar a [bancada A2plus](A2plus_Workbench/pt-br.md), não é possível aplicar automaticamente a cor das peças montadas nas faces de corte correspondentes. Todas as faces de corte terão a mesma cor selecionada no diálogo. O motivo é que o A2plus não insere as peças [como link](App_Link/pt-br.md), mas as carrega como arquivo.






## Informações de Fundo 

**Corte Seccional** é inspirado pela macro [Corte Seccional](Macro_cross_section/pt-br.md) e funciona tecnicamente da seguinte maneira:

Todos os objetos visíveis são colocados em um contêiner <img alt="" src=images/Part_Compound.svg  style="width:24px;"> [Part Compound](Part_Compound/pt-br.md). Para a opção **Cortar objetos que se intersectam**, é utilizado um contêiner <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragmentos Booleanos](Part_BooleanFragments/pt-br.md). O composto é cortado usando um objeto <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Box](Part_Box/pt-br.md). A caixa deve ser grande o suficiente para cobrir todo o volume de todos os objetos visíveis. Para conseguir isso, a caixa delimitadora dos objetos é adquirida. Ao mudar a visualização, adicionando/removendo objetos ou alterando o documento, a caixa delimitadora precisa ser atualizada. Isso é feito quando o botão **Atualizar visualização** é clicado.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SectionCut/pt-br
