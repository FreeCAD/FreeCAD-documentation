# Feature list/es
Esta es una lista extensa, pero no completa, de las características que FreeCAD implementa.


{{TOCright}}

## Notas de la versión 

-   [Liberación 0.20](Release_notes_0.20/es.md) - Junio 2022
-   [Liberación 0.19](Release_notes_0.19/es.md) - Marzo 2021
-   [Liberación 0.18](Release_notes_0.18/es.md) - Marzo 2019
-   [Liberación 0.17](Release_notes_0.17/es.md) - Abril 2018
-   [Liberación 0.16](Release_notes_0.16/es.md) - Abril 2016
-   [Liberación 0.15](Release_notes_0.15/es.md) - Marzo 2015
-   [Liberación 0.14](Release_notes_0.14/es.md) - Marzo 2014
-   [Liberación 0.13](Release_notes_0.13/es.md) - Enero 2013
-   [Liberación 0.12](Release_notes_0.12/es.md) - Diciembre 2011
-   [Liberación 0.11](Release_notes_0.11/es.md) - Marzo 2011

## Características clave 

-   ![](images/Feature1.jpg ) A complete [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE)-based **geometry kernel** allowing complex 3D operations on complex shape types, with native support for concepts like [Boundary Representation](https://en.wikipedia.org/wiki/Boundary_representation) (BREP), [Non-uniform rational basis spline](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) (NURBS) curves and surfaces, a wide range of geometric entities, boolean operations and [fillets](https://en.wikipedia.org/wiki/Fillet_(mechanics)), and built-in support of [STEP](https://en.wikipedia.org/wiki/ISO_10303) and [IGES](https://en.wikipedia.org/wiki/IGES) formats 
-   ![](images/Feature3.jpg ) A full **parametric model**. All FreeCAD objects are natively parametric, meaning their shape can be based on [properties](Property.md) or even depend on other objects. All changes are recalculated on demand, and recorded by an undo/redo stack. New object types can be added easily, and can even be [fully programmed in Python](Scripted_objects.md).
-   ![](images/Feature4.jpg ) A **modular architecture** that allows plugin extensions (modules) to add functionality to the core application. An extension can be as complex as a whole new application programmed in C++ or as simple as a [Python script](Power_users_hub.md) or self-recorded [macro](Macros.md). You have complete access to almost any part of FreeCAD from the built-in **Python** interpreter, macros or external scripts, be it [geometry creation and transformation](Topological_data_scripting.md), the 2D or 3D representation of that geometry ([scenegraph](Scenegraph.md)) or even the [FreeCAD interface](PySide.md) 
-   ![](images/Feature5.jpg ) Import/export to **standard formats** such as [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) or [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) in addition to FreeCAD\'s native **[FCStd](File_Format_FCStd.md)** file format. The level of compatibility between FreeCAD and a given file format can vary, since it depends on the module that implements it.
-   ![](images/Feature7.jpg ) A [Sketcher](Sketcher_Workbench.md) with integrated constraint-solver, allowing you to sketch geometry-constrained 2D shapes. The constrained 2D shapes built with Sketcher may then be used as a base to build other objects throughout FreeCAD.
-   ![](images/Feature9.jpg ) A [Robot simulation](Robot_Workbench.md) module that allows you to study robot movements in a graphical environment.
-   ![](images/Feature8.jpg ) A [technical drawing module](TechDraw_Workbench.md) with options for detail views, cross sectional views, dimensioning and others, allowing you to generate 2D views of existing 3D models. The module then produces ready-to-export SVG or PDF files. An older [Drawing workbench](Drawing_Workbench.md) with sparse Gui-commands but a powerful Python functionality also exists.
-   ![](images/Feature-raytracing.jpg ) A [Rendering](Raytracing_Workbench.md) module that can export 3D objects for rendering with external renderers. It currently only supports [povray](http://en.wikipedia.org/wiki/POV-Ray) and [LuxRender](http://en.wikipedia.org/wiki/LuxRender), but is expected to be extended to other renderers in the future.
-   ![](images/Feature-arch.jpg ) An [Architecture](Arch_Workbench.md) module that allows [Building Information Modeling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM)-like workflow, with [Industry Foundation Classes](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) compatibility.
-   ![](images/Feature-CAM.jpg ) A [Path module](Path_Workbench.md) dedicated to mechanical machining for [Computer Aided Manufacturing](https://en.wikipedia.org/wiki/Computer-aided_manufacturing) (CAM). Using the Path module you may output, display and adjust the [G code](http://en.wikipedia.org/wiki/G-code) used to control the target machine.
-   ![](images/Feature_spreadsheet.png ) An [Integrated Spreadsheet](Spreadsheet_Workbench.md) and an [expression parser](Expressions.md) which may be used to drive formula-based models and organize model data in a central location.

## Características generales 

-   **multiplataforma**. Se ejecuta y se comporta exactamente de la misma manera en Windows, Linux y macOS.

-   **completa aplicación de interfaz gráfica de usuario (GUI)**. FreeCAD cuenta con una completa interfaz gráfica de usuario basada en el famoso entorno [Qt](http://www.qtsoftware.com/), con un visualizador 3D basado en [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor), que permite un rápido renderizado de escenas 3D y una representación gráfica de escenas muy accesible.

-   **ejecuta como una aplicación de línea de comandos**, con menos requerimientos de memoria. En el modo de línea de comandos, FreeCAD se ejecuta sin su interfaz gráfica GUI, pero con todas sus herramientas de geometría. Puede ser, por ejemplo, utilizado como servidor para producir contenidos para otras aplicaciones.

-   **puede ser importado como un [módulo de Python](Embedding_FreeCAD/es.md)**. FreeCAD puede ser importado en cualquier aplicación que pueda ejecutar scripts de Python. Como en el modo de línea de comandos, la parte de la interfaz de FreeCAD no está disponible, pero todas las herramientas de geometría son accesibles.

-   **concepto de ambiente de trabajo**: En la interfaz de FreeCAD, las herramientas se agrupan en *entornos de trabajo* ([Ambiente de trabajo](Workbenches/es.md)). Esto permite mostrar sólo las herramientas utilizadas para llevar a cabo una cierta tarea, manteniendo el espacio de trabajo ordenado y acondicionado, y que la aplicación se cargue rápidamente.

-   **plugin/módulo marco para la carga tardía de características/tipos de datos**. FreeCAD está dividido en una aplicación central con módulos que se cargan sólo cuando se necesitan. Casi todas las herramientas y tipos de geometría se almacenan en módulos. Los módulos se comportan como plugins; además de la carga tardía, se pueden añadir o eliminar módulos individuales de una instalación existente de FreeCAD.

-   **objetos de documentos asociativos paramétricos**. Todos los objetos de un documento de FreeCAD pueden ser definidos por parámetros. Esos parámetros pueden ser modificados y recalculados en cualquier momento. Dado que las relaciones entre los objetos se mantienen, la modificación de un objeto se propagará automáticamente a cualquier objeto dependiente.

-   *creación primitiva paramétrica*. Los objetos primitivos como la caja, la esfera, el cilindro, etc. pueden ser creados especificando sus restricciones geométricas.

-   **operaciones de modificación gráfica**. FreeCAD puede realizar traslación, rotación, escalado, espejado, desplazamiento (ya sea trivial o como se describe en [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) o conversión de formas, en cualquier plano del espacio tridimensional.

-   *\'[Geometría sólida constructiva](Constructive_solid_geometry/es.md) (operaciones booleanas)*. FreeCAD puede hacer operaciones constructivas de geometría sólida (unión, diferencia, intersección).

-   **creación gráfica de geometría plana**. Se pueden crear gráficamente líneas, hilos, rectángulos, B-splines y arcos circulares o elípticos en cualquier plano del espacio 3D.

-   **modelado con rectas o revueltas** **extrusiones**, **secciones** y **redondeos**.

-   **Componentes topológicos** como **vertices**, **bordes**, **hilos** y **planos**.

-   *probando y reparando*. FreeCAD tiene herramientas para probar mallas (prueba de sólidos, prueba de no-dos-móviles, prueba de auto-intercesión) y para reparar mallas (llenado de agujeros, orientación uniforme).

-   **Anotaciones**. FreeCAD puede insertar anotaciones para el texto o las dimensiones.

-   **Deshacer/Rehacer marco**. Todo en FreeCAD es deshacer/rehacer, con acceso de usuario a la pila de deshacer. Se pueden deshacer varios pasos a la vez.

-   **orientado a la transacción**. La pila de deshacer/rehacer almacena las transacciones de documentos, no las acciones individuales, permitiendo que cada herramienta defina exactamente lo que debe deshacerse o rehacerse.

-   **marco de trabajo [Guión](Scripting/es.md) incorporado**. FreeCAD cuenta con un intérprete [Python](http://www.python.org/) incorporado, con una API que cubre casi cualquier parte de la aplicación, la interfaz, la geometría y la representación de esta geometría en el visor 3D. El intérprete puede ejecutar tanto scripts complejos como comandos individuales; se pueden programar módulos enteros completamente en Python.

-   **Consola de Python incorporada**. El intérprete de Python incluye una consola con resaltado de sintaxis, autocompletado y un navegador de clases. Los comandos de Python pueden ser emitidos directamente en FreeCAD y devolver inmediatamente los resultados, permitiendo a los escritores de scripts probar la funcionalidad sobre la marcha, explorar el contenido de los módulos de FreeCAD y aprender fácilmente sobre los aspectos internos de FreeCAD.

-   **refleja la interacción del usuario**. Todo lo que el usuario hace en la interfaz de FreeCAD ejecuta código Python, que puede imprimirse en la consola y registrarse en macros.

-   Capacidades **completas de grabación y edición de [macro](Macros/es.md)**. Los comandos de Python emitidos cuando el usuario manipula la interfaz pueden ser grabados, editados si es necesario, y guardados para ser reproducidos más tarde.

-   **Formato compuesto (basado en ZIP) para guardar documentos**. Los documentos de FreeCAD se guardan con una extensión **.[FCStd](File_Format_FCStd.md)**. El documento puede contener muchos tipos diferentes de información como geometría, scripts o iconos en miniatura. El archivo **|.FCStd** es en sí mismo un contenedor zip; un archivo FreeCAD guardado ya ha sido comprimido.

-   **Interfaz gráfica de usuario totalmente personalizable/scriptible**. La interfaz basada en [Qt](https://www.qt.io) de FreeCAD es totalmente accesible a través del intérprete de Python. Aparte de las simples funciones que FreeCAD proporciona a los ambientes de trabajo, todo el framework Qt es accesible. El usuario puede realizar cualquier operación en la GUI como crear, añadir, acoplar, modificar o eliminar widgets y barras de herramientas.

-   **miniaturas**. (actualmente sólo en sistemas Linux) Los iconos de los documentos de FreeCAD muestran el contenido del archivo en la mayoría de las aplicaciones de gestión de archivos, como el Nautilus de Gnome.

-   **Instalador MSI modular**. El instalador de FreeCAD permite instalaciones flexibles en sistemas Windows. También se soportan paquetes para sistemas Ubuntu.

## Extra Workbenches 

Usuarios talentosos han creado varios [Ambiente de trabajo externos](external_workbenches/es.md) personalizados.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/es
