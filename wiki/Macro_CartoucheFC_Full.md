# Macro CartoucheFC Full
{{Macro
|Name=Macro_CartoucheFC_Full
|Icon=Macro_CartoucheFC_Full.png
|Description=This macro is a complete application, it allows to fill the cartridge of the drawing sheet with full editabletext (For [Drawing Workbench](Drawing_Workbench.md)).
|Author=Mario52
|Version=00.10
|Date=2017-02-15
|FCVersion=All version using Drawing Workbench
|Download=[https://www.freecadweb.org/wiki/images/6/68/Macro_CartoucheFC_Full.png ToolBar Icon]
}}

## Description

This macro is a complete application, it allows to fill simply all the fields of the cartridge

Choice in the page [Misc_templates_Full](Misc_templates_Full.md)

Here the order of filling in the line FreeCAD texteditable. The date and time fields are separated by a **\"space negative space\" \" - \"** and constitute a single line textedit.

<img alt="CartoucheFC_Full" src=images/Macro_CartoucheFC_Full_00.png  style="width:680px;">

## Usage

**PS: Some characters such as & \$ are not accepted (and possibly other special characters).**

If you have any questions or want to add a function, you can address you on the french forum [Remplir cartouche](http://forum.freecadweb.org/viewtopic.php?f=12&t=2049)

-   The window remains above other Windows, thereby controlling the cartridge without leaving the program.
-   Copy the code into a file named **Macro_CartoucheFC_Full.FCMacro** and place it in your usual macros directory.
-   After you have created your drawing sheet using the Drawing of FreeCAD module, run the macro **Macro_CartoucheFC_Full**.
-   At the opening, the program will register in memory all data already present in the cartridge of the sheet (if they are filled), all these data will be automatically returned to using the button ** Memo** and kept in memory until the closure of the programme.
-   First select your page to work
-   Date button ** D.** and time ** H.** displayed the date and time of the system.

  -The date format depends on the selected symbol **EU** or **US** which determines the regional format. Change does not happen automatically (for the case or you have entered a date manually) you must again click buttons dates if you change the symbol (check before printing).

-   Choice your format page
-   Button **Symbole EU** or US change the meaning of the symbol of projection \"Select your Symbol\" is displayed by default, and then the active symbol appears. Click on the button and check the leaf symbol, click a second time to modify the symbol.

  -The choice of this symbol, affects the date format **EU = dd/MM/yyyy** and **US = MM/dd/yyyy**.

  -**Attention**: this command does not pass through the button **Apply** and immediately changes the symbol to each presses on the key, always check if you have the appropriate symbol on your worksheet.

-   Button **Clean** Clears all fields in the cartridge. You can revert to the original data using the button **Memo**.
-   Button **Apply** saves all fields of the cartridge in the sheet. You can revert to the original data using the button **Memo** (except for the regional symbol that works in independent and is effective immediately).

## Code

The icon for you toolBar ![](images/Macro_CartoucheFC_Full.png )



**Macro_CartoucheFC_Full.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
***************************************************************************
*   Copyright (c) 2014 2016 2017 <mario52>                                *
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
#OS: Windows 10
#Word size of OS: 64-bit
#Word size of FreeCAD: 64-bit
#Version: 0.16.6706 (Git)
#Build type: Release
#Branch: releases/FreeCAD-0-16
#Hash: f86a4e411ff7848dea98d7242f43b7774bee8fa0
#Python version: 2.7.8
#Qt version: 4.8.7
#Coin version: 4.0.0a
#OCC version: 6.8.0.oce-0.17

__title__   = "Macro_CartoucheFC_Full"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__Wiki__    = "http://www.freecadweb.org/wiki/Macro_CartoucheFC_Full"
__version__ = "00.10"
__date__    = "15/02/2017"

__Requires__ = ("all version and freecad " +
" DESIGNED_BY, CREATION_DATE, CHECKED_BY, CHECK_DATE, SIZE, SCALE, WEIGHT, DRAWING_NUMBER, SHEET, " +
" TITLE, DESCRIPTION, COMPANY, COPYRIGHT, Note_A, Note_B, Note_C, Note_D, Note_E, Note_F, Note_G, Note_H, Note_I" )
__Template__ = " A3_Landscape_xx_FULL.svg, A3_Portrait_xx_FULL, A4_Landscape_xx_FULL.svg, A4_Portrait_xx_FULL"
__Template_Link__ = "http://www.freecadweb.org/wiki/index.php?title=Misc_templates_Full"

import PySide
from PySide import QtCore, QtGui

import Draft, Part, FreeCAD, math, PartGui, FreeCADGui
from math import sqrt, pi, sin, cos, asin
from FreeCAD import Base

def utf8(unio):
    return unicode(unio).encode('UTF8')

global path
#path = FreeCAD.ConfigGet("AppHomePath")
path = FreeCAD.ConfigGet("UserAppData")

global PageActive      ; PageActive  = "Select your page" # essais 
#global PageActive      ; PageActive  = "Page" # page active
global DESIGNED_BY     ; DESIGNED_BY = ""     # lineEdit01 DESIGNED_BY
global MDESIGNED_BY    ; MDESIGNED_BY = ""    # 
global CREATION_DATE   ; CREATION_DATE = ""   # lineEdit02 CREATION_DATE date
global MCREATION_DATE  ; MCREATION_DATE = ""  # 
global CREA_DATE       ; CREA_DATE = ""       # lineEdit02h date
global MCREA_DATE      ; MCREA_DATE = ""      # 
global CREA_TIME       ; CREA_TIME = ""       # lineEdit02h heure
global MCREA_TIME      ; MCREA_TIME = ""      # 
global CHECKED_BY      ; CHECKED_BY = ""      # lineEdit03
global MCHECKED_BY     ; MCHECKED_BY = ""     # 
global CHECK_DATE      ; CHECK_DATE = ""      # lineEdit04 date
global MCHECK_DATE     ; MCHECK_DATE = ""     # 
global CHEC_DATE       ; CHEC_DATE = ""       # lineEdit04 date
global MCHEC_DATE      ; MCHEC_DATE = ""      # 
global CHEC_TIME       ; CHEC_TIME = ""       # lineEdit04h heure
global MCHEC_TIME      ; MCHEC_TIME = ""      # 
global SIZE            ; SIZE = ""            # lineEdit05
global MSIZE           ; MSIZE = ""           # 
global SCALE           ; SCALE =  ""          # lineEdit06
global MSCALE          ; MSCALE =  ""         # 
global WEIGHT          ; WEIGHT =  ""         # lineEdit07
global MWEIGHT         ; MWEIGHT =  ""        # 
global DRAWING_NUMBER  ; DRAWING_NUMBER = ""  # lineEdit08
global MDRAWING_NUMBER ; MDRAWING_NUMBER = "" # 
global SHEET           ; SHEET =  ""          # lineEdit09
global MSHEET          ; MSHEET =  ""         # 
global TITLE           ; TITLE =  ""          # textEdit_01
global MTITLE          ; MTITLE =  ""         # 
global DESCRIPTION     ; DESCRIPTION =  ""    # textEdit_02
global MDESCRIPTION    ; MDESCRIPTION = ""    # 
global COMPANY         ; COMPANY = ""         # textEdit_02b
global MCOMPANY        ; MCOMPANY = ""        # 
global COPYRIGHT       ; COPYRIGHT = ""       # lineEdit_20
global MCOPYRIGHT      ; MCOPYRIGHT = ""      # 
global Note_A          ; Note_A = ""          # lineEdit_10
global MNote_A         ; MNote_A = ""         # 
global Note_B          ; Note_B = ""          # lineEdit_11
global MNote_B         ; MNote_B = ""         # 
global Note_C          ; Note_C = ""          # lineEdit_12
global MNote_C         ; MNote_C = ""         # 
global Note_D          ; Note_D = ""          # lineEdit_13
global MNote_D         ; MNote_D = ""         # 
global Note_E          ; Note_E = ""          # lineEdit_14
global MNote_E         ; MNote_E = ""         # 
global Note_F          ; Note_F = ""          # lineEdit_15
global MNote_F         ; MNote_F = ""         # 
global Note_G          ; Note_G = ""          # lineEdit_16
global MNote_G         ; MNote_G = ""         # 
global Note_H          ; Note_H = ""          # lineEdit_17
global MNote_H         ; MNote_H = ""         # 
global Note_I          ; Note_I = ""          # lineEdit_18
global MNote_I         ; MNote_I = ""         # 

global SymbolSwitch    ; SymbolSwitch = 1     # 0=US 1=EU
global ui              ; ui     = ""

def heure():
    return QtCore.QTime().currentTime().toString('hh:mm:ss')
def dateEu():
    return QtCore.QDate().currentDate().toString('dd/MM/yyyy') # forme euro
def dateUK():
    return QtCore.QDate().currentDate().toString('yyyy/MM/dd') # forme UK
def dateUs():
    return QtCore.QDate().currentDate().toString('MM/dd/yyyy') # forme US
def dateComp():
    return QtCore.QDate().currentDate().toString('dddd d MMMM yyyy') # Retourne "dimanche 20 Juillet 77"

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

def errorDialog(msg):
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical,u"Error Message",msg)
    diag.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint) # cette fonction met la fenetre en avant
    diag.exec_()

def symbol_EU(depx, depy, scale):    #symbol_EU =O
    global PageActive
    global ui

    try:
        page = App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0]
    except Exception:
        page = App.activeDocument().getObjectsByLabel(PageActive)[0]if len(str(page)) != 2:
        comP   = []
        nameL  = []
        if "Page" in (page.Name):
            for ii in (page.Group):
                if ((ii.Label) == "Symbol_EU") or ((ii.Label) == "Symbol_US") :
                    App.activeDocument().removeObject(ii.Name)

        points=[FreeCAD.Vector(-7.5,0.0,0.0),FreeCAD.Vector(20.0,0.0,0.0)]
        i = Draft.makeWire(points,closed=False,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        points=[FreeCAD.Vector(12.5,7.5,0.0),FreeCAD.Vector(12.5,-7.5,0.0)]
        i = Draft.makeWire(points,closed=False,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        points=[FreeCAD.Vector(-5,2.5,0.0),FreeCAD.Vector(5.0,5.0,0.0),FreeCAD.Vector(5.0,-5.0,0.0),FreeCAD.Vector(-5.0,-2.5,0.0)]
        i = Draft.makeWire(points,closed=True,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        pl=FreeCAD.Placement()
        pl.Rotation.Q=(0.0,-0.0,-0.0,1.0)
        pl.Base=FreeCAD.Vector(12.5,-0.0,0.0)
        i = Draft.makeCircle(radius=2.5,placement=pl,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        i = Draft.makeCircle(radius=5.0,placement=pl,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)    comp = Part.makeCompound(comP)
        Part.show(comp)
        App.ActiveDocument.ActiveObject.Label = "Symbol_EU"    obj = FreeCAD.ActiveDocument.ActiveObject
        obj.ViewObject.LineColor = (0.0,0.0,0.0)
        obj.ViewObject.Visibility = False
        
        obj2 = Draft.makeDrawingView(obj, page) 
        obj2.X = depx
        obj2.Y = depy
        obj2.Scale = scale #0.8    # A3
        obj2.Label = "Symbol_EU"    for i in nameL: App.activeDocument().removeObject(i)    App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0].addObject(obj)
        App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0].addObject(obj2)
        App.ActiveDocument.recompute()
    else:
        ui.pushButton05.setStyleSheet("background-color: red")       # This function gives a color button
        FreeCAD.Console.PrintError("Error selected page [ " + PageActive + " ]" + "\n")

def symbol_US(depx, depy, scale):    #symbol_US O=
    global PageActive
    global ui

    try:
        page = App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0]
    except Exception:
        page = App.activeDocument().getObjectsByLabel(PageActive)[0]

    if len(str(page)) != 2:
        comP   = []
        nameL  = []    if "Page" in (page.Name):
            for ii in (page.Group):
                if ((ii.Label) == "Symbol_EU") or ((ii.Label) == "Symbol_US") :
                    App.activeDocument().removeObject(ii.Name)

        points=[FreeCAD.Vector(-7.5,0.0,0.0),FreeCAD.Vector(20.0,0.0,0.0)]
        i = Draft.makeWire(points,closed=False,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        points=[FreeCAD.Vector(0.0,7.5,0.0),FreeCAD.Vector(0.0,-7.5,0.0)]
        i = Draft.makeWire(points,closed=False,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        points=[FreeCAD.Vector(7.5,2.5,0.0),FreeCAD.Vector(17.5,5.0,0.0),FreeCAD.Vector(17.5,-5.0,0.0),FreeCAD.Vector(7.5,-2.5,0.0)]
        i = Draft.makeWire(points,closed=True,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        pl=FreeCAD.Placement()
        pl.Rotation.Q=(0.0,-0.0,-0.0,1.0)
        pl.Base=FreeCAD.Vector(0.0,-0.0,0.0)
        i = Draft.makeCircle(radius=2.5,placement=pl,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)
        i = Draft.makeCircle(radius=5.0,placement=pl,face=False,support=None)
        comP.append(i.Shape)
        nameL.append(i.Name)    comp = Part.makeCompound(comP)
        Part.show(comp)
        App.ActiveDocument.ActiveObject.Label = "Symbol_US"    obj = FreeCAD.ActiveDocument.ActiveObject
        obj.ViewObject.LineColor = (0.0,0.0,0.0)
        obj.ViewObject.Visibility = False    obj2 = Draft.makeDrawingView(obj, page) 
        obj2.X = depx
        obj2.Y = depy
        obj2.Scale = scale #0.8    # A3
        obj2.Label = "Symbol_US"    for i in nameL: App.activeDocument().removeObject(i)    App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0].addObject(obj)
        App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0].addObject(obj2)
        App.ActiveDocument.recompute()
    else:
        ui.pushButton05.setStyleSheet("background-color: red")       # This function gives a color button
        FreeCAD.Console.PrintError("Error selected page [ " + PageActive + " ]" + "\n")

def memoEntree():
    global MDESIGNED_BY, MCREATION_DATE, MCREA_DATE  , MCREA_TIME, MCHECKED_BY, MCHECK_DATE
    global MCHEC_DATE  , MCHEC_TIME    , MSIZE       , MSCALE    , MWEIGHT    ,MDRAWING_NUMBER
    global MSHEET      , MTITLE        , MDESCRIPTION, MCOMPANY  , MCOPYRIGHT
    global MNote_A, MNote_B, MNote_C, MNote_D, MNote_E, MNote_F, MNote_G, MNote_H, MNote_I
    global PageActive

    try:
        page = App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0].Name
    except Exception:
        page = App.activeDocument().getObjectsByLabel(PageActive)[0]

    try:
        MDESIGNED_BY   = App.activeDocument().getObject(page).EditableTexts[0]  # lineEdit01 DESIGNED_BY
        MCREATION_DATE = App.activeDocument().getObject(page).EditableTexts[1]  # lineEdit02 CREATION_DATE date

        MCREA_DATE = MCREA_TIME = MCHEC_DATE = MCHEC_TIME = ""

        try:
            MCREA_DATE = MCREATION_DATE.split(" - ")[0]                         # lineEdit02h date
        except:
            MCREA_DATE = MCREATION_DATE
        try:
            MCREA_TIME = MCREATION_DATE.split(" - ")[1]                         # lineEdit02h heure
        except: None    

        MCHECKED_BY = App.activeDocument().getObject(page).EditableTexts[2]     # lineEdit03
        MCHECK_DATE = App.activeDocument().getObject(page).EditableTexts[3]     # lineEdit04 date

        try:
            MCHEC_DATE = MCHECK_DATE.split(" - ")[0]                            # lineEdit04 date
        except:
            MCHEC_DATE = MCHECK_DATE
        try:
            MCHEC_TIME = MCHECK_DATE.split(" - ")[1]                            # lineEdit04h heure
        except: None    

        MSIZE = App.activeDocument().getObject(page).EditableTexts[4]           # lineEdit05
        MSCALE = App.activeDocument().getObject(page).EditableTexts[5]          # lineEdit06
        MWEIGHT = App.activeDocument().getObject(page).EditableTexts[6]         # lineEdit07
        MDRAWING_NUMBER = App.activeDocument().getObject(page).EditableTexts[7] # lineEdit08
        MSHEET = App.activeDocument().getObject(page).EditableTexts[8]          # lineEdit09
        MTITLE = App.activeDocument().getObject(page).EditableTexts[9]          # textEdit_01

        try:
            MDESCRIPTION = App.activeDocument().getObject(page).EditableTexts[10]   # textEdit_02
            MCOMPANY = App.activeDocument().getObject(page).EditableTexts[11]       # textEdit_02b
            MCOPYRIGHT = App.activeDocument().getObject(page).EditableTexts[12]     # lineEdit_20
            MNote_A = App.activeDocument().getObject(page).EditableTexts[13]        # lineEdit_10
            MNote_B = App.activeDocument().getObject(page).EditableTexts[14]        # lineEdit_11
            MNote_C = App.activeDocument().getObject(page).EditableTexts[15]        # lineEdit_12
            MNote_D = App.activeDocument().getObject(page).EditableTexts[16]        # lineEdit_13
            MNote_E = App.activeDocument().getObject(page).EditableTexts[17]        # lineEdit_14
            MNote_F = App.activeDocument().getObject(page).EditableTexts[18]        # lineEdit_15
            MNote_G = App.activeDocument().getObject(page).EditableTexts[19]        # lineEdit_16
            MNote_H = App.activeDocument().getObject(page).EditableTexts[20]        # lineEdit_17
            MNote_I = App.activeDocument().getObject(page).EditableTexts[21]        # lineEdit_18
        except Exception:
            App.Console.PrintError("Erreur cartouche level DESCRIPTION (Missing field)"+"\n"
                        "You may be using an inadequate template. Try with this template"+"\n")
            App.Console.PrintMessage("http://www.freecadweb.org/wiki/index.php?title=Misc_templates_Full"+"\n\n")
            App.Console.PrintError("Or for the original FreeCAD template use this macro"+"\n")
            App.Console.PrintMessage("http://www.freecadweb.org/wiki/index.php?title=Macro_CartoucheFC"+"\n")        errorDialog("Erreur cartouche level DESCRIPTION (Missing field)"+"\n"
                        "You may be using an inadequate template. Try with this template"+"\n"
                        "http://www.freecadweb.org/wiki/index.php?title=Misc_templates_Full"+"\n\n"
                        "Or for the original FreeCAD template use this macro"+"\n"
                        "http://www.freecadweb.org/wiki/index.php?title=Macro_CartoucheFC"+"\n\n")

    except:
        errorDialog("Erreur cartouche")

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        global path
        global PageActive
        self.window = MainWindow

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(810, 400)
        MainWindow.setMaximumSize(QtCore.QSize(810, 400))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

#        self.pushButton01 = QtGui.QPushButton(self.centralWidget)
#        self.pushButton01.setGeometry(QtCore.QRect(115, 360, 93, 28))
#        self.pushButton01.setObjectName(_fromUtf8("pushButton01"))
#        self.pushButton01.clicked.connect(self.on_pushButton01_clicked) #connection pushButton01

        self.pushButton02 = QtGui.QPushButton(self.centralWidget)
        self.pushButton02.setGeometry(QtCore.QRect(225, 360, 93, 28))
        self.pushButton02.setObjectName(_fromUtf8("pushButton02"))
        self.pushButton02.clicked.connect(self.on_pushButton02_clicked) #connection pushButton02

        self.pushButton03 = QtGui.QPushButton(self.centralWidget)
        self.pushButton03.setGeometry(QtCore.QRect(335, 360, 93, 28))
        self.pushButton03.setToolTip("The memo button work only with the first Page")
        self.pushButton03.setObjectName(_fromUtf8("pushButton03"))
        self.pushButton03.clicked.connect(self.on_pushButton03_clicked) #connection pushButton03

        self.pushButton04 = QtGui.QPushButton(self.centralWidget)
        self.pushButton04.setGeometry(QtCore.QRect(445, 360, 93, 28))
        self.pushButton04.setObjectName(_fromUtf8("pushButton04"))
        self.pushButton04.clicked.connect(self.on_pushButton04_clicked) #connection pushButton04

        self.pushButton05 = QtGui.QPushButton(self.centralWidget)
        self.pushButton05.setGeometry(QtCore.QRect(555, 360, 93, 28))
#        self.pushButton05.setStyleSheet("background-color: red")       # This function gives a color button
        self.pushButton05.setObjectName(_fromUtf8("pushButton05"))
        self.pushButton05.clicked.connect(self.on_pushButton05_clicked) #connection pushButton05

        #####
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 159, 190, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(115, 5, 61, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        ############### font and color Label
        font = QtGui.QFont()
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color : #ff0000")
        ############### font and color
        self.label_20.setVisible(False)

        self.radioButton_0 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_0.setGeometry(QtCore.QRect(95, 1, 91, 17))
        self.radioButton_0.setChecked(True)
        self.radioButton_0.setEnabled(False)
        self.radioButton_0.setVisible(False)
        self.radioButton_0.setObjectName(_fromUtf8("radioButton_0"))

        self.radioButton_1 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(95, 20, 91, 17))
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.radioButton_1.clicked.connect(self.on_radioButton_A3_clicked)# connect radioButton_A3

        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(95, 39, 91, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_2.clicked.connect(self.on_radioButton_A3_clicked)# connect radioButton_A3

        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(95, 58, 91, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_3.clicked.connect(self.on_radioButton_A4_clicked)# connect radioButton_A4

        self.radioButton_4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(95, 76, 91, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_4.clicked.connect(self.on_radioButton_A4_clicked)# connect radioButton_A4

        self.lineEdit_05 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_05.setGeometry(QtCore.QRect(10, 16, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_05.setFont(font)
        self.lineEdit_05.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_05.setObjectName(_fromUtf8("lineEdit_05"))
        self.lineEdit_05.setText(SIZE)

        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(10, 58, 74, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.radioButton_EU = QtGui.QRadioButton(self.frame)
        self.radioButton_EU.setGeometry(QtCore.QRect(0, 1, 41, 17))
        self.radioButton_EU.setChecked(True)
        self.radioButton_EU.setObjectName(_fromUtf8("radioButton_EU"))
        self.radioButton_EU.clicked.connect(self.on_radioButton_EU_clicked) #connection radioButton_EU

        self.radioButton_US = QtGui.QRadioButton(self.frame)
        self.radioButton_US.setGeometry(QtCore.QRect(37, 1, 41, 17))
        self.radioButton_US.setObjectName(_fromUtf8("radioButton_US"))
        self.radioButton_US.clicked.connect(self.on_radioButton_US_clicked) #connection radioButton_US

        self.pushButton10 = QtGui.QPushButton(self.frame)
        self.pushButton10.setGeometry(QtCore.QRect(0, 18, 75, 23))
        self.pushButton10.setToolTip("Create the symbol EU or US"+"\n"
                                     "This button is Independent of the Write button"+"\n"
                                     "If you desire modify the symbol in the cartouche,"+"\n"
                                     "delete the inadequate symbol manualy.")
        self.pushButton10.setEnabled(False)
        self.pushButton10.setObjectName(_fromUtf8("pushButton10"))
        self.pushButton10.clicked.connect(self.on_pushButton10_clicked)     #connection pushButton10

        #####

        self.pushButton06 = QtGui.QPushButton(self.centralWidget)
        self.pushButton06.setGeometry(QtCore.QRect(170, 57, 20, 20))
        self.pushButton06.setObjectName(_fromUtf8("pushButton06"))
        self.pushButton06.clicked.connect(self.on_pushButton06_clicked) #connection pushButton06

        self.pushButton07 = QtGui.QPushButton(self.centralWidget)
        self.pushButton07.setGeometry(QtCore.QRect(190, 57, 20, 20))
        self.pushButton07.setObjectName(_fromUtf8("pushButton07"))
        self.pushButton07.clicked.connect(self.on_pushButton07_clicked) #connection pushButton07

        self.pushButton08 = QtGui.QPushButton(self.centralWidget)
        self.pushButton08.setGeometry(QtCore.QRect(170, 137, 20, 20))
        self.pushButton08.setObjectName(_fromUtf8("pushButton08"))
        self.pushButton08.clicked.connect(self.on_pushButton08_clicked) #connection pushButton08

        self.pushButton09 = QtGui.QPushButton(self.centralWidget)
        self.pushButton09.setGeometry(QtCore.QRect(190, 137, 20, 20))
        self.pushButton09.setObjectName(_fromUtf8("pushButton09"))
        self.pushButton09.clicked.connect(self.on_pushButton09_clicked) #connection pushButton09

        self.lineEdit_01 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_01.setGeometry(QtCore.QRect(20, 20, 190, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit_01.setFont(font)
        self.lineEdit_01.setObjectName(_fromUtf8("lineEdit_01"))
        self.lineEdit_01.setText(DESIGNED_BY)

        self.lineEdit_02 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_02.setGeometry(QtCore.QRect(20, 60, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit_02.setFont(font)
        self.lineEdit_02.setObjectName(_fromUtf8("lineEdit_02"))
        self.lineEdit_02.setText(CREA_DATE)

        self.lineEdit_02h = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_02h.setGeometry(QtCore.QRect(98, 60, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit_02h.setFont(font)
        self.lineEdit_02h.setObjectName(_fromUtf8("lineEdit_02h"))
        self.lineEdit_02h.setText(CREA_TIME)

        self.lineEdit_03 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_03.setGeometry(QtCore.QRect(20, 100, 190, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit_03.setFont(font)
        self.lineEdit_03.setObjectName(_fromUtf8("lineEdit_03"))
        self.lineEdit_03.setText(CHECKED_BY)

        self.lineEdit_04 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_04.setGeometry(QtCore.QRect(20, 140, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit_04.setFont(font)
        self.lineEdit_04.setObjectName(_fromUtf8("lineEdit_04"))
        self.lineEdit_04.setText(CHEC_DATE)

        self.lineEdit_04h = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_04h.setGeometry(QtCore.QRect(98, 140, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit_04h.setFont(font)
        self.lineEdit_04h.setObjectName(_fromUtf8("lineEdit_04h"))
        self.lineEdit_04h.setText(CHEC_TIME)

        self.lineEdit_06 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_06.setGeometry(QtCore.QRect(20, 280, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_06.setFont(font)
        self.lineEdit_06.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_06.setObjectName(_fromUtf8("lineEdit_06"))
        self.lineEdit_06.setText(SCALE)

        self.lineEdit_07 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_07.setGeometry(QtCore.QRect(100, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_07.setFont(font)
        self.lineEdit_07.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_07.setObjectName(_fromUtf8("lineEdit_07"))
        self.lineEdit_07.setText(WEIGHT)

        self.lineEdit_08 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_08.setGeometry(QtCore.QRect(220, 280, 341, 41))
        self.lineEdit_08.setObjectName(_fromUtf8("lineEdit_08"))
        self.lineEdit_08.setText(DRAWING_NUMBER)

        self.lineEdit_09 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_09.setGeometry(QtCore.QRect(570, 280, 81, 41))
        self.lineEdit_09.setObjectName(_fromUtf8("lineEdit_09"))
        self.lineEdit_09.setText(SHEET)

        self.lineEdit_20 = QtGui.QLineEdit(self.centralWidget) # Copyright
        self.lineEdit_20.setGeometry(QtCore.QRect(20, 330, 771, 22))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.lineEdit_20.setText(COPYRIGHT)

        self.lineEdit_10 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(690, 290, 101, 30))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_10.setText(Note_A)

        self.lineEdit_11 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(690, 260, 101, 30))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_11.setText(Note_B)

        self.lineEdit_12 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(690, 230, 101, 30))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_12.setText(Note_C)

        self.lineEdit_13 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(690, 200, 101, 30))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_13.setText(Note_D)

        self.lineEdit_14 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(690, 170, 101, 30))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_14.setText(Note_E)

        self.lineEdit_15 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(690, 140, 101, 30))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_15.setText(Note_F)

        self.lineEdit_16 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(690, 110, 101, 30))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_16.setText(Note_G)

        self.lineEdit_17 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(690, 80, 101, 30))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_17.setText(Note_H)

        self.lineEdit_18 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(690, 50, 101, 30))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_18.setText(Note_I)
##
        self.lineEdit_page = QtGui.QLineEdit(self.centralWidget)         # nom de page
        self.lineEdit_page.setGeometry(QtCore.QRect(20, 365, 181, 20))
        self.lineEdit_page.setToolTip("Name page to work"+"\n"
                                      "The name of the first page is always named 'Page'"
                                      "Select the new page in the Combo view")
        self.lineEdit_page.setObjectName(_fromUtf8("lineEdit_page"))
        self.lineEdit_page.setEnabled(False)
        self.lineEdit_page.setStyleSheet("color: red")
        self.lineEdit_page.setText(PageActive)
        self.lineEdit_page.textChanged.connect(self.on_lineEdit_page_Pressed) # 

        self.label_01T = QtGui.QLabel(self.centralWidget)
        self.label_01T.setGeometry(QtCore.QRect(220, 0, 91, 16))
        self.label_01T.setObjectName(_fromUtf8("label_01T"))

        self.textEdit_01 = QtGui.QTextEdit(self.centralWidget)            # Title
        self.textEdit_01.setGeometry(QtCore.QRect(220, 20, 431,55 ))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_01.setFont(font)
        self.textEdit_01.setObjectName(_fromUtf8("textEdit_01"))
        self.textEdit_01.setText(TITLE)

        self.label_02T = QtGui.QLabel(self.centralWidget)
        self.label_02T.setGeometry(QtCore.QRect(220, 80, 101, 16))
        self.label_02T.setObjectName(_fromUtf8("label_02T"))

        self.textEdit_02 = QtGui.QTextEdit(self.centralWidget)            # DESCRIPTION
        self.textEdit_02.setGeometry(QtCore.QRect(220, 100, 431, 55))
        self.textEdit_02.setObjectName(_fromUtf8("textEdit_02"))
        self.textEdit_02.setText(DESCRIPTION)

        self.label_02bT = QtGui.QLabel(self.centralWidget)
        self.label_02bT.setGeometry(QtCore.QRect(220, 160, 90, 16))
        self.label_02bT.setObjectName(_fromUtf8("label_02bT"))

        self.textEdit_02b = QtGui.QTextEdit(self.centralWidget)            # COMPANY
        self.textEdit_02b.setGeometry(QtCore.QRect(220, 180, 340, 60))
        self.textEdit_02b.setObjectName(_fromUtf8("textEdit_02b"))
        self.textEdit_02b.setText(COMPANY)

        self.label_01 = QtGui.QLabel(self.centralWidget)
        self.label_01.setGeometry(QtCore.QRect(20, 0, 91, 16))
        self.label_01.setObjectName(_fromUtf8("label_01"))

        self.label_02 = QtGui.QLabel(self.centralWidget)
        self.label_02.setGeometry(QtCore.QRect(20, 40, 53, 16))
        self.label_02.setObjectName(_fromUtf8("label_02"))

        self.label_03 = QtGui.QLabel(self.centralWidget)
        self.label_03.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.label_03.setObjectName(_fromUtf8("label_03"))

        self.label_04 = QtGui.QLabel(self.centralWidget)
        self.label_04.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_04.setObjectName(_fromUtf8("label_04"))

        self.label_06 = QtGui.QLabel(self.centralWidget)
        self.label_06.setGeometry(QtCore.QRect(20, 260, 53, 16))
        self.label_06.setObjectName(_fromUtf8("label_06"))

        self.label_07 = QtGui.QLabel(self.centralWidget)
        self.label_07.setGeometry(QtCore.QRect(100, 260, 101, 16))
        self.label_07.setObjectName(_fromUtf8("label_07"))

        self.label_08 = QtGui.QLabel(self.centralWidget)
        self.label_08.setGeometry(QtCore.QRect(220, 260, 121, 16))
        self.label_08.setObjectName(_fromUtf8("label_08"))

        self.label_09 = QtGui.QLabel(self.centralWidget)
        self.label_09.setGeometry(QtCore.QRect(570, 260, 53, 16))
        self.label_09.setObjectName(_fromUtf8("label_09"))

        self.label_10 = QtGui.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(670, 290, 16, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.label_11 = QtGui.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(670, 260, 16, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.label_12 = QtGui.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(670, 230, 16, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.label_13 = QtGui.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(670, 200, 18, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))

        self.label_14 = QtGui.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(670, 170, 15, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.label_15 = QtGui.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(670, 140, 14, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))

        self.label_16 = QtGui.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(670, 110, 18, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))

        self.label_17 = QtGui.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(670, 80, 18, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))

        self.label_18 = QtGui.QLabel(self.centralWidget)
        self.label_18.setGeometry(QtCore.QRect(670, 50, 10, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))

        self.label_19 = QtGui.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(720, 15, 100, 33))
        self.label_19.setObjectName(_fromUtf8("label_19"))

        self.label_page = QtGui.QLabel(self.centralWidget)
        self.label_page.setGeometry(QtCore.QRect(20, 350, 181, 16))
        self.label_page.setObjectName(_fromUtf8("label_page"))

        self.label_Version = QtGui.QLabel(self.centralWidget)        # Version
        self.label_Version.setGeometry(QtCore.QRect(685, 383, 121, 20))
        self.label_Version.setObjectName(_fromUtf8("label_Version"))

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint) # cette fonction met la fenetre en avant
        MainWindow.setWindowTitle("Cartouche (Full)")
#        self.pushButton01.setText("Position")
        self.pushButton02.setText("Quit") #Quitter
        self.pushButton03.setText("Memo")
        self.pushButton04.setText("Clean")#Nettoyer
        self.pushButton05.setText("Write")#Appliquer
        self.pushButton06.setText("D.")
        self.pushButton07.setText("H.")
        self.pushButton08.setText("D.")
        self.pushButton09.setText("H.")
        self.pushButton10.setText("Create Symb.")

        self.label_01.setText("Designed by :")
        self.label_02.setText("Date :")
        self.label_03.setText("Checked by :")
        self.label_04.setText("Date :")
        self.label_06.setText("Scale :")
        self.label_07.setText("Weight (Kg) :")
        self.label_08.setText("Drawing number :")
        self.label_01T.setText("Title :")
        self.label_02T.setText("Description :")
        self.label_02bT.setText("Company :")
        self.label_09.setText("Sheet :")

        self.label_10.setText("A")
        self.label_11.setText("B")
        self.label_12.setText("C")
        self.label_13.setText("D")
        self.label_14.setText("E")
        self.label_15.setText("F")
        self.label_16.setText("G")
        self.label_17.setText("H")
        self.label_18.setText("I")
        self.label_19.setText("Notes")
        self.label_20.setText("Warning")
        self.label_page.setText("Name page to work")
        self.label_Version.setText("Ver: 00.10 15/02/2017")        # Version
        self.groupBox.setTitle("Size :")
        self.radioButton_1.setText("A3 Landscape")
        self.radioButton_2.setText("A3 Portrait")
        self.radioButton_3.setText("A4 Landscape")
        self.radioButton_4.setText("A4 Portrait")
        self.radioButton_EU.setText("EU")
        self.radioButton_US.setText("US")
        self.lineEdit_05.setText("?")

#______________________________________________________________________________________
    # Radio Boutons
    def on_radioButton_A3_clicked(self):  # connect radioButton_A3
        self.label_20.setVisible(False)
        self.pushButton10.setEnabled(True)
        self.lineEdit_05.setText("A3")
        self.pushButton10.setStyleSheet("color: QPalette.Base")           # origin system

    def on_radioButton_A4_clicked(self):  # connect radioButton_A4
        self.label_20.setVisible(False)
        self.pushButton10.setEnabled(True)
        self.lineEdit_05.setText("A4")
        self.pushButton10.setStyleSheet("color: QPalette.Base")           # origin system
    # Radio Boutons

    def on_radioButton_EU_clicked(self):    # Bouton /Symbole EU
        global SymbolSwitch
        SymbolSwitch = 1

    def on_radioButton_US_clicked(self):    # Bouton /Symbole US
        global SymbolSwitch
        SymbolSwitch = 0

    def on_pushButton10_clicked(self):      # Bouton /Symbole EU US disposition dans le cartouche
        global SymbolSwitch
        global PageActive
        self.label_20.setVisible(False)

        if self.radioButton_0.isChecked():
            self.label_20.setVisible(True)
            self.pushButton10.setEnabled(False)
            self.pushButton10.setStyleSheet("color: red")
            self.lineEdit_page.setStyleSheet("color: red")
            FreeCAD.Console.PrintError("Select one format A3 or A4 for the Symbole" + "\n")
        else:
            self.pushButton10.setEnabled(True)
            self.pushButton10.setStyleSheet("background-color: #FF5B2B")
            self.pushButton10.setText("Wait.")
            FreeCADGui.updateGui()                # rafraichi l'ecran
            if SymbolSwitch == 1:
                if self.radioButton_1.isChecked():
                    symbol_EU(247.5, 263.5, 0.8)  # A3 Landscape
                elif self.radioButton_2.isChecked():
                    symbol_EU(124.55, 386.3, 0.8) # A3 Portrait
                elif self.radioButton_3.isChecked():
                    symbol_EU(158.7, 181.35, 0.6) # A4 Landscape
                elif self.radioButton_4.isChecked():
                    symbol_EU(71.9, 269.0, 0.6)   # A4 Portrait
            else:
                if self.radioButton_1.isChecked():
                    symbol_US(247.5, 263.5, 0.8)  # A3 Landscape
                elif self.radioButton_2.isChecked():
                    symbol_US(124.55, 386.3, 0.8) # A3 Portrait
                elif self.radioButton_3.isChecked():
                    symbol_US(158.7, 181.35, 0.6) # A4 Landscape
                elif self.radioButton_4.isChecked():
                    symbol_US(71.9, 269.0, 0.6)   # A4 Portrait
            self.pushButton10.setStyleSheet("color: QPalette.Base")           # origin system
            self.pushButton10.setText("Create Symb.")
            FreeCADGui.updateGui()                                 # rafraichi l'ecran
        
    def on_lineEdit_page_Pressed(self):   # Name page
        global PageActive
        PageActive = self.lineEdit_page.text()

    def on_pushButton09_clicked(self):    # Bouton /heure document
        self.lineEdit_04h.setText(str(heure()))

    def on_pushButton08_clicked(self):    # Bouton date/ document
        global SymbolSwitch
        if SymbolSwitch==0:
            self.lineEdit_04.setText(str(dateUs()))
        else:
            self.lineEdit_04.setText(str(dateEu()))

    def on_pushButton07_clicked(self):    # Bouton /heure checked
        self.lineEdit_02h.setText(str(heure()))

    def on_pushButton06_clicked(self):    # Bouton date/ checked
        global SymbolSwitch
        if SymbolSwitch==0:
            self.lineEdit_02.setText(str(dateUs()))
        else:
            self.lineEdit_02.setText(str(dateEu()))

    def on_pushButton05_clicked(self):    # Bouton Appliquer
        try:
            global DESIGNED_BY, CREATION_DATE, CREA_DATE  , CREA_TIME, CHECKED_BY, CHECK_DATE
            global CHEC_DATE  , CHEC_TIME    , SIZE       , SCALE    , WEIGHT    ,DRAWING_NUMBER
            global SHEET      , TITLE        , DESCRIPTION, COMPANY  , COPYRIGHT
            global Note_A, Note_B, Note_C, Note_D, Note_E, Note_F, Note_G, Note_H, Note_I
            global ui
            global SymbolSwitch
            global PageActive

            try:
                page = App.activeDocument().getObjectsByLabel(PageActive.encode('utf-8'))[0]
            except Exception:
                page = App.activeDocument().getObjectsByLabel(PageActive)[0]        if len(str(page)) != 2:            self.pushButton05.setStyleSheet("background-color: #FF5B2B")
                self.pushButton05.setText("Wait.")
                FreeCADGui.updateGui()                # rafraichi l'ecran

                DESIGNED_BY = (self.lineEdit_01.text())
                CREATION_DATE = (self.lineEdit_02.text())+" - "+(self.lineEdit_02h.text())
                CHECKED_BY = (self.lineEdit_03.text())
                CHECK_DATE = (self.lineEdit_04.text())+" - "+(self.lineEdit_04h.text())
                SIZE = (self.lineEdit_05.text())
                SCALE = (self.lineEdit_06.text())
                WEIGHT = (self.lineEdit_07.text())
                DRAWING_NUMBER = (self.lineEdit_08.text())
                SHEET = (self.lineEdit_09.text())
                TITLE = (self.textEdit_01.toPlainText())
                DESCRIPTION = (self.textEdit_02.toPlainText())
                COMPANY = (self.textEdit_02b.toPlainText())
                COPYRIGHT = (self.lineEdit_20.text())            Note_A = (self.lineEdit_10.text())
                Note_B = (self.lineEdit_11.text())
                Note_C = (self.lineEdit_12.text())
                Note_D = (self.lineEdit_13.text())
                Note_E = (self.lineEdit_14.text())
                Note_F = (self.lineEdit_15.text())
                Note_G = (self.lineEdit_16.text())
                Note_H = (self.lineEdit_17.text())
                Note_I = (self.lineEdit_18.text())            try:
                    FreeCAD.getDocument(App.ActiveDocument.Name).getObject(page.Name).EditableTexts = [DESIGNED_BY, CREATION_DATE, CHECKED_BY, CHECK_DATE, SIZE, SCALE, WEIGHT, DRAWING_NUMBER, SHEET, TITLE, DESCRIPTION, COMPANY, COPYRIGHT, Note_A, Note_B, Note_C, Note_D, Note_E, Note_F, Note_G, Note_H, Note_I, ]
#old                    FreeCAD.getDocument(App.ActiveDocument.Name).getObjectsByLabel(PageActive.encode('utf-8'))[0].EditableTexts = [DESIGNED_BY, CREATION_DATE, CHECKED_BY, CHECK_DATE, SIZE, SCALE, WEIGHT, DRAWING_NUMBER, SHEET, TITLE, DESCRIPTION, COMPANY, COPYRIGHT, Note_A, Note_B, Note_C, Note_D, Note_E, Note_F, Note_G, Note_H, Note_I, ]
                    App.ActiveDocument.recompute()
                    FreeCAD.Console.PrintMessage("Write done to ( " + page.Label + " )" + "\n")
                    self.pushButton05.setStyleSheet("color: QPalette.Base")
                except Exception:
                    FreeCAD.Console.PrintError("Error write cartouche or verify the selected page ( " + page.Label + " )" + "\n")
                    self.pushButton05.setStyleSheet("background-color: red")
            else:
                FreeCAD.Console.PrintError("Error selected page ( " + Page.Label + " )" + "\n")
                self.pushButton05.setStyleSheet("background-color: red")

        except Exception:
            self.pushButton05.setStyleSheet("background-color: red")
            FreeCAD.Console.PrintError("Error or not page " + "\n")
        self.pushButton05.setText("Write")
        App.ActiveDocument.recompute()

    def on_pushButton04_clicked(self):    # Bouton nettoyer

        self.lineEdit_01.setText("")
        self.lineEdit_02.setText("")
        self.lineEdit_02h.setText("")
        self.lineEdit_03.setText("")
        self.lineEdit_04.setText("")
        self.lineEdit_04h.setText("")
        self.lineEdit_05.setText("?")
        self.lineEdit_06.setText("")
        self.lineEdit_07.setText("")
        self.lineEdit_08.setText("")
        self.lineEdit_09.setText("")
        self.textEdit_01.setText("")
        self.textEdit_02.setText("")
        self.textEdit_02b.setText("")
        self.lineEdit_20.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.lineEdit_17.setText("")
        self.lineEdit_18.setText("")

        self.pushButton10.setStyleSheet("color: QPalette.Base")                # origin system
        self.label_20.setVisible(False)
        self.radioButton_0.setChecked(True)
        self.pushButton05.setEnabled(True)
        self.pushButton05.setStyleSheet("background-color: QPalette.Base")     # origin system
        self.groupBox.setEnabled(True)

    def on_pushButton03_clicked(self):    # Bouton Memo
        global MDESIGNED_BY, MCREATION_DATE, MCREA_DATE  , MCREA_TIME, MCHECKED_BY, MCHECK_DATE
        global MCHEC_DATE  , MCHEC_TIME    , MSIZE       , MSCALE    , MWEIGHT    ,MDRAWING_NUMBER
        global MSHEET      , MTITLE        , MDESCRIPTION, MCOMPANY  , MCOPYRIGHT
        global MNote_A, MNote_B, MNote_C, MNote_D, MNote_E, MNote_F, MNote_G, MNote_H, MNote_I
        
        self.lineEdit_01.setText(MDESIGNED_BY)
        self.lineEdit_02.setText(MCREA_DATE)
        self.lineEdit_02h.setText(MCREA_TIME)
        self.lineEdit_03.setText(MCHECKED_BY)
        self.lineEdit_04.setText(MCHEC_DATE)
        self.lineEdit_04h.setText(MCHEC_TIME)
        self.lineEdit_05.setText("?") #(SIZE)
        self.lineEdit_06.setText(MSCALE)
        self.lineEdit_07.setText(MWEIGHT)
        self.lineEdit_08.setText(MDRAWING_NUMBER)
        self.lineEdit_09.setText(MSHEET)
        self.textEdit_01.setText(MTITLE)
        self.textEdit_02.setText(MDESCRIPTION)
        self.textEdit_02b.setText(MCOMPANY)
        self.lineEdit_20.setText(MCOPYRIGHT)
        self.lineEdit_10.setText(MNote_A)
        self.lineEdit_11.setText(MNote_B)
        self.lineEdit_12.setText(MNote_C)
        self.lineEdit_13.setText(MNote_D)
        self.lineEdit_14.setText(MNote_E)
        self.lineEdit_15.setText(MNote_F)
        self.lineEdit_16.setText(MNote_G)
        self.lineEdit_17.setText(MNote_H)
        self.lineEdit_18.setText(MNote_I)
#        self.lineEdit_page.setText(PageActive)
        self.radioButton_0.setChecked(True)

    def on_pushButton02_clicked(self):    # Bouton Quitter
        App.Console.PrintMessage("End CartoucheFC_Full\r\n")
        self.window.hide()
        FreeCADGui.Selection.removeObserver(s)           # Uninstalls the resident function
        App.Console.PrintMessage("removeObserver"+"\n")

#    def on_pushButton01_clicked(self):    # Bouton appel de Position
#        MainWindow.resize(210, 480)
#        executer()
#        MainWindow.resize(810, 480)
#______________________________________________________________________________________

class SelObserver:
    print "run.."
    def setSelection(self,document):                     # Selection in ComboView
        global PageActive
        global ui
        if len(Gui.Selection.getSelection(document)) == 1:

            ff = ui
            ff.lineEdit_page.setStyleSheet("color: QPalette.Base")           # origin system
            ff.pushButton05.setEnabled(True)
            ff.pushButton05.setStyleSheet("background-color: QPalette.Base") # origin system
            ff.groupBox.setEnabled(True)

            if (str(Gui.Selection.getSelection(document)[0].Name[0:4]) == "Page"):
                PageActive = str(Gui.Selection.getSelection(document)[0].Label.encode('utf-8'))
                try:
                    ff.lineEdit_page.setText(unicode(PageActive,'utf-8'))    # convert if accent
                except Exception:
                    ff.lineEdit_page.setText(PageActive)                     # normal

                memoEntree()                    # entree memo click mouse
                ff.on_pushButton03_clicked()    # Bouton Memo
            else:
                FreeCAD.Console.PrintError("Select a valid Page__________________________" + "\n")
                ff.lineEdit_page.setStyleSheet("color: red")
                ff.lineEdit_page.setText("Select a valid Page")              # 
                ff.pushButton05.setEnabled(False)
                ff.pushButton05.setStyleSheet("background-color: red")       # This function gives a color button
                ff.groupBox.setEnabled(False)

                FreeCAD.Console.PrintMessage("                 " + "Name            Label" + "\n")
                for i in App.ActiveDocument.Objects:
                    if i.Name[0:4] == "Page":
                        name = i.Name + "                 "
                        labe = i.Label+ "                 "
                        FreeCAD.Console.PrintMessage("    Valid Page : " + name[:15] + "," + labe[:25] + "\n")
                FreeCAD.Console.PrintError("_____________________________________________" + "\n")

for obj in FreeCAD.ActiveDocument.Objects:        # deslectionne
        FreeCADGui.Selection.removeSelection(obj)

s=SelObserver()
FreeCADGui.Selection.addObserver(s)               # install the function mode resident 

MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(MainWindow)
MainWindow.show()
}}



## Other

The fields have no length limit, check your cartouche.

This program creates a drawing representing the regional projection symbol on your project, do not touch it is registered therefore hidden form invisible.

If you want it to be cleared uncomment the commented lines and vice versa 


```python

#    App.getDocument(App.ActiveDocument.Name).removeObject("Symbol_EU")
    FreeCADGui.getDocument(App.ActiveDocument.Name).getObject("Symbol_EU").Visibility = False
```

 et  
```python

#    App.getDocument(App.ActiveDocument.Name).removeObject("Symbol_US")
    FreeCADGui.getDocument(App.ActiveDocument.Name).getObject("Symbol_US").Visibility = False
``` (I had some times an error in execution when the symbol was erased)

This module works with the drawing sheet included in FreeCAD this sheet is called **Page**, do not change the name of this sheet!

## Revision

ver \"00.10\" : 15/02/2017 : tuning page multiple (It is possible to lose a page if there are too many)

ver \"00.09\" : 10/02/2017 : add radio button for choice symbol and correct the placement symbol in the separate page

ver \"00.08 : 06/02/2017 : the dialog box name page accept the accent

ver \"00.07 : 05/02/2017 : add save cartouche with name page (for multi page in projects) ps: not for character accentuate \"àùé \...\"

ver 00.06 : 13/10/2016 : selection format page and position for the symbol convention (for FreeCAD ver 0.17)

ver 5 : 08/08/2014 PyQt4 and PySide



---
⏵ [documentation index](../README.md) > Macro CartoucheFC Full
