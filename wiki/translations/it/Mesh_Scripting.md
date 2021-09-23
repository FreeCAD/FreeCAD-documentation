# Mesh Scripting/it



{{TOCright}}


<div class="mw-translate-fuzzy">

### Introduzione

Prima di tutto si deve importare il modulo Mesh:


</div>

To get access to the `Mesh` module you have to import it first:


```python
import Mesh
```


<div class="mw-translate-fuzzy">

### Creazione e caricamento 

Per creare un oggetto mesh vuoto basta usare il costruttore standard:


</div>

To create an empty mesh object just use the standard constructor:


```python
mesh = Mesh.Mesh()
```


<div class="mw-translate-fuzzy">

Inoltre è possibile creare un oggetto da un file


</div>


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

Oppure crearlo tramite un gruppo di triangoli descritti dai loro vertici:


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

Il Kernel Mesh si occupa di creare una corretta struttura topologica dei dati individuando i punti e i bordi coincidenti.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Modellazione

Per creare delle geometrie regolari è possibile utilizzare lo script Python BuildRegularGeoms.py.


</div>

To create regular geometries you can use one of the `create*()` methods. A torus, for instance, can be created as follows:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```


<div class="mw-translate-fuzzy">

I primi due parametri definiscono i raggi del toroide e il terzo parametro è un fattore di sub-campionamento che stabilisce quanti triangoli vengono creati. Maggiore è questo valore e più il corpo è liscio, più questo valore è piccolo e più il corpo è grossolano (sfaccettato).

La classe Mesh fornisce una serie di funzioni booleane che possono essere utilizzate per operazioni di modellazione. Essa fornisce l\'unione, l\'intersezione e la differenza tra due oggetti mesh.


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

Ecco infine, un esempio completo che calcola l\'intersezione tra una sfera e un cilindro che interseca la sfera.


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

### Prove

Una nutrita (anche se difficile da usare) libreria di script riferiti a Mesh sono gli script dell\'unita di test del Modulo Mesh. In questa unit test sono letteralmente chiamati tutti i metodi e sono ottimizzate tutte le proprietà e gli attributi. Quindi, se siete abbastanza coraggiosi, date un\'occhiata al [modulo unit test](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Mesh/App/MeshTestsApp.py?view=markup).


</div>

An extensive, though hard to use, source of mesh related scripting are the unit test scripts of the `Mesh` module. In these unit tests literally all methods are called and all properties/attributes are tweaked. So if you are bold enough, take a look at the [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).


<div class="mw-translate-fuzzy">

Vedere anche [Mesh API](Mesh_API/it.md)


</div>


{{Top}}


{{Powerdocnavi

}} {{Mesh Tools navi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
