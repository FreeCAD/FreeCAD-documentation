# Frequently asked questions/pt-br
Esta página apresenta respostas para algumas das perguntas mais comuns e que são feitas nos fóruns do FreeCAD. Se você tiver algum problema ou alguma dúvida sobre o FreeCAD, aqui é o primeiro lugar onde deve procurar por respostas. Se você não encontrar a resposta aqui, procure tirar sua dúvida no [fórum do FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3)!

## Instalação

### Qual é a maneira mais fácil de instalar o FreeCAD no meu sistema? 


<div class="mw-translate-fuzzy">

Se você estiver no Windows ou Mac OS, a maneira mais simples é ir à página [Download](Download.md), que reúne os instaladores prontos para você baixar. Se você estiver usando Debian, Fedora ou Ubuntu, entre outras distribuições Linux, o FreeCAD está incluído nos repositórios de software padrão e você pode simplesmente instalá-lo com o gerenciador de software. No Ubuntu, a equipe do FreeCAD também mantém seus próprios [Repositórios PPA](Installing_on_Linux/pt-br#Desenvolvimento_PPA.md). Para mais detalhes sobre como instalar o FreeCAD, consulte a página de instalação relacionado ao seu sistema operacional: ([Windows](Installing_on_Windows/pt-br.md), [Linux](Installing_on_Linux/pt-br.md) ou [Mac](Installing_on_Mac/pt-br.md)).


</div>

### Quais os pré-requisitos para executar o FreeCAD? 

Em contraste com a maioria dos softwares CAD 3D, o FreeCAD pode funcionar sem problemas em computadores mais modestos - é conhecido por funcionar em CPUs Pentium IV e Intel Core2 Solo. Se o seu computador estiver rodando um sistema operacional atual, é provável que o FreeCAD seja executado. O único pré-requisito é que sua placa gráfica ou chipset deve suportar a tecnologia [OpenGL](https://en.wikipedia.org/wiki/OpenGL), de preferência da versão 2.0 em dinte. Em caso de problemas, consulte a seção [Solução de problemas](Frequently_asked_questions/pt-br#Solução_de_problemas.md) desta FAQ.

#### Multitarefa

Neste momento, o núcleo de modelagem geométrica subjacente do FreeCAD (composto pela biblioteca [OpenCASCADE Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology)) tem suporte parcial para multitarefa. Veja a página [multithreading](multithreading/pt-br.md) para mais detalhes.

#### Para usuários de Mac 

Somente a arquitetura MacIntel é suportada. Não há builds disponíveis para a arquitetura PowerPC.

### E se eu quiser compilar o FreeCAD sozinho? 

O código fonte do FreeCAD está sempre disponível no repositório de código-fonte do projeto. Você pode compilar o FreeCAD por conta própria, caso queira utilizar os recursos mais recentes em desenvolvimento. Para saber compilar, é preciso ter um pouco de conhecimento de informática. Acreditamos, porém, que o procedimento simples de realizar. Na página [aqui](Compile_on_Linux/pt-br#obtendo_a_fonte.md) explicamos como ter acesso ao código-fonte, e existem instruções detalhadas para compilar o código nas páginas [Compilar para Windows](Compile_on_Windows/pt-br.md), [Compilar para Linux](Compile_on_Linux/pt-br.md) e [Compilar para MacOS](Compile_on_MacOS/pt-br.md).

### O FreeCAD me diz que algum módulo ou aplicativo está faltando 

O FreeCAD depende de várias peças para oferecer todas as suas funcionalidades. Todos os principais componentes são agrupados dentro das instalações do FreeCAD (para Windows ou Mac) ou fornecidos pelo seu gerenciador de pacotes, no caso de distribuições Linux. Normalmente, portanto, você não tem com o que se preocupar. Se você instalou o FreeCAD a partir de fontes não-oficiais, ou se você mesmo compilou o FreeCAD, alguma peça pode estar faltando. A falta de um componente não compromete o funcionamento do FreeCAD, mas pode causar a indisponibilidade de alguma ferramenta.

Alguns componentes utilizados para a importação e exportação de alguns tipos de formatos de arquivo, como Collada ou DWG, não podem fazer parte dos pacotes de instalação do FreeCAD. Nestes casos, você mesmo deve realizar a instalação dos componentes.

Todos esses componentes e a maneira apropriada de instalá-los estão listados na página [Módulos python extras](Extra_python_modules/pt-br.md)

## Solução de problemas 

### O FreeCAD não inicia de forma alguma 

Pode haver muitas razões para isso. A mais provável é que falte alguma biblioteca. Tente iniciar o FreeCAD a partir de um terminal (digite {{SystemInput|freecad}} em um prompt de comando, {{SystemInput|FreeCAD}} em alguns sistemas) para ver se alguma mensagem de erro aparece. Leia também o restante deste FAQ, pois aqui podem ter mais pistas para detectar a causa do problema. Se nada der certo, procure por auxílio no [forum](http://forum.freecadweb.org/), certamente haverá alguém que poderá ajudar.

Em alguns Windows mais antigos, como o XP, você pode receber esta mensagem de erro: **A aplicação não pode iniciar, porque a configuração lado a lado está errada. A reinstalação do aplicativo pode resolver o problema.**

Este problema pode ocorrer devido à falta de bibliotecas de tempo de execução CRT, ou a versão instalada destas bibliotecas é mais antiga que a versão vinculada à versão do FreeCAD que você está tentando instalar. Neste caso, será preciso instalar o **Microsoft Visual C++ Redistributable Package** que você encontrará no site da Microsoft. Veja também a [mensagem no fórum](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961) que trata do assunto.

### FreeCAD inicia normalmente, mas nem todos os ícones são exibidos; alguns são substituídos por um \'X\' preto 

Algumas partes do FreeCAD dependem de um módulo Python externo chamado Pivy. Na instalação do FreeCAD para Windows, o Pivy está incluído. Em sistemas Debian/Ubuntu, o pacote python-pivy é disponível, por padrão, nos respectivos repositórios. Em outros sistemas, no momento, você mesmo pode ter que compilar o Pivy. Note que, embora algumas ferramentas não estejam disponíveis sem o Pivy instalado, o resto do FreeCAD funciona normalmente.

### Tenho problemas de visualização, a vista 3D não se comporta corretamente, há lixo quando movo ou rotaciono a vista, etc. 

O FreeCAD depende do OpenGL para exibir conteúdos 3D, e portanto requer que o ambiente OpenGL esteja funcionando corretamente. Em alguns sistemas, o OpenGL não é ativado por padrão, e você precisará ativá-lo no software da sua placa gráfica. Se isto não funcionar, talvez seja preciso, instalar ou atualizar os drivers da sua placa de vídeo. Este problema acontece com mais frequência em sistemas Linux ou em sistemas virtuais. Se você estiver em um sistema baseado em Linux, tente os seguintes passos:

-   verifique se seu computador possui uma placa gráfica com capacidade 3D
-   digite {{SystemInput|glxinfo}} em um terminal e verifique se saída de vídeo tem a configuração Renderização Direta definida como \"sim\", e que o fornecedor/renderizador/versão OpenGL corresponde à versão da sua placa gráfica.
-   instale outro software baseado em OpenGL ([Blender](http://www.blender.org), por exemplo) e verifique se ele roda e exibe corretamente.

### O FreeCAD falha na inicialização 

Um crash pode ser um sintoma de um bug mais sério, ou algum problema em sua configuração. A maior parte das falhas na inicialização ocorre devido a uma das razões a seguir:

#### Os drivers OpenGL não estão instalados ou não estão funcionando corretamente 

Esta é uma causa muito comum. Neste caso, o FreeCAD simplesmente trava na inicialização ou sempre que você abre uma visualização 3D (por exemplo, criando um novo documento).

Tente descobrir qual é seu chip gráfico ou placa de vídeo e depois verifique se ele suporta [OpenGL](https://en.wikipedia.org/wiki/OpenGL). A seguir, verifique se o driver correto está instalado, Se não estiver, encontre o driver correto e instale-o. Uma boa maneira de verificar se OpenGL está disponível é tentar executar outro aplicativo que faz uso de OpenGL, como o [blender](http://www.blender.org).


<div class="mw-translate-fuzzy">

Para obter mais informações sobre travamentos do seu FreeCAD, inicie-o utilizando o parâmetro {{SystemInput|--write-log}}}. Isto criará o arquivo {**FreeCAD.log**}, localizado em {**$HOME/.FreeCAD**} no Linux e Mac OS X, ou na pasta {**%APPDATA%/FreeCAD** em sistemas Windows.
</div>

<div class="mw-translate-fuzzy">
Em alguns casos raros, você pode ter um driver de vídeo instalado que não é compatível com sua placa gráfica. Tivemos um caso em que o laptop do usuário tinha um chipset Intel on-board, mas alguns drivers ATI estavam instalados. [http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042]
Depois de remover os arquivos da ATI e reinstalar o driver correto, o FreeCAD começou a funcionar.
</div>

==== Alguma biblioteca, necessária para o FreeCAD, não está presente em seu sistema, ou não foi encontrada pelo FreeCAD ====

Pode haver duas possibilidades para este problema: ou falta simplesmente uma biblioteca, então o FreeCAD se recusará a começar, ou a biblioteca está lá, mas é uma versão mais antiga do que o FreeCAD espera, então ocorrerá um crash quando o FreeCAD tentar usar um recurso ausente daquela biblioteca. Um exemplo comum é que quando ambos Qt3 e Qt4 são instalados em seu sistema, o FreeCAD pode detectar Qt4, mas se sua instalação de Qt não estiver devidamente configurada, algumas peças de Qt3 ainda podem ser usadas, causando falhas.

Favor rever o procedimento de instalação ([Windows](Installing_on_Windows/pt-br.md), [Linux](Installing_on_Linux/pt-br.md) ou [Mac](Installing_on_Mac/pt-br.md)),  certifique-se de instalar todas as bibliotecas necessárias (na maioria dos sistemas linux isso é feito automaticamente), e verifique qual é o número mínimo de versão para cada um dos componentes.

Se tudo parecer correto, descreva o problema no [http://forum.freecadweb.org/ forum] ou [enviar um bug](Tracker/pt-br.md). Se você estiver em um sistema linux, é fácil fazer um backtrace debug, que fornece informações muito úteis sobre a falha para os desenvolvedores:
* em um terminal, tipo: {{SystemInput|gdb freecad}} (assumindo que o pacote gdb esteja instalado)
* dentro de gdb, digite {{SystemInput|run}}
* após o acidente, digite {{SystemInput|bt}} para obter o relatório de erro, que você pode incluir em seu relatório de erro.

=== FreeCAD congela após a inicialização ===

Ao iniciar o FreeCAD, a GUI aparece quase imediatamente, mas a GUI é congelada e o processador está aproximadamente em 99%. Isto pode acontecer na área de trabalho do KDE quando se utiliza o tema Oxygen. Este é um bug no tema Oxygen e a escolha de outro tema deve resolver este problema.

=== FreeCAD trava ao criar um novo documento ou abrir um arquivo ===

Se o FreeCAD falhar ao criar uma nova visualização 3D, tente iniciar o FreeCAD a partir de um terminal. Se uma mensagem de erro aparecer quando o travamento ocorrer, mencionando {{SystemOutput|Assertion Failed}}, e um nome de componente começando com "So" ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, etc.), as chances são muito altas, especialmente se você estiver no Linux, que o FreeCAD esteja tentando usar duas versões diferentes da biblioteca Coin, o que causa o travamento.
Para verificar se esse é de fato o problema, tente o seguinte:
* Localize o executável FreeCAD (geralmente em **/usr/lib/FreeCAD/bin**)
* Execute o comando {{{SystemInput|ldd FreeCAD}} a partir de um terminal
* Anote a versão da biblioteca {**libCoin.so**} que o FreeCAD está usando (por exemplo **libCoin.so.60**)

-   Localize a biblioteca {**libSoQt.so**} (geralmente em **/usr/lib**})
-   correr {{{SystemInput|ldd libSoQt.so}}} e verifique se ele se liga à mesma versão Coin do FreeCAD

Se houver alguma diferença, o FreeCAD ou o SoQt devem ser recompilados (melhor recompilar aquele que usa a versão mais antiga da Coin). O comportamento normal é tentar contatar as pessoas responsáveis pela embalagem do SoQt ou do FreeCAD e gentilmente pedir-lhes que considerem a recompilação. Se você quiser dar esse passo por si mesmo, e não for possível recompilar o SoQt porque ele quebra outras aplicações em seu sistema, você pode forçar o FreeCAD a compilar com a versão Coin necessária com {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. Mas você tem que ter certeza de que o pacote de desenvolvimento correto desta versão Coin está instalado.

### FreeCAD trava após a Editar → Alinhamento 

Uma falha de segmentação acontece em {{SystemOutput|vbo_save_playback_vertex_list()}}. Isto significa que a implementação do VBO no driver gráfico é ruim. A fim de evitar o cache de chamadas OpenGL você pode tentar definir a variável de ambiente {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} e reiniciar o FreeCAD.

### Tenho problemas para executar o FreeCAD no Mac OSX 

Não é tão fácil dar um suporte adequado para plataforma Mac (o que não ocorre com as versões para Windows ou Linux) porque nenhum dos principais desenvolvedores possui um.

Os pacotes OSX são compilados por usuários voluntários do FreeCAD, e pode ser que não funcionem corretamente em sua máquina, dependendo de seu sistema. Neste caso, vá aos fóruns e procure pelos tópicos relacionados ao Mac OSX.

### Não consigo alterar valores numéricos nos painéis de propriedades do FreeCAD 

<img alt="language options" src=images/Jj62l.png  style="width:480px;">

Provavelmente, você tem uma configuração incorreta das configurações regionais do Windows. Verifique se você tem o mesmo símbolo para separador decimal e símbolo de agrupamento de dígitos em suas configurações regionais. Se o fizer, [adapte suas configurações de sistema](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) para usar caracteres diferentes para o símbolo de agrupamento de dígitos e separador decimal. Note que não é obrigatório ter ponto como separador decimal. É obrigatório o uso de símbolos diferentes nestas duas configurações. 

### O FreeCAD estava funcionando normalmente, e de repente não inicia mais 

Isto também pode acontecer se você tivesse uma versão mais antiga do FreeCAD instalada, e você atualizasse para uma versão mais nova. Nesse processo, os arquivos de configuração do FreeCAD podem ter sido corrompidos por alguma razão, e agora o FreeCAD não consegue mais lê-los, e não inicia. A solução é simplesmente apagar estes arquivos de configuração, assim o FreeCAD irá recriá-los na primeira execução.


<div class="mw-translate-fuzzy">

-   No Windows: Abra o explorador de arquivos, e escreva **%APPDATA%\FreeCAD** como o caminho do arquivo. Uma vez lá, apague os arquivos **user.cfg** e **system.cfg**.
-   No Linux: Navegue até **/home/USERNAME/.FreeCAD** e exclua os arquivos **user.cfg** e **system.cfg**
-   No Mac: Navegue até **/UserNAME/Library/Preferences/FreeCAD** e apague os arquivos **user.cfg** e **system.cfg**


</div>

O FreeCAD deve agora recomeçar normalmente com todas as suas configurações reiniciadas.


<div class="mw-translate-fuzzy">

Há um [Macro findConfigFiles](Macro_findConfigFiles.md) disponível para ajudar na localização de seus arquivos de configuração. Ele pode ser instalado usando o Gerenciador de Extensões no menu Tools (Ferramentas). **Ferramentas → Gerenciador de Extensões → Macros → findConfigFiles** A macro vai encontrar sua pasta de arquivos de configuração, copiá-la para a área de transferência e (tentar) abrir esse local com seu navegador de arquivos padrão. Ela não faz nenhuma alteração em seus arquivos ou configurações.


</div>

## Usando o FreeCAD 

### O FreeCAD é realmente livre? Mesmo para uso comercial? 

O FreeCAD é um [software de código aberto](http://en.wikipedia.org/wiki/Open-source_software), e é livre não só para uso, pessoal ou comercial, mas também para distribuir, modificar, ou mesmo usar em uma aplicação de código fechado. Para resumir, você está livre para fazer (quase) tudo o que quiser com ele. Consulte a página [Licença](Licence/pt-br.md) para obter mais detalhes.

### Como faço para girar a vista 3D? 


<center>

Image:Style_of_navigation.png\|A partir do **botão direito** do mouse Image:Style of navigation menu.png\|No menu **Editar → Preferências →**


</center>





<div class="mw-translate-fuzzy">

O FreeCAD oferece vários [modos de navegação](Mouse_Model/pt-br.md), que podem ser definidos pela janela de preferências ou clicando com o botão direito do mouse. Para saber mais sobre os modos de navegação, consulte a página [Modelo do mousePara](Mouse_Model/pt-br.md) o modo padrão, o \"Navegação CAD\", os comandos são os seguintes,


</div>

### O que eu posso fazer com o FreeCAD? Por onde eu começo? 

Vá para a página [Começar a usar](Getting_started/pt-br.md) para uma rápida descrição das ferramentas que você pode usar. Há também uma nova seção [Tutoriais](Tutorials/pt-br.md) contendo alguns recursos. A seção [Central do Usuário](User_hub/pt-br.md) contém informações mais detalhadas sobre as diferentes bancadas de trabalho do FreeCAD. Note que como o FreeCAD é relativamente novo, sua interface de usuário ainda é muito nua e não apresenta muitas ferramentas. Mas já há funcionalidades muito mais avançadas disponíveis no [Python scripting](Power_users_hub/pt-br.md).

### Existe documentação para os recém-chegados? Como posso aprender a usar o FreeCAD? 

Há muita documentação espalhada em diferentes lugares, tanto dentro como fora do site do FreeCAD. Talvez você queira começar com a página [Começar a usar](Getting_started/pt-br.md). A seção [Tutoriais](Tutorials/pt-br.md) contém muitas páginas de tutoriais especializados para ajudá-lo a começar com as diferentes bancadas de trabalho. O [Manual:Introdução](Manual:Introduction/pt-br.md) é um guia geral, completo e orientado ao usuário do FreeCAD. A seção [Central do Usuário](User_hub/pt-br.md) deste wiki lista todas as páginas destinadas aos usuários finais. Em sites externos como [Youtube](https://www.youtube.com/results?search_query=freecad), você também encontrará uma série de tutoriais em vídeo criados pelos usuários. E, por último, mas não menos importante, o [forum](https://forum.freecadweb.org) contém muitas respostas a perguntas feitas por outros recém-chegados.

### Eu quero importar/exportar dados no formato XYZ para/de FreeCAD. Como posso fazer isso? 


<div class="mw-translate-fuzzy">

Favor consultar a página [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Talvez suas perguntas já tenham sido respondidas lá.


</div>

### Where can I find workarounds for features that FreeCAD currently does not support? 

Please refer to the [Workarounds](Workarounds.md) page.

## Modelando peças a partir de geometrias simples 

=

### Como crio sólidos a partir de extrusões? Não consigo o resultado pretendido 

The theory is simple: Lines (or wires), when extruded, form faces. Faces, when extruded, form solids.


<div class="mw-translate-fuzzy">

A teoria é simples: As linhas (ou fios), quando extrudidas, formam faces. Faces, quando extrudadas, formam sólidos. Se você extrudar algo e o resultado não for um sólido, então o algo não era uma face. Se você tiver linhas e quiser extrudar um sólido delas, você deve primeiro selecionar linhas que formam um perímetro fechado (selecione vários objetos pressionando **Ctrl**), junte-as em um fio usando ([Promomovedor Draft](Draft_Upgrade/pt-br.md)), depois faça uma face desse fio (<img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> Ferramenta de atualização novamente). Aí está, se tudo correu bem, agora você pode extrudi-lo para um sólido.


</div>

Agora, pode haver muitas pequenas reviravoltas que fazem com que você obtenha o resultado errado. A melhor maneira de ter certeza é verificar o que está dentro do objeto que você está extrudindo. O conteúdo dos objetos pode ser facilmente explorado com python. Supondo, por exemplo, que você tenha um objeto chamado \"Wire\", você poderia digitar isto no console Python:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

O código acima recupera a forma de um objeto, mostra as faces e as linhas deste objeto se houver e se essas estiverem fechadas. Se você não tiver nenhuma face, você não terá um sólido. Se não houver linhas fechadas, elas não se tornarão uma face. Se você estiver interessado, você pode encontrar mais informações sobre o que você pode verificar com Python na página [Scripts para criação topológica](Topological_data_scripting/pt-br.md). Se você não puder unir várias linhas em um fio, a causa provável é que seus extremos não se encontram, deve haver pequenos espaços entre eles (alguns deles). Aqui, receio, minha experiência me diz que a maneira mais rápida seria redesenhar a linha sobre ela.

### Minhas operações booleanas falham, ou dão resultados estranhos 

O núcleo de modelagem geométrica [Open CASCADE](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) usado no FreeCAD para a geometria da Peça, embora provavelmente o melhor núcleo de geometria de código aberto disponível, tem suas falhas e limitações. De fato, as operações booleanas (fusão, subtração, interseção) não são suas melhores características, e muitas vezes dão resultados estranhos. Esta é uma limitação atual que não temos como resolver de uma só vez, portanto seu melhor caminho é tentar obter o resultado desejado modelando de outra forma. Por exemplo, problemas com primitivos como o cilindro podem muitas vezes ser resolvidos usando um círculo extrudado em seu lugar. Superfícies coplanares entre as peças podem causar problemas, bem como tangência de superfície. Como regra geral, se uma forma não funcionar, tente remodelá-la de maneira diferente. Em 99% dos casos no final, você conseguirá obter o resultado desejado.

### When I export (or view) my model, the holes are filled in 


<div class="mw-translate-fuzzy">

### Quando eu exporto (ou visualizo) meu modelo, os furos são preenchidos 

Não usar **Crtl** + **A** (Selecionar tudo) para exportar tudo da árvore hierárquica. Se o modelo for de um único item, tente selecionar apenas o item mais novo (geralmente o último) na árvore hierárquica.


</div>


<div class="mw-translate-fuzzy">

Ao criarmos um modelo no [PartDesign Workbench](PartDesign_Workbench.md), cada recurso toma a forma do último e adiciona ou remove algo, criando dependências lineares de recurso para recurso à medida que o modelo é criado. Portanto, uma característica \"Corte\" não é apenas o furo cortado em si, mas a peça inteira com o corte. É por isso que o usuário normalmente deveria ter apenas o item mais novo (função) na árvore do modelo visível, pois caso contrário as fases do modelo se sobrepõem, e os furos são preenchidos pelas características do modelo anterior.


</div>


<div class="mw-translate-fuzzy">

Para ativar ou desativar a visibilidade de um objeto, selecione-o na árvore hierárquica e pressione **spacebar** em seu teclado. Normalmente tudo, exceto o último item na árvore hierárquica, deve estar cinza e, portanto, não visível na visualização 3D.


</div>

### Meus objetos paramétricos quebram quando modifico seus esboços de base 

Você encontrou o (in)fame problema da toponímia. Este é atualmente um grande problema no FreeCAD para os recém-chegados. Ela está presente em toda parte no FreeCAD, mas é mais importante quando se utilizam [sketches](Sketcher_Workbench/pt-br.md)(esboços). A explicação é simples: ao recalcular um esboço, as entidades geométricas (bordas, faces \...) são reconstruídas em uma ordem diferente, dependendo da prioridade das restrições. Eles recebem então um nome diferente (Edge1, Edge2, Face1, Face2 \...). A maioria das operações subsequentes depende desses nomes para identificar o subcomponente em que estão trabalhando. Portanto, quando o esboço é reconstruído, as funções baseadas em tais subcomponentes podem mudar repentinamente sua geometria básica e dar um resultado incorreto.

Este é um problema muito difícil de ser superado (o [Projeto de Nomenclatura Topológica](Topological_Naming_Project/pt-br.md) visa resolvê-lo). Entretanto, há muitas soluções disponíveis para mitigar o problema, e os usuários mais avançados geralmente conseguem evitá-lo completamente. Um par de estratégias são:

-   Saiba que os sketches(esboços) são altamente sensíveis ao problema. A referência a uma borda específica de um esboço, ou a uma face de um objeto construída sobre um sketches(esboços), como um [PartDesign Pad(Protrusão)](PartDesign_Pad/pt-br.md), é perigosa, a menos que você esteja bastante confiante de que estes sketches(esboços)não mudarão com o tempo ou que o sketch(esboço)seja muito simples. Um bloco construído sobre um simples sketch(esboço)retangular, por exemplo, provavelmente será seguro, pois, gerará apenas uma face, portanto não há problema de ordem.
-   Preferir outros tipos de objetos como [Part](Part_Workbench/pt-br.md) ou [Draft](Draft_Workbench/pt-br.md) quando possível. Estes objetos são sempre construídos da mesma maneira, portanto, seus componentes geométricos geralmente seguem a mesma ordem cada vez que são reconstruídos. Eles são muito menos suscetíveis a problemas de toponímia.
-   Para anexar outros objetos às faces da geometria baseada em esboços, use antes o [plano de referência](PartDesign_Plane/pt-br.md). Estes \"objetos de ajuda\" invisíveis não dependem da geometria do esboço, portanto, permanecem estáveis ao longo do tempo.

## Contribuindo para o FreeCAD 

### O FreeCAD é um programa tão bom! Como posso ajudar? 

Há muitas maneiras diferentes de ajudar, mesmo que você não seja um programador. Aqui estão algumas coisas que você pode fazer:

-   Dar algum feedback para os desenvolvedores do FreeCAD: É sempre útil saber o que as pessoas pensam, o que elas acharam bom, o que elas sentem falta, etc. Deixe uma nota no [forum](http://forum.freecadweb.org/) dando sua opinião ou faça um pedido no nosso [rastreador de problemas](https://tracker.freecadweb.org/main_page.php)!
-   Ajuda para escrever a documentação: A documentação que temos aqui neste site é, às vezes, muito limitada. Se você descobriu algo que não está bem documentado, acrescente seu conhecimento lá!
-   Ajude os outros recém-chegados: Fique no fórum e ajude as novas pessoas a resolver questões básicas, como instalar, como inserir um cubo, etc.
-   [Traduza a documentação](Help_FreeCAD/pt-br#Traduza_a_documentação.md) para seu próprio idioma
-   [Traduza o FreeCAD](Help_FreeCAD/pt-br#Traduza_o_FreeCAD.md) para seu próprio idioma
-   Escreva [Tutoriais](Tutorials/pt-br.md), ou grave tutoriais em vídeo: Os tutoriais são uma maneira muito fácil para os recém-chegados conhecerem um novo programa. Se você fez algumas coisas legais, por que não mostrar a outras pessoas como fazer?
-   Contribuir com bens e exemplos: Ainda nos faltam bons arquivos de exemplos no FreeCAD. Se você criou algo bom, compartilhe conosco!
-   [Enviar bugs](Tracker/pt-br.md): É muito importante ter todos os bugs possíveis corrigidos. Se você encontrar um, relate o mais claramente possível, para que possamos entender exatamente o que está acontecendo.
-   Tente fazer um pouco de código Python: Você nunca programou antes, mas quer tentar? Python é fácil. Leia nossa [introdução à Python](Introduction_to_Python/pt-br.md), mas cuidado, você pode ficar viciado rapidamente!
-   Veja a página [Ajude o FreeCAD](Help_FreeCAD/pt-br.md) para mais detalhes sobre como contribuir.

### Como posso obter permissão para editar a wiki? 

Consulte o parágrafo [Trabalhe na documentação](Help_FreeCAD/pt-br#Trabalhe_na_documentação.md) para obter mais detalhes sobre como contribuir.

### O FreeCAD participa do Google Summer of Code? 

Sim. Desde 2016, o FreeCAD participa do Google Summer of Code. Veja [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) para informações sobre as edições passadas, e [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) no fórum para o anúncio original.

### Quero começar a traduzir o wiki para meu próprio idioma. O que eu faço? 

Este wiki está hospedando um monte de conteúdos. O material mais atualizado e interessante está reunido no [manual](Online_Help_Toc/pt-br.md).

Consulte o parágrafo [Traduza a documentação](Help_FreeCAD/pt-br#Traduza_a_documentação.md) para obter mais detalhes sobre como traduzir o wiki.

### Can I buy swag? 

FreeCAD doesn\'t offer swag you can order to support the project. But you can create your own. See our [Swag](Swag.md) page for instructions.

## Licenciamento, cópia e reutilização 

### Tenho que pagar alguma coisa para usar o FreeCAD? 

O FreeCAD é totalmente gratuito para usar, baixar, redistribuir ou modificar. Ele é um [software open-source](https://en.wikipedia.org/wiki/Open_source), publicado sob os termos da [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), que garante a você essas liberdades e, ainda mais importante, garante que essas liberdades nunca lhe serão tiradas.

### Posso reutilizar qualquer parte da arte do FreeCAD ou peças do site? 

Claro. Todas as obras de arte (ícones, banners, etc.) do FreeCAD são licenciadas LGPL, assim como o código do FreeCAD. Sirva-se na página [Objetos gráficos](Artwork/pt-br.md). O site é um site MediaWiki padrão, todos os elementos gráficos podem ser reutilizados livremente, e se você estiver curioso sobre como ajustar o software MediaWiki como nós fizemos, procure as páginas comuns especiais de css e js.

### Posso reutilizar peças do FreeCAD em outra aplicação? 

Sim, você pode usar as partes principais do FreeCAD em outras aplicações, desde que você cumpra com os termos da LGPL. Bibliotecas de terceiros, [bancadas de trabalho externas](External_workbenches/pt-br.md), e [macros](Macros/pt-br.md) podem estar sujeitas a seus próprios termos de licença, portanto, favor consultar seus autores. Mais detalhes na página [Licença](Licence/pt-br.md).



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > Frequently asked questions/pt-br
