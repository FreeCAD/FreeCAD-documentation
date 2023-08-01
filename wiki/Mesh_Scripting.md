# Mesh Scripting
## Introduction

To get access to the `Mesh` module you have to import it first:

 
```python
import Mesh
```

## Creation

To create an empty mesh object just use the standard constructor:

 
```python
mesh = Mesh.Mesh()
```

You can also create an object from a file:

 
```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

Or create it out of a set of triangles described by their corner points:

 
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

The Mesh-Kernel takes care of creating a topologically correct data structure by sorting coincident points and edges.



## Modeling

To create regular geometries you can use one of the `create*()` methods. A torus, for instance, can be created as follows:

 
```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```

The first two parameters define the radii of the torus and the third parameter is a sub-sampling factor for how many triangles are created. The higher this value the smoother the mesh.

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

Here is an example that creates a pipe using the `difference()` method:

 
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



## Notes

An extensive, though hard to use, source of mesh related scripting are the unit test scripts of the `Mesh` module. In these unit tests literally all methods are called and all properties/attributes are tweaked. So if you are bold enough, take a look at the [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

See also: [Mesh API](Mesh_API.md).



  {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh Scripting
