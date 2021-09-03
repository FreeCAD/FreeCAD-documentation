





{{TOCright}}

O controle do cubo de navegação, ou *\'cubo de navegação*, é uma ajuda gráfica de interface com o usuário para reorientar a visualização 3D. Por padrão, ele é visível e reside no canto superior direito da tela 3D. Se você estiver olhando para a vista 3D padrão, ela se parece com o seguinte:

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

O cubo de navegação é composto de várias partes:

-   Setas direcionais
-   Cubo de navegação principal
-   Menu mini-cubo

Se você colocar o ponteiro do mouse sobre uma entidade no cubo de navegação, ele fica azul-claro. Clicando em um clique, a vista 3D será reorientada conforme indicado pela função. No exemplo abaixo, a vista 3D foi girada por um [movimento do mouse](Mouse_Model/pt-br.md) \"não-padrão\". O ponteiro está em um canto (indicado pela cor azul); clicando irá reorientar a vista 3D para uma vista axonométrica padrão com este canto na sua frente.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Setas direcionais {#setas_direcionais}

Há seis setas direcionais: quatro setas triangulares, na parte superior, inferior, esquerda e direita; e duas setas curvas, uma de cada lado da seta superior.

Clicando nas setas triangulares, a vista 3D girará 45 graus em torno de uma linha perpendicular à direção da seta. Clicando nas setas curvas, a vista 3D será girada em torno de uma linha que aponta na sua direção.

## Cubo Principal de Navegação {#cubo_principal_de_navegação}

O cubo de navegação principal (\"cubo de navegação\" no restante desta seção) segue a orientação do objeto na vista 3D principal. Qualquer operação que reoriente a visualização principal em 3D também reorientará o cubo de navegação.

O cubo de navegação é essencialmente uma visão 3D de um cubo com seus três principais tipos de componentes (facetas, bordas e cantos) melhorados para que eles possam ser facilmente clicados com o ponteiro. Ao clicar em um determinado componente, a visualização 3D será centralizada e orientada para você. O cubo de navegação é um tanto \"esmagado\", como se a característica mais distante de você fosse maior do que a que está diretamente à sua frente. Isto permite que você veja as características adjacentes àquela que está diante de você e, portanto, selecione-as. Por exemplo, numa visão \"normal\" de um cubo normal, quando uma faceta está de frente para você, você também pode ver as quatro bordas e os quatro cantos dessa faceta. No cubo de navegação \"esmagado\", você também pode ver entidades representando cada uma das facetas adjacentes, as quatro bordas conectando os cantos da face voltados para você com a face oposta e os cantos da face oposta. Isto permite selecionar qualquer vista padrão possível, exceto pela face oposta e suas bordas (21 de 26 vistas possíveis):

-   A face voltada para você (não faz nada, já que essa é a visão atual)
-   As quatro bordas da face atual
-   Os quatro cantos da face atual
-   As quatro faces adjacentes
-   As quatro bordas que levam à face oposta
-   Os quatro cantos da face oposta

Não é possível:

-   A face oposta
-   As bordas da face oposta

Nota: No momento de escrever (v 0.18), o cubo de navegação tem alguns problemas. Nem todas as características são atualmente selecionáveis. Em particular, as bordas não podem ser selecionadas, nem os quatro cantos da face imediatamente oposta.

### Seleção de Faces {#seleção_de_faces}

Clicando em uma faceta orientará a visualização em 3D com essa faceta específica voltada para você. Como mencionado acima, há outros pontos de seleção disponíveis na visão facial. Há quatro \"barras\" finas em cada uma das bordas externas, representando as quatro facetas adjacentes; clicando nestas, seleciona-se a vista correspondente à faceta adjacente. Quatro cantos arredondados podem ser usados para definir a visão axonométrica correspondente. Há também um conjunto interno de bordas e cantos, que atualmente não são funcionais.

### Seleção de bordas {#seleção_de_bordas}

Infelizmente, a seleção de bordas está atualmente quebrada. A tentativa de selecionar uma borda selecionará a face por trás dela. Ao clicar em uma borda, você deve centralizá-la de modo que ela esteja de frente para você.

### Seleção de cantos {#seleção_de_cantos}

Clicando em um dos cantos você terá uma visão axonométrica a partir daquele canto. Como mencionado acima, atualmente, quando um rosto está diretamente voltado para você, os cantos desse rosto não podem ser selecionados.

## Menu mini-cubo {#menu_mini_cubo}

No canto inferior direito do cubo de navegação está um pequeno cubo. Clicando neste cubo, aparecerá um menu que você pode usar para mudar o tipo de vista (Ortográfica, Perspectiva, Isométrica) e para \"Zoom to Fit\".

## Movendo a exibição do cubo de navegação {#movendo_a_exibição_do_cubo_de_navegação}

Você pode mover toda a estrutura de controle do cubo de navegação para outro local na tela 3D, pressionando o mouse em qualquer lugar no cubo de navegação principal e arrastando. A estrutura não começará a se mover até que o ponteiro do mouse tenha passado a borda do cubo de navegação principal.

## Configuração

O cubo de navegação é configurável, incluindo o ajuste de seu tamanho: {{MenuCommand|Editar → Preferências... → Tela → Navegação → Cubo de Navegação }} <small>(v0.19)</small> .


<div class="mw-translate-fuzzy">

Para uma configuração mais avançada, consulte o **CubeMenu** [Bancadas de trabalho externas](External_workbenches/pt-br.md).


</div>







[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
