# Mesh to Part/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

## Conversia obiectelor Piese în Plasă 


</div>


<div class="mw-translate-fuzzy">

Conversia obiectelor de nivel superior, cum ar fi [Part shell](Part_Workbench.md) în obiecte mai simple, cum ar fi [meshes](Mesh_Workbench.md) este o operație simplă, în care toate fațetele unui obiect Piesă i se aplică o discretizarea în triunghiur. Rezultatul acestei discretizări(tessellation) este apoi folosit pentru a construi o plasă   * (să presupunem că documentul nostru conține un obiect de piesă)


</div>


```python
import Mesh

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape
faces = []

triangles = shp.tessellate(1) # the number represents the precision of the tessellation
for tri in triangles[1]   *
    face = []
    for i in tri   *
        face.append(triangles[0][i])
    faces.append(face)

m = Mesh.Mesh(faces)
Mesh.show(m)
```

Alternative example   *


```python
import Mesh
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape

mesh = FreeCAD.ActiveDocument.addObject("Mesh   *   *Feature", "Mesh")
mesh.Mesh = MeshPart.meshFromShape(
        Shape=shp,
        LinearDeflection=0.01,
        AngularDeflection=0.025,
        Relative=False)
```


<div class="mw-translate-fuzzy">

## Convertirea Plaselor în obiecte Part 


</div>


<div class="mw-translate-fuzzy">

Convertirea ochiurilor de plasă în obiecte piese este o operație extrem de importantă în lucrul cu CAD, pentru că de multe ori primiți date 3D în format de ochiuri de plasă de la alte persoane sau ieșite din alte aplicații. Meshurile sunt foarte practice pentru a reprezenta geometria liberă și pentru scenele vizuale mari, deoarece este foarte ușoară, dar pentru CAD, în general, preferăm obiecte de nivel mai înalt care transportă mult mai multe informații, cum ar fi ideea de solid sau fațetele făcute din curbe în loc de triunghiuri.


</div>


<div class="mw-translate-fuzzy">

Convertirea ochiurilor de plasă în obiecte de nivel superior (manipulate de [Part Workbench](Part_Workbench.md) în FreeCAD) nu este o operație ușoară. Mesh-urile pot fi realizate din mii de triunghiuri (de exemplu, atunci când sunt generate de un scanner 3D) și având solide realizate din același număr de fețe ar fi extrem de greu de manipulat. Deci, în general, doriți să optimizați obiectul când faceți conversia.


</div>


<div class="mw-translate-fuzzy">

FreeCAD oferă în prezent două metode pentru a transforma Plasele în obiecte piese (Part). Prima metodă este o conversie simplă, directă, fără optimizare   *


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

Cea de-a doua metodă oferă posibilitatea de a considera aspectul ochiurilor de plasă coplanare atunci când unghiul dintre ele este sub o anumită valoare. Acest lucru permite construirea unor forme mai simple   * (să presupunem că documentul nostru conține un obiect Mesh)


</div>


```python
import Mesh
import Part
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Mesh object must be preselected
mesh = obj.Mesh
segments = mesh.getPlanarSegments(0.00001) # use rather strict tolerance here
faces = []

for i in segments   *
    if len(i) > 0   *
        # a segment can have inner holes
        wires = MeshPart.wireFromSegment(mesh, i)
        # we assume that the exterior boundary is that one with the biggest bounding box
        if len(wires) > 0   *
            ext = None
            max_length=0
            for i in wires   *
                if i.BoundBox.DiagonalLength > max_length   *
                    max_length = i.BoundBox.DiagonalLength
                    ext = i

            wires.remove(ext)
            # all interior wires mark a hole and must reverse their orientation, otherwise Part.Face fails
            for i in wires   *
                i.reverse()

            # make sure that the exterior wires comes as first in the list
            wires.insert(0, ext)
            faces.append(Part.Face(wires))

solid = Part.Solid(Part.Shell(faces))
Part.show(solid)
```


 {{Mesh Tools navi}}

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/ro
