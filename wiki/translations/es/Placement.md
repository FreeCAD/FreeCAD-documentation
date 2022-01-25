# Placement/es
## Introducción

**Placement o Ubicación** es el modo en que Freecad especifica la localización y la inclinación (orientación) de un objeto en el espacio. Placement puede ser especificado de múltiples formas y manipulado a través de [Código](Python_scripting_tutorial/es#Vectors_and_placements.md), del [Editor de propiedades](Property_editor/es.md) o seleccionando desde el menú **Editar → Ubicación...** para abrir el [Panel de tareas de Ubicación](Std_Placement.md).

### Accediendo a los atributos de Placement 

Se puede acceder y modificar los atributos de Ubicación de un objeto de 3 maneras:

![Placement o Ubicación en el panel de propiedades](images/PlacementPropertiesv10-800x800.png ) 

![Código de Placement como y/p/r y Matriz de su [API](images/Placement_API.md).](PlacePyConv10.png ) 

![Panel de tareas de Placement o Ubicación](images/PlacementDialogv10.png ) 

## Tipos de Ubicación 

La ubicación es almacenada internamente como una posición y una rotación (el eje de rotación y el ángulo transformados en un cuaternión [quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Mientras que hay diferentes formas de especificar una rotación, por ejemplo con un centro de rotación, esto se usa únicamente con fines de cálculo de rotación y no es almacenado para operaciones posteriores. De manera similar, si se especifica un eje de rotación de (1,1,1), puede ser normalizado cuando es almacenado en el cuaternión y aparece como (0.58, 0.58, 0.58) cuando se observa el objeto después.

### Ángulo, Eje y Posición 

**Placement = \[Ángulo, Eje, Posición\]**

La primera forma de **Ubicación** fija la localización de un objeto en el espacio con una posición, y describe su orientación como una simple rotación sobre un eje.

**Ángulo = r** es un escalar que indica la cantidad de rotación sobre un **Eje**. Se introduce en grados, pero se almacena internamente en radianes.

**Eje = (ax,ay,az)** Es un vector que describe un eje de rotación (Ver Nota sobre eje de rotación). Ejemplos:

   (1,0,0)       ==> sobre el eje **X** 
   (0,1,0)       ==> sobre el eje **Y** 
   (0,0,1)       ==> sobre el eje **Z** 
   (0.71,0.71,0) ==> sobre la línea **y=x**

Se puede observar que también es posible trasladar (mover) un objeto a lo largo de su eje de rotación (movimiento axial) introduciendo la distancia a mover en la casilla {{SpinBox|Axial: 0.0mm}} y pulsando el botón **Aplicar axial**. (Una manera de visualizar el movimiento axial es pensando en un aeroplano con una hélice giratoria en su morro \-- la hélice gira *alrededor* de un eje de rotación mientras el avión se mueve *a lo largo* de ese mismo eje.) Los valores del vector pueden ser pensados como la cantidad relativa de movimiento que se aplicará en esa dirección. Por ejemplo, en el caso de que y=x (0.71,0.71,0) el valor contenido en la casilla Axial es aplicado en la misma medida en las direcciones X e Y, pero no aparece ningún movimiento en la dirección Z.

**Posición= (x,y,z)** Es un vector que describe el punto desde el que la geometría del objeto será calculada (de hecho, un \"origen local\" del objeto). Observe que en la programación, Placement.Base se usa para señalar el componente de Posición de un emplazamiento. El editor de propiedades llama a este valor **Position** y el panel de tareas de Placement o Ubicación lo llama **Traslación**.

### Ángulos de Euler: Posición y Yaw (Guiñada), Pitch (Cabeceo) y Roll (Alabeo) 

Si en Rotación seleccionamos Ángulos de Euler aparecen estos campos: ![Placement task panel: {{ComboBox|Euler angles}} selected](images/PlacementDialogv10b.png )  **Rotación = \[Traslación, Guiñada-Cabeceo-Alabeo\]** Roll (Alabeo) o Ángulo de rotación alrededor del eje X. Pitch (Cabeceo) o Ángulo de rotación alrededor del eje Y. Yaw (Guiñada) o Ángulo de rotación alrededor del eje Z. Estos términos son usados en aviación.

La segunda forma de **Ubicación** fija la localización de un objeto en el espacio con una **Posición** (como en la primera forma), pero describe su orientación usando los ángulos [Yaw, Pitch y Roll](http://en.wikipedia.org/wiki/Yaw,_pitch,_and_roll). Estos ángulos son llamados a veces [Ángulos de Euler](http://en.wikipedia.org/wiki/Euler_angles) o Ángulos Tait-Bryan. Yaw, Pitch y Roll (Guiñada, Cabeceo y Alabeo) son términos usados habitualmente en aviación y se usan para la orientación de un Body (cuerpo).

**Posición = (x,y,z)** Es un vector que describe el punto desde el que la geometría del objeto será calculada (de hecho, un \"origen local\" del objeto).

**Yaw-Pitch-Roll = (y,p,r)** Es una tupla o agrupación de valores que especifica la orientación de un objeto. Los valores para y,p,r especifican los grados de rotación de cada uno de los ejes z,y,x (ver nota).  
```python
>>> App.getDocument("Sin_nombre").Cylinder.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
```

App.Rotation(10,20,30) = Ángulo Euler

**Yaw o Guiñada** = 10 grados (**Z**)

**Pitch o Cabeceo** = 20 grados (**Y**)

**Roll o Alabeo** = 30 grados (**X**)

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Yaw o Guiñada** es la rotación alrededor del **eje Z**, es decir, una rotación de izquierda a derecha.
(El ángulo yaw es la **Psi ψ**). 

![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pitch o Cabeceo** es la rotación alrededor del **eje Y**, es decir, morro arriba y morro abajo.
(El ángulo Pitch es la **Phi φ**). 

![](images/Tache_Placement_Roulis_fr_Mini.gif )**Roll o Alabeo** es la rotación alrededor del **eje X**, es decir, ala arriba o abajo.
(El ángulo Roll es la **Thêta θ**). 

### Matriz

**Placement = Matriz**

La tercera forma de **Ubicación** describe la posición y orientación del objeto con una matriz de transformación afín de 4x4 ([Affine Transformation](http://en.wikipedia.org/wiki/Affine_transformation)).

**Matriz** =

  ((r11,r12,r13,t1),
   (r21,r22,r23,t2),
   (r31,r32,r33,t3),
   (0,0,0,1)) , donde rij indica rotación y ti traslación. 




## La ventana de diálogo Ubicación 

La ventana de diálogo Ubicación es invocada desde el menú **Editar**. Se usa para precisar la rotación/traslación de los objetos. También se usa cuando se necesita crear un boceto en un plano \"no estándar\" o para cambiar la orientación de un boceto a un nuevo plano.

El apartado **Traslación** ajusta la localización del objeto en el espacio. El apartado **Centro** ajusta el eje de rotación a uno que no pasa a través del punto de referencia del objeto. El apartado **Rotación** ajusta el ángulo o ángulos de rotación y la manera de especificarlos.

Pero mientras los elementos dentro de cada sección se aplican generalmente al propósito de cada sección, hay también algunos elementos en una sección que pueden afectar a los de otra sección. Por ejemplo, pinchando el botón de Puntos seleccionados en la sección **Centro** con 2 puntos seleccionados en la vista 3D, resulta no sólo el hecho de introducir las coordenadas en las casillas de **Centro** con las coordenadas de los puntos medios entre esos dos puntos seleccionados, sino que también crea un eje personalizado a lo largo de la línea definida por esos dos puntos seleccionados en la sección **Rotación** . Otro ejemplo es, introduciendo un valor en la casilla de Axial y pinchando el botón de Aplicar axial en la sección **Traslación** , traslada (mueve) el objeto a lo largo del eje definido en la sección **Rotación** .

La casilla **Aplicar cambios incrementales** es útil cuando las traslaciones/rotaciones se tienen que aplicar con respecto a la actual posición/orientación relativa del objeto. Pinchando esta casilla, los campos de diálogo de entrada se resetean a cero, pero no cambia la orientación o localización del objeto. La introducción de datos posteriores sí cambiarán la orientación/localización, pero son aplicados desde la actual posición del objeto. Habilitar esta casilla es útil también cuando se usa el botón de Puntos seleccionados para prevenir cambios de emplazamiento no deseados.

PD: Desde la versión 0.17, introduciendo nuevo objeto de Part, dicho objeto tiene su emplazamiento, y el emplazamiento del objeto creado en el objeto Part es incrementado con la Ubicación de Part. {{Version/es|0.17}} Para obtener la Ubicación de Part, usar el siguiente código: 
```python
import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print sel[0].Placement
print sel[0].getGlobalPlacement()   # return the GlobalPlacement
print sel[0].getParentGeoFeatureGroup() # return the GeoFeatureGroup, ex:  Body or a Part.
print  "____________________"
```

El botón de **Puntos seleccionados** se usa para introducir las coordenadas en la sección **Centro** en las casillas de coordenadas y adicionalmente (cuando se seleccionan 2 o 3 puntos) para crear un eje de rotación personalizado (definido por el usuario) en la sección **Rotación** . Un punto puede ser un vértice, pero puede ser también cualquier punto a lo largo de una arista o sobre una cara. Cuando se selecciona una arista o cara, la arista o cara son seleccionadas al completo, pero Freecad también recuerda sobre qué punto de la cara o arista se encontraba el puntero del ratón cuando esa arista o cara fueron seleccionadas. Son las coordenadas de ese punto las que se introducirán en la caja de diálogo de Ubicación cuando se pulse el botón de **Puntos seleccionados** . Se puede pensar que esta no es una manera muy precisa de seleccionar un punto, y es cierto, pero en muchos casos está suficientemente asegurado que ese punto seleccionado está en esa arista o cara. En los casos en los que se necesita designar un punto para ser usado con precisión, se debe seleccionar un vértice. Cuando no hay un vértice en la localización deseada, se debe considerar la creación de uno, quizás en un boceto temporal adjunto a esa cara o arista, o quizás usando un objeto del banco de trabajo Draft, como una línea o punto, etc.

Vamos primero a considerar el simple caso de seleccionar un punto. El flujo de trabajo es, primero, seleccionar el punto deseado, después pulsar el botón **Puntos seleccionados** . Las coordenadas del punto seleccionado serán usadas para rellenar las casillas X, Y, y Z de la sección **Centro** . A partir de aquí cualquier rotación realizada al objeto será aplicada alrededor de este centro de rotación.

Vamos ahora a considerar el caso de seleccionar 2 puntos. Hay que seleccionar los 2 puntos deseados, y entonces pulsar el botón **Puntos seleccionados** . Las coordenadas del punto medio entre los 2 puntos seleccionados quedan introducidas en las casillas X, Y, y Z de la sección **Centro** . A partir de aquí cualquier rotación realizada al objeto será aplicada alrededor de este centro de rotación. Pero además de establecer las coordenadas de la sección **Centro** como personalizadas (definidas por el usuario) , el eje es también añadido al elemento **Eje** de la sección **Rotación** . (Nota: Estando en el modo de rotación Euler, el modo cambia al modo de Rotación con un eje y el nuevo eje personalizado es seleccionado como el actual eje de rotación.) A partir de aquí cualquier rotación realizada usando el nuevo eje personalizado lo hará alrededor de este eje de rotación. Por añadidura, la distancia es medida entre los 2 puntos seleccionados, y esta información es mostrada en la Vista de informe. (Nota: Mantener pulsada la tecla Shift (Mayúsculas) mientras se presiona el botón **Puntos seleccionados** para copiar la medida de distancia al portapapeles.) Introduciendo esta distancia en la casilla Axial de la sección **Traslación** y pulsando el botón **Aplicar axial** se puede trasladar (mover) el objeto para que el primer punto seleccionado ocupe ahora las coordenadas ocupadas por el segundo punto seleccionado (en el momento en que el botón **Puntos seleccionados** fue pulsado).

A continuación vamos a considerar el caso de seleccionar 3 puntos. Hay que seleccionar los 3 puntos deseados, y entonces pulsar el botón **Puntos seleccionados** . Las coordenadas del primer punto seleccionado (el orden de selección es muy importante aquí) quedan introducidas en las casillas X, Y, y Z de la sección **Centro** . Como 3 puntos definen un plano, FreeCAD es capaz de tomar ventaja de esto y usar estos 3 puntos para crear un nuevo eje de rotación personalizado (definido por el usuario) que es normal (perpendicular) a este plano definido. Al igual que seleccionando 2 puntos, la distancia entre puntos es también mostrada en la Vista de informe, pero esta vez es la distancia entre el segundo y el tercer punto seleccionado. (Nota: Mantener pulsada la tecla Shift (Mayúsculas) mientras se presiona el botón **Puntos seleccionados** \-- Shift + Click \-- para copiar la medida del ángulo al portapapeles.) Adicionalmente, el ángulo entre el segundo y el tercer punto es también medido y mostrado en la Vista de informe. Introduciendo este ángulo en la casilla **Ángulo** de la sección **Rotación** se puede rotar el objeto con mucha precisión, de forma que ahora el segundo punto seleccionado queda alineado con las coordenadas ocupadas por el tercer punto seleccionado. (Nota: Se puede incrementar el número de dígitos usados a través de la casilla del menú Editar -\> Preferencias -\> General -\> Unidades -\> Número de decimales si se desea una mayor precisión.)

## Ejemplos

Rotaciones alrededor de un eje simple:

<img alt="Before Rotation" src=images/RotationAboutZBefore.png  style="width:600px;"> Antes de Rotación (Vista superior) 

<img alt="After Rotation about Z" src=images/RotationAboutZAfter.png  style="width:600px;"> Después de Rotación alrededor de Z (Vista superior) 

<img alt="After Rotation about y=x" src=images/RotationAboutYXAfter.png  style="width:600px;"> Después de Rotación alrededor de y=x (Vista desde la derecha) 

Rotación con el punto central desplazado:

<img alt="Before Rotation" src=images/RotationOffsetBefore.png  style="width:600px;"> Antes de Rotación (Vista superior) 

<img alt="After Rotation about Z" src=images/RotationOffsetAfter.png  style="width:600px;"> Después de Rotación alrededor de Z (Vista superior) 

Rotación usando ángulos de Euler:

<img alt="Before Rotation" src=images/RotationEulerBefore.png  style="width:600px;"> Antes de Rotación 

<img alt="After Rotation" src=images/RotationEulerAfter.png  style="width:600px;"> Después de Rotación 

## Placement.Base versus Definición de forma 

Placement o Ubicación no es la única manera de posicionar una forma en el espacio. Observando la consola de Python en esta imagen:

![Dos formas con la misma Ubicación](images/2Placements800.png )

Los dos cubos tienen el mismo valor de Ubicación, pero están en emplazamientos diferentes. Esto es porque las dos formas están definidas por vértices diferentes (curvas de formas más complejas). Para las dos formas de la ilustración anterior:

 >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
 >>> for v in ev: print v.X,",",v.Y,",",v.Z
 ... 
 30.0,30.0,0.0
 30.0,30.0,10.0
 40.0,30.0,0.0
 40.0,30.0,10.0
 40.0,40.0,0.0
 40.0,40.0,10.0
 30.0,40.0,0.0
 30.0,40.0,10.0
 >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
 >>> for v in e1v: print v.X,",",v.Y,",",v.Z
 ... 
 0.0,10.0,0.0
 0.0,10.0,10.0
 10.0,10.0,0.0
 10.0,10.0,10.0
 10.0,0.0,0.0
 10.0,0.0,10.0
 0.0,0.0,0.0
 0.0,0.0,10.0
 >>> 
 

Los vértices (o vectores) que definen la forma usan el atributo de Placement.Base como orígen. Así pues, si se desea mover una forma 10 unidades a lo largo del eje **X** , se debería añadir 10 a las coordenadas de **X** de todos los vértices o se podría establecer el valor de Placement.Base como (10,0,0).

## Uso de \"Centro\" para controlar el eje de rotación 

Por defecto, el eje de rotación no es realmente el eje x/y/z , sino una línea paralela al eje seleccionado, pero que pasa por el punto de referencia (Placement.Base) del objeto a rotar. Esto se puede cambiar usando los campos de Centro de la ventana de diálogo de Ubicación o, en programación, usando el parámetro Centro del constructor FreeCAD.Placement.

Por ejemplo, suponiendo que tenemos un cubo (ver debajo) posicionado en (20,20,10). ![Antes de Rotación](images/LocalZBefore2.png ) Queremos girar el cubo alrededor de su propia línea de centro vertical (por ejemplo el eje Z local), pero manteniéndolo en su misma posición. Se puede conseguir fácilmente especificando un valor de Centro igual a las coordenadas del punto central del cubo (25,25,15). ![Después de Rotación](images/LocalZAfter2.png )

En programación, se haría como sigue: 
```python
import FreeCAD
obj = App.ActiveDocument.Box                       # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)   # 45° about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,15)                  # central point of box 
pos = obj.Placement.Base                           # position point of box
newplace = FreeCAD.Placement(pos,rot,centre)       # make a new Placement object
obj.Placement = newplace                           # spin the box
``` Los mismos comandos con el archivo de ejemplo [RotateCoG2.fcstd](http://forum.freecadweb.org/download/file.php?id=1651) (discusión en el [forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3950#p31052)) 
```python
import FreeCAD
obj = App.ActiveDocument.Extrude                    # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)    # 45 about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)    # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                    # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,0)                    # "centre" of rotation (where local Z cuts XY)
pos = obj.Placement.Base                            # original placement of obj
newplace = FreeCAD.Placement(pos,rot,centre)        # make a new Placement object
obj.Placement = newplace                            # spin the box
```

## Uso de Placement en expresiones 

En expresiones es posible usar los componentes de la ubicación, por ejemplo para acceder al componente x del objeto llamado \"Cubo\": 
```python
<<Cubo>>.Placement.Base.x
```

Se puede acceder al àngulo de rotación mediante: 
```python
<<Cube>>.Placement.Rotation.Angle
```

Se puede acceder al eje de rotación con: 
```python
<<Cube>>.Placement.Rotation.Axis.x
<<Cube>>.Placement.Rotation.Axis.y
<<Cube>>.Placement.Rotation.Axis.z
``` cuando uno de estos valores suele ser 1 mientras los otros son 0.

Se puede usar también la Ubicación al completo en una única expresión. Para ello: Pinchar con el botón derecho del ratón sobre la propiedad Placement en el Editor de propiedades, seleccionar \"Mostrar todo\" y aparecerán más propiedades adicionales. Si se vuelve a pinchar con el botón derecho otra vez sobre Placement, el menú contextual incluirá \"Expresión\...\". Seleccionando Expresión se abrirá su caja de diálogo y lo que se introduzca irá a la propiedad de Placement en vez de a las propiedades hijas.

Para hacer que la ubicación del \"Boceto\" sea la misma que la del \"Cilindro\", se debería introducir la expresión para el boceto de esta manera: 
```python
<<Cubo>>.Placement
``` ![Estableciendo la Ubicación completa en una sola expresión](images/PlacementInExpression.png )

**NOTE:** It\'s also possible to *create* Placement objects in expressions. See the [Expressions](Expressions#Placement.md) page for details.

## Notas

-   Las propiedades de Ubicación (Placement) en la pestaña de datos aparecen como desactivadas en los objetos que están adjuntos a algún otro objeto. En ese caso, el desplazamiento (Attachment) del adjunto tiene que ser editado.
-   Los ejes y el ángulo pueden ser también expresados como un cuaternión [quaternion](http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation).
-   El punto de referencia de un objeto puede ser diferente dependiendo del objeto. Algunos ejemplos para objetos comunes:

  Objeto                                           Punto de referencia
   
  Part.Cubo                                        izquierda (minx), delante (miny), abajo (minz) vértice
  Part.Esfera                                      centro de la esfera (por ejemplo centro de cuadro delimitador)
  Part.Cilindro                                    centro de la cara inferior
  Part.Cono                                        centro de la cara inferior (o la punta del cono si el radio inferior es 0)
  Part.Toro                                        centro del toro
  Resultados de operaciones derivadas de bocetos   la forma hereda la posición del boceto sobre el que reposa. Los bocetos comienzan siempre en la posición = (0,0,0). Esta posición corresponde al origen del boceto.

## Otros

-   La Ubicación relativa de los objetos será tratada con posterioridad en el banco de trabajo Assembly (Ensamblaje).

## Más

-   Este tutorial: [Aeroplano](Aeroplane/es.md) abarca los mecanismos del cambio de ubicación de un objeto extensivamente.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Placement/es
