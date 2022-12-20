# Mesh to Part/pl
{{TOCright}}

### Konwersja obiektów środowiska Część do siatek 

Konwersja obiektów wyższego poziomu takich jak [część](Part_Workbench/pl.md) środowiska Część, na prostsze obiekty takie jak [siatka](Mesh_Workbench/pl.md) środowiska Projekt Siatki jest całkiem prostą operacją, gdzie wszystkie ściany obiektu Część są triangulowane. Wynik tej triangulacji *(teselacji)* jest następnie używany do skonstruowania siatki:


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

Przykład alternatywny:


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

## Konwersja siatki do obiektów środowiska Część 

Konwersja siatek na obiekty Część jest często wykonywaną operacją. Bardzo często otrzymuje się dane 3D w formacie siatki. Siatki są dość praktyczne do reprezentowania geometrii o dowolnym kształcie i dużych scen wizualnych, ponieważ są bardzo lekkie. Jednak w programie FreeCAD preferujemy obiekty wyższego poziomu, bryły, które mogą przenosić znacznie więcej informacji i pozwalają na zakrzywione ściany.

Konwersja siatek do obiektów wyższego poziomu *(obsługiwana przez środowisko pracy [Część](Part_Workbench/pl.md) w FreeCAD)* nie jest łatwą operacją. Siatki mogą zawierać tysiące trójkątów *(np. gdy są generowane przez skaner 3D)*, a bryły złożone z takiej samej liczby ścian byłyby niezwykle trudne do manipulowania. Więc generalnie chcesz zoptymalizować obiekt podczas konwersji.

FreeCAD oferuje obecnie dwie metody konwersji siatek na obiekty Część. Pierwsza metoda to prosta, bezpośrednia konwersja bez żadnej optymalizacji:


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```

Druga metoda oferuje możliwość uwzględnienia ścianek siatki jako współpłaszczyznowych, gdy kąt między nimi jest mniejszy od określonej wartości, zmniejszając liczbę ścian w wyniku końcowym:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/pl
