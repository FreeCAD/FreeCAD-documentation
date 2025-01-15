---
 TutorialInfo:l
   Topic:  Skrypty części: Łożysko kulkowe - część 1
   Level:  Początkujący
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files:  nie dołączono
}}

### Wprowadzenie

Ten poradnik ma na celu wprowadzenie początkujących użytkowników w tworzenie części za pomocą skryptów Python w programie FreeCAD.
Ten samouczek będzie omawiał, jak zbudować łożysko kulkowe przy użyciu metody CSG.
Kod wygeneruje nowy dokument FreeCAD zawierający 12 kształtów **.
Będzie to wyglądać tak:
!{width="400"}

### Przebieg pracy 

Przebieg pracy jest mniej więcej identyczny z tym, jak tworzyłbyś część w środowisku pracy Część.
Tylko kilka małych różnic.
\* Utwórz nowy pusty dokument i ustaw go jako aktywny dokument.

-   Wstaw Walec.
-   Wstaw Walec.
-   Wykonaj operację logiczną - wycięcia, aby uzyskać podstawowy kształt wewnętrznej obręczy.
-   Wybierz wszystkie krawędzie i zastosuj filet.
-   Wstaw torus.
-   Przesuń torus w odpowiednie miejsce i wykonaj operację logiczną wycięcia, aby utworzyć rowek na kule.
-   Powtórz wszystkie kroki, aby uzyskać kształt zewnętrznej obręczy.
-   Wstaw pierwszą kulę.
-   Wstaw inne kule, używając matematyki do obliczenia pozycji kul.
-   Ustaw widok na izometryczny.
-   Przybliż, aby zmieścić wszystko.

### Zaokrąglanie krawędzi 

W warsztacie częściowym, korzystając z interfejsu graficznego, wybierasz skosy w widoku 3D lub w menu dla zaokrągleń, a następnie stosujesz zaokrąglenia.
Tutaj wybieramy wszystkie krawędzie kształtu i stosujemy zaokrąglenia.
Dlatego musimy wybrać krawędzie PRZED utworzeniem rowka.

### Uwagi

Ten poradnik wykorzystuje elementy pierwotne części i operacje logiczne, co może być wymagające dla wydajności.
Aby wykonać zeszkolony fragment z przekręconymi szkicami, przejrzyj samouczek Skrypty części: Łożysko kulkowe - część 2.

### Odnośniki internetowe 

Obiekty tworzone skryptami: Strona Wiki wyjaśniająca podstawy tworzenia skryptów
Skrypty danych topologicznych: Samouczek odsłaniający podstawy tworzenia skryptów
Skrypty części: Łożysko kulkowe - część 2: Wykonanie za pomocą szkiców
Bearing Script 1: Baza dla tego poradnika, podziękowania dla JMG \...

### Kod


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

# Scripted Parts: Ball Bearing - Part 1/pl

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted Parts: Ball Bearing - Part 1/pl
