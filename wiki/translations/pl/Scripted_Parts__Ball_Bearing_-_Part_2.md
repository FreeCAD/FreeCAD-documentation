---
 TutorialInfo:l
   Topic:  Skrypty części: Łożysko kulkowe - część 2
   Level:  Początkujący
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files:  nie dołączono
}}

### Wprowadzenie

Ten poradnik ma na celu wprowadzenie początkujących użytkowników w tworzenie części za pomocą skryptów Python w programie FreeCAD.
Ten samouczek będzie omawiał, jak zbudować łożysko kulkowe przy użyciu szkiców i ich wyciągnięcia przez obrót.
Kod wygeneruje nowy dokument FreeCAD zawierający 12 kształtów **.
Będzie to wyglądać tak:
!{width="400"}

### Przebieg pracy 

Przebieg pracy jest mniej więcej identyczny z tym, jak tworzyłbyś część w środowisku projektowania Część.
Istnieje tylko kilka drobnych różnic.
\*Utwórz nowy pusty dokument i ustaw go jako aktywny dokument

-   Narysuj podstawowy kształt zewnętrznego pierścienia składający się z czterech prostych linii i czterech łuków

!{width="150"}

-   Połącz linie i łuki, a następnie zaktualizuj je do jednego ciągu.
-   Zaktualizuj ciąg do powierzchni.
-   Obróć powierzchnię, aby uzyskać kształt.
-   Narysuj koło.
-   Zaktualizuj koło do ciągu.
-   Zaktualizuj ciąg do powierzchni.
-   Obróć powierzchnię i zastosuj odcięcie funkcją logiczną, aby uzyskać rowek w zewnętrznym pierścieniu.
-   Narysuj podstawowy kształt wewnętrznego pierścienia składający się z czterech prostych linii i czterech łuków.
-   Połącz linie i łuki, a następnie zaktualizuj je do jednej polilinii.
-   Zaktualizuj ciąg do powierzchni.
-   Obróć powierzchnię, aby uzyskać kształt.
-   Narysuj koło.
-   Zaktualizuj koło do ciągu.
-   Zaktualizuj ciąg do powierzchni.
-   Obróć powierzchnię i zastosuj odcięcie funkcją logiczną, aby uzyskać rowek wewnętrznym pierścieniu.
-   Wstaw kule tak samo jak w części 1 **
-   Ustaw widok na aksometryczny.
-   Powiększ, aby wszystko zmieściło się na ekranie.

### Tworzenie rowka 

Narysowanie łuku wymaga podania trzech punktów lub kąta początkowego i końcowego.
W narzędziu do rysowania będziemy korzystać z wiązań, aby zdefiniować punkt początkowy i punkt końcowy łuku.
Ponieważ nie możemy tego zrobić w skrypcie, narysujemy zaokrąglony prostokąt i dokonamy jego obrotu, aby uzyskać podstawowy \"kształt pierścienia\".
Następnie narysujemy okrąg i dokonamy jego obrotu, aby uzyskać geometrię rowka.
Następnie zastosujemy odcięcie operacją logiczną do dwóch obrotowych kształtów i uzyskamy kompletny kształt wewnętrznego / zewnętrznego pierścienia.

### Wstawianie kul 

Prawidłowy sposób wstawiania kul przy użyciu narzędzia do rysowania byłby następujący:
\*Narysuj łuk ** z ośrodkiem identycznym z początkiem układu współrzędnych i narysuj linię zamykającą \"otwartą\" stronę łuku.

-   Przekształć oba elementy w polilinię, podnieś do postaci twarzy, obróć wokół osi z, aby uzyskać kształt kuli.
-   Użyj polecenia \"przesuń\", aby przenieść kulę w odpowiednie miejsce.
-   Powtórz powyższe kroki dziewięć razy, wykorzystując funkcję matematyczną do tworzenia i pozycjonowania kolejnych kul.
-   Tę operację powtarzania można zaprogramować za pomocą pętli.

Jednakże ten sposób nie jest efektywny, wstawianie podstawowych kształtów i ich pozycjonowanie jest łatwiejsze i szybsze w tym przypadku.
Więc używamy tego samego sposobu co w \"Skrypty części: Łożysko kulkowe - część 1\".

### Odnośniki internetowe 

Obiekty tworzone skryptami: Strona Wiki wyjaśniająca podstawy tworzenia skryptów
Skrypty danych topologicznych: Poradnik odsłaniający podstawy tworzenia skryptów
Skrypty części: Łożysko kulkowe - część 1: Wykonanie za pomocą szkiców
Łożyska ze szkiców tworzonych skryptami: Baza dla tego poradnika, podziękowania dla JMG \...

### Kod


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

# Scripted Parts: Ball Bearing - Part 2/pl

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 2/pl
