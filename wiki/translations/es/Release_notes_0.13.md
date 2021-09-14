# Release notes 0.13/es

 Este es un resumen de los cambios más interesantes realizados en FreeCAD desde la última versión. Mira [aquí](http://www.freecadweb.org/tracker/changelog_page.php) para ver una lista completa de los cambios.


<div class="mw-translate-fuzzy">

Versiones anteriores: [0.12](Release_notes_0.12/es.md) - [0.11](Release_notes_0.11/es.md)


</div>

![800px](images/FreeCAD013.jpg)

*modelado en FreeCAD por psicofil*

## General

-   **Preferencias de Color**: ¿Aburrido del aspecto por defecto de FreeCAD con sus antiguas líneas negras sobre formas grises? Ahora se puede editar en las preferencias del usuario (Mostrar-\> Color), junto con otros colores por defecto.
-   **Alineamiento**: Dos formas se pueden alinear entre si con hasta tres puntos con esta herramienta disponible en el menú Editar.

## Módulo de Dibujo 

-   **Operación de Clip**: Un nuevo objeto de [clip](Drawing_Clip/es.md) permite situar vistas de los objetos enlazados dentro de rectángulos en las hojas de dibujo.
-   **Bloques de títulos editables**: Cuando se diseñan [plantillas de dibujo](Drawing_templates/es.md), ahora es posible marcar textos como editables. Dichos textos se convierten directamente en editables en FreeCAD.
-   **Operación Anotaciones**: Un nuevo objeto [Anotación](Drawing_Annotation/es.md), una operación simple para situar rápidamente bloques de texto en una hoja de dibujo.
-   **Vistas ortográficas**: Una nueva herramienta [Vistas ortográficas del dibujo](Drawing_Orthoviews/es.md) facilita la creación de múltiples vistas todas alineadas entre sí, de acuerdo con el sistema de proyección del primer cuadrante o del tercer cuadrante.
-   Algunos errores corregidos ahora permiten imprimir páginas a escala.

## Módulo de Croquizado 

-   **Point Creation**

![](images/Release-0.13-PointTool.png )

Points can now be added and used as a feature within a sketch

-   **Sketch Origin**

![](images/Release-0.13-Origin.png )

User can now use the sketch\'s origin to define geometry as well as the sketch axes.

-   **Tangency and perpendicularity constraints for arcs and circles.**
-   **Constraints with respect to external (projected) geometry.**
-   **Improved counting of the sketch degrees of freedom.**
-   **Symmetry constraint with respect to a symmetry point** (midpoint constraint).

-   **Improved Datum Label and Constraint Visuals:**

![](images/Release-0.13-SketcherDimensions.png )

-   -   Each constraint label (including arrows) will correctly scale to the size of the scene automatically to the 3D viewport
    -   Datum label text for Distance, Distance X, Distance Y and Radius can be freely positioned now with greater control.
    -   Small improvements to overlapping constraint icons and fix freezes.
    -   Datum Label text will reverse when the view is orientated from the opposite side.

-   **Fully constrained Sketches are now highlighted:**

![The sketch color turns from white to green to indicate it is fully constrained. These default colors can be customized.](images/Release-0.13-SketcherFullyConstrained.png )

-   **Rubber band selection:**

![](images/Release-0.13-RubberBandSelection.png )

Geometry (Points, Lines and Curves) may be selected by dragging on the background to create a rectangular selection.

-   **Extended functionality of the polyline tool:** using the m key one can switch between arc and line mode and among free, tangent and perpendicular transitions from the previous segment.

-   **Map sketch to face** is a new tool to map (or remap) an existing sketch to the selected face on a solid. This allows the use of this sketch for features such as Pad and Pocket.

-   **Small Improvements:**
    -   When constructing geometry, tool tip with related information is shown next to cursor.
    -   **Sketch view** which sets the 3D view perpendicular to the sketch plane has now an icon in the Sketcher toolbar.

## Módulo de Boceto 

-   El importador de DXF ahora soporta puntos y directrices

-   **Taskmode**: El modo Vista de tareas del módulo de Boceto está ahora por defecto. No te preocupes, si te gusta la barra de herramientas, aún está disponible en los parámetros de configuración del Boceto.
-   **importador DXF**: El importador DXF ahora soporta puntos (traducidos como [puntos de Boceto](Draft_Point/es.md)) y directrices (traducidas como contornos de Boceto)
-   **Nuevo sistema de ajuste**: El [sistema de ajuste](Draft_Snap/es.md) del módulo de Boceto se ha reescrito casi desde cero. Ahora es mucho más sencillo de extender y utilizar en otros archivos de guión y módulos. tiene ahora una nueva visualización con iconos de ajuste del cursor, y una barra de herramientas que permite activar y desactivar ubicaciones de ajuste o el sistema de ajuste por completo.

![800px](images/013-draft-snap.jpg)

-   **Mejoras en las restricciones**: Cuando introduces puntos 3D, además de la restricción con mayúsculas existente, puedes ahora restringir el movimiento en dirección X, Y o Z presionando las teclas **X**, **Y** o **Z**. Presionándolas de nuevo se desactiva la restricción.
-   **Conversión Boceto \<-\> Croquis**: El entorno de Boceto ahora dispone de una nueva herramienta de conversión [Draft2Sketch](Draft_Draft2Sketch/es.md), que convierte los objetos de Boceto seleccionados (o cualquier forma plana) a croquis, y viceversa.
-   **Herramienta Clonar**: Crea copias de los objetos seleccionados con esta útil herramienta. Cuando el original cambia, los clones se actualizan automáticamente. Los clones se pueden mover, rotar y también tienen una propiedad de escala que te permite cambiar el tamaño de la copia.
-   **Importador SVG**: El importador SVG ahora ofrece un soporte mucho mejor para las curvas Bezier. La definición global de unidades del usuario ahora se respeta y la geometría se escala correctamente a milímetros. Se ha añadido soporte para nuevos elementos como elipses y rectángulos redondeados. El analizador se ha revisado y ahora maneja rutas de Adobe Illustrator.
-   **Redondeo en esquinas**: Varios objetos de Boceto ([Contorno](Draft_Wire/es.md), [Rectángulos](Draft_Rectangle/es.md) y [Polígonos](Draft_Polygon/es.md)) ahora tienen una propiedad **Radio de Redondeo**, que redondea sus esquinas con el valor de radio indicado.

![800px](images/013-draft-fillet.jpg)

-   **Vista de objeto 2D**: La nueva herramienta [Shape2DView](Draft_Shape2DView/es.md) permite rápidamente situar una vista 2D de un objeto seleccionado en el documento. Puedes especificar el vector de proyección.

![800px](images/013-draft-shape2dview.jpg)

## Módulo de Arquitectura 

-   **Integración del Boceto**: Los módulos de Arquitectura y Boceto están ahora fuertemente integrados. Las herramientas de Arquitectura utilizan el sistema de [ajuste del Boceto](Draft_Snap/es.md), y todas las herramientas del Boceto están presentes en el entorno de Arquitectura. En realidad, si quieres, ahora puedes desactivar por completo el módulo de Boceto (Preferencias -\> Boceto -\> Ocultar el entorno de Boceto)
-   **Nueva herramienta Muro**: La herramienta [Muro](Arch_Wall/es.md) se ha mejorado considerablemente, y ahora presenta un modo de dibujo directo, que se activa cuando presionas el botón de Muro sin ningún elemento seleccionado, esto te permite dibujar muros como si dibujases simples líneas. Además, los muros ahora se conectan automáticamente cuando te ajustas a un muro existente.

![800px](images/013-arch-wall.jpg)

!!FUZZY!!\* **Nueva herramienta tejado**: Una nueva herramienta [Tejado](Arch_Roof/es.md) está disponible en el módulo de Arquitectura, que te permite crear rápidamente tejados con pendiente a partir de una cara seleccionada.

-   **Nueva herramienta Ventana**: Las [Ventanas](Arch_Window/es.md) se crean ahora directamente en la parte superior de una forma plana que contiene uno o más contornos, como un rectángulo o un croquis. Si dicha forma fue dibujada directamente sobre una cara de un muro, la ventana cortará una abertura en el muro.
-   **Nuevo sistema de secciones**: Ahora es muy simple crear planos 2D, secciones y elevaciones de tu modelo: Sitúa un objeto [plano de sección](Arch_SectionPlane/es.md), lo orientas del modo que desees, lo editas para incluir los objetos que se deben ver, y ya lo tienes!
-   **Nuevo renderizador sólido**: En adición al renderizador alámbrico 2D basado en OpenCasCADe actualmente utilizado por el [módulo de dibujo](Drawing_Workbench/es.md), el módulo de Arquitectura ahora disponme de un nuevo renderizador 2D, que es capaz de renderizar caras rellenas a una hoja de dibujo SVG, ofreciendo vistas 2D mucho mejores.

![800px](images/013-arch-vrm.jpg)

-   **Importador IFC con [IfcOpenShell](http://www.ifcopenshell.org)**: El módulo de Arquitectura ahora puede utilizar [IfcOpenShell](http://www.ifcopenshell.org) si está instalado en tu sistema. Esto permite importar IFC mucho mejor, y todo el contenido del archivo IFC se garantiza que sea importado.
-   **Nuevos objetos Pisos y Construcciones**: Las Construcciones y los Pisos ahora son grupos, de modo que puedes añadir y eliminar objetos de ellos con un simple arrastrar y soltar desde las vista de árbol.
-   **Nuevo sistema de ejes**: Un nuevo [sistema de ejes](Arch_Axis/es.md) se ha añadido y permite rápidamente disponer de sistemas de ejes complejos. Dichos ejes se pueden añadir a objetos [Estructura](Arch_Structure/es.md), de modo que se propaguen automáticamente sobre los nodos de la rejilla.

![800px](images/013-arch-axes.jpg)

-   **Objetos de Arquitectura a partir de mallas**: Los [Muros](Arch_Wall/es.md) y [Estructuras](Arch_Structure/es.md) se pueden crear ahora directamente a partir de una malla, suponiendo que esté cerrada, sólidos y todas las aristas son [manifold](http://doc.spatial.com/index.php/Manifold_and_Non-manifold_Objects). Esto permite transformaciones muy rápidas de geometría importada de otras aplicaciones como [blender](http://www.blender.org) en objetos de Arquitectura válidos.

## Módulo de Piezas 

-   **Refinar forma** es una nueva utilidad que limpia las caras después de ejecutar algunas operaciones en una forma. Se puede establecer para ejecutarse automáticamente después de las operaciones booleanas en las Preferencias.
-   **Nueva herramienta recubrimiento** puede extruir un conjunto completo de superficies o una forma sólida a través de una serie de croquis u objetos de Boceto.
-   **Nueva herramienta barrido** puede extruir un conjunto completo de superficies o una forma sólida a través de una serie de croquis u objetos de Boceto y una trayectoria (croquis, arista u objeto de Boceto).
-   **Constructor de formas** y **Creación de primitivas** son ahora parte de la barra de herramientas Pieza para tener un acceso más rápido.

## Módulo de Diseño de Piezas 

-   **Saliente** y **Cajera** son ahora más potentes gracias a más parámetros, como extruir hasta el primero / último, hasta la cara, 2 dimensiones, simétrica al plano.
-   **Chaflán** y **Redondeo** se han actualizado: seleccionar una cara ahora está permitido, todas las aristas exteriores e interiores de la cara serán procesados.
-   **Revolución**: una línea constructiva se puede utilizar ahora como eje de revolución.
-   **Nueva herramienta muesca**: corta material de tu sólido revolucionando un croquis.

## Módulo de Diseño Naval 

-   Nuevo módulo de Diseño naval

## Ratón 3D 

-   Se ha añadido soporte para ratones 3D (Spaceball, Space Navigator) en la versión de Windows.
-   Una nueva pestaña **Spaceball Motion** en el letrero de diálogo de personalización permite una ajuste fino del ratón a los parámetros que desees, directamente desde FreeCAD.

## OpenSCAD module 

-   Este nuevo módulo (experimental) proporciona capacidad de importar archivos OpenSCAD en FreeCAD. Este formato de archivo es muy popular en la comunidad RepRap y en el sitio de compartir diseños digitales Thingiverse.
-   OpenSCAD script can be executed from within FreeCAD, by OpenSCAD (if installed on your computer), with the result appearing in your FreeCAD document.
-   For more information see the [OpenSCAD Workbench](OpenSCAD_Workbench.md) page on the FreeCAD wiki

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)
