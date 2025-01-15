# Localisation/pt-br
## Visão geral 

**Localização** é, em geral, o processo de fornecer um Software com uma interface de usuário em vários idiomas. No FreeCAD, você pode definir o idioma da interface do usuário em **Editar → Preferências → Geral**. O FreeCAD usa o [Qt](wikipedia:Qt_(toolkit).md) para permitir o suporte a vários idiomas. Em sistemas Unix/Linux, o FreeCAD usa as configurações de localidade atuais do seu sistema por padrão.



## Ajudando a traduzir o FreeCAD 

Uma das coisas muito importantes que os usuários podem contribuir com o FreeCAD (se, por exemplo, não tiverem habilidades de programação) é ajudar a traduzir seus diferentes aspectos (código-fonte, wiki, website, documentação, etc.) para outro idioma. Aqui estão as maneiras de como fazer isso.



## Traduzir o código fonte do FreeCAD 

O FreeCAD utiliza um sistema de tradução on-line colaborativo de terceiros chamado [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

É um software proprietário, mas gratuito para projetos [FOSS](https://pt.wikipedia.org/wiki/Software_livre_e_de_c%C3%B3digo_aberto). Abaixo estão as instruções sobre como usá-lo:

-   Vá para a [página do projeto de tradução FreeCAD no Crowdin](http://crowdin.net/project/freecad)
-   Faça login criando um novo perfil ou usando uma conta de terceiros (GitHub, GitLab, GMail etc\...)
-   Clique no idioma que deseja traduzir
-   Comece a traduzir clicando no botão **|Traduzir** ao lado de um dos arquivos. Por exemplo, **FreeCAD.ts** contém as sequências de texto para a GUI principal do FreeCAD.
-   Você pode votar nas traduções existentes ou pode criar a sua própria.

{{Message|Se você está participando ativamente da tradução do FreeCAD e deseja ser informado antes que o próximo lançamento esteja pronto para ser lançado, para que haja tempo para revisar sua tradução, inscreva-se em uma das equipes de tradução do FreeCAD no Crowdin.}}


**Nota:**

Detalhes sobre como usar o Crowdin podem ser encontrados na página [Crowdin Administration](Crowdin_Administration.md).



## Traduzindo bancadas externas 

Visite [Traduzindo uma bancada externa](Translating_an_external_workbench.md).



## Preferências para tradutores do FreeCAD 

A partir do FreeCAD 0.20, as seguintes variáveis podem ser adicionadas manualmente à seção BaseApp/Preferences/General do arquivo **user.cfg** para ajudar no desenvolvimento de novas traduções:

**AdditionalLanguageDomainEntries** - para adicionar idiomas totalmente novos ao FreeCAD que não são atualmente suportados pelo código-fonte, você pode usar esta preferência do usuário para adicionar à lista de idiomas disponíveis. O formato dos idiomas é \"Language Name\"=\"code\"; por exemplo:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - adiciona um diretório adicional para o FreeCAD procurar por arquivos \*.qm. Este local terá precedência sobre \$userAppDataDir/translations e \$resourceDir/translations. Por exemplo:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>



## Traduzindo o wiki do FreeCAD 

Este wiki hospeda muitos conteúdos, a maioria dos quais compõem o manual. Você pode navegar pela documentação a partir da [Página principal](Main_Page/pt-br.md), ou dar uma olhada no manual do usuário [Índice da Ajuda Online](Online_Help_Toc/pt-br.md).

Para traduzir o wiki, você deve ter permissões de edição do wiki; veja [How can I get edit permission on the wiki?](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki?.md).

Você também deve ter conhecimento suficiente da marcação wiki e seguir as diretrizes gerais de estilo descritas em [Páginas Wiki](WikiPages/pt-br.md).



### Extenção para tradução do Mediawiki 

Quando o wiki saiu do SourceForge, [Yorik](User_Yorik.md) instalou [MediaWiki\'s Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate) que facilita a tradução de páginas. As vantagens da extensão de tradução são que o título da página agora pode ser traduzido, as traduções são monitoradas, ela notifica se a página original foi atualizada e mantém as traduções sincronizadas com a página original em inglês.

A ferramenta está documentada em [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate) e faz parte do [Pacote de extensão de idiomas do MediaWiki](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).


<div class="mw-translate-fuzzy">

Para começar a preparar uma página para tradução de forma rápida, leia o [Exemplo de tradução de página](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). Basicamente um par de tags


</div>

    &lt;translate&gt; ... &lt;/translate&gt;


<div class="mw-translate-fuzzy">

precisam envolver toda a página para ativar o sistema de tradução, e a página precisa ser marcada para tradução.


</div>

Para ver um exemplo de como a ferramenta de tradução funciona, visite a [Página principal](Main_Page/pt-br.md). Você verá uma barra de idiomas gerada automaticamente na parte superior. Clique em [Deutsch](Main_Page/de.md) (Alemão), ele irá levá-lo para [Main Page/de](Main_Page/de.md). Logo abaixo do título, \"Hauptseite\" (em inglês \"Página principal\"), você pode ler , XX sendo a porcentagem atual de tradução. Clique em \"Traduzir\" no topo da página para iniciar o utilitário de tradução para atualizar, corrigir e revisar a tradução existente.


<div class="mw-translate-fuzzy">

Se você for para [Main Page/pt-br](Main_Page/pt-br.md), notará que não pode mais editar a página diretamente clicando nas tags \[Edit\], e o link superior \"Editar\" foi substituído pelo link \"Traduzir\" que abre o utilitário de tradução.


</div>

Ao adicionar novo conteúdo, a página em inglês deve ser criada primeiro e depois traduzida para outro idioma. Se alguém quiser alterar ou adicionar conteúdo em uma página, a página em inglês deve ser modificada primeiro.

Se você não tiver certeza de como proceder com as traduções, não hesite em pedir ajuda no [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) ou no \[https ://forum.freecadweb.org/viewforum.php?f=11 subfórum de idioma específico\] no [fórum FreeCAD](http://forum.freecadweb.org).



### Notas importantes 

Todos os usuários do wiki que têm permissões de \"Editor\" podem iniciar o utilitário de tradução para escrever, salvar e revisar traduções.

No entanto, somente usuários com permissões de \"Administrador\" podem marcar páginas para tradução. Uma página que não esteja marcada para tradução não usará a extensão de tradução e não será sincronizada corretamente com as informações em inglês.

A barra lateral esquerda também pode ser traduzida, mas somente os administradores podem modificar esse elemento do site. Siga as instruções específicas em [Localização da barra lateral](Localisation_Sidebar/pt-br.md).

Na primeira vez que você mudar uma página para o novo sistema de tradução, ela perderá todas as suas traduções \"manuais\" antigas. Para recuperar uma tradução, você deve salvar uma cópia off-line do texto antigo antes da mudança. Em seguida, você pode usar esse texto traduzido antigo para preencher as unidades de tradução no novo sistema. Você também pode abrir uma versão anterior do histórico e obter o texto antigo dessa forma. Isso deve ser feito para cada idioma que tinha uma página traduzida.



### Traduzir a documentação do FreeCAD 

De acordo com o consenso geral, a página de referência no wiki é a página em inglês, que deve ser criada primeiro. Se você quiser alterar ou adicionar conteúdo a uma página, deve fazê-lo primeiro na página em inglês e, somente depois que a atualização for concluída, portar a modificação para a página traduzida.



### Instruções de tradução antigas 

++
| Estas instruções são apenas para fins históricos. As traduções devem usar o novo sistema com a [#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) descrita acima.                                                                                                                                                                                                                                                                                                                                                                                              |
++
| Então o primeiro passo é **verificar se a tradução manual já foi iniciada para o seu idioma** (procure na barra lateral esquerda, em \"manual\").                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Caso contrário, acesse o [forum](http://forum.freecadweb.org/) e diga que deseja iniciar uma nova tradução, criaremos a configuração básica para o idioma que você deseja trabalhar.                                                                                                                                                                                                                                                                                                                                                                                                        |
| Você deve então [obter permissão de edição do wiki](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Se o seu idioma já estiver listado, veja quais páginas ainda não têm tradução (elas serão listadas em vermelho). A técnica é simples: **vá para uma página vermelha, copie/cole o conteúdo da página em inglês correspondente e comece a traduzir**.                                                                                                                                                                                                                                                                                                                                        |
| Não se esqueça de incluir todas as tags e modelos da página original em inglês. Alguns desses modelos terão um equivalente em seu idioma (por exemplo, existe um modelo Docnav em francês chamado Docnav/fr). Você deve usar **uma barra e seu código de idioma** em quase todos os links. Veja outras páginas já traduzidas para ver como eles fizeram isso.                                                                                                                                                                                                                               |
| Adicione uma barra e o código do seu idioma nas categorias, como \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| E se não tiver certeza, vá aos fóruns e peça às pessoas que verifiquem o que você fez e digam se está certo ou não.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Quatro modelos são comumente usados ​​em páginas de manual. Esses 4 modelos possuem versões localizadas (Template:Docnav/fr, Template:fr, etc\...)                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -   [Template:GuiCommand](Template_GuiCommand.md) : é o bloco de informações do Comando Gui no canto superior direito da documentação do comando.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -   [Template:Docnav](Template_Docnav.md) : é a barra de navegação no final das páginas, mostrando as páginas anteriores e seguintes.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -   [Template:Userdocnavi](Template_Userdocnavi.md) : fornece links diretos para as páginas base principais                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Convenção de nomenclatura de páginas**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Por favor, observe que, devido às limitações na implementação do motor MediaWiki no Sourceforge, exigimos que todas as suas páginas mantenham o nome original em inglês, acrescentando uma barra e o código do seu idioma. Por exemplo, a página traduzida para Sobre o FreeCAD deveria ser Sobre o Freecad/es para espanhol, Sobre o FreeCAD/pl para polonês, etc. A razão é simples: para que se os tradutores forem embora, os administradores do wiki, que não falam todos os idiomas, saberá para que servem essas páginas. Isso facilitará a manutenção e evitará a perda de páginas. |
| Se você quiser que o modelo Docnav mostre páginas vinculadas em seu idioma, você pode usar **redirecionar páginas**. Eles são basicamente links de atalho para a página real. Aqui está um exemplo com a página francesa de Sobre o FreeCAD.                                                                                                                                                                                                                                                                                                                                                |
| \* A página Sobre o FreeCAD/fr é a página com conteúdo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -   A página À propos de FreeCAD contém este código:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -   Na página Sobre o FreeCAD/fr, o código Docnav ficará assim:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| A página \"Bienvenue dans l\'aide en ligne de FreeCAD\" redireciona para Online_Help_Startpage/fr, e a página \"Fonctionnalités\" redireciona para Feature_list/fr.                                                                                                                                                                                                                                                                                                                                                                                                                         |
++



## Tradução do site do FreeCAD 

A tradução do site do FreeCAD agora é feita por meio de [Crowdin](https://crowdin.com/translate/freecad/561/en-en). O arquivo é denominado **homepage.po**.



## Desenvolvimento - Como adicionar localização 

Esta seção é para desenvolvedores que desejam adicionar localização ao seu código.



### Preparando seus módulos FreeCAD/master para tradução 

Estas são as partes do processo de tradução do FreeCAD:

-   extrair cadeias de texto do código-fonte em arquivos \*.ts
-   Carregar arquivos \*.ts no [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   Tradução de strings no Crowdin
-   Extração de arquivos \*.ts modificados/novos do Crowdin
-   Converter arquivos \*.ts em arquivos \*.qm e atualizar o arquivo \*.qrc de cada módulo
-   Atualizar o FreeCAD master

Todas as etapas acima são executadas pelos \"scripts de tradução\", que são executados periodicamente por um administrador.

Preparar seu módulo para tradução é muito fácil. Primeiro, é necessário garantir que você tenha um diretório \"translations\" em **myModule/Gui/Resources**. Em seguida, abra uma janela de terminal (ou equivalente no Windows/OSX) em seu diretório \"translations\" e digite o seguinte comando: 
```pythonlupdate -ts myModule.ts```

Isso cria um arquivo de tradução vazio. Uma vez feito isso, você precisa garantir que os scripts de tradução sejam atualizados como nesta [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

Tudo depois disso é automático no que diz respeito a um desenvolvedor. O administrador extrairá as sequências de texto, os tradutores as traduzirão e, em seguida, o administrador extrairá as traduções e atualizará o FreeCAD/master.



### Preparando seu módulo ou macro de terceiros para tradução 

Os módulos ou macros de terceiros são traduzidos da mesma forma, exceto pelo fato de que você mesmo deve fazer parte do trabalho. Esta [discussão no fórum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) descreve os detalhes.

Atualização: consulte [Traduzindo um workbench externo](Translating_an_external_workbench/pt-br.md)



## Automatizando as atualizações de tradução do Crowdin 

Atualmente, os mantenedores do FreeCAD usam a API do Crowdin por meio de [Crowdin Scripts](Crowdin_Scripts/pt-br.md) para puxar e enviar traduções para o Crowdin e de volta para o repositório do Github. A API do Crowdin oferece aos mantenedores do FreeCAD a capacidade de automatizar aspectos do fluxo de trabalho de tradução do projeto. Para obter mais informações, consulte a [Documentação da API do Crowdin](https://support.crowdin.com/api/api-integration-setup/).



## Páginas relacionadas 

-   [Administração do Crowdin](Crowdin_Administration/pt-br.md)
-   [Scripts Crowdin](Crowdin_Scripts/pt-br.md)

## Scripting


**Veja também:**

[FreeCAD Noções básicas de programação](FreeCAD_Scripting_Basics/pt-br.md).

Para obter um dicionário com os idiomas suportados pela interface do FreeCAD, use o método `supportedLocales` do módulo `FreeCADGui`.


```python
locales = FreeCADGui.supportedLocales()
```

Após a execução, `locales` conterá:


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

Para obter o idioma da interface atual, use o método `getLocale` do mesmo módulo:


```python
locale = FreeCADGui.getLocale()
```

Se o idioma atual for o inglês, `locale` conterá:


```python
'English'
```

Para obter o [código de idioma](https://support.crowdin.com/api/language-codes/) correspondente, você pode usar:


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

Se o idioma atual for o inglês, o resultado será:


```python
'en'
```

Para definir o idioma da interface atual, use o método `setLocale` do mesmo módulo. Você pode especificar o idioma ou o código do idioma:


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/pt-br
