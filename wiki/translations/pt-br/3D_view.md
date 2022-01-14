# 3D view/pt-br
## Introdução


{{TOCright}}

A [ vista 3D](3D_view.md),que constitui a janela mais importante da [ interface](interface.md) do FreeCAD, é uma instância da Coin3D, biblioteca para implementação de área de modelagem que segue o padrão OpenInventor 2.1 [ scenegraph](Scenegraph.md)

Certas propriedades da visualização, como cor de fundo, estilo [ de navegação do mouse](Mouse_navigation.md), e tarefas como fazer um zoom, podem ser configuradas no [ editor de preferências](Preferences_Editor.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">


{{Caption | A [ Draft](visualização_3D]]_é_um_componente_do_FreeCAD_[[interface]]. Por padrão, ele mostra um pequeno widget com eixos de coordenadas e o cubo de navegação, que também tem eixos de coordenadas; a grade pode ser exibida e configurada carregando a bancada de trabalho [[Draft Workbench .md).}}

## Ações


**Note:**

links para as ações da <small>(v0.19)</small> .

Uma vez que a [ vista hierárquica de objetos](tree_view.md) lista a maioria dos objetos que estão visíveis na área de modelagem 3D, é possível realizar, direto nesta área, muitas ações que normalmente são executadas pela [ vista hierárquica de objetos](tree_view.md).

Quando a bancada de trabalho [Start](Start_Workbench.md) está ativa, ao clicar com o botão direito do mouse na área de modelagem 3D, aparece apenas o comando

-    **[Estilos de navegação](Mouse_navigation.md)**, que dá acesso a diferentes métodos de uso dos botões do mouse ou do trackpad do notebook.

Entretanto, quando uma [bancada de trabalho](Workbenches.md) é carregada, outros comandos aparecem:

-    **Link actions**: [Criar link](Std_LinkMake.md).

    -   
        **Criar grupo de links**
        
        : [Agrupamento simples](Std_LinkMakeGroup.md), [Agrupar com links](Std_LinkMakeGroup.md), [Grupo com vínculos de transformação](Std_LinkMakeGroup.md).

-    **[Enquadrar tudo](Std_ViewFitAll.md)**: ajusta a visibilidade para que todos os objetos do documento apareçam na tela.

-    **[Enquadrar seleção](Std_ViewFitSelection.md)**: ajusta a visibilidade para que todos os objetos selecionados apareçam na tela.

-    **[Estilo de desenho](Std_DrawStyle.md)**: escolha entre o Estilo padrão, Pontos, Arame, Linha oculta, Sem sombreamento, Sombreado e Linhas planas.

-    **[Vistas padrão](Std_View_Menu.md)**: [Isométrico](Std_ViewIsometric.md), [Frente](Std_ViewFront.md), [Topo](Std_ViewTop.md), [Direito](Std_ViewRight.md), [Traseira](Std_ViewRear.md), [De baixo](Std_ViewBottom.md), [Esquerda](Std_ViewLeft.md), [Girar para esquerda](Std_ViewRotateLeft.md), [Girar para direita](Std_ViewRotateRight.md).

-    **Measure**: [Alternar medição](View_Measure_Toggle_All.md), [Limpar medições](View_Measure_Clear_All.md).

-    **Janela do documento**: [Ancorado](Std_ViewDockUndockFullscreen.md), [Desancorado](Std_ViewDockUndockFullscreen.md), and [Tela cheia](Std_ViewDockUndockFullscreen.md).

Outros comandos podem ser disponibilizados, dependendo da bancada de trabalho ativa e do(s) objetos(s) selecionado(s).

Por exemplo, com a bancada [Part](Part_Workbench.md) ativa e com um objeto selecionado:

-    **[Aparência...](Std_SetAppearance.md)**: abre a caixa de diálogo que permite alterar as cores e tamanhos de linhas e vértices, assim como as cores das faces.

-    **[Mudar visibilidade](Std_ToggleVisibility.md)**: exibe ou oculta o objeto selecionado.

-    **[Alternar seletibilidade](Std_ToggleSelectability.md)**: desliga a possibilidade de selecionar o objeto na área de modelagem 3D. Este comando torna o atributo `Selectable` do objeto para `True` ou `False`. Altere o status da propriedade **Selectable** no [editor de propriedades](property_editor.md).

-    **[Ir para a seleção](Std_TreeSelection.md)**: expande a [vista hierárquica do modelo](tree_view.md) para exibir o objeto selecionado na estrutura hierárquica.

-    **[Cor aleatória](Std_RandomColor.md)**: atribui uma cor ao objeto de modo aleatório. O atributo `ShapeColor` do objeto é alterado, definindo-se uma sequência composta por uma cadeia de três números que variam aleatoriamente entre 0 e 1, para que representem os canais de cores `(r,g,b)`. A propriedade pode ser alterada em **Shape Color** no [editor de propriedades](property_editor.md).

-    **[Excluir](Std_Delete.md)**: remove o objeto do documento e da área de modelagem 3D, acionando o método `removeObject()`.

Outro exemplo: com a bancada [Draft](Draft_Workbench.md) ativa e um objeto selecionado, são apresentados os mesmos comandos exibidos pela bancada [Part](Part_Workbench.md), e mais:

-    **Draft**: comandos para a criação e a modificação de objetos da bancada [Draft](Draft_Workbench.md).

-    **Utilities**: comandos contextuais adicionais, que fazem parte da bancada[Draft](Draft_Workbench.md).

## Detalhes

O FreeCAD usa a biblioteca integradora Quarter, para que a biblioteca de visualização de alto nível Coin3D seja utilizada junto ao framework Qt.

É possível interagir diretamente com o cenário de visualização 3D do [console Python](Python_console.md) usando a biblioteca Python Pivy.

Para mais informações, veja a documentação para usuários avançados:

-   [Scenegraph](Scenegraph.md), descrição da biblioteca Coin3D.
-   [Pivy](Pivy.md), uso da Coin3D a partir do console Python.
-   [Bibliotecas de terceiros](Third_Party_Libraries.md) usadas pelo FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html): documentação para C++ da Coin 3D.


{{Interface navi

}}

---
[documentation index](../README.md) > 3D view/pt-br
