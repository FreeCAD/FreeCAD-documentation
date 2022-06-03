# Mesh Scripting/fr
{{TOCright}}

## Introduction

Pour accéder au module `Mesh`, vous devez d\'abord l\'importer   *


```python
import Mesh
```

## Création

Pour créer un objet maillage vide il suffit d\'utiliser la commande standard    *


```python
mesh = Mesh.Mesh()
```

Vous pouvez aussi créer un objet à partir d\'un fichier   *


```python
mesh = Mesh.Mesh("D   */temp/Something.stl")
```

ou créer un ensemble de triangles en les décrivant par leurs sommets (Vertex)    *


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

Le Mesh-Kernel prend soin de créer une structure de données topologiquement correcte en triant les points et les bords coïncidents. {{Top}}

## Modélisation

Pour créer des formes géométriques, vous pouvez utiliser l\'une des méthodes `create*()`. Un tore, par exemple, peut être créé comme suit   *


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```

Les deux premiers paramètres définissent les rayons du tore, et le troisième paramètre est un facteur de sous-échantillonnage pour le nombre de triangles qui seront créés. Plus cette valeur est élevée plus la figure sera lisse.

Le module `Mesh` propose également trois méthodes booléennes   * `union()`, `intersection()` et `difference()`   *


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

Voici un exemple qui crée un tube en utilisant la méthode `difference()`   *


```python
import FreeCAD, Mesh
cylA = Mesh.createCylinder(2.0, 10.0, True, 1.0, 36)
cylB = Mesh.createCylinder(1.0, 12.0, True, 1.0, 36)
cylB.Placement.Base = (FreeCAD.Vector(-1, 0, 0)) # move cylB to avoid co-planar faces
pipe = cylA
pipe = pipe.difference(cylB)
pipe.flipNormals() # somehow required
doc = FreeCAD.ActiveDocument
obj = d.addObject("Mesh   *   *Feature", "Pipe")
obj.Mesh = pipe
doc.recompute()
```


{{Top}}

## Remarques

Les scripts, bien que difficile à utiliser, de test unitaire du module `Mesh` constituent une source étendue de scripts liés au maillage. Dans ces tests unitaires, toutes les méthodes sont appelées et toutes les propriétés / attributs sont modifiés. Donc, si vous êtes assez audacieux, jetez un œil au [module de test unitaire](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

Voir aussi   * [Mesh API](Mesh_API/fr.md). {{Top}}  {{Mesh Tools navi}} 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh Scripting/fr
