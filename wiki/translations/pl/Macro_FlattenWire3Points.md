# Macro FlattenWire3Points/pl
{{Macro
|Name=FlattenWire3Points
|Name/pl=FlattenWire3Points
|Icon=Macro_FlattenWire3Points.png
|Description=Ta makrodefinicja spłaszcza polilinie środowiska Rysunek Roboczy, które nie są płaskie na płaszczyźnie zdefiniowanej przez 3 punkty.<br/> Aby użyć tego makra, wybierz pierwsze 3 wierzchołki z pojedynczej polilinii Rysunek Roboczy.
|Author=Yorik
|Version=1.0
|Date=2016-02-06
|FCVersion=Wszystkie
|Download=[https   *//www.freecadweb.org/wiki/images/1/1e/Macro_FlattenWire3Points.png Ikonka paska narzędzi]
}}

## Opis

Ta makrodefinicja spłaszcza polilinie środowiska Rysunek Roboczy, które nie są płaskie na płaszczyźnie zdefiniowanej przez 3 punkty.
Aby użyć tego makra, wybierz pierwsze 3 wierzchołki z pojedynczej [polilinii](Draft_Wire/pl.md) Rysunek Roboczy.

## Tworzenie skryptów 

Ikonka paska narzędzi ![](images/Macro_FlattenWire3Points.png )

**Macro_FlattenWire3Points.FCMacro**


{{MacroCode|code=

 import FreeCAD,FreeCADGui,Draft
 
 # check selection
 sel = FreeCADGui.Selection.getSelectionEx()
 ok = True
 if len(sel) != 1   *
    FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
    ok = False
 sel = sel[0]
 if Draft.getType(sel.Object) not in ["Wire","BSpline"]   *
    FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
    ok = False
 if len(sel.SubElementNames) != 3   *
    FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
    ok = False
 for e in sel.SubElementNames   *
    if not "Vertex" in e   *
        FreeCAD.Console.PrintError("Please select 3 vertices from one Draft wire\n")
        ok = False
 
 if ok   *
    # define a plane
    p1 = getattr(sel.Object.Shape,sel.SubElementNames[0]).Point
    p2 = getattr(sel.Object.Shape,sel.SubElementNames[1]).Point
    p3 = getattr(sel.Object.Shape,sel.SubElementNames[2]).Point
    p4 = p2.sub(p1).cross(p3.sub(p1))# project wire points
    points = []
    for p in sel.Object.Points   *
        points.append(p.projectToPlane(p1,p4))
    sel.Object.Points = points
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FlattenWire3Points/pl
