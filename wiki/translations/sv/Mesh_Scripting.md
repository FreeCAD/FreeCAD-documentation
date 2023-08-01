# Mesh Scripting/sv
<div class="mw-translate-fuzzy">

### Introduktion

Först av allt så måste du importera Nätmodulen:


</div>

To get access to the `Mesh` module you have to import it first:


```python
import Mesh
```


<div class="mw-translate-fuzzy">

### Skapande och laddning 

För att skapa ett tomt nätobjekt använd standardkonstruktören:


</div>

To create an empty mesh object just use the standard constructor:


```python
mesh = Mesh.Mesh()
```


<div class="mw-translate-fuzzy">

Du kan också skapa ett objekt från en fil


</div>


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

Eller skapa det från ett set av trianglar, beskrivna av dess hörnpunkter:


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

Mesh-Kernel tar hand om skapandet av en topologiskt korrekt datastruktur genom att sortera sammanfallande punkter och kanter tillsammans.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Modellering

För att skapa reguljärageometrier så kan du används Python skriptet BuildRegularGeoms.py.


</div>

To create regular geometries you can use one of the `create*()` methods. A torus, for instance, can be created as follows:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```


<div class="mw-translate-fuzzy">

De första två parametrarna definierar toroidens radier och den tredje parametern är en sub-sampling faktor för hur många trianglar som skapas. Ju högre värde på denna faktorn, desto jämnare blir kroppen.

Nät klassen har ett set med booleska funktioner som kan användas för modelleringsändamål. Den erbjuder förening, skärning och skillnad mellan två nätobjekt.


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

Slutligen, ett komplett exempel som beräknar skärningen mellan en sfär och en cylinder som skär sfären.


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

### Special

En extensiv, fast svåranvänd, källa för Nätrelaterade skript är Nätmodulens enhetstestskript. I detta enhetstest så kallas samtliga metoder och samtliga egenskaper/attribut ändras. Så om du är tillräckligt modig, ta en titt på [Unit Test module](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Mesh/App/MeshTestsApp.py?view=markup).


</div>

An extensive, though hard to use, source of mesh related scripting are the unit test scripts of the `Mesh` module. In these unit tests literally all methods are called and all properties/attributes are tweaked. So if you are bold enough, take a look at the [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

See also: [Mesh API](Mesh_API.md). {{Top}}  {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh Scripting/sv
