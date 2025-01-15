# <img alt="Icono del entorno de trabajo Render" src=images/Render_workbench_icon.svg  style="width:64px;"> Render Workbench/es






## Introducción

El entorno de trabajo Render le permite producir imágenes de alta calidad a partir de modelos FreeCAD, utilizando motores de renderizado externos de código abierto.

Image:Pabellon_de_Barcelona.png\|Pabellón de Barcelona
Captura de pantalla Image:Pabellon_de_Barcelona_Pov_large.png\|Pabellón de Barcelona
Renderizado con Povray Image:Pabellon_de_Barcelona_Cycles.png\|Pabellón de Barcelona
Cycles rendering Image:Asm_V4.png\|Asm V4
Captura de pantalla Image:Asm_V4_lux.png\|Asm V4
Renderizado con LuxCore Image:Asm_V4_ospray2.png\|Asm V4
Renderizado con Ospray Image:Church_of_the_light.png\|Iglesia de la luz
Captura de pantalla Image:Church_of_the_light_lux2.png\|Iglesia de la luz
LuxCore rendering Image:Church_of_the_light_cycles.png\|Iglesia de la luz
Renderizado con Cycles Image:Car.png\|Carro
Captura de pantalla Image:Car_ospray.png\|Carro
Renderizado con Ospray Image:Car_lux.png\|Carro
Renderizado con LuxCore Image:Brick_assembly.png\|Ensamblaje de ladrillos
Captura de pantalla Image:Brick_assembly_appleseed.png\|Ensamblaje de ladrillos
Renderizado con Appleseed Image:Brick_assembly_luxcore.png\|Ensamblaje de ladrillos
Renderizado con Luxcore Image:VillaSavoye.png\|Villa Savoye
Captura de pantalla Image:VillaSavoye appleseed.png\|Villa Savoye
Renderizado con Appleseed Image:VillaSavoye Cycles.png\|Villa Savoye
Renderizado con Cycles

Render, un entorno de trabajo puro de Python, se integra perfectamente en FreeCAD: toda la escena de renderizado (objetos, iluminación, materiales, cámara, etc.) se puede describir con objetos de FreeCAD para exportarlos a renderizadores externos.

En comparación con otros enfoques basados ​​en aplicaciones de gráficos por computadora de terceros, Render tiene como objetivo:

-   Evitar que el usuario aprenda otro software de gráficos 3D/por computadora: todo lo que necesita saber está en FreeCAD.
-   Simplificar el flujo de trabajo de renderizado y liberar al usuario de cualquier manipulación de archivos intermediarios, como de importación, exportación, retoque de escenas, etc.
-   Hacer que la configuración de la escena sea persistente y, especialmente, evitar el retrabajo en una herramienta externa cada vez que se modifica el modelo.



## Renderizadores soportados 

Actualmente se admiten seis motores de renderizado:

-   LuxCoreRender
-   Appleseed
-   Cycles (versión standalone)
-   Pov-Ray
-   Intel Ospray Studio
-   Pbrt-v4 (experimental)



## Uso

En el modo de inicio rápido, una vez realizada correctamente la instalación del banco de trabajo, renderizar un modelo FreeCAD es solo un proceso de 4 pasos:

1.  **Cree un proyecto de renderizado:** Presione el botón en la barra de herramientas correspondiente a su renderizador y seleccione una plantilla adecuada para su renderizador (puede comenzar con un estilo de \'estudio\', como **appleseed_studio_light.appleseed**, **cycles_studio_light.xml**, **luxcore_studio_light.cfg**, **povray_studio_light.pov**, etc.).
2.  **Agregue vistas de sus objetos de su proyecto de renderizado:** Seleccione tanto los objetos como el proyecto y presione el botón **Agregar vista**.
3.  **Establece tu punto de vista:** [Navegue en la vista 3D](Manual_Navigating_in_the_3D_view.md) a la posición deseada y cambie al modo [perspectiva](Std_PerspectiveCamera.md).
4.  **Renderice:** Seleccione su proyecto y presione el botón **Renderizar** en la barra de herramientas (también disponible en el menú contextual del proyecto).

**Y debería obtener una primera representación de su modelo.**

Puede encontrar más instrucciones en el [repositorio de GitHub](https://github.com/FreeCAD/FreeCAD-render) o en la ayuda en línea.



## Características

Las características incluyen, entre otras:

-   Iluminación: luces puntuales, áreas de luz, sol-cielo y plantillas de iluminación preestablecidas.
-   Cámaras.
-   Gestión de materiales (utilizando sombreadores habituales: mate, brillante, vidrio, etc.), incluyendo las texturas.
-   Modo por lotes/modo UI.
-   Eliminador de ruido.
-   Condición de parada (muestra por píxel).
-   Control de mallado: deflexiones angulares y lineales, auto-alisado.



## Enlaces

¿Desea más información? Simplemente siga el enlace: <https://github.com/FreeCAD/FreeCAD-render>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > [External Workbenches](Category_External%20Workbenches.md) > Render Workbench/es
