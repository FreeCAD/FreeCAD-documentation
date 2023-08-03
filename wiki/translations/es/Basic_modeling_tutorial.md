# Basic modeling tutorial/es
---
 TutorialInfo:s
   Topic:  Introducción a la modelización
   Level:  Principiante
   Time:  15 minutos
   Author: User:Normandc
   FCVersion: cualquier
   Files: ninguno
}}



## Introducción

Este Tutorial de Modelado Básico te mostrará cómo modelar un ángulo de hierro. Una cosa que hay que saber es que FreeCAD es modular por diseño, y como para muchos otros programas de CAD, siempre hay más de una manera de hacer las cosas. Exploraremos dos métodos aquí.

This tutorial was written with version 0.15 of FreeCAD.

## Antes de empezar 

Ten en cuenta que FreeCAD está todavía en una fase temprana de desarrollo, por lo que puede que no seas tan productivo como con otra aplicación de CAD, y seguramente te encontrarás con errores, o experimentarás cuelgues. FreeCAD tiene ahora la capacidad de guardar archivos de copia de seguridad. El número de esos archivos de copia de seguridad puede ser especificado en el diálogo de preferencias. No dudes en permitir 2 o 3 archivos de copia de seguridad hasta que sepas bien cómo manejar FreeCAD.

Guarde su trabajo a menudo, de vez en cuando guarde su trabajo con un nombre diferente, para tener una copia \"segura\" a la que recurrir, y esté preparado para la posibilidad de que algunos comandos no le den los resultados esperados.

## Introducción a las técnicas de modelado 

La primera  técnica de modelado de sólidos es Geometría constructiva de sólidos . También hay una explicación detallada  de Geometría constructiva de sólidos en el wiki. Trabajas con formas primitivas como cubos, cilindros, esferas y conos para construir tu geometría combinándolas, restando una forma de la otra, o intersectándolas. Estas herramientas forman parte del Ambiente de trabajo Pieza. También puedes aplicar transformaciones en las formas, como aplicar redondeos o chaflanes en las aristas. Estas herramientas también están en el Ambiente de trabajo Pieza.

Luego existen otras herramientas más avanzadas. Tu empiezas dibujando un perfil 2D que puedas extruir o revolucionar.

Así que vamos a comenzar tratando de hacer un pie de hierro para una mesa con estos 2 métodos.


<div class="mw-translate-fuzzy">

## 1er Método - Por Geometría Sólida Constructiva 

1.  Comienza con el Ambiente de trabajo Pieza !.
2.  Si no has abierto un nuevo documento de FreeCAD , desde el menú desplegable haz clic en **Archivo , Nuevo** o haz clic en el !{width="32"} **Crear un nuevo documento vacío**\' icono.
3.  Haga clic en el !{width="32"} Caja para crear una caja
4.  Cambia sus dimensiones seleccionándola en el espacio 3D, o haciendo clic en la pestaña Proyecto de la izquierda, y luego
5.  Haz clic en la pestaña Datos de la parte inferior, y cambia los valores de Longitud, Anchura y Altura a 50mm, 50 y 750 ** *Nota*: *cuando se tomaron estas capturas, las propiedades estaban ordenadas de forma diferente, siendo la Altura la primera*.
6.  La caja ahora llena la mayor parte de la vista 3D. Haga clic en !{width="32"} Encajar todo para ajustar la vista a la caja recién creada.
7.  Crea una segunda caja de la misma manera, pero con los valores L=40, W=40 y H=750mm. Por defecto esta caja se superpondrá a la primera. **
8.  Ahora restaremos la segunda caja a la primera. Seleccione primero la primera forma , luego la segunda , ¡el orden de selección es importante!  a la selección de CAD o Blender).
9.  En la barra de herramientas del ambiente de trabajo de piezas, haga clic en el !{width="32"} Cortar.


</div>

!Fig. 1.1 El primer cubo

!Fig. 1.2 El segundo cubo superpuesto sobre el primero, preparado para ser restado

!Fig. 1.3 Después de la resta


<div class="mw-translate-fuzzy">

Ahora tienes tu primer ángulo de hierro **. Te habrás fijado que, en la pestaña de Proyecto a la izquierda, ambos cubos han sido reemplazados por un objeto \"Cut\". En realidad, no han desaparecido, sino que se han agrupado en el objeto Cut. Pulsa en el + en frente de él, y verás que ambos cubos siguen ahí, pero sin resaltar **. Si pulsas en cada uno de ellos y pulsas la barra espaciadora, se mostrarán. La barra espaciadora alterna la visibilidad de los objetos seleccionados. **


</div>


<div class="mw-translate-fuzzy">

No quieres el ángulo orientado en esa posición? Simplemente necesitas cambiar la ubicación de la forma Box001. Selecciónalo, ocultalo y en la pestaña de Datos, pulsa sobre el + enfrente a Placement, entonces se despliega la ubicación, y cambia sus coordenadas X e Y. Presiona Enter, oculta la forma Box001 de nuevo, y la orientación de tu ángulo es ahora diferente. ** Incluso puedes cambiar las dimensiones de las formas, y el objeto Cut se actualizará.


</div>

!Fig. 1.4 La operación corte retiene sus objetos originales ")

!Fig. 1.5 Aún puedes hacer visibles los cubos originales


<div class="mw-translate-fuzzy">

Por cierto, podemos añadir redondeos al ángulo para que parezca más real, utilizando la herramienta !{width="32"} Redondeo. **


</div>

!Fig. 1.6 Las aristas redondeadas


<div class="mw-translate-fuzzy">

## Segundo método - Extruyendo un croquis 

Este método requiere que comiences dibujando un perfil 2D. Necesitas activar el Módulo de croquizado 2D .


</div>


<div class="mw-translate-fuzzy">

Después necesitamos establecer el plano de trabajo. Dependiendo de tu versión de FreeCAD, lo tendrás directamente en la barra de herramientas, a la derecha, el botón que indica \"None\". Pulsalo, y a la izquierda aparecerán justo después de \"Comando activo: Seleccionar plano Equidistancia\", un campo de texto y una serie de botones. Asumiendo que quieres comenzar tu perfil en la vista en planta, seleciona XY. El botón \"None\" mostrará ahora \"Top\" como plano activo. Ver nota.

Selecciona la herramienta ! Wire o Polilínea , y comienza a dibujar la forma, utilizando los campos de texto para las posiciones X e Y. La casilla de verificación Relativo debería estar activada, así como la de \"Relleno\".


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

!Fig. 1.7 La Polilínea base


</div>


<div class="mw-translate-fuzzy">

Pulsa la tecla cero del para establecer la vista axonométrica.


</div>


<div class="mw-translate-fuzzy">

Activa el Entorno de Pieza.


</div>


<div class="mw-translate-fuzzy">

Pulsa en la herramienta de !{width="32"} Extruir.


</div>


<div class="mw-translate-fuzzy">

En la pestaña de Tareas a la izquierda, selecciona el objeto **Wire**. Introduce la longitud deseada, digamos que 750mm. Deja la dirección Z. Pulsa en Aplicar. Ahora deberías tener un objeto **Extrude** en la pestaña del Proyecto **


</div>

!Fig. 1.8 El objeto extruido

Algo que se debe tener en cuenta con respecto a este método: para editar la forma, tienes que editar la Polilínea, no es tan sencillo como en el método anterior.


<div class="mw-translate-fuzzy">

Y también existen otros métodos para hacerlo! Espero que estos dos ejemplos te inicien. Seguramente te encuentres con algunos inconvenientes por el camino , pero no dudes en preguntar en el foro de FreeCAD!


</div>


<div id="DraftPlaneButton/es">

Nota sobre el botón del plano de trabajo de Boceto:


</div>

La etiqueta en tu botón podría ser diferente, dependiendo de tu versión y también de lo que estuvieras haciendo antes. La etiqueta del botón podría ser: \"Planta\", \"alzado\", \"vista lateral\", \"Ninguna\" o una representación de un vector como d. También podría estar en blanco. Por ejemplo:

!Seleccionar Plano Ninguno

!Seleccionar Plano Planta


<div class="mw-translate-fuzzy">

!Seleccionar Plano Vista 


</div>

Las instrucciones de arriba funcionarán, sin importar la etiqueta que tenga el botón.


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Basic modeling tutorial/es
