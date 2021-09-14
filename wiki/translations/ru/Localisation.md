# Localisation/ru







{{TOCright}}

## Обзор

**Локализация** в целом, это процесс создания многоязыкового пользовательского интерфейса для программного обеспечения. В FreeCAD вы можете установить язык пользовательского интерфейса в **Правка → Настройки → Основные**. FreeCAD использует [Qt](wikipedia:Qt_(toolkit).md) чтобы поддерживать несколько языков. По умолчанию в Unix/Linux системах, FreeCAD использует текущие языковые настройки вашей системы для выбора языка интерфейса FreeCAD.

## Помощь с переводом FreeCAD 

Одно из очень важных дел которое пользователи могут сделать для FreeCAD (если например они не имеют навыков программирования ), это помочь с переводом различных частей проекта (программа, сайт, вики, документация и т. д.) на другой язык. Вот как это можно сделать

## Перевод программного обеспечения FreeCAD 

FreeCAD использует стороннюю систему коллективных онлайн-переводов, называемую [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

Она проприетарная, но бесплатна для проектов с открытым исходным кодом. Ниже представлены инструкции по использованию этой системы.

-   Отправляйтесь на [страницу проекта перевода FreeCAD на Crowdin](http://crowdin.net/project/freecad);
-   Войдите, создав новый профиль, или воспользовавшись сторонними аккаунтами (GitHub, GitLab, GMail итд\...);
-   Щелкните иконку языка на котоый хотите перевести;
-   Начните переводить , щелкнув на **Translate** рядом с одним из файлов. Например, *FreeCAD.ts* содержит текстовые строки для главного окна FreeCAD.
-   Вы можете голосовать за существующие переводы, или вы можете создавать свой собственный.

{{Message|Если вы активно принимаете участие в переводе FreeCAD и хотите быть в курсе когда будет готов к запуску следующий релиз, так чтобы было время рассмотреть ваш перевод, пожалуйста подпишитесь на одну из команд перевода FreeCAD в Crowdin.}}


**Note:**

Details on how to use crowdin can be found on the [Crowdin Administration](Crowdin_Administration.md) page.

## Перевод внешних верстаков 

Подробности на странице [перевод внешних верстаков](Translating_an_external_workbench.md).

## Перевод FreeCAD wiki 

В этой вики содержится много контента, большинство из которого собрано в руководства. Вы можете просмотреть документацию, начиная со [стартовой страницы](Main_Page/ru.md) или можно взглянуть на [руководство пользователя](Online_Help_Toc/ru.md)

Примечание: чтобы иметь возможность перевести вики, вам нужно иметь права редактирования, насчёт их получения смотрите [Как я могу полчить права для редактирования wiki?](Frequently_asked_questions/ru#How_can_I_get_edit_permission_on_the_wiki?.md).

У Вас должны быть достаточные знания о языке форматировании вики, и следовать общими стилевым правилам, описанным на странице [WikiPages](WikiPages/ru.md)

### Расширение перевода Mediawiki 

После того, как вики была убрана с SourceForge, [Yorik](User:Yorik.md) установил [расширение перевода MediaWiki](http://www.mediawiki.org/wiki/Help:Extension:Translate), которое облегчает переводы между страницами. Преимущество расширения для перевода в том, что он отслеживает переводы, уведомляет, если исходная страница была обновлена, и поддерживает синхронизацию переводов с оригинальной страницей на английском языке.

Инструмент описан в [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate) и является частью [MediaWiki Language Extension Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Чтобы быстро начать работу по подготовке страницы для перевода, пожалуйста, прочитайте [страницу с примером перевода](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/ru). По сути, требуется пара тэгов

    &lt;translate&gt; ... &lt;/translate&gt;

окружающих всю страницу, для активации системы перевода, и страница должна будет промаркирована для перевода.


<div class="mw-translate-fuzzy">

Чтобы увидеть пример того, как работает инструмент перевода, один раз плагин перевод активируется на странице, вы можете посетить [ Стартовую страницу](Main_Page/ru.md). Вы увидите новую языковую строку меню внизу. Она была сгенерирована автоматически. Нажмите, например, на немецкую ссылку, это преместит Вас на [ стартовую страницу на немецком языке](Main_Page/de.md). Прямо под названием, вы можете прочитать \"Эта страница представляет собой \'переведенную версию\' страницы Стартовая страница и перевод завершен на хх%.\" (Хх - это текущий фактический процент перевода). Нажмите на ссылку \"translated version\", чтобы начать перевод, либо обновить или исправить существующий перевод.


</div>


<div class="mw-translate-fuzzy">

Если вы перейдете на [Заглавную страницу](Main_Page/ru.md), то обнаружите, что вы не можете больше редактировать эту страницу напрямую нажатием на вкладку \[Редактировать\], и ссылка сверху *Править* будет заменена на *Перевести* которая будет открывать утилиту (плагин) для перевода.


</div>

При добавлении нового контента, вначале должна быть создана страница на английском языке, а затем она переводится на другой язык. Если кто-то хочет изменить или добавить контент на странице, английскую версию надо исправить в первую очередь.

Если вы не уверены, что делать с переводом, не стесняйтесь обратится за помощью на [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) или на [особый языковой субфорум](https://forum.freecadweb.org/viewforum.php?f=11) на [форуме FreeCAD](http://forum.freecadweb.org/).

### Важные замечания 

Каждый пользователь вики, имеющий права \"Редактора\", может запустить утилиту для перевода, записывать, сохранять и просматривать переводы.

Однако только пользователи с правами \"Администратора\" могут отмечать страницы для перевода. Страница, которая не помечена для перевода, не будет использовать расширение перевода и не будет правильно синхронизирована с информацией на английском языке.

Боковая панель расположенная слева также подлежит переведу, но только Администраторы могут изменить этот эллемент сайта. Пожалуйста, следуйте инструкциям на странице [Боковая панель Локализации](Localisation_Sidebar/ru.md).


<div class="mw-translate-fuzzy">

**Примечание:** первый раз при переключении страниц на новую систему перевода, она теряет все свои старые \"Ручные\" переводы. Чтобы восстановить перевод, вам необходимо открыть более раннюю версию из архива, и копировать / вставлять абзацы вручную в новой системе перевода.


</div>

### Translate the FreeCAD documentation 

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

### Старые инструкции по переводу 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| These instructions are for historical background only. Translations should use the new system with the [\#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) described above.                                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| So the first step is to **check if the manual translation has already been started for your language** (look in the left sidebar, under \"manual\").                                                                                                                                                                                                                                                                                                                                                                                                                     |
| If not, head to the [forum](http://forum.freecadweb.org/) and say that you want to start a new translation, we\'ll create the basic setup for the language you want to work on.                                                                                                                                                                                                                                                                                                                                                                                          |
| You must then [gain wiki edit permission](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| If your language is already listed, see what pages are still missing a translation (they will be listed in red). The technique is simple: **go into a red page, and copy/paste the contents of the corresponding English page, and start translating**.                                                                                                                                                                                                                                                                                                                  |
| Do not forget to include all the tags and templates from the original English page. Some of those templates will have an equivalent in your language (for example, there is a French Docnav template called Docnav/fr). You should use **a slash and your language code** in almost all the links. Look at other already translated pages to see how they did it.                                                                                                                                                                                                        |
| Add a slash and your language code in the categories, like \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| And if you are unsure, head to the forums and ask people to check what you did and tell you if it\'s right or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Four templates are commonly used in manual pages. These 4 templates have localized versions (Template:Docnav/fr, Template:fr, etc\...)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   [Template:GuiCommand](Template:GuiCommand.md) : is the Gui Command information block in upper-right of command documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template:Docnav](Template:Docnav.md) : it is the navigation bar at the bottom of the pages, showing previous and next pages.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template:Userdocnavi](Template:Userdocnavi.md) : gives direct links to the main base pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \'\'\' Page Naming Convention \'\'\'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
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
| The page \"Bienvenue dans l\'aide en ligne de FreeCAD\" redirects to Online\_Help\_Startpage/fr, and the page \"Fonctionnalités\" redirects to Feature\_list/fr.                                                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Перевод веб сайта FreeCAD 

Translation of the FreeCAD website is now done through [Crowdin](https://crowdin.com/translate/freecad/561/en-en). The file is named {{FileName|homepage.po}}.

## Разработка - Как добавить локализацию 

Этот раздел для разработчиков, которые хотят добавить окализацию в свой код.

### Подготовка ваших FreeCAD/master модулей для перевода 

These are the parts to the FreeCAD translation process:

-   extract text strings from source code into \*.ts files
-   load \*.ts files into [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   translation of strings within Crowdin
-   extract modified/new \*.ts files from Crowdin
-   convert \*.ts files into \*.qm files and update each module\'s \*.qrc file
-   update FreeCAD master

All of the above steps are performed by the \"translation scripts\" which are run by an administrator periodically.

Preparing your module for translation is quite easy. First, you need to ensure that you have a \"translations\" directory in {{FileName|myModule/Gui/Resources}}. Then open a terminal window (or Windows/OSX equivalent) in your \"translations\" directory and enter the following command: 
```pythonlupdate -ts myModule.ts```

This creates an empty translation file. Once this is done, you need to ensure that the translation scripts are updated as in this [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

Everything after this is automatic as far as a developer is concerned. The administrator will extract the text strings, the translators will translate them, then the administrator will extract the translations and update FreeCAD/master.

### Подготовка вашего стороннего модуля или макроса для перевода 

3rd party modules or macros are translated in much the same fashion, except that you must do some of the work yourself. This [forum discussion](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) describes the details.

Update: see [Translating an external workbench](Translating_an_external_workbench.md)

### Older module translation techniques 

[Localization Older Methods](Localization_Older_Methods.md) describes the use of translation tools such as Qt Linguist, lupdate, lrelease, pylupdate4, etc in detail. Most of this is no longer required for FreeCAD/master modules, but may be helpful preparing and updating 3rd party modules.

## Автоматическое обновление переводов Crowdin 

В настоящее время лица ведущие разработку FreeCAD используют [Crowdin скрипты](Crowdin_Scripts/ru.md) для извлечения и отправки переводов в Crowdin и обратно в репозиторий Github. Crowdin API предоставляет разработчикам FreeCAD возможность автоматизировать аспекты рабочего процесса перевода проекта, для получения дополнительной информации см. [Документация по Crowdin API](https://support.crowdin.com/api/api-integration-setup/).

## Связанные страницы 

-   [Crowdin Администрация](Crowdin_Administration/ru.md)
-   [Crowdin Скрипты](Crowdin_Scripts/ru.md)





 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Wiki](Category:Wiki.md)
