# Mesh to Part/es



{{TOCright}}


<div class="mw-translate-fuzzy">

## Convertir Objetos parte en mallas 


</div>


<div class="mw-translate-fuzzy">

La conversión de objetos de alto nivel, tales como [formas de Piezas](Part_Workbench/es.md) en objetos más simples como [mallas](Mesh_Workbench/es.md) es una operación bastante sencilla, en la que todas las caras de un objeto Pieza son triangularizadas. El resultado de esa triangulación (o teselado) se utiliza para construir una malla:


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

## Convertir Mallas en objetos Pieza 


</div>


<div class="mw-translate-fuzzy">

La conversión de mallas en objetos Pieza es una operación muy importante en el trabajo de CAD, ya que a menudo se reciben datos 3D en formato de malla de otras personas o son generados con otras aplicaciones. Las mallas son muy prácticas para representar la geometría de forma libre y para grandes escenas visuales, ya que son muy ligeras. Pero, por lo general, el CAD prefiere objetos de nivel superior que llevan mucha más información, como la idea de sólidos, o caras hechas de curvas, en lugar de triángulos.


</div>


<div class="mw-translate-fuzzy">

La conversión de las mallas a esos objetos de nivel superior (manejados por el [Módulo de Piezas](Part_Workbench/es.md) en FreeCAD) no es una operación fácil. Las mallas pueden tener miles de triángulos (por ejemplo, los generados por un escáner 3D), y si los sólidos se hacen con el mismo número de caras, serían extremadamente pesados de manipular. Así que por lo general, se desea optimizar el objeto durante la conversión.


</div>


<div class="mw-translate-fuzzy">

FreeCAD actualmente ofrece dos métodos para convertir mallas en piezas. El primer método es una conversión sencilla, directa, sin ningún tipo de optimización:


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

El segundo método ofrece la posibilidad de considerar coplanares las facetas de malla que forman entre si un pequeño ángulo. Esto permite la construcción de formas mucho más simples:


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


{{Powerdocnavi

}} {{Mesh Tools navi}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
