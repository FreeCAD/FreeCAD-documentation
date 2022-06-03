---
- TutorialInfo   */es
   Topic   * Part Workbench
   Level   * Beginner
   Time   *
   Author   *
   FCVersion   *
   Files   *
---

# Engine Block Tutorial/es

 }


<div class="mw-translate-fuzzy">




</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width   *300px;">


</div>


<div class="mw-translate-fuzzy">

Este es un tutorial de introducción al modelado en FreeCAD. El propósito del tutorial es introducirte a los tipos de datos primitivos para los objetos paramétricos, operaciones booleanas, croquizado 2D, y el proceso de convertir croquis 2D en modelos 3D. purposes of the tutorial are to introduce you to the primitive data types for parametric objects, boolean operations, 2D drafting, and the process of converting 2D drafts into 3D models. Como ejemplo de trabajo modelaremos el bloque de un motor simple y el cárter visto a la derecha.


</div>


<div class="mw-translate-fuzzy">

## Empezando

Para empezar, abre FreeCAD, ve a *Archivo -\> Nuevo* para crear un nuevo documento, y luego a *Archivo -\> Guardar* para guardarlo en tu equipo, he llamado a mi proyecto \'Engine\'. Habrás notado que después de guardar el proyecto, la *vista en árbol* a la izquierda de la pantalla mostrará el nombre del proyecto en el que estas trabajando. Puedes tener más de un proyecto abierto a la vez y cada proyecto se mostrará como la raíz de un árbol en la vista en árbol.


</div>


<div class="mw-translate-fuzzy">

## Definiendo el bloque 

Ahora empezaremos a trabajar en el modelo actual. Comenzaremos añadiendo un cubo para el contorno del bloque motor. Para ello necesitamos añadir una *pieza* al modelo, ve a Vista-\>Entorno-\>Pieza para seleccionar el [Módulo de Pieza](Part_Workbench/es.md). Observaras que después de seleccionar el entorno, tienes una configuración de barras de botones diferente en las barras de herramientas de arriba. Cambia a algunos de los otros entornos para familiarizarte con el sistema de entornos y luego vuelve al módulo de pieza.


</div>


<div class="mw-translate-fuzzy">

### El alojamiento 

En el módulo de pieza verás un puñado de iconos para crear objetos primitivos como cubos, esferas, conos, etc. Pulsa el icono del cubo (<img alt="" src=images/Part_Box.png  style="width   *16px;">) para añadir un cubo a la escena. Cada una de las primitivas listada tiene un conjunto de parámetros que son definidos cuando se añade la primitiva. Si quieres puedes añadir un tipo de cada primitiva para ver como son. Las primitivas se pueden eliminar de la escena seleccionándolas y pulsando la tecla de suprimir. Existen dos modos de seleccionar objetos, puedes pulsar con el botón izquierdo del ratón en la vista 3D, o hacer clic sobre ellos en la vista en árbol. En ambos casos, manteniendo la tecla CTRL pulsada te permitirá seleccionar múltiples elementos. Puedes hacer un zoom en la vista 3D moviendo la rueda de tu ratón. Para encuadrar la vista pulsar el botón del medio y mover el ratón. Para girar la vista mantén presionado el botón central del ratón y sin soltarlo presiona el botón izquierdo y mueve el ratón. Tambien puedes hacer clic con el botón del medio en alguna parte de tu modelo 3D para hacer que la vista gire alrededor de dicho punto. También, los números 1-6 y el 0 te mostrarán carias vistas de la escena (planta, alzado, axonométrica, etc.). Dedica un minuto o dos habituándote con la manipulación de las vistas 3D.


</div>


<div class="mw-translate-fuzzy">


   *   *Lectura adicional   * [Navegando en el espacio 3D](Mouse_Model/es.md)*


</div>


<div class="mw-translate-fuzzy">

Una vez que tengas el cubo y estés habituado al funcionamiento del ratón, comenzaremos definiendo las dimensiones del modelo CAD. Selecciona el cubo haciendo clic en la vista en árbol y pulsa en la pestaña \'Datos\' en la *Vista de Propiedades* ubicada debajo de la vista en árbol (ve a *Vista -\> Vistas -\> Vista de Propiedades* di la has cerrado). En la pestaña Datos puedes modificar las propiedades del objeto que has seleccionado. Dependiendo del tipo de objeto seleccionado habrá diferentes parámetros para establecer en la pestaña de Datos. Para un cubo necesitamos 3 vectores, uno para su ubicación en el espacio 3D, otro para su orientación, y el tercero para especificar sus dimensiones. Para una esfera podrías especificar el centro, y el radio; Los conos tienen un radio,a altura y posición; etc. Estamos construyendo un pequeño bloque motor de 2 cilindros de modo que establece el tamaño y posición del cubo a los valores siguientes (asegúrate de que pones los XYZ en la \'Posición\', los de \'Eje\' establecen el eje de rotación y los valores por defecto están como queremos)   *


</div>


<div class="mw-translate-fuzzy">


   *   {\| class=wikitable border=1

\|- \| X   * 0.0 mm \|\| Altura   * 110.0 mm \|- \| Y   * -40.0 mm \|\| Largo   * 140.0 mm \|- \| Z   * 0.0 mm \|\| Ancho   * 80.0 mm \|- \|}


</div>


<div class="mw-translate-fuzzy">

Ahora que tienes el bloque motor dimensionado adecuadamente deberíamos darle un nombre de descripción. Selecciónalo en la vista en árbol y pulsa en el botón derecho para renombrarlo o presiona la tecla *F2*. Llámalo \"Alojamiento\'.


</div>


<div class="mw-translate-fuzzy">

### El primer cilindro 

Después tallaremos el primer cilindro a través de todo el bloque motor. Para ello añadiremos un cilindro al modelo con el tamaño que queramos abrir y haremos una operación booleana para \"restar\" el material del bloque. Pulsa el icono para añadir un cilindro (<img alt="" src=images/Part_Cylinder.png  style="width   *16px;">) y luego selecciónalo y establece sus propiedades a las siguientes   *


</div>


   *   {\| class=wikitable border=1

\|- \| X   * 40.0 mm \|\| Altura   * 110.0 mm \|- \| Y   * 0.0 mm \|\| Radio   * 25.0 mm \|- \| Z   * 0.0 mm \|\| \|- \|}


<div class="mw-translate-fuzzy">

Una vez que las propiedades estén establecidas correctamente deberías ver las caras circulares del cilindro en las partes superior e inferior del bloque motor. Llámalo *Cilindro 1* seleccionándolo en la vista en árbol.


</div>


<div class="mw-translate-fuzzy">

### El segundo cilindro 

Podríamos hacer el segundo cilindro del mismo modo, sin embargo es mucho más sencillo copiar el primer cilindro y cambiar la coordenada X de su ubicación. Para ello, selecciona el *Cilindro 1* y ve a *Editar -\> Duplicar selección*. Verás que el segundo cilindro aparece en la vista en árbol (llámalo *Cilindro 2*), pero no lo verás en la vista 3D ya que está ubicado en la misma posición que el primer cilindro. Ahora selecciona el *Cilindro 2* en la vista en árbol y cambia su coordenada X por 100 mm. Observarás que como se ha movido el cilindro en la vista 3D. Una vez que el segundo cilindro esté debidamente ubicado puedes verlo seleccionando el *Alojamiento* y pulsando la *barra espaciadora* para ocultarlo (Observa que los objetos ocultos están difuminados en la vista en árbol). Oculta los tres objetos uno a uno y luego vuelve a mostrarlos pulsando de nuevo la barra espaciadora al seleccionarlos en la vista en árbol.


</div>

### Tallando los cilindros 

<img alt="" src=images/_Engine_Block_Tutorial_-_Bored_Block.png  style="width   *300px;">


<div class="mw-translate-fuzzy">

Ahora que ambos cilindros están en su ubicación los utilizaremos para tallar el bloque. Para ello utilizaremos *operaciones booleanas* en nuestras 3 primitivas. Comenzaremos haciendo una unión de los dos cilindros. Selecciona el *Cilindro 1* y pulsa *CTRL* para seleccionar también el *Cilindro 2*. Ahora pulsa el icono de Unión (<img alt="" src=images/Part_Fuse.png  style="width   *16px;">) para fusionar los objetos. Observarás que en la vista en árbol, ahora hay un objeto llamado *Fusion*. Si pulsas el icono de la flecha a la izquierda de su nombre en la vista en árbol verás los dos cilindros, pero su nombre se ha difuminado. En lugar de Fusion, lo renombraremos como *Cilindros*. Ahora tallaremos el bloque motor. Selecciona el *Alojamiento* y *luego* los *Cilindros* y presiona el icono de Cortar (<img alt="" src=images/Part_Cut.png  style="width   *16px;">). Los dos objetos seleccionados se combinaran de nuevo y el resultado se llamará *Cut* (que podrías renombrar a *Bloque tallado*). Presiona la tecla *2* para ver la vista en planta, deberías ver a través de los agujeros de los cilindros en el bloque motor. A la derecha puedes ver como debería quedar.


</div>

### La ventaja clave del modelado paramétrico 

Ahora que hemos tallado los cilindros tomaremos un momento para ver una de las ventajas de este sistema. Supongamos que en algún punto de nuestro desarrollo, nos damos cuenta de que queremos los cilindros un poco mayores. Debido a que las operaciones se guardan y agrupan en la vista en árbol, podemos cambiar el tamaño de los cilindros y FreeCAD simplemente recalculará la unión y la diferencia. Prueba a modificar el radio y la posición de los dos cilindros y luego vuelve a dejarlos como se indicaba arriba.

## El cárter 

### Alojamiento y tapas del acoplamiento 


<div class="mw-translate-fuzzy">

A continuación trabajaremos en el cárter bajo el bloque motor. Añade un nuevo cubo, renombralo a we will work on a crankcase under the engine block. Add a new box, rename it to *Alojamiento del cárter*, y asignale las siguientes propiedades   *


</div>


<div class="mw-translate-fuzzy">


   *   {\| class=wikitable border=1

\|- \| X   * 0.0 mm \|\| Height   * 85.0 mm \|- \| Y   * -50.0 mm \|\| Length   * 140.0 mm \|- \| Z   * -85.0 mm \|\| Width   * 100.0 mm \|- \|}


</div>


<div class="mw-translate-fuzzy">

Para separar el cárter le daremos un color diferente. Puedes cambiarlo pulsando con el botón derecho y seleccionando Apariencia. Puedes asignarle un color tu mismo o darle al objeto un color aleatorio (selecciona color aleatorio de nuevo si no te gusta el color). Añade otro cubo llamado *Tallado de acoplamiento*, y asignale las siguientes propiedades, y luego corta el *Tallado de acoplamiento* del *Alojamiento del cárter* (selecciona primero el *Alojamiento del cárter*)   *


</div>

Add another box called **Bearing carve**, give it the following properties, and then cut the **Bearing carve** away from the **Crankcase Billet** (i.e. select the billet first)   *


<div class="mw-translate-fuzzy">


   *   {\| class=wikitable border=1

\|- \| X   * 0.0 mm \|\| Height   * 30.0 mm \|- \| Y   * -40.0 mm \|\| Length   * 140.0 mm \|- \| Z   * -85.0 mm \|\| Width   * 80.0 mm \|- \|}


</div>


<div class="mw-translate-fuzzy">

Renombra el corte resultante como *Cárter tallado*.


</div>


<div class="mw-translate-fuzzy">

### Tallando el alojamiento del eje 

Lo siguiente que haremos será un corte semicircular para situar el cigüeñal. Comenzaremos con un cilindro, pero la orientación por defecto del cilindro es vertical, y necesitamos uno horizontal. Esto significa que debemos enterarnos de como girar el cilindro para alinearlo correctamente con nuestro motor. Queremos el cigúeñal a lo largo del eje X, esto significa que desde su ubicación por defecto necesitamos girarlo 90º alrededor del eje Y. Crea un cilindro llamado *Tallado del Cigúeñal* y asignale estas propiedades (Observa que tenemos que especificar el parámetro de orientación además de las dimensiones y posición de los casos anteriores)   *


</div>


   *   {\| class=wikitable border=1

\|- \| Axis X   * 0.0 mm \|\| Angle   * 90.0 degrees \|- \| Axis Y   * 1.0 mm \|\| \|- \| Axis Z   * 0.0 mm \|\| \|- \| Position X   * 0.0 mm \|\| Height   * 140.0 mm \|- \| Position Y   * 0.0 mm \|\| Radius   * 20.0 mm \|- \| Position Z   * -55.0 mm \|\| \|- \|}


<div class="mw-translate-fuzzy">

Corta el *Tallado del Cigúeñal* del *Cárter tallado* y renombralo como *Cárter con alojamientos*.


</div>

### Terminando el cárter 


<div class="mw-translate-fuzzy">

Para terminar cortaremos dos cubos para que las bielas de los pistones puedan pasar del cárter al bloque motor. Crea dos cubos llamados *Cubo tallado 1* y *Cubo tallado 1* con las siguientes propiedades, únelos en un objeto llamado *Cubos tallados*, y córtalos del *Cárter con alojamientos*, llamando al resultado final \"Cárter\". Recuerda que puedes ocultar el bloque motor.


</div>


<div class="mw-translate-fuzzy">


   *   {\| class=wikitable border=1

\|- \| X   * 15.0 mm \|\| Height   * 55.0 mm \|- \| Y   * -25.0 mm \|\| Length   * 50.0 mm \|- \| Z   * -55.0 mm \|\| Width   * 50.0 mm \|- \|}


</div>


<div class="mw-translate-fuzzy">


   *   {\| class=wikitable border=1

\|- \| X   * 75.0 mm \|\| Height   * 55.0 mm \|- \| Y   * -25.0 mm \|\| Length   * 50.0 mm \|- \| Z   * -55.0 mm \|\| Width   * 50.0 mm \|- \|}


</div>

<img alt="" src=images/_Engine_Block_Tutorial_-_Crankcase.png  style="width   *300px;">

A la derecha puedes ver el resultado final. Lo siguiente que haremos es utilizar el modo de croquizado para diseñar el patrón de pernos de fijación y eliminar gran parte del material que recubre los cilindros del bloque motor.

## Croquizado 2D del diseño de la junta del bloque motor 

Para los pernos de fijación y la forma del bloque motor utilizaremos más operaciones booleanas para \"tallar\" la partes del bloque que no queremos.


<div class="mw-translate-fuzzy">

### Entrando al modo de croquizado 2De 

Lo primero que tenemos que hacer es cambiar al entorno de Croquizado 2D, seleccionando *Croquizado 2D* en la lista desplegable de la barra de herramientas superior, que actualmente dice *Pieza* o desde *Vista -\> Entornos*. Incluso aunque vamos a hacer un dibujo 2D seguiremos trabajando en la vista en 3D, diciéndole a FreeCAD en que plano vamos a trabajar. Después de activar el entorno de Croquizado 2D se mostrará la barra de comandos de croquis, a la derecha de ella se mostrarán varios iconos. Si pulsamos en el icono que está más a la izquierda nos permitirá especificar el plano de trabajo. Permite indicar una equidistancia y seleccionar algunos planos predefinidos   * XY, XZ, YZ, Vista, y Ninguno. Los tres primeros son la planta, el alzado y el perfil, *Vista* utilizará el plano perpendicular a la dirección de la vista, y la última opción no proyectará sobre ningún plano dejando definir las completamente las coordenadas XYZ para cualquier punto. Seleccionamos la opción XY e indicamos un valor de 110 en el cuadro de texto de Equidistancia para trabajar en un plano paralelo al XY localizado a 110 mm de altura.


</div>


<div class="mw-translate-fuzzy">

Aunque todo lo que dibujemos se proyectará sobre el plano de trabajo independientemente de cual sea la vista 3D actual, puede ser útil situar la vista perpendicular al plano actual. Pulsa la tecla 2 del teclado para activar la vista en planta.


</div>


<div class="mw-translate-fuzzy">

### Dibujando los pernos 

Selecciona el icono *Circunferencia* (<img alt="" src=images/Draft_Circle.png  style="width   *16px;">). FreeCAD te preguntará por la ubicación del centro y por el radio. Puedes indicarlos con el ratón en el área gráfica o con el teclado. Añadir elementos croquizados con el ratón es más sencillo y rápido, pero no es muy preciso. Dibujaremos 3 circunferencias en las coordenadas y con los radios indicados a continuación.


</div>

Adding drafting elements with the mouse is fast and easy, but it is not very precise. For the actual bolt pattern we use the fact that moving the mouse will update the numbers in the text boxes just above the 3D view so we can see roughly the coordinates of where we want to place things. Once we have these rough coordinates we can type in the real values we want for precise positioning. Reset to the top view of the engine, click the *Add circle* button, and move your mouse around the top left corner of the engine block taking not of a good location for the head bolt. It looks like X=10, Y=30, would be a good place for the circle (note the Z coordinate should be grayed out, if it is not you need to set the plane properly like in the previous section, pressing escape will cancel drawing the circle).

Now that you see how to easily determine the coordinates of drawing elements you can easily design a bolt pattern or other 2 dimensional layout for a part such as fluid channels, circuit-board traces, etc. For our 3 head bolts let\'s on this side of the engine, let\'s use the following coordinates. Note that when you are typing in values to the boxes you can press enter to move on to the next box, and it is also a good idea to move your mouse out of the 3D view before you start typing in the coordinates as too much mouse movement will overwrite the numbers you have already entered in the text entry fields. Also, on my system I had trouble with the typed in circles having their Z coordinates set to 12.5 for some reason, if this is a problem for you, you can set the drawing projection plane to *None* and then manually enter the Z coordinates for the circles to be 110. Finally, when creating the circles, make sure to check the box labeled *Filled* otherwise when we extrude them later they will just create tubes like a toilet paper tube instead of a solid cylinder.

   *   {\| class=wikitable border=1

\|- \| X1   * 10 \|\| Y1   * 25 \|\| Radius   * 2.5 mm \|- \| X2   * 70 \|\| Y2   * 25 \|\| Radius   * 2.5 mm \|- \| X3   * 130 \|\| Y3   * 25 \|\| Radius   * 2.5 mm \|}


<div class="mw-translate-fuzzy">

Llama a estas circunferencias *Perno 1* *Perno 2* y *Perno 3*.


</div>


<div class="mw-translate-fuzzy">

### El otro lado del bloque 

Ahora que los tres primeros pernos están situados de un lado del bloque motor, necesitamos otros tres del otro lado, hay tres formas de crearlos   *

-   Añadiendo circunferencias como hicimos antes.

-   Seleccionando los tres que hemos creado antes y copiandolos y moviendolos a su ubicación, al igual que hicimos con los dos cilindros iniciales.

-   Utilizar la funcionalidad de simetría.

Como ya hemos visto las dos primeras opciones, vamos a utilizar la tercera. Volvemos a activar el entorno de *Pieza* y pulsamos el icono de Simetría (<img alt="" src=images/Part_Mirror.png  style="width   *16px;">). Se mostrará a la izquierda de la pantalla la Vista de Tareas, donde antes veíamos la pestaña Vista del Proyecto, un letrero en el que se pueden especificar los parámetros del comando Simetría. Selecciona *Perno 1* de la lista en la Vista de Tareas e indica como de Simetría el XZ, presiona OK (haz lo mismo con *Perno 2* y *Perno 3*).


</div>

Since you should already know how to do the first and second way, we will choose the third way for this example model. Each of the three methods has its own advantages and disadvantages, but a good operating rule is that simple models (like this one) probably should use the first or second methods, whereas models with lots of duplication and/or duplication of very complicated shapes/objects should probably use the third method.

So even though it is a bit of overkill we will mirror these bolts as a demonstration. Switch back to the part workbench (note that you can always switch to the *Complete* workbench to see all the tools at once if you would rather not switch back and forth (deprecated since v0.17)) by going to **View → Workbench**. Select the three bolt circles in the tree view, and then press the mirror button (<img alt="" src=images/Part_Mirror.svg  style="width   *16px;">). Once you press the mirror button you should notice a new display called the *Combo view* pop up on in the pane underneath the Tree view. Many of the tools need additional input before they can run and the Combo view lets you enter these parameters. You can make the Combo view larger by dragging the divider line separating it from the Property view up or down. Select **Bolt 1** from the list on the Combo view and set the *mirror plane* to XZ, then press OK (do the same for bolts 2 and 3).

At this point you should have a basic engine block with the cylinders bored out and the headbolt locations marked.

### Eliminando el material excedente del bloque motor 

Ahora que tenemos los taladros marcados para los pernos queremos recortar la parte exterior del bloque con una forma más conveniente. Esto hará el motor más ligero, permitirá que se enfríe mejor y se utilizará menos material para fundir el bloque. Al igual que con el los pernos crearemos un croquis 2D con la forma exterior que deseamos para el producto final. Utilizaremos geometría constructiva 2D para servir como referencia al trazar una spline con la forma exterior del bloque.

Como guía dibujaremos dos polígonos regulares concéntricos con cada cilindro. Cambia a la vista en planta , oculta el cárter y haz visible el bloque motor, cambia al entorno de croquizado 2D seleccionando el plano de trabajo XY y una equidistancia de 110 mm (tal como se hizo anteriormente). Activa el icono del *modo de Geometría Constructiva* en la barra de comandos (el icono representa una paleta y está justo al lado de donde hemos indicado el plano de trabajo). El modo de Geometría Constructiva funciona exactamente como el modo normal, pero los objetos se dibujan con un color diferente y se añaden automáticamente en un grupo separado en la vista en árbol.

   *   *Lectura adicional   * [Modo de Geometría Constructiva](Draft_ToggleConstructionMode/es.md)*


<div class="mw-translate-fuzzy">

Pulsa en el icono para crear un *Polígono regular* (<img alt="" src=images/Draft_Polygon.png  style="width   *16px;">) y mueve tu ratón sobre la arista de uno de los cilindros mientras presionas la tecla CTRL. Deberías ver como el cursor se ajusta al eje del cilindro, selecciona dicho punto haciendo clic. El programa pregunta por el número de lados del polígono regular y el radio en el que se inscribirá. Indicamos un radio de 30 e indicamos 14 para el número de lados. Añade otro polígono centrado en el mismo punto pero de radio 45 mm y 22 lados. Para terminar añade otros dos polígonos exactamente iguales en el otro cilindro. Cuando termines, deberías tener dos figuras \"polygon\".


</div>

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline.png  style="width   *300px;">


<div class="mw-translate-fuzzy">

Ahora dibujaremos una spline para definir el exterior del bloque motor. Como esta va a ser parte del objeto final, desactiva el modo de Geometría Constructiva y selecciona el icono para añadir una spline (<img alt="" src=images/Draft_BSpline.png  style="width   *16px;">) apoyándote en los vértices de los polígonos anteriores seleccionándolos mientras se pulsa la tecla CTRL. Cuando estés a punto de volver a indicar el primer punto, o punto de partida, para cerrar la spline pulsa el icono \"Cerrar\" en la barra de comandos de Croquizado.


</div>

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline_Edit_Mode.png  style="width   *300px;">

The control points are not shown in that picture so I have added a second screenshot showing the finished spline in edit mode (click the *Edit mode* button to turn editing on or off for the selected object, make sure to turn it off when you are done editing it or just skip over this step if you are satisfied with your engine block shape). Also, note that there is a discontinuity on the leftmost edge of the spline curve, even though it is closed properly, this is a bug in the program behavior and is currently being fixed, as a result your spline curve may look slightly different if you are running a newer version of the software than is available at this time.

### Extrusión del diseño 2D en el modelo 3D para finalizar el diseño 


<div class="mw-translate-fuzzy">

Vuelve al entorno de pieza y selecciona el icono *Extruir croquis* (<img alt="" src=images/Part_Extrude.png  style="width   *16px;">). En el combobox mostrado utiliza CTRL para seleccionar las 6 circunferencias y el contorno cerrado definido por la spline. La dirección por defecto es en el sentido del eje Z positivo, pero nosotros queremos extruirlo hacia abajo, de modo que la cambiamos a X=0, Y=0 y Z=-1, después indicamos 110 para la longitud (la altura del bloque motor) y pulsamos OK. En este momento todos los objetos extruidos se llaman \"Extrude001\...\" así que los renombraremos como *Taladro Perno 1*, *Taladro Perno 2*\... hasta el *6* y a la extrusión de la spline *Spline extruida*. Vuelve a visualizar todos los componentes ocultos.


</div>

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width   *300px;">


<div class="mw-translate-fuzzy">

Selecciona los 6 objetos *Taladro Perno 1*, *Taladro Perno 2*\... y únelos llamando al resultado *Taladros de los Pernos*. Luego selecciona el \"Bloque taladrado\" y los *Taladros de los Pernos* en ese orden y realiza una operación booleana de corte llamando al resultado *Bloque con taladros*. Finalmente, selecciona el *Bloque con taladros* y el *Spline extruida* en ese orden y selecciona la operación booleana *Intersección* (<img alt="" src=images/Part_Common.png  style="width   *16px;">), y llama al resultado *Bloque motor*. El resultado final debería ser similar al de la imagen de la derecha.


</div>

Your final object should look like the picture on the right.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Engine Block Tutorial/es
