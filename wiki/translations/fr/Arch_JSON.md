# Arch JSON/fr





L\'objectif principal de ce format d\'exportation est de faciliter le traitement des données du modèle FreeCAD à partir de langages de programmation. Le format [JSON](http://json.org/) est le suivant:

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

Notez que les facettes forment des triangles et leurs valeurs entières référencent des points dans le tableau **vertices**. Les normales des facettes sont trouvées à la position correspondante dans le tableau **normals**, **description**, **color** et **wires** sont tous optionnels. Ce format pourrait facilement être étendu pour inclure des données de modèles supplémentaires.





 

[Category:File Formats](Category:File_Formats.md)
