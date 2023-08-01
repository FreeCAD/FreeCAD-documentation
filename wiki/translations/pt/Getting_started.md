# Getting started/pt
{{TOCright}}



## Introdução


<div class="mw-translate-fuzzy">

O FreeCAD é uma [aplicação de modelação paramétrica](About_FreeCAD.md) 3D CAD/CAE . É primeiramente feita para desenho mecânico, mas também serve todos os outros usos onde seja necessário modelar objetos 3D com precisão e controlo sobre o processo/historial de modelação.


</div>


<div class="mw-translate-fuzzy">

O FreeCAD continua numa fase inicial de desenvolvimento, pelo que, apesar de já oferecer uma larga lista (que continua a crescer) de [funcionalidades](Feature_list.md), muito continua a faltar, especialmente quando comparado com soluções comerciais, pelo que pode não ser considerado suficientemente desenvolvido para utilização em ambiente de produção. Ainda assim, existe uma [comunidade](http://forum.freecadweb.org/index.php) em rápido crescimento de utilizadores entusiastas, e podem ser já encontrados [muitos exemplos](https://forum.freecadweb.org/viewforum.php?f=24) de projetos de qualidade desenvolvidos com o FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Tal como todos os projetos \"open-source\", O projeto FreeCAD não é um trabalho entregue pelos desenvolvedores em sentido único. Ele depende muito da sua comunidade para crescer, ganhar funcionalidades, e estabilidade (corrigir de bugs). Por isso convém não esquecer, quando começar a usar o FreeCAD, se gostar de trabalhar com ele, pode influenciar diretamente e [ajudar](Help_FreeCAD/pt.md) o projeto!


</div>

Ver também:


<div class="mw-translate-fuzzy">

-   [Migrar para o FreeCAD do Fusion360](Migrating_to_FreeCAD_from_Fusion360/pt.md)
-   [Tutoriais](Tutorials/pt.md)
-   [Tutoriais em video](Video_tutorials/pt.md)


</div>



## Instalação


<div class="mw-translate-fuzzy">

Antes de mais (se ainda não o fez) transfira e instale o FreeCAD. Veja a página [ Transferir](Download/pt.md) para informações acerca das versões mais recentes e atualizações, e a pagina [ instalação](Installing/pt.md) para informação sobre como instalar o FreeCAD. Existem pacotes de instalação prontos para o Windows (.msi), Ubuntu e Debian (.deb) openSUSE (.rpm) e Mac OSX. Como o FreeCAD é open-source, se for aventureiro, e quiser ver as funcionalidades novinhas em folha que estão a ser desenvolvidas mesmo agora, pode também descarregar o código fonte e [compilar](Compiling.md) o FreeCAD.


</div>




<div class="mw-translate-fuzzy">

## Explorando o FreeCAD 


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*O interface FreeCAD standard*


<div class="mw-translate-fuzzy">

1.  Vista 3D, mostrando o conteúdo do documento
2.  A vista em árvore, que mostra a hierarquia e o histórico da construção de todos os objetos do documento
3.  O [editor de propriedades](Property_editor/pt.md), que permite ver e modificar propriedades do(s) objeto(s) selecionado(s)
4.  A janela de mensagens, que é onde o FreeCAD apresenta mensagens, avisos e erros
5.  A consola python, onde todos os comandos executados pelo FreeCAD são apresentados, e onde se pode inserir código python
6.  O seletor de [bancadas de trabalho](Workbenches/pt.md), onde pode ser selecionada a bancada de trabalho ativa


</div>


<div class="mw-translate-fuzzy">

O conceito principal por detrás da interface do FreeCAD é a separação em [ bancadas de trabalho](workbenches/pt.md). Uma bancada de trabalho é uma coleção de ferramentas ajustadas a uma tarefa especifica, tal como trabalhar com [malhas (meshes)](Mesh_Workbench/pt.md), ou desenhar [objetos 2D (traços)](Draft_Workbench/pt.md), ou [esboços restringidos (sketches)](Sketcher_Workbench/pt.md). Pode mudar a bancada de trabalho ativa com o seletor de bancadas de trabalho(6). Pode [personalizar](Interface_Customization/pt.md) as ferramentas incluídas em cada bancada de trabalho, adicionar ferramentas de outras bancadas de trabalho ou mesmo ferramentas criadas por si, que nós chamamos [macros](macros/pt.md). Existe também uma bancada de trabalho generica que abarca as ferramentas mais comunmente utilizadas das outras bancadas, chamada **bancada de trabalho complete**.


</div>


<div class="mw-translate-fuzzy">

Quando você inicia o FreeCAD, pela primeira vez, é apresentada a página inicial do FreeCAD:


</div>

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">


<div class="mw-translate-fuzzy">

A página inicial do FreeCAD permite saltar rapidamente para uma das bancada de trabalho mais comuns, abrir um dos ficheiros recentes , ou ver as últimas notícias do universo FreeCAD. Pode alterar a bancada de trabalho predefinida em [preferências](Preferences_Editor.md).


</div>



## Navegação no espaço 3D 

O FreeCAD tem disponíveis vários [modos de navegação](Mouse_Model.md), que alteram a forma como usa o seu rato para interagir com os objetos nas vista 3D ou com a própria vista. Um deles foi especificamente feito para [touchpads](Mouse_Model#Touchpad_Navigation/pt.md), onde o botão do meio do rato não é utilizado. A tabela seguinte descreve o modo predefinido, chamado **Navegação CAD** (Pode mudar rapidamente o modo de navegação clicando com o botão direito do rato numa área vazia da vista 3D):


<div class="mw-translate-fuzzy">

Existem também diversas vistas predefinidas (vista de cima, vista de frente, etc) disponíveis no menu ver e na barra de ferramentas Ver, e através de atalhos numéricos (**1**, **2**, etc\...), ou clicando com o botão direito do rato num objeto ou numa área vazia da vista 3D, o que dá acesso rápido a algumas operações, como especificar uma determinada vista ou localizar um objeto na vista de árvore.


</div>



## Primeiros passos com o FreeCAD 


<div class="mw-translate-fuzzy">

O objetivo do FreeCAD é permitir fazer modelos 3D de alta precisão, manter o controlo apertado destes modelos (sendo capaz recuar no histórico da modelação e alterar parâmetros), para eventualmente construir esses modelos (via 3D printing, maquinação CNC ou até construção em estaleiro). É portanto muito diferente de algumas outras aplicações 3D feitas com outros propósitos, tais como animação ou jogos. A sua curva de aprendizagem pode ser íngreme, especialmente se for o seu primeiro contacto com a modelação 3D. Se ficar encalhado em certo ponto, não se esqueça da comunidade amigável de utilizadores no [FreeCAD forum](http://forum.freecadweb.org/index.php) que será capaz de o ajudar rapidamente.


</div>


<div class="mw-translate-fuzzy">

A bancada de trabalho que começará a utilizar depende do tipo de trabalho que precisa de fazer: se vai trabalhar em modelos de mecânica, ou mais genericamente quaisquer objetos de pequena escala, vai querer provavelmente experimentar a [Bancada de trabalho PartDesign (desenho de peças) ](PartDesign_Workbench/pt.md). Se vai trabalhar em 2D, então mude para a [bancada de trabalho Draft (traço) ](Draft_Workbench/pt.md), ou a [ bancada de trabalho Sketch (esboço)](Sketcher_Workbench/pt.md) se precisar de restrições. Se quer fazer BIM, lance a [ Bancada de trabalho Arch (arquitetura)](Arch_Workbench/pt.md). Se trabalha em desenho de barcos, existe a bancada especial [Bancada de trabalho Ship](Ship_Workbench/pt.md) para si. E se vem do universo do OpenSCAD, experimente a [ bancada de trabalho OpenSCAD](OpenSCAD_Workbench/pt.md).


</div>


<div class="mw-translate-fuzzy">

Pode alternar bancadas de trabalho a qualquer altura, e também [personalizar](Interface_Customization/pt.md) a sua bancada de trabalho favorita adicionando ferramentas de outras bancadas de trabalho.


</div>



## Trabalhar com as bancadas de trabalho PartDesign (desenho de peças) Sketcher (esboço) 


<div class="mw-translate-fuzzy">

A [ Bancada de trabalho PartDesign (Desenho de peças)](PartDesign_Workbench/pt.md) está especialmente talhada para a construção de objetos complexos, a aprtir de formas simples, e adicionando ou removendo peças (que nós chamamos \"features\"), até conseguir obter o objeto final. Todas as \"features\" aplicadas durante o processo de modelação são guardadas numa vista separada chamada [vista em árvore](Document_structure.md), que também contem outros objetos do documento. Podemos pensar no \"PartDesign\" como uma sucessão de operações, cada uma aplicada sobre o resultado da precedente, formando uma grande cadeia. Na vista em árvore , pode-se ver o objeto final, mas pode expandir-se e alcançar todos as fases anteriores, e alterar qualquer dos seus parâmetros, atualizando automaticamente o objeto final.


</div>


<div class="mw-translate-fuzzy">

A bancada de trabalho \"PartDesign\" faz uso intensivo de outra bancada de trabalho, A [Bancada de trabalho Sketcher (esboço)](Sketcher_Workbench/pt.md). Esta permite desenhar formas 2D, que são definidas aplicando restrições à forma 2D. Por exemplo, pode desenhar um retângulo e definir o tamanho de um lado aplicando uma restrição de comprimento a um dos lados. Esse lado deixa de puder ser redimensionado (a menos que a restrição seja alterada).


</div>

Estas formas 2D feitas com o \"sketcher\" são muito usadas na bancada de trabalho \"PartDesign\", por exemplo para criar um volume 3D , ou para desenhar áreas nas faces de objetos que serão depois escavadas ao volume principal. Este é um fluxo de trabalho típico do \"PartDesign\":

1.  Criar um novo sketch (esboço)
2.  desenhar uma forma fechada (assegure-se de que todos os pontos estão unidos)
3.  Fechar o sketch (esboço)
4.  Transformar o sketch (esboço) num solido 3D usando a ferramenta \"pad\"
5.  Selecionar uma face do sólido
6.  Criar um segundo sketch (esboço) (desta vez ele vai ser desenhado sobre a face selecionada)
7.  Desenhar uma forma fechada
8.  Fechar o sketch (esboço)
9.  Criar um pocket (bolso) a partir do segundo sketch (esboço), no primeiro objeto

Obtendo um objeto como este:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

A qualquer altura, pode selecionar o sketch (esboço) original e modificá-lo, ou alterar os parâmetros de extrusão das operações \"pad\" ou \"pocket\", atualizando assim o objeto final.



## Trabalhando com as bancadas de trabalho \"Draft\" (traço) e \"Arch\"(Arquitetura) 


<div class="mw-translate-fuzzy">

As [bancadas de trabalho \"Draft\" (traço)](Draft_Workbench/pt.md) e [Bancada de trabalho \"Arch\" (arquitetura)](Arch_Workbench/pt.md) comportam-se de forma um pouco diferente das bancadas de trabalho acima descritas, ainda assim seguem as mesmas regras, que são comuns a todo o FreeCAD. Resumindo, enquanto o \"Sketcher\" e \"PartDesign\" são feitas principalmente para desenhar peças individuais , \"Draft\" e \"Arch\" são feitas para facilitar, quando se trabalha, com diversas peças mais simples.


</div>


<div class="mw-translate-fuzzy">

A [Bancada de trabalho Draft (traço)](Draft_Workbench/pt.md) oferece ferramentas 2D parecidas com as que se encontram nas aplicações CAD tradicionais como o [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Contudo , O desenho 2D está longe de ser o objetivo do FreeCAD, por isso, não espere encontrar o conjunto completo de ferramentas que essas aplicações dedicadas oferecem. Muitas das ferramentas do \"Draft\" funcionam não só em 2D como na totalidade do espaço 3D, e beneficia de um sistema de ajuda especial como o [Planos de trabalho](Draft_SelectPlane.md) e [\"object snapping\"](Draft_Snap.md).


</div>


<div class="mw-translate-fuzzy">

A [bancada de trabalho \"Arch\" (Arquitetura)](Arch_Workbench/pt.md) acrescenta ferramentas [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) ao FreeCAD, permitindo construir modelos de arquitetura com objetos paramétricos. A bancada de trabalho \"Arch\" (Arquitetura) depende muito de outros módulos como o \"Draft\" (traço) e \"Sketcher\" (esboço). Todas as ferramentas do \"Draft\" estão também presentes bancada de trabalho \"Arch\" (Arquitetura), e muitas ferramentas \"Arch\" fazem uso dos sistemas de apoio e ajuda do \"Draft\".


</div>

O fluxo de trabalho típico com a as bancadas de trabalho \"Arch\" (Arquitetura) e \"Draft\" (traço) será:

1.  Desenhar algumas linhas com a ferramenta de **Linha** \"Draft\"
2.  Selecionar cada linha e clicar na ferramenta **Parede** para construir uma parede em cada uma delas
3.  Unir as paredes selecionando-as e pressionando a ferramenta **Adicionar** da bancada \"Arch\"
4.  Criar um objeto piso, e mover as paredes para dentro dele na vista de árvore
5.  Criar um objeto edifício, e mover o piso para dentro dele na vista de árvore
6.  criar uma janela clicando na ferramenta **Janela**, selecionar uma predefinição no painel, e depois clicar na face de uma parede
7.  Adicionar cotas dimensionais selecionando primeiro o plano de trabalho se necessário, e depois usando a ferramenta **Dimensão** do \"Draft\"

Obtendo isto:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

Mais em[ Tuturials](Tutorials.md).


</div>



## Addons, Macros e bancadas de trabalho externas 

O Freecad, sendo um software open source, dá a possibilidade de complementar as suas bancadas de trabalho com addons.

O princípio [Extensões](Addon/pt.md) é baseado no desenvolvimento de um complemento da bancada de trabalho. Qualquer utilizador pode desenvolver uma função que considere faltar para as suas próprias necessidades ou, em última instância, para a comunidade. Com o fórum, o utilizador pode solicitar uma opinião ou ajuda. Ele pode partilhar, ou não, o objeto de seu desenvolvimento de acordo com as regras de direitos autorais a definir. Gratuito para ela/ele. Para desenvolver, o utilizador tem disponíveis funções de [scripting](Power_users_hub/pt.md).

Existem dois tipos de addons:

1.  [Macros](Macros/pt.md): pequenos trechos de código Python que adicionam uma nova ferramenta ou funcionalidade. As macros normalmente começam como uma forma de simplificar ou automatizar a tarefa de desenhar ou editar um objecto em particular. Se muitas dessas macros são agrupadas dentro de um directório, o directório inteiro pode ser distribuído como uma nova bancada de trabalho.
2.  [Bancadas de trabalho externas](External_workbenches/pt.md): colecções de ferramentas programadas em Python ou C++ que ampliam de forma importante o Freecad . Se uma bancada de trabalho está suficientemente desenvolvida e bem documentada, pode até ser incluída como uma das bancadas de trabalho base dentro do Freecad. Em [Bancadas de trabalho externas](External_workbenches/pt.md), irá encontrar o fundamento de cada uma e uma lista das várias bancadas externas.



## Programação (Scripting) 

E finalmente, um dos recursos mais poderosos do FreeCAD é o ambiente de [ programação (scripting)](scripting.md). Desde da consola python integrada (ou a partir de qualquer outro script Python externo), pode obter acesso a praticamente qualquer parte do FreeCAD, criar ou modificar geometria, modificar a apresentação desses objetos na cena 3D ou aceder e modificar a interface do FreeCAD. A programação Python pode também ser usada em [ macros](macros/pt.md), que proporcionam um método fácil de criar comandos personalizados.




<div class="mw-translate-fuzzy">

## Novidades


</div>


<div class="mw-translate-fuzzy">

-   [Notas de lançamento da versão 0.17](Release_notes_0.17/pt.md) : Veja o que há de novo na versão 0.17 do FreeCAD
-   [Notas de lançamento da versão0.16](Release_notes_0.16/pt.md) : Veja o que há de novo na versão 0.16 do FreeCAD
-   \[\[Release notes 0.15/pt\|Notas de lançamento da versão

0.15\]\] : Veja o que há de novo na versão 0.15 do FreeCAD

-   [Notas de lançamento da versão 0.14](Release_notes_0.14.md) : Veja o que há de novo na versão 0.14 do FreeCAD
-   [Notas de lançamento da versão 0.13](Release_notes_0.13.md) : Veja o que há de novo na versão 0.13 do FreeCAD
-   [Notas de lançamento da versão 0.12](Release_notes_0.12.md) : Veja o que há de novo na versão 0.12 do FreeCAD
-   [Notas de lançamento da versão 0.11](Release_notes_0.11.md) : Veja o que há de novo na versão 0.11 do FreeCAD


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > Getting started/pt
