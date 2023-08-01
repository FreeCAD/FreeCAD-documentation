# Macro FCInfoToMouse
{{Macro
|Name=Macro FCInfoToMouse
|Icon=FCInfoToMouse.png
|Description=Provides info about coordinates, length, and angles in real-time next to the mouse pointer.
|Author=Mario52
|Version=00.04
|Date=2018-03-27
}}

## Description

Provides info about coordinates, length, and angles in real-time next to the mouse pointer in a bubble annotation displayed in the [3D view](3D_view.md)

 

 <img alt="" src=images/Macro_FCInfoToMouse_00.png style="width:480px;">  
*FCInfoToMouse macro in action*

## Usage

1.  Install the FCInfoToMouse macro in your macros directory via the [Addon Manager](Std_AddonMgr.md)
2.  Run the [Macro](Macros.md)

:   Result: an annotation appears and the mouse coordinate information is displayed in real-time.





:   

    :   <img alt="" src=images/Macro_FCInfoToMouse_01.png  style="width:240px;">
    :   
        
*Figure 1*
        

  - **X, Y, Z**: mouse coordinates are displayed in the bubble (this only applies when \"Single\" mode is enabled) as seen in Fig. 1

:   

    :   Once the mouse is clicked for the first time, additional info is displayed (when \"Forced\" mode is enabled this setting will be solely displayed)





:   

    :   <img alt="" src=images/Macro_FCInfoToMouse_02.png  style="width:240px;">
    :   
        
*Figure 2*
        

  - **X1, Y1, Z1** : Initial coordinates of the 1st mouse click

  - **X2, Y2, Z2** : Current coordinates of the mouse

  - **L** : Length between the first mouse click and the location of the current mouse pointer

  - **XY, YZ, XZ** : Angles between the 1st point and moving mouse pointer in the XY, YZ, and XZ planes  

:   

    :   <img alt="" src=images/Macro_FCInfoToMouse_03.png  style="width:240px;">

:   
    
*Figure 3 - when mouse pointer is over an object, the name of the object will be displayed*
    





:   

    :   If the mouse hovers over an object, the object name appears at the top of the annotation (see Figure 3).

 

### Keyboard Shortcuts 

****SHIFT** + **Q****: Quit the FCInfoToMouse macro. Upon quitting the macro, the annotation remains at its current mouse pointer location. Begin using the mouse normally if you want to delete the annotation manually.

****SHIFT** + **M****: Toggle the mode between:

-   **single** which displays only the coordinates of the mouse pointer (Figure 1)
-   **force** which displays the \"**comprehensive visualisation**\" (Figure 2)
-   **normal** which displays the default behavior of the macro

****SHIFT** + **C**** : for \"**hidden / visible**\"

****SHIFT** + **D**** : to \"**Open/Close**\" a Spreadsheet with the coordinates saved to:

:   {\| class=\"wikitable\" style=\"text-align: center; color: green;\"

!Cell **A** !Cell **B** !Cell **C** !Cell **D** \|- \|x, y, z


</td>

\|x


</td>

\|y


</td>

\|z


</td>

\|}

### Notes

At any time, you can change the properties of the annotation by clicking the object FCInfoToMouse in Combo View and click the View tab

If you want change the number of decimal change the line 43 (default 4)

Example for 6 decimal places:

original value 
```python
global arrondi    ; arrondi    = 4
``` replace to 
```python
global arrondi    ; arrondi    = 6
```

To make the configuration of the permanent annotation you can change the values in the configuration section lines **104 to 122**

 

## Script

The icon **FCInfoToMouse.png** <img alt="FCInfoToMouse" src=images/FCInfoToMouse.png  style="width:64px;"> for the [Customize_ToolsBar](http://www.freecadweb.org/wiki/index.php?title=Customize_ToolsBar) 

**Macro_FCInfoToMouse.FCMacro**


{{MacroCode|code=

# -*- coding: utf-8 -*-
"""
***************************************************************************
*   Copyright (c) 2016 <mario52>                                          *
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
# http://forum.freecadweb.org/viewtopic.php?f=22&t=9215
# FCInfoToMouse

__title__   = "FCInfoToMouse"
__author__  = "Mario52"
__url__     = "https://www.freecadweb.org/wiki/Macro_FCInfoToMouse"
__version__ = "00.04"
__date__    = "27/03/2018"
#
import Draft, Part
import math,FreeCAD
from FreeCAD import Base
import time
App = FreeCAD

global arrondi    ; arrondi    = 4

global objectAnn  ; objectAnn  = "" 
global positionX1 ; positionX1 = 0.0
global positionY1 ; positionY1 = 0.0
global positionZ1 ; positionZ1 = 0.0
global force      ; force      = 0
global hidden     ; hidden     = 0
global coorBegin  ; coorBegin  = ""
global pas        ; pas        = 0

global spreadSheet; spreadSheet= 0
global compteur   ; compteur   = 0 
global spread     ; spread     = ""

from math import sqrt, pi, sin, cos, asin, acos, atan, atan2, degrees

def angle2(vecteur_x1,vecteur_y1,vecteur_x2,vecteur_y2,mode):   #tester getAngle ( Vector )
# calcul de l'inclinaison d'une ligne a partir de deux Vecteurs
# si "mode" = 1 alors affichage en degres sinon en radian
    try:
        deltaX = vecteur_x2 - vecteur_x1
        deltaY = vecteur_y2 - vecteur_y1
        if mode ==1:
            angle = degrees(atan2(float(deltaY),float(deltaX))) # degres  (mode = 1)
        else:
            angle = atan2(float(deltaY),float(deltaX))          # radian  (mode = 0)
        return round(angle,arrondi)
    except Exception:
        None

def sub(first, other): 
    "sub(Vector,Vector) - subtracts second vector from first one"
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return FreeCAD.Vector(first.x-other.x, first.y-other.y, first.z-other.z)

def length(first):
    "lengh(Vector) - gives vector length"
    if isinstance(first,FreeCAD.Vector):
        return math.sqrt(first.x*first.x + first.y*first.y + first.z*first.z)

def dist(first, other):
    "dist(Vector,Vector) - returns the distance between both points/vectors"
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return length(sub(first,other))

def codeColor(color):
    try:
        rgb = float((float(color)/255.0))
    except Exception:
        rgb = 0.0
    return rgb


doc = FreeCAD.ActiveDocument    
if doc == None:
    doc = FreeCAD.newDocument()

# for modify the configuration : line 104 to 122
# PS: if DisplayMode = "Line" and Frame = False the annotation is transparent
#
##### Configuration  Modify here # Begin #######################################
                                                                               #
#BackgroundColor :                                                             #
red_B           = 0.0                # 0.0 to 255.0                            #
green_B         = 84.0               # 0.0 to 255.0                            #
blue_B          = 255.0              # 0.0 to 255.0                            #
                                                                               #
displayMode     = "Line"             # "Line" or "Object"                      #
fontName        = "MS Shell Dlg 2"   # "MS Shell Dlg 2" for Windows            #
fontSize        = 8.0                # Font size                               #
frame           = False              # "False" or "True"                       #
justification   = "Left"             # "Left", "Right", "Center"               #
                                                                               #
#TextColor       :                                                             #
red_T           = 255.0              # 0.0 to 255.0                            #
green_T         = 255.0              # 0.0 to 255.0                            #
blue_T          = 255.0              # 0.0 to 255.0                            #
                                                                               #
##### Configuration  End End ###################################################

v=Gui.activeDocument().activeView()
objectAnn = App.ActiveDocument.addObject("App::AnnotationLabel","FCInfoToMouse")# create work annotation
objectAnn.LabelText=["Hello FreeCAD World"]

FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).BackgroundColor = (codeColor(red_B),codeColor(green_B),codeColor(blue_B))   #
FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).DisplayMode     = displayMode                                               #
FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).FontName        = fontName                                                  #
FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).FontSize        = fontSize                                                  #
FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).Frame           = frame                                                     #
FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).Justification   = justification                                             #
FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).TextColor       = (codeColor(red_T),codeColor(green_T),codeColor(blue_T))   #

import os, sys, platform
global PolicePath;    PolicePath = ""

#if platform.system() == "Windows" :
#    PolicePath = "C:/Windows/Fonts/ARIAL.TTF"
#elif platform.system() == "Linux" :
#    PolicePath = "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf"
#elif platform.system() == "Darwin":
#    PolicePath = "/Library/Fonts/Arial.ttf"
#else:
#    PolicePath = "C:/Windows/Fonts/ARIAL.TTF"

p=FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft")
PolicePath = p.GetString("FontFile")

class ViewObserver:
    def __init__(self, view):
       self.view = view

    def logPosition(self, info):
        global objectAnn
        global positionX1, positionY1, positionZ1
        global pas, arrondi
        global coorBegin
        global force
        global hidden
        global PolicePath
        global spreadSheet
        global compteur
        global spread

######## for testing key ############
#        try:                       #
#            print info["Key"]      #
#            print info["State"]    #
##            print ord(info["Key"]) #
#        except Exception:          #
#            None                   #
#####################################

        Button1 = 0

        try:
            if (info["Key"] == "Q") and (info["State"] == "DOWN"):                        # SHIFT + Q for quit
                v.removeEventCallback("SoEvent",c)                                        # close event observation
                FreeCAD.Console.PrintMessage( "End FCInfoToMouse" + "\n")
        except Exception:
            None

        try:
            if (info["Key"] == "M") and (info["State"] == "DOWN"):                        # SHIFT + M for force display
                if force == 0:
                    force = 1
                    FreeCAD.Console.PrintMessage( "Forced " + "\n")
                elif force == 1:
                    force = 2
                    FreeCAD.Console.PrintMessage( "Single " + "\n")
                elif force == 2:
                    force = 0
                    FreeCAD.Console.PrintMessage( "Normal " + "\n")
        except Exception:
            None

        try:
            if (info["Key"] == "C") and (info["State"] == "DOWN"):                        # SHIFT + C for hidden / visible annotation OK
                if hidden == 0:
                    hidden = 1
                    FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).Visibility = False
                    FreeCAD.Console.PrintMessage( "concealed " + "\n")
                else:
                    hidden = 0
                    FreeCADGui.getDocument(doc.Name).getObject(objectAnn.Label).Visibility = True
                    FreeCAD.Console.PrintMessage( "visible " + "\n")
        except Exception:
            None

        try:
            if (info["Key"] == "D") and (info["State"] == "DOWN"):                        # SHIFT + S for Open spreadSheet
                if spreadSheet == 0:
                    #spread = FreeCAD.ActiveDocument.getObjectsByLabel(spread.Name)[0]    # for append in existant SpreadSheet
                    spread = App.activeDocument().addObject('Spreadsheet::Sheet','MySpreedSheett')
                    spreadSheet = 1
                    FreeCAD.Console.PrintMessage("SpreadSheet open : " + spread.Name + "\n")
                else:
                    spreadSheet = 0
                    FreeCAD.Console.PrintMessage("SpreadSheet closed" + "\n")
                compteur    = 0
        except Exception:
            None

        try:
            object2 = ""
            object = v.getObjectInfo(v.getCursorPos())                                    # here for object preselected
            object2 = object["Object"] + "." + object["Component"]                        # object + component
            pnt = FreeCAD.Vector(float(object["x"]),float(object["y"]),float(object["z"]))# vector on position mouse to object
#            print "pnt ",pnt
        except Exception:
            pos = info["Position"]                                                        # if mouse in 3D view
            pnt = self.view.getPoint(pos)                                                 # vector detect on mouse position 3D view
#            print "pnt ",pnt

        try:
            if (info["Button"] == "BUTTON1") and (info["State"] == "DOWN"):               # coordinates clic to mouse
                positionX1 = round(pnt[0],arrondi)
                positionY1 = round(pnt[1],arrondi)
                positionZ1 = round(pnt[2],arrondi)
                
                coorBegin = ""
                coorBegin = "X1: "+str(positionX1)+"  Y1: "+str(positionY1)+"  Z1: "+str(positionZ1)
                if pas == 0:
                    pas = 1
                else:
                    pas = 0

                try:                                                   # spreadSheet
                    if spreadSheet == 1:
                        compteur += 1
                        spread.set("A"+str(compteur) ,  str(positionX1) + ", " + str(positionY1) + ", " + str(positionZ1))
                        spread.set("B"+str(compteur) ,  str(positionX1))
                        spread.set("C"+str(compteur) ,  str(positionY1))
                        spread.set("D"+str(compteur) ,  str(positionZ1))
                        App.ActiveDocument.recompute()
                        FreeCAD.Console.PrintMessage(str(compteur) + " : " +  str(positionX1) + ", " + str(positionY1) + ", " + str(positionZ1) + "\n")
                except Exception:
                    None
                
        except Exception:
            None

        try:
            objectAnn.BasePosition = (pnt[0], pnt[1], pnt[2])
            if force == 2:
                objectAnn.LabelText = ["X: " + str(round(pnt[0],arrondi)) + " Y: " + str(round(pnt[1],arrondi)) + " Z: " + str(round(pnt[2],arrondi))]
            else:
                if ((pas == 1) or (force == 1)):
                    coorEnd = longueur = angles = ""
                    coorEnd = "X2: " + str(round(pnt[0],arrondi)) + "  Y2: " + str(round(pnt[1],arrondi)) + "  Z2: " + str(round(pnt[2],arrondi))
                    longueur = "L: " + str(round(dist(FreeCAD.Vector(positionX1,positionY1,positionZ1), FreeCAD.Vector(pnt[0], pnt[1], pnt[2])),12)) # around to 12 decimales
                    alphaXY = alphaXY = alphaXZ = 0.0
                    alphaXY = str(round(angle2(positionX1,positionY1,pnt[0],pnt[1],1),arrondi))
                    alphaYZ = str(round(angle2(positionY1,positionZ1,pnt[1],pnt[2],1),arrondi))
                    alphaXZ = str(round(angle2(positionX1,positionZ1,pnt[0],pnt[2],1),arrondi))
        
                    angles = "XY: " + alphaXY + unichr(176) + "  YZ: " + alphaYZ + unichr(176) + "  XZ: " + alphaXZ + unichr(176)    # unichr(176) = degrees character
        
                    if object2 == "":
                        objectAnn.LabelText = [coorBegin, coorEnd, longueur, angles,]
                    else:
                        objectAnn.LabelText = [object2, coorBegin, coorEnd, longueur, angles,]
                else:
                    if object2 == "":
                        objectAnn.LabelText = ["X: " + str(round(pnt[0],arrondi)) + " Y: " + str(round(pnt[1],arrondi)) + " Z: " + str(round(pnt[2],arrondi)),]
                    else:
                        objectAnn.LabelText = [object2, "X: " + str(round(pnt[0],arrondi)) + " Y: " + str(round(pnt[1],arrondi)) + " Z: " + str(round(pnt[2],arrondi))]

        except Exception:
            FreeCAD.Console.PrintError("End FCInfoToMouse by an error" + "\n")
            v.removeEventCallback("SoEvent",c)                                            # close event observation

##### Begin ######
FreeCAD.Console.PrintMessage("__Welcome to FCInfoToMouse__" + "\n")
FreeCAD.Console.PrintMessage("SHIFT + Q : for quit" + "\n")
FreeCAD.Console.PrintMessage("SHIFT + M : for force display, mode single, mode normal" + "\n")
FreeCAD.Console.PrintMessage("SHIFT + C : for concealed / visible" + "\n")
FreeCAD.Console.PrintMessage("SHIFT + D : for create spreadSheet / close spreadSheet" + "\n")
FreeCAD.Console.PrintMessage("____________________________" + "\n")

pas = 0
o = ViewObserver(v)
try:
    c = v.addEventCallback("SoEvent",o.logPosition)
except Exception:
    App.ActiveDocument.removeObject(objectAnn.Label)
    FreeCAD.Console.PrintMessage( "Not GUI End FCInfoToMouse" + "\n")


}}



or to Gists [Macro_FCInfoToMouse.FCMacro](https://gist.github.com/mario52a/974214c4b83beaa41495) or the zip [Macro_FCInfoToMouse.FCMacro.zip](https://gist.github.com/mario52a/974214c4b83beaa41495/archive/d62630049d4663369fc80519a7655ee4c32c8711.zip)  

## Limitation

It is possible that the macro does not recognize some keys  

## Links

The discussion on the forum [From autocad to freecad](http://forum.freecadweb.org/viewtopic.php?f=3&t=13592)

My macros on [mario52a](https://gist.github.com/mario52a) gists  

## Version

27/03/2018 ver 00.04 : add function \"Save the coordinate in a spreadSheet key \"D\" flip/flop on,off

24/01/2016 ver 00.03 : add section configuration and replace key \"C\" to \"M\"

23/01/2016 ver 00.02 : add function \"single\", replace key \"H\" to \"C\" and correct bug

02/01/2016 : ver 0.1



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro FCInfoToMouse
