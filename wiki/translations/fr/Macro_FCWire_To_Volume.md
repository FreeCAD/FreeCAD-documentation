# Macro FCWire To Volume/fr
 {{Macro/fr
|Name=Macro FCWire To Volume
|Icon=Macro_FCWire_To_Volume.png
|Description=Créez l'opération booléenne avec les fils sélectionnés. Appuyez sur le bouton 2d pour créer l'opération booléenne sur un fil 2D.
|Author=Mario52
|Version=0.02c
|Date=2020/04/11
|FCVersion=0.19
|Download=[https://www.freecadweb.org/wiki/images/f/f2/Macro_FCWire_To_Volume.png ToolBar Icon]
}}

## Description

Cette macro crée une extrusion avec des objets Draft en une seule opération.

<img alt="" src=images/Macro_FCWire_To_Volume_01.png  style="width:400px;">

## Utilisation

Sélectionnez vos objet qui serviront à la création de l\'extrusion, donnez la hauteur de l\'extrusion choisissez le type d\'extrusion et validez avec le bouton **Create**. Appuyez sur le bouton 2d pour créer l\'opération booléenne sur un fil 2D.

![](images/Macro_FCWire_To_Volume_00.png )

### Epaisseur solide 

-    {{SpinBox|SpinBox}}: Donnez l\'épaisseur

### Choix

#### Booléen


{{RadioButton|TRUE|Intersection}}

: Opération booléenne


{{RadioButton|Substraction}}

: Opération booléenne


{{RadioButton|Union}}

: Opération booléenne


{{RadioButton|Xor}}

: Opération booléenne

#### Axes


{{RadioButton|X Axis}}

: Axe X


{{RadioButton|Y Axis}}

: Axe Y


{{RadioButton|TRUE|Z Axis}}

: Axe Z (défaut)


{{RadioButton|Direction}}

: (Non fonctionnel plus tard)

#### Option


{{CheckBox|TRUE|Single object}}

: Si la case à cocher est cochée, l\'objet se trouve sur un seul objet sinon l\'objet créé conserve la hiérarchie de la construction de l\'objet


{{CheckBox|TRUE|Hidden}}

: Les objets originaux sont cachés


{{CheckBox|Color}}

: S\'il a vérifié l\'objet résultant est coloré en rouge

#### Commande

-    **Create 2D**: Créez l\'objet booléen 2D (fil de contour avec {{Incode|Draft.makeShape2DView()}})

-    **Create 3D**: Créer l\'objet booléen 3D (solide)

-    **Help**: Connectez-vous à la page wiki (dans le navigateur FreeCAD)

-    **Quit**: Quittez la macro

## Script

Copiez la macro dans votre répertoire de macros

L\'icône pour votre barre d\'outils <img alt="" src=images/Macro_FCWire_To_Volume.png  style="width:32px;">

**Macro\_FCWire\_To\_Volume.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
"""
***************************************************************************
*   Copyright (c) 2016 2017 2018 2019 2020 <mario52>                      *
*                                                                         *
*   This file is a supplement to the FreeCAD CAx development system.      *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU Lesser General Public License (LGPL)    *
*   as published by the Free Software Foundation; either version 2 of     *
*   the License, or (at your option) any later version.                   *
*   for detail see the LICENCE text file.                                 *
**                                                                       **
*   Use at your own risk. The author assumes no liability for data loss.  *
*              It is advised to backup your data frequently.              *
*             If you do not trust the software do not use it.             *
**                                                                       **
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
#Macro_FCWire_To_Volume 10/10/2016_01, 2020/04/08_02, 2020/04/10_2b, 2020/04/11_2c
#
#OS: Windows 10 (10.0)
#Word size of OS: 64-bit
#Word size of FreeCAD: 64-bit
#Version: 0.19.20311 (Git)
#Build type: Release
#Branch: master
#Hash: 915e551bbb7e3614bc804f1ae1f65027b5432b9f
#Python version: 3.6.8
#Qt version: 5.12.1
#Coin version: 4.0.0a
#OCC version: 7.3.0
#
__title__   = "Macro_FCWire_To_Volume"
__author__  = "Mario52"
__url__     = "https://wiki.freecadweb.org/Macro_FCWire_To_Volume"
__version__ = "00.02c"
__date__    = "2020/04/11"    #YYYY/MM/DD

if int(FreeCAD.Version()[1]) < 18:      # Version de FreeCAD
    FreeCAD.Console.PrintMessage("This version " + __title__ + " rmu  work with the FreeCAD 0.18 or higher. " + "\n\n")

import PySide2
from PySide2 import (QtWidgets, QtCore, QtGui)
from PySide2.QtWidgets import (QWidget, QApplication, QSlider, QGraphicsView, QGraphicsScene, QVBoxLayout, QStyle)
from PySide2.QtGui import (QPainter, QColor, QIcon)
#from PySide2.QtSvg import *
#import PySide2.QtXml
import WebGui

import Draft, Part, PartGui, FreeCADGui, FreeCAD
from FreeCAD import Base
import math
from math import sqrt, pi, sin, cos, asin

Gui = FreeCADGui
App = FreeCAD

global create2D ; create2D = 0
global ui       ; ui       = ""
global doc

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

    def __init__(self ):
        self.window = MainWindow
        #self.path   = FreeCAD.ConfigGet("AppHomePath")
        self.path   = FreeCAD.ConfigGet("UserAppData")
        self.path   = self.path.replace("\\","/")

        self.thicknessValue  = 0.0
        self.thicknessX      = 0.0     # extrusion
        self.thicknessY      = 0.0     # extrusion
        self.thicknessZ      = 0.0     # extrusion
        self.thicknessD      = 0.0     # extrusion

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("__title__"))
        MainWindow.resize(300, 300)
#        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
#        MainWindow.setMaximumSize(QtCore.QSize(300, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.groupBox0 = QtWidgets.QGroupBox()
        self.groupBox_01 = QtWidgets.QGroupBox()

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setMaximum(999999.999999)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setValue(0.0)
        self.doubleSpinBox.setAlignment(PySide2.QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setSuffix(" mm")
        self.doubleSpinBox.valueChanged.connect(self.on_doubleSpinBox) ###
        ####
        self.groupBox_02 = QtWidgets.QGroupBox()

        self.GroupBox_Bool = QtWidgets.QGroupBox()
        self.RB_Intersection = QtWidgets.QRadioButton()
        self.RB_Intersection.setIcon(QtGui.QIcon.fromTheme("bool",QtGui.QIcon(":/icons/Part_Common.svg")))
        self.RB_Intersection.setChecked(True)
        self.RB_Cut = QtWidgets.QRadioButton()
        self.RB_Cut.setIcon(QtGui.QIcon.fromTheme("bool",QtGui.QIcon(":/icons/Part_Cut.svg")))
        self.RB_Union = QtWidgets.QRadioButton()
        self.RB_Union.setIcon(QtGui.QIcon.fromTheme("bool",QtGui.QIcon(":/icons/Part_Fuse.svg")))
        self.RB_Xor = QtWidgets.QRadioButton()
        self.RB_Xor.setIcon(QtGui.QIcon.fromTheme("bool",QtGui.QIcon(":/icons/Part_XOR.svg")))
        ####
        self.groupBox_Axis = QtWidgets.QGroupBox()
        self.RB_Axis_X = QtWidgets.QRadioButton()
        self.RB_Axis_X.setIcon(QtGui.QIcon.fromTheme("axis",QtGui.QIcon(":/icons/Std_CoordinateSystem.svg")))
        self.RB_Axis_Y = QtWidgets.QRadioButton()
        self.RB_Axis_Y.setIcon(QtGui.QIcon.fromTheme("axis",QtGui.QIcon(":/icons/Std_CoordinateSystem.svg")))
        self.RB_Axis_Z = QtWidgets.QRadioButton()
        self.RB_Axis_Z.setChecked(True)
        self.RB_Axis_Z.setIcon(QtGui.QIcon.fromTheme("axis",QtGui.QIcon(":/icons/Std_CoordinateSystem.svg")))
        self.RB_Axis_D = QtWidgets.QRadioButton()
        self.RB_Axis_D.setEnabled(False)
        self.RB_Axis_D.setIcon(QtGui.QIcon.fromTheme("axis",QtGui.QIcon(":/icons/Part_Line_Parametric.svg")))#Std_CoordinateSystem
        ####
        self.groupBox_03 = QtWidgets.QGroupBox()
        self.checkBox_01 = QtWidgets.QCheckBox()
        self.checkBox_01.setChecked(True)             #  # False
        self.checkBox_01.setIcon(QtGui.QIcon.fromTheme("part",QtGui.QIcon(":/icons/Tree_Part.svg")))
        self.checkBox_01.clicked.connect(self.on_checkBox_01) ###

        self.CB_Create_2D_Visible = QtWidgets.QCheckBox()
        self.CB_Create_2D_Visible.setChecked(True)    #    # False
        self.CB_Create_2D_Visible.clicked.connect(self.on_CB_Create_2D_Visible) ###
#        self.CB_Create_2D_Visible.setIcon(QtGui.QIcon.fromTheme("draft",QtGui.QIcon(":/icons/dagViewVisible.svg")))#

        self.CB_Colorer = QtWidgets.QCheckBox()
        self.CB_Colorer.setChecked(False)             # True   # 
        self.CB_Colorer.setIcon(QtGui.QIcon.fromTheme("part",QtGui.QIcon(":/icons/colors.svg")))
        ####
        self.groupBox_04 = QtWidgets.QGroupBox()
        self.PB_Create_2D = QtWidgets.QPushButton()
        self.PB_Create_2D.clicked.connect(self.on_PB_Create_2D) ###
        self.PB_Create_2D.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogOkButton))) #
        self.PB_Create = QtWidgets.QPushButton()
        self.PB_Create.clicked.connect(self.on_PB_Create) ###
        self.PB_Create.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogOkButton))) #
        self.PB_Help = QtWidgets.QPushButton()
        self.PB_Help.clicked.connect(self.on_PB_Help) ###
        self.PB_Help.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion))) #
        self.PB_Quit = QtWidgets.QPushButton()
        self.PB_Quit.clicked.connect(self.on_PB_Quit) ###
        self.PB_Quit.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))) #

        ####gridLayout####
        self.gridLayout0 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout0.setContentsMargins(10, 10, 10, 10)
        self.gridLayout0.addWidget(self.groupBox0, 0, 0, 1, 1)
        ####
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox0)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        ####
        self.gridLayout_02 = QtWidgets.QGridLayout(self.groupBox_01)
        self.gridLayout_02.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_02.addWidget(self.doubleSpinBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_01, 0, 0, 1, 2)
        ####
        self.gridLayout_03 = QtWidgets.QGridLayout(self.groupBox_02)
        self.gridLayout_03.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_03.addWidget(self.groupBox_02, 0, 0, 1, 1)
        ####
        self.gridLayout_04 = QtWidgets.QGridLayout(self.GroupBox_Bool)
        self.gridLayout_04.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_04.addWidget(self.RB_Intersection, 0, 0, 1, 1)
        self.gridLayout_04.addWidget(self.RB_Cut, 1, 0, 1, 1)
        self.gridLayout_04.addWidget(self.RB_Union, 2, 0, 1, 1)
        self.gridLayout_04.addWidget(self.RB_Xor, 3, 0, 1, 1)
        self.gridLayout_03.addWidget(self.GroupBox_Bool, 0, 0, 1, 1)
        ####
        self.gridLayout_05 = QtWidgets.QGridLayout(self.groupBox_Axis)
        self.gridLayout_05.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_05.addWidget(self.RB_Axis_X, 0, 0, 1, 1)
        self.gridLayout_05.addWidget(self.RB_Axis_Y, 1, 0, 1, 1)
        self.gridLayout_05.addWidget(self.RB_Axis_Z, 2, 0, 1, 1)
        self.gridLayout_05.addWidget(self.RB_Axis_D, 3, 0, 1, 1)
        self.gridLayout_03.addWidget(self.groupBox_Axis, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_02, 1, 0, 1, 2)
        ####
        self.gridLayout_06 = QtWidgets.QGridLayout(self.groupBox_03)
        self.gridLayout_06.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_06.addWidget(self.checkBox_01, 0, 0, 1, 1)
        self.gridLayout_06.addWidget(self.CB_Create_2D_Visible, 0, 1, 1, 1)
        self.gridLayout_06.addWidget(self.CB_Colorer, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_03, 2, 0, 1, 2)
        ####
        self.gridLayout_07 = QtWidgets.QGridLayout(self.groupBox_04)
        self.gridLayout_07.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_07.addWidget(self.PB_Create_2D, 0, 0, 1, 1)
        self.gridLayout_07.addWidget(self.PB_Create, 0, 1, 1, 1)
        self.gridLayout_07.addWidget(self.PB_Help, 1, 0, 1, 1)
        self.gridLayout_07.addWidget(self.PB_Quit, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_04, 3, 0, 1, 2)
        ####gridLayout####

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("FCWire To Volume")
        MainWindow.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint)        # PySide2 cette fonction met la fenetre en avant

        self.groupBox0.setTitle(_translate("MainWindow", "Ver : " + __version__ + " : " + __date__) + " rmu") #__title__ + " " +
        self.groupBox_01.setTitle(_translate("MainWindow", "Thickness Solide"))
        self.groupBox_02.setTitle(_translate("MainWindow", "Choice"))

        self.GroupBox_Bool.setTitle(_translate("MainWindow", "Boolean"))
        self.RB_Intersection.setText(_translate("MainWindow", "Intersection"))
        self.RB_Cut.setText(_translate("MainWindow", "Substraction"))
        self.RB_Union.setText(_translate("MainWindow", "Union"))
        self.RB_Xor.setText(_translate("MainWindow", "Xor"))

        self.groupBox_Axis.setTitle(_translate("MainWindow", "Axis"))
        self.RB_Axis_X.setText(_translate("MainWindow", "X Axis"))
        self.RB_Axis_X.setToolTip(_translate("MainWindow", "Plane YZ extrude direction X"))
        self.RB_Axis_Y.setText(_translate("MainWindow", "Y Axis"))
        self.RB_Axis_Y.setToolTip(_translate("MainWindow", "Plane XZ extrude direction Y"))
        self.RB_Axis_Z.setText(_translate("MainWindow", "Z Axis"))
        self.RB_Axis_Z.setToolTip(_translate("MainWindow", "Plane XY extrude direction Z"))
        self.RB_Axis_D.setText(_translate("MainWindow", "Direction"))
        self.RB_Axis_D.setToolTip(_translate("MainWindow", "Extrude direction (for later)"))

        self.groupBox_03.setTitle(_translate("MainWindow", "Option"))
        self.checkBox_01.setText(_translate("MainWindow", "Single object"))
        self.checkBox_01.setToolTip(_translate("MainWindow", "Check this checkBox"+"\n"+
                                               "for create single object"))
        self.CB_Create_2D_Visible.setText(_translate("MainWindow", "Hidden"))
        self.CB_Create_2D_Visible.setToolTip(_translate("MainWindow", "The object used are Hidden"))
        self.CB_Colorer.setText(_translate("MainWindow", "Color"))
        self.CB_Colorer.setToolTip(_translate("MainWindow", "If is checked the result is colored in red"))
        self.groupBox_04.setTitle(_translate("MainWindow", "Command"))
        self.PB_Create_2D.setText(_translate("MainWindow", "Create 2D"))
        self.PB_Create_2D.setToolTip(_translate("MainWindow", "This button Create 2D object (Draft.makeShape2DView)" + "\n" +
                                                "The projection is make in the Z axis" + "\n" +
                                                "The selection order is decisive for the desired result (Substraction)"))
        self.PB_Create.setText(_translate("MainWindow", "Create 3D"))
        self.PB_Create.setToolTip(_translate("MainWindow", "Create the object 3D" + "\n" +
                                             "The selection order is decisive for the desired result (Substraction)"))
        self.PB_Help.setText(_translate("MainWindow", "Help"))
        self.PB_Help.setToolTip(_translate("MainWindow", "Display the wiki page in the FreeCAD browser"))
        self.PB_Quit.setText(_translate("MainWindow", "Quit"))
        self.PB_Quit.setToolTip(_translate("MainWindow", "Quit Wire to volume, Salut"))


    def on_doubleSpinBox(self,value):
        self.thicknessValue = value
        self.doubleSpinBox.setStyleSheet("Base")
        self.PB_Create_2D.setStyleSheet("Base")
        self.PB_Create.setStyleSheet("Base")

    def on_checkBox_01(self):
        if self.checkBox_01.isChecked():
            self.checkBox_01.setIcon(QtGui.QIcon.fromTheme("part",QtGui.QIcon(":/icons/Tree_Part.svg")))
            self.checkBox_01.setText(u"Single object")
        else:
            self.checkBox_01.setIcon(QtGui.QIcon.fromTheme("part",QtGui.QIcon(":/icons/sel-instance.svg")))
            self.checkBox_01.setText(u"Objects")

    def on_CB_Create_2D_Visible(self):
        if self.CB_Create_2D_Visible.isChecked():
#            self.CB_Create_2D_Visible.setIcon(QtGui.QIcon.fromTheme("draft",QtGui.QIcon(":/icons/dagViewVisible.svg")))#
            self.CB_Create_2D_Visible.setIcon(QtGui.QIcon.fromTheme("part",QtGui.QIcon("")))
            self.CB_Create_2D_Visible.setText(u"Hidden")
        else:
            self.CB_Create_2D_Visible.setIcon(QtGui.QIcon.fromTheme("part",QtGui.QIcon(":/icons/dagViewVisible.svg")))
            self.CB_Create_2D_Visible.setText(u"Visible")

    def on_PB_Create_2D(self):
        global create2D
        global ui

        sel = FreeCADGui.Selection.getSelection()
        self.PB_Create_2D.setStyleSheet("Base")
        self.PB_Create.setStyleSheet("Base")
        if len(sel) < 2:
            create2D = 0
            self.PB_Create_2D.setStyleSheet("background-color: white;\n"
                                            "border:2px solid rgb(239, 41, 41);")  # bord white and red
        else:
            create2D = 1
            self.thicknessValue = 1.0
            self.doubleSpinBox.setValue(self.thicknessValue)
            self.RB_Axis_Z.setChecked(True)
            ui.on_PB_Create()
        
    def on_PB_Create(self):
        global create2D
        global doc

        selectionObjects = FreeCADGui.Selection.getSelection()
        self.doubleSpinBox.setStyleSheet("Base")
        self.PB_Create_2D.setStyleSheet("Base")
        self.PB_Create.setStyleSheet("Base")
        noface = 0
        ####
        if create2D > 0:
            lab00 = selectionObjects[0].Label
            lab01 = selectionObjects[1].Label
            boolChoice = ""
            if self.RB_Intersection.isChecked():
                boolChoice = "Comm"
            elif self.RB_Cut.isChecked():
                boolChoice = "Subs"
            elif self.RB_Union.isChecked():
                boolChoice = "Unio"
            elif self.RB_Xor.isChecked():
                boolChoice = "Diff"

            if self.checkBox_01.isChecked():
                None
            else:
                FCSpring = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroup","Wire2D_" + lab00 + "_" + boolChoice + "_" +lab01)
        ####
        try:
            selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0] # select one element SubObjects
            if str(selectedEdge)[1:5] == "Face":
                noface = 1
        except Exception:
            None

        selectionDuplicate  = []
        del selectionDuplicate[:]
        p  = []
        del p[:]
        
        try:
            ###########
            self.thicknessX = 0.0
            self.thicknessY = 0.0
            self.thicknessZ = 0.0
        #        self.thicknessD = 0.0
        
            if self.RB_Axis_X.isChecked():
                self.thicknessX = self.thicknessValue
            if self.RB_Axis_Y.isChecked():
                self.thicknessY = self.thicknessValue
            if self.RB_Axis_Z.isChecked():
                self.thicknessZ = self.thicknessValue
        #        if self.RB_Axis_D.isChecked():
        #            self.thicknessD = self.thicknessValue
            ###########
        
            if (len(selectionObjects) >= 2) and (noface == 0) and (self.thicknessX + self.thicknessY + self.thicknessZ != 0.0):
                for i in selectionObjects:            # duplicate object
                    Part.show(i.Shape.copy())
                    sD = doc.ActiveObject
                    sD.Label = i.Name
                    selectionDuplicate.append(sD)
            
                for i in (selectionDuplicate):        # extrude object
                    a = Draft.extrude(i,Base.Vector(self.thicknessX,self.thicknessY,self.thicknessZ))    # axis extrude X Y Z
                    a.Solid = True
                    p.append(a)
            
                if self.RB_Intersection.isChecked():
                    name = "Common_" + selectionDuplicate[0].Label         ## create Common_
                    tx = doc.addObject("Part::MultiCommon",name)
                    tx.Shapes = p
                    doc.recompute()
                    if self.checkBox_01.isChecked():
                        Part.show(tx.Shape)
                        singleO = App.ActiveDocument.ActiveObject
                        singleO.Label = name
                        doc.removeObject(tx.Name)
                        for i in range(len(selectionDuplicate)):
                            doc.removeObject(selectionDuplicate[i].Name)
                            doc.removeObject(p[i].Name)
                    if self.CB_Colorer.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (1.0,0.0,0.0)
                    App.Console.PrintMessage("RB_Intersection ")
        
                elif self.RB_Cut.isChecked():
                    name = str("Cut_" + selectionDuplicate[0].Label)       ## create Cut_
                    tx = doc.addObject("Part::Cut",name)
                    tx.Base = p[0]
                    tx.Tool = p[1]
                    doc.recompute()
                    if self.checkBox_01.isChecked():
                        Part.show(tx.Shape)
                        singleO = App.ActiveDocument.ActiveObject
                        singleO.Label = name
                        doc.removeObject(tx.Name)
                        for i in range(len(selectionDuplicate)):
                            doc.removeObject(selectionDuplicate[i].Name)
                            doc.removeObject(p[i].Name)
                    if self.CB_Colorer.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (1.0,0.0,0.0)
                    App.Console.PrintMessage("RB_Cut ")
            
                elif self.RB_Union.isChecked():
                    name = str("Fusion_" + selectionDuplicate[0].Label)    ## create Fusion_
                    tx = doc.addObject("Part::MultiFuse",name)
                    tx.Shapes = p
                    doc.recompute()
                    if self.checkBox_01.isChecked():
                        Part.show(tx.Shape)
                        singleO = App.ActiveDocument.ActiveObject
                        singleO.Label = name
                        doc.removeObject(tx.Name)
                        for i in range(len(selectionDuplicate)):
                            doc.removeObject(selectionDuplicate[i].Name)
                            doc.removeObject(p[i].Name)
                    if self.CB_Colorer.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (1.0,0.0,0.0)
                    App.Console.PrintMessage("RB_Union")
            
                elif self.RB_Xor.isChecked():
                    name = "CommonD_" + selectionDuplicate[0].Label        ##
                    commun = doc.addObject("Part::MultiCommon",name)
                    commun.Shapes = p
                    name = str("FusionD_" + selectionDuplicate[0].Label)   ##
                    fusion = doc.addObject("Part::MultiFuse",name)
                    fusion.Shapes = p
                    name = str("Difference_" + selectionDuplicate[0].Label)## create Difference_
                    difference = doc.addObject("Part::Cut",name)
                    difference.Base = fusion
                    difference.Tool = commun
                    doc.recompute()
                    if self.checkBox_01.isChecked():
                        Part.show(difference.Shape)
                        singleO = App.ActiveDocument.ActiveObject
                        singleO.Label = name
                        doc.removeObject(commun.Name)
                        doc.removeObject(fusion.Name)
                        doc.removeObject(difference.Name)
                        for i in range(len(selectionDuplicate)):
                            doc.removeObject(selectionDuplicate[i].Name)
                            doc.removeObject(p[i].Name)
                    if self.CB_Colorer.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (1.0,0.0,0.0)
                    App.Console.PrintMessage("RB_Xor ")
            
                doc.recompute()
                App.Console.PrintMessage(str(self.thicknessX)+" "+str(self.thicknessY)+" "+str(self.thicknessZ) + "\n")
            else:
                if (self.thicknessX + self.thicknessY + self.thicknessZ == 0.0):
                    App.Console.PrintError("Thickness = 0" + "\n")
                    self.doubleSpinBox.setStyleSheet("background-color: white;\n"
                                                     "border:2px solid rgb(239, 41, 41);")  # bord white and red
                else:
                    App.Console.PrintError("Not for Face" + "\n")
        
            #### section 2D
            if create2D > 0:
                objSolid = App.ActiveDocument.getObject(FreeCAD.ActiveDocument.ActiveObject.Name)
                objSolid.Label = "objSolid"
        
                object2D = Draft.makeShape2DView(objSolid)
                object2D.Label = "object2D"
                FreeCAD.ActiveDocument.recompute()
        
                Gui.Selection.clearSelection()
                Gui.Selection.addSelection(object2D)
        
                if self.CB_Create_2D_Visible.isChecked():
                    FreeCADGui.ActiveDocument.getObject(objSolid.Name).Visibility = False
                else:
                    FreeCADGui.ActiveDocument.getObject(objSolid.Name).ShapeColor = (1.0,0.0,0.0)
                    FreeCADGui.ActiveDocument.getObject(objSolid.Name).Transparency = 80
        
                if self.CB_Colorer.isChecked():
                    FreeCADGui.ActiveDocument.getObject(object2D.Name).LineColor = (1.0,0.0,0.0)
        
                ##### bon ordre pour effacer
                if self.checkBox_01.isChecked():
                    Part.show(object2D.Shape.copy())
                    if self.CB_Colorer.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.LineColor = (1.0,0.0,0.0)
                    App.ActiveDocument.ActiveObject.Label = ("Wire2D_" + lab00 + "_" + boolChoice + "_" +lab01)
                    doc.removeObject(object2D.Name)
                    doc.removeObject(objSolid.Name)
                else:
                    FCSpring.addObject(objSolid)
                    FCSpring.addObject(object2D)
        
            if self.CB_Create_2D_Visible.isChecked():
                FreeCADGui.ActiveDocument.getObject(selectionObjects[0].Name).Visibility = False
                FreeCADGui.ActiveDocument.getObject(selectionObjects[1].Name).Visibility = False
            #### section 2D
        
            create2D = 0
            FreeCAD.ActiveDocument.recompute()
        except Exception:
            print( "Wrong selection or operation")
            self.PB_Create.setStyleSheet("background-color: white;\n"
                                         "border:2px solid rgb(239, 41, 41);")  # bord white and red

    def on_PB_Help(self): # 
        WebGui.openBrowser("https://wiki.freecadweb.org/Macro_FCWire_To_Volume")
        App.Console.PrintMessage("https://wiki.freecadweb.org/Macro_FCWire_To_Volume" + "\n")

    def on_PB_Quit(self):                        # Quit
        App.Console.PrintMessage(str("Fin FCWire To Volume ")+"\n")
        self.window.hide()

    ####

doc = FreeCAD.ActiveDocument
if doc == None:
    doc = FreeCAD.newDocument()

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

}}

## Exemple


<center>

<File:Macro> FCWire To Volume 01.png\|Example 3D


</center>


<center>

Image:Macro FCWire To Volume 02.png\|Example 2D Image:Macro FCWire To Volume 03.png\|Common


</center>


<center>

Image:Macro FCWire To Volume 04.png\|Example 2D Image:Macro FCWire To Volume 05.png\|Union


</center>

## Lien

La discussion sur le forum [Bunch of issues/questions](http://forum.freecadweb.org/viewtopic.php?f=3&t=16570&start=50)

## Version

ver 02c: 11/04/2020 : corriger la faute de frappe \"Printmessage\" à \"PrintMessage\"

ver 02b: 10/04/2020 : ajout d\'icônes et bouton d\'aide

ver 02 : 07/04/2020 : conversion pour PySide2 Qt5 et mise en page, en ajoutant le fil 2D (contour)

ver 01 : 10/10/2016 :
