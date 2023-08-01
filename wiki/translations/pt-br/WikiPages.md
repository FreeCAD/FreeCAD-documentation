# WikiPages/pt-br
{{TOCright}}

Esta página é uma extensão da página [Help:Editing](Special:MyLanguage/Help_Editing.md) e dá orientações comuns para escrever e atualizar a documentação do wiki FreeCAD. Resume várias discussões e sessões de troca de ideias.



## Antes de começar 


<div class="mw-translate-fuzzy">

-   Esta documentação wiki é baseada no [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), o mesmo 'software' que alimenta a [Wikipédia](https://pt.wikipedia.org/). Se você já contribuiu para a Wikipédia, a edição de páginas wiki FreeCAD deve ser fácil.
-   Ao contrário da Wikipedia, o wiki FreeCAD está protegido contra 'spam'. É necessário solicitar uma conta [no forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   Se nunca utilizou 'software' wiki antes, por favor leia [Help:Editing](Special:MyLanguage/Help_Editing.md) para se familiarizar com a marcação que é utilizada.
-   Para o uso avançado do 'software' wiki, ver [MediaWiki Ajuda:Conteúdo](https://www.mediawiki.org/wiki/Help:Contents/pt-br). Nem todas as características do MediaWiki estão disponíveis neste wiki FreeCAD, mas muitas estão.
-   Gostamos de manter a documentação de fácil leitura, por isso evite utilizar características complexas. Mantenha-a simples.
-   Use uma sandbox para testar o seu código, por exemplo, [FreeCADDocu:Sandbox](FreeCADDocu_Sandbox.md) ou uma página específica com o seu nome [Sandbox:Yourname](Sandbox_Yourname.md).
-   Por favor, esteja atento às traduções. O wiki FreeCAD utiliza suporte de tradução automática para fornecer páginas em diversas línguas. Para cada página podem existir várias versões linguísticas. Em muitas páginas vê-se etiquetas como <translate>...</translate> e muitas etiquetas individuais como . Estas últimas são criadas pelo sistema de tradução. Elas ligam os títulos e parágrafos às suas versões traduzidas. Não devem ser alterados, já que isso destruiria essas ligações. No entanto, não há problema em mover parágrafos ou alterar a redação, desde que as etiquetas permaneçam com eles. Se remover um título ou um parágrafo, deve também remover a etiqueta correspondente. Tenha em conta que as alterações nos títulos e parágrafos existentes influenciam as traduções existentes. As suas modificações devem valer a pena. Não se preocupe quando adicionar novo material porque o sistema irá adicionar novas etiquetas automaticamente após as suas edições. Para mais informações ver [Localisation](Special:MyLanguage/Localisation.md) e a página original [Help:Extensão:Translate/Exemplo de tradução de página](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/pt-br).


</div>



## Orientações gerais 



### Descrições concisas 

Ao descrever o FreeCAD tente ser conciso e direto e evite a repetição. Descrever o que o FreeCAD \"faz\", e não o que o FreeCAD \"não faz\". Evite também expressões coloquiais. Utilizar \"alguns\" quando se lida com um número indeterminado, ou especificar a quantidade correta.

Descrição ruim
:   [PartDesign Workbench](Special:MyLanguage/PartDesign_Workbench.md) a PartDesign é uma bancada de trabalho para a concepção de peças que visa fornecer ferramentas para a modelação de peças sólidas complexas.





Boa descrição
:   [PartDesign Workbench](Special:MyLanguage/PartDesign_Workbench.md) visa fornecer ferramentas para modelação de peças sólidas complexas.



### Informação centralizada 

Evitar duplicar informações. Insira a informação numa nova página, e crie um link para esta, e utilize o quando precisar reutilizar informação.

Não utilizar a tranclusão de páginas ([Help:Editing#Modelos e paginas Transcluidas](Special:MyLanguage/Help:Editing#Templates_and_transcluding_pages.md)), visto que isto torna o wiki difícil de traduzir. Utilize apenas os modelos descritos abaixo em [#Modelos](#Modelos.md).



### Estilo

Os modelos são usados para estilizar as páginas de ajuda. Eles dão à documentação uma aparência uniforme. Há um modelo para comandos de \'menu\', Arquivo → Salvar, um modelo para mostrar as teclas a serem pressionadas, **Shift**, para mostrar um valor booleano, `True`, etc. Familiarize-se com a seção [#Modelos](#Modelos.md) antes de escrever páginas de ajuda.



### Sinalizadores temporários 

Se estiver a trabalho numa página grande é aconselhável marcar a página como em construção ou como inacabada. Isto assegura que os administradores do wiki não marquem a sua página como pronta para tradução enquanto ainda está a alterá-la.


<div class="mw-translate-fuzzy">

Para sinalizar uma página, adicionar  ou  na primeira linha. Com  convidará outros a juntarem-se a ti para terminar a página, enquanto  indica que tu realizarás o trabalho e que outros devem esperar o autor concluir.


</div>

Uma vez terminado o trabalho, por favor não se esqueça de retirar os sinalizadores!



## Exemplos

Para se familiarizar rapidamente com a estrutura e estilo do wiki FreeCAD veja a página modelo: [Modelo GuiCommand](Special:MyLanguage/GuiCommand_model.md).


<div class="mw-collapsible mw-collapsed toccolours">



## Estrutura


<div class="mw-collapsible-content">

A [Central do Usuário](Special:MyLanguage/User_hub.md) fornece um [Índice \'On-line\' de Ajuda](Special:MyLanguage/Online_Help_Toc.md). Este é usado como referência principal para compilar automaticamente a ajuda \'offline\' que se encontra no FreeCAD, bem como a documentação PDF \'offline\'.


<div class="mw-translate-fuzzy">

O [Modelo:Docnav](Template_Docnav.md) é utilizado para ligar páginas sequencialmente, seguindo a estrutura do [Índice \'On-line\' de Ajuda](Special:MyLanguage/Online_Help_Toc.md). Veja [#Modelos](#Modelos.md) para uma lista de todos os Modelos.


</div>



### Nomes de página 


<div class="mw-translate-fuzzy">

Os nomes das páginas devem ser curtos, e eles devem utilizar o estilo capitular: todas as palavras, exceto a primeira e os nomes próprios, tem de estar em caixa baixa. Este é o [estilo adotado pela Wikipédia](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Capital_letters#Headings,_headers,_and_captions) para seus artigos.


</div>


<div class="mw-translate-fuzzy">


Nome de página ruim:
:   Construção de Aviões da AeroCompany


</div>


<div class="mw-translate-fuzzy">


Bom nome de página:
:   Construção de aviões da AeroCompany


</div>

Os nomes das páginas de bancada de trabalho de alto nível devem ter este formato: em inglês XYZ Workbench em ‎português do Brasil Bancada de trabalho XYZ onde XYZ é o nome da bancada de trabalho, por exemplo, [PartDesign Workbench](PartDesign_Workbench.md), [Bancada de trabalho PartDesign](Special:MyLanguage/PartDesign_Workbench.md). E os nomes das páginas que descrevem os comandos (ou ferramentas) pertencentes a um bancada de trabalho devem ter este formato: XYZ Comando por exemplo, [PartDesign Pad](PartDesign_Pad/pt-br.md). Note que deve-se usar o nome do comando como ele aparece no código fonte.



### Títulos


<div class="mw-translate-fuzzy">

Tal como os nomes das páginas, os títulos dos parágrafos devem ser curtos e utilizar estilo capitular. Não deve utilizar H1 no título (= Título =) na sua marcação wiki, visto que o título da página é automaticamente adicionado como título principal H1.


</div>

### Links

Você deve usar o nome do link original para links sempre que possível. Isso esclarece a página referenciada na documentação impressa ou 'offline'. Evite palavras sem sentido para o link.

Link ruim

:   Para obter mais informações sobre como desenhar objetos 2D, clique [ aqui](Draft_Workbench/pt-br.md).





Bom link
:   Para obter mais informações sobre o desenho de objetos 2D, consulte a [ Bancada de trabalho Draft](Draft_Workbench/pt-br.md).

O melhor formato para um link é:


<div class="mw-translate-fuzzy">

[name of page](Name_of_page.md)


</div>

Traduzido:


<div class="mw-translate-fuzzy">

[nome da pagina](Name_of_page/pt-br.md)


</div>

Note que o que vem antes de |, é o link real, isto é importante. Se o nome da sua página for Nome_da_página, o link falhará se você digitar Nome_da_Página (P em maiúsculo). Antes do caractere | todos os espaços devem ser substituídos por traço baixo (_). Isto é para ajudar os tradutores que utilizam programas de tradução, sem os sublinhados o link seria traduzido pelo 'software', o que é indesejável.

Para criar um link para um determinado parágrafo, adicione uma cerquilha # e o títulos a referenciar. Exemplo:

[WikiPages](WikiPages#Name.md)

Traduzido:

[PaginasWiki](WikiPages/pt-br#Nome.md)

Dentro da mesma página, você pode omitir o nome da página. Exemplo:

[Nomes](#Nomes.md)

Para criar um link para o topo da página você pode usar:

</translate>{{Top}}<translate>


<div class="mw-translate-fuzzy">

Este link funcionará até mesmo se não houver parágrafo \'Topo\' na página. Ele é especialmente útil para páginas longas, pois permite que o usuário volte rapidamente à lista de conteúdo. Você pode colocá-lo no final de cada parágrafo. Certifique-se de que haja uma linha vazia antes e depois do link.


</div>


Image link
:   <img alt="Optional text that is shown when you hover the image\|link=Draft_Wire" src=images/Draft_Wire.svg  style="width:24px;">

To use an image as a link:

![](images/)

Image link + text link
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md)

If you leave out the optional text the link itself will be shown when the image is hovered, which is preferable, and you should also add a text link after the image link:

![](images/)_[Draft_Wire](Draft_Wire.md)



### Páginas do Workbench 

Uma página de bancada de trabalho de alto nível deve começar com:

-   Uma descrição de para que serve a bancada de trabalho.
-   Uma imagem para ilustrar a descrição.

Consulte [#Captura de tela](#Captura_de_tela.md) para obter convenções sobre a inclusão de imagens.



### Páginas de comando 

As páginas de comando que descrevem as ferramentas da bancada de trabalho não devem ser muito longas, elas devem apenas explicar o que um comando pode e o que não pode fazer, e como usá-lo. Você deve manter as imagens e os exemplos no mínimo possível. Tutoriais podem expandir os detalhes de como usar a ferramenta e fornecer detalhes passo a passo.

Consulte a página [Modelo GuiCommand](GuiCommand_model/pt-br.md) para obter mais detalhes.



### Tutoriais

Um tutorial bem escrito deve ensinar como alcançar determinados resultados práticos rapidamente. Não deve ser muito longo, mas deve incluir instruções e imagens passo-a-passo suficientes para guiar o usuário. Conforme o FreeCAD evolui, os tutoriais podem tornar-se obsoletos, por isso é importante mencionar a versão FreeCAD usada nele, ou necessária para realizar o tutorial.

Para obter exemplos, visite a página [Tutoriais](Tutorials/pt-br.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Modelos


<div class="mw-collapsible-content">

A estilização das páginas wiki do FreeCAD é conseguida através da utilização de modelos ([Help:Editing#Templates_and_transcluding_pages](Special:MyLanguage/Help:Editing#Templates_and_transcluding_pages.md)). Garantem um aspecto e uma sensação padronizados em todas as páginas, e também tornam possível reestilizar o wiki. Para consultar a lista completa de modelos definidos, acesse [Todas as páginas com prefixo (Template:)](Special:PrefixIndex/Template:.md). Mas, por favor, utilize apenas os modelos listados nas tabelas abaixo. Apenas em casos muito especiais deverá utilizar diretamente as marcações HTML.

Clique no link do modelo para ver as instruções de utilização de um modelo, e para ver a sua implementação. Os modelos são uma característica poderosa do 'software' MediaWiki. Deve ser um usuário wiki experiente se desejar propor adições e modificações aos modelos existentes. Se implementados de forma errada, os modelos dificultam a tradução de páginas para outras línguas, pelo que a sua utilização deve ser limitada à formatação de texto, a transclusão de páginas deve ser evitada. Veja [MediaWiki Help:Predefinições](https://www.mediawiki.org/wiki/Help:Templates/pt-br) para saber mais.



### Modelos simples 

Estes modelos aceitam um parâmetro de texto simples, e o formatam com um estilo particular.

++++
| Modelo                                                                                                        | Aparência                               | Descrição                                                                                                                                                                                                                                                                                                                                               |
+===============================================================================================================+=========================================+=========================================================================================================================================================================================================================================================================================================================================================+
| [Top](Template_Top.md)                                                                                |                          | Use it to add a link to the top of the page.                                                                                                                                                                                                                                                                                                            |
|                                                                                                               | {{Top}}                                 |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [Emphasis](Template_Emphasis.md)                                                                      |                          | Utilize-o para enfatizar um pedaço do texto.                                                                                                                                                                                                                                                                                                            |
|                                                                                                               | **ênfase**                     |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [KEY](Template_KEY.md)                                                                                |                          | Utilize-o para indicar a tecla que precisa ser pressionada.                                                                                                                                                                                                                                                                                             |
|                                                                                                               | **Alt**                             |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [ASCII](Template_ASCII.md)                                                                            |                          | Utilize-o para indicar uma tecla ascii com uma imagem (.svg) que precisa de ser pressionada. É necessário fornecer o carácter desejado ou o número do código ascii.                                                                                                                                                                                     |
|                                                                                                               | {{ASCII|A}}                             |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [Button](Template_Button.md)                                                                          |                          | Utilize-o para indicar um botão na 'interface' gráfica do usuário que precisa de ser clicado.                                                                                                                                                                                                                                                           |
|                                                                                                               | **Cancelar**                     |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [RadioButton](Template_RadioButton.md)                                                                |                          | Utilize-o para inserir um botão de opção na 'interface' gráfica do usuário que pode de ser {{RadioButton|TRUE|Selecionado}} ou {{RadioButton|FALSE|Não Selecionado}}.                                                                                                                                                       |
|                                                                                                               | {{RadioButton|Opção}}                   |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [CheckBox](Template_CheckBox.md)                                                                      |                          | Utilize-o para criar uma caixa de verificação na 'interface' gráfica do usuário que pode de ser {{CheckBox|TRUE|Checado}} ou {{CheckBox|FALSE|Não verificado}}.                                                                                                                                                             |
|                                                                                                               | {{CheckBox|Opção}}                      |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [SpinBox](Template_SpinBox.md)                                                                        |                          | Utilize-o para inserir um botão giratório na 'interface' gráfica do usuário para ele possa ajustar um valor.                                                                                                                                                                                                                                            |
|                                                                                                               | {{SpinBox|1.50}}                        |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [ComboBox](Template_ComboBox.md)                                                                      |                          | Utilize-o para indicar uma caixa de combinação na 'interface' gráfica do usuário que precisa de ser modificada.                                                                                                                                                                                                                                         |
|                                                                                                               | {{ComboBox|Menu 1}}                     |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [LineEdit](Template_LineEdit.md)                                                                      |                          | Use it to indicate a LineEdit in the graphical user interface that needs to be modified.                                                                                                                                                                                                                                                                |
|                                                                                                               | {{LineEdit|Metal Nickel (Ni)}}          |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [FALSE](Template_FALSE.md), [false](Template_false.md)                                        |                          | Use-o para indicar um valor booleano falso, por exemplo, como uma propriedade no [editor de propriedade](Property_editor/pt-br.md). Isto é um atalho. Como é um valor, prefira Modelo [Value](Template_Value.md). {{Value|false}}                                                                                         |
|                                                                                                               | `False`                               |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | , {{false}}               |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [TRUE](Template_TRUE.md), [true](Template_true.md)                                            |                          | Use-o para indicar um valor booleano verdadeiro, por exemplo, como uma propriedade no [editor de propriedade](Property_editor/pt-br.md). Isto é um atalho. Como é um valor, prefira Modelo [Value](Template_Value.md). {{Value|true}}                                                                                     |
|                                                                                                               | `True`                                |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | , {{true}}                |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [MenuCommand](Template_MenuCommand.md)                                                                |                          | Utilize-a para indicar a localização de um comando dentro de um determinado menu.                                                                                                                                                                                                                                                                       |
|                                                                                                               | **Arquivo → Salvar**        |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [FileName](Template_FileName.md)                                                                      |                          | Utilize-o para indicar um nome de um arquivo ou diretório.                                                                                                                                                                                                                                                                                              |
|                                                                                                               | **Nome do arquivo**            |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [SystemInput](Template_SystemInput.md)                                                                |                          | Use-o para indicar o texto de entrada digitado pelo usuário.                                                                                                                                                                                                                                                                                            |
|                                                                                                               | {{SystemInput|Digite este texto}}       |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [SystemOutput](Template_SystemOutput.md)                                                              |                          | Use-o para indicar a saída de texto do sistema.                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | {{SystemOutput|Texto de saída}}         |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [Incode](Template_Incode.md)                                                                          |                          | Use-o para incluir o código-fonte em linha com uma fonte monoespaçada. Ele deve caber em uma linha.                                                                                                                                                                                                                                                     |
|                                                                                                               | `import FreeCAD`               |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [PropertyView](Template_PropertyView.md)                                                              |                          | Use-o para indicar uma propriedade de Visualização no [editor de propriedades](Property_editor/pt-br.md). Exemplos de propriedades de visualização incluem {{emphasis| Cor da linha}}, {{emphasis| Largura da linha}}, {{emphasis| Cor do ponto}}, {{emphasis| Tamanho do ponto}}, etc. |
|                                                                                                               | **Cor**                    |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [PropertyData](Template_PropertyData.md)                                                              |                          | Use-o para indicar uma propriedade de Dados no [editor de propriedades](Property_editor.md). As propriedades de dados diferem para diferentes tipos de objetos.                                                                                                                                                                                 |
|                                                                                                               | **Posição**                |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [Properties Title](Template_Properties_Title.md) / [TitleProperty](Template_TitleProperty.md) |                          | Use-o para indicar o título de um grupo de propriedade no [editor de propriedades](Property_editor.md). O título não será incluído no índice automático.                                                                                                                                                                                        |
|                                                                                                               | {{Properties_Title|Base}}               |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [Obsolete](Template_Obsolete.md)                                                                      |                          | Use-o para indicar que uma característica se tornou obsoleta na versão FreeCAD especificada.                                                                                                                                                                                                                                                            |
|                                                                                                               | {{Obsolete|0.19}}                       |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [Version](Template_Version.md)                                                                        |                          | Use-o para indicar que uma característica foi introduzida na versão FreeCAD especificada.                                                                                                                                                                                                                                                               |
|                                                                                                               | <small>(v0.18)</small>                         |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [VersionMinus](Template_VersionMinus.md)                                                              |                          | Use-o para indicar que um recurso está disponível na versão FreeCAD especificada e nas versões anteriores.                                                                                                                                                                                                                                              |
|                                                                                                               | {{VersionMinus|0.16}}                   |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [VersionPlus](Template_VersionPlus.md)                                                                |                          | Use-o para indicar que um recurso está disponível na versão FreeCAD especificada e nas versões posteriores.                                                                                                                                                                                                                                             |
|                                                                                                               | <small>(v0.17)</small>                     |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [ColoredText](Template_ColoredText.md)                                                                |                          | Use este modelo para colorir o fundo, texto, ou fundo e texto. (Pagina [ColoredText](Template_ColoredText.md) para mais exemplos)                                                                                                                                                                                                               |
|                                                                                                               | {{ColoredText|Texto Colorido}}          |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++
| [ColoredParagraph](Template_ColoredParagraph.md)                                                      |                          | Use este modelo para colorir o fundo, texto ou fundo e o texto de um parágrafo inteiro. (Página [ColoredParagraph](Template_ColoredParagraph.md) para mais exemplos)                                                                                                                                                                            |
|                                                                                                               | {{ColoredParagraph|Parágrafo Colorido}} |                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                      |                                                                                                                                                                                                                                                                                                                                                         |
++++



### Modelos complexos 

Estes modelos requerem mais parâmetros de entrada, ou produzem um bloco de texto com um formato particular.

++++
| Modelo                                                                                           | Aparência                                                                                                                    | Descrição                                                                                                                                                                                                                                                                                                                     |
+==================================================================================================+==============================================================================================================================+===============================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template_Prettytable.md)                                                   | Esta tabela                                                                                                                  | Use-o para formatar tabelas como esta. Propriedades adicionais da tabela podem ser adicionadas.                                                                                                                                                                                                                               |
++++
| [Caption](Template_Caption.md)                                                           |                                                                                                                    | Use-o para adicionar uma explicação abaixo de uma imagem. Ela pode ser alinhada à esquerda ou alinhada ao centro.                                                                                                                                                                                                             |
|                                                                                                  | <div style="width:400px;">                                                                                                   |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                               |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  | 
*Algumas legendas para uma imagem*                                                                                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                    |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  | </div>                                                                                                                       |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
++++
| [Clear](Template_Clear.md)                                                               |                                                                                                                              | Use-o para limpar colunas. Siga a definição do modelo para uma explicação detalhada. Ele é freqüentemente usado para impedir o fluxo de texto ao lado de imagens não relacionadas.                                                                                                                                            |
++++
| [Code](Template_Code.md)                                                                 |                                                                                                               | Use-o para incluir exemplos de códigos de várias linhas com uma fonte monoespaçada. O idioma padrão é Python, mas outros idiomas podem ser especificados.                                                                                                                                                                     |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           | [Pythondeve](Python/pt-br.md) aderir às recomendações gerais estabelecidas pelo [PEP8: Guia de estilo para código Python](https://www.python.org/dev/peps/pep-0008/). Em particular, os parênteses devem seguir imediatamente o nome da função, e um espaço deve seguir uma vírgula. Isto torna o código mais legível |
++++
| [Fake heading](Template_Fake_heading.md)                                                 |                                                                                                               | Use-o para criar um título que não será automaticamente incluído no índice.                                                                                                                                                                                                                                                   |
|                                                                                                  | {{Fake heading|Titulo|2}}                                                                                                    |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
++++
| [GuiCommand](Template_GuiCommand.md)                                                     | Veja [Modelo GuiCommand](GuiCommand_model/pt-br.md)                                                                  | Use-o para criar uma caixa com informações úteis para documentar os comandos (ferramentas) da bancada de trabalho.                                                                                                                                                                                                            |
++++
| [TutorialInfo](Template_TutorialInfo.md)                                                 | Veja, por exemplo,[Tutorial básico de modelagem](Basic_modeling_tutorial/pt-br.md)                                   | Use-o para criar uma caixa com informações úteis para documentar [tutoriais](Tutorials.md).                                                                                                                                                                                                                           |
++++
| [Macro](Template_Macro.md)                                                               | Veja, por exemplo, [Macro FlattenWire](Macro_FlattenWire.md)                                                         | Utilize-o para criar uma caixa com informações úteis para documentar [macros](macros.md).                                                                                                                                                                                                                             |
++++
| [Docnav](Template_Docnav.md)                                                             |                                                                                                               | Use-o para criar uma barra com as palavras \"próximo\", \"anterior\" e \"índice\", e os links apropriados, o que é útil para colocar as páginas em uma determinada sequência.                                                                                                                                                 |
|                                                                                                  |                                                                                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
++++
| [VeryImportantMessage](Template_VeryImportantMessage.md)                                 |                                                                                                               | Use-o para criar uma caixa destacada com uma mensagem muito importante. Use com parcimônia, apenas para indicar problemas maiores na funcionalidade do software, descontinuação de ferramentas e similares.                                                                                                                   |
|                                                                                                  | **Mensagem importante**                                                                                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
++++
| [Page in progress](Template_Page_in_progress.md)                                         |                                                                                                               | Use isto para páginas que ainda estão em andamento ou que estão sendo retrabalhadas no momento. Não se esqueça de remover isto quando a página estiver pronta.                                                                                                                                                                |
|                                                                                                  | {{Page in progress|Página em andamento}}                                                                                     |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
++++
| [UnfinishedDocu](Template_UnfinishedDocu.md)                                             |                                                                                                               | Use-o para criar uma caixa destacada indicando uma página de documentação inacabada.                                                                                                                                                                                                                                          |
|                                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
++++
| [Softredirect](Template_Softredirect.md)                                                 |                                                                                                                              | Use-o ao invés do redirecionamento normal, quando estiver redirecionando para uma página especial (como Mídia: ou Categoria:), casos em que o redirecionamento normal é desativado.                                                                                                                                           |
++++
| [Quote](Template_Quote.md)                                                               |                                                                                                               | Use-o para criar uma caixa de texto com uma citação e referência literal.                                                                                                                                                                                                                                                     |
|                                                                                                  | {{Quote|text=Cry "Havoc" and let slip the dogs of war.|sign=William Shakespeare|source=''Julius Caesar'', act III, scene I}} |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                              | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                              |
|                                                                                                  |                                                                                                                              |                                                                                                                                                                                                                                                                                                                            |
++++
| [Userdocnavi](Template_Userdocnavi.md), [Powerdocnavi](Template_Powerdocnavi.md) |                                                                                                                              | Use-os para criar caixas de navegação para a documentação do usuário, a documentação do usuário avançado e a documentação do desenvolvedor. Isto permite saltar rapidamente entre as diferentes seções da documentação. Eles também colocam a página correspondente na categoria apropriada.                                  |
|                                                                                                  |                                                                                                                              |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                              |                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                              | </div>                                                                                                                                                                                                                                                                                                                        |
|                                                                                                  |                                                                                                                              |                                                                                                                                                                                                                                                                                                                            |
++++


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Artes gráficas 


<div class="mw-collapsible-content">

Imagens e capturas de tela são necessárias para produzir uma documentação completa do FreeCAD. Elas são particularmente úteis para ilustrar exemplos e tutoriais. As imagens devem ser mostradas em seu tamanho original, para que apresentem detalhes suficientes e sejam legíveis se incluírem texto. As imagens [Bitmap](bitmap.md) não devem ser redimensionadas.

Evite imagens animadas (GIF) nas páginas de ajuda geral. Animações e vídeos devem ser reservados para tutoriais não destinados a serem usados como documentação PDF offline.

As imagens podem ser carregadas através da página [Enviar arquivo](Special:Upload/pt-br.md).



### Nome


<div class="mw-translate-fuzzy">

Dê nomes significativos às suas imagens. Se você tiver uma imagem que mostre as características de um determinado comando, você deve usar o nome desse comando com `_example` no final. Por exemplo, para o comando [Draft Offset](Draft_Offset/pt-br.md), a imagem deve ser chamada `Draft_Offset_example.jpg`.


</div>



### Captura de tela 

Os tamanhos recomendados para as capturas de tela são:

-   Nativo 400x200 (ou largura=400 e altura\<=200), para páginas de[referência de comando](GuiCommand_model/pt-br.md), para permitir que a imagem caiba na parte esquerda da página, e para outras fotos padrão.
-   Nativo 600x400 (ou largura=600 e altura\<=400), para páginas de[referência de comando](GuiCommand_model.md), quando você realmente precisa de uma imagem maior, e ainda permitir que a imagem caiba na parte esquerda da página, e para outras fotos padrão.
-   Nativo 1024x768 (ou largura=1024 e altura\<=768), apenas para imagens em tela cheia.
-   Tamanhos menores são possíveis ao mostrar detalhes.
-   Evite imagens com resoluções maiores, pois elas não serão muito portáteis para outros tipos de displays ou para a documentação PDF impressa.

Você não deve depender de uma configuração personalizada de sua área de trabalho ou sistema operacional quando criar capturas de tela e deve usar os padrões gráficos da plataforma do FreeCAD sempre que possível.

Para criar uma captura de tela você pode usar as opções fornecidas por seu sistema operacional, ou uma dessas macros: <img alt="" src=images/Snip.png  style="width:24px;"> [Macro de Corte](Macro_Snip/pt-br.md) e <img alt="" src=images/Macro_Screen_Wiki.png  style="width:24px;"> [Macro de tela Wiki](Macro_Screen_Wiki/pt-br.md).



### Texto

Para facilitar a tradução da documentação, tente evitar capturas de tela que contenham textos. Se você não puder evitar isto, considere tirar fotos separadas da 'interface' e da [vista 3D](3D_view/pt-br.md). A imagem da visualização 3D pode ser reutilizada em cada tradução, enquanto um tradutor pode tirar uma captura de tela da 'interface' localizada, se necessário.



### Ícones e imagens 

Consulte a página [Objetos gráficos](Artwork.md) para todas as ilustrações e ícones que foram criados para o FreeCAD, e que também podem ser utilizados em páginas de documentação. Se quiser contribuir com ícones, favor ler as [Diretrizes para trabalhos gráficos](Artwork_Guidelines.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Traduções


<div class="mw-collapsible-content">

Por consenso, a página de referência no wiki é a página em inglês, que deve ser criada primeiro. Se quiser alterar ou adicionar conteúdo a uma página, deve fazê-lo primeiro à página inglesa, e só após concluída a atualização, deve ser feita a modificação na página traduzida.

O wiki FreeCAD utiliza uma extensão de tradução que permite gerir traduções entre páginas mais facilmente; para mais detalhes, ver [Localização Traduzir a wiki do FreeCAD](Special:MyLanguage/Localisation#Translate_the_FreeCAD_wiki.md).

Outros recursos úteis são:

-   [código de idioma ISO](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) para identificar o código de duas letras para uma linguagem específica para a qual se pretende traduzir.
-   [Google Tradutor](http://translate.google.com/) para ajuda com traduções.
-   [Deepl Tradutor](https://www.deepl.com/translator) para ajuda com traduções.



## Algumas dicas para tradutores 



### Traduzir GuiCommand 

    {{GuiCommand
    |Name=FEM EquationFlux
    |MenuLocation=Solve → Flux equation
    |Workbenches=[FEM](FEM_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Traduzido:

    {{GuiCommand/fr
    |Name=FEM EquationFlux
    |Name/fr=FEM Équation d'écoulement
    |MenuLocation=Solveur → Équation de flux
    |Workbenches=[Atelier FEM](FEM_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM Tutoriel](FEM_tutorial/fr.md)
    }}



### Traduzir navi 

    {{FEM_Tools_navi}}

Traduzido:

    {{FEM_Tools_navi/fr}}



### Traduzir link 

    [Part Module](Part_Module.md)

Traduzido:

    [Atelier Part](Part_Module/fr.md)



### Traduzir Docnav 

    

Traduzido:

    

Exemplo com ícones:

    

Traduzido:

    


</div>


</div>




<div class="mw-translate-fuzzy">

## Renomeando e excluindo 


</div>

### Create pages 

Before creating a new page you should first check if a similar page already exists. If that is the case it is usually better to edit that existing page instead. When in doubt please open a topic in the [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21) first.

To create a new page do one of the following:

-   Visit the URL with the desired page name, for example: https://wiki.freecadweb.org/My_New_Page, and click on \'create this page\'.
-   Do a wiki search for the page name, and click on the red text in \'Create the page \"My New Page\" on this wiki!\'.



### Renomear páginas 

Como o FreeCAD é um projeto em permanente desenvolvimento, é por vezes necessário rever o conteúdo do wiki. Se os nomes dos comandos forem alterados no código-fonte, as páginas wiki que os documentam têm de ser renomeadas também. Isto só pode ser feito pelos administradores do wiki. Para informar os administradores, abrir um tópico no [fórum Wiki](https://forum.freecadweb.org/viewforum.php?f=21) e listar a alteração de nome necessária nesta forma:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...



### Excluir arquivos e páginas 

Caso precise apagar um arquivo, vá à sua página (https://www.freecadweb.org/wiki/File:***.***) e edite-o. Não importa se a página está em branco ou não, adicione isto como primeiro elemento: {{Delete}} e imediatamente abaixo descreva por que razão a página deve ser apagada. Além disso, abrir um tópico no [fórum Wiki](https://forum.freecadweb.org/viewforum.php?f=21).

Para páginas, o procedimento é o mesmo.



## Discussão

O [subforum Desenvolvimento/Wiki](http://forum.freecadweb.org/viewforum.php?f=21) no [fórum FreeCAD](https://forum.freecadweb.org) oferece um espaço dedicado à discussão de tópicos da wiki, a aparência da wiki e tudo o mais relacionado com a wiki. Coloque lá as suas perguntas e sugestões.



## Terminologia - política de nomenclatura 



### Inglês

Consulte [Glossário](Glossary.md).



### Outros idiomas 


<div class="mw-translate-fuzzy">

-   [Italiano](Italian_Translation.md)
-   [Francês](French_Translation.md)
-   [Alemão](German_Translation.md)
-   [Polonês](Polish_Translation.md)


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Documentation](Category_Documentation.md) > [Wiki](Category_Wiki.md) > [Wiki Documentation](Category_Wiki Documentation.md) > [Administration](Category_Administration.md) > WikiPages/pt-br
