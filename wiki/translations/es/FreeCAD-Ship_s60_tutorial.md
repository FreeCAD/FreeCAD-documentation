---
- TutorialInfo   */es
   Topic   *Ambiente de Trabajo
   Level   *Principiante
   Time   *
   Author   *
   FCVersion   *
   Files   *
---

# FreeCAD-Ship s60 tutorial/es





## Introducción

En este tutorial trabajaremos con un nave de la Serie 60, de la Universidad de Iowa. El tutorial está orientado a mostrar cómo se trabaja con un nave monocasco simétrico, sin embargo se pueden realizar nave multicasco o no simétricos con el mismo procedimiento.

Más información sobre <img alt="" src=images/Workbench_Ship.svg  style="width   *24px;"> [Ambiente de trabajo de naves](Ship_Workbench/es.md).

## Cargando geometría 

### Fondo

El <img alt="" src=images/Workbench_Ship.svg  style="width   *24px;"> [Ambiente de trabajo nave](Ship_Workbench/es.md) trabaja sobre **Entidades de nave**, que deben ser creadas sobre la geometría proporcionada. La geometría debe ser un sólido (o conjunto de sólidos), se deben tener en cuenta los siguientes criterios   *

-   Se debe proporcionar toda la geometría del casco (incluyendo los cuerpos simétricos).
-   La geometría de estribor debe incluirse en el dominio *y* negativo.
-   El punto de origen (0,0,0) es la intersección de la **sección media** (punto medio entre la perpendicular de popa y la de proa) y la **línea base**.

![Vista esquemática del criterio de signos.](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

Criterio de signos de FreeCAD-Ship.


</center>

### Cargando la geometría del Serie 60 

Para ayudar a los nuevos usuarios, el banco de trabajo Ship incluye un cargador de ejemplos de geometrías, con los siguientes para elegir   *

-   Serie 60 de la Universidad de Iowa
-   Buque canónico de Wigley
-   Catamarán de la serie 60
-   Catamarán de Wigley

![Icono del cargador de geometrías de naves de ejemplo](images/Ship_Load.svg )


<center>

Icono del cargador de ejemplos de geometrías de naves


</center>

Ejecutando la herramienta (Diseño de buques/Cargar un ejemplo de geometría de nave) se mostrará un cuadro de diálogo. Selecciona **Serie 60 de la Universidad de Iowa** y pulsa Aceptar. La herramienta carga un nuevo documento con la geometría **s60\_IowaUniversity**.


**'''¡Atención, antes de editar nada!''
Ahora está trabajando con el archivo de ejemplo original.
Para preservar el ejemplo original sin editar, '''debes guardarlo primero como un nuevo archivo antes de editar nada'''**

.

## Crear instancia del nave 

Para crear una **Instancia de nave** selecciona la geometría s60 y ejecuta la **herramienta de creación de nave** (Diseño de buques/Crear un nuevo nave).

![Herramienta de creación nave](images/Ship_Logo.svg )


<center>

Icono de la herramienta de creación de naves


</center>

Se mostrará el diálogo de la tarea de creación de una nave y algunas anotaciones en la [vista 3D](3D_view/es.md). Las anotaciones desaparecerán cuando cierres la herramienta de creación de naves, así que no te preocupes por esto.

Se deben introducir los datos más relevantes del nave (el <img alt="" src=images/Workbench_Ship.svg  style="width   *24px;"> El ambiente de trabajo nave utiliza un sistema de introducción de datos progresivo, por lo que las operaciones básicas pueden realizarse conociendo sólo los datos básicos del nave, siendo necesaria más información a medida que las operaciones se hacen más complejas).

### Datos del nave 

Las principales dimensiones deben ser introducidas aquí   *

-   Eslora   * Eslora entre perpendiculares, 25,5 m para este nave.
-   Manga   * Manga total del nave, 3,389 m para este nave.
-   Calado   * Calado de diseño, 1,0 m para este nave.

![Anotaciones sobre la vista frontal.](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Anotaciones sobre la vista frontal.


</center>

La eslora entre perpendiculares depende del calado de diseño, por tanto si no se conoce la eslora entre perpendiculares se puede fijar el calado y ajustar la eslora hasta que coincida con la intersección entre la roda (línea tope de la proa) con la flotación.

![Anotaciones sobre la vista lateral.](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Anotaciones sobre la vista lateral.


</center>

Se puede seguir la misma metodología para proceder con la manga. Conviene darse cuenta que se trata de la manga total, luego se debe considerar el nave completo, aunque la anotación sólo marque el costado de estribor.

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

El dibujo de líneas es un conjunto de líneas de cortes de sección en los 3 ejes, que finalmente mostrarán la geometría del casco en un Plano de Líneas. Necesitamos proporcionar las líneas para las 3 siguientes vistas   *

-   Plano del cuerpo (usando los cortes transversales)
-   Plano de la carena (usando los cortes longitudinales)
-   Plano de media manga (usando los cortes de líneas de agua)

### Cortes transversales 

Normalmente se deben realizar 21 secciones transversales equidistantes entre perpendiculares. para ello FreeCAD proporciona una herramienta automática para poder hacerlo, simplemente selecciona el tipo de secciones **Transversales**, ve a la casilla **Auto crear** y pon **21** secciones, luego pulsa **Crear secciones**

![Vista previa de las cuadernas.](images/S60OutlineTransversal.png )


<center>

Vista previa de las cuadernas.


</center>

Se rellena la tabla de secciones y se muestra la vista previa de secciones llamada **OutlineDraw**. Normalmente se añaden más secciones en proa y popa, donde se registran curvaturas más complejas, para ello

1.  Ir al final de la tabla y hacer *doble clic* en un elemento vacío para editarlo.
2.  Pulse **intro** para confirmar.
3.  Agregue las siguientes secciones   *

   *   

       *   X~22~ = -12.1125 m
       *   X~23~ = 12.1125 m

Dependiendo de la complejidad de la geometría, la previsualización puede llevar algún tiempo.

### Cortes longitudinales 

Hay que añadir dos cortes longitudinales, por lo que hay que seleccionar el tipo de secciones **Longitudinales**, ir a la casilla **Creación automática**\' y poner **2** secciones, luego pulsar **Crear secciones**. Tabla de secciones se llena, y la vista previa de las secciones actualizadas.

### Líneas de agua 

6 Líneas de agua entre la línea de base y el proyecto de diseño debe ser añadido, así que seleccione **Líneas de agua** tipo de secciones, vaya a **Auto crear**\' caja y establecer **5**\' (Z = 0 m no se considerará, añadir manualmente si lo necesita) secciones, a continuación, pulse **Crear secciones**. La tabla de secciones se llena, y la vista previa de las secciones se actualiza.

Hay que añadir varias líneas de agua adicionales   *

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m

### Realizar el trazado 

Selecciona la escala **1   *100** y pulsa **Aceptar** para que la herramienta genere las secciones 3D en un nuevo objeto.

![Plano de formas.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Plano de formas.


</center>

Para trazar estas secciones puedes utilizar el [Ambiente de trabajo de dibujo](Drawing_Workbench/es.md)   *

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

El calado y el trimado (ángulo de rotación del *borde y* del casco, positivo si el calado de popa puede aumentar) deben ser proporcionados. Se pueden realizar varias curvas de áreas, dependiendo de las situaciones de carga del buque, pero se deben realizar dos trazados típicos   *

-   Curva de áreas transversales de diseño   * Sin ángulo de trimado y utilizando el calado de diseño, 1,0 m en este caso.
-   Curva de áreas transversales de máximo calado   * Sin ángulo de trimado y con el máximo calado permitido, 2,0 m en este caso.

### Datos de salida 

Se muestran algunos datos relevantes en tiempo real   *

-   **L**   * Longitud entre perpendiculares, valor establecido en la creación de la instancia de la nave.
-   **B**   * Viga seleccionada en la creación del nave.
-   T\'\'\'   * Calado real en el centro del nave.
-   **Trim**   * Ángulo de trimado.
-   T~AP~\'\'   * Después del calado perpendicular.
-   T~FP~\'\'   * Calado perpendicular a proa.
-   **Desplazamiento**   * Desplazamiento del buque (considerado el agua salada, dividir por 1,025 para conocer el volumen desplazado).
-   XCB\'\'\'   * Coordenada X del punto central de flotación (relativa a la sección media del nave).

Cuando se pulsa el botón **Aceptar** se realiza un trazado (dependiendo de la complejidad de la geometría puede llevar algún tiempo, puedes ver el progreso en el terminal, y detener el trabajo pulsando **Ctrl**+**C**). Cuando la tarea ha terminado FreeCAD generará un gráfico (ver la documentación del [Ambiente de trabajo diagrama](Plot_Workbench/es.md)) y una hoja de cálculo (ver la documentación del [Ambiente de trabajo Hoja de cálculo](Spreadsheet_Workbench/es.md)).

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

Al lanzar la herramienta se muestra el cuadro de diálogo donde deberemos establecer los valores de trimado y calados. Normalmente las curvas hidrostáticas se presentan en un rango de calados para cada ángulo de trimado. En este tutorial sólo consideraremos el nave sin trimar, y puesto que no conocemos las situaciones de carga, para un amplio rango de calados (Convencionalmente se ajustan al rango de calados plausible para el buque).

Por tanto establecemos los siguientes valores   *

-   **Trimado** = 0º
-   **Calado mínimo** = 0.1 m
-   **Calado máximo** = 2.0 m
-   **Numero de puntos** = 39. Un gran número de puntos implica largos tiempos de cálculo, y en ocasiones las diferencias no serán perceptibles. Para el número propuesto el cálculo puede llevar un minuto aproximadamente.

Cuando se pulsa el botón **Aceptar** se realizan gráficos (ver la documentación de [Ambiente de trabajo diagrama](Plot_Workbench/rs.md)) y se genera una hoja de cálculo (ver la documentación de [Ambiente de trabajo hoja de cálculo](Spreadsheet_Workbench/es.md)).

![Curvas hidrostáticas.](images/FreeCAD-Ship-HydrostaticsCurves.jpg )


<center>

Curvas hidrostáticas.


</center>

## Seguir aprendiendo 

El [Tutorial de FreeCAD-Nave s60 (II)](FreeCAD-Ship_s60_tutorial_(II)/es.md) es el segundo capítulo de la serie 60 de la nave universitaria de Iowa.

[Category   *Ship](Category_Ship.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial/es
