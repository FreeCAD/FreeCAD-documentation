# Arch OBJ/de
## Beschreibung

Zusätzlich zu FreeCADs Standard-[OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file)-Exportfunktion hat derArbeitsbereich [BIM](BIM_Workbench/de.md) eine alternative Exportfunktion, die komplanare Flächen als eine einzige OBJ-Fläche exportiert, anstatt sie als [Form](Shape/de.md)-basierte Objekte zu triangulieren, wie es die Standard-Exportfunktion tut.



## Exportieren ohne GUI 

Exportieren ohne die grafische Benutzeroberfläche ist auf der Kommandozeile nur mit dem Exportwerkzeug des Arbeitsbereichs [Mesh](Mesh_Export/de.md) möglich.

In diesem Beispiel wird eine STEP-Datei importiert, die Farben der [Form](Shape/de.md) werden gespeichert, dann ein Netzobjekt daraus erstellt, die Farben des Originalobjekts auf die Flächen des neuen Netzobjekts angewendet, das dann im OBJ-Format exportiert wird. Weil dies mit dem Mesh-Arbeitsbereich passiert, ist das Ergebnis ein trianguliertes Netz.


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



## Weitere Informationen 

-   [Convert STEP to Wavefront OBJ with colors of faces](https://forum.freecadweb.org/viewtopic.php?f=8&t=37452) STEP zu OBJ umwandeln, mit den Farben von Flächen



## Anleitungen

-   [Import von STL oder OBJ](Import_from_STL_or_OBJ/de.md)
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Arch OBJ/de
