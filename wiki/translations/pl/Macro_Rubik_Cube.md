# Macro Rubik Cube/pl
{{Macro
|Name=Macro Rubik Cube
|Icon=Macro_Rubik_Cube.png
|Description=Macro to Display a Rubik Cube and interactively do slice rotations.
|Author=Aleph0
|SeeAlso=[Macro Megaminx](Macro_Megaminx.md)
|Version=00.05
|Date=2018-12-15
|FCVersion= <= 0.17
|Download=[https://www.freecadweb.org/wiki/images/7/7c/Macro_Rubik_Cube.png ToolBar Icon]
}}

## Description

Macro to Display a Rubik Cube and interactively do slice rotations.

![](images/Macro_Rubik_Cube.png ) 

## Script

ToolBar Icon <img alt="" src=images/Macro_Rubik_Cube.png  style="width:64px;">

**Macro\_Rubik\_Cube.FCMacro**

    # -*- coding: utf-8 -*-
    """
    ***************************************************************************
    *                                                                         *
    *   This macro creates a virtual Rubik Cube and enable you to manipulate  *
    *   it.                                                                   *
    *   You can chooose the size (number of small cubes along an edge).       *
    *   It then makes the cube: large sizes can take a while.                 *
    *   It then displays several views of the cube.                           *
    *   The central and largest view is an axonometric projection.            *
    *   This has arrows around it which you can click on to rotate slices.    *
    *   There are some text direction labels near the arrows: clicking on one *
    *   of those rotates the whole cube. You have to click on the actual      *
    *   letter: FreeCAD doesn't see clicks on the text background             *
    *   Another view is an axonometric projection from the other side.        *
    *   Another view combines views towards each face so as to                *
    *   look like a net of the cube's surface unfolded.                       *
    *   
    *   The macro maintains a history of the slice rotations you have done.   *
    *   It puts three buttons at the top of the window.                       *
    *   One undoes the last slice rotation and removes it from the history.   *
    *   One saves the history to the clipboard as a sequence of function      *
    *   calls which can be pasted into a macro which can then be called       *
    *   to replay the same set of rotations. Thus you can save an "operator"  *
    *   (a sequence of slice rotation which does something useful).           *
    *   The third button resets the cube to its initial state                 *
    *   and clears the history.                                               *
    *                                                                         *
    *   There are also some functions defined which can be called from the    *
    *   python console window:                                                *
    *   fix_reload() modifies a restored FreeCAD save file to add the extra   *
    *   views and interactive controls that this macro and its functions use; *
    *   ramdomise() randomises the cube;                                      *
    *   reverse_history(), reflectX_history(), reflectY_history(),            *
    *   reflectZ_history(), rotpX_history(), rotmX_history(),                 *
    *   rotpY_history(), rotmY_history(), rotpZ_history(), and                *
    *   rotmZ_history() each replace the history by a version modified in the *
    *   manner indicated - these are useful for creating modified operators.  *
    *   step_history() replays the history, popping a dialog box before each  *
    *   rotation - this is useful if you have developed an operator using the *
    *   model and you want to do the same rotations on a real cube.           *
    *                                                                         *
    ***************************************************************************
    *   Copyright © 2018 Richard P. Parkins, M. A.                            *
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
    *                                                                         *
    ***************************************************************************
    """
    __title__   = "Rubik_cube"
    __author__  = "Aleph0"
    __version__ = "00.05"
    __date__    = "15/12/2018"
    __Comment__ = "Virtual Rubik Cube"
    __Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_Rubik_Cube"
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

    # This parameter determines the speed at which slice rotations are animated
    # If you have a faster computer you can increase the value
    # This will make the animation smoother
    # If you have a slow computer you can decrease the value
    # This will make the animation faster but more jerky for large cubes
    slowness = 500

    import FreeCAD
    import Part
    import Draft
    import time
    import random
    from FreeCAD import Base
    from FreeCAD import Console
    from pivy import coin
    from pivy.coin import *
    from PySide import *

    # This horrible hack is needed because some versions of FreeCAD seem to have
    # been built with a mixture of Qt4 and Qt5. In those versions, the Qt5 version
    # of setOverrideCursor() doesn't work, but the Qt4 version of MainWindow
    # doesn't seem to have a centralWidget(), which we need.
    try:
        import PyQt4.QtGui
        def busyCursor():
            PyQt4.QtGui.QApplication.setOverrideCursor(
                PyQt4.QtGui.QCursor(PyQt4.QtCore.Qt.WaitCursor))
        def restoreCursor():
            PyQt4.QtGui.QApplication.restoreOverrideCursor()
    except Exception:
        def busyCursor():
            QtGui.QApplication.setOverrideCursor(
                QtGui.QCursor(QtCore.Qt.WaitCursor))
        def restoreCursor():
            QtGui.QApplication.restoreOverrideCursor()

    # If this is the first time this macro has been run in this invocation of
    # FreeCAD, create our dictionary of document-specific data structures
    if not hasattr(FreeCAD, "Rubik_Cube_executed"):
        FreeCAD.Rubik_Cube_executed = 1
        Dictionary = {}

    # Create a new document and make it current
    App.ActiveDocument = App.newDocument("Rubik_Cube")
    Gui.ActiveDocument = Gui.getDocument(str(App.ActiveDocument.Name))

    # for debugging
    def showMessage(s):
        diag = QtGui.QMessageBox(QtGui.QMessageBox.NoIcon, '', s)
        diag.setWindowModality(QtCore.Qt.NonModal)
        diag.exec_()

    # This bit of code pops up the dialog to ask for the size and whether to orient
    # inner faces (useful if you are simulating a cube which has non-symmetrical
    # patterns instead of plain colours).
    defaultSize = 3
    class AskSizeWindow(QtGui.QDialog):
        # automagically called when a class instance is created
        def __init__(self):
            super(AskSizeWindow, self).__init__()
            self.initUI()
        # Lay out the interactive elements
        def initUI(self):
            self.setWindowTitle("Rubik Cube Size")
            geom = Gui.getMainWindow().geometry()
            width = 300
            height = 200
            margin = 10
            xpos = geom.center().x() - width / 2
            ypos = geom.center().y() - height / 2
            self.setGeometry(xpos, ypos, width, height)
            ypos = margin
            self.label_1 = QtGui.QLabel(self)
            self.label_1.setGeometry(QtCore.QRect(width/2 - 100, ypos, 200, 25)) 
            self.label_1.setObjectName("label_1")
            self.label_1.setText("Number of small cubes")
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)
            ypos = ypos + 25
            self.label_2 = QtGui.QLabel(self)
            self.label_2.setGeometry(QtCore.QRect(width/2 - 100, ypos, 200, 25)) 
            self.label_2.setObjectName("label_1")
            self.label_2.setText("along an edge")
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            ypos = ypos + 25
            self.spinBox = QtGui.QSpinBox(self)
            self.spinBox.setGeometry(QtCore.QRect(width/2 - 50, ypos, 100, 30))
            self.spinBox.setMinimum(2)
            self.spinBox.setMaximum(100)
            Dictionary[str(App.ActiveDocument.Name)+"Size"] = defaultSize
            self.spinBox.setValue(defaultSize)
            self.spinBox.setSingleStep(1)
            self.spinBox.setObjectName("spinBox")
            self.spinBox.valueChanged.connect(self.on_spinBox_valueChanged)
            ypos = ypos + 40
            self.checkBox = QtGui.QCheckBox("Oriented inner faces", self)
            self.checkBox.setGeometry(QtCore.QRect(width/2 - 100, ypos, 200, 30))
            Dictionary[str(App.ActiveDocument.Name)+"Oriented"] = QtCore.Qt.Unchecked
            self.checkBox.setCheckState(QtCore.Qt.Unchecked)
            self.checkBox.setObjectName("checkBox")
            self.checkBox.stateChanged.connect(self.on_checkBox_stateChanged)
            ypos = ypos + 40
            self.OKbutton = QtGui.QPushButton(self)
            self.OKbutton.setGeometry(QtCore.QRect(width/2 - 40, ypos, 80, 40))
            self.OKbutton.setText("OK")
            self.OKbutton.clicked.connect(self.onOK)
        def on_spinBox_valueChanged(self, val):
            Dictionary[str(App.ActiveDocument.Name)+"Size"] = val
        def on_checkBox_stateChanged(self, val):
            Dictionary[str(App.ActiveDocument.Name)+"Oriented"] = val
        def onOK(self):
            self.close()
            self.destroy()
    # now create the class instance which shows the dialog
    AskSizeWindow().exec_()

    # Display a wait cursor while we are making the cube
    busyCursor()

    # Dialog box shown on each step by step_history()
    class StepWindow(QtGui.QDialog):
        # automagically called when a class instance is created
        def __init__(self):
            super(StepWindow, self).__init__()
            # Lay out the interactive elements
            mw = Gui.getMainWindow()
            cw = mw.centralWidget()
            ww = 220
            wh = 100
            margin = 10
            self.setWindowTitle("Next Step")
            geom1 = mw.geometry()
            geom2 = cw.geometry()
            xpos = geom1.left() + geom2.center().x() - ww / 2
            buttons = Dictionary[str(App.ActiveDocument.Name)+"buttons"]
            buttonsheight = buttons.geometry().height()
            # The 25 is a bit magic to get the Dialog box just below the buttons
            ypos = geom1.top() + geom2.top() + buttonsheight + 25
            self.setGeometry(xpos, ypos, ww, wh)
            ypos = margin
            self.label_1 = QtGui.QLabel(self)
            self.label_1.setGeometry(QtCore.QRect(ww/2 - 100, ypos, 200, 25)) 
            self.label_1.setObjectName("label_1")
            ypos = ypos + 40
            self.OKbutton = QtGui.QPushButton(self)
            self.OKbutton.setGeometry(QtCore.QRect(margin, ypos, 80, 40))
            self.OKbutton.setText("OK")
            self.OKbutton.clicked.connect(self.onOK)
            self.Quitbutton = QtGui.QPushButton(self)
            xpos = ww - 80 - margin
            self.Quitbutton.setGeometry(QtCore.QRect(xpos, ypos, 80, 40))
            self.Quitbutton.setText("Stop")
            self.Quitbutton.clicked.connect(self.onQuit)
        def onOK(self):
            self.close()
            self.destroy()
        def onQuit(self):
            Dictionary[str(App.ActiveDocument.Name)+"Stepping"] = 0
            self.close()
            self.destroy()

    # This bit of code catches clicks on the rotation arrows
    class ViewObserver:
        def __init__(self):
            self.view = FreeCADGui.ActiveDocument.ActiveView
            self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(),self.getpoint)  
        def getpoint(self,event_cb):
            event = event_cb.getEvent()
            if event.getButton() == 1:
                pos = event.getPosition().getValue()
                obInfo = self.view.getObjectInfo((int(pos[0]),int(pos[1])))
                if obInfo != None:
                    obj = App.ActiveDocument.getObject(obInfo["Object"])
                    obname = obj.Label
                    if obname[:5] == "arrow":
                        if event.getState() == 1:
                            wh = obname[5:7]
                            i = int(obname[7:])
                            if wh == "mX":
                                mrotmX(i,i+1)
                            elif wh == "pX":
                                mrotpX(i,i+1)
                            elif wh == "mY":
                                mrotmY(i,i+1)
                            elif wh == "pY":
                                mrotpY(i,i+1)
                            elif wh == "mZ":
                                mrotmZ(i,i+1)
                            elif wh == "pZ":
                                mrotpZ(i,i+1)
                        event_cb.setHandled()
                    elif obname[:5] == "label":
                        if event.getState() == 1:
                            wh = obname[5:7]
                            n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
                            if wh == "mX":
                                mrotmX(0,n)
                            elif wh == "pX":
                                mrotpX(0,n)
                            elif wh == "mY":
                                mrotmY(0,n)
                            elif wh == "pY":
                                mrotpY(0,n)
                            elif wh == "mZ":
                                mrotmZ(0,n)
                            elif wh == "pZ":
                                mrotpZ(0,n)
                        event_cb.setHandled()

    # Create a ViewObserver and save it in the dictionary so that it does not get
    # garbage-collected
    Dictionary[str(App.ActiveDocument.Name)+"ViewObserver"] = ViewObserver()

    # This bit of code creates the basic cube model
    # It is composed of faces rather than cubes because I haven't found a way of
    # making a cube with different coloured faces
    # Each face has a name and a label
    # The name is persistent regardless of how the face moves about the cube
    # The label changes and tells where the face is now: this is needed for
    # fix_reload()
    # I don't make the interior cubies because you can never see them
    fcd = App.ActiveDocument
    n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
    # Make array of 6 faces for each of n x n x n cubies
    fc = [[[[None for j in range(6)] for ix in range(n)]
            for iy in range(n)] for ix in range(n)]
    Dictionary[str(App.ActiveDocument.Name)+"cubies"] = fc
    oriented = Dictionary[str(App.ActiveDocument.Name)+"Oriented"]
    for ix in range(n):
        fx = ix - (n - 1) / 2.0
        for iy in range(n):
            fy = iy - (n - 1) / 2.0
            for iz in range(n):
                if ix != 0 and ix != n-1 and (
                  iy != 0 and iy != n-1 and
                  iz != 0 and iz != n-1):
                    continue
                fz = iz - (n - 1) / 2.0
                fs = str(ix)+"q"+str(iy)+"q"+str(iz)
                x0y0z0 = Base.Vector(fx-0.5,fy-0.5,fz-0.5)
                x0y0z1 = Base.Vector(fx-0.5,fy-0.5,fz+0.5)
                x0y1z0 = Base.Vector(fx-0.5,fy+0.5,fz-0.5)
                x0y1z1 = Base.Vector(fx-0.5,fy+0.5,fz+0.5)
                x1y0z0 = Base.Vector(fx+0.5,fy-0.5,fz-0.5)
                x1y0z1 = Base.Vector(fx+0.5,fy-0.5,fz+0.5)
                x1y1z0 = Base.Vector(fx+0.5,fy+0.5,fz-0.5)
                x1y1z1 = Base.Vector(fx+0.5,fy+0.5,fz+0.5)
                if oriented != QtCore.Qt.Unchecked and (
                  ix == 0 and iy != 0 and iy != n-1 and iz != 0 and iz != n-1):
                    x0y2z1 = Base.Vector(fx-0.5,fy,fz)
                    face = Part.Face(Part.makePolygon(
                        [x0y0z0,x0y0z1,x0y2z1,x0y1z1,x0y1z0,x0y0z0]))
                else:
                    face = Part.Face(Part.makePolygon(
                        [x0y0z0,x0y0z1,x0y1z1,x0y1z0,x0y0z0]))
                f1 = fcd.addObject("Part::Feature", "ff"+fs+"x0")
                f1.Shape = face
                f1.Label = "fs"+fs+"x0"
                if ix == 0:
                    f1.ViewObject.DiffuseColor=[(1.0,1.0,1.0)]
                else:
                    f1.ViewObject.DiffuseColor=[(0.0,0.0,0.0)]
                f1.ViewObject.RootNode.setName(coin.SbName("ff"+fs+"x0"))
                if oriented != QtCore.Qt.Unchecked and (
                  ix == n - 1 and iy != 0 and iy != n-1 and iz != 0 and iz != n-1):
                    x1y2z1 = Base.Vector(fx+0.5,fy,fz)
                    face = Part.Face(Part.makePolygon(
                        [x1y0z0,x1y0z1,x1y2z1,x1y1z1,x1y1z0,x1y0z0]))
                else:
                    face = Part.Face(Part.makePolygon(
                        [x1y0z0,x1y0z1,x1y1z1,x1y1z0,x1y0z0]))
                f2 = fcd.addObject("Part::Feature", "ff"+fs+"x1")
                f2.Shape = face
                f2.Label = "fs"+fs+"x1"
                if ix == n - 1:
                    f2.ViewObject.DiffuseColor=[(1.0,0.0,0.0)]
                else:
                    f2.ViewObject.DiffuseColor=[(0.0,0.0,0.0)]
                f2.ViewObject.RootNode.setName(coin.SbName("ff"+fs+"x1"))
                if oriented != QtCore.Qt.Unchecked and (
                  ix != 0 and ix != n-1 and iy == 0 and iz != 0 and iz != n-1):
                    x1y0z2 = Base.Vector(fx,fy-0.5,fz)
                    face = Part.Face(Part.makePolygon(
                        [x0y0z0,x0y0z1,x1y0z1,x1y0z2,x1y0z0,x0y0z0]))
                else:
                    face = Part.Face(Part.makePolygon(
                        [x0y0z0,x0y0z1,x1y0z1,x1y0z0,x0y0z0]))
                f3 = fcd.addObject("Part::Feature", "ff"+fs+"y0")
                f3.Shape = face
                f3.Label = "fs"+fs+"y0"
                if iy == 0:
                    f3.ViewObject.DiffuseColor=[(0.0,1.0,0.0)]
                else:
                    f3.ViewObject.DiffuseColor=[(0.0,0.0,0.0)]
                f3.ViewObject.RootNode.setName(coin.SbName("ff"+fs+"y0"))
                if oriented != QtCore.Qt.Unchecked and (
                  ix != 0 and ix != n-1 and iy == n - 1 and iz != 0 and iz != n-1):
                    x1y1z2 = Base.Vector(fx,fy+0.5,fz)
                    face = Part.Face(Part.makePolygon(
                        [x0y1z0,x0y1z1,x1y1z1,x1y1z2,x1y1z0,x0y1z0]))
                else:
                    face = Part.Face(Part.makePolygon(
                        [x0y1z0,x0y1z1,x1y1z1,x1y1z0,x0y1z0]))
                f4 = fcd.addObject("Part::Feature", "ff"+fs+"y1")
                f4.Shape = face
                f4.Label = "fs"+fs+"y1"
                if iy == n - 1:
                    f4.ViewObject.DiffuseColor=[(1.0,0.0,1.0)]
                else:
                    f4.ViewObject.DiffuseColor=[(0.0,0.0,0.0)]
                f4.ViewObject.RootNode.setName(coin.SbName("ff"+fs+"y1"))
                if oriented != QtCore.Qt.Unchecked and (
                  ix != 0 and ix != n-1 and iy != 0 and iy != n-1 and iz == 0):
                    x2y0z0 = Base.Vector(fx,fy,fz-0.5)
                    face = Part.Face(Part.makePolygon(
                        [x0y0z0,x0y1z0,x1y1z0,x1y0z0,x2y0z0,x0y0z0]))
                else:
                    face = Part.Face(Part.makePolygon(
                        [x0y0z0,x0y1z0,x1y1z0,x1y0z0,x0y0z0]))
                f5 = fcd.addObject("Part::Feature", "ff"+fs+"z0")
                f5.Shape = face
                f5.Label = "fs"+fs+"z0"
                if iz == 0:
                    f5.ViewObject.DiffuseColor=[(1.0,1.0,0.0)]
                else:
                    f5.ViewObject.DiffuseColor=[(0.0,0.0,0.0)]
                f5.ViewObject.RootNode.setName(coin.SbName("ff"+fs+"z0"))
                if oriented != QtCore.Qt.Unchecked and (
                  ix != 0 and ix != n-1 and iy != 0 and iy != n-1 and iz == n - 1):
                    x2y0z1 = Base.Vector(fx,fy,fz+0.5)
                    face = Part.Face(Part.makePolygon(
                        [x0y0z1,x0y1z1,x1y1z1,x1y0z1,x2y0z1,x0y0z1]))
                else:
                    face = Part.Face(Part.makePolygon(
                        [x0y0z1,x0y1z1,x1y1z1,x1y0z1,x0y0z1]))
                f6 = fcd.addObject("Part::Feature", "ff"+fs+"z1")
                f6.Shape = face
                f6.Label = "fs"+fs+"z1"
                if iz == n - 1:
                    f6.ViewObject.DiffuseColor=[(0.0,0.0,1.0)]
                else:
                    f6.ViewObject.DiffuseColor=[(0.0,0.0,0.0)]
                f6.ViewObject.RootNode.setName(coin.SbName("ff"+fs+"z1"))
                fc[ix][iy][iz]=[f1,f2,f3,f4,f5,f6]

    # This bit of code creates the clickable arrows
    # Note we make them not selectable because mouse clicking on them
    # does a slice rotation instead of selecting the arrow.
    for i in range(n):
        fx = i - (n - 1) / 2.0
        fy = -(n / 2.0)
        fz = -(0.2 + n / 2.0)
        fs = "arrowpX"+str(i)
        v0 = Base.Vector(fx-0.1,fy,fz)
        v1 = Base.Vector(fx-0.1,fy,fz-0.5)
        v2 = Base.Vector(fx-0.2,fy,fz-0.5)
        v3 = Base.Vector(fx,fy,fz-0.7)
        v4 = Base.Vector(fx+0.2,fy,fz-0.5)
        v5 = Base.Vector(fx+0.1,fy,fz-0.5)
        v6 = Base.Vector(fx+0.1,fy,fz)
        arrow = fcd.addObject("Part::Feature", fs)
        arrow.Shape = Part.Face(Part.makePolygon([v0,v1,v2,v3,v4,v5,v6,v0]))
        arrow.ViewObject.DiffuseColor = [(0.0,0.0,0.0)]
        arrow.ViewObject.RootNode.setName(coin.SbName(fs))
        arrow.ViewObject.Selectable = False
        fy = 0.2 + n / 2.0
        fz = n / 2.0
        fs = "arrowmX"+str(i)
        v0 = Base.Vector(fx-0.1,fy,fz)
        v1 = Base.Vector(fx-0.1,fy+0.5,fz)
        v2 = Base.Vector(fx-0.2,fy+0.5,fz)
        v3 = Base.Vector(fx,fy+0.7,fz)
        v4 = Base.Vector(fx+0.2,fy+0.5,fz)
        v5 = Base.Vector(fx+0.1,fy+0.5,fz)
        v6 = Base.Vector(fx+0.1,fy,fz)
        arrow = fcd.addObject("Part::Feature", fs)
        arrow.Shape = Part.Face(Part.makePolygon([v0,v1,v2,v3,v4,v5,v6,v0]))
        arrow.ViewObject.DiffuseColor = [(0.0,0.0,0.0)]
        arrow.ViewObject.RootNode.setName(coin.SbName(fs))
        arrow.ViewObject.Selectable = False
        fx = n / 2.0
        fy = i - (n - 1) / 2.0
        fz = -(0.2 + n / 2.0)
        fs = "arrowpY"+str(i)
        v0 = Base.Vector(fx,fy-0.1,fz)
        v1 = Base.Vector(fx,fy-0.1,fz-0.5)
        v2 = Base.Vector(fx,fy-0.2,fz-0.5)
        v3 = Base.Vector(fx,fy,fz-0.7)
        v4 = Base.Vector(fx,fy+0.2,fz-0.5)
        v5 = Base.Vector(fx,fy+0.1,fz-0.5)
        v6 = Base.Vector(fx,fy+0.1,fz)
        arrow = fcd.addObject("Part::Feature", fs)
        arrow.Shape = Part.Face(Part.makePolygon([v0,v1,v2,v3,v4,v5,v6,v0]))
        arrow.ViewObject.DiffuseColor = [(0.0,0.0,0.0)]
        arrow.ViewObject.RootNode.setName(coin.SbName(fs))
        arrow.ViewObject.Selectable = False
        fx = -(0.2 + n / 2.0)
        fy = i - (n - 1) / 2.0
        fz = n / 2.0
        fs = "arrowmY"+str(i)
        v0 = Base.Vector(fx,fy-0.1,fz)
        v1 = Base.Vector(fx-0.5,fy-0.1,fz)
        v2 = Base.Vector(fx-0.5,fy-0.2,fz)
        v3 = Base.Vector(fx-0.7,fy,fz)
        v4 = Base.Vector(fx-0.5,fy+0.2,fz)
        v5 = Base.Vector(fx-0.5,fy+0.1,fz)
        v6 = Base.Vector(fx,fy+0.1,fz)
        arrow = fcd.addObject("Part::Feature", fs)
        arrow.Shape = Part.Face(Part.makePolygon([v0,v1,v2,v3,v4,v5,v6,v0]))
        arrow.ViewObject.DiffuseColor = [(0.0,0.0,0.0)]
        arrow.ViewObject.RootNode.setName(coin.SbName(fs))
        arrow.ViewObject.Selectable = False
        fx = n / 2.0
        fy = 0.2 + n / 2.0
        fz = i - (n - 1) / 2.0
        fs = "arrowpZ"+str(i)
        v0 = Base.Vector(fx,fy,fz-0.1)
        v1 = Base.Vector(fx,fy+0.5,fz-0.1)
        v2 = Base.Vector(fx,fy+0.5,fz-0.2)
        v3 = Base.Vector(fx,fy+0.7,fz)
        v4 = Base.Vector(fx,fy+0.5,fz+0.2)
        v5 = Base.Vector(fx,fy+0.5,fz+0.1)
        v6 = Base.Vector(fx,fy,fz+0.1)
        arrow = fcd.addObject("Part::Feature", fs)
        arrow.Shape = Part.Face(Part.makePolygon([v0,v1,v2,v3,v4,v5,v6,v0]))
        arrow.ViewObject.DiffuseColor = [(0.0,0.0,0.0)]
        arrow.ViewObject.RootNode.setName(coin.SbName(fs))
        arrow.ViewObject.Selectable = False
        fx = -(0.2 + n / 2.0)
        fy = -(n / 2.0)
        fz = i - (n - 1) / 2.0
        fs = "arrowmZ"+str(i)
        v0 = Base.Vector(fx,fy,fz-0.1)
        v1 = Base.Vector(fx-0.5,fy,fz-0.1)
        v2 = Base.Vector(fx-0.5,fy,fz-0.2)
        v3 = Base.Vector(fx-0.7,fy,fz)
        v4 = Base.Vector(fx-0.5,fy,fz+0.2)
        v5 = Base.Vector(fx-0.5,fy,fz+0.1)
        v6 = Base.Vector(fx,fy,fz+0.1)
        arrow = fcd.addObject("Part::Feature", fs)
        arrow.Shape = Part.Face(Part.makePolygon([v0,v1,v2,v3,v4,v5,v6,v0]))
        arrow.ViewObject.DiffuseColor = [(0.0,0.0,0.0)]
        arrow.ViewObject.RootNode.setName(coin.SbName(fs))
        arrow.ViewObject.Selectable = False

    # Utility routine for doLabels() to make a single label
    def makeLabel(text, mat):
        n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
        tx = Draft.makeText(text)
        tx.Label = "label"+text
        tx.ViewObject.TextColor = (0.0,0.0,0.0)
        tx.ViewObject.FontSize = 0.2 * n
        tx.ViewObject.Justification = 'Center'
        node = tx.ViewObject.RootNode
        node.setName(coin.SbName("label"+text))
        if node.getNumChildren() > 0:
            child = node.getChild(0)
            if child.getTypeId().getName().__str__() == "Transform":
                child.setMatrix(mat)

    # This bit of code creates some labels for the arrows
    # Clicking on one rotates the whole cube
    def doLabels():
        n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
        m = coin.SbMatrix()
        m.makeIdentity()
        m.setTransform(
            coin.SbVec3f(0.0, - n / 2.0, -(1.0 + n * 0.7)),
            coin.SbRotation(coin.SbVec3f(1.0, 0.0, 0.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        makeLabel("pX", m)
        m = coin.SbMatrix()
        m.makeIdentity()
        m.setTransform(
            coin.SbVec3f(0.0, 1.1 + n / 2.0, n / 2.0),
            coin.SbRotation(coin.SbVec3f(0.0, 1.0, 0.0), 0.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        makeLabel("mX", m)
        m = coin.SbMatrix()
        m.makeIdentity()
        m.setTransform(
            coin.SbVec3f(n / 2.0, 0.0, -(1.0 + n * 0.7)),
            coin.SbRotation(coin.SbVec3f(0.0, 0.0, 1.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        m1 = coin.SbMatrix()
        m1.makeIdentity()
        m1.setTransform(
            coin.SbVec3f(0.0, 0.0, 0.0),
            coin.SbRotation(coin.SbVec3f(1.0, 0.0, 0.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        m1.multRight(m)
        makeLabel("pY", m1)
        m = coin.SbMatrix()
        m.makeIdentity()
        m.setTransform(
            coin.SbVec3f(-1.1 - n / 2.0, 0.0, n / 2.0),
            coin.SbRotation(coin.SbVec3f(0.0, 0.0, 1.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        makeLabel("mY", m)
        m = coin.SbMatrix()
        m.makeIdentity()
        m.setTransform(
            coin.SbVec3f(n / 2.0, 0.7 + n * 0.6, 0.0),
            coin.SbRotation(coin.SbVec3f(0.0, 1.0, 0.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        makeLabel("pZ", m)
        m = coin.SbMatrix()
        m.makeIdentity()
        m.setTransform(
            coin.SbVec3f(-1.1 - n / 2.0, - n / 2.0, 0.0),
            coin.SbRotation(coin.SbVec3f(1.0, 0.0, 0.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        m1 = coin.SbMatrix()
        m1.makeIdentity()
        m1.setTransform(
            coin.SbVec3f(0.0, 0.0, 0.0),
            coin.SbRotation(coin.SbVec3f(0.0, 0.0, 1.0), 3.14159 / 2.0),
            coin.SbVec3f(1.0, 1.0, 1.0))
        m1.multRight(m)
        makeLabel("mZ", m1)

    # now call it to make them
    doLabels()

    Gui.ActiveDocument.ActiveView.viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")

    # Viewfit doesn't seem to do the right thing with MultiViews
    # so we adjust the camera height manually before creating them
    def fixCamera(lift):
        # This gets FreeCAD's top level SceneGraph (including camera node),
        # not the document's SceneGraph which hangs off of it
        v = Gui.ActiveDocument.ActiveView.getViewer()
        sceneGraph = v.getSoEventManager().getSceneGraph()
        camera = sceneGraph.getChild(2)
        if camera.getTypeId().getName().__str__() == "OrthographicCamera":
            if lift:
                camera.height.setValue((2.0 + n / 20.0) * camera.height.getValue())
            return camera.orientation.getValue()
    rotation = fixCamera(True)

    # This bit of code finds the widget corresponding to the View3DInventor
    def findView(widget):
        if widget.metaObject().className().__str__() == "Gui::View3DInventor":
            return widget
        else:
            result = None
            for child in widget.children():
                v = findView(child)
                if v != None:
                    result = v
            return result

    # This bit of code disables the default Phong shading
    # and avoids the face colours appearing to change during rotation
    def fixLightModel():
        v = Gui.ActiveDocument.ActiveView.getViewer()
        sceneGraph = v.getSoEventManager().getSceneGraph()
        if str(sceneGraph.getChild(0).getName()) <> "LightModel":
            lm=coin.SoLightModel()
            lm.model.setValue(0)
            lm.setName("LightModel")
            sceneGraph.insertChild(lm,0)
    fixLightModel()

    # This bit of code persuades FreeCAD'a renderer to put
    # several views of the cube into the same window
    def MultiViews(parent, child, i, rotation):
        n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
        newchild=coin.SoMultipleCopy()
        newchild.addChild(child)
        views=coin.SoMFMatrix()
        views.setNum(8)
        m1=coin.SbMatrix()
        m1.makeIdentity()
        views.set1Value(0,m1)
        m2=coin.SbMatrix()
        m2.setTransform(
            coin.SbVec3f(n * 0.9 + 0.4, n * 0.9 + 0.4, 0.0),
            coin.SbRotation(coin.SbVec3f(-0.5,0.5,1),3.14159),
            coin.SbVec3f(0.5,0.5,0.5))
        views.set1Value(1,m2)
        m3=coin.SbMatrix()
        m3.setTransform(
            coin.SbVec3f(- n * 1.15 - 0.7, - n * 1.15 - 0.7, 0.0),
            rotation,
            coin.SbVec3f(0.5,0.5,0.5))
        views.set1Value(2,m3)
        m4=coin.SbMatrix()
        m4.setTransform(
            coin.SbVec3f(0,n,0),
            coin.SbRotation(coin.SbVec3f(1,0,0),3.14159*90/180.0),
            coin.SbVec3f(1,1,1))
        m4.multRight(m3)
        views.set1Value(3,m4)
        m5=coin.SbMatrix()
        m5.setTransform(
            coin.SbVec3f(n,0,0),
            coin.SbRotation(coin.SbVec3f(0,1,0),-3.14159*90/180.0),
            coin.SbVec3f(1,1,1))
        m5.multRight(m3)
        views.set1Value(4,m5)
        m6=coin.SbMatrix()
        m6.makeIdentity()
        m6.setTransform(
            coin.SbVec3f(-n,0,0),
            coin.SbRotation(coin.SbVec3f(0,1,0),3.14159*90/180.0),
            coin.SbVec3f(1,1,1))
        m6.multRight(m3)
        views.set1Value(5,m6)
        m7=coin.SbMatrix()
        m7.setTransform(
            coin.SbVec3f(0,-n,0),
            coin.SbRotation(coin.SbVec3f(-1,0,0),3.14159*90/180.0),
            coin.SbVec3f(1,1,1))
        m7.multRight(m3)
        views.set1Value(6,m7)
        m8=coin.SbMatrix()
        m8.setTransform(
            coin.SbVec3f(0,-n*2,0),
            coin.SbRotation(coin.SbVec3f(-1,0,0),3.14159),
            coin.SbVec3f(1,1,1))
        m8.multRight(m3)
        views.set1Value(7,m8)
        newchild.matrix=views
        parent.replaceChild(i,newchild)
    def createMultiViews(rotation):
        sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
        if sg.getNumChildren() != 0:
            for i in range(sg.getNumChildren()):
                child = sg.getChild(i)
                type = child.getTypeId().getName().__str__()
                if child.getTypeId().getName().__str__() == 'Separator':
                    name = child.getName().__str__()[:5]
                    if name != "arrow" and name != "label":
                        MultiViews(sg,child,i,rotation)
                if child.getTypeId().getName().__str__() == 'MultipleCopy':
                    if child.getNumChildren() != 0:
                        name = child.getChild(0).getName().__str__()
                        if fcd.getObject(name) == None:
                            child.removeAllChildren()
    createMultiViews(rotation)

    # This bit of code animates a slice rotation
    def rotate(dir, rs, re, steps):
        n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
        fc = Dictionary[str(App.ActiveDocument.Name)+"cubies"]
        fd = [[[[None for j in range(6)] for ix in range(n)] for iy in range(n)] for ix in range(n)]
        fp = [[[[Base.Placement() for j in range(6)] for ix in range(n)] for iy in range(n)] for ix in range(n)]
        xyz = ["x0","x1","y0","y1","z0","z1"]
        if dir.x > 0:
            # We need an explicit matrix for the final rotation step
            # to prevent rounding errors accumulating over time
            ff = Base.Matrix(1,0,0,0,0,0,-1,0,0,1,0,0,0,0,0,1)
            kk =[0,1,5,4,2,3]
            for iy in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[j][iy][iz][0] <> None:
                            for k in range(6):
                                c = fc[j][iy][iz][k]
                                c.Label = c.Name
                                fd[j][iy][iz][k] = c
                                fp[j][iy][iz][k] = c.Placement
            if steps > 0:
                fm = Base.Matrix()
                fm.rotateX(1.570795 / steps)
                for i in range(steps):
                    for iy in range(n):
                        for iz in range(n):
                            for j in range(rs, re):
                                if fc[j][iy][iz][0] <> None:
                                    for k in range(6):
                                        c = fc[j][iy][iz][k]
                                        p = c.Placement
                                        c.Placement = Base.Placement(fm).multiply(p)
                    Gui.updateGui()
            for iy in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[j][iy][iz][0] <> None:
                            for k in range(6):
                                c = fd[j][iz][n-1-iy][kk[k]]
                                p = fp[j][iz][n-1-iy][kk[k]]
                                c.Label = "fs"+str(j)+"q"+str(iy)+"q"+str(iz)+xyz[k]
                                c.Placement = Base.Placement(ff).multiply(p)
                                fc[j][iy][iz][k] = c
        elif dir.x < 0:
            ff = Base.Matrix(1,0,0,0,0,0,1,0,0,-1,0,0,0,0,0,1)
            kk =[0,1,4,5,3,2]
            for iy in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[j][iy][iz][0] <> None:
                            for k in range(6):
                                c = fc[j][iy][iz][k]
                                c.Label = c.Name
                                fd[j][iy][iz][k] = c
                                fp[j][iy][iz][k] = c.Placement
            if steps > 0:
                fm = Base.Matrix()
                fm.rotateX(-1.570795 / steps)
                for i in range(steps):
                    for iy in range(n):
                        for iz in range(n):
                            for j in range(rs, re):
                                if fc[j][iy][iz][0] <> None:
                                    for k in range(6):
                                        c = fc[j][iy][iz][k]
                                        p = c.Placement
                                        c.Placement = Base.Placement(fm).multiply(p)
                    Gui.updateGui()
            for iy in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[j][iy][iz][0] <> None:
                            for k in range(6):
                                c = fd[j][n-1-iz][iy][kk[k]]
                                p = fp[j][n-1-iz][iy][kk[k]]
                                c.Label = "fs"+str(j)+"q"+str(iy)+"q"+str(iz)+xyz[k]
                                c.Placement = Base.Placement(ff).multiply(p)
                                fc[j][iy][iz][k] = c
        elif dir.y > 0:
            ff = Base.Matrix(0,0,1,0,0,1,0,0,-1,0,0,0,0,0,0,1)
            kk =[4,5,2,3,1,0]
            for ix in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[ix][j][iz][0] <> None:
                            for k in range(6):
                                c = fc[ix][j][iz][k]
                                c.Label = c.Name
                                fd[ix][j][iz][k] = c
                                fp[ix][j][iz][k] = c.Placement
            if steps > 0:
                fm = Base.Matrix()
                fm.rotateY(1.570795 / steps)
                for i in range(steps):
                    for ix in range(n):
                        for iz in range(n):
                            for j in range(rs, re):
                                if fc[ix][j][iz][0] <> None:
                                    for k in range(6):
                                        c = fc[ix][j][iz][k]
                                        p = c.Placement
                                        c.Placement = Base.Placement(fm).multiply(p)
                    Gui.updateGui()
            for ix in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[ix][j][iz][0] <> None:
                            for k in range(6):
                                c = fd[n-1-iz][j][ix][kk[k]]
                                p = fp[n-1-iz][j][ix][kk[k]]
                                c.Label = "fs"+str(ix)+"q"+str(j)+"q"+str(iz)+xyz[k]
                                c.Placement = Base.Placement(ff).multiply(p)
                                fc[ix][j][iz][k] = c
        elif dir.y < 0:
            ff = Base.Matrix(0,0,-1,0,0,1,0,0,1,0,0,0,0,0,0,1)
            kk =[5,4,2,3,0,1]
            for ix in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[ix][j][iz][0] <> None:
                            for k in range(6):
                                c = fc[ix][j][iz][k]
                                c.Label = c.Name
                                fd[ix][j][iz][k] = c
                                fp[ix][j][iz][k] = c.Placement
            if steps > 0:
                fm = Base.Matrix()
                fm.rotateY(-1.570795 / steps)
                for i in range(steps):
                    for ix in range(n):
                        for iz in range(n):
                            for j in range(rs, re):
                                if fc[ix][j][iz][0] <> None:
                                    for k in range(6):
                                        c = fc[ix][j][iz][k]
                                        p = c.Placement
                                        c.Placement = Base.Placement(fm).multiply(p)
                    Gui.updateGui()
            for ix in range(n):
                for iz in range(n):
                    for j in range(rs, re):
                        if fc[ix][j][iz][0] <> None:
                            for k in range(6):
                                c = fd[iz][j][n-1-ix][kk[k]]
                                p = fp[iz][j][n-1-ix][kk[k]]
                                c.Label = "fs"+str(ix)+"q"+str(j)+"q"+str(iz)+xyz[k]
                                c.Placement = Base.Placement(ff).multiply(p)
                                fc[ix][j][iz][k] = c
        elif dir.z > 0:
            ff = Base.Matrix(0,-1,0,0,1,0,0,0,0,0,1,0,0,0,0,1)
            kk = [3,2,0,1,4,5]
            for ix in range(n):
                for iy in range(n):
                    for j in range(rs, re):
                        if fc[ix][iy][j][0] <> None:
                            for k in range(6):
                                c = fc[ix][iy][j][k]
                                c.Label = c.Name
                                fd[ix][iy][j][k] = c
                                fp[ix][iy][j][k] = c.Placement
            if steps > 0:
                fm = Base.Matrix()
                fm.rotateZ(1.570795 / steps)
                for i in range(steps):
                    for ix in range(n):
                        for iy in range(n):
                            for j in range(rs, re):
                                if fc[ix][iy][j][0] <> None:
                                    for k in range(6):
                                        c = fc[ix][iy][j][k]
                                        p = c.Placement
                                        c.Placement = Base.Placement(fm).multiply(p)
                    Gui.updateGui()
            for ix in range(n):
                for iy in range(n):
                    for j in range(rs, re):
                        if fc[ix][iy][j][0] <> None:
                            for k in range(6):
                                c = fd[iy][n-1-ix][j][kk[k]]
                                p = fp[iy][n-1-ix][j][kk[k]]
                                c.Label = "fs"+str(ix)+"q"+str(iy)+"q"+str(j)+xyz[k]
                                c.Placement = Base.Placement(ff).multiply(p)
                                fc[ix][iy][j][k] = c
        elif dir.z < 0:
            ff = Base.Matrix(0,1,0,0,-1,0,0,0,0,0,1,0,0,0,0,1)
            kk = [2,3,1,0,5,4]
            for ix in range(n):
                for iy in range(n):
                    for j in range(rs, re):
                        if fc[ix][iy][j][0] <> None:
                            for k in range(6):
                                c = fc[ix][iy][j][k]
                                c.Label = c.Name
                                fd[ix][iy][j][k] = c
                                fp[ix][iy][j][k] = c.Placement
            if steps > 0:
                fm = Base.Matrix()
                fm.rotateZ(-1.570795 / steps)
                for i in range(steps):
                    for ix in range(n):
                        for iy in range(n):
                            for j in range(rs, re):
                              if fc[ix][iy][j][0] <> None:
                                for k in range(6):
                                    c = fc[ix][iy][j][k]
                                    p = c.Placement
                                    c.Placement = Base.Placement(fm).multiply(p)
                    Gui.updateGui()
            for ix in range(n):
                for iy in range(n):
                    for j in range(rs, re):
                        if fc[ix][iy][j][0] <> None:
                            for k in range(6):
                                c = fd[n-1-iy][ix][j][kk[k]]
                                p = fp[n-1-iy][ix][j][kk[k]]
                                c.Label = "fs"+str(ix)+"q"+str(iy)+"q"+str(j)+xyz[k]
                                c.Placement = Base.Placement(ff).multiply(p)
                                fc[ix][iy][j][k] = c

    def slowrotate(dir, rs, re):
        n = Dictionary[str(App.ActiveDocument.Name)+"Size"]
        steps = slowness / (n * n)
        if re > rs:
            rotate(dir, rs, re, steps / (re - rs))
            Gui.updateGui()

    # Quick rotation for use when randomising or modifying history
    def fastrotate(dir, rs, re):
        rotate(dir, rs, re, 0)

    # These functions manage the history
    # Once you have created a cube, these functions will be defined and in scope
    # and you can call them from another macro created by saving history
    # or by hand from the python console window
    history = []
    Dictionary[str(App.ActiveDocument.Name)+"history"] = history
    def mrotpX(i,j):
        slowrotate(Base.Vector(1,0,0),i,j)
        Dictionary[str(App.ActiveDocument.Name)+"history"].append("mrotpX("+str(i)+","+str(j)+")")
    def mrotpY(i,j):
        slowrotate(Base.Vector(0,1,0),i,j)
        Dictionary[str(App.ActiveDocument.Name)+"history"].append("mrotpY("+str(i)+","+str(j)+")")
    def mrotpZ(i,j):
        slowrotate(Base.Vector(0,0,1),i,j)
        Dictionary[str(App.ActiveDocument.Name)+"history"].append("mrotpZ("+str(i)+","+str(j)+")")
    def mrotmX(i,j):
        slowrotate(Base.Vector(-1,0,0),i,j)
        Dictionary[str(App.ActiveDocument.Name)+"history"].append("mrotmX("+str(i)+","+str(j)+")")
    def mrotmY(i,j):
        slowrotate(Base.Vector(0,-1,0),i,j)
        Dictionary[str(App.ActiveDocument.Name)+"history"].append("mrotmY("+str(i)+","+str(j)+")")
    def mrotmZ(i,j):
        slowrotate(Base.Vector(0,0,-1),i,j)
        Dictionary[str(App.ActiveDocument.Name)+"history"].append("mrotmZ("+str(i)+","+str(j)+")")
    def undo():
        history = Dictionary[str(App.ActiveDocument.Name)+"history"]
        if len(history) > 0:
            fs = history.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[(p+1):(len(fs)-1)])
            if wh == "mrotmX":
                slowrotate(Base.Vector(1,0,0),i,j)
            elif wh == "mrotpX":
                slowrotate(Base.Vector(-1,0,0),i,j)
            elif wh == "mrotmY":
                slowrotate(Base.Vector(0,1,0),i,j)
            elif wh == "mrotpY":
                slowrotate(Base.Vector(0,-1,0),i,j)
            elif wh == "mrotmZ":
                slowrotate(Base.Vector(0,0,1),i,j)
            elif wh == "mrotpZ":
                slowrotate(Base.Vector(0,0,-1),i,j)
    def itostring(i, n):
        if 2 * i == n - 1:
            return "n/2"
        elif i <= n / 2:
            return str(i)
        elif i == n - 1:
            return "n-1"
        else:
            return "n-" + str(n-i) 
    def jtostring(j, n):
        if j <= n / 2:
           return str(j)
        elif 2 * j == n + 1:
            return "n/2+1"
        elif j == n:
            return "n"
        elif j == n - 1:
            return "n-1"
        else:
            return "n-" + str(n-j) 
    def saveHistory():
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        if len(history) > 0:
            # This statement will be needed at the start of any macro
            # to get the size of the cube in the currently active document
            # in case we have several documents open at once
            fs = "n = Dictionary[str(App.ActiveDocument.Name)+'Size']\n"
            for s in history:
                p = s.index(",")
                i = int(s[7:p])
                j = int(s[(p+1):(len(s)-1)])
                fs = fs + s[:7] + itostring(i, n) + ","
                fs = fs + jtostring(j, n) + ")\n"
            clip = QtCore.QCoreApplication.instance().clipboard()
            clip.setText(fs)
    def reset():
        busyCursor()
        fcd = App.ActiveDocument
        Dictionary[str(fcd.Name)+"history"] = []
        n = Dictionary[str(fcd.Name)+"Size"]
        fc = Dictionary[str(fcd.Name)+"cubies"]
        for obj in fcd.Objects:
            fs = obj.Name
            if fs[0:2] == "ff":
                obj.Label = fs
        for obj in fcd.Objects:
            fs = obj.Name
            if fs[0:2] == "ff":
                obj.Label = "fs"+fs[2:]
                obj.Placement = Base.Placement()
                l = len(fs)
                q1 = fs.find("q")
                q2 = fs.find("q",q1+1)
                ix = int(fs[2:q1])
                iy = int(fs[q1+1:q2])
                iz = int(fs[q2+1:l-2])
                k = "x0x1y0y1z0z1".find(fs[l-2:])/2
                fc[ix][iy][iz][k] = obj
        restoreCursor()

    # Randomise the cube
    def randomise():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        random.seed()
        i = random.randrange(0,6)
        for x in range(n*24):
            i = (i + 2 - i % 2 + random.randrange(0,4)) % 6
            j = random.randrange(0,n)
            if i == 0:
                fastrotate(Base.Vector(1,0,0),j,j+1)
                history.append("mrotpX("+str(j)+","+str(j+1)+")")
            elif i == 1:
                fastrotate(Base.Vector(-1,0,0),j,j+1)
                history.append("mrotmX("+str(j)+","+str(j+1)+")")
            elif i == 2:
                fastrotate(Base.Vector(0,1,0),j,j+1)
                history.append("mrotpY("+str(j)+","+str(j+1)+")")
            elif i == 3:
                fastrotate(Base.Vector(0,-1,0),j,j+1)
                history.append("mrotmY("+str(j)+","+str(j+1)+")")
            elif i == 4:
                fastrotate(Base.Vector(0,0,1),j,j+1)
                history.append("mrotpZ("+str(j)+","+str(j+1)+")")
            elif i == 5:
                fastrotate(Base.Vector(0,0,-1),j,j+1)
                history.append("mrotmZ("+str(j)+","+str(j+1)+")")
        restoreCursor()

    # Various macros to modify the history
    # They all read the history and undo it, and then perform some modified version
    # of the history. The modifications can be time-reversal, reflection along an
    # axis (as if the cube were reflected, the history replayed,
    # and the cube reflected back again), or rotation (as if the cube were rotated,
    # the history replayed, and the cube rotated back again).
    def slow_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        Gui.updateGui()
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                mrotpX(i,j)
            elif wh == "mrotmX":
                mrotmX(i,j)
            elif wh == "mrotpY":
                mrotpY(i,j)
            elif wh == "mrotmY":
                mrotmY(i,j)
            elif wh == "mrotpZ":
                mrotpZ(i,j)
            elif wh == "mrotmZ":
                mrotmZ(i,j)
        restoreCursor()
    def step_history():
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        Gui.updateGui()
        Dictionary[str(fcd.Name)+"Stepping"] = 1
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            w = StepWindow()
            w.label_1.setText("Doing "+wh+"("+str(i)+","+str(j)+")")
            w.label_1.setAlignment(QtCore.Qt.AlignCenter)
            w.exec_()
            if Dictionary[str(fcd.Name)+"Stepping"] == 0:
                break
            if wh == "mrotpX":
                mrotpX(i,j)
            elif wh == "mrotmX":
                mrotmX(i,j)
            elif wh == "mrotpY":
                mrotpY(i,j)
            elif wh == "mrotmY":
                mrotmY(i,j)
            elif wh == "mrotpZ":
                mrotpZ(i,j)
            elif wh == "mrotmZ":
                mrotmZ(i,j)
    def reverse_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        for fs in nh:
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
        restoreCursor()
    def undo_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        for fs in nh:
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
        restoreCursor()
    def reflectX_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(1,0,0),n-j,n-i)
                history.append("mrotpX("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(-1,0,0),n-j,n-i)
                history.append("mrotmX("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
        restoreCursor()
    def reflectY_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,1,0),n-j,n-i)
                history.append("mrotpY("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,-1,0),n-j,n-i)
                history.append("mrotmY("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
        restoreCursor()
    def reflectZ_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,1),n-j,n-i)
                history.append("mrotpZ("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,-1),n-j,n-i)
                history.append("mrotmZ("+str(n-j)+","+str(n-i)+")")
        restoreCursor()
    def rotpX_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,-1,0),n-j,n-i)
                history.append("mrotmY("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,1,0),n-j,n-i)
                history.append("mrotpY("+str(n-j)+","+str(n-i)+")")
        restoreCursor()
    def rotmX_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,0,-1),n-j,n-i)
                history.append("mrotmZ("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,0,1),n-j,n-i)
                history.append("mrotpZ("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
        restoreCursor()
    def rotpY_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(0,0,-1),n-j,n-i)
                history.append("mrotmZ("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(0,0,1),n-j,n-i)
                history.append("mrotpZ("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
        restoreCursor()
    def rotmY_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(-1,0,0),n-j,n-i)
                history.append("mrotmX("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(1,0,0),n-j,n-i)
                history.append("mrotpX("+str(n-j)+","+str(n-i)+")")
        restoreCursor()
    def rotpZ_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(0,1,0),i,j)
                history.append("mrotpY("+str(i)+","+str(j)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(0,-1,0),i,j)
                history.append("mrotmY("+str(i)+","+str(j)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(-1,0,0),n-j,n-i)
                history.append("mrotmX("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(1,0,0),n-j,n-i)
                history.append("mrotpX("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
        restoreCursor()
    def rotmZ_history():
        busyCursor()
        fcd = App.ActiveDocument
        history = Dictionary[str(fcd.Name)+"history"]
        n = Dictionary[str(fcd.Name)+"Size"]
        nh = []
        while len(history) > 0:
            nh.append(history.pop())
        reset()
        history = Dictionary[str(fcd.Name)+"history"]
        while len(nh) > 0:
            fs = nh.pop()
            wh = fs[:6]
            p = fs.index(",")
            i = int(fs[7:p])
            j = int(fs[p+1:len(fs)-1])
            if wh == "mrotpX":
                fastrotate(Base.Vector(0,-1,0),n-j,n-i)
                history.append("mrotmY("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotmX":
                fastrotate(Base.Vector(0,1,0),n-j,n-i)
                history.append("mrotpY("+str(n-j)+","+str(n-i)+")")
            elif wh == "mrotpY":
                fastrotate(Base.Vector(1,0,0),i,j)
                history.append("mrotpX("+str(i)+","+str(j)+")")
            elif wh == "mrotmY":
                fastrotate(Base.Vector(-1,0,0),i,j)
                history.append("mrotmX("+str(i)+","+str(j)+")")
            elif wh == "mrotpZ":
                fastrotate(Base.Vector(0,0,1),i,j)
                history.append("mrotpZ("+str(i)+","+str(j)+")")
            elif wh == "mrotmZ":
                fastrotate(Base.Vector(0,0,-1),i,j)
                history.append("mrotmZ("+str(i)+","+str(j)+")")
        restoreCursor()

    # This bit of code creates the buttons at the top of the view window
    # The buttons are in a frameless window to save screen space
    class ButtonRow(QtGui.QWidget):
        def __init__(self):
            super(ButtonRow, self).__init__()
            mw = Gui.getMainWindow()
            view3DWidget = findView(mw.centralWidget())
            if view3DWidget != None:
                self.setParent(view3DWidget)
            self.setAutoFillBackground(True)
            self.undoButton = QtGui.QPushButton(self)
            self.undoButton.setText("Undo")
            self.undoButton.clicked.connect(self.onUndo)
            self.saveButton = QtGui.QPushButton(self)
            self.saveButton.setText("Copy history to clipboard")
            self.saveButton.clicked.connect(self.onSave)
            self.resetButton = QtGui.QPushButton(self)
            self.resetButton.setText("Reset")
            self.resetButton.clicked.connect(self.onReset)
            self.show()
        def onUndo(self):
            undo()
        def onReset(self):
            reset()
        def onSave(self):
            saveHistory()
        def paintEvent(self, event):
            # we position the buttons every paint
            # in case the window size has changed
            bh = 30
            bw = 80
            mw = Gui.getMainWindow()
            view3DWidget = findView(mw.centralWidget())
            if view3DWidget != None:
                geom = view3DWidget.geometry()
                xpos = 0
                self.setGeometry(xpos, 0, geom.width(), bh + 10)
                gap = (geom.width() - 5 * bw) / 4
                if gap < 0:
                    gap = 0
                xpos = gap
                self.undoButton.setGeometry(xpos, 0, bw, bh)
                xpos = xpos + gap + bw
                self.saveButton.setGeometry(xpos, 0, 3 * bw, bh)
                xpos = xpos + 3 * bw + gap
                self.resetButton.setGeometry(xpos, 0, bw, bh)
            # now do the paint, which will paint the buttons as well since they
            # are this widget's children
            super(ButtonRow, self).paintEvent(event)
    Dictionary[str(App.ActiveDocument.Name)+"buttons"] = ButtonRow()

    # FreeCAD's file save only saves the state of the camera
    # and the shapes, positions, orientations, names, and labels
    # of the objects in the scene 
    # This function recreates all the other stuff after reloading a saved file
    # I haven't found a way to make FreeCAD save the history, so it gets reset
    def fix_reload():
        busyCursor()
        fcd = App.ActiveDocument
        # first we find how big a cube we have
        n = 0
        for obj in fcd.Objects:
            fs = obj.Name
            if fs[0:2] == "ff":
                i = int(fs[2:fs.index("q")])
                if i > n:
                    n = i
            elif fs[0:4] == "Text":
                # get rid of this because it's incorrectly positioned
                # we'll create a new one later
                fcd.removeObject(fs)
            elif fs[0:5] == "arrow":
                obj.ViewObject.RootNode.setName(coin.SbName(fs))
        n = n + 1
        fc = [[[[None for j in range(6)] for ix in range(n)] for iy in range(n)] for ix in range(n)]
        Dictionary[str(fcd.Name)+"Size"] = n
        for obj in fcd.Objects:
            fs = obj.Label
            if fs[0:2] == "fs":
                l = len(fs)
                q1 = fs.find("q")
                q2 = fs.find("q",q1+1)
                ix = int(fs[2:q1])
                iy = int(fs[q1+1:q2])
                iz = int(fs[q2+1:l-2])
                k = "x0x1y0y1z0z1".find(fs[l-2:])/2
                fc[ix][iy][iz][k] = obj
        Dictionary[str(fcd.Name)+"cubies"] = fc
        Dictionary[str(fcd.Name)+"ViewObserver"] = ViewObserver()
        doLabels() # create new labels
        rotation = fixCamera(False)
        # create the buttons at the top of the window
        Dictionary[str(App.ActiveDocument.Name)+"buttons"] = ButtonRow()
        fixLightModel()
        createMultiViews(rotation)
        history = [] # according to Henry Ford
        Dictionary[str(fcd.Name)+"history"] = history
        restoreCursor()
        FreeCAD.Console.PrintLog("fix_reload() done\n")

    restoreCursor()



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Rubik Cube/pl
