# Topological data scripting/es



{{TOCright}}

## Introducción

Aquí te explicaremos cómo controlar el módulo [Pieza](Part_Workbench/es.md) directamente desde el intérprete de Python de FreeCAD, o desde cualquier guión externo. Asegúrate de navegar por la sección [Guionización](Scripting/es.md) y las páginas [Básicos de Guionización FreeCAD](FreeCAD_Scripting_Basics/es.md) si necesitas más información sobre cómo funciona el guionización de Python en FreeCAD. Si eres nuevo en Python, es una buena idea leer primero la [Introducción a Python](Introduction_to_Python/es.md).

### Ver también 

-   [Guionización Pieza](Part_scripting/es.md)
-   [OpenCASCADE](OpenCASCADE/es.md)

## Diagrama de clase 

Este es un resumen [Lenguaje Unificado de Modelado (UML)](http://es.wikipedia.org/wiki/Lenguaje_Unificado_de_Modelado) de las clases más importantes del módulo Pieza: ![Clases de Python del módulo Pieza](images/Part_Classes.jpg ) {{Top}}

### Geometría

Los objetos geométricos son los bloques de construcción de todos los objetos topológicos:

-   **Geom** Clase base de los objetos geométricos.
-   **Línea** Una línea recta en 3D, definida por un punto inicial y un punto final.
-   **Círculo** Círculo o segmento de círculo definido por un punto central y un punto inicial y final.
-   Etc.


{{Top}}

### Topología

Los siguientes tipos de datos topológicos están disponibles:

-   **Compuesto** Un grupo de cualquier tipo de objetos topológicos.
-   **Sólido compuesto** Un sólido compuesto es un conjunto de sólidos conectados por sus caras. Amplía las nociones de ALAMBRE y CASCO a los sólidos.
-   **Sólido** Una parte del espacio limitada por cáscaras. Es tridimensional.
-   **Cáscara** Conjunto de caras conectadas por sus aristas. Una cáscara puede ser abierta o cerrada.
-   En 2D es parte de un plano; en 3D es parte de una superficie. Su geometría está limitada (recortada) por los contornos. Es bidimensional.
-   **Alambre** Conjunto de aristas conectadas por sus vértices. Puede ser un contorno abierto o cerrado dependiendo de si las aristas están unidas o no.
-   **Arista** Elemento topológico que corresponde a una curva restringida. Una arista está generalmente limitada por los vértices. Tiene una dimensión.
-   Vértice Elemento topológico que corresponde a un punto. Tiene una dimensión cero.
-   **Forma** Término genérico que abarca todo lo anterior.


{{Top}}

## Ejemplo: Crear una topología simple 

![Hilo](images/Wire.png )

Ahora crearemos una topología construyéndola a partir de una geometría más sencilla. Como caso de estudio utilizaremos una pieza como la que se ve en la imagen que consta de cuatro vértices, dos arcos y dos líneas. {{Top}}

### Crear geometría 

Primero creamos las distintas partes geométricas de este cable. Asegurándonos de que las partes que tienen que ser conectadas más tarde comparten los mismos vértices.

Así que primero creamos los puntos:


```python
import Part
from FreeCAD import Base
V1 = Base.Vector(0, 10, 0)
V2 = Base.Vector(30, 10, 0)
V3 = Base.Vector(30, -10, 0)
V4 = Base.Vector(0, -10, 0)
```


{{Top}}

### Arco

![Círculo](images/Circel.png )

Para cada arco necesitamos un punto de ayuda:


```python
VC1 = Base.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = Base.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}

### Línea

![Línea](images/Line.png )

Los segmentos de línea se pueden crear a partir de dos puntos:


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}

### Poniendo todo junto 

El último paso es poner los elementos base de la geometría juntos y formar una forma topológica:


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}

### Crear un prisma 

Ahora extruir el hilo en una dirección y crear una forma 3D real:


```python
W = Part.Wire(S1.Edges)
P = W.extrude(Base.Vector(0, 0, 10))
```


{{Top}}

### Mostrar todo 


```python
Part.show(P)
```


{{Top}}

## Crear formas básicas 


<div class="mw-translate-fuzzy">

Puedes crear fácilmente objetos topológicos básicos con los métodos `make...()` del módulo Pieza:


</div>


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```

Algunos métodos disponibles `make...()`:

-    `makeBox(l, w, h, [p, d])`Hace una caja situada en p y apuntando a la dirección d con las dimensiones (l,w,h).

-    `makeCircle(radius)`Hace un círculo con un radio determinado.

-    `makeCone(radius1, radius2, height)`Hace un cono con los radios y la altura dados.

-    `makeCylinder(radius, height)`Hace un cilindro con un radio y altura dados.

-    `makeLine((x1, y1, z1), (x2, y2, z2))`Hace una línea desde dos puntos.

-    `makePlane(length, width)`Hace un plano con longitud y anchura.

-    `makePolygon(list)`Hace un polígono a partir de una lista de puntos.

-    `makeSphere(radius)`Hace una esfera con un radio determinado.

-    `makeTorus(radius1, radius2)`Hace un toro con los radios dados.

Ver la página [Pieza API](Part_API/es.md) para una lista completa de los métodos disponibles del módulo Pieza. {{Top}}

### Módulos de importación 

Primero necesitamos importar el módulo Pieza para poder usar su contenido en Python. También importaremos el módulo Base desde dentro del módulo FreeCAD:


```python
import Part
from FreeCAD import Base
```


{{Top}}

### Crear un vector 

[Vectores](https://es.wikipedia.org/wiki/Vector) son una de las piezas de información más importantes cuando se construir formas. Suelen contener tres números (pero no necesariamente siempre): las coordenadas cartesianas X, Y y Z. Se crea un vector así:


```python
myVector = Base.Vector(3, 2, 0)
```

Hemos creado un vector en las coordenadas X = 3, Y = 2, Z = 0. En el módulo de la pieza, los vectores se utilizan en todas partes. Las formas de la pieza también utilizan otro tipo de representación de puntos llamada Vértice que es simplemente un contenedor para un vector. Se accede al vector de un vértice así:


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}

### Crear un borde 

Un borde no es más que una línea con dos vértices:


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Nota: También se puede crear un borde pasando dos vectores:


```python
vec1 = Base.Vector(0, 0, 0)
vec2 = Base.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

Puedes encontrar la longitud y el centro de un borde así:


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}

### Poniendo la forma en la pantalla 

Hasta ahora hemos creado un objeto de borde, pero no aparece en ninguna parte de la pantalla. Esto se debe a que la escena 3D de FreeCAD sólo muestra lo que tú le dices que muestre. Para ello, utilizamos este sencillo método:


```python
Part.show(edge)
```

La función mostrar crea un objeto en nuestro documento de FreeCAD y le asigna nuestra forma \"borde\". Utilízala siempre que sea el momento de mostrar tu creación en pantalla. {{Top}}

### Crear un hilo 

Un hilo es una línea de varias aristas y puede crearse a partir de una lista de aristas o incluso de una lista de hilos:


```python
edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])
wire3.Edges
> [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
Part.show(wire3)
```


<div class="mw-translate-fuzzy">

Part.show(wire3) mostrará las 4 aristas que componen nuestro contorno. Otra información útil se puede recuperar fácilmente:


</div>


```python
wire3.Length
> 40.0
wire3.CenterOfMass
> Vector (5, 5, 0)
wire3.isClosed()
> True
wire2.isClosed()
> False
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de una cara 

Sólo serán válidas las caras creadas a partir de contornos cerrados. En este ejemplo, wire3 es un contorno cerrado pero wire2 no es un contorno cerrado (mira más arriba)


</div>

Only faces created from closed wires will be valid. In this example, wire3 is a closed wire but wire2 is not (see above):


```python
face = Part.Face(wire3)
face.Area
> 99.99999999999999
face.CenterOfMass
> Vector (5, 5, 0)
face.Length
> 40.0
face.isValid()
> True
sface = Part.Face(wire2)
sface.isValid()
> False
```


<div class="mw-translate-fuzzy">

Sólo las caras tendrán un área, ni los contornos ni las aristas.


</div>


{{Top}}

### Crear un círculo 

Se puede crear un círculo así:


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```

Si quieres crearlo en una cierta posición y con una cierta dirección:


```python
ccircle = Part.makeCircle(10, Base.Vector(10, 0, 0), Base.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```


<div class="mw-translate-fuzzy">

ccircle se creará a una distancia de 10 en el eje x desde el origen, y estará orientado hacia el eje x. Nota: makeCircle sólo acepta Base.Vector() para posición y normal, pero no admite tuplas. Tambien puedes crear una parte de una circunferencia dando su ángulo de inicio y fin, así:


</div>


```python
from math import pi
arc1 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 180, 360)
```


<div class="mw-translate-fuzzy">

Juntando arc1 y arc2 obtendremos una circunferencia. Los ángulos deberán indicarse en grados, si los tienes en radianes simplemente conviertelos según la fórmula: degrees = radians \* 180/PI o usando el módulo Python de matemáticas (después de importarlo, obviamente):


</div>


```python
import math
degrees = math.degrees(radians)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un arco por varios puntos 

Desafortunadamente no hay ninguna función makeArc pero tenemos la función Part.Arc para crear un arco a lo largo de tres puntos. Básicamente se puede suponer como un arco de unión entre el punto de partida y el punto final, pasando por el punto medio. Part.Arc crea un objeto arco en el que .toShape() tiene que ser llamado para obtener el objeto arista, del mismo modo como utilizamos Part.Line en lugar de Part.makeLine.


</div>

Unfortunately there is no `makeArc()` function, but we have the `Part.Arc()` function to create an arc through three points. It creates an arc object joining the start point to the end point through the middle point. The arc object\'s `toShape()` function must be called to get an edge object, the same as when using `Part.LineSegment` instead of `Part.makeLine`.


```python
arc = Part.Arc(Base.Vector(0, 0, 0), Base.Vector(0, 5, 0), Base.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```


<div class="mw-translate-fuzzy">

Arc solo acepta puntos como Base.Vector() no acepta tuplas. arc\_edge es lo que queremos que podemos mostrar utilizando Part.show(arc\_edge). También puedes obtener un arco utilizando una porción de una circunferencia:

arc\_edge es lo que queríamos conseguir, y podemos visualizar utilizando Part.show (arc\_edge). Si desea una pequeña parte de un círculo como un arco, también es posible:


</div>


```python
from math import pi
circle = Part.Circle(Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```


<div class="mw-translate-fuzzy">

Los arcos son aristas válidas, como las líneas. Así que también pueden utilizarse en los contornos.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un polígono 

Un polígono es simplemente un contorno con múltiples aristas rectas. La función makePolygon toma una lista de puntos y crea un contorno a través de dichos puntos:


</div>

A polygon is simply a wire with multiple straight edges. The `makePolygon()` function takes a list of points and creates a wire through those points:


```python
lshape_wire = Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
```


{{Top}}

### Create a bézier curve 

Bézier curves are used to model smooth curves using a series of poles (points) and optional weights. The function below makes a `Part.BezierCurve()` from a series of `FreeCAD.Vector()` points. Note: when \"getting\" and \"setting\" a single pole or weight, indices start at 1, not 0.


```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un plano 

Un plano es simplemente una superficie rectangular plana. El método utilizado para crear uno es este: **makePlane(length,width,\[start\_pnt,dir\_normal\])**. Por defecto start\_pnt = Vector(0,0,0) y dir\_normal = Vector(0,0,1). Utilizando dir\_normal = Vector(0,0,1) crearemos el plano orientado hacia el eje Z, mientras que con dir\_normal = Vector(1,0,0) crearemos el plano orientado hacia el eje X:


</div>

A Plane is a flat rectangular surface. The method used to create one is `makePlane(length, width, [start_pnt, dir_normal])`. By default start\_pnt = Vector(0, 0, 0) and dir\_normal = Vector(0, 0, 1). Using dir\_normal = Vector(0, 0, 1) will create the plane facing in the positive Z axis direction, while dir\_normal = Vector(1, 0, 0) will create the plane facing in the positive X axis direction:


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, Base.Vector(3, 0, 0), Base.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


<div class="mw-translate-fuzzy">

BoundBox es un prisma encerrando el plano con una diagonal empezando en (3,0,0) y terminando en (5,0,2). Aquí el espesor de BoundBox en el eje Y es cero, ya que nuestra forma es totalmente plana.


</div>


<div class="mw-translate-fuzzy">

Nota: makePlane sólo acepta Base.Vector() para start\_pnt y dir\_normal pero no tuplas


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de una elipse 

Para crear una elipse existen varios métodos:


</div>

There are several ways to create an ellipse:


```python
Part.Ellipse()
```


<div class="mw-translate-fuzzy">

Crea una elipse cuyo radio mayor es 2 y el radio menor 1 con centro en el (0,0,0)


</div>


```python
Part.Ellipse(Ellipse)
```


<div class="mw-translate-fuzzy">

Crea una copia de la elipse dada


</div>


```python
Part.Ellipse(S1, S2, Center)
```


<div class="mw-translate-fuzzy">

Crea una elipse centrada en el punto Center, donde el plano de la elipse está definido por Center, S1 y S2, su eje mayor está definido por Center y S1, su radio mayor es la distancia entre Center y S1, y su radio menor es la distancia entre S2 y el eje mayor.


</div>


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```


<div class="mw-translate-fuzzy">

Crea una elipse con radios mayor y menor MajorRadius y MinorRadius respectivamente, y ubicada en el plano definido por Center y la normal (0,0,1)


</div>


```python
eli = Part.Ellipse(Base.Vector(10, 0, 0), Base.Vector(0, 5, 0), Base.Vector(0, 0, 0))
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

En el código de arriba hemos pasado S1, S2 y center. De forma similar a Arc, Ellipse también crea un objeto elipse pero no una arista, así que tenemos que convertirlo en una arista utilizando toShape() para mostrarlo.


</div>


<div class="mw-translate-fuzzy">

Nota: Arc sólo acepta Base.Vector() para puntos pero no tuplas


</div>


```python
eli = Part.Ellipse(Base.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

para el constructor de la elipse de arriba hemos pasado el centro, MajorRadius y MinorRadius


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un toro 

Utilizando el método **makeTorus(radius1,radius2,\[pnt,dir,angle1,angle2,angle\])**. Por defecto pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0,angle2=360 y angle=360. Considera un toro como un pequeño circulo barrido a lo largo de una circunferencia grande. Radius1 es el radio de la circunferencia grande, radius2 es el radio del círculo pequeño, pnt es el centro del toro y dir es la dirección normal. angle1 y angle2 son ángulos en radianes para el círculo pequeño, el último parámetro angle es para hacer una sección del toro:


</div>

Using `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = 0, angle2 = 360 and angle = 360. Consider a torus as small circle sweeping along a big circle. Radius1 is the radius of the big circle, radius2 is the radius of the small circle, pnt is the center of the torus and dir is the normal direction. angle1 and angle2 are angles in degrees for the small circle; the last angle parameter is to make a section of the torus:


```python
torus = Part.makeTorus(10, 2)
```


<div class="mw-translate-fuzzy">

El código de arriba creará un toro con diámetro 20 (radio 10) y espesor 4 (radio del círculo pequeño 2)


</div>


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
```


<div class="mw-translate-fuzzy">

El código de arriba creará una sección del toro


</div>


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 360, 180)
```


<div class="mw-translate-fuzzy">

El código de arriba creará un semi toro, sólo el último parámetro se ha cambiado, dando el valor 180 creará el toro desde 0 hasta 180, eso es, medio toro.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un cubo o prisma 

Utilizando **makeBox(length,width,height,\[pnt,dir\])**. Por defecto pnt=Vector(0,0,0) y dir=Vector(0,0,1)


</div>

Using `makeBox(length, width, height, [pnt, dir])`. By default pnt = Vector(0, 0, 0) and dir = Vector(0, 0, 1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de una esfera 

Utilizando **makeSphere(radius,\[pnt, dir, angle1,angle2,angle3\])**. Por defecto pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=-90, angle2=90 y angle3=360. angle1 y angle2 son el punto vertical mínimo y máximo de la esfera, angle3 es el diámetro de la esfera.


</div>

Using `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 and angle3 = 360. Angle1 and angle2 are the vertical minimum and maximum of the sphere, angle3 is the sphere diameter.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un cilindro 

Utilizando **makeCylinder(radius,height,\[pnt,dir,angle\])**. Por defecto pnt=Vector(0,0,0),dir=Vector(0,0,1) y angle=360


</div>

Using `makeCylinder(radius, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360. 
```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}


<div class="mw-translate-fuzzy">

#### Creación de un cono 

Utilizando **makeCone(radius1,radius2,height,\[pnt,dir,angle\])**. Por defecto pnt=Vector(0,0,0), dir=Vector(0,0,1) y angle=360


</div>

Using `makeCone(radius1, radius2, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360. 
```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}


<div class="mw-translate-fuzzy">

## Modificando formas 

Existen diversos métodos para modificar formas. Algunas son simples operaciones de transformación como mover o rotar formas, otras son más complejas, como la unión y diferencia de una forma y otra. are simple transformation operations such as moving or rotating shapes, other are more complex, such as unioning and subtracting one shape from another. Tenlo en cuenta


</div>

There are several ways to modify shapes. Some are simple transformation operations such as moving or rotating shapes, others are more complex, such as unioning and subtracting one shape from another. {{Top}}


<div class="mw-translate-fuzzy">

### Operaciones de transformación 


</div>


<div class="mw-translate-fuzzy">

#### Traslación de una forma 

Traslación es el acto de mover una forma de una situación a otra. Cualquier forma (aristas, caras, cubos, etc\...) se puede trasladar del mismo modo:


</div>

Translating is the act of moving a shape from one place to another. Any shape (edge, face, cube, etc\...) can be translated the same way: 
```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(Base.Vector(2, 0, 0))
```


<div class="mw-translate-fuzzy">

Esto moverá nuestra forma \"myShape\" 2 unidades en la dirección del eje X.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Rotación de una forma 

Para rotar una forma, necesitas especificar el centro de rotación, el eje, y el ángulo de rotación:


</div>

To rotate a shape, you need to specify the rotation center, the axis, and the rotation angle: 
```python
myShape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1), 180)
``` El código de arriba rotará la forma 180 grados alrededor del eje Z. {{Top}}


<div class="mw-translate-fuzzy">

#### Transformaciones genéricas con matrices 

Una matriz es un modo muy conveniente de almacenar transformaciones en el mundo 3D. En una simple matriz, puedes establecer traslaciones, rotaciones y valores de escala a ser aplicados a un objeto. Por ejemplo:


</div>

A matrix is a very convenient way to store transformations in the 3D world. In a single matrix, you can set translation, rotation and scaling values to be applied to an object. For example: 
```python
myMat = Base.Matrix()
myMat.move(Base.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
```


<div class="mw-translate-fuzzy">

Nota: Las matrices de FreeCAD funcionan en radianes. También, casi todas las operaciones de matrices que toman un vector pueden tomar 3 números, así estas dos líneas hacen lo mismo:


</div>


```python
myMat.move(2, 0, 0)
myMat.move(Base.Vector(2, 0, 0))
```


<div class="mw-translate-fuzzy">

Cuando nuestra matriz es establecida, podemos aplicarla a nuestra forma. FreeCAD proporciona 2 métodos para hacerlo: transformShape() y transformGeometry(). La diferencia es que con el primero, estas seguro de que no ocurrirá ninguna deformación (mira \"escalando una forma\" más abajo). Podemos aplicar nuestra transformación así:


</div>


```python
myShape.transformShape(myMat)
```

o 
```python
myShape.transformGeometry(myMat)
```{{Top}}


<div class="mw-translate-fuzzy">

#### Escalando una forma 

Escalando una forma es una operación más peligrosa porque, a diferencia de la traslación o rotación, un escalado no uniforme (con diferentes valores para los ejes X,Y y Z) puede modificar la estructura de la forma. Por ejemplo, escalando una circunferencia con un valor horizontal superior al vertical la transformará en una elipse, que se comporta matemáticamente de forma muy diferente. Para el escalado, no podemos utilizar transformShape, tenemos que usar transformGeometry():


</div>

Scaling a shape is a more dangerous operation because, unlike translation or rotation, scaling non-uniformly (with different values for X, Y and Z) can modify the structure of the shape. For example, scaling a circle with a higher value horizontally than vertically will transform it into an ellipse, which behaves mathematically very differently. For scaling, we cannot use the `transformShape()`, we must use `transformGeometry()`: 
```python
myMat = Base.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```{{Top}}


<div class="mw-translate-fuzzy">

### Operaciones Booleanas 


</div>


<div class="mw-translate-fuzzy">

#### Diferencia

La diferencia de una forma con otra se llama \"corte\" en el argot de OCC/FreeCAD y se hace así:


</div>

Subtracting a shape from another one is called \"cut\" in FreeCAD and is done like this: 
```python
cylinder = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
sphere = Part.makeSphere(5, Base.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```{{Top}}


<div class="mw-translate-fuzzy">

#### Intersección

del mismo modo, la intersección entre dos formas es denominada \"común\" y se hace de este modo:


</div>

The same way, the intersection between two shapes is called \"common\" and is done this way: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```{{Top}}


<div class="mw-translate-fuzzy">

#### Unión

La unión se llama \"fusión\" y funciona del mismo modo:


</div>

Union is called \"fuse\" and works the same way: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```{{Top}}


<div class="mw-translate-fuzzy">

#### Sección

Una sección es la intersección entre una forma de un sólido y una forma de un plano. Devolverá una curva de intersección, un componente con aristas


</div>

A \"section\" is the intersection between a solid shape and a plane shape. It will return an intersection curve, a compound curve composed of edges. 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
section = cylinder1.section(cylinder2)
section.Wires
> []
section.Edges
> [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
 <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
 <Edge object at 0D8F4BB0>]
```{{Top}}


<div class="mw-translate-fuzzy">

#### Extrusión

Extrusión es el acto de \"empujar\" una forma plana en determinada dirección resultando en un cuerpo sólido. Piensa en una círculo convirtiéndose en un tubo:


</div>

Extrusion is the act of \"pushing\" a flat shape in a certain direction, resulting in a solid body. Think of a circle becoming a tube by \"pushing it out\": 
```python
circle = Part.makeCircle(10)
tube = circle.extrude(Base.Vector(0, 0, 2))
```


<div class="mw-translate-fuzzy">

Si tu círculo está hueco, obtendrás un tubo hueco. Si no es hueco, obtendrás un cilindro sólido:


</div>


```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(Base.Vector(0, 0, 2))
```


{{Top}}


<div class="mw-translate-fuzzy">

## Exploración de formas 

Puedes explorar fácilmente la estructura de datos topológicos:


</div>

You can easily explore the topological data structure: 
```python
import Part
b = Part.makeBox(100, 100, 100)
b.Wires
w = b.Wires[0]
w
w.Wires
w.Vertexes
Part.show(w)
w.Edges
e = w.Edges[0]
e.Vertexes
v = e.Vertexes[0]
v.Point
```


<div class="mw-translate-fuzzy">

Escribiendo las líneas de arriba en el interprete de Python, conseguirás una buena comprensión de la estructura de los objetos de piezas. Aquí, nuestro comando makeBox() crea una forma sólida. Este sólido, como todos los sólidos de piezas, contiene caras. Las caras siempre contienen contornos, que son listas de aristas que bordean la cara. Cada cara tiene al menos un contorno cerrado (puede tener más si la cara tiene huecos). En el contorno, podemos mirar en cada arista de forma separada, y dentro de cada arista, podemos ver los vértices. Las aristas rectas tienen sólo dos vértices, obviamente.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Análisis de aristas 

En el caso de una arista con una curva arbitraria, es más probable que quieras hacer una discretización. En FreeCAD las aristas son parametrizadas por sus longitudes. Eso significa que puedes recorrer una arista/curva por su longitud:


</div>

In case of an edge, which is an arbitrary curve, it\'s most likely you want to do a discretization. In FreeCAD the edges are parametrized by their lengths. That means you can walk an edge/curve by its length: 
```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
```


<div class="mw-translate-fuzzy">

Ahora puedes acceder a un montón de propiedades de la arista utilizando la longitud como una posición. Eso significa que si la arista es de 100mm de longitud el punto inicial es y la posición final es 100.


</div>


```python
anEdge.tangentAt(0.0)          # tangent direction at the beginning
anEdge.valueAt(0.0)            # Point at the beginning
anEdge.valueAt(100.0)          # Point at the end of the edge
anEdge.derivative1At(50.0)     # first derivative of the curve in the middle
anEdge.derivative2At(50.0)     # second derivative of the curve in the middle
anEdge.derivative3At(50.0)     # third derivative of the curve in the middle
anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
anEdge.curvatureAt(50.0)       # the curvature
anEdge.normalAt(50)            # normal vector at that position (if defined)
```


{{Top}}


<div class="mw-translate-fuzzy">

### Utilizando la selección 

Aquí vemos ahora cómo podemos utilizar la selección que el usuario hizo en la vista. Antes de nada creamos un cubo y lo mostramos en la vista


</div>

Here we see now how we can use a selection the user did in the viewer. First of all we create a box and show it in the viewer. 
```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
```


<div class="mw-translate-fuzzy">

Selecciona ahora algunas caras o aristas. Con este archivo de guión puedes iterar todos los objetos seleccionados y sus subelementos:


</div>


```python
for o in Gui.Selection.getSelectionEx():
    print(o.ObjectName)
    for s in o.SubElementNames:
        print("name: ", s)
        for s in o.SubObjects:
            print("object: ", s)
```

Selecciona algunas aristas y este archivo de guión calculará la longitud: 
```python
length = 0.0
for o in Gui.Selection.getSelectionEx():
    for s in o.SubObjects:
        length += s.Length

print("Length of the selected edges: ", length)
```{{Top}}


<div class="mw-translate-fuzzy">

## Examen completo: La botella OCC 

Un ejemplo típico encontrado en la [página de primeros pasos de OpenCasCade](http://www.opencascade.org/org/gettingstarted/appli/) es cómo construir una botella. Este es un buen ejercicio también para FreeCAD. En realidad, puedes seguir nuestro ejemplo de abajo y la página de OCC simultáneamente, comprenderás bien cómo están implementadas las estructuras de OCC en FreeCAD. El archivo de guión completo de abajo está también incluido en la instalación de FreeCAD (dentro del directorio Mod/Part) y puede llamarse desde el interprete de Python escribiendo:


</div>

A typical example found on the [OpenCasCade Technology website](https://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html) is how to build a bottle. This is a good exercise for FreeCAD too. In fact, if you follow our example below and the OCC page simultaneously, you will see how well OCC structures are implemented in FreeCAD. The script is included in the FreeCAD installation (inside the {{FileName|Mod/Part}} folder) and can be called from the Python interpreter by typing: 
```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```{{Top}}


<div class="mw-translate-fuzzy">

### El archivo de guión completo 

Aquí está el archivo de guión completo MakeBottle:


</div>

For the purpose of this tutorial we will consider a reduced version of the script. In this version the bottle will not be hollowed out, and the neck of the bottle will not be threaded. 
```python
import Part, math
from FreeCAD import Base

def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)

    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

el = makeBottleTut()
Part.show(el)
```{{Top}}


<div class="mw-translate-fuzzy">

### Explicación detallada 


</div>


```python
import Part, math
from FreeCAD import Base
```


<div class="mw-translate-fuzzy">

Necesitaremos, desde luego, el módulo de piezas, pero también el módulo FreeCAD.Base, que contiene estructuras básicas de FreeCAD como vectores y matrices.


</div>


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)
```


<div class="mw-translate-fuzzy">

Aquí definimos nuestra función makeBottle. Esta función se puede llamar sin argumentos, como hicimos arriba, en cuyo caso se utilizaran los valores por defecto para ancho, alto, y espesor. Luego, definimos un conjunto de puntos que serán utilizados para construir nuestro perfil base.


</div>


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```


<div class="mw-translate-fuzzy">

Aquí en realidad definimos la geometría: un arco, creado por 3 puntos, y dos segmentos de línea, creados por 2 puntos.


</div>


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```


<div class="mw-translate-fuzzy">

Recuerdas la diferencia entre geometría y formas? Aquí construimos formas a partir de nuestra geometría de construcción. 3 aristas (las aristas pueden ser rectas o curvas), luego un contorno creado a partir de dichas tres aristas.


</div>


```python
    ...
    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])
```


<div class="mw-translate-fuzzy">

Hasta ahora construimos sólo medio perfil. Más sencillo que construir el perfil completo del mismo modo, simplemente podemos crear una simetría de lo que hicimos, y pegar ambas partes. Así primero creamos una matriz. Una matriz es un modo muy común para aplicar transformaciones a objetos en el mundo 3D, ya que puede contener en una estructura todas las transformaciones básicas que los objetos pueden sufrir (mover, rotar y escalar). Aquí, después de crear la matriz, creamos una simétrica, y creamos una copia de nuestro contorno con esa matriz de transformación aplicada. Ahora tenemos 2 contornos, y podemos crear un tercer contorno a partir de ellos, ya que los contornos son en realidad listas de aristas.


</div>


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```


<div class="mw-translate-fuzzy">

Ahora que tenemos un contorno cerrado, se puede convertir en una cara. Una vez que tengamos una cara, podemos extruirla. Haciendo esto, creamos un sólido. Entonces aplicamos un pequeño redondeo a nuestro objeto porque queremos crear un buen diseño, no es así?


</div>


```python
    ...
    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
```


<div class="mw-translate-fuzzy">

El cuerpo de nuestra botella está creado, aún tenemos que crear el cuello. Así que creamos un nuevo sólido, con un cilindro.


</div>


```python
    ...
    myBody = myBody.fuse(myNeck)
```


<div class="mw-translate-fuzzy">

La operación de fusión, que en otras aplicaciones es llamada unión, es muy potente. Tendrá cuidado de pegar lo que necesita ser pegado y eliminar las partes que necesiten ser eliminadas.


</div>


```python
    ...
    return myBody
```


<div class="mw-translate-fuzzy">

Obtenemos nuestro sólido de pieza como resultado de nuestra función. Ese sólido de pieza, como cualquier otra forma de piezas, se puede atribuir a un objeto en el documento de FreeCAD, con:


</div>


```python
el = makeBottleTut()
Part.show(el)
```


<div class="mw-translate-fuzzy">

o, de forma más simple:


</div>


{{Top}}

## Example: Pierced box 

Here is a complete example of building a pierced box.

The construction is done one side at a time. When the cube is finished, it is hollowed out by cutting a cylinder through it. 
```python
import Part, math
from FreeCAD import Base

size = 10
poly = Part.makePolygon([(0, 0, 0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])

face1 = Part.Face(poly)
face2 = Part.Face(poly)
face3 = Part.Face(poly)
face4 = Part.Face(poly)
face5 = Part.Face(poly)
face6 = Part.Face(poly)
     
myMat = Base.Matrix()

myMat.rotateZ(math.pi / 2)
face2.transformShape(myMat)
face2.translate(Base.Vector(size, 0, 0))

myMat.rotateZ(math.pi / 2)
face3.transformShape(myMat)
face3.translate(Base.Vector(size, size, 0))

myMat.rotateZ(math.pi / 2)
face4.transformShape(myMat)
face4.translate(Base.Vector(0, size, 0))

myMat = Base.Matrix()

myMat.rotateX(-math.pi / 2)
face5.transformShape(myMat)

face6.transformShape(myMat)               
face6.translate(Base.Vector(0, 0, size))

myShell = Part.makeShell([face1, face2, face3, face4, face5, face6])   
mySolid = Part.makeSolid(myShell)

myCyl = Part.makeCylinder(2, 20)
myCyl.translate(Base.Vector(size / 2, size / 2, 0))

cut_part = mySolid.cut(myCyl)

Part.show(cut_part)
```{{Top}}


<div class="mw-translate-fuzzy">

## Cargando y guardando 

Existen diversas formas de guardar tu trabajo en el módulo de piezas. Puedes desde luego guardar el documento de FreeCAD, pero también puedes guardar objetos de pieza directamente en formatos de CAD comunes, como BREP, IGS, STEP y STL.


</div>

There are several ways to save your work. You can of course save your FreeCAD document, but you can also save [Part](Part_Workbench.md) objects directly to common CAD formats, such as BREP, IGS, STEP and STL.


<div class="mw-translate-fuzzy">

El guardado de una forma en un archivo es sencillo. Existen los métodos exportBrep(), exportIges(), exportStl() y exportStep() disponibles para todos los objetos de forma. Así, haciendo:


</div>


```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
```


<div class="mw-translate-fuzzy">

se guardará nuestro cubo en un archivo STEP. Para cargar un archivo BREP, IGES o STEP, simplemente haz lo contrario:


</div>


```python
import Part
s = Part.Shape()
s.read("test.stp")
```

To convert a STEP file to an IGS file: 
```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```{{Top}} {{Powerdocnavi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
