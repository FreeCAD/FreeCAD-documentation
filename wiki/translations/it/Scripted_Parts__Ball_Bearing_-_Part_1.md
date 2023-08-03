---
 TutorialInfo:t
   Topic:  Parti con script - Cuscinetto a sfere #1
   Level:  Base
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Introduzione

Questo tutorial si propone di introdurre i principianti alla creazione di parti con script python all\'interno di FreeCAD.
Questo tutorial descrive come costruire un cuscinetto a sfere con un flusso di lavoro CSG.
Il codice produrrà un nuovo documento di FreeCAD con 12 forme .
Esso sarà simile a questo:
!{width="400"}

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
Per fare un script di Part usando degli schizzi rivoluzionati vedere il tutorial Parti con script: Cuscinetto a sfere - Parte 2 .

### Link

Script di oggetti: La pagina wiki che spiega i principi fondamentali di scripting
Script di dati topologici: Un tutorial per fornire le basi di scripting
Parti con script - Cuscinetto a sfere Parte 2: Costruirlo con degli schizzi
Bearing Script 1: Base per questo tutorial, grazie a JMG \...

### Codice


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

# Scripted Parts: Ball Bearing - Part 1/it

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 1/it
