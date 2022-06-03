# Macro Draft Circle 3 Points 3D/it
{{Macro/it
|Name=Macro Draft Circle 3 Points 3D
|Translate=Cerchio da 3 punti 3D
|Icon=Macro_Draft_Circle_3_Points.png
|Description=Crea un cerchio passante per tre punti selezionati nello spazio.
|Author=galou_breizh
|Version=01.00
|Date=2013-03-16
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/1/10/Macro_Draft_Circle_3_Points.png ToolBar Icon]
}}

## Descrizione

Questa macro crea un cerchio passante per tre punti selezionati nello spazio 3D.

I punti possono essere oggetti come punti oppure cubi, cilindri \... in questo caso sono utilizzate le coordinate del loro centro.

<img alt="" src=images/Macro_Draft_Circle_3_Points_3D.png  style="width   *480px;">


<div class="mw-translate-fuzzy">

## Utilizzo

Selezionare 3 punti o forme nella vista 3D poi avviare la macro.

Se la forma è una linea, le coordinate sono date dal centro della linea.


</div>

## Limitazioni

L\'ordine di selezione delle forme influenza l\'angolo \"**AXIS**\" e inverte l\'inclinazione del cerchio. In questo caso, invertire o cambiare l\'ordine di selezione delle forme.

Le coordinate **X,Y,Z** di valore **0** oppure un allineamento non permettono l\'esecuzione dei calcoli, possono restituire un errore di divisione per zero che viene mostrato con \"**The three points are aligned**\"

## Script

ToolBar Icon ![](images/Macro_Draft_Circle_3_Points.png )

**Macro\_Draft\_Circle\_3\_Points\_3D.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
# Create a circle from 3 points selected on the X, Y, Z map
# 04/03/2013
# From https   *//en.wikipedia.org/wiki/Circumscribed_circle#Cartesian_coordinates_from_cross-_and_dot-products
# Also see    * https   *//math.stackexchange.com/questions/2658318/how-to-find-the-circumcenter-of-a-triangle-and-the-length-of-the-corresponding-r
# O=R/2S*(acosα⋅A+bcosβ⋅B+ccosγ⋅C)  ; R is circumradius, S is area of triangle
# 08/08/2014 PyQt4 and PySide

#OS   * Windows Vista
#Word size   * 32-bit
#Version   * 0.14.3700 (Git)
#Branch   * releases/FreeCAD-0-14
#Hash   * 32f5aae0a64333ec8d5d160dbc46e690510c8fe1
#Python version   * 2.6.2
#Qt version   * 4.5.2
#Coin version   * 3.1.0
#SoQt version   * 1.4.1
#OCC version   * 6.5.1

try   *
    import PyQt4
    from PyQt4 import QtCore, QtGui
except Exception   *
    import PySide
    from PySide import QtCore, QtGui
from math import pi, asin
import Draft, FreeCAD, FreeCADGui
from FreeCAD import Base

def errorDialog(msg)   *
    # Create a simple dialog QMessageBox
    # The first argument indicates the icon used   * one of QtGui.QMessageBox.{NoIcon, Information, Warning, Critical, Question} 
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical,u"Error Message",msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()

def affiche(x,y,z,r,angle)   *
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Coordinates",u"Coordinate X    * "+str(x)+"\r\n"+u"Coordinate Y    * "+str(y)+"\n"+u"Coordinate Z    * "+str(z)+"\nRadius\t      * "+str(r)+"\nAngle\t      * "+str(angle))
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.setWindowModality(QtCore.Qt.NonModal)
    diag.exec_()

# objects selected
sel = FreeCADGui.Selection.getSelection()
# If there are 3 selected points so...
if len(sel)==3    *
    # Assignment of variables
    P1 = sel[0].Shape.BoundBox.Center
    P2 = sel[1].Shape.BoundBox.Center
    P3 = sel[2].Shape.BoundBox.Center

    P1P2 = (P2 - P1).Length
    P2P3 = (P3 - P2).Length
    P3P1 = (P1 - P3).Length

    # Circle radius.
    l = ((P1 - P2).cross(P2 - P3)).Length
    try   *
        #if l < 1e-8   *
        #    errorDialog("The three points are aligned")
        r = P1P2 * P2P3 * P3P1 / 2 / l
    except   *
        errorDialog("The three points are aligned")
    else   *
        # Sphere center.
        a = P2P3**2 * (P1 - P2).dot(P1 - P3) / 2 / l**2
        b = P3P1**2 * (P2 - P1).dot(P2 - P3) / 2 / l**2
        c = P1P2**2 * (P3 - P1).dot(P3 - P2) / 2 / l**2
        P1.multiply(a)
        P2.multiply(b)
        P3.multiply(c)
        PC = P1 + P2 + P3

        # Creation of a circle
        pl = Base.Placement()
        v = (P1 - P2).cross(P3 - P2)
        v.normalize()
        axis = Base.Vector(0, 0, 1).cross(v)
        angle = asin(axis.Length) * 180 / pi
        axis.normalize()
        pl = Base.Placement(PC, axis, angle)
        Draft.makeCircle(r, placement=pl, face=False, support=None)
        # Displays the result in the windows
        affiche((PC.x),(PC.y),(PC.z),r,angle)
        # Displays the result in the FreeCAD report view
        #FreeCAD.Console.PrintMessage("Coordinate X    * "+str(PC.x)+"\n")
        #FreeCAD.Console.PrintMessage("Coordinate Y    * "+str(PC.y)+"\n")
        #FreeCAD.Console.PrintMessage("Coordinate Z    * "+str(PC.z)+"\n")
        #FreeCAD.Console.PrintMessage("Radius          * "+str(r)+"\n")
        #FreeCAD.Console.PrintMessage("Angle           * "+str(angle)+"\n")
else   *
    # If the condition is not met, repeat
    #FreeCAD.Console.PrintError("Select 3 points and repeat\n")
    errorDialog("Select 3 points and repeat\n")

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Draft Circle 3 Points 3D/it
