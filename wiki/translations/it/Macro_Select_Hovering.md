 {{Macro/it
|Name=Macro Select Hovering
|Icon=Macro_Select_Hovering.png
|Translate=Macro Seleziona passando il mouse.
|Description=Questa macro seleziona a scelta una Faccia, Bordo, Vertice passando il mouse.<br/>PS: Per deselezionare una faccia (o altro) cliccare {{KEY | Pause grab}} e usare la procedura standard: CTRL + Click
|Author=Mario52
|Version=00.03b
|Date=2020-10-28
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d8/Macro_Select_Hovering.png ToolBar Icon]
}}

![Macro Select Hovering](images/Select_Hovering00.gif )

![Macro Select Hovering](images/Macro_Select_Hovering_00.png )

## Descrizione

Questa macro seleziona a scelta una Faccia, Bordo, Vertice passando sopra con il mouse

PS: Per deselezionare una faccia (o altro) cliccare {{KEY | Pause grab}} e usare la procedura standard: CTRL + Click

## Utilizzo

Passare sopra agli elementi con il mouse

### Icone

L\'icona deve essere copiata nella stessa directory della macro

## Script

L\'icona per la barra degli strumenti ![Macro Select Hovering](images/Macro_Select_Hovering.png )

**Macro\_Select\_Hovering.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
"""
***************************************************************************
*   Copyright (c) 2017 2018 2019 2020 <mario52>                           *
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
*           WARNING! All changes in this file will be lost and            *  
*                  may cause malfunction of the program                   *
***************************************************************************
"""
#
#Macro_ _01-25/12/2017 02-26/12/2017 03-26/12/2017 03b-28/10/2020
#
#OS: Windows 10
#Word size of OS: 64-bit
#Word size of FreeCAD: 64-bit
#Version: 0.16.6712 (Git)
#Build type: Release
#Branch: releases/FreeCAD-0-16
#Hash: da2d364457257a7a8c6fb2137cea12c45becd71a
#Python version: 2.7.8
#Qt version: 4.8.7
#Coin version: 4.0.0a
#OCC version: 6.8.0.oce-0.17
#
__title__   = "Macro_Select_Hovering"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__Wiki__    = "http://www.freecadweb.org/wiki/index.php?title=Macro_Select_Hovering"
__version__ = "00.03b"
__date__    = "28/10/2020"

import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *
 
import Draft, Part, PartGui, FreeCADGui, FreeCAD

Gui = FreeCADGui
App = FreeCAD

global ui         ; ui           = ""
global s          ; s            = ""

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.window = MainWindow
        #################################################################################
        #self.path  = FreeCAD.ConfigGet("AppHomePath")
        #self.path  = FreeCAD.ConfigGet("UserAppData")
        #self.path  = "your path"
        param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")# macro path
        self.path = param.GetString("MacroPath","") + "/"                   # macro path
        self.path = self.path.replace("\\","/")
#        print( "Path for the icons : " , self.path)
        #################################################################################
        self.FontImpost    = "Arial"
        self.fontGlobal_08 = QtGui.QFont()            # pour compatibilite Windows Linux
        self.fontGlobal_08.setFamily(self.FontImpost) # pour compatibilite Windows Linux
        self.fontGlobal_08.setPointSize(8.0)          # pour compatibilite Windows Linux
        #self.xxxx.setFont(self.fontGlobal_08)        # pour W L
        #self.xxxx.setFont(QtGui.QFont(self.FontImpost,weight=QtGui.QFont.Bold))  # Bold
        #################################################################################

        self.comptFace         = 0
        self.comptEdge         = 0
        self.comptVertex       = 0
        self.Stop_Grab         = 1
        self.comptSurfaceFace  = 0.0
        self.comptSurfaceTotal = 0.0
        self.comptLengthObject = 0.0
        self.comptLengthTotal  = 0.0

    def setupUi(self, MainWindow):
        MainWindow.resize(197, 307)
        MainWindow.setMinimumSize(QtCore.QSize(197, 307))
        MainWindow.setMaximumSize(QtCore.QSize(197, 307))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.GBOX_01_Face = QtGui.QGroupBox(self.centralwidget)
        self.GBOX_01_Face.setGeometry(QtCore.QRect(10, 10, 176, 91))
        self.GBOX_01_Face.setFont(self.fontGlobal_08)         # pour W L
        self.GBOX_01_Face.setObjectName(_fromUtf8("GBOX_01_Face"))

        self.LE_02_Area_Object = QtGui.QLineEdit(self.GBOX_01_Face)
        self.LE_02_Area_Object.setGeometry(QtCore.QRect(90, 60, 75, 20))
        self.LE_02_Area_Object.setFont(self.fontGlobal_08)    # pour W L
        self.LE_02_Area_Object.setObjectName(_fromUtf8("LE_02_Area_Object"))

        self.LAB_05_Area_Object = QtGui.QLabel(self.GBOX_01_Face)
        self.LAB_05_Area_Object.setGeometry(QtCore.QRect(90, 40, 71, 16))
        self.LAB_05_Area_Object.setFont(self.fontGlobal_08)   # pour W L
        self.LAB_05_Area_Object.setObjectName(_fromUtf8("LAB_05_Area_Object"))

        self.CB_01_Sel_Face = QtGui.QCheckBox(self.GBOX_01_Face)
        self.CB_01_Sel_Face.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.CB_01_Sel_Face.setFont(self.fontGlobal_08)       # pour W L
        self.CB_01_Sel_Face.setObjectName(_fromUtf8("CB_01_Sel_Face"))

        self.LE_01_Area_Total = QtGui.QLineEdit(self.GBOX_01_Face)
        self.LE_01_Area_Total.setGeometry(QtCore.QRect(10, 60, 75, 20))
        self.LE_01_Area_Total.setFont(self.fontGlobal_08)     # pour W L
        self.LE_01_Area_Total.setObjectName(_fromUtf8("LE_01_Area_Total"))

        self.LAB_01_Face = QtGui.QLabel(self.GBOX_01_Face)
        self.LAB_01_Face.setGeometry(QtCore.QRect(110, 23, 56, 16))
        self.LAB_01_Face.setFont(self.fontGlobal_08)          # pour W L
        self.LAB_01_Face.setObjectName(_fromUtf8("LAB_01_Face"))

        self.LAB_04_Area_Total = QtGui.QLabel(self.GBOX_01_Face)
        self.LAB_04_Area_Total.setGeometry(QtCore.QRect(10, 40, 56, 16))
        self.LAB_04_Area_Total.setFont(self.fontGlobal_08)    # pour W L
        self.LAB_04_Area_Total.setObjectName(_fromUtf8("LAB_04_Area_Total"))


        self.GBOX_02_Edge = QtGui.QGroupBox(self.centralwidget)
        self.GBOX_02_Edge.setGeometry(QtCore.QRect(10, 105, 176, 91))
        self.GBOX_02_Edge.setFont(self.fontGlobal_08)         # pour W L
        self.GBOX_02_Edge.setObjectName(_fromUtf8("GBOX_02_Edge"))

        self.LAB_02_Edge = QtGui.QLabel(self.GBOX_02_Edge)
        self.LAB_02_Edge.setGeometry(QtCore.QRect(110, 25, 56, 16))
        self.LAB_02_Edge.setFont(self.fontGlobal_08)          # pour W L
        self.LAB_02_Edge.setObjectName(_fromUtf8("LAB_02_Edge"))

        self.CB_02_Sel_Edge = QtGui.QCheckBox(self.GBOX_02_Edge)
        self.CB_02_Sel_Edge.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.CB_02_Sel_Edge.setFont(self.fontGlobal_08)       # pour W L
        self.CB_02_Sel_Edge.setObjectName(_fromUtf8("CB_02_Sel_Edge"))

        self.LE_03_Length_Total = QtGui.QLineEdit(self.GBOX_02_Edge)
        self.LE_03_Length_Total.setGeometry(QtCore.QRect(10, 60, 75, 20))
        self.LE_03_Length_Total.setFont(self.fontGlobal_08)   # pour W L
        self.LE_03_Length_Total.setObjectName(_fromUtf8("LE_03_Length_Total"))

        self.LE_04_Length_Object = QtGui.QLineEdit(self.GBOX_02_Edge)
        self.LE_04_Length_Object.setGeometry(QtCore.QRect(90, 60, 75, 20))
        self.LE_04_Length_Object.setFont(self.fontGlobal_08)  # pour W L
        self.LE_04_Length_Object.setObjectName(_fromUtf8("LE_04_Length_Object"))

        self.LAB_06_Length_Total = QtGui.QLabel(self.GBOX_02_Edge)
        self.LAB_06_Length_Total.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.LAB_06_Length_Total.setFont(self.fontGlobal_08)  # pour W L
        self.LAB_06_Length_Total.setObjectName(_fromUtf8("LAB_06_Length_Total"))

        self.LAB_07_Length_Obgect = QtGui.QLabel(self.GBOX_02_Edge)
        self.LAB_07_Length_Obgect.setGeometry(QtCore.QRect(90, 40, 71, 16))
        self.LAB_07_Length_Obgect.setFont(self.fontGlobal_08) # pour W L
        self.LAB_07_Length_Obgect.setObjectName(_fromUtf8("LAB_07_Length_Obgect"))


        self.GBOX_03_Vertex = QtGui.QGroupBox(self.centralwidget)
        self.GBOX_03_Vertex.setGeometry(QtCore.QRect(10, 200, 176, 46))
        self.GBOX_03_Vertex.setFont(self.fontGlobal_08)       # pour W L
        self.GBOX_03_Vertex.setObjectName(_fromUtf8("GBOX_03_Vertex"))

        self.LAB_03_Vertex = QtGui.QLabel(self.GBOX_03_Vertex)
        self.LAB_03_Vertex.setGeometry(QtCore.QRect(110, 25, 56, 16))
        self.LAB_03_Vertex.setFont(self.fontGlobal_08)        # pour W L
        self.LAB_03_Vertex.setObjectName(_fromUtf8("LAB_03_Vertex"))

        self.CB_03_Sel_Vertex = QtGui.QCheckBox(self.GBOX_03_Vertex)
        self.CB_03_Sel_Vertex.setGeometry(QtCore.QRect(10, 22, 91, 17))
        self.CB_03_Sel_Vertex.setFont(self.fontGlobal_08)     # pour W L
        self.CB_03_Sel_Vertex.setObjectName(_fromUtf8("CB_03_Sel_Vertex"))


        self.GBOX_04_Main = QtGui.QGroupBox(self.centralwidget)
        self.GBOX_04_Main.setGeometry(QtCore.QRect(10, 250, 176, 51))
        self.GBOX_04_Main.setFont(self.fontGlobal_08)         # pour W L
        self.GBOX_04_Main.setObjectName(_fromUtf8("GBOX_04_Main"))

        self.PB_02_Stop_Grab = QtGui.QPushButton(self.GBOX_04_Main)
        self.PB_02_Stop_Grab.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.PB_02_Stop_Grab.setFont(self.fontGlobal_08)      # pour W L
        self.PB_02_Stop_Grab.setObjectName(_fromUtf8("PB_02_Stop_Grab"))
        self.PB_02_Stop_Grab.clicked.connect(self.on_PB_02_Stop_Grab_clicked)

        self.PB_01_Quit = QtGui.QPushButton(self.GBOX_04_Main)
        self.PB_01_Quit.setGeometry(QtCore.QRect(5, 20, 75, 23))
        self.PB_01_Quit.setFont(self.fontGlobal_08)           # pour W L
        self.PB_01_Quit.setObjectName(_fromUtf8("PB_01_Quit"))
        self.PB_01_Quit.clicked.connect(self.on_PB_Quit_clicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Select_Hovering")
        MainWindow.setWindowIcon(QtGui.QIcon(self.path + __title__ +".png"))#
        self.GBOX_01_Face.setTitle("Face")
        self.CB_01_Sel_Face.setText("Select Face")
        self.LAB_01_Face.setText("0")
        self.LAB_04_Area_Total.setText("Area Total")
        self.LAB_05_Area_Object.setText("Area Object")

        self.GBOX_02_Edge.setTitle("Edge")
        self.CB_02_Sel_Edge.setText("Select Edge")
        self.LAB_02_Edge.setText("0")
        self.LAB_06_Length_Total.setText("Length Total")
        self.LAB_07_Length_Obgect.setText("Length Object")

        self.GBOX_03_Vertex.setTitle("Vertex")
        self.CB_03_Sel_Vertex.setText("Select Vertex")
        self.LAB_03_Vertex.setText("0")

        self.GBOX_04_Main.setTitle("Main")
        self.PB_01_Quit.setText("Quit")
        self.PB_02_Stop_Grab.setText("Pause grab")

        MainWindow.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint)       # PySide cette fonction met la fenetre en avant


    def on_PB_02_Stop_Grab_clicked(self):
        global s

        if self.Stop_Grab == 1:
            FreeCADGui.Selection.removeObserver(s)                             # desinstalle la fonction residente SelObserver
            self.Stop_Grab = 0
            self.PB_02_Stop_Grab.setText("Active grab")
            print( "Grab pause")
        else:
            s=SelObserver()
            FreeCADGui.Selection.addObserver(s)                                # installe la fonction en mode resident
            self.Stop_Grab = 1
            self.PB_02_Stop_Grab.setText("Pause grab")
            print( "Grab active")

    def on_PB_Quit_clicked(self):
        global s

        FreeCADGui.Selection.removeObserver(s)                              # desinstalle la fonction residente SelObserver
        self.window.hide()                                                  # hide the window and close the macro
        print( "Quit ",__title__)

##################################################################################################
class SelObserver:
    global ui

    def setPreselection(self,doc,obj,sub): # preselection
        global ui

        if ui.CB_01_Sel_Face.isChecked():

            if (sub[:4] == "Face") and (Gui.Selection.isSelected (FreeCAD.ActiveDocument.getObject(obj), sub) == False):
                Gui.Selection.addSelection(FreeCAD.ActiveDocument.getObject(obj), sub)
                ui.comptFace += 1
                ui.LAB_01_Face.setText(str(ui.comptFace))

                ui.comptSurfaceFace = FreeCAD.ActiveDocument.getObject(obj).Shape.Faces[int(sub[4:])-1].Area
                ui.comptSurfaceTotal += ui.comptSurfaceFace
                ui.LE_01_Area_Total.setText(str(ui.comptSurfaceTotal))
                ui.LE_02_Area_Object.setText(str(ui.comptSurfaceFace))


        if ui.CB_02_Sel_Edge.isChecked():

            if (sub[:4] == "Edge") and (Gui.Selection.isSelected (FreeCAD.ActiveDocument.getObject(obj), sub) == False):
                objetSelect = Gui.Selection.addSelection(FreeCAD.ActiveDocument.getObject(obj), sub)

                ui.comptEdge += 1
                ui.LAB_02_Edge.setText(str(ui.comptEdge))

                ui.comptLengthObject = FreeCAD.ActiveDocument.getObject(obj).Shape.Edges[int(sub[4:])-1].Length
                ui.comptLengthTotal += ui.comptLengthObject
                ui.LE_03_Length_Total.setText(str(ui.comptLengthTotal))
                ui.LE_04_Length_Object.setText(str(ui.comptLengthObject))


        if ui.CB_03_Sel_Vertex.isChecked():

            if sub[:6] == "Vertex" and (Gui.Selection.isSelected (FreeCAD.ActiveDocument.getObject(obj), sub) == False):
                Gui.Selection.addSelection(FreeCAD.ActiveDocument.getObject(obj), sub)
                ui.comptVertex += 1
                ui.LAB_03_Vertex.setText(str(ui.comptVertex))


#    def removePreselection(self,doc,obj,sub) # 
#        print( "removePreselection")
#    def addSelection(self,doc,obj,sub,pnt):  # Selection
#        print( "addSelection")
#    def removeSelection(self,doc,obj,sub):   # Effacer l'objet selectionne
#        print( "removeSelection")
#    def setSelection(self,doc):              # Selection dans ComboView
#        FreeCADGui.Selection.removeObserver(s)
#        print( "setSelection quit")

    def clearSelection(self,doc):            # Si clic sur l'ecran, effacer la selection
        global ui

        ui.comptFace   = 0
        ui.comptEdge   = 0
        ui.comptVertex = 0
        ui.comptSurfaceFace  = 0.0
        ui.comptSurfaceTotal = 0.0
        ui.comptLengthObject = 0.0
        ui.comptLengthTotal  = 0.0
        ui.LAB_01_Face.setText(str(ui.comptFace))
        ui.LAB_02_Edge.setText(str(ui.comptEdge))
        ui.LAB_03_Vertex.setText(str(ui.comptVertex))
        ui.LE_01_Area_Total.setText(str(ui.comptSurfaceTotal))
        ui.LE_02_Area_Object.setText(str(ui.comptSurfaceFace))
        ui.LE_03_Length_Total.setText(str(ui.comptLengthTotal))
        ui.LE_04_Length_Object.setText(str(ui.comptLengthObject))
#        print( "clearSelection")

s=SelObserver()
FreeCADGui.Selection.addObserver(s)          # installe la fonction en mode resident
###################################################################################################

doc = FreeCAD.ActiveDocument
if doc == None:
    doc = FreeCAD.newDocument()

MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(MainWindow)
ui.setupUi(MainWindow)
MainWindow.show()



}}

## Versioni

ver 00.03b (28/10/2020) : add print**()** for Python 3

ver 00.03 (26/12/2017) : replace test with (FreeCAD.ActiveDocument.getObject(obj), sub) == False)

ver 00.02 (26/12/2017) :

ver 00.01 (25/12/2017) :

## Vincolo

[Multiple face selection to convert a shape to a solid](https://forum.freecadweb.org/viewtopic.php?f=3&t=26370)
