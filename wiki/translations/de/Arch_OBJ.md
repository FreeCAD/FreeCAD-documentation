


{{docnav/de
|[DAE](Arch_DAE/de.md)
|[JSON](Arch_JSON/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
}}

## Beschreibung

Zusätzlich zur Standard-FreeCAD [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file)-Exportfunktion hat das [Arch-Modul](Arch_Workbench/de.md) eine alternative Exportfunktion, die nebeneinander liegende Flächen als vollständige (whole) Flächen exportiert, anstatt als dreiecksbasierte [Formteil](Shape/de.md)-Objekte, wie es die Standard-Exportfunktion tut.

## Exportieren ohne GUI {#exportieren_ohne_gui}

Exportieren ohne die grafische Benutzeroberfläche ist auf der Kommandozeile nur mit dem [Mesh-Arbeitsbereich](Mesh_Export/de.md)-Exporter möglich.

In diesem Beispiel wird eine STEP-Datei importiert, die Farben der [Form](Shape/de.md) werden gespeichert, dann ein Polygonnetz daraus erstellt, die Farben des Originalobjekts auf die Flächen des neuen Netzes angewendet, das dann im OBJ-Format exportiert wird. Weil dies mit dem Mesh-Arbeitsbereich passiert, ist das Ergebnis ein trianguliertes Netz.


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

## Weitere Informationen {#weitere_informationen}

-   [Convert STEP to Wavefront OBJ with colors of faces](https://forum.freecadweb.org/viewtopic.php?f=8&t=37452)

## Übungen

-   [Import von STL oder OBJ](Import_from_STL_or_OBJ/de.md)
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)


{{docnav/de
|[DAE](Arch_DAE/de.md)
|[JSON](Arch_JSON/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
}}


 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
