 {{TutorialInfo/es
|Topic= Introduction to modelling
|Level= Beginner
|Time= 15 minutes
|Author=
|FCVersion=
|Files=
}}

## Introduction


<div class="mw-translate-fuzzy">

Este Tutorial de Modelado Básico te mostrará cómo modelar un ángulo de hierro. Una cosa que deberías saber es que FreeCAD es modular según el diseño, y como muchos otros programas de CAD, siempre hay más de un modo de hacer las cosas. Exploraremos dos métodos aquí.


</div>

## Antes de empezar {#antes_de_empezar}

Recuerda que FreeCAD aún está en un estado inicial de desarrollo, así que posiblemente no seas tan productivo como con otras aplicaciones de CAD, y encontrarás algunos errores, o experimentes algunos cuelgues de la aplicación. FreeCAD ahora dispone de la opción de realizar copias de respaldo. El numero de archivos de respaldo se puede especificar en el letrero de diálogo de Preferencias. No dudes en permitir 2 o 3 archivos de respaldo hasta que conozcas bien como trabajar con FreeCAD.

Guarda tu trabajo frecuentemente, de vez en cuando guarda tu trabajo con un nombre diferente, así tendrás una copia \"a salvo\" a la que puedas volver, y prepárate para la posibilidad de que algunos comandos pudieran no ofrecer los resultados que esperabas.


<div class="mw-translate-fuzzy">

## Introducción a las técnicas de modelado {#introducción_a_las_técnicas_de_modelado}

La primera (y básica) técnica de modelado sólido es la [Geometría constructiva de sólidos (CSG)](http://es.wikipedia.org/wiki/Geometr%C3%ADa_constructiva_de_s%C3%B3lidos). Trabajas principalmente con formas primitivas como cubos, cilindros, esferas y conos para construir tu geometría combinándolos, eliminando una forma de otra, o intersecándolas. Estas herramientas son parte del [Entorno de Pieza](Part_Workbench/es.md). También puedes aplicar transformaciones a las formas, como aplicar redondeos o chaflanes en las aristas. Estas herramientas pertenecen también al tools are also in the [Entorno de Pieza](Part_Workbench/es.md).


</div>

Luego existen otras herramientas más avanzadas. Tu empiezas dibujando un perfil 2D que puedas extruir o revolucionar.

Así que vamos a comenzar tratando de hacer un pie de hierro para una mesa con estos 2 métodos.


<div class="mw-translate-fuzzy">

## Primer Método - Por Geometría constructiva de sólidos {#primer_método___por_geometría_constructiva_de_sólidos}

-   Empieza con el [Entorno de Pieza](Part_Workbench/es.md) (Menú **Vista \> Entorno \> Pieza**)
-   Clic en el botón <img alt="" src=images/Part_Box.png  style="width:32px;"> [Cubo](Part_Box.md) para crear un Cubo
-   Cambia sus dimensiones seleccionándolas en el espacio 3D, o pulsando la pestaña Proyecto a la izquierda, luego
-   Pulsa en la pestaña Datos en la parte inferior, y cambia los valores de Alto, largo y ancho a 750mm, 50 y 50 *(ver Fig. 1.1)*
-   Crea un segundo cubo del mismo modo, pero con los valores 750, 40 y 40mm. Por defecto este cubo se superpondrá al primero. *(ver Fig. 1.2)*
-   Ahora resta el segundo cubo al primero. Selecciona el primer cubo primero (denominado Box), luego el segundo cubo (denominado Box001), el orden de la selección es importante! (Asegúrate de que ambas formas están seleccionadas en el árbol de Proyectos. Recuerda: en el modo de navegación de Inventor, Ctrl + click no funciona para la selección múltiple. [Cambia](Mouse_Model/es.md) al modo de navegación CAD o para seleccionar.)
-   En la barra de herramientas del entorno de Pieza, pulsa sobre la herramienta <img alt="" src=images/Part_Cut.png  style="width:32px;"> [Cortar](Part_Cut.md).


</div>

![Fig. 1.1 El primer cubo](images/Tutorial-normand01.jpg )

![Fig. 1.2 El segundo cubo superpuesto sobre el primero, preparado para ser restado](images/Tutorial-normand02.jpg )

![Fig. 1.3 Después de la resta](images/Tutorial-normand03.jpg )


<div class="mw-translate-fuzzy">

Ahora tienes tu primer ángulo de hierro *(Fig. 1.3)*. Te habrás fijado que, en la pestaña de Proyecto a la izquierda, ambos cubos han sido reemplazados por un objeto \"Cut\". En realidad, no han desaparecido, sino que se han agrupado en el objeto Cut. Pulsa en el + en frente de él, y verás que ambos cubos siguen ahí, pero sin resaltar *(Fig. 1.4)*. Si pulsas en cada uno de ellos y pulsas la barra espaciadora, se mostrarán. La barra espaciadora alterna la visibilidad de los objetos seleccionados. *(Fig. 1.5)*


</div>


<div class="mw-translate-fuzzy">

No quieres el ángulo orientado en esa posición? Simplemente necesitas cambiar la ubicación de la forma Box001. Selecciónalo, ocultalo y en la pestaña de Datos, pulsa sobre el + enfrente a Placement, entonces se despliega la ubicación, y cambia sus coordenadas X e Y. Presiona Enter, oculta la forma Box001 de nuevo, y la orientación de tu ángulo es ahora diferente. *(Fig. 1.5)* Incluso puedes cambiar las dimensiones de las formas, y el objeto Cut se actualizará.


</div>

![Fig. 1.4 La operación corte retiene sus objetos originales (los cubos)](images/Tutorial-normand04.jpg )

![Fig. 1.5 Aún puedes hacer visibles los cubos originales](images/Tutorial-normand05.jpg )


<div class="mw-translate-fuzzy">

Por cierto, podemos añadir redondeos al ángulo para que parezca más real, utilizando la herramienta <img alt="" src=images/Part_Fillet.png  style="width:32px;"> [Redondeo](Part_Fillet.md). 
*(Fig. 1.6)*


</div>

![Fig. 1.6 Las aristas redondeadas](images/Tutorial-normand06.jpg )


<div class="mw-translate-fuzzy">

## Segundo método - Extruyendo un croquis {#segundo_método___extruyendo_un_croquis}

Este método requiere que comiences dibujando un perfil 2D. Necesitas activar el [Módulo de croquizado 2D](Draft_Module/es.md) (Menú **Vista \> Entorno \> Croquizado 2d**).


</div>


<div class="mw-translate-fuzzy">

Después necesitamos establecer el [plano de trabajo](Draft_SelectPlane/es.md). Dependiendo de tu versión de FreeCAD, lo tendrás directamente en la barra de herramientas, a la derecha, el botón que indica \"None\". Pulsalo, y a la izquierda aparecerán justo después de \"Comando activo: Seleccionar plano Equidistancia\", un campo de texto y una serie de botones. Asumiendo que quieres comenzar tu perfil en la vista en planta, seleciona XY. El botón \"None\" mostrará ahora \"Top\" como plano activo. [Ver nota.](#DraftPlaneButton/es.md)

Selecciona la herramienta ![](images/Draft_Wire.png ) [Wire o Polilínea (línea de múltiples puntos)](Draft_Wire.md), y comienza a dibujar la forma, utilizando los campos de texto para las posiciones X e Y. La casilla de verificación Relativo debería estar activada, así como la de \"Relleno\".


</div>


<div class="mw-translate-fuzzy">

-   1st punto: 0,0
-   2nd punto: 50,0
-   3rd punto: 0,10
-   4th punto: -40,0
-   5th punto: 0,40
-   6th punto: -10,0
-   No se indica el 7th punto, en su lugar pulsa en el botón \"Cerrar\" para cerrar el perfil. Ahora deberías tener este perfil, titulado \"Wire\" en la pestaña del Proyecto:


</div>


<div class="mw-translate-fuzzy">

![Fig. 1.7 La Polilínea base](images/Tutorial-normand07.jpg )


</div>


<div class="mw-translate-fuzzy">

Pulsa la tecla cero del para establecer la vista axonométrica.


</div>


<div class="mw-translate-fuzzy">

Activa el [Entorno de Pieza](Part_Workbench/es.md).


</div>


<div class="mw-translate-fuzzy">

Pulsa en la herramienta de <img alt="" src=images/Part_Extrude.png  style="width:32px;"> [Extruir](Part_Extrude.md).


</div>


<div class="mw-translate-fuzzy">

En la pestaña de Tareas a la izquierda, selecciona el objeto **Wire**. Introduce la longitud deseada, digamos que 750mm. Deja la dirección Z. Pulsa en Aplicar. Ahora deberías tener un objeto **Extrude** en la pestaña del Proyecto *(fig. 1.8)*


</div>

![Fig. 1.8 El objeto extruido](images/Tutorial-normand08.jpg )

Algo que se debe tener en cuenta con respecto a este método: para editar la forma, tienes que editar la Polilínea, no es tan sencillo como en el método anterior.


<div class="mw-translate-fuzzy">

Y también existen otros métodos para hacerlo! Espero que estos dos ejemplos te inicien. Seguramente te encuentres con algunos inconvenientes por el camino (A mi me pasó cuando aprendí a trabajar con FreeCAD, y tenía experiencia en CAD 3D ), pero no dudes en preguntar en el [foro de FreeCAD](http://forum.freecadweb.org)!


</div>


<div id="DraftPlaneButton/es">

Nota sobre el botón del plano de trabajo de Boceto:


</div>

La etiqueta en tu botón podría ser diferente, dependiendo de tu versión y también de lo que estuvieras haciendo antes. La etiqueta del botón podría ser: \"Planta\", \"alzado\", \"vista lateral\", \"Ninguna\" o una representación de un vector como d(0.0,0.0,1.0). También podría estar en blanco. Por ejemplo:

![Seleccionar Plano Ninguno](images/DraftPlaneNone.png )

![Seleccionar Plano Planta](images/DraftPlaneTop.png )


<div class="mw-translate-fuzzy">

![Seleccionar Plano Vista](images/DraftPlaneView.png ) 


</div>

Las instrucciones de arriba funcionarán, sin importar la etiqueta que tenga el botón.


{{Tutorials navi

}}  
