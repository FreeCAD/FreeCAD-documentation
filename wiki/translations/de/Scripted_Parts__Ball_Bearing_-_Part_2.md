---
 TutorialInfo:e
   Topic:  Part Scripting - Ball Bearing #2
   Level:  Beginner
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Einleitung

Dieses Tutorial ist gedacht als Einführung wie man Modelle erstellt mit Hilfe von Python Skripten innerhalb von FreeCAD.
Dieses Tutorial erklärt wie man ein Kugellager erstellt mittels Sizzen, die dann rotiert werden.
Der Code wird ein neues FreeCAD-Dokument erstellen mit 12 einzelnen Körpern .
Das Ergebnis sieht so aus:
!{width="400"}

### Arbeitsablauf

Der Arbeitsablauf ist mehr oder weniger identisch mit dem Ablauf, mit dem Sie ein Modell im Arbeitsbereich \"Part Design\" erstellen würden.
Es gibt nur wenige Unterschiede.
\*Erstelle ein neues leeres Dokument und mache es zum aktiven Dokument

-   Zeichne die grundlegende Figur des äußeren Ringes bestehend aus vier Linien und vier Kreisbögen.

!{width="150"}

-   Verbinde die Elemente und upgrade Sie zu einem Draht 
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche um einen Rotationskörper zu erhalten
-   Zeichne einen Kreis
-   Upgrade des Kreises zu einem Draht 
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche und Hinzufügen einer boolschen Verschneidung um die Rille des äußeren Ringes zu erhalten
-   Zeichne die grundlegende Figur des inneren Ringes bestehend aus vier Linien und vier Kreisbögen.
-   Verbinde die Elemente und upgrade Sie zu einem Draht 
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche um einen Rotationskörper zu erhalten
-   Zeichne einen Kreis
-   Upgrade des Kreises zu einem Draht 
-   Upgrade des wires zu einer Fläche
-   Rotieren der Fläche und Hinzufügen einer boolschen Verschneidung um die Rille des inneren Ringes zu erhalten
-   Einfügen der Kugeln auf dieselbe Art wie in Teil 1 
-   Wechsle in die axometrische Ansicht
-   Zoom auf Alles

### Erstellen der Rille 

Das Zeichnen eines Kreibogen benötigt entweder drei Punkte oder eine Startwinkel und einen Endwinkel.
Im Sketcher würden wir Beschränkungen verwenden um den Startpunkt und den Endpunkt des Kreisbogens zu bestimmen.
Da wir dies in scripting nicht möglich ist, werden wir ein abgerundetes Rechteck zeichnen und es rotieren lassen, um einen Basis-Ring zu erhalten.
Dann zeichnen wir eine Kreis und rotieren ihn, um die Geometrie der Rille zu erhalten.
Dann fügen wir eine boolsche Verschneidung hinzu und wir haben die komplette Form des inneren/äußeren Ringes.

### Einfügen der Kugeln 

Der korrekte skizzen-basierende Ablauf um die Kugeln einzufügen wäre wie folgt:
\*Zeichne einen Halbkreis mit dem Zentrum im Nullpunkt und zeichne eine Linie, die die offene Seite des Halbkreises schließt.

-   Wandle die zwei Elemente in einen Draht  um, upgrade zur Fläche und rotiere um die Z-Achse, um eine Kugel zu erhalten
-   Dann mit dem \"translate\"-Befehl die Kugel in die korrekte Position bringen
-   Die obigen Schritte neun mal wiederholen und mittels Formel die korrekte Positon der Kugel ermittlen
-   Diese Operation kann mittels einer Schelife programmiert werden

Dies ist nicht sehr effektiv, es ist der schnellere Weg, Grundkörper einzufügen und diese zu positionieren
Also benutzen wir dieselbe Methode wie in Teil 1.

### Links

Skriptgenerierte Objekte: Diese Wiki-Seite erklärt die Grundlagen für part scripting
Topologisches Datenskripten: Ein Tutorial für die Grundlagen des part scriptings
Skriptgenerierte Teile: Kugellager - Teil 1: Erstellen des Modelles mittels Grundkörpern
Bearings from scripted sketches: Basis für dieses Tutorial, vielen Dank an JMG \...

### Code


{{Code   code: 
## Ball-bearing Skript
## 11.08.2016 von r-frank 
## basierend auf dem ball bearing script by JMG
## 
#
#um Grundkoerper einzufuegen
import Part
#um die Position der Kugeln berechnen zu koennen
import math
#zum Bewegen des Torus
from FreeCAD import Base
#
#Werte#
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
#Erste Koordinate des Zentrums der Kugel
CBall=/2)+R2
#Zweite Koordinate des Zentrums der Kugel
PBall=TH/2
#
#Erstelle neues Dokument
App.newDocument
App.setActiveDocument
#
#Linien fuer die Grundform des aeusseren Ringes
L1o=Part.makeLine,)
L2o=Part.makeLine,)
L3o=Part.makeLine,)
L4o=Part.makeLine,)
#Ecken abrunden
A1o=Part.makeCircle,Base.Vector,0,90)
A2o=Part.makeCircle,Base.Vector,90,180)
A3o=Part.makeCircle,Base.Vector,180,270)
A4o=Part.makeCircle,Base.Vector,270,360)
#Verbinden der Elemente, Upgrade, Revolve und Cut fuer aeusseren Ring
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
#Linien fuer die Grundform des inneren Ringes
L1i=Part.makeLine,)
L2i=Part.makeLine,)
L3i=Part.makeLine,)
L4i=Part.makeLine,)
#Ecken abrunden
A1i=Part.makeCircle,Base.Vector,0,90)
A2i=Part.makeCircle,Base.Vector,90,180)
A3i=Part.makeCircle,Base.Vector,180,270)
A4i=Part.makeCircle,Base.Vector,270,360)
#Verbinden der Elemente, Upgrade, Revolve und Cut fuer inneren Ring
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
#Kugeln einfuegen#
for i in range:
  Ball=Part.makeSphere
  Alpha=/NBall
  BV=,CBall*math.sin,TH/2)
  Ball.translate
  Part.show
#
#Alles huebsch machen ...#
App.ActiveDocument.recompute
Gui.ActiveDocument.ActiveView.viewAxometric
Gui.SendMsgToActiveView
---

# Scripted Parts: Ball Bearing - Part 2/de

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 2/de
