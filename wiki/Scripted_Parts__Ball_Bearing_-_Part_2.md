---
 TutorialInfo:
   Topic:  Part Scripting - Ball Bearing #2
   Level:  Beginner
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Introduction

This tutorial is meant as a beginner\'s introduction to creating parts with python scripts within FreeCAD.
This tutorial will cover how to build a ball bearing with a workflow that consists of creating sketches and revolving them.
The code will produce a new FreeCAD document with 12 shapes .
It will look like this:
!{width="400"}

### Workflow

The workflow is more or less identical how you would create the part in part design workbench.
Just some small differences.
\*Create a new empty document and make it the active document

-   Draw the basic shape of the outer ring consisting of four straight lines and four arcs

!{width="150"}

-   Connect the lines and arcs and upgrade them to one single wire
-   Upgrade the wire to a face
-   Revolve the face to get a shape
-   Draw a circle
-   Upgrade circle to wire
-   Upgrade wire to face
-   Revolve face and apply boolean cut to obtain groove in outer ring
-   Draw the basic shape of the inner ring consisting of four straight lines and four arcs
-   Connect the lines and arcs and upgrade them to one single wire
-   Upgrade the wire to a face
-   Revolve the face to get a shape
-   Draw a circle
-   Upgrade circle to wire
-   Upgrade wire to face
-   Revolve face and apply boolean cut to obtain groove in inner ring
-   Insert balls with same workflow as in part 1 
-   Set view to axometric
-   Zoom to fit all

### Making the groove 

Drawing an arc needs either three points or a start angle and an end angle.
In the sketcher we would use constraints to define the start point and the end point of the arc.
Since we can\'t do this in scripting, we draw a rounded rectangle and revolve it to get a basic \"ring shape\".
Then we draw a circle and revolve it to get the geometry of the groove.
Then we apply a boolean cut to the two revolved shapes and we have the complete shape of the inner/outer ring.

### Inserting the balls 

The correct sketcher-based workflow of inserting the balls would be:
\*Draw an arc  with center being identical with the origin and draw a line closing the \"open\" side of the arc

-   Convert the two elements to a wire, upgrade to a face, revolve around z-axis to get a ball shape
-   Use \"translate\" command to move the ball into correct position
-   Repeat the above steps nine times involving math function to create and position the other balls
-   This repeat-operation could be programmed with a loop

Now this is not effective, inserting primitives and positioning them is easier and faster in this case.
So we use the same method as in \"Scripted Parts: Ball Bearing - Part 1\".

### Links

Scripted objects: The wiki page explaining the basics of scripting
Topological data scripting: A tutorial for covering basics of scripting
Scripted Parts: Ball Bearing - Part 1: Doing it with part primitives
Bearings from scripted sketches: Base for this tutorial, thanks to JMG \...

### Code


{{Code   code: 
## Ball-bearing script
## 11.08.2016 by r-frank 
## based on ball bearing script by JMG
## 
#
#needed for doing boolean operations
import Part
#needed for calculating the positions of the balls
import math
#needed for translation and rotation of objects
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
#
#Lines for basic shape of outer ring
L1o=Part.makeLine,)
L2o=Part.makeLine,)
L3o=Part.makeLine,)
L4o=Part.makeLine,)
#Corner rounding for basic shape of outer ring
A1o=Part.makeCircle,Base.Vector,0,90)
A2o=Part.makeCircle,Base.Vector,90,180)
A3o=Part.makeCircle,Base.Vector,180,270)
A4o=Part.makeCircle,Base.Vector,270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
OR=Part.Wire
OR=Part.Face
OR=OR.revolve,Base.Vector)
C1=Part.makeCircle/2,0,TH/2),Base.Vector,0,360)
GRo=Part.Wire
GRo=Part.Face
GRo=GRo.revolve,Base.Vector)
OR=OR.cut
Part.show
#
#Lines for basic shape of inner ring
L1i=Part.makeLine,)
L2i=Part.makeLine,)
L3i=Part.makeLine,)
L4i=Part.makeLine,)
#Corner rounding for basic shape of inner ring
A1i=Part.makeCircle,Base.Vector,0,90)
A2i=Part.makeCircle,Base.Vector,90,180)
A3i=Part.makeCircle,Base.Vector,180,270)
A4i=Part.makeCircle,Base.Vector,270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
IR=Part.Wire
IR=Part.Face
IR=IR.revolve,Base.Vector)
C2=Part.makeCircle/2,0,TH/2),Base.Vector,0,360)
GRi=Part.Wire
GRi=Part.Face
GRi=GRi.revolve,Base.Vector)
IR=IR.cut
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
App.ActiveDocument.recompute
Gui.ActiveDocument.ActiveView.viewAxometric
Gui.SendMsgToActiveView
---

# Scripted Parts: Ball Bearing - Part 2

  
 {{Powerdocnavi}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 2
