# Macro GenerateViews/pl
{{Macro
|Name=GenerateViews
|Description=Macro for automatic 2D views generation with 6 normal projections and one isometric.
|Author=PR-DC
|Download=[https://wiki.freecadweb.org/File:GenerateViews.svg ToolBar Icon]
|Date=2022-01-08
|Version=1.0.0
|FCVersion=0.18.4 and above
|SeeAlso=[https://github.com/PR-DC/PRDC_GenerateViews_FC Github repository]
}}

## Description

Macro for automatic 2D views generation with 6 normal projections and one isometric.

## Usage

Open the model and run the macro program (check input parameters inside macro for adjustments).

![](images/PRDC_GenerateViews_FC.png )

## Script

ToolBar Icon ![](images/GenerateViews.svg )

**GenerateViews.FCMacro**


{{MacroCode|code=
# Macro for automatic 2D views generation
# with 6 normal projections and one isometric
# Author: Milos Petrasinovic <mpetrasinovic@prdc.rs>
# PR-DC, Republic of Serbia
# info@pr-dc.com
# 
# 
#
# Copyright (C) 2022 PRDC <info@pr-dc.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  PARAMS 
dx = 10 # space between views along x axis
dy = 10 # space between views along y axis
# 

__Name__ = 'GenerateViews'
__Comment__ = 'Macro for automatic 2D views generation.'
__Author__ = 'Milos Petrasinovic <mpetrasinovic@pr-dc.com>'
__Version__ = '1.0.0'
__Date__ = '2022-01-07'
__License__ = 'GPL-3.0-or-later'
__Web__ = 'https://github.com/PR-DC/PRDC_GenerateViews_FC'
__Wiki__ = 'https://wiki.freecadweb.org/Macro_GenerateViews'
__Icon__ = 'GenerateViews.svg'
__Help__ = 'Open model and run the macro program!'
__Status__ = 'stable'
__Requires__ = 'Freecad >= 0.18'
__Communication__ = 'https://github.com/PR-DC/PRDC_GenerateViews_FC/issues/'
__Files__ = 'GenerateViews.svg'

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui
import Draft

doc = App.activeDocument()
doc_gui = Gui.activeDocument()
shapes = []

def GetShapes(objs, shapes):
    for obj in objs:
        if obj.TypeId == 'App::DocumentObjectGroup':
            GetShapes(obj.OutList, shapes)
        elif hasattr(obj, "Shape") and doc_gui.getObject(obj.Name).Visibility:
            shapes.append(obj)
    return shapes

def InitPosition(obj):
    doc.recompute()
    BB = obj.Shape.BoundBox
    Draft.move(obj, App.Vector(-BB.XMin, -BB.YMin, 0.0), copy=False)
    return [BB.XMax-BB.XMin, BB.YMax-BB.YMin]
    
if doc is not None:
    shapes = GetShapes(doc.RootObjects, shapes)
    if len(shapes):
        if len(shapes) == 1:
            model = shapes[0]
        else:
            model = doc.addObject("Part::Compound", "DrawingModel")
            model.Links = shapes
            doc.recompute()
        
        # Generate views
        Top = Draft.makeShape2DView(model, App.Vector(0, 0, 1))
        Top.Label = "TopView"
        TopBB = InitPosition(Top)
        Bottom = Draft.makeShape2DView(model, App.Vector(0, 0, -1))
        Bottom.Label = "BottomView"
        BottomBB = InitPosition(Bottom)
        Front = Draft.makeShape2DView(model, App.Vector(0, -1, 0))
        Front.Label = "FrontView"
        Draft.rotate(Front, -90, center=App.Vector(0, 0, 0), axis=App.Vector(0, 0, 1), copy=False)
        FrontBB = InitPosition(Front)
        Rear = Draft.makeShape2DView(model, App.Vector(0, 1, 0))
        Rear.Label = "RearView"
        Draft.rotate(Rear, -90, center=App.Vector(0, 0, 0), axis=App.Vector(0, 0, 1), copy=False)
        RearBB = InitPosition(Rear)
        Right = Draft.makeShape2DView(model, App.Vector(1, 0, 0))
        Right.Label = "RightView"
        Draft.rotate(Right, 180, center=App.Vector(0, 0, 0), axis=App.Vector(0, 0, 1), copy=False)
        RightBB = InitPosition(Right)
        Left = Draft.makeShape2DView(model, App.Vector(-1, 0, 0))
        Left.Label = "LeftView"
        Draft.rotate(Left, 180, center=App.Vector(0, 0, 0), axis=App.Vector(0, 0, 1), copy=False)
        LeftBB = InitPosition(Left)
        Isometric = Draft.makeShape2DView(model, App.Vector(0.57735, 0.57735, 0.57735))
        Isometric.Label = "IsometricView"
        IsometricBB = InitPosition(Isometric)
        doc.recompute()
        
        # Views position 
        RearPos = [RightBB[0]+2*dx, dy]
        Draft.move(Rear, App.Vector(RearPos[0], RearPos[1], 0.0), copy=False)
        RightPos = [dx, RearBB[1]+2*dy]
        Draft.move(Right, App.Vector(RightPos[0], RightPos[1], 0.0), copy=False)
        TopPos = [RearPos[0], RightPos[1]]
        Draft.move(Top, App.Vector(TopPos[0], TopPos[1], 0.0), copy=False)
        FrontPos = [RearPos[0], TopPos[1]+TopBB[1]+dy]
        Draft.move(Front, App.Vector(FrontPos[0], FrontPos[1], 0.0), copy=False)
        LeftPos = [TopPos[0]+TopBB[0]+dx, TopPos[1]]
        Draft.move(Left, App.Vector(LeftPos[0], LeftPos[1], 0.0), copy=False)
        BottomPos = [LeftPos[0]+LeftBB[0]+dx, TopPos[1]]
        Draft.move(Bottom, App.Vector(BottomPos[0], BottomPos[1], 0.0), copy=False)
        IsometricPos = [LeftPos[0], FrontPos[1]]
        Draft.move(Isometric, App.Vector(IsometricPos[0], IsometricPos[1], 0.0), copy=False)
        doc.recompute()
        
        if len(shapes) > 1:
            doc.removeObject(model.Name)
            for obj in shapes:
                doc_gui.getObject(obj.Name).Visibility = True
                
        # Add views to group
        ViewsGroup = doc.addObject('App::DocumentObjectGroup', 'ViewsGroup')
        ViewsGroup.addObjects([Top, Bottom, Front, Rear, Right, Left, Isometric])
        
        Gui.updateGui()
    else:
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Error")
        msgBox.setText("No shapes for drawing!")
        msgBox.exec_()
        App.Console.PrintError("\nError: No shapes for drawing!\n")
else:
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle("Error")
    msgBox.setText("No active document!")
    msgBox.exec_()
    App.Console.PrintError("\nError: No active document!\n")
}}

## Links

The forum discussion [New Macros: GenerateViews and GenerateDrawing](https://forum.freecadweb.org/viewtopic.php?f=22&t=65135)



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro GenerateViews/pl
