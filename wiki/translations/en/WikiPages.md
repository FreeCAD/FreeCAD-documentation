# WikiPages/en
{{TOCright}}

This page is an extension of the _ page and gives common guidelines for writing and updating the FreeCAD wiki documentation. It summarizes several discussions and brainstorming sessions

## Before starting 

-   This wiki documentation is based on [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), the same software that powers [Wikipedia](https://en.wikipedia.org/wiki/Main_Page). If you have contributed to Wikipedia, editing FreeCAD wiki pages should be easy.
-   Contrary to Wikipedia, the FreeCAD wiki is write-protected to avoid spam. You must request an account [on the forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   If you have never used wiki software before, please read _ to become familiar with the markup that is used.
-   For advanced use of the wiki software, see [MediaWiki Help:Contents](https://www.mediawiki.org/wiki/Help:Contents). Not all features of MediaWiki are available in this FreeCAD wiki, but many are.
-   We like to keep the documentation easy to read, so avoid using complex features. Keep it simple.
-   Use a sandbox to test your code, for example, _ or a particular page with your name _. Sandbox pages must be placed in the Sandbox category. This is done by adding [[Category:Sandbox]] at the bottom of the wiki code.
-   Please be aware of the translations. The FreeCAD wiki uses automated translation support to provide pages in many languages. For every page multiple language versions can exist. On many pages you will see tags like <translate>...</translate> and many single tags like . The latter mark so-called translation units and are created by the translation system, you should never create them manually. They link the headings and paragraphs to their translated versions. You should not change them as that would destroy those links. It is however fine to move paragraphs or change wording as long as the tags stay with them. If you remove a heading or a paragraph you should also remove the tag belonging to it. Please be aware that changes to existing headings and paragraphs affect the current translations. Your changes should be worth it. Do not worry when adding new material because the system will add new tags automatically after your edits. For more information see [Localisation](Localisation.md) and the original [Mediawiki:Extension:Translate page](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example).

## General guidelines 

### Concise descriptions 

When describing FreeCAD try to be concise and to the point and avoid repetition. Describe what FreeCAD *does*, not what FreeCAD *does not do*. Also avoid colloquial expressions such as \'a couple\'. Use \'some\' when dealing with an indeterminate number, or specify the correct quantity.

Bad description
:   [PartDesign Workbench](PartDesign_Workbench.md): the PartDesign Workbench is a workbench for part design that aims to provide tools for modelling complex solid parts.





Good description
:   [PartDesign Workbench](PartDesign_Workbench.md): aims to provide tools for modelling complex solid parts.

### Centralized information 

Avoid duplicating the same information in different places. Insert the information in a new page, and link to this page from other pages that require this information.

Do not use transclusion of pages (_), as this makes the wiki difficult to translate. Use only the templates described below in [\#Templates](#Templates.md).

### Styling

Templates are used to style the help pages. They give the documentation a consistent look and feel. There is a template for menu commands, **File → Save**, a template to style keys to be pressed, **Shift**, to show a Boolean value, `True`, etc. Please get familiar with the [\#Templates](#Templates.md) section before writing help pages.

### Temporary flags 

If you are working on a large page it is advisable to mark the page either as a work in progress or as unfinished. This assures that wiki admins don\'t mark your page as ready for translation while you are still changing it.

To flag a page add either  or  as the first line. With  you invite others to join you in finishing the page, while  indicates that you will do the work yourself and others should give you some time.

Once the work is done, please don\'t forget to remove the flags!

## Examples

To quickly get familiar with the structure and style of the FreeCAD wiki look at the model page: [GuiCommand model](GuiCommand_model.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Structure


<div class="mw-collapsible-content">

The [User hub](User_hub.md) provides a [Table of Contents](Online_Help_Toc.md). This is used as the main reference for automatically building the offline help you can reach from FreeCAD, as well as the offline PDF documentation.

The _ is used to sequentially link pages, following to the structure of the [Table of Contents](Online_Help_Toc.md). See [\#Templates](#Templates.md) for a list of all templates.

### Page names 

Page names should be short, and they should use sentence case: all words except the first one and proper names, should be in lowercase. This is the [style used by Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Capital_letters#Headings,_headers,_and_captions) for their articles.

Bad page name:
:   Construction Of AeroCompany Airplanes





Good page name:
:   Construction of AeroCompany airplanes

The names of top level workbench pages must have this format: XYZ Workbench, where XYZ is the name of the workbench, for example _. Note that you should use the command name as it occurs in the source code.

A previous convention was to use title case: every word should begin with a capital letter, unless they are articles, prepositions, conjunctions, or other grammatical particles (f.e. \'of\', \'on\', \'in\', \'a\', \'an\', \'and\'). There are many existing pages using this style, but it is discouraged for new pages. This was discussed in the forum thread [(Lowercase links) Use a lower case title for a wiki page](https://forum.freecadweb.org/viewtopic.php?p=266029#p266029).

### Headings

Like page names, paragraph headings should be short and use sentence case. You should not use H1 headings (= Heading =) in your wiki markup since the page title is automatically added as the main H1 heading.

### Links

You should use the original link name for links whenever possible. This clarifies the referenced page in printed or offline documentation. Please avoid non-meaningful words for the link.

Bad link
:   For more information on drafting 2D objects click [here](Draft_Workbench.md).





Good link
:   For more information on drafting 2D objects refer to the [Draft Workbench](Draft_Workbench.md).

The preferred format for a link is:

[name of page](Name_of_page.md)

Translated:

[nom de la page](Name_of_page/fr.md)

Note that for the part before the | character, the actual link, case is relevant. If your page name is Name_of_page the link will fail if you type Name_of_Page (upper case P). Before the | character all spaces should be replaced by underscores (_). This is to assist translators using translation software, without the underscores the link would be translated by the software which is undesirable.

To link to a certain paragraph add a # sign and its headings to the page name. Example:

[WikiPages](WikiPages#Links.md)

Translated:

[WikiPages](WikiPages/fr#Liens.md)

Within the same page you can omit the page name. Example:

[Links](#Links.md)

To link to the top of the page you can use:

</translate>{{Top}}<translate>

This template should automatically display the correct text depending on the language of the page. A link to the top of the page is especially useful for long pages as it allows the user to quickly jump back to the table of content. You can put it at the end of each paragraph. Make sure there is an empty line before and after the template.

Image link
:   <img alt="Optional text that is shown when you hover the image\|link=Draft\_Wire" src=images/Draft_Wire.svg  style="width:24px;">

To use an image as a link:

![](images/)

Image link + text link
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md)

If you leave out the optional text the link itself will be shown when the image is hovered, which is preferable, and you should also add a text link after the image link:

![](images/)_[Draft_Wire](Draft_Wire.md)

### Workbench pages 

A top level workbench page should start with:

-   A description of what the workbench is used for.
-   An image to illustrate the description.

See [\#Screen capture](#Screen_capture.md) for conventions on including images.

### Command pages 

Command pages describing workbench tools should not be too long, they should only explain what a command can do and what it can\'t, and how to use it. You should keep pictures and examples to a minimum. Tutorials can expand on how to use the tool and provide step-by-step details.

Please refer to the [GuiCommand model](GuiCommand_model.md) page for more details.

### Tutorials

A well written tutorial should teach how to achieve certain practical results quickly. It shouldn\'t be too long, but should include sufficient step-by-step instructions and images to guide the user. As FreeCAD evolves, tutorials may become obsolete, so it is important to mention the FreeCAD version used in, or required for, a tutorial.

For examples visit the [Tutorials](Tutorials.md) page.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Templates


<div class="mw-collapsible-content">

Styling of the FreeCAD wiki pages is achieved through the use of templates (_). They ensure a standardized look and feel across all pages, and also make it possible to re-style the wiki. You can see the complete list of defined templates by accessing _. But please only use the templates listed in the tables below. Only in very special cases should you use HTML tags directly.

Click on the template link to see the usage instructions for a template, and to see its implementation. Templates are a powerful feature of the MediaWiki software. You should be an experienced wiki user if you wish to propose additions and modifications to existing templates. If implemented incorrectly, templates make it difficult to translate pages into other languages, so their use should be limited to text formatting, page transclusion should be avoided. See [MediaWiki Help:Templates](https://www.mediawiki.org/wiki/Help:Templates) to learn more.

### Simple templates 

These templates accept a simple text parameter, and format it with a particular style.

+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Template                                                                                                      | Appearance                             | Description                                                                                                                                                                                                                                                                                    |
+===============================================================================================================+========================================+================================================================================================================================================================================================================================================================================================+
| _                                                                                |                         | Use it to add a link to the top of the page.                                                                                                                                                                                                                                                   |
|                                                                                                               | {{Top}}                                |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                         | Use it to emphasize a piece of text.                                                                                                                                                                                                                                                           |
|                                                                                                               | **emphasis**                  |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                                |                         | Use it to indicate a keyboard key that needs to be pressed.                                                                                                                                                                                                                                    |
|                                                                                                               | **Alt**                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                            |                         | Use it to indicate a ascii key in a image (.svg) that needs to be pressed. You must give the character desired or the number of the code ascii of the character.                                                                                                                               |
|                                                                                                               | {{ASCII|A}}                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                          |                         | Use it to indicate a button in the graphical user interface that needs to be pressed.                                                                                                                                                                                                          |
|                                                                                                               | **Cancel**                      |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                         | Use it to indicate a radio button in the graphical user interface that needs to be {{RadioButton|TRUE|Selected}} or {{RadioButton|FALSE|Not}}.                                                                                                                     |
|                                                                                                               | {{RadioButton|Option}}                 |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                         | Use it to indicate a checkbox in the graphical user interface that needs to be {{CheckBox|TRUE|Checked}} or {{CheckBox|FALSE|Not}}.                                                                                                                                |
|                                                                                                               | {{CheckBox|Option}}                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                        |                         | Use it to indicate a spinbox in the graphical user interface that needs to be modified.                                                                                                                                                                                                        |
|                                                                                                               | {{SpinBox|1.50}}                       |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                         | Use it to indicate a combobox in the graphical user interface that needs to be modified.                                                                                                                                                                                                       |
|                                                                                                               | {{ComboBox|Menu 1}}                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _, _                                        |                         | Use it to indicate a False Boolean value, for example, as a property in the _ {{Value|false}}                                           |
|                                                                                                               | `False`                              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
|                                                                                                               | , {{false}}              |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _, _                                            |                         | Use it to indicate a True Boolean value, for example, as a property in the _ {{Value|true}}                                             |
|                                                                                                               | `True`                               |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
|                                                                                                               | , {{true}}               |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                         | Use it to indicate the location of a command inside a particular menu.                                                                                                                                                                                                                         |
|                                                                                                               | **File → Save**            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                         | Use it to indicate a name of a file or directory.                                                                                                                                                                                                                                              |
|                                                                                                               | {{FileName|File name}}                 |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                         | Use it to indicate user typed input text.                                                                                                                                                                                                                                                      |
|                                                                                                               | {{SystemInput|Type this text}}         |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                         | Use it to indicate text output from the system.                                                                                                                                                                                                                                                |
|                                                                                                               | {{SystemOutput|Output text}}           |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                          |                         | Use it to include in-line source code with a monospace font. It should fit in one line.                                                                                                                                                                                                        |
|                                                                                                               | `import FreeCAD`              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                         | Use it to indicate a View property in the [property editor](Property_editor.md). Examples of View properties include {{emphasis|Line Color}}, {{emphasis|Line Width}}, {{emphasis|Point Color}}, {{emphasis|Point Size}}, etc. |
|                                                                                                               | **Color**                 |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                         | Use it to indicate a Data property in the [property editor](Property_editor.md). Data properties are different for different types of objects.                                                                                                                                         |
|                                                                                                               | **Position**              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _ / _ |                         | Use it to indicate the title of a property group in the [property editor](Property_editor.md). The title will not be included in the automatic table of contents.                                                                                                                      |
|                                                                                                               | {{Properties_Title|Base}}              |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                         | Use it to indicate that a feature became obsolete in the specified FreeCAD version.                                                                                                                                                                                                            |
|                                                                                                               | {{Obsolete|0.19}}                      |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                        |                         | Use it to indicate that a feature was introduces in the specified FreeCAD version.                                                                                                                                                                                                             |
|                                                                                                               | <small>(v0.18)</small>                        |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                         | Use it to indicate that a feature is available in the specified FreeCAD version and earlier versions.                                                                                                                                                                                          |
|                                                                                                               | {{VersionMinus|0.16}}                  |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                         | Use it to indicate that a feature is available in the specified FreeCAD version and later versions.                                                                                                                                                                                            |
|                                                                                                               | <small>(v0.17)</small>                    |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                         | Use this template to color the background, text, or background and text. (_ page for more examples)                                                                                                                                               |
|                                                                                                               | {{ColoredText|Colored Text}}           |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                      |                         | Use this template to color the background, text, or background and text of an entire paragraph. _ page for more examples)                                                                                                               |
|                                                                                                               | {{ColoredParagraph|Colored Paragraph}} |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Complex templates 

These templates require more input parameters, or produce a block of text with a particular format.

+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Template                                                                                         | Appearance                                                                                                                   | Description                                                                                                                                                                                                                                                                                                               |
+==================================================================================================+==============================================================================================================================+===========================================================================================================================================================================================================================================================================================================================+
| _                                                   | This table                                                                                                                   | Use it to format tables such as this one. Additional table properties can be added.                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                           |                                                                                                                    | Use it to add an explanation below an image. It can be left aligned or center aligned.                                                                                                                                                                                                                                    |
|                                                                                                  | <div style="width:400px;">                                                                                                   |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                               |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  | 
*Some caption for an image*                                                                                        |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                    |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  | </div>                                                                                                                       |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                               |                                                                                                                              | Use it to clear columns. Follow the definition of the template for a detailed explanation. It is often used to stop text from flowing next to unrelated images.                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                 |                                                                                                               | Use it to include multi-line code examples with a monospace font. The default language is Python, but other languages can be specified.                                                                                                                                                                                   |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                                 |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           | [Python](Python.md) code should adhere to the general recommendations established by [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). In particular, parentheses should immediately follow the function name, and a space should follow a comma. This makes the code more readable |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                 |                                                                                                               | Use it to create a heading that will not be automatically included in the table of contents.                                                                                                                                                                                                                              |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                   |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                     | See [GuiCommand model](GuiCommand_model.md)                                                                          | Use it to create a box with useful information to document workbench commands (tools).                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                 | See for example [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                | Use it to create a box with useful information to document [tutorials](Tutorials.md).                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                               | See for example [Macro FlattenWire](Macro_FlattenWire.md)                                                            | Use it to create a box with useful information to document [macros](macros.md).                                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                             |                                                                                                               | Use it to create a bar with the words \'next\', \'previous\', and \'index\', and the appropriate links, which is useful for putting pages in a particular sequence.                                                                                                                                                       |
|                                                                                                  |                                                                                 |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                 |                                                                                                               | Use it to create a highlighted box with a very important message. Use sparingly, only to indicate major problems in the functionality of the software, discontinuation of tools, and similar.                                                                                                                             |
|                                                                                                  | **Important Message**                                                                                   |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                         |                                                                                                               | Use this for pages that are still in progress or that are currently being reworked. Don\'t forget to remove this when the page is ready.                                                                                                                                                                                  |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                        |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                             |                                                                                                               | Use it to create a highlighted box indicating an unfinished documentation page.                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                 |                                                                                                                              | Use it instead of the normal redirect, when you are redirecting to a special page (such as Media: or Category:), in which cases the normal redirect is disabled.                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                               |                                                                                                               | Use it to create a box of text with a literal quote and reference.                                                                                                                                                                                                                                                        |
|                                                                                                  | {{Quote|text=Cry "Havoc" and let slip the dogs of war.|sign=William Shakespeare|source=''Julius Caesar'', act III, scene I}} |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _, _ |                                                                                                                              | Use them to create navigation boxes for the user documentation, the power user documentation, and the developer documentation. This allows quickly jumping between different sections of the documentation. They also place the corresponding page in the proper category.                                                |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Graphics


<div class="mw-collapsible-content">

Images and screenshots are necessary to produce a complete documentation of FreeCAD. They are particularly useful to illustrate examples and tutorials. Images should be shown in their original size, so they present sufficient detail and are readable if they include text. [Bitmap](bitmap.md) images should not be resized.

Avoid animated pictures (GIF) in the general help pages. Animations and videos should be reserved for tutorials not intended to be used as offline PDF documentation.

Images can be uploaded through the _ page.

### Name

Give meaningful names to your images. If you have an image that showcases the characteristics of a particular command, you should use the name of that command with `_example` at the end. For example for the command [Draft Offset](Draft_Offset.md) the image should be called `Draft_Offset_example.jpg`.

### Screen capture 

Recommended sizes for screen captures are:

-   Native 400x200 (or width=400 and height\<=200), for [command reference](GuiCommand_model.md) pages, to allow the picture to fit in the left part of the page, and for other standard snapshots.
-   Native 600x400 (or width=600 and height\<=400), for [command reference](GuiCommand_model.md) pages, when you really need a bigger picture, and still allow the picture to fit in the left part of the page, and for other standard snapshots.
-   Native 1024x768 (or width=1024 and height\<=768), only for full screen images.
-   Smaller sizes are possible when showing details.
-   Avoid images with larger resolutions, as they won\'t be very portable to other kinds of displays or the printed PDF documentation.

You shouldn\'t depend on a custom configuration of your desktop or operating system when you create screenshots and you should use the visual defaults of the FreeCAD interface whenever possible.

To create a screenshots you can use the options provided by your operating system, or one of these macros: <img alt="" src=images/Snip.png  style="width:24px;"> _.

### Text

To ease documentation translations, try to avoid screenshots that contain texts. If you cannot avoid this, consider taking separate screenshots of the interface and the [3D view](3D_view.md). The image of the 3D view can be reused in every translation, while a translator can take a screenshot of the localized interface if necessary.

### Icons and graphics 

Refer to the [Artwork](Artwork.md) page for all artwork and icons that have been created for FreeCAD, and which can also be used in documentation pages. If you would like to contribute icons, please read the [Artwork Guidelines](Artwork_Guidelines.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Translations


<div class="mw-collapsible-content">

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

The FreeCAD wiki supports a translation extension that allows managing translations between pages easier; for details, see [Localisation Translating the wiki](Localisation#Translating_the_wiki.md).

Other useful resources are:

-   [ISO language codes](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) to identify the two-letter code for a particular language that you want to translate to.
-   [Google Translate](http://translate.google.com/) for help with translations.
-   [Deepl translator](https://www.deepl.com/translator) for help with translations.

## Some tips for translators 

### Translate GuiCommand 

    {{GuiCommand
    |Name=FEM EquationFluxsolver
    |MenuLocation=Solve → Equation fluxsolver
    |Workbenches=[FEM](Fem_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Translated:

    {{GuiCommand/fr
    |Name=FEM EquationFluxsolver
    |Name/fr=FEM EquationFluxsolver
    |MenuLocation=Solveur → Equation fluxsolver
    |Workbenches=[Atelier FEM](Fem_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutoriel](FEM_tutorial/fr.md)
    }}

### Translate navi 

    {{FEM_Tools_navi}}

Translated:

    {{FEM_Tools_navi/fr}}

### Translate link 

    [Part Module](Part_Module.md)

Translated:

    [Atelier Pièces](Part_Module/fr.md)

### Translate Docnav 

    

Translated:

    

Example with icons:

    

Translated:

    


</div>


</div>

## Create, rename and delete pages 

### Create pages 

Before creating a new page you should first check if a similar page already exists. If that is the case it is usually better to edit that existing page instead. When in doubt please open a topic in the [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21) first.

To create a new page do one of the following:

-   Visit the URL with the desired page name, for example: https://wiki.freecadweb.org/My_new_page, and click on \'create this page\'.
-   Do a wiki search for the page name, and click on the red text in \'Create the page \"My new page\" on this wiki!\'.

### Rename pages 

Since FreeCAD is a project under permanent development, it is sometimes necessary to revise the content of the wiki. If the names of commands are changed in the source code, the wiki pages documenting them have to be renamed as well. This can only be done by wiki administrators. To inform them, open a topic in the [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21) and list the necessary renaming operation in this form:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...

### Delete files and pages 

In case you need to delete a file, go to its page (https://www.freecadweb.org/wiki/File:***.***) and edit it. No matter if the page is blank or not, add this as the first element: {{Delete}} and directly below it describe why the page should be deleted. Additionally, open a topic in the [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21).

For pages the procedure is the same.

## Discussion

The [Development/Wiki subforum](http://forum.freecadweb.org/viewforum.php?f=21) in the [FreeCAD forum](https://forum.freecadweb.org) provides a dedicated space for discussing wiki topics, the wiki appearance and anything else related to the wiki. Direct your questions and suggestions there.

## Terminology - naming policy 

### English

See [Glossary](Glossary.md).

### Other languages 

-   [Italiano](Italian_Translation.md)
-   [Français](French_Translation.md)
-   [Deutsch](German_Translation.md)
-   [Polish](Polish_translation.md)

_ _ _ _

---
[documentation index](../README.md) > [Documentation](Category_Documentation.md) > WikiPages/en
