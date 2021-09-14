# Getting started/pt-br




<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Prefácio

FreeCAD é uma aplicação de modelagem 3D [aplicação de modelagem paramétrica](About_FreeCAD/pt-br.md). Ele é feito principalmente para projetos mecânicos, mas também serve a todos os outros usos onde você precisa modelar objetos 3D com precisão e controle sobre o histórico da modelagem.

O FreeCAD está em desenvolvimento desde 2002 e oferece uma grande lista de [ recursos](Feature_list/pt-br.md). Ainda faltam recursos, mas elas são suficientemente poderosas para o uso por hobby e pequenas oficinas. Existe uma comunidade em rápido crescimento de usuários entusiastas que participam do [fórum do FreeCAD](http://forum.freecadweb.org/index.php) e você pode encontrar nele muitos [exemplos](https://forum.freecadweb.org/viewforum.php?f=24) de projetos de qualidade desenvolvidos com o FreeCAD. Veja também, [FreeCAD usado na produção](FreeCAD_used_in_production/pt-br.md).

Como todos os projetos de software livre, o FreeCAD depende de sua comunidade para crescer, ganhar recursos e corrigir bugs. Não se esqueça disso ao usar o FreeCAD; se você gostar, pode [doar](Donate/pt-br.md) e [ajude o FreeCAD](Help_FreeCAD/pt-br.md) de várias maneiras, como escrever documentação e fazer traduções.

Veja também:

-   [Migrando para o FreeCAD do Fusion360](Migrating_to_FreeCAD_from_Fusion360/pt-br.md)
-   [Tutoriais](Tutorials/pt-br.md)
-   [Tutorials em video](Video_tutorials/pt-br.md)

## Instalação

Primeiramente, baixe e instale o FreeCAD. Consulte a página [Download](Download/pt-br.md) para obter informações sobre versões e atualizações atuais e a instruções de instalação para seu sistema operacional ([Windows](Installing_on_Windows/pt-br.md), [Linux](Installing_on_Linux/pt-br.md) ou [Mac](Installing_on_Mac/pt-br.md)). Existem pacotes de instalação prontos para Windows (.msi), Debian e Ubuntu (.deb), openSUSE (.rpm) e Mac OSX. O FreeCAD está disponível nos gerenciadores de pacotes de muitas outras distribuições Linux. Também está disponível um executável [AppImage](AppImage/pt-br.md) independente, que será executado nos sistemas Linux de 64 bits mais recentes. Como o FreeCAD é de código aberto, você também pode pegar o código-fonte e [compilá-lo](Compiling.md).

## Explorando a interface 

=

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;"> 
*Interface padrão FreeCAD em 0.19.*


</div>


**Ver uma explicação completa em [Interface](Interface/pt-br.md).**


:   1\. O [área de visão principal](main_view_area/pt-br.md), que pode conter diferentes janelas com abas, principalmente o [3D view](3D_view/pt-br.md).
:   2\. A [3D view](3D_view/pt-br.md), que mostra os objetos geométricos do documento.
:   3\. A [vista em árvore](tree_view/pt-br.md). (parte do [visualização combinada](combo_view/pt-br.md)), mostrando a hierarquia e o histórico de construção dos objetos no documento; também pode exibir o [painel\_de\_tarefa](task_panel/pt-br.md) para comandos ativos.
:   4\. O editor [editor de propriedade](property_editor/pt-br.md). (parte do [visualização combinada](combo_view/pt-br.md)), que permite visualizar e modificar as propriedades dos objetos selecionados.
:   5\. A [vista de seleção](selection_view/pt-br.md), que indica os objetos ou subelementos dos objetos (vértices, bordas, faces) que são selecionados.
:   6\. A [visualização de relatório](report_view/pt-br.md). (ou janela de saída), onde são mostradas mensagens, avisos e erros.
:   7\. O [console Python](Python_console/pt-br.md), onde todos os comandos executados são impressos, e onde você pode digitar o código [Python](Python/pt-br.md).
:   8\. A [barra de status](status_bar/pt-br.md), onde algumas mensagens e dicas de ferramentas aparecem.
:   9\. A área da barra de ferramentas, onde as barras de ferramentas estão ancoradas.
:   10\. O [seletor de bancada](Std_Workbench/pt-br.md), onde você seleciona a [bancada de trabalho](workbenches/pt-br.md) ativa.
:   11\. O [menu padrão](Standard_Menu/pt-br.md), que contém as operações básicas do programa.


<div class="mw-translate-fuzzy">

O principal conceito por trás da interface do FreeCAD é que está separada em [bancadas de trabalho](workbenches/pt-br.md). Uma bancada de trabalho é uma coleção de ferramentas agrupadas para uma tarefa específica, como trabalhos com [malhas](Mesh_Workbench/pt-br.md), desenhos de [objetos 2D](Draft_Workbench/pt-br.md) ou [esboços restritos](Sketcher_Workbench/pt-br.md). Você pode alternar o ambiente de trabalho atual com o [ seletor de bancada de trabalho](Std_Workbench/pt-br.md). Você pode [ customizar](Interface_Customization/pt-br.md) as ferramentas incluídas em cada ambiente de trabalho, adicionar ferramentas de outros ambientes ou até mesmo ferramentas criadas por nós, que chamamos de [ macros](macros/pt-br.md). Os pontos de partida amplamente utilizados são o [ bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md) e o [ bancada de trabalho Part](Part_Workbench/pt-br.md).


</div>

Quando você inicia o FreeCAD pela primeira vez, é apresentado ao Start Center. Veja como aparace o Start Center na versão 0.18:

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;"> 
*Para FreeCAD 0.17 veja esta [start center](Media:Startcenter0.17.jpg.md) screenshot.*


</div>


<div class="mw-translate-fuzzy">

O Start Center te permite saltar rapidamente para as bancadas de trabalho mais comuns, abrir arquivos recentes ou ver as últimas novidades do universo FreeCAD. Você pode alterar a bancada de trabalho predefinida em [Preferências](Preferences_Editor.md).


</div>

## Navegando no espaço 3D 


<div class="mw-translate-fuzzy">

FreeCAD tem vários modos diferentes [estilos de navegação](Mouse_Model/pt-br.md) disponíveis, que mudam a maneira como você usa o mouse para interagir com os objetos na visualização 3D e a própria visualização. Um deles é feito especificamente para [touchpads](Mouse_Model/pt-br#Navegação_Touchpad.md), onde o botão do meio do mouse não é usado. A tabela a seguir descreve o modo padrão, chamado *\'Navegação CAD* (Você pode mudar rapidamente o modo de navegação atual clicando com o botão direito do mouse em uma área vazia da visualização 3D):


</div>


{{CAD Navigation
|Select_name=Selecionar
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista<br>Primeiro método
|Rotate_view_alt_name=Rotacionar vista<br>Método alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.

Manter pressionado **Ctrl** permite a seleção de múltiplos objetos.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.
|Pan_mode_text=Pan mode: segure a tecla **Ctrl**, pressione o botão direito do mouse uma vez, depois mova o ponteiro. <small>(v0.17)</small> 
|Zoom_text=Utilizar a roda do mouse para aumentar e diminuir o zoom.

Clicando no botão do meio do mouse, a vista é centrada novamente na localização do cursor.
|Zoom_mode_text=Zoom mode: segure as teclas **Ctrl** e **Shift**, pressione o botão direito do mouse uma vez, depois mova o ponteiro. 
<small>(v0.17)</small> 
|Rotate_view_text=Segure o botão central do mouse, depois pressione e segure o botão esquerdo do mouse, depois mova o ponteiro.

A localização do cursor quando o botão central do mouse é pressionado determina o centro de rotação. A rotação funciona como girar uma bola que gira ao redor de seu centro. Se os botões forem soltos antes de você parar o movimento do mouse, a visualização continua [girando](Std_DemoMode/pt-br.md), se isto estiver habilitado.

Um duplo clique com o botão do meio do mouse define um novo centro de rotação.
|Rotate_view_mode_text=Rotate mode: pressione a tecla **Shift**, pressione o botão direito do mouse uma vez, depois mova o ponteiro. <small>(v0.17)</small> 
|Rotate_view_alt_text=Segure o botão central do mouse, depois pressione e segure o botão direito do mouse, depois mova o ponteiro.

Com este método, o botão central do mouse pode ser solto depois que o botão direito do mouse for pressionado.

Os usuários que usam o mouse com a mão direita podem achar este método mais fácil do que o primeiro método.}}

Você também tem várias predefinições de visualização (vista superior, vista frontal, etc.) disponíveis no menu Ver, na barra de ferramentas Ver, e por atalhos numéricos (**1**, **2**, etc\...). Clicando com o botão direito do mouse em um objeto ou em uma área vazia da visualização 3D, você tem acesso rápido a algumas operações comuns, tais como definir uma determinada visualização, ou localizar um objeto na visualização em árvore.

## Primeiros passos com FreeCAD 

O foco do FreeCAD é permitir fazer modelos 3D de alta precisão, manter um controle rigoroso sobre esses modelos (poder voltar ao histórico de modelagem e alterar parâmetros), e eventualmente construir esses modelos (via impressão 3D, usinagem CNC ou mesmo canteiro de obras). Portanto, é muito diferente de algumas outras aplicações 3D feitas para outros fins, tais como filme de animação ou jogos. Sua curva de aprendizado pode ser íngreme, especialmente se este for seu primeiro contato com a modelagem 3D. Se você for atingido em algum momento, não se esqueça que a comunidade amigável de usuários no [FreeCAD forum](http://forum.freecadweb.org/index.php) pode ser capaz de tirá-lo de lá em pouco tempo.


<div class="mw-translate-fuzzy">

A bancada de trabalho que você começará a usar no FreeCAD depende do tipo de trabalho que você precisa fazer: Se você vai trabalhar em modelos mecânicos, ou mais geralmente qualquer objeto de pequena escala, você provavelmente vai querer experimentar o [Bancadas de trabalho PartDesign](PartDesign_Workbench/pt-br.md). Se você vai trabalhar em 2D, então mude para o [Bancada de trabalho Draft](Draft_Workbench/pt-br.md), ou para o [Bancada de trabalho Sketcher](Sketcher_Workbench/pt-br.md) se você precisar de restrições. Se você quiser fazer o BIM, abra o [Bancadas de trabalho Arch](Arch_Workbench/pt-br.md). E se você vem do mundo OpenSCAD, experimente o [Bancadas de trabalho OpenSCAD ](OpenSCAD_Workbench/pt-br.md). Há também muitos [Bancadas de trabalho externas](External_workbenches/pt-br.md) desenvolvidos pela comunidade disponíveis.


</div>


<div class="mw-translate-fuzzy">

Você pode trocar de bancada de trabalho a qualquer momento, e também [customizar](Interface_Customization/pt-br.md) sua bancada de trabalho favorita para adicionar ferramentas de outras bancadas de trabalho.


</div>

## Trabalhando com as bancadas PartDesign e Sketcher 


<div class="mw-translate-fuzzy">

O [Bancadas de trabalho PartDesign](PartDesign_Workbench/pt-br.md) é feito para construir objetos complexos, a partir de formas simples, e adicionar ou remover peças (chamadas de \"características\"), até chegar ao seu objeto final. Todas as características que você aplicou durante o processo de modelagem são armazenadas em uma visão separada chamada [vista de árvore](Document_structure/pt-br.md), que também contém os outros objetos em seu documento. Você pode pensar em um objeto PartDesign como uma sucessão de operações, cada uma aplicada ao resultado do anterior, formando uma grande cadeia. Na visualização em árvore, você vê seu objeto final, mas pode expandi-lo e recuperar todos os estados anteriores, e alterar qualquer um de seus parâmetros, o que atualiza automaticamente o objeto final.


</div>


<div class="mw-translate-fuzzy">

A bancada de trabalho PartDesign faz uso pesado de outra bancada de trabalho, a [Bancada de trabalho Sketcher](Sketcher_Workbench/pt-br.md). O desenhista permite desenhar formas 2D, que são definidas pela aplicação de Restrições à forma 2D. Por exemplo, você pode desenhar um retângulo e definir o tamanho de um lado, aplicando uma restrição de comprimento a um dos lados. Esse lado então não pode mais ser redimensionado (a menos que a restrição seja alterada).


</div>

Essas formas 2D feitas com o desenhista são muito utilizadas na bancada de trabalho PartDesign, por exemplo para criar volumes 3D, ou para desenhar áreas nas faces de seu objeto que serão então escavadas a partir de seu volume principal. Este é um fluxo de trabalho típico do PartDesign:

1.  Criar um novo sketch (esboço)
2.  desenhar uma forma fechada (assegure-se de que todos os pontos estão unidos)
3.  Fechar o sketch (esboço)
4.  Transformar o sketch (esboço) num solido 3D usando a ferramenta \"pad\"
5.  Selecionar uma face do sólido
6.  Criar um segundo sketch (esboço) (desta vez ele vai ser desenhado sobre a face selecionada)
7.  Desenhar uma forma fechada
8.  Fechar o sketch (esboço)
9.  Criar um pocket (bolso) a partir do segundo sketch (esboço), no primeiro objeto

O que lhe dá um objeto como este:

<img alt="" src=images/Partdesign_example.jpg  style="width:1024px;">

A qualquer momento, você pode selecionar os esboços originais e modificá-los, ou alterar os parâmetros de extrusão das operações de bloco ou bolso, o que atualizará o objeto final.

## Trabalhando com as bancadas Draft e Arch 


<div class="mw-translate-fuzzy">

O [Bancada de Trabalho Draft](Draft_Workbench/pt-br.md) e o [Bancada de Trabalho Arch](Arch_Workbench/pt-br.md) comportam-se de forma um pouco diferente dos outros bancos de trabalho acima, embora sigam as mesmas regras, que são comuns a todos os FreeCAD. Em resumo, enquanto o Sketcher e o PartDesign são feitos principalmente para desenhar peças únicas, o Draft e o Arch são feitos para facilitar seu trabalho quando se trabalha com vários objetos mais simples.


</div>


<div class="mw-translate-fuzzy">

A [bancada de trabalho Draft](Draft_Workbench/pt-br.md) oferece ferramentas 2D um pouco semelhantes ao que você pode encontrar em aplicações CAD 2D tradicionais, tais como [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Entretanto, estando o esboço 2D longe do escopo do FreeCAD, não espere encontrar ali toda a gama de ferramentas que estas aplicações dedicadas oferecem. A maioria das ferramentas de rascunho funciona não apenas em um plano 2D, mas também em todo o espaço 3D, e se beneficia de sistemas de ajuda especiais como [Work planes](Draft_SelectPlane/pt-br.md) e [object snapping](Draft_Snap/pt-br.md).


</div>


<div class="mw-translate-fuzzy">

A [bancada de trabalho Arch](Arch_Workbench.md) acrescenta a ferramentas [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) ao FreeCAD, permitindo construir modelos arquitetônicos com objetos paramétricos. A bancada de trabalho Arch se baseia amplamente em outros módulos, como Draft e Sketcher. Todas as ferramentas Draft também estão presentes no bancada de trabalho Arch, e a maioria das ferramentas Arch faz uso dos sistemas de ajuda Draft.


</div>

O fluxo de trabalho típico com a as bancadas de trabalho \"Arch\" (Arquitetura) e \"Draft\" (traço) será:

1.  Desenhar algumas linhas com a ferramenta de **Linha** \"Draft\"
2.  Selecionar cada linha e clicar na ferramenta **Parede** para construir uma parede em cada uma delas
3.  Unir as paredes selecionando-as e pressionando a ferramenta **Adicionar** da bancada \"Arch\"
4.  Criar um objeto piso, e mover as paredes para dentro dele na vista de árvore
5.  Criar um objeto edifício, e mover o piso para dentro dele na vista de árvore
6.  criar uma janela clicando na ferramenta **Janela**, selecionar uma predefinição no painel, e depois clicar na face de uma parede
7.  Adicionar cotas dimensionais selecionando primeiro o plano de trabalho se necessário, e depois usando a ferramenta **Dimensão** do \"Draft\"

O que lhe dará isto:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:1024px;">

Para mais informações, visite a página [Tutoriais](Tutorials.md) .

## Addons, Macro e Bancadas Externas 

O Freecad, como um software de código aberto, oferece a possibilidade de complementar suas bancadas de trabalho com addons.

O princípio [Extensões](Addon/pt-br.md) é baseado no desenvolvimento de um complemento de bancada de trabalho. Qualquer usuário pode desenvolver uma função que ele ou ela considere faltar para suas próprias necessidades ou, em última instância, para a comunidade. Com o fórum, o usuário pode solicitar uma opinião, ajuda no fórum. Ele pode compartilhar, ou não, o objeto de seu desenvolvimento de acordo com as regras de direitos autorais a definir. Livre para ela/ele. Para desenvolver, o usuário tem disponíveis funções [scripting](Power_users_hub/pt-br.md).


<div class="mw-translate-fuzzy">

Há dois tipos de extensões:

1.  [Macros](Macros/pt-br.md): pequenos trechos de código Python que fornecem uma nova ferramenta ou funcionalidade. As macros geralmente começam como uma forma de simplificar ou automatizar a tarefa de desenhar ou editar um determinado objeto. Se muitas destas macros forem coletadas dentro de um diretório, o diretório inteiro pode ser distribuído como uma nova bancada de trabalho.
2.  [ Bancadas de trabalho externas](External_workbenches/pt-br.md): coleções de ferramentas programadas em Python ou C++ que estendem o FreeCAD de uma forma importante. Se uma bancada de trabalho estiver suficientemente desenvolvida e bem documentada, ela pode ser incluída como uma das bancadas de trabalho de base no FreeCAD. Em [bancos de trabalho externos](External_workbenches/pt-br.md), você encontrará o princípio e uma lista da biblioteca existente.


</div>

## Scripting

E, finalmente, um dos recursos mais poderosos do FreeCAD é o ambiente [ scripting](scripting.md). No console python integrado (ou em qualquer outro script Python externo) você pode acessar quase qualquer parte do FreeCAD, criar ou modificar geometria, modificar a representação desses objetos na cena 3D ou acessar e modificar a interface do FreeCAD. O script Python também pode ser usado em [ macros](macros.md), que fornece um método fácil para criar comandos personalizados.

## Novidades

-   Veja as [notas de lançamento](Feature_list/pt-br#Notas_de_lançamento.md) para uma lista detalhada de recursos.


<div class="mw-translate-fuzzy">





</div>




[Category:User\_Documentation/pt-br](Category:User_Documentation/pt-br.md)
