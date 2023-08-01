# Macro HealArcs/it
{{Macro/it
|Name=HealArcs
|Translate=Cura gli archi
|Icon=Macro_HealArcs.png
|Description=Talvolta gli archi vengono trasformati in BSpline, per esempio quando si applicano ad essi delle operazioni di scala. Questa macro ricrea gli archi dalle BSpline. È utile prima di esportare in dxf
|Author=Yorik
|Version=0.1
|Date=2011-09-24
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/5/5a/Macro_HealArcs.png ToolBar Icon]
}}

## Descrizione

Talvolta gli archi vengono trasformati in BSpline, per esempio quando si applicano ad essi delle operazioni di scala. Questa macro ricrea gli archi dalle BSpline. È utile prima di esportare in dxf

## Script

Icona barra strumenti ![](images/Macro_HealArcs.png ) **Macro_HealArcs.FCMacro**


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
![](images/Button_right.svg) [documentation index](../README.md) > Macro HealArcs/it
