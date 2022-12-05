# Macro Print SceneGraph
{{Macro
|Name=Macro_Print_SceneGraph
|Icon=Macro_Print_SceneGraph.png
|Description=This macro traverses the SceneGraph and prints all the nodes and their fields in the Report View window. It can be used just for information or you can add code to modify parts of the SceneGraph in some way or print more details for particular types of node.
|Author=Aleph0
|Version=00.03
|Date=2017-10-24
|FCVersion=0.16.6703
|Download=[https://www.freecadweb.org/wiki/images/0/0b/Macro_Print_SceneGraph.png ToolBar Icon]
}}

## Description

This macro traverses the SceneGraph and prints all the nodes and their fields in the Report View window. It can be used just for information or you can add code to modify parts of the SceneGraph in some way or print more details for particular types of node.

## Script

ToolBar Icon  ![](images/Macro_Print_SceneGraph.png )

**Macro_Print_SceneGraph.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
"""
***************************************************************************
*                                                                         *
*   This macro traverses the SceneGraph and prints all the nodes and      *
*   their fields in the Report View window. It can be used just for       *
*   information or you can add code to modify parts of the SceneGraph in  *
*   some way or print more details for particular types of node.          *
*                                                                         *
***************************************************************************
*   Copyright © 2017 Richard P. Parkins, M. A.                          *
*                                                                         *
*   This file is a supplement to the FreeCAD CAx development system.      *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU Lesser General Public License (LGPL)    *
*   as published by the Free Software Foundation; either version 2 of     *
*   the License, or (at your option) any later version.                   *
*   for detail see the LICENCE text file.                                 *
*                                                                         *
*   This software is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU Library General Public License for more details.                  *
*                                                                         *
*   You should have received a copy of the GNU Library General Public     *
*   License along with this macro; if not, write to the Free Software     *
*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
*   USA                                                                   *
***************************************************************************
"""
__title__   = "Print_SceneGraph"
__author__  = "Aleph0"
__version__ = "00.03"
__date__    = "24/10/2017"
__Comment__ = "SceneGraph explorer"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_Print_SceneGraph"
__Help__ = "see first few lines of macro text"
__Status__ = "stable"
__Requires__ = "freecad 0.16"

#OS: Ubuntu 14.04.5 LTS
#Word size of OS: 64-bit
#Word size of FreeCAD: 64-bit
#Version: 0.16.6703 (Git)
#Build type: None
#Branch: releases/FreeCAD-0-16
#Hash: 2ce5c8d2e3020d05005ed71f710e09e9aa561f40
#Python version: 2.7.6
#Qt version: 4.8.6
#Coin version: 4.0.0a
#OCC version: 6.8.0.oce-0.17

import FreeCAD
from pivy import coin
import PySide
from PySide import QtGui, QtCore

def printFields(node,indent):
    nm = node.getName().__str__()
    if nm != "":
        FreeCAD.Console.PrintLog(indent+"name: "+nm+"\n") 
    fl = node.getFieldData()
    for i in range(fl.getNumFields()):
        name = fl.getFieldName(i)
        if name.__str__() != "point":
            val = node.getField(fl.getFieldName(i)).get()
            FreeCAD.Console.PrintLog(indent+str(name)+" -> "+str(val)+"\n")

def printTree(node,indent):
    FreeCAD.Console.PrintLog(indent+node.__str__()+"\n")
    if node.getTypeId().getName().__str__() == "Coordinate3":
        points=node.point
        for i in range(points.getNum()):
            FreeCAD.Console.PrintLog(indent+" "+str(i)+": "+str(points[i].getValue())+"\n")
    if node.getTypeId().getName().__str__() == "Coordinate4":
        points=node.point
        for i in range(points.getNum()):
            FreeCAD.Console.PrintLog(indent+" "+str(i)+": "+str(points[i].getValue())+"\n")
    printFields(node,indent+" ")
    if node.getChildren().__str__() != "None":
        for i in range(node.getNumChildren()):
            printTree(node.getChild(i),indent+" ")

ad = FreeCADGui.ActiveDocument
if ad == None:
    FreeCAD.Console.PrintLog("No active document\n")
else:
    QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
    printTree(ad.ActiveView.getViewer().getSoEventManager().getSceneGraph(), "")
    QtGui.QApplication.restoreOverrideCursor()
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Print SceneGraph
