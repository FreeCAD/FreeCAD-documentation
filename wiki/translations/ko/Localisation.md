# Localisation/ko
## 요약

여기서 **현지화** 의 의미는 주로, 외국 언어로 된 소프트웨어의 화면을 만드는 것 입니다. 프리캐드의 **Edit → Preferences → Application**에서 사용자 언어를 설정할 수 있습니다. 프리캐드는 다양한 언어 지원이 가능하도록 [Qt를](wikipedia:Qt_(toolkit).md) 사용합니다. 유닉스/리눅스 시스템에서, 프리캐드는 기본적으로 여러분의 컴퓨터의 지역설정을 사용합니다.



## FreeCAD 번역 돕기 

사용자가 프리캐드에 기여할 수 있는 매우 중요한 것 중 한 가지는 (예를 들어 프로그래밍 기술이 없는 경우) 다양한 측면(소스 코드, 위키, 웹사이트, 문서 등)을 다른 언어로 번역하는 것을 돕는 일이고 방법은 다음과 같습니다.



## 프리캐드 소스 코드 번역 

FreeCAD 는 외부의 [Crowdin](https://crowdin.net) 라고 하는 온라인 공동 번역 시스템을 도입 했습니다.

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

이는 독점 소프트웨어이지만 [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software) 프로젝트에서는 무료입니다. 다음은 사용 방법에 대한 지침입니다.

-   [Crowdin의 FreeCAD 번역 프로젝트 페이지](http://crowdin.net/project/freecad)로 이동하세요.
-   새 프로필을 생성하거나 타사 계정(GitHub, GitLab, GMail 등\...)을 사용하여 로그인하세요.
-   번역하려는 언어를 클릭하세요.
-   파일 옆에 있는 **Translate** 버튼을 클릭하여 번역을 시작하세요. 예를 들어, **FreeCAD.ts**에는 FreeCAD 기본 GUI에 대한 텍스트 문자열이 포함되어 있습니다.
-   기존 번역에 투표하거나 직접 만들 수도 있습니다.

{{Message|FreeCAD 번역에 적극적으로 참여하고 있고 다음 릴리스가 출시되기 전에 알림을 받아 번역을 검토할 시간이 있으면 Crowdin FreeCAD 번역 팀 중 하나를 구독하세요.}}


**참고:**

Crowdin 사용 방법에 대한 자세한 내용은 [Crowdin 관리](Crowdin_Administration.md) 페이지에서 확인할 수 있습니다.



## 외부 작업대 번역 

[외부 작업대 번역을](Translating_an_external_workbench.md) 참고하세요



## 번역가를 위한 FreeCAD 기본 설정 

FreeCAD 0.20부터 다음 변수를 user.cfg 파일의 BaseApp/Preferences/General 섹션에 수동으로 추가하여 새로운 번역 개발을 지원할 수 있습니다.

**AdditionalLanguageDomainEntries** - 현재 소스 코드에서 지원되지 않는 완전히 새로운 언어를 FreeCAD에 추가하려면,이 사용자 기본 설정을 사용하여 사용 가능한 언어 목록에 추가할 수 있습니다. 언어 형식은 \"Language Name\"=\"code\"입니다. 예를 들어:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - \*.qm 파일을 검색하기 위해 FreeCAD용 추가 디렉토리를 추가합니다. 이 위치는 \$userAppDataDir/translations 및 \$resourceDir/translations보다 우선합니다. 예를 들어:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>



## FreeCAD 위키 번역 

이 위키는 많은 내용을 담고 있으며 대부분이 매뉴얼을 구성합니다. [홈페이지에서](Main_Page/ko.md) 시작하는 문서를 찾아보거나 [온라인 도움말 목차를](Online_Help_Toc/ko.md) 보세요.

위키를 번역하려면, 위키 편집 권한을 가져야 합니다; [How can I get edit permission on the wiki?](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki?.md) 를 보세요.

You should also have enough knowledge of wiki markup and follow the general styling guidelines described on [WikiPages](WikiPages.md).



### Mediawiki 번역 확장 

When the wiki moved away from SourceForge, [Yorik](User_Yorik.md) installed [MediaWiki\'s Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate) which facilitates translating pages. Advantages of the translation extension are that the page title can now be translated, it keeps track of translations, it notifies if the original page has been updated, and it maintains translations in sync with the original English page.

The tool is documented in [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate), and is part of [MediaWiki Language Extension Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

To quickly get started on preparing a page for translation, please read the [Page translation example](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). A pair of tags need to surround the entire page to activate the translation system:

    &lt;translate&gt; ... &lt;/translate&gt;

The page also needs to be marked for translation.

To see an example of how the translation tool works, visit the [Main Page](Main_Page.md). You will see an automatically generated language bar at the top. Click on [Deutsch](Main_Page/de.md) (German), it will get you to [Main Page/de](Main_Page/de.md). Right under the title, \"Hauptseite\" (in English \"Main Page\"), you can read , XX being the current percentage of translation. Click on \"Translate\" at the top of the page to start the translation utility to update, correct and review the existing translation.

If you go to [Main Page](Main_Page.md), you will notice that you cannot edit the page directly anymore by clicking the \[Edit\] tags, and the top link \"Edit\" has been substituted by the \"Translate\" link that opens the translation utility.

When adding new content, the English page should be created first, then translated into another language. If someone wants to change or add content in a page, the English page should be modified first.

If you are unsure on how to proceed with the translations, don\'t hesitate to ask for help in the [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) or in the [specific language subforum](https://forum.freecadweb.org/viewforum.php?f=11) in the [FreeCAD forum](http://forum.freecadweb.org).



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




<div class="mw-translate-fuzzy">

## FreeCAD 웹사이트 번역 

Translation of the FreeCAD website is now done through [Crowdin](https://crowdin.com/translate/freecad/561/en-en). The file is named **homepage.po**.


</div>

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


{{docnav|Branding|Extra python modules}}


</div>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/ko
