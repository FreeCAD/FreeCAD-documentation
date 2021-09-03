 {{TutorialInfo/de
|Topic= Part Scripting - Ball Bearing #2
|Level= Beginner
|Time= 30 min
|Author=r-frank
|FCVersion=0.16.6706
|Files=
}}

### Einleitung

Dieses Tutorial ist gedacht als Einführung wie man Modelle erstellt mit Hilfe von Python Skripten innerhalb von FreeCAD.
Dieses Tutorial erklärt wie man ein Kugellager erstellt mittels Sizzen, die dann rotiert werden.
Der Code wird ein neues FreeCAD-Dokument erstellen mit 12 einzelnen Körpern (Innerer Ring, äußerer Ring und 10 Kugeln).
Das Ergebnis sieht so aus:
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

### Arbeitsablauf

Der Arbeitsablauf ist mehr oder weniger identisch mit dem Ablauf, mit dem Sie ein Modell im Arbeitsbereich \"Part Design\" erstellen würden.
Es gibt nur wenige Unterschiede.
\*Erstelle ein neues leeres Dokument und mache es zum aktiven Dokument

-   Zeichne die grundlegende Figur des äußeren Ringes bestehend aus vier Linien und vier Kreisbögen.

<img alt="" src=images/TutorialBallBearing_P2-Sketch.png  style="width:150px;">

-   Verbinde die Elemente und upgrade Sie zu einem Draht (wire)
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche um einen Rotationskörper zu erhalten
-   Zeichne einen Kreis
-   Upgrade des Kreises zu einem Draht (wire)
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche und Hinzufügen einer boolschen Verschneidung um die Rille des äußeren Ringes zu erhalten
-   Zeichne die grundlegende Figur des inneren Ringes bestehend aus vier Linien und vier Kreisbögen.
-   Verbinde die Elemente und upgrade Sie zu einem Draht (wire)
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche um einen Rotationskörper zu erhalten
-   Zeichne einen Kreis
-   Upgrade des Kreises zu einem Draht (wire)
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche und Hinzufügen einer boolschen Verschneidung um die Rille des inneren Ringes zu erhalten
-   Einfügen der Kugeln auf dieselbe Art wie in Teil 1 (wegen der Effektivität)
-   Wechsle in die axometrische Ansicht
-   Zoom auf Alles

### Erstellen der Rille {#erstellen_der_rille}

Das Zeichnen eines Kreibogen benötigt entweder drei Punkte oder eine Startwinkel und einen Endwinkel.
Im Sketcher würden wir Beschränkungen verwenden um den Startpunkt und den Endpunkt des Kreisbogens zu bestimmen.
Da wir dies in scripting nicht möglich ist, werden wir ein abgerundetes Rechteck zeichnen und es rotieren lassen, um einen Basis-Ring zu erhalten.
Dann zeichnen wir eine Kreis und rotieren ihn, um die Geometrie der Rille zu erhalten.
Dann fügen wir eine boolsche Verschneidung hinzu und wir haben die komplette Form des inneren/äußeren Ringes.

### Einfügen der Kugeln {#einfügen_der_kugeln}

Der korrekte skizzen-basierende Ablauf um die Kugeln einzufügen wäre wie folgt:
\*Zeichne einen Halbkreis mit dem Zentrum im Nullpunkt und zeichne eine Linie, die die offene Seite des Halbkreises schließt.

-   Wandle die zwei Elemente in einen Draht (wire) um, upgrade zur Fläche und rotiere um die Z-Achse, um eine Kugel zu erhalten
-   Dann mit dem \"translate\"-Befehl die Kugel in die korrekte Position bringen
-   Die obigen Schritte neun mal wiederholen und mittels Formel die korrekte Positon der Kugel ermittlen
-   Diese Operation kann mittels einer Schelife programmiert werden

Dies ist nicht sehr effektiv, es ist der schnellere Weg, Grundkörper einzufügen und diese zu positionieren
Also benutzen wir dieselbe Methode wie in Teil 1.


<div class="mw-translate-fuzzy">

### Links

[Scripted objects](Scripted_objects.md): Diese Wiki-Seite erklärt die Grundlagen für part scripting
[Topological data scripting](Topological_data_scripting.md): Ein Tutorial für die Grundlagen des part scriptings
[Scripted Parts: Ball Bearing - Part 1/de](Scripted_Parts:_Ball_Bearing_-_Part_1/de.md): Erstellen des Modelles mittels Grundkörpern
[Bearings from scripted sketches](http://linuxforanengineer.blogspot.de/2013/12/bearings-from-scripted-sketches.html): Basis für dieses Tutorial, vielen Dank an JMG \...


</div>


<div class="mw-translate-fuzzy">

### Code


```python
## Ball-bearing Skript
## 11.08.2016 von r-frank (BPLRFE/LearnFreeCAD on Youtube)
## basierend auf dem ball bearing script by JMG
## (http://linuxforanengineer.blogspot.de/2013/12/bearings-from-scripted-sketches.html)
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
#Linien fuer die Grundform des aeusseren Ringes
L1o=Part.makeLine((R4,0,TH-RR),(R4,0,RR))
L2o=Part.makeLine((R4-RR,0,0),(R3+RR,0,0))
L3o=Part.makeLine((R3,0,RR),(R3,0,TH-RR))
L4o=Part.makeLine((R3+RR,0,TH),(R4-RR,0,TH))
#Ecken abrunden
A1o=Part.makeCircle(RR,Base.Vector(R4-RR,0,RR),Base.Vector(0,1,0),0,90)
A2o=Part.makeCircle(RR,Base.Vector(R3+RR,0,RR),Base.Vector(0,1,0),90,180)
A3o=Part.makeCircle(RR,Base.Vector(R3+RR,0,TH-RR),Base.Vector(0,1,0),180,270)
A4o=Part.makeCircle(RR,Base.Vector(R4-RR,0,TH-RR),Base.Vector(0,1,0),270,360)
#Verbinden der Elemente, Upgrade, Revolve und Cut fuer aeusseren Ring
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
#Linien fuer die Grundform des inneren Ringes
L1i=Part.makeLine((R2,0,TH-RR),(R2,0,RR))
L2i=Part.makeLine((R2-RR,0,0),(R1+RR,0,0))
L3i=Part.makeLine((R1,0,RR),(R1,0,TH-RR))
L4i=Part.makeLine((R1+RR,0,TH),(R2-RR,0,TH))
#Ecken abrunden
A1i=Part.makeCircle(RR,Base.Vector(R2-RR,0,RR),Base.Vector(0,1,0),0,90)
A2i=Part.makeCircle(RR,Base.Vector(R1+RR,0,RR),Base.Vector(0,1,0),90,180)
A3i=Part.makeCircle(RR,Base.Vector(R1+RR,0,TH-RR),Base.Vector(0,1,0),180,270)
A4i=Part.makeCircle(RR,Base.Vector(R2-RR,0,TH-RR),Base.Vector(0,1,0),270,360)
#Verbinden der Elemente, Upgrade, Revolve und Cut fuer inneren Ring
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
#Kugeln einfuegen#
for i in range(NBall):
  Ball=Part.makeSphere(RBall)
  Alpha=(i*2*math.pi)/NBall
  BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),TH/2)
  Ball.translate(BV)
  Part.show(Ball)
#
#Alles huebsch machen ...#
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```


</div>


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
