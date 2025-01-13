# Arch JSON/pl
## Opis

Głównym celem tego formatu eksportu jest ułatwienie przetwarzania danych modelu FreeCAD z języków programowania. Format [JSON](http://json.org/) jest następujący:

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

Należy zauważyć, że ścianki tworzą trójkąty, a ich wartości całkowite są punktami odniesienia w tablicy **wierzchołków**. Fasetowe wektory normalne znajdują się w odpowiednim miejscu w tablicy **normalne**. **Opis**, **kolor** i **linie łamane** są opcjonalne. Format ten może być łatwo rozszerzony o dodatkowe dane modelu.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Arch JSON/pl
