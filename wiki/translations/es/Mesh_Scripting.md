# Mesh Scripting/es
{{TOCright}}

## Introducción

Para obtener acceso al módulo `Malla` hay que importarlo primero:


```python
import Mesh
```

## Creación

Para crear un objeto de malla vacío basta con utilizar el constructor estándar:


```python
mesh = Mesh.Mesh()
```

También puede crear un objeto a partir de un archivo:


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

O crearla a partir de un conjunto de triángulos descritos por sus puntos de esquina:


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

El Núcleo-Malla se encarga de crear una estructura de datos topológicamente correcta ordenando los puntos y aristas coincidentes. {{Top}}

## Modelización

Para crear geometrías regulares se puede utilizar uno de los métodos `create*()`. Un toroide, por ejemplo, se puede crear de la siguiente manera:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```

Los dos primeros parámetros definen los radios del toroide y el tercer parámetro es un factor de submuestreo para saber cuántos triángulos se crean. Cuanto mayor sea este valor, más suave será la malla.

El módulo `Malla` también proporciona tres métodos booleanos: `union()`, `intersection()` y `difference()`:


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

Este es un ejemplo que crea una tubería utilizando el método `difference()`:


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


{{Top}}

## Notas

Una fuente extensa, aunque difícil de usar, de scripts relacionados con la malla son los scripts de pruebas unitarias del módulo `Mesh`. En estas pruebas unitarias se llaman literalmente todos los métodos y se ajustan todas las propiedades/atributos. Así que si eres lo suficientemente audaz, echa un vistazo al módulo [Unit Test](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

Ver también: [Interfaz de programación de aplicaciones Malla](Mesh_API.md). {{Top}} {{Powerdocnavi}} {{Mesh Tools navi}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Mesh](Mesh_Workbench.md) > Mesh Scripting/es
