# Macro FlattenWire3Points

  {{Macro
|Name=FlattenWire3Points
|Icon=Macro_FlattenWire3Points.png
|Description=This macro flattens draft wires that are not planar on a plane defined by 3 points.<br/> To use this macro, select first 3 vertices from a single Draft Wire.
|Author=Yorik
|Version=1.0
|Date=2016-02-06
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/1e/Macro_FlattenWire3Points.png ToolBar Icon]
}}

## Description

This macro flattens draft wires that are not planar on a plane defined by 3 points. To use this macro, select first 3 vertices from a single [Draft Wire](Draft_Wire.md).

## Script

ToolBar icon ![](images/Macro_FlattenWire3Points.png ) 

**Macro\_FlattenWire3Points.FCMacro**


{{MacroCode|code=

 import FreeCAD,FreeCADGui,Draft
 
 # check selection
 sel = FreeCADGui.Selection.getSelectionEx()
 ok = True
 if len(sel) != 1:
    FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
    ok = False
 sel = sel[0]
 if Draft.getType(sel.Object) not in ["Wire","BSpline"]:
    FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
    ok = False
 if len(sel.SubElementNames) != 3:
    FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
    ok = False
 for e in sel.SubElementNames:
    if not "Vertex" in e:
        FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
        ok = False
 
 if ok:
    # define a plane
    p1 = getattr(sel.Object.Shape,sel.SubElementNames[0]).Point
    p2 = getattr(sel.Object.Shape,sel.SubElementNames[1]).Point
    p3 = getattr(sel.Object.Shape,sel.SubElementNames[2]).Point
    p4 = p2.sub(p1).cross(p3.sub(p1))# project wire points
    points = []
    for p in sel.Object.Points:
        points.append(p.projectToPlane(p1,p4))
    sel.Object.Points = points
}}

