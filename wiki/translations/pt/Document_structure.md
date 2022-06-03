# Document structure/pt
{{TOCright}}

![](images/Screenshot_treeview.jpg ) O documento FreeCAD contém todos os objectos da sua cena. Ele pode conter grupos e objectos feitos com qualquer bancada. Portanto, você pode alternar entre bancadas de trabalho, e ainda trabalhar no mesmo documento. O documento é o que fica guardado no disco quando você salvar seu trabalho. Você também pode abrir vários documentos ao mesmo tempo em FreeCAD e abra várias vistas do mesmo documento.


<div class="mw-translate-fuzzy">

Dentro do documento, os objectos podem ser movidos em grupos, e de ter um nome único. Gerir grupos, objectos e nomes de objecto é feito principalmente a partir da tela Árvore. Ele também pode ser feito, é claro, como tudo na FreeCAD, a partir do interpretador Python. Na vista de árvore, você pode criar grupos, mover objectos para grupos, apagar objectos ou grupos, clicando com o botão direito na vista de árvore ou em um objecto, renomear objectos clicando duas vezes em seus nomes, ou possivelmente outras operações, dependendo a bancada actual.


</div>


<div class="mw-translate-fuzzy">

Os objectos dentro de um documento FreeCAD pode ser de diferentes tipos. Cada bancada pode criar seus próprios tipos de objectos, por exemplo, o [Mesh Workbench](Mesh_Workbench.md) cria objectos de malha, os [Part Workbench](Part_Workbench.md) cria objectos parciais , o [Draft Workbench](Draft_Workbench.md) também cria objectos parciais, etc.


</div>

Se houver pelo menos um documento aberto em FreeCAD, há sempre um e só um documento activo. Esse é o documento que aparece na visualização em 3D actual, o documento que você está trabalhando actualmente.

## Aplicação e interface de usuário 


<div class="mw-translate-fuzzy">

Como quase tudo em FreeCAD, a área da Interface Gráfica do Usuário (GUI) esta separada da área da aplicação base (App). Isto também é válido para documentos. Os documentos também são feitos de duas partes   * o documento da Aplicação, que contém os nossos objectos, e o documento Vista, que contém a representação na tela de nossos objectos.


</div>


<div class="mw-translate-fuzzy">

Pense nisso como dois espaços, onde os objectos são definidos. Seus parâmetros construtivos (É um cubo? É um cone? Qual o tamanho?) São armazenados no documento do aplicativo, enquanto a sua representação gráfica (é desenhado com linhas pretas? Com as caras azuis?) São armazenados no documento Vista. Por que é assim? Porque FreeCAD também pode ser usado sem interface gráfica, por exemplo dentro de outros programas, e ainda deve ser capaz de manipular os nossos objectos, mesmo que nada é desenhado na tela.


</div>

Outra coisa que está contido dentro do documento Vista são as vistas em 3D. Um documento pode ter vários pontos de vista aberta, para que possa inspeccionar o seu documento a partir de vários pontos de vista, ao mesmo tempo. Talvez você gostaria de ver uma vista de topo e uma vista frontal do seu trabalho, ao mesmo tempo? Então, você vai ter duas vistas do mesmo documento, ambos armazenados no documento Vista. A criação de novos pontos de vista ou vistas de fechamento pode ser feito a partir do menu Ver ou clicando com o botão direito em uma guia vista.

## Scripting


<div class="mw-translate-fuzzy">

Os documentos podem ser facilmente criados, acessados e modificados a partir do interpretador Python. Por exemplo   *


</div>


```python
FreeCAD.ActiveDocument
```

Irá devolver o documento (activo) actual. 
```python
FreeCAD.ActiveDocument.Blob
``` Acessaria um objecto chamado \"Blob\" dentro do seu documento. 
```python
FreeCADGui.ActiveDocument
``` Devolveria o documento Vista associado ao documento actual. 
```python
FreeCADGui.ActiveDocument.Blob
``` Acessaria a parte de representação gráfica (vista) do nosso objecto Blob 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Voltaria a visão actual


<div class="mw-translate-fuzzy">


{{docnav/pt|Mouse Model/pt|Preferences Editor/pt}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Document structure/pt
