# Macro Extract Wires from Mesh/pl
{{Macro
|Name=Macro Extract Wires from Mesh
|Icon=Macro_Extract_Wires_from_Mesh.png
|Description=Finds boundary wires in selected mesh objects. Boundary wires are formed from all the edges found in the mesh that are shared by only one face, that is, they are "border" edges. The found wires get added to the document (one compound per mesh object), while the mesh itself gets hidden.
|Author=Yorik
|Version=1
|Date=2016-12-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/28/Macro_Extract_Wires_from_Mesh.png ToolBar Icon]
}}

## Description

Finds boundary wires in selected mesh objects. Boundary wires are formed from all the edges found in the mesh that are shared by only one face, that is, they are \"border\" edges. The found wires get added to the document (one compound per mesh object), while the mesh itself gets hidden.

## Script

ToolBar Icon ![](images/Macro_Extract_Wires_from_Mesh.png )

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
