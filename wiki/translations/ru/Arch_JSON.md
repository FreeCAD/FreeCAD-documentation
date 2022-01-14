# Arch JSON/ru
<div class="mw-translate-fuzzy">


{{docnav/ru
|[OBJ](Arch_OBJ/ru.md)
|[3DS](Arch_3DS/ru.md)
|[Модуль Arch](Arch_Workbench/ru.md)
}}


</div>

The main purpose of this export format is to make it easier to process FreeCAD model data from programming languages. The [JSON](http://json.org/) format is as follows:

      {
        "version": "0.0.1",
        "description": "Mesh data exported from FreeCAD",
        "objects": [
          {
            "name": "<object name>",
            "description": "<object description>",
            "color": "<object color>",
            "wires": [[[<float>, <float>, <float>], . . .], . . .],
            "vertices": [[<float>, <float>, <float>], . . .],
            "normals": [[<float>, <float>, <float>], . . .],
            "facets": [[<int>, <int>, <int>], . . .]
          }, . . .
        ]
      }

Note that facets form triangles and their integer values reference points in the **vertices** array. Facet normals are found at the corresponding position in the **normals** array. **description**, **color** and **wires** are all optional. This format could easily be expanded to include additional model data.


<div class="mw-translate-fuzzy">


{{docnav/ru
|[OBJ](Arch_OBJ/ru.md)
|[3DS](Arch_3DS/ru.md)
|[Модуль Arch](Arch_Workbench/ru.md)
}}


</div>


 

[<img src="images/Property.png" style="width:16px"> File Formats](Category_File_Formats.md)

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Arch](Arch_Workbench.md) > Arch JSON/ru
