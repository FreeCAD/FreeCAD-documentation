# <img alt="ícone da bancada de trabalho Spreadsheet" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/pt-br

## Introdução

A <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [bancada de trabalho Spreadsheet](Spreadsheet_Workbench.md) permite criar e editar planilhas, usar dados da planilha como parâmetros em um modelo, preencher a planilha com dados recuperados de um modelo, realizar cálculos e exportar os dados para outras aplicações de planilhas como o LibreOffice ou o Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Uma planilha com determinadas células preenchidas com texto e quantidades*

## Ferramentas

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Criar planilha](Spreadsheet_CreateSheet/pt-br.md): criar uma nova planilha de cálculo.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Import](Spreadsheet_Import.md): import a CSV file into a spreadsheet.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Export](Spreadsheet_Export.md): export a CSV file from a spreadsheet.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Merge cells](Spreadsheet_MergeCells.md): merge selected cells.

-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Split cell](Spreadsheet_SplitCell.md): split previously merged cells.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Align left](Spreadsheet_AlignLeft.md): align the contents of selected cells to the left.

-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Align center](Spreadsheet_AlignCenter.md): align the contents of selected cells to the center horizontally.

-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Align right](Spreadsheet_AlignRight.md): align the contents of selected cells to the right.

-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Align top](Spreadsheet_AlignTop.md): align the contents of selected cells to the top.

-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Align vertical center](Spreadsheet_AlignVCenter.md): align the contents of selected cells to the center vertically.

-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Align bottom](Spreadsheet_AlignBottom.md): top align the contents of selected cells to the bottom.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Style bold](Spreadsheet_StyleBold.md): set the contents of selected cells to bold.

-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Style italic](Spreadsheet_StyleItalic.md): set the contents of selected cells to italic.

-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Style underline](Spreadsheet_StyleUnderline.md): set the contents of selected cells to underlined.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Definir pseudônimo](Spreadsheet_SetAlias/pt-br.md): definir alias para células selecionadas.


</div>


<div class="mw-translate-fuzzy">

-    **Preto**e **Branco** definir o primeiro plano e as cores de fundo das células selecionadas.


</div>

## Preferences

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width:32px;"> [Preferences](Spreadsheet_Preferences.md): the preferences for the Spreadsheet Workbench. <small>(v0.20)</small> 

## Insert and remove rows and columns 

Rows and columns can be inserted or removed by right-clicking a row or column header and selecting the appropriate option from the contex menu. It is possible to select multiple rows or columns first. Either by holding down the **Ctrl** key while selecting the headers, or by holding down the left mouse button and dragging.

In FreeCAD version 0.19 and earlier rows are inserted above the selected rows, and columns on the left of the selected columns. In FreeCAD version 0.20 you can specify the insertion side.

Note that removing rows or columns with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

## Cut and copy-paste cells 

Cut and copy-paste operations can be used on cells in FreeCAD spreadsheets. You can use the normal shortcuts for these operations: **Ctrl**+**X**, **Ctrl**+**C** and **Ctrl**+**V** respectively. To select multiple cells hold down the **Ctrl** key while selecting, or hold down the left mouse button and drag to select a rectangular cell range.

The cut and copy operations store the contents and properties of the cells on the Clipboard. The paste operation writes the data in such a way that the content of the top left cell of the stored data is dropped in the active cell. Other stored content is placed relative to that cell. Formulas are updated accordingly.

Note that removing cells with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

In FreeCAD version 0.19 and earlier there is a bug that can cause FreeCAD to hang if a non-rectangular cell range is pasted. It is advisable to save your work before performing any paste operations.

## Propriedades celulares 


<div class="mw-translate-fuzzy">

As propriedades de uma célula de planilha podem ser editadas com um clique com o botão direito do mouse sobre uma célula. As seguintes propriedades o diálogo aparece:


</div>

![](images/SpreadsheetCellPropDialog.png )

Conforme indicado pelas abas, as seguintes propriedades podem ser alteradas:


<div class="mw-translate-fuzzy">

-   Cor: Cor do texto e cor de fundo
-   Alinhamento: Alinhamento horizontal e vertical do texto
-   Estilo: Estilo do texto: negrito, itálico, sublinhado
-   Unidades: Unidades de exibição para esta célula. Por favor, leia a seção abaixo [Unidades](#Unidades.md).
-   Pseudônimo: Defina um [pseudônimo](Spreadsheet_SetAlias/pt-br.md) para esta célula. Este apelido pode ser usado em fórmulas celulares e também em [expressões](Expressions/pt-br.md) gerais; veja a seção [Dados da planilha em expressões](#Dados_da_planilha_em_expressões.md) para mais informações.


</div>

## Expressões celulares 


<div class="mw-translate-fuzzy">

Uma célula de planilha pode conter um texto ou uma expressão arbitrária. Tecnicamente, as expressões devem começar com um sinal igual a \'=\'. Entretanto, a planilha tenta ser inteligente; se você digitar o que parece ser uma expressão sem o sinal \'=\' principal, uma será adicionada automaticamente.


</div>


<div class="mw-translate-fuzzy">

As expressões celulares podem conter números, funções, referências a outras células e referências a propriedades do modelo (Mas veja [Limitações atuais](#Limitações_atuais.md) abaixo). As células são referenciadas por sua coluna (letra CAPITULAR) e linha (número). Uma célula também pode ser referenciada por sua [pseudônimo](#alias_name.md)(abaixo).Exemplo: B4 + A6


</div>


<div class="mw-translate-fuzzy">

Nota: As expressões celulares são tratadas pelo FreeCAD como código de programação. Portanto, quando você edita uma célula, o conteúdo que você vê não está seguindo suas configurações de visualização:

-   o separador decimal é sempre um ponto
-   o número de decimais exibidos pode diferir do seu [configurações de preferências](Preferences_Editor/pt-br#Unidades.md)


</div>

As referências a objetos no modelo são explicadas em [Referências a dados CAD](#References_to_CAD-data.md) abaixo. A utilização dos valores das células da planilha para definir as propriedades do modelo é explicada em [Dados da planilha em expressões](#Spreadsheet_data_in_expressions.md) abaixo. Para mais informações sobre as expressões e as funções disponíveis, veja [Expressões](Expressions/pt-br.md).

## Interação entre as planilhas e o modelo CAD 

Os dados nas células de uma planilha podem ser usados nas expressões de parâmetros do modelo CAD. Assim, uma planilha pode ser usada como fonte para valores de parâmetros utilizados em todo o modelo, reunindo efetivamente os valores em um só lugar. Quando os valores são alterados na planilha, eles são propagados ao longo do modelo.

Da mesma forma, as propriedades dos objetos do modelo CAD podem ser usadas em expressões em células de planilhas. Isto permite o uso de propriedades de objetos como volume ou área na planilha eletrônica. Se o nome de um objeto no modelo CAD for alterado, a alteração será automaticamente propagada para quaisquer referências nas expressões da planilha usando o nome que foi alterado.

Mais de uma planilha de cálculo pode ser usada em um documento. Uma planilha pode ser identificada usando seu nome ou sua etiqueta.


<div class="mw-translate-fuzzy">

O FreeCAD atribuirá automaticamente um nome exclusivo a uma planilha de cálculo quando ela for criada. Estes nomes seguem o padrão `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` e assim por diante. O nome não pode ser alterado manualmente, e não é visível nas propriedades da planilha. Ele pode ser usado para se referir à planilha em uma [Expressão](Expressions/pt-br.md) (ver [Dados da planilha em expressões](#Dados_da_planilha_em_expressões.md) abaixo.)


</div>


<div class="mw-translate-fuzzy">

O rótulo de uma planilha é automaticamente definido com o nome da planilha no momento da criação. Ao contrário do nome, a etiqueta pode ser alterada, por exemplo, no painel de propriedades ou usando a ação do menu de contexto Renomear. Note que a etiqueta de uma planilha dentro de um documento tem que ser única; se você tentar mudar a etiqueta para uma etiqueta já usada por outra planilha, o FreeCAD não aceitará a nova etiqueta.


</div>


<div class="mw-translate-fuzzy">

Verificações FreeCAD para dependências cíclicas. Ver [Limitações atuais](#Limitações_atuais.md).


</div>

### Referências a dados CAD 

Como indicado acima, é possível consultar os dados do modelo CAD em expressões de planilhas.


<div class="mw-translate-fuzzy">

A tabela a seguir mostra alguns exemplos assumindo que o modelo tem uma característica chamada \"MyCube\":

  Dados CAD                                                           Célula em Planilha             Resultado
    
  Comprimento paramétrico de um cubo de bancada de trabalho parcial   =MyCube.Length                 Comprimento com unidades mm
  Volume do Cubo                                                      =MyCube.Shape.Volume           Volume em mm³ sem unidades
  Tipo da forma do cubo                                               =MyCube.Shape.ShapeType        String: Solid
  Rótulo do Cubo                                                      =MyCube.Label                  String: MyCube
  x-coordenada do centro de massa do Cubo                             =MyCube.Shape.CenterOfMass.x   x-coordenada em mm sem unidades


</div>

### Dados da planilha em expressões 


<div class="mw-translate-fuzzy">

Para usar os dados da planilha em outras partes do FreeCAD, você geralmente criará uma [Expressão](Expressions.md) que se refere à planilha e à célula que contém os dados que você deseja usar. Você pode identificar as planilhas por nome ou por etiqueta, e pode identificar as células por posição ou por pseudônimo. O auto-completamento está disponível para todas as formas de referência.


</div>


<div class="mw-translate-fuzzy">

++++
|                       | Planilha por nome                                   | Planilha por Rótulo                                    |
+=======================+=====================================================+========================================================+
| Célula por Posição    |                                      |                                         |
|                       | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                       |                                                  |                                                     |
++++
| Célula por Pseudónimo |                                      |                                         |
|                       | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                       |                                                  |                                                     |
++++


</div>


<div class="mw-translate-fuzzy">


<div class="mw-collapsible mw-collapsed">

A maneira recomendada de consultar os dados da planilha é usar a etiqueta da planilha e o nome da célula. Para uma explicação mais profunda dos prós e contras dos modos de endereçamento, veja a seção expandida abaixo.


<div class="mw-collapsible-content">


</div>

O uso do rótulo da planilha tem a vantagem de poder ser livremente alterado para descrever o conteúdo da planilha. Também é mais fácil identificar a planilha que está sendo utilizada, já que o texto na expressão corresponde à etiqueta mostrada na visualização do modelo e das propriedades. Se você decidir mudar o rótulo de uma planilha, as referências existentes ao conteúdo da planilha serão atualizadas, para que você não quebre suas expressões ao renomear a planilha. O nome interno da planilha não está prontamente disponível em nenhum lugar, exceto dentro do editor de expressões, portanto, se você usar o nome interno e mais tarde decidir renomear as planilhas, você poderá ter dificuldade em rastrear seus dados de expressão de volta à sua fonte.

Esteja ciente de que quando você cria uma nova planilha, o nome e a etiqueta são os mesmos, por isso é fácil usar acidentalmente o nome da planilha em vez da etiqueta. Uma maneira simples de evitar isto é dar à planilha um nome significativo antes de começar a usá-la em expressões.

While you may use the row and column number in an expression to reference a cell, best practice is to give the cell an alias name and use that. See [Cell properties](#Cell_properties.md) on how to set the alias. For example, if the data in cell B1 contained the length parameter for an object, an alias name of `MyObject_Length` would allow the value to be referred to as `<<MyParams>>.MyObject_Length` instead of `Spreadsheet.B1`. Besides being much easier to read and understand, alias names are also much easier to change if you decide to adjust the structure of your spreadsheet. Using an alias also has the advantage that it is reasier to see which cells are used to control other parts of the document. Note that FreeCAD will automatically adjust the positional references in expressions if you insert or remove rows and columns in the spreadsheet, so even if you use row and column numbers in an expression, you can insert rows and columns without breaking the references to the surrounding cells.


</div>


</div>

### Modelos complexos e recompilações 

A edição de uma planilha irá desencadear uma recomputação do modelo 3D, mesmo que as mudanças não afetem o modelo. Para um modelo complexo, uma recomputação pode levar muito tempo, e ter que esperar após cada edição é, naturalmente, bastante irritante.


<div class="mw-translate-fuzzy">

Há três soluções para lidar com isso:

1.  Pular temporariamente as recomputas:
    -   Na [Vista em árvore](Tree_view/pt-br.md) clique com o botão direito do mouse sobre o <img alt="" src=images/Document.svg  style="width:24px;"> documento que contém a planilha de cálculo.
    -   Selecione a opção **Skip recomputes** no menu de contexto.
    -   Há uma grande desvantagem para esta solução. Os novos valores inseridos na planilha não serão exibidos até que o documento seja recalculado. Em vez disso `#PENDENTE` é mostrado.
    -   Você pode recalcular manualmente, usando o comando [Atualização](Std_Refresh.md), ou desabilitar a opção **Skip recomputes** quando você terminar de editar.
2.  Use uma macro para saltar automaticamente as recomputas durante a edição de uma planilha:
    -   Download e execução [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   Esta solução economiza alguns passos em relação à primeira solução, mas também tem a desvantagem mencionada.
3.  Colocar a planilha em um arquivo separado:
    -   Você pode consultar os dados de uma planilha de um arquivo externo com esta sintaxe: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   A vantagem de ter a planilha em outro arquivo sobre o desligamento de recomputas é que a própria planilha é recalculada.
    -   A desvantagem é que o modelo não será recalculado automaticamente após alterações na planilha.
    -   No cenário onde você primeiro abre o arquivo \'planilha\', altera um ou mais valores e depois abre o arquivo \'modelo\', não haverá nenhuma indicação de que o modelo precisa ser recalculado. Mas se ambos os arquivos estiverem abertos, o ícone [Atualização](Std_Refresh/pt-br.md) será atualizado corretamente para o arquivo \'modelo\' após as mudanças no arquivo \'planilha\'.


</div>

## Unidades

A Planilha tem uma noção de dimensão (unidades) associada aos valores das células. Um número inserido sem uma unidade associada não tem dimensão. A unidade deve ser inserida imediatamente após o valor do número, sem espaço interveniente. Se um número tiver uma unidade associada, essa unidade será usada em todos os cálculos. Por exemplo, a multiplicação de dois comprimentos com a unidade mm dá uma área com a unidade mm².

Se uma célula contém um valor que representa uma dimensão, ela deve ser inserida com sua unidade associada. Embora em muitos casos simples se possa sobreviver com um valor sem dimensão, é insensato não entrar com a unidade. Se um valor representando uma dimensão for inserido sem sua unidade associada, há algumas seqüências de operações que fazem com que o FreeCAD reclame de unidades incompatíveis em uma expressão quando ela aparece, a expressão deve ser válida. (Isto pode ser melhor compreendido visualizando [este tópico](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) nos fóruns do FreeCAD.)


<div class="mw-translate-fuzzy">

Você pode mudar as unidades exibidas para um valor de célula usando o diálogo de propriedades [guia de unidades](#units_tab.md). (acima). Isto não altera o valor contido na célula; ele apenas converte o valor existente para exibição. O valor utilizado para os cálculos não muda, e os resultados das fórmulas que utilizam o valor não mudam. Por exemplo, uma célula contendo o valor \"5,08cm\" pode ser exibida como \"2in\", alterando o valor da aba de unidades para \"in\".


</div>

Um número sem dimensão não pode ser alterado para um número com uma unidade pelo diálogo de propriedades da célula. Pode-se colocar uma cadeia de unidades, e essa cadeia será exibida; mas a célula ainda contém um número sem dimensões. Para mudar um valor sem dimensão para um valor com uma dimensão, o próprio valor deve ser reentrado com sua unidade associada.

Ocasionalmente, pode ser desejável se livrar de uma dimensão em uma expressão. Isto pode ser feito multiplicando por 1 com uma unidade recíproca.

## Importação e exportação 

### CSV format 


<div class="mw-translate-fuzzy">

As folhas podem ser importadas e exportadas para o formato [csv](https://en.wikipedia.org/wiki/Comma-separated_values) que também pode ser lido e escrito pela maioria das outras aplicações de planilhas como o Microsoft Excel ou o LibreOffice Calc. Ao importar arquivos para o FreeCAD, o delimitador (o caractere que é usado para separar colunas) deve ser o caracter TAB (que pode ser definido ao exportar de outras aplicações). A importação de um arquivo CSV está disponível a partir do menu **Planilha → Importar Planilha** ou clicando no ícone <img alt="" src=images/SpreadsheetImport.svg  style="width:24px;">. Esta função de importação não abre arquivos Excel ou qualquer outro formato de planilha eletrônica.


</div>

### XLSX format 


<div class="mw-translate-fuzzy">

Planilhas em formato Excel \"xlsx\" podem ser importadas através do menu **Arquivo → Import...**. As planilhas do Excel também podem ser abertas clicando no menu **Arquivo → Abrir...** ou clicando no ícone ou clicando no ícone <img alt="" src=images/Document-open.svg  style="width:24px;">. Nesses casos, é criado um novo documento com uma planilha dentro. As seguintes características são suportadas:


</div>


<div class="mw-translate-fuzzy">

-   todas as funções que também estão disponíveis na planilha do FreeCAD. Outras funções dão um erro na célula correspondente após a importação.
-   Nomes de células
-   Mais de uma \"Folha\" na planilha Excel-spreadsheet. Neste caso, uma planilha FreeCAD é criada para cada planilha do Excel.


</div>


<div class="mw-translate-fuzzy">

Outras funcionalidades não são importadas para a planilha do FreeCAD. O Excel-importado é o da <small>(v0.17)</small>  do FreeCAD


</div>

## Impressão

Para lidar com a configuração da página necessária para impressão, as planilhas do FreeCAD são impressas inserindo-as em [Visualizar planilha do TechDraw](TechDraw_SpreadsheetView/pt-br.md).

## Limitações atuais 


<div class="mw-translate-fuzzy">

Verificações FreeCAD para dependências cíclicas. Por projeto, essa verificação pára no nível do objeto da planilha. Como conseqüência, não se deve ter uma planilha que contenha tanto células cujos valores são usados para especificar parâmetros para o modelo, quanto células cujos valores usam a saída do modelo. Por exemplo, você não pode ter células especificando o comprimento, largura e altura de um objeto, e outra célula que faz referência ao volume total da forma resultante. Esta restrição pode ser superada com duas planilhas: uma usada como fonte de dados para parâmetros de entrada no modelo e a outra usada para cálculos baseados nos dados geométricos resultantes.


</div>

## Cell binding 


<small>(v0.20)</small> 

It is possible to bind the content of cells to other spreadsheet cells. This can be useful when dealing with large tables or to get cell content from another spreadsheet.

### Create binding 

To bind, for example, the cell range A3-C4 to the cell range B1-D2:

1.  Select the cell range A3-C4.
2.  Right-click and select **Bind...** from the context menu.
3.  The **Bind Spreadsheet Cells** dialog opens.
4.  Set the range B1-D2 for the **To cells**:
    ![](images/Spreadsheet_binding-dialog.png )
5.  Press **OK**.
6.  Bound cells have a blue border to highlight the binding.
7.  If you now enter something in cell C1, the same will immediately appear in cell B3.

![](images/Spreadsheet_binding-result.png ) 
*The spreadsheet may now look like this*

### Change binding 

1.  Right-click a bound cell (there is no need to highlight the whole bound range) and select **Bind...** from the context menu.
2.  The **Bind Spreadsheet Cells** dialog opens.
3.  Change one or more options. Note that the **Bind cells**, the bound cell range, cannot be changed.
4.  Press **OK**.

### Remove binding 

1.  Right-click a bound cell (there is no need to highlight the whole bound range) and select **Bind...** from the context menu.
2.  The **Bind Spreadsheet Cells** dialog opens.
3.  Press **Unbind**.

### Notes

-   The **Hide dependency of binding** option can be used to prevent problems with cyclic dependencies between spreadsheets. Selecting it is necessary when, for example, cells in *Spreadsheet A* are bound to *Spreadsheet B*, while cells in *Spreadsheet B*, in turn, are bound to some other cells in *Spreadsheet A*. This option should be used with caution:
    -   Hiding dependencies can be dangerous because broken dependencies can damage your FreeCAD file. For example, when you delete a spreadsheet you will not be warned about hidden dependencies.
    -   When you open a document with a spreadsheet containing a hidden dependency, you will get the spreadsheet marked to be recomputed. This is because a cyclic dependency cannot be recomputed automatically. To recompute the [Std Refresh](Std_Refresh.md) tool must be used.
-   The cell binding has a range check and warns you about mismatched ranges. For example binding 1x3 cells to 3x2 cells cannot work because it is unknown which 3 cells of the original 6 cells should be used.
-   You cannot change the cell range of an existing binding. You must first unbind the cells and then create a new binding.
-   The frame color indicating the binding cannot be changed yet.

## Configuration tables 


<small>(v0.20)</small> 

You can use Spreadsheets to create configuration tables with sets of predefined parameters for your model, and then dynamically change which configuration to use. See [this Forum post](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183) if you want to know more about the inner workings of this feature.


<div class="mw-collapsible mw-collapsed toccolours">

Expand this section for a brief tutorial on creating a configuration table.


<div class="mw-collapsible-content">

1.  In a new document, first create a [Std Part](Std_Part.md), then create a [Part Box](Part_Box.md), a [Part Cylinder](Part_Cylinder.md) and a Spreadsheet.
2.  The Box and the Cylinder are automatically placed in the [Std Part](Std_Part.md) container. Manually put the Spreadsheet in the container as well.
3.  In the Spreadsheet enter the content as shown below. Set the alias for B2 as {{Value|width}}, C2 as {{Value|length}} and D2 as {{Value|radius}}:
    ![](images/Spreadsheet_configuration_table_screenshot_4.png )
4.  Bind the [expressions](Expressions.md) {{Value|Spreadsheet.width}} and {{Value|Spreadsheet.length}} to the Box\'s properties **Width** and **Length**, respectively:
    ![](images/Spreadsheet_configuration_table_screenshot_2.png )
5.  Bind the expression {{Value|Spreadsheet.radius}} to the Cylinder\'s property **Radius**. Also change the **Height** of the Cylinder to {{Value|5 mm}} so that it is lower than the Box.
6.  Right-click the cell A2 in the Spreadsheet and select **Configuration table...** from the context menu.
7.  The **Setup Configuration Table** dialog opens.
8.  Enter the following:
    ![](images/Spreadsheet_configuration_table_screenshot_5.png )
9.  Press **OK**.
10. A new property called **Configuration** is be added to the [Std Part](Std_Part.md) container to choose the configuration as shown below:
    ![](images/Spreadsheet_configuration_table_screenshot_6.png )

You can use either a [Std Link](Std_LinkMake.md) or a [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md) to instantiate a [Variant Instance](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183&p=532130#p532130) of a configurable object with the following steps:

1.  Create a [Std Link](Std_LinkMake.md) to the [Std Part](Std_Part.md) container and set its **Link Copy On Change** property to {{Value|Enabled}}.
2.  Move the Link to a new place by changing its **Placement** so that it is easier to distinguish from the original object.
3.  Select a different **Configuration** for the Link to create a variant instance.

Similar steps apply to a [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md), except that its property for activating a variant instance is called **Bind Copy On Change**.


</div>


</div>

## Noções básicas de script 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/pt-br
