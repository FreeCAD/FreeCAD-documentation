


{{TutorialInfo/es
|Topic=Ambiente de Trabajo
|Level=Principiante
|Time=
|Author=
|FCVersion=
|Files=
}}

## Introducción

En este tutorial trabajaremos con un nave de la Serie 60, de la Universidad de Iowa. El tutorial está orientado a mostrar cómo se trabaja con un barco monocasco simétrico, sin embargo se pueden realizar barcos multicasco o no simétricos con el mismo procedimiento.

Más información sobre <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> [Ambiente de trabajo de naves](Ship_Workbench/es.md).

## Cargando geometría 

### Fondo

El <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> [Ambiente de trabajo nave](Ship_Workbench/es.md) trabaja sobre **Entidades de barco**, que deben ser creadas sobre la geometría proporcionada. La geometría debe ser un sólido (o conjunto de sólidos), se deben tener en cuenta los siguientes criterios:

-   Se debe proporcionar toda la geometría del casco (incluyendo los cuerpos simétricos).
-   La geometría de estribor debe incluirse en el dominio *y* negativo.
-   El punto de origen (0,0,0) es la intersección de la **sección media** (punto medio entre la perpendicular de popa y la de proa) y la **línea base**.

![Vista esquemática del criterio de signos.](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

Criterio de signos de FreeCAD-Ship.


</center>

### Cargando la geometría del Serie 60 

Para ayudar a los nuevos usuarios, el banco de trabajo Ship incluye un cargador de ejemplos de geometrías, con los siguientes para elegir:

-   Serie 60 de la Universidad de Iowa
-   Buque canónico de Wigley
-   Catamarán de la serie 60
-   Catamarán de Wigley

![Icono del cargador de geometrías de barcos de ejemplo](images/Ship_Load.SVG )


<center>

Icono del cargador de ejemplos de geometrías de barcos


</center>

Ejecutando la herramienta (Diseño de buques/Cargar un ejemplo de geometría de barco) se mostrará un cuadro de diálogo. Selecciona **Serie 60 de la Universidad de Iowa** y pulsa Aceptar. La herramienta carga un nuevo documento con la geometría **s60\_IowaUniversity**.


{{VeryImportantMessage|'''¡Atención, antes de editar nada!''
Ahora está trabajando con el archivo de ejemplo original.
Para preservar el ejemplo original sin editar, '''debes guardarlo primero como un nuevo archivo antes de editar nada'''}}

.

## Crear instancia del barco 

Para crear una **Instancia de barco** selecciona la geometría s60 y ejecuta la **herramienta de creación de barco** (Diseño de buques/Crear un nuevo barco).

![Herramienta de creación de barcos](images/Ship_Logo.svg )


<center>

Icono de la herramienta de creación de barcos


</center>

Se mostrará el diálogo de la tarea de creación de una nave y algunas anotaciones en la [vista 3D](3D_view/es.md). Las anotaciones desaparecerán cuando cierres la herramienta de creación de naves, así que no te preocupes por esto.

Se deben introducir los datos más relevantes del barco (el <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> El ambiente de trabajo de barcos utiliza un sistema de introducción de datos progresivo, por lo que las operaciones básicas pueden realizarse conociendo sólo los datos básicos del barco, siendo necesaria más información a medida que las operaciones se hacen más complejas).

### Datos del barco 

Las principales dimensiones deben ser introducidas aquí:

-   Eslora: Eslora entre perpendiculares, 25,5 m para este barco.
-   Manga: Manga total del barco, 3,389 m para este barco.
-   Calado: Calado de diseño, 1,0 m para este barco.

![Anotaciones sobre la vista frontal.](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Anotaciones sobre la vista frontal.


</center>

La eslora entre perpendiculares depende del calado de diseño, por tanto si no se conoce la eslora entre perpendiculares se puede fijar el calado y ajustar la eslora hasta que coincida con la intersección entre la roda (línea tope de la proa) con la flotación.

![Anotaciones sobre la vista lateral.](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Anotaciones sobre la vista lateral.


</center>

Se puede seguir la misma metodología para proceder con la manga. Conviene darse cuenta que se trata de la manga total, luego se debe considerar el barco completo, aunque la anotación sólo marque el costado de estribor.

Cuando se pulsa el botón **Aceptar**, se crea una nueva instancia de Nave llamada **Nave** en el diálogo *Etiquetas y Atributos*. Ya no necesitamos la geometría, así que puedes ocultarla.

![Icono de las instancias Buque.](images/FreeCAD-Ship-ShipInstance.png )


<center>

Icono de las instancias Buque.


</center>

A partir de aquí, debes tener seleccionada la opción **Nave** antes de ejecutar cualquiera de las herramientas del ambiente de trabajo nave.

## Dibujo de líneas 

El ambiente de trabajo del nave ofrece una herramienta que facilita la obtención de un plano de líneas a partir del dibujo de líneas del nave

![Herramienta de dibujo de líneas](images/Ship_OutlineDraw.svg )


<center>

Icono de la herramienta de dibujo de líneas


</center>

El dibujo de líneas es un conjunto de líneas de cortes de sección en los 3 ejes, que finalmente mostrarán la geometría del casco en un Plano de Líneas. Necesitamos proporcionar las líneas para las 3 siguientes vistas:

-   Plano del cuerpo (usando los cortes transversales)
-   Plano de la carena (usando los cortes longitudinales)
-   Plano de media manga (usando los cortes de líneas de agua)

### Cortes transversales 

Normalmente se deben realizar 21 secciones transversales equidistantes entre perpendiculares. para ello FreeCAD proporciona una herramienta automática para poder hacerlo, simplemente selecciona el tipo de secciones **Transversales**, ve a la casilla **Auto crear** y pon **21** secciones, luego pulsa {{Bitton|Crear secciones}}

![Vista previa de las cuadernas.](images/S60OutlineTransversal.png )


<center>

Vista previa de las cuadernas.


</center>

Se rellena la tabla de secciones y se muestra la vista previa de secciones llamada **OutlineDraw**. Normalmente se añaden más secciones en proa y popa, donde se registran curvaturas más complejas, para ello

1.  Ir al final de la tabla y hacer *doble clic* en un elemento vacío para editarlo.
2.  Pulse **intro** para confirmar.
3.  Agregue las siguientes secciones:

:   

    :   X~22~ = -12.1125 m
    :   X~23~ = 12.1125 m

Dependiendo de la complejidad de la geometría, la previsualización puede llevar algún tiempo.

### Cortes longitudinales 

Hay que añadir dos cortes longitudinales, por lo que hay que seleccionar el tipo de secciones **Longitudinales**, ir a la casilla **Creación automática**\' y poner **2** secciones, luego pulsar **Crear secciones**. Tabla de secciones se llena, y la vista previa de las secciones actualizadas.

### Líneas de agua 

6 Líneas de agua entre la línea de base y el proyecto de diseño debe ser añadido, así que seleccione **Líneas de agua** tipo de secciones, vaya a **Auto crear**\' caja y establecer **5**\' (Z = 0 m no se considerará, añadir manualmente si lo necesita) secciones, a continuación, pulse **Crear secciones**. La tabla de secciones se llena, y la vista previa de las secciones se actualiza.

Hay que añadir varias líneas de agua adicionales:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m

### Perform plot 

Select **1:100** scale and press **Accept** to let the tool to generate the 3D sections in a new object.

![Plano de formas.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Plano de formas.


</center>

In order to plot these sections you can use the [Drawing workbench](Drawing_Workbench.md):

![Secciones resultantes.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Seccioens resultantes.


</center>

## Curva de áreas transversales 

Uno de los parámetros hidrodinámicos típicos en el diseño de buques es la curva de áreas transversales, que permite obtener algunos indicadores sobre el comportamiento del casco (resistencia al remolque, comportamiento en el mar, \...). El ambiente de trabajo nave proporciona una herramienta sencilla para realizar la curva de áreas transversales.

![Icono de la herramienta de trazado de curvas de áreas.](images/FreeCAD-Ship-AreaCurveIco.png )


<center>

Icono de la herramienta de trazado de curvas de áreas.


</center>

Cuando se ejecuta la herramienta se muestra un diálogo de tarea, y se crea una vista previa de la superficie libre en la [vista 3D](3D_view/es.md) (La vista previa de la superficie libre se eliminará cuando la herramienta termine, así que no se preocupe por esto). En el diálogo de la tarea están presentes los datos de entrada y salida.

### Datos de entrada 

El calado y el trimado (ángulo de rotación del *borde y* del casco, positivo si el calado de popa puede aumentar) deben ser proporcionados. Se pueden realizar varias curvas de áreas, dependiendo de las situaciones de carga del buque, pero se deben realizar dos trazados típicos:

-   Curva de áreas transversales de diseño: Sin ángulo de trimado y utilizando el calado de diseño, 1,0 m en este caso.
-   Curva de áreas transversales de máximo calado: Sin ángulo de trimado y con el máximo calado permitido, 2,0 m en este caso.


<div class="mw-translate-fuzzy">

### Datos de salida 

FreeCAD-Ship muestra un informe de salida que se actualiza en tiempo real, que incluye los siguientes datos:

-   **L**: Eslora entre perpendiculares, valor que se estableció durante la creación del buque.
-   **B**: Manga total que se estableció durante la creación del buque.
-   **T**: Calado actual en la cuaderna maestra.
-   **Trim**: Ángulo de trimado.
-   **T~AP~**: Calado en la perpendicular de popa.
-   **T~FP~**: Calado en la perpendicular de proa.
-   **Displacement**: Desplazamiento del buque (Se considera agua salada, por tanto se debe dividir por 1.025 para conocer el volumen desplazado).
-   **XCB**: Coordenada *X* del centro de flotación (relativo a la cuaderna maestra).


</div>

When **Accept** button is pressed a plot is performed (depending on geometry complexity can take some time, you can see progress on terminal, and stop the work pressing **Ctrl**+**C**). When the task has finished FreeCAD will generate a Plot (see the [Plot workbench](Plot_Workbench.md) documentation) and a SpreadSheet (see the [Spreadsheet workbench](Spreadsheet_Workbench.md) documentation).

![Curva de áreas para el calado de diseño. ](images/FreeCAD-Ship-s60Areas.png )


<center>

Curva de áreas para el calado de diseño.


</center>

Puede realizar de la misma forma la curva de áreas para el calado máximo y así poder observar las diferencias (Por ejemplo, se podrá observar que la curva de áreas sobrepasa las perpendiculares de proa y popa)

## Hidrostáticas

El cálculo de las hidrostaticas es una parte clave en el proceso de diseño del buque, pues provee información crucial acerca de la estabilidad del buque. Las sociedades de clasificación exigen esta información de cara a certificar los buques, ya que unida a la información referente a las condiciones de carga aportan la información básica sobre la estabilidad del buque. FreeCAD-Ship incorpora una herramienta para calcular las principales curvas hidrostaticas (Las curvas GZ no han sido implementadas por el momento).

![Icono de la herramienta de Hidrostáticas.](images/FreeCAD-Ship-HydrostaticsIco.png‎ )


<center>

Icono de la herramienta de Hidrostáticas.


</center>

Al lanzar la herramienta se muestra el cuadro de diálogo donde deberemos establecer los valores de trimado y calados. Normalmente las curvas hidrostáticas se presentan en un rango de calados para cada ángulo de trimado. En este tutorial sólo consideraremos el barco sin trimar, y puesto que no conocemos las situaciones de carga, para un amplio rango de calados (Convencionalmente se ajustan al rango de calados plausible para el buque).

Por tanto establecemos los siguientes valores:

-   **Trimado** = 0º
-   **Calado mínimo** = 0.1 m
-   **Calado máximo** = 2.0 m
-   **Numero de puntos** = 39. Un gran número de puntos implica largos tiempos de cálculo, y en ocasiones las diferencias no serán perceptibles. Para el número propuesto el cálculo puede llevar un minuto aproximadamente.

When **Accept** button is pressed plots are performed (see the [Plot workbench](Plot_Workbench.md) documentation) and a spreadsheet is generated (see the [Spreadsheet workbench](Spreadsheet_Workbench.md) documentation).

![Curvas hidrostáticas.](images/FreeCAD-Ship-HydrostaticsCurves.jpg )


<center>

Curvas hidrostáticas.


</center>

## Seguir aprendiendo 

El [Tutorial de FreeCAD-Nave s60 (II)](FreeCAD-Ship_s60_tutorial_(II)/es.md) es el segundo capítulo de la serie 60 de la nave universitaria de Iowa.


{{Ship Tools navi

}}
