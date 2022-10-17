# Localisation/ko
<div class="mw-translate-fuzzy">


{{docnav|Branding|Extra python modules}}


</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

**지역화**는 일반적으로 다중 언어 사용자 인터페이스를 가진 소프트웨어 제공 절차입니다. In FreeCAD you can set the language of the user interface under **Edit → Preferences → Application**. FreeCAD uses [Qt](wikipedia   *Qt_(toolkit).md) to enable multiple language support. On Unix/Linux systems, FreeCAD uses the current locale settings of your system by default.


</div>

**Localisation** is in general the process of providing a Software with a multiple language user interface. In FreeCAD you can set the language of the user interface under **Edit → Preferences → General**. FreeCAD uses [Qt](wikipedia   *Qt_(toolkit).md) to enable multiple language support. On Unix/Linux systems, FreeCAD uses the current locale settings of your system by default.

## FreeCAD 번역 도움 

One of the very important things users can contribute to FreeCAD (if for example they don\'t have programming skills) is to help translate its different aspects (source code, wiki, website, documentation etc\...) in to another language. Here are the ways to do that.


<div class="mw-translate-fuzzy">

## FreeCAD 소스 코드 번역 

FreeCAD utilizes a third party collaborative on-line translation system called [Crowdin](https   *//crowdin.net). It is proprietary software but free to FOSS projects. Below are instructions on how to use it   *


</div>

FreeCAD utilizes a third party collaborative on-line translation system called [Crowdin](https   *//crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width   *320px;">

It is proprietary software but free to FOSS projects. Below are instructions on how to use it   *

-   Go to the [FreeCAD translation project page on Crowdin](http   *//crowdin.net/project/freecad)
-   Login by creating a new profile, or using a third-party account (GitHub, GitLab, GMail etc\...)
-   Click on the language you wish to translate
-   Start translating by clicking on the **Translate** button next to one of the files. For example, **FreeCAD.ts** contains the text strings for the FreeCAD main GUI.
-   You can vote for existing translations, or you can create your own.

{{Message|If you are actively taking part in translating FreeCAD and want to be informed before next release is ready to be launched, so there is time to review your translation, please subscribe to one of the Crowdin FreeCAD translation teams.}}


**Note   ***

Details on how to use crowdin can be found on the [Crowdin Administration](Crowdin_Administration.md) page.

## Translating external workbenches 

Visit [Translating an external workbench](Translating_an_external_workbench.md).

## FreeCAD Preferences for Translators 

Starting with FreeCAD 0.20, the following variables can be manually added to the BaseApp/Preferences/General section of the user.cfg file to assist with the development of new translations   *

**AdditionalLanguageDomainEntries** - to add entirely new languages to FreeCAD that are not currently supported by the source code, you can use this user preference to add to the list of available languages. The format of the languages is \"Language Name\"=\"code\"; for example   *

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - add an additional directory for FreeCAD to search for \*.qm files. This location will take precedence over \$userAppDataDir/translations and \$resourceDir/translations. For example   *

    <FCText Name="AdditionalTranslationsDirectory">C   */Users/FreeCADUser/TestTranslations</FCText>

## FreeCAD 위키 번역 


<div class="mw-translate-fuzzy">

이 위키는 많은 내용을 담고 있으며 대부분이 매뉴얼을 구성합니다. [Main Page에서](Main_Page.md) 시작하는 문서를 찾아보거나 [Online Help Toc](Online_Help_Toc.md) 사용자 매뉴얼을 보세요.


</div>


<div class="mw-translate-fuzzy">

위키를 번역하려면, 위키 편집 권한을 가져야 합니다; FAQ 를 보세요.


</div>

You should also have enough knowledge of wiki markup and follow the general styling guidelines described on [WikiPages](WikiPages.md).

### Mediawiki 번역 확장 

When the wiki moved away from SourceForge, [Yorik](User_Yorik.md) installed [MediaWiki\'s Translation extension](http   *//www.mediawiki.org/wiki/Help   *Extension   *Translate) which facilitates translating pages. Advantages of the translation extension are that the page title can now be translated, it keeps track of translations, it notifies if the original page has been updated, and it maintains translations in sync with the original English page.

The tool is documented in [Help   *Extension   *Translate](http   *//www.mediawiki.org/wiki/Help   *Extension   *Translate), and is part of [MediaWiki Language Extension Bundle](http   *//www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

To quickly get started on preparing a page for translation, please read the [Page translation example](http   *//www.mediawiki.org/wiki/Help   *Extension   *Translate/Page_translation_example). Essentially, a pair of

    &lt;translate&gt; ... &lt;/translate&gt;

tags need to surround the entire page to activate the translation system, and the page needs to be marked for translation.

To see an example of how the translation tool works, visit the [Main Page](Main_Page.md). You will see an automatically generated language bar at the top. Click on [Deutsch](Main_Page/de.md) (German), it will get you to [Main Page/de](Main_Page/de.md). Right under the title, \"Hauptseite\" (in English \"Main Page\"), you can read , XX being the current percentage of translation. Click on \"Translate\" at the top of the page to start the translation utility to update, correct and review the existing translation.

If you go to [Main Page](Main_Page.md), you will notice that you cannot edit the page directly anymore by clicking the \[Edit\] tags, and the top link \"Edit\" has been substituted by the \"Translate\" link that opens the translation utility.

When adding new content, the English page should be created first, then translated into another language. If someone wants to change or add content in a page, the English page should be modified first.

If you are unsure on how to proceed with the translations, don\'t hesitate to ask for help in the [Development → Wiki subforum](https   *//forum.freecadweb.org/viewforum.php?f=21) or in the [specific language subforum](https   *//forum.freecadweb.org/viewforum.php?f=11) in the [FreeCAD forum](http   *//forum.freecadweb.org).

### 중요한 노트 

Every wiki user that has \"Editor\" permissions is able to launch the translate utility to write, save and review translations.

However, only users with \"Administrator\" permissions are able to mark pages for translation. A page that is not marked for translation won\'t make use of the translation extension and won\'t be correctly synchronized to the English information.

The left sidebar is also translatable, but only Administrators can modify this element of the site. Please follow the dedicated instructions on [Localisation Sidebar](Localisation_Sidebar.md).

The first time you switch a page to the new translation system, it loses all its old \"manual\" translations. To recover a translation, you should save an offline copy of the old text before the switch. Then you can use this old translated text to fill in the translation units in the new system. You can also open an earlier version from the history, and get the old text in this way. This has to be done for every language that had a translated page.


<div class="mw-translate-fuzzy">

## FreeCAD 문서 번역 


</div>

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

### 옛 번역 명령 

++
| These instructions are for historical background only. Translations should use the new system with the [#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) described above.                                                                                                                                                                                                                                                                                                                                                                  |
++
| So the first step is to **check if the manual translation has already been started for your language** (look in the left sidebar, under \"manual\").                                                                                                                                                                                                                                                                                                                                                                                                                     |
| If not, head to the [forum](http   *//forum.freecadweb.org/) and say that you want to start a new translation, we\'ll create the basic setup for the language you want to work on.                                                                                                                                                                                                                                                                                                                                                                                          |
| You must then [gain wiki edit permission](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| If your language is already listed, see what pages are still missing a translation (they will be listed in red). The technique is simple   * **go into a red page, and copy/paste the contents of the corresponding English page, and start translating**.                                                                                                                                                                                                                                                                                                                  |
| Do not forget to include all the tags and templates from the original English page. Some of those templates will have an equivalent in your language (for example, there is a French Docnav template called Docnav/fr). You should use **a slash and your language code** in almost all the links. Look at other already translated pages to see how they did it.                                                                                                                                                                                                        |
| Add a slash and your language code in the categories, like \[\[Category   *Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| And if you are unsure, head to the forums and ask people to check what you did and tell you if it\'s right or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Four templates are commonly used in manual pages. These 4 templates have localized versions (Template   *Docnav/fr, Template   *fr, etc\...)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   [Template   *GuiCommand](Template_GuiCommand.md)    * is the Gui Command information block in upper-right of command documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template   *Docnav](Template_Docnav.md)    * it is the navigation bar at the bottom of the pages, showing previous and next pages.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template   *Userdocnavi](Template_Userdocnavi.md)    * gives direct links to the main base pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Page Naming Convention**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Please take note that, due to limitations in the Sourceforge implementation of the MediaWiki engine, we require that your pages all keep their original English counterpart\'s name, appending a slash and your language code. For example, the translated page for About FreeCAD should be About Freecad/es for Spanish, About FreeCAD/pl for polish, etc. The reason is simple   * so that if translators go away, the wiki\'s administrators, who do not speak all languages, will know what these pages are for. This will facilitate maintenance and avoid lost pages. |
| If you want the Docnav template to show linked pages in your language, you can use **redirect pages**. They are basically shortcut links to the actual page. Here is an example with the French page for About FreeCAD.                                                                                                                                                                                                                                                                                                                                                  |
| \* The page About FreeCAD/fr is the page with content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   The page À propos de FreeCAD contains this code   *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   In the About FreeCAD/fr page, the Docnav code will look like this   *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The page \"Bienvenue dans l\'aide en ligne de FreeCAD\" redirects to Online_Help_Startpage/fr, and the page \"Fonctionnalités\" redirects to Feature_list/fr.                                                                                                                                                                                                                                                                                                                                                                                                            |
++


<div class="mw-translate-fuzzy">

## FreeCAD 웹사이트 번역 

Translation of the FreeCAD website is now done through [Crowdin](https   *//crowdin.com/translate/freecad/561/en-en). The file is named **homepage.po**.


</div>

Translation of the FreeCAD website is now done through [Crowdin](https   *//crowdin.com/translate/freecad/561/en-en). The file is named **homepage.po**.

## Development - How to Add Localisation 

This section is for developers who want to add localisation to their code.

### Preparing your FreeCAD/master modules for translation 

These are the parts to the FreeCAD translation process   *

-   extract text strings from source code into \*.ts files
-   load \*.ts files into [FreeCAD Crowdin](http   *//crowdin.net/project/freecad).
-   translation of strings within Crowdin
-   extract modified/new \*.ts files from Crowdin
-   convert \*.ts files into \*.qm files and update each module\'s \*.qrc file
-   update FreeCAD master

All of the above steps are performed by the \"translation scripts\" which are run by an administrator periodically.

Preparing your module for translation is quite easy. First, you need to ensure that you have a \"translations\" directory in **myModule/Gui/Resources**. Then open a terminal window (or Windows/OSX equivalent) in your \"translations\" directory and enter the following command   * 
```pythonlupdate -ts myModule.ts```

This creates an empty translation file. Once this is done, you need to ensure that the translation scripts are updated as in this [pull request](https   *//github.com/FreeCAD/FreeCAD/pull/810).

Everything after this is automatic as far as a developer is concerned. The administrator will extract the text strings, the translators will translate them, then the administrator will extract the translations and update FreeCAD/master.

### Preparing your 3rd party module or macro for translation 

3rd party modules or macros are translated in much the same fashion, except that you must do some of the work yourself. This [forum discussion](https   *//www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) describes the details.

Update   * see [Translating an external workbench](Translating_an_external_workbench.md)

### Older module translation techniques 

[Localization Older Methods](Localization_Older_Methods.md) describes the use of translation tools such as Qt Linguist, lupdate, lrelease, pylupdate4, etc in detail. Most of this is no longer required for FreeCAD/master modules, but may be helpful preparing and updating 3rd party modules.

## Automating Crowdin Translation Updates 

Currently FreeCAD maintainers use the Crowdin API via [Crowdin Scripts](Crowdin_Scripts.md) to pull and push translations in to Crowdin and back in to the Github repo. The Crowdin API gives FreeCAD maintainers the ability to automate aspects of the project\'s translation workflow, for more info refer to the [Crowdin API documentation](https   *//support.crowdin.com/api/api-integration-setup/).

## Related Pages 

-   [Crowdin Administration](Crowdin_Administration.md)
-   [Crowdin Scripts](Crowdin_Scripts.md)

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To get a dictionary with the languages the FreeCAD interface supports, use the `supportedLocales` method of the `FreeCADGui` module.


```python
locales = FreeCADGui.supportedLocales()
```

After execution `locales` will contain   *


```python
{'English'   * 'en', 'Afrikaans'   * 'af', 'Arabic'   * 'ar', 'Basque'   * 'eu', 'Catalan'   * 'ca', 'Chinese Simplified'   * 'zh-CN', 'Chinese Traditional'   * 'zh-TW', 'Croatian'   * 'hr', 'Czech'   * 'cs', 'Dutch'   * 'nl', 'Filipino'   * 'fil', 'Finnish'   * 'fi', 'French'   * 'fr', 'Galician'   * 'gl', 'German'   * 'de', 'Hungarian'   * 'hu', 'Indonesian'   * 'id', 'Italian'   * 'it', 'Japanese'   * 'ja', 'Kabyle'   * 'kab', 'Korean'   * 'ko', 'Lithuanian'   * 'lt', 'Norwegian'   * 'no', 'Polish'   * 'pl', 'Portuguese'   * 'pt-PT', 'Portuguese, Brazilian'   * 'pt-BR', 'Romanian'   * 'ro', 'Russian'   * 'ru', 'Slovak'   * 'sk', 'Slovenian'   * 'sl', 'Spanish'   * 'es-ES', 'Swedish'   * 'sv-SE', 'Turkish'   * 'tr', 'Ukrainian'   * 'uk', 'Valencian'   * 'val-ES', 'Vietnamese'   * 'vi'}
```

To get the current interface language use the `getLocale` method of the same module   *


```python
locale = FreeCADGui.getLocale()
```

If the current language is English `locale` will contain   *


```python
'English'
```

To get the corresponding [language code](https   *//support.crowdin.com/api/language-codes/) you can use use   *


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

If the current language is English the result will be   *


```python
'en'
```

To set the current interface language use the `setLocale` method of the same module. You can specify the language or the language code   *


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```


<div class="mw-translate-fuzzy">


{{docnav|Branding|Extra python modules}}


</div>




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Wiki](Category_Wiki.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/ko
