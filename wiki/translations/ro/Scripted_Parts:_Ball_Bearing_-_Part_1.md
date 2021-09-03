 {{TutorialInfo/ro
|Topic= Part Scripting - Ball Bearing #1
|Level= Beginner
|Time= 30 min
|Author=r-frank
|FCVersion=0.16.6706
|Files=
}}

### Introduction

Acest tutorial este conceput ca o introducere pentru începători în crearea de piese cu script Python în cadrul FreeCAD.
Acest tutorial descrie cum să construiți un rulment cu bile CSG-workflow.
Codul va produce un nou document FreeCAD cu 12 forme (Inel INterior, Inel exterior și 10 bile/sfere).
Va arăta astfel:
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

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

### Filleting edges {#filleting_edges}

In part workbench using the GUI, you would select chamfers in the 3D view or in the menu for fillets and then apply the fillets.
Here we select all edges of a shape and apply fillets.
Therefore we need to select the edges BEFORE creating the groove.

### Note

Acest tutorial folosește primitive și operații booleene, care pot fi consumatoare de performanță.
For doing a scripted part with revolved sketches have a look at the tutorial [Scripted Parts: Ball Bearing - Part 2](Scripted_Parts:_Ball_Bearing_-_Part_2.md).

### Links

[Scripted objects](Scripted_objects.md): Pagina wiki explică elementele de bază ale scripting-ului
[Topological data scripting](Topological_data_scripting.md): Un tutorial care acoperă elementele de bază ale scripturilor
[Scripted Parts: Ball Bearing - Part 2](Scripted_Parts:_Ball_Bearing_-_Part_2.md): Doing it with sketches
[Bearing Script 1](http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html): Base for this tutorial, thanks to JMG \...

### Code


```python
## Ball-bearing script
## 11.08.2016 by r-frank (BPLRFE/LearnFreeCAD on Youtube)
## based on ball bearing script by JMG
## (http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html)
#
#needed for inserting primitives
import Part
#needed for calculating the positions of the balls
import math
#needed for translation of torus
from FreeCAD import Base
#
#VALUES#
#(radius of shaft/inner radius of inner ring)
R1=15.0
#(outer radius of inner ring)
R2=25.0
#(inner radius of outer ring)
R3=30.0
#(outer radius of outer ring)
R4=40.0
#(thickness of bearing)
TH=15.0
#(number of balls)
NBall=10
#(radius of ball)
RBall=5.0
#(rounding radius for fillets)
RR=1
#first coordinate of center of ball
CBall=((R3-R2)/2)+R2
#second coordinate of center of ball
PBall=TH/2
#
#Create new document
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
#
#Inner Ring#
B1=Part.makeCylinder(R1,TH)
B2=Part.makeCylinder(R2,TH)
IR=B2.cut(B1)
#get edges and apply fillets
Bedges=IR.Edges
IRF=IR.makeFillet(RR,Bedges)
#create groove and show shape
T1=Part.makeTorus(CBall,RBall)
T1.translate(Base.Vector(0,0,TH/2))
InnerRing=IRF.cut(T1)
Part.show(InnerRing)
#
#Outer Ring#
B3=Part.makeCylinder(R3,TH)
B4=Part.makeCylinder(R4,TH)
OR=B4.cut(B3)
#get edges and apply fillets
Bedges=OR.Edges
ORF=OR.makeFillet(RR,Bedges)
#create groove and show shape
T2=Part.makeTorus(CBall,RBall)
T2.translate(Base.Vector(0,0,TH/2))
OuterRing=ORF.cut(T2)
Part.show(OuterRing)
#
#Balls#
for i in range(NBall):
  Ball=Part.makeSphere(RBall)
  Alpha=(i*2*math.pi)/NBall
  BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),TH/2)
  Ball.translate(BV)
  Part.show(Ball)
#
#Make it pretty#
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
