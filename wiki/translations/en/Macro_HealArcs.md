# Macro HealArcs/en
{{Macro
|Name=HealArcs
|Icon=Macro_HealArcs.png
|Description=Sometimes arcs are transformed into BSplines, for example when scale operations have been applied to them. This macro recreates valid arcs from them. Useful before exporting to dxf. Useful before exporting to dxf.
|Author=Yorik
|Version=0.1
|Date=2011-09-24
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/5/5a/Macro_HealArcs.png ToolBar Icon]
}}

## Description

Sometimes arcs are transformed into BSplines, for example when scale operations have been applied to them. This macro recreates valid arcs from them. Useful before exporting to dxf

## Script

ToolBar Icon ![](images/Macro_HealArcs.png ) **Macro\_HealArcs.FCMacro**


{{MacroCode|code=

try   *
    import DraftGeomUtils as fcgeo
except   *
    from draftlibs import fcgeo
import FreeCAD,FreeCADGui,Part

sel = FreeCADGui.Selection.getSelection()
if not sel   *
    FreeCAD.Console.PrintWarning("Select something first!")
else   *
    removeList = []
    for obj in sel   *
        ed = obj.Shape.Edges[0]
        arc = fcgeo.arcFromSpline(ed)
        if arc   *
            Part.show(arc)
            removeList.append(obj.Name)
    FreeCAD.ActiveDocument.recompute()
    print("removing", removeList)
    for n in removeList   *
        FreeCAD.ActiveDocument.removeObject(n)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro HealArcs/en
