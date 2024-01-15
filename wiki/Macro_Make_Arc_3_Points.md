# Macro Make Arc 3 Points
{{Macro
|Name=Macro Make Arc 3 Points
|Icon=Macro_Make_Arc_3_Points.png
|Description=Creates a arc from 3 selected points.
|Author=Mario52
|Version=02.00
|Date=2019-07-29
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/92/Macro_Make_Arc_3_Points.png ToolBar Icon]
}}

## Description

This macro creates a arc on 3 selected points.

## Usage

Launch the macro, select 3 points, the arc is created and the coordinates and the length of the arc are displayed in the report view.

(PS: It is not required to hold down the Ctrl key)

## Script

The icon for the toolBar <img alt="" src=images/Macro_Make_Arc_3_Points.png  style="width:36px;">

 **Macro_Make_Arc_3_Points.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from FreeCAD import Base

__title__   = "Macro_Make_Arc_3_points"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.02"
__date__    = "29/07/2019"

global selected; selected = []
App = FreeCAD

class SelObserver:
    print( "Create Arc to 3 points ...")
    def addSelection(self,doc,obj,sub,pnt):  # Selection 
        global selected
        selected.append(pnt)
        if len(selected) == 1:
            print( "Point 1 : ",FreeCAD.Vector(selected[0]))
        elif len(selected) == 2:
            print( "Point 2 : ",FreeCAD.Vector(selected[1]))
        elif len(selected) == 3:
            print( "Point 3 : ",FreeCAD.Vector(selected[2]))
            try:
                C1 = Part.Arc(FreeCAD.Vector(selected[0]),FreeCAD.Vector(selected[1]),FreeCAD.Vector(selected[2]))
                S1 = Part.Shape([C1])
                W = Part.Wire(S1.Edges)
                Part.show(W)
                App.ActiveDocument.ActiveObject.Label   = "Arc_3_Points"
                print( "Length  : ",W.Length)
            except Exception:
                print( "Three points are collinear or bad selection")
            del selected[:]
            FreeCADGui.Selection.removeObserver(s)
            print( "End Make_Arc_3_Points")
            print( "_____________________")

s=SelObserver()
FreeCADGui.Selection.addObserver(s)


}}



---
⏵ [documentation index](../README.md) > Macro Make Arc 3 Points
