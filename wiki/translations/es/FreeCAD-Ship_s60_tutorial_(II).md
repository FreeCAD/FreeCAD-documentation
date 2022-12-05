---
- TutorialInfo:/es
   Topic:Ship Workbench
   Level: Beginner
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial (II)/es





## Vista general 

Antes de empezar este tutorial, asegúrate de que ya has realizado [la primera parte](FreeCAD-Ship_s60_tutorial/es.md).

Aprende más sobre el ambiente de trabajo de la nave en su página wiki dedicada: [Ambiente de trabajo Nave](Ship_Workbench/es.md)

## Introducción

En el tutorial anterior nos centramos en cálculos hidrostáticos, mientras que en el presente tutorial comenzaremos a trabajar con pesos, aprendiendo a definir los pesos del nave y sus tanques, para así poder calcular la curva de GZ, que es el parámetro hidrostático más importante en cuanto a estabilidad transversal del buque se refiere. GZ es el brazo del momento estático generado cuando el buque adquiere una escora. Por supuesto siempre que GZ sea positivo, el nave tendrá un momento adrizante que tratará de reponer la situación de equilibrio anterior a la escora, pero cuando GZ se torna negativo la estabilidad del buque se habrá agotado, tendiendo éste a dar la vuelta buscando un nuevo equilibrio.

La IMO (Organización Marítima Internacional) establece los siguientes criterios mínimos de estabilidad transversal:

-   *GM* \>= 0.15 m. *GM* (altura metacéntrica) es la tangente inicial de la curva de *GZ*.
-   El valor máximo de *GZ* se debe dar a escoras superiores a 30 grados.
-   Con una escora de 30 grados *GZ* debe ser al menos de 0.2 m.
-   El área por debajo de la curva de *GZ* hasta los 40 grados de escora debe ser al menos de 0.090 m · rad.
-   El área por debajo de la curva de *GZ* hasta los 30 grados de escora debe ser al menos de 0.055 m · rad.
-   El área por debajo de la curva de *GZ* entre los 30 y los 40 grados de escora debe ser al menos de 0.030 m · rad.

En este tutorial vamos a configurar los pesos y los depósitos de nuestra nave de la serie 60, en una situación simulada.

## Pesos del buque 

De cara a poder calcular la curva de GZ se necesita conocer el peso del buque, y la posición del centro de gravedad para cada ángulo de escora. de tal forma que los pesos se pueden dividir en dos categorías:

-   Pesos fijos que se mueven solidariamente con el nave.
-   Tanques, cuyo líquido en su interior modifica su forma desplazando el centro de gravedad, siendo necesario recalcularlo para ángulo de escora.

El ambiente de trabajo del buque ofrece dos herramientas diferentes para generar cada instancia.

![Icono de la herramienta de definición de pesos.](images/FreeCAD-Ship-WeightIco.png )


<center>

Icono de la herramienta de definición de pesos.


</center>

La herramienta de definición de pesos puede utilizarse para establecer la primera categoría de pesos. Cuando se lanza la herramienta por primera vez (con la instancia del nave seleccionada), la mesa de trabajo del nave inicializa los pesos del nave con el nave ligero (igual al desplazamiento del nave) que se coloca en la coordenada X del centro de gravedad del nave, y a la altura del calado de diseño. Normalmente hay al menos 2 pesos relevantes:

-   Estructura.
-   Motor principal (o varios de ellos).

Así que vamos a cambiarlo. Haciendo doble clic sobre cada celda podemos editar el valor, estableciendo los pesos:

-   Estructura, 15000 kg, (-0,1, 0, 1,25) m
-   Motor de estribor, 5000 kg, (-6,5, -0,65, 0,5) m
-   Motor de babor, 5000 kg, (-6,5, 0,65, 0,5) m
-   Motor de emergencia, 2500 kg, (0,2, 0, 2,5) m

![Vista previa de los pesos.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Vista previa de los pesos.


</center>

La posición de los pesos se muestra en la [vista 3D](3D_view/es.md). Nota: las anotaciones se eliminarán cuando se cierre la herramienta. Al pulsar **Aceptar** los pesos se almacenarán en la instancia de su nave.

## Tanques

Los tanques deben ser creados en la parte superior de la geometría sólida, como la instancia de la nave, por lo que el primer paso es crear dos tanques de proa (uno por cada lado de la nave) las geometrías sólidas que vamos a considerar (por lo general los buques tienen una gran cantidad de tanques de combustible, agua dulce, agua salada, carga, etc).

### Creación de la geometría 

Para generar tanques cargamos [modulo de piezas](Part_Workbench/es.md), y creamos una caja sólida.

Tenemos que editar la caja, por lo que la seleccionamos en el árbol **Atributos y etiquetas**, y cambiamos de vista a la pestaña de datos. Expandir Colocación, y en ellos Posición, y establecer *x* a 1,5, y z a -1. Queremos cambiar la longitud de la caja también el cambio de 5,0 (tenga en cuenta que las unidades pueden ser en mm, no se preocupe por esto).

La geometría de nuestro tanque será la parte común de la caja que acabamos de crear, y del nave. Como estamos interesados en la geometría del nave podemos ocultar nuestra instancia de buque **Ship**, y mostrar la geometría **s60_IowaUniversity**. Seleccionando la caja y la geometría del buque empleamos la herramienta intersección, generandose así la geometría de nuestro tanque de estribor.

![Geometría del tanque generada.](images/FreeCAD-Ship-S60TankGeometry.png )


<center>

Geometría del tanque generada.


</center>

Para generar la geometría del tanque de babor simplemente seleccionamos nuestro tanque a estribor y ejecutamos la herramienta de simetría, tomando XZ como plano de simetría.

Para convertir las geometrías en el tipo convencional simplemente cargamos el [módulo de esbozado](Draft_Workbench/es.md), y ejecutamos promocionar sobre cada una de las geometrías generadas. Podemos renombrar las geometrías como:

-   StarboardTankGeom
-   BoardTankGeom

También podemos borrar la caja, pues no la necesitaremos más.

### Generación de instancias de tanques 

Si recargamos [módulo FreeCAD-Ship](Ship_Workbench/es.md) otra vez, podemos encontrar la herramienta generadora de instancias de tanques.

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial (II)/es
