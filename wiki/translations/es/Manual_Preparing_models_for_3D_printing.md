# Manual:Preparing models for 3D printing/es
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Uno de los principales usos de FreeCAD es producir objetos del mundo real. Estos pueden ser diseñados en FreeCAD, y luego hacerse realidad de diferentes maneras, como comunicándolos a otras personas que luego los construirán, o, cada vez más frecuentemente, enviándolos directamente a una [impresora 3D](https://en.wikipedia.org/wiki/3D_printing) o a una [fresadora CNC](https://en.wikipedia.org/wiki/Milling_%28machining%29). Este capítulo le mostrará cómo preparar sus modelos para enviarlos a estas máquinas.


</div>


<div class="mw-translate-fuzzy">

Si has sido precavido al modelar, la mayor parte de las dificultades que puedes encontrar al imprimir tu modelo en 3D ya han sido evitadas. Esto implica básicamente:


</div>


<div class="mw-translate-fuzzy">

-   Asegúrate de que tus objetos 3D son *sólidos*. Los objetos del mundo real son sólidos, el modelo 3D debe ser sólido también. Hemos visto en capítulos anteriores que FreeCAD te ayuda mucho en ese aspecto, y que el [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md) te notificará si haces una operación que impide que tu modelo sea sólido. El [Ambiente de Trabajo Pieza](Part_Workbench/es.md) también contiene un <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Comprobar geometría](Part_CheckGeometry/es.md) que es muy útil para comprobar posibles defectos.
-   Asegurarse de las **dimensiones** de sus objetos. Un milímetro será un milímetro en la vida real. Cada dimensión es importante.
-   Controlar la **degradación**. Ningún sistema de impresión 3D o de fresado CNC puede tomar archivos FreeCAD directamente. La mayoría de ellos sólo entienden un lenguaje de máquina llamado [G-Code](https://es.wikipedia.org/wiki/G-code). El G-code tiene docenas de dialectos diferentes, cada máquina o proveedor suele tener el suyo propio. La conversión de tus modelos en G-Code puede ser fácil y automática, pero también puedes hacerlo manualmente, con un control total sobre la salida. En cualquier caso, es inevitable que se produzca alguna pérdida de calidad de tu modelo durante el proceso.

Cuando se imprime en 3D, siempre hay que asegurarse de que esta pérdida de calidad se mantiene por debajo de los requisitos mínimos.


</div>

-   **Confirming the Accuracy of Dimensions**: Precision is critical---what you design in FreeCAD will translate directly to real-world measurements. A millimeter in FreeCAD is a millimeter in the physical object, so each dimension must be carefully considered and verified to ensure accuracy.

-   **Managing Degradation**: It\'s important to remember that no 3D printer or CNC mill can directly process FreeCAD files. These machines use G-Code, a machine language with various dialects depending on the machine or vendor. The process of converting your model into G-Code can often be done automatically through slicer software, but you also have the option to do it manually for greater control. However, during this conversion, some loss of detail or quality is inevitable, particularly when converting the model to a mesh format for printing. You must ensure that this degradation remains within acceptable limits and doesn't affect the functionality or appearance of your final object.

-   **Export Format Compatibility**: For 3D printing, STL is the most commonly used format, but it inherently converts your model into a mesh of triangles, which can result in some loss of detail. It's essential to choose the right resolution when exporting to STL, balancing between detail retention and file size. Similarly, for CNC machining, formats like STEP or IGES are preferable as they maintain the original geometric integrity of the design better than STL. Choosing the right format ensures that the conversion to G-Code remains accurate.

-   **Mesh Analysis and Calibration**: Before exporting your model to a slicer or CNC toolpath generator, it's advisable to run a mesh analysis using FreeCAD's [Mesh Workbench](Mesh_Workbench.md) to detect irregularities, non-manifold edges, or other mesh issues that might complicate the manufacturing process. Additionally, even with a perfect model, make sure your 3D printer or CNC machine is properly calibrated (e.g., for bed leveling, stepper motor settings, or extruder configuration) to avoid quality problems in the final product.

In the following sections, we\'ll assume that you\'ve already taken care of creating solid models with the correct dimensions. Our focus will now shift to managing the conversion process to G-Code, ensuring that your model maintains the necessary quality for 3D printing or CNC machining. By addressing these considerations, you\'ll be better equipped to produce successful physical objects directly from your FreeCAD models.



### Exportación a slicers 


<div class="mw-translate-fuzzy">

Esta es la técnica más utilizada para impresión 3D. El objeto 3D se exporta a otro programa (el slicer) que generará el G-code del objeto, cortándolo en finas capas (de ahí el nombre), que reproducirán los movimientos que hará la impresora 3D. Como muchas de esas impresoras son de fabricación casera, suele haber pequeñas diferencias entre unas y otras. Estos programas suelen ofrecer posibilidades de configuración avanzadas que permiten adaptar la salida exactamente a las características de su impresora 3D.


</div>


<div class="mw-translate-fuzzy">

La impresión 3D real, sin embargo, es un tema demasiado amplio para este manual. Pero veremos cómo exportar y utilizar estos cortadores para comprobar que la salida es correcta.


</div>

Slicers often include additional insights, such as estimating print time, material usage, and cost based on the filament or resin being used. This allows you to make informed decisions about the printing process and tweak settings for efficiency or material conservation. Although the deeper intricacies of 3D printing---such as machine calibration, material selection, and post-processing---are beyond the scope of this guide, we will focus on how to properly export your FreeCAD model and use slicer software to ensure the output is correct and optimized for your specific printer



### Convertir objetos en mallas 


<div class="mw-translate-fuzzy">

Ninguno de los slicers, en este momento, tomará directamente la geometría sólida como la que producimos en FreeCAD. Así que tendremos que convertir cualquier objeto que queramos imprimir en 3D en una [Malla poligonal](https://es.wikipedia.org/wiki/Malla_poligonal) primero, que el slicer pueda abrir. Afortunadamente, así como convertir una malla en un sólido es una operación complicada, lo contrario, convertir un sólido en una malla, es muy sencillo. Lo único que debemos tener cuidado, es que es aquí donde se producirá la degradación que mencionamos anteriormente. Debemos comprobar que la degradación se mantiene dentro de unos límites aceptables.


</div>


<div class="mw-translate-fuzzy">

Todo el manejo de la malla, en FreeCAD, se hace mediante otro ambiente de trabajo específico, el [Ambiente de trabajo Malla](Mesh_Workbench/es.md). Este ambiente de trabajo contiene, además de las herramientas más importantes que convierten entre objetos Pieza y Malla, varias utilidades destinadas a analizar y reparar mallas. Aunque el trabajo con mallas no es el objetivo de FreeCAD, cuando se trabaja con el modelado 3D, a menudo se necesita tratar con objetos de malla, ya que su uso está muy extendido entre otras aplicaciones. Este ambiente de trabajo te permite manejarlos completamente en FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   Convirtamos uno de los objetos que hemos modelado en los capítulos anteriores, como la pieza de lego (que puedes descargar desde el final del capítulo anterior).
-   Abre el archivo de FreeCAD que contiene la pieza de lego.
-   Cambia al [Ambiente de trabajo Malla](Mesh_Workbench/es.md)
-   Selecciona el ladrillo lego
-   Selecciona el menú **Mallas → Crear malla desde forma**
-   Se abrirá un panel de tareas con varias opciones. Algunos algoritmos de malla adicionales (Mefisto o Netgen) pueden no estar disponibles, dependiendo de cómo se haya compilado tu versión de FreeCAD. El algoritmo de malla estándar siempre estará presente. Ofrece menos posibilidades que los otros dos, pero es totalmente suficiente para objetos pequeños que se ajustan al tamaño máximo de impresión de una impresora 3D.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_meshing_01.jpg )


</div>

-   Let\'s convert the Lego piece we created in the last chapter into an STL mesh. The geometry can be downloaded at the end of said chapter.
-   Open the FreeCAD file containing the Lego piece.
-   Switch to the [Mesh Workbench](Mesh_Workbench.md)
-   Select the Lego brick
-   Select menu **Meshes → Create Mesh from Shape**
-   A task panel will open with several options. Some additional meshing algorithms (Mefisto or Netgen) might not be available, depending on how your version of FreeCAD was compiled. The Standard meshing algorithm will always be present. It offers fewer possibilities than the two others, but is totally sufficient for small objects that fit into the maximum print size of a 3D printer.

![](images/FreeCAD_MeshLego.png )


<div class="mw-translate-fuzzy">

-   Seleccione el mallado **Estándar**, y deje el valor de la desviación en el valor por defecto de **0,10**. Pulse **Ok**.
-   Se creará un objeto de malla, exactamente encima de nuestro objeto sólido. Oculta el sólido, o mueve uno de los objetos a un lado, para poder comparar ambos.
-   Cambie la propiedad **Vista → Modo de visualización** del nuevo objeto malla a **Líneas planas**, para ver cómo se ha producido la triangulación.
-   Si no estás contento, y crees que el resultado es demasiado grueso, puedes repetir la operación, bajando el valor de la desviación. En el ejemplo de abajo, la malla de la izquierda utiliza el valor por defecto de **0,10**, mientras que la de la derecha utiliza **0,01**:


</div>

![](images/Exercise_meshing_02.jpg )

Sin embargo, en la mayoría de los casos, los valores por defecto darán un resultado satisfactorio.

-   Ahora podemos exportar nuestra malla a un formato de malla, como [STL](https://es.wikipedia.org/wiki/STL), que es actualmente el formato más utilizado en la impresión 3D, utilizando el menú **Archivo → Exportar** y eligiendo el formato de archivo STL.


<div class="mw-translate-fuzzy">

Si no tienes una impresora 3D, suele ser muy fácil encontrar servicios comerciales que imprimen y te envían los objetos impresos por correo. Entre los más famosos están [Shapeways](http://www.shapeways.com/) y [Sculpteo](http://www.sculpteo.com/), pero normalmente encontrarás muchos otros en tu propia ciudad. En todas las ciudades importantes, hoy en día se encuentran [Fablaboratorio](https://es.wikipedia.org/wiki/Fab_lab)s, que son talleres equipados con una serie de máquinas de fabricación en 3D, que casi siempre incluyen al menos una impresora 3D. Los Fab labs suelen ser espacios comunitarios, que te permitirán utilizar sus máquinas, de forma gratuita o de pago, dependiendo del Fab lab, pero también te enseñarán a utilizarlas y promoverán otras actividades en torno a la fabricación 3D.


</div>




<div class="mw-translate-fuzzy">

### Usando Slic3r 


</div>


<div class="mw-translate-fuzzy">

[Slic3r](http://slic3r.org/) es una aplicación que convierte objetos STL en G-code que puede enviarse directamente a las impresoras 3D. Al igual que FreeCAD, es gratuito, de código abierto y funciona en Windows, Mac OS y Linux. Configurar correctamente las cosas para la impresión 3D es un proceso complicado, en el que debes tener un buen conocimiento de tu impresora 3D, por lo que no es muy útil generar el G-code antes de ir a imprimir (tu archivo de G-code podría no funcionar bien en otra impresora), pero de todos modos nos es útil para comprobar que nuestro archivo STL será imprimible sin problemas.


</div>


<div class="mw-translate-fuzzy">

Este es nuestro archivo STL exportado abierto en Slic3r. Usando la pestaña **vista previa**, y moviendo el deslizador de la derecha, podemos visualizar la trayectoria que seguirá el cabezal de la impresora 3D para construir nuestro objeto.


</div>

This is our exported STL file opened in PrusaSlicer. By just pressing on the **slice** button, the software divides your model into layers, generates the toolpaths for the 3D printer, and applies the necessary speed and temperature settings. It calculates the infill, support structures, and perimeters, then creates the G-code, which contains detailed instructions for the printer. You can preview the sliced model layer by layer, check estimated print time and filament usage, and finally save or send the G-code to your printer for the actual printing process.


<div class="mw-translate-fuzzy">

![](images/Exercise_meshing_03.jpg )


</div>


<div class="mw-translate-fuzzy">

[Cura](https://ultimaker.com/en/products/cura-software) es otra aplicación gratuita y de código abierto para Windows, Mac y Linux, mantenida por el fabricante de impresoras 3D [Ultimaker](https://ultimaker.com). Algunos usuarios de FreeCAD han creado un [Ambiente de trabajo Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin) que utiliza cura internamente. El Ambiente de trabajo Cura está disponible en el repositorio [FreeCAD complementos](https://github.com/FreeCAD/FreeCAD-addons). Para utilizar el Ambiente de trabajo Cura, también necesitas instalar el propio Cura, que no está incluido en el ambiente de trabajo.


</div>

### Generating G-code 


<div class="mw-translate-fuzzy">

FreeCAD también ofrece formas más avanzadas de generar G-code directamente. Esto es a menudo mucho más complicado que el uso de herramientas automáticas como vimos anteriormente, pero tiene la ventaja de permitirte controlar completamente la salida. Esto no suele ser necesario cuando se utilizan impresoras 3D, pero se vuelve muy importante cuando se trata de fresado CNC, ya que las máquinas son mucho más complejas.


</div>


<div class="mw-translate-fuzzy">

La generación de trayectorias de fresado CNC es otro tema demasiado extenso para que quepa en este manual, por lo que vamos a mostrar cómo construir un proyecto sencillo de trayectorias, sin preocuparnos mucho de la mayoría de los detalles del mecanizado CNC real.


</div>


<div class="mw-translate-fuzzy">

-   Cargue el archivo que contiene nuestra pieza de lego, y cambie al [Ambiente de trabajobtrayectoria](Path_Workbench/es.md).
-   Como la pieza final ya no contiene una cara superior rectangular, oculta la pieza final de lego, y muestra el primer pad cúbico que hicimos, que tiene una cara superior rectangular.
-   Selecciona la cara superior y pulsa el <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Perfil](Path_Profile/es.md).
-   Establece su propiedad **Desplazamiento** a 1mm.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_path_01.jpg )


</div>

-   Load the file containing our Lego piece, and switch to the <img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [CAM Workbench](CAM_Workbench.md).
-   Press on the <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Job](CAM_Job.md) button and select our lego piece.
-   Since this section doesn't aim to provide an in-depth tutorial of the CAM Workbench, we will be using the default values. If you would like a more detailed tutorial, please refer to [CAM walk-through](CAM_Walkthrough_for_the_Impatient.md). Keep in mind that in the CAM Workbench, a stock body is automatically created around your object, representing the raw material that will be machined. Right now, this stock body extends 1 mm in all directions from the object.

![](images/FreeCAD_CAM1.png )


<div class="mw-translate-fuzzy">

-   A continuación, vamos a duplicar este primer bucle un par de veces, para que la herramienta esculpa todo el bloque. Seleccionamos el trazado del Perfil, y pulsamos el botón <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Arreglo](Path_Array/es.md).
-   Ajuste la propiedad **Copias** de l\'arreglo a 8, y su **Desplazamiento**\' a -2mm en la dirección Z, y mueva la colocación de l\'arreglo 2mm en la dirección Z, para que el corte comience un poco por encima de la almohadilla, e incluya también la altura de los puntos.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_path_02.jpg )


</div>

![](images/FreeCAD_CAMtree.png )


<div class="mw-translate-fuzzy">

-   Ahora hemos definido una trayectoria que, al ser seguida por la fresadora, tallará un volumen rectangular de un bloque de material. Ahora tenemos que tallar el espacio entre los puntos, para revelarlos. Oculta el Pastilla, y vuelve a mostrar la pieza final, para que podamos seleccionar la cara que se encuentra entre los puntos.
-   Selecciona la cara superior, y pulsa el <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Forma de bolsillo](Path_Pocket_Shape/es.md). Ajuste la propiedad **Desplazamiento** a 1mm, y la **altura de retracción**\' a 20mm. Esa es la altura a la que se desplazará el cortador cuando cambie de un bucle a otro. De lo contrario, el cortador podría cortar uno de nuestros puntos:


</div>


<div class="mw-translate-fuzzy">

-   Ahora sólo queda unir estas dos operaciones en una. Esto se puede hacer con un [Trayectoria Pedido](Path_Job/es.md). Pulse el botón <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Pedido](Path_Job/es.md).
-   Poner la propiedad **Utilizar Colocaciones** del proyecto en True, porque hemos cambiado la colocación de las matrices, y queremos que eso se tenga en cuenta en el proyecto.
-   En la vista de árbol, arrastre y suelte las dos matrices en el proyecto. Puedes reordenar las matrices dentro del proyecto si es necesario, haciendo doble clic.
-   El proyecto puede ahora ser exportado a G-code, seleccionándolo, eligiendo el menú **Archivo -\> Exportar**, seleccionando el formato G-code, y en el diálogo emergente que se abrirá, seleccionando un script de post-procesamiento de acuerdo a su máquina.


</div>


<div class="mw-translate-fuzzy">

Hay muchas aplicaciones disponibles para simular el corte real, una de ellas que también es multiplataforma y de código abierto, como FreeCAD, es [Camotics](http://camotics.org/).


</div>


<div class="mw-translate-fuzzy">

**Descargas**\'


</div>


<div class="mw-translate-fuzzy">

-   El archivo STL generado en este ejercicio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   El archivo generado en este ejercicio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   El archivo de G-code generado en este ejercicio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>


</div>


<div class="mw-translate-fuzzy">

**Leer más**


</div>

**Downloads**

-   The STL file generated in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   The file generated during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   The G-code file generated in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Read more**


<div class="mw-translate-fuzzy">

-   [Ambiente de trabajo Malla](Mesh_Workbench/es.md)
-   [El formato de archivo STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [Ambiente de trabajo Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [Ambiente de trabajo Trayectoria](Path_Workbench/es.md)
-   [Camotics](http://camotics.org/)


</div>

### Videos

-   [Cómo usar FreeCAD para la impresión 3D \| Usando la rama Realthunder](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN). Una lista de reproducción de vídeos de Maker Tales sobre cómo utilizar FreeCAD para la impresión 3D.



---
⏵ [documentation index](../README.md) > [CAM](Category_CAM.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/es
