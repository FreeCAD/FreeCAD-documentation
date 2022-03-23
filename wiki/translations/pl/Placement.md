# Placement/pl
## Przegląd

**Umiejscowienie** to sposób w jaki FreeCAD określa położenie i pozycję *(orientację)* obiektu w przestrzeni. Umiejscowienie może być określone w wielu formach i manipulowane poprzez [skrypty](Python_scripting_tutorial#Vectors_and_placements.md), [Edytor właściwości](Property_editor/pl.md) lub wybierając **Edycja → Umiejscowienie...** aby otworzyć [Panel zadań umiejscowienie](Std_Placement/pl.md).

### Dostęp do atrybutu Umiejscowienie 

Atrybuty Umiejscowienia obiektu mogą być dostępne i modyfikowane na 3 sposoby:

![Umiejscowienie w edytorze właściwości](images/PlacementPropertiesv10-800x800.png ) 

![Umiejscowienie w skrypcie jako y/p/r i Macierz i jej [API](images/Placement_API/pl.md).](PlacePyConv10.png ) 

![Panel zadań umiejscowienia](images/PlacementDialogv10.png ) 

## Formy umiejscowienia 

Umiejscowienie jest przechowywane wewnętrznie jako pozycja i obrót (oś obrotu i kąt przekształcone w [quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Chociaż istnieje kilka form określania obrotu, na przykład środek obrotu, jest on używany tylko do wpływania na obliczanie obrotu i nie jest przechowywany do późniejszych operacji. Podobnie, jeśli określona jest oś obrotu o wartości (1,1,1), może ona zostać znormalizowana podczas przechowywania w kwaternionie i pojawić się jako (0.58, 0.58, 0.58) podczas późniejszego przeglądania obiektu.

### Kąt, oś i pozycja 

**Umiejscowienie = \[Kąt, Oś i Pozycja\]**

Pierwsza forma **Umiejscowienia** ustala położenie obiektu w przestrzeni za pomocą Pozycji i opisuje jego orientację jako pojedynczy obrót wokół osi.

**Kąt = r** jest skalarem wskazującym wielkość obrotu obiektu wokół **Osi**. Wprowadzany jako stopnie, ale przechowywany wewnętrznie jako radiany.

**Oś = (ax,ay,az)** jest wektorem opisującym oś obrotu *(patrz uwaga o osi obrotu)*. Przykładami są:

   *(1,0,0)* ==> wokół osi **X**,
   *(0,1,0)* ==> wokół osi **Y**,
   *(0,0,1)* ==> wokół **osi Z**,
   *(0,71,0,71,0)* ==> wokół prostej **y=x**.

Zauważ, że możliwe jest również translacja *(przemieszczanie)* obiektu wzdłuż tej osi obrotu (ruch osiowy) poprzez wpisanie odległości do przemieszczenia w polu {{SpinBox|Osiowo: 0.0mm}} i kliknięcie **Zastosuj osiowo**. \'\'(Jednym ze sposobów wyobrażenia sobie ruchu osiowego jest samolot ze śmigłem obracającym się na dziobie - śmigło obraca się *wokół* osi obrotu, podczas gdy samolot porusza się *wzdłuż* tej samej osi)\'\'. Wartości w wektorze można traktować jako względną wielkość ruchu, który zostanie wykonany w danym kierunku. Na przykład w przypadku y=x *(0,71,0,71,0)* wartość zawarta w polu wyboru osi zostanie zastosowana w równej mierze w kierunkach X i Y, ale w kierunku Z nie nastąpi żaden ruch.

**Pozycja = (x,y,z)** to wektor opisujący punkt, od którego będzie obliczana geometria obiektu *(w efekcie jest to \"lokalny początek\" obiektu)*. Należy zauważyć, że w skryptach do oznaczenia składowej położenia obiektu Placement.Base jest używana wartość Placement.Base. Edytor właściwości nazywa tę wartość **pozycją**, a panel zadań umieszczania - przesunięciem.

### Pozycja i odchylenie, pochylenie oraz obrót 

![Panel zadań umiejscowienia: {{ComboBox|Kąty Eulera}} zaznaczone](images/PlacementDialogv10b.png )  **Umiejscowienie = \[Pozycja, odchylenie, pochylenie, obrót\]**.

Druga forma **Umiejscowienia** określa położenie obiektu w przestrzeni za pomocą **Pozycji** *(tak jak w pierwszej formie)*, ale opisuje jego orientację za pomocą [Kątów odchylenia, pochylenia i obrotu](http://en.wikipedia.org/wiki/Yaw,_pitch,_and_roll). Kąty te są czasem określane jako [kąty Eulera](http://en.wikipedia.org/wiki/Euler_angles) lub kąty Tait-Bryana. Odchylenie, Pochylenie i Obrót to powszechnie używane w lotnictwie określenia orientacji *(lub położenia)* ciała.

**Położenie = (x,y,z)** to wektor opisujący punkt, od którego będzie obliczana geometria obiektu *(w efekcie \"lokalne odniesienie położenia\" obiektu)*.

**Odchylenie-Pochylenie-Obrót = (y,p,r)** to krotka określająca położenie obiektu. Wartości dla y,p,r określają stopnie obrotu wokół każdej z osi z,y,x *(patrz uwaga)*.  
```python
>>> App.getDocument("Sans_nom").Cylinder.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
```

App.Rotation(10,20,30) = Kąt Eulera

**Odchylenie** = 10° *(**Z**)*

**Pochylenie** = 20° *(**Y**)*

**Obrót** = 30° *(**X**)*

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Odchylenie** to obrót wokół **osi Z**, czyli obrót z lewej strony na prawą.
*(Kąt odchylenia jest równy **Psi ψ**)*. 

![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pochylenie** to obrót wokół **osi Y**, czyli do góry i do dołu.
*(Kąt nachylenia jest wartością **Phi φ**)*. 

![](images/Tache_Placement_Roulis_fr_Mini.gif )**Obrót** to obrót wokół osi X, czyli w górę i w dół skrzydła.
*(Kąt obrotu to **Thêta θ**)*. 

### Macierz

**Umiejscowienie = Macierz**

Trzecia forma **Umiejscowienia** opisuje położenie i orientację obiektu za pomocą macierzy transformacji afinicznej 4x4 *([Affine Transformation](http://en.wikipedia.org/wiki/Affine_transformation))*.

**Macierz** =

  ((r11,r12,r13,t1),
   (r21,r22,r23,t2),
   (r31,r32,r33,t3),
   (0,0,0,1)) , gdzie r*ij* określa obrót, a t*i* - przesunięcie. 




## Okno dialogowe umiejscowienia 

Okno dialogowe Umiejscowienia jest wywoływane z menu **Edycja**. Służy ono do precyzyjnego obracania / przesuwania obiektów. Jest ono również używane, gdy chcemy utworzyć szkic na \"niestandardowej\" płaszczyźnie lub zmienić orientację szkicu na nową płaszczyznę.

Sekcja **Przesunięcie** dostosowuje położenie obiektu w przestrzeni. Sekcja **Środek** dostosowuje oś obrotu do takiej, która nie przechodzi przez punkt odniesienia obiektu. W sekcji **Obrót** dostosowuje się kąt*(y)* obrotu oraz metodę określania tych kątów.

Chociaż elementy w każdej sekcji mają zasadniczo zastosowanie do celów danej sekcji, niektóre elementy w jednej sekcji mogą mieć wpływ na elementy w innej sekcji. Na przykład kliknięcie przycisku Wybrane punkty w sekcji **Środek** z zaznaczonymi dwoma punktami w oknie widoku 3D powoduje nie tylko wypełnienie pól wyboru współrzędnych **Środek** współrzędnymi punktu środkowego między tymi dwoma zaznaczonymi punktami, ale także utworzenie niestandardowej osi wzdłuż linii zdefiniowanej przez te dwa zaznaczone punkty w sekcji **Obrót**. W innym przykładzie umieszczenie wartości w polu wyboru osi i kliknięcie przycisku Zastosuj oś w sekcji **Przesunięcie** powoduje translację *(przesunięcie)* obiektu wzdłuż osi zdefiniowanej w sekcji **Obrót**.

Pole wyboru **Zastosuj zmiany przyrostowe** jest przydatne, gdy translacje / obroty mają być wykonywane względem aktualnego położenia / pochylenia obiektu, a nie względem pierwotnego położenia / pochylenia. Zaznaczenie tego pola resetuje pola dialogowe do zera, ale nie zmienia orientacji ani położenia obiektu. Kolejne wpisy zmieniają orientację / położenie, ale są stosowane od aktualnej pozycji obiektu. Włączenie tego pola wyboru jest również przydatne podczas korzystania z przycisku Wybrane punkty, ponieważ może ono czasami zapobiegać niepożądanym zmianom położenia.

PS: od wersji 0.17 wprowadzono nowy obiekt Część, obiekt ten posiada swoje umiejscowienie, a obiekt Umiejscowienie utworzony w obiekcie Część jest inkrementowany o Umiejscowienie części. {{Version/pl|0.17}} Aby uzyskać Umiejscowienie środowiska Część użyj następującego kodu: 
```python
import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print sel[0].Placement
print sel[0].getGlobalPlacement()   # return the GlobalPlacement
print sel[0].getParentGeoFeatureGroup() # return the GeoFeatureGroup, ex:  Body or a Part.
print  "____________________"
```

Przycisk **Wybrane punkty** służy do wypełniania współrzędnych w polach współrzędnych **Środek** oraz *(po wybraniu 2 lub 3 punktów)* dodatkowo do tworzenia własnej (zdefiniowanej przez użytkownika) osi obrotu w sekcji **Obrót**. Punktem może być wierzchołek, ale może to być także dowolny punkt wzdłuż krawędzi lub na powierzchni. Gdy zaznaczasz krawędź lub ścianę, zaznaczana jest cała krawędź lub ściana, ale FreeCAD zapamiętuje również, na który punkt na tej ścianie lub krawędzi najeżdżał kursor myszki, gdy ta krawędź lub ściana była zaznaczona. To właśnie współrzędne tego punktu są używane w oknie dialogowym Umiejscowienie, gdy zostanie kliknięty przycisk **Wybrane punkty**. Być może uważasz, że nie jest to zbyt precyzyjny sposób zaznaczania punktu, i masz rację, ale w wielu przypadkach wystarczy, że wybrany punkt będzie znajdował się na tej krawędzi lub ścianie. W przypadkach, gdy trzeba precyzyjnie wyznaczyć punkt, który ma zostać użyty, należy wybrać wierzchołek. Jeśli w żądanym miejscu nie ma żadnego wierzchołka, można go utworzyć, np. w tymczasowym szkicu dołączonym do tej ściany lub krawędzi, lub za pomocą obiektu środowiska Rysunek Roboczy, takiego jak linia lub punkt itp.

Rozważmy najpierw prosty przypadek wybrania jednego punktu. W tym celu należy najpierw zaznaczyć żądany punkt, a następnie kliknąć przycisk **Wybrane punkty**. Współrzędne wybranego punktu zostaną użyte do wypełnienia pól obrotowych X, Y i Z w sekcji **Środek**. Teraz każdy obrót wykonywany na obiekcie będzie się odbywał wokół tego środka obrotu.

Rozważmy teraz przypadek wybrania dwóch punktów. Wybieramy dwa żądane punkty, a następnie klikamy przycisk **Wybrane punkty**. Współrzędne punktu środkowego między dwoma wybranymi punktami zostaną umieszczone w polach X, Y i Z w sekcji **Środek**. Teraz każdy obrót wykonywany na obiekcie będzie się odbywał wokół tego środka obrotu. Jednak oprócz ustawienia współrzędnych sekcji **Środek** do elementu **Oś** w sekcji **Obrót** dodaje się również oś niestandardową *(zdefiniowaną przez użytkownika)*. *(Uwaga: jeśli byłeś w trybie obrotu Eulera, tryb ten zostanie przełączony na tryb obrotu z osią, a nowa oś niestandardowa zostanie wybrana jako bieżąca oś obrotu)*. Teraz każdy obrót wykonany przy użyciu nowej osi niestandardowej będzie się odbywał wokół tej osi obrotu. Dodatkową zaletą jest pomiar odległości między dwoma wybranymi punktami, a informacja ta jest podawana w widoku raportu. *(Uwaga: Przytrzymaj klawisz **Shift** podczas klikania przycisku **Wybrane punkty**, aby skopiować pomiar odległości do schowka)*. Wprowadzając tę odległość do pola wyboru Oś w sekcji **Przesunięcie** i klikając przycisk **Zastosuj osiowe**, można przesunąć obiekt tak, że pierwszy zaznaczony punkt zajmuje teraz współrzędne zajmowane przez drugi zaznaczony punkt *(w momencie kliknięcia przycisku **Wybrane punkty**)*.

Rozważmy teraz przypadek wybrania trzech punktów. Wybieramy trzy żądane punkty, a następnie klikamy przycisk **Wybrane punkty**. Współrzędne pierwszego wybranego punktu *(kolejność wyboru jest tu bardzo ważna)* zostaną umieszczone w polach X, Y i Z w sekcji **Środek**. Ponieważ te trzy punkty definiują płaszczyznę, FreeCAD może to wykorzystać i użyć tych punktów do utworzenia nowej niestandardowej *(zdefiniowanej przez użytkownika)* osi obrotu, która jest normalną *(prostopadła)* do tej zdefiniowanej płaszczyzny. Podobnie jak w przypadku dwuch wybranych punktów, odległość między punktami jest również wyświetlana w widoku raportu, ale tym razem jest to odległość między drugim i trzecim wybranym punktem. *(Uwaga: Przytrzymaj klawisz **Shift** podczas klikania przycisku **Wybrane punkty** \-- Shift + Kliknij \-- aby skopiować miarę kąta do schowka)*. Dodatkowo, kąt między drugim i trzecim punktem jest również mierzony i wyświetlany w widoku raportu. Wprowadzając ten kąt do pola wyboru **Kąt** w sekcji **Obrót** możemy bardzo precyzyjnie obrócić obiekt tak, aby teraz drugi zaznaczony punkt był w jednej linii ze współrzędnymi trzeciego zaznaczonego punktu. *(Uwaga: jeśli chcesz uzyskać większą precyzję, możesz zwiększyć liczbę cyfr w menu Edycja → Preferencje → Ogólne → Jednostki → Liczba miejsc po przecinku)*.

## Przykłady

Obroty wokół jednej osi:

<img alt="Przed obrotem" src=images/RotationAboutZBefore.png  style="width:600px;"> Przed obróceniem *(widok z góry)* 

<img alt="Po obrocie wokół osi Z" src=images/RotationAboutZAfter.png  style="width:600px;"> Po obróceniu wokół osi Z *(widok z góry)* 

<img alt="Po obróceniu wokół y=x" src=images/RotationAboutYXAfter.png  style="width:600px;"> Po obróceniu wokół y=x (widok z prawej strony) 

Obrót z przesunięciem punktu środkowego:

<img alt="Przed obróceniem" src=images/RotationOffsetBefore._png  style="width:600px;"> Przed obrotem *(widok z góry)* 

<img alt="Po obrocie wokół Z" src=images/RotationOffsetAfter._png  style="width:600px;"> Po obrocie wokół Z *(widok z góry)* 

Obrót z użyciem kątów Eulera:

<img alt="Przed obrotem" src=images/RotationEulerBefore.png  style="width:600px;"> Przed obrotem 

<img alt="Po obróceniu" src=images/RotationEulerAfter.png  style="width:600px;"> Po obróceniu 

## Placement.Base a Definicja kształtu 

Umiejscowienie nie jest jedynym sposobem pozycjonowania kształtu w przestrzeni. Zwróć uwagę na konsolę Python na tym obrazku:

![Dwa kształty o tym samym umiejscowieniu](images/2Placements800.png )

Oba prostopadłościany mają taką samą wartość dla Umiejscowienia, ale różnią się lokalizacją! Dzieje się tak ponieważ te dwie figury są zdefiniowane przez różne wierzchołki *(krzywe w bardziej złożonych kształtach)*. Dla dwóch kształtów na powyższej ilustracji:

 >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
 >>> for v in ev: print v.X,",",v.Y,",",v.Z
 ... 
 30.0,30.0,0.0
 30.0,30.0,10.0
 40.0,30.0,0.0
 40.0,30.0,10.0
 40.0,40.0,0.0
 40.0,40.0,10.0
 30.0,40.0,0.0
 30.0,40.0,10.0
 >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
 >>> dla v w e1v: print v.X,",",v.Y,",",v.Z
 ... 
 0.0,10.0,0.0
 0.0,10.0,10.0
 10.0,10.0,0.0
 10.0,10.0,10.0
 10.0,0.0,0.0
 10.0,0.0,10.0
 0.0,0.0,0.0
 0.0,0.0,10.0
 >>> 
 

Wierzchołki *(lub wektory)* definiujące kształt używają atrybutu Placement.Base jako ich punktu odniesienia położenia. Jeśli chcemy przesunąć kształt o 10 jednostek wzdłuż osi X, możemy dodać 10 do współrzędnych **X** wszystkich wierzchołków lub ustawić wartość atrybutu Placement.Base na (10,0,0).

## Używanie \"środka\" do kontroli osi obrotu 

Domyślnie oś obrotu nie jest w rzeczywistości osią x/y/z. Jest to linia równoległa do wybranej osi, ale przechodząca przez punkt odniesienia (Placement.Base) obiektu, który ma zostać obrócony. Można to zmienić za pomocą pól Środek w oknie dialogowym Umiejscowienie lub, w skryptach, za pomocą parametru Środek konstruktora FreeCAD.Placement. Naciśnij kombinację klawiszy **CTRL** + **ENTER**, aby zatwierdzić i przejść do następnego komunikatu, lub **ALT** + **SHIFT** + **D**, aby pominąć, lub **ALT** + **SHIFT** + **B**, aby podać opis zmian lub przytrzymaj klawisz **ALT**, aby zobaczyć inne skróty. Dodaj dokumentację

Na przykład, załóżmy, że mamy prostopadłościan *(jak poniżej)* umieszczony w punkcie (20,20,10). ![Przed obrotem](images/LocalZBefore2.png ) Chcemy obrócić prostopadłościan wokół jego pionowej linii środkowej *(tzn. lokalnego Z)*, zachowując tę samą pozycję. Możemy to łatwo osiągnąć, określając wartość Center równą współrzędnym punktu centralnego prostopadłościanu (25,25,15). ![Po obróceniu](images/LocalZAfter2.png )

W skrypcie zrobilibyśmy to następująco: 
```python
import FreeCAD
obj = App.ActiveDocument.Box                       # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)   # 45° about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,15)                  # central point of box 
pos = obj.Placement.Base                           # position point of box
newplace = FreeCAD.Placement(pos,rot,centre)       # make a new Placement object
obj.Placement = newplace                           # spin the box
``` Ten sam skrypt w pliku przykładowym [RotateCoG2.fcstd](http://forum.freecadweb.org/download/file.php?id=1651) *(dyskusja na [forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3950#p31052))*. 
```python
import FreeCAD
obj = App.ActiveDocument.Extrude                    # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)    # 45 about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)    # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                    # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,0)                    # "centre" of rotation (where local Z cuts XY)
pos = obj.Placement.Base                            # original placement of obj
newplace = FreeCAD.Placement(pos,rot,centre)        # make a new Placement object
obj.Placement = newplace                            # spin the box
```

## Używanie umiejscowienia w wyrażeniach 

W wyrażeniach można używać składowych umiejscowienia. W wyrażeniach możliwe jest użycie składowych umiejscowienia, na przykład w celu uzyskania dostępu do składowej x obiektu oznaczonego jako \"Cube\": 
```python
<<Cube>>.Placement.Base.x
```

Dostęp do kąta obrotu można uzyskać przez 
```python
<<Cube>>.Placement.Rotation.Angle
```

Dostęp do osi obrotu można uzyskać za pomocą 
```python
<<Cube>>.Placement.Rotation.Axis.x
<<Cube>>.Placement.Rotation.Axis.y
<<Cube>>.Placement.Rotation.Axis.z
``` gdzie często jedną z tych wartości jest {{Value|1}}, a pozostałe są równe {{Value|0}}.

W jednym wyrażeniu można także użyć całego Umiejscowienia: Kliknij prawym przyciskiem myszy właściwość Umiejscowienie w edytorze właściwości, wybierz opcję \"pokaż wszystkie\", wtedy zostaną wyświetlone dodatkowe właściwości. Jeśli następnie ponownie klikniesz prawym przyciskiem myszy na Umiejscowienie, w menu kontekstowym pojawi się Wyrażenie, wybierz opcję Wyrażenie, a otworzy się okno dialogowe Wyrażenie, w którym wszystko, co wpiszesz, trafi do właściwości Umiejscowienia, a nie do jej właściwości podrzędnych.

Aby zrównać umiejscowienie \"Szkicu\" z umiejscowieniem \"Cylindra\", należałoby wprowadzić wyrażenie dla Szkicu w taki sposób 
```python
<<Cube>>.Placement
``` ![Ustawienia całego Umiejscowienia w jednym wyrażeniu](images/PlacementInExpression.png )

**UWAGA:** Możliwe jest również *tworzenie* obiektów Umiejscowienie w wyrażeniach. Zobacz stronę [Wyrażenia](Expressions/pl#Umiejscowienie.md), aby dowiedzieć się więcej.

## Uwagi

-   Właściwości Umiejscowienie w zakładce Dane są nieaktywne dla obiektów, które są dołączone do innego obiektu. Zamiast tego należy edytować Przesunięcie dołączenia.
-   Oś i Kąt mogą być również wyrażone jako [kwaternion](http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation).
-   Punkt odniesienia obiektu różni się w zależności od obiektu. Kilka przykładów dla typowych obiektów:

  Obiekt                        Punkt odniesienia
   
  Part.Box                      lewy *(minx)*, przedni *(miny)*, dolny *(minz)* wierzchołek
  Part.Sphere                   środek sfery *(tj. środek ramki otaczającej)*
  Part.Cylinder                 środek dolnej ściany
  Part.Cone                     środek powierzchni dolnej ściany *(lub wierzchołek, jeśli promień dolny wynosi 0)*
  Part.Torus                    środek torusa
  Obiekty pochodne od szkiców   obiekty dziedziczą pozycję bazowego szkicu. Szkice zawsze zaczynają się w pozycji = (0,0,0). Pozycja ta odpowiada punktowi położenia odniesienia w szkicu.

## Problemy

-   Względne rozmieszczanie obiektów będzie docelowo obsługiwane w środowisku pracy Złożenie.

## Więcej

-   Ten poradnik: [Aeroplan](Aeroplane/pl.md) obszernie omawia mechanikę zmiany położenia obiektu.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Placement/pl
