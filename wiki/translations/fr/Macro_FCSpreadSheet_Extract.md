# Macro FCSpreadSheet Extract/fr

 {{Macro/fr
|Name=Macro_FCSpreadsheet_Extract
|Icon=Macro_FCSpreadsheet_Extract.png
|Description=Cette macro enregistre les données de la feuille de calcul dans un fichier csv avec la formule ou dans un fichier xml.<br/> <br/>{{ColoredText|#ff0000|#ffffff|Nouvelle version tourne seulement avec FC version 0.18 and more (PySide2 Qt5)}} <br/> <br/> Pour la version précédente voir [https://gist.githubusercontent.com/mario52a/29f7dce6934e8adf5d584bdddd2e469f/raw/ef0b0de56a65afc34a9a1a969969797910f3a004/Macro_FCSpreadSheet_Extract.FCMacro Macro_FCSpreadSheet_Extract.FCMacro] et installez la manuellement.
|Author=Mario52
|Version=0.2
|Date=2020-03-14
|FCVersion=0.18 et plus
|Download=[https://www.freecadweb.org/wiki/images/d/d5/Macro_FCSpreadsheet_Extract.png ToolBar Icon]
}}

## Description

Cette macro enregistre les données de la feuille de calcul dans un fichier csv avec la formule ou dans un fichier xml.

## Utilisation

Lancez la macro.

## Script

L\'icône pour votre barre d\'outils qui est à placer dans le même répertoire que la macro ![](images/Macro_FCSpreadsheet_Extract.png )

**Macro\_FCSpreadSheet\_Extract.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
***************************************************************************
*   Copyright (c) 2018 2019 2020 <mario52>                                *
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
#05/05/2018 14/03/2020
#
__title__   = "FCSpreadSheet_Extract"
__author__  = "Mario52"
__url__     = "https://www.freecadweb.org"
__Wiki__    = "https://wiki.freecadweb.org/Macro_FCSpreadSheet_Extract"
__version__ = "00.03"
__date__    = "2020/03/14" #YYYY/MM/DD


#### Test FreeCAD.Version above 0.17 BEGIN ##########################################################################################################
import WebGui
#WebGui.openBrowser("http://www.freecadweb.org/")
try:
    import PySide
    from PySide import QtGui
    import sys, os
    def errorDialog(msg):
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical,u"Error FreeCAD Version",msg )
        diag.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint) # PySide #cette fonction met la fenetre en avant
        diag.setStyleSheet("QLabel {color : #ffffff; background-color : #FF3300;  font: bold}")
        WebGui.openBrowser("https://gist.githubusercontent.com/mario52a/29f7dce6934e8adf5d584bdddd2e469f/raw/ef0b0de56a65afc34a9a1a969969797910f3a004/Macro_FCSpreadSheet_Extract.FCMacro" + "\n\n")
        diag.exec_()
        diag.setStyleSheet("Base")

    if int(FreeCAD.Version()[1]) < 18:      # Version of FreeCAD
        memo = PySide.QtGui.QClipboard()    # Copy the title in to the clipBoard
        memo.setText(__title__)    
        FreeCAD.Console.PrintMessage("https://gist.githubusercontent.com/mario52a/29f7dce6934e8adf5d584bdddd2e469f/raw/ef0b0de56a65afc34a9a1a969969797910f3a004/Macro_FCSpreadSheet_Extract.FCMacro" + "\n\n")
        errorDialog("This version " + __title__ + " works with FreeCAD v0.18 or higher. " + "\n\n"
                    "PySide2 Qt version: 5" + "\n\n"
                    "The macro it was derived from (30/04/2018 for FC v0.17) is displayed in your FreeCAD browser" + "\n\n"
                    "copy and paste it into the FCSpreadSheet_Extract macro or install it manually." + "\n\n"
                    "If the code is not displayed in the FreeCAD browser page," + "\n"
                    "copy the URL displayed in the Report View")
except Exception:
    None
#### Test FreeCAD.Version above 0.17 END ############################################################################################################

import PySide2
from PySide2 import QtWidgets, QtGui ,QtCore 
from PySide2.QtGui import *
from PySide2.QtCore import *
import copy
import re


path = FreeCAD.ConfigGet("UserAppData")
#path = Your path

global ESCAPE
global tableau
global data

########## separator 
ESCAPE = "\t"           #tabulation    #compatible FC
#ESCAPE = ","            #virgule       #compatible FCInfo
#ESCAPE = ";"            #point virgule #option
#ESCAPE = " "            #espace        #option
#ESCAPE = ""             #vide          #option
##########

def decodeColonne(colonne = "A"):                                  # converti la chaine A ... ZZ en numero de colonne ex: A = 1; AA = 27
    colonne  = re.split('[0-9]+', colonne, flags=re.IGNORECASE)[0] # supp the alphanumeric number ex: A2 = A; A12 = A (1A return 0)
    try:
        if len(colonne) > 1:
            return ((ord(colonne[0].upper()) - 64) * 26 ) + (ord(colonne[1].upper()) - 64) # max 2 car (AAAA return 27)
        else:
            return (ord(colonne.upper()) - 64 )
    except Exception:
        return 0

def decodeOccupation(dataTableau = ""):  # decode the max occupation Colonnes, Lines and give the cell occupation
    #
    #lineMax, colonneMax, cellsOccupation = decodeOccupation(FreeCAD.ActiveDocument.getObject(str(Sheet.Name)))
    #
    try:
        #tyty = unicode(dataTableau.cells.Content, "utf-8")
        tyty = dataTableau.cells.Content
        tyty = tyty.split(">")

        ####
        cellsOccupation = [] 
        cellsSorted     = []                                                 # search the "A1" definition
        for i in tyty[1:-2]:                                                 # split les cases dans la chaine XML
            i = i[i.find('"')+1:]
            i = i[:i.find('"')]
            cellsOccupation.append(i)

        cellsSorted = copy.deepcopy(cellsOccupation)
        cellsSorted.sort()

        ####
        linesMax = 0
        for i in cellsSorted:                                                # recherche le max (ligne et colonne)
            colonnesMax = re.split('[0-9]+', i, flags=re.IGNORECASE)         # colonne max (AA)
            try:
                dummy   = int(re.split('[A-Z]+', i, flags=re.IGNORECASE)[1]) # line
                if dummy > linesMax:
                    linesMax = dummy                                         # lines max
            except Exception:
                None
        del cellsSorted[:]
        ####
        return linesMax, decodeColonne(colonnesMax[0]), cellsOccupation      # return linesMax , colonnesMax, cellsOccupation

    except Exception:
        FreeCAD.Console.PrintError("Error data, Enter object <Sheet object> ex:" + "\n")
        FreeCAD.Console.PrintError("lineMax, colonneMax, cellsOccupation = decodeOccupation(FreeCAD.ActiveDocument.getObject(str(Sheet.Name)))" + "\n")
        return 0, 0, []

def caseTableau(ligne = 1, colonne = 1):                                     # calcule et code la case du tableur ex: 1,1 = A1; 7,7 = G7
    #
    # print caseTableau( 1, 1)
    #
    if ligne < 1: ligne = 1
    if ligne > 16384: ligne = 16384
    if colonne < 1: colonne = 1
    if colonne > 702: colonne = 702
    if (colonne > 26):
        if abs(colonne % 26) == 0:
            return chr(64 + (abs(colonne / 26) -1)) + chr(90) + str(ligne)
        else:
            return chr(64 + (abs(colonne / 26))) + chr(64 + (abs(colonne % 26))) + str(ligne)
    else:
        return chr(colonne + 64) + str(ligne)

def saveDataInFile(data = ""):
    global tableau

    SaveName, Filter = PySide2.QtWidgets.QFileDialog.getSaveFileName(None, "Save a file txt", path, "CSV (*.csv);;XML (*.xml)") # PySide

    if (SaveName == ""):
        App.Console.PrintMessage("Process aborted"+"\n")
    else:
        App.Console.PrintMessage("Registration of "+SaveName+"\n")
        try:
            file = open(SaveName, 'w')
            try:
                if Filter == "XML (*.xml)":
                    ext = "(*.xml)"
                    file.write(tableau.cells.Content)          # save XML
                else:
                    ext = "(*.csv)"
                    for i in data:
#                        file.write(unicode(i).encode("utf-8")) # save CSV
                        file.write(i) # save CSV

                        print(i)

            except Exception:
                App.Console.PrintError("Error write file "+ext+"\n")
            finally:
                file.close()
        except Exception:
            App.Console.PrintError("Error Open file "+SaveName+"\n")

##tableau.getContents("A2")                             #lire une celulle
##print App.ActiveDocument.Spreadsheet.cells.Content    #lire toutes les celulles # XML

try:
    for i in FreeCAD.ActiveDocument.Objects:               # search SpreadSheet in all object
        obj = FreeCAD.ActiveDocument.getObject(i.Name).TypeId.split("::")[0]
        if obj == "Spreadsheet":
            tableau = FreeCAD.ActiveDocument.getObject(str(i.Name))
            print( "Name : ",i.Name," ; Label : ",i.Label)
            break                                          # quit to the first SpreadSheetlinesMax    = decodeOccupation(tableau)[0]             # linesMax
    colonnesMax = decodeOccupation(tableau)[1]             # colonnesMax
    #print decodeOccupation(tableau)[2]                    # display the cells occupiedprint( "Number cell : ", linesMax * colonnesMax," (", linesMax," L x ", colonnesMax," C)")
    FreeCADGui.updateGui()                                          # rafraichi l'ecrandataToSave = []
    for i in range(1, linesMax+1):
        for ii in range(1, colonnesMax+1):
    #        dataToSave.append(unicode(tableau.getContents(caseTableau(i,ii)), 'utf-8') + ESCAPE)
            dataToSave.append(tableau.getContents(caseTableau(i,ii)) + ESCAPE)
        dataToSave.append("\n")saveDataInFile(dataToSave)
    del dataToSave[:]print( "__Fin FCSpreadSheet_Extract__________\n")
except Exception:
    print ("No SpreadSheet in the document or Error")


}}

