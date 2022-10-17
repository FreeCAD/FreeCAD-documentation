# WikiPages/es
{{TOCright}}

Esta página es una extensión de la página [Ayuda   *Edición](Help_Editing.md) y da pautas comunes para escribir y actualizar la documentación del wiki de FreeCAD. Resume varias discusiones y sesiones de brainstorming

## Antes de empezar 


<div class="mw-translate-fuzzy">

-   Esta documentación wiki está basada en [MediaWiki](https   *//www.mediawiki.org/wiki/MediaWiki), el mismo software que utiliza [Wikipedia](https   *//es.wikipedia.org/wiki/Main_Page). Si has contribuido a la Wikipedia, editar las páginas del wiki de FreeCAD debería ser fácil.
-   A diferencia de Wikipedia, el wiki de FreeCAD está protegido contra la escritura para evitar el spam. Debes solicitar una cuenta [en el foro](http   *//forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   Si nunca has usado el software wiki antes, por favor lee [Ayuda   *Edición](Help_Editing.md) para familiarizarte con el marcado que se usa.
-   Para el uso avanzado del software wiki, vea [Ayuda de MediaWiki   *Contenido](https   *//www.mediawiki.org/wiki/Help   *Contents). No todas las características de MediaWiki están disponibles en este wiki de FreeCAD, pero muchas sí.
-   Nos gusta mantener la documentación fácil de leer, así que evita usar características complejas. Mantén la sencillez.
-   Usa un sandbox para probar tu código, por ejemplo, [FreeCADDocu   *Sandbox](FreeCADDocu_Sandbox.md) o una página particular con tu nombre [Sandbox   *Yourname](Sandbox_Yourname.md).
-   Por favor, ten en cuenta las traducciones. El wiki de FreeCAD utiliza soporte de traducción automática para proporcionar páginas en muchos idiomas. Para cada página pueden existir múltiples versiones lingüísticas. En muchas páginas verás etiquetas como <translate>...</translate> y muchas etiquetas simples como . Estas últimas son creadas por el sistema de traducción. Vinculan los títulos y los párrafos a sus versiones traducidas. No debería cambiarlos, ya que eso destruiría esos enlaces. Sin embargo, puede mover los párrafos o cambiar la redacción siempre que las etiquetas permanezcan con ellos. Si elimina un epígrafe o un párrafo, debe eliminar también la etiqueta que le corresponde. Tenga en cuenta que los cambios en los títulos y párrafos existentes afectan a las traducciones actuales. Sus cambios deben valer la pena. No se preocupe cuando añada nuevo material porque el sistema añadirá nuevas etiquetas automáticamente después de sus ediciones. Para más información, consulte [Localización](Localisation/es.md) y la página original [Mediawiki   *Extensión   *Traducir](https   *//www.mediawiki.org/wiki/Help   *Extension   *Translate/Page_translation_example).


</div>

## Directrices generales 

### Descripciones concisas 

Cuando describas FreeCAD intenta ser conciso y directo y evita las repeticiones. Describe lo que FreeCAD *hace*, no lo que FreeCAD *no hace*. Evita también expresiones coloquiales como \"un par\". Utilice \"algunos\" cuando se trate de un número indeterminado, o especifique la cantidad correcta.

Mala descripción
   *   [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/de.md)   * el Ambiente de trabajo DiseñoPieza es un ambiente de trabajo para el diseño de piezas que pretende proporcionar herramientas para el modelado de piezas sólidas complejas.





Buena descripción
   *   [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/de.md)   * tiene como objetivo proporcionar herramientas para el modelado de piezas sólidas complejas.

### Información centralizada 

Evite duplicar la misma información en diferentes lugares. Inserte la información en una nueva página, y enlace a esta página desde otras páginas que requieran esta información.

No utilices la transclusión de páginas ([Ayuda   *Edición#Plantillas y páginas transcluidas](Help   *Editing#Templates_and_transcluding_pages.md)), ya que esto dificulta la traducción del wiki. Utiliza sólo las plantillas descritas en [#Plantillas](#Templates.md).

### Estilismo

Las plantillas se utilizan para dar estilo a las páginas de ayuda. Proporcionan a la documentación un aspecto consistente. Hay una plantilla para los comandos del menú, **Archivo → Guardar**, una plantilla para dar estilo a las teclas a pulsar, **Shift**, para mostrar un valor booleano, `True`, etc. Por favor, familiarícese con la sección [#Plantillas](#Templates.md) antes de escribir páginas de ayuda.

### Banderas temporales 

Si está trabajando en una página grande, es aconsejable marcar la página como trabajo en curso o como inacabada. Esto asegura que los administradores del wiki no marquen su página como lista para ser traducida mientras usted todavía la está cambiando.


<div class="mw-translate-fuzzy">

Para marcar una página, añada  o  como primera línea. Con  invitas a otros a unirse a ti para terminar la página, mientras que  indica que tú mismo harás el trabajo y que los demás deben darte algo de tiempo.


</div>

Una vez terminado el trabajo, no olvides retirar las banderas.

## Ejemplos

Para familiarizarse rápidamente con la estructura y el estilo del wiki de FreeCAD mira la página del modelo   * [Modelo de GuiCommando](GuiCommand_model/es.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Estructura


<div class="mw-collapsible-content">

El [El centro de usuarios](User_hub/es.md) proporciona un [Índice de contenidos](Online_Help_Toc/es.md). Esto se utiliza como referencia principal para construir automáticamente la ayuda offline que puedes alcanzar desde FreeCAD, así como la documentación offline en PDF.


<div class="mw-translate-fuzzy">

La [Template   *Docnav](Template_Docnav.md) se utiliza para enlazar secuencialmente las páginas, siguiendo la estructura del [Índice de contenidos](Online_Help_Toc/es.md). Ver [#Plantillas](#Plantillas.md) para una lista de todas las plantillas.


</div>

### Nombres de páginas 


<div class="mw-translate-fuzzy">

Los nombres de las páginas deben ser cortos, y deben utilizar las mayúsculas y minúsculas   * todas las palabras, excepto la primera y los nombres propios, deben ir en minúsculas. Este es el estilo [utilizado por Wikipedia](https   *//en.wikipedia.org/wiki/Wikipedia   *Manual_of_Style/Capital_letters#Headings,_headers,_and_captions) para sus artículos.


</div>


<div class="mw-translate-fuzzy">


Malo Nombre de página   *
   *   Construction Of AeroCompany Airplanes


</div>


<div class="mw-translate-fuzzy">


Buen nombre de página   *
   *   Construction of AeroCompany airplanes


</div>

Los nombres de las páginas de los ambientes de trabajo de nivel superior deben tener este formato XYZ Workbench, donde XYZ es el nombre del ambiente de trabajo, por ejemplo [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md). Y los nombres de las páginas que describen los comandos (o herramientas) pertenecientes a un banco de trabajo deben tener este formato XYZ Command, por ejemplo [DiseñoPieza Alcolchado](PartDesign_Pad/es.md). Ten en cuenta que debes utilizar el nombre del comando tal y como aparece en el código fuente.

### Rúbricas

Paragraph headings should be short and use sentence case   * all words except the first one and proper names, should be in lowercase. You should not use H1 headings (= Heading =) in your wiki markup since the page title is automatically added as the main H1 heading.

### Enlaces

You should use the original link name for links whenever possible. This clarifies the referenced page in printed or offline documentation. Please avoid non-meaningful words for the link.

Bad link
   *   For more information on drafting 2D objects click [here](Draft_Workbench.md).





Good link
   *   For more information on drafting 2D objects refer to the [Draft Workbench](Draft_Workbench.md).

The preferred format for a link is   *

[Name of Page](Name_of_Page.md)

Traducido   *

[Nom de la Page](Name_of_Page/fr.md)

Note that for the part before the | character, the actual link, case is relevant. If your page name is Name_of_page the link will fail if you type Name_of_Page (upper case P). Before the | character all spaces should be replaced by underscores (_). This is to assist translators using translation software, without the underscores the link would be translated by the software which is undesirable.

To link to a certain paragraph add a # sign and its headings to the page name. Example   *

[WikiPages](WikiPages#Links.md)

Traducido   *

[WikiPages](WikiPages/fr#Liens.md)

Within the same page you can omit the page name. Example   *

[Links](#Links.md)

To link to the top of the page you can use   *

</translate>{{Top}}<translate>

This template should automatically display the correct text depending on the language of the page. A link to the top of the page is especially useful for long pages as it allows the user to quickly jump back to the table of content. You can put it at the end of each paragraph. Make sure there is an empty line before and after the template.

Image link
   *   <img alt="Optional text that is shown when you hover the image\|link=Draft_Wire" src=images/Draft_Wire.svg  style="width   *24px;">

To use an image as a link   *

![](images/)

Image link + text link
   *   <img alt="" src=images/Draft_Wire.svg  style="width   *24px;"> [Draft Wire](Draft_Wire.md)

If you leave out the optional text the link itself will be shown when the image is hovered, which is preferable, and you should also add a text link after the image link   *

![](images/)_[Draft_Wire](Draft_Wire.md)

### Páginas del ambiente de trabajo 

A top level workbench page should start with   *

-   A description of what the workbench is used for.
-   An image to illustrate the description.

See [#Screen capture](#Screen_capture.md) for conventions on including images.

### Páginas de comandos 

Command pages describing workbench tools should not be too long, they should only explain what a command can do and what it can\'t, and how to use it. You should keep pictures and examples to a minimum. Tutorials can expand on how to use the tool and provide step-by-step details.

Please refer to the [GuiCommand model](GuiCommand_model.md) page for more details.

### Tutoriales

A well written tutorial should teach how to achieve certain practical results quickly. It shouldn\'t be too long, but should include sufficient step-by-step instructions and images to guide the user. As FreeCAD evolves, tutorials may become obsolete, so it is important to mention the FreeCAD version used in, or required for, a tutorial.

For examples visit the [Tutorials](Tutorials.md) page.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


<div class="mw-translate-fuzzy">

## Platillas


<div class="mw-collapsible-content">


</div>


<div class="mw-collapsible-content">

Styling of the FreeCAD wiki pages is achieved through the use of templates ([Help   *Editing#Templates_and_transcluding_pages](Help   *Editing#Templates_and_transcluding_pages.md)). They ensure a standardized look and feel across all pages, and also make it possible to re-style the wiki. You can see the complete list of defined templates by accessing [Special   *PrefixIndex/Template   *](Special   *PrefixIndex/Template   *.md). But please only use the templates listed in the tables below. Only in very special cases should you use HTML tags directly.

Click on the template link to see the usage instructions for a template, and to see its implementation. Templates are a powerful feature of the MediaWiki software. You should be an experienced wiki user if you wish to propose additions and modifications to existing templates. If implemented incorrectly, templates make it difficult to translate pages into other languages, so their use should be limited to text formatting, page transclusion should be avoided. See [MediaWiki Help   *Templates](https   *//www.mediawiki.org/wiki/Help   *Templates) to learn more.

### Plantillas sencillas 

These templates accept a simple text parameter, and format it with a particular style.

++++
| Template                                                                                                      | Appearance                             | Description                                                                                                                                                                                                                                                                                    |
+===============================================================================================================+========================================+================================================================================================================================================================================================================================================================================================+
| [Top](Template_Top.md)                                                                                |                         | Use it to add a link to the top of the page.                                                                                                                                                                                                                                                   |
|                                                                                                               | {{Top}}                                |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Emphasis](Template_Emphasis.md)                                                                      |                         | Use it to emphasize a piece of text.                                                                                                                                                                                                                                                           |
|                                                                                                               | **emphasis**                  |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [KEY](Template_KEY.md)                                                                                |                         | Use it to indicate a keyboard key that needs to be pressed.                                                                                                                                                                                                                                    |
|                                                                                                               | **Alt**                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [ASCII](Template_ASCII.md)                                                                            |                         | Use it to indicate a ascii key in a image (.svg) that needs to be pressed. You must give the character desired or the number of the code ascii of the character.                                                                                                                               |
|                                                                                                               | {{ASCII|A}}                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Button](Template_Button.md)                                                                          |                         | Use it to indicate a button in the graphical user interface that needs to be pressed.                                                                                                                                                                                                          |
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
| [FileName](Template_FileName.md)                                                                      |                         | Use it to indicate a name of a file or directory.                                                                                                                                                                                                                                              |
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
| [Incode](Template_Incode.md)                                                                          |                         | Use it to include in-line source code with a monospace font. It should fit in one line.                                                                                                                                                                                                        |
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
| [Obsolete](Template_Obsolete.md)                                                                      |                         | Use it to indicate that a feature became obsolete in the specified FreeCAD version.                                                                                                                                                                                                            |
|                                                                                                               | {{Obsolete|0.19}}                      |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++
| [Version](Template_Version.md)                                                                        |                         | Use it to indicate that a feature was introduces in the specified FreeCAD version.                                                                                                                                                                                                             |
|                                                                                                               | <small>(v0.18)</small>                        |                                                                                                                                                                                                                                                                                                |
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
| [ColoredParagraph](Template_ColoredParagraph.md)                                                      |                         | Use this template to color the background, text, or background and text of an entire paragraph. [ColoredParagraph](Template_ColoredParagraph.md) page for more examples)                                                                                                               |
|                                                                                                               | {{ColoredParagraph|Colored Paragraph}} |                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                |
++++

### Plantillas complejas 

These templates require more input parameters, or produce a block of text with a particular format.

++++
| Template                                                                                         | Appearance                                                                                                                   | Description                                                                                                                                                                                                                                                                                                               |
+==================================================================================================+==============================================================================================================================+===========================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template_Prettytable.md)                                                   | This table                                                                                                                   | Use it to format tables such as this one. Additional table properties can be added.                                                                                                                                                                                                                                       |
++++
| [Caption](Template_Caption.md)                                                           |                                                                                                                    | Use it to add an explanation below an image. It can be left aligned or center aligned.                                                                                                                                                                                                                                    |
|                                                                                                  | <div style="width   *400px;">                                                                                                   |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                               |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  | 
*Some caption for an image*                                                                                        |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                    |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  | </div>                                                                                                                       |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [Clear](Template_Clear.md)                                                               |                                                                                                                              | Use it to clear columns. Follow the definition of the template for a detailed explanation. It is often used to stop text from flowing next to unrelated images.                                                                                                                                                           |
++++
| [Code](Template_Code.md)                                                                 |                                                                                                               | Use it to include multi-line code examples with a monospace font. The default language is Python, but other languages can be specified.                                                                                                                                                                                   |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                                 |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           | [Python](Python.md) code should adhere to the general recommendations established by [PEP8   * Style Guide for Python Code](https   *//www.python.org/dev/peps/pep-0008/). In particular, parentheses should immediately follow the function name, and a space should follow a comma. This makes the code more readable |
++++
| [Fake heading](Template_Fake_heading.md)                                                 |                                                                                                               | Use it to create a heading that will not be automatically included in the table of contents.                                                                                                                                                                                                                              |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                   |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [GuiCommand](Template_GuiCommand.md)                                                     | See [GuiCommand model](GuiCommand_model.md)                                                                          | Use it to create a box with useful information to document workbench commands (tools).                                                                                                                                                                                                                                    |
++++
| [TutorialInfo](Template_TutorialInfo.md)                                                 | See for example [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                | Use it to create a box with useful information to document [tutorials](Tutorials.md).                                                                                                                                                                                                                             |
++++
| [Macro](Template_Macro.md)                                                               | See for example [Macro FlattenWire](Macro_FlattenWire.md)                                                            | Use it to create a box with useful information to document [macros](macros.md).                                                                                                                                                                                                                                   |
++++
| [Docnav](Template_Docnav.md)                                                             |                                                                                                               | Use it to create a bar with the words \'next\', \'previous\', and \'index\', and the appropriate links, which is useful for putting pages in a particular sequence.                                                                                                                                                       |
|                                                                                                  |                                                                                 |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [VeryImportantMessage](Template_VeryImportantMessage.md)                                 |                                                                                                               | Use it to create a highlighted box with a very important message. Use sparingly, only to indicate major problems in the functionality of the software, discontinuation of tools, and similar.                                                                                                                             |
|                                                                                                  | **Important Message**                                                                                   |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [Page in progress](Template_Page_in_progress.md)                                         |                                                                                                               | Use this for pages that are still in progress or that are currently being reworked. Don\'t forget to remove this when the page is ready.                                                                                                                                                                                  |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                        |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [UnfinishedDocu](Template_UnfinishedDocu.md)                                             |                                                                                                               | Use it to create a highlighted box indicating an unfinished documentation page.                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [Softredirect](Template_Softredirect.md)                                                 |                                                                                                                              | Use it instead of the normal redirect, when you are redirecting to a special page (such as Media   * or Category   *), in which cases the normal redirect is disabled.                                                                                                                                                          |
++++
| [Quote](Template_Quote.md)                                                               |                                                                                                               | Use it to create a box of text with a literal quote and reference.                                                                                                                                                                                                                                                        |
|                                                                                                  | {{Quote|text=Cry "Havoc" and let slip the dogs of war.|sign=William Shakespeare|source=''Julius Caesar'', act III, scene I}} |                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                           |
++++
| [Userdocnavi](Template_Userdocnavi.md), [Powerdocnavi](Template_Powerdocnavi.md) |                                                                                                                              | Use them to create navigation boxes for the user documentation, the power user documentation, and the developer documentation. This allows quickly jumping between different sections of the documentation. They also place the corresponding page in the proper category.                                                |
++++


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


<div class="mw-translate-fuzzy">

## Gráficos


<div class="mw-collapsible-content">


</div>


<div class="mw-collapsible-content">

Images and screenshots are necessary to produce a complete documentation of FreeCAD. They are particularly useful to illustrate examples and tutorials. Images should be shown in their original size, so they present sufficient detail and are readable if they include text. [Bitmap](bitmap.md) images should not be resized.

Avoid animated pictures (GIF) in the general help pages. Animations and videos should be reserved for tutorials not intended to be used as offline PDF documentation.

Images can be uploaded through the [Special   *Upload](Special_Upload.md) page.

### Nombre

Give meaningful names to your images. If you have an image that showcases the characteristics of a particular command, you should use the name of that command with `_example` at the end. For example for the command [Draft Offset](Draft_Offset.md) the image should be called `Draft_Offset_example.png`.

### Captura de pantalla 

Recommended sizes for screen captures are   *

-   Native 400x200 (or width=400 and height\<=200), for [command reference](GuiCommand_model.md) pages, to allow the picture to fit in the left part of the page, and for other standard snapshots.
-   Native 600x400 (or width=600 and height\<=400), for [command reference](GuiCommand_model.md) pages, when you really need a bigger picture, and still allow the picture to fit in the left part of the page, and for other standard snapshots.
-   Native 1024x768 (or width=1024 and height\<=768), only for full screen images.
-   Smaller sizes are possible when showing details.
-   Avoid images with larger resolutions, as they won\'t be very portable to other kinds of displays or the printed PDF documentation.

You shouldn\'t depend on a custom configuration of your desktop or operating system when you create screenshots and you should use the visual defaults of the FreeCAD interface whenever possible.

To create a screenshots you can use the options provided by your operating system, or one of these macros   * <img alt="" src=images/Snip.png  style="width   *24px;"> [Macro Snip](Macro_Snip.md) and <img alt="" src=images/Macro_Screen_Wiki.png  style="width   *24px;"> [Macro Screen Wiki](Macro_Screen_Wiki.md).

### Texto

To ease documentation translations, try to avoid screenshots that contain texts. If you cannot avoid this, consider taking separate screenshots of the interface and the [3D view](3D_view.md). The image of the 3D view can be reused in every translation, while a translator can take a screenshot of the localized interface if necessary.

### Iconos y gráficos 

Refer to the [Artwork](Artwork.md) page for all artwork and icons that have been created for FreeCAD, and which can also be used in documentation pages. If you would like to contribute icons, please read the [Artwork Guidelines](Artwork_Guidelines.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


<div class="mw-translate-fuzzy">

## Traducciones


<div class="mw-collapsible-content">

Según el consenso general, la página de referencia en la wiki es la página inglesa, que debería crearse primero. Si quieres cambiar o añadir contenido a una página, debes hacerlo primero en la página inglesa, y sólo una vez completada la actualización, portar la modificación a la página traducida.


</div>


<div class="mw-collapsible-content">

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

The FreeCAD wiki supports a translation extension that allows managing translations between pages easier; for details, see [Localisation Translating the wiki](Localisation#Translating_the_wiki.md).

Other useful resources are   *

-   [ISO language codes](http   *//en.wikipedia.org/wiki/List_of_ISO_639-1_codes) to identify the two-letter code for a particular language that you want to translate to.
-   [Google Translate](http   *//translate.google.com/) for help with translations.
-   [Deepl translator](https   *//www.deepl.com/translator) for help with translations.

## Algunos consejos para los traductores 

### Traducir GuiCommando 

    {{GuiCommand
    |Name=FEM EquationFlux
    |MenuLocation=Solve → Flux equation
    |Workbenches=[FEM](FEM_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Translated   *

    {{GuiCommand/fr
    |Name=FEM EquationFlux
    |Name/fr=FEM Équation d'écoulement
    |MenuLocation=Solveur → Équation de flux
    |Workbenches=[Atelier FEM](FEM_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM Tutoriel](FEM_tutorial/fr.md)
    }}

### Traducir navi 

    {{FEM_Tools_navi}}

Translated   *

    {{FEM_Tools_navi/fr}}

### Traducir enlace 

    [Part Module](Part_Module.md)

Translated   *

    [Atelier Part](Part_Module/fr.md)

### Traducir Docnav 

    

Translated   *

    

Example with icons   *

    

Translated   *

    


</div>


</div>


<div class="mw-translate-fuzzy">

## Renombrar y borrar 


</div>

### Create pages 

Before creating a new page you should first check if a similar page already exists. If that is the case it is usually better to edit that existing page instead. When in doubt please open a topic in the [Wiki forum](https   *//forum.freecadweb.org/viewforum.php?f=21) first.

To create a new page do one of the following   *

-   Visit the URL with the desired page name, for example   * https   *//wiki.freecadweb.org/My_New_Page, and click on \'create this page\'.
-   Do a wiki search for the page name, and click on the red text in \'Create the page \"My New Page\" on this wiki!\'.

### Cambiar el nombre de las páginas 

Since FreeCAD is a project under permanent development, it is sometimes necessary to revise the content of the wiki. If the names of commands are changed in the source code, the wiki pages documenting them have to be renamed as well. This can only be done by wiki administrators. To inform them, open a topic in the [Wiki forum](https   *//forum.freecadweb.org/viewforum.php?f=21) and list the necessary renaming operation in this form   *

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...

### Eliminar archivos y páginas 

In case you need to delete a file, go to its page (https   *//www.freecadweb.org/wiki/File   ****.***) and edit it. No matter if the page is blank or not, add this as the first element   * {{Delete}} and directly below it describe why the page should be deleted. Additionally, open a topic in the [Wiki forum](https   *//forum.freecadweb.org/viewforum.php?f=21).

For pages the procedure is the same.

## Debate

The [Development/Wiki subforum](http   *//forum.freecadweb.org/viewforum.php?f=21) in the [FreeCAD forum](https   *//forum.freecadweb.org) provides a dedicated space for discussing wiki topics, the wiki appearance and anything else related to the wiki. Direct your questions and suggestions there.

## Terminología - política de nomenclatura 

### Inglés

See [Glossary](Glossary.md).

### Otros idiomas 

-   [Italiano](Italian_Translation.md)
-   [Français](French_Translation.md)
-   [Deutsch](German_Translation.md)
-   [Polish](Polish_Translation.md)

[Category   *Documentation](Category_Documentation.md) [Category   *Wiki](Category_Wiki.md) [Category   *Wiki Documentation](Category_Wiki_Documentation.md) [Category   *Administration](Category_Administration.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Documentation](Category_Documentation.md) > [Wiki](Category_Wiki.md) > [Wiki Documentation](Category_Wiki Documentation.md) > [Administration](Category_Administration.md) > WikiPages/es
