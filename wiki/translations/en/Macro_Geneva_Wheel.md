# Macro Geneva Wheel/en

 {{Macro
|Name=Geneva Wheel
|Icon=GW_Dim.png
|Description=Allows the user to create a Geneva wheel mechanism from scratch. Must edit values within the Macro to alter the size of the object.
|Author=Drei
|Version=1.0
|Date=2014-09-21
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/8/8d/GW_Dim.png ToolBar Icon]
}}

## Description

Allows the user to create a Geneva wheel mechanism from scratch. Must edit values within the Macro to alter the size of the object.

![](images/Geneva.png )

## How To Use 

This Macro creates the main parts of a Geneva Wheel Mechanism. It depends on six values that must be altered in the code, read the comments in the code. The variables are:

+------------------------------+----------------------------------+
| Input                        | Output                           |
+==============================+==================================+
| -   a = Drive Crank Radius   | -   c = Distance Between Centers |
| -   b = Geneva Wheel Radius  | -   s = Slot Center Width        |
| -   n = Driven Slot Quantity | -   w = Slot Width               |
| -   p = Drive Pin Diameter   | -   y = Stop Arc Radius          |
| -   t = Tolerance            | -   z = Stop Disc Radius         |
| -   h = Height               | -   v = Clearance Arc            |
+------------------------------+----------------------------------+

## Link

[Macro Geneva Wheel GUI](Macro_Geneva_Wheel_GUI.md): A GUI front end based on this macro that allows the user to create a Geneva wheel mechanism from scratch.

## Script

ToolBar Icon ![](images/GW_Dim.png )

**Macro\_Geneva\_Wheel.FCMacro**


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




