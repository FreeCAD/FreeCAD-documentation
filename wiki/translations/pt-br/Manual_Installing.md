# Manual:Installing/pt-br
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

O FreeCAD utiliza a licença [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License); você pode baixar, instalar, redistribuir e usar o FreeCAD da maneira que desejar, independentemente do tipo de trabalho que você realizará com ele (comercial ou não comercial). Você não está vinculado a nenhuma cláusula ou restrição, e os arquivos que você produzir com ele são totalmente seus. A única coisa que a licença realmente proíbe é afirmar que você programou o FreeCAD por conta própria!


</div>


<div class="mw-translate-fuzzy">

O FreeCAD se comporta da mesma forma no Windows, Mac OS e Linux. No entanto, o processo de instalação difere um pouco dependendo da sua plataforma. No Windows e Mac, a comunidade do FreeCAD fornece pacotes pré-compilados (instaladores) prontos para download; enquanto no Linux, o código-fonte é disponibilizado aos mantenedores das distribuições Linux, que são responsáveis por empacotar o FreeCAD para suas distribuições específicas. Como resultado, no Linux, você geralmente pode instalar o FreeCAD diretamente pelo aplicativo de gerenciador de software.


</div>


<div class="mw-translate-fuzzy">

A página oficial para baixar o FreeCAD para Windows e Mac OS é <https://github.com/FreeCAD/FreeCAD/releases>.


</div>

**Versões do FreeCAD**


<div class="mw-translate-fuzzy">

As versões oficiais do FreeCAD, que você pode encontrar na página mencionada acima e no gerenciador de software da sua distribuição, são versões estáveis. No entanto, o desenvolvimento do FreeCAD é rápido! Novos recursos e correções de bugs são adicionados quase todos os dias. Como pode demorar um tempo entre os lançamentos estáveis, você pode ter interesse em testar uma versão mais atualizada do FreeCAD. Essas versões de desenvolvimento, ou pré-lançamentos, são carregadas de tempos em tempos na página de [download](https://github.com/FreeCAD/FreeCAD/releases) mencionada acima, ou, se você estiver usando Ubuntu ou Fedora, a comunidade do FreeCAD também mantém o [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) e os \'daily builds\' no [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) que são atualizados regularmente com as mudanças mais recentes.


</div>


<div class="mw-translate-fuzzy">

Se você estiver instalando o FreeCAD em uma máquina virtual, esteja ciente de que o desempenho pode ser baixo (em alguns casos, inutilizável) devido às limitações do suporte a [OpenGL](https://en.wikipedia.org/wiki/OpenGL) na maioria das máquinas virtuais.


</div>



### Instalando no Windows 


<div class="mw-translate-fuzzy">

1.  Baixe o instalador (.exe) correspondente à sua versão do Windows (32bit ou 64bit) na [página de downloads](https://github.com/FreeCAD/FreeCAD/releases). Os instaladores do FreeCAD devem funcionar em qualquer versão do Windows a partir do Windows 7.
2.  Dê um clique duplo no instalador baixado.
3.  Aceite os termos da licença LGPL, este será um dos poucos casos em que você pode realmente clicar no botão \"aceitar\" sem ler o texto. Sem cláusulas ocultas: ![](images/Freecad-windows-install-01.jpg )
4.  Você pode deixar o caminho padrão aqui ou mudar, se preferir: ![](images/Freecad-windows-install-02.jpg )
5.  Não há necessidade de definir a variável PYTHONPATH, a menos que você planeje fazer alguma programação avançada em Python, caso em que provavelmente já sabe para que isso serve: ![](images/Freecad-windows-install-03.jpg )
6.  Durante a instalação, alguns componentes adicionais, que estão agrupados dentro do instalador, também serão instalados: ![](images/Freecad-windows-install-04.jpg )
7.  Pronto, o FreeCAD está instalado. Você o encontrará no menu iniciar. ![](images/Freecad-windows-install-05.jpg )


</div>

**Instalando uma versão de desenvolvimento**


<div class="mw-translate-fuzzy">

Empacotar o FreeCAD e criar um instalador leva algum tempo e dedicação, por isso, normalmente, as versões de desenvolvimento (também chamadas de pré-lançamento) são fornecidas como arquivos .zip (ou .7z). Estes não precisam ser instalados; basta descompactá-los e iniciar o FreeCAD dando um clique duplo no arquivo FreeCAD.exe que você encontrará dentro. Isso também permite que você mantenha as versões estáveis e \"instáveis\" juntas no mesmo computador.


</div>



### Instalando no Linux 


<div class="mw-translate-fuzzy">

Na maioria das distribuições Linux modernas (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary, etc.), o FreeCAD pode ser instalado com um clique, diretamente do aplicativo de gerenciamento de software fornecido pela sua distribuição (a aparência pode diferir das imagens abaixo, pois cada distribuição utiliza sua própria ferramenta).


</div>


<div class="mw-translate-fuzzy">

1.  Abra o gerenciador de software e procure por \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Clique no botão \"instalar\" e pronto, o FreeCAD será instalado. Não se esqueça de avaliá-lo depois!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">


</div>

**Métodos alternativos**


<div class="mw-translate-fuzzy">

Uma das grandes vantagens de usar o Linux é a multiplicidade de possibilidades para personalizar seu software, então não se restrinja. No Ubuntu e derivados, o FreeCAD também pode ser instalado a partir de um [PPA](https://launchpad.net/~freecad-maintainers) mantido pela comunidade do FreeCAD (que contém versões estáveis e de desenvolvimento). No Fedora, versões recentes de desenvolvimento do FreeCAD podem ser instaladas a partir do [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), e como este é um software open source, você também pode facilmente [compilar o FreeCAD você mesmo](Compiling/pt-br.md).


</div>



### Instalando no Mac OS 

Instalar o FreeCAD no Mac OS atualmente é tão fácil quanto nas outras plataformas. No entanto, como há menos pessoas na comunidade que possuem um Mac, os pacotes disponíveis às vezes ficam algumas versões atrás em relação às outras plataformas.


<div class="mw-translate-fuzzy">

1.  Baixe o pacote compactado correspondente à sua versão na [página de downloads](https://github.com/FreeCAD/FreeCAD/releases).
2.  Abra a pasta Downloads e descompacte o arquivo zip baixado: ![](images/Freecad-mac-01.jpg )
3.  Arraste o aplicativo FreeCAD de dentro do arquivo zip para a pasta Aplicativos: ![](images/Freecad-mac-02.jpg )
4.  Pronto, o FreeCAD está instalado! ![](images/Freecad-mac-03.jpg )

5\. Se o sistema impedir que o FreeCAD seja iniciado devido a permissões restritas para aplicativos não provenientes da App Store, será necessário habilitar essa opção nas configurações do sistema: ![](images/Freecad-mac-04.jpg )


</div>



### Desinstalando


<div class="mw-translate-fuzzy">

Esperamos que você não precise desinstalar o FreeCAD, mas é bom saber como fazer. No Windows e Linux, desinstalar o FreeCAD é bem simples. No Windows, use a opção padrão de \"remover software\" encontrada no painel de controle; no Linux, remova-o com o mesmo gerenciador de software que você usou para instalá-lo. No Mac OS, basta removê-lo da pasta Aplicativos.


</div>



### Configurando preferências básicas 


<div class="mw-translate-fuzzy">

Uma vez que o FreeCAD esteja instalado, você pode querer abri-lo e alterar algumas preferências. As configurações de preferências do FreeCAD estão localizadas no menu **Editar → Preferências**. Abaixo estão algumas configurações básicas que você pode querer alterar; você pode navegar pelas páginas de preferências para verificar se há mais alguma coisa que deseja modificar.


</div>

#### General category, General tab 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Language**: By default, FreeCAD will select your operating system\'s language, but you have the option to change it. Thanks to the dedication of many contributors, FreeCAD is available in a wide array of languages.
2.  **Units**: This setting allows you to choose the default units system for your projects.

#### General category, Document tab 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Create a new document at startup**: FreeCAD will automatically open a new document each time the program starts.
2.  **Storage options**: Configure settings here to help you recover your work in the event of a crash.
3.  **\'Authoring and license**\': In this area, you can determine the settings for new files. To facilitate sharing, consider starting with a more permissive, copyleft license like Creative Commons.

#### Display category, Navigation tab 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Zoom at cursor**: When enabled, zoom actions center on the mouse cursor. If disabled, zoom focuses on the center of the view.
2.  **Invert zoom**: This option reverses the zoom direction in relation to mouse movement.

#### Workbenches tab 

![](images/FreeCAD_022_WBMenu.png )

Although FreeCAD typically opens to the start page, this setting lets you bypass it. You can start directly in your preferred workbench. Additionally, you can customize which workbenches are displayed in the selector menu.

#### Import-Export tab 

![](images/FreeCAD_022_ImportExport.png )

Here, define basic parameters for importing and exporting in various formats.



### Instalando conteúdo adicional 


<div class="mw-translate-fuzzy">

À medida que o projeto FreeCAD e sua comunidade crescem rapidamente, e também porque é fácil de estender, começam a surgir contribuições externas e projetos paralelos feitos por membros da comunidade e outros entusiastas em toda a internet. A maioria desses projetos externos são bancadas de trabalho ou macros, e podem ser facilmente instalados diretamente dentro do FreeCAD através do [Gerenciador de Addons](Std_AddonMgr.md), localizado no menu **Ferramentas**. O gerenciador de addons permite que você instale muitos componentes interessantes, por exemplo:


</div>

![](images/FreeCAD_022_AddonsMenu.png )


<div class="mw-translate-fuzzy">

1.  A [Biblioteca de Peças](https://github.com/FreeCAD/FreeCAD-library), que contém todo tipo de modelos úteis, ou partes de modelos, criados pelos usuários do FreeCAD e que podem ser usados livremente em seus projetos. A biblioteca pode ser acessada diretamente dentro da sua instalação do FreeCAD.
2.  [Bancadas de Trabalho Adicionais](https://github.com/FreeCAD/FreeCAD-addons), que estendem a funcionalidade do FreeCAD para tarefas específicas, como animar partes de seus modelos ou áreas, como dobragem de chapas metálicas ou BIM. Explicações detalhadas de cada bancada e as ferramentas que ela contém estão disponíveis em cada página de addon, que você pode visitar clicando no link correspondente no gerenciador de addons.
3.  Uma [coleção de macros](https://github.com/FreeCAD/FreeCAD-macros), que também está disponível [na wiki do FreeCAD](Macros_recipes.md) junto com a documentação sobre como utilizá-las.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">


</div>

**Leia mais**

-   [Mais opções de download](Download/pt-br.md)
-   [PPA do FreeCAD para Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [PPA de addons do FreeCAD para Ubuntu](https://launchpad.net/freecad-extras)
-   [Compile o FreeCAD você mesmo](Compiling/pt-br.md)
-   [Traduções do FreeCAD](https://crowdin.com/project/freecad)
-   [Página do FreeCAD no GitHub](https://github.com/FreeCAD)
-   [Gerenciador de addons do FreeCAD](Std_AddonMgr/pt-br.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/pt-br
