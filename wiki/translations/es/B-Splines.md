# B-Splines/es
{{TOCright}}

Esta página describe cómo utilizar las B-splines en FreeCAD. También ofrece información sobre qué son las B-splines y para qué aplicaciones son útiles.

## Motivación

Si ya conoces las B-splines y su aplicación, puedes continuar directamente con la sección [B-splines en FreeCAD](#B-splines_en_FreeCAD.md).

Supongamos que quiere diseñar una pieza que debe producirse con una impresora 3D. La pieza debe tener un borde de esta manera:

<img alt="" src=images/B-splines_Motivation-start.png  style="width:450px;">

Hay que imprimir la pieza en dirección de la parte inferior del boceto hacia la parte superior. Las estructuras de soporte externas pueden no ser una opción. Por lo tanto, tiene que añadir un soporte directamente a su pieza. ¿Qué opciones tiene?

-   Opción 1: se podría añadir una línea desde el punto (20, 0) hasta el punto (80, 40):

<img alt="" src=images/B-splines_Motivation-line.png  style="width:450px;">

Sin embargo, esta solución necesita mucho volumen y, por tanto, peso y material.

-   Opción 2: puedes conectar los dos puntos con un arco de círculo. Para ahorrar volumen, el arco debe terminar tangencialmente en el punto (80,40). Entonces tu solución se ve así:

<img alt="" src=images/B-splines_Motivation-circle.png  style="width:450px;">

BIEN. Pero en el fondo no necesitas apoyo inmediato.

-   Opción 3: se podría ahorrar algo más de volumen si la conexión entre los 2 puntos es una curva que empieza tangencialmente en (0, 20) y termina tangencialmente en (80, 40):

<img alt="" src=images/B-splines_Motivation-bezier.png  style="width:450px;">

Así, una curva con la que se puedan conectar dos puntos tangencialmente a un punto de referencia puede ser muy útil para las construcciones. Las curvas de Bézier ofrecen esta característica.

## Curvas Bézier 

### Derivación

Curvas de Bézier son polinomios que describen la conexión entre 2 puntos. El polinomio más sencillo que conecta 2 puntos es una recta ($A*x^1+B$) por lo que también las curvas de Bézier lineales son lineales:

![](images/Bezier_linear_anim.gif ) 
*Animación 1: Curva de Bézier lineal.*

Sin embargo, un polinomio se vuelve primero útil cuando podemos controlarlo. Así que debe haber un punto entre los 2 puntos finales que nos permita definir cómo se conectan los puntos finales. Como en la opción 3 del ejemplo anterior, la curva es útil cuando comienza y termina tangencialmente a las líneas que cruzan los puntos finales. Y esta es una característica principal de las curvas Bézier. Así que vamos a añadir un punto de control entre los 2 puntos finales. La curva comenzará tangencialmente hacia este punto de control, lo que significa que es tangencial a la línea que podemos dibujar entre el punto inicial y el punto de control. Yendo hacia atrás desde el punto final, la curva también será tangente a la línea que podemos dibujar entre el punto de control y el punto final. La animación 2 muestra el aspecto de esta curva.

![](images/Bezier_quadratic_anim.gif )


<div class="mw-translate-fuzzy">



*Animación 2: Curva cuadrática de Bézier. P1 es el punto de control.}
</div>

La animación aclara lo que es básicamente la curva: una transición de P0 a P2 al girar la línea P0-P1 para convertirse en la línea P1-P2. Por lo tanto, obtenemos la bonita característica de inicio/fin tangencial.

Una curva de este tipo sólo puede ser descrita por un polinomio cuadrático. (El número de vueltas a la izquierda/derecha + 1 es el orden necesario del polinomio. Un polinomio cuadrático tiene una sola vuelta, un polinomio cúbico tiene dos vueltas, y así sucesivamente). Por lo tanto, una curva de Bézier con un punto de control es una curva de Bézier cuadrática (de segundo orden).

Tener un solo punto de control a menudo no es suficiente. Tomemos el ejemplo de la motivación anterior. Allí, en la opción 3, terminamos la curva tangencialmente en la dirección x. ¿Pero cómo se pueden conectar los puntos (20, 0) y (80, 40) para que la curva termine tangencialmente en la dirección y? Para conseguirlo se necesita primero un giro a la derecha y luego a la izquierda, es decir, un polinomio cúbico (de tercer orden). Y eso significa que para una curva de Bézier necesitamos (o se puede decir que ganamos) un segundo punto de control. La animación 3 muestra una curva de Bézier cúbica.

[[File:Bezier_cubic_anim.gif]]
{{Caption|Animación 3: Curva cúbica de Bézier.*

Para responder a la pregunta, la solución con el final de la dirección y tangencial para el ejemplo es ésta:

[<img src=images/B-splines_Motivation-cubic-bezier.png style="width:450px">

=== Matemáticas ===

Si estás interesado en entender las matemáticas de fondo, aquí tienes lo básico.

Una curva de Bézier se calcula con esta fórmula:

<math>\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}

\_{\\text{término polinómico}}\\underbrace{\\left(1-t\\right)\^{n-i}t\^{i}}\_{\\text{término polinómico}}\\; \\underbrace{P\_{i}}\_{\\text{coordenada de punto}} 

*n* es por tanto el grado de la curva. Así, una curva de Bézier de grado *n* es un polígono de orden *n*. Los factores $P_{i}$ son, de hecho, las coordenadas de los puntos de control de las curvas de Bézier. Para una visualización, véase [Control de las curvaturas de Bézier](https://pomax.github.io/bezierinfo/#control).

Si le interesa más, eche un vistazo a [Las matemáticas de las curvas de Bézier](https://pomax.github.io/bezierinfo/#explanation) con una derivación muy bien animada de las matemáticas de las curvas de Bézier.

### Reglas

En el texto anterior ya habrás notado algunas \"reglas\" para las curvas de Bézier:

-   El grado del polinomio es también el grado de las curvas.
-   Si necesitas $n$ vueltas, necesitas al menos una curva de Bézier de $n+1$ grado.
-   Una curva de Bézier siempre comienza tangencialmente a la línea entre el punto inicial y el primer punto de control (y termina tangencialmente a la línea entre el último punto de control y el punto final).

## B-Splines 

### Básicos

[Este vídeo](https://www.youtube.com/watch?v=bE1MrrqBAl8) enumera al principio los problemas prácticos de las curvas de Bézier. Por ejemplo, que al añadir o cambiar un punto de control se modifica toda la curva. Estos problemas se pueden resolver uniendo varias curvas de Bézier. El resultado es un llamado spline, en particular un B-spline (spline de base). El vídeo también explica que una unión de curvas de Bézier cuadráticas forma un B-spline cuadrático uniforme y que una unión de curvas de Bézier cúbicas forma un B-spline cúbico uniforme.

De los vídeos podemos recoger \"reglas\" útiles para las B-splines:

-   El primer y último punto de control es el punto final/inicial de la spline.
-   Al igual que para las curvas de Bézier, las splines siempre comienzan tangencialmente a la línea entre el punto de inicio y el primer punto de control (y terminan tangencialmente a la línea entre el último punto de control y el punto final).
-   Una unión de $S$ curvas de Bézier con el grado $D$ tiene $S+D$ puntos de control.
    -   Dado que en la mayoría de los casos se trabaja con B-splines cúbicas podemos afirmar entonces que $N$ puntos de control conducen a $N-3$ segmentos de Bézier y a su vez $N-4$ puntos de unión de segmentos.
-   Una B-spline de grado $D$ ofrece en cada punto una derivada continua de orden $D-1$.
    -   Para una B-spline cúbica esto significa que la curvatura (derivada de segundo orden) no cambia al viajar de un segmento al siguiente. Esta es una característica muy útil como veremos más adelante.

Si está interesado en más detalles sobre las propiedades de la B-Spline, eche un vistazo al vídeo [MOOC Curvas 8.2: Propiedades de las curvas B-spline](https://www.youtube.com/watch?v=xXJylM2S72s).

### Base

El nombre *B-spline* significa *Spline de base*. En lugar de formar la spline como una combinación de curvas de Bézier, el enfoque es modelar **la misma spline** de una manera diferente. La idea es utilizar otro conjunto de polinomios como base. Una combinación lineal de estos polinomios base $B_D(t)$ con el orden $D$ forma la spline B. [En este vídeo](https://www.youtube.com/watch?v=dPPTCy4L4rY) se explica el paso de los puntos de control de Bézier a las funciones base polinómicas que describen el spline. Matemáticamente podemos describir una B-spline con esta fórmula:

$\quad
c(t)=\sum_{k=0}^{N}p_{k}B_{k, D}(t)$

De este modo, $p_k$ es el $k$-ésimo punto de control del spline B y también un factor para el $k$-ésimo polinomio base $B_{k, D}(t)$. Cada polinomio base describe la spline en una región determinada y por lo tanto, mover un punto de control no afecta a toda la spline. Para entender esto, es muy recomendable echar un vistazo a [este vídeo](https://www.youtube.com/watch?v=vjTyWIKviNc) a partir del minuto 2:23.

Como se explica en el vídeo, los polinomios base son polinomios de Bernstein. El conjunto de polinomios de base para una determinada B-spline se puede visualizar de esta manera:

![](images/Bernstein_Polynomials.svg ) 
*Un conjunto de polinomios de Bernstein de orden 4. Describen una B-spline de 4º orden con 5 puntos de control.*

En cada posición de la spline $t$ la suma de polinomios es 1 (indicado por la línea naranja). Al principio sólo influye el polinomio rojo, ya que todos los demás polinomios son allí 0. A mayor $t$ la spline es descrita por una combinación lineal de diferentes polinomios base. En la imagen anterior, cada polinomio es mayor que 1 para todo el rango $0 < t < 1$. Este no es necesariamente el caso. Como se muestra en el vídeo, los polinomios base son básicamente sólo mayores que 0 para un determinado rango de posiciones de la spline. El intervalo en el que un polinomio base es mayor que 0 es descrito por el *vector nudo*. Si está interesado en aprender sobre el vector de nudos, eche un vistazo a [este vídeo](https://www.youtube.com/watch?v=ni5NNPCVvDY).

### B-splines no-uniformes 

Una propiedad de los polinomios de Bernstein es que cuando se observan las diferentes partes de la S-spline Bézier, la longitud del recorrido de cada parte es la misma. (La longitud de la trayectoria suele llamarse *tiempo de recorrido*). Como puedes imaginar, puede ser útil tener B-splines cuyas partes Bézier tengan diferentes longitudes de trayectoria. Esto puede lograrse ponderando los diferentes polinomios:

$\quad
c(t)=\sum_{k=0}^{N}d_{k}B_{k, D}(t)w_k$

$w_k$ es el peso del $k$-ésimo punto de control. Cuando los pesos no son iguales, la B-spline se llama **no-uniforme**.

Especialmente cuando las B-splines deben utilizarse para el modelado en 3D, son necesarias las B-splines normalizadas y no uniformes. La normalización se realiza mediante una división por las funciones base ponderadas. Así, cuando todas las $w_k$ son iguales, obtenemos una B-spline uniforme, independiente del propio peso:

$\quad
c(t)=\cfrac{\sum_{k=0}^{N}d_{k}B_{k, D}(t)w_k}{\sum_{k=0}^{N}B_{k, D}(t)w_k}$

Estas B-splines no-uniformes y racionales (por la división) suelen llamarse **NURBS**\'. Observando su fórmula, vemos que en realidad son una B-spline con una base ponderada $R_{k, D}(t)$:

$\quad
c(t)=\sum_{k=0}^{N}d_{k}R_{k, D}(t)$

mientras que

$\quad
R_{k, D}=\cfrac{B_{k,D}(u)w_k}{\sum_{l=1}^N B_{l,D}(t)w_l}$

## B-splines en FreeCAD 

FreeCAD ofrece la posibilidad de crear B-splines uniformes o no uniformes de cualquier grado en 2D a través del [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md).

### Creación

Para crear B-splines, entra en un sketch y utiliza el botón de la barra de herramientas **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Crear B-spline](Sketcher_CreateBSpline/es.md)**. A continuación, haz clic con el botón izquierdo para establecer un punto de control, mueve el ratón con el botón izquierdo para establecer el siguiente punto de control y así sucesivamente. Finalmente, haz clic con el botón derecho para terminar la definición y crear la B-spline.

Por defecto se crean splines cúbicas uniformes, excepto que no hay suficientes puntos de control para hacerlo. Así que cuando se crea una B-splinecon sólo 2 puntos de control, se obtiene por supuesto una spline que es curva lineal simple de Bézier, para 3 puntos de control se obtiene una curva cuadrática de Bézier, primero con 5 puntos de control se obtiene una spline B cúbica que consiste en 2 segmentos de Bézier.

Para crear B-splines periódicas (B-splines que forman una curva cerrada), utiliza el botón de la barra de herramientas **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [B-spline periódica](Sketcher_CreatePeriodicBSpline/es.md)**. No es necesario fijar el último punto de control sobre el primero porque la B-spline se cerrará automáticamente:

![](images/Sketcher_Periodic-B-spline-creation.gif )

Las B-splines también pueden generarse a partir de segmentos de croquis existentes. Para ello, seleccione los elementos y pulse el botón de la barra de herramientas **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Convertir geometría en B-spline](Sketcher_BSplineApproximate/es.md)**.

### Cambio de grado 

Para cambiar el grado, seleccione la B-spline y utilice el botón de la barra de herramientas **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> [Aumentar grado de la B-spline](Sketcher_BSplineIncreaseDegree/es.md)** o **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> [Decrementar grado de B-spline](Sketcher_BSplineDecreaseDegree/es.md)**.

Nota:\'\'\' Disminuir el grado no puede revertir un aumento anterior del grado, ver la página Wiki [Disminuir el grado de la B-spline](Sketcher_BSplineDecreaseDegree/es.md) para una explicación.

### Cambiar la multiplicidad de nudos 

Los puntos donde se conectan dos curvas Bézier para formar la B-spline se llaman nudos. La multiplicidad de nudos determina cómo se conectan las partes de Bézier, vea la página Wiki [Aumentar multiplicidad de nudos](Sketcher_BSplineIncreaseKnotMultiplicity/es.md) para más detalles.

Para cambiar la multiplicidad de nudos, utilice los botones de la barra de herramientas **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:24px"> [B-spline aumenta la multiplicidad de nudos](Sketcher_BSplineIncreaseKnotMultiplicity/es.md)** o **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [B-spline disminuye la multiplicidad de los nudos](Sketcher_BSplineDecreaseKnotMultiplicity/es.md)**.

**Nota:** La creación de dos B-Splines conectadas entre sí no se unirá a una sola B-spline nueva. Por lo tanto, su punto de conexión no es un nodo. La única manera de obtener un nuevo nodo en una B-spline existente es disminuir el grado. Sin embargo, puede obtener muchos nudos nuevos. Por tanto, la mejor opción es redibujar la B-spline con más puntos de control.

### Cambiar el peso 

Alrededor de cada punto de control se ve un círculo amarillo oscuro. Su radio establece el peso del punto de control correspondiente. Por defecto todos los círculos tienen el radio *1*. Esto se indica con una restricción de radio para el primer círculo del punto de control.

Para crear una B-spline no uniforme los pesos tienen que ser no uniformes. Para conseguirlo puedes cambiar la [restricción de radio](Sketcher_ConstrainRadius/es.md) del primer círculo del punto de control:

![](images/Sketcher_Changing-control-point-weigth-constraint.gif )

o eliminas la restricción de que todos los círculos sean iguales y luego estableces diferentes restricciones de radio para los círculos.

Si no se establece ninguna restricción de radio, también se puede cambiar el radio arrastrando:

![](images/Sketcher_Changing-control-point-weigth-dragging.gif )

En el ejemplo de arrastre se ve que un peso alto atrae la curva hacia el punto de control mientras que un peso muy bajo cambia la curva como si el punto de control casi no existiera.

Cuando miras la [función de creación](#B-splines_no-uniformes.md) para B-splines racionales no uniformes ves que un peso de cero llevaría a una división por cero. Por lo tanto, sólo se pueden especificar pesos mayores que cero.

### Mostrar Información 

Como la forma de una B-spline no dice mucho sobre sus propiedades, FreeCAD ofrece [diferentes herramientas](Sketcher_Workbench/es#Herramientas_de_la_B-spline_de_Sketcher.md) para mostrar las propiedades:

+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Propiedad                  | Botón de la barra de herramientas                                                                                                                     |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Grado**                  |                                                                                                                                        |
|                            | **[<img src=images/Sketcher_BSplineDegree.svg style="width:16px"> [Mostrar/ocultar el polígono de control de la B-spline](Sketcher_BSplineDegree/es.md)**               |
|                            |                                                                                                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Polígono de control**    |                                                                                                                                        |
|                            | **[<img src=images/Sketcher_BSplinePolygon.svg style="width:16px"> [Mostrar/ocultar el polígono de control de la B-spline](Sketcher_BSplinePolygon/es.md)**             |
|                            |                                                                                                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Peine de curvatura**     |                                                                                                                                        |
|                            | **[<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [Mostrar/Ocultar peine de curvatura B-spline](Sketcher_BSplineComb/es.md)**                             |
|                            |                                                                                                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Multiplicidad de nudos** |                                                                                                                                        |
|                            | **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:16px"> [Mostrar/Ocultar multiplicidad de nudos B-spline](Sketcher_BSplineKnotMultiplicity/es.md)** |
|                            |                                                                                                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Pesos**                  |                                                                                                                                        |
|                            | **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Mostrar/Ocultar el peso del punto de control de la B-spline](Sketcher_BSplinePoleWeight/es.md)** |
|                            |                                                                                                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

### Limitaciones

De momento (FreeCAD 0.19) hay algunas limitaciones al usar splines que debes conocer:

1.  No puedes establecer restricciones tangenciales.En este ejemplo <img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width:450px;"> quieres asegurar que la spline toca la curva azul 2 veces tangencialmente. Esto sería útil porque la línea azul podría ser, por ejemplo, el límite espacial para su diseño.
2.  No se puede insertar un nuevo punto de control entre dos puntos de control existentes seleccionados. No hay otra forma que redibujar la spline.
3.  No se puede eliminar un punto de control. También en este caso debe redibujar la spline
4.  No se puede crear una curva de desplazamiento para una B-spline utilizando la herramienta [Borrador Desplazamiento](Draft_Offset/es.md).

## Casos típicos de uso 

Según las propiedades de las B-splines, hay 3 casos de uso principales:

1.  Curvas que comienzan/terminan tangencialmente a una determinada dirección. Un ejemplo de esto es el ejemplo de motivación [arriba](#Motivación.md).
2.  Curvas que describen diseños más grandes y proporcionan la libertad de cambios locales. Véase [este ejemplo](#Diseño.md) más abajo.
3.  Curvas que proporcionan una cierta continuidad (derivada). Véase [este ejemplo](#Continuidad_en_las_transiciones_geométricas.md) más abajo.

### Diseño

Tomemos por ejemplo el caso de que usted diseñe la carcasa de una batidora de cocina. Su forma deseada debe ser como esta:

![](images/Sketcher_spline-exmple-mixer-shell.png )

Para definir la forma exterior es ventajoso utilizar una B-spline porque cuando se cambia un punto de control para cambiar la curvatura en la parte inferior, la curvatura en el lado y la parte superior no se cambiará:

![](images/Sketcher_spline-exmple-mixer-sketch.gif )

### Continuidad en las transiciones geométricas 

Hay varios casos en los que es físicamente necesario tener una cierta continuidad superficial en las transiciones geométricas. Tomemos por ejemplo las paredes interiores de un canal de fluido. Cuando tienes un cambio en el diámetro del canal, no quieres tener un borde porque los bordes introducirían turbulencias. Por lo tanto, como en el ejemplo de motivación [arriba](#Motivación.md), uno utiliza splines para este propósito.

El desarrollo de las curvas de Bézier fue impulsado inicialmente por la industria automovilística francesa. Además del ahorro de material y la reducción de la resistencia al flujo de aire, también había que mejorar el aspecto de los coches. Y cuando se observa el elegante diseño de los coches franceses de los años 60 y 70 se ve que las curvas de Bézier dieron un impulso al diseño de los coches.

Tomemos como ejemplo esta tarea en el diseño de coches: El guardabarros del coche debe \"tener un buen aspecto\". He aquí un croquis básico de nuestra tarea:

<img alt="" src=images/Spline-Fender-sketch1.svg  style="width:250px;">

\"Tener un buen aspecto\" significa que el cliente (potencial) mire el guardabarros y no vea reflejos de luz inesperados ni tampoco cambios repentinos en el reflejo de la pintura del automóvil. Entonces, ¿qué se necesita para evitar cambios en los reflejos? Mirar de cerca el guardabarros:

<img alt="" src=images/Spline-Fender-sketch2.svg  style="width:300px;"> 
*En el área espacial por encima del borde, la intensidad de la luz reflejada es baja (denotada por la elipse roja) porque no se refleja luz directamente en la dirección del borde al ojo.*

Cuando hay un borde, hay una zona espacial en la que la luz reflejada tiene menos intensidad y esto es lo que se nota al mirar el guardabarros. Para evitar esto necesitas un cambio continuo en la pendiente de tus elementos de superficie. La pendiente es la derivada de primer orden y como se explica en la sección [Basicos](#Basicos.md), una B-spline de segundo grado (cuadrática) ofrece en cada punto una derivada continua de primer orden.

¿Pero es esto realmente suficiente? En el punto de transición geométrica tenemos ahora en ambos lados la misma pendiente, pero la pendiente puede cambiar de forma diferente en ambos lados. Entonces tenemos esta situación:

<img alt="" src=images/Spline-Fender-sketch3.svg  style="width:300px;">

Por lo tanto, también tenemos zonas espaciales en las que la intensidad de la luz reflejada es diferente. Para evitar esto, necesitamos en el punto geométrico de transición también una continuidad de la derivada de segundo orden y, por tanto, una B-spline cúbica.

---
[documentation index](../README.md) > B-Splines/es
