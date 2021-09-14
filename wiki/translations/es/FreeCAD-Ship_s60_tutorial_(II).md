# FreeCAD-Ship s60 tutorial (II)/es




{{TutorialInfo/es
|Topic=Ship Workbench
|Level= Beginner
|Time=
|Author=
|FCVersion=
|Files=
}}

## Overview


<div class="mw-translate-fuzzy">

Asegúrese de haber realizado la [primera parte](FreeCAD-Ship_s60_tutorial/es.md) de este tutorial antes de comenzar con este capítulo.


</div>


<div class="mw-translate-fuzzy">

Puedes encontrar más información sobre [FreeCAD-Ship aquí](FreeCADShip_Workbench/es.md)


</div>

## Introducción

En el tutorial anterior nos centramos en cálculos hidrostáticos, mientras que en el presente tutorial comenzaremos a trabajar con pesos, aprendiendo a definir los pesos del barco y sus tanques, para así poder calcular la curva de GZ, que es el parámetro hidrostático más importante en cuanto a estabilidad transversal del buque se refiere. GZ es el brazo del momento estático generado cuando el buque adquiere una escora. Por supuesto siempre que GZ sea positivo, el barco tendrá un momento adrizante que tratará de reponer la situación de equilibrio anterior a la escora, pero cuando GZ se torna negativo la estabilidad del buque se habrá agotado, tendiendo éste a dar la vuelta buscando un nuevo equilibrio.

La IMO (Organización Marítima Internacional) establece los siguientes criterios mínimos de estabilidad transversal:

-   *GM* \>= 0.15 m. *GM* (altura metacéntrica) es la tangente inicial de la curva de *GZ*.
-   El valor máximo de *GZ* se debe dar a escoras superiores a 30 grados.
-   Con una escora de 30 grados *GZ* debe ser al menos de 0.2 m.
-   El área por debajo de la curva de *GZ* hasta los 40 grados de escora debe ser al menos de 0.090 m · rad.
-   El área por debajo de la curva de *GZ* hasta los 30 grados de escora debe ser al menos de 0.055 m · rad.
-   El área por debajo de la curva de *GZ* entre los 30 y los 40 grados de escora debe ser al menos de 0.030 m · rad.


<div class="mw-translate-fuzzy">

Trabajaremos en este tutorial sobre nuestro serie 60, generando una distribución irreal de tanques y pesos.


</div>

## Pesos del buque 

De cara a poder calcular la curva de GZ se necesita conocer el peso del buque, y la posición del centro de gravedad para cada ángulo de escora. de tal forma que los pesos se pueden dividir en dos categorías:

-   Pesos fijos que se mueven solidariamente con el barco.
-   Tanques, cuyo líquido en su interior modifica su forma desplazando el centro de gravedad, siendo necesario recalcularlo para ángulo de escora.


<div class="mw-translate-fuzzy">

Cada tipo de peso tiene una herramienta específica en FreeCAD-Ship.


</div>

![Icono de la herramienta de definición de pesos.](images/FreeCAD-Ship-WeightIco.png )


<center>

Icono de la herramienta de definición de pesos.


</center>


<div class="mw-translate-fuzzy">

La herramienta de definición de pesos se usa para definir los pesos de la primera categoría. En el momento en que se lanza la herramienta por primera vez para un barco, este inicializa un peso como su peso en rosca, que es igual a su desplazamiento, y esta situado en la coordenada longitudinal del centro de empujes y en la flotación. Este peso en rosca se guarda automáticamente independientemente de si aceptamos o cancelamos. Normalmente existen al menos dos importantes partidas de peso:

-   Estructura.
-   Motores.


</div>


<div class="mw-translate-fuzzy">

Nostros vamos a establecer los siguientes pesos y posiciones para nuestro serie 60:

-   Structure, 15000 kg, (-0.1, 0, 1.25) m
-   Starboard engine, 5000 kg, (-6.5, -0.65, 0.5) m
-   Board engine, 5000 kg, (-6.5, 0.65, 0.5) m
-   Emergency engine, 2500 kg, (0.2, 0, 2.5) m


</div>

![Vista previa de los pesos.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Vista previa de los pesos.


</center>


<div class="mw-translate-fuzzy">

Los pesos se previsualizan en la ventana 3D. Todas estas anotaciones se eliminarán al terminar de trabajar con la herramienta, luego no se preocupe de ellas.


</div>


<div class="mw-translate-fuzzy">

## Tanques

Los tanques se generan a partir de geometrías solidas, de una forma similar a como trabajamos para crear un buque. Por tanto comenzaremos creando dos solidos (uno a cada banda) que más tarde convertiremos en instancias tanque. En este ejemplo nos limitaremos a considerar dos tanques a proa, aunque usualmente un barco puede tener decenas o incluso cientos de ellos.


</div>

### Creación de la geometría 

Para generar la geometría nos cambiados al [modulo de piezas](Part_Workbench/es.md), y creamos una caja sólida.


<div class="mw-translate-fuzzy">

Las dimensions de la caja, y su posición, no nos convienen, y por tanto vamos a modificarla. Para ello la seleccionamos en el árbol de **etiquetas y atributos**, y en la pestaña Datos desplegamos el emplazamiento, y dentro de él la posición, cambiando la coordenada *x* a 1.5, y la coordenada *z* a -1. También modificamos la longitud de la caja por 5.0 (las unidades pueden estar en milímetros, no te preocupes por ello).


</div>

La geometría de nuestro tanque será la parte común de la caja que acabamos de crear, y del barco. Como estamos interesados en la geometría del barco podemos ocultar nuestra instancia de buque **Ship**, y mostrar la geometría **s60\_IowaUniversity**. Seleccionando la caja y la geometría del buque empleamos la herramienta intersección, generandose así la geometría de nuestro tanque de estribor.

![Geometría del tanque generada.](images/FreeCAD-Ship-S60TankGeometry.png )


<center>

Geometría del tanque generada.


</center>

Para generar la geometría del tanque de babor simplemente seleccionamos nuestro tanque a estribor y ejecutamos la herramienta de simetría, tomando XZ como plano de simetría.

Para convertir las geometrías en el tipo convencional simplemente cargamos el [módulo de esbozado](Draft_Workbench/es.md), y ejecutamos promocionar sobre cada una de las geometrías generadas. Podemos renombrar las geometrías como:

-   StarboardTankGeom
-   BoardTankGeom

También podemos borrar la caja, pues no la necesitaremos más.


<div class="mw-translate-fuzzy">

### Creación de las instancias de tanque. 

Recuperando nuestro [módulo FreeCAD-Ship](FreeCADShip_Workbench/es.md), podremos encontrar la herramienta de generación de tanques.


</div>

![Icono de la herramienta de generación de tanques.](images/FreeCAD-Ship-TankIco.png )


<center>

Icono de la herramienta de generación de tanques.


</center>


<div class="mw-translate-fuzzy">

Ahora seleccionamos la geometría **StarboardTankGeom** y ejecutamos la herramienta de generación de tanques, abriéndose un diálogo donde estableceremos un llenado del 40%, y una densidad del fluido de 925 kg/m³ (Aproximadamente fuel pesado). Al aceptar una nueva instancia llamada **Tank** nos aparecera, nosotros la podemos renombrar como **StarboardTank**.


</div>

Repetimos la misma operación para generar el tanque **BoardTank** de babor.

![Vista de todos los pesos del buque.](images/FreeCAD-Ship-S60WeightsTanksPreview.png )


<center>

Vista de todos los pesos del buque.


</center>

En la figura anterior se muestra el buque al que vamos a calcular su curva de GZ.


<div class="mw-translate-fuzzy">

### Curva de GZ 

FreeCAD-Ship dispone una herramienta sencilla para el cálculo de la curva GZ.


</div>


<div class="mw-translate-fuzzy">

![Icono de la herramienta de cálculo de GZ.](images/FreeCAD-Ship-HydrostaticsIco.png )


<center>

Icono de la herramienta de cálculo de GZ.


</center>


</div>


<div class="mw-translate-fuzzy">

Con la instancia buque seleccionada lanzamos la herramienta. Lo primero que encontramos en el diálogo es una lista con todos los tanques presentes en el documento. Como en nuestro caso queremos emplear los dos tanques los seleccionamos en la lista, remarcándose con un fondo diferente.


</div>

La herramienta puede informarnos sobre el calado y el desplazamiento resultantes, para lo que presionamos sobre **Actualizar desplazamiento y calado**, operación que puede tomar algún tiempo. Recibiremos la siguiente información:

-   Desplazamiento = 37505.5 kg
-   Calado = 0.818664 m


<div class="mw-translate-fuzzy">

Luego nos encontramos en una situación de carga de poco desplazamiento, puesto que el calado es un 20% inferior al de diseño. Normalmente bajos calados implican una mala estabilidad, de tal forma que dependiendo de los resultados de la curva GZ, puede ser necesario (si se desea operar en ésta condición) añadir tanques de lastre en el fondo de cara a rebajar el centro de gravedad y aumentar el calado.


</div>

La herramienta también puede calcular automáticamente el trimado del buque (presionando sobre **Auto**), operación que puede tomar alrededor de un minuto en éste caso. En este caso el buque tomaría un trimado de 0.95 grados por popa. Nosotros no consideraremos trimado ninguno (0 grados).

También debemos introducir los ángulos de escora a considerar. En este ejemplo queremos conocer el comportamiento del buque a cualquier ángulo, luego establecemos los siguientes valores:

-   0 grados de escora inicial.
-   180 grados de escora final.
-   46 puntos, o un punto por cada 2 grados de escora. El cálculo de GZ puede llevar largos tiempos de computación, dependiendo de la complejidad de la geometría y el número de puntos solicitados, luego tenga cuidado con este valor.


<div class="mw-translate-fuzzy">

Al aceptar la herramienta comienza a calcular. Si arrancaste FreeCAD desde una terminal podrás conocer el progreso del cálculo, e incluso detenerlo con **Ctrl+C**. En unos segundos recibiremos la curva de GZ.


</div>

La herramienta emplea [pyxplot](http://www.pyxplot.org.uk/) y [ghostscript](http://www.ghostscript.com/), al igual que el generador de curvas de áreas o el de hidrostáticas. Puede encontrar el archivo **gz.dat** generado en el directorio que se indica en la vista de informe (Vista/Vistas/Vista de informe), pudiendo cargar este archivo desde un programa de hojas de cálculo (por ejemplo [libreOffice](http://www.libreoffice.org)). Junto al archivo de salida se situán algunos archivos adicionales:

-   **gz.dat**: Datos de la curva de GZ.
-   **gz.pyxplot**: Guión para pyxplot para la generación de la figura.
-   **gz.eps**: Imagen en formato EPS.
-   **gz.png**: Imagen en formato PNG.

Estos archivos se sobreescribirán la próxima vez que lance la herramienta, luego cópielos en otro lugar si desea conservarlos.

### Resultados

<img alt="Curva de GZ." src=images/FreeCAD-Ship-s60GZ.png  style="width:800px;">


<center>

Curva de GZ.


</center>


<div class="mw-translate-fuzzy">

El máximo valor de *GZ* se sitúa a 45 grados, muy por encima de los 30 grados que exige la normativa. Con una escora de 30 grados *GZ* vale 0.25 m, siendo el mínimo de 0.2 metros. El área bajo la curva de GZ hasta los 30 grados es de 0.065 m·rad, mientras que hasta los cuarenta grados de escora computa 0.092 m·rad, ambos valores por encima de los exigidos. Sin embargo, el área bajo la curva de GZ entre los 30 y los 40 grados de escora es de 0.027 m·rad, valor por debajo del mínimo exigido por la normativa de la IMO.


</div>


<div class="mw-translate-fuzzy">

Para solucionarlo sería necesario lastrar el buque en ésta condición de carga. Por otra parte, podemos ver como la curva de GZ da valores positivos hasta los 95 grados, siendo insuficiente para cumplir los requerimientos de la IMO, lo que nos da una idea de lo exigente de los criterios aplicables a la estabilidad de buques.


</div>


<div class="mw-translate-fuzzy">

Por supuesto este ejemplo no es real, entre otras cosas porque no se pueden llevar tanques de combustible en el doble fondo, o sin disponer doble casco, pero es un buen ejemplo para aprender a manejar [FreeCAD-Ship](FreeCADShip_Workbench/es.md).


</div>


{{Ship Tools navi

}}
