---
 TutorialInfo:l
   Topic: Modelowanie
   Level: Początkujący
   Author: User:EmmanuelG
   Time: 1 godzina
   FCVersion: 0.16 lub nowszy
   Files: https://www.thingiverse.com/thing:2403310 Thingiverse 2403310
---

# Toothbrush Head Stand/pl







## Problem z życia codziennego 

Elektryczne szczoteczki do zębów rzadko występują ze stojakiem na główkę, natomiast w rodzinie często można zobaczyć wiele główek używanych z jednym korpusem. Wiele osób borykających się ze wspólnym problemem prowadzi nas do różnych rozwiązań, co można zobaczyć na Thingiverse *(200-800 projektów jest związanych z tym tematem)*. Oto pierwsza odpowiedź i jak ją zaprojektować.

Ten poradnik przeprowadzi Cię przez proces wymodelowania części pokazanej na poniższym obrazku przy użyciu podstawowych narzędzi ze środowiska [Projekt Części](PartDesign_Workbench/pl.md) *(wiele narzędzi i możliwości nie zostało omówionych)*.

![](images/TBHS-model.png )



## Pierwszy pomysł: płyta 

-   Na stronie startowej wybierz ![](images/Workbench_PartDesign.svg ) *Projekt Części* lub utwórz nowy dokument i wybierz środowisko *Projekt Części*.

![](images/TBHS-0.png )

![](images/TBHS-0.png )



## Utwórz szkic 

-   Kliknij na <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [**Nowy szkic**](Sketcher_NewSketch/pl.md). Albo z menu podrzędnego w oknie zadania po lewej stronie, albo z paska narzędziowego powyżej, albo z menu Projekt Części na górze.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

W oknie dialogowym zostanie wyświetlony monit o wybranie orientacji szkicu i podanie odsunięcia.

-   Wybierzemy Płaszczyznę XY jak na powyższym obrazku *(ta orientacja odpowiada wspólnej płycie konstrukcyjnej większości drukarek 3D)*, a następnie kliknij OK.

<img alt="" src=images/TBHS-2.JPG  style="width:800px;">

Jesteś teraz zwrócony do płaszczyzny XY z góry i masz dostęp do narzędzi kreślarskich.

-   Kliknij narzędzie <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [**Utwórz prostokąt**](Sketcher_CreateRectangle/pl.md)
-   Kliknij, aby umieścić pierwszy punkt.
-   Kliknij, aby umieścić przeciwległy narożnik.
-   Naciśnij **ESC** lub kliknij prawym przyciskiem myszy, aby zakończyć korzystanie z narzędzia.

<img alt="" src=images/TBHS-3.JPG  style="width:800px;">

Masz teraz pływający prostokąt o nieokreślonych wymiarach.

-   Kliknij linię prostokąta, aby uzyskać dostęp do narzędzi wiązań po prawej stronie paska narzędzi *(w zależności od rozmiaru ekranu może być konieczne przeciągnięcie ich w lewo, aby zobaczyć je wszystkie)*.
-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md)
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź {{Value|80 mm}} i kliknij **OK**.
-   Powtórz czynność z drugim bokiem prostokąta, również wpisując {{Value|80 mm}}.

<img alt="" src=images/TBHS-4.JPG  style="width:800px;">

Masz teraz ruchomy kwadrat.

-   Kliknij lewy dolny punkt kwadratu.
-   Kliknij na początek płaszczyzny XY *(na przecięciu dwóch grubych linii)*.
-   Kliknij na <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [Wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md).

<img alt="" src=images/TBHS-5.JPG  style="width:800px;">

Masz teraz całkowicie związany szkic, o czym informuje Cię solwer po lewej stronie i zmiana jego koloru. Dobrą praktyką jest posiadanie zawsze całkowicie zawężonego szkicu.

Niedostatecznie związany szkic może pozostawić miejsce na niechciane zmiany, jeśli zmodyfikujesz coś później.

Z drugiej strony, szkic z nadmiernymi więzami również nie jest dobry. W takim przypadku solwer ostrzega o nadmiarowych wiązaniach i należy usunąć niektóre z nich.

-   Aby opuścić szkic, kliknij przycisk **Zamknij** po lewej stronie lub ikonę <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> na pasku narzędzi lub naciśnij **ESC**.

<img alt="" src=images/TBHS-6.JPG  style="width:800px;">

Teraz widzisz tylko kwadrat, a menu kontekstowe zadań po lewej stronie pokazuje więcej opcji niż wcześniej.



### Utwórz wyciągnięcie 

-   Kliknij na widok <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Aksonometryczny** wśród standardowych widoków, aby lepiej zobaczyć, co się stanie.
-   Kliknij na <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Wyciągnięcie**.
-   Wprowadź {{Value|4 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS-7.JPG  style="width:800px;">

Twój szkic ma teraz objętość!



### Utwórz na nim szkic 

-   Wybierz górną powierzchnię

<img alt="" src=images/TBHS-8.JPG  style="width:800px;">

Zmienia się kolor ściany i dostępnych jest więcej opcji w menu podręcznym.

-   Kliknij na <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Utwórz szkic**. Ponieważ wybrano ścianę, nie zostanie wyświetlony monit o wybranie płaszczyzny.

<img alt="" src=images/TBHS-9.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Utwórz okrąg**](Sketcher_CreateCircle/pl.md), kliknij ponownie aby umieścić środek, przesuń wskaźnik i kliknij, aby zdefiniować promień.
-   Narysuj 4 okręgi na podkładce \'\'(o dowolnym rozmiarze)\'.\'
-   Naciśnij **ESC** lub kliknij prawym przyciskiem myszy, aby zakończyć korzystanie z narzędzia.

<img alt="" src=images/TBHS-10.JPG  style="width:800px;">

-   Wybierz okręgi
-   Kliknij na <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [**Wiązanie równości**](Sketcher_ConstrainEqual/pl.md).

<img alt="" src=images/TBHS-11.JPG  style="width:800px;">

Teraz okręgi mają ten sam promień.

-   Kliknij na <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Utwórz geometrię zewnętrzną](Sketcher_External/pl.md).
-   Kliknij na cztery boki kwadratu, doda to linie, kolor magenta.

<img alt="" src=images/TBHS-12.JPG  style="width:800px;">

Linie te posłużą jako odniesienie do pozycjonowania okręgów.

-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Równanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Kliknij na środek okręgu.
-   Kliknij na linię w kolorze magenta.
-   Ustaw odległość *(20 mm z każdej strony)*.

<img alt="" src=images/TBHS-13.JPG  style="width:800px;">

-   Kliknij na okrąg
-   Kliknij na <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Wiązanie promienia](Sketcher_ConstrainRadius/pl.md) i ustaw go na {{Value|1,5mm}}.

<img alt="" src=images/TBHS-14.JPG  style="width:800px;">

-   Aby opuścić szkic, kliknij przycisk **Zamknij** po lewej stronie lub ikonę <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> na pasku narzędzi lub naciśnij **ESC**.

<img alt="" src=images/TBHS-15.JPG  style="width:800px;">



### Utwórz wyciągnięcie 

-   Kliknij na widok <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Aksonometryczny** wśród standardowych widoków, aby lepiej zobaczyć, co się stanie.
-   Kliknij na <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Wyciągnij**.
-   Wprowadź wartość {{Value|25 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS-16.JPG  style="width:800px;">

Masz już podstawowy kształt, potrzebujesz tylko ostatecznych poprawek.



### Zaokrąglanie narożników 

-   Przytrzymując **CTRL** kliknij pionową krawędź w każdym rogu, aby wybrać cztery z nich.

Nie wahaj się pomóc, przełączając tryb wyświetlania (tuż po lewej stronie widoku aksonometrycznego) między <img alt="" src=images/DrawStyleWireFrame.svg  style="width:32px;"> **Szkieletowy** a <img alt="" src=images/DrawStyleFlatLines.svg  style="width:32px;"> **cieniowany z krawędziami**.

<img alt="" src=images/TBHS-17.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [**Zaokrąglenie**](PartDesign_Fillet/pl.md).
-   Ustaw promień na {{Value|20 mm}}.

<img alt="" src=images/TBHS-18.JPG  style="width:800px;">

O wiele lepiej.



### Zwiększenie wytrzymałości 

Musimy dodać materiał u podstawy cylindrów, aby były mniej podatne na pęknięcia. Ze względu na orientację drukowania te małe powierzchnie będą kruche na styku z podstawą.

-   Wybierz okręgi u podstawy cylindrów.

<img alt="" src=images/TBHS-19.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Sfazowanie](PartDesign_Chamfer/pl.md).
-   Ustaw wartość {{Value|2 mm}}.

<img alt="" src=images/TBHS-20.JPG  style="width:800px;">



### Sfazowanie krawędzi 

-   Wybierz powierzchnię pod podstawą, dodaj <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Sfazowanie** o wartości {{Value|0,5 mm}}.

Pierwsza warstwa plastiku jest często nieco zbyt mocno zgnieciona, co zrekompensuje to i zaoszczędzi czas na czyszczenie modelu. Jeśli pierwsza warstwa jest w porządku, poprawi tylko wygląd.

<img alt="" src=images/TBHS-21.JPG  style="width:800px;">

-   Wybierz krawędzie na granicy górnej powierzchni *(przytrzymując **CTRL**)*.

<img alt="" src=images/TBHS-23.JPG  style="width:800px;">

-   Dodaj <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Sfazowanie** {{Value|1 mm}}. To jest tylko kwestia estetyczna.

<img alt="" src=images/TBHS-22.JPG  style="width:800px;">

Gotowe !



## Eksport do pliku .STL 

-   W widoku Złożonym po lewej stronie, wybierz widok drzewa zamiast kontekstowego menu zadań, kliknij ostatnią cechę *(fazę)*.

<img alt="" src=images/TBHS-24.JPG  style="width:800px;">

-   Teraz możesz wybrać \"Eksportuj\...\" z menu Plik w lewym górnym rogu i wybrać format pliku .STL.
-   Wystarczy go wydrukować :-)



## Inspiracja

Powyższy model stanowi dobry punkt wyjścia do korzystania z FreeCAD, ale jako stojak na główkę szczoteczki do zębów ma swoje wady: ze względu na orientację wydruku i małą powierzchnię drążki są podatne na złamania.

Zainspirowani różnorodnością rozwiązań zaproponowanych przez inne osoby, stworzymy drugą wersję, która będzie znacznie lepsza.

<img alt="" src=images/TBHS-v2.jpg  style="width:800px;">

Nie martw się, często trzeba przejść przez kilka poprawek dla danego pomysłu *(np.: po użyciu prototypu na obrazku dodaliśmy więcej miejsca między główkami, aby się nie stykały)*.

W tej drugiej części nauczysz się również korzystać z większej liczby narzędzi, takich jak potężne \"powtórzenie liniowe\".



## Drugi pomysł: pasmo 

-   Utwórz nowy dokument i wybierz środowisko pracy ![](images/Workbench_PartDesign.svg ) **Projekt Części**.



### Utwórz szkic 

-   Utwórz <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nowy szkic** na płaszczyźnie XY.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

-   Narysuj <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Utwórz wpust](Sketcher_CreateSlot/pl.md),
    -   Kliknij, aby umieścić pierwszy środek,
    -   Przesuń, aby zdefiniować długość i promień,
    -   Kliknij, aby ustawić drugi środek.

<img alt="" src=images/TBHS2-1.JPG  style="width:800px;">

Masz teraz pływający wpust o nieokreślonych wymiarach.

-   Kliknij jedną z poziomych linii wpustu.
-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wpisz {{Value|75 mm}} i kliknij **OK**.
    -   Dotyczy to stojaka na 3 główki, policz 25 mm dla każdej, jeśli chcesz więcej

<img alt="" src=images/TBHS2-2.JPG  style="width:800px;">

-   Kliknij jeden punkt linii poziomej
-   Kliknij na jeden punkt drugiej poziomej linii
-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź {{Value|29 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-3.JPG  style="width:800px;">

-   Narysuj <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Utwórz wpust](Sketcher_CreateSlot/pl.md) wokół pierwszego wpustu.

<img alt="" src=images/TBHS2-4.JPG  style="width:800px;">

-   Spraw, aby środki drugiego wpustu pokrywały się ze środkami pierwszego wpustu za pomocą <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [wiązania zbieżności](Sketcher_ConstrainCoincident/pl.md).

<img alt="" src=images/TBHS2-5.JPG  style="width:800px;">

-   Kliknij na jeden punkt poziomej linii pierwszego wpustu.
-   Kliknij na jeden punkt najbliższej poziomej linii drugiego wpustu.
-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź {{Value|3 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-6.JPG  style="width:800px;">

-   Aby szkic był w pełni związany:
    -   Kliknij lewy dolny punkt drugiego wpustu,
    -   Kliknij na początek planu XY,
    -   Kliknij na <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md).

<img alt="" src=images/TBHS2-7.JPG  style="width:800px;">

-   Aby opuścić szkic, kliknij przycisk **Zamknij** po lewej stronie lub ikonę <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> na pasku narzędzi lub naciśnij **ESC**.

<img alt="" src=images/TBHS2-8.JPG  style="width:800px;">



### Utwórz wyciągnięcie 

-   Kliknij na widok <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Aksonometryczny** wśród standardowych widoków, aby lepiej zobaczyć, co się stanie.
-   Kliknij na <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Wyciągnij**.
-   Wprowadź wartość {{Value|30 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-9.JPG  style="width:800px;">



### Utwórz na nim szkic 

-   Wybierz górną powierzchnię

<img alt="" src=images/TBHS2-10.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Utwórz szkic**. Ponieważ wybrano ścianę, nie zostanie wyświetlony monit o wybranie płaszczyzny.

<img alt="" src=images/TBHS2-11.JPG  style="width:800px;">

-   Narysuj <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Sześciokąt](Sketcher_CreateHexagon/pl.md).
    -   Kliknij, aby umieścić środek,
    -   Przesuń, aby zdefiniować promień,
    -   Kliknij, aby ustawić.

<img alt="" src=images/TBHS2-12.JPG  style="width:800px;">

-   Kliknij na krawędź sześciokąta.
-   Kliknij na <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> [Zwiąż w poziomie](Sketcher_ConstrainHorizontal/pl.md)

<img alt="" src=images/TBHS2-13.JPG  style="width:800px;">

-   Kliknij na środek sześciokąta.
-   Kliknij na poziomą linię płaszczyzny XY
-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź wartość {{Value|15 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-14.JPG  style="width:800px;">

-   Kliknij środek sześciokąta
-   Kliknij pionową płaszczyznę XY
-   Kliknij <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź {{Value|10 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-15.JPG  style="width:800px;">

Kliknij niebieski okrąg sześciokąta.

-   Kliknij na <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;">. [Wiązanie promienia](Sketcher_ConstrainRadius/pl.md)
-   Okno dialogowe wyświetli monit o ustawienie wymiaru. Wprowadź {{Value|8 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-16.JPG  style="width:800px;">

-   Aby opuścić szkic, kliknij przycisk **Zamknij** po lewej stronie lub ikonę <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> na pasku narzędzi lub naciśnij **ESC**.

<img alt="" src=images/TBHS2-17.JPG  style="width:800px;">



### Utwórz otwór 

-   Kliknij na widok <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Aksonometryczny** wśród standardowych widoków, aby lepiej zobaczyć, co się stanie.
-   Kliknij na [32px](Plik:PartDesign_Pocket.svg.md) [Kieszeń](PartDesign_Pocket/pl.md).
-   Wybierz *do pierwszego* z rozwijanego menu i kliknij **OK**.

<img alt="" src=images/TBHS2-18.JPG  style="width:800px;">



### Powtarzanie liniowe 

-   W widoku złożonym po lewej stronie, wybierz widok drzewa zamiast kontekstowego menu zadań, kliknij cechę kieszeni.
-   Kliknij na <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Szyk liniowy](PartDesign_LinearPattern/pl.md).
-   Ustaw długość na {{Value|55 mm}} i liczbę wystąpień na {{Value|3}}, a następnie kliknij **OK**.

<img alt="" src=images/TBHS2-19.JPG  style="width:800px;">



### Utwórz na nim szkic 

-   Wybierz wewnętrzną ścianę

<img alt="" src=images/TBHS2-20.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Utwórz szkic**. Ponieważ wybrano ścianę, nie zostanie wyświetlony monit o wybranie płaszczyzny.

<img alt="" src=images/TBHS2-21.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [Utwórz okrąg](Sketcher_CreateCircle/pl.md), kliknij, aby umieścić środek, przesuń kursor i kliknij, aby zdefiniować promień.

<img alt="" src=images/TBHS2-22.JPG  style="width:800px;">

-   Kliknij na środek okręgu.
-   Kliknij na poziomą linię płaszczyzny XY.
-   Kliknij na <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź wartość {{Value|15 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-23.JPG  style="width:800px;">

-   Kliknij środek okręgu.
-   Kliknij pionową płaszczyznę XY.
-   Kliknij <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
-   Pojawi się okno dialogowe z prośbą o ustawienie wymiaru. Wprowadź {{Value|10 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-24.JPG  style="width:800px;">

-   Kliknij na okrąg.
-   Kliknij na <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Wiązanie promienia](Sketcher_ConstrainRadius/pl.md)
-   Okno dialogowe wyświetli monit o ustawienie wymiaru. Wprowadź {{Value|3,5 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-25.JPG  style="width:800px;">

-   Aby opuścić szkic, kliknij przycisk **Zamknij** po lewej stronie lub ikonę <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> na pasku narzędzi lub naciśnij **ESC**.

<img alt="" src=images/TBHS2-26.JPG  style="width:800px;">



### Utwórz wyciągnięcie 

-   Kliknij na widok <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Aksonometryczny** wśród standardowych widoków, aby lepiej zobaczyć, co się stanie.
-   Kliknij na <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Wyciągnięcie**.
-   Wprowadź {{Value|4 mm}} i kliknij **OK**.

<img alt="" src=images/TBHS2-27.JPG  style="width:800px;">



### Powtarzanie liniowe 

-   W widoku złożonym po lewej stronie, wybierz widok drzewa zamiast kontekstowego menu zadań, kliknij cechę wyciągnięcia.
-   Kliknij na <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Szyk liniowy](PartDesign_LinearPattern/pl.md).
-   Ustaw długość na {{Value|55 mm}} i liczbę wystąpień na {{Value|3}}, a następnie kliknij **OK**.

<img alt="" src=images/TBHS2-28.JPG  style="width:800px;">



### Pochylenie ścian 

-   Wybierz krawędź każdego okrągłego wyciągnięcia.

<img alt="" src=images/TBHS2-29.JPG  style="width:800px;">

-   Kliknij na <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Pochylenie ścian](PartDesign_Draft/pl.md).
-   Ustaw kąt szkicu na {{Value|40°}}.
-   Kliknij \"Płaszczyzna neutralna\" i wybierz powierzchnię, na której rysowany jest szkic.
-   Zaznacz opcję \"Odwróć kierunek wyciągnięcia\".

<img alt="" src=images/TBHS2-30.JPG  style="width:800px;">

Mogliśmy użyć sfazowania, aby zrobić coś podobnego, ale w tym przypadku bardziej odpowiednie jest pochylenie.

Faza = lewa / Pochylenie = prawa

<img alt="" src=images/TBHS2-30-chamfer.JPG  style="width:200px;"><img alt="" src=images/TBHS2-30-draft.JPG  style="width:200px;">



### Wykończenia

-   Przytrzymując klawisz **CTRL** wybierz dolną i górną powierzchnię.

<img alt="" src=images/TBHS2-31-bottom.JPG  style="width:200px;"><img alt="" src=images/TBHS2-31-top.JPG  style="width:200px;">

-   -   Dodaj <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Sfazowanie** {{Value|0,5 mm}}.

<img alt="" src=images/TBHS2-31.JPG  style="width:800px;">

Perfekcyjnie!



## Eksport do pliku .STL 

-   W widoku Combo po lewej stronie, wybierz widok drzewa zamiast kontekstowego menu zadań, kliknij ostatnią cechę *(fazę)*.

<img alt="" src=images/TBHS2-32.JPG  style="width:800px;">

-   Teraz możesz wybrać \"Eksportuj\...\" z menu Plik w lewym górnym rogu i wybrać format pliku .STL.
-   Wydrukuj go zamiast pierwszej wersji lub zastąp go, jeśli ostatecznie się zepsuł ;-)


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Toothbrush Head Stand/pl
