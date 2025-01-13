# Macro Extract Wires from Mesh/pl
{{Macro/pl
|Name=Macro Extract Wires from Mesh
|Translate=Makrodefinicja: Wyodrębnij linie z siatki
|Icon=Macro_Extract_Wires_from_Mesh.png
|Description=Znajduje polilinie graniczne w wybranych obiektach siatki. Polilinie graniczne są tworzone ze wszystkich krawędzi znalezionych w siatce, które są współdzielone tylko przez jedną ścianę, czyli są to krawędzie "brzegowe". Znalezione polilinie są dodawane do dokumentu ''(jeden związek na obiekt siatki)'', podczas gdy sama siatka jest ukrywana.
|Author=Yorik
|Version=1
|Date=2016-12-17
|FCVersion=wszystkie
|Download=[https://www.freecadweb.org/wiki/images/2/28/Macro_Extract_Wires_from_Mesh.png Ikonka paska narzędzi]
}}



## Opis

Znajduje polilinie graniczne w wybranych obiektach siatki. Polilinie graniczne są tworzone ze wszystkich krawędzi znalezionych w siatce, które są współdzielone tylko przez jedną ścianę, czyli są to krawędzie \"brzegowe\". Znalezione polilinie są dodawane do dokumentu *(jeden związek na obiekt siatki)*, podczas gdy sama siatka jest ukrywana.



## Skrypt

Ikonka paska narzędzi ![](images/Macro_Extract_Wires_from_Mesh.png )

**Macro_Extract_Wires_from_Mesh.FCMacro**


{{MacroCode|code=
#!/usr/bin/python

# This macro will extract wires from selected meshes
# The result is a new Part Compound containing wires, one per original mesh object
# The selected meshes will be hidden but still selected after the operation.
# Warning, it takes a bit of time...

import FreeCAD,FreeCADGui,Part,Draft,DraftGeomUtils,Mesh
for obj in FreeCADGui.Selection.getSelection():
    if obj.isDerivedFrom("Mesh::Feature"):
        shape = Part.Shape()
        shape.makeShapeFromMesh(obj.Mesh.Topology,0.1)
        edges = []
        lut = {}
        for f in shape.Faces:
            for e in f.Edges:
                lut.setdefault(e.hashCode(),[]).append(e)
        for k,v in lut.items():
            if len(v) == 1:
                edges.extend(v)
        if edges:
            wires = DraftGeomUtils.findWires(edges)
            if wires:
                Part.show(Part.makeCompound(wires))
                obj.ViewObject.hide()
}}



---
⏵ [documentation index](../README.md) > Macro Extract Wires from Mesh/pl
