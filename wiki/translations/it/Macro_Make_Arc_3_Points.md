# Macro Make Arc 3 Points/it
{{Macro/it
|Name=Macro Make Arc 3 Points
|Icon=Macro_Make_Arc_3_Points.png
|Translate=Arco da 3 punti
|Description=Crea un arco da 3 punti selezionati.
|Author=Mario52
|Version=01.00
|Date=2016-07-14
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/9/92/Macro_Make_Arc_3_Points.png ToolBar Icon]
}}

## Descrizione

Questa macro crea un arco da 3 punti selezionati


<div class="mw-translate-fuzzy">

## Uso

Avviare la macro, poi selezionare 3 punti. Viene creato uno arco. Le coordinate e la lunghezza dell\'arco sono visualizzati nella vista rapporto.


</div>

Nota   *non è necessario tenere premuto il tasto Ctrl

## Script

L\'icona per la barra degli strumenti   * <img alt="" src=images/Macro_Make_Arc_3_Points.png  style="width   *36px;">

**Macro\_Make\_Arc\_3\_Points.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
from FreeCAD import Base

__title__   = "Macro_Make_Arc_3_points"
__author__  = "Mario52"
__url__     = "http   *//www.freecadweb.org/index-fr.html"
__version__ = "00.02"
__date__    = "29/07/2019"

global selected; selected = []
App = FreeCAD

class SelObserver   *
    print( "Create Arc to 3 points ...")
    def addSelection(self,doc,obj,sub,pnt)   *  # Selection 
        global selected
        selected.append(pnt)
        if len(selected) == 1   *
            print( "Point 1    * ",FreeCAD.Vector(selected[0]))
        elif len(selected) == 2   *
            print( "Point 2    * ",FreeCAD.Vector(selected[1]))
        elif len(selected) == 3   *
            print( "Point 3    * ",FreeCAD.Vector(selected[2]))
            try   *
                C1 = Part.Arc(FreeCAD.Vector(selected[0]),FreeCAD.Vector(selected[1]),FreeCAD.Vector(selected[2]))
                S1 = Part.Shape([C1])
                W = Part.Wire(S1.Edges)
                Part.show(W)
                App.ActiveDocument.ActiveObject.Label   = "Arc_3_Points"
                print( "Length     * ",W.Length)
            except Exception   *
                print( "Three points are collinear or bad selection")
            del selected[   *]
            FreeCADGui.Selection.removeObserver(s)
            print( "End Make_Arc_3_Points")
            print( "_____________________")

s=SelObserver()
FreeCADGui.Selection.addObserver(s)


}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Make Arc 3 Points/it
