# Macro HealArcs/cs
{{Macro/cs
|Name=HealArcs
|Translate=HealArcs
|Icon=Macro_HealArcs.png
|Description=Oblouky jsou někdy transformovány do B-křivek, například když na ně jsou aplikovány změny měřítka. Toto makro z nich znovu vytvoří platný oblouk. Je to užitečné před exportem do dxf
|Author=Yorik
|Version=0.1
|Date=2011-09-24
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/5/5a/Macro_HealArcs.png ToolBar Icon]
}}

## Description

Oblouky jsou někdy transformovány do B-křivek, například když na ně jsou aplikovány změny měřítka. Toto makro z nich znovu vytvoří platný oblouk. Je to užitečné před exportem do dxf

## Skript

ToolBar Icon ![](images/Macro_HealArcs.png ) **Macro_HealArcs.FCMacro**


{{MacroCode|code=

try:
    import DraftGeomUtils as fcgeo
except:
    from draftlibs import fcgeo
import FreeCAD,FreeCADGui,Part

sel = FreeCADGui.Selection.getSelection()
if not sel:
    FreeCAD.Console.PrintWarning("Select something first!")
else:
    removeList = []
    for obj in sel:
        ed = obj.Shape.Edges[0]
        arc = fcgeo.arcFromSpline(ed)
        if arc:
            Part.show(arc)
            removeList.append(obj.Name)
    FreeCAD.ActiveDocument.recompute()
    print("removing", removeList)
    for n in removeList:
        FreeCAD.ActiveDocument.removeObject(n)
}}



---
⏵ [documentation index](../README.md) > Macro HealArcs/cs
