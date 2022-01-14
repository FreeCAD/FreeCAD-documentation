# Manual:Preparing models for 3D printing/es
{{Manual:TOC/es}}

Uno de los principales usos de FreeCAD es producir objetos del mundo real. Estos pueden ser diseñados en FreeCAD, y luego hacerse realidad de diferentes maneras, como comunicándolos a otras personas que luego los construirán, o, cada vez más frecuentemente, enviándolos directamente a una [impresora 3D](https://en.wikipedia.org/wiki/3D_printing) o a una [fresadora CNC](https://en.wikipedia.org/wiki/Milling_%28machining%29). Este capítulo le mostrará cómo preparar sus modelos para enviarlos a estas máquinas.

Si has sido precavido al modelar, la mayor parte de las dificultades que puedes encontrar al imprimir tu modelo en 3D ya han sido evitadas. Esto implica básicamente:

-   Asegúrate de que tus objetos 3D son *sólidos*. Los objetos del mundo real son sólidos, el modelo 3D debe ser sólido también. Hemos visto en capítulos anteriores que FreeCAD te ayuda mucho en ese aspecto, y que el [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md) te notificará si haces una operación que impide que tu modelo sea sólido. El [Ambiente de Trabajo Pieza](Part_Workbench/es.md) también contiene un <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Comprobar geometría](Part_CheckGeometry/es.md) que es muy útil para comprobar posibles defectos.
-   Asegurarse de las **dimensiones** de sus objetos. Un milímetro será un milímetro en la vida real. Cada dimensión es importante.
-   Controlar la **degradación**. Ningún sistema de impresión 3D o de fresado CNC puede tomar archivos FreeCAD directamente. La mayoría de ellos sólo entienden un lenguaje de máquina llamado [G-Code](https://es.wikipedia.org/wiki/G-code). El G-code tiene docenas de dialectos diferentes, cada máquina o proveedor suele tener el suyo propio. La conversión de tus modelos en G-Code puede ser fácil y automática, pero también puedes hacerlo manualmente, con un control total sobre la salida. En cualquier caso, es inevitable que se produzca alguna pérdida de calidad de tu modelo durante el proceso.

Cuando se imprime en 3D, siempre hay que asegurarse de que esta pérdida de calidad se mantiene por debajo de los requisitos mínimos.

Abajo, supondremos que se cumplen los dos primeros criterios y que, a estas alturas, usted es capaz de producir objetos sólidos con dimensiones correctas. Ahora veremos cómo abordar el tercer punto.

### Exportación a slicers 

Esta es la técnica más utilizada para impresión 3D. El objeto 3D se exporta a otro programa (el slicer) que generará el G-code del objeto, cortándolo en finas capas (de ahí el nombre), que reproducirán los movimientos que hará la impresora 3D. Como muchas de esas impresoras son de fabricación casera, suele haber pequeñas diferencias entre unas y otras. Estos programas suelen ofrecer posibilidades de configuración avanzadas que permiten adaptar la salida exactamente a las características de su impresora 3D.

La impresión 3D real, sin embargo, es un tema demasiado amplio para este manual. Pero veremos cómo exportar y utilizar estos cortadores para comprobar que la salida es correcta.

### Convertir objetos en mallas 

Ninguno de los slicers, en este momento, tomará directamente la geometría sólida como la que producimos en FreeCAD. Así que tendremos que convertir cualquier objeto que queramos imprimir en 3D en una [Malla poligonal](https://es.wikipedia.org/wiki/Malla_poligonal) primero, que el slicer pueda abrir. Afortunadamente, así como convertir una malla en un sólido es una operación complicada, lo contrario, convertir un sólido en una malla, es muy sencillo. Lo único que debemos tener cuidado, es que es aquí donde se producirá la degradación que mencionamos anteriormente. Debemos comprobar que la degradación se mantiene dentro de unos límites aceptables.

Todo el manejo de la malla, en FreeCAD, se hace mediante otro ambiente de trabajo específico, el [Ambiente de trabajo Malla](Mesh_Workbench/es.md). Este ambiente de trabajo contiene, además de las herramientas más importantes que convierten entre objetos Pieza y Malla, varias utilidades destinadas a analizar y reparar mallas. Aunque el trabajo con mallas no es el objetivo de FreeCAD, cuando se trabaja con el modelado 3D, a menudo se necesita tratar con objetos de malla, ya que su uso está muy extendido entre otras aplicaciones. Este ambiente de trabajo te permite manejarlos completamente en FreeCAD.

-   Convirtamos uno de los objetos que hemos modelado en los capítulos anteriores, como la pieza de lego (que puedes descargar desde el final del capítulo anterior).
-   Abre el archivo de FreeCAD que contiene la pieza de lego.
-   Cambia al [Ambiente de trabajo Malla](Mesh_Workbench/es.md)
-   Selecciona el ladrillo lego
-   Selecciona el menú **Mallas → Crear malla desde forma**
-   Se abrirá un panel de tareas con varias opciones. Algunos algoritmos de malla adicionales (Mefisto o Netgen) pueden no estar disponibles, dependiendo de cómo se haya compilado tu versión de FreeCAD. El algoritmo de malla estándar siempre estará presente. Ofrece menos posibilidades que los otros dos, pero es totalmente suficiente para objetos pequeños que se ajustan al tamaño máximo de impresión de una impresora 3D.

![](images/Exercise_meshing_01.jpg )

-   Seleccione el mallado **Estándar**, y deje el valor de la desviación en el valor por defecto de **0,10**. Pulse **Ok**.
-   Se creará un objeto de malla, exactamente encima de nuestro objeto sólido. Oculta el sólido, o mueve uno de los objetos a un lado, para poder comparar ambos.
-   Cambie la propiedad **Vista → Modo de visualización** del nuevo objeto malla a **Líneas planas**, para ver cómo se ha producido la triangulación.
-   Si no estás contento, y crees que el resultado es demasiado grueso, puedes repetir la operación, bajando el valor de la desviación. En el ejemplo de abajo, la malla de la izquierda utiliza el valor por defecto de **0,10**, mientras que la de la derecha utiliza **0,01**:

![](images/Exercise_meshing_02.jpg )

Sin embargo, en la mayoría de los casos, los valores por defecto darán un resultado satisfactorio.

-   Ahora podemos exportar nuestra malla a un formato de malla, como [STL](https://es.wikipedia.org/wiki/STL), que es actualmente el formato más utilizado en la impresión 3D, utilizando el menú **Archivo → Exportar** y eligiendo el formato de archivo STL.

Si no tienes una impresora 3D, suele ser muy fácil encontrar servicios comerciales que imprimen y te envían los objetos impresos por correo. Entre los más famosos están [Shapeways](http://www.shapeways.com/) y [Sculpteo](http://www.sculpteo.com/), pero normalmente encontrarás muchos otros en tu propia ciudad. En todas las ciudades importantes, hoy en día se encuentran [Fablaboratorio](https://es.wikipedia.org/wiki/Fab_lab)s, que son talleres equipados con una serie de máquinas de fabricación en 3D, que casi siempre incluyen al menos una impresora 3D. Los Fab labs suelen ser espacios comunitarios, que te permitirán utilizar sus máquinas, de forma gratuita o de pago, dependiendo del Fab lab, pero también te enseñarán a utilizarlas y promoverán otras actividades en torno a la fabricación 3D.

### Usando Slic3r 

[Slic3r](http://slic3r.org/) es una aplicación que convierte objetos STL en G-code que puede enviarse directamente a las impresoras 3D. Al igual que FreeCAD, es gratuito, de código abierto y funciona en Windows, Mac OS y Linux. Configurar correctamente las cosas para la impresión 3D es un proceso complicado, en el que debes tener un buen conocimiento de tu impresora 3D, por lo que no es muy útil generar el G-code antes de ir a imprimir (tu archivo de G-code podría no funcionar bien en otra impresora), pero de todos modos nos es útil para comprobar que nuestro archivo STL será imprimible sin problemas.

Este es nuestro archivo STL exportado abierto en Slic3r. Usando la pestaña **vista previa**, y moviendo el deslizador de la derecha, podemos visualizar la trayectoria que seguirá el cabezal de la impresora 3D para construir nuestro objeto.

![](images/Exercise_meshing_03.jpg )

### Usando el complemento Cura 

[Cura](https://ultimaker.com/en/products/cura-software) es otra aplicación gratuita y de código abierto para Windows, Mac y Linux, mantenida por el fabricante de impresoras 3D [Ultimaker](https://ultimaker.com). Algunos usuarios de FreeCAD han creado un [Ambiente de trabajo Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin) que utiliza cura internamente. El Ambiente de trabajo Cura está disponible en el repositorio [FreeCAD complementos](https://github.com/FreeCAD/FreeCAD-addons). Para utilizar el Ambiente de trabajo Cura, también necesitas instalar el propio Cura, que no está incluido en el ambiente de trabajo.

Una vez que hayas instalado tanto Cura como el Ambiente de trabajo Cura, podrás utilizarlo para producir el archivo de G-code directamente desde los objetos de la pieza, sin necesidad de convertirlos en mallas, y sin necesidad de abrir una aplicación externa. La producción de otro archivo de G-code a partir de nuestro ladrillo Lego, utilizando esta vez el Ambiente de trabajo Cura, se realiza de la siguiente manera:

-   Cargar el archivo que contiene nuestro ladrillo Lego (se puede descargar al final del capítulo anterior)
-   Pasar al [Ambiente de trabajo Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Configurar el espacio de la impresora eligiendo el menú **Impresión 3D → Crear una definición de impresora 3D**. Como no vamos a imprimir de verdad, podemos dejar los ajustes como están. La geometría de la cama de impresión y el espacio disponible se mostrarán en la vista 3D.
-   Mueve el ladrillo Lego a un lugar adecuado, como el centro de la cama de impresión. Recuerda que los objetos de DiseñoPieza no se pueden mover directamente, por lo que tienes que mover su primer boceto (el primer rectángulo), o mover (e imprimir) una copia, que se puede hacer con la herramienta [Pieza → Crear una copia simple](Part_SimpleCopy/es.md). La copia se puede mover, por ejemplo con <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Borrador → Mover](Draft_Move/es.md).
-   Seleccionar el objeto a imprimir, y seleccionar el menú **Impresión 3D → Cortar con Cura Engine**.
-   En el panel de tareas que se abrirá, asegúrate de que la ruta del ejecutable de Cura está correctamente configurada. Como no vamos a imprimir realmente, podemos dejar el resto de opciones como están. Pulse **Ok**\'. Se generarán dos archivos en el mismo directorio que tu archivo de FreeCAD, un archivo STL y un archivo G-code.

![](images/Exercise_meshing_05.jpg )

-   El G-code generado también puede ser reimportado a FreeCAD (usando el preprocesador slic3r) para su comprobación.

### Generación de G-code 


**'''Aviso:''' Esta sección fue hecha para FreeCAD 0.16. Se han hecho cambios significativos en la creación de trayectorias. Por favor, consulta la documentación del [Ambiente de trabajo trayectorias](Path_Workbench/es.md) en general o el tutorial como [caminar trayectorias](Path_Walkthrough_for_the_Impatient/es.md)!**

FreeCAD también ofrece formas más avanzadas de generar G-code directamente. Esto es a menudo mucho más complicado que el uso de herramientas automáticas como vimos anteriormente, pero tiene la ventaja de permitirte controlar completamente la salida. Esto no suele ser necesario cuando se utilizan impresoras 3D, pero se vuelve muy importante cuando se trata de fresado CNC, ya que las máquinas son mucho más complejas.

La generación de trayectorias en G-code en FreeCAD se realiza con el [Ambiente de trabajo trayectoria](Path_Workbench/es.md). Cuenta con herramientas que generan trayectorias de máquina completas y otras que generan sólo partes de un proyecto de G-code, que luego pueden ser ensambladas para formar una operación de fresado completa.

La generación de trayectorias de fresado CNC es otro tema demasiado extenso para que quepa en este manual, por lo que vamos a mostrar cómo construir un proyecto sencillo de trayectorias, sin preocuparnos mucho de la mayoría de los detalles del mecanizado CNC real.

-   Cargue el archivo que contiene nuestra pieza de lego, y cambie al [Ambiente de trabajobtrayectoria](Path_Workbench/es.md).
-   Como la pieza final ya no contiene una cara superior rectangular, oculta la pieza final de lego, y muestra el primer pad cúbico que hicimos, que tiene una cara superior rectangular.
-   Selecciona la cara superior y pulsa el <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Perfil](Path_Profile/es.md).
-   Establece su propiedad **Desplazamiento** a 1mm.

![](images/Exercise_path_01.jpg )

-   A continuación, vamos a duplicar este primer bucle un par de veces, para que la herramienta esculpa todo el bloque. Seleccionamos el trazado del Perfil, y pulsamos el botón <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Arreglo](Path_Array/es.md).
-   Ajuste la propiedad **Copias** de l\'arreglo a 8, y su **Desplazamiento**\' a -2mm en la dirección Z, y mueva la colocación de l\'arreglo 2mm en la dirección Z, para que el corte comience un poco por encima de la almohadilla, e incluya también la altura de los puntos.

![](images/Exercise_path_02.jpg )

-   Ahora hemos definido una trayectoria que, al ser seguida por la fresadora, tallará un volumen rectangular de un bloque de material. Ahora tenemos que tallar el espacio entre los puntos, para revelarlos. Oculta el Pastilla, y vuelve a mostrar la pieza final, para que podamos seleccionar la cara que se encuentra entre los puntos.
-   Selecciona la cara superior, y pulsa el <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Forma de bolsillo](Path_Pocket_Shape/es.md). Ajuste la propiedad **Desplazamiento** a 1mm, y la **altura de retracción**\' a 20mm. Esa es la altura a la que se desplazará el cortador cuando cambie de un bucle a otro. De lo contrario, el cortador podría cortar uno de nuestros puntos:

![](images/Exercise_path_03.jpg )

-   Una vez más, haz un arreglo. Selecciona el objeto cavidad, y presiona el botón <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Arreglo](Path_Array/es.md). Ajuste el número de **Copias** a 1 y el **Desplazamiento**\' a -2mm en la dirección Z. Mueve la colocación del Arreglo en 2mm en la dirección Z. Nuestras dos operaciones están ahora hechas:

![](images/Exercise_path_04.jpg )

-   Ahora sólo queda unir estas dos operaciones en una. Esto se puede hacer con un [Trayectoria Pedido](Path_Job/es.md). Pulse el botón <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Pedido](Path_Job/es.md).
-   Poner la propiedad **Utilizar Colocaciones** del proyecto en True, porque hemos cambiado la colocación de las matrices, y queremos que eso se tenga en cuenta en el proyecto.
-   En la vista de árbol, arrastre y suelte las dos matrices en el proyecto. Puedes reordenar las matrices dentro del proyecto si es necesario, haciendo doble clic.
-   El proyecto puede ahora ser exportado a G-code, seleccionándolo, eligiendo el menú **Archivo -\> Exportar**, seleccionando el formato G-code, y en el diálogo emergente que se abrirá, seleccionando un script de post-procesamiento de acuerdo a su máquina.

Hay muchas aplicaciones disponibles para simular el corte real, una de ellas que también es multiplataforma y de código abierto, como FreeCAD, es [Camotics](http://camotics.org/).

**Descargas**\'

-   El archivo STL generado en este ejercicio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   El archivo generado en este ejercicio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   El archivo de G-code generado en este ejercicio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Leer más**

-   [Ambiente de trabajo Malla](Mesh_Workbench/es.md)
-   [El formato de archivo STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [Ambiente de trabajo Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [Ambiente de trabajo Trayectoria](Path_Workbench/es.md)
-   [Camotics](http://camotics.org/)

### Videos

-   [Cómo usar FreeCAD para la impresión 3D \| Usando la rama Realthunder](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN). Una lista de reproducción de vídeos de Maker Tales sobre cómo utilizar FreeCAD para la impresión 3D.




[<img src="images/Property.png" style="width:16px"> Path](Category_Path.md) [<img src="images/Property.png" style="width:16px"> Mesh](Category_Mesh.md) [<img src="images/Property.png" style="width:16px"> Tutorials](Category_Tutorials.md)

---
[documentation index](../README.md) > [Path](Category_Path.md) > Manual:Preparing models for 3D printing/es
