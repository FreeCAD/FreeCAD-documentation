# Mesh to Part/sv
{{TOCright}}


<div class="mw-translate-fuzzy">

## Konvertera Del objekt till Nät 


</div>


<div class="mw-translate-fuzzy">

Att konvertera högnivåobjekt som [Del former](Part_Workbench/sv.md) till enklare objekt som [nät](Mesh_Workbench/sv.md) är en ganska enkel operation, där alla ytor på ett Del objekt blir triangulerade. Resultatet av denna triangulering (tessellering) används sedan till att konstruera ett nät: (Låt oss anta att vårt dokument innehåller ett Del objekt)


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

## Konvertera Nät till Del objekt 


</div>


<div class="mw-translate-fuzzy">

Konvertering av Nät till Del objekt är en mycket viktig operation i CAD arbete, eftersom du mycket ofta tar emot 3D data i nätformat från andra människor eller utmatade från andra applikationer. Nät är mycket praktiskt för att representera friformsgeometri och stora visuella scener, eftersom den är mycket kompakt, men för CAD föredrar vi i allmänhet mer högnivåobjekt som bär mycket mer information, som solider, eller ytor som är skapade av kurvor istället för trianglar.


</div>


<div class="mw-translate-fuzzy">

Konvertering av nät till dessa högnivåobjekt (hanterat av [Del Modulen](Part_Workbench/sv.md) i FreeCAD) är inte en lätt operation. Nät kan vara gjord av tusentals trianglar (till exempel när de är genererade av en 3D skanner), och att ha solider gjorda med samma antal ytor skulle bli väldigt tungrott att manipulera. Så generellt sett så vill du optimera objektet när du konverterar.


</div>


<div class="mw-translate-fuzzy">

FreeCAD erbjuder för närvarande två metoder för att konvertera Nät till Del objekt. Den första metoden är en enkel, direkt konvertering, utan någon optimering:


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

Den andra metoden erbjuder möjligheten att anse nätfasetter koplanära när vinkeln mellan dem är under ett visst värde. Detta tillåter uppbyggnad av mycket enklare former: (Låt oss anta att vårt dokument innehåller ett Nät objekt)


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

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/sv
