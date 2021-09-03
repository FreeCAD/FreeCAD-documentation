





{{TOCright}}

## Prólogo

FreeCAD es una 3D [aplicación de modelado paramétrico](About_FreeCAD/es.md). Esta primeramente hecha para diseño mecánico, pero también sirve a muchos otros usos donde donde necesitas modelado 3D con precisión y control sobre historial de modelado.

FreeCAD se ha estado desarrollando desde 2002, y ofrece una amplia lista de [características](Feature_list/es.md). Todavía faltan capacidades, pero es lo suficientemente potente para el uso de aficionados y pequeños talleres. Hay una comunidad en rápido crecimiento de usuarios entusiastas que participan en el [foro de FreeCAD](http://forum.freecadweb.org/index.php), y se pueden encontrar [muchos ejemplos](https://forum.freecadweb.org/viewforum.php?f=24) de proyectos de calidad desarrollados con FreeCAD allí. Véase también, [FreeCAD utilizado en producción](FreeCAD_used_in_production/es.md).

Como todos los proyectos de software libre, FreeCAD depende de su comunidad para crecer, obtener características y corregir errores. No olvide esto cuando use FreeCAD; si le gusta, puede [donar](Donate/es.md) y [ayudar a FreeCAD](Help_FreeCAD/es.md) de varias maneras, como escribir documentación y hacer traducciones.

Ver también:

-   [Migrando a FreeCAD desde Fusion360](Migrating_to_FreeCAD_from_Fusion360/es.md)
-   [Tutoriales](Tutorials/es.md)
-   [Video Tutoriales](Video_tutorials/es.md)

## Instalación


<div class="mw-translate-fuzzy">

En primer lugar, descargue e instale FreeCAD. Consulte la página [Descargar](Download/es.md) para obtener información sobre las versiones y actualizaciones actuales, y la página [Instalar](Installing/es.md) para obtener instrucciones de instalación. Hay paquetes de instalación listos para Windows (.msi), Debian y Ubuntu (.deb), openSUSE (.rpm), y Mac OSX. FreeCAD está disponible en los gestores de paquetes de muchas otras distribuciones de Linux. También está disponible un ejecutable [AppImage](AppImage/es.md) independiente, que se ejecutará en los sistemas Linux de 64 bits más recientes. Como FreeCAD es de código abierto, también puede tomar el código fuente y [compilar](Compiling/es.md) usted mismo.


</div>

## Explorando la interfaz {#explorando_la_interfaz}

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;"> 
*Interfaz estándar de FreeCAD en 0.19.*


</div>


**Vea una explicación completa en [Interfaz](Interface/es.md).**


:   1\. El [área\_de\_visión\_principal](main_view_area/es.md), que puede contener diferentes ventanas con pestañas, principalmente la [vista\_3D](3D_view/es.md).
:   2\. La [Vista\_3D](3D_view/es.md), que muestra los objetos geométricos del documento.
:   3\. La [vista\_árbol](tree_view/es.md) (parte de la [Vista combo](combo_view/es.md)), mostrando la jerarquía y el historial de construcción de los objetos del documento; también puede mostrar el [panel de tareas](task_panel/es.md) para los comandos activos.
:   4\. El [editor de propiedades](property_editor/es.md) (parte de la [Vista combo](combo_view/es.md)), que permite ver y modificar las propiedades de los objetos seleccionados.
:   5\. La [vista de selección](selection_view/es.md), que indica los objetos o subelementos de los objetos (vértices, bordes, caras) que están seleccionados.
:   6\. La [vista\_de\_informe](report_view/es.md) (o ventana de salida), donde se muestran los mensajes, advertencias y errores.
:   7\. La [Consola Python](Python_console/es.md), donde se imprimen todos los comandos ejecutados, y donde se puede introducir el código [Python](Python/es.md).
:   8\. La [barra de estado](status_bar/es.md), donde aparecen algunos mensajes y tooltips.
:   9\. El área de la barra de herramientas, donde están acopladas las barras de herramientas.
:   10\. El [seleccionador de bancos ambientes de trabajo](Std_Workbench/es.md), donde se selecciona el [ambiente de trabajo](workbenches/es.md) activo.
:   11\. El [menú estándar](Standard_Menu/es.md), que contiene las operaciones básicas del programa.

El concepto principal detras de la interface de Freecad es que esta separado en [Ambientes de trabajos](workbenches/es.md). Un Ambiente de trabajo es una colección de herramientas adecuadas para una tarea especifica, tal como trabajar con [mallas](Mesh_Workbench/es.md), o dibujar [objetos 2D](Draft_Workbench/es.md), o [Croquis restringido](Sketcher_Workbench/es.md). Puedes cambiar el ambiente de trabajo actual con el [selector de ambientes de trabajo](Std_Workbench/es.md). Puedes [personalizar](Interface_Customization/es.md) la herramientas incuidas en cada ambiente de trabajo, agregar herramientas de otros ambiente de trabajo o incluso herramientas propias, que nosotros llamamos [macros](macros/es.md). Puntos de inicio ampliamente utilizados son [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md) and [Ambiente de trabajo Pieza](Part_Workbench/es.md).

Cuando comienzas FreeCAD por primera vez, se te presenta el centro de inicio. Esto es lo que parece para la versión 0.18:

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;"> 
*Para FreeCAD 0.17 vea esta [centro de inicio](Media:Startcenter0.17.jpg.md) pantalla.*

El centro de inicio te permite dirigirte rapidamente a uno de los ambientes de trabajo mas comunes, abre uno de los archivos recientes, u observa las ultimas noticias del mundo de FreeCAD. Puedes cambiar el banco de trabajo predeterminado dentro de [preferencias](Preferences_Editor/es.md).

## Navegando en el espacio 3D {#navegando_en_el_espacio_3d}

FreeCAD tiene tres diferentes [Modos de navegación](Mouse_navigation/es.md) disponibles, que se pueden establecer en las preferencias del diálogo de configuración o cambiar pulsando el botón derecho en la vista 3D. Para ver más detalles sobre los modos mira la página [Modos de navegación](Mouse_navigation/es.md). Para el modo de navegación por defecto **Navegación CAD**(Puedes cambiar rapidamente el actual modo de navegación dado clic derecho en un area vaci de la vista 3D):


{{CAD Navigation/es}}


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

También tiene varias vistas preconfiguradas (vista superior, vista frontal, etc.) disponibles en el menú Ver, en la barra de herramientas Ver, y, por atajos numéricos (**1**, **2**, etc\...). Dado clic derecho sobre un objeto o sobre un area vacia de la vista 3D, tienes acceso directo a algunas operaciones comunes, tal como configurar una vista particular, o ubicar un objeto en la vista de árbol.

## Primeros paso con FreeCAD {#primeros_paso_con_freecad}

El enfoque de FreeCAD es permitirte hacer modelos 3D de alta presición, para mantener un control ajustado sobre estos modelos(ser capaz de retroceder dentro del historial de modelado y cambiar parametros), y eventualmente construir estos modelos (impresion 3D, mecanizado CNC o incluso sitio de construción). Es por lo tanto muy diferente de algunas otras aplicaciones 3D hechas para otros propositos, tal como animacion o juegos. Su curva de aprendizaje puede ser doloroza, especialmente si este es tu primer contacto con modelado 3D. Si esta atorado en algun punto, no olvides que la amigable comunidad de usuarios en el [Foro de FreeCAD](http://forum.freecadweb.org/index.php) podrian sacarte en poco tiempo.

El ambiente de trabajo que empezaras a utilizar depende sobre el tipo de trabajo que necesitas hacer: Si tu vas a trabajar sobre modelos mecanicos, o más generalmente hablando cualquier objecto de pequeña escala, tu podrias probablemente querer probar el [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md). Si vas a trabajar en 2D, entonces cambia a el [Ambiente de trabajo Borrador](Draft_Workbench/es.md) o el [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md) si necesitas acotaciones. si tu quieres hacer BIM, ejecuta el [Ambiente de trabajo Arquitectura](Arch_Workbench/es.md). Si estas trabajando con diseño de barcos, allí esta un [Ambiente de trabajo Navío](Ship_Workbench/es.md) para tí. Y si tu vienes del mundo de OpenSCAD prueba el [Ambiente de trabajo OpenSCAD](OpenSCAD_Workbench/es.md). También hay disponibles muchos [Ambientes de trabajo externos](External_workbenches/es.md) desarrollados por la comunidad.

Tú puedes cambiar de ambiente de trabajo en el momento que quieras, y también [personalizar](Interface_Customization/es.md) tu Ambiente de trabajo favoritos agregando herramientas de otros Ambiente de trabajos.

## Trabajando con el Ambiente de trabajo DiseñoPiezas y Ambiente de trabajo Croquizador {#trabajando_con_el_ambiente_de_trabajo_diseñopiezas_y_ambiente_de_trabajo_croquizador}

El [Ambiente de trabajo diseño de parte](PartDesign_Workbench/es.md) esta especialmente hecho para hacer objetos complejos, iniciando a partir de simples formas, y agregando o removiendo piezas (que nosotros llamamos \"características\"),hasta que obtienes tu objeto final.Todas las características que tu apliques durante el proceso modelado seran almacenadas en una vista separada llamada [vista de árbol](Document_structure/es.md), el cual contiene los otros objetos de tu documento.Puedes pensar que los objetos de diseño de parte son como una sucesión de operaciones, cada una aplicada al resultado del que lo precede, formando una gran cadena. Dentro de la vista de árbol, puedes ver el objeto final, pero puedes expandirla y contraer todos los estados que lo preceden, y cambiar cualquiera de sus parámetros, el cual automáticamente actualiza el objeto final.

El Ambiente de trabajo diseño de parte es fuertemente utilizado por otros Ambiente de trabajo, el [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md). El Boceto te permite dibujar formas 2D, las cuales son definidas aplicando cotas a las formas 2D. Por ejemplo, tal vez quieras dibujar un rectángulo y colocar el tamaño de lado a lado de una cota de longitud a una esquina de los lados. Ese lado entonces no puede ser cambiar el tamaño mas(al menos que la cota sea cambiada).

Esas formas 2D hechas con Boceto son utilizadas mucho en el banco de trabajo diseño de parte, por ejemplo para crear volúmenes 3D, o para dibujar áreas sobre una de las caras de tu objeto que luego sera ahuecado a partir del del volumen principal. Este es un flujo de trabajo típico de diseño de parte:

1.  Crear un boceto nuevo
2.  Crea un dibujo con forma cerrada(asegurarse que todos los puntos están cerrados)
3.  Cerrar el boceto
4.  Expandir el boceto a un solido 3D utilizando la herramienta de rellenado.
5.  Selecciona una cara del solido
6.  Crea un segundo boceto (Esta vez sera dibujado sobre la cara seleccionada)
7.  Dibuja una forma cerrada
8.  Cierra el boceto
9.  Crea un vaciado a partir del segundo boceto, sobre el primer objeto

El cual te da un objeto como este:

<img alt="" src=images/Partdesign_example.jpg  style="width:1024px;">

En cualquier momento, puedes seleccionar el origen del croquis y modificarlo, o cambiar los parametros de extrusión de la plataforma u operaciones de baciado, las cuales actualizarán el objeto final.

## Trabajando con el Ambiente de trabajo Borrador y el Ambiente de trabajo Arquitectura {#trabajando_con_el_ambiente_de_trabajo_borrador_y_el_ambiente_de_trabajo_arquitectura}

El [Ambiente de trabajo Borrador](Draft_Workbench/es.md) y [Ambiente de trabajo Arquitectura](Arch_Workbench/es.md) se comportan un poco diferente que los otros bancos de trabajo de arriba, a pesar que ellos siguen las mismas reglas, las cuales son comunes de todo FreeCAD. En breve, mientras el Boceto y diseño de parte están hechas primeramente para diseñar piezas sencillas, borrador y arquitectura son hechos para facilitar tu trabajo cuando están trabajando con varios, objetos sencillos.

El [Ambiente de trabajo Borrador](Draft_Workbench/es.md) le ofrece herramientas 2D un poco similares a las que puede encontrar en aplicaciones CAD 2D tradicionales como [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Sin embargo, el dibujo en 2D está muy lejos del alcance de FreeCAD, no espere encontrar allí la gama completa de herramientas que ofrecen estas aplicaciones dedicadas. La mayoría de las herramientas Borrador funcionan no solo en un plano 2D sino también en el espacio 3D completo, y se benefician de los sistemas auxiliares especiales tales como [Planos de trabajo](Draft_SelectPlane/es.md) y [Atrapar objeto](Draft_Snap/es.md).

El [Ambiente de trabajo Arquitectura](Arch_Workbench/es.md) agrega herramientas [modelado de información de construcción (BIM)](https://es.wikipedia.org/wiki/Modelado_de_informaci%C3%B3n_de_construcci%C3%B3n) a FreeCAD, lo que le permite construir modelos arquitectónicos con objetos paramétricos. El Ambiente de trabajo Arquitectura se basa mucho en otros módulos, como Borrador y Croquizador. Todas las herramientas de borrador están también presentes en el ambiente de trabajo de Arquitectura, y la mayoría de las herramientas de Arquitectura hacen uso de los sistemas de ayuda de Borrador.

Un flujo de trabajo típico con los ambientes de trabajo Arquitectura y Borrador podría ser:

1.  Dibuja un par de líneas con la herramienta línea de Borrador
2.  Selecciona cada línea y presione la herramienta Muro para construir un muro en cada una de ellas
3.  Une las paredes seleccionándolas y presionando la herramienta Arquitectura Add
4.  Crea un objeto de piso y mueve tus muros dentro desde la vista de árbol
5.  Crea un objeto de construcción y mueve tu piso dentro desde la vista de árbol
6.  Crea una ventana haciendo clic en la herramienta Ventana, selecciona un ajuste preestablecido en su panel y luego haz clic en una cara de un muro
7.  Añade dimensiones configurando primero el plano de trabajo si es necesario, luego usando la herramienta Borrador Dimension

El cual te dará esto:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:1024px;">

Más en la [Tutorialespágina](Tutorials/es.md).

## Complementos, Macro y Ambiente de trabajo Externos {#complementos_macro_y_ambiente_de_trabajo_externos}

Freecad, como software de código abierto, ofrece la posibilidad de complementar sus ambiente de trabajo con complementos.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Guión

Y finalmente, una de las características más poderosas de FreeCAD es el entorno [scripting](scripting/es.md). Desde la consola python integrada (o desde cualquier otro script python externo), se puede acceder a casi cualquier parte de FreeCAD, crear o modificar la geometría, modificar la representación de esos objetos en la escena 3D o acceder y modificar la interfaz de FreeCAD. El script Python también se puede utilizar en [macros](macros/es.md), que proporcionan un método sencillo para crear comandos personalizados.

## ¿Qué hay de nuevo {#qué_hay_de_nuevo}

-   Vea la [notas de lanzamiento](Feature_list/es#Release_notes.md) para la lista detallada de características.





{{Userdocnavi/es}}

[Category:User Documentation/es](Category:User_Documentation/es.md)
