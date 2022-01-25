# Render project/es
**(2020) This page refers to an attempt to update the [Raytracing Workbench](Raytracing_Workbench.md), proposed around 2012. Its original author never completed the implementation so this information is outdated, and should not be considered current.

New development is happening in the [https://github.com/FreeCAD/FreeCAD-render Render Workbench], a complete Python replacement for the [Raytracing Workbench](Raytracing_Workbench.md).

Despite this page mentioning the "Render module", this is not the same project as the new [https://github.com/FreeCAD/FreeCAD-render Render Workbench].
**

## Overview


{{TOCright}}


<div class="mw-translate-fuzzy">

## Módulo de Render 

El módulo de render proporciona un modo sencillo y conciso para realizar trabajos de renderizado de las piezas de FreeCAD. Su filosofía está basada en un sistema de plantillas de modo que puedas ver tu trabajo de un modo más eficiente. El módulo de Render trata de ocultar el complicado proceso de renderizado al usuario, de modo que sólo tengas que preocuparte del diseño de las piezas.


</div>

El módulo de render está diseñado para trabajar con múltiples motores de renderizado, pero actualmente sólo está soportado LuxRender. El progreso del trabajo es el siguiente:

-   Crear una operación de render.
-   Seleccionar los parámetros y plantillas deseados
-   Asignar materiales a las piezas visibles en tu documento
-   Situar tu cámara
-   Previsualizar el renderizado

Una breve explicaciónde las partes en el módulo de Render:

### Operación de Render 

La operación de Render contiene la información que será pasada al programa de Render como la configuración de la cámara y del renderizado, y materiales además del plugin de renderizado a utlizar. Esto quiere decir que puedes crear diversas operaciones de renderizado diferentes con diferentes materiales, configuraciones de cámara que sean independientes unas de las otras. La operación también toma control sobre el proceso de renderizado.

### Material de Renderizado 

Cada material de renderizado está basado en una biblioteca de materiales que está almacenada en archivos .XML independientes. Dichos materiales de renderizado pueden tener asignadas propiedades como el color o brillo y otros parámetros. Dichos materiales se adjuntan a un objeto en el documento.





**Para utilizar el entorno de Render, actualmente deberías ser capaz de compilarlo desde la rama de los desrrolladores.**


<div class="mw-translate-fuzzy">

### Utilizando el módulo de Render: 

Primero comprueba el siguiente repositorio <https://github.com/mrlukeparry/freecad/tree/render> y comprueba el ramal de \'render\'. Después asegúrate de poder construirlo.


</div>

Descarga o instala la última versión 1.03 de Lux Render para tu sistema operativo desde <http://www.luxrender.net/en_GB/download> y asegúrate de que funciona correctamente.


<div class="mw-translate-fuzzy">

Abre FreeCAD e inicia el entorno de Raytracing. Debes establecer la \'Ruta del ejecutable\' para Lux Render. Esto se puede hacer en Editar-\>Preferencias-\>Raytracing. Debe establecerse la ruta del ejectable de luxconsole.


</div>

![](images/luxRenderExecPath.png )

Crea tus piezas con FreeCAD. Después vuelve al entorno de Raytracing crea una \'operación de Render\'. Editando esta operación se mostrará una nueva vista de tareas:

![](images/renderTaskView.png )

Cuando creas una operación de Render almacenará la posición actual y el tipo de cámara utilizada en tu vista 3D. Puedes libremente reubicarla y pulsar \'Guardar cámara\' para guardar el estado actual de a cámara en laoperación.

Puedes establecer otros preajustes de render:

#### Preajustes de Render 

Los preajustes de Render se especifican al plugin de renderizado que se está utilizando. Cambian el proceso de render para mejorar la calidad del resultado o la velocidad a la que dicho resultado es generado. Con Lux Render, \'MLT Unbiased\' produce resultados de buena calidad en un tiempo razonable. \'Direct Lighting Preview\' produce un resultado más rápido pero de por calidad.

#### Plantilla de Render 

Las plantillas de Render son actualmente específicas del plugin de render. Mediante la selección de una plantilla, se generarán una escena predefinida en cuanto a iluminación, geometría con tus piezas. Actualmente \'Lux Classic\' trabaja correctamente y produce resultados satisfactorios. Intenta calcular la escena basada en tu posición de cámara y el tamaño completo de las piezas visibles.

### Iniciar un renderizado 

Una vez se han establecido los parámetros de la operación, puedes renderizar la escena. Por ejemplo, esta es la escena de ejemplo. Cualquier parte que no sea visible en el documento no será incluida en el renderizado.

![](images/Example.png )

El botón de la \'Ventana de Previsualización\' renderiza la vista actual de la ventana 3D. El botón de \'Previsualización\' utilizará la posición de la cámara guardada y también el tamaño del resultado. Sólo se puede ejecutar una previsualización a la vez por operación de render, pero puedes ejecutar varios procesos de renderizado de varias operaciones de render distintas.

![](images/renderButtons.png )

Después de iniciar un renderizado. Aparecerá una nueva ventana de previsualización. Dependiendo de la complejidad de tu escena, puede llevar unos segundos mientras se exporta y carga por el programa de render externo. Se mostrará una pantalla de carga.

![](images/loading.png )

Si el proceso de renderizado es satisfactorio, el resultado se mostrará automáticamente. Puedes mover libremente la imagen y hacer un zoom en ella.

![](images/sceneOutput.png )

### Renderizados imparciales 

Esencialmente el programa de render simulará rayos de luz \'rebotando\' a través de una escena. Cuando esta luz golpea a una cámara será visible en el resultado. A medida que más rayos golpean la cámara la imagen se va construyendo. Al principio la imagen parecerá distorsionada cuando la luz no alcanza a la cámara.

Cuando estés satisfecho con el resultado, presiona \'Detener renderizado\'. Podrás entonces guardar el resultado a la ubicación deseada (actualmente se almacena en formato .png)

![](images/unbiasedRendering.png )

#### Velocidad de renderizado 

Los procesos de renderizado son típicamente ejecutados por la CPU. El tiempo tomado para obtener un resultado satisfactorio depende del tamaño del resultado, de la escena, del número y complejidad de materiales utilizados, las luces y el rendimiento global del sistema. Una simple previsualización para una pieza simple puede llevar un minuto, mientras que un resultado de calidad alta puede llevar varias horas.

### Adjuntando materiales 

Asegúrate de estar en modo de edición para la operación de Render. Pulsa Añadir material en la barra de herramientas. Una lista de bibliotecas de materiales se mostrará en la vista de tareas. Puedes a través de ellas arrastrando la lista o utilizando la rueda del ratón.

![](images/materialSelection.png )

Para adjuntar un material a una pieza en tu documento, arrastra el icono del material y suéltalo sobre la pieza en la vista 3D.

![](images/materialDragNDrop.png )

Cuando estés satisfecho con la configuración de las propiedades, pulsa \'Guardar\'.

![](images/materialProperties.png )

When you\'re happy setting the properties, click \'Save\'.

Todos los materiales dentro de la operación de render se mostrarán en el listado de la vista. Estos se pueden seleccionar y borrar o si el material tiene propiedades se puede editar haciendo doble clic sobre el.

![](images/materialListView.png )

## Links

See also [Raytracing tutorial](Raytracing_tutorial.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Render](Category_Render.md) > Render project/es
