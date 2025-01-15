---
 TutorialInfo:
   Topic:  Part Scripting - Ball Bearing #1
   Level:  Beginner
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Introduction

This tutorial is meant as a beginner\'s introduction to creating parts with python scripts within FreeCAD.
This tutorial will cover how to build a ball bearing with a CSG-workflow.
The code will produce a new FreeCAD document with 12 shapes .
It will look like this:
!{width="400"}

### Workflow

The workflow is more or less identical how you would create the part in part workbench.
Just some small differences.
\*Create a new empty document and make it the active document

-   Insert Cylinder
-   Insert Cylinder
-   Do boolean cut to get basic shape of inner ring
-   Select all edges and apply a fillet
-   Insert torus
-   Move torus into position and do a boolean cut to create the groove for the balls
-   Repeat all steps for getting the shape for the outer ring
-   Insert first ball
-   Insert other balls using math to calculate the position of the balls
-   Set view to axometric
-   Zoom to fit all

### Filleting edges 

In part workbench using the GUI, you would select chamfers in the 3D view or in the menu for fillets and then apply the fillets.
Here we select all edges of a shape and apply fillets.
Therefore we need to select the edges BEFORE creating the groove.

### Notes

This tutorial is using part primitives and boolean operations, which can be performance consuming.
For doing a scripted part with revolved sketches have a look at the tutorial Scripted Parts: Ball Bearing - Part 2.

### Links

Scripted objects: The wiki page explaing the basics of scripting
Topological data scripting: A tutorial for covering basics of scripting
Scripted Parts: Ball Bearing - Part 2: Doing it with sketches
Bearing Script 1: Base for this tutorial, thanks to JMG \...

### Code


{{Code   code: 
## Ball-bearing script
## 11.08.2016 by r-frank 
## based on ball bearing script by JMG
## 
#
#needed for inserting primitives
import Part
#needed for calculating the positions of the balls
import math
#needed for translation of torus
from FreeCAD import Base
#
#VALUES#
#
R1=15.0
#
R2=25.0
#
R3=30.0
#
R4=40.0
#
TH=15.0
#
NBall=10
#
RBall=5.0
#
RR=1
#first coordinate of center of ball
CBall=/2)+R2
#second coordinate of center of ball
PBall=TH/2
#
#Create new document
App.newDocument
App.setActiveDocument
App.ActiveDocument=App.getDocument
Gui.ActiveDocument=Gui.getDocument
#
#Inner Ring#
B1=Part.makeCylinder
B2=Part.makeCylinder
IR=B2.cut
#get edges and apply fillets
Bedges=IR.Edges
IRF=IR.makeFillet
#create groove and show shape
T1=Part.makeTorus
T1.translate)
InnerRing=IRF.cut
Part.show
#
#Outer Ring#
B3=Part.makeCylinder
B4=Part.makeCylinder
OR=B4.cut
#get edges and apply fillets
Bedges=OR.Edges
ORF=OR.makeFillet
#create groove and show shape
T2=Part.makeTorus
T2.translate)
OuterRing=ORF.cut
Part.show
#
#Balls#
for i in range:
  Ball=Part.makeSphere
  Alpha=/NBall
  BV=,CBall*math.sin,TH/2)
  Ball.translate
  Part.show
#
#Make it pretty#
App.activeDocument.recompute
Gui.activeDocument.activeView.viewAxometric
Gui.SendMsgToActiveView
---

# Scripted Parts: Ball Bearing - Part 1/en

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted Parts: Ball Bearing - Part 1/en
