---
- TutorialInfo:/pl
   Topic:Umocowanie
   Level:Średniozaawansowany / zaawansowany
   Author:drmacro
   Time:1 godzina
   FCVersion:0.19 lub nowszy
   Files:do ustalenia
---

# Advanced Attachment OYX/pl





<img alt="" src=images/AttOYX_Setup.png  style="width:800px;"> 
*Obiekt w pozycji początkowej*

## Wprowadzenie

Ta demonstracja dotyczy użycia trybu umocowania OYX w celu dostosowania pozycji odniesienia położenia szkicu, jak opisano na stronie [Część: Edycja mocowania](Part_EditAttachment/pl.md), nie jest ona wyczerpująca, ale może pomóc użytkownikom w eksperymentowaniu.

Na powyższym rysunku zaprezentowano geometrię użytą w tej demonstracji.

Prawy dolny rysunek przedstawia widok sceny z góry. Zwróć uwagę, że scena przedstawia szkic zawierający kwadrat oraz tekst wskazujący osie pionowe *(Y)* i poziome *(X)* szkicu. Lewy dolny róg kwadratu znajduje się w punkcie 0,0,0 szkicu *(punkt położenia odniesienia)*.

Odniesienie położenia szkicu i odniesienie położenia globalne *(oznaczone przez czerwony, zielony i niebieski [krzyż osi](Std_AxisCross/pl.md))* to ten sam punkt. Na pozostałych obrazkach widać, że kwadrat znajduje się w punkcie Z=0, a więc szkic znajduje się w płaszczyźnie XY.

Kolejne dwa szkice zawierają geometrię, która zostanie użyta do zmiany położenia szkicu zawierającego kwadrat. Jeden szkic zawiera pomarańczową linię, która jest zorientowana wzdłuż globalnej osi Z w płaszczyźnie XZ. Drugi szkic zawiera żółtą linię na płaszczyźnie XY.

## Dyskusja

Sposób umocowania Wyrównaj O-Y-X jest zdefiniowany w następujący sposób w [Część: Edycja mocowania](Part_EditAttachment/pl.md): *Dopasowuje punkt odniesienia położenia obiektu do pierwszego wierzchołka odniesienia i wyrównuje jego osie płaszczyzny pionowej i poziomej do wierzchołka / wzdłuż linii*. Wskazuje również, że istnieje kilka kombinacji odniesienia.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź

Zacznijmy od kombinacji \"wierzchołek, wierzchołek, wierzchołek\".

Jeśli dopasujemy definicję do odniesienia:

Pierwszy wybrany wierzchołek spowoduje ustawienie punktu odniesienia położenia szkicu na wybranym wierzchołku.

Drugi wybrany wierzchołek dopasuje oś pionową szkicu *(w konfiguracji demonstracyjnej oś ta jest oznaczona jako **Y**)*.

Jeśli więc wybierzemy lewy/górny wierzchołek żółtej krawędzi *(widoczny na większym rysunku po prawej stronie)* oraz dolny / prawy wierzchołek żółtej krawędzi, szkic zostanie umieszczony w taki sposób:

<img alt="" src=images/AttOYX_vv.png  style="width:800px;">

:; Uwagi:

:   Opcja Umocowania O-Y-X jest wybierana w oknie dialogowym Dołączanie.
:   Punkt odniesienia położenia szkicu znajduje się teraz w lewym / górnym wierzchołku żółtej linii.
:   Oś Y szkicu jest teraz wyrównana z żółtą linią.
:   Oś Z szkicu jest prostopadła do żółtej linii.

Jeśli teraz dodamy trzecie odniesienie, wybierając górny wierzchołek pomarańczowej krawędzi, otrzymamy nowy wygląd sceny:

<img alt="" src=images/AttOYX_vvv.png  style="width:800px;">

:; Uwagi:

:   Teraz oś X szkicu jest wyrównana w kierunku wybranego wierzchołka pomarańczowej krawędzi.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Advanced Attachment OYX/pl
