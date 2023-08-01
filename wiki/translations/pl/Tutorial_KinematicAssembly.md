---
- TutorialInfo:/pl
   Topic:Złożenie 3, prosty mechanizm
   Level:Przydatna jest podstawowa znajomość narzędzi środowiska pracy Złożenie 3
   FCVersion:0.20 i następne
   Time:30 minut
   Author:[FBXL5](User_FBXL5.md)
---

# Tutorial KinematicAssembly/pl





## Wprowadzenie

Ten poradnik jest o tym, jak zbudować prosty mechanizm, głównie przy użyciu narzędzi z zewnętrznego <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [środowiska Złożenie 3](Assembly3_Workbench/pl.md).

Złożenie kinematyczne, które stworzymy, będzie zbudowane z czterech części: Podstawy, Suwaka, Korby i Korbowodu. Są one połączone z wykorzystaniem czterech węzłów.

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:400px;"> 
*Złożone części: Podstawa ''(bursztynowy)'', Suwak ''(jasnoniebieski)'', Korba ''(czerwony)'', Korbowód ''(zielony)''*

## Złożenie

### Części

**Podstawa** to obiekt składający się z dwóch głównych elementów geometrycznych: otworu i sworznia. Oba są walcowe. Reszta kształtu nie jest istotna w tym poradniku, chyba że powoduje kolizje. To samo dotyczy innych części.

<img alt="" src=images/Assembly3_KinematicExample-02.png  style="width:300px;">

**Suwak** składa się z wałka z sworzniem na jednym z końców. Oba są walcowe.

<img alt="" src=images/Assembly3_KinematicExample-03.png  style="width:300px;">

**Korba** ma otwór i sworzeń. Znów, oba są walcowe.

<img alt="" src=images/Assembly3_KinematicExample-04.png  style="width:300px;">

**Korbowód** ma dwa walcowe otwory.

<img alt="" src=images/Assembly3_KinematicExample-05.png  style="width:300px;">

### Węzły

#### Zablokowana Podstawa 

Aby utrzymać zespół w zadanym położeniu, należy zablokować podstawę.

:   *(Jeśli polecenie <img alt="" src=images/Assembly_LockMover.svg  style="width:16px;"> [Zablokuj przesunięcie](Assembly3_LockMover/pl.md) jest aktywne, narzędzia ruchu są wyłączone, tak długo jak wybrana jest zablokowana część)*.

1.  Wybierz jedną ścianę Podstawy.
2.  Wciśnij przycisk **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Utwórz "Wiązanie zablokowania"](Assembly3_ConstraintLock/pl.md)**, aby Podstawa pozostawało na swoim miejscu na stałe.

<img alt="" src=images/Assembly3_KinematicExample-08.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_KinematicExample-09.png  style="width:300px;"> 
*Zaznaczona ściana → Powstały Element*

Następnie wszystkie cztery części zostaną połączone czterema węzłami. Łańcuch kinematyczny zaczyna się od podstawy.

#### Węzeł Postawa-Suwak 

Węzeł Podstawa-Suwak jest **węzłem walcowym** Umożliwia on Suwakowi ślizgać się wzdłuż i obracać dookoła osi Z otworu Podstawy, jednocześnie utrzymując osie Z obu elementów wyrównane *(współosiowe)*.

Pasującym wiązaniem jest wiązanie \"Wiązanie osi\". Działa ono z elementami, które reprezentują geometrię walcową, takimi jak powierzchnie walcowe, powierzchnie kołowe i krawędzie kołowe.

1.  Wybierz powierzchnie walcowe otworu Podstawy i wałka Suwaka.
2.  Wciśnij przycisk **<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Utwórz "Wiązanie osi"](Assembly3_ConstraintAxial/pl.md)**.
3.  Opcjonalnie zmień etykietę utworzonych elementów (edytuj ich właściwość **Label**).

<img alt="" src=images/Assembly3_KinematicExample-10.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_KinematicExample-11.png  style="width:300px;"> 
*Wybrane ściany → Wyrównane obiekty*

#### Węzeł Podstawa-Korba 

Węzeł Postawa-Korba jest **węzłem typu zawias**. Pozwala on obracać się Korbie wokół osi Z sworznia Podstawy, jednocześnie utrzymując wyrównanie *(współosiowość)* osi Z obu elementów oraz stałą odległość między płaszczyznami XY.

Pasującym wiązaniem jest wiązanie *Zbieżność płaszczyzn*. Działa ono na elementach będących geometrią planarną jak okrągłe powierzchnie i okrągłe krawędzie *(w tym przypadku)*.

1.  Wybierz okrągłą powierzchnię lub zewnętrzną okrągłą krawędź sworznia Podstawy oraz zewnętrzną okrągłą krawędź otworu Korby.
2.  Wciśnij przycisk **<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Utwórz wiązanie "Zbieżność płaszczyzn"](Assembly3_ConstraintCoincidence/pl.md)**.
3.  Opcjonalnie zmień etykiety utworzonych elementów.

<img alt="" src=images/Assembly3_KinematicExample-12.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_KinematicExample-13.png  style="width:300px;"> 
*Zaznaczona ściana i krawędź → Wyrównane obiekty*

#### Węzeł Suwak-Korbowód 

Węzeł Suwak-Korba jest **węzłem typu zawias**. Pozwala on obracać się Korbowodowi wokół osi Z sworznia Suwaka, jednocześnie utrzymując wyrównanie *(współosiowość)* osi Z obu elementów oraz stałą odległość między płaszczyznami XY.

Pasującym wiązaniem jest wiązanie *Zbieżność płaszczyzn* *(zobacz wyżej)*.

1.  Wybierz okrągłą powierzchnię lub zewnętrzną okrągłą krawędź sworznia Suwaka oraz zewnętrzną okrągłą krawędź otworu Korbowodu.
2.  Wciśnij przycisk **<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Utwórz wiązanie "Zbieżność płaszczyzn"](Assembly3_ConstraintCoincidence/pl.md)**.
3.  Opcjonalnie zmień etykiety utworzonych elementów.

<img alt="" src=images/Assembly3_KinematicExample-14.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_KinematicExample-15.png  style="width:300px;"> 
*Zaznaczona ściana i krawędź → Wyrównane obiekty*

#### Węzeł Korba-Korbowód 

Węzeł Korba-Korbowód jest **węzłem walcowym** Umożliwia on Korbowodowi obracać się dookoła i ślizgać się wzdłuż osi Z sworznia Korby, jednocześnie utrzymując osie Z obu elementów wyrównane *(współosiowe)*. Jednak możliwe jest tylko obracanie, ponieważ ruch ślizgowy jest ograniczony przez kombinację węzła Podstawa-Korba oraz węzła Suwak-Korbowód.

Pasującym wiązaniem jest \"Wiązanie osi\" *(zobacz wyżej)*.

1.  Wybierz powierzchnie walcowe sworznia Korby i otworu Korbowodu.
2.  Wciśnij przycisk **<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Utwórz "Wiązanie osi"](Assembly3_ConstraintAxial/pl.md)**.
3.  Opcjonalnie zmień etykietę utworzonych elementów.

<img alt="" src=images/Assembly3_KinematicExample-16.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:300px;"> 
*Wybrane ściany → Wyrównane obiekty*

#### Nadmiarowe Wiązania 

Gdy Podstawa jest zamocowana i wszystkie cztery przeguby są związane, w oknie [Widoku raportu](Report_view/pl.md) pojawiają się dwa komunikaty:

-   Ostrzeżenie *(pomarańczowy)*: \"\...wiązania nadmiarowe\".
-   Zwykły komunikat *(czarny)*: \"\...pozostało stopni swobody: 0\".

Taka kombinacja komunikatów występuje, gdy części zespołu są nadmiernie związane, ale solwer nadal jest w stanie znaleźć poprawne rozwiązanie. Ale co jest przyczyną nadmiarowości?

Jest to kierunek Z sworzni. Jeśli przyjrzymy się na przykład sworzniowi Suwaka, zauważymy, że oś Z jego obiektu elementu jest związana równolegle do osi Z sworznia Podstawy poprzez łańcuch złożeń Podstawa-Korba-Korbowód-Suwak. Oznacza to, że sworzeń Suwaka nie może obracać się wokół swoich osi X i Y.

<img alt="" src=images/Assembly3_KinematicExample-06.png  style="width:400px;">

Z drugiej strony obrót wokół osi X *(kolor czerwony)* jest już uniemożliwiony przez węzeł Podstawa-Korba, a zatem odpowiedni stopień swobody *(dof)* jest związany dwukrotnie *(= nadmiarowy)* i powoduje wyświetlenie ostrzeżenia.

:   Aby uniknąć tej nadmiarowości, można by wstawić obiekt pomocniczy i odpowiednie wiązania, ale to temat na inny poradnik.
:   Aby uniknąć podwójnego wiązania odsunięcia między Podstawą a Korbowodem, użyto różnych wiązań, z których tylko jedno blokuje ruch wzdłuż osi Z.

### Siłownik

Teraz jest to nadal złożenie statyczne. Aby przekształcić je w złożenie kinematyczne, należy użyć jednego z wiązań jako nastawnika. Aby użyć wiązania \"Zbieżność płaszczyzn\" w węźle Podstawa-Korba jako nastawnika, musimy kontrolować kąt między sworzniem Podstawy a Korbą. Można to zrobić, ustawiając właściwość **Zablokuj kąt** na wartość {{TRUE/pl}}. W celu późniejszego wykorzystania etykieta jest oznaczana przyrostkiem **.Driver**.

Właściwosć**Kąt** może zostać teraz użyta do obracania Korbą.

<img alt="" src=images/Assembly3_KinematicExample-07.gif  style="width:350px;">

## Sterownik

Dobrze byłoby mieć okno dialogowe do zmiany wartości właściwości bez wpisywania i z automatycznym przeliczaniem.

Spójrz na poradnik [Sterownik Kinematyczny](Tutorial_KinematicController/pl.md).



---
⏵ [documentation index](../README.md) > Tutorial KinematicAssembly/pl
