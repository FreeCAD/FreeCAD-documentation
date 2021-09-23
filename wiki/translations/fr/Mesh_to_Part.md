# Mesh to Part/fr
{{TOCright}}

## Conversion d\'objets Part en maillages 

La conversion d\'objets de niveau supérieur tels que les objets [Part](Part_Workbench/fr.md) en objets plus simples tels qu\'en [maillages](Mesh_Workbench/fr.md) est une opération directe où toutes les faces d\'un objet Part sont triangulées. Le résultat de cette triangulation (pavage ou tessellation) est ensuite utilisé pour construire un maillage:


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

Exemple alternatif:


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

## Conversion de maillages en objets Part 

La conversion de maillages en objets Part est une opération très courante. Très souvent, vous recevez des données 3D dans un format maillé. Les maillages sont plutôt pratiques pour représenter la géométrie de forme libre et les grandes scènes visuelles car ils sont très légers. Dans FreeCAD, nous préférons généralement les objets de niveau supérieur, les solides, qui peuvent comporter beaucoup plus d\'informations et permettre des faces courbes.

La conversion es mailles en un de ces objets de niveau supérieur (gérés par l\'[atelier Part](Part_Workbench/fr.md) dans FreeCAD) n\'est pas une opération facile. Le maillage peut contenir des milliers de triangles (par exemple lorsqu\'ils sont générés par un scanner 3D) et les solides constitués du même nombre de faces seraient extrêmement difficiles à manipuler. Donc, vous voudrez généralement voir l\'objet optimisé lors de la conversion.

FreeCAD propose actuellement deux méthodes pour convertir des objets Part en maillage. La première méthode est simple, la conversion directe, sans aucune optimisation:


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```

La deuxième méthode offre la possibilité de considérer les facettes du maillage coplanaires lorsque l\'angle entre elles est inférieur à une certaine valeur, ce qui réduit le nombre de faces dans le résultat final:


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


{{Powerdocnavi

}} {{Mesh Tools navi}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/fr
