# Arch JSON/it
<div class="mw-translate-fuzzy">





</div>

Lo scopo principale di questo formato di esportazione è rendere più semplice l\'elaborazione dei dati del modello di FreeCAD dai linguaggi di programmazione. Il formato [JSON](http://json.org/) è il seguente:

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

Nota che le faccette formano triangoli e i loro valori di riferimento delle valori interi nella matrice **vertices**. Le normali delle sfaccettature si trovano nella posizione corrispondente nell\'array **normal**. **description**, **color** e **wires** sono tutti opzionali. Questo formato potrebbe essere facilmente esteso per includere ulteriori dati del modello.


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch JSON/it
