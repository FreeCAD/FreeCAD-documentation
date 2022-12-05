# Macro Geneva Wheel/fr
{{Macro/fr
|Name=Geneva Wheel
|Icon=GW_Dim.png
|Description=Cette macro crée un mécanisme de roue de Genève à partir de zéro.
|Author=Drei
|Version=1.0
|Date=2014-09-21
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/8/8d/GW_Dim.png ToolBar Icon]
}}

## Description

Permet à l\'utilisateur de créer un mécanisme de roue de Genève à partir de zéro. Vous devez modifier les valeurs dans la macro pour modifier la taille de l\'objet.

![](images/Geneva.png )

## Utilisation

Cette macro crée un mécanisma Geneva Wheel. Il dépend de six valeurs à modifier dans le code, lisez les commentaires dans le code. les variables à modifier sont :

+++
| Input                        | Output                           |
+==============================+==================================+
| -   a = Drive Crank Radius   | -   c = Distance Between Centers |
| -   b = Geneva Wheel Radius  | -   s = Slot Center Width        |
| -   n = Driven Slot Quantity | -   w = Slot Width               |
| -   p = Drive Pin Diameter   | -   y = Stop Arc Radius          |
| -   t = Tolerance            | -   z = Stop Disc Radius         |
| -   h = Height               | -   v = Clearance Arc            |
+++

## Liens

[Macro Geneva Wheel GUI](Macro_Geneva_Wheel_GUI/fr.md): Même macro mais avec interface graphique.

## Script

ToolBar Icon ![](images/GW_Dim.png )

**Macro_Geneva_Wheel.FCMacro**


{{MacroCode|code=
#Creation of a Geneva Wheel with Parametric values  By: Isaac Ayala (drei)
#This Macro creates the main parts of a Geneva Wheel Mechanism 

#It depends on six values that must be altered in the following code
#The variables are a, b, n, p, t and h. 

#Definition for each variable
#    Input
#a = Drive Crank Radius
#b = Geneva Wheel Radius
#n = Driven Slot Quantity
#p = Drive Pin Diameter
#t = Tolerance
#h = Height
#    Output
#c = Distance Between Centers
#s = Slot Center Width
#w = Slot Width
#y = Stop Arc Radius
#z = Stop Disc Radius
#v = Clearance Arc

#Please note that you can alter the code so it depends on five values exclusively
#Just replace c, and either a or b with the following
#    Keep value for a
#c = a/math.sin(math.pi/n)
#b = math.sqrt((math.pow(c,2))-(math.pow(a,2)))
#    Keep value for b
#c = b/math.cos(math.pi/n)
#a = math.sqrt((math.pow(c,2))-(math.pow(b,2)))

from __future__ import division
import time
import math
from PySide import QtCore, QtGui
from FreeCAD import Base
import Part

#Inputs
a = 25.0
b = 60.0
n = 6
p = 4
t = 0.01
h = 5
T = 60

#Outputs
c = math.sqrt(pow(a,2) + pow(b,2))
s = a + b - c
w = p + t
y = a - (1.5 * p)
z = y - t
v = (b * z)/a 

#    Create the Drive Crank (Will be placed on the origin)
driveCrank = Part.makeCylinder(z, h)
driveCrank.translate(Base.Vector(0,0,0))

genevaWheelClearanceCut = Part.makeCylinder(b, h)
genevaWheelClearanceCut.translate(Base.Vector(-c,0,0))

driveCrank = driveCrank.cut(genevaWheelClearanceCut)

driveCrankBase = Part.makeCylinder((1.5*a), h)
driveCrankBase.translate(Base.Vector(0,0,-h))

driveCrank = driveCrank.fuse(driveCrankBase)

drivePin = Part.makeCylinder(p,h)
drivePin.translate(Base.Vector(-a,0,0))

driveCrank = driveCrank.fuse(drivePin)

#    Create the Geneva  Wheel (Will be placed on the x-axis on the left side)
genevaWheel = Part.makeCylinder(b,h)
genevaWheel.translate(Base.Vector(-c,0,0))

stopArc = Part.makeCylinder(y, h)
stopArc.translate(Base.Vector(((y-(b/2)),0,0)))
stopArc.rotate(Base.Vector(-c,0,0),Base.Vector(0,0,1),30)

for i in range(6):
    stopArc.rotate(Base.Vector(-c,0,0),Base.Vector(0,0,1),60)
    genevaWheel = genevaWheel.cut(stopArc)

slotLength = Part.makeBox(s,(2*w),h)
slotLength.translate(Base.Vector(-a,-w,0))

slotRadius = Part.makeCylinder(w,h)
slotRadius.translate(Base.Vector(-a,0,0))

slot=slotLength.fuse(slotRadius)

for i in range(6):
    slot.rotate(Base.Vector(-c,0,0),Base.Vector(0,0,1),60)
    genevaWheel = genevaWheel.cut(slot)

#    Display Result

Part.show(driveCrank)
Part.show(genevaWheel)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Geneva Wheel/fr
