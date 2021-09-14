# Release notes 0.12/es

Este es un resumen de los cambios más interesantes en FreeCAD desde la anterior versión. Mira [aquí](http://www.freecadweb.org/tracker/changelog_page.php) para ver la lista completa de cambios.

Versiones anteriores: [0.11](Release_notes_0.11/es.md)

### Bienvenida!

-   Cuando abres FreeCAD por primera vez, te da la bienvenida un flamante centro de inicio, que recopila las acciones más habituales que podrías desear hacer, como abrir un entorno especifico, cargar uno de los archivos recientes en los que has trabajado, leer las últimas novedades del desarrollo de FreeCAD, o ver uno de los numerosos vídeotutoriales que la comunidad de FreeCAD ha estado creando recientemente.

![](images/FreeCAD_start_center.jpg )

### Croquizador & Diseño de Piezas 

<img alt="" src=images/Rim_bling.png  style="width:800px;">

-   El [Croquizador](Sketcher_Workbench/es.md) ha recibido una importante cantidad de trabajo desde la versión anterior, y ahora está basado en un nuevo solucionador diseñado desde cero para la tarea. El Croquizador ahora es capaz de realizar casi todas las operaciones 2D del módulo de [Boceto](Draft_Workbench/es.md), y situar un amplio rango de restricciones en los elementos del croquis.

-   Además, el [Entorno de Diseño de Pieza](PartDesign_Workbench/es.md) también ha avanzado mucho y ofrece diversas herramientas comunes (y totalmente paramétricas) para trabajar sobre los croquis, como extrusiones, recubrimientos o revoluciones.

### Arquitectura

-   Un nuevo [Módulo de Arquitectura](Arch_Workbench/es.md) forma parte ahora de FreeCAD. Aún está en una etapa inicial de desarrollo, pero ya dispone de un par de objetos de utilidad, como muros y elementos estructurales (columnas y vigas). Estos pueden crearse sobre geometría 2D existente, como líneas, contornos o croquis, especificando un ancho y una altura, o, en caso de los elementos estructurales, a partir de perfiles 2D. También pueden estar basados en sólidos, o incluso otras formas sólidas, como adicciones o sustracciones, permitiendo virtualmente cualquier geometría posible.

![](images/Arch_screenshot.jpg )

-   El módulo de arquitectura también dispone de un importador de [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes), un importador y exportador de [DAE (collada)](http://en.wikipedia.org/wiki/Collada), y un exportador especial de [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file) más ajustado a los modelos arquitectónicos que el estándar.

-   Incluido en el módulo de arquitectura está también una creciente colección de herramientas para facilitar el proceso de trabajo con objetos de malla a partir de otras aplicaciones como [Blender](http://www.blender.org). Los objetos de malla, si están bien modelados, pueden convertirse en formas simples de forma fácil y automática, y luego en objetos paramétricos del módulo de arquitectura.

### Boceto 2D 

![](images/Draft_taskview.jpg )

-   Reclama tu espacio de trabajo! El módulo de Boceto ahora dispone un nuevo modo de UI que utiliza el sistema de Tareas de FreeCAD, que recopila todas las interacciones del usuario en un mismo sitio, recuperando el precioso espacio que ocupaba la barra de herramientas de Boceto. Para activarlo, ve a las preferencias de Boceto y activa el modo de barra de Tareas.

-   La herramienta de Recortar/Extender ahora permite extruir caras individuales de objetos existentes.

-   Diversos nuevos modos de ajuste se han añadido, permitiendo ahora ajustar paralela y perpendicularmente a líneas existentes, y a ubicaciones que estén alineadas con otros segmentos de línea.

-   El módulo de Boceto también dispone una nueva herramienta que crea, dentro del mismo documento, una vista 2D proyectada de cualquier forma 3D.

-   Los objetos de Boceto pueden dibujarse ahora directamente sobre caras existentes. Si no especificas un plano de trabajo, será adaptado temporalmente a la cara subyacente.

-   El módulo de Boceto es capaz ahora de importar curvas Bézier de archivos SVG.


{{languages/es | {{en|Release_notes_0.12}} {{fr|Release_notes_0.12/fr}} {{it|Release_notes_0.12/it}} {{pl|Release_notes_0.12/pl}} {{ru|Release_notes_0.12/ru}} }}

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)
