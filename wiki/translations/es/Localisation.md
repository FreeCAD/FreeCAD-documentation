# Localisation/es
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Vista general 

\"Localización\" es en general el proceso de proveer un software con una interfaz de usuario con múltiples lenguajes. En FreeCAD puedes cambiar el lenguaje de la interfaz en **Editar→Preferencias→General**. FreeCAD usa [Qt](wikipedia:Qt_(toolkit).md) para facilitar el soporte de múltiples lenguajes. En Unix/Linux, FreeCAD utiliza la configuración local actual de tu sistema como predeterminado.

## Ayudando a traducir FreeCAD 


<div class="mw-translate-fuzzy">

Una de las cosas más importantes que los usuarios pueden contribuir a FreeCAD (si por ejemplo no tienen conocimientos de programación) es ayudar a traducir sus diferentes aspectos (código fuente, wiki, sitio web, documentación, etc\...) a otro idioma. Aquí están las formas de hacerlo


</div>

## Traducir el código fuente de FreeCAD 

FreeCAD utiliza un sistema de traducción colaborativa en línea de terceros llamado [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

Se trata de un software propietario, pero gratuito para los proyectos FOSS. A continuación encontrará instrucciones sobre cómo utilizarlo:

-   Ir a la [FreeCAD página del proyecto de traducción en Crowdin](http://crowdin.net/project/freecad)
-   Iniciar sesión creando un nuevo perfil, o utilizando una cuenta de terceros (GitHub, GitLab, GMail, etc\...)
-   Haga clic en el idioma que desea traducir
-   Comienza a traducir haciendo clic en el botón **Traducir** junto a uno de los archivos. Por ejemplo, {{FileName|FreeCAD.ts}} contiene las cadenas de texto para la interfaz gráfica principal de FreeCAD.
-   Puedes votar por las traducciones existentes, o puedes crear las tuyas propias.

{{Message|Si estás participando activamente en la traducción de FreeCAD y quieres estar informado antes de que la próxima versión esté lista para ser lanzada, para que haya tiempo de revisar tu traducción, por favor suscríbete a uno de los equipos de traducción de Crowdin FreeCAD.}}


**Nota:**

Los detalles sobre cómo utilizar crowdin se pueden encontrar en la página [Administración de Crowdin](Crowdin_Administration/es.md).

## Traduciendo ambientes de trabajo externos 

Visite [Traducir un ambiente de trabajo externos](Translating_an_external_workbench/es.md).

## FreeCAD Preferences for Translators 

Starting with FreeCAD 0.20, the following variables can be manually added to the BaseApp/Preferences/General section of the user.cfg file to assist with the development of new translations:

**AdditionalLanguageDomainEntries** - to add entirely new languages to FreeCAD that are not currently supported by the source code, you can use this user preference to add to the list of available languages. The format of the languages is \"Language Name\"=\"code\"; for example:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - add an additional directory for FreeCAD to search for \*.qm files. This location will take precedence over \$userAppDataDir/translations and \$resourceDir/translations. For example:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>

## Traducir la wiki de FreeCAD 

Este wiki alberga muchos contenidos, la mayoría de los cuales conforman el manual. Puedes navegar por la documentación a partir de la [Página principal](Main_Page/es.md), o echar un vistazo al manual de usuario [Ayuda en línea Índice de contenidos](Online_Help_Toc/es.md).

Para traducir el wiki, debes tener permisos de edición del wiki; consulta [¿Cómo puedo obtener permiso de edición en el wiki?](Frequently_asked_questions/es#¿Cómo_puedo_obtener_permiso_de_edición_en_el_wiki?.md).

También deberías tener suficientes conocimientos de marcado wiki y seguir las directrices generales de estilo descritas en [PáginasWiki](WikiPages/es.md).

### Extensión de traducción de Mediawiki 

Cuando el wiki se alejó de SourceForge, [Yorik](User_Yorik.md) instaló [MediaWiki\'s Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate) que facilita la traducción de las páginas. Las ventajas de la extensión de traducción son que el título de la página puede ser traducido, mantiene un registro de las traducciones, notifica si la página original ha sido actualizada, y mantiene las traducciones sincronizadas con la página original en inglés.

La herramienta está documentada en [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate), y forma parte de [MediaWiki Language Extension Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Para empezar rápidamente a preparar una página para su traducción, lea el [Ejemplo de traducción de una página](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). Esencialmente, un par de

    &lt;translate&gt; ... &lt;/translate&gt;

tags rodear toda la página para activar el sistema de traducción, y la página debe estar marcada para ser traducida.


<div class="mw-translate-fuzzy">

Para ver un ejemplo de cómo funciona la herramienta de traducción, visite la [Página principal](Main_Page/es.md). Verá una barra de idiomas generada automáticamente en la parte superior. Haga clic en [Hauptseite](Main_Page/de.md) (alemán), le llevará a [Main Page/de](Main_Page/de.md). Justo debajo del título, puedes leer , siendo XX el porcentaje actual de traducción. Haga clic en \"Traducir\" en la parte superior de la página para iniciar la utilidad de traducción para actualizar, corregir y revisar la traducción existente.


</div>

Si va a [Main Page](Main_Page.md), notará que ya no puede editar la página directamente haciendo clic en las etiquetas \[Edit\], y el enlace superior \"Editar\" ha sido sustituido por el enlace \"Traducir\" que abre la utilidad de traducción.

Cuando se añade un nuevo contenido, la página en inglés debe crearse primero y luego traducirse a otro idioma. Si alguien quiere cambiar o añadir contenido en una página, la página en inglés debe ser modificada primero.

Si no estás seguro de cómo proceder con las traducciones, no dudes en pedir ayuda en el [Desarrollo → subforo Wiki](https://forum.freecadweb.org/viewforum.php?f=21) o en el [subforo de idiomas específicos](https://forum.freecadweb.org/viewforum.php?f=11) en el [foro de FreeCAD](http://forum.freecadweb.org).

### Notas importantes 


<div class="mw-translate-fuzzy">

Todos los usuarios de la wiki que tengan permisos de \"Editor\" pueden lanzar la utilidad de traducción y escribir, guardar y revisar las traducciones.


</div>

Sin embargo, sólo los usuarios con permisos de \"Administrador\" pueden marcar las páginas para su traducción. Una página que no esté marcada para ser traducida no hará uso de la extensión de traducción y no se sincronizará correctamente con la información en inglés.

La barra lateral izquierda también es traducible, pero sólo los administradores pueden modificar este elemento del sitio. Por favor, siga las instrucciones dedicadas en [Barra lateral de localización](Localisation_Sidebar/es.md).

La primera vez que se cambia una página al nuevo sistema de traducción, se pierden todas sus antiguas traducciones \"manuales\". Para recuperar una traducción, debes guardar una copia offline del texto antiguo antes del cambio. Entonces podrás utilizar este texto antiguo traducido para rellenar las unidades de traducción en el nuevo sistema. También puedes abrir una versión anterior desde el historial, y obtener el texto antiguo de esta manera. Esto tiene que hacerse para cada idioma que tenía una página traducida.

### Traducir la documentación de FreeCAD 

Según el consenso general, la página de referencia en la wiki es la página en inglés, que debería crearse primero. Si quieres cambiar o añadir contenido a una página, debes hacerlo primero en la página en inglés, y sólo una vez completada la actualización, portar la modificación a la página traducida.

### Instrucciones de traducción antiguas 

++
| Estas instrucciones son sólo para el fondo histórico. Las traducciones deben utilizar el nuevo sistema con la [\#Extensión de traducción de Mediawiki](#Extensión_de_traducción_de_Mediawiki.md) descrita anteriormente.                                                                                                                                                                                                                                                                                                                                                                                         |
++
| Así que el primer paso es **comprobar si ya se ha iniciado la traducción manual para tu idioma** (mira en la barra lateral izquierda, en \"manual\").                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Si no es así, dirígete al \[foro <http://forum.freecadweb.org/>\] y di que quieres empezar una nueva traducción, crearemos la configuración básica para el idioma en el que quieres trabajar.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| A continuación, debes [obtener permiso de edición en la wiki](Frequently_asked_questions#Cómo_puedo_obtener_permiso_de_edición_en_la_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Si tu idioma ya está en la lista, mira qué páginas aún no tienen traducción (aparecerán en rojo). La técnica es sencilla: **entra en una página roja, y copia/pega el contenido de la página inglesa correspondiente, y empieza a traducir**.                                                                                                                                                                                                                                                                                                                                                                            |
| No olvides incluir todas las etiquetas y plantillas de la página original en inglés. Algunas de esas plantillas tendrán un equivalente en tu idioma (por ejemplo, hay una plantilla Docnav francesa llamada Docnav/fr). En casi todos los enlaces debes usar **una barra y el código de tu idioma**. Mira otras páginas ya traducidas para ver cómo lo hicieron.                                                                                                                                                                                                                                                         |
| Añade una barra y el código de tu idioma en las categorías, como \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Y si no estás seguro, dirígete a los foros y pide a la gente que compruebe lo que has hecho y te diga si está bien o no.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Hay cuatro plantillas que se utilizan habitualmente en las páginas de manual. Estas 4 plantillas tienen versiones localizadas (Template:Docnav/fr, Template:fr, etc\...)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   [Template:GuiCommand](Template_GuiCommand.md) : es el bloque de información del comando Gui en la parte superior derecha de la documentación del comando.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -   [Template:Docnav](Template_Docnav.md) : es la barra de navegación en la parte inferior de las páginas, mostrando las páginas anteriores y siguientes.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -   [Template:Userdocnavi](Template_Userdocnavi.md) : da enlaces directos a las principales páginas base                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \'\'\' Convención de nomenclatura de páginas \'\'\'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Por favor, ten en cuenta que, debido a las limitaciones en la implementación de Sourceforge del motor MediaWiki, requerimos que todas tus páginas mantengan el nombre de su contraparte original en inglés, añadiendo una barra y el código de tu idioma. Por ejemplo, la página traducida de About FreeCAD debe ser About Freecad/es para el español, About FreeCAD/pl para el polaco, etc. La razón es simple: para que si los traductores se van, los administradores del wiki, que no hablan todos los idiomas, sepan para qué son estas páginas. Esto facilitará el mantenimiento y evitará que se pierdan páginas. |
| Si quieres que la plantilla Docnav muestre páginas enlazadas en tu idioma, puedes usar **páginas de redirección**. Son básicamente enlaces de acceso directo a la página real. Aquí hay un ejemplo con la página francesa de Acerca de FreeCAD.                                                                                                                                                                                                                                                                                                                                                                          |
| \* La página Acerca de FreeCAD/fr es la página con contenido                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   La página À propos de FreeCAD contiene este código:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   En la página À propos de FreeCAD/fr, el código Docnav tendrá el siguiente aspecto:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| La página \"Bienvenue dans l\'aide en ligne de FreeCAD\" redirige a Online\_Help\_Startpage/fr, y la página \"Fonctionnalités\" redirige a Feature\_list/fr.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
++

## Traducir el sitio web de FreeCAD 

La traducción de la FreeCAD página web se realiza ahora a través de [Crowdin](https://crowdin.com/translate/freecad/561/en-en). El archivo se llama {{FileName|homepage.po}}.

## Desarrollo - Cómo añadir la localización 

Esta sección es para los desarrolladores que quieren añadir localización a su código.

### Preparando tus módulos de FreeCAD/master para la traducción 

Estas son las partes del proceso de traducción de FreeCAD:

-   extraer las cadenas de texto del código fuente en archivos \*.ts
-   cargar los archivos \*.ts en [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   traducción de cadenas dentro de Crowdin
-   extraer archivos \*.ts modificados/nuevos de Crowdin
-   convertir archivos \*.ts en archivos \*.qm y actualizar el archivo \*.qrc de cada módulo
-   actualizar el maestro de FreeCAD

Todos los pasos anteriores son realizados por los \"scripts de traducción\" que son ejecutados por un administrador periódicamente.

Preparar su módulo para la traducción es bastante fácil. En primer lugar, debe asegurarse de que tiene un directorio \"translations\" en {{FileName|myModule/Gui/Resources}}. A continuación, abra una ventana de terminal (o su equivalente en Windows/OSX) en su directorio \"translations\" e introduzca el siguiente comando: 
```pythonlupdate -ts myModule.ts```

Esto crea un archivo de traducción vacío. Una vez hecho esto, hay que asegurarse de que los scripts de traducción se actualizan como en este [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

Todo lo que sigue es automático en lo que respecta a un desarrollador. El administrador extraerá las cadenas de texto, los traductores las traducirán, luego el administrador extraerá las traducciones y actualizará FreeCAD/master.

### Preparar su módulo o macro de terceros para la traducción 

Los módulos o macros de terceros se traducen prácticamente de la misma manera, con la diferencia de que debes hacer parte del trabajo tú mismo. Este [discusión del foro](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) describe los detalles.

Actualización: ver [Traducir un banco de trabajo externo](Translating_an_external_workbench/es.md)

### Técnicas de traducción de módulos más antiguas 

[Localización Métodos antiguos](Localization_Older_Methods/es.md) describe el uso de herramientas de traducción como Qt Linguist, lupdate, lrelease, pylupdate4, etc en detalle. La mayor parte de esto ya no es necesario para los módulos de FreeCAD/master, pero puede ser útil para preparar y actualizar módulos de terceros.

## Automatización de las actualizaciones de las traducciones de Crowdin 

Actualmente los mantenedores de FreeCAD utilizan la API de Crowdin a través de [Crowdin Guiones](Crowdin_Scripts/es.md) para extraer y enviar las traducciones a Crowdin y de vuelta al repositorio de Github. La API de Crowdin ofrece a los mantenedores de FreeCAD la posibilidad de automatizar aspectos del flujo de trabajo de traducción del proyecto, para más información consulta la [Documentación de la API de Crowdin](https://support.crowdin.com/api/api-integration-setup/).

## Páginas relacionadas 

-   [Administración de Crowdin](Crowdin_Administration/es.md)
-   [Scripts de Crowdin](Crowdin_Scripts/es.md)

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/es
