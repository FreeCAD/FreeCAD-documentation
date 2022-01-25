# Mesh to Part/it
{{TOCright}}


<div class="mw-translate-fuzzy">

## Convertire oggetti Parte in Mesh 


</div>


<div class="mw-translate-fuzzy">

La conversione di oggetti di alto livello come le [forme di Parte](Part_Workbench/it.md) in oggetti semplici come gli [oggetti Mesh](Mesh_Workbench/it.md) è una operazione piuttosto semplice, nella quale tutte le facce di un oggetto Parte vengono triangolate (suddivise in maglie di una rete). Il risultato di tale triangolazione (tassellatura) viene poi utilizzato per costruire un oggetto mesh: (supponiamo che il nostro documento contenga un oggetto Parte)


</div>


```python
import Mesh

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape
faces = []

triangles = shp.tessellate(1) # the number represents the precision of the tessellation
for tri in triangles[1]:
    face = []
    for i in tri:
        face.append(triangles[0][i])
    faces.append(face)

m = Mesh.Mesh(faces)
Mesh.show(m)
```

Alternative example:


```python
import Mesh
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape

mesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh.Mesh = MeshPart.meshFromShape(
        Shape=shp,
        LinearDeflection=0.01,
        AngularDeflection=0.025,
        Relative=False)
```


<div class="mw-translate-fuzzy">

## Convertire oggetti Mesh in Parte 


</div>


<div class="mw-translate-fuzzy">

La conversione di oggetti Mesh in oggetti Parte è un\'operazione estremamente importante nel lavoro CAD perché molto spesso i dati 3D si ricevono da altri in formato mesh o sono generati da altre applicazioni. I mesh sono molto pratici per rappresentare le geometrie di forma libera e grandi scene visive in quanto sono molto leggeri, ma per lavori CAD si preferiscono generalmente oggetti di livello superiore, che contengono molte più informazioni, come il concetto di solido, o facce composte da curve invece che da triangoli.


</div>


<div class="mw-translate-fuzzy">

Convertire gli oggetti mesh in oggetti di livello superiore, come sono gli oggetti gestiti dal [Modulo Parte](Part_Workbench/it.md) di FreeCAD non è un\'operazione facile. L\'oggetto Mesh può contenere migliaia di triangoli (per esempio quando è generato da uno scanner 3D), e manipolare solidi costituiti dallo stesso numero di facce sarebbe estremamente pesante. Quindi, in genere, si desidera ottimizzare l\'oggetto durante la conversione.


</div>


<div class="mw-translate-fuzzy">

FreeCAD attualmente offre due metodi per convertire Mesh in oggetti Parte. Il primo metodo è una semplice conversione, diretta, senza alcuna ottimizzazione:


</div>


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```


<div class="mw-translate-fuzzy">

Il secondo metodo offre la possibilità di considerare complanari le sfaccettature delle maglie quando l\'angolo tra di loro è inferiore a un certo valore. Questo permette di costruire delle forme molto più semplici: (supponiamo che il nostro documento contenga un oggetto Mesh)


</div>


```python
import Mesh
import Part
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Mesh object must be preselected
mesh = obj.Mesh
segments = mesh.getPlanarSegments(0.00001) # use rather strict tolerance here
faces = []

for i in segments:
    if len(i) > 0:
        # a segment can have inner holes
        wires = MeshPart.wireFromSegment(mesh, i)
        # we assume that the exterior boundary is that one with the biggest bounding box
        if len(wires) > 0:
            ext = None
            max_length=0
            for i in wires:
                if i.BoundBox.DiagonalLength > max_length:
                    max_length = i.BoundBox.DiagonalLength
                    ext = i

            wires.remove(ext)
            # all interior wires mark a hole and must reverse their orientation, otherwise Part.Face fails
            for i in wires:
                i.reverse()

            # make sure that the exterior wires comes as first in the list
            wires.insert(0, ext)
            faces.append(Part.Face(wires))

solid = Part.Solid(Part.Shell(faces))
Part.show(solid)
```


 {{Mesh Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/it
