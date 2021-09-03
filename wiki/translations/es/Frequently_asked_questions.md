




Esta página intenta responder a las preguntas más comunes que se hacen en los foros de FreeCAD. Si tienes un problema o una pregunta sobre FreeCAD, comprueba primero lo que se indica a continuación. Entonces, si no puedes encontrar una respuesta para tu pregunta específica, dirígete al [foro de FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3).

## Instalación

### ¿Cuál es la forma más fácil de instalar FreeCAD en mi sistema? 


<div class="mw-translate-fuzzy">

Si estás en Windows o Mac OS, la forma más sencilla es ir a la página [Descargar](Download/es.md), donde encontrarás varios paquetes listos para instalar. Si estás en Debian, Fedora o Ubuntu y algunas otras distribuciones, FreeCAD ya está incluido en los repositorios de software estándar y puedes simplemente instalarlo con el gestor de software. En Ubuntu, el equipo de FreeCAD también mantiene sus propios repositorios [PPA](Installing_on_Linux/es#PPA_estable.md). Para más detalles sobre la instalación, consulta la página de instalación de tu sistema operativo ([Windows](Installing_on_Windows/es.md), [Linux](Installing_on_Linux/es.md) o [Mac](Installing_on_Mac/es.md)).


</div>

### ¿Cuáles son los requisitos previos para ejecutar FreeCAD? 

A diferencia de la mayoría de los programas de CAD en 3D, FreeCAD puede funcionar sin problemas en los ordenadores más modestos: se sabe que funciona en CPUs Pentium IV e Intel Core2 Solo. Si tu ordenador ejecuta un sistema operativo actual, lo más probable es que FreeCAD funcione. El único prerrequisito es que tu tarjeta gráfica o chipset debe soportar [OpenGL](https://en.wikipedia.org/wiki/OpenGL), preferiblemente no más antigua que la v2.0. En caso de problemas, consulta la sección [Solución de problemas](Frequently_asked_questions/es#Solución_de_problemas.md) de este FAQ.

#### Multithreading

El núcleo de modelado geométrico subyacente de FreeCAD, la biblioteca de terceros [Tecnología OpenCASCADE](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT), [sólo tiene soporte parcial de multihilo en este momento](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). Mira la página [multithreading](multithreading/es.md) para más detalles.

#### Para los usuarios Mac 

Sólo se admite la arquitectura MacIntel. No hay versiones disponibles para la arquitectura PowerPC.

### ¿Qué pasa si quiero compilar FreeCAD yo mismo? 


<div class="mw-translate-fuzzy">

El código fuente de FreeCAD está siempre disponible en el repositorio de código fuente del proyecto. Compilar FreeCAD por ti mismo te permite utilizar las características más recientes que se están desarrollando, pero requiere un poco de conocimiento informático, aunque el procedimiento es bastante sencillo. El acceso al código fuente se explica [aquí](Compile_on_Linux/es#Obtener_la_fuente.md), y tenemos instrucciones detalladas para compilar en [Windows](Compile_on_Windows/es.md), [Linux](Compile_on_Linux/Unix/es.md) y [MacOS](Compile_on_MacOS/es.md).


</div>

### FreeCAD me dice que falta algún módulo o aplicación 

FreeCAD depende de muchas cosas para ofrecer toda su funcionalidad. Todos los principales componentes necesarios están normalmente incluidos en tu instalación de FreeCAD o proporcionados por tu gestor de paquetes, así que normalmente no tienes nada de qué preocuparte. Sin embargo, si has instalado FreeCAD desde fuentes no oficiales, o has compilado FreeCAD tú mismo, puede faltar alguna pieza, que no es crítica para FreeCAD en sí mismo, pero puede causar que alguna funcionalidad no esté disponible. Algunos formatos de archivo específicos como Collada o DWG también requieren componentes adicionales, que no pueden ser incluidos en FreeCAD, y deben ser instalados por ti mismo por separado.

Todos esos componentes y la forma adecuada de instalarlos están listados en la página [Módulos extra python](Extra_python_modules/es.md).

## Solución de problemas 

### FreeCAD no se inicia en absoluto 

Puede haber muchas razones para ello, la más probable es que falte alguna biblioteca. Intenta iniciar FreeCAD desde un terminal (escribe {{SystemInput|freecad}} en el prompt del terminal, {{SystemInput|FreeCAD}} en algunos sistemas) para ver si aparece algún mensaje de error. Además, lee el resto de este FAQ ya que puede darte más pistas para detectar la causa del problema. Si nada ayuda, cuéntalo en el \[foro <http://forum.freecadweb.org/>\], seguro que habrá alguien que pueda ayudarte.

En algunos sistemas Windows XP más antiguos puede aparecer un mensaje de error como el siguiente **La aplicación no puede iniciarse, porque la configuración de lado a lado es incorrecta. La reinstalación de la aplicación puede resolver el problema.** La razón de este problema es que en tu sistema o bien faltan las librerías de ejecución de CRT o la versión instalada es demasiado antigua porque FreeCAD fue enlazado con una versión más reciente. En este caso tienes que instalar el **Microsoft Visual C++ Redistributable Package** que encontrarás en Microsoft. Ver también el correspondiente [mensaje del foro](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).

### FreeCAD se inicia normalmente, pero no se muestran todos los iconos, algunos de ellos son reemplazados por una \'X\' negra 

Algunas partes de FreeCAD dependen de un módulo externo de Python llamado Pivy. En Windows, pivy está incluido en la instalación de FreeCAD. En sistemas Debian/Ubuntu, el paquete python-pivy es parte de los repositorios de software estándar. En otros sistemas, por el momento, puede que tengas que compilar pivy tú mismo. Ten en cuenta que aunque algunas herramientas no están disponibles sin pivy, el resto de FreeCAD funciona normalmente.

### Tengo problemas de visualización, la vista 3D no se comporta correctamente, hay basura cuando muevo/roto la vista, etc. 

FreeCAD depende de OpenGL para mostrar contenidos 3D, y por lo tanto requiere un entorno OpenGL que funcione. En algunos sistemas, OpenGL no está activado por defecto, y puede que necesites instalar o actualizar tus drivers gráficos. Este problema ocurre con mayor frecuencia en sistemas Linux o en sistemas virtuales. Si estás en un sistema basado en Linux, intenta los siguientes pasos:

-   verifique que su ordenador tiene una tarjeta gráfica con capacidad 3D
-   Escriba {{SystemInput|glxinfo}} en una ventana de terminal, y compruebe en la salida que Direct Rendering está configurado como \"sí\", y que el proveedor/renderizador/versión de OpenGL coincide con su tarjeta gráfica.
-   Instala otro software basado en OpenGL ([Blender](http://www.blender.org), por ejemplo) y comprueba si se ejecuta y muestra correctamente.

### FreeCAD se bloquea al iniciar 

Un fallo puede indicar un error más grave o algún problema en la configuración. La mayoría de los fallos de arranque se producen por una de las dos razones siguientes:

#### Los controladores OpenGL no están instalados, o no funcionan correctamente 

Esta es una causa muy común del problema. Los síntomas son simplemente que FreeCAD se bloquea al inicio, o cada vez que abres una vista 3D (por ejemplo creando un nuevo documento). Intenta averiguar cuál es tu chip gráfico, luego averigua si soporta [OpenGL](https://en.wikipedia.org/wiki/OpenGL) (la mayoría de los chips recientes lo hacen), luego encuentra el controlador correcto e instálalo. Una buena forma de comprobar si OpenGL está disponible es intentar ejecutar otra aplicación OpenGL como [blender](http://www.blender.org).


<div class="mw-translate-fuzzy">

Y como consejo general para obtener más información sobre los fallos con FreeCAD puedes iniciarlo con el parámetro del programa {{SystemInput|--write-log}}. Esto creará el archivo {{FileName|FreeCAD.log}} en {{FileName|$HOME/.FreeCAD}} en Linux y Mac OS X o {{FileName|%APPDATA%/FreeCAD}} en sistemas Windows.


</div>

En algunos casos raros puede tener instalado un controlador gráfico que no se ajusta a su tarjeta gráfica. Tuvimos un caso en el que el portátil del usuario tenía una gráfica Intel a bordo pero tenía instalados unos drivers ATI. [1](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042) Después de eliminar los archivos y volver a instalar el controlador correcto FreeCAD empezó a funcionar.

#### Alguna biblioteca, necesaria para FreeCAD, no está presente en su sistema, o no fue encontrada por FreeCAD 

Puede haber dos caminos para este problema: o simplemente falta alguna librería, por lo que FreeCAD se negará a iniciarse, o la librería está ahí, pero es una versión más antigua que la que FreeCAD espera, por lo que se producirá un fallo cuando FreeCAD intente usar una característica que falta de esa librería. Un ejemplo común es cuando tienes Qt3 y Qt4 instalado en tu sistema, FreeCAD podría detectar Qt4 pero si tu instalación de Qt no está configurada correctamente, algunas piezas de Qt3 podrían seguir siendo utilizadas, provocando fallos.

Por favor, revise el procedimiento de instalación ([Windows](Installing_on_Windows/es.md), [Linux](Installing_on_Linux/es.md) o [Mac](Installing_on_Mac/es.md)), asegúrese de que ha instalado todas las librerías necesarias (en la mayoría de los sistemas linux esto se hace automáticamente), y compruebe cuál es el número de versión mínimo para cada uno de los componentes.

Si todo parece correcto, describe el problema en el [foro](http://forum.freecadweb.org/) o en [enviar un error](Tracker/es.md). Si estás en un sistema linux, es fácil hacer un backtrace de depuración, que proporciona información muy útil sobre el fallo a los desarrolladores:

-   en un terminal, escriba {{SystemInput|gdb freecad}} (asumiendo que el paquete gdb está instalado)
-   dentro de gdb, escriba {{SystemInput|run}}
-   Después de la caída, escriba {{SystemInput|bt}} para obtener el seguimiento, que puede incluir en su informe de error.

### FreeCAD se congela tras el arranque 

Al iniciar FreeCAD la GUI aparece casi inmediatamente pero la GUI está congelada y la cpu está al 99%. Esto puede ocurrir en el escritorio KDE cuando se utiliza el tema Oxígeno. Es un error del tema Oxígeno y elegir otro tema debería solucionar este problema.

### FreeCAD se bloquea al crear un nuevo documento o abrir un archivo 

If FreeCAD crashes when it creates a new 3D view, try launching FreeCAD from a terminal. If a message error appears when the crash occurs, mentioning {{SystemOutput|Assertion Failed}}, and a component name beginning with \"So\" ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, etc.), the chances are very high, especially if you are on Linux, that FreeCAD is trying to use two different versions of the Coin library, which causes the crash. To verify if that is indeed the problem, try the following:

-   Locate the FreeCAD executable (usually in {{FileName|/usr/lib/FreeCAD/bin}})
-   Run the command {{SystemInput|ldd FreeCAD}} from a terminal
-   Note down the version of the {{FileName|libCoin.so}} library that FreeCAD is using (for example {{FileName|libCoin.so.60}})
-   Locate the {{FileName|libSoQt.so}} library (usually in {{FileName|/usr/lib}})
-   run {{SystemInput|ldd libSoQt.so}} and check if it links to the same Coin version as FreeCAD

If there is any difference, either FreeCAD or SoQt must be recompiled (better to recompile the one that uses the oldest Coin version). The normal behavior is to try to contact the people responsible for packaging either SoQt or FreeCAD and kindly ask them to consider recompiling. If you want to undertake that step for yourself, and it is not possible to recompile SoQt because it breaks other applications on your system, you can force FreeCAD to compile with the required Coin version with {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. But you have to make sure that the correct development package of this Coin version is installed.

### FreeCAD se bloquea después de Edición → Alineación 

Un fallo de segmentación ocurre en {{SystemOutput|vbo_save_playback_vertex_list()}}. Esto significa que la implementación de VBO en el controlador gráfico es mala. Para evitar el almacenamiento en caché de las llamadas a OpenGL puedes intentar establecer la variable de entorno {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} y reiniciar FreeCAD.


<div class="mw-translate-fuzzy">

### Tengo problemas para ejecutar FreeCAD en Mac OSX 


</div>


<div class="mw-translate-fuzzy">

La plataforma Mac es menos fácil de soportar que Windows o Linux, ya que ninguno de los desarrolladores principales posee una. Los paquetes para OSX son compilados por usuarios voluntarios de FreeCAD, y a veces pueden no funcionar correctamente en tu máquina, dependiendo de tu sistema. Tu mejor oportunidad es probablemente ir a los foros, buscar hilos relacionados con Mac OSX, y discutir tu problema allí o ver si alguien más encontró una solución.


</div>

### No puedo cambiar los valores numéricos en los paneles de propiedades de FreeCAD 

<img alt="opciones de idioma" src=images/Jj62l.png  style="width:480px;">

Lo más probable es que tenga una mala configuración regional de Windows. Compruebe si tiene el mismo símbolo para el separador decimal y el símbolo de agrupación de dígitos en su configuración regional. Si es así, [adapte la configuración de su sistema](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) para utilizar caracteres diferentes para el símbolo de agrupación de dígitos y el separador decimal. Tenga en cuenta que no es obligatorio utilizar el punto como separador de decimales. Es obligatorio utilizar símbolos diferentes en estas dos configuraciones. 

### FreeCAD se estaba ejecutando normalmente, y de repente ya no se inicia 

Esto también puede ocurrir si tenías una versión anterior de FreeCAD instalada, y actualizaste a una versión más reciente. En ese proceso, los archivos de configuración de FreeCAD podrían haberse corrompido por alguna razón, y ahora FreeCAD no puede leerlos más, y falla al iniciarse. La solución es simplemente borrar estos archivos de configuración, para que FreeCAD los recree en la primera ejecución.

-   On Windows: Open the file explorer, and write {{FileName|%APPDATA%\FreeCAD}} as the file path. Once there, delete the files {{FileName|user.cfg}} and {{FileName|system.cfg}}
-   On Linux: Navigate to {{FileName|/home/USERNAME/.FreeCAD}} and delete the files {{FileName|user.cfg}} and {{FileName|system.cfg}}
-   On Mac: Navigate to {{FileName|/Users/USERNAME/Library/Preferences/FreeCAD}} and delete the files {{FileName|user.cfg}} and {{FileName|system.cfg}}

FreeCAD should now start again normally with all its settings reset.

There is a [Macro findConfigFiles](Macro_findConfigFiles.md) available to help in locating your configuration files. It can be installed using the Addon Manager in the Tools menu. **Tools → Addon Manager → Macros → findConfigFiles**. The macro will find your config file folder, copy it to the clipboard, and (attempt to) open that location with your default file browser. It makes no changes to your files or settings.

## Utilizando FreeCAD 

### ¿Es FreeCAD realmente gratuito? ¿Incluso para uso comercial? 

FreeCAD es [software de código abierto](http://en.wikipedia.org/wiki/Open-source_software), y es libre no sólo para usarlo, para uno mismo o para hacer un trabajo comercial, sino también para distribuirlo, modificarlo, o incluso usarlo en una aplicación de código cerrado. En resumen, usted es libre de hacer (casi) todo lo que quiera con él. Vea la página [Licencia](Licence/es.md) para más detalles.

### ¿Cómo puedo girar la vista 3D? 


<center>

Image:Style\_of\_navigation.png\|From the **right button** mouse Image:Style of navigation menu.png\|From the menu **Edit → Preferences →**


</center>




FreeCAD has several different [navigation modes](Mouse_navigation.md) available, that can be set in the preferences settings dialog or changed by right-clicking in the 3D view. For full details about the modes, see the [Mouse navigation](Mouse_navigation.md) page. For the default mode (\"CAD Navigation\"), the commands are as follows, 


{{CAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view<br>First method
|Rotate_view_alt_name=Rotate view<br>Alternate method
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.

Holding down **Ctrl** allows the selection of multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.
|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [spinning](spinning.md), if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}

### ¿Qué puedo hacer con FreeCAD? ¿Por dónde empiezo? 

Head to the [Getting started](Getting_started.md) page for a quick description of the tools you can use. There is also a new [Tutorials](Tutorials.md) section containing a few resources. The [User hub](User_hub.md) section contains more detailed information about the different workbenches of FreeCAD. Note that since FreeCAD is relatively new, its user interface is still very bare and doesn\'t feature many tools. But much more advanced functionality is already available to you from [Python scripting](Power_users_hub.md).

### ¿Hay documentación para los recién llegados? ¿Cómo puedo aprender a usar FreeCAD? 

There is a lot of documentation spread in different places, both on and outside the FreeCAD website. You might want to start with the [Getting started](Getting_started.md) page. The [Tutorials](Tutorials.md) section contains many specialized tutorial pages to help you getting started with the different workbenches. The [Manual:Introduction](Manual:Introduction.md) is a general, complete user-oriented guide to FreeCAD. The [User hub](User_hub.md) section of this wiki lists all pages aimed at end users. On external sites like [Youtube](https://www.youtube.com/results?search_query=freecad), you will also find a load of video tutorials created by users. And, last but not least, the [forum](https://forum.freecadweb.org) contains a lot of replies to questions asked by other newcomers.

### Quiero importar/exportar datos en formato XYZ a/desde FreeCAD. ¿Cómo lo hago? 

Please refer to the page [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Maybe your questions are already answered there.

## Trabajar con la geometría de la pieza 

### ¿Cómo puedo extrudir cosas en sólidos? No obtengo el resultado correcto 

The theory is simple: Lines (or wires), when extruded, form faces. Faces, when extruded, form solids. If you extrude something and the result is not a solid, then the something was not a face. If you have lines and you want to extrude a solid from them, you must first select lines that form a closed perimeter (select several objects by pressing **Ctrl**), join them into a wire ([Draft Upgrade tool](Draft_Upgrade.md)), then make a face from that wire (<img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> Upgrade tool again). There you are, if all went well you can now extrude it to a solid.

Now, there can be many little twists that make you obtain the wrong result. The best way to make sure is to check what\'s inside the object you are extruding. Objects contents can be easily explored with python. Assuming for example you have an object called \"Wire\", you could type this into the Python console:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

The above code retrieves the shape from an object, shows the faces and wires your object has (if any), and, if there are wires, prints if those wires are closed. If you don\'t have any face, you won\'t get a solid. If there is no closed wire, it won\'t become a face. If you are interested, there is more info about what you can check with Python on the [part scripting](Topological_data_scripting.md) page. If you cannot join several lines into a wire, the most probable cause is that their endpoints don\'t meet, there must be small gaps between (some of) them. There, I\'m afraid, my experience tells me the quickest way would be to redraw a wire on top of them.

### Mis operaciones booleanas fallan, o dan resultados extraños 

The [Open CASCADE](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) geometric modeling kernel used in FreeCAD for Part geometry, although probably the best open-source geometry kernel available, has its flaws and limitations. Indeed the boolean operations (fusion, subtraction, intersection) are not its best features, and often give strange results. This is a current limitation we have no way to solve at once, so your best path is to try obtaining the desired result by modeling another way. For example, problems with primitives such as cylinder can often be solved by using an extruded circle instead. Coplanar surfaces between parts can cause trouble, as well as surface tangency. As a general rule, if a shape doesn\'t work, try remodeling it a different way. In 99% of the cases at the end you will manage to obtain the result you want.

### When I export (or view) my model, the holes are filled in 

Don\'t use **Crtl** + **A** (Select All) to export everything from the hierarchy tree. If the model is of one single item, try selecting only the newest item (usually the last one) in the hierarchy tree.

As we create a model in the [PartDesign Workbench](PartDesign_Workbench.md), each feature takes the shape of the last one and adds or removes something, creating linear dependencies from feature to feature as the model is created. Hence a \"Cut\" feature is not only the cut hole itself, but the whole part with the cut. This is why the user usually should only have the newest item (feature) in the model tree visible, because otherwise the phases of the model overlay each other, and holes are filled in by the earlier model features.

To toggle visibility of an object on or off, select it in the hierarchy tree and press **spacebar** on your keyboard. Usually everything but the last item in the hierarchy tree should be greyed out and therefore not visible in the 3D view.

### Mis objetos paramétricos se rompen cuando modifico sus bocetos base 

You have met the (in)famous toponaming problem. This is currently a major issue in FreeCAD for newcomers. It is present all over FreeCAD, but is more prominent when using [sketches](Sketcher_Workbench.md). The explanation is simple: When recalculating a sketch, the geometric entities (edges, faces\...) are rebuilt in a different order, depending on the constraints precedence. They then receive a different name (Edge1, Edge2, Face1, Face2\...). Most subsequent operations depend on these names to identify which subcomponent they work on. Therefore, when the sketch is rebuilt, features that are based on such subcomponents might suddenly get their base geometry changed and give a wrong result.

This is a very hard problem to overcome (the [Topological Naming Project](Topological_Naming_Project.md) aims at solving it). However, there are many workarounds available to mitigate the problem, and more advanced users generally manage to avoid it completely. A couple of strategies are:

-   Know that sketches are highly sensitive to the problem. Referencing a specific edge of a sketch, or a face of an object built on a sketch, such as a [PartDesign Pad](PartDesign_Pad.md), is dangerous, unless you are pretty confident that these sketches will not change over time or the sketch is very simple. A Pad built on a simple rectangular sketch, for example, will likely be safe as it will generate only one face, so there is no order problem.
-   Prefer other kinds of objects such as [Part](Part_Workbench.md) or [Draft](Draft_Workbench.md) when possible. These objects are always built the same way, and therefore their geometric components usually follow the same order each time they are rebuilt. They are much less susceptible to toponaming problems.
-   To attach further objects onto the faces of sketch-based geometry, prefer using [Datum geometry](PartDesign_Plane.md). These invisible \"helper objects\" don\'t depend on sketch geometry, and therefore stay stable over time.

## Contribución a FreeCAD 

### ¡FreeCAD es un gran programa! ¿Cómo puedo ayudar? 

There are a lot of different ways to help, even if you are not a programmer. Here are a couple of things you can do:

-   Give some feedback to the FreeCAD developers: It is always useful to know what people think, what they found good, what they miss, etc. Drop a note on the [forum](http://forum.freecadweb.org/) giving your opinion or make a request on our [issue tracker](https://tracker.freecadweb.org/main_page.php)!
-   Help with writing documentation: The documentation we have here on this site is sometimes very limited. If you discovered something that is not well documented, add your knowledge there!
-   Help others newcomers: Hang around the forum, and help new people to solve basic questions, like how do I install, how do I add a cube, etc.
-   [Translate the documentation](Help_FreeCAD#Translate_the_documentation.md) into your own language
-   [Translate FreeCAD](Help_FreeCAD#Translate_FreeCAD.md) into your own language
-   Write [Tutorials](Tutorials.md), or record video tutorials: Tutorials are a very easy way for newcomers to learn a new software. If you did some nice stuff, why not show other people how to do it?
-   Contribute with assets and examples: We are still missing good example files in FreeCAD. If you created something good, share it with us!
-   [Submit bugs](Tracker.md): It is very important to have all possible bugs fixed. If you find one, report it as clearly as possible, so we can understand exactly what\'s happening.
-   Try to do some Python coding: You never programmed before but you want to try? Python is easy. Read our [introduction to Python](Introduction_to_Python.md), but beware, you might get addicted quickly!
-   See the [Help FreeCAD](Help_FreeCAD.md) page for more details on how to contribute.

### ¿Cómo puedo obtener permiso de edición en el wiki? 

See the [Work on the documentation](Help_FreeCAD#Work_on_the_documentation.md) page paragraph for more details on how to contribute.

### ¿Participa FreeCAD en el Google Summer of Code? 

Yes. Beginning in 2016, FreeCAD participates in Google Summer of Code. See [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) for information on past editions, and [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) in the forum for the original announcement.

### Quiero empezar a traducir el wiki en mi propio idioma. ¿Qué hago? 

This wiki is hosting a lot of contents. The most up-to-date and interesting material is gathered in the [manual](Online_Help_Toc.md).

See the [Translate the documentation](Help_FreeCAD#Work_on_the_documentation.md) page paragraph for more details on how to translate the wiki.

## Licencia, copia y reutilización 

### ¿Tengo que pagar algo para usar FreeCAD? 

No. FreeCAD is totally free to use, to download, to redistribute, or to modify. It is [open-source software](https://en.wikipedia.org/wiki/Open_source), published under the terms of the [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), which guarantees you those freedoms and, even more important, guarantees you that these freedoms will never be taken from you.

### ¿Puedo reutilizar cualquier parte del material gráfico de FreeCAD o piezas del sitio web? 

Sure. All the artwork (icons, banners, etc.) of FreeCAD are licensed LGPL, same as the FreeCAD code. Help yourself on the [Artwork](Artwork.md) page. The website is a standard MediaWiki site, all graphic elements can freely be reused, and if you are curious about how to tweak the MediaWiki software like we did, look for the special Common css and js pages.

### ¿Puedo reutilizar piezas de FreeCAD en otra aplicación? 

Yes, you can use the core parts of FreeCAD in other applications as long as you comply with the terms of the LGPL. Third party libraries, [external workbenches](External_workbenches.md), and [macros](Macros.md) may be subject to their own license terms, so please consult with their authors. More details on the [Licence](Licence.md) page.







[Category:Documentation{{\#translation:}}](Category:Documentation.md)
