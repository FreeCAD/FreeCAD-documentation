# Property editor/pt-br
{{TOCright}}



## Introdução

O [editor de propriedades](property_editor/pt-br.md) aparece quando a guia **Model** da [visão combinada](combo_view/pt-br.md) está ativa na [interface](interface/pt-br.md); ele permite gerenciar as propriedades publicamente expostas dos objetos de documento.

Geralmente, o editor de propriedade é destinado a lidar com apenas um objeto de cada vez. Os valores mostrados no editor de propriedade pertencem ao objeto selecionado do documento ativo. Apesar disso, algumas propriedades como cores, podem ser definidas para vários objetos selecionados. Se não houver elementos selecionados, o editor de propriedades estará vazio.

Nem todas as propriedades podem ser modificadas sempre; dependendo do status específico da propriedade, algumas delas serão invisíveis (não listadas), ou somente leitura (não editáveis).


{{TOCright}}

![](images/FreeCAD_Property_editor_empty.png )



*Editor de propriedade vazia, quando nenhum objeto é selecionado.*



## Tipos de propriedade 

Uma propriedade é uma informação como um número ou uma cadeia de texto que é anexada a um documento FreeCAD ou a um objeto no documento.

Objetos personalizados [objetos com scripts](scripted_objects/pt-br.md) podem usar qualquer um dos tipos de propriedade definidos no sistema base. Veja a lista completa em [Propriedade](Property/pt-br.md).

Alguns dos tipos de propriedade mais comumente utilizados são:


```python
App::PropertyBool
App::PropertyFloat
App::PropertyAngle
App::PropertyDistance
App::PropertyInteger
App::PropertyString
App::PropertyMatrix
App::PropertyVector
App::PropertyPlacement
```

Objetos diferentes podem ter diferentes tipos de propriedade. No entanto, muitos objetos têm os mesmos tipos porque são derivados da mesma classe interna. Por exemplo, a maioria dos objetos que descrevem formas geométricas (linhas, círculos, retângulos, sólidos, peças importadas, etc.) tem a propriedade \"Colocação\" que define sua posição na [Vista 3D](3D_view/pt-br.md).



## Propriedades de visualização e dados 

Há duas classes de propriedades funcionais acessíveis através de abas no editor de propriedades:

-   Propriedades da **Vista** as propriedades relacionadas à aparência \"visual\" do objeto. As propriedades de visualização estão ligadas ao atributo **ViewProvider**(`ViewObject`) do objeto e só são acessíveis quando a interface gráfica do usuário (GUI) é carregada. Eles não são acessíveis quando se usa o FreeCAD no modo de console ou como biblioteca sem cabeça.
-   Propriedades dos **dados** relativos aos parâmetros \"físicos\" do objeto. As propriedades dos **dados**definem as características essenciais do objeto; elas sempre existem, mesmo quando o FreeCAD é usado no modo console ou como uma biblioteca. Isto significa que se você carregar um documento em modo console, você pode alterar o raio de um círculo ou o comprimento de uma linha, mesmo que não consiga ver o resultado na tela.

Por esta razão, as propriedades dos **dados** são consideradas mais \"importantes\", uma vez que, na verdade, definem a geometria de uma forma. Por outro lado, as propriedades de **Vista** são menos importantes porque afetam apenas a aparência da superfície da geometria. Por exemplo, um círculo com um raio de 10 mm é diferente de um círculo com um raio de 5 mm; a cor dos círculos (propriedade da aparência) não afeta sua forma, mas o raio (propriedade de dados). Em muitos casos, nesta documentação, a palavra \"Propriedade\" se refere a uma \"propriedade de dados\", não a uma \"propriedade de aparência\".



### Propriedades básicas 


**Veja também: [Nome do objeto](Object_name/pt-br.md)**

O mais básico [script de objeto](scripted_objects/pt-br.md) não exibe nenhuma propriedade de **Dados** no editor de propriedade, exceto por seu atributo `Label`. O `Rótulo` é uma cadeia editável pelo usuário que identifica o objeto na [vista em árvore](tree_view.md). Por outro lado, o `Nome` de um objeto é um atributo interno que é atribuído ao objeto no momento de sua criação. Este atributo é somente de leitura, portanto não pode ser modificado, nem é exibido no editor de propriedade.

Um objeto paramétrico básico é criado da seguinte forma


```python
obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width:" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width:" height="264px;">



*Aba Vista e Dados do editor de propriedade, para um objeto básico "App::FeaturePython" com script.*

A maioria dos objetos geométricos que podem ser criados e exibidos em [Vista 3D](3D_view/pt-br.md) são derivados de uma `Parte::Característica`. Veja a [Característica Part](Part_Feature/pt-br.md) para conhecer as propriedades mais básicas desses objetos.

Para a geometria 2D, a maioria dos objetos são derivados de `Part::Part2DObject` (ela mesma derivada de `Part::Feature`) sendo a base dos [Sketche](Sketch/pt-br.md), e elementos do [Draft](Draft_Workbench/pt-br.md). Veja a [Part Part2DObject](Part_Part2DObject/pt-br.md) para as propriedades mais básicas destes objetos.



## Ações

Clicar com o botão direito do mouse em um espaço vazio na vista ou com uma propriedade selecionada mostra apenas um comando:

-    **Mostrar todos:**se ativo, além das propriedades padrão que já aparecem, mostra todos os dados ocultos e exibe as propriedades nas respectivas abas.

    -   Dados:\"Proxy\", \"Label2\", \"Expression Engine\", e \"Visibility\".
    -   Vista:\"Proxy\".

Quando a opção **Mostrar todas** está ativa, e uma propriedade é selecionada, mais ações estão disponíveis com um segundo clique do botão direito:

-    **Mostrar todas**: desabilita o comando **Mostrar todas**, escondendo assim os dados adicionais e as propriedades de exibição.

-    **Adicionar propriedade**: Isto funciona tanto com objetos definidos em C++, quanto com [scripts de objetos](scripted_objects/pt-br.md) escritos em Python.

-    **Expressão...**:chama o editor de fórmula, que permite o uso de [expressões](Expressions.md) no valor da propriedade.

-    **Hidden**: se ativo, define a propriedade como oculta, o que significa que ela só será exibida no editor da propriedade se **Mostrar todas** está ativo.

-    **Output**: se ativo, define a propriedade como uma saída.

-    **NoRecompute**: se ativo, define a propriedade como não recalculada quando o documento é recalculado; isto é útil quando uma propriedade não deve ser afetada por outras atualizações.

-    **ReadOnly**:se ativo, define a propriedade para somente leitura. Não será mais editável no editor da propriedade até que esta configuração seja desativada. A entrada do menu **Expressão...** não está mais disponível. Nota: Ainda pode ser possível alterar o imóvel através de um diálogo que atualize o imóvel.

-    **Transient**:se ativo, define a propriedade como transitória. O valor de uma propriedade transitória não é armazenado em um arquivo. Quando um arquivo é aberto, ele é instanciado com seu valor padrão.

-    **Touched**:se estiver ativo, ele é atingido e está pronto para ser recalculado.

-    **EvalOnRestore**: se estiver ativo, ele é avaliado quando o documento é restaurado.



## Exemplo de propriedades de um objeto PartDesign 

Nesta seção mostramos algumas propriedades comuns visíveis para um [Corpo PartDesign](PartDesign_Body/pt-br.md) e uma [Função PartDesign](PartDesign_Feature/pt-br.md). As propriedades específicas de um objeto podem ser encontradas na página de documentação específica para esse objeto.



### Vista

A maioria dessas propriedades são herdadas do objeto básico [Part Feature](Part_Feature/pt-br.md).


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_Property_editor_View.png  style="width:490px;"> {{TitleProperty|Base}}


</div>


{{TitleProperty|Base}}

-    **Angular Deflection**:Esta é outra maneira de especificar a finura de geração da malha para renderização em tela ou exportação. O valor padrão é 28,5 graus, ou 0,5 radianos. Quanto menor o valor, mais suave será a aparência na [Vista 3D](3D_view/pt-br.md), e mais fina será a malha exportada.

-    **Bounding Box**: indica se uma caixa mostrando a extensão global do objeto é exibida.

-    **Deviation**: define a precisão da representação poligonal do modelo na [vista 3D](3D_view/pt-br.md) (tesselação). Valores mais baixos indicam melhor qualidade. O valor está em porcentagem do tamanho do objeto.

-    **Display Mode**: modo de exibição de corpo inteiro,{{Value|Flat lines}} (padrão), {{Value|Shaded}}, {{Value|Wireframe}}, {{Value|Points}}.

-    **Display Mode Body**:modo de exibição da ponta do corpo, {{Value|Through}} (padrão), {{Value|Tip}}.

-    **Draw Style**: {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dotted}}, {{Value|Dashdot}}; define o estilo das bordas na [vista 3D](3D_view/pt-br.md).

-    **Lighting**: {{Value|One side}}, {{Value|Two side}} (padrão).

-    **Line Color**: cor RGB das bordas, é por padrão {{value|(25, 25, 25)}}.

-    **Line Width**: a espessura das bordas, é por padrão {{value|2}} pixels.

-    **On Top When Selected**: {{value|Disabled}}, {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Point Color**: a cor RGB dos vértices, por padrão {{value|(25, 25, 25)}}.

-    **Point Size**: o tamanho dos vértices, é por padrão {{value|2}} pixels.

-    **Selectable**:se o objeto é selecionável ou não.

-    **Selection Style**: {{value|Shape}}, {{value|BoundBox}}.

-    **Shape Color**: a cor RGB da forma, é por padrão {{value|(204, 204, 204)}}.

-    **Show In Tree**: se estiver definido para `True`, to objeto aparece na estrutura em árvore. Caso contrário, é definido como invisível.

-    **Transparency**: o grau de transparência de {{value|0}} (padrão) a {{value|100}}.

-    **Visibility**: se o objeto esta visível na [vista 3D](3D_view/pt-br.md) ou não. Alternar com o **Space** no teclado.









### Data

Neste caso, observamos as propriedades da função [Revolução PartDesign](PartDesign_Revolution/pt-br.md).


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:490px;"> {{TitleProperty|Base}}


</div>


{{TitleProperty|Base}}

-    **Label**: o nome definido pelo usuário dado ao objeto, isto pode ser alterado conforme desejado.


{{TitleProperty|Part Design}}

-    **Refine**: se a fusão feita com outros objetos deve ser refinada.


{{TitleProperty|Revolution}}

-    **Base**: o ponto no espaço que especifica onde ocorre a revolução. Ela não pode ser modificada diretamente, somente quando se edita o recurso.

-    **Axis**: o eixo em torno do qual a revolução será realizada. Ele não pode ser modificado diretamente, somente quando se edita o recurso.

-    **Angle**: o ângulo que especifica quanto do elemento base é girado. Por padrão é {{value|360°}}, mas pode ser qualquer fração disso.


{{TitleProperty|Sketch Based}}

-    **Midplane**:se o objeto base for um [Sketch](Sketch/pt-br.md), quando esta propriedade for `True`, ela fará a revolução com o esboço servindo como o plano de simetria. Isto é visível se o **Angle** diferir de {{value|360°}}.

-    **Reversed**: por padrão é `True`. Seja para realizar a revolução em uma direção ou em outra.




## Scripting


**Veja também:**

[FreeCAD Noções básicas Script](FreeCAD_Scripting_Basics/pt-br.md).

Consulte a página de [objetos com scripts](scripted_objects/pt-br.md) para obter informações completas sobre como adicionar propriedades a objetos definidos através de um script [Python](Python.md).

A maioria das propriedades visíveis no editor de propriedades são acessíveis a partir do [console Python](Python_console.md). Geralmente estas propriedades são apenas atributos da classe que define o objeto selecionado. Por exemplo, se o editor de propriedade exibir a propriedade **Group**, isso significa que o objeto tem o atributo `Group`.


```python
print(obj.Group)
```

Estes atributos (propriedades) são adicionados com o método `addProperty` do objeto base. Como mínimo, é necessário especificar o tipo de [propriedade](property/pt-br.md) e seu nome.


```python
obj.addProperty("App::PropertyFloat", "Custom")
print(obj.Custom)
```

As propriedades seguem a convenção `CapitalCamelCase` ou `PascalCase`, o que significa que cada palavra começa com uma letra maiúscula e não há nenhum sublinhado. Quando o editor de propriedade exibe estes nomes, ele deixa um espaço entre cada letra maiúscula, facilitando a leitura.


```python
obj.addProperty("App::PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Editor de propriedade mostrando as propriedades de dados de um  [PartDesign Body](PartDesign_Body/pt-br.md), com duas propriedades adicionais, "Custom" e "Custom Camel Property".*

Da mesma forma, as propriedades **View**são adicionadas, não ao objeto base, mas ao seu `ViewObject`.Então, segue-se que propriedades como **Angular Deflection**, **Bounding Box**, **Display Mode**, **Display Mode Body**, **Line Color**, e outros, podem ser examinados e alterados a partir no [console Python](Python_console/pt-br.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

Todas as propriedades públicas do objeto e seu provedor de visão estão contidas no atributo `PropertiesList` correspondente.


```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```





{{Interface navi

}} {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Property editor/pt-br
