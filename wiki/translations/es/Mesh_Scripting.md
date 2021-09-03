


{{TOCright}}


<div class="mw-translate-fuzzy">

### Introducción

En primer lugar tienes que importar el módulo Malla:


</div>

To get access to the `Mesh` module you have to import it first:


```python
import Mesh
```


<div class="mw-translate-fuzzy">

### Creación y Carga {#creación_y_carga}

Para crear un objeto malla vacío sólo tienes que utilizar el constructor estándar:


</div>

To create an empty mesh object just use the standard constructor:


```python
mesh = Mesh.Mesh()
```


<div class="mw-translate-fuzzy">

También puedes crear un objeto desde un archivo


</div>


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

O también puedes crear la malla a partir de un conjunto de triángulos descrito por sus vértices:


```python
triangles = [
# triangle 1
[-0.5000, -0.5000, 0.0000], [0.5000, 0.5000, 0.0000], [-0.5000, 0.5000, 0.0000],
#triangle 2
[-0.5000, -0.5000, 0.0000], [0.5000, -0.5000, 0.0000], [0.5000, 0.5000, 0.0000],
]
meshObject = Mesh.Mesh(triangles)
Mesh.show(meshObject)
```


<div class="mw-translate-fuzzy">

El núcleo de mallas, Mesh-Kernel, se encarga de crear una estructura topológica de datos correcta, ordenando conjuntamente los puntos coincidentes y los bordes.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### Modelado

Para crear geometrías regulares puedes utilizar el script de Python BuildRegularGeoms.py.


</div>

To create regular geometries you can use one of the `create*()` methods. A torus, for instance, can be created as follows:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```


<div class="mw-translate-fuzzy">

Los dos primeros parámetros definen los radios del toroide y el tercer parámetro es un factor de submuestreo relacionado con el número de triángulos que se han de crear. Cuanto mayor sea este valor, más suave es la forma y mejor acabado tiene el cuerpo.


</div>

The `Mesh` module also provides three Boolean methods: `union()`, `intersection()` and `difference()`:


```python
m1, m2              # are the input mesh objects
m3 = Mesh.Mesh(m1)  # create a copy of m1
m3.unite(m2)        # union of m1 and m2, the result is stored in m3
m4 = Mesh.Mesh(m1)
m4.intersect(m2)    # intersection of m1 and m2
m5 = Mesh.Mesh(m1)
m5.difference(m2)   # the difference of m1 and m2
m6 = Mesh.Mesh(m2)
m6.difference(m1)   # the difference of m2 and m1, usually the result is different to m5
```


<div class="mw-translate-fuzzy">

Por último, un ejemplo completo que calcula la intersección entre una esfera y un cilindro que corta a la esfera.


</div>


```python
import FreeCAD, Mesh
cylA = Mesh.createCylinder(2.0, 10.0, True, 1.0, 36)
cylB = Mesh.createCylinder(1.0, 12.0, True, 1.0, 36)
cylB.Placement.Base = (FreeCAD.Vector(-1, 0, 0)) # move cylB to avoid co-planar faces
pipe = cylA
pipe = pipe.difference(cylB)
pipe.flipNormals() # somehow required
doc = FreeCAD.ActiveDocument
obj = d.addObject("Mesh::Feature", "Pipe")
obj.Mesh = pipe
doc.recompute()
```

[top](#top.md)


<div class="mw-translate-fuzzy">

### Ajustes y pruebas {#ajustes_y_pruebas}

Una extensa, aunque dificil de usar, librería de archivos de guión relacionados con mallas son los scripts de prueba del módulo Malla. En esta unidad, literalmente todos los métodos son invocados, y se ajustan todas las propiedades y atributos. Así que si eres lo suficientemente audaz, echa un vistazo al [Módulo de prueba de unidades](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Mesh/App/MeshTestsApp.py?view=markup).


</div>

An extensive, though hard to use, source of mesh related scripting are the unit test scripts of the `Mesh` module. In these unit tests literally all methods are called and all properties/attributes are tweaked. So if you are bold enough, take a look at the [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

See also: [Mesh API](Mesh_API.md).

[top](#top.md)


{{Powerdocnavi

}} {{Mesh Tools navi}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
