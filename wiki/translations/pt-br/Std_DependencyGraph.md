---
 GuiCommand:
   Name: Std DependencyGraph
   Localização do menu: Ferramentas , Gráfico de dependência...
   Bancadas: Todo
---

# Std DependencyGraph/pt-br


</div>



## Descrição


<div class="mw-translate-fuzzy">

O comando Std DependencyGraph exibe as dependências entre objetos no documento ativo em um \'gráfico de dependência\'. Ao contrário do modo de [Vista em árvore](Tree_view/pt-br.md), os objetos são listados em ordem cronológica inversa, com o primeiro objeto criado na parte inferior.


</div>

le pode ser útil na análise de um documento FreeCAD e na localização de bifurcações em uma árvore. O layout do gráfico de dependência dependerá de qual bancada de trabalho foi usada para criar os objetos no documento. Por exemplo, um modelo feito exclusivamente na bancada de trabalho [PartDesignpode](PartDesign_Workbench/pt-br.md) exibir um gráfico de dependência linear com uma única ramificação vertical. Um modelo feito com operações da bancada [Part](Part_Workbench/pt-br.md) terá muitas filiais, mas para uma única parte elas se juntarão no topo após as operações [booleanasbooleanas](Part_Boolean/pt-br.md). Se não o fizerem, significa que são objetos separados.

O gráfico de dependência é puramente uma ferramenta de visualização, portanto, não pode ser editado. Ele é atualizado automaticamente se forem feitas alterações no modelo.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width:400px;"> 
*Exemplo de um gráfico de dependência com um corpo PartDesign à esquerda e um objeto criado com operações Part à direita*



## Instalação


<div class="mw-translate-fuzzy">

Para usar o comando, um software de terceiros chamado [Graphviz](http://graphviz.org/)precisa ser instalado. Se você não o tiver pré-instalado ou se ele estiver instalado em um local não convencional, o FreeCAD exibirá a seguinte caixa de diálogo:


</div>

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows

Baixe o instalador do graphviz-2.xx na [página Download do Graphviz](https://graphviz.org/download/#windows) e inicie-o para instalá-lo. Algumas versões mais antigas parecem ter problemas para exibir o gráfico; A versão 2.38 e mais recente são conhecidas por serem confiáveis. Você pode encontrar todas as versões do graphviz no [Gitlab](https://gitlab.com/graphviz/graphviz/-/releases).

### macOS

Você pode instalar o Graphviz usando [Homebrew](https://brew.sh/) se tiver o macOS Big Sur (11) (ou superior). Ao instalar o Homebrew, não fique nervoso, se o macOS pedir que você instale atualizações, por exemplo, para as ferramentas de linha de comando do Xcode. Essas atualizações são executadas posteriormente pelo processo de instalação.


{{Code|lang=text|code=
brew install graphviz
}}

Isso instala os binários do Graphviz em **/usr/local/bin** para macOS na Intel ou **/opt/homebrew** para macOS no Apple Silicon/ARM. O FreeCAD deve encontrar automaticamente esses locais. Se o programa Graphviz não for encontrado, você será solicitado a especificar um caminho. Infelizmente, não podemos navegar diretamente para o programa na caixa de diálogo de arquivo que surge de **Ferramentas → gráfico de dependência...**. Há duas opções: Você pode usar a combinação de teclas Cmd+Shift+. para mostrar itens ocultos. Ou você pode usar a combinação de teclas Cmd+Shift+G para obter um campo de entrada para o caminho. Insira um destes caminhos no [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
/usr/local/bin
}}

ou:


{{Code|lang=text|code=
/opt/homebrew/bin
}}

e confirme o campo de entrada e a caixa de diálogo de seleção de arquivo.

Caso os binários do Graphviz estejam instalados em um local não padrão, tente encontrar o programa com o comando:


{{Code|lang=text|code=
type dot
}}

Ele produzirá algo como:


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

E você pode dizer ao FreeCAD para olhar nesse diretório.

Se você não tiver o macOS Big Sur (11) (ou superior) Homebrew pode não funcionar, mas você pode usar [MacPorts](https://www.macports.org/index.php) em vez disso. Basta baixar a [versão apropriada para o seu sistema operacional](https://www.macports.org/install.php). Quando a instalação estiver concluída, digite este comando no [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
sudo port install graphviz
}}

Digite sua senha e aguarde enquanto as dependências são baixadas e instaladas (pode levar algum tempo).

Os binários do Graphviz podem estar em **/usr/local/bin** ou **/opt/local/bin/dot**. FreeCAD pode encontrar automaticamente o programa Graphviz com a caixa de diálogo de arquivo que surge de **Ferramentas → gráfico de dependência ...**, se não digite este comando:


{{Code|lang=text|code=
type dot
}}

Ele produzirá algo como:


{{Code|lang=text|code=
dot is /opt/local/bin/dot
}}

E você pode dizer ao FreeCAD para olhar nesse diretório como explicado antes.

Também é possível tornar o diretório opt visível com este comando:


{{Code|lang=text|code=
defaults write com.apple.finder AppleShowAllFiles YES;
}}

então:


{{Code|lang=text|code=
killall Finder /System/Library/CoreServices/Finder.app;
}}

Portanto, você pode dizer ao FreeCAD para seguir este caminho. Ele foi testado com sucesso no macOS 10.13 (High Sierra).

### Linux

Na maioria das distribuições Linux (Debian/Ubuntu, Fedora, OpenSUSE), você só precisa instalar o pacote Graphviz a partir dos repositórios. No entanto, semelhante ao macOS, nos casos em que os binários do Graphviz estão instalados em um local não padrão, tente encontrar o programa com o comando:


{{Code|lang=text|code=
type dot
}}

Pode produzir algo como


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

E, portanto, você pode apontar FreeCAD para olhar nesse diretório.



## Utilização

1.  Selecione a opção **Ferramentas → <img src="images/Std_DependencyGraph.svg" width=16px> gráfico de dependência...** no menu.
2.  Uma nova guia intitulada Gráfico de dependência é aberta na [área de exibição Principal](Main_view_area/pt-br.md).
3.  Use a roda de rolagem do mouse para aumentar ou diminuir o zoom.
4.  Use os controles deslizantes na parte inferior e à direita da tela para deslocar a exibição. Como alternativa, mantenha pressionado o botão esquerdo do mouse e mova o mouse.



## Salvar

Você pode salvar um gráfico de dependência:

1.  Verifique se a guia Gráfico de dependência está em primeiro plano.
2.  Selecione a opção **Arquivo → [Salvar](Std_Save/pt-br.md)** ou **Arquivo → [→ Salvar como](Std_SaveAs/pt-br.md)** no menu.
3.  Digite um nome de arquivo e selecione o tipo de arquivo (\*.gv, \*.png, \*.bmp, \*.gif, \*.jpg, \*.svg ou \*.pdf).
4.  Pressione o botão **Salvar**.



## Princípios gerais 


<div class="mw-translate-fuzzy">

-   O gráfico mostra objetos em ordem cronológica inversa.
-   A direção das setas que mostram dependências deve sempre apontar para baixo, do objeto filho para o objeto pai. \* Uma seta apontando para cima indica uma dependência cíclica, um problema que precisa ser resolvido.
-   Um esboço que contém links para [geometria externa](Sketcher_External/pt-br.md) terá um número com um sufixo \'x\' além da seta ligando-o ao seu pai, mostrando o número de geometrias externas vinculadas no esboço.
-   Os objetos podem ter dependências para vários pais. Por exemplo, para um modelo construído no [PartDesign](PartDesign_Workbench/pt-br.md), um Pocket pode ser vinculado ao seu Sketch e ao recurso Pad que veio antes dele.
-   As dependências não permitidas (por exemplo, entre uma operação [Draft](Draft_Workbench/pt-br.md)/[Part](Part_Workbench/pt-br.md) e um elemento dentro de um PartDesign Body) serão exibidas com uma seta vermelha. Esse tipo de link geralmente mostra um erro \"Links saem do escopo permitido\" na [visualização de Relatório](Report_view/pt-br.md).
-   Um [contêiner Part](Std_Part/pt-br.md) e [PartDesign Body](PartDesign_Body/pt-br.md) colocam seu conteúdo dentro de um quadro com um plano de fundo colorido aleatoriamente. Sua Origem também encerra seu conteúdo (planos e eixos padrão) em um quadro.
-   Um [Grupo](Std_Group/pt-br.md) é exibido como um único elemento vinculado ao seu conteúdo.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [3rd_Party](Category_3rd_Party.md) > Std DependencyGraph/pt-br
