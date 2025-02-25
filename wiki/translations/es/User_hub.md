# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/es



Esta área es el área de ayuda principal para los nuevos usuarios de FreeCAD.

FreeCAD está en continuo desarrollo, por lo que puede faltar información o estar desactualizada. Si no encuentras la información que necesitas, no dudes en preguntar en el [Foro de FreeCAD](https://forum.freecad.org).

Si quieres contribuir a FreeCAD, por favor [donar](donate/es.md), y mira la página [Ayuda a FreeCAD](Help_FreeCAD/es.md) para otras formas de contribuir.Si quieres editar este wiki, solicita una cuenta en el wiki con permisos de editor [en el foro](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830), y lee las [Páginas del wiki](WikiPages/es.md) para conocer las directrices generales que debes seguir.

Si quieres saber cómo empezó FreeCAD hace años visita la página [History](History/es.md).



## Utilizando FreeCAD 



### Introducción

-   [Resumen de la aplicación](About_FreeCAD/es.md): Una visión general de FreeCAD
-   Instalación: Cómo instalar FreeCAD en [Windows](Installing_on_Windows/es.md), [Linux](Installing_on_Linux/es.md) y [Mac](Installing_on_Mac/es.md)
-   [Instalación de archivos de ayuda](Installing_Helpfile/es.md): cómo instalar la documentación offline que se basa en este wiki.
-   [Instalar componentes adicionales](Installing_additional_components/es.md): cómo instalar componentes adicionales de terceros que pueden trabajar junto con FreeCAD.
-   [Cómo empezar](Getting_started/es.md): Una rápida visión general de las herramientas disponibles.
-   [PMF](Frequently_asked_questions/es.md): Preguntas más frecuentes
-   [Tutoriales](Tutorials/es.md) que cubren diferentes partes de FreeCAD



#### ¿Migrando desde otro software? 

-   [Soluciones alternativas](Workarounds/es.md)
-   [Migrando a FreeCAD desde Fusion360](Migrating_to_FreeCAD_from_Fusion360/es.md)
-   [Migrando a FreeCAD desde OnShape](Migrating_to_FreeCAD_from_OnShape/es.md)
-   [Migrando a FreeCAD desde SolidWorks](Migrating_to_FreeCAD_from_SolidWorks/es.md)
-   [Migrando a FreeCAD desde Revit](Migrating_to_FreeCAD_from_Revit/es.md)
-   [Guía de migración BIM de FreeCAD](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [Tabla de compatibilidad de aplicaciones BIM](BIM_application_compatibility_table/es.md)



### Aplicación basica 

-   [Interfaz](Interface/es.md): la interfaz de FreeCAD se compone de varios elementos gráficos en la pantalla, incluyendo la [vista 3D](3D_view/es.md), la [vista de árbol](Tree_view/es.md), el [editor de propiedades](Property_editor/es.md), el [panel de tareas](Task_panel/es.md), y la [consola Python](Python_console/es.md).
-   [Navegación con ratón](Mouse_navigation/es.md): los diferentes tipos de uso del ratón o trackpad para navegar en la vista 3D.
-   [Métodos de selección](Selection_methods/es.md): los diferentes métodos de selección de objetos en el software.
-   [Nombrado de objetos](Object_name/es.md): todos los objetos de FreeCAD tienen un `Name` de sólo lectura que los identifica de forma única, y un `Label` que es editable por el usuario.
-   [Editor de Preferencias](Preferences_Editor/es.md): el sistema que permite controlar muchas propiedades del sistema base y de los bancos de trabajo individuales.
-   [Formatos de archivo](Import_Export/es.md): los diferentes formatos de archivo que FreeCAD puede leer y escribir.



### Ambientes de trabajo 

Los [bancos de trabajo](Workbenches/es.md) son colecciones de herramientas utilizadas para tareas específicas. Estos son los bancos de trabajo base que se incluyen en cada instalación de FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Herramientas estándar](Std_Base/es.md). Estos comandos y herramientas están presentes en todos los bancos de trabajo.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> El [banco de trabajo Assembly](Assembly_Workbench.md) para la construcción y resolución de ensamblajes mecánicos. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> El [banco de trabajo BIM](BIM_Workbench.md) para trabajar con elementos arquitectónicos y crear modelos [BIM](https://en.wikipedia.org/wiki/Building_information_modeling). Combina el banco de trabajo Arch y el anteriormente externo banco de trabajo BIM disponible en {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> El [banco de trabajo CAM](CAM_Workbench.md) es usado para producir instrucciones de código-G. Este banco de trabajo se llamaba \"banco de trabajo Path\"en {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> El [banco de trabajo Draft](Draft_Workbench/es.md) contiene herramientas 2D y operaciones CAD básicas en 2D y 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> El [banco de trabajo FEM](FEM_Workbench/es.md) proporciona un flujo de trabajo de análisis de elementos finitos (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> El [Banco de Trabajo de Inspección](Inspection_Workbench/es.md) está hecho para dar herramientas específicas para el examen de formas. Todavía está en una etapa temprana de desarrollo.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> El [banco de trabajo Material](Material_Workbench.md) maneja el sistema de materiales de FreeCAD. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> El \[\[Mesh_Workbench/es\|banco de

trabajo Mesh\]\] para trabajar con mallas trianguladas.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> El [banco de trabajo OpenSCAD](OpenSCAD_Workbench/es.md) para la interoperabilidad con OpenSCAD y la reparación de [geometría sólida constructiva](Constructive_solid_geometry/es.md) (CSG) del historial del modelo.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> El [Banco de Trabajo Part](Part_Workbench/es.md) para trabajar con primitivas geométricas y operaciones booleanas.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> El [banco de trabajo PartDesign](PartDesign_Workbench/es.md) para construir formas de piezas a partir de croquis.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> El [banco de trabajo Points](Points_Workbench/es.md) para trabajar con nubes de puntos.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> El [Banco de Trabajo de Ingeniería Inversa](Reverse_Engineering_Workbench/es.md) pretende proporcionar herramientas específicas para convertir formas/sólidos/mallas en características paramétricas compatibles con FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> El [banco de Trabajo de Robots](Robot_Workbench/es.md) para estudiar los movimientos de los robots. Actualmente no esta mantenido.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> El [banco de trabajo Sketcher](Sketcher_Workbench/es.md) para trabajar con croquis de geometría restringida.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> El [banco de trabajo de Hojas de Cálculo](Spreadsheet_Workbench/es.md) para crear y manipular datos de hojas de cálculo.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> El [banco de trabajo de Superficies](Surface_Workbench/es.md) proporciona herramientas para crear y modificar superficies. Es similar a la opción [Pieza Constructor](Part_Builder/es.md) Opción de cara desde las aristas.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> El [Banco de Trabajo Dibujo Técnico](TechDraw_Workbench/es.md) para producir dibujos técnicos a partir de modelos 3D. Es el sucesor del [Banco de Trabajo de Dibujo](Drawing_Workbench/es.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> El [banco de Trabajo del Prueba Estructura del marco](Testing/es.md) es para depurar FreeCAD.

### Macros

[Macros](Macros/es.md) son fragmentos relativamente pequeños de código [Python](Python/es.md) que realizan una tarea simple o compleja que no está disponible en el sistema base de FreeCAD.

Usuarios avanzados han escrito varios [macros](macros/es.md) para enriquecer FreeCAD con mas capacidades.

Desde FreeCAD 0.17, muchas macros pueden ser instaladas usando el [Gestor de complementos](Std_AddonMgr/es.md). Para una lista de las macros consulte la página [Recetas de macros](Macros_recipes/es.md). Para la instalación manual vea [Cómo instalar macros](How_to_install_macros/es.md).



### Bancos de trabajo externos 

Cuando se desarrollan muchas macros o funciones juntas, y se organizan en barras de herramientas y menús, pueden convertirse en un nuevo banco de trabajo.

Los [bancos de trabajo externos](External_workbenches/es.md) son colecciones de funciones que no forman parte del sistema base de FreeCAD, normalmente desarrolladas por usuarios experimentados, y dirigidas a una necesidad particular.

Desde FreeCAD 0.17, muchos bancos de trabajo pueden ser instalados usando el [Gestor de complementos](Std_AddonMgr/es.md). Para la instalación manual vea [Cómo instalar bancos de trabajo adicionales](How_to_install_additional_workbenches/es.md).



## Referencia

-   [Referencia de comandos](List_of_Commands/es.md): Una lista completa de los comandos disponibles de FreeCAD.



## Ayuda en línea 

Esta es la ayuda en línea oficial de FreeCAD. Por favor ten en cuenta que el sistema de ayuda en línea entero está actualmente en construcción. Podrá ser utilizado para generar un archivo .CHM, que se distribuirá con los paquetes binarios de FreeCAD. De momento la ayuda en línea resume algunas de las secciones más completas de esta wiki.

-   [Sistema de ayuda en línea - Índice de contenidos](Online_Help_Toc/es.md)



## Más

-   El [Centro de usuarios avanzados](Power_users_hub/es.md) es el lugar al que ir si quieres ver usos más avanzados de FreeCAD
-   El [Portal de la Comunidad de FreeCAD](FreeCAD_Community_Portal/es.md) lista los proyectos realizados por los miembros de la comunidad en torno a FreeCAD.
-   ¿No entiendes un término o una frase usada en FreeCAD? Prueba la página [Glossary](Glossary/es.md).



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/es
