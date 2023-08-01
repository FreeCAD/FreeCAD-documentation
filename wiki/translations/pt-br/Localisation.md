# Localisation/pt-br
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}



## Visão geral 

**Localização** é, em geral, o processo de fornecer um Software com uma interface de usuário em vários idiomas. No FreeCAD, você pode definir o idioma da interface do usuário em **Editar → Preferências → Geral**. O FreeCAD usa o [Qt](wikipedia:Qt_(toolkit).md) para permitir o suporte a vários idiomas. Em sistemas Unix/Linux, o FreeCAD usa as configurações de localidade atuais do seu sistema por padrão.



## Ajudando a traduzir o FreeCAD 

Uma das coisas muito importantes que os usuários podem contribuir com o FreeCAD (se, por exemplo, não tiverem habilidades de programação) é ajudar a traduzir seus diferentes aspectos (código-fonte, wiki, website, documentação, etc.) para outro idioma. Aqui estão as maneiras de como fazer isso.



## Traduzir o código fonte do FreeCAD 

O FreeCAD utiliza um sistema de tradução on-line colaborativo de terceiros chamado [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">


<div class="mw-translate-fuzzy">

É um software proprietário, mas gratuito para projetos [FOSS](https://pt.wikipedia.org/wiki/Software_livre_e_de_c%C3%B3digo_aberto). Abaixo estão as instruções sobre como usá-lo:


</div>

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

Para começar a preparar uma página para tradução de forma rápida, leia o [Exemplo de tradução de página](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). Basicamente um par de tags

    &lt;translate&gt; ... &lt;/translate&gt;

precisam envolver toda a página para ativar o sistema de tradução, e a página precisa ser marcada para tradução.

Para ver um exemplo de como a ferramenta de tradução funciona, visite a [Página principal](Main_Page/pt-br.md). Você verá uma barra de idiomas gerada automaticamente na parte superior. Clique em [Deutsch](Main_Page/de.md) (Alemão), ele irá levá-lo para [Main Page/de](Main_Page/de.md). Logo abaixo do título, \"Hauptseite\" (em inglês \"Página principal\"), você pode ler , XX sendo a porcentagem atual de tradução. Clique em \"Traduzir\" no topo da página para iniciar o utilitário de tradução para atualizar, corrigir e revisar a tradução existente.

Se você for para [Main Page/pt-br](Main_Page/pt-br.md), notará que não pode mais editar a página diretamente clicando nas tags \[Edit\], e o link superior \"Editar\" foi substituído pelo link \"Traduzir\" que abre o utilitário de tradução.

Ao adicionar novo conteúdo, a página em inglês deve ser criada primeiro e depois traduzida para outro idioma. Se alguém quiser alterar ou adicionar conteúdo em uma página, a página em inglês deve ser modificada primeiro.

Se você não tiver certeza de como proceder com as traduções, não hesite em pedir ajuda no [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) ou no \[https ://forum.freecadweb.org/viewforum.php?f=11 subfórum de idioma específico\] no [fórum FreeCAD](http://forum.freecadweb.org).

### Important notes 

Every wiki user that has \"Editor\" permissions is able to launch the translate utility to write, save and review translations.

However, only users with \"Administrator\" permissions are able to mark pages for translation. A page that is not marked for translation won\'t make use of the translation extension and won\'t be correctly synchronized to the English information.

The left sidebar is also translatable, but only Administrators can modify this element of the site. Please follow the dedicated instructions on [Localisation Sidebar](Localisation_Sidebar.md).

The first time you switch a page to the new translation system, it loses all its old \"manual\" translations. To recover a translation, you should save an offline copy of the old text before the switch. Then you can use this old translated text to fill in the translation units in the new system. You can also open an earlier version from the history, and get the old text in this way. This has to be done for every language that had a translated page.

### Translate the FreeCAD documentation 

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

### Old translation instructions 

++
| These instructions are for historical background only. Translations should use the new system with the [#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) described above.                                                                                                                                                                                                                                                                                                                                                                  |
++
| So the first step is to **check if the manual translation has already been started for your language** (look in the left sidebar, under \"manual\").                                                                                                                                                                                                                                                                                                                                                                                                                     |
| If not, head to the [forum](http://forum.freecadweb.org/) and say that you want to start a new translation, we\'ll create the basic setup for the language you want to work on.                                                                                                                                                                                                                                                                                                                                                                                          |
| You must then [gain wiki edit permission](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| If your language is already listed, see what pages are still missing a translation (they will be listed in red). The technique is simple: **go into a red page, and copy/paste the contents of the corresponding English page, and start translating**.                                                                                                                                                                                                                                                                                                                  |
| Do not forget to include all the tags and templates from the original English page. Some of those templates will have an equivalent in your language (for example, there is a French Docnav template called Docnav/fr). You should use **a slash and your language code** in almost all the links. Look at other already translated pages to see how they did it.                                                                                                                                                                                                        |
| Add a slash and your language code in the categories, like \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| And if you are unsure, head to the forums and ask people to check what you did and tell you if it\'s right or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Four templates are commonly used in manual pages. These 4 templates have localized versions (Template:Docnav/fr, Template:fr, etc\...)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   [Template:GuiCommand](Template_GuiCommand.md) : is the Gui Command information block in upper-right of command documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template:Docnav](Template_Docnav.md) : it is the navigation bar at the bottom of the pages, showing previous and next pages.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template:Userdocnavi](Template_Userdocnavi.md) : gives direct links to the main base pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Page Naming Convention**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Please take note that, due to limitations in the Sourceforge implementation of the MediaWiki engine, we require that your pages all keep their original English counterpart\'s name, appending a slash and your language code. For example, the translated page for About FreeCAD should be About Freecad/es for Spanish, About FreeCAD/pl for polish, etc. The reason is simple: so that if translators go away, the wiki\'s administrators, who do not speak all languages, will know what these pages are for. This will facilitate maintenance and avoid lost pages. |
| If you want the Docnav template to show linked pages in your language, you can use **redirect pages**. They are basically shortcut links to the actual page. Here is an example with the French page for About FreeCAD.                                                                                                                                                                                                                                                                                                                                                  |
| \* The page About FreeCAD/fr is the page with content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   The page À propos de FreeCAD contains this code:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   In the About FreeCAD/fr page, the Docnav code will look like this:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The page \"Bienvenue dans l\'aide en ligne de FreeCAD\" redirects to Online_Help_Startpage/fr, and the page \"Fonctionnalités\" redirects to Feature_list/fr.                                                                                                                                                                                                                                                                                                                                                                                                            |
++

## Translate the FreeCAD website 

Translation of the FreeCAD website is now done through [Crowdin](https://crowdin.com/translate/freecad/561/en-en). The file is named **homepage.po**.

## Development - How to Add Localisation 

This section is for developers who want to add localisation to their code.

### Preparing your FreeCAD/master modules for translation 

These are the parts to the FreeCAD translation process:

-   extract text strings from source code into \*.ts files
-   load \*.ts files into [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   translation of strings within Crowdin
-   extract modified/new \*.ts files from Crowdin
-   convert \*.ts files into \*.qm files and update each module\'s \*.qrc file
-   update FreeCAD master

All of the above steps are performed by the \"translation scripts\" which are run by an administrator periodically.

Preparing your module for translation is quite easy. First, you need to ensure that you have a \"translations\" directory in **myModule/Gui/Resources**. Then open a terminal window (or Windows/OSX equivalent) in your \"translations\" directory and enter the following command: 
```pythonlupdate -ts myModule.ts```

This creates an empty translation file. Once this is done, you need to ensure that the translation scripts are updated as in this [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

Everything after this is automatic as far as a developer is concerned. The administrator will extract the text strings, the translators will translate them, then the administrator will extract the translations and update FreeCAD/master.

### Preparing your 3rd party module or macro for translation 

3rd party modules or macros are translated in much the same fashion, except that you must do some of the work yourself. This [forum discussion](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) describes the details.

Update: see [Translating an external workbench](Translating_an_external_workbench.md)

### Older module translation techniques 

[Localization Older Methods](Localization_Older_Methods.md) describes the use of translation tools such as Qt Linguist, lupdate, lrelease, pylupdate4, etc in detail. Most of this is no longer required for FreeCAD/master modules, but may be helpful preparing and updating 3rd party modules.

## Automating Crowdin Translation Updates 

Currently FreeCAD maintainers use the Crowdin API via [Crowdin Scripts](Crowdin_Scripts.md) to pull and push translations in to Crowdin and back in to the Github repo. The Crowdin API gives FreeCAD maintainers the ability to automate aspects of the project\'s translation workflow, for more info refer to the [Crowdin API documentation](https://support.crowdin.com/api/api-integration-setup/).

## Related Pages 

-   [Crowdin Administration](Crowdin_Administration.md)
-   [Crowdin Scripts](Crowdin_Scripts.md)

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To get a dictionary with the languages the FreeCAD interface supports, use the `supportedLocales` method of the `FreeCADGui` module.


```python
locales = FreeCADGui.supportedLocales()
```

After execution `locales` will contain:


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

To get the current interface language use the `getLocale` method of the same module:


```python
locale = FreeCADGui.getLocale()
```

If the current language is English `locale` will contain:


```python
'English'
```

To get the corresponding [language code](https://support.crowdin.com/api/language-codes/) you can use use:


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

If the current language is English the result will be:


```python
'en'
```

To set the current interface language use the `setLocale` method of the same module. You can specify the language or the language code:


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/pt-br
