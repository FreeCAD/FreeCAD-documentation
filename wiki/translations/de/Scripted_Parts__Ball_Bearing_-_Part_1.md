---
- TutorialInfo:/de
   Topic: Part Scripting - Ball Bearing #1
   Level: Beginner
   Time: 30 min
   Author:r-frank
   FCVersion:0.16.6706
   Files:
}}

### Einleitung

Dieses Tutorial ist gedacht als Einführung wie man Modelle erstellt mit Hilfe von Python Skripten innerhalb von FreeCAD.
Dieses Tutorial erklärt wie man ein Kugellager erstellt mittels eines CSG-Arbeitsablaufes.
Der Code wird ein neues FreeCAD-Dokument erstellen mit 12 einzelnen Körpern (Innerer Ring, äußerer Ring und 10 Kugeln).
Das Ergebnis sieht so aus:
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

### Arbeitsablauf

Der Arbeitsablauf ist mehr oder weniger identisch mit dem Ablauf, mit dem Sie ein Modell im Arbeitsbereich \"Part\" erstellen würden.
Es gibt nur wenige Unterschiede.
\*Erstelle ein neues leeres Dokument und mache es zum aktiven Dokument

-   Einfügen eines Zylinders
-   Einfügen eines Zylinders
-   Durchführung einer boolschen Verschneidung um die grundlegende Form des inneren Ringes zu bekommen
-   Alle Kanten auswählen und einen Radius anbringen
-   Einfügen eines Torus
-   Bewege den Torus in die korrekte Position und führe eine boolsche Verschneidung durch um die Rille für die Kugeln zu bekommen
-   Wiederhole alle Schritte um den äußeren Ring zu erstellen
-   Einfügel der ersten Kugel
-   Einfügen der restlichen Kugeln und benutzen von Formeln um die korrekten Positionen der Kugeln zu berechnen
-   Wechsle in die axometrische Ansicht
-   Zoom auf Alles

### Kanten verrunden 

Im Arbeitsbereich Part würde man mittels Benutzeroberfläche die Kanten in der 3D-Ansicht markieren und dann die Radien anbringen.
Hier wählen wir alle Kanten eines Körpers aus und bringen die Radien an.
Deshalb müssen wir die Kanten auswählen BEVOR wir die Rille für die Kugeln herstellen.

### Bemerkungen

Dieses Tutorial benutzt Grundkörper und boolsche Operationen, welche sehr rechenintensiv sein können.
Um zu sehen, wie man einen Körper mittels rotierten Skizzen erstellt, werfen Sie bitte einen Blick auf das Tutorial [Scripted Parts: Ball Bearing - Part 2/de](Scripted_Parts:_Ball_Bearing_-_Part_2/de.md).

### Links

[Scripted objects](Scripted_objects.md): Diese Wiki-Seite erklärt die Grundlagen für part scripting
[Topological data scripting](Topological_data_scripting.md): Ein Tutorial für die Grundlagen des part scriptings
[Scripted Parts: Ball Bearing - Part 2](Scripted_Parts:_Ball_Bearing_-_Part_2.md): Erstellen des Modelles mittels Skizzen
[Bearing Script 1](http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html): Basis für dieses Tutorial, vielen Dank an JMG \...

### Code


{{Code   code:
## Ball-bearing Skript
## 11.08.2016 von r-frank (BPLRFE/LearnFreeCAD on Youtube)
## basierend auf dem ball bearing script by JMG
## (http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html)
#
#um Grundkoerper einzufuegen
import Part
#um die Position der Kugeln berechnen zu koennen
import math
#zum Bewegen des Torus
from FreeCAD import Base
#
#Werte#
#(Radius des Schaftes/innerer Radius des inneren Ringes)
R1=15.0
#(Aussenradius des Innenringes)
R2=25.0
#(Innenradius des Aussenringes)
R3=30.0
#(Aussenradius des Aussenringes)
R4=40.0
#(Dicke des Lagers)
TH=15.0
#(Anzahl der Kugeln)
NBall=10
#(Radius der Kugeln)
RBall=5.0
#(Verrundungs-Radius)
RR=1
#Erste Koordinate des Zentrums der Kugel
CBall=((R3-R2)/2)+R2
#Zweite Koordinate des Zentrums der Kugel
PBall=TH/2
#
#Erstelle neues Dokument
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
#
#Innerer Ring#
B1=Part.makeCylinder(R1,TH)
B2=Part.makeCylinder(R2,TH)
IR=B2.cut(B1)
#Kanten auswaehlen und Radius anbringen
Bedges=IR.Edges
IRF=IR.makeFillet(RR,Bedges)
#Rille erstellen und Koerper einblenden
T1=Part.makeTorus(CBall,RBall)
T1.translate(Base.Vector(0,0,TH/2))
InnerRing=IRF.cut(T1)
Part.show(InnerRing)
#
#Aeusserer Ring#
B3=Part.makeCylinder(R3,TH)
B4=Part.makeCylinder(R4,TH)
OR=B4.cut(B3)
#Kanten auswaehlen und Radius anbringen
Bedges=OR.Edges
ORF=OR.makeFillet(RR,Bedges)
#Rille erstellen und Koerper einblenden
T2=Part.makeTorus(CBall,RBall)
T2.translate(Base.Vector(0,0,TH/2))
OuterRing=ORF.cut(T2)
Part.show(OuterRing)
#
#Kugeln#
for i in range(NBall):
  Ball=Part.makeSphere(RBall)
  Alpha=(i*2*math.pi)/NBall
  BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),TH/2)
  Ball.translate(BV)
  Part.show(Ball)
#
#Und das Ganze noch huebsch machen ...#
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
---

# Scripted Parts: Ball Bearing - Part 1/de

 

{{Powerdocnavi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 1/de
