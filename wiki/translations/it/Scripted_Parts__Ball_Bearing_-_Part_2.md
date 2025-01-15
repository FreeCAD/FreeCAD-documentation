---
 TutorialInfo:t
   Topic:  Parti con script - Cuscinetto a sfere - #2
   Level:  Base
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Introduzione

Questo tutorial si propone di introdurre i principianti alla creazione di parti con script python all\'interno di FreeCAD.
Questo tutorial descrive come costruire un cuscinetto a sfere con un flusso di lavoro che consiste nel creare degli schizzi e rivoluzionarli.
Il codice produrrà un nuovo documento di FreeCAD con 12 forme .
Esso sarà simile a questo:
!{width="400"}

### Flusso di lavoro 

Il flusso di lavoro è quasi identico a quello che si dovrebbe usare per creare la parte nell\'ambiente PartDesign. Solo alcune piccole differenze.

-   Creare un nuovo documento vuoto e renderlo attivo
-   Disegnare la forma di base dell\'anello esterno composta da quattro segmenti e quattro archi

!{width="150"}

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
-   Inserire le sfere con lo stesso flusso di lavoro usato nella parte 1 del tutorial 
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
\*Disegnare un arco  con il centro coincidente con l\'origine e tracciare una linea di chiusura del lato \"aperto\" dell\'arco

-   Convertire i due elementi ad un wire, promuoverli in una faccia, ruotare la faccia attorno all\'asse z per ottenere la forma di una sfera
-   Utilizzare il comando *Muovi* per spostare la sfera nella posizione corretta
-   Ripetere i passaggi precedenti nove volte coinvolgendo la funzione math per creare e posizionare le altre sfere
-   Questa operazione di ripetizione può essere programmata con un loop

In questo caso, questo non è efficace, inserire delle primitive e posizionarle è più facile e veloce.
Quindi usiamo lo stesso metodo usato in Parti con script: Cuscinetto a sfere - Parte 1.

### Link

Script di oggetti: La pagina wiki che spiega i principi fondamentali di scripting
Script di dati topologici: Un tutorial per fornire le basi di scripting
Parti con script: Cuscinetto a sfere - Parte 1: Costruirlo con primitive di Parte
Bearings from scripted sketches: Base per questo tutorial, grazie a JMG \...

### Codice


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

# Scripted Parts: Ball Bearing - Part 2/it

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted Parts: Ball Bearing - Part 2/it
