# Mesh Scripting/ro
<div class="mw-translate-fuzzy">

### Introducere

Înainte de toate trebuie să importați un modul Mesh:


</div>

To get access to the `Mesh` module you have to import it first:


```python
import Mesh
```


<div class="mw-translate-fuzzy">

### Creație și Încărcare 

Pentru a crea un obiectr vid Plasă utilizați construcția standard:


</div>

To create an empty mesh object just use the standard constructor:


```python
mesh = Mesh.Mesh()
```


<div class="mw-translate-fuzzy">

Puteți crea un obiect din fișierul


</div>


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

Sau o creați dintr-un set de triunghiuri descris de către punctele de colț:


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

Mesh-Kernel are grijă de o structură topologică corectă a datelor prin sortare

împreună a punctelor și marginilor coincidente.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Modelare

Pentru a crea geometrii obișnuite, puteți utiliza scriptul Python BuildRegularGeoms.py.


</div>

To create regular geometries you can use one of the `create*()` methods. A torus, for instance, can be created as follows:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```


<div class="mw-translate-fuzzy">

Primii doi parametri definesc razele toroidului, iar al treilea parametru este un factor de subeșantionare pentru câte triunghiuri sunt create. Cu cât această valoare este mai mare cu atât este mai lină și cu cât este mai groasă corpul. Clasa Mesh oferă un set de funcții booleene care pot fi utilizate în scopuri de modelare. Oferă uniune, intersecție și diferență de două obiecte de plasă.


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

În cele din urmă, un exemplu complet al intersecției între o sferă și un cilindru care intersectează sfera.


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


{{Top}}


<div class="mw-translate-fuzzy">

### Odds and Ends 

O extensie (deși greu de folosit) de scripting Mesh sunt script-urile de testare a Mesh-Module. În această unitate se fac toate testele de compilare și sunt manipulate toate proprietățile și atributele. Cine are curaj îndeajuns, poate privi la [Unit Test module](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Mesh/App/MeshTestsApp.py?view=markup).


</div>

An extensive, though hard to use, source of mesh related scripting are the unit test scripts of the `Mesh` module. In these unit tests literally all methods are called and all properties/attributes are tweaked. So if you are bold enough, take a look at the [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).


<div class="mw-translate-fuzzy">

See also [Mesh API](Mesh_API.md)


</div>


{{Top}}


 {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > [Mesh](Mesh_Workbench.md) > Mesh Scripting/ro
