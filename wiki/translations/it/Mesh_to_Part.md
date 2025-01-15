# Mesh to Part/it
## Convertire oggetti Parte in Mesh 

La conversione di oggetti di alto livello come le [forme di Parte](Part_Workbench/it.md) in oggetti semplici come gli [oggetti Mesh](Mesh_Workbench/it.md) è una operazione piuttosto semplice, nella quale tutte le facce di un oggetto Parte vengono triangolate (suddivise in maglie di una rete). Il risultato di tale triangolazione (tassellatura) viene poi utilizzato per costruire un oggetto mesh:


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

Esempio alternativo::


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

## Convertire Mesh in oggetti Parte 

La conversione delle mesh in oggetti parte è un\'operazione comune. Molto spesso riceverai dati 3D in formato mesh. Le mesh sono abbastanza pratiche per rappresentare la geometria a forma libera e grandi scene visive, in quanto sono molto leggere. Ma in FreeCAD generalmente preferiamo oggetti di livello superiore, solidi, che possono trasportare molte più informazioni e consentire facce curve.

Convertire gli oggetti mesh in oggetti di livello superiore, come sono gli oggetti gestiti dal [Ambiente Parte](Part_Workbench/it.md) di FreeCAD non è un\'operazione facile. L\'oggetto Mesh può contenere migliaia di triangoli (per esempio quando è generato da uno scanner 3D), e manipolare solidi costituiti dallo stesso numero di facce sarebbe estremamente difficile. Quindi, in genere, si desidera ottimizzare l\'oggetto durante la conversione.

FreeCAD attualmente offre due metodi per convertire mesh in oggetti Parte. Il primo metodo è una semplice conversione, diretta, senza alcuna ottimizzazione:


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```

Il secondo metodo offre la possibilità di considerare complanari le sfaccettature delle maglie quando l\'angolo tra di loro è inferiore a un certo valore, riducendo il numero di facce nel risultato finale:


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
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/it
