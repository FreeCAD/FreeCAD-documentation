---
- TutorialInfo:/it
   Topic: Parti con script - Cuscinetto a sfere - #2
   Level: Base
   Time: 30 min
   Author:r-frank
   FCVersion:0.16.6706
   Files:
}}

### Introduzione

Questo tutorial si propone di introdurre i principianti alla creazione di parti con script python all\'interno di FreeCAD.
Questo tutorial descrive come costruire un cuscinetto a sfere con un flusso di lavoro che consiste nel creare degli schizzi e rivoluzionarli.
Il codice produrrà un nuovo documento di FreeCAD con 12 forme (anello interno, anello esterno e 10 sfere).
Esso sarà simile a questo:
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

### Flusso di lavoro 

Il flusso di lavoro è quasi identico a quello che si dovrebbe usare per creare la parte nell\'ambiente PartDesign. Solo alcune piccole differenze.

-   Creare un nuovo documento vuoto e renderlo attivo
-   Disegnare la forma di base dell\'anello esterno composta da quattro segmenti e quattro archi

<img alt="" src=images/TutorialBallBearing_P2-Sketch.png  style="width:150px;">

-   Collegare le linee e gli archi e promuoverli in un unico contorno
-   Promuovere il contorno in una faccia
-   Rivoluzionare la faccia per ottenere una forma
-   Disegnare un cerchio
-   Promuovere il cerchio in un contorno
-   Promuovere il contorno in una faccia
-   Rivoluzionare la faccia e applicare un taglio booleano per ottenere la scanalatura dell\'anello esterno
-   Disegnare la forma di base dell\'anello interno composta da quattro segmenti e quattro archi
-   Collegare le linee e gli archi e promuoverli in un unico contorno
-   Promuovere il contorno in una faccia
-   Rivoluzionare la faccia per ottenere una forma
-   Disegnare un cerchio
-   Promuovere il cerchio in un contorno
-   Promuovere il contorno in una faccia
-   Rivoluzionare la faccia e applicare un taglio booleano per ottenere la scanalatura dell\'anello interno
-   Inserire le sfere con lo stesso flusso di lavoro usato nella parte 1 del tutorial (dato che è efficace)
-   Impostare la vista assonometrica
-   Zoom per adattare la vista alla finestra

### Creare la scanalatura 

Per disegnare un arco servono tre punti o un angolo iniziale ed un angolo finale.
In uno schizzo si potrebbero usare i vincoli per definire il punto iniziale e il punto finale dell\'arco.
Dato che in uno script questo non è possibile, si disegna un rettangolo arrotondato e lo si rivoluziona per ottenere la forma di base dell\'anello.
Poi si disegna un cerchio e lo si ruota per ottenere la geometria della scanalatura.
Infine si applica un taglio booleano tra le due forme rivoluzionate e per ottenere la forma completa dell\'anello interno e di quello esterno.

### Inserire le sfere 

Il corretto flusso di lavoro basato su Sketcher per inserire le sfere sarebbe:
\*Disegnare un arco (semicerchio) con il centro coincidente con l\'origine e tracciare una linea di chiusura del lato \"aperto\" dell\'arco

-   Convertire i due elementi ad un wire, promuoverli in una faccia, ruotare la faccia attorno all\'asse z per ottenere la forma di una sfera
-   Utilizzare il comando *Muovi* per spostare la sfera nella posizione corretta
-   Ripetere i passaggi precedenti nove volte coinvolgendo la funzione math per creare e posizionare le altre sfere
-   Questa operazione di ripetizione può essere programmata con un loop

In questo caso, questo non è efficace, inserire delle primitive e posizionarle è più facile e veloce.
Quindi usiamo lo stesso metodo usato in [Parti con script: Cuscinetto a sfere - Parte 1](Scripted_Parts:_Ball_Bearing_-_Part_1/it.md).

### Link

[Script di oggetti](Scripted_objects/it.md): La pagina wiki che spiega i principi fondamentali di scripting
[Script di dati topologici](Topological_data_scripting/it.md): Un tutorial per fornire le basi di scripting
[Parti con script: Cuscinetto a sfere - Parte 1](Scripted_Parts:_Ball_Bearing_-_Part_1/it.md): Costruirlo con primitive di Parte
[Bearings from scripted sketches](http://linuxforanengineer.blogspot.de/2013/12/bearings-from-scripted-sketches.html): Base per questo tutorial, grazie a JMG \...

### Codice


{{Code   code:
## Ball-bearing script
## 11.08.2016 by r-frank (BPLRFE/LearnFreeCAD on Youtube)
## based on ball bearing script by JMG
## (http://linuxforanengineer.blogspot.de/2013/12/bearings-from-scripted-sketches.html)
#
#needed for doing boolean operations
import Part
#needed for calculating the positions of the balls
import math
#needed for translation and rotation of objects
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
#
#Lines for basic shape of outer ring
L1o=Part.makeLine((R4,0,TH-RR),(R4,0,RR))
L2o=Part.makeLine((R4-RR,0,0),(R3+RR,0,0))
L3o=Part.makeLine((R3,0,RR),(R3,0,TH-RR))
L4o=Part.makeLine((R3+RR,0,TH),(R4-RR,0,TH))
#Corner rounding for basic shape of outer ring
A1o=Part.makeCircle(RR,Base.Vector(R4-RR,0,RR),Base.Vector(0,1,0),0,90)
A2o=Part.makeCircle(RR,Base.Vector(R3+RR,0,RR),Base.Vector(0,1,0),90,180)
A3o=Part.makeCircle(RR,Base.Vector(R3+RR,0,TH-RR),Base.Vector(0,1,0),180,270)
A4o=Part.makeCircle(RR,Base.Vector(R4-RR,0,TH-RR),Base.Vector(0,1,0),270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
OR=Part.Wire([L1o,A1o,L2o,A2o,L3o,A3o,L4o,A4o])
OR=Part.Face(OR)
OR=OR.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
C1=Part.makeCircle(RBall,Base.Vector(R2+(R3-R2)/2,0,TH/2),Base.Vector(0,1,0),0,360)
GRo=Part.Wire([C1])
GRo=Part.Face(GRo)
GRo=GRo.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
OR=OR.cut(GRo)
Part.show(OR)
#
#Lines for basic shape of inner ring
L1i=Part.makeLine((R2,0,TH-RR),(R2,0,RR))
L2i=Part.makeLine((R2-RR,0,0),(R1+RR,0,0))
L3i=Part.makeLine((R1,0,RR),(R1,0,TH-RR))
L4i=Part.makeLine((R1+RR,0,TH),(R2-RR,0,TH))
#Corner rounding for basic shape of inner ring
A1i=Part.makeCircle(RR,Base.Vector(R2-RR,0,RR),Base.Vector(0,1,0),0,90)
A2i=Part.makeCircle(RR,Base.Vector(R1+RR,0,RR),Base.Vector(0,1,0),90,180)
A3i=Part.makeCircle(RR,Base.Vector(R1+RR,0,TH-RR),Base.Vector(0,1,0),180,270)
A4i=Part.makeCircle(RR,Base.Vector(R2-RR,0,TH-RR),Base.Vector(0,1,0),270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
IR=Part.Wire([L1i,A1i,L2i,A2i,L3i,A3i,L4i,A4i])
IR=Part.Face(IR)
IR=IR.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
C2=Part.makeCircle(RBall,Base.Vector(R2+(R3-R2)/2,0,TH/2),Base.Vector(0,1,0),0,360)
GRi=Part.Wire([C2])
GRi=Part.Face(GRi)
GRi=GRi.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
IR=IR.cut(GRi)
Part.show(IR)
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
App.ActiveDocument().recompute()
Gui.ActiveDocument.ActiveView.viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
---

# Scripted Parts: Ball Bearing - Part 2/it

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 2/it
