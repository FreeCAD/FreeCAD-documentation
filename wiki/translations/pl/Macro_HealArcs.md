# Macro HealArcs/pl

 {{Macro
|Name=HealArcs
|Name/pl=HealArcs
|Icon=Macro_HealArcs.png
|Description=Czasami łuki są przekształcane w krzywą złożoną, na przykład gdy zastosowano do nich operacje skalowania. To makro odtwarza z nich prawidłowe łuki. Przydatne przed eksportem do formatu DXF. 
|Author=Yorik
|Version=0.1
|Date=2011-09-24
|FCVersion=Wszystkie|Download=[https://www.freecadweb.org/wiki/images/5/5a/Macro_HealArcs.png Ikonka paska narzędzi]
}}

## Opis

Czasami łuki są przekształcane w krzywą złożoną, na przykład gdy zastosowano do nich operacje skalowania. To makro odtwarza z nich prawidłowe łuki. Przydatne przed eksportem do formatu DXF.

## Tworzenie skryptów 

Ikonka paska narzędzi ![](images/Macro_HealArcs.png ) **Macro\_HealArcs.FCMacro**


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
    print "removing ",removeList
    for n in removeList:
        FreeCAD.ActiveDocument.removeObject(n)
}}




