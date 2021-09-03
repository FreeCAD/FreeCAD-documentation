


<div class="mw-translate-fuzzy">





</div>

## Descrizione


<div class="mw-translate-fuzzy">

Oltre all\'esportatore [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file) standard di FreeCAD, il [Modulo Architettura](Arch_Workbench/it.md) dispone di un esportatore alternativo che esporta le facce complanari come facce OBJ intere, invece di triangolazioni eseguite su oggetti costruiti su [forme](Shape/it.md) di base, come fa l\'esportatore standard.


</div>

## Exporting without GUI {#exporting_without_gui}

Exporting without the graphical interface is possible from the command line, using the [Mesh Workbench](Mesh_Workbench.md) exporter only.

In this example, a STEP file is imported, the colors of the [Shape](Shape.md) are saved, then a mesh is created from it, the colors of the original object are re-applied to the faces of the new mesh, which is then exported to OBJ format. Since this is done with the Mesh Workbench, the result is a triangulated mesh.


```python
import Mesh
import MeshPart
import Import

data = Import.open("example.stp")
shape = data[0][0].Shape
shape_colors = data[0][1]

mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=0.1, Segments=True)

face_colors = [(0, 0, 0)] * mesh.CountFacets

for i in range(mesh.countSegments()):
    color = shape_colors[i]
    segm = mesh.getSegment(i)
    for j in segm:
        face_colors[j] = color

mesh.write(Filename="new_example.obj", Material=face_colors, Format="obj")
```

## More information {#more_information}

-   [Convert STEP to Wavefront OBJ with colors of faces](https://forum.freecadweb.org/viewtopic.php?f=8&t=37452)

## Tutorial

-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)
-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
