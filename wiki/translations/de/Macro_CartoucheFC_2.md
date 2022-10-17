# Macro CartoucheFC 2/de
{{Macro/de
|Name=Macro CartoucheFC 2
|Translate=Macro CartoucheFC 2
|Icon=Macro_CartoucheFC_2.png
|Description=Dieses Makro ist eine vollständige Anwendung. Es ermöglicht, die Kartusche des Zeichenblatts mit vollem Bearbeitungstext zu füllen. (Nur für den [Drawing Arbeitsbereich](Drawing_Workbench/de.md)).
|Author=Mario52
|Version=5.0
|Date=2014-08-08
|FCVersion=Alle Versionen, die den Drawing-Arbeitsbereich benutzen
|Download=[https   *//www.freecadweb.org/wiki/images/0/00/Macro_CartoucheFC_2.png ToolBar Icon]
}}

## Beschreibung

Dieses Makro ist eine vollständige Anwendung. Es ermöglicht das einfache Ausfüllen aller Felder der Kassette[A3 Landscape english](Drawing_templates/de.md)

<img alt="Macro CartoucheFC Modele 2" src=images/Macro_CartoucheFC_Modele_02.png  style="width   *680px;">

Das Bild stellt die Hierarchie des Ausfüllens der Felder dar, die im Fenster \"textEditable\" in FreeCAD belegt sind

## Verwendung

Die Verwendung ist sehr einfach, führen Sie das Makro aus und ändern Sie die Felder.

-   Die Schaltfläche **Quit**, um die Anwendung zu beenden.
-   Die Taste **Memo** gibt den Inhalt der Kassette beim Öffnen des Makros wieder.
-   Die Schaltfläche **Clear** bereinigt alle Felder im Makro (Felder werden durch Drücken auf **Memo** gerendert).
-   Die Schaltfläche **Apply** wendet die Änderungen an der Vorlage an.

Das Fenster bleibt über allen Fenstern, um die Änderungen zu visualisieren (diese Funktion kann unangenehm sein, wenn Sie sich dafür entscheiden, ein neues Fenster zu öffnen, und ist nicht verfügbar).

**PS   * Einige Zeichen wie und \$ werden nicht akzeptiert (und möglicherweise andere Sonderzeichen).**

Wenn Sie Fragen haben oder eine Funktion hinzufügen möchten, können Sie sich im französischen Forum an Sie wenden [Remplir cartouche](http   *//forum.freecadweb.org/viewtopic.php?f=12&t=2049)

## Code

ToolBar Icon ![](images/Macro_CartoucheFC_2.png )

**Macro_CartoucheFC_2.FcMacro**


{{MacroCode|code=

# -*- coding   * utf-8 -*-
"""
***************************************************************************
*   Copyright (c) 2014 <mario52>                                          *
*                                                                         *
*   This file is a supplement to the FreeCAD CAD development system.      *
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
# Macro_CartoucheFC_2.FcMacro
# 
# il faut que la page (drawing viewer) s'appelle " Page " qui est le nom par défaut du module Drawing
# cette macro fonctionne avec la feuille A3_Landscape_ qui possede tous les champs EditableTexts
# 
# http   *//www.freecadweb.org/wiki/index.php?title=Drawing_templates
# Fill the area of the cartridge
# It is necessary that the page (drawing viewer) is called "Page", which is the default name of the Drawing module
# Python 2.6
# 08/08/2014 ver 5.0 (pour cartouche modèle 2 (A3 Landscape english)) # PyQt and PySide 
# Created   *  by mario52
# PyQt and PySide 

#OS   * Windows Vista
#Word size   * 32-bit
#Version   * 0.14.3700 (Git)
#Branch   * releases/FreeCAD-0-14
#Hash   * 32f5aae0a64333ec8d5d160dbc46e690510c8fe1
#Python version   * 2.6.2
#Qt version   * 4.5.2
#Coin version   * 3.1.0
#SoQt version   * 1.4.1

try   *
    import PyQt4                        # PyQt4
    from PyQt4 import QtCore, QtGui     # PyQt4
except Exception   *
    import PySide                       # PySide
    from PySide import QtCore, QtGui    # PySide

import Draft, Part, FreeCAD, math, PartGui, FreeCADGui
from math import sqrt, pi, sin, cos, asin
from FreeCAD import Base

def utf8(unio)   *
    return unicode(unio).encode('UTF8')

global path
global Drawn_by               ; Drawn_by       = ""   # lineEdit_001
global DRAWN_BY               ; DRAWN_BY       = ""   # lineEdit_002
global Controlled_by          ; Controlled_by  = ""   # lineEdit_003
global CONTROLLED_BY          ; CONTROLLED_BY  = ""   # lineEdit_004
global Date                   ; Date           = ""   # lineEdit_005
global DATE                   ; DATE           = ""   # lineEdit_006
global Controlled_2           ; Controlled_2   = ""   # lineEdit_007
global CONTROLLED_2           ; CONTROLLED_2   = ""   # lineEdit_008
global Controlled_3           ; Controlled_3   = ""   # lineEdit_009
global CONTROLLED_3           ; CONTROLLED_3   = ""   # lineEdit_010
global SCALE                  ; SCALE          = ""   # lineEdit_011
global MOD                    ; MOD            = ""   # lineEdit_012
global COMPANY                ; COMPANY        = ""   # lineEdit_013
global ADRESS                 ; ADRESS         = ""   # lineEdit_014
global COUNTRY                ; COUNTRY        = ""   # lineEdit_015
global PART_NAME              ; PART_NAME      = ""   # lineEdit_016
global Project_number         ; Project_number = ""   # lineEdit_017
global A_                     ; A_             = ""   # lineEdit_018
global A__                    ; A__            = ""   # lineEdit_019
global B_                     ; B_             = ""   # lineEdit_020
global B__                    ; B__            = ""   # lineEdit_021
global C_                     ; C_             = ""   # lineEdit_022
global C__                    ; C__            = ""   # lineEdit_023
global D_                     ; D_             = ""   # lineEdit_024
global D__                    ; D__            = ""   # lineEdit_025
global E_                     ; E_             = ""   # lineEdit_026
global E__                    ; E__            = ""   # lineEdit_027
global Quantity               ; Quantity       = ""   # lineEdit_028
global Part_ID_number         ; Part_ID_number = ""   # lineEdit_029
global Fabrication_tolerances ; Fabrication_tolerance = "" #lineEdit_030
global Material               ; Material       = ""   # lineEdit_031
global _01                    ; _01            = ""   # lineEdit_032
global _001_001               ; _001_001       = ""   # lineEdit_033
global ISO2768_fh             ; ISO2768_fh     = ""   # lineEdit_034
global IRON                   ; IRON           = ""   # lineEdit_035

path = FreeCAD.ConfigGet("AppHomePath")

try   *
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError   *
    def _fromUtf8(s)   *
        return s
try   *
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig)   *
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError   *
    def _translate(context, text, disambig)   *
        return QtGui.QApplication.translate(context, text, disambig)

def errorDialog(msg)   *
    # Create a simple dialog QMessageBox
    # The first argument indicates the icon used   * one of QtGui.QMessageBox.{NoIcon, Information, Warning, Critical, Question} 
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical,u"Error Message",msg)
    try   *
        diag.setWindowFlags(PyQt4.QtCore.Qt.WindowStaysOnTopHint)  # PyQt4 cette fonction met la fenêtre en avant
    except Exception   *
        diag.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint) # PySide cette fonction met la fenêtre en avant
    #diag.setWindowModality(QtCore.Qt.ApplicationModal) # la fonction a été désactivée pour favoriser "WindowStaysOnTopHint"
    diag.exec_()

try   *
    Drawn_by = App.activeDocument().getObject("Page").EditableTexts[0]          # lineEdit_001
    DRAWN_BY = App.activeDocument().getObject("Page").EditableTexts[1]          # lineEdit_002
    Controlled_by = App.activeDocument().getObject("Page").EditableTexts[2]     # lineEdit_003
    CONTROLLED_BY = App.activeDocument().getObject("Page").EditableTexts[3]     # lineEdit_004
    Date = App.activeDocument().getObject("Page").EditableTexts[4]              # lineEdit_005
    DATE = App.activeDocument().getObject("Page").EditableTexts[5]              # lineEdit_006
    Controlled_2 = App.activeDocument().getObject("Page").EditableTexts[6]      # lineEdit_007
    CONTROLLED_2 = App.activeDocument().getObject("Page").EditableTexts[7]      # lineEdit_008
    Controlled_3 = App.activeDocument().getObject("Page").EditableTexts[8]      # lineEdit_009
    CONTROLLED_3 = App.activeDocument().getObject("Page").EditableTexts[9]      # lineEdit_010
    SCALE = App.activeDocument().getObject("Page").EditableTexts[10]            # lineEdit_011
    MOD = App.activeDocument().getObject("Page").EditableTexts[11]              # lineEdit_012
    COMPANY = App.activeDocument().getObject("Page").EditableTexts[12]          # lineEdit_013
    ADRESS = App.activeDocument().getObject("Page").EditableTexts[13]           # lineEdit_014
    COUNTRY = App.activeDocument().getObject("Page").EditableTexts[14]          # lineEdit_015
    PART_NAME = App.activeDocument().getObject("Page").EditableTexts[15]        # lineEdit_016
    Project_number = App.activeDocument().getObject("Page").EditableTexts[16]   # lineEdit_017
    A_ = App.activeDocument().getObject("Page").EditableTexts[17]               # lineEdit_018
    A__ = App.activeDocument().getObject("Page").EditableTexts[18]              # lineEdit_019
    B_ = App.activeDocument().getObject("Page").EditableTexts[19]               # lineEdit_020
    B__ = App.activeDocument().getObject("Page").EditableTexts[20]              # lineEdit_021
    C_ = App.activeDocument().getObject("Page").EditableTexts[21]               # lineEdit_022
    C__ = App.activeDocument().getObject("Page").EditableTexts[22]              # lineEdit_023
    D_ = App.activeDocument().getObject("Page").EditableTexts[23]               # lineEdit_024
    D__ = App.activeDocument().getObject("Page").EditableTexts[24]              # lineEdit_025
    E_ = App.activeDocument().getObject("Page").EditableTexts[25]               # lineEdit_026
    E__ = App.activeDocument().getObject("Page").EditableTexts[26]              # lineEdit_027
    Quantity= App.activeDocument().getObject("Page").EditableTexts[27]          # lineEdit_028
    Part_ID_number = App.activeDocument().getObject("Page").EditableTexts[28]   # lineEdit_029
    Fabrication_tolerance = App.activeDocument().getObject("Page").EditableTexts[29] #lineEdit_030
    Material = App.activeDocument().getObject("Page").EditableTexts[30]         # lineEdit_031
    _01 = App.activeDocument().getObject("Page").EditableTexts[31]              # lineEdit_032
    _001_001 = App.activeDocument().getObject("Page").EditableTexts[32]         # lineEdit_033
    ISO2768_fh = App.activeDocument().getObject("Page").EditableTexts[33]       # lineEdit_034
    IRON = App.activeDocument().getObject("Page").EditableTexts[34]             # lineEdit_035

except   *
    errorDialog("Error read cartridge")

class Ui_MainWindow(object)   *

    def __init__(self, MainWindow)   *
        self.window = MainWindow

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(849, 462)
        MainWindow.setMaximumSize(QtCore.QSize(849, 462))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        self.pushButton02 = QtGui.QPushButton(self.centralWidget)
        self.pushButton02.setGeometry(QtCore.QRect(210, 420, 93, 28))
        self.pushButton02.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton02.clicked.connect(self.on_pushButton02_clicked) # Bouton Quitter # Quit

        self.pushButton03 = QtGui.QPushButton(self.centralWidget)
        self.pushButton03.setGeometry(QtCore.QRect(320, 420, 93, 28))
        self.pushButton03.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton03.clicked.connect(self.on_pushButton03_clicked) # Bouton Memo # Memo

        self.pushButton04 = QtGui.QPushButton(self.centralWidget)
        self.pushButton04.setGeometry(QtCore.QRect(430, 420, 93, 28))
        self.pushButton04.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton04.clicked.connect(self.on_pushButton04_clicked) # Bouton nettoyer # Clear

        self.pushButton01 = QtGui.QPushButton(self.centralWidget)
        self.pushButton01.setGeometry(QtCore.QRect(540, 420, 93, 28))
        self.pushButton01.setObjectName(_fromUtf8("pushButton"))
        self.pushButton01.clicked.connect(self.on_pushButton01_clicked) # Bouton Appliquer # Apply

        self.lineEdit_001 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_001.setGeometry(QtCore.QRect(540, 100, 101, 22))
        self.lineEdit_001.setObjectName(_fromUtf8("lineEdit_001"))
        self.lineEdit_001.setText(Drawn_by)

        self.lineEdit_002 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_002.setGeometry(QtCore.QRect(650, 100, 121, 22))
        self.lineEdit_002.setObjectName(_fromUtf8("lineEdit_002"))
        self.lineEdit_002.setText(DRAWN_BY)

        self.lineEdit_003 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_003.setGeometry(QtCore.QRect(540, 140, 101, 22))
        self.lineEdit_003.setObjectName(_fromUtf8("lineEdit_003"))
        self.lineEdit_003.setText(Controlled_by)

        self.lineEdit_004 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_004.setGeometry(QtCore.QRect(650, 140, 121, 22))
        self.lineEdit_004.setObjectName(_fromUtf8("lineEdit_004"))
        self.lineEdit_004.setText(CONTROLLED_BY)

        self.lineEdit_005 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_005.setGeometry(QtCore.QRect(540, 180, 101, 22))
        self.lineEdit_005.setObjectName(_fromUtf8("lineEdit_005"))
        self.lineEdit_005.setText(Date)

        self.lineEdit_006 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_006.setGeometry(QtCore.QRect(650, 180, 121, 22))
        self.lineEdit_006.setObjectName(_fromUtf8("lineEdit_006"))
        self.lineEdit_006.setText(DATE)

        self.lineEdit_007 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_007.setGeometry(QtCore.QRect(540, 220, 101, 22))
        self.lineEdit_007.setObjectName(_fromUtf8("lineEdit_007"))
        self.lineEdit_007.setText(Controlled_2)

        self.lineEdit_008 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_008.setGeometry(QtCore.QRect(650, 220, 121, 22))
        self.lineEdit_008.setObjectName(_fromUtf8("lineEdit_008"))
        self.lineEdit_008.setText(CONTROLLED_2)

        self.lineEdit_009 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_009.setGeometry(QtCore.QRect(540, 260, 101, 22))
        self.lineEdit_009.setObjectName(_fromUtf8("lineEdit_009"))
        self.lineEdit_009.setText(Controlled_3)

        self.lineEdit_010 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_010.setGeometry(QtCore.QRect(650, 260, 121, 22))
        self.lineEdit_010.setObjectName(_fromUtf8("lineEdit_010"))
        self.lineEdit_010.setText(CONTROLLED_3)

        self.lineEdit_011 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_011.setGeometry(QtCore.QRect(780, 100, 61, 61))
        self.lineEdit_011.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_011.setObjectName(_fromUtf8("lineEdit_011"))
        self.lineEdit_011.setText(SCALE)

        self.lineEdit_012 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_012.setGeometry(QtCore.QRect(10, 100, 131, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_012.setFont(font)
        self.lineEdit_012.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_012.setObjectName(_fromUtf8("lineEdit_012"))
        self.lineEdit_012.setText(MOD)

        self.lineEdit_013 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_013.setGeometry(QtCore.QRect(10, 300, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_013.setFont(font)
        self.lineEdit_013.setObjectName(_fromUtf8("lineEdit_013"))
        self.lineEdit_013.setText(COMPANY)

        self.lineEdit_014 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_014.setGeometry(QtCore.QRect(10, 340, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_014.setFont(font)
        self.lineEdit_014.setObjectName(_fromUtf8("lineEdit_014"))
        self.lineEdit_014.setText(ADRESS)

        self.lineEdit_015 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_015.setGeometry(QtCore.QRect(10, 380, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_015.setFont(font)
        self.lineEdit_015.setObjectName(_fromUtf8("lineEdit_015"))
        self.lineEdit_015.setText(COUNTRY)

        self.lineEdit_016 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_016.setGeometry(QtCore.QRect(280, 300, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_016.setFont(font)
        self.lineEdit_016.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_016.setObjectName(_fromUtf8("lineEdit_016"))
        self.lineEdit_016.setText(PART_NAME)

        self.lineEdit_017 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_017.setGeometry(QtCore.QRect(590, 300, 251, 101))
        self.lineEdit_017.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_017.setFont(font)
        self.lineEdit_017.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_017.setObjectName(_fromUtf8("lineEdit_017"))
        self.lineEdit_017.setText(Project_number)

        self.lineEdit_018 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_018.setGeometry(QtCore.QRect(150, 260, 71, 22))
        self.lineEdit_018.setObjectName(_fromUtf8("lineEdit_018"))
        self.lineEdit_018.setText(A_)

        self.lineEdit_019 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_019.setGeometry(QtCore.QRect(230, 260, 301, 22))
        self.lineEdit_019.setObjectName(_fromUtf8("lineEdit_019"))
        self.lineEdit_019.setText(A__)

        self.lineEdit_020 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_020.setGeometry(QtCore.QRect(150, 220, 71, 22))
        self.lineEdit_020.setObjectName(_fromUtf8("lineEdit_020"))
        self.lineEdit_020.setText(B_)

        self.lineEdit_021 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_021.setGeometry(QtCore.QRect(230, 220, 301, 22))
        self.lineEdit_021.setObjectName(_fromUtf8("lineEdit_021"))
        self.lineEdit_021.setText(B__)

        self.lineEdit_022 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_022.setGeometry(QtCore.QRect(150, 180, 71, 22))
        self.lineEdit_022.setObjectName(_fromUtf8("lineEdit_022"))
        self.lineEdit_022.setText(C_)

        self.lineEdit_023 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_023.setGeometry(QtCore.QRect(230, 180, 301, 22))
        self.lineEdit_023.setObjectName(_fromUtf8("lineEdit_023"))
        self.lineEdit_023.setText(C__)

        self.lineEdit_024 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_024.setGeometry(QtCore.QRect(150, 140, 71, 22))
        self.lineEdit_024.setObjectName(_fromUtf8("lineEdit_024"))
        self.lineEdit_024.setText(D_)

        self.lineEdit_025 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_025.setGeometry(QtCore.QRect(230, 140, 301, 22))
        self.lineEdit_025.setObjectName(_fromUtf8("lineEdit_025"))
        self.lineEdit_025.setText(D__)

        self.lineEdit_026 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_026.setGeometry(QtCore.QRect(150, 100, 71, 22))
        self.lineEdit_026.setObjectName(_fromUtf8("lineEdit_026"))
        self.lineEdit_026.setText(E_)

        self.lineEdit_027 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_027.setGeometry(QtCore.QRect(230, 100, 301, 22))
        self.lineEdit_027.setObjectName(_fromUtf8("lineEdit_027"))
        self.lineEdit_027.setText(E__)

        self.lineEdit_028 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_028.setGeometry(QtCore.QRect(10, 60, 101, 22))
        self.lineEdit_028.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_028.setObjectName(_fromUtf8("lineEdit_028"))
        self.lineEdit_028.setText(Quantity)

        self.lineEdit_029 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_029.setGeometry(QtCore.QRect(120, 60, 131, 22))
        self.lineEdit_029.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_029.setObjectName(_fromUtf8("lineEdit_029"))
        self.lineEdit_029.setText(Part_ID_number)

        self.lineEdit_030 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_030.setGeometry(QtCore.QRect(260, 60, 381, 22))
        self.lineEdit_030.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_030.setObjectName(_fromUtf8("lineEdit_030"))
        self.lineEdit_030.setText(Fabrication_tolerance)

        self.lineEdit_031 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_031.setGeometry(QtCore.QRect(650, 60, 191, 22))
        self.lineEdit_031.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_031.setObjectName(_fromUtf8("lineEdit_031"))
        self.lineEdit_031.setText(Material)

        self.lineEdit_032 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_032.setGeometry(QtCore.QRect(10, 20, 101, 22))
        self.lineEdit_032.setObjectName(_fromUtf8("lineEdit_032"))
        self.lineEdit_032.setText(_01)

        self.lineEdit_033 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_033.setGeometry(QtCore.QRect(120, 20, 131, 22))
        self.lineEdit_033.setObjectName(_fromUtf8("lineEdit_033"))
        self.lineEdit_033.setText(_001_001)

        self.lineEdit_034 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_034.setGeometry(QtCore.QRect(260, 20, 381, 22))
        self.lineEdit_034.setObjectName(_fromUtf8("lineEdit_034"))
        self.lineEdit_034.setText(ISO2768_fh)

        self.lineEdit_035 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_035.setGeometry(QtCore.QRect(650, 20, 191, 22))
        self.lineEdit_035.setObjectName(_fromUtf8("lineEdit_035"))
        self.lineEdit_035.setText(IRON)

        self.label_1 = QtGui.QLabel(self.centralWidget)
        self.label_1.setGeometry(QtCore.QRect(790, 85, 41, 16))
        self.label_1.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 325, 53, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 365, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 285, 161, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(280, 285, 151, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(590, 285, 191, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(10, 85, 53, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(150, 85, 53, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(540, 85, 61, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(540, 125, 101, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(540, 165, 53, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(540, 205, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(540, 245, 81, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(10, 45, 71, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(120, 45, 121, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(260, 45, 141, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(650, 45, 71, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))

        self.graphicsView = QtGui.QGraphicsView(self.centralWidget)     # Fenêtre pour logo # Logo windows
        self.graphicsView.setGeometry(QtCore.QRect(780, 220, 61, 61))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_18 = QtGui.QLabel(self.centralWidget)
        self.label_18.setGeometry(QtCore.QRect(790, 205, 41, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow)   *
        try   *
            MainWindow.setWindowFlags(PyQt4.QtCore.Qt.WindowStaysOnTopHint)  # PyQt4
        except Exception   *
            MainWindow.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint) # PySide

        MainWindow.setWindowTitle(_translate("MainWindow", "Cartouche mod 2", None))

        self.pushButton01.setText(_translate("MainWindow", "Apply", None))
        self.pushButton02.setText(_translate("MainWindow", "Quit", None))
        self.pushButton03.setText(_translate("MainWindow", "Memo", None))
        self.pushButton04.setText(_translate("MainWindow", "Clear", None))

        self.lineEdit_001.setText(_translate("MainWindow", "Drawn_by", None))
        self.lineEdit_002.setText(_translate("MainWindow", "DRAWN_BY", None))
        self.lineEdit_003.setText(_translate("MainWindow", "Controlled_by", None))
        self.lineEdit_004.setText(_translate("MainWindow", "CONTROLLED_BY", None))
        self.lineEdit_005.setText(_translate("MainWindow", "Date", None))
        self.lineEdit_006.setText(_translate("MainWindow", "DATE", None))
        self.lineEdit_007.setText(_translate("MainWindow", "Controlled_2", None))
        self.lineEdit_008.setText(_translate("MainWindow", "CONTROLLED_2", None))
        self.lineEdit_009.setText(_translate("MainWindow", "Controlled_3", None))
        self.lineEdit_010.setText(_translate("MainWindow", "CONTROLLED_3", None))
        self.lineEdit_011.setText(_translate("MainWindow", "SCALE", None))
        self.lineEdit_012.setText(_translate("MainWindow", "MOD", None))
        self.lineEdit_013.setText(_translate("MainWindow", "COMPANY", None))
        self.lineEdit_014.setText(_translate("MainWindow", "ADRESS", None))
        self.lineEdit_015.setText(_translate("MainWindow", "COUNTRY", None))
        self.lineEdit_016.setText(_translate("MainWindow", "PART_NAME", None))
        self.lineEdit_017.setText(_translate("MainWindow", "Project_number", None))
        self.lineEdit_018.setText(_translate("MainWindow", "A_", None))
        self.lineEdit_019.setText(_translate("MainWindow", "A__", None))
        self.lineEdit_020.setText(_translate("MainWindow", "B_", None))
        self.lineEdit_021.setText(_translate("MainWindow", "B__", None))
        self.lineEdit_022.setText(_translate("MainWindow", "C_", None))
        self.lineEdit_023.setText(_translate("MainWindow", "C__", None))
        self.lineEdit_024.setText(_translate("MainWindow", "D_", None))
        self.lineEdit_025.setText(_translate("MainWindow", "D__", None))
        self.lineEdit_026.setText(_translate("MainWindow", "E_", None))
        self.lineEdit_027.setText(_translate("MainWindow", "E__", None))
        self.lineEdit_028.setText(_translate("MainWindow", "Quantity", None))
        self.lineEdit_029.setText(_translate("MainWindow", "Part_ID_number", None))
        self.lineEdit_030.setText(_translate("MainWindow", "Fabrication_tolerance", None))
        self.lineEdit_031.setText(_translate("MainWindow", "Material", None))
        self.lineEdit_032.setText(_translate("MainWindow", "_01", None))
        self.lineEdit_033.setText(_translate("MainWindow", "_001_001", None))
        self.lineEdit_034.setText(_translate("MainWindow", "ISO2768_fh", None))
        self.lineEdit_035.setText(_translate("MainWindow", "IRON", None))

        self.label_1.setText(_translate("MainWindow", "Scale    *", None))
        self.label_2.setText(_translate("MainWindow", "Address    *", None))
        self.label_3.setText(_translate("MainWindow", "Country    *", None))
        self.label_4.setText(_translate("MainWindow", "Company name    *", None))
        self.label_5.setText(_translate("MainWindow", "Part name    *", None))
        self.label_6.setText(_translate("MainWindow", "Project number / id    *", None))
        self.label_7.setText(_translate("MainWindow", "Size    *", None))
        self.label_8.setText(_translate("MainWindow", "Notes    *", None))
        self.label_9.setText(_translate("MainWindow", "Draw by    *", None))
        self.label_10.setText(_translate("MainWindow", "Controlled by    *", None))
        self.label_11.setText(_translate("MainWindow", "Date    *", None))
        self.label_12.setText(_translate("MainWindow", "Controlled 2    *", None))
        self.label_13.setText(_translate("MainWindow", "Controlled 3    *", None))
        self.label_14.setText(_translate("MainWindow", "Quantity    *", None))
        self.label_15.setText(_translate("MainWindow", "Part ID / Number    *", None))
        self.label_16.setText(_translate("MainWindow", "Fabrication tolerance    *", None))
        self.label_17.setText(_translate("MainWindow", "Material    *", None))
        self.label_18.setText(_translate("MainWindow", "Logo    *", None))

    def on_pushButton01_clicked(self)   *    # Bouton Appliquer # Appli buttom
        Drawn_by = utf8(self.lineEdit_001.text())
        DRAWN_BY = utf8(self.lineEdit_002.text())
        Controlled_by = utf8(self.lineEdit_003.text())
        CONTROLLED_BY = utf8(self.lineEdit_004.text())
        Date = utf8(self.lineEdit_005.text())
        DATE = utf8(self.lineEdit_006.text())
        Controlled_2 = utf8(self.lineEdit_007.text())
        CONTROLLED_2 = utf8(self.lineEdit_008.text())
        Controlled_3 = utf8(self.lineEdit_009.text())
        CONTROLLED_3 = utf8(self.lineEdit_010.text())
        SCALE = utf8(self.lineEdit_011.text())
        MOD = utf8(self.lineEdit_012.text())
        COMPANY = utf8(self.lineEdit_013.text())
        ADRESS = utf8(self.lineEdit_014.text())
        COUNTRY = utf8(self.lineEdit_015.text())
        PART_NAME = utf8(self.lineEdit_016.text())
        Project_number = utf8(self.lineEdit_017.text())
        A_ = utf8(self.lineEdit_018.text())
        A__ = utf8(self.lineEdit_019.text())
        B_ = utf8(self.lineEdit_020.text())
        B__ = utf8(self.lineEdit_021.text())
        C_ = utf8(self.lineEdit_022.text())
        C__ = utf8(self.lineEdit_023.text())
        D_ = utf8(self.lineEdit_024.text())
        D__ = utf8(self.lineEdit_025.text())
        E_ = utf8(self.lineEdit_026.text())
        E__ = utf8(self.lineEdit_027.text())
        Quantity = utf8(self.lineEdit_028.text())
        Part_ID_number = utf8(self.lineEdit_029.text())
        Fabrication_tolerance = utf8(self.lineEdit_030.text())
        Material = utf8(self.lineEdit_031.text())
        _01 = utf8(self.lineEdit_032.text())
        _001_001 = utf8(self.lineEdit_033.text())
        ISO2768_fh = utf8(self.lineEdit_034.text())
        IRON = utf8(self.lineEdit_035.text())

        try   *
            FreeCAD.getDocument (App.ActiveDocument.Name).getObject("Page").EditableTexts =[unicode(Drawn_by,'utf-8'), unicode(DRAWN_BY,'utf-8'), unicode(Controlled_by,'utf-8'), unicode(CONTROLLED_BY,'utf-8'), unicode(Date,'utf-8'), unicode(DATE,'utf-8'), unicode(Controlled_2, 'utf-8'), unicode(CONTROLLED_2,'utf-8'), unicode(Controlled_3,'utf-8'), unicode(CONTROLLED_3,'utf-8'), unicode(SCALE,'utf-8'), unicode(MOD,'utf-8'), unicode(COMPANY,'utf-8'), unicode(ADRESS,'utf-8'), unicode(COUNTRY, 'utf-8'), unicode(PART_NAME,'utf-8'), unicode(Project_number,'utf-8'), unicode(A_,'utf-8'), unicode(A__,'utf-8'), unicode(B_,'utf-8'), unicode(B__,'utf-8'), unicode(C_,'utf-8'), unicode(C__,'utf-8'), unicode(D_,'utf-8'), unicode(D__,'utf-8'), unicode(E_,'utf-8'), unicode(E__,'utf-8'), unicode(Quantity,'utf-8'), unicode(Part_ID_number,'utf-8'), unicode(Fabrication_tolerance,'utf-8'), unicode(Material,'utf-8'), unicode(_01,'utf-8'), unicode(_001_001,'utf-8'), unicode(ISO2768_fh,'utf-8'), unicode(IRON,'utf-8'),]  # PyQt4
            App.ActiveDocument.recompute()
        except Exception   *#
            FreeCAD.getDocument (App.ActiveDocument.Name).getObject("Page").EditableTexts =[Drawn_by.encode('utf-8'), DRAWN_BY.encode('utf-8'), Controlled_by.encode('utf-8'), CONTROLLED_BY.encode('utf-8'), Date.encode('utf-8'), DATE.encode('utf-8'), Controlled_2.encode('utf-8'), CONTROLLED_2.encode('utf-8'), Controlled_3.encode('utf-8'), CONTROLLED_3.encode('utf-8'), SCALE.encode('utf-8'), MOD.encode('utf-8'), COMPANY.encode('utf-8'), ADRESS.encode('utf-8'), COUNTRY.encode('utf-8'), PART_NAME.encode('utf-8'), Project_number.encode('utf-8'), A_.encode('utf-8'), A__.encode('utf-8'), B_.encode('utf-8'), B__.encode('utf-8'), C_.encode('utf-8'), C__.encode('utf-8'), D_.encode('utf-8'), D__.encode('utf-8'), E_.encode('utf-8'), E__.encode('utf-8'), Quantity.encode('utf-8'), Part_ID_number.encode('utf-8'), Fabrication_tolerance.encode('utf-8'), Material.encode('utf-8'), _01.encode('utf-8'), _001_001.encode('utf-8'), ISO2768_fh.encode('utf-8'), IRON.encode('utf-8'),]                                       # PySide
            App.ActiveDocument.recompute()

    def on_pushButton04_clicked(self)   *    # Bouton nettoyer # Clear buttom

        Drawn_by = ""             ;self.lineEdit_001.setText("")
        DRAWN_BY = ""             ;self.lineEdit_002.setText("")
        Controlled_by = ""        ;self.lineEdit_003.setText("")
        CONTROLLED_BY = ""        ;self.lineEdit_004.setText("")
        Date  = ""                ;self.lineEdit_005.setText("")
        DATE = ""                 ;self.lineEdit_006.setText("")
        Controlled_2 = ""         ;self.lineEdit_007.setText("")
        CONTROLLED_2 = ""         ;self.lineEdit_008.setText("")
        Controlled_3 = ""         ;self.lineEdit_009.setText("")
        CONTROLLED_3 = ""         ;self.lineEdit_010.setText("")
        SCALE = ""                ;self.lineEdit_011.setText("")
        MOD = ""                  ;self.lineEdit_012.setText("")
        COMPANY = ""              ;self.lineEdit_013.setText("")
        ADRESS = ""               ;self.lineEdit_014.setText("")
        COUNTRY = ""              ;self.lineEdit_015.setText("")
        PART_NAME = ""            ;self.lineEdit_016.setText("")
        Project_number = ""       ;self.lineEdit_017.setText("")
        A_ = ""                   ;self.lineEdit_018.setText("")
        A__ = ""                  ;self.lineEdit_019.setText("")
        B_ = ""                   ;self.lineEdit_020.setText("")
        B__ = ""                  ;self.lineEdit_021.setText("")
        C_ = ""                   ;self.lineEdit_022.setText("")
        C__ = ""                  ;self.lineEdit_023.setText("")
        D_ = ""                   ;self.lineEdit_024.setText("")
        D__ = ""                  ;self.lineEdit_025.setText("")
        E_ = ""                   ;self.lineEdit_026.setText("")
        E__ = ""                  ;self.lineEdit_027.setText("")
        Quantity = ""             ;self.lineEdit_028.setText("")
        Part_ID_number = ""       ;self.lineEdit_029.setText("")
        Fabrication_tolerance = "";self.lineEdit_030.setText("")
        Material = ""             ;self.lineEdit_031.setText("")
        _01 = ""                  ;self.lineEdit_032.setText("")
        _001_001 = ""             ;self.lineEdit_033.setText("")
        ISO2768_fh = ""           ;self.lineEdit_034.setText("")
        IRON = ""                 ;self.lineEdit_035.setText("")

    def on_pushButton03_clicked(self)   *    # Bouton Memo # Memo buttom
        self.lineEdit_001.setText(Drawn_by)
        self.lineEdit_002.setText(DRAWN_BY)
        self.lineEdit_003.setText(Controlled_by)
        self.lineEdit_004.setText(CONTROLLED_BY)
        self.lineEdit_005.setText(Date)
        self.lineEdit_006.setText(DATE)
        self.lineEdit_007.setText(Controlled_2)
        self.lineEdit_008.setText(CONTROLLED_2)
        self.lineEdit_009.setText(Controlled_3)
        self.lineEdit_010.setText(CONTROLLED_3)
        self.lineEdit_011.setText(SCALE)
        self.lineEdit_012.setText(MOD)
        self.lineEdit_013.setText(COMPANY)
        self.lineEdit_014.setText(ADRESS)
        self.lineEdit_015.setText(COUNTRY)
        self.lineEdit_016.setText(PART_NAME)
        self.lineEdit_017.setText(Project_number)
        self.lineEdit_018.setText(A_)
        self.lineEdit_019.setText(A__)
        self.lineEdit_020.setText(B_)
        self.lineEdit_021.setText(B__)
        self.lineEdit_022.setText(C_)
        self.lineEdit_023.setText(C__)
        self.lineEdit_024.setText(D_)
        self.lineEdit_025.setText(D__)
        self.lineEdit_026.setText(E_)
        self.lineEdit_027.setText(E__)
        self.lineEdit_028.setText(Quantity)
        self.lineEdit_029.setText(Part_ID_number)
        self.lineEdit_030.setText(Fabrication_tolerance)
        self.lineEdit_031.setText(Material)
        self.lineEdit_032.setText(_01)
        self.lineEdit_033.setText(_001_001)
        self.lineEdit_034.setText(ISO2768_fh)
        self.lineEdit_035.setText(IRON)

    def on_pushButton02_clicked(self)   *    # Bouton Quitter # Quit buttom
        App.Console.PrintMessage("End cartridge mod 2\r\n")
        self.window.hide()

MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(MainWindow)
MainWindow.show()

}}

## Ausführung

5.0    * 08/08/2014



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CartoucheFC 2/de
