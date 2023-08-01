# Manual:Creating and manipulating geometry/es
{{Manual:TOC/es}}

En los capítulos anteriores, hemos aprendido sobre los diferentes ambientes de trabajo de FreeCAD, y cómo cada uno de ellos implementa sus propias herramientas y tipos de geometría. El mismo concepto se aplica cuando se trabaja desde el código de Python.

También vimos que la gran mayoría de los ambientes de trabajo de FreeCAD dependen de uno muy fundamental: el [Ambiente de trabajo Pieza](Part_Workbench/es.md). De hecho, muchos otros ambientes de trabajo, como [Borrador](Draft_Workbench/es.md) y [Arquitectura](Arch_Workbench/es.md), hacen exactamente lo que haremos en este capítulo: usar código Python para crear y manipular la geometría de la Pieza.

Así que lo primero que tenemos que hacer para trabajar con la geometría Pieza, es hacer el equivalente en Python a cambiar al Ambiente de trabajo Pieza: importar el módulo Pieza:


```python
import Part 
```

Tómese un minuto para explorar el contenido del módulo Pieza, escribiendo Pieza. y navegando por los diferentes métodos disponibles. El módulo Pieza ofrece varias funciones convenientes como makeBox, makeCircle, etc\... que construirán instantáneamente un objeto para usted. Pruebe esto, por ejemplo:


```python
Part.makeBox(3,5,7) 
```

Entrar en Cuando presione Entrar después de escribir la línea anterior, no aparecerá nada en la vista 3D, pero se imprimirá algo como esto en la consola de Python:


```python
<Solid object at 0x5f43600> 
```

Aquí es donde tiene lugar un concepto importante. Lo que hemos creado aquí es una forma de pieza. No es un objeto de documento de FreeCAD (todavía). En FreeCAD, los objetos y su geometría son independientes. Piensa en un objeto documento de FreeCAD como un contenedor, que albergará una forma. Los objetos paramétricos también tendrán propiedades como Longitud y Anchura, y **recalcularán** su Forma sobre la marcha, siempre que una de las propiedades cambie. Lo que hemos hecho aquí es calcular una forma manualmente.

Ahora podemos crear fácilmente un objeto de documento \"genérico\" en el documento actual (asegúrate de tener al menos un documento nuevo abierto), y darle una forma de caja como la que acabamos de hacer:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Observe como manejamos miObj.Shape , note que se hace exactamente como lo hicimos en el capítulo anterior, cuando cambiamos otras propiedades de un objeto, como box.Height = 5 . De hecho, **Forma** también es una propiedad, al igual que **Altura**\'. Sólo que toma una Forma Pieza, no un número. En el próximo capítulo veremos mejor cómo se construyen estos objetos paramétricos.

Por ahora, vamos a explorar nuestras Formas Pieza con más detalle. Al final del capítulo sobre [modelado tradicional con el Ambiente de trabajo Pieza](Manual:Traditional_modeling,_the_CSG_way/es.md) mostramos una tabla que explica cómo se construyen las Formas Pieza, y sus diferentes componentes (Vértices, aristas, caras, etc). Los mismos componentes existen aquí y pueden ser recuperados desde Python. Las Formas Pieza siempre tienen los siguientes atributos: Vértices, Aristas, Hilos, Caras, Carcasas y Sólidos. Todos ellos son listas, que pueden contener cualquier número de elementos o estar vacías:


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```


<div class="mw-translate-fuzzy">

Por ejemplo, vamos a encontrar el área de cada cara de nuestra forma de caja anterior:


</div>


```python
for f in boxShape.Faces:
   print(f.Area)
```

O, para cada arista, su punto inicial y su punto final:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```

Como ves, si nuestra boxShape tiene un atributo \"Vértices\", cada arista de la boxShape también tiene un atributo \"Vértices\". Como podemos esperar, la boxShape tendrá 8 vértices, mientras que la arista sólo tendrá 2, que son ambos parte de la lista de 8.

Siempre podemos comprobar cuál es el tipo de una forma:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Así que para retomar el tema de las Formas Pieza: Todo comienza con los vértices. Con uno o dos vértices, se forma una Arista (los círculos completos sólo tienen un vértice). Con una o más aristas, se forma un hilo. Con uno o más hilos cerrados, se forma una cara (los hilos adicionales se convierten en \"agujeros\" en la cara). Con una o más Caras, se forma una Cáscara. Cuando una carcasa está completamente cerrada (hermética), se puede formar un sólido a partir de ella. Y, por último, se puede unir cualquier número de formas de cualquier tipo, lo que se denomina un compuesto.

Ahora podemos intentar crear formas complejas desde cero, construyendo todos sus componentes uno a uno. Por ejemplo, intentemos crear un volumen como éste:

![](images/Exercise_python_03.jpg )

Empezaremos creando una forma plana como ésta:

![](images/Wire.png )

En primer lugar, vamos a crear los cuatro puntos base:


```python
V1 = FreeCAD.Vector(0,10,0)
V2 = FreeCAD.Vector(30,10,0)
V3 = FreeCAD.Vector(30,-10,0)
V4 = FreeCAD.Vector(0,-10,0)
```

Entonces podemos crear los dos segmentos lineales:

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```

Ten en cuenta que no necesitamos crear Vértices. Podríamos crear inmediatamente Part.LineSegments a partir de los Vectores de FreeCAD. Esto se debe a que aquí no hemos creado aristas todavía. Un segmento de línea de pieza (al igual que un círculo de pieza, un arco de pieza, una elipse de pieza o una curva de pieza) no crea una arista, sino una geometría base sobre la que se creará una arista. Las aristas siempre se crean a partir de dicha geometría base, que se almacena en su atributo Curva. Así que si tiene una Arista, haciendo:


```python
print(Edge.Curve) 
```

te mostrará qué tipo de arista es, es decir, si está basada en una línea, en un arco, etc\... Pero volvamos a nuestro ejercicio, y construyamos los segmentos de arco. Para esto, necesitaremos un tercer punto, así que podemos usar el conveniente Part.Arc, que toma 3 puntos:

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
C1 = Part.Arc(V1,VC1,V4)
VC2 = FreeCAD.Vector(40,0,0)
C2 = Part.Arc(V2,VC2,V3)
```

Ahora tenemos 2 líneas (L1 y L2) y 2 arcos (C1 y C2). Tenemos que convertirlos en aristas:


```python
E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)
```


<div class="mw-translate-fuzzy">

Alternativamente, las geometrías base también tienen una función toShape() que hace exactamente lo mismo:


</div>


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```


<div class="mw-translate-fuzzy">

Una vez que tenemos una serie de Aristas, ahora podemos formar un Hilo, dándole una lista de Aristas. Debemos tener en cuenta el orden.


</div>


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

Y podemos comprobar si nuestro hilo se ha entendido correctamente, y que está correctamente cerrado:


```python
print( W.isClosed() ) 
```

Que imprimirá \"Verdadero\" o \"Falso\". Para hacer una Cara, necesitamos Hilos cerrados, por lo que siempre es una buena idea comprobarlo antes de crear la Cara. Ahora podemos crear una Cara, dándole un solo Alambre (o una lista de Alambres si queremos agujeros):


```python
F = Part.Face(W) 
```

Entonces lo extruimos:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Tenga en cuenta que P ya es un sólido:


```python
print(P.ShapeType) 
```

Esto se debe a que cuando extruimos una sola Cara, siempre obtenemos un Sólido. Este no sería el caso, por ejemplo, si hubiéramos extruido el Hilo en su lugar:


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Lo que, por supuesto, nos dará una carcasa hueca, a la que le faltan las caras superior e inferior.

Ahora que tenemos nuestra forma final, estamos ansiosos por verla en pantalla. Así que vamos a crear un objeto genérico, y asignarle nuestro nuevo Sólido:


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()
```

Como alternativa, el módulo Pieza también proporciona un acceso directo que realiza la operación anterior más rápidamente (pero no se puede elegir el nombre del objeto):


```python
Part.show(P) 
```

Todo lo anterior, y mucho más, se explica en detalle en la página [Guionización Pieza](Topological_data_scripting/es.md), junto con ejemplos.

**Leer más**

-   [El ambiente de trabajo Pieza](Part_Workbench/es.md)
-   [Guionización Pieza](Topological_data_scripting/es.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/es
