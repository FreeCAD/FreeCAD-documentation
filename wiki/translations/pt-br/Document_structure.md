# Document structure/pt-br
![](images/Screenshot_treeview.jpg ) Um documento FreeCAD contém todos os objetos de sua cena. Pode conter tanto grupos quanto objetos criados com qualquer oficina. Assim, você pode alternar entre as oficinas e ainda trabalhar no mesmo documento. Este documento é o que é salvo em disco quando você salva seu trabalho. Você também pode abrir vários documentos em simultâneo, no FreeCAD, e abrir várias visualizações do mesmo documento.

No documento, os objetos podem ser movidos em grupos, e ter um nome único. O gerenciamento de grupos, objetos e nomes de objetos é feito principalmente a partir da [Vista em árvore](Tree_view/pt-br.md). **Nota:** Também pode ser feito, é claro, como tudo no FreeCAD, a partir do intérprete [Python](Python/pt-br.md). Na [Vista em árvore](Tree_view/pt-br.md), você pode criar <img alt="" src=images/Std_Group.svg  style="width:16px;">. [grupos](Std_Group/pt-br.md), mover objetos para grupos, apagar objetos ou grupos, clicando com o botão direito na [Vista em árvore](Tree_view/pt-br.md) ou em um objeto, renomear objetos clicando duas vezes em seus nomes, ou possivelmente outras operações, dependendo da bancada de trabalho atual.

Os objetos em um documento FreeCAD podem ser de diferentes tipos. Cada bancada de trabalho pode criar seus próprios tipos de objetos; por exemplo, o <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Bancada de trabalho Mesh](Mesh_Workbench/pt-br.md) cria malhas, o <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Bancada de trabalho Part](Part_Workbench/pt-br.md) cria objetos de peças (Part), o <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Bancada de trabalho Draft](Draft_Workbench/pt-br.md) também cria objetos de peças (Part), etc.

Se há pelo menos um documento aberto no FreeCAD, só pode haver um documento ativo. Este é o documento que é exibido na visualização 3D atual, o documento em que você está trabalhando.

## Aplicação e interface do usuário 

Como a arquitetura do FreeCAD é totalmente modular, a interface gráfica ou o ambiente gráfico é separado da parte da aplicação. Isto também é válido para os documentos. Os documentos também são separados em duas partes: o documento de Aplicação, que contém os objetos, e o documento Exibir, que contém a representação em tela dos objetos.

Pense nisso como dois espaços nos quais os objetos são definidos. Seus parâmetros de construção (é um cubo? um cone? de que tamanho?) são armazenados no documento de Aplicação, enquanto sua representação gráfica (o objeto é desenhado com linhas pretas? com faces azuis?) é armazenada no documento de Visualização. Por que isso acontece? Porque o FreeCAD também pode ser usado sem a interface gráfica, por exemplo, dentro de outros programas, e precisamos ser capazes de manipular os objetos, mesmo que nada seja exibido na tela.

Outra coisa que está contido dentro do documento Vista são as vistas em 3D. Um documento pode ter vários pontos de vista aberta, para que possa inspecionar o seu documento a partir de vários pontos de vista, em simultâneo. Talvez você gostaria de ver uma vista de topo e uma vista frontal do seu trabalho, em simultâneo? Então, você vai ter duas vistas do mesmo documento, ambos armazenados no documento Vista. A criação de novos pontos de vista ou vistas de fechamento pode ser feito a partir do menu Vistar, ou clicando com o botão direito em uma guia vista.

## Scripting

Os documentos podem ser criados, acessados e modificados facilmente a partir do intérprete [Python](Python/pt-br.md). Por exemplo : 
```python
FreeCAD.ActiveDocument
``` Irá devolver o documento atual (ativo) 
```python
FreeCAD.ActiveDocument.Blob
``` Acessaria um objeto chamado \"Blob\" dentro do seu documento. 
```python
FreeCADGui.ActiveDocument
``` Retornará a visualização do documento associado com o documento atual 
```python
FreeCADGui.ActiveDocument.Blob
``` Acessa a representação gráfica (vista) do objeto \"Blob\" 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Retorna à visão atual



---
⏵ [documentation index](../README.md) > Document structure/pt-br
