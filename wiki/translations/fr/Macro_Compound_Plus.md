# Macro Compound Plus/fr
{{Macro/fr
|Name=Macro Compound Plus
|Description = {{ColoredText|#ff0000|#ffffff|Nouvelle interface graphique modifiée pour le HD dpi (QGridLayout) exécutez uniquement la version FC 0.19 et plus (PySide2 Qt5)}}<br/><br/> Pour la version précédente, voir [https://gist.github.com/mario52a/7be361a8c489deec918f664fdcfc4394/11ae1a55229c84d9aab4e9a36099d90f52909958 Macro_Compound_Plus 00.02] et installez-le manuellement.<br/><br/>
Commande Draft définie dans une petite macro pour l'exemple de fil 2D: travailler avec les fichiers DXF. La macro détecte: Ligne, Arc, Cercle, Ellipse, BSplineCurve et reproduit le fil DXF dans un objet Draft. Le texte est converti en ShapeString.
|Author=Mario52
|Version=00.04
|Date=2020-08-15
|FCVersion= 0.19
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Compound_Plus.png ToolBar Icon]
}}

## Description

Commande Draft définie dans une petite macro pour l\'exemple de fil 2D: travaille avec les fichiers DXF. La macro détecte: Ligne, Arc, Cercle, Ellipse, BSplineCurve et reproduit le fil DXF dans un objet Draft. Le texte est converti en ShapeString.

## Utilisation

![Macro_Compound_Plus_00](images/Macro_Compound_Plus_00.png )

### Choix

-    **<img src="images/Part_Compound.svg" width=16px> Compound I**Type I \[1 + 1 = 1\] : créez un composé unique de tous les objets sélectionnés sans historique.

-    **<img src="images/Part_Compound.svg" width=16px> Compound II**Type II \[1 + 1 = A (1 + 1)\] : Créez un composé de tous les objets sélectionnés avec l\'historique de tous les objets. Idem \"**Menu → Part → Make compound**\".

### {{CheckBox}} Couleur de l\'option 

S\'il {{CheckBox}} est vérifiée, la couleur de l\'objet à travailler sont colorées (bord, sommet)

-    **{{ColoredText|#ff0000|<img src="images/Workbench_Image.svg" width=16px> Color** }}: Donne une couleur à l\'objet. (Rouge par défaut 255, 0, 0)

### Outils

-   LineEdit: affiche (Index de police/nombre de police) le chemin et le nom de la police.

-    **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)**: convertir le texte <img alt="" src=images/Draft_Text.svg  style="width:16px;"> en une chaîne de forme <img alt="" src=images/Draft_ShapeString.svg  style="width:16px;"> (La hauteur du texte converti est respectée mais le résultat visuel peut ne pas être respecté, voir la propriété Vue combinée pour confirmer). (A) est la hauteur de la valeur automatique du texte.

    -   
        {{SpinBox|0,00 Auto}}
        
        : Si spinbox est égal à 0.0, la hauteur de la VALEUR du texte est respectée. Si différent de 0.0, le **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** se change en mode manuel **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (M)**.

-    **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**: Cette commande convertit le fil en une ligne avec des coordonnées. (ex: un composé rétrogradé n\'a pas de coordonnées, cette fonction crée une ligne avec les coordonnées comme ligne de dépouille et reproduit le fil DXF dans un objet dépouille sont détectées: ligne, arc, cercle, ellipse, BSplineCurve.

    -   
        {{SpinBox|0,00 Auto}}
        
        : Donne une épaisseur du fil. Si spinbox est égal à 0.0, la hauteur de la VALEUR du texte est respectée, si différent de 0.0, le **<img src="images/Draft_Line.svg" width=16px> Convert Wire (A)** se change en mode manuel **Convert Wire (M)**.

-    {{CheckBox|<img src="images/Draft_BezCurve.svg" width=16px> BezierCurve}}: Par défaut, le BezierCurve détecté est <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;">, s\'il est coché, le BezierCurve est cubique <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> et le bouton change {{CheckBox|TRUE|<img src="images/Draft_CubicBezCurve.svg" width=16px> Cubic BezierCurve}}

-    {{RadioButton|TRUE|<img src="images/Std_DrawStyleFlatLines.svg" width=16px> FlatLines}}: les objets créés sont des FlatLines.

-    {{RadioButton|<img src="images/Std_DrawStyleWireFrame.svg" width=16px> Wireframe}}: Les objets créés sont Wireframe.

-    {{RadioButton|<img src="images/Std_DrawStylePoints.svg" width=16px> Points}}: Les objets créés sont des Points.

-    **[<img src=images/Draft_Upgrade.svg style="width:16px"> UpGrade**: UpGrade

-    **[<img src=images/Draft_Downgrade.svg style="width:16px"> DownGrade**: DownGrade

### Pour le composé I et le bord de conversion 

Cette section fonctionne uniquement avec les outils **<img src="images/Part_Compound.svg" width=16px> Compound I
**, **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** et **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**

-    {{RadioButton|TRUE|None}}: Tous les objets d\'origine restent tels quels.

-    {{RadioButton|Hidden original objest(s)}}: Masque les objets originaux.

-    {{RadioButton|Delete original objest(s)}}: supprime les objets originaux.

### Forcer sur une forme: Ligne 

Si l\'objet ligne, arc ou cercle n\'est pas reconnu (comme forme dans un objet 3D de volume), cette section force la création d\'une ligne, d\'un arc ou d\'un cercle.

aucune vérification n\'est effectuée, cette section plateau permet de créer une forme 2D demandée (Draft) en fonction des données fournies

-    {{RadioButton|TRUE|<img src="images/Draft_Line.svg" width=16px> Lines}}: pour créer une ligne.

-    {{RadioButton|<img src="images/Draft_Arc.svg" width=16px> Arc}}: pour créer un arc.

-    {{RadioButton|<img src="images/Draft_Circle.svg" width=16px> Circle}}: pour créer un cercle

-    **<img src="images/Draft_Line.svg" width=16px> Force on : Line**: Bouton Force

### Commande

-   Barre de progression

-    **Reset**: réinitialiser la macro

-    **Quit**: Quittez la macro, bye

-    **Help**:afficher la page wiki dans le navigateur FreeCAD

## Script

L\' icône pour votre barre d\'outils ![](images/Macro_Compound_Plus.png ) a copier dans votre répertoire de macros.

[Comment créer une barre d\'outils](Customize_Toolbars/fr.md), [Comment installer une macro](How_to_install_macros/fr.md)

Le script sur github [Macro_Compound_Plus.FCMacro](https://gist.github.com/mario52a/7be361a8c489deec918f664fdcfc4394)

**Macro_Compound_Plus.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
***************************************************************************
*   Copyright (c) 2016 2017 2018 1019 2020 <mario52>                      *
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
#Macro_Compound_Plus 05/08/2016 /_00 24/01/2018 /.02 2018-01-24/.03 2020/05/12 15-08-2020/ 0.04 forcer
#
#OS: Windows 10 (10.0)
#Word size of OS: 64-bit
#Word size of FreeCAD: 64-bit
#Version: 0.19.22209 (Git)
#Build type: Release
#Branch: master
#Hash: 9c3f9b72a82249d5fcf1f543dd69a78740251b26
#Python version: 3.6.8
#Qt version: 5.12.1
#Coin version: 4.0.0a
#OCC version: 7.3.0
#Locale: French/Mars (fr_MA)
#
#Icon.fromTheme by FreeCAD
#
__title__   = "Macro_Compound_Plus"
__author__  = "Mario52"
__url__     = "https://wiki.freecadweb.org/Macro_Compound_Plus"
__version__ = "0.04"
__date__    = "2020/08/15"    #YYYYMMDD
__icon__    = "https://wiki.freecadweb.org/images/f/fd/Macro_Compound_Plus.png"
__gistLoc__ = "https://gist.github.com/mario52a/7be361a8c489deec918f664fdcfc4394"
#
import PySide2
from PySide2 import (QtWidgets, QtCore, QtGui)
from PySide2.QtWidgets import (QWidget, QApplication, QSlider, QGraphicsView, QGraphicsScene, QVBoxLayout, QStyle)
from PySide2.QtGui import (QPainter, QColor, QIcon)
from PySide2.QtSvg import *
import PySide2.QtXml

import Draft, Part, PartGui, FreeCADGui, FreeCAD
from FreeCAD import Base
from FreeCAD import Vector
import math
from math import sqrt, pi, sin, cos, asin, degrees, radians

import re
import operator
from operator import itemgetter, attrgetter, methodcaller    # pour sort 
App = FreeCAD
Gui = FreeCADGui

import os, time, sys
import platform
import WebGui

global doc  ; doc = App.activeDocument()
global ui   ; ui         = ""

#### Test FreeCAD.Version simple ############################################################################################################
import WebGui
if int(FreeCAD.Version()[1]) < 19:      # Version de FreeCAD
    rawAddress = "https://gist.githubusercontent.com/mario52a/7be361a8c489deec918f664fdcfc4394/raw/11ae1a55229c84d9aab4e9a36099d90f52909958/Macro_Compound_Plus.FCMacro"
    FreeCAD.Console.PrintError("This version " + __title__ + " " + __version__ + " rmu  work with the FreeCAD 0.19 or higher." + "\n\n")
    FreeCAD.Console.PrintError("SOME FUNCTIONS MAY NOT WORK PROPERLY " + "\n\n")
    FreeCAD.Console.PrintError("For the precedent version (00.02) see the page " + "\n\n")
    FreeCAD.Console.PrintError(rawAddress + "\n\n")

    msg = ("This version " + __title__ + " " + __version__ + " rmu  work only with the FreeCAD 0.19 or higher." + "\n\n"
           "SOME FUNCTIONS MAY NOT WORK PROPERLY " + "\n\n"
           "For the precedent version click the button " + "\n\n")
    diag = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, __title__ + " " + __version__ , msg) #NoIcon, Information, Warning, Critical, Question
    diag.addButton(" See the raw page Compound Plus version 00.02 ", QtWidgets.QMessageBox.AcceptRole) #0
    diag.addButton(" Quit ", QtWidgets.QMessageBox.RejectRole)             #1
    diag.addButton(" Upgrade FreeCAD ", QtWidgets.QMessageBox.ActionRole)  #2
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    button = diag.exec_()
    if button == QtWidgets.QMessageBox.AcceptRole:
        WebGui.openBrowser(rawAddress)
    if button == 2: #ActionRole:
        WebGui.openBrowser("https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre")

#### Test FreeCAD.Version simple ############################################################################################################
global switchVersion; switchVersion = 0
try: 
    import draftmake    # only 0.19 for arc3points
    from draftmake.make_arc_3points import make_arc_3points
except Exception:
    switchVersion = 1

setIconTTF = [
"16 16 6 1",
"   c None",
".  c #204A87",
"+  c None",
"@  c #729FCF",
"#  c #CC0000",
"$  c #EDD400",
".+++++++++++@@@@",
".++++++++@+@++@@",
".++#####++++@@+@",
".+++$#$$$++@+@+@",
".++++#$+++++++@+",
".++++#$#####++++",
".++++#$+$#$$$+++",
".++++#$++#$+++++",
".@++++$++#$+###+",
".@@++++++#$+#$$$",
"..@@+++++#$+#$++",
"...@@+++++$+###+",
"....@@++++++#$$$",
".....@@+++++#$++",
"......@@+++++$++",
"................"]

setIconFON = [
"16 16 6 1",
"   c None",
".  c #204A87",
"+  c None",
"@  c #F57900",
"#  c #CC0000",
"$  c #EDD400",
".+++++++++++@@@@",
".++++++++@+@++@@",
".++###++++++@@+@",
".++#$$$++++@+@+@",
".++#$+++++++++@+",
".++###+###++++++",
".++#$$$#$#$+++++",
".++#$++#$#$+++++",
".@++$++#$#$##+#+",
".@@++++#$#$##$#$",
"..@@+++###$#$##$",
"...@@+++$$$#$##$",
"....@@+++++#$+#$",
".....@@++++#$+#$",
"......@@++++$++$",
"................"]

setIconOTF = [
"16 16 6 1",
"   c None",
".  c #204A87",
"+  c None",
"@  c #4E9A06",
"#  c #CC0000",
"$  c #EDD400",
".+++++++++++@@@@",
".++++++++@+@++@@",
".++###++++++@@+@",
".++#$#$++++@+@+@",
".++#$#$+++++++@+",
".++#$#$###++++++",
".++#$#$+#$$+++++",
".++###$+#$++++++",
".@++$$$+#$+###++",
".@@+++++#$+#$$$+",
"..@@++++#$+#$+++",
"...@@++++$+###++",
"....@@+++++#$$$+",
".....@@++++#$+++",
"......@@++++$+++",
"................"]

setIconPOL = [
"16 16 12 1",
"   c None",
".  c #204A87",
"+  c None",
"@  c #06989A",
"#  c #73D216",
"$  c #000000",
"%  c #75507B",
"&  c #729FCF",
"*  c #CC0000",
"=  c #F57900",
"-  c #EDD400",
";  c #4E9A06",
".+++++++++++@#$%",
".++++++++$+#++&$",
".++***++++++=@+%",
".++*-*-++++*+&+$",
".++*-*-+++++++*+",
".++***-***++++++",
".++*---*-*-+++++",
".++*-++*-*-+++++",
".$++-++*-*-*++++",
".*@++++*-*-*-+++",
"..#*+++***-*-+++",
"...;#+++---*-+++",
"....%=+++++*-+++",
".....;$++++****+",
"......@%++++",
"................"]

#path#################################################################
global path                                                          #
#path  = FreeCAD.ConfigGet("AppHomePath")                             # path FreeCAD installation
#path  = FreeCAD.ConfigGet("UserAppData")                             # path FreeCAD User data
#path  = "your path"                                                  # your directory path
param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro") # macro path
path  = param.GetString("MacroPath","") + "/"                        # macro path
path  = path.replace("\\","/")                                       # convert the "\" to "/"
#FreeCAD.Console.PrintMessage( "Path for the icons : " + path  + "\n")# 
######################################################################

#### matplotlib #################################################################
#import glob
#files_TTF = glob.glob(self.pathFont + "/*.TTF") 

##################################
import matplotlib
import matplotlib.font_manager
import matplotlib.font_manager as fontman
import matplotlib.font_manager as fontconfig
from matplotlib.font_manager import FontProperties

#from matplotlib.ft2font import FT2Font
##################################

global newPolicePath
global PolicePath
global nomPolice

if platform.system()   == "Windows" :
    PolicePath = "C:/Windows/Fonts/ARIAL.TTF"
elif platform.system() == "Linux" :
    PolicePath = "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf"
elif platform.system() == "Darwin":
    PolicePath = "/Library/Fonts/Arial.ttf"
else:
    PolicePath = "C:/Windows/Fonts/ARIAL.TTF"

nomPolice     = os.path.basename(PolicePath).split('.')[0]
newPolicePath = os.path.dirname(PolicePath).split('.')[0]

#### matplotlib #################################################################
#### Config Begin matplotlib font #######################
                                                        # # https://en.wikipedia.org/wiki/Web_colors
global setColorTTF       ; setColorTTF       = "blue"   # .TTF   color by "extension name" or hexa "#0000FF" 
global setColorFON       ; setColorFON       = "orange" # .FON   color by "extension name" or hexa "#FFA500"
global setColorOTF       ; setColorOTF       = "green"  # .OTF   color by "extension name" or hexa "#008000"
global setColorPOL       ; setColorPOL       = "black"  # .OTHER color by "extension name" or hexa "#000000"
                                                      #####
global switchModeTextList; switchModeTextList= 1        # 0 = mode text normal (et noir) coupe le switchFontComBox
                                                        # 1 = permet le switchFontComBox 1 (default)
                                                      #####
global switchFontComBox  ; switchFontComBox  = 1        # 0 = (et switchModeTextList= 1) mode texte (en couleur) dans liste ComboBox plus rapide
                                                        # 1 = (et switchModeTextList= 1) fontFamily dans liste ComboBox plus lent mais plus beau! (default)
                                                      #####
global setSystemFonts    ; setSystemFonts    = 1        # 0 = matplotlib.font_manager.findSystemFonts("C:/", "ttf") 
                                                        #     fait toutes les fontes (dans tous les dossiers et sous dossiers du DD) time !!
                                                        # 1 = fontman.findSystemFonts(self.pathFont)
                                                        #     fait toutes les fontes du repertoire (et dans tous les sous dossiers) (default)
                                                      #####
global seTtextAlignement ; seTtextAlignement = 0        # 0 = AlignLeft (default)
                                                        # 1 = AlignCenter
                                                        # 2 = AlignRight
                                                      #####
#### Config End matplotlib font #########################

#### matplotlib #################################################################

def createSpace(texte):    # detecte majuscule et ajoute un espace devant la lettre
    # return createSpace(TexTe) = Tex Te , if createSpace(TEXTE) = TEXTE
    if texte.isupper():
        stringSpace = texte
    else:
        try:
            stringSpace = texte[0]
            for i in texte[1:]:
                if re.search(r"[A-Z]", i): i = " " +  i
                stringSpace += i
        except Exception:
            stringSpace = texte
    return stringSpace

def family(chaine):
    # return family(chaine)[1] = Family , family(chaine)[2] = typeCar (form [a, b, c ...]
    famille = typeCar = ""
    try:
        if chaine.find('-') != -1:
            famille = chaine[:chaine.find('-')]
            typeCar = chaine[chaine.find('-')+1:]
        else:
            famille = chaine
            typeCar = ""
    except Exception:
        famille = chaine
        typeCar = ""
    typeCar = str(createSpace(typeCar)).split()
    return [createSpace(famille), typeCar]

class MyLabelPatience():        # fenetre image d'attente de chargement
    global path
    label = QtWidgets.QLabel()
    label.setText("<img src=" + path + "Macro_Compound_Plus.png><b><center>Wait please</center> \n\n<center>i search the fonts !\n\n</right></b>")
    ecran = FreeCADGui.getMainWindow().frameGeometry()
    xF = 250; yF = 120
    xW = (ecran.width()/2) - (xF/2)
    yW = (ecran.height()/2)- (yF/2)
    label.setGeometry(xW, yW, xF, yF)
    label.setStyleSheet("QLabel {background-color : #F0C300;font: 12pt; }");
    label.setWindowFlags(PySide2.QtCore.Qt.WindowFlags(PySide2.QtCore.Qt.FramelessWindowHint))        # pas de bords
    label.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint)         # PySide cette fonction met la fenetre en avant
#### matplotlib #################################################################

def unsignedDecode(value, mode = 0): # mode 0 = entier, mode 1 = float (a partir de ex: 4283773951)
                                     # 4283773951 = [255 85 51 255] = [red, green, blue, transparent]
    value = hex(value)
#    print(value)
    a1 = value[0:2]
    a2 = "000000000" + value[2:]
    a2 = a2[len(a2)-8:]
    value = a1 + a2
    if mode == 0:   # for button
        red         = int(value[2:4 ],16)
        green       = int(value[4:6 ],16)
        blue        = int(value[6:8 ],16)
        transparent = int(value[8:10],16)
    else:           # for FreeCAD object
        red         = float(int(value[2:4 ],16) / 255.0)
        green       = float(int(value[4:6 ],16) / 255.0)
        blue        = float(int(value[6:8 ],16) / 255.0)
        transparent = float(int(value[8:10],16) / 255.0)
    return [red, green, blue, transparent]

def unsignedEncode(red = 0, green = 0, blue = 0, transparent = 255): # convert red, green, blue, transparence to unique number
                                                                     #(255 *256*256*256 ) + (85 *256*256) + (51 *256) +(255) = 4283773951
    value = (red *256*256*256 ) + (green *256*256) + (blue *256) + (transparent)
    return value

#write parameter
#FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/FCMmacro/FCTexture").SetString("Path",pathFile)
#read parameter
#pathFile = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/FCMmacro/FCTexture").GetString("Path")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Ui_Compound(object):

    def __init__(self):
        global path
        global nomPolice

        self.path          = path
        self.nameL         = []
        self.comP          = []
        del        self.nameL[:]
        del         self.comP[:]

        self.lineWidth     = 0.0
        self.TextLabel     = ""
        self.TextLabelText = ""
        self.TextPosition  = ""
        self.TextFontSize  = 8.0
        self.TextTextColor = ""
        self.fonte         = ""
        self.fontSizeManual= False
        self.lineSizeManual= False

        ####font textEdit
        self.nomPolice     = "Arial"
        self.FontTextSize  = 20
        self.fonteComp     = ""
        self.font          = QtGui.QFont()
        ####font textEdit
        self.FontSize      = 0.0

        # for button
        self.red     = 255   #204.0
        self.green   = 0     #204.0
        self.blue    = 0     #204.0
        self.alpha   = 255   #255 = visibility max (opacity)

        # for object FC
        self.redFL   = 1.0
        self.greenFL = 0.0
        self.blueFL  = 0.0
        self.alphaFL = 1.0   # 1.0 = visibility max (opacity)

        self.tableau       = [] #Index (), [chemin plus nom fichier (nomPathPolice), nom sans extension (nomSimple), nomSimpleExt (nomSimple + Ext)]
        self.index         = 0  #Index ()

    #### font ######################
    def searchFont(self,pathSearch):
        global setSystemFonts
        global seTtextAlignement
        global switchFontComBox
        global switchModeTextList

        MyLabelPatience.label.show()
        FreeCADGui.updateGui()                                 # rafraichi l'ecran

        files_All_Fonts = ""
        ##https://matplotlib.org/_modules/matplotlib/font_manager.html
        if setSystemFonts == 0:
            files_All_Fonts = matplotlib.font_manager.findSystemFonts(pathSearch, "ttf")  # fait toutes les fontes ? ()
        else:
            files_All_Fonts = fontman.findSystemFonts(pathSearch)                         # fait toutes les fontes (et dans tous les sous dossiers)

        if len(files_All_Fonts) > 0:           
            self.tableau = []
            self.index = 0

            for fonte in files_All_Fonts:
                ####
                nomPathPolice = nomFichier = nomSimpleExt = nomSimple = nomExtension = nameName = ""

                nomPathPolice = fonte.replace("\\","/")     # convert the "\" to "/"
                nomFichier    = nomPathPolice.split("/")    # complet split
                nomSimpleExt  = nomFichier[-1]              # nom avec extension
                nomSimple     = nomFichier[-1][:-4]         # nom sans extension
                nomExtension  = nomSimpleExt[nomSimpleExt.rfind('.')+1:].upper() # extension
                ####
                try:
#                    nameFamily    = matplotlib.font_manager.FontProperties(fname=fonte).get_family()            ##['sans-serif']
#                    nameStyle     = matplotlib.font_manager.FontProperties(fname=fonte).get_style()              #normal
#                    nameVariant   = matplotlib.font_manager.FontProperties(fname=fonte).get_variant()            #normal
#                    nameWeight    = matplotlib.font_manager.FontProperties(fname=fonte).get_weight()             #normal
#                    nameStretch   = matplotlib.font_manager.FontProperties(fname=fonte).get_stretch()            #normal
#                    nameFileComp  = matplotlib.font_manager.FontProperties(fname=fonte).get_file()              ##c:\windows\fonts\NotoNaskhArabicUI-Regular.ttf
#                    nameSize      = matplotlib.font_manager.FontProperties(fname=fonte).get_size()               #10.0
                    nameName      = matplotlib.font_manager.FontProperties(fname=fonte).get_name()              ##Noto Naskh Arabic UI
#                    nameSizePoint = matplotlib.font_manager.FontProperties(fname=fonte).get_size_in_points()     #10.0
#                    nameSlant     = matplotlib.font_manager.FontProperties(fname=fonte).get_slant()              #normal
#                    namePattern   = matplotlib.font_manager.FontProperties(fname=fonte).get_fontconfig_pattern() #:family=sans-serif:style=normal:variant=normal:weight=normal:stretch=normal:file=c:\windows\fonts\NotoNaskhArabicUI-Regular.ttf:size=10.0
                except Exception:
                    nameFamily = nameStyle = nameVariant = nameWeight = nameStretch = nameFileComp = nameSize = nameName = nameSizePoint = nameSlant = namePattern = ""
                ####
                if nameName == "" :
                    nameName = nomSimple
                self.tableau.append([0, nomPathPolice, nomSimple, nomSimpleExt.upper(), nomExtension.upper(), nameName])
                
            self.tableau = sorted(self.tableau, key=itemgetter(3))          # sorted by nomSimple.upper()

            try:
                for line in range(len(self.tableau)):                       # enleve les doubles (bon)
                    if self.tableau[line][2] == self.tableau[line + 1][2]:  # enleve les doubles (bon)
                        del(self.tableau[line + 1])                         # enleve les doubles (bon)
            except Exception:
                None

            self.comboBoxPy.clear()
            for line in range(len(self.tableau)): 
                try:
                    self.tableau[line][0] = line                 # ajoute le numero de ligne
                    if self.tableau[line][2].upper() == "ARIAL": # detecte la fonte de base
                        self.index = line                ####Section common color and font begin ######################
                    model = self.comboBoxPy.model()

                    if switchModeTextList == 1:
                        if self.tableau[line][4] == "TTF":
                            item = QtGui.QStandardItem(QtGui.QPixmap(setIconTTF), str(line))
                            item.setForeground(QtGui.QColor(setColorTTF))
                        elif self.tableau[line][4] == "FON":
                            item = QtGui.QStandardItem(QtGui.QPixmap(setIconFON), str(line))
                            item.setForeground(QtGui.QColor(setColorFON))
                        elif self.tableau[line][4] == "OTF":
                            item = QtGui.QStandardItem(QtGui.QPixmap(setIconOTF), str(line))
                            item.setForeground(QtGui.QColor(setColorOTF))
                        else:
                            item = QtGui.QStandardItem(QtGui.QPixmap(setIconPOL), str(line))
                            item.setForeground(QtGui.QColor(setColorPOL))

                        if   seTtextAlignement == 0:
                            item.setTextAlignment(QtCore.Qt.AlignLeft)
                        elif seTtextAlignement == 1:
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                        elif seTtextAlignement == 2:
                            item.setTextAlignment(QtCore.Qt.AlignRight)
                        else:
                            self.comboBoxPy.addItem(self.tableau[line][2])    
                        model.appendRow(item)
                    else:
                        self.comboBoxPy.addItem("")
                    self.comboBoxPy.setItemText(line, self.tableau[line][2])
                    ####Section item color and font end ##########################                ####Section setfont Family switchFontComBox begin#############
                    if (switchFontComBox == 1) and (switchModeTextList == 1):
                        typeCar = font = ""
                        font = QtGui.QFont()
                        #font = item.font()
        
                        typeCar   = family(self.tableau[line][2])[1]
                        font.setBold(False)
                        font.setItalic(False)
        
                        if len(typeCar) > 0:
                            for option in typeCar:
                                if option == "Bold":
                                    font.setBold(True)
                                if (option == "Italic") or (option == "It") or (option == "Slanted"):
                                    font.setItalic(True)
                                if option == "Oblique":
                                    font.setItalic(True)
                        #'Bold''Regular''Slanted''Italic''Medium''Extra''Light''Condensed''Black''It''Semibold'
                        
                        font.setFamily(self.tableau[line][5])
                        font.setPixelSize(15)
                        if switchModeTextList == 1:
                            item.setFont(font)
                        else:
                            self.comboBoxPy.addItem("")
                    ####Section setfont Family switchFontComBox end###############

                except Exception:
                    FreeCAD.Console.PrintMessage("searchFont()" + "\n")
                    None
            self.lineEdit_NameFile.setText("(" + str(self.index + 1) + "/" + str(len(self.tableau)) + ") " + self.tableau[self.index][1])
            #print(len(self.tableau))
            #for i in self.tableau:
            #    print(i)
            self.comboBoxPy.setCurrentIndex(self.index)
            self.fonteComp = self.tableau[self.index][1]
            MyLabelPatience.label.close()

    #### font ######################

    def setupUi(self, MainWindow):
        global PolicePath
        global setSystemFonts
        global setColorTTF
        global setColorFON
        global setColorOTF
        global setColorPOL
        global seTtextAlignement
        global switchFontComBox
        global switchModeTextList
        global ui

        self.window = MainWindow

        Compound.setObjectName("Compound")
        Compound.resize(250, 440)
#        MainWindow.setMinimumSize(QtCore.QSize(250, 440))
#        MainWindow.setMaximumSize(QtCore.QSize(250, 440))

        self.centralwidget = QtWidgets.QWidget(Compound)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox()

        self.groupBox_Choice = QtWidgets.QGroupBox()

        self.PB_01_Compound_01 = QtWidgets.QPushButton()
        self.PB_01_Compound_01.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Part_Compound.svg")))
        self.PB_01_Compound_01.clicked.connect(self.on_PB_01_Compound_01)                    # 

        self.label_02_Type_1 = QtWidgets.QLabel()

        self.PB_02_Compound_02 = QtWidgets.QPushButton()
        self.PB_02_Compound_02.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Part_Compound.svg")))
        self.PB_02_Compound_02.clicked.connect(self.on_PB_02_Compound_02)                    # 

        self.label_03_Type_2 = QtWidgets.QLabel()
        ####

        self.groupBox_00 = QtWidgets.QGroupBox()
#        self.groupBox_00.setAlignment(QtWidgets.AlignLeft)                    # AlignLeft     AlignCenter      AlignRight
        self.groupBox_00.setCheckable(True)
        self.groupBox_00.setChecked(False)
        self.groupBox_00.clicked.connect(self.on_groupBox_00)                  # 

        self.PB_03_Color = QtWidgets.QPushButton()
        self.PB_03_Color.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/colors.svg")))
        self.PB_03_Color.clicked.connect(self.on_PB_03_Color)                                # 
        self.PB_03_Color.setStyleSheet("background-color: rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")")
        ####

        self.groupBox_Tools = QtWidgets.QGroupBox()

        self.lineEdit_NameFile = QtWidgets.QLineEdit()
        self.comboBoxPy = QtWidgets.QComboBox()
        ####
        #self.pathFont = PolicePath[:-10]
        self.pathFont = PolicePath[:len(PolicePath)-(PolicePath[::-1].index("/"))-1]
        ####

        self.PB_04_Convert_Text = QtWidgets.QPushButton()
        self.PB_04_Convert_Text.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_Text.svg")))
        self.PB_04_Convert_Text.clicked.connect(self.on_PB_04_Convert_Text)                            # ""

        ui.searchFont(self.pathFont)
        QtCore.QObject.connect(self.comboBoxPy, QtCore.SIGNAL("currentIndexChanged(int)"), self.on_fontComboBoxPython)

        self.DS_02_Size_Font = QtWidgets.QDoubleSpinBox()
        self.DS_02_Size_Font.setValue(0.0)
        self.DS_02_Size_Font.setSuffix(" Auto")
        self.DS_02_Size_Font.valueChanged.connect(self.on_DS_02_Size_Font_valueChanged)             # 

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.PB_04c_Convert_Edge = QtWidgets.QPushButton()
        self.PB_04c_Convert_Edge.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_Line.svg")))
        self.PB_04c_Convert_Edge.clicked.connect(self.on_PB_04c_Convert_Edge)                 # ""

        self.DS_01_Width_Line = QtWidgets.QDoubleSpinBox()
        self.DS_01_Width_Line.setValue(0.0) #self.lineWidth
        self.DS_01_Width_Line.setSuffix(" Auto")
        self.DS_01_Width_Line.valueChanged.connect(self.on_DS_01_Width_Line_valueChanged)             # 

        self.CB_BezierCurve = QtWidgets.QCheckBox()
        self.CB_BezierCurve.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_BezCurve.svg")))
        self.CB_BezierCurve.clicked.connect(self.on_CB_BezierCurve_clicked)

        self.RB_01_FlatLines = QtWidgets.QRadioButton()
        self.RB_01_FlatLines.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/DrawStyleFlatLines.svg")))
        self.RB_01_FlatLines.setChecked(True)
        self.RB_02_Wireframe = QtWidgets.QRadioButton()
        self.RB_02_Wireframe.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/DrawStyleWireFrame.svg")))
        self.RB_03_Points = QtWidgets.QRadioButton()
        self.RB_03_Points.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/DrawStylePoints.svg")))
        ####

        self.groupBox_Force_LAC = QtWidgets.QGroupBox()

        self.PB_Force_LAC = QtWidgets.QPushButton()
        self.PB_Force_LAC.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Line.svg")))
        self.PB_Force_LAC.clicked.connect(self.on_PB_Force_LAC)                 # ""

        self.RB_Force_01_Line = QtWidgets.QRadioButton()
        self.RB_Force_01_Line.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Line.svg")))
        self.RB_Force_01_Line.setChecked(True)
        self.RB_Force_01_Line.clicked.connect(self.on_RB_Force_clicked)
        self.RB_Force_02_Arc = QtWidgets.QRadioButton()
        self.RB_Force_02_Arc.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Arc.svg")))
        self.RB_Force_02_Arc.clicked.connect(self.on_RB_Force_clicked)
        if switchVersion == 1:
            self.RB_Force_02_Arc.setEnabled(False)
        self.RB_Force_03_Circle = QtWidgets.QRadioButton()
        self.RB_Force_03_Circle.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Circle.svg")))
        self.RB_Force_03_Circle.clicked.connect(self.on_RB_Force_clicked)
       ####

        self.groupBox_01 = QtWidgets.QGroupBox()

        self.RB_01_Default = QtWidgets.QRadioButton()
        self.RB_01_Default.setChecked(True)
        self.RB_02_Hidden = QtWidgets.QRadioButton()
        self.RB_03_Delete = QtWidgets.QRadioButton()
        self.RB_03_Delete.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))) #
#        self.RB_03_Delete.setChecked(True)

        self.PB_09_Upgrade = QtWidgets.QPushButton()
        self.PB_09_Upgrade.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_Upgrade.svg")))
        self.PB_09_Upgrade.clicked.connect(self.on_PB_09_Upgrade)                       # 

        self.PB_06_Downgrade = QtWidgets.QPushButton()
        self.PB_06_Downgrade.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_Downgrade.svg")))
        self.PB_06_Downgrade.clicked.connect(self.on_PB_06_Downgrade)                       # 

        self.groupBox_Command = QtWidgets.QGroupBox()

        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)

        self.PB_05_Reset = QtWidgets.QPushButton()
        self.PB_05_Reset.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogResetButton))) #
        self.PB_05_Reset.clicked.connect(self.on_PB_05_Reset)                               # 

        self.PB_07_Quit = QtWidgets.QPushButton()
        self.PB_07_Quit.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))) #
        self.PB_07_Quit.clicked.connect(self.on_PB_07_Quit)                                 # 

        self.PB_08_Help = QtWidgets.QPushButton()
        self.PB_08_Help.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion))) #
        self.PB_08_Help.clicked.connect(self.on_PB_Help_clicked)                                 # 

        #### layout ###################################################
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Choice)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.addWidget(self.PB_01_Compound_01, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_02_Type_1, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.PB_02_Compound_02, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_03_Type_2, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Choice, 0, 0, 1, 1)

        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_00)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.addWidget(self.PB_03_Color, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_00, 1, 0, 1, 1)

        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_Tools)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_5.addWidget(self.lineEdit_NameFile, 0, 0, 1, 3)
        self.gridLayout_5.addWidget(self.comboBoxPy, 1, 0, 1, 3)
        self.gridLayout_5.addWidget(self.PB_04_Convert_Text, 2, 0, 1, 2)
        self.gridLayout_5.addWidget(self.DS_02_Size_Font, 2, 2, 1, 1)
        self.gridLayout_5.addWidget(self.line, 3, 0, 1, 3)
        self.gridLayout_5.addWidget(self.PB_04c_Convert_Edge, 4, 0, 1, 2)
        self.gridLayout_5.addWidget(self.DS_01_Width_Line, 4, 2, 1, 1)
        self.gridLayout_5.addWidget(self.CB_BezierCurve, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.RB_01_FlatLines, 6, 0, 1, 1)
        self.gridLayout_5.addWidget(self.RB_02_Wireframe, 6, 1, 1, 1)
        self.gridLayout_5.addWidget(self.RB_03_Points, 6, 2, 1, 1)
        self.gridLayout_5.addWidget(self.PB_09_Upgrade, 7, 0, 1, 1)
        self.gridLayout_5.addWidget(self.PB_06_Downgrade, 7, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Tools, 2, 0, 1, 1)

        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_01)
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_7.addWidget(self.RB_01_Default, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.RB_02_Hidden, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.RB_03_Delete, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_01, 3, 0, 1, 1)

        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_Force_LAC)
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_8.addWidget(self.PB_Force_LAC, 0, 0, 1, 3)
        self.gridLayout_8.addWidget(self.RB_Force_01_Line, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.RB_Force_02_Arc, 1, 1, 1, 1)
        self.gridLayout_8.addWidget(self.RB_Force_03_Circle, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Force_LAC, 4, 0, 1, 1)

        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_Command)
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_6.addWidget(self.progressBar, 0, 0, 1, 3)
        self.gridLayout_6.addWidget(self.PB_05_Reset, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.PB_07_Quit, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.PB_08_Help, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Command, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        #### layout ###################################################

        Compound.setCentralWidget(self.centralwidget)

        self.retranslateUi(Compound)
        QtCore.QMetaObject.connectSlotsByName(Compound)

    def retranslateUi(self, Compound):
        Compound.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint)                    # PySide cette fonction met la fenetre en avant
        Compound.setWindowIcon(QtGui.QIcon(self.path + 'Macro_Compound_Plus.png'))         # change l'icone de la fenetre principale
        Compound.setWindowTitle("Compound +")

        self.groupBox.setTitle("Version : " + __date__ + " : " + __version__)

        self.groupBox_Choice.setTitle("Choice")
        self.PB_01_Compound_01.setText("Compound I")
        self.PB_01_Compound_01.setToolTip("Make a compound Block unique")
        self.PB_02_Compound_02.setText("Compound II")
        self.PB_02_Compound_02.setToolTip("Make a compound same Part, Menu > Part > Make compound")
        self.label_02_Type_1.setText("Type I [ 1 + 1 = 1 ]")
        self.label_03_Type_2.setText("Type II [ 1 + 1 = A (1 + 1) ]")

        self.groupBox_00.setTitle("Option color")
        self.groupBox_00.setToolTip("If this box is unchecked the colors attributes and width line\n"
                                    "of the original line(s) are not modified\n"
                                    "This chekBox work with all objects\n")
        self.PB_03_Color.setText("Color")
        self.PB_03_Color.setToolTip("Change the color of object(s) selected(s) value by defaut rvb 255,0,0")

        self.groupBox_Tools.setTitle("Tools")

        self.lineEdit_NameFile.setToolTip("(Number index / Number Fonts) Complete path and name of Font file")

        self.comboBoxPy.setToolTip("Choice your Font" + "\n" +
                                   "\n" +
                                   "You must modify the configuration of display" + "\n" +
                                   "See in the beginning of the macro section (line 120):" + "\n" +
                                   "####" + "\n" +
                                   "Config Begin matplotlib font" + "\n" 
                                   "switchModeTextList= 1\t# 0 = mode text normal (the switchFontComBox is enabled)" + "\n"
                                   "\t\t\t# 1 = switchFontComBox authorized (default)" + "\n"
                                   "\t\t\t#####" + "\n"
                                   "switchFontComBox  = 1\t# 0 = mode text in color .. faster" + "\n"
                                   "\t\t\t# 1 = fontFamily listed ComboBox slower but beautiful (default)" + "\n"
                                   "\t\t\t#####" + "\n"
                                   "setSystemFonts    = 1\t# 0 = matplotlib.font_manager.findSystemFonts" + "\n"
                                   "\t\t\t#   all fonts in System font" + "\n"
                                   "\t\t\t# 1 = fontman.findSystemFonts(self.pathFont) (default)" + "\n"
                                   "\t\t\t# all fonts in all directory and sub directory" + "\n"
                                   "\t\t\t#####" + "\n"
                                   "seTtextAlignement = 0\t# 0 = AlignLeft (default)" + "\n"
                                   "\t\t\t# 1 = AlignCenter" + "\n"
                                   "\t\t\t# 2 = AlignRight" + "\n"
                                   "\t\t\t#####" + "\n"
                                   "Config End matplotlib font" + "\n"
                                   "####" + "\n" +
                                   "Read the info")
        self.PB_04_Convert_Text.setText("Convert Text (A)")
        self.PB_04_Convert_Text.setToolTip("Convert the selected text in ShapeString\n"
                                           "By default Convert (A)utomatic use the font preselected and the size of original text\n"
                                           "If the values or font is modified the button change of Convert (M)anual\n"
                                           "The label of the texte are modified to SString_original text (max 30 characters)")
        self.DS_02_Size_Font.setToolTip("Size of the font of the ShapeString")
        self.PB_04c_Convert_Edge.setText("Convert Wire (A)")
        self.PB_04c_Convert_Edge.setToolTip("Convert the wire to object Draft" + "\n"
                                            "Select the wire(s) in the 3D view" + "\n\n"
                                            "Are detected : Line, Circle, Arc, Ellipse, BSplineCurve" + "\n"
                                            "BezierCurve, BezierCurve Cubic (if checked)" + "\n\n"
                                            "If the Surface or Point or other wire unknown are detected," + "\n"
                                            "the selection Object is duplicated" + "\n"
                                            "If the values is modified the button change of Convert (M)anual\n")
        self.DS_01_Width_Line.setToolTip("Give a new width for the line(s) selected(s)")
        self.CB_BezierCurve.setText("BezierCurve")
        self.CB_BezierCurve.setToolTip("If checked the BezierCurve is Cubic")

        self.RB_01_FlatLines.setText("FlatLines")
        self.RB_01_FlatLines.setToolTip("FlatLines")
        self.RB_02_Wireframe.setText("Wireframe")
        self.RB_02_Wireframe.setToolTip("Wireframe")
        self.RB_03_Points.setText("Points")
        self.RB_03_Points.setToolTip("Points")

        self.PB_09_Upgrade.setText("UpGrade")
        self.PB_09_Upgrade.setToolTip("Upgrade the selected object Same Draft > Upgrade")
        self.PB_06_Downgrade.setText("DownGrade")
        self.PB_06_Downgrade.setToolTip("Downgrade the selected object Same Draft > Downgrade")

        self.groupBox_01.setTitle("For Compound I and Convert")
        self.RB_01_Default.setText("None")
        self.RB_01_Default.setToolTip("The object stay as is\n"
                                      "For Compound I and Convert text to String")
        self.RB_02_Hidden.setText("Hidden original object(s) ")
        self.RB_02_Hidden.setToolTip("The original object are hidden after transform\n"
                                     "For Compound I and Convert text to String")
        self.RB_03_Delete.setText("Delete original object(s)")
        self.RB_03_Delete.setToolTip("The original object are deleted after transform\n"
                                     "For Compound I and Convert text to String")

        self.groupBox_Force_LAC.setTitle("Force on a form : Line")
        self.groupBox_Force_LAC.setToolTip("This section lets you choose the shape.\n"
                                           "Force the creation of the object, Line, Arc or Circle\n"
                                           "(in the case of non-satisfaction of creation in the Tools section)\n" 
                                           "No verification is made on the selection.\n"
                                           "You have to choose the shape that will be created,\n"
                                           "only one verification in the possibility of creation of the object is made,\n"
                                           "according to the detected coordinates")
        self.PB_Force_LAC.setText("Force on : Line")
        self.RB_Force_01_Line.setText("Line")
        self.RB_Force_01_Line.setToolTip("Force on Line if possible")
        self.RB_Force_02_Arc.setText("Arc")
        self.RB_Force_02_Arc.setToolTip("Force on Arc if possible")
        self.RB_Force_03_Circle.setText("Circle")
        self.RB_Force_03_Circle.setToolTip("Force on Circle if possible")

        self.groupBox_Command.setTitle("Command")
        self.PB_05_Reset.setText("Reset")
        self.PB_05_Reset.setToolTip("Reset the values")
        self.PB_07_Quit.setText("Quit")
        self.PB_07_Quit.setToolTip("Quit Compound +")
        self.PB_08_Help.setText("Help")
        self.PB_08_Help.setToolTip("Quit Compound +")

    def on_fontComboBoxPython(self,indeX):                                          # 0: for fontComboBoxPython
        global PolicePath

        self.index = indeX
        self.lineEdit_NameFile.setText("(" + str(self.index + 1) + "/" + str(len(self.tableau)) + ") " + self.tableau[self.index][1])
        PolicePath = self.tableau[self.index][1]

        famille = typeCar = self.font = ""
        self.font = QtGui.QFont()
        typeCar   = family(self.tableau[self.index][2])[1]
        self.font.setBold(False)
        self.font.setItalic(False)

        if len(typeCar) > 0:
            for option in typeCar:
                if option == "Bold":
                    self.font.setBold(True)
                if (option == "Italic") or (option == "It") or (option == "Slanted"):
                    self.font.setItalic(True)
                if option == "Oblique":
                    self.font.setItalic(True)
        #'Bold''Regular''Slanted''Italic''Medium''Extra''Light''Condensed''Black''It''Semibold'#+
        
        self.font.setFamily(self.tableau[self.index][5])
        self.font.setPointSize(self.FontTextSize)
        ####
        self.fonteComp = self.tableau[self.index][1]
#        FreeCAD.Console.PrintMessage(str(self.index) + " , " + self.tableau[self.index][1] + " , " + self.tableau[self.index][2] + " , ' " + famille + "' , ' " + typeCar + " ' \n")

    def on_PB_newPathFont(self):
        global ui
        global newPolicePath
        global setSystemFonts

        newPolicePath = str(PySide2.QtWidgets.QFileDialog.getExistingDirectory(None, "Select new font directory", newPolicePath, PySide2.QtWidgets.QFileDialog.ShowDirsOnly))
        if newPolicePath:
            MyLabelPatience.label.show()
            FreeCADGui.updateGui()                             # rafraichi l'ecran
            ui.searchFont(newPolicePath)
            setSystemFonts = 1
            MyLabelPatience.label.close()

    def on_PB_systemPath(self):
        global ui
        global setSystemFonts

        MyLabelPatience.label.show()
        FreeCADGui.updateGui()                                 # rafraichi l'ecran
        setSystemFonts = 0
        ui.searchFont(self.pathFont)
        MyLabelPatience.label.close()

    def on_PB_01_Compound_01(self):
        global doc
        
        self.selectionObjects = FreeCADGui.Selection.getSelection()
        if len(self.selectionObjects) > 0:
            try:
                self.nameL         = []
                self.comP          = []
                del        self.nameL[:]
                del         self.comP[:]

                self.progressBar.setMaximum(len(self.selectionObjects))
                compteur = 0
                for i in self.selectionObjects:
                    self.nameL.append(i.Name)
                    self.comP.append(i.Shape)
                    compteur += 1
                    self.progressBar.setValue(compteur)
                    Gui.updateGui()
                    print( "Object : ",i.Name)

                comp = Part.makeCompound(self.comP)
                Part.show(comp)

                if self.groupBox_00.isChecked():
                    FreeCADGui.ActiveDocument.ActiveObject.LineWidth  = self.lineWidth
                    FreeCADGui.ActiveDocument.ActiveObject.LineColor  = (self.redFL, self.greenFL, self.blueFL)
                    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (self.redFL, self.greenFL, self.blueFL)
                    FreeCADGui.ActiveDocument.ActiveObject.PointColor = (self.redFL, self.greenFL, self.blueFL)

                App.ActiveDocument.ActiveObject.Label = "reproShape_T_I"
        
                if self.RB_01_Default.isChecked():
                    None
                if self.RB_02_Hidden.isChecked():
                    for i in range(len(self.nameL)):
                        print( "Hidden : ",self.nameL[i])
                        FreeCADGui.ActiveDocument.getObject(self.nameL[i]).Visibility = False
                try:
                    if self.RB_03_Delete.isChecked():
                        for i in range(len(self.nameL)):
                            print( "Delete : ",self.nameL[i])
                            doc.removeObject(self.nameL[i])
                except Exception:
                    FreeCAD.Console.PrintError("Error Delete : ",self.nameL[i] + "\n")
                
            except Exception:
                FreeCAD.Console.PrintError("Error objects "+"\n")
            self.progressBar.setValue(0)
            FreeCAD.ActiveDocument.recompute()
        else:
            FreeCAD.Console.PrintError("Not objects selected "+"\n")
#        FreeCAD.Console.PrintMessage(str("on_PB_01_Compound_01 ")+"\n")

    def on_PB_02_Compound_02(self):
        self.selectionObjects = FreeCADGui.Selection.getSelection()
        if len(self.selectionObjects) > 0:
            try:
                self.nameL         = []
                self.comP          = []
                del        self.nameL[:]
                del         self.comP[:]
                
                App.activeDocument().addObject("Part::Compound","Compound")
                
                self.progressBar.setMaximum(len(self.selectionObjects))
                compteur = 0
                for i in self.selectionObjects:
                    self.nameL.append(App.ActiveDocument.getObject(i.Name))
                    compteur += 1
                    self.progressBar.setValue(compteur)
                    Gui.updateGui()
                    print( i.Name)
                App.activeDocument().Compound.Links = self.nameL
                App.activeDocument().recompute()

                if self.groupBox_00.isChecked():
                    FreeCADGui.ActiveDocument.ActiveObject.LineWidth  = self.lineWidth
                    FreeCADGui.ActiveDocument.ActiveObject.LineColor  = (self.redFL, self.greenFL, self.blueFL)
                    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (self.redFL, self.greenFL, self.blueFL)
                    FreeCADGui.ActiveDocument.ActiveObject.PointColor = (self.redFL, self.greenFL, self.blueFL)
                # else:
                    # FreeCADGui.ActiveDocument.ActiveObject.LineWidth  = 
                    # FreeCADGui.ActiveDocument.ActiveObject.LineColor  = 
                    # FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = 
                    # FreeCADGui.ActiveDocument.ActiveObject.PointColor = 
                
                App.ActiveDocument.ActiveObject.Label = "reproShape_T_II"
        
            except Exception:
                FreeCAD.Console.PrintError("Error objects "+"\n")
            self.progressBar.setValue(0)
            FreeCAD.ActiveDocument.recompute()
        else:
            FreeCAD.Console.PrintError("Not objects selected "+"\n")
#        FreeCAD.Console.PrintMessage(str("on_PB_02_Compound_02 ")+"\n")

    def on_PB_03_Color(self):
        #p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")
        #print( p.GetUnsigned("DefaultShapeLineColor"))
        self.PB_03_Color.setStyleSheet("background-color: QPalette.Base")        # origin system
        self.window.hide()                                                       # hide the window open color
        couleur = QtWidgets.QColorDialog.getColor()
        
        if couleur.isValid():
            self.red   = int(str(couleur.name()[1:3]),16)
            self.green = int(str(couleur.name()[3:5]),16)
            self.blue  = int(str(couleur.name()[5:7]),16)

            self.redFL   = float(couleur.redF())
            self.greenFL = float(couleur.greenF())
            self.blueFL  = float(couleur.blueF())
            self.alphaFL = float(couleur.alphaF())
            self.PB_03_Color.setStyleSheet("background-color: rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")")

        self.window.show()                                                        # show the window and close color
#        FreeCAD.Console.PrintMessage(str("PB_03_Color ")+"\n")

    def on_PB_04_Convert_Text(self):        # convert Text to ShapeString
        global PolicePath
        global doc
        
        self.selectionObjects = FreeCADGui.Selection.getSelection()
        self.progressBar.setMaximum(len(self.selectionObjects))
        compteur = 0
        if len(self.selectionObjects) > 0:
            #objA = self.selectionObjects[0]
            for objA in self.selectionObjects:

                try:
                    self.TextLabel     = objA.Label
                    self.TextLabelText = objA.Text[0]      #0.19
                    self.TextPosition  = objA.Placement    #0.19
                    self.TextFontSize  = objA.ViewObject.FontSize 

                    if self.fontSizeManual:
                        self.TextFontSize = self.FontSize

                    self.TextTextColor = objA.ViewObject.TextColor
                    texte = self.TextLabelText #0.19

                    ss=Draft.makeShapeString(String = texte, FontFile=PolicePath, Size=float(self.TextFontSize), Tracking=0)

                    if self.RB_01_FlatLines.isChecked():
                        ss.ViewObject.DisplayMode = u"Flat Lines"
                    if self.RB_02_Wireframe.isChecked():
                        ss.ViewObject.DisplayMode = u"Wireframe"
                    if self.RB_03_Points.isChecked():
                        ss.ViewObject.DisplayMode = u"Points"

                    plm  = self.TextPosition
                    ss.Placement=plm
                    ss.Support=None
                    ss.Label = "SString_"+texte[:30]
                    if self.groupBox_00.isChecked():
                        #### imposted colors
                        FreeCADGui.ActiveDocument.getObject(ss.Name).ShapeColor = (self.redFL, self.greenFL, self.blueFL)
                        FreeCADGui.ActiveDocument.getObject(ss.Name).LineColor  = (self.redFL, self.greenFL, self.blueFL)
                        FreeCADGui.ActiveDocument.getObject(ss.Name).PointColor = (self.redFL, self.greenFL, self.blueFL)
                    else:
#                        #### preferences colors
#                        r, b, g, t = unsignedDecode(FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").GetUnsigned("DefaultShapeColor"),1)
#                        FreeCADGui.ActiveDocument.getObject(ss.Name).ShapeColor = (r, b, g, t)
#                        r, b, g, t = unsignedDecode(FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").GetUnsigned("DefaultShapeLineColor"),1)
#                        FreeCADGui.ActiveDocument.getObject(ss.Name).LineColor  = (r, b, g, t)
#                        r, b, g, t = unsignedDecode(FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").GetUnsigned("DefaultShapeVertexColor"),1)
#                        FreeCADGui.ActiveDocument.getObject(ss.Name).PointColor = (r, b, g, t)

                        #### original object colors
                        FreeCADGui.ActiveDocument.getObject(ss.Name).ShapeColor = objA.ViewObject.TextColor
                        FreeCADGui.ActiveDocument.getObject(ss.Name).LineColor  = objA.ViewObject.LineColor
                        ##FreeCADGui.ActiveDocument.getObject(ss.Name).LineWidth  = objA.ViewObject.LineWidth
                        
                    compteur += 1
                    self.progressBar.setValue(compteur)

                    if self.RB_01_Default.isChecked():
                        None
                    if self.RB_02_Hidden.isChecked():
                        print( "Hidden : ",objA.Name)
                        FreeCADGui.ActiveDocument.getObject(objA.Name).Visibility = False
                    try:
                        if self.RB_03_Delete.isChecked():
                            print( "Delete : ",objA.Name)
                            doc.removeObject(objA.Name)
                    except Exception:
                        FreeCAD.Console.PrintError("Error Delete : ",objA.Name + "\n")

                    Gui.updateGui()
                except Exception:
                    FreeCAD.Console.PrintError("Not object TEXT or error" + "\n")

            self.progressBar.setValue(0)
            FreeCAD.ActiveDocument.recompute()
        else:
            FreeCAD.Console.PrintError("Select one or more objects TEXT" + "\n")
#        FreeCAD.Console.PrintMessage(str("on_PB_04_Convert_Text ")+"\n")

    def on_DS_02_Size_Font_valueChanged(self,value):
                        
        
        self.FontSize = value
        if self.FontSize != 0:
            self.PB_04_Convert_Text.setText("Convert Text (M)")
            self.DS_02_Size_Font.setSuffix(" mm Size")
            self.fontSizeManual = True
        else:
            self.PB_04_Convert_Text.setText("Convert Text (A)")
            self.DS_02_Size_Font.setSuffix(" Auto")
            self.fontSizeManual = False
        #App.Console.PrintMessage("New FontSize " + str(self.FontSize)+"\n")

    def on_PB_04c_Convert_Edge(self):                                                    # Convert Edge to line
        self.selectionObjects = FreeCADGui.Selection.getSelectionEx()                    # Select an object or sub object
        self.progressBar.setMaximum(len(self.selectionObjects))
        compteur = 0
        for selection in self.selectionObjects:
            nameObject = selection.Object.Name
            countSubName = 0
            for selectedEdge in selection.SubObjects:
                subName = selection.SubElementNames[countSubName]
                compteur += 1
                self.progressBar.setValue(compteur)
                if (hasattr(selectedEdge,"Surface")) or (hasattr(selectedEdge,"Point")):
                    Part.show(selectedEdge.copy())                                       # create repro shape subObject
                    FreeCAD.Console.PrintMessage("Object Point or Surface duplicated !!" + "\n")
                    FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(Copy)"
                else:
                    try:
                        s = selectedEdge
                        if str(s.Curve) == "<Ellipse object>":                           # Ellipse
                            FreeCAD.Console.PrintMessage("Detected : Ellipse" + "\n")
                            pl=FreeCAD.Placement()
                            pl.Rotation = FreeCAD.Rotation(s.Curve.XAxis, s.Curve.YAxis, s.Curve.Axis, "ZXY")
                            pl.Base     = s.Curve.Center
                            ellipse = Draft.makeEllipse(s.Curve.MajorRadius, s.Curve.MinorRadius, placement=pl, face=False, support=None)
                            FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(Ellipse)"
                            edge  = selectedEdge
                            ellipse.FirstAngle = degrees(edge.FirstParameter)
                            ellipse.LastAngle  = degrees(edge.LastParameter)
                            Draft.autogroup(ellipse)
                
                        elif str(s.Curve) == "<Line object>":                            # Line
                            FreeCAD.Console.PrintMessage("Detected : Line" + "\n")
                            points = []
                            points = selectedEdge.Edges[0].discretize(3)                 # Dicretize
                            wire   =  Draft.makeLine(points[0],points[-1])
                            FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(Line)"
                            Draft.autogroup(wire)
                            points[:]    = []
                                
                        elif (hasattr(s.Curve,"Center")) and (hasattr(s.Curve,"Radius")):# arc or circle
                            FreeCAD.Console.PrintMessage("Detected : Arc or Circle" + "\n")
                            ##https://github.com/yorikvanhavre/FreeCAD/blob/master/src/Mod/Draft/Draft.py#L264
                            pl=FreeCAD.Placement()
                            pl.Rotation = FreeCAD.Rotation(s.Curve.XAxis, s.Curve.YAxis, s.Curve.Axis, "ZXY")
                            pl.Base     = s.Curve.Center
                            circle = Draft.makeCircle(radius=s.Curve.Radius, placement=pl, face=False, support=None)
                            circle.FirstAngle = degrees(selectedEdge.FirstParameter)
                            circle.LastAngle  = degrees(selectedEdge.LastParameter)-360
                            FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(CiOrArc)"
                            Draft.autogroup(circle)
                
                        elif (str(s.Curve) == "<BSplineCurve object>"):
                            #print(s.Curve.getPoles())
                            points   = []

                            #try:
                                #points = s.Curve.getPoles() ?                            # getPoles
                            #except Exception:
                            bspline = s.Curve
                            arcs    = bspline.toBiArcs(0.001)
                            BsplineNumberElement = len(arcs)
                            points  = selectedEdge.Edges[0].discretize(BsplineNumberElement * 10)# Dicretize
                            spline   = Draft.makeBSpline(points, closed=False, face=False, support=None)
                            
                            FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(BSplineC)"
                            Draft.autogroup(spline)
                            points[:]= []
                            FreeCAD.Console.PrintMessage("Detected : BSplineCurve (" + str(BsplineNumberElement) + " poles x 10)" + "\n")
            
                        elif (str(s.Curve) == "<BezierCurve object>"):                   # BezierCurve
                            FreeCAD.Console.PrintMessage("Detected : BezierCurve" + "\n")
                            #print(s.Curve.getPoles())
                            points = []
                            
                            try:
                                points = s.Curve.getPoles()                              # getPoles
                            except Exception:
                                points = selectedEdge.Edges[0].discretize(1000)          # Discretize
                            try:
                                if self.CB_BezierCurve.isChecked():
                                    bezCurve = Draft.makeBezCurve(points, closed=False, support=None, degree=3)     #makeBezCurve3 (cubic) 0.19
                                    FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(BezCubic)"
                                else:
                                    bezCurve = Draft.makeBezCurve(points, closed=False, support=None, degree=None)  #makeBezCurve 0.19
                                    FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(BezCurve)"
                                Draft.autogroup(bezCurve)
                            except Exception:
                                bezCurve = Draft.makeBezCurve(points,closed=False,support=None)  #makeBezCurve 0.18
                                Draft.autogroup(bezCurve)
                            points[:]= []
            
                        else:
                            FreeCAD.Console.PrintMessage("Object duplicated !" + "\n")
                            Part.show(selectedEdge.copy())                               # create repro shape subObject
                            FreeCAD.ActiveDocument.ActiveObject.Label = nameObject + "_" + subName + "_(Dupicate)"
            
                    except Exception:
                        FreeCAD.Console.PrintMessage("Error !!!" + "\n")
                        
                try:
                    if self.RB_01_FlatLines.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.DisplayMode = u"Flat Lines"
                    if self.RB_02_Wireframe.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.DisplayMode = u"Wireframe"
                    if self.RB_03_Points.isChecked():
                        FreeCADGui.ActiveDocument.ActiveObject.DisplayMode = u"Points"
                except Exception:
                    None

                if self.lineWidth != 0.0:
                    FreeCADGui.ActiveDocument.ActiveObject.LineWidth  = self.lineWidth
                else:
                    FreeCADGui.ActiveDocument.ActiveObject.LineWidth  = selection.Object.ViewObject.LineWidth
                    
                try:
                    if self.groupBox_00.isChecked():
                                                                                          
                        FreeCADGui.ActiveDocument.ActiveObject.LineColor  = (self.redFL, self.greenFL, self.blueFL)
                        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (self.redFL, self.greenFL, self.blueFL)
                        FreeCADGui.ActiveDocument.ActiveObject.PointColor = (self.redFL, self.greenFL, self.blueFL)
                    else:
                                                                                                                 
                        FreeCADGui.ActiveDocument.ActiveObject.PointSize  = selection.Object.ViewObject.PointSize
                        FreeCADGui.ActiveDocument.ActiveObject.LineColor  = selection.Object.ViewObject.LineColor
                        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = selection.Object.ViewObject.ShapeColor
                        FreeCADGui.ActiveDocument.ActiveObject.PointColor = selection.Object.ViewObject.PointColor
                except Exception:
                    None
                    
                countSubName += 1
                
            if self.RB_01_Default.isChecked():
                None
            if self.RB_02_Hidden.isChecked():
                print( "Hidden : ",nameObject)
                FreeCADGui.ActiveDocument.getObject(nameObject).Visibility = False
            try:
                if self.RB_03_Delete.isChecked():
                    print( "Delete : ",nameObject)
                    doc.removeObject(nameObject)
            except Exception:
                FreeCAD.Console.PrintError("Error Delete : ",str(nameObject) + "\n")

        self.progressBar.setValue(0)
        FreeCAD.ActiveDocument.recompute()
#        FreeCAD.Console.PrintMessage(str("on_PB_04c_Convert_Edge")+"\n")

    def on_groupBox_00(self):
        if self.groupBox_00.isChecked():
            None
        else:
            None
#        FreeCAD.Console.PrintMessage(str("on_groupBox_00")+"\n")

    def on_RB_Force_clicked(self):

        if self.RB_Force_01_Line.isChecked():
            self.groupBox_Force_LAC.setTitle("Force on a form : Line")
            self.PB_Force_LAC.setText("Force on : Line")
            self.PB_Force_LAC.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Line.svg")))
        elif self.RB_Force_02_Arc.isChecked():
            self.groupBox_Force_LAC.setTitle("Force on a form : Arc")
            self.PB_Force_LAC.setText("Force on : Arc")
            self.PB_Force_LAC.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Arc.svg")))
        elif self.RB_Force_03_Circle.isChecked():
            self.groupBox_Force_LAC.setTitle("Force on a form : Circle")
            self.PB_Force_LAC.setText("Force on : Circle")
            self.PB_Force_LAC.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Circle.svg")))

    def on_PB_Force_LAC(self):

        try:
            selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0]                    # Select an object or sub object
            selection    = FreeCADGui.Selection.getSelection()[0]
            nameObject   = selection.Name
            subName      = FreeCADGui.Selection.getSelectionEx()[0].SubElementNames[0]
            s            = selectedEdge

            if self.RB_Force_01_Line.isChecked():   # Force create Line
                points = []
                points = selectedEdge.Edges[0].discretize(3)                 # Dicretize
                if (points[0] == points[-1]) :
                    App.Console.PrintError("Bad selection the points are egual"+"\n")
                else:
                    wireLine = Draft.makeLine(points[0],points[-1])
                    wireLine.ViewObject.LineColor = (1.0,0.0,0.0)         # give color
                    wireLine.Label = nameObject + "_" + subName + "_(Line)" 
                    Draft.autogroup(wireLine)
                points[:] = []

            elif self.RB_Force_02_Arc.isChecked():   # Force create Arc

                #App.Console.PrintError("This fonction is only availlable with FreeCAD 0.19 (Arc)"+"\n")
                points = []
                selectedArc = []
                points = selectedEdge.Edges[0].discretize(3)                 # Dicretize
                selectedArc = points

                if (selectedArc[0]==selectedArc[1]) or (selectedArc[0]==selectedArc[2]) or selectedArc[1]==selectedArc[2] :
                    App.Console.PrintError("Bad selection the points are egual (Line)"+"\n")
                else:
                    try:
                        C1 = Part.Arc(FreeCAD.Vector(selectedArc[0]),FreeCAD.Vector(selectedArc[1]),FreeCAD.Vector(selectedArc[2]))
                        S1 = Part.Shape([C1])                                      # create arc base
                        Part.show(S1)

                        obj = App.ActiveDocument.ActiveObject                      # select the object created
                        Gui.Selection.addSelection(obj)
                        sel = obj.Shape

                        CircleDirection = sel.Curve.Axis                           # decode the datas
                        CircleRayon     = sel.Curve.Radius
                        CircleAxis      = sel.Curve.Center

                        App.ActiveDocument.removeObject(obj.Label)                 # remove arc master

                        v = CircleDirection                                        # give direction to circle
                        r = App.Rotation(App.Vector(0,0,1),v)
                        pl=FreeCAD.Placement()
                        pl.Base=FreeCAD.Vector(CircleAxis)
                        pl.Rotation.Q = r.Q
                         
                        arc3Points = make_arc_3points(selectedArc)

                        arc3Points.ViewObject.LineColor = (1.0,0.0,0.0)         # give color
                        arc3Points.Label =  nameObject + "_" + subName + "_(" + str(round(CircleRayon,3)) + "_r)_(Arc)"
                    except Exception:
                        App.Console.PrintError("Three points are collinear or bad selection (Arc)"+"\n"
                                               "Tray Force Circle"+"\n")
                del selectedArc[:]

            elif self.RB_Force_03_Circle.isChecked():   # Force create Circle

                selectedCircle = []
                points = selectedEdge.Edges[0].discretize(7)                 # Dicretize
                selectedCircle = points

                if (selectedCircle[0]==selectedCircle[1]) or (selectedCircle[0]==selectedCircle[2]) or selectedCircle[1]==selectedCircle[2] :
                    App.Console.PrintError("Bad selection the points are egual"+"\n")
                else:
                    try:
                        C1 = Part.Arc(FreeCAD.Vector(selectedCircle[0]),FreeCAD.Vector(selectedCircle[1]),FreeCAD.Vector(selectedCircle[2]))
                        S1 = Part.Shape([C1])                                      # create arc base
                        Part.show(S1)

                        obj = App.ActiveDocument.ActiveObject                      # select the object created
                        Gui.Selection.addSelection(obj)
                        sel = obj.Shape

                        CircleDirection = sel.Curve.Axis                           # decode the datas
                        CircleRayon     = sel.Curve.Radius
                        CircleAxis      = sel.Curve.Center

                        App.ActiveDocument.removeObject(obj.Label)                 # remove arc master

                        v = CircleDirection                                        # give direction to circle
                        r = App.Rotation(App.Vector(0,0,1),v)
                        pl=FreeCAD.Placement()
                        pl.Base=FreeCAD.Vector(CircleAxis)
                        pl.Rotation.Q = r.Q
                        circle3Points = Draft.makeCircle(radius=CircleRayon, placement=pl, face=False, support=None)
                        circle3Points.ViewObject.LineColor = (1.0,0.0,0.0)         # give color
                        circle3Points.Label =  nameObject + "_" + subName + "_(" + str(round(CircleRayon,3)) + "_r)_(Circle)"
                        Draft.autogroup(circle3Points)
                    except Exception:
                        App.Console.PrintError("Three points are collinear or bad selection (Circle)"+"\n")
                del selectedCircle[:]

            FreeCAD.ActiveDocument.recompute()
        except Exception:
            App.Console.PrintError("Error in Create Forced object" + "\n")

    def on_DS_01_Width_Line_valueChanged(self,LineWidth):
        self.lineWidth = LineWidth
        if self.lineWidth != 0.0:
            self.DS_01_Width_Line.setSuffix(" mm Width")
            self.PB_04c_Convert_Edge.setText("Convert Wire (M)")
        else:
            self.DS_01_Width_Line.setSuffix(" Auto")
            self.PB_04c_Convert_Edge.setText("Convert Wire (A)")
#        FreeCAD.Console.PrintMessage(str("on_DS_01_Width_Line_valueChanged ")+str(self.lineWidth)+"\n")

    def on_CB_BezierCurve_clicked(self):
        if self.CB_BezierCurve.isChecked():
            self.CB_BezierCurve.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_CubicBezCurve.svg")))
            self.CB_BezierCurve.setText("Cubic BezierCurve")
        else:
            self.CB_BezierCurve.setIcon(QtGui.QIcon.fromTheme("Part",QtGui.QIcon(":/icons/Draft_BezCurve.svg")))
            self.CB_BezierCurve.setText("BezierCurve")
#        FreeCAD.Console.PrintMessage(str("on_CB_BezierCurve_clicked ")+"\n")

    def on_PB_05_Reset(self):                     # 
        global ui
        global setSystemFonts
        global PolicePath
        global nomPolice
 
        #p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")
        #print( p.GetUnsigned("DefaultShapeLineColor"))
        self.red     = 255   #204               # for button
        self.green   = 0     #204
        self.blue    = 0     #204
        self.alpha   = 255   # 255 = visibility max (opacity)
        self.redFL   = float(255.0 / 255.0)     # for object FC
        self.greenFL = float(0.0   / 255.0)
        self.blueFL  = float(0.0   / 255.0)
        self.alphaFL = float(255.0 / 255.0)     # 1.0 = visibility max (opacity)
        
        self.PB_03_Color.setStyleSheet("background-color: rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")")
        self.groupBox_00.setChecked(False)
        
        self.RB_01_Default.setChecked(True)
        self.lineWidth = 0.0
        self.DS_01_Width_Line.setValue(self.lineWidth)
        self.DS_02_Size_Font.setValue(0.0)

        self.groupBox_Force_LAC.setTitle("Force on a form : Line")
        self.PB_Force_LAC.setText("Force on : Line")
        self.PB_Force_LAC.setIcon(QtGui.QIcon.fromTheme("Vieuw",QtGui.QIcon(":/icons/Draft_Line.svg")))
        self.RB_Force_01_Line.setChecked(True)

        MyLabelPatience.label.show()
        FreeCADGui.updateGui()                                 # rafraichi l'ecran
        setSystemFonts = 0
        ui.searchFont(self.pathFont)
        MyLabelPatience.label.close()

        self.fontSizeManual    = False
        self.PB_04_Convert_Text.setText("Convert Text (A)")
        self.FontSize  = 0.0
        self.DS_02_Size_Font.setValue(self.FontSize)
        self.fonte     = PolicePath + "/" + nomPolice + ".TTF"
        self.CB_BezierCurve.setChecked(False)
        self.RB_01_FlatLines.setChecked(True)

#        FreeCAD.Console.PrintMessage(str("on_PB_05_Reset ")+"\n")

    def on_PB_09_Upgrade(self):                     # 
        try:
            Draft.upgrade(FreeCADGui.Selection.getSelection(), delete=True)
            FreeCAD.ActiveDocument.recompute()
        except Exception:
            None
#        FreeCAD.Console.PrintMessage(str("on_PB_06_Downgrade ")+"\n")

    def on_PB_06_Downgrade(self):                     # 
        try:
            Draft.downgrade(FreeCADGui.Selection.getSelection(),delete=True)
            FreeCAD.ActiveDocument.recompute()
        except Exception:
            None
#        FreeCAD.Console.PrintMessage(str("on_PB_06_Downgrade ")+"\n")

    def on_PB_07_Quit(self):                     # 
        FreeCAD.Console.PrintMessage("End Compound +"+"\n")
        self.window.hide()
#        FreeCAD.Console.PrintMessage(str("on_PB_06_Quit ")+"\n")

    def on_PB_Help_clicked(self):
        WebGui.openBrowser("https://wiki.freecadweb.org/Macro_Compound_Plus")
        App.Console.PrintMessage("https://wiki.freecadweb.org/Macro_Compound_Plus" + "\n")
#        FreeCAD.Console.PrintMessage(str("Help ")+"\n")

###### Read Configuration begin ####
#switchModeTextList = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetBool("switchModeTextList")
#switchFontComBox   = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetBool("switchFontComBox")
#setSystemFonts     = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetBool("setSystemFonts")
#seTtextAlignement  = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetInt("seTtextAlignement")
###### Read Configuration end   ####

###### Write Configuration begin ####
#FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("switchModeTextList", True)    # True or False
#FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("switchFontComBox", True)      # True or False
#FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("setSystemFonts", True)        # True or False
#FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetInt("seTtextAlignement", 0)         # 0, 1, or 2
FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetString("Version",__version__ + " (" + __date__ + ")")# 
###### Write Configuration end   ####

Compound = QtWidgets.QMainWindow()
ui = Ui_Compound()
ui.setupUi(Compound)
Compound.show()
}}

## Liens

Mes macros sur [Github](https://gist.github.com/mario52a)

## Version

-   15/08/2020 ver 0.04: ajout de la section \"Forcer la forme\" si non détectée, créer Ligne, Arc et Cercle sur forcé
-   14/05/2020 ver 00.03: mise à niveau pySide2 et Qt5 et (police matPlotLib) et convertir Cercle, Arc, Ellipse, BezierCurve
-   24/01/2018 ver 00.02: sup \"import PyQt4\"
-   21/11/2016 ver 00.01:



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Compound Plus/fr
