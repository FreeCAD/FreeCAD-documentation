# WikiPages/ru
This page is an extension of the [Help:Editing](Help_Editing.md) page and gives common guidelines for writing and updating the FreeCAD wiki documentation. It summarizes several discussions and brainstorming sessions



## Прежде чем начать 


<div class="mw-translate-fuzzy">

-   Эта вики - документация основана на [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), это программное обеспечение, абсолютно аналогичное [Википедии](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0). Если вы до этого вносили правки в Википедию, то редактирование вики-страниц FreeCAD для вас должно быть легкой задачей.
-   В отличие от Википедии, вики FreeCAD защищена от записи, чтобы избежать спама. Вы должны запросить учетную запись [на форуме](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   Если вы никогда раньше не использовали программное обеспечение wiki, пожалуйста, прочитайте [Help:Editing](Help_Editing.md), чтобы ознакомиться с используемой разметкой.
-   Для расширенного использования программного обеспечения wiki см. [MediaWiki Справка:Содержание](https://www.mediawiki.org/wiki/Help:Contents/ru). Не все функции MediaWiki доступны в этой вики FreeCAD, но многие из них доступны.
-   Нам нравится, чтобы документация была легкой для чтения, поэтому избегайте использования сложных функций. Пусть все будет просто.
-   Используйте песочницу для тестирования кода, например, [FreeCADDocu:Sandbox](FreeCADDocu_Sandbox.md) или конкретную страницу с вашим именем [Sandbox:Yourname](Sandbox_Yourname.md).
-   Пожалуйста, обратите внимание на переводы. Вики FreeCAD использует поддержку автоматического перевода для предоставления страниц на многих языках. Для каждой страницы может существовать несколько языковых версий. На многих страницах вы увидите теги, такие как <translate>...</translate> и множество отдельных тегов, таких как . Последние создаются системой перевода. Они связывают заголовки и абзацы со своими переведенными версиями. Вы не должны изменять их, так как это разрушит эти ссылки. Однако можно перемещать абзацы или изменять формулировки до тех пор, пока теги остаются с ними. Если вы удаляете заголовок или абзац, вы также должны удалить принадлежащий ему тег. Пожалуйста, имейте в виду, что изменения в существующих заголовках и абзацах влияют на текущие переводы. Ваши изменения должны быть действительно важны, чтобы этого стоить. Не беспокойтесь при добавлении нового материала, потому что система автоматически добавит новые теги после ваших изменений. Для получения дополнительной информации см. [Локализация](Localisation/ru.md) и оригинал [Mediawiki:Пример страницы для перевода](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/ru).


</div>



## Общие рекомендации 



### Краткие описания 

При описании FreeCAD старайтесь быть краткими, избегать повторений и излагать свои мысли по существу. Опишите, то что FreeCAD \"может сделать\", а не то, что он \"не может\". Также избегайте разговорных выражений, таких напримаер как \"пара\",\"около того\",\"вроде\". Когда имеете дело с неопределенным числом, пишите \"некоторое значение\" или укажите корректное количество.

Пример плохого описания
:   [Верстак PartDesign](PartDesign_Workbench/ru.md): верстак PartDesign, это верстак для проектирования деталей который предоставляет инструменты для моделирования сложных твердых деталей.





Пример хорошего описания
:   [Верстак PartDesign](PartDesign_Workbench/ru.md): предоставляет инструменты для проектирования сложных твердых тел.



### Централизованная информация 

Избегайте дублирования одной и той же информации в разных местах. Вставьте информацию на новую страницу и добавьте ссылку на эту страницу с других страниц, которым требуется эта информация.

Do not use transclusion of pages ([Help:Editing#Templates and transcluding pages](Help:Editing#Templates_and_transcluding_pages.md)), as this makes the wiki difficult to translate. Use only the templates described below in [#Templates](#Templates.md).



### Стиллизирование

Templates are used to style the help pages. They give the documentation a consistent look and feel. There is a template for menu commands, **File → Save**, a template to style keys to be pressed, **Shift**, to show a Boolean value, `True`, etc. Please get familiar with the [#Templates](#Templates.md) section before writing help pages.

### Temporary flags 

If you are working on a large page it is advisable to mark the page either as a work in progress or as unfinished. This assures that wiki admins don\'t mark your page as ready for translation while you are still changing it.

To flag a page add either  or  as the first line. With  you invite others to join you in finishing the page, while  indicates that you will do the work yourself and others should give you some time.

Once the work is done, please don\'t forget to remove the flags!



## Примеры

To quickly get familiar with the structure and style of the FreeCAD wiki look at the model page: [GuiCommand model](GuiCommand_model.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Structure


<div class="mw-collapsible-content">

The [User hub](User_hub.md) provides a [Table of Contents](Online_Help_Toc.md). This is used as the main reference for automatically building the offline help you can reach from FreeCAD, as well as the offline PDF documentation.

The [Template:Docnav](Template_Docnav.md) is used to sequentially link pages, following the structure of the [Table of Contents](Online_Help_Toc.md). See [#Templates](#Templates.md) for a list of all templates.



### Названия Страниц 

Page names should be short and they should use title case: every word should begin with a capital letter, unless they are articles, prepositions, conjunctions, or other grammatical particles (f.e. \'of\', \'on\', \'in\', \'a\', \'an\', \'and\').


<div class="mw-translate-fuzzy">


Плохое название для страницы:
:   Конструкция Аэропланов AeroCompany


</div>


<div class="mw-translate-fuzzy">


Хорошее название:
:   Конструкция аэропланов AeroCompany


</div>

The names of top level workbench pages must have this format: XYZ Workbench, where XYZ is the name of the workbench, for example [PartDesign Workbench](PartDesign_Workbench.md). And the names of pages describing the commands (or tools) belonging to a workbench must have this format: XYZ Command, for example [PartDesign Pad](PartDesign_Pad.md). Note that you should use the command name as it occurs in the source code.



### Заголовки

Paragraph headings should be short and use sentence case: all words except the first one and proper names, should be in lowercase. You should not use H1 headings (= Heading =) in your wiki markup since the page title is automatically added as the main H1 heading.



### Ссылки

Вы должны использовать оригинальное название ссылки, если это возможно. Это уточняет страницу, на которую ссылается печатная или offline документация. Пожалуйста, избегайте бессмысленных слов для ссылки.

Плохая ссылка
:   Для получения более подробной информации по рисованию 2D объектов кликните [тута](Draft_Workbench/ru.md).





Хорошая ссылка
:   Для получения более подробной информации о рисовании 2D обратитесь к [верстаку Draft](Draft_Workbench/ru.md).

Предпочтительным форматом для ссылки является:


<div class="mw-translate-fuzzy">

[name of page](Name_of_page.md)


</div>

После перевода:


<div class="mw-translate-fuzzy">

[название страницы](Name_of_page/ru.md)


</div>

Note that for the part before the | character, the actual link, case is relevant. If your page name is Name_of_page the link will fail if you type Name_of_Page (upper case P). Before the | character all spaces should be replaced by underscores (_). This is to assist translators using translation software, without the underscores the link would be translated by the software which is undesirable.

To link to a certain paragraph add a # sign and its headings to the page name. Example:

[WikiPages](WikiPages#Links.md)

После перевода:

[WikiPages](WikiPages/fr#Liens.md)

Within the same page you can omit the page name. Example:

[Links](#Links.md)

To link to the top of the page you can use:

</translate>{{Top}}<translate>

This template should automatically display the correct text depending on the language of the page. A link to the top of the page is especially useful for long pages as it allows the user to quickly jump back to the table of content. You can put it at the end of each paragraph. Make sure there is an empty line before and after the template.

Image link

:   <img alt="Optional text that is shown when you hover the image\|link=Draft_Wire" src=images/Draft_Wire.svg  style="width:24px;">

To use an image as a link:

![](images/)

Image link + text link
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md)

If you leave out the optional text the link itself will be shown when the image is hovered, which is preferable, and you should also add a text link after the image link:

![](images/)_[Draft_Wire](Draft_Wire.md)



### Страницы верстаков 

A top level workbench page should start with:

-   A description of what the workbench is used for.
-   An image to illustrate the description.

See [#Screen capture](#Screen_capture.md) for conventions on including images.

### Command pages 

Command pages describing workbench tools should not be too long, they should only explain what a command can do and what it can\'t, and how to use it. You should keep pictures and examples to a minimum. Tutorials can expand on how to use the tool and provide step-by-step details.

Please refer to the [GuiCommand model](GuiCommand_model.md) page for more details.



### Руководства

A well written tutorial should teach how to achieve certain practical results quickly. It shouldn\'t be too long, but should include sufficient step-by-step instructions and images to guide the user. As FreeCAD evolves, tutorials may become obsolete, so it is important to mention the FreeCAD version used in, or required for, a tutorial.

For examples visit the [Tutorials](Tutorials.md) page.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Шаблоны


<div class="mw-collapsible-content">

Styling of the FreeCAD wiki pages is achieved through the use of templates ([Help:Editing#Templates_and_transcluding_pages](Help:Editing#Templates_and_transcluding_pages.md)). They ensure a standardized look and feel across all pages, and also make it possible to re-style the wiki. You can see the complete list of defined templates by accessing [Special:PrefixIndex/Template:](Special:PrefixIndex/Template:.md). But please only use the templates listed in the tables below. Only in very special cases should you use HTML tags directly.

Click on the template link to see the usage instructions for a template, and to see its implementation. Templates are a powerful feature of the MediaWiki software. You should be an experienced wiki user if you wish to propose additions and modifications to existing templates. If implemented incorrectly, templates make it difficult to translate pages into other languages, so their use should be limited to text formatting, page transclusion should be avoided. See [MediaWiki Help:Templates](https://www.mediawiki.org/wiki/Help:Templates) to learn more.



### Простейшие шаблоны 

Эти шаблоны форматируют простой текстовый параметр в определенном стиле.

++++
| Шаблон                                                                                                        | Внешний вид                            | Описание                                                                                                                                                                                                                                                                                       |
+===============================================================================================================+========================================+================================================================================================================================================================================================================================================================================================+
| [Top](Template_Top.md)                                                                                |                         | Use it to add a link to the top of the page.                                                                                                                                                                                                                                                   |
|                                                                                                               | {{Top}}                                |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Emphasis](Template_Emphasis.md)                                                                      |                         | Используйте его, чтобы подчеркнуть фрагмент текста.                                                                                                                                                                                                                                            |
|                                                                                                               | **emphasis**                  |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [KEY](Template_KEY.md)                                                                                |                         | Используйте его в случае, когда нужно указать клавишу клавиатуры, которую необходимо нажать.                                                                                                                                                                                                   |
|                                                                                                               | **Alt**                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [ASCII](Template_ASCII.md)                                                                            |                         | Используйте его, для отображения клавиши в виде (.svg) изображения, которую нужно нажать. В качестве параметра, вы должны указать желаемый символ или номер ascii-кода символа.                                                                                                                |
|                                                                                                               | {{ASCII|A}}                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Button](Template_Button.md)                                                                          |                         | Используйте его для указания кнопки в графическом пользовательском интерфейсе, которую необходимо нажать.                                                                                                                                                                                      |
|                                                                                                               | **Cancel**                      |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [RadioButton](Template_RadioButton.md)                                                                |                         | Use it to indicate a radio button in the graphical user interface that needs to be {{RadioButton|TRUE|Selected}} or {{RadioButton|FALSE|Not}}.                                                                                                                     |
|                                                                                                               | {{RadioButton|Option}}                 |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [CheckBox](Template_CheckBox.md)                                                                      |                         | Use it to indicate a checkbox in the graphical user interface that needs to be {{CheckBox|TRUE|Checked}} or {{CheckBox|FALSE|Not}}.                                                                                                                                |
|                                                                                                               | {{CheckBox|Option}}                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [SpinBox](Template_SpinBox.md)                                                                        |                         | Use it to indicate a spinbox in the graphical user interface that needs to be modified.                                                                                                                                                                                                        |
|                                                                                                               | {{SpinBox|1.50}}                       |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [ComboBox](Template_ComboBox.md)                                                                      |                         | Use it to indicate a combobox in the graphical user interface that needs to be modified.                                                                                                                                                                                                       |
|                                                                                                               | {{ComboBox|Menu 1}}                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [LineEdit](Template_LineEdit.md)                                                                      |                         | Use it to indicate a LineEdit in the graphical user interface that needs to be modified.                                                                                                                                                                                                       |
|                                                                                                               | {{LineEdit|Metal Nickel (Ni)}}         |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [FALSE](Template_FALSE.md), [false](Template_false.md)                                        |                         | Use it to indicate a False Boolean value, for example, as a property in the [property editor](Property_editor.md). This is a shortcut. Since it is a value, prefer Template [Value](Template_Value.md) {{Value|false}}                                           |
|                                                                                                               | `False`                              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
|                                                                                                               | , {{false}}              |                                                                                                                                                                                                                                                                                                |
++++
| [TRUE](Template_TRUE.md), [true](Template_true.md)                                            |                         | Use it to indicate a True Boolean value, for example, as a property in the [property editor](Property_editor.md). This is a shortcut. Since it is a value, prefer Template [Value](Template_Value.md) {{Value|true}}                                             |
|                                                                                                               | `True`                               |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
|                                                                                                               | , {{true}}               |                                                                                                                                                                                                                                                                                                |
++++
| [MenuCommand](Template_MenuCommand.md)                                                                |                         | Use it to indicate the location of a command inside a particular menu.                                                                                                                                                                                                                         |
|                                                                                                               | **File → Save**            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [FileName](Template_FileName.md)                                                                      |                         | Используйте его для указания имени файла или каталога.                                                                                                                                                                                                                                         |
|                                                                                                               | **File name**                 |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [SystemInput](Template_SystemInput.md)                                                                |                         | Use it to indicate user typed input text.                                                                                                                                                                                                                                                      |
|                                                                                                               | {{SystemInput|Type this text}}         |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [SystemOutput](Template_SystemOutput.md)                                                              |                         | Use it to indicate text output from the system.                                                                                                                                                                                                                                                |
|                                                                                                               | {{SystemOutput|Output text}}           |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Incode](Template_Incode.md)                                                                          |                         | Используйте его для выделения блоков исходного кода написанного моноширинным шрифтом. Содержимое должно умещаться в одну строку.                                                                                                                                                               |
|                                                                                                               | `import FreeCAD`              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [PropertyView](Template_PropertyView.md)                                                              |                         | Use it to indicate a View property in the [property editor](Property_editor.md). Examples of View properties include {{emphasis|Line Color}}, {{emphasis|Line Width}}, {{emphasis|Point Color}}, {{emphasis|Point Size}}, etc. |
|                                                                                                               | **Color**                 |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [PropertyData](Template_PropertyData.md)                                                              |                         | Use it to indicate a Data property in the [property editor](Property_editor.md). Data properties are different for different types of objects.                                                                                                                                         |
|                                                                                                               | **Position**              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Properties Title](Template_Properties_Title.md) / [TitleProperty](Template_TitleProperty.md) |                         | Use it to indicate the title of a property group in the [property editor](Property_editor.md). The title will not be included in the automatic table of contents.                                                                                                                      |
|                                                                                                               | {{Properties_Title|Base}}              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Obsolete](Template_Obsolete.md)                                                                      |                         | Используйте его, чтобы указать, что функция устарела в указанной версии FreeCAD.                                                                                                                                                                                                               |
|                                                                                                               | {{Obsolete|0.19}}                      |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Version/ru](Template:Version/ru.md)                                                                  |                         | Используйте его, чтобы указать, что функция была введена в указанной версии FreeCAD.                                                                                                                                                                                                           |
|                                                                                                               | {{Version/ru|0.18}}                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [VersionMinus](Template_VersionMinus.md)                                                              |                         | Use it to indicate that a feature is available in the specified FreeCAD version and earlier versions.                                                                                                                                                                                          |
|                                                                                                               | {{VersionMinus|0.16}}                  |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [VersionPlus](Template_VersionPlus.md)                                                                |                         | Use it to indicate that a feature is available in the specified FreeCAD version and later versions.                                                                                                                                                                                            |
|                                                                                                               | <small>(v0.17)</small>                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [ColoredText](Template_ColoredText.md)                                                                |                         | Use this template to color the background, text, or background and text. ([ColoredText](Template_ColoredText.md) page for more examples)                                                                                                                                               |
|                                                                                                               | {{ColoredText|Colored Text}}           |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [ColoredParagraph](Template_ColoredParagraph.md)                                                      |                         | Use this template to color the background, text, or background and text of an entire paragraph. ([ColoredParagraph](Template_ColoredParagraph.md) page for more examples)                                                                                                              |
|                                                                                                               | {{ColoredParagraph|Colored Paragraph}} |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++



### Сборные шаблоны 

These templates require more input parameters, or produce a block of text with a particular format.

++++
| Template                                                                                         | Appearance                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                |
+==================================================================================================+==============================================================================================================================+============================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template_Prettytable.md)                                                   | This table                                                                                                                   | Use it to format tables such as this one. Additional table properties can be added.                                                                                                                                                                                                                                        |
++++
| [Caption](Template_Caption.md)                                                           |                                                                                                                    | Use it to add an explanation below an image. It can be left aligned or center aligned.                                                                                                                                                                                                                                     |
|                                                                                                  | <div style="width:400px;">                                                                                                   |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                               |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  | 
*Some caption for an image*                                                                                        |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                    |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  | </div>                                                                                                                       |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [Clear](Template_Clear.md)                                                               |                                                                                                                              | Use it to clear columns. Follow the definition of the template for a detailed explanation. It is often used to stop text from flowing next to unrelated images.                                                                                                                                                            |
++++
| [Code](Template_Code.md)                                                                 |                                                                                                               | Use it to include multi-line code examples with a monospace font. The default language is Python, but other languages can be specified.                                                                                                                                                                                    |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                                 |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           | [Python](Python.md) code should adhere to the general recommendations established by [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). In particular, parentheses should immediately follow the function name, and a space should follow a comma. This makes the code more readable. |
++++
| [CodeDownload](Template_CodeDownload.md)                                                 |                                                                                                               | Use it to create a link on a [macro](Macros.md) page.                                                                                                                                                                                                                                                              |
|                                                                                                  | {{CodeDownload|https://wiki.freecad.org/Main_Page|Some label}}                                                               |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [Codeextralink](Template_Codeextralink.md)                                               |                                                                                                               | Use it if the code of a [macro](Macros.md) is too large to be hosted on the Wiki. The code can then be hosted somewhere else, and the raw link to it specified with this template. The [Addon Manager](Std_AddonMgr.md) will use this link.                                                                |
|                                                                                                  | {{Codeextralink|https://wiki.freecad.org/Main_Page}}                                                                         |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [Fake heading](Template_Fake_heading.md)                                                 |                                                                                                               | Use it to create a heading that will not be automatically included in the table of contents.                                                                                                                                                                                                                               |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                   |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [GuiCommand](Template_GuiCommand.md)                                                     | See [GuiCommand model](GuiCommand_model.md)                                                                          | Use it to create a box with useful information to document workbench commands (tools).                                                                                                                                                                                                                                     |
++++
| [TutorialInfo](Template_TutorialInfo.md)                                                 | See for example [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                | Use it to create a box with useful information to document [tutorials](Tutorials.md).                                                                                                                                                                                                                              |
++++
| [Macro](Template_Macro.md)                                                               | See for example [Macro FlattenWire](Macro_FlattenWire.md)                                                            | Use it to create a box with useful information to document [macros](macros.md).                                                                                                                                                                                                                                    |
++++
| [Docnav](Template_Docnav.md)                                                             |                                                                                                               | Use it to create a bar with arrows and appropriate links, which is useful for putting pages in a particular sequence.                                                                                                                                                                                                      |
|                                                                                                  |                                                                                 |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [VeryImportantMessage](Template_VeryImportantMessage.md)                                 |                                                                                                               | Use it to create a highlighted box with a very important message. Use sparingly, only to indicate major problems in the functionality of the software, discontinuation of tools, and similar.                                                                                                                              |
|                                                                                                  | **Important Message**                                                                                   |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [Page in progress](Template_Page_in_progress.md)                                         |                                                                                                               | Use this for pages that are still in progress or that are currently being reworked. Don\'t forget to remove this when the page is ready.                                                                                                                                                                                   |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                        |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [UnfinishedDocu](Template_UnfinishedDocu.md)                                             |                                                                                                               | Use it to create a highlighted box indicating an unfinished documentation page.                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [Softredirect](Template_Softredirect.md)                                                 |                                                                                                                              | Use it instead of the normal redirect, when you are redirecting to a special page (such as Media: or Category:), in which cases the normal redirect is disabled.                                                                                                                                                           |
++++
| [Quote](Template_Quote.md)                                                               |                                                                                                               | Use it to create a box of text with a literal quote and reference.                                                                                                                                                                                                                                                         |
|                                                                                                  | {{Quote|text=Cry "Havoc" and let slip the dogs of war.|sign=William Shakespeare|source=''Julius Caesar'', act III, scene I}} |                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                            |
++++
| [Userdocnavi](Template_Userdocnavi.md), [Powerdocnavi](Template_Powerdocnavi.md) |                                                                                                                              | Use them to create navigation boxes for the user documentation, the power user documentation, and the developer documentation. This allows quickly jumping between different sections of the documentation. They also place the corresponding page in the proper category.                                                 |
++++


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Графика


<div class="mw-collapsible-content">

Изображения и скриншоты необходимы для создания полной документации FreeCAD. Они особенно полезны для иллюстрации примеров и учебных пособий. Изображения должны быть показаны в их оригинальном размере, чтобы они представляли достаточную детализацию и были читабельны, если они содержат в себе текст. Размеры [растровых изображений](bitmap/ru.md) не могут быть изменены.

Избегайте анимированных картинок (GIF) на страницах общей справки. Анимации и видео следует зарезервировать для учебных пособий, не предназначенных для использования в качестве offline документации в формате PDF.

Изображения можно загрузить через [Special:Upload](Special:Upload/ru.md) страницу.

### Name

Give meaningful names to your images. If you have an image that showcases the characteristics of a particular command, you should use the name of that command with `_example` at the end. For example for the command [Draft Offset](Draft_Offset.md) the image should be called `Draft_Offset_example.png`.



### Снимки с экрана 

Рекомендуемые размеры для снимков экрана::

-   400x200 (или ширина=400 и высота\<=200) для страниц [описывающих команнды Gui](GuiCommand_model/ru.md), чтобы изображение помещалось в левой части страницы, а также для других стандартных снимков.
-   600x400 (или ширина=600 и высота\<=400), для страниц [описывающих команнды Gui](GuiCommand_model/ru.md), только когда вам действительно нужно изображение большего размера, и при этом старйтесь уместить изображение в левой части страницы, а также для других стандартных снимков.
-   1024x768 (или ширина=1024 и высота\<=768), только для полноэкранных изображений.
-   При отображении деталей возможны меньшие размеры.
-   Избегайте изображений с большим разрешением, так как они не будут очень переносимыми для других видов дисплеев или печатной документации в формате PDF.

Вы не должны зависеть от пользовательской конфигурации вашего рабочего стола или операционной системы при создании скриншотов, по возможности рекомендуется использовать визуальные настройки интерфейса FreeCAD по умолчанию.

To create a screenshots you can use the options provided by your operating system, or one of these macros: <img alt="" src=images/Snip.png  style="width:24px;"> [Macro Snip](Macro_Snip.md) and <img alt="" src=images/Macro_Screen_Wiki.png  style="width:24px;"> [Macro Screen Wiki](Macro_Screen_Wiki.md).

### Text

To ease documentation translations, try to avoid screenshots that contain texts. If you cannot avoid this, consider taking separate screenshots of the interface and the [3D view](3D_view.md). The image of the 3D view can be reused in every translation, while a translator can take a screenshot of the localized interface if necessary.



### Иконки и графика 

Refer to the [Artwork](Artwork.md) page for all artwork and icons that have been created for FreeCAD, and which can also be used in documentation pages. If you would like to contribute icons, please read the [Artwork Guidelines](Artwork_Guidelines.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Переводы


<div class="mw-collapsible-content">

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

The FreeCAD wiki supports a translation extension that allows managing translations between pages easier; for details, see [Localisation Translating the wiki](Localisation#Translating_the_wiki.md).

Other useful resources are:

-   [ISO language codes](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) to identify the two-letter code for a particular language that you want to translate to.
-   [Google Translate](http://translate.google.com/) for help with translations.
-   [Deepl translator](https://www.deepl.com/translator) for help with translations.



## Несколько советов для переводчиков 

### Translate GuiCommand 

    {{GuiCommand
    |Name=FEM EquationFlux
    |MenuLocation=Solve → Flux equation
    |Workbenches=[FEM](FEM_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Translated:

    {{GuiCommand/fr
    |Name=FEM EquationFlux
    |Name/fr=FEM Équation d'écoulement
    |MenuLocation=Solveur → Équation de flux
    |Workbenches=[Atelier FEM](FEM_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM Tutoriel](FEM_tutorial/fr.md)
    }}

### Translate navi 

    {{FEM_Tools_navi}}

Translated:

    {{FEM_Tools_navi/fr}}

### Translate link 

    [Part Workbench](Part_Workbench.md)

Translated:

    [Atelier Part](Part_Workbench/fr.md)

### Translate Docnav 

    

Translated:

    

Example with icons:

    

Translated:

    


</div>


</div>



## Создание, переименовывание и удаление страниц 

### Create pages 

Before creating a new page you should first check if a similar page already exists. If that is the case it is usually better to edit that existing page instead. When in doubt please open a topic in the [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21) first.

To create a new page do one of the following:

-   Visit the URL with the desired page name, for example: https://wiki.freecadweb.org/My_New_Page, and click on \'create this page\'.
-   Do a wiki search for the page name, and click on the red text in \'Create the page \"My New Page\" on this wiki!\'.

### Rename pages 

Since FreeCAD is a project under permanent development, it is sometimes necessary to revise the content of the wiki. If the names of commands are changed in the source code, the wiki pages documenting them have to be renamed as well. This can only be done by wiki administrators. To inform them, open a topic in the [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21) and list the necessary renaming operation in this form:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...



### Удаление файлов и страниц 

В случае, если вам нужно удалить файл, перейдите на его страницу (https://www.freecadweb.org/wiki/File:***.***) и отредактируйте его. Независимо от того, является ли страница пустой или нет, добавьте это в качестве первого элемента: {{Delete}} и прямо под ним опишите, почему страница должна быть удалена. Помимо этого, откройте тему в [Вики-форуме](https://forum.freecadweb.org/viewforum.php?f=21).

Для страниц процедура идентичная.



## Обсуждение

The [Development/Wiki subforum](http://forum.freecadweb.org/viewforum.php?f=21) in the [FreeCAD forum](https://forum.freecadweb.org) provides a dedicated space for discussing wiki topics, the wiki appearance and anything else related to the wiki. Direct your questions and suggestions there.



## Терминология - стратегия именования 



### На английском 

Смотри [Глоссарий](Glossary/ru.md).



### Другие языки 

-   [Italiano](Italian_Translation.md)
-   [Français](French_Translation.md)
-   [Deutsch](German_Translation.md)
-   [Polish](Polish_Translation.md)
-   [Spanish](Spanish_Translation.md)



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > [Wiki](Category_Wiki.md) > [Wiki Documentation](Category_Wiki%20Documentation.md) > [Administration](Category_Administration.md) > [FEM](Category_FEM.md) > WikiPages/ru
