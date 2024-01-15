---
 GuiCommand:
   Name: Part Sweep
   Name/es: Part Barrido
   MenuLocation: Pieza , Barrido...
   Workbenches: Part_Workbench/es
   SeeAlso: Part_Loft
---

# Part Sweep/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Part Barrido](Part_Sweep/es.md) se usa para crear una cara, una carcasa o una forma sólida desde uno o más perfiles (atravesando secciones) proyectados a lo largo de una trayectoria.


</div>


<div class="mw-translate-fuzzy">

La herramienta Barrido del banco de trabajo Part es similar a la de <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft.md) con el añadido de una trayectoria para definir la proyección entre perfiles.


</div>

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*A solid sweep generated from a single profile (A) distributed along a spine (B)*



## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/Part_Sweep.svg" width=16px> '''Crear barrido'''** . Esto abre los parámetros de Barrido del [Panel de tareas](Task_panel/es.md).
2.  En *Perfiles disponibles* de la columna de la izquierda (anteriormente *Vértice/Arista/Alambre/Cara* en la versión v0.16), pinchar sobre el elemento que será usado como perfil del barrido, después pinchar la flecha que indica hacia la derecha para colocarlo en los *Perfiles seleccionados* de la columna de la derecha (anteriormente *Barrido* en la versión v0.16). Repetir la operación si se desea utilizar más de un perfil. Usar las flechas que indican hacia arriba y hacia abajo para reordenar los perfiles seleccionados.
3.  Pulsar el botón **Trayectoria del barrido** y después, elegir entre cualquiera de estos dos modos de selección:
    -   *Selección de un único segmento*: Seleccionar una o más aristas consecutivas en la [3D View](3D_View.md) (pulsar **CTRL** para selección múltiple) y presionar **Hecho**. El barrido únicamente será generado a lo largo de las aristas seleccionadas.
    -   *Selección de una trayectoria completa*: Ir a la pestaña Modelo de la Vista combinada, seleccionar en el árbol el objeto 2D que se ha de usar como trayectoria, volver al [Panel de tareas](Task_panel/es.md) y pulsar **Hecho**. Otra manera sería haciendo doble clic con el ratón sobre una de las aristas consecutivas para que se seleccionen todas ellas. El barrido será generado a lo largo de todas las aristas consecutivas halladas en el objeto 2D.
4.  Definir las opciones [Crear sólido](#Solid.md) y [Ángulo fijo](#Frenet.md).
5.  Aceptar con el botón **OK**


</div>

### Accepted geometry 


<div class="mw-translate-fuzzy">

### Geometría aceptada 

-   **Perfiles**: Puede ser un punto (vértice), línea (arista), alambre o cara. Las aristas y los alambres pueden ser abiertos o cerrados. Hay varias [Limitaciones y complicaciones de perfil](Part_Sweep#Profile_limitations_and_complications.md), ver más abajo. Sin embargo, los perfiles pueden provenir de primitivas del banco de trabajo Part, operaciones del banco de trabajo Draft y de bocetos.


</div>


<div class="mw-translate-fuzzy">

-   **Trayectoria**: Se puede usar una línea (arista) o una serie de líneas conectadas, alambres o diferentes primitivas del banco de trabajo Part, operaciones del banco de trabajo Draft o un boceto. La trayectoria se suele seleccionar directamente desde la ventana principal del modelo, aunque también puede ser seleccionada desde la [Vista árbol](Tree_view/es.md) (pestaña Modelo de la [Vista combinada](Combo_view/es.md)). La trayectoria puede ser también una forma completa apropiada o un subcomponente apropiado de una forma más avanzada (por ejemplo, una arista de un <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Cube.md) podría ser seleccionada como trayectoria). La trayectoria puede ser tanto abierta como cerrada, creando consecuentemente un barrido abierto o cerrado. Una trayectoria cerrada, como la de un círculo del banco de trabajo Part tendrá como resultado un barrido cerrado. Por ejemplo, el barrido de un círculo más pequeño alrededor de una trayectoria de un círculo mayor, creará un toro.


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Options

#### Solid


<div class="mw-translate-fuzzy">

## Propiedades

### Sólido

Si \"Solid\" es seleccionado como \"true\", FreeCAD crea un sólido, siempre y cuando los perfiles sean de una geometría cerrada; si es seleccionado como \"false\", FreeCAD crea una cara o (si es más de una cara) una carcasa tanto para perfiles abiertos como cerrados.


</div>

#### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">


<div class="mw-translate-fuzzy">

### Frenet o Ángulo fijo 

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;"> La propiedad \"Frenet\" controla la forma en que la orientación del perfil va cambiando según va siguiendo la trayectoria del barrido. Si \"Frenet\" es \"false\", la orientación del perfil se mantiene constante de punto a punto. La forma resultante tiene la mínima torsión posible. Sin embargo, Cuando un perfil genera un barrido a lo largo de una hélice, sufre como un deslizamiento que va desviando su orientación suavemente, va rotando siguiendo la hélice. Seleccionar la propiedad \"Frenet\" a true para evitar este tipo de deformaciones.


</div>


<div class="mw-translate-fuzzy">

Si \"Frenet\" es \"true\" la orientación del perfil se computa en base a la curvatura local y los vectores de tangencia de la trayectoria. De este modo la orientación del perfil se mantiene constante cuando realiza el barrido alrededor de una hélice, debido a que el vector de curvatura de una hélice recta está siempre dirigido a su eje. Sin embargo, cuando la trayectoria no es una hélice, la forma resultante puede tener un aspecto, a veces, como de extrañas torsiones. Para más información, ver [Frenet Serret formulas](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).


</div>

#### Transition


<div class="mw-translate-fuzzy">

### Transición

\"Transition\" establece el estilo de transición que se aplicará a las uniones de los tramos de la trayectoria (por ejemplo cuando la trayectoria es un alambre). La propiedad no se muestra en el [Panel de tareas](Task_panel/es.md) y se puede encontrar en las propiedades tras ser creado el barrido.

-   Transformed. Transformadas.
-   Right corner. Hace las uniones angulares, rectas.
-   Round corner. Hace las uniones redondeadas.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A Part Sweep object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Sweep}}

-    **Sections|LinkList**: lists the sections used.

-    **Spine|LinkSub**: spine (path) to sweep along.

-    **Solid|Bool**: true or false (default). True creates a Solid.

-    **Frenet|Bool**: true or false (default). True uses Frenet algorithm.

-    **Transition|Enumeration**: transition mode. Options are *Transformed*, *Right corner* or *Round corner*.

## Limitations

### Vertex or point 

A vertex or point may only be used as the first and/or last profile.
For example:

-   You cannot Sweep from a circle to a point, to an ellipse.
-   You can however Sweep from a point to a circle to an ellipse to another point.

### Profiles

In one Sweep, all profiles (lines wires etc.) must be either open or closed.
For example:

-   FreeCAD cannot Sweep between a Part Circle and a Part Line.

### Sketches

-   The profile may be created with a sketch. However only valid sketches will be available for selection in the task panel.
-   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire).

### Draft Workbench objects 

A profile can be a [Draft Workbench](Draft_Workbench.md) object.
The following objects can be valid profiles:

-   Point
-   Line, Wire
-   B-spline, Bézier Curve
-   Circle, Ellipse
-   Rectangle, Polygon

### Part Workbench objects 

A profile can be a Part object created with the [Part Primitives](Part_Primitives.md) command.
The following objects can be valid profiles:

-   Point (Vertex)
-   Line (Edge)
-   Helix, Spiral
-   Circle, Ellipse
-   Regular Polygon
-   Plane (Face)

## Links


<div class="mw-translate-fuzzy">

## Enlaces

-   Como Barrido es usado a menudo para crear roscas para tornillos, debería ver [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/es
