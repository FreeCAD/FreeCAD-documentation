# Arch JSON/de
## Beschreibung

Der Hauptzweck dieses Exportformat ist es, FreeCAD-Modelldaten mit anderen Programmiersprachen zu verarbeiten. Das [JSON](http://json.org/)-Format ist wie folgt:

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

Beachte, dass Facetten Dreiecke bilden und ihre Integer-Werte sich auf Punkte im **vertices**-Feld (vertices array) beziehen. Facetten-\'Normale\' (normals) finden sich an der entsprechenden Position im **normals**-Feld (normals array). **description**, **color** und **wires** sind alle optional. Dieses Format kann leicht erweitert werden, um zusätzliche Modelldaten zu enthalten.



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [BIM](Category_BIM.md) > Arch JSON/de
