# Macro Rotate To Point/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Rotate To Point
|Translate=Macro Rotatzione su Punto
|Icon=Macro_Rotate_To_Point.svg
|Description={{ColoredText|#ff0000|#ffffff|Nuva versione GUI modicato per HD dpi (QGridLayout) funziona solo su FC version 0.18 e più alto (PySide2 Qt5)}} <br/> <br/> Questa macro fa ruotare un oggetto su se stesso intorno all'asse scelto.</br>Si puo salvare in un file tutte le coordinate lavorate e salvarlo in un file "Coordinate [(0.06,1.30,0.0), (85.0,0.0,0.0)]" o in una macro completa per creare un'animazione<br/><br/>Per la precedente versione vedi [https   *//gist.githubusercontent.com/mario52a/2fc48333deca5a31e6232c29a9db5e4c/raw/9231d5b1d218357305cc0404e46bf6c107509a0e/Macro%2520Rotate%2520To%2520Point.FCMacro Macro_Rotate_To_Point] e installa manualmente.
|Author=Mario52
|Version=00.09
|Date=2021/02/25
|FCVersion=0.18 e più
|Download=[https   *//www.freecadweb.org/wiki/images/d/d1/Macro_Rotate_To_Point.svg ToolBar Icon]
}}


</div>

## Descrizione

Questa macro permette di ruotare un oggetto su se stesso scegliendo l\'asse di rotazione. L\'asse può essere il centro del contenitore dell\'oggetto

-   il centro BoundBox
-   il centro di massa
-   la direzione di un filo
-   l\'ultimo punto cliccato

## Uso


<div class="mw-translate-fuzzy">

1.  Carica la macro con [Addon Manager](Std_AddonMgr/it.md)
2.  Lancia la macro
3.  Clic uno obietto
4.  Celia una orientazione


</div>

![Interface Rotate to point ](images/Macro_Rotate_To_Point_00.png ) 

### Point Rotation 

-   Bounbox Center    * Seleziona come asse di rotazione il centro del BoundBox
-   Center of Mass    * Seleziona come asse di rotazione il Centro di massa
-   Point Clicked    * Seleziona come asse di rotazione l\'ultimo punto cliccato 1   * Selezionare l\'oggetto 2   * usare il tasto **CTRL** per scegliere un punto esterno all\'oggetto
    -   1   * seleziona uno obietto
    -   2   * utilizza **CTRL** per scegliere un oggetto in più

### Axis Rotation 

-   Rotation(Z) Yaw    * asse Yaw
-   Rotation(Y) Pitch    * asse Pitch
-   Rotation(X) Roll    * asse Roll
-   Rotation(D) Direction   * Ruota intorno alla linea, filo selezionato

### Coordinates Point clicked 

-   DoubleSpinBox    * Coordinate X del clic del mouse (modificabile solo nel modo \"Point Clicked\")
-   DoubleSpinBox    * Coordinate Y del clic del mouse (modificabile solo nel modo \"Point Clicked\")
-   DoubleSpinBox    * Coordinate Z del clic del mouse (modificabile solo nel modo \"Point Clicked\")

### Work

-    {{CheckBox|Translation}}   * Se questo checkBox è {{CheckBox|TRUE|checked}} la rotazione è disabilitata, il posizionamento dell\'oggetto viene eseguito sull\'asse selezionato.

-    **Point**   * viene creato un punto per visualizzare l\'asse di rotazione del punto   * X rossa, Y verde, Z blu

-   Line Edit   * la modifica della linea mostra la coordinata originale dell\'asse selezionato + i dati di input forniti nella casella di selezione

-    {{SpinBox|0,0000}}   * immettere la modifica

-    **Apply**   * applica la modifica all\'oggetto

-   La coordinata viene visualizzata

### Data

-   Finestra per la visualizzazione delle coordinate memorizzate

-    **Save**   * salva i dati nel file

-    **Clear**   * elimina e pulisci l\'editor di testo

-    **Delete**   * elimina la riga selezionata

-    **Memorize**   * memorizza e visualizza le coordinate

-    {{CheckBox|Macro}}   *

    -   Modalità normale {{CheckBox | Macro}} la coordinata viene salvata in questa modalità   * **\[(0.06,1.30,0.0), (85.0,0.0,0.0)\],**
    -   Modalità macro {{CheckBox|TRUE|0,0 Coordinate}} la coordinata viene salvata in una macro completa direttamente nella directory delle macro con lo stesso nome dell\'estensione del documento .FCMacro
        -   **Opzioni della macro**
        -   **\_\_ pompe\_\_\_\_engrenage\_\_**   * Nome del documento
        -   **\_\_ 22 Coordinates\_\_**   * numero di coordinate
        -   **Digita il tasto Q per uscire**   * Esci dalla macro
        -   **Digita il tasto D per diminuire la velocità**   * Diminuisci la velocità dell\'animazione
        -   **Digita il tasto I per aumentare la velocità**   * Aumenta la velocità dell\'animazione
        -   **Digitare il tasto P per mettere in pausa/continuare o il tasto RETURN o ESCAPE**   * Pausa/Anime
        -   **Digitare il tasto S per procedere passo dopo passo (tasto RETURN o ESCAPE per continuare)**   * Passo dopo passo
        -   **Digitare la chiave M per questo messaggio**   * Visualizza questo memo
        -   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-    {{CheckBox|Memo on Click}}   *

    -   Modalità normale {{CheckBox|Memo on Click}}   * i dati non vengono salvati sulla finestra, è necessario premere il pulsante **Memo (2)** per salvare le coordinate
    -   Modalità Memo on Click {{CheckBox|TRUE|Memo on Demand}}   * i dati vengono salvati automaticamente facendo clic sul pulsante **Apply**

### Command

-    **Quit**   * chiude la macro

-    **Original**   * dopo aver modificato i dati dell\'oggetto puoi tornare alla posizione originale, se non hai deselezionato l\'oggetto corrente.

-    **0,0,0**   * questa opzione posiziona l\'oggetto nella coordinata di base ` 0, 0, 0`

-    **Reset**   * reimposta i dati nella macro e deseleziona l\'oggetto corrente (stesso clic del mouse nella [vista 3D](3D_view/it.md))

## Script

ToolBar Icon PNG ![](images/Macro_Rotate_To_Point.png ) SVG ![](images/Macro_Rotate_To_Point.svg )

**Macro\_Rotate\_To\_Point.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
from __future__ import unicode_literals
"""
***************************************************************************
*   Copyright (c) 2017 2018 2019 2020 2021 <mario52>                      *
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
#
#OS   * Windows 10 (10.0)
#Word size of OS   * 64-bit
#Word size of FreeCAD   * 64-bit
#Version   * 0.19.24219 (Git)
#Build type   * Release
#Branch   * master
#Hash   * 8c26baebab320b8c1c3279bc8eb34a1eb6c7a363
#Python version   * 3.6.8
#Qt version   * 5.12.1
#Coin version   * 4.0.0a
#OCC version   * 7.3.0
#Locale   * French/Mars (fr_Ma)
#
#
__title__   = "Rotate_To_Point"
__author__  = "Mario52"
__url__     = "https   *//www.freecadweb.org/"
__Wiki__    = "https   *//www.freecadweb.org/wiki/Macro_Rotate_To_Point"
__version__ = "00.10"
__date__    = "2021/03/08"  #YYYY/MM/DD
#
#
import PySide2
from PySide2 import (QtWidgets, QtCore, QtGui)
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QComboBox
#from PySide2.QtWidgets import (QWidget, QApplication, QSlider, QGraphicsView, QGraphicsScene, QVBoxLayout, QStyle, QListWidget)
#from PySide2.QtCore import QDate
#from PySide2.QtGui import (QPainter, QColor, QIcon, QBrush, QPalette)
from PySide2.QtSvg import *

import unicodedata
import re
import operator
from operator import itemgetter, attrgetter, methodcaller    # pour sort 

import Draft, Part, PartGui, FreeCADGui, FreeCAD
from FreeCAD import Base
import DraftVecUtils
import time, os

Gui = FreeCADGui
App = FreeCAD

global ui            ; ui             = ""
global sourisPass    ; sourisPass     = 0
global positionMouse ; positionMouse  = ""

global selM          ; selM           = ""
global originalObject; originalObject = ""
global myObject      ; myObject       = ""
global myObjectName  ; myObjectName   = ""
global originalPlacement; originalPlacement = ""
global valeur        ; valeur         = 0.0

global axisX         ; axisX          = 0.0
global axisY         ; axisY          = 0.0
global axisZ         ; axisZ          = 0.0

global posX          ; posX           = 0.0
global posY          ; posY           = 0.0
global posZ          ; posZ           = 0.0

global rotAngleX     ; rotAngleX      = 0.0
global rotAngleY     ; rotAngleY      = 0.0
global rotAngleZ     ; rotAngleZ      = 0.0

global saveOnDisk    ; saveOnDisk     = []
global saveListView  ; saveListView   = ""
global memorySelected; memorySelected = []
global countMemory   ; countMemory    = 0
global duplicate_Memory ;duplicate_Memory = []
global duplicate_View; duplicate_View = []

global s             ; s               = ""

##path###########################################################################
global path, path2                                                  #
#path  = FreeCAD.ConfigGet("AppHomePath")                           # path FreeCAD installation
#path  = FreeCAD.ConfigGet("UserAppData")                           # path FreeCAD User data
#path  = "your path"                                                # your directory path
param = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macro")# macro path
path = param.GetString("MacroPath","") + "/"                        # macro path
path = path.replace("\\","/")                                       # convert the "\" to "/"
#print( "Path for the icons    * " , path  )                            # 
#################################################################################

global pathFile
#### Configuration begin ##############################################################
pathFile = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__ ).GetString("setLastPath")
if pathFile == ""   *
    pathFile = path
    FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetString("setLastPath",pathFile)
####
FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetString("Version",__version__ + " (" + __date__ + ")")
global switchZoomOnCilck
switchZoomOnCilck = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetBool("switchZoomOnCilck")
if switchZoomOnCilck == 0   *
    FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("switchZoomOnCilck", switchZoomOnCilck)
#### Configuration end   ##############################################################

#### wiki help page ####
import WebGui

#def on_PB_Help(self)   * # 
#    WebGui.openBrowser("http   *//www.freecadweb.org/wiki/index.php?title=xxxx")
#    App.Console.PrintMessage("http   *//www.freecadweb.org/wiki/index.php?title=xxxx" + "\n")
#### wiki help page ####

global switchVersionMacroSearch#; switchVersionMacroSearch = False
try   *
    def versionSearch()   *
        import urllib
        import requests
        contentPage = requests.get("https   *//wiki.freecadweb.org/Macro_" + __title__).text
        for i in contentPage.split("\n")   *            # list page to line
            if "ctEven macro-version" in i   *
                versionDetect = (i.split(">")[1])
            if "ctEven macro-date" in i   *
                dateDetect = (i.split(">")[1])
            try   *
                if (len(versionDetect) != 0) and (len(dateDetect) != 0)   *
                    break
            except Exception   *
                None
        try   *
            if (versionDetect == __version__) and (dateDetect == __date__)   *
                None
            else   *
                msg = ("New version availlable    * " + "\n" + 
                      str(versionDetect) + "   *" + str(dateDetect) + "\n" + 
                      "You can install with AddonManager")
                FreeCAD.Console.PrintMessage("your actual version       * " + str(__version__) + "    * " + str(__date__) + "\n")
                FreeCAD.Console.PrintMessage("new version availlable    * " + str(versionDetect) + "    * " + str(dateDetect) + "\n")
                diag = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'New Version', msg)
                diag.setWindowModality(QtCore.Qt.ApplicationModal)
                diag.exec_()
        except Exception   *
            None
        return versionDetect, dateDetect
    
#    switchVersionMacroSearch = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetBool("switchVersionMacroSearch")
#    if switchVersionMacroSearch == 0   *
#        FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("switchVersionMacroSearch", switchVersionMacroSearch)
#    if switchVersionMacroSearch == True   *
#        versionSearch()
except Exception   *
    FreeCAD.Console.PrintMessage("Failed to establish a connection" + "\n")
#### Detect version macro ###########################################

switchVersionMacroSearch = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).GetBool("switchVersionMacroSearch")

if switchVersionMacroSearch == 0   *
    FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("switchVersionMacroSearch", switchVersionMacroSearch)
if switchVersionMacroSearch == True   *
    versionSearch()
#### Detect version macro ###########################################


Quit_Icon = [
"24 24 3 1",
"   c None",
".  c #FFFFFF",
"+  c #CC0000",
"          ....          ",
"++++++++++....++++++++++",
"+.......++....++.......+",
"+.......++....++.......+",
"+.......++....++.......+",
"+...++++++....++++++...+",
"+...++++++....++++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+......................+",
"+......................+",
"+......................+",
"++++++++++++++++++++++++"
]

boundBox_Center_Icon = [
"24 24 8 1",
"   c None",
".  c #284871",
"+  c #234C86",
"@  c #314B64",
"#  c #EF2929",
"$  c #4A74A4",
"%  c #4478AD",
"&  c #4E9A06",
"                        ",
"           #            ",
"           #            ",
"           #            ",
"      &&&&&#            ",
"      &    #&&&&&&&     ",
"     &    +#..   &&     ",
"    &&&&&+%#%%. & &     ",
"    &  ++&&&&&&&  &     ",
"    &  +$$$$$$&+@ &     ",
"    & +%$$$$$$&+@ &     ",
"####&###$$$$$+&+####### ",
"    & +%$$$$++&+@ &     ",
"    & +%$$$+++&+@ &     ",
"    &  +$$++++&@  &     ",
"    &   ++++++&@  &     ",
"    &    @@@@@&   &     ",
"    &      #  &  &      ",
"    &&&&&  #  &&&       ",
"         &&&&&&         ",
"           #            ",
"           #            ",
"           #            ",
"                        "
]

centerMass_Icon = [
"24 24 9 1",
"   c None",
".  c #000100",
"+  c #CD0000",
"@  c #6B6014",
"#  c #B0A22C",
"$  c #D5B716",
"%  c #E9D235",
"&  c #F7E66C",
"*  c #FBF4BC",
"                        ",
"                        ",
"                        ",
"                        ",
"         ......         ",
"       ..#%%%%#..       ",
"      .@&&&%%%%%@.      ",
"     .@&**&%%%%%%@.     ",
"     .&***&%%%%%%%.     ",
"    .#&**&%%+%%%%%#.    ",
"    .%&&&%%++%%%$$%.    ",
"    .%%%%+++++$$$$$.    ",
"    .%%%%%+++++$$$$.    ",
"    .%%%%$$++$$$$$$.    ",
"    .#%$$$$+$$$$$$#.    ",
"     .%$$$$$$$$$$%.     ",
"     .@%$$$$$$$$$@.     ",
"      .@%$$$$$$%@.      ",
"       ..#$$$$#..       ",
"         ......         ",
"                        ",
"                        ",
"                        ",
"                        "
]

point_Clicked_Icon = [
"24 24 7 1",
"   c None",
".  c #730000",
"+  c #9F0000",
"@  c #E90000",
"#  c #C39F03",
"$  c #ECD309",
"%  c #FBE851",
"                        ",
"         #####          ",
"        #%%%%%#         ",
"       #%%%%%%$#        ",
"      #%%%%%$$$$#       ",
"      #%%%%$$$$$#       ",
"      #%%%+.$$$$#       ",
"      #%%%++.$$$#       ",
"       #%%+@+.$#        ",
"       #%%+@@+.#        ",
"        ##+@@@+.        ",
"          +@@@@+.       ",
"          +@@@@@+.      ",
"          +@@@@@@+.     ",
"          +@@@@@@@..    ",
"          +@@@@@@@@..   ",
"          +@@@@@@@@@..  ",
"          +@@@@@@+....  ",
"          +@@@@@+       ",
"          +@@++@@.      ",
"          +@+. .@@.     ",
"          ++.   .@.     ",
"                .+..    ",
"                 ..     "
]

axis_X_Icon = [
"24 24 6 1",
"   c None",
".  c #000000",
"+  c #A40000",
"@  c #EE2A2A",
"#  c #729FCF",
"$  c #B9BCB5",
"           $$   $$$$    ",
"          $$$$  $  $    ",
"         $$$$$$   $     ",
"         $$$$$$  $      ",
"        $$$$$$$$ $$$    ",
"          $$$$          ",
"          $$$$          ",
"          $$$$          ",
"          $$$$          ",
"          $$$$    $$  $$",
"         $$##$$   $$  $$",
" .  .    $####$     $$$ ",
"  ...    +####$     $$  ",
"  ..    +@####$$    $   ",
" . ... +@@@+$$$$$  $$   ",
"      +@@@+  $$$$$      ",
"     +@@@+    $$$$$     ",
"  +++@@@+      $$$$$$$  ",
"  +@@@@+        $$$$$$  ",
"  +@@@+          $$$$$  ",
"  +++++          $$$$$  ",
"                        ",
"                        ",
"                        "
]

axis_Y_Icon = [
"24 24 7 1",
"   c None",
".  c #030303",
"+  c #4E9A06",
"@  c #729FCF",
"#  c #B9BCB5",
"$  c #BABDB6",
"%  c #8AE134",
"           $$   ####    ",
"          $$$$  #  #    ",
"         $$$$$$   #     ",
"         $$$$$$  #      ",
"        $$$$$$$$ ###    ",
"          $$$$          ",
"          $$$$          ",
"          $$$$          ",
"          $$$$          ",
"          $$$$    ..  ..",
"         $$@@$$   ..  ..",
" #  #    $@@@@$     ... ",
"  ###    $@@@@+     ..  ",
"  ##    $$@@@@%+    .   ",
" # ### $$$$$+%%%+  ..   ",
"      $$$$$  +%%%+      ",
"     $$$$$    +%%%+     ",
"  $$$$$$$      +%%%+++  ",
"  $$$$$$        +%%%%+  ",
"  $$$$$          +%%%+  ",
"  $$$$$          +++++  ",
"                        ",
"                        ",
"                        "
]

axis_Z_Icon = [
"24 24 6 1",
"   c None",
".  c #000000",
"+  c #204A87",
"@  c #1D89B6",
"#  c #729FCF",
"$  c #B9BCB5",
"           ++    ...    ",
"          +@@+     .    ",
"         +@@@@+   .     ",
"         +@@@@+  .      ",
"        +++@@+++ ...    ",
"          +@@+          ",
"          +@@+          ",
"          +@@+          ",
"          +@@+          ",
"          +@@+    $$  $$",
"         ++##++   $$  $$",
" $  $    +####+     $$$ ",
"  $$$    $####$     $$  ",
"  $$    $$####$$    $   ",
" $ $$$ $$$$$$$$$$  $$   ",
"      $$$$$  $$$$$      ",
"     $$$$$    $$$$$     ",
"  $$$$$$$      $$$$$$$  ",
"  $$$$$$        $$$$$$  ",
"  $$$$$          $$$$$  ",
"  $$$$$          $$$$$  ",
"                        ",
"                        ",
"                        "
]

direction_Icon = [
"24 24 6 1",
"   c None",
".  c #000000",
"+  c #A40000",
"@  c #EE2A2A",
"#  c #565854",
"$  c #729FCF",
"                        ",
"                        ",
"                 +++++  ",
"                  +@@+  ",
"                 +@@@+  ",
"                +@@@++  ",
"               +@@@+ +  ",
"              +@@@+     ",
"             +@@@+      ",
"            +@@@+       ",
"           +@@@+        ",
"          +@@@+         ",
"         +@@@+          ",
"        +@@@+           ",
"       +@@@+            ",
"      +@@@+             ",
"   + +@@@+              ",
"   ++@@@+               ",
"   +@@@+                ",
"   +@@+                 ",
"   +++++                ",
"                        ",
"                        ",
"                        "
]

point_Icon = [
"24 24 8 1",
"   c None",
".  c #000100",
"+  c #B0A22C",
"@  c #E9D235",
"#  c #6B6014",
"$  c #F7E66C",
"%  c #FBF4BC",
"&  c #D5B716",
"                        ",
"                        ",
"                        ",
"                        ",
"         ......         ",
"       ..+@@@@+..       ",
"      .#$$$@@@@@#.      ",
"     .#$%%$@@@@@@#.     ",
"     .$%%%$@@@@@@@.     ",
"    .+$%%$@@@@@@@@+.    ",
"    .@$$$@@@@@&&&&&.    ",
"    .@@@@@@@&&&&&&&.    ",
"    .@@@@@&&&&&&&&&.    ",
"    .@@@@&&&&&&&&&&.    ",
"    .+@@&&&&&&&&&&+.    ",
"     .@&&&&&&&&&&&.     ",
"     .#&&&&&&&&&&#.     ",
"      .#&&&&&&&&#.      ",
"       ..+&&&&+..       ",
"         ......         ",
"                        ",
"                        ",
"                        ",
"                        "
]

apply_Icon = [
"24 24 3 1",
"   c None",
".  c #4E9A06",
"+  c #FFFFFF",
"                        ",
"                        ",
"                        ",
"                  .     ",
"                 .+.    ",
"                .+.+.   ",
"               .+...+.  ",
"              .+.....+. ",
"     .       .+.......+.",
"    .+.     .+.......+. ",
"   .+.+.   .+.......+.  ",
"  .+...+. .+.......+.   ",
" .+.....+.+.......+.    ",
".+.......+.......+.     ",
" .+.............+.      ",
"  .+...........+.       ",
"   .+.........+.        ",
"    .+.......+.         ",
"     .+.....+.          ",
"      .+...+.           ",
"       .+.+.            ",
"        .+.             ",
"         .              ",
"                        "
]

quit_Icon = [
"24 24 3 1",
"   c None",
".  c #FFFFFF",
"+  c #CC0000",
"          ....          ",
"++++++++++....++++++++++",
"+.......++....++.......+",
"+.......++....++.......+",
"+.......++....++.......+",
"+...++++++....++++++...+",
"+...++++++....++++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...+++++......+++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+...++++++++++++++++...+",
"+......................+",
"+......................+",
"+......................+",
"++++++++++++++++++++++++"
]

save_Icon = [
"24 24 9 1",
"   c None",
".  c #A30500",
"+  c #5D5F5C",
"@  c #3967A0",
"#  c #4B9A00",
"$  c #7E9BBD",
"%  c #A9ABA8",
"&  c #C7C9C6",
"*  c #DCDEDB",
"                        ",
"      @@@@@             ",
"    @@$$$$$@            ",
"    @$$$$$$$@           ",
"   @@@@@@$@$$@          ",
"         @$@@@          ",
"    +%&&&@$@@@@&%%%     ",
"    +*@@@$@@@@@@@@&%    ",
"   +%*@@@@@@@@@@@@*&+   ",
"   +***@@@@@@@@@@***+   ",
"  +%***&@@@@@@@@&****+  ",
"  +****&&@@@@@@&&****+  ",
"  +***&&&&@@@@&&&&***+  ",
" +%***&&&&&@@&&&&&****+ ",
" +***&&&&&&&&&&&&&&***+ ",
" %********************+ ",
" %********************+ ",
" %&&&&&&&&&&&&&&&&&&&&+ ",
" %&%%%%%%%%%%%%%%%%%%%+ ",
" %&%%%%%%%%%%%%%%%%%%%+ ",
" %&%&&&%%%%%%%@%%#%%.%+ ",
" %%%%%%%%%%%%%%%%%%%%%+ ",
" ++++++++++++++++++++++ ",
"                        "
]

clear_Icon = [
"24 24 9 1",
"   c None",
".  c #000200",
"+  c #8B0606",
"@  c #875209",
"#  c #E3383A",
"$  c #C19916",
"%  c #C4A163",
"&  c #E2C928",
"*  c #E4D05A",
"   @@@                  ",
"  @%%%@                 ",
"  @%*@@                 ",
"  @%@*%@                ",
"   @%$$%@               ",
"   @%%$%%@              ",
"    @%$$$*@             ",
"     @$**+++            ",
"     @*%+##+.           ",
"      ++##+*$           ",
"      +#++****$         ",
"      ++****&**$        ",
"       &**&*&&&*$       ",
"       &*&&&*&$&*$      ",
"       $*&*&$&&$$*$     ",
"       $*&$&*$*&*$*$    ",
"        *&$$&&$&&&&*$   ",
"        $*&$&**$$**@    ",
"        $*&$&****&$     ",
"         $*$***$$@      ",
"         $***$@ @       ",
"          $@$@          ",
"            @           ",
"                        "
]

delete_Icon = [
"24 24 3 1",
"   c None",
".  c #A40000",
"+  c #EE2A2A",
"                        ",
"                        ",
"       .         .      ",
"      .+.       .+.     ",
"     .+++.     .+++.    ",
"    .+++++.   .+++++.   ",
"   .+++++++. .+++++++.  ",
"    .+++++++.+++++++.   ",
"     .+++++++++++++.    ",
"      .+++++++++++.     ",
"       .+++++++++.      ",
"        .+++++++.       ",
"       .+++++++++.      ",
"      .+++++++++++.     ",
"     .+++++++++++++.    ",
"    .+++++++.+++++++.   ",
"   .+++++++. .+++++++.  ",
"    .+++++.   .+++++.   ",
"     .+++.     .+++.    ",
"      .+.       .+.     ",
"       .         .      ",
"                        ",
"                        ",
"                        "
]

memo_Allume_Icon = [
"24 24 9 1",
"   c None",
".  c #4F514E",
"+  c #635D41",
"@  c #676966",
"#  c #848784",
"$  c #888A87",
"%  c #E9D312",
"&  c #FEEE4D",
"*  c #FDFFFC",
"                        ",
"                        ",
"                        ",
"                        ",
"         %%%%%%         ",
"        %%&&&&%%        ",
"       %%&&&&&&%%       ",
"      %%&&&**&&&%%      ",
"     %%&&&****&&&%%     ",
"     %&&&******&&&%     ",
"     %&&&******&&&%     ",
"     %&&&******&&&%     ",
"     %%&&&****&&&%%     ",
"      %%&&&**&&&%%      ",
"       %%&&&&&&%%       ",
"        %%%&&%%%        ",
"         .%%%%+         ",
"         @.....         ",
"         ..#$$@         ",
"         @@....         ",
"         ..$$$@         ",
"         @@....         ",
"          $$$$          ",
"                        "
]

memo_Eteint_Icon = [
"24 24 9 1",
"   c None",
".  c #000000",
"+  c #204A87",
"@  c #555753",
"#  c #4F514E",
"$  c #635D41",
"%  c #676966",
"&  c #848784",
"*  c #888A87",
"                        ",
"                        ",
"                        ",
"                        ",
"         ......         ",
"        ........        ",
"       ..........       ",
"      ............      ",
"     ....+.+.+.+...     ",
"     ...+.+.+.++...     ",
"     ...@......@...     ",
"     ...@......@...     ",
"     ....@....@....     ",
"      ....@..@....      ",
"       ...@..@...       ",
"        ..@..@..        ",
"         #@..@$         ",
"         %#####         ",
"         ##&**%         ",
"         %%####         ",
"         ##***%         ",
"         %%####         ",
"          ****          ",
"                        "
]

origin_Icon = [
"24 24 14 1",
"   c None",
".  c #EF2929",
"+  c #A40000",
"@  c #DDDFDC",
"#  c #888A85",
"$  c #DDDEDB",
"%  c #DCDEDB",
"&  c #DCDEDC",
"*  c #DBDDDA",
"=  c #BABDB6",
"-  c #555753",
";  c #729FCF",
">  c #3465A4",
",  c #8191AA",
"                        ",
"                        ",
"           .+           ",
"          ..++          ",
"         ....++         ",
"        .....+++        ",
"       ....@#++++       ",
"      ....@@@#++++      ",
"     ....@@@@@#++++     ",
"    ....@@@@$@@#++++    ",
"   ....@@@$@@%@@#++++   ",
"  ....@@@@@@@@%@@#++++  ",
"  ...@@@%%%%&%%*@@#+++  ",
"  ..@@@@@@@@@@@@@@@#++  ",
"   #@@=#---@@=====@#    ",
"   #@@=#---@@;>>>;@#    ",
"   #@@,#---@@;>>>;@#    ",
"   #@@,#---@@;>>>;@#    ",
"   #@@=#---@@@#    ",
"   #@@=#---@@@@@@@@#    ",
"   #@@=##--@@@@@@@@#    ",
"   #################    ",
"                        ",
"                        "
]

zero_Icon = [
"24 24 6 1",
"   c None",
".  c #CC0000",
"+  c #000000",
"@  c #BABDB6",
"#  c #4E9A06",
"$  c #204A87",
"           ..           ",
"           ..           ",
"           ..           ",
"           ..           ",
"           ..           ",
"           ..           ",
"           ..           ",
"   ++@     ..@     ++@  ",
"  ++++@   +..+@   ++++@ ",
" ++@ ++@ ++..++@ ++@ ++@",
" +@   +@ +@.. +@ +@   +@",
"######+@###$$#+@######+@",
"######+@###$$#+@######+@",
" ++@ ++@ ++..++@ ++@ ++@",
"  ++++ +  ++++ +  ++++  ",
"   ++ ++   ++ ++   ++   ",
"      +    .. +         ",
"     ++    ..++         ",
"    ++     ..+          ",
"           ..           ",
"           ..           ",
"           ..           ",
"           ..           ",
"           ..           "
]

reset_Icon = [
"24 24 3 1",
"   c None",
".  c #3465A4",
"+  c #888A85",
"                        ",
"      ........          ",
"     .++++++++.         ",
"    .++..+....+.  ..... ",
"    .+.. .+....+. .+++. ",
"    .+.   .+....+..+.+. ",
"    ...    .+....+.+.+. ",
"            .+....+..+. ",
"             .+......+. ",
"              .+.....+. ",
"               .+....+. ",
"  ......        .+...+. ",
"  .++++.         .++++. ",
"  .+...+.        ...... ",
"  .+....+.              ",
"  .+.....+.             ",
"  .+......+.            ",
"  .+..+....+.           ",
"  .+.+.+....+.    ...   ",
"  .+.+..+....+.   .+.   ",
"  .+++. .+....+. ..+.   ",
"  .....  .+....+..++.   ",
"          .++++++++.    ",
"           ........     "
]

code_Python_Icon = [
"24 24 3 1",
"   c None",
".  c #3B7AAC",
"+  c #EDD400",
"                        ",
"  ++++++++++++++++++++. ",
"  +                   . ",
"  +                   . ",
"  +     .....         . ",
"  +    . .....        . ",
"  +    ....... +      . ",
"  +        ... +++    . ",
"  +   ........ ++++   . ",
"  +  ......... +++++  . ",
"  + .........  ++++++ . ",
"  + .......   +++++++ . ",
"  + ......  +++++++++ . ",
"  +  ..... +++++++++  . ",
"  +   .... ++++++++   . ",
"  +    ... +++        . ",
"  +      . +++++++    . ",
"  +        +++++ +    . ",
"  +         +++++     . ",
"  +                   . ",
"  +                   . ",
"  +                   . ",
"  +.................... ",
"                        "
]

code_FC_Icon = [
"24 24 5 1",
"   c None",
".  c #000000",
"+  c #CB0208",
"@  c #204A86",
"#  c #BABDB6",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"@@@    @@@    @@@    @@@",
"@        @    @        @",
"@   ++#  @    @   ++#  @",
"@  ++++# @    @  ++++# @",
"@ ++# ++#@    @ ++# ++#@",
"@ +#   +#@    @ +#   +#@",
"@ +#   +#@    @ +#   +#@",
"@ +#   +#@    @ +#   +#@",
"@ ++# ++#@    @ ++# ++#@",
"@  ++++  @    @  ++++  @",
"@   ++   @    @   ++   @",
"@        @    @        @",
"@        @    @        @",
"@@@    @@@  . @@@    @@@",
"           ..           ",
"           .            ",
"          ..            ",
"         ..             ",
"                        "
]

rotate_Icon = [
"24 24 4 1",
"   c None",
".  c #000100",
"+  c #000201",
"@  c #6695BF",
"                        ",
"       ++++++++         ",
"      +@@@@@@@@+        ",
"     +@@......@@++      ",
"    +@@.@@@@@@.@@@+ ++  ",
"   +@@.@@++++@@.@@@+@+  ",
"  +@@.@@+    +@@.@@@@+  ",
" +@@.@@+      +@@.@@@+  ",
" +@.@@+        +@@.@@@+ ",
" +@.@+       ++@@@@@@@+ ",
" +@.@+        ++@@@@@@+ ",
" +@.@+          +++@@@+ ",
" +@.@+            +++++ ",
" +@.@+                  ",
" +@.@@+                 ",
" +@@.@@+      +++       ",
"  +@@.@@+     +@+       ",
"   +@@.@@+++++@@+       ",
"    +@@.@@@@@@@@+       ",
"     +@@.....@@+        ",
"      +@@@@@@@++        ",
"       +++++++          ",
"                        ",
"                        "
]

translate_Icon = [
"24 24 9 1",
"   c None",
".  c #000100",
"+  c #000407",
"@  c #6694BF",
"#  c #6D92BE",
"$  c #6A93C5",
"%  c #6795C0",
"&  c #6F93C0",
"*  c #6896C1",
"                        ",
"                        ",
"          ..            ",
"          .@.           ",
"          .@@..         ",
"          .@@@@.        ",
"          .@@@@@.       ",
" ..........@@@@@@.      ",
"  +**&%%&@&@@@@@@@.     ",
" .............+@@@$..   ",
"  +@@@@@@@@@@@@@@@@@@.  ",
" ..........+@@@@@@@@@@. ",
"  +@@@@@@@@@@@@@@@@@@+  ",
" ........+@@@@@@@@@++   ",
"  +@@@@@@@@@@@@@@@.     ",
" ..........@@@@@@.      ",
"          .@@@@@.       ",
"          .@@@@.        ",
"          .@@..         ",
"          .@.           ",
"          ..            ",
"                        ",
"                        ",
"                        "
]

OnClickApply_Icon = [
"24 24 9 1",
"   c None",
".  c #910000",
"+  c #F20001",
"@  c #54595E",
"#  c #4B9A00",
"$  c #8A8C89",
"%  c #B0B2AE",
"&  c #FED758",
"*  c #DFE1DC",
"                        ",
"        ..              ",
"        .......         ",
"         ....++         ",
"         .+.+++         ",
"      ....+++++         ",
"      $.+++++++%%%%     ",
"     **$.++++++***&&    ",
"    %***$.+++++&*&&&    ",
"    *****$.++++&&&&*    ",
"   %******$.+++&&&**%   ",
"   *******&$.++&&&&**   ",
"   ***&&&&&&$.+&&&&&&&  ",
"  %*******&&&$.&&&&**%  ",
"  *********&&&$&&&****  ",
"  ********&&&&&&&&&***% ",
" %*******&&&*&&&*&&&**% ",
" %%%%%%%%&&%%%&%%%&&%%$ ",
" %%%$%%%%%%%%%&%@%#%+%$ ",
" %%%$$%%%%%%%%&%%%%%%%$ ",
" %%%%%%%%%%%%%&%%%%%%%$ ",
" $%%%%%%%%%%%%%%%%%%%%$ ",
"  @@@@@@@@@@@@@@@@@@@@@ ",
"                        "
]

normalWork_Icon = [
"24 24 9 1",
"   c None",
".  c #565854",
"+  c #555753",
"@  c #2E3436",
"#  c #FFFFFF",
"$  c #FCE94F",
"%  c #FEFEFE",
"&  c #EDD400",
"*  c #BABDB6",
"                        ",
" ...................... ",
" .                    . ",
" . +++++ +++++        . ",
" .                    . ",
" .                    . ",
" . +++++ +++++        . ",
" .                    . ",
" .                    . ",
" . +++++ +++++        . ",
" .                    . ",
" .                    . ",
" ...................... ",
"                        ",
"                        ",
"         @@@@@@@@@@@@@@@",
"         @#$$#########%@",
"         @#&&###@@@#@@%@",
"         @%&&%########%@",
"         @#**#########%@",
"         @@@@@@@@@@@@@@@",
"                        ",
"                        ",
"                        "
]

PointCenter_Icon = [
"24 24 9 1",
"   c None",
".  c #CB0007",
"+  c #363C3C",
"@  c #A34467",
"#  c #666768",
"$  c #756D98",
"%  c #999E9D",
"&  c #C2C4C0",
"*  c #E3E5E1",
"                        ",
"        +++++++         ",
"      ++%&***&#++       ",
"     +&***&&&***&+      ",
"    +**%#+++++%&**+     ",
"   +*&#+       +#&*+    ",
"  +**#+         +#**+   ",
" +%*#+           +#*%+  ",
" +*&+  .      .   +&*+  ",
"+#*%    ..  ..     %*#+ ",
"+%*#    ......     #*%+ ",
"+%*+     ....      +*%+ ",
"+%*+     ....      +*%+ ",
"+#*#    ......     #*#+ ",
" +*%    ..  ..     %*+  ",
" +&*   .      .   +*&+  ",
"  +*+            +%*+   ",
"  +&*+          +#*&+   ",
"   +&*++      ++%*&+    ",
"    +&**&+++++&**&+     ",
"     +#&*******%#+      ",
"      ++#%%%%%#++       ",
"        +++++++         ",
"                        "
]

positif_Icon = [
"24 24 9 1",
"   c None",
".  c #213B07",
"+  c #3B6212",
"@  c #487415",
"#  c #5AA713",
"$  c #66BB14",
"%  c #6FC31C",
"&  c #7ACE23",
"*  c #80D82B",
"                        ",
"                        ",
"         ++++++         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"  ++++++++****++++++++  ",
"  +******************+  ",
"  +******************+  ",
"  +******************+  ",
"  +******************+  ",
"  ++++++++****++++++++  ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         +****+         ",
"         ++++++         ",
"                        ",
"                        "
]

negatif_Icon = [
"24 24 9 1",
"   c None",
".  c #000100",
"+  c #3C0406",
"@  c #680A0D",
"#  c #7B0B13",
"$  c #B00206",
"%  c #C40D0D",
"&  c #D7171A",
"*  c #EA2525",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"  @@@@@@@@@@@@@@@@@@@@  ",
"  @******************@  ",
"  @******************@  ",
"  @******************@  ",
"  @******************@  ",
"  @@@@@@@@@@@@@@@@@@@@  ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        "
]


global objectPlacementAngle ; objectPlacementAngle = ""
def objectRealPlacement3D(obj)   *
    global objectPlacementAngle
    try   *
        objectPlacement      = obj.Shape.Placement
        #### 
        objectPlacementBase  = FreeCAD.Vector(objectPlacement.Base)
        ####
        objectWorkCenter     = objectPlacementBase
        ####
        objectPlacementAngle = objectPlacement.Rotation.toEuler()

        if hasattr(obj, "getGlobalPlacement")   *
            globalPlacement       = obj.getGlobalPlacement()
            globalPlacementBase   = FreeCAD.Vector(globalPlacement.Base)
            objectRealPlacement3D = globalPlacementBase.add(objectWorkCenter).sub(objectPlacementBase)
            objectPlacementAngle  = globalPlacement.Rotation.toEuler()
        else   *
            objectRealPlacement3D = objectWorkCenter

        return objectRealPlacement3D
    except Exception   *
        return FreeCAD.Vector(0.0, 0.0, 0.0)

try   *
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError   *
    def _fromUtf8(s)   *
        return s
        
class Ui_MainWindow(object)   *
    def __init__(self )   *
        global path, path2
        self.window = MainWindow
        self.path = path

        self.vueActive = FreeCADGui.ActiveDocument.ActiveView
        self.click = self.vueActive.addEventCallback("SoMouseButtonEvent",self.souris)

    def souris(self,info)   *
        global sourisPass
        if (info["Button"] == "BUTTON1") and (info["State"] == "DOWN")   *
            #time.sleep(0.02)
            sourisPass = 0
            #print("ok")

    def setupUi(self, MainWindow)   *
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        global saveListView

#        MainWindow.resize(360, 300)
#        MainWindow.setMinimumSize(QtCore.QSize(330, 10))
#        MainWindow.setMaximumSize(QtCore.QSize(330, 330))
#        MainWindow.setStyleSheet("background-color   * rgb(50, 50, 50);")  
#        MainWindow.move(900, 100)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        ####
        self.groupBox_Rotation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Rotation.setEnabled(False)

        self.RB_Bond_Box_Center = QtWidgets.QRadioButton()
        self.RB_Bond_Box_Center.setChecked(True)
        self.RB_Bond_Box_Center.setIcon(QtGui.QIcon(QtGui.QPixmap(boundBox_Center_Icon))) #icone dans une variable 
        self.RB_Bond_Box_Center.clicked.connect(self.on_RB_CenterRot)

        self.RB_Center_Mass = QtWidgets.QRadioButton()
        self.RB_Center_Mass.setIcon(QtGui.QIcon(QtGui.QPixmap(centerMass_Icon))) # icone dans une variable 
        self.RB_Center_Mass.clicked.connect(self.on_RB_CenterRot)

        self.RB_Point_Clicked = QtWidgets.QRadioButton()
        self.RB_Point_Clicked.setIcon(QtGui.QIcon(QtGui.QPixmap(point_Clicked_Icon))) # icone dans une variable 
        self.RB_Point_Clicked.clicked.connect(self.on_RB_CenterRot)

        ####
        self.groupBox_Axis = QtWidgets.QGroupBox()
        self.groupBox_Axis.setEnabled(False)

        self.RB_Rotation_0 = QtWidgets.QRadioButton()    # factice pour bouton invisible
        self.RB_Rotation_0.setVisible(False)
#        self.RB_Rotation_0.clicked.connect(self.on_RB_Rotation_0)

        self.RB_Rotation_X = QtWidgets.QRadioButton()
        self.RB_Rotation_X.setChecked(True)
        self.RB_Rotation_X.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_Z_Icon))) # icone dans une variable 
        self.RB_Rotation_X.clicked.connect(self.on_RB_Rotation_X)

        self.RB_Rotation_Y = QtWidgets.QRadioButton()
        self.RB_Rotation_Y.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_Y_Icon))) # icone dans une variable 
        self.RB_Rotation_Y.clicked.connect(self.on_RB_Rotation_Y)
#        self.RB_Angle_Y.setFont(QtGui.QFont(self.FontImpost,weight=QtGui.QFont.Bold))  # Bold
#        self.RB_Angle_Y.setStyleSheet("color    * #008700")                         # Color text

        self.RB_Rotation_Z = QtWidgets.QRadioButton()
        self.RB_Rotation_Z.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_X_Icon))) # icone dans une variable 
        self.RB_Rotation_Z.clicked.connect(self.on_RB_Rotation_Z)

        self.RB_Direction_D = QtWidgets.QRadioButton()
        self.RB_Direction_D.setIcon(QtGui.QIcon(QtGui.QPixmap(direction_Icon))) # icone dans une variable 
        self.RB_Direction_D.clicked.connect(self.on_RB_Direction_D)
        ####

        self.groupBox_Pos_Mouse = QtWidgets.QGroupBox()
        self.groupBox_Pos_Mouse.setEnabled(False)

        self.DS_Pos_Mouse_X = QtWidgets.QDoubleSpinBox()
        self.DS_Pos_Mouse_X.setMinimum(-999999.9)
        self.DS_Pos_Mouse_X.setMaximum(99999999.9)
        self.DS_Pos_Mouse_X.setDecimals(6)
        self.DS_Pos_Mouse_X.setSuffix(" X")
#        self.DS_Pos_Mouse_X.setIcon(QtGui.QIcon(QtGui.QPixmap(CameraToFace))) # icone dans une variable 
        self.DS_Pos_Mouse_X.valueChanged.connect(self.on_DS_Pos_Mouse_X)

        self.DS_Pos_Mouse_Y = QtWidgets.QDoubleSpinBox()
        self.DS_Pos_Mouse_Y.setMinimum(-999999.9)
        self.DS_Pos_Mouse_Y.setMaximum(99999999.9)
        self.DS_Pos_Mouse_Y.setDecimals(6)
        self.DS_Pos_Mouse_Y.setSuffix(" Y")
#        self.PB_To_Face.setIcon(QtGui.QIcon(QtGui.QPixmap(CameraToFace))) # icone dans une variable 
        self.DS_Pos_Mouse_Y.valueChanged.connect(self.on_DS_Pos_Mouse_Y)

        self.DS_Pos_Mouse_Z = QtWidgets.QDoubleSpinBox()
        self.DS_Pos_Mouse_Z.setMinimum(-999999.9)
        self.DS_Pos_Mouse_Z.setMaximum(99999999.9)
        self.DS_Pos_Mouse_Z.setDecimals(6)
        self.DS_Pos_Mouse_Z.setSuffix(" Z")
#        self.PB_To_Face.setIcon(QtGui.QIcon(QtGui.QPixmap(CameraToFace))) # icone dans une variable 
        self.DS_Pos_Mouse_Z.valueChanged.connect(self.on_DS_Pos_Mouse_Z)

        ####
        self.groupBox_Work = QtWidgets.QGroupBox()
        self.groupBox_Work.setEnabled(False)

#        self.SC_Slider_Bar = QtWidgets.QSlider()
#        self.SC_Slider_Bar.setMinimum(0.0)
#        self.SC_Slider_Bar.setMaximum(359.0)
#        self.SC_Slider_Bar.setValue(0.0)
#        self.SC_Slider_Bar.setSliderPosition(0)
#        self.SC_Slider_Bar.setOrientation(QtCore.Qt.Horizontal)
#        self.SC_Slider_Bar.valueChanged.connect(self.on_SC_Slider_Bar)

        self.LE_Increment = QtWidgets.QLineEdit()
        self.LE_Increment.setReadOnly(True)
        self.LE_Increment.setText(str(0.0))
        #self.LE_Increment.returnPressed.connect(self.on_LE_Increment_Pressed)
        self.LE_Increment.textChanged.connect(self.on_LE_Increment_Pressed)

        self.DS_Value_Angle_Dimension = QtWidgets.QDoubleSpinBox()
        self.DS_Value_Angle_Dimension.setMinimum(-360.0)
        self.DS_Value_Angle_Dimension.setMaximum(360.0)
        self.DS_Value_Angle_Dimension.setSuffix(" Degrees")
        self.DS_Value_Angle_Dimension.setDecimals(4)
        self.DS_Value_Angle_Dimension.valueChanged.connect(self.on_DS_Value_Angle_Dimension)

        self.PB_Negatif = QtWidgets.QPushButton()
        self.PB_Negatif.setIcon(QtGui.QIcon(QtGui.QPixmap(negatif_Icon))) # icone dans une variable 
        self.PB_Negatif.clicked.connect(self.on_PB_Negatif_clicked)

        self.PB_Apply = QtWidgets.QPushButton()
        self.PB_Apply.setAutoRepeat(True)
        self.PB_Apply.setIcon(QtGui.QIcon(QtGui.QPixmap(apply_Icon))) # icone dans une variable 
        self.PB_Apply.clicked.connect(self.on_PB_Apply_clicked)

        self.CB_Position = QtWidgets.QCheckBox()
        #self.CB_Position.setEnabled(False)
        self.CB_Position.setIcon(QtGui.QIcon(QtGui.QPixmap(translate_Icon))) #icone dans une variable 
        self.CB_Position.clicked.connect(self.on_CB_Position)

        self.PB_Point = QtWidgets.QPushButton()
        #self.PB_Point.setEnabled(False)
        self.PB_Point.setIcon(QtGui.QIcon(QtGui.QPixmap(point_Icon))) # icone dans une variable 
        self.PB_Point.clicked.connect(self.on_CB_Point)

        self.PB_PointCenter = QtWidgets.QPushButton()
        #self.PB_PointCenter.setEnabled(False)
        self.PB_PointCenter.setIcon(QtGui.QIcon(QtGui.QPixmap(PointCenter_Icon))) # icone dans une variable 
        self.PB_PointCenter.clicked.connect(self.on_PB_PointCenter)

        self.CBox_View = QtWidgets.QComboBox()
        #QtCore.QObject.connect(self.CBox_View, QtCore.SIGNAL("currentIndexChanged(QString)"), self.on_CBox_View)
        QtCore.QObject.connect(self.CBox_View, QtCore.SIGNAL("activated(QString)"), self.on_CBox_View)

        self.CBox_Impost = QtWidgets.QComboBox()
        self.CBox_Impost.setCurrentIndex(4)
        self.CBox_Impost.setMaxVisibleItems(16)
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        self.CBox_Impost.addItem("")
        QtCore.QObject.connect(self.CBox_Impost, QtCore.SIGNAL("currentIndexChanged(QString)"), self.on_CBox_Impost)

        self.CBox_Memory = QtWidgets.QComboBox()
        #self.CBox_Memory.addItem("")
        self.CBox_Memory.setDuplicatesEnabled(True) #False
        #QtCore.QObject.connect(self.CBox_Memory, QtCore.SIGNAL("currentIndexChanged(QString)"), self.on_CBox_Memory)
        QtCore.QObject.connect(self.CBox_Memory, QtCore.SIGNAL("activated(QString)"), self.on_CBox_Memory)

        self.groupBox_Data = QtWidgets.QGroupBox()
        self.groupBox_Data.setEnabled(False)

        self.TE_Memorize = QtWidgets.QListView()
        saveListView = QtGui.QStandardItemModel()
        self.TE_Memorize.setModel(saveListView)
        self.TE_Memorize.setSelectionRectVisible(True)#
        self.TE_Memorize.setAlternatingRowColors(True)#
        self.TE_Memorize.setStyleSheet("alternate-background-color   *#fdeeee;")
        self.TE_Memorize.clicked[QtCore.QModelIndex].connect(self.on_TE_Clicked)

        self.PB_Save_Memorize = QtWidgets.QPushButton()
        self.PB_Save_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(save_Icon))) # icone dans une variable 
        self.PB_Save_Memorize.clicked.connect(self.on_PB_Save_Memorize)

        self.PB_ClearMemo = QtWidgets.QPushButton()
        self.PB_ClearMemo.setIcon(QtGui.QIcon(QtGui.QPixmap(clear_Icon))) # icone dans une variable 
        self.PB_ClearMemo.clicked.connect(self.on_PB_ClearMemo)

        self.PB_Delete_Line_Memory = QtWidgets.QPushButton()
        self.PB_Delete_Line_Memory.setIcon(QtGui.QIcon(QtGui.QPixmap(delete_Icon))) # icone dans une variable 
        self.PB_Delete_Line_Memory.clicked.connect(self.on_PB_Delete_Line_Memory)

        self.PB_Memorize = QtWidgets.QPushButton()
        self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Eteint_Icon))) # icone dans une variable 
        self.PB_Memorize.clicked.connect(self.on_PB_Memorize)

        self.CB_On_Click_Apply = QtWidgets.QCheckBox()
        self.CB_On_Click_Apply.setIcon(QtGui.QIcon(QtGui.QPixmap(OnClickApply_Icon))) # icone dans une variable 
        self.CB_On_Click_Apply.clicked.connect(self.on_CB_On_Click_Apply)

        self.CB_DataInMacro = QtWidgets.QCheckBox()
        self.CB_DataInMacro.setIcon(QtGui.QIcon(QtGui.QPixmap(code_Python_Icon))) # icone dans une variable 
        self.CB_DataInMacro.clicked.connect(self.On_CB_DataInMacro)

        self.label_00 = QtWidgets.QLabel()
        self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
        ####

        self.groupBox_Command = QtWidgets.QGroupBox()

        self.PB_Quit = QtWidgets.QPushButton()
        self.PB_Quit.setIcon(QtGui.QIcon(QtGui.QPixmap(quit_Icon))) # icone dans une variable 
        self.PB_Quit.clicked.connect(self.on_PB_Quit_clicked)

        self.PB_Original = QtWidgets.QPushButton()
        self.PB_Original.setIcon(QtGui.QIcon(QtGui.QPixmap(origin_Icon))) # icone dans une variable 
        self.PB_Original.clicked.connect(self.on_PB_Original_clicked)

        self.PB_Zero = QtWidgets.QPushButton()
        self.PB_Zero.setIcon(QtGui.QIcon(QtGui.QPixmap(zero_Icon))) # icone dans une variable 
        self.PB_Zero.clicked.connect(self.on_PB_Zero_clicked)

        self.PB_Reset = QtWidgets.QPushButton()
        self.PB_Reset.setIcon(QtGui.QIcon(QtGui.QPixmap(reset_Icon))) # icone dans une variable 
        self.PB_Reset.clicked.connect(self.on_PB_Reset_clicked)

        #### Gridlayout Header
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout_00_00 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_00_00.setContentsMargins(10, 10, 10, 10)#Gauche Haut Droit Bas
        #### Gridlayout Header
        #### Gridlayout BEGIN
        self.grid_00_01 = QtWidgets.QGridLayout()
#        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_Rotation)
        self.grid_00_01.addWidget(self.groupBox_Rotation, 0, 0, 1, 1)
        self.grid_00_01.setContentsMargins(0, 0, 0, 0)                    #Gauche Haut Droite Bas
        self.grid_00_01_00 = QtWidgets.QGridLayout(self.groupBox_Rotation)
        self.grid_00_01_00.setContentsMargins(10, 10, 0, 10)
        self.grid_00_01_00.addWidget(self.RB_Bond_Box_Center, 0, 0, 1, 1)
        self.grid_00_01_00.addWidget(self.RB_Center_Mass, 1, 0, 1, 1)
        self.grid_00_01_00.addWidget(self.RB_Point_Clicked, 2, 0, 1, 1)
        self.gridLayout_00_00.addLayout(self.grid_00_01, 0, 0, 1, 1)
        ####
        self.grid_00_02 = QtWidgets.QGridLayout()
        self.grid_00_02.addWidget(self.groupBox_Axis, 0, 0, 1, 1)
        self.grid_00_02.setContentsMargins(0, 0, 0, 0)
        self.grid_00_02_00 = QtWidgets.QGridLayout(self.groupBox_Axis)
        self.grid_00_02_00.setContentsMargins(10, 10, 0, 10)
        self.grid_00_02_00.addWidget(self.RB_Rotation_X, 0, 0, 1, 1)
        self.grid_00_02_00.addWidget(self.RB_Rotation_Y, 1, 0, 1, 1)
        self.grid_00_02_00.addWidget(self.RB_Rotation_Z, 2, 0, 1, 1)
        self.grid_00_02_00.addWidget(self.RB_Direction_D, 3, 0, 1, 1)
        self.gridLayout_00_00.addLayout(self.grid_00_02, 0, 1, 1, 1)
        ####
        self.grid_00_03 = QtWidgets.QGridLayout()
        self.grid_00_03.addWidget(self.groupBox_Pos_Mouse, 1, 0, 1, 1)
        self.grid_00_03.setContentsMargins(0, 0, 0, 0)
        self.grid_00_03_00 = QtWidgets.QGridLayout(self.groupBox_Pos_Mouse)
        self.grid_00_03_00.setContentsMargins(10, 10, 10, 10)
        self.grid_00_03_00.addWidget(self.DS_Pos_Mouse_X, 0, 0, 1, 1)
        self.grid_00_03_00.addWidget(self.DS_Pos_Mouse_Y, 0, 1, 1, 1)
        self.grid_00_03_00.addWidget(self.DS_Pos_Mouse_Z, 0, 2, 1, 1)
        self.gridLayout_00_00.addLayout(self.grid_00_03, 1, 0, 1, 2)
        ####
        self.grid_00_044 = QtWidgets.QGridLayout()
        self.grid_00_044.addWidget(self.groupBox_Work, 2, 0, 1, 1)
        self.grid_00_044.setContentsMargins(0, 0, 0, 0)
        self.grid_00_044_00 = QtWidgets.QGridLayout(self.groupBox_Work)
        self.grid_00_044_00.addWidget(self.CB_Position, 0, 0, 1, 1)
        self.grid_00_044_00.addWidget(self.PB_Point, 0, 1, 1, 1)
        self.grid_00_044_00.addWidget(self.PB_PointCenter, 0, 2, 1, 1)
        #
        self.grid_00_044_00.addWidget(self.CBox_View, 1, 0, 1, 1)
        self.grid_00_044_00.addWidget(self.CBox_Impost, 1, 1, 1, 1)
        self.grid_00_044_00.addWidget(self.CBox_Memory, 1, 2, 1, 1)
        #
        self.grid_00_044_00.addWidget(self.PB_Negatif, 2, 0, 1, 1)
        self.grid_00_044_00.addWidget(self.DS_Value_Angle_Dimension, 2, 1, 1, 1)
        self.grid_00_044_00.addWidget(self.PB_Apply, 2, 2, 1, 1)
        #
        self.grid_00_044_00.addWidget(self.LE_Increment, 3, 0, 1, 3)
        self.grid_00_044_00.addWidget(self.label_00, 4, 0, 1, 3)
        self.gridLayout_00_00.addLayout(self.grid_00_044, 2, 0, 1, 2)
        ####
        self.grid_00_044b = QtWidgets.QGridLayout()
        self.grid_00_044b.addWidget(self.groupBox_Data, 3, 0, 1, 1)
        self.grid_00_044b.setContentsMargins(0, 0, 0, 0)
        self.grid_00_044b_00 = QtWidgets.QGridLayout(self.groupBox_Data)
        self.grid_00_044b_00.addWidget(self.TE_Memorize, 0, 0, 1, 4)
        self.grid_00_044b_00.addWidget(self.PB_Save_Memorize, 1, 0, 1, 1)
        self.grid_00_044b_00.addWidget(self.PB_ClearMemo, 1, 1, 1, 1)
        self.grid_00_044b_00.addWidget(self.PB_Delete_Line_Memory, 1, 2, 1, 1)
        self.grid_00_044b_00.addWidget(self.PB_Memorize, 1, 3, 1, 1)
        self.grid_00_044b_00.addWidget(self.CB_DataInMacro, 2, 0, 1, 1)
        self.grid_00_044b_00.addWidget(self.CB_On_Click_Apply, 2, 1, 1, 1)
        self.gridLayout_00_00.addLayout(self.grid_00_044b, 3, 0, 1, 2)
        ####
        self.grid_00_08 = QtWidgets.QGridLayout()
        self.grid_00_08.addWidget(self.groupBox_Command, 4, 0, 1, 1)
        self.grid_00_08.setContentsMargins(0, 0, 0, 0)
        self.grid_00_08_00 = QtWidgets.QGridLayout(self.groupBox_Command)
        self.grid_00_08_00.addWidget(self.PB_Quit, 0, 0, 1, 1)
        self.grid_00_08_00.addWidget(self.PB_Original, 0, 1, 1, 1)
        self.grid_00_08_00.addWidget(self.PB_Zero, 0, 2, 1, 1)
        self.grid_00_08_00.addWidget(self.PB_Reset, 0, 3, 1, 1)
        self.gridLayout_00_00.addLayout(self.grid_00_08, 4, 0, 1, 2)
        #### Gridlayout END

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow)   *
        global path

        MainWindow.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint)        # this function turns the front window (stay to hint)
        MainWindow.setWindowIcon(QtGui.QIcon(self.path+"Macro_Rotate_To_Point.png")) # change l'icone de la fenetre principale
        MainWindow.setWindowTitle(__title__ + " (" + __version__ + "    * " + __date__ + " (rmu)")

        _translate = QtCore.QCoreApplication.translate
        self.groupBox_Rotation.setTitle(_translate("MainWindow", "Point Rotation"))
        self.RB_Bond_Box_Center.setText(_translate("MainWindow", "Bounbox Center"))
        self.RB_Bond_Box_Center.setToolTip(_translate("MainWindow", "Point rotation on BoundBox Center"))
        self.RB_Center_Mass.setText(_translate("MainWindow", "Center of Mass"))
        self.RB_Center_Mass.setToolTip(_translate("MainWindow", "Point rotation on Center Mass"))
        self.RB_Point_Clicked.setText(_translate("MainWindow", "Point clicked"))
        self.RB_Point_Clicked.setToolTip(_translate("MainWindow", "Point rotation on Point Mouse clicked on the object"+"\n"
                                         "If twoo points are clicked, the second point is used for axis rotation"+"\n"
                                         "The point axis rotation Can be changed during the work as long as the object is selected"+"\n"
                                         "For this press the CTRL KEY and click the new point rotation"))
        ####
        self.groupBox_Axis.setTitle(_translate("MainWindow", "Axis Rotation"))
        self.RB_Rotation_X.setText(_translate("MainWindow", "Rotation(Z) Yaw"))
        self.RB_Rotation_X.setToolTip(_translate("MainWindow", "Rotation on Axis Yaw (Z)"))
        self.RB_Rotation_Y.setText(_translate("MainWindow", "Rotation(Y) Pitch"))
        self.RB_Rotation_Y.setToolTip(_translate("MainWindow", "Rotation on Axis Pitch (Y)"))
        self.RB_Rotation_Z.setText(_translate("MainWindow", "Rotation(X) Roll"))
        self.RB_Rotation_Z.setToolTip(_translate("MainWindow", "Rotation on Axis Roll (X)"))
        self.RB_Direction_D.setText(_translate("MainWindow", "Direction"))
        self.RB_Direction_D.setToolTip(_translate("MainWindow", "Rotation or Translation on Direction" + "\n"
                                                                "For use the Direction option   *" + "\n"
                                                                "Select First   * the object to Rotate/Translate" + "\n"
                                                                "Second   * the path   * Line, Wire or Edge"))
        ####
        self.groupBox_Work.setTitle(_translate("MainWindow", "Work"))
        self.groupBox_Pos_Mouse.setTitle(_translate("MainWindow", "Coordinates Point clicked"))
        self.groupBox_Pos_Mouse.setToolTip(_translate("MainWindow", "Position click mouse modification possible only with mode Point clicked"))
        self.DS_Pos_Mouse_X.setToolTip(_translate("MainWindow", "Position click mouse X" + "\n" +
                                       "modification only with mode Point clicked"))
        self.DS_Pos_Mouse_Y.setToolTip(_translate("MainWindow", "Position click mouse Y" + "\n" +
                                       "modification only with mode Point clicked"))
        self.DS_Pos_Mouse_Z.setToolTip(_translate("MainWindow", "Position click mouse Z" + "\n" +
                                       "modification only with mode Point clicked"))
        ####
        self.CB_Position.setText(_translate("MainWindow", "Translation"))
        self.CB_Position.setToolTip(_translate("MainWindow", "Check for move the object to axis choice X, Y or Z"))
        self.PB_Point.setText(_translate("MainWindow", "Point"))
        self.PB_Point.setToolTip(_translate("MainWindow", "Create one point to visualise the point rotation"))
        self.PB_PointCenter.setText(_translate("MainWindow", "Center"))
        self.PB_PointCenter.setToolTip(_translate("MainWindow", "Create one point on center face, circle "))
        self.LE_Increment.setToolTip(_translate("MainWindow", "Display the original Data + the modification"))
        #
        #self.CBox_View.setItemText(0,_translate("MainWindow",  "0"))
        self.CBox_View.setToolTip(_translate("MainWindow", "Memorize the view associate with the Object worked" + "\n"
                                             "For automate the zoom on object clicked, see   *" + "\n"
                                             "User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__ + " > switchZoomOnCilck" "\n"
                                             "and check the 'switchZoomOnCilck' option on True and restart " + __title__ ))

        self.CBox_Impost.setCurrentIndex(4)
        self.CBox_Impost.setMaxVisibleItems(16)
        self.CBox_Impost.setItemText(0, "0.0001")
        self.CBox_Impost.setItemText(1, "0.001")
        self.CBox_Impost.setItemText(2, "0.01")
        self.CBox_Impost.setItemText(3, "0.1")
        self.CBox_Impost.setItemText(4, "0")
        self.CBox_Impost.setItemText(5, "1")
        self.CBox_Impost.setItemText(6, "5")
        self.CBox_Impost.setItemText(7, "10")
        self.CBox_Impost.setItemText(8, "20")
        self.CBox_Impost.setItemText(9, "30")
        self.CBox_Impost.setItemText(10, "40")
        self.CBox_Impost.setItemText(11, "45")
        self.CBox_Impost.setItemText(12, "60")
        self.CBox_Impost.setItemText(13, "90")
        self.CBox_Impost.setItemText(14, "120")
        self.CBox_Impost.setItemText(15, "180")
        self.CBox_Impost.setToolTip(_translate("MainWindow", "Value standard imposted"))
        #
        self.CBox_Memory.setItemText(0,_translate("MainWindow",  "0"))
        self.CBox_Memory.setToolTip(_translate("MainWindow", "Value used memorized"))
        #
        self.DS_Value_Angle_Dimension.setToolTip(_translate("MainWindow", "Enter the modification"))
        self.PB_Negatif.setText(_translate("MainWindow", "Invert"))
        self.PB_Apply.setToolTip(_translate("MainWindow", "Apply the modification"))
        self.PB_Apply.setText(_translate("MainWindow", "Apply"))
        self.label_00.setText(_translate("MainWindow", " Select one Object or give one value Angle/Dimension"))
        #self.label_00.setToolTip("Display the modification Axis and Rotation or Position")
        ####
        self.groupBox_Data.setTitle(_translate("MainWindow", "Data"))
        self.PB_Save_Memorize.setText(_translate("MainWindow", "Save"))
        self.PB_Save_Memorize.setToolTip(_translate("MainWindow", "Save the memorized placement" + "\n"
                                                    "Format to save    * [Placement.Base], [Placement.Rotation.toEuler]" + "\n"
                                                    "Ex   * [0.0,0.0,0.0],[0.0,0.0,0.0] with the ext   * .CoorInfo" + "\n"
                                                    "If the file exist, the data is saved in Append (adding) mode" + "\n"
                                                    "If the CheckBox is checked for a Macro the file is saved in Write mode"))
        self.PB_ClearMemo.setText(_translate("MainWindow", "Clear"))
        self.PB_ClearMemo.setToolTip(_translate("MainWindow", "Clear the memo data" + "\n"
                                                              "The Reset button is not actif for this option"))
        self.PB_Delete_Line_Memory.setText(_translate("MainWindow", "Delete"))
        self.PB_Delete_Line_Memory.setToolTip(_translate("MainWindow", "Delete the line selected"))
        self.PB_Memorize.setText(_translate("MainWindow", "Memorize"))
        self.PB_Memorize.setToolTip(_translate("MainWindow", "Memorize the placement displayed"))
        self.CB_DataInMacro.setText(_translate("MainWindow", "Macro"))
        self.CB_DataInMacro.setToolTip(_translate("MainWindow", "If checked, the coordinate is saved in Python code (complete macro) in your Macro directory" + "\n"
                                                                "Actual    * " + path + "\n"
                                                                "Select the object and run the macro" + "\n"
                                                                "\t" + "The macro saved has various options    *" + "\n"
                                                                "\t" + " (Q)uit, (D)ecrease, (I)ncrease, (P)ause, (S)tep, (M)emo" + "\n"
                                                                "If this is not checked, the data hare saved in coordinate mode" + "\n"
                                                                "\t" + "Ex   * [0.0,0.0,0.0],[0.0,0.0,0.0] with the ext   * .CoorInfo" + "\n"))
        self.CB_On_Click_Apply.setText(_translate("MainWindow", "Memo on click"))
        self.CB_On_Click_Apply.setToolTip(_translate("MainWindow", "Memorize the coordinates on all Click Apply button"))
        ####
        self.groupBox_Command.setTitle(_translate("MainWindow", "Command"))
        self.PB_Quit.setText(_translate("MainWindow", "Quit"))
        self.PB_Quit.setToolTip(_translate("MainWindow", "Quite the macro"))
        self.PB_Original.setText(_translate("MainWindow", "Original"))
        self.PB_Original.setToolTip(_translate("MainWindow", "Move the object to the original position"))
        self.PB_Reset.setText(_translate("MainWindow", "Reset"))
        self.PB_Reset.setToolTip(_translate("MainWindow", "Reset the complete data macro"))
        self.PB_Zero.setText(_translate("MainWindow", "0,0,0"))
        self.PB_Zero.setToolTip(_translate("MainWindow", "Move the object to the base coordinates 0, 0, 0"))

    def on_DS_Pos_Mouse_X(self,val)   *
        global positionMouse
        global axisX

        positionMouse = [val, positionMouse[1], positionMouse[2]]
        axisX = positionMouse[0]
        self.DS_Pos_Mouse_X.setValue(axisX)
#        print("on_DS_Pos_Mouse_X ", val)

    def on_DS_Pos_Mouse_Y(self,val)   *
        global positionMouse
        global axisY

        positionMouse = [positionMouse[0], val, positionMouse[2]]
        axisY = positionMouse[1]
        self.DS_Pos_Mouse_Y.setValue(axisY)
#        print("on_DS_Pos_Mouse_Y ", val)

    def on_DS_Pos_Mouse_Z(self,val)   *
        global positionMouse
        global axisZ

        positionMouse = [positionMouse[0], positionMouse[1], val]
        axisZ = positionMouse[2]
        self.DS_Pos_Mouse_Z.setValue(axisZ)
#        print("on_DS_Pos_Mouse_Z ", val)

#    def on_SC_Slider_Bar(self,val)   *
#        global ui
#        global valeur
#        global myObject
#
#        if (myObject != "") and (self.CB_Free.isChecked())   *
#            valeur = val
#            self.DS_Value_Angle_Dimension.setValue(1)
#            self.SC_Slider_Bar.setValue(valeur)
#            ui.on_PB_Apply_clicked()
#
##            if self.CB_Free.isChecked()   *
##                ui.on_PB_Apply_clicked()
##        else   *
##            self.DS_Value_Angle_Dimension.setValue(0.0)
##            self.SC_Slider_Bar.setValue(0.0)

#        print("on_SC_Scroll_Bar ", valeur)

    def on_PB_Delete_Line_Memory(self)   *    #self.TE_Memorize    #QListView
        global countMemory
        global saveOnDisk

        self.model = model = QtGui.QStandardItemModel()
        try   *
            self.PB_Delete_Line_Memory.setStyleSheet("Base")
            lineSelected = self.TE_Memorize.selectionModel().selectedRows()[0].row()
            #textLigne = self.TE_Memorize.selectionModel().currentIndex().data() # affiche la ligne selectionnee
            self.TE_Memorize.model().removeRow(lineSelected)
            del saveOnDisk[lineSelected]
            countMemory -= 1
            self.PB_Memorize.setText("Memo (" + str(countMemory) + ")")
        except Exception   *
            self.PB_Delete_Line_Memory.setStyleSheet("background-color   * rgb(255, 0, 0)")
#        print("on_PB_Delete_Line_Memory ")

    def on_TE_Clicked(self, index)   *    # click dans la fenetre 
        global saveOnDisk
        global saveListView
        global memorySelected        

####ori colore la ligne######
#        item = saveListView.itemFromIndex(index)
#        item.setBackground(QtGui.QBrush(QtGui.QColor("#ef1919")))
#        if (item.index().row()) in memorySelected   *
##            memorySelected.remove(item.index().row())
#            baseBackground = self.TE_Memorize.palette().color(QPalette.Window)
#            item.setBackground(QtGui.QBrush(QtGui.QColor(baseBackground)))
#        else   *
#            memorySelected.append(item.index().row())
##        print(memorySelected)
####ori colore la ligne######

        item = saveListView.itemFromIndex(index)
        memorySelected = []
        memorySelected.append(item.index().row())
#        print("on_TE_Clicked ",memorySelected[0])    #self.TE_Memorize

    def on_PB_PointCenter(self)   *
        global objectPlacementAngle

        try   *
            sel = FreeCADGui.Selection.getSelection()
            placementOrigine = objectRealPlacement3D(FreeCAD.ActiveDocument.getObject(sel[0].Name))# search the original Placement
            Part.show(FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy())               # create repro shape subObject
            a = App.ActiveDocument.ActiveObject
            a.Placement.Base = placementOrigine
            a.Placement.Rotation = App.Rotation(objectPlacementAngle[0], objectPlacementAngle[1], objectPlacementAngle[2])
            point = Draft.makePoint(a.Shape.BoundBox.Center)
            App.ActiveDocument.ActiveObject.recompute()
            #App.ActiveDocument.ActiveObject.touch()
            App.ActiveDocument.ActiveObject.purgeTouched()
        except Exception   *
            self.PB_PointCenter.setStyleSheet("background-color   * red")
        try   *
            App.ActiveDocument.removeObject(a.Name)
        except Exception   *
            None
#        print("on_PB_PointCenter")

    def on_PB_Memorize(self)   *
        global myObject
        global myObjectName
        global saveOnDisk
        global saveListView
        global countMemory
        global valeur

#        if (valeur != 0)   *
        self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Allume_Icon))) # icone dans une variable 
        countMemory += 1
        xPB = str(myObject.Placement.Base[0])
        yPB = str(myObject.Placement.Base[1])
        zPB = str(myObject.Placement.Base[2])
        xPR = str(myObject.Placement.Rotation.toEuler()[0])
        yPR = str(myObject.Placement.Rotation.toEuler()[1])
        zPR = str(myObject.Placement.Rotation.toEuler()[2])
        #####
        #           #myObjectName , [(3.7,0.0,41.8),          (0.0,3.0,0.0)],
        #           #nomObjet     , Placement.Base ,          Placement.Rotation.toEuler()
        dummy = '["' + str(myObjectName) + '",' + "("+xPB+","+yPB+","+zPB+"),("+xPR+","+yPR+","+zPR+")],"
        ####
        saveOnDisk.append(dummy)
        self.PB_Memorize.setText("Memo (" + str(countMemory) + ")")
        self.PB_Memorize.setStyleSheet("background-color   * rgb(188, 245, 169)"); # bouton
        self.PB_Delete_Line_Memory.setStyleSheet("Base")
        item = QtGui.QStandardItem(dummy)
        saveListView.appendRow(item)
#        else   *
#            self.PB_Memorize.setStyleSheet("background-color   * #ff0000;")
#            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Eteint_Icon))) # icone dans une variable 
##        print("on_PB_Memorize ",saveListView,"  ",str(countMemory))

    def on_PB_Save_Memorize(self)   *  # Save_Memorize in macro file
        global pathFile
        global saveOnDisk
        global countMemory
        global path

        if countMemory != 0   *
            if self.CB_DataInMacro.isChecked()   *
#                SaveName, Filter = PySide2.QtWidgets.QFileDialog.getSaveFileName(None, "Save a file FCMacro", path, "FCMacro (*.FCMacro);;Python (*.py)")                   # PySide2
                nomMacro = FreeCAD.ActiveDocument.Name
                SaveName, Filter = PySide2.QtWidgets.QFileDialog.getSaveFileName(None, "Save a file FCMacro", path + nomMacro, "(*.FCMacro);;Python (*.py)") # PySide2
            else   *
                SaveName, Filter = PySide2.QtWidgets.QFileDialog.getSaveFileName(None, "Save a file CoorInfo", pathFile, "CoorInfo (*.CoorInfo);;Ascii (*.asc);;TXT (*.txt)")   # PySide2

            if SaveName == ""   *                                                            # if the name file are not selected then Abord process
                App.Console.PrintMessage("Process aborted"+"\n")
            else   *                                                                         # if the name file are selected or created then 
                ####new2
                pathFile      = os.path.dirname(SaveName) + "/"  #= C   */Provisoire400/
                formatFichier = os.path.splitext(SaveName)[1]    #= .png
                SaveName      = os.path.splitext(SaveName)[0]    #= /home/kubuntu/.FreeCAD/Macro/Texture_007_H #= C   */Provisoire400/image3D
                SaveNameformatFichier = SaveName + formatFichier #= C   */Provisoire400/image3D.png
                ####new2
                
                ######## sauve le dernier chemin utilise si n'est pas une macro########
                if self.CB_DataInMacro.isChecked()   *
                    None
                else   *
                    FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetString("setLastPath",pathFile)
                ######## sauve le dernier chemin utilise si n'est pas une macro########

                App.Console.PrintMessage("Registration of "+SaveNameformatFichier+"\n")
                try   *
                    if self.CB_DataInMacro.isChecked()   *
                        file = open(SaveNameformatFichier, 'w') #'w'write
                    else   *
                        file = open(SaveNameformatFichier, 'a') #'a'append
                    try   *
                        #### macro first section begin
                        if self.CB_DataInMacro.isChecked()   *
                            file.write("# -*- coding   * utf-8 -*-" + "\n")
                            file.write("##" + "\n")
                            try   *
                                nameAuthor = str(unicodedata.normalize('NFD', __author__).encode('ascii','ignore'))
                            except Exception   * nameAuthor = "Sir X"
                            try   *
                                file.write("##Created by      * " + __title__ + "    * " + __version__ + "   *" + __date__ + "     * " + nameAuthor + "\n")
                                file.write("##Document        * " + FreeCAD.ActiveDocument.Name + "\n")
                                #file.write("##Date            * " + str(QDate.currentDate().toString()) + "\n")           # mer. mars 3 2021
                                file.write("##Date            * " + str(QDate.currentDate().toString("yyyy/MM/dd")) + "    # yyyy/MM/dd" + "\n")
                                file.write("##Object(First)   * " + str(FreeCADGui.Selection.getSelection()[0].Name) + "\n")
                                file.write("##Coordinates     * " + str(countMemory) + "\n")
                                file.write("##" + "\n")
                            except Exception   * None
                            file.write("import Draft, Part" + "\n")
                            file.write("import PySide2" + "\n")
                            file.write("from pivy import coin" + "\n")
                            file.write("import time, os" + "\n")
                            file.write("" + "\n")
                            file.write("import FreeCAD, FreeCADGui" + "\n")
                            file.write("App = FreeCAD" + "\n")
                            file.write("Gui = FreeCADGui" + "\n")
                            file.write("" + "\n")
                            file.write("global Document; Document = " + chr(34) + FreeCAD.ActiveDocument.Name + chr(34) + "\n")
                            file.write("global xxData  ; xxData   = [] " + "\n")
                            file.write("global xxKey   ; xxKey    = " + chr(34) + chr(34) + "\n")
                            file.write("global v, o, c" + "\n")
                            file.write("global vitesse ; vitesse  = 0.02" + "\n")
                            file.write("" + "\n")
                            file.write("def help()   *" + "\n")
                            file.write("    global xxData" + "\n")
                            file.write("    global Document" + "\n")
                            file.write('    App.Console.PrintMessage("__' + FreeCAD.ActiveDocument.Name + '__"+"' + chr(92) + 'n")' + "\n")
                            file.write('    App.Console.PrintMessage("__" + str(len(xxData)) + " Coordinates__"+"' + chr(92) + 'n")' + "\n")
                            file.write('    App.Console.PrintMessage("Type Key Q to Quit"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("Type Key D to Decrease speed"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("Type Key I to Increase speed"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("Type Key P to Pause/Continue or key RETURN or ESCAPE"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("Type Key S to Step by Step (key RETURN or ESCAPE to continue)"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("Type Key R to Reverse"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("Type Key M for this message"+"' + chr(92) + 'n")' +  "\n")
                            file.write('    App.Console.PrintMessage("____________________________"+"' + chr(92) + 'n")' +  "\n")
                            file.write('\n')
                            file.write('class ViewObserver   *' +  "\n")
                            file.write('    def logPosition(self, info)   *' +  "\n")
                            file.write('        global xxKey' +  "\n")
                            file.write('        global v, o, c' +  "\n")
                            file.write('        global vitesse' +  "\n")
                            file.write('' +  "\n")
                            file.write('        xxKey = info["Key"].upper()' +  "\n")
                            file.write('        if xxKey in "QIDPSRM" or xxKey == "RETURN" or xxKey == "PAD_ENTER" or xxKey == "ESCAPE"   *' +  "\n")
                            file.write('            if (xxKey == "Q")   *                        # Quit' +  "\n")
                            file.write('                v.removeEventCallback("SoKeyboardEvent",c)' +  "\n")
                            file.write('                FreeCAD.Console.PrintMessage("End " + Document + "' + chr(92) + 'n")' +  "\n")
                            file.write('' +  "\n")
                            file.write('            if (xxKey == "I")   *                        # Increase' +  "\n")
                            file.write('                vitesse -= 0.01' +  "\n")
                            file.write('                if vitesse <= 0   *' +  "\n")
                            file.write('                    vitesse = 0' +  "\n")
                            file.write('                    App.Console.PrintMessage("Speed maximum"+"' + chr(92) + 'n")' +  "\n")
                            file.write('                else   *' +  "\n")
                            file.write('                    App.Console.PrintMessage(str(vitesse)+"' + chr(92) + 'n")' +  "\n")
                            file.write('' +  "\n")
                            file.write('            if (xxKey == "D")   *                        # Decrease' +  "\n")
                            file.write('                vitesse += 0.01' +  "\n")
                            file.write('                App.Console.PrintMessage(str(vitesse)+"' + chr(92) + 'n")' +  "\n")
                            file.write('' +  "\n")
                            file.write('            if (xxKey == "R")   *                        # Reverse' +  "\n")
                            file.write('                xxData.reverse()' +  "\n")
                            file.write('' +  "\n")
                            file.write('            if (xxKey == "M")   *                        # Help memo' +  "\n")
                            file.write('                help()' +  "\n")
                            file.write('##Begin of file' + "\n")
                            file.write('xxData = [' + "\n")
                        #### macro first section end
                        #### save data
                        for i in saveOnDisk   *
                            file.write(i + "\n")
                        #### save data
                        #### macro second section begin
                        if self.CB_DataInMacro.isChecked()   *
                            file.write(']' + "\n")
                            file.write('##End of file' + "\n")
                            file.write('' + "\n")
                            file.write('createPoint = 0    # 0=not point 1=create point #used by "S"    *Step to Step' + "\n")
                            file.write('try   *' + "\n")
                            file.write('    v = Gui.activeDocument().activeView()' + "\n")
                            file.write('    o = ViewObserver()' + "\n")
                            file.write('    c = v.addEventCallback("SoKeyboardEvent",o.logPosition)' + "\n")
                            file.write('' + "\n")
                            file.write('    ##Select the object' + "\n")
                            file.write('    ##myObject = FreeCADGui.Selection.getSelection()[0]    #select the object' + "\n")
                            file.write('    help()    #help message' + "\n")
                            file.write('' + "\n")
                            file.write('    ##Loop' + "\n")
                            file.write('    while xxKey != "Q"   *' + "\n")
                            file.write('            comptCoordinate = -1          # coordinte 0 to ...x' + "\n")
                            file.write('            for p in xxData   *' + "\n")
                            file.write('                #if (xxKey == "Q")   * break # Quit the loop after finish the complete loop (commented by default   * if used quit the loop as is)' + "\n")
                            file.write('                comptCoordinate += 1' + "\n")
                            file.write('                ##         p[1]=Coordinate x,y,z;  p[2]=Rotation angle x (Roll), y (Pitch), z (Yaw)' + "\n")
                            file.write('                px = float(p[1][0]);    rx = float(p[2][0])' + "\n")
                            file.write('                py = float(p[1][1]);    ry = float(p[2][1])' + "\n")
                            file.write('                pz = float(p[1][2]);    rz = float(p[2][2])' + "\n")
                            file.write('                App.ActiveDocument.getObject(p[0]).Placement=App.Placement(App.Vector(px,py,pz), App.Rotation(rx,ry,rz), App.Vector(0,0,0))' + "\n")
                            file.write('                Gui.updateGui()                                            # rafraichi l''ecran' + "\n")
                            file.write('                time.sleep(vitesse)' + "\n")
                            file.write('' + "\n")
                            file.write('                if xxKey == "P"   *                                           # Pause' + "\n")
                            file.write('                    xxKey = ""' + "\n")
                            file.write('                    comptLoop = 0' + "\n")
                            file.write('                    while xxKey != "P"   *' + "\n")
                            file.write('                        if xxKey == "RETURN" or xxKey == "PAD_ENTER" or xxKey == "ESCAPE"   * break' + "\n")
                            file.write('                        comptLoop += 1' + "\n")
                            file.write('                        if comptLoop > 50000   *' + "\n")
                            file.write('                            comptLoop = 0' + "\n")
                            file.write('                            App.Console.PrintError("You is in mode Pause    * Type P or RETURN or ESCAPE to continue" + "' + chr(92) + 'n")' + "\n")
                            file.write('                        Gui.updateGui()                                    # rafraichi l''ecran' + "\n")
                            file.write('                    xxKey = ""' + "\n")
                            file.write('' + "\n")
                            file.write('                if xxKey == "S"   *                                           # Step by Step' + "\n")
                            file.write('                    App.Console.PrintMessage(str(App.ActiveDocument.getObject(p[0]).Placement) + " #(" + str(comptCoordinate) + ")" + "' + chr(92) + 'n")' + "\n")
                            file.write('                    ####' + "\n")
                            file.write('                    if createPoint == 1   *' + "\n")
                            file.write('                        point = Draft.makePoint(App.ActiveDocument.getObject(p[0]).Placement.Base)   # create point to Placement.Base' + "\n")
                            file.write('                        Draft.autogroup(point)                             #' + "\n")
                            file.write('                        FreeCAD.ActiveDocument.recompute()                 #' + "\n")
                            file.write('                    ####' + "\n")
                            file.write('                    xxKey = ""' + "\n")
                            file.write('                    while xxKey != "S"   *' + "\n")
                            file.write('                        if xxKey == "RETURN" or xxKey == "PAD_ENTER" or xxKey == "ESCAPE"   * break' + "\n")
                            file.write('                        xxKey = ""' + "\n")
                            file.write('                        Gui.updateGui()                                    # rafraichi l''ecran' + "\n")
                            file.write('' + "\n")
                            file.write('except Exception   *' + "\n")
                            file.write('    FreeCAD.Console.PrintError("' + chr(92) + 'n"+"Not document open, or not object selected" + "' + chr(92) + 'n")' + "\n")
                            file.write('    try   *' + "\n")
                            file.write('         v.removeEventCallback("SoKeyboardEvent",c)' + "\n")
                            file.write('    except Exception   *' + "\n")
                            file.write('        None' + "\n")
                            file.write('' + "\n")
                        #### macro second section end

                    except Exception   *
                        self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
                        self.label_00.setText(" Error write file")
#                        App.Console.PrintError("Error write file "+"\n")
                    finally   *
                        file.close()
                except Exception   *
                    self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
                    self.label_00.setText(" Error Write file " + SaveName)
#                    App.Console.PrintError("Error Write file " + SaveName+"\n")
#        print("on_PB_Save_Memorize")

    def on_PB_ClearMemo(self)   *
        global saveOnDisk
        global saveListView
        global countMemory
        global memorySelected

        try   *
            model = saveListView = QtGui.QStandardItemModel()
            self.TE_Memorize.model().removeRows(0, countMemory)# model.rowCount()
            saveOnDisk     = []
            self.TE_Memorize.setModel(saveListView)
            countMemory    = 0
            memorySelected = []
            self.PB_Memorize.setText("Memo")
            self.PB_Memorize.setStyleSheet("Base")
            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Eteint_Icon))) # icone dans une variable 
        except Exception   *
            None
#        print("on_PB_ClearMemo")

    def on_CB_On_Click_Apply(self)   *

        if self.CB_On_Click_Apply.isChecked()   *
            self.CB_On_Click_Apply.setIcon(QtGui.QIcon(QtGui.QPixmap(normalWork_Icon))) # icone dans une variable 
            self.CB_On_Click_Apply.setText(u"Memo on demand")
            self.CB_On_Click_Apply.setToolTip(u"Memorize the coordinates on demand")
            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Allume_Icon))) # icone dans une variable 
            self.groupBox_Data.setEnabled(True)
        else   *
            self.CB_On_Click_Apply.setIcon(QtGui.QIcon(QtGui.QPixmap(OnClickApply_Icon))) # icone dans une variable 
            self.CB_On_Click_Apply.setText(u"Memo on click")
            self.CB_On_Click_Apply.setToolTip(u"Memorize the coordinates on all Click Apply button")
#        print("on_CB_On_Click_Apply")

    def On_CB_DataInMacro(self)   *

        if self.CB_DataInMacro.isChecked()   *
            self.CB_DataInMacro.setIcon(QtGui.QIcon(QtGui.QPixmap(code_FC_Icon))) # icone dans une variable 
            self.CB_DataInMacro.setText(u"Coordinate")
            self.PB_Save_Memorize.setText("Save (wr)")
            self.PB_Save_Memorize.setToolTip("The file is open in mode Write" + "\n"
                                             "If the file exist, the file is crushed" + "\n"
                                             "")
        else   *
            self.CB_DataInMacro.setIcon(QtGui.QIcon(QtGui.QPixmap(code_Python_Icon))) # icone dans une variable 
            self.CB_DataInMacro.setText(u"Macro")
            self.PB_Save_Memorize.setText("Save (ap)")
            self.PB_Save_Memorize.setToolTip("The file is open in mode Append" + "\n"
                                             "If the file exist, the the data hare adding in the file" + "\n"
                                             "")
#        print("On_CB_DataInMacro")

    def on_DS_Value_Angle_Dimension(self,val)   *
        global valeur
        global myObject
        global axisX, axisY, axisZ
        global posX, posY, posZ
        global rotAngleX, rotAngleY, rotAngleZ

        valeur = val
        if (myObject == "") or (valeur == 0)   *
            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Eteint_Icon))) # icone dans une variable 
            self.DS_Value_Angle_Dimension.setValue(0.0)
            self.DS_Value_Angle_Dimension.setStyleSheet("background-color   * rgb(250, 88, 88)")
#            self.SC_Slider_Bar.setValue(0.0)
            None
        else   *
            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Allume_Icon))) # icone dans une variable 
            self.DS_Value_Angle_Dimension.setStyleSheet("Base")
            self.PB_Memorize.setStyleSheet("Base")
#            self.SC_Slider_Bar.setValue(valeur)
            if self.CB_Position.isChecked()   *                 # translate

                if self.RB_Rotation_X.isChecked()   *
                    posX = valeur
                    posY = posZ = 0.0
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[0],4) + valeur))
                elif self.RB_Rotation_Y.isChecked()   *
                    posY = valeur
                    posX = posZ = 0.0
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[1],4) + valeur))
                elif self.RB_Rotation_Z.isChecked()   *
                    posZ = valeur
                    posX = posY = 0.0
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[2],4) + valeur))
                elif self.RB_Direction_D.isChecked()   *
                    posZ = valeur
                    posX = posY = 0.0
                    xD = str(round(myObject.Placement.Base[0],4))
                    yD = str(round(myObject.Placement.Base[1],4))
                    zD = str(round(myObject.Placement.Base[2],4))
                    self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")

                self.label_00.setText("[Pos=(" + str(round(myObject.Placement.Base[0],2))+" , " + 
                                                 str(round(myObject.Placement.Base[1],2))+" , " + 
                                                 str(round(myObject.Placement.Base[2],2))+")] " +
                                      "[Axis=("+ str(round(axisX,2)) + " , " + str(round(axisY,2)) + " , " + str(round(axisZ,2)) + ")]")

            else   *                                            # rotation

                if self.RB_Rotation_X.isChecked()   *
                    rotAngleX = valeur
                    rotAngleY = rotAngleZ = 0.0
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[0],4) + valeur))
                elif self.RB_Rotation_Y.isChecked()   *
                    rotAngleY = valeur
                    rotAngleZ = rotAngleX = 0.0
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[1],4) + valeur))
                elif self.RB_Rotation_Z.isChecked()   *
                    rotAngleZ = valeur
                    rotAngleX = rotAngleY = 0.0
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[2],4) + valeur))
                elif self.RB_Direction_D.isChecked()   *
                    rotAngleZ = valeur
                    rotAngleX = rotAngleY = 0.0
                    xD = str(round(myObject.Placement.Rotation.toEuler()[0],4))
                    yD = str(round(myObject.Placement.Rotation.toEuler()[1],4))
                    zD = str(round(myObject.Placement.Rotation.toEuler()[2],4))
                    self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")

                self.label_00.setText("[Rot=(" + str(round(rotAngleX,2)) + " , " + str(round(rotAngleY,2)) + " , " + str(round(rotAngleZ,2)) + ")] " +
                                      "[Axis=("+ str(round(axisX,2)) + " , " + str(round(axisY,2)) + " , " + str(round(axisZ,2)) + ")]")
#        print("on_DS_Value_Angle_Dimension ", valeur)

    def on_PB_Negatif_clicked(self)   *

        if valeur < 0   *
            self.PB_Negatif.setIcon(QtGui.QIcon(QtGui.QPixmap(negatif_Icon))) # icone dans une variable 
        else   *
            self.PB_Negatif.setIcon(QtGui.QIcon(QtGui.QPixmap(positif_Icon))) # icone dans une variable 

        self.DS_Value_Angle_Dimension.setValue(-valeur)    # !?
#        print("on_PB_Negatif_clicked")

    def on_CBox_View(self,text)   *  # memory view on object worked
        global duplicate_View
        global myObjectName
        global switchZoomOnCilck

        if text == "Empty"   *
            #duplicate_View = sorted(list(set(duplicate_View))) # trie et tire les doublons
            duplicate_View = sorted(duplicate_View, key=itemgetter(0)) # sort
            try   *          # supprime les doublons apres avoir ete trie (sorted)
                doublon = 1
                while doublon < len(duplicate_View)   *
                    if (duplicate_View[doublon][0] == duplicate_View[doublon-1][0])   *
                        del duplicate_View[doublon-1]
                        doublon -= 1
                    doublon += 1
            except Exception   *
                None
            self.CBox_View.blockSignals(True)
            self.CBox_View.clear()
            for i in range(len(duplicate_View))   *    # copie les noms tries dans ComboBox_View
                self.CBox_View.addItem(duplicate_View[i][0])
                self.CBox_View.blockSignals(False)
            #self.CBox_View.setItemText(0,_translate("MainWindow",  "0"))
        else   *
            for i in range(len(duplicate_View))   *
                if text == duplicate_View[i][0]   *
                    Gui.ActiveDocument.ActiveView.setCamera(duplicate_View[i][1])    #restore previously stored camera settings
                    ##camera = Gui.ActiveDocument.ActiveView.getCamera()              #store camera settings to 'cam'
#        print("on_CBox_View ",text)

    def on_CBox_Impost(self,text)   *  # value length and degrees

        if self.CB_Position.isChecked()   *
            self.CBox_Impost.setCurrentIndex(4)
            self.CBox_Impost.setItemText(0, "0.0001")
            self.CBox_Impost.setItemText(1, "0.001")
            self.CBox_Impost.setItemText(2, "0.01")
            self.CBox_Impost.setItemText(3, "0.1")
            self.CBox_Impost.setItemText(4, "0")
            self.CBox_Impost.setItemText(5, "1")
            self.CBox_Impost.setItemText(6, "5")
            self.CBox_Impost.setItemText(7, "10")
            self.CBox_Impost.setItemText(8, "25")
            self.CBox_Impost.setItemText(9, "50")
            self.CBox_Impost.setItemText(10, "100")
            self.CBox_Impost.setItemText(11, "250")
            self.CBox_Impost.setItemText(12, "500")
            self.CBox_Impost.setItemText(13, "1000")
            self.CBox_Impost.setItemText(14, "5000")
            self.CBox_Impost.setItemText(15, "10000")
        else   *
            self.CBox_Impost.setCurrentIndex(4)
            self.CBox_Impost.setItemText(0, "0.0001")
            self.CBox_Impost.setItemText(1, "0.001")
            self.CBox_Impost.setItemText(2, "0.01")
            self.CBox_Impost.setItemText(3, "0.1")
            self.CBox_Impost.setItemText(4, "0")
            self.CBox_Impost.setItemText(5, "1")
            self.CBox_Impost.setItemText(6, "5")
            self.CBox_Impost.setItemText(7, "10")
            self.CBox_Impost.setItemText(8, "20")
            self.CBox_Impost.setItemText(9, "30")
            self.CBox_Impost.setItemText(10, "40")
            self.CBox_Impost.setItemText(11, "45")
            self.CBox_Impost.setItemText(12, "60")
            self.CBox_Impost.setItemText(13, "90")
            self.CBox_Impost.setItemText(14, "120")
            self.CBox_Impost.setItemText(15, "180")
        self.DS_Value_Angle_Dimension.setProperty("value", text)
#        print("on_CBox_Impost ",text)

    def on_CBox_Memory(self,text)   *  # memory the value sort and delete duplicate
        global duplicate_Memory

        self.DS_Value_Angle_Dimension.setValue(float(text))
        duplicate_Memory.append(float(text))
        duplicate_Memory = sorted(list(set(duplicate_Memory))) # sort
        self.CBox_Memory.blockSignals(True)
        self.CBox_Memory.clear()
        for i in range(len(duplicate_Memory))   *
            self.CBox_Memory.addItem(str(duplicate_Memory[i]))
            self.CBox_Memory.blockSignals(False)
#        print("on_CBox_Memory ",text)

    def on_LE_Increment_Pressed(self,text)   *
        None
#        print("on_LE_Increment_Pressed")

    def on_PB_Apply_clicked(self)   *
        global valeur
        global selM
        global myObject
        global myObjectName
        global duplicate_View

        global axisX, axisY, axisZ
        global posX, posY, posZ
        global rotAngleX, rotAngleY, rotAngleZ

        if (myObject == "") or (valeur == 0)   *
            self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
            self.label_00.setText(" Select one Object or give one value Angle/Dimension")
#            FreeCAD.Console.PrintError("Select one Object or give one value Angle/Dimension" + "\n")
            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Eteint_Icon))) # icone dans une variable 
            if valeur == 0   *
                self.DS_Value_Angle_Dimension.setStyleSheet("background-color   * rgb(250, 88, 88)")
        else   *
            self.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Allume_Icon))) # icone dans une variable 

            #Gui.ActiveDocument.ActiveView.setCamera(camera)    #restore previously stored camera settings
            camera = Gui.ActiveDocument.ActiveView.getCamera() #store camera settings to 'cam'
            duplicate_View.append([myObjectName, camera])

            self.on_CBox_View("Empty")
            self.on_CBox_Memory(self.DS_Value_Angle_Dimension.value())

            if self.CB_Position.isChecked()   *                 # translate

                if self.RB_Direction_D.isChecked()   *          # direction
                    try   *
                        selectedEdge = FreeCADGui.Selection.getSelectionEx()[1].SubObjects[0]         # select one element and axis second object (2 selections)
                    except Exception   *
                        try   *
                            selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[1]     # select one element and axis same object   (2 selections)
                        except Exception   *
                            try   *
                                selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0] # select one element and axis same object   (1 selection)
                            except Exception   *
                                None
                    pointsTrajet = []
                    try   *
                        pointsTrajet  = selectedEdge.discretize(Distance = 1.0)                       # discretize the element
                    except Exception   *
                        direction = myObject.Vertexes[0].Point
                        pointsTrajet = direction
                        None
                    
                    try   *
                        direction = pointsTrajet[1].sub(pointsTrajet[0])                              # search the direction line or sub
                    except Exception   *
                        try   *
                            direction = myObject.Vertexes[0].Point                                    # direction point
                        except Exception   *
                            direction = App.Vector(0.0,0.0,0.0)
                    
                    selM.Placement.Base = myObject.Placement.Base + App.Vector(direction).scale(valeur, valeur, valeur)
                else   *
                    selM.Placement = App.Placement(App.Vector(posX, posY, posZ), App.Rotation(0.0,0.0,0.0), App.Vector(0.0,0.0,0.0)).multiply(App.ActiveDocument.getObject(myObjectName).Placement)
                myObject = selM

                if self.RB_Rotation_X.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[0],4)))
                elif self.RB_Rotation_Y.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[1],4)))
                elif self.RB_Rotation_Z.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[2],4)))
                elif self.RB_Direction_D.isChecked()   *
                    xD = str(round(myObject.Placement.Base[0],4))
                    yD = str(round(myObject.Placement.Base[1],4))
                    zD = str(round(myObject.Placement.Base[2],4))
                    self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")

                self.label_00.setText("[Pos=(" + str(round(myObject.Placement.Base[0],2))+" , " + 
                                                 str(round(myObject.Placement.Base[1],2))+" , " + 
                                                 str(round(myObject.Placement.Base[2],2))+")] " +
                                      "[Axis=("+ str(round(axisX,2)) + " , " + str(round(axisY,2)) + " , " + str(round(axisZ,2)) + ")]")

            else   *                                            # rotation
                if self.RB_Direction_D.isChecked()   *          # direction
                    try   *
                        selectedEdge = FreeCADGui.Selection.getSelectionEx()[1].SubObjects[0]         # select one element and axis second object (2 selections)
                    except Exception   *
                        try   *
                            selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[1]     # select one element and axis same object   (2 selections)
                        except Exception   *
                            try   *
                                selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0] # select one element and axis same object   (1 selection)
                            except Exception   *
                                None
                    try   *
                        direction = selectedEdge.Vertexes[1].Point.sub(selectedEdge.Vertexes[0].Point)# search the direction line or sub
                    except Exception   *
                        try   *
                            direction = objectRotation.Vertexes[0].Point
                        except Exception   *
                            direction = App.Vector(0.0,0.0,0.0)
                    selM.Placement = App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(direction), valeur), App.Vector(axisX, axisY, axisZ)).multiply(App.ActiveDocument.getObject(myObjectName).Placement)
                else   *
                    selM.Placement = App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(rotAngleX, rotAngleY, rotAngleZ), App.Vector(axisX, axisY, axisZ)).multiply(App.ActiveDocument.getObject(myObjectName).Placement) # other method
                myObject = selM

                if self.RB_Rotation_X.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[0],4)))
                elif self.RB_Rotation_Y.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[1],4)))
                elif self.RB_Rotation_Z.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[2],4)))
                elif self.RB_Direction_D.isChecked()   *
                    xD = str(round(myObject.Placement.Rotation.toEuler()[0],4))
                    yD = str(round(myObject.Placement.Rotation.toEuler()[1],4))
                    zD = str(round(myObject.Placement.Rotation.toEuler()[2],4))
                    self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")

                self.label_00.setText("[Rot=(" + str(round(myObject.Placement.Rotation.toEuler()[0],2)) + " , " +
                                                 str(round(myObject.Placement.Rotation.toEuler()[1],2)) + " , " + 
                                                 str(round(myObject.Placement.Rotation.toEuler()[2],2)) + ")] " +
                                      "[Axis=("+ str(round(axisX,2))+" , "+ str(round(axisY,2))+" , "+ str(round(axisZ,2))+")]")
            if self.CB_On_Click_Apply.isChecked()   *
                self.on_PB_Memorize()
#            FreeCAD.ActiveDocument.recompute()
#        print("on_PB_Apply_clicked")

    def on_RB_Rotation_0(self)   *
        None
#        print("on_RB_Rotation_0")

    def on_RB_Rotation_X(self)   *
        global myObject

        if self.CB_Position.isChecked()   *              
            self.LE_Increment.setText(str(round(myObject.Placement.Base[0],4)))                  # pos X
        else   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[0],4)))    # yaw = Z
        self.DS_Value_Angle_Dimension.setValue(0.0)
#        print("on_RB_Rotation_X")

    def on_RB_Rotation_Y(self)   *
        global myObject

        if self.CB_Position.isChecked()   *              
            self.LE_Increment.setText(str(round(myObject.Placement.Base[1],4)))                  # pos Y
        else   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[1],4)))    # pitch= Y
        self.DS_Value_Angle_Dimension.setValue(0.0)
#        print("on_RB_Rotation_Y")

    def on_RB_Rotation_Z(self)   *
        global myObject

        if self.CB_Position.isChecked()   *              
            self.LE_Increment.setText(str(round(myObject.Placement.Base[2],4)))                  #  pos Z
        else   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[2],4)))    # roll = X
        self.DS_Value_Angle_Dimension.setValue(0.0)
#        print("on_RB_Rotation_Z")

    def on_RB_Direction_D(self)   *
        global myObject

        if self.CB_Position.isChecked()   *              
            xD = str(round(myObject.Placement.Base[0],4))
            yD = str(round(myObject.Placement.Base[1],4))
            zD = str(round(myObject.Placement.Base[2],4))
        else   *
            xD = str(round(myObject.Placement.Rotation.toEuler()[0],4))
            yD = str(round(myObject.Placement.Rotation.toEuler()[1],4))
            zD = str(round(myObject.Placement.Rotation.toEuler()[2],4))
        self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")
        self.DS_Value_Angle_Dimension.setValue(0.0)
#        print("on_RB_Direction_D")

    def on_RB_CenterRot(self)   *                                # zero
        global myObject
        global selM
        global positionMouse
        global axisX, axisY, axisZ
        
        try   *
            if hasattr(selM, "Shape")   *
                sel = selM.Shape
            elif hasattr(selM, "Mesh")   *         # upgrade with wmayer thanks #http   *//forum.freecadweb.org/viewtopic.php?f=13&t=22331
                sel = selM.Mesh
            elif hasattr(selM, "Points")   *
                sel = selM.Points
            myObject = sel

            self.groupBox_Pos_Mouse.setEnabled(False)
            if self.RB_Bond_Box_Center.isChecked()   *           # axis
                axisX = myObject.BoundBox.Center.x
                axisY = myObject.BoundBox.Center.y
                axisZ = myObject.BoundBox.Center.z
                self.label_00.setToolTip("Axis BoundBox.Center")
                self.RB_Center_Mass.setStyleSheet("Base")
            elif self.RB_Center_Mass.isChecked()   *
                try   *
                    axisX = myObject.CenterOfMass.x
                    axisY = myObject.CenterOfMass.y
                    axisZ = myObject.CenterOfMass.z
                    self.label_00.setToolTip("Axis Center Of Mass")
                except Exception   *   # case Mesh.MeshObject
                    self.RB_Bond_Box_Center.setChecked(True)
                    self.RB_Center_Mass.setStyleSheet("background-color   * rgb(250, 88, 88)")
            elif self.RB_Point_Clicked.isChecked()   *
                axisX = positionMouse[0]
                axisY = positionMouse[1]
                axisZ = positionMouse[2]
                self.groupBox_Pos_Mouse.setEnabled(True)
                self.label_00.setToolTip("Point Mouse")
           
        except Exception   *
            self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
            self.label_00.setText("Error CenterRot_0")
##            FreeCAD.Console.PrintError("Error CenterRot_0" + "\n" + "or Bad selection" + "\n")
##        print("on_RB_CenterRot")

    def on_CB_Position(self)   *
        global myObject
        global posX, posY, posZ
        global axisX, axisY, axisZ
        global ui

        self.on_CBox_Impost("")
        if self.CB_Position.isChecked()   *              
            self.DS_Value_Angle_Dimension.setMinimum(-999999999.999999999)
            self.DS_Value_Angle_Dimension.setMaximum(999999999.999999999)
            self.DS_Value_Angle_Dimension.setSuffix(" mm")
            self.RB_Rotation_Z.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_Z_Icon))) # icone dans une variable 
            self.RB_Rotation_X.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_X_Icon))) # icone dans une variable 
            self.CB_Position.setIcon(QtGui.QIcon(QtGui.QPixmap(rotate_Icon))) #icone dans une variable 
            self.CB_Position.setToolTip(u"UnCheck for rotate the object in axis selected")
            self.CB_Position.setText(u"Rotation")
            self.CB_Position.setToolTip(u"Rotate the object to axis choice X, Y, Z or D")
            self.groupBox_Rotation.setEnabled(False)
            self.RB_Bond_Box_Center.setChecked(True)
            
#            self.SC_Slider_Bar.setMinimum(-1000)
#            self.SC_Slider_Bar.setMaximum(1000)
#            self.DS_Value_Angle_Dimension.setMinimum(-1000)
#            self.DS_Value_Angle_Dimension.setMaximum(1000)

            self.groupBox_Axis.setTitle("Axis Translation")
            self.RB_Rotation_Z.setText("Translation Z ")          # translate
            self.RB_Rotation_Y.setText("Translation Y ")
            self.RB_Rotation_X.setText("Translation X ")
            self.RB_Direction_D.setText("Translation D ")

            try   *
                self.label_00.setText("[Pl.Base=(" + str(round(myObject.Placement.Base[0],2)) + " , " + 
                                                 str(round(myObject.Placement.Base[1],2)) + " , " + 
                                                 str(round(myObject.Placement.Base[2],2)) + ")] " +
                                      "[Axis=("+ str(round(axisX,2)) + " , " + str(round(axisY,2)) + " , " + str(round(axisZ,2)) + ")]")
                if self.RB_Rotation_X.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[0],4)))
                elif self.RB_Rotation_Y.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[1],4)))
                elif self.RB_Rotation_Z.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Base[2],4)))
                elif self.RB_Direction_D.isChecked()   *
                    xD = str(round(myObject.Placement.Base[0],4))
                    yD = str(round(myObject.Placement.Base[1],4))
                    zD = str(round(myObject.Placement.Base[2],4))
                    self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")
            except Exception   *
                self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
                self.label_00.setText("Error Position_0 or Bad selection")
##                FreeCAD.Console.PrintError("Error Position_0" + "\n" + "or Bad selection" + "\n")
        else   *
            self.DS_Value_Angle_Dimension.setMinimum(-360.0)
            self.DS_Value_Angle_Dimension.setMaximum(360.0)
            self.DS_Value_Angle_Dimension.setSuffix(" Degrees")
            self.RB_Rotation_Z.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_X_Icon))) # icone dans une variable 
            self.RB_Rotation_X.setIcon(QtGui.QIcon(QtGui.QPixmap(axis_Z_Icon))) # icone dans une variable 
            self.CB_Position.setIcon(QtGui.QIcon(QtGui.QPixmap(translate_Icon))) #icone dans une variable 
            self.CB_Position.setText(u"Translation")
            self.CB_Position.setToolTip(u"Check for move the object to axis choice X, Y, Z or D")
            self.groupBox_Rotation.setEnabled(True)
#            self.SC_Slider_Bar.setMinimum(0.0)
#            self.SC_Slider_Bar.setMaximum(359.0)
#            self.DS_Value_Angle_Dimension.setMinimum(0.0)
#            self.DS_Value_Angle_Dimension.setMaximum(359.0)

            self.groupBox_Axis.setTitle("Axis Rotation")
            self.RB_Rotation_Z.setText("Rotation(X) Roll")      # rotation
            self.RB_Rotation_Y.setText("Rotation(Y) Pitch")
            self.RB_Rotation_X.setText("Rotation(Z) Yaw")
            self.RB_Direction_D.setText("Rotation(D)")

            try   *
                self.label_00.setText("[Rot=(" + str(round(myObject.Placement.Rotation.toEuler()[0],2)) + " , " +
                                                 str(round(myObject.Placement.Rotation.toEuler()[1],2)) + " , " + 
                                                 str(round(myObject.Placement.Rotation.toEuler()[2],2)) + ")] " +
                                      "[Axis=("+str(round(axisX,2))+" , "+ str(round(axisY,2))+" , "+ str(round(axisZ,2))+")]")
                if self.RB_Rotation_X.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[0],4)))
                elif self.RB_Rotation_Y.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[1],4)))
                elif self.RB_Rotation_Z.isChecked()   *
                    self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[2],4)))
                elif self.RB_Direction_D.isChecked()   *
                    xD = str(round(myObject.Placement.Rotation.toEuler()[0],4))
                    yD = str(round(myObject.Placement.Rotation.toEuler()[1],4))
                    zD = str(round(myObject.Placement.Rotation.toEuler()[2],4))
                    self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")
            except Exception   *
                self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
                self.label_00.setText("Error Position_1 or Bad selection")
#                FreeCAD.Console.PrintError("Error Position_0" + "\n" + "or Bad selection" + "\n")

        self.DS_Value_Angle_Dimension.setValue(0.0)
#        print("on_CB_Position")

    def on_CB_Point(self)   *
        global ui
        global myObject
        global selM
        global myObjectName
        global positionMouse
        
        if hasattr(selM, "Shape")   *
            sel = selM.Shape
        elif hasattr(selM, "Mesh")   *         # upgrade with wmayer thanks #http   *//forum.freecadweb.org/viewtopic.php?f=13&t=22331
            sel = selM.Mesh
        elif hasattr(selM, "Points")   *
            sel = selM.Points
        myObject = sel

        if self.RB_Bond_Box_Center.isChecked()   *           # axis
            point = Draft.makePoint(myObject.BoundBox.Center.x, myObject.BoundBox.Center.y, myObject.BoundBox.Center.z)
            point.ViewObject.PointColor = (1.0,0.0,0.0)
            point.Label = "Point_BoundBox_Center"
            self.RB_Center_Mass.setStyleSheet("Base")
        elif self.RB_Center_Mass.isChecked()   *
            try   *
                point = Draft.makePoint(myObject.CenterOfMass.x, myObject.CenterOfMass.y, myObject.CenterOfMass.z)
                point.ViewObject.PointColor = (0.0,1.0,0.0)
                point.Label = "Point_CenterOfMass"
            except Exception   *   # case Mesh.MeshObject
                self.RB_Bond_Box_Center.setChecked(True)
                self.RB_Center_Mass.setStyleSheet("background-color   * rgb(250, 88, 88)")
        elif self.RB_Point_Clicked.isChecked()   *
            point = Draft.makePoint(positionMouse[0], positionMouse[1], positionMouse[2])
            point.ViewObject.PointColor = (0.0,0.0,1.0)
            point.Label = "Point_positionMouse"
        Gui.Selection.addSelection(App.ActiveDocument.getObject(myObjectName))
        FreeCAD.ActiveDocument.recompute()
#        ui.on_RB_CenterRot()
#        print("on_CB_Point")

    def on_PB_Zero_clicked(self)   *
        global myObject
        global selM

#        if (myObject != "")   *
#            try   *
        myObject = selM
        pl = App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(0.0, 0.0, 0.0), App.Vector(0.0, 0.0, 0.0))
        myObject.Placement = pl    if self.RB_Rotation_X.isChecked()   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[0],4)))
        elif self.RB_Rotation_Y.isChecked()   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[1],4)))
        elif self.RB_Rotation_Z.isChecked()   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[2],4)))
        elif self.RB_Direction_D.isChecked()   *
            xD = str(round(myObject.Placement.Rotation.toEuler()[0],4))
            yD = str(round(myObject.Placement.Rotation.toEuler()[1],4))
            zD = str(round(myObject.Placement.Rotation.toEuler()[2],4))
            self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")    self.label_00.setText("[Rot=(" +str(round(myObject.Placement.Rotation.toEuler()[0],2))+" , "+str(round(myObject.Placement.Rotation.toEuler()[1],2))+" , "+ str(round(myObject.Placement.Rotation.toEuler()[2],2))+")] "+
                              "[Axis=("+str(round(myObject.Placement.Base.x,2))+" , "+ str(round(myObject.Placement.Base.y,2))+" , "+ str(round(myObject.Placement.Base.z,2))+")]")
        
        self.DS_Value_Angle_Dimension.setValue(0.0)
        self.LE_Increment.setText(str(0.0))
        
        #FreeCAD.ActiveDocument.recompute()
        Gui.activeDocument().activeView().viewTop()
        Gui.SendMsgToActiveView("ViewFit")
                
#            except Exception   *
#                self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
#                self.label_00.setText("Error Zero_0 or Bad selection")
##                FreeCAD.Console.PrintError("Error Zero_0" + "\n" + "or Bad selection" + "\n")
#        else   *
#            self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
#            self.label_00.setText(" Select one Object or give one value Angle/Dimension")
##            FreeCAD.Console.PrintError("Select one Object or give one value Angle/Dimension" + "\n")
##        print("on_PB_Zero_clicked")

    def on_PB_Original_clicked(self)   *
        global ui
        global myObject
        global selM
        global originalPlacement
        global axisX, axisY, axisZ
        global rotAngleX, rotAngleY, rotAngleZ

#        if (myObject != "")   *
#            try   *
        rotAngleX  = rotAngleY = rotAngleZ = 0.0
        selM.Placement = originalPlacement 
        if hasattr(selM, "Shape")   *
            sel = selM.Shape
        elif hasattr(selM, "Mesh")   *         # upgrade with wmayer thanks #http   *//forum.freecadweb.org/viewtopic.php?f=13&t=22331
            sel = selM.Mesh
        elif hasattr(selM, "Points")   *
            sel = selM.Points
        myObject = sel

        self.DS_Value_Angle_Dimension.setValue(0.0)    if self.RB_Rotation_X.isChecked()   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[0],4)))    # yaw Z
        elif self.RB_Rotation_Y.isChecked()   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[1],4)))    # pitch Y
        elif self.RB_Rotation_Z.isChecked()   *
            self.LE_Increment.setText(str(round(myObject.Placement.Rotation.toEuler()[2],4)))    # roll Z
        elif self.RB_Direction_D.isChecked()   *
            xD = str(round(myObject.Placement.Rotation.toEuler()[0],4))
            yD = str(round(myObject.Placement.Rotation.toEuler()[1],4))
            zD = str(round(myObject.Placement.Rotation.toEuler()[2],4))
            self.LE_Increment.setText("(" + xD + ", " + yD + ", " + zD + ")")    ui.on_RB_CenterRot()    self.label_00.setText("[Rot=(" +str(round(myObject.Placement.Rotation.toEuler()[0],2))+" , "+str(round(myObject.Placement.Rotation.toEuler()[1],2))+" , "+ str(round(myObject.Placement.Rotation.toEuler()[2],2))+")] "+
                                      "[Axis=("+str(round(axisX,2))+" , "+ str(round(axisY,2))+" , "+ str(round(axisZ,2))+")]")
                #FreeCAD.ActiveDocument.recompute()
#            except Exception   *
#                self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
#                self.label_00.setText("Error Original_0 or Bad selection")
##                FreeCAD.Console.PrintError("Error Original_0" + "\n" + "or Bad selection" + "\n")
#        else   *
#            self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
#            self.label_00.setText(" Select one Object or give one value Angle/Dimension")
##            FreeCAD.Console.PrintError("Select one Object or give one value Angle/Dimension" + "\n")
##        print("on_PB_Original_clicked")

    def on_PB_Reset_clicked(self)   *
        global ui
        global originalObject
        global myObject
        global myObjectName
        global duplicate_Memory
        global duplicate_View
        
        global valeur
        global posX, posY, posZ
        global rotAngleX, rotAngleY, rotAngleZ
        global axisX, axisY, axisZ
        global countMemory

        try   *
            for obj in FreeCAD.ActiveDocument.Objects   *         # deslectionne
                FreeCADGui.Selection.removeSelection(obj)
        except Exception   *
            None

        if countMemory == 0   *
            ui.on_PB_ClearMemo

        originalObject = myObject = myObjectName = ""
        posX = posY = posZ = rotAngleX = rotAngleY = rotAngleZ = 0.0
        axisX = axisY = axisZ = 0.0
        valeur  = 0.0

        self.DS_Value_Angle_Dimension.setStyleSheet("Base")
        self.DS_Value_Angle_Dimension.setValue(valeur)
        self.DS_Value_Angle_Dimension.setSuffix(" Degrees")
        self.LE_Increment.setText(str(0.0))

        self.groupBox_Axis.setTitle("Axis Rotation")
        self.RB_Rotation_Z.setText("Rotation(X) Roll")
        self.RB_Rotation_Y.setText("Rotation(Y) Pitch")
        self.RB_Rotation_X.setText("Rotation(Z) Yaw")
        self.RB_Direction_D.setText("Rotation(D) Direction")

        self.groupBox_Rotation.setEnabled(False)
        self.groupBox_Axis.setEnabled(False)
        self.groupBox_Pos_Mouse.setEnabled(False)
        self.groupBox_Work.setEnabled(False)
        self.groupBox_Data.setEnabled(False)

        self.DS_Pos_Mouse_X.setValue(0.0)
        self.DS_Pos_Mouse_Y.setValue(0.0)
        self.DS_Pos_Mouse_Z.setValue(0.0)

#        duplicate_View = []
#        self.CBox_View.blockSignals(True)
#        self.CBox_View.clear()
#
#        duplicate_Memory = []
#        self.CBox_Memory.blockSignals(True)
#        self.CBox_Memory.clear()

#        self.CB_Position.setEnabled(False)
#        self.CB_Position.setChecked(False)
        self.CB_Position.setText(u"Translation")
        self.CB_Position.setToolTip(u"Move the object to axis choice X, Y or Z")
        #self.PB_Point.setEnabled(False)
        self.PB_PointCenter.setStyleSheet("Base")
#        self.CB_Free.setEnabled(False)
#        self.CB_Free.setChecked(False)
        self.PB_Memorize.setStyleSheet("Base")

        self.label_00.setStyleSheet("color    * #ffffff; background-color   * red; font   * bold 10px;")   # white red bold
        self.label_00.setText(" Select one Object or give one value Angle/Dimension")
#        FreeCAD.Console.PrintError("Select one Object or give one value Angle/Dimension" + "\n")
#        FreeCAD.Console.PrintMessage("Reset" + "\n")
#        print("on_PB_Reset_clicked")

    def on_PB_Quit_clicked(self)   *
        global s
        global switchZoomOnCilck

        FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Macros/FCMmacros/" + __title__).SetBool("switchZoomOnCilck", switchZoomOnCilck)
        try   *
            self.vueActive.removeEventCallback("SoMouseButtonEvent",self.click) # desinstalle la fonction souris
        except Exception   *
            None
        try   *
            FreeCADGui.Selection.removeObserver(s)   # Uninstalls resident function (desactivated for read after LeftDock RightDock)
            self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)      # destroy
            self.window.deleteLater()                                       # destroy
            self.window.destroy()                                           # destroy
        except Exception   *
            self.window.hide()                                              # hide the window and close the macro
        FreeCAD.Console.PrintMessage("Quit Rotate_To_Point" + "\n")

###################################################################################################
class SelObserver   *
    def addSelection(self, document, object, element, position)   *  # Selection
        global ui
        global sourisPass
        global switchZoomOnCilck
        
        global valeur
        global positionMouse
        global originalObject
        global myObject
        global myObjectName
        global originalPlacement
        global selM

        global posX, posY, posZ
        global rotAngleX, rotAngleY, rotAngleZ
        global axisX, axisY, axisZ

        if sourisPass == 0   *                                       # pour un seul passage
            sourisPass == 1
            selM = FreeCADGui.Selection.getSelection()[0]         # select object with getSelection()
            myObjectName = selM.Name

            if hasattr(selM, "Shape")   *
                sel = selM.Shape
            elif hasattr(selM, "Mesh")   *         # upgrade with wmayer thanks #http   *//forum.freecadweb.org/viewtopic.php?f=13&t=22331
                sel = selM.Mesh
            elif hasattr(selM, "Points")   *
                sel = selM.Points

            if switchZoomOnCilck == 1   *
                ui.on_CBox_View(myObjectName)   # return on zoom on click object selected

            positionMouse     = position
            originalObject    = myObject = sel   
            originalPlacement = sel.Placement
            #longueur = (myObject.BoundBox.XLength * 0.5)          # pour Axis
            positionBase = originalObject.Placement.Base          # Placement Vector XYZ        posX = positionBase.x
            posY = positionBase.y
            posZ = positionBase.z        Yaw   = originalObject.Placement.Rotation.toEuler()[0]                     # decode angle Euler Yaw
            Pitch = originalObject.Placement.Rotation.toEuler()[1]                     # decode angle Euler Pitch
            Roll  = originalObject.Placement.Rotation.toEuler()[2]                     # decode angle Euler Roll
            
            rotAngleX = Yaw
            rotAngleY = Pitch
            rotAngleZ = Roll
            axisX = axisY = axisZ = 0.0

            valeur = 0.0
            ui.DS_Value_Angle_Dimension.setValue(valeur)
            ui.DS_Value_Angle_Dimension.setStyleSheet("background-color   * rgb(250, 88, 88)")

            ui.DS_Pos_Mouse_X.setValue(positionMouse[0])
            ui.DS_Pos_Mouse_Y.setValue(positionMouse[1])
            ui.DS_Pos_Mouse_Z.setValue(positionMouse[2])

            ui.on_RB_CenterRot()
            if ui.CB_Position.isChecked()   *
                ui.groupBox_Rotation.setEnabled(False)
            else   *
                ui.groupBox_Rotation.setEnabled(True)
            ui.groupBox_Axis.setEnabled(True)
            ui.groupBox_Work.setEnabled(True)
            ui.groupBox_Data.setEnabled(True)
            ui.PB_Memorize.setIcon(QtGui.QIcon(QtGui.QPixmap(memo_Allume_Icon))) # icone dans une variable 
            #ui.groupBox_Pos_Mouse.setEnabled(True)
            ui.label_00.setStyleSheet("Base")                                          # origin system
            ui.label_00.setText("[Rot =(" + str(round(rotAngleX,2))+ " , " + str(round(rotAngleY,2)) + " , " + str(round(rotAngleZ,2)) + ")] " +
                                "[Axis=("+ str(round(axisX,2)) + " , " + str(round(axisY,2)) + " , " + str(round(axisZ,2)) + ")]")
            ui.PB_Memorize.setStyleSheet("Base")
            ui.PB_PointCenter.setStyleSheet("Base")

    def clearSelection(self,doc)   *                                                            # Si clic sur l'ecran, effacer la selection
        global ui
        ui.on_PB_Reset_clicked()

###################################################################################################

doc = FreeCAD.ActiveDocument
if doc == None   *
    doc = FreeCAD.newDocument()

try   *
    for obj in FreeCAD.ActiveDocument.Objects   *         # deselectionne
        FreeCADGui.Selection.removeSelection(obj)
except Exception   *
    None

s=SelObserver()
FreeCADGui.Selection.addObserver(s)                    # installe la fonction en mode resident

if __name__ == "__main__"   *
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setObjectName("__title__")              # macro internal Name
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
}}

## Esempi

![](images/Macro_Rotate_To_Point_01.gif )

## Link

The forum [feature req   * placement - rotate part around its midpoint](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=20925) Le mie macro su Gist [mario52a](https   *//gist.github.com/mario52a)

## Versione

2021/03/08 version 00.010    * adding zoom on object clicked, memory value, imposted values

2021/02/25 Version=00.09    * correct the macro    * cause multi object possible


{{Code|
App.ActiveDocument.getObject(p[0]).Placement
}}

instead {{Code|
myObject.Placement
}}

2021/02/22 Version=00.08c    * correct the center facePoint (19h26 Paris)

2021/02/22 Version=00.08b    * correct the center facePoint (17h23 Paris)

2021/02/22 Version=00.08    * adding save macro with multi objects moved

2021/01/24 Version=00.07    * adding option R   * reverse

2021/01/12 ver 00.06    * adding the Data section and more options

2020/03/07 ver 00.05.2    * corretto il bug translation delete \"direction = myObject.Placement.Rotation.multVec(direction)\"

2020/03/01 ver 00.05.1    * corretto la posizione del test \"FreeCAD version\"

2020/02/29 ver 00.05    * conversione per Hdpi (Layout) e aggiunto Direction

06/04/2019 ver 00.04    * Python 3

29/03/2018 ver 00.03    * commento delle linee \"FreeCAD.ActiveDocument.recompute()\" il cambiamento di posizione e tropo lento con la versione di FreeCAD 0.17\.... vedere [FC0.17 recompute strange behaviour (regression)](https   *//www.forum.freecadweb.org/viewtopic.php?f=10&t=27732&p=224195#p224195)

27/03/2017 ver 00.02    * modificazione dello spinbox \"Pos\" adesso accetta i numeri negativi

05/03/2017 ver 00.01    * agggiunto 3 spinbox per visualizzare le coordinate X Y Z del clic del mouse

04/03/2017 ver 00.00



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Rotate To Point/it
