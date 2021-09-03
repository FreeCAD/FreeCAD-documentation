 {{TutorialInfo/it
|Topic= Parti con script - Cuscinetto a sfere #1
|Level= Base
|Time= 30 min
|Author=r-frank
|FCVersion=0.16.6706
|Files=
}}

### Introduzione

Questo tutorial si propone di introdurre i principianti alla creazione di parti con script python all\'interno di FreeCAD.
Questo tutorial descrive come costruire un cuscinetto a sfere con un flusso di lavoro [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry).
Il codice produrrà un nuovo documento di FreeCAD con 12 forme (anello interno, anello esterno e 10 sfere).
Esso sarà simile a questo:
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

### Flusso di lavoro 

Il flusso di lavoro è quasi identico a quello che si dovrebbe usare per creare la parte nell\'ambiente Part. Solo alcune piccole differenze.

-   Creare un nuovo documento vuoto e renderlo attivo
-   Inserire un Cilindro
-   Inserire un Cilindro
-   Fare un taglio booleano per ottenere la forma di base dell\'anello interno
-   Selezionare tutti i bordi e applicare un raccordo
-   Inserire un Toro
-   Spostare il toro in posizione e fare un taglio booleano per creare la scanalatura per le sfere
-   Ripetere tutti i passaggi per ottenere la forma per l\'anello esterno
-   Inserire prima sfera
-   Inserire le altre sfere usando math per calcolare la loro posizione
-   Impostare la vista assonometrica
-   Zoom per adattare la vista alla finestra

### Raccordare i bordi 

Nell\'ambiente Part utilizzando la GUI, è necessario selezionare i raccordi nella vista 3D o nel menu per i raccordi e poi applicare i raccordi.
Qui si selezionano tutti i bordi di una forma e poi si applicano i raccordi.
Quindi bisogna selezionare i bordi prima di creare la scanalatura.

### Note

Questo tutorial utilizza le primitive di Parte e le Operazioni booleane, che consumano molte risorse.
Per fare un script di Part usando degli schizzi rivoluzionati vedere il tutorial [Parti con script: Cuscinetto a sfere - Parte 2 ](Scripted_Parts:_Ball_Bearing_-_Part_2/it.md).

### Link

[Script di oggetti](Scripted_objects/it.md): La pagina wiki che spiega i principi fondamentali di scripting
[Script di dati topologici](Topological_data_scripting/it.md): Un tutorial per fornire le basi di scripting
[Parti con script - Cuscinetto a sfere Parte 2](Scripted_Parts:_Ball_Bearing_-_Part_2/it.md): Costruirlo con degli schizzi
[Bearing Script 1](http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html): Base per questo tutorial, grazie a JMG \...

### Codice


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
