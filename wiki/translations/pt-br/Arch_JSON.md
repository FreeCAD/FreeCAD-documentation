# Arch JSON/pt-br
<div class="mw-translate-fuzzy">





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





</div>


 

_

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Arch](Arch_Workbench.md) > Arch JSON/pt-br
