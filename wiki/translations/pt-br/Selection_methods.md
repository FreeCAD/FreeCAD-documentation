# Selection methods/pt-br
{{TOCright}}



## Visão geral 

Os métodos de seleção no FreeCAD permitem a seleção de objetos no [FreeCAD Interface](Interface/pt-br.md): tais como [vista 3D](3D_view/pt-br.md), [vista em árvore](Tree_view/pt-br.md), [métodos de seleção](Selection_view/pt-br.md), [vista de seleção](Selection_view/pt-br.md), e outros diálogos. Alguns métodos de seleção são específicos das bancadas de trabalho e estão documentados na documentação específica das bancadas de trabalho.



## Vista 3D 

Na [vista 3D](3D_view/pt-br.md) há várias maneiras de selecionar objetos.



### Seleção simples 


<div class="mw-translate-fuzzy">

A seleção simples com o mouse (por padrão, clique com o botão esquerdo do mouse) e a pré-seleção são descritas na página [Estilos de Navegação](Mouse_Model/pt-br.md).


</div>



### Cliques repetidos 


<div class="mw-translate-fuzzy">

O primeiro clique seleciona um sub-elemento (vértice, borda ou face) do objeto sob o mouse. Um segundo clique seleciona o objeto inteiro. <small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

O terceiro clique estende a seleção a seu objeto \'container\' ([PartDesign Body](PartDesign_Body.md), [Std Part](Std_Part.md), e outros). Outros cliques expandem a seleção até a cadeia de \'contêineres\'. <small>(v0.19)</small> 


</div>



### Comandos de seleção 

-   Para selecionar todos os objetos: [Std Std_SelectAll](Std_SelectAll/pt-br.md).
-   Para encaixotar selecione vários objetos principais: [Std Std BoxSelection](Std_BoxSelection/pt-br.md).
-   Para encaixotar selecione várias faces: [Std BoxElementSelection](Std_BoxElementSelection/pt-br.md) ou [Part BoxSelection](Part_BoxSelection/pt-br.md).



## Vista de seleção 

A [vista de seleção](Selection_view/pt-br.md) mostra os nomes dos objetos selecionados, incluindo seu nome completo de um objeto, por exemplo, {`Unnamed#Body.Box001.Face17`}.

Também permite realizar algumas ações como [Std ViewFitSelection](Std_ViewFitSelection/pt-br.md), e enviar o objeto para o [Python console](Python_console/pt-br.md).



### Exportação de objeto 

\"Isto deve estar na página [Vista de seleção](selection_view/pt-br.md)\".

Selecione qualquer objeto complexo, por exemplo, [PartDesign Body](PartDesign_Body/pt-br.md) ou [Std Part](Std_Part/pt-br.md), depois na [vista de seleção](selection_view/pt-br.md) selecione novamente o objeto e pressione **Ctrl**. + **C** no teclado para abrir o diálogo **Object selection**. Isto permite copiar o objeto selecionado junto com todos ou apenas alguns dos objetos de dependência desse objeto. Por exemplo, para uma [Std Part](Std_Part/pt-br.md) os possíveis objetos a serem selecionados incluem a [Std Part](Std_Part/pt-br.md) em si, mas também sua Origem, seus três eixos base (XYZ), e seus três planos base (XY, YZ, XZ).

Após pressionar **OK**, os objetos selecionados são copiados para a memória, e depois podem ser colados no documento para duplicar apenas esses objetos.

![](images/ObjectSelection.png )



*Diálogo de seleção de objetos que é lançado a partir do [vista de seleção](Selection_view/pt-br.md).*



## Vista em árvore 

Na [vista em árvore](tree_view/pt-br.md) os itens podem ser selecionados, ou desmarcados, um de cada vez, segurando a tecla **Ctrl** e clicando com o mouse.

Um intervalo de itens pode ser selecionado clicando no primeiro item, segurando **Shift**, e clicando no último item.

A seleção de um único item também mostrará suas propriedades no [editor de propriedade](property_editor/pt-br.md).

Um duplo clique abrirá qualquer [painel de tarefas](task_panel/pt-br.md) associado que contenha ações. Certifique-se de fechar este painel de tarefas antes de executar outro comando ou mudar para qualquer outra bancada de trabalho.

Mais métodos estão disponíveis abrindo o menu de contexto (clique com o botão direito do mouse), dependendo do objeto selecionado ou da bancada de trabalho ativa; veja as informações em [vista em árvore](tree_view/pt-br.md).

## Scripting

A seleção de objetos é inerentemente uma tarefa gráfica e, portanto, só está disponível quando a 'interface' gráfica do usuário é carregada.


<div class="mw-translate-fuzzy">

Estes comandos podem ser usados em [macros](Macros/pt-br.md) ou a partir do [console Python](Python_console/pt-br.md).


</div>


```python
import FreeCADGui as Gui

Gui.Selection.addSelection
Gui.Selection.addSelectionGate
Gui.Selection.Filter
```


<div class="mw-translate-fuzzy">

O comando `addSelectionGate` restringe o usuário de selecionar objetos não especificados na cadeia de seleção. Um símbolo aparece quando o ponteiro está sobre um item que não está no grupo especificado.


</div>


```python
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Edge")

#### or
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Face")

#### or
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Vertex")
```

To remove `SelectionGate()`:


```python
Gui.Selection.removeSelectionGate()
```

Consulte a [Documentação do código-fonte](Source_documentation/pt-br.md) e [Ajuda Padrão do Python](Std_PythonHelp/pt-br.md) para obter mais ajuda sobre o uso dessas ferramentas.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > Selection methods/pt-br
