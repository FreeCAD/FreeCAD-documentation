---
 TutorialInfo:e
   Topic:  Part Scripting - Ball Bearing #1
   Level:  Beginner
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Einleitung

Dieses Tutorial ist gedacht als Einführung wie man Modelle erstellt mit Hilfe von Python Skripten innerhalb von FreeCAD.
Dieses Tutorial erklärt wie man ein Kugellager erstellt mittels eines CSG-Arbeitsablaufes.
Der Code wird ein neues FreeCAD-Dokument erstellen mit 12 einzelnen Körpern .
Das Ergebnis sieht so aus:
!{width="400"}

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
Um zu sehen, wie man einen Körper mittels rotierten Skizzen erstellt, werfen Sie bitte einen Blick auf das Tutorial Scripted Parts: Ball Bearing - Part 2/de.

### Links

Scripted objects: Diese Wiki-Seite erklärt die Grundlagen für part scripting
Topological data scripting: Ein Tutorial für die Grundlagen des part scriptings
Scripted Parts: Ball Bearing - Part 2: Erstellen des Modelles mittels Skizzen
Bearing Script 1: Basis für dieses Tutorial, vielen Dank an JMG \...

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
App.ActiveDocument=App.getDocument
Gui.ActiveDocument=Gui.getDocument
#
#Innerer Ring#
B1=Part.makeCylinder
B2=Part.makeCylinder
IR=B2.cut
#Kanten auswaehlen und Radius anbringen
Bedges=IR.Edges
IRF=IR.makeFillet
#Rille erstellen und Koerper einblenden
T1=Part.makeTorus
T1.translate)
InnerRing=IRF.cut
Part.show
#
#Aeusserer Ring#
B3=Part.makeCylinder
B4=Part.makeCylinder
OR=B4.cut
#Kanten auswaehlen und Radius anbringen
Bedges=OR.Edges
ORF=OR.makeFillet
#Rille erstellen und Koerper einblenden
T2=Part.makeTorus
T2.translate)
OuterRing=ORF.cut
Part.show
#
#Kugeln#
for i in range:
  Ball=Part.makeSphere
  Alpha=/NBall
  BV=,CBall*math.sin,TH/2)
  Ball.translate
  Part.show
#
#Und das Ganze noch huebsch machen ...#
App.activeDocument.recompute
Gui.activeDocument.activeView.viewAxometric
Gui.SendMsgToActiveView
---

# Scripted Parts: Ball Bearing - Part 1/de

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted Parts: Ball Bearing - Part 1/de
