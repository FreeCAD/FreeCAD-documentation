# Aeroplane/es
{{TutorialInfo/es
|Topic=Part Workbench
|Level=Beginner
|Time=10 minutes
|Author=Hughthecat
|FCVersion=
|Files=
}}

## Primeros pasos 

Trabajaremos en el <img alt="" src=images/Workbench_Part.svg  style="width:24px;">[Ambiente de trabajo Piezas](Part_Workbench/es.md) - selecciona el módulo de piezas en **Vista → Entorno → Pieza** o desde el [Selector Ambiente de trabajos](Workbench_Selector/es.md).

-   Crea un nuevo documento vacío.
-   Cambia a <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [vista isometrica](Std_ViewIsometric/es.md).
-   Alternar la cruz del eje **ON** (a través del menú Vista).
-   Asegúrese de que tiene la [Combo Vista](Combo_view/es.md) mostrando (a través de **Vista → Vistas**).

-   Crea un cilindro pulsando en el botón <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Cilindro](Part_Cylinder/es.md).
-   Selecciónelo haciendo clic en Cilindro en el visor de proyectos.
-   Haz clic en la pestaña Datos en la parte inferior del visor de proyectos.

Cambia la altura a 20mm. Deja el radio en 2mm.

Haga clic en [Colocación](Placement/es.md) (fíjate en la pequeña **[+]**) y aparecerá un botón con tres puntos **...**. Haga clic en él. (También puede seleccionar: **Menú → Editar → Colocación**) Aparecerá el visor de tareas.

<img alt="" src=images/HTCaeroplane01.png  style="width:300px;">

Si no está familiarizado con los ejes XYZ, juegue con los números del cuadro de traducción. Cuando termine de jugar haga clic en el botón **Reset**.

## Segundos pasos 

<img alt="" src=images/HTCaeroplane02.png  style="width:400px;">

Ahora vamos a rotar el cilindro de forma que se sitúe a lo largo del eje X. Para ello hay que rotarlo alrededor del eje Y. El cuadro de Rotación debe decir \'Eje de rotación con ángulo\' así que cambie el Eje a Y e incremente el Ángulo hasta que llegue a 90. Haga clic en **OK**.

Me gustaría practicar con la rotación de la vista en este momento. Deberías ver la \'costura\' del cilindro en la parte inferior.

<img alt="" src=images/HTCaeroplane03.png  style="width:400px;">

Ahora vamos a añadir y modificar una caja así que haz clic en el botón <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/es.md). Selecciónalo haciendo clic en Caja en el visor de proyectos. Cambia el Alto a 1mm, el Largo a 5mm y el Ancho a 20mm.

Haga clic en [Colocación → **...**](Placement/es.md) para obtener el visor de Tareas. Utilizando el cuadro de traducción introduzca Y: -10 y Z: -1. Haga clic en **Aceptar**.

Ahora vamos a fusionar estas dos formas con una operación booleana. Haz clic en el botón <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Operaciones Booleanas](Part_Boolean/es.md) y el visor de Tareas mostrará el selector de Operaciones Booleanas.

Asegúrese de que la Unión está seleccionada, y que el Cilindro y la Caja están marcados una vez en las dos listas de formas. Haga clic en **Aplicar**. Haga clic en **Cerrar**. Ahora tiene un único objeto llamado **Fusión**\'.




Vamos a añadir más cubos para completar nuestro modelo. Crea un cubo, Selecciona el cubo y cambia su altura a 5mm, longitud a 3mm y ancho a 1mm. Cambia su ubicación a Y: -0.5.

Ahora necesitamos unir nuestra Fusión a la Caja001, así que lo haremos de la manera más rápida. Haga clic en Fusion en el visor de proyectos y **Ctrl**+clic en Box001. Esto selecciona ambas partes juntas. Ahora haz clic en el <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fuse](Part_Fuse/es.md) para obtener **Fusion001**.

Ahora debería tener un modelo simple de avión. Haz clic con el botón derecho en **Fusion001** y renómbralo **Aeroplano**.

<img alt="" src=images/HTCaeroplane04.png  style="width:500px;">

Supongamos que tuviéramos que acercar un poco las alas pero si probamos modificando la traslación en X se moverá todo el aeroplano. Sólo queremos mover las alas, de modo que cancela la Ubicación.

Expanda el Aeroplano (haga clic en el {{Botón|[+]}} al lado) y expanda la Fusión.

Haga clic en Caja y obtenga su [Colocación en Tareas](Placement/es.md). Observa que ya tiene Y: -10 y Z: -1 en la Traducción. Cambia la traducción de X a 3 y haz clic en **Aplicar**. Así está mejor. Haga clic en **Aceptar**.




## Rotaciones

Haz clic en Aeroplano y obtén su [Colocación en Tareas](Placement.md). En la sección de Rotación cambia donde dice \'Eje de rotación con ángulo\' por \'Ángulos de Euler\' porque son mucho más fáciles de trabajar.

![izquierda](images/Tache_Placement_Lacet_fr_Mini.gif )**Desvío** es la rotación alrededor del **eje Z**, es decir la rotación de izquierda a derecha. (El ángulo de desvío es **Psi ψ**).  ![izquierda](images/Tache_Placement_Tangage_fr_Mini.gif )**Paso** es la rotación alrededor del **eje Y**, es decir nariz arriba y nariz abajo. (El ángulo de paso es el **Phi φ**).  ![\|izquierda](images/Tache_Placement_Roulis_fr_Mini.gif )**Volteado** es la rotación alrededor del **eje X**, es decir alas arriba y abajo. (El ángulo del rollo es el **Thêta θ**). 

Sin embargo, incluso aquí hay que recordar algunas cosas importantes:

-   Las rotaciones positivas son en el sentido horario del reloj cuando son vistas desde el origen a lo largo de un eje positivo. O dicho de otro modo: Las rotaciones positivas son en sentido antihorario cuando se visualiza desde la parte positiva de un eje hacia el origen.

-   Aunque las tres etiquetas son Desvío, Paso y Volteado no es realmente lo que son. Desvío, Paso y Volteado son referencias a las *coordenadas del cuerpo* de un objeto en el espacio 3D. Las etiquetas deberían ser Encabezado, Elevación y Ladeado o incluso Azimuth, Inclination y Ladeado porque en realidad se refieren a las *coordenadas espaciales* del sistema 3D. Son los *ángulos de Tait-Bryan*. Si quieres más información, prueba [Ángulos de Euler](https://es.wikipedia.org/wiki/%C3%81ngulos_de_Euler#%C3%81ngulos_de_Tait-Bryan).

-   Con el Aeroplano en su posición actual se aplican las siguientes reglas simples. El Encabezado es la rotación alrededor del eje Z, por ejemplo a izquierda o derecha. El ladeo es la rotación alrededor del eje Y, por ejemplo morro arriba o abajo. Volteado es la rotación alrededor del eje X, por ejemplo alas arriba y abajo. Esto está bien para empezar pero no será cierto más adelante!

Practica con los tres giros. Solo necesitas cambiar las cosas unos pocos grados para tener una idea. Resetea cuando termines.

Ahora vamos a ver porque las etiquetas de Desvío, Paso y Volteado no se ajustan realmente. Cambia el Volteado a 90°. El Desvío debería mover la nariz del aeroplano hacia arriba y abajoy el Paso debería moverlo de un lado al otro *como vimos anteriormente*. Lo hacen? No, no lo hacen! El Paso cambia el Desvío y el Desvío cambia el Paso. OK, Resetea.

Así que, un modo mejor de pensar en las rotaciones es que el Desvío cambia la Longitud, el Paso cambia la Latitud y el Volteado cambia la dirección que se está aplicando. Puedes consultar [Convenciones de ejes](http://en.wikipedia.org/wiki/Axes_conventions) para ver otras deswcripciones.

Bien, de vuelta al trabajo. Cambie el Desvío a 45° y el Paso a -30°. Haga clic en Aceptar para mostrar que la operación se ha completado. Ahora vuelva a la [Tarea de Colocación](Placement/es.md) y mire el cuadro de Rotación. Ha vuelto a ser \"Eje de rotación con ángulo\" y tiene unos números extraños en los cuadros Eje y Ángulo. El mío tenía Eje: (0.219493,-0.529904,0.819161) y Ángulo: 53.65°. Los tres números entre paréntesis son las componentes XYZ de un vector unitario en el espacio 3D. Es el eje alrededor del cual nuestro avión original fue rotado para obtener nuestro avión final. El ángulo es el grado de rotación. Inteligente, eh, ¡pero no muy amigable! Fue Euler quien demostró que se podía combinar una serie de rotaciones XYZ en una rotación sobre un eje.

Aquí tienes algunas sugerencias para practicar con el aeroplano:

-   Cambia la coordenada Z de la Ubicación (y aplica) luego cambia los valores de rotación y mira su efecto. Luego prueba cambiando las ubicaciones en X e Y y las rotaciones.
-   Cambia el centro en X (y aplica) luego cambia los valores de rotación y mira el efecto que se produce. Prueba cambiando el centro en Y y Z y las rotaciones.

Espero que este pequeño tutorial te ayude a manejar mejor las rotaciones.


{{Tutorials navi

}}

---
[documentation index](../README.md) > Aeroplane/es
