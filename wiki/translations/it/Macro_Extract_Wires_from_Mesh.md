# Macro Extract Wires from Mesh/it



{{Macro/it
|Name=Macro Extract Wires from Mesh
|Icon=Macro_Extract_Wires_from_Mesh.png
|Translate=Wire da Mesh
|Description=Estrae i bordi wire dai mesh selezionati
|Author=Yorik
|Version=1
|Date=2016-12-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/2/28/Macro_Extract_Wires_from_Mesh.png ToolBar Icon]
}}

## Descrizione

Trova i contorni di wire negli oggetti mesh selezionati. I contorni wire sono formati da tutti i bordi trovati nell\'oggetto mesh che sono condivisi da una sola faccia, cioè, che sono spigoli \"confine\". I wire trovati vengono aggiunti al documento (un composto per oggetto mesh), mentre la mesh stessa viene nascosta.

## Script

ToolBar Icon ![](images/Macro_Extract_Wires_from_Mesh.png )

**Macro\_Extract\_Wires\_from\_Mesh.FCMacro**


```python
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
```

