# Frequently asked questions/pt-br
Esta página tenta responder as perguntas mais comuns feitas nos fóruns do FreeCAD. Se você tiver algum problema ou pergunta em relação ao FreeCAD, verifique abaixo primeiro. Depois, se você não encontrar uma resposta para sua pergunta específica, vá para o [Fórum FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3)!

## Instalação

### Qual é a maneira mais fácil de instalar o FreeCAD no meu sistema? 


<div class="mw-translate-fuzzy">

Se você estiver no Windows ou Mac OS, a maneira mais simples é ir para a página [Download](Download.md), onde você encontrará vários pacotes prontos para instalar. Se você estiver no Debian, Fedora ou Ubuntu e em algumas outras distribuições, o FreeCAD já está incluído nos repositórios de software padrão e você pode simplesmente instalá-lo com o gerenciador de software. No Ubuntu, a equipe do FreeCAD também mantém seus próprios [Repositórios PPA](Installing_on_Linux/pt-br#Desenvolvimento_PPA.md). Para maiores detalhes sobre instalação, consulte a página de instalação de seu sistema operacional ([Windows](Installing_on_Windows/pt-br.md), [Linux](Installing_on_Linux/pt-br.md) ou [Mac](Installing_on_Mac/pt-br.md)).


</div>

### Quais são os pré-requisitos para executar o FreeCAD? 

Em contraste com a maioria dos softwares CAD 3D, o FreeCAD pode funcionar sem problemas nos computadores mais modestos - é conhecido por funcionar em CPUs Pentium IV e Intel Core2 Solo. Se seu computador estiver rodando um sistema operacional atual, é provável que o FreeCAD seja executado. O único pré-requisito é que sua placa gráfica ou chipset deve suportar [OpenGL](https://en.wikipedia.org/wiki/OpenGL), de preferência não mais antigo que a v2.0. Em caso de problemas, consulte a seção [Solução de problemas](Frequently_asked_questions/pt-br#Solução_de_problemas.md) desta FAQ.

#### Multithreading

O núcleo de modelagem geométrica subjacente do FreeCAD, a [OpenCASCADE Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT) biblioteca de terceiros, tem apenas suporte parcial para multithreading neste momento. Veja a página [multithreading](multithreading/pt-br.md) para mais detalhes.

#### Para usuários de Mac 

Somente a arquitetura MacIntel é suportada. Não há construções disponíveis para a arquitetura PowerPC.

### E se eu quiser compilar o FreeCAD sozinho? 


<div class="mw-translate-fuzzy">

O código fonte do FreeCAD está sempre disponível no repositório de código fonte do projeto. A compilação do FreeCAD por conta própria permite utilizar os recursos mais recentes que estão sendo desenvolvidos, mas requer um pouco de conhecimento de informática, embora o procedimento seja bastante simples. O acesso ao código fonte é explicado [aqui](Compile_on_Linux/pt-br#Obtendo_a_fonte.md), e temos instruções detalhadas para compilação em [Windows](Compile_on_Windows/pt-br.md), [Linux](Compile_on_Linux/pt-br.md) e [MacOS](Compile_on_MacOS/pt-br.md).


</div>

### FreeCAD me diz que algum módulo ou aplicativo está faltando 

O FreeCAD depende de muitas coisas para oferecer todas as suas funcionalidades. Todos os principais componentes necessários são geralmente agrupados dentro de sua instalação FreeCAD ou fornecidos pelo seu gerenciador de pacotes, portanto, normalmente você não tem nada com que se preocupar. No entanto, se você instalou o FreeCAD a partir de fontes não oficiais, ou se você mesmo compilou o FreeCAD, alguma peça pode estar faltando, o que não é crítico para o próprio FreeCAD, mas pode fazer com que alguma funcionalidade não esteja disponível. Alguns formatos específicos de arquivo como Collada ou DWG também requerem componentes extras, que não podem ser agrupados no FreeCAD, e devem ser instalados por você mesmo separadamente.

Todos esses componentes e a maneira apropriada de instalá-los estão listados na página [Módulos python extras](Extra_python_modules/pt-br.md)

## Solução de problemas 

### O FreeCAD não inicia de forma alguma 

Pode haver muitas razões para isso, a mais provável é que falte alguma biblioteca. Tente iniciar o FreeCAD a partir de um terminal (digite {{SystemInput|freecad}} em um prompt de comando, {{SystemInput|FreeCAD}} em alguns sistemas) para ver se alguma mensagem de erro aparece. Leia também o restante deste FAQ, pois ele pode lhe dar mais pistas para detectar a causa do problema. Se nada ajudar, fale sobre isso no [forum](http://forum.freecadweb.org/), certamente haverá alguém que poderá ajudar.

Em alguns sistemas Windows XP mais antigos, você pode receber uma mensagem de erro como esta: **A aplicação não pode iniciar, porque a configuração lado a lado está errada. A reinstalação do aplicativo pode resolver o problema.** A razão deste problema é que em seu sistema ou as bibliotecas de tempo de execução CRT estão ausentes, ou a versão instalada é muito antiga porque o FreeCAD foi vinculado a uma versão mais recente. Neste caso você tem que instalar o **Microsoft Visual C++ Redistributable Package** que você encontrará na Microsoft. Veja também a correspondente [mensagem do fórum](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).

### FreeCAD inicia normalmente, mas nem todos os ícones são exibidos, alguns deles são substituídos por um \'X\' preto 

Algumas partes do FreeCAD dependem de um módulo Python externo chamado Pivy. No Windows, o pivy está incluído na instalação do FreeCAD. Em sistemas Debian/Ubuntu, o pacote python-pivy é parte de repositórios de software padrão. Em outros sistemas, no momento, você mesmo pode ter que compilar o pivy. Note que embora algumas ferramentas não estejam disponíveis sem pivy, o resto do FreeCAD funciona normalmente.

### Tenho problemas de visualização, a vista 3D não se comporta corretamente, há lixo quando movo/rodo a vista, etc. 

O FreeCAD depende do OpenGL para exibir conteúdos 3D, e portanto requer um ambiente OpenGL funcional. Em alguns sistemas, OpenGL não é ativado por padrão, e você pode precisar instalar ou atualizar seus drivers gráficos. Este problema acontece com mais freqüência em sistemas Linux ou em sistemas virtuais. Se você estiver em um sistema baseado em Linux, tente os seguintes passos:

-   verificar se seu computador possui uma placa gráfica com capacidade 3D
-   digite {{SystemInput|glxinfo}} em um terminal, e verifique na saída que a Renderização Direta está definida como \"sim\", e que o fornecedor/renderizador/versão OpenGL corresponde à sua placa gráfica.
-   instalar outro software baseado em OpenGL ([Blender](http://www.blender.org), por exemplo) e verificar se ele roda e exibe corretamente.

### FreeCAD falha na inicialização 

Uma falha pode indicar um bug mais sério, ou algum problema em sua configuração. A maioria das falhas na inicialização ocorre devido a uma das duas razões a seguir:

#### Os drivers OpenGL não estão instalados, ou não funcionam corretamente 

Esta é uma causa muito comum desse problema. Os sintomas são simplesmente que o FreeCAD trava na inicialização, ou sempre que você abre uma visualização 3D (por exemplo, criando um novo documento). Tente descobrir qual é seu chip gráfico, depois descubra se ele suporta [OpenGL](https://en.wikipedia.org/wiki/OpenGL) (os chips mais recentes suportam), depois encontre o driver correto e instale-o. Uma boa maneira de verificar se OpenGL está disponível é tentar executar outro aplicativo OpenGL, como [blender](http://www.blender.org).


<div class="mw-translate-fuzzy">

E como uma dica geral para obter mais informações sobre falhas com o FreeCAD, você pode iniciá-lo com o parâmetro do programa {{SystemInput|--write-log}}}. Isto criará o arquivo {{{FileName|FreeCAD.log}}} em {{{FileName|$HOME/.FreeCAD}}} no Linux e Mac OS X ou {{{FileName|%APPDATA%/FreeCAD}} em sistemas Windows.
</div>

Em alguns casos raros, você pode ter um driver gráfico instalado que não se encaixa em sua placa gráfica. Tivemos um caso em que o laptop do usuário tinha um gráfico Intel on-board, mas alguns drivers ATI foram instalados. [http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042]
Depois de remover os arquivos e reinstalar o driver correto, o FreeCAD começou a funcionar.

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
* Localize o executável FreeCAD (geralmente em {{FileName|/usr/lib/FreeCAD/bin}})
* Execute o comando {{{SystemInput|ldd FreeCAD}} a partir de um terminal
* Anote a versão da biblioteca {{{FileName|libCoin.so}}} que o FreeCAD está usando (por exemplo {{FileName|libCoin.so.60}})

-   Localize a biblioteca {{{FileName|libSoQt.so}}} (geralmente em {{FileName|/usr/lib}}})
-   correr {{{SystemInput|ldd libSoQt.so}}} e verifique se ele se liga à mesma versão Coin do FreeCAD

Se houver alguma diferença, o FreeCAD ou o SoQt devem ser recompilados (melhor recompilar aquele que usa a versão mais antiga da Coin). O comportamento normal é tentar contatar as pessoas responsáveis pela embalagem do SoQt ou do FreeCAD e gentilmente pedir-lhes que considerem a recompilação. Se você quiser dar esse passo por si mesmo, e não for possível recompilar o SoQt porque ele quebra outras aplicações em seu sistema, você pode forçar o FreeCAD a compilar com a versão Coin necessária com {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. Mas você tem que ter certeza de que o pacote de desenvolvimento correto desta versão Coin está instalado.

### FreeCAD trava após a Editar → Alinhamento 

Uma falha de segmentação acontece em {{SystemOutput|vbo_save_playback_vertex_list()}}. Isto significa que a implementação do VBO no driver gráfico é ruim. A fim de evitar o cache de chamadas OpenGL você pode tentar definir a variável de ambiente {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} e reiniciar o FreeCAD.


<div class="mw-translate-fuzzy">

### Eu tenho problemas para executar o FreeCAD no Mac OSX 


</div>


<div class="mw-translate-fuzzy">

A plataforma Mac é não é tão fácil de suportar como o Windows ou Linux, já que nenhum dos principais desenvolvedores possui um. Os pacotes OSX são compilados por usuários voluntários do FreeCAD, e às vezes podem não funcionar corretamente em sua máquina, dependendo de seu sistema. Sua melhor chance é provavelmente ir aos fóruns, procurar por tópicos relacionados ao Mac OSX e discutir seu problema lá ou ver se alguém encontrou uma solução.


</div>

### Não posso alterar valores numéricos nos painéis de propriedades do FreeCAD 

<img alt="language options" src=images/Jj62l.png  style="width:480px;">

Provavelmente, você tem uma configuração incorreta das configurações regionais do Windows. Verifique se você tem o mesmo símbolo para separador decimal e símbolo de agrupamento de dígitos em suas configurações regionais. Se o fizer, [adapte suas configurações de sistema](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) para usar caracteres diferentes para o símbolo de agrupamento de dígitos e separador decimal. Note que não é obrigatório ter ponto como separador decimal. É obrigatório o uso de símbolos diferentes nestas duas configurações. 

### O FreeCAD estava funcionando normalmente, e de repente não inicia mais 

Isto também pode acontecer se você tivesse uma versão mais antiga do FreeCAD instalada, e você atualizasse para uma versão mais nova. Nesse processo, os arquivos de configuração do FreeCAD podem ter sido corrompidos por alguma razão, e agora o FreeCAD não consegue mais lê-los, e não inicia. A solução é simplesmente apagar estes arquivos de configuração, assim o FreeCAD irá recriá-los na primeira execução.

-   No Windows: Abra o explorador de arquivos, e escreva {{FileName|%APPDATA%\FreeCAD}} como o caminho do arquivo. Uma vez lá, apague os arquivos {{FileName|user.cfg}} e {{FileName|system.cfg}}.
-   No Linux: Navegue até {{FileName|/home/USERNAME/.FreeCAD}} e exclua os arquivos {{FileName|user.cfg}} e {{FileName|system.cfg}}
-   No Mac: Navegue até {{FileName|/UserNAME/Library/Preferences/FreeCAD}} e apague os arquivos {{FileName|user.cfg}} e {{FileName|system.cfg}}

O FreeCAD deve agora recomeçar normalmente com todas as suas configurações reiniciadas.

Há um [Macro findConfigFiles](Macro_findConfigFiles.md) disponível para ajudar na localização de seus arquivos de configuração. Ele pode ser instalado usando o Gerenciador de Extensões no menu Tools (Ferramentas). **Ferramentas → Gerenciador de Extensões → Macros → findConfigFiles** A macro vai encontrar sua pasta de arquivos de configuração, copiá-la para a área de transferência e (tentar) abrir esse local com seu navegador de arquivos padrão. Ela não faz nenhuma alteração em seus arquivos ou configurações.

## Usando o FreeCAD 

### O FreeCAD é realmente livre? Mesmo para uso comercial? 

O FreeCAD é um [software de código aberto](http://en.wikipedia.org/wiki/Open-source_software), e é livre não só para uso, pessoal ou comercial, mas também para distribuir, modificar, ou mesmo usar em uma aplicação de código fechado. Para resumir, você está livre para fazer (quase) tudo o que quiser com ele. Consulte a página [Licença](Licence/pt-br.md) para obter mais detalhes.

### Como faço para girar a vista 3D? 


<center>

Image:Style\_of\_navigation.png\|A partir do **botão direito** do mouse Image:Style of navigation menu.png\|No menu **Editar → Preferências →**


</center>





<div class="mw-translate-fuzzy">

O FreeCAD tem vários modos diferentes [modos de navegação](Mouse_Model/pt-br.md) disponíveis, que podem ser definidos no diálogo de preferências ou alterados clicando com o botão direito do mouse na visualização 3D. Para detalhes completos sobre os modos, consulte a página [Modelo do mousePara](Mouse_Model/pt-br.md) o modo padrão (\"Navegação CAD\"), os comandos são os seguintes,


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

Os usuários que usam o mouse com a mão direita podem achar este método mais fácil do que o primeiro método.
}}

### O que eu posso fazer com o FreeCAD? Por onde eu começo? 

Vá para a página [Começar a usar](Getting_started/pt-br.md) para uma rápida descrição das ferramentas que você pode usar. Há também uma nova seção [Tutoriais](Tutorials/pt-br.md) contendo alguns recursos. A seção [Central do Usuário](User_hub/pt-br.md) contém informações mais detalhadas sobre as diferentes bancadas de trabalho do FreeCAD. Note que como o FreeCAD é relativamente novo, sua interface de usuário ainda é muito nua e não apresenta muitas ferramentas. Mas já há funcionalidades muito mais avançadas disponíveis no [Python scripting](Power_users_hub/pt-br.md).

### Existe documentação para os recém-chegados? Como posso aprender a usar o FreeCAD? 

Há muita documentação espalhada em diferentes lugares, tanto dentro como fora do site do FreeCAD. Talvez você queira começar com a página [Começar a usar](Getting_started/pt-br.md). A seção [Tutoriais](Tutorials/pt-br.md) contém muitas páginas de tutoriais especializados para ajudá-lo a começar com as diferentes bancadas de trabalho. O [Manual:Introdução](Manual:Introduction/pt-br.md) é um guia geral, completo e orientado ao usuário do FreeCAD. A seção [Central do Usuário](User_hub/pt-br.md) deste wiki lista todas as páginas destinadas aos usuários finais. Em sites externos como [Youtube](https://www.youtube.com/results?search_query=freecad), você também encontrará uma série de tutoriais em vídeo criados pelos usuários. E, por último, mas não menos importante, o [forum](https://forum.freecadweb.org) contém muitas respostas a perguntas feitas por outros recém-chegados.

### Eu quero importar/exportar dados no formato XYZ para/de FreeCAD. Como posso fazer isso? 

Favor consultar a página [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Talvez suas perguntas já tenham sido respondidas lá.

## Trabalhando com a geometria da peça 

=

### Como posso extrudar coisas em sólidos? Eu não consigo o resultado certo 


<div class="mw-translate-fuzzy">

A teoria é simples: As linhas (ou fios), quando extrudidas, formam faces. Faces, quando extrudadas, formam sólidos. Se você extrudar algo e o resultado não for um sólido, então o algo não era uma face. Se você tiver linhas e quiser extrudar um sólido delas, você deve primeiro selecionar linhas que formam um perímetro fechado (selecione vários objetos pressionando **Ctrl**), junte-as em um fio usando ([Promomovedor Draft](Draft_Upgrade/pt-br.md)), depois faça uma face desse fio ([16px](arquivo:Draft_Upgrade.svg.md) Ferramenta de atualização novamente). Aí está, se tudo correu bem, agora você pode extrudi-lo para um sólido.


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

### Quando eu exporto (ou visualizo) meu modelo, os furos são preenchidos 

Não usar **Crtl** + **A** (Selecionar tudo) para exportar tudo da árvore hierárquica. Se o modelo for de um único item, tente selecionar apenas o item mais novo (geralmente o último) na árvore hierárquica.

Ao criarmos um modelo no [PartDesign Workbench](PartDesign_Workbench.md), cada recurso toma a forma do último e adiciona ou remove algo, criando dependências lineares de recurso para recurso à medida que o modelo é criado. Portanto, uma característica \"Corte\" não é apenas o furo cortado em si, mas a peça inteira com o corte. É por isso que o usuário normalmente deveria ter apenas o item mais novo (função) na árvore do modelo visível, pois caso contrário as fases do modelo se sobrepõem, e os furos são preenchidos pelas características do modelo anterior.

Para ativar ou desativar a visibilidade de um objeto, selecione-o na árvore hierárquica e pressione **spacebar** em seu teclado. Normalmente tudo, exceto o último item na árvore hierárquica, deve estar cinza e, portanto, não visível na visualização 3D.

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

## Licenciamento, cópia e reutilização 

### Tenho que pagar alguma coisa para usar o FreeCAD? 

O FreeCAD é totalmente gratuito para usar, baixar, redistribuir ou modificar. Ele é um [software open-source](https://en.wikipedia.org/wiki/Open_source), publicado sob os termos da [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), que garante a você essas liberdades e, ainda mais importante, garante que essas liberdades nunca lhe serão tiradas.

### Posso reutilizar qualquer parte da arte do FreeCAD ou peças do site? 

Claro. Todas as obras de arte (ícones, banners, etc.) do FreeCAD são licenciadas LGPL, assim como o código do FreeCAD. Sirva-se na página [Objetos gráficos](Artwork/pt-br.md). O site é um site MediaWiki padrão, todos os elementos gráficos podem ser reutilizados livremente, e se você estiver curioso sobre como ajustar o software MediaWiki como nós fizemos, procure as páginas comuns especiais de css e js.

### Posso reutilizar peças do FreeCAD em outra aplicação? 

Sim, você pode usar as partes principais do FreeCAD em outras aplicações, desde que você cumpra com os termos da LGPL. Bibliotecas de terceiros, [bancadas de trabalho externas](External_workbenches/pt-br.md), e [macros](Macros/pt-br.md) podem estar sujeitas a seus próprios termos de licença, portanto, favor consultar seus autores. Mais detalhes na página [Licença](Licence/pt-br.md).







[Category:Documentation](Category:Documentation.md)

---
[documentation index](../README.md) > [Documentation](Category:Documentation.md) > Frequently asked questions/pt-br
