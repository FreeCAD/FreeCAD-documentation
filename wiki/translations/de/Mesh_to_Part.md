# Mesh to Part/de
{{TOCright}}

## Umwandeln von Teilobjekten in Polygonnetze 

Die Konvertierung von übergeordneten Objekten wie [Teil](Part_Workbench/de.md) formen in einfachere Objekte wie [Polygonnetz](Mesh_Workbench/de.md) ist ein sehr einfacher vorwärtsgerichteter Vorgang, bei der alle Flächen eines Teilobjekts trianguliert werden. Das Ergebnis dieser Triangulation (Tesselierung) wird dann zum Aufbau eines Polygonnetzes verwendet:


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

Alternativbeispiel:


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

## Umwandlung von Polygonnetzen in Teilobjekte 

Die Umwandlung von Netzen in Teilobjekte ist ein gängiger Vorgang. Sehr oft erhälst du 3D Daten in einem Netzformat. Netze sind sehr praktisch für die Darstellung von Freiformgeometrie und großen visuellen Szenen, da sie sehr leicht sind. In FreeCAD bevorzugen wir jedoch im Allgemeinen übergeordnete Objekte, Volumenkörper, die viel mehr Informationen tragen können und gekrümmte Flächen ermöglichen.

Das Umwandeln von Netzen in diese übergeordneten Objekte (die vom [Part-Arbeitsbereich](Part_Workbench/de.md) in FreeCAD behandelt werden) ist keine einfache Operation. Netze können Tausende von Dreiecken enthalten (z.B. wenn sie von einem 3D Scanner erzeugt werden), und Körper, die aus der gleichen Anzahl von Flächen bestehen, wären extrem schwierig zu bearbeiten. Daher möchtest du im Allgemeinen das Objekt bei der Konvertierung optimieren.

FreeCAD bietet derzeit zwei Möglichkeiten, Polygonnetze in Bauteilobjekte zu konvertieren. Die erste Methode ist eine einfache, direkte Umwandlung, ohne jegliche Optimierung:


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```

Die zweite Methode bietet die Möglichkeit, Polygonnetzfacetten koplanar zu betrachten, wenn der Winkel zwischen ihnen unter einem bestimmten Wert liegt, wodurch die Anzahl der Flächen im Endergebnis reduziert wird:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/de
