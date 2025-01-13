# 3D view/pt-br
## Introdução




A [ vista 3D](3D_view.md),que constitui a janela mais importante da [ interface](interface.md) do FreeCAD, é uma instância da Coin3D, biblioteca para implementação de área de modelagem que segue o padrão OpenInventor 2.1 [ scenegraph](Scenegraph.md)

Certas propriedades da visualização, como cor de fundo, estilo [ de navegação do mouse](Mouse_navigation.md), e tarefas como fazer um zoom, podem ser configuradas no [ editor de preferências](Preferences_Editor.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">


{{Caption | A [ Draft](visualização_3D]]_é_um_componente_do_FreeCAD_[[interface]]. Por padrão, ele mostra um pequeno widget com eixos de coordenadas e o cubo de navegação, que também tem eixos de coordenadas; a grade pode ser exibida e configurada carregando a bancada de trabalho [[Draft Workbench .md).}}



## Menu de contexto 

The options in the context menu of the 3D view depend on the selected object(s) and the currently active workbench. To display this menu optionally select one or more objects and then right-click in the 3D view.



## Detalhes

O FreeCAD usa a biblioteca integradora Quarter, para que a biblioteca de visualização de alto nível Coin3D seja utilizada junto ao framework Qt.


<div class="mw-translate-fuzzy">

É possível interagir diretamente com o cenário de visualização 3D do [console Python](Python_console.md) usando a biblioteca Python Pivy.


</div>

Para mais informações, veja a documentação para usuários avançados:

-   [Scenegraph](Scenegraph.md), descrição da biblioteca Coin3D.
-   [Pivy](Pivy.md), uso da Coin3D a partir do console Python.
-   [Bibliotecas de terceiros](Third_Party_Libraries.md) usadas pelo FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html): documentação para C++ da Coin 3D.


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > 3D view/pt-br
