# Sketcher Micro Tutorial - Constraint Practices/pl
{{TutorialInfo/pl
|Topic=Modelowanie
|Level=początkujący
|Time=30 minut
|Author=Mark Stephen ([Quick61](User:Quick61.md)) and vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&p=371659#p371659 Sketcher: wiązania praktycznie]
}}

## Wprowadzenie

Ten tutorial został pierwotnie napisany przez Quick61 i został zaktualizowany i odnowiony przez vocx.

## Witamy

Ten poradnik ma na celu pomóc nowemu użytkownikowi FreeCAD zapoznać się z technikami i najlepszymi praktykami dotyczącymi tworzenia wiązań [szkicu](Sketch.md) oraz przepływem pracy Środowiska <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/pl.md).

Istnieje ogólna zasada dotycząca wiązań szkicownika FreeCAD, im mniej jest **wiązań wymiarów**, tym lepiej.

Lepiej jest używać **wiązania geometryczne** w miejsce wymiarowego, jeśli to możliwe. Ma to związek z wewnętrznym działaniem algorytmu wyliczającego wiązania Środowiska Sketcher.

## Sposób postępowania 

1\. Uruchom program FreeCAD, utwórz nowy pusty dokument przez menu **Plik → <img src=images/Std_New.svg style="width:16px"> [Nowy](Std_New.md)**.

:   1.1. Przełacz interfejs na Środowisko pracy [Sketcher](Sketcher_Workbench/pl.md) z [paska narzędzi Środowisko](Std_Workbench.md), lub menu **[Widok](Std_View_Menu/pl.md) → Środowisko → Sketcher**.

Kilka działań do zapamiętania:

-   Naciśnij prawy przycisk myszy, lub naciśnij jeden raz klawisz **Esc** na klawiaturze, aby wyłączyć aktywne narzędzie w trybie edycji.
-   Aby wyjść z trybu edycji szkicu, naciśnij przycisk **Zamknij** w [panelu zadań](task_panel.md), lub naciśnij dwukrotnie klawisz **Esc** na klawiaturze.
-   Aby ponownie wejść w tryb edycji, kliknij dwukrotnie na obiekt szkicu w <img src=images/Sketcher_EditSketch.svg style="width:widoku drzewa](tree_view.md), lub wybierz go, a następnie kliknij na przycisk **[16px">. [Edycja szkicu](Sketcher_EditSketch.md)**.

## Utwórz szkic 

2\. Kliknij w przycisk **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [Utwórz nowy szkic](Sketcher_NewSketch.md)**.

:   2.1. Wybierz orientację szkicu, czyli jedną z płaszczyzn bazowych XY, XZ lub YZ. Będziemy korzystać z ustawień domyślnych dla płaszczyzny i opcji.
:   2.2 Kliknij **OK**, aby rozpocząć tworzenie szkicu.


**Uwaga:**

w [panelu zadań](task_panel.md) rozwinąć sekcję **Edycja kontrolek** i upewnić się, że opcja **Automatyczne wiązania** jest wyłączona. Wyłącz również przyciąganie do siatki i ukryj siatkę.

## Podejście pierwsze: wiązania dotyczące danych 

3\. Narysujemy całkowicie związany kwadrat, wyśrodkowany w punkcie początku układu współrzędnych.

:   3.1. Kliknij na **<img src="images/Sketcher_CreatePolyline.svg" width=16px> [Utwórz polilinię ...](Sketcher_CreatePolyline/pl.md)**, a następnie wytycz cztery linie w ogólnym kształcie prostokąta, wokół punktu początku.

<img alt="" src=images/01a_Sk02_Sketcher_Rectangle_unconstrained.png  style="width:" height="400px;"> 
*Szkic prostokąta bez wiązań.*

:   3.2. Wybierz pierwszą linię poziomą i naciśnij przycisk **<img src=images/_Constraint_HorizontalDistance.svg style="width:16px"> [Ustal poziomą odległość](Sketcher_ConstrainDistanceX/pl.md)**, wprowadź wartość {{Value|20mm}}.
:   3.3. Wybierz drugą linię poziomą i nadaj wiązanie z tą samą długością.
:   3.4. Wybierz pierwszą linię pionową i naciśnij przycisk **<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Ustal pionową odległość](Sketcher_ConstrainDistanceY/pl.md)**, wprowadź wartość {{Value|20mm}}.
:   3.5. Wybierz drugą linię pionową i nadaj wiązanie z tą samą długością.
:   3.6. Wybierz jeden dolny punkt narożny *(a)* i punkt początku szkicu, naciśnij **<img src=images/Constraint_HorizontalDistance.svg  style="width: 16px"> [Ustal poziomą odległość](Sketcher_ConstrainDistanceX/pl.md)**, a następnie wpisz {{Value|10mm}}.
:   3.7. Wybierz górny punkt narożnika *(b)* powyżej punktu narożnika *(a)* oraz punkt początku szkicu, a następnie powtórnie zastosuj wiązanie poziome z taką samą odległością.
:   3.8. Wybierz inny dolny punkt narożnika *(c)*, oraz punkt początkowy szkicu i naciśnij **<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Ustal pionową odległość](Sketcher_ConstrainDistanceY/pl.md)**, a następnie wpisz {{Value|10mm}}.
:   3.9. Wybierz ponownie górny punkt narożny *(b)* i początek szkicu, a następnie ponownie utwórz wiązanie pionowe z taką samą odległością.

<img alt="" src=images/01b_Sk02_Sketcher_Rectangle_constrained_lengths_1.png  style="width:" height="400px;"> <img alt="" src=images/01c_Sk02_Sketcher_Rectangle_constrained_lengths_2.png  style="width:" height="400px;"> 
*Z lewej: wiązania dotyczące wymiarów dla boków. Z prawej: dodatkowe wiązania odległości wewnętrznych.*

Patrząc na sekcję **Wiązania** w [Panelu zadań](task_panel/pl.md), widzimy, że istnieje zbyt wiele wiązań. Zaburzają one również widok szkicu. Wiązania te są również skomplikowane obliczeniowo dla solvera. Choć nie stanowi to problemu z prostym kształtem, to jednak może on stać się jednym z bardziej złożonych kształtów.

## Lepsza droga: wymiary i wiązania geometryczne 

4\. Narysujemy całkowicie związany kwadrat, wyśrodkowany w punkcie początku układu współrzędnych. Podczas tworzenia nowego szkicu, upewnij się, że opcja **Automatyczne wiązania** jest wyłączona.

:   4.1. Kliknij na **<img src="images/Sketcher_CreatePolyline.svg" width=16px> [Utwórz polilinię ...](Sketcher_CreatePolyline/pl.md)**, a następnie wytycz cztery linie w ogólnym kształcie prostokąta, wokół punktu początku.
:   4.2. Zaznacz jedna z linii poziomych, i kliknij na przycisk **<img src=images/Constraint_Horizontal.svg style="width:16px"> [Utwórz wiązanie poziome](‎Sketcher_ConstrainHorizontal/pl.md)**.
:   4.3. Zaznacz kolejna linię poziomą i powtórz tworzenie wiązania.
:   4.4. Zaznacz jedna z linii pionowych, i kliknij na przycisk **<img src=images/Constraint_Vertical.svg style="width:16px"> [Utwórz wiązanie pionowe](‎Sketcher_ConstrainVertical/pl.md)**.
:   4.5. Zaznacz kolejna linię pionową i powtórz tworzenie wiązania.

<img alt="" src=images/02a_Sk02_Sketcher_Rectangle_constrained_horizontal-vertical.png  style="width:" height="400px;"> 
*Wiązania geometryczne poziome i pionowe.*

:   4.6. Zaznacz pierwszą z linii poziomych, i naciśnij przycisk **<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Ustal poziomą odległość](Sketcher_ConstrainDistanceX/pl.md)**, wprowadź wartość {{Value|20mm}}. Obserwujemy, że druga pozioma linia zmienia rozmiar w tym samym czasie.
:   4.7. Zaznacz pierwszą z linii pionowych, i naciśnij przycisk **<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Ustal pionową odległość](Sketcher_ConstrainDistanceY/pl.md)**, wprowadź wartość {{Value|20mm}}. Obserwujemy, że druga pionowa linia zmienia rozmiar w tym samym czasie.
:   4.8. Zaznacz jeden dolny punkt narożny *(a)* i punkt początku szkicu, naciśnij przycisk **<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Ustal poziomą odległość](Sketcher_ConstrainDistanceX/pl.md)**, wprowadź wartość {{Value|10mm}}.
:   4.9. Zaznacz punkt narożny *(b)* powyżej poprzednio używanego punktu *(a)* oraz punkt początku szkicu, naciśnij przycisk **<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Ustal pionową odległość](Sketcher_ConstrainDistanceY/pl.md)**, wprowadź wartość {{Value|10 mm}}.

<img alt="" src=images/02b_Sk02_Sketcher_Rectangle_constrained_lengths_1.png  style="width:" height="400px;"> <img alt="" src=images/02c_Sk02_Sketcher_Rectangle_constrained_lengths_2.png  style="width:" height="400px;"> 
*Z lewej: wiązania dotyczące wymiarów tylko dwóch boków. Z prawej: dodatkowe wiązania dotyczące tylko dwóch odległości wewnętrznych.*

W porównaniu do pierwszego, ten szkic jest związany znacznie lepiej. Poziome i pionowe wiązania geometryczne pozwalają nam na zastosowanie mniejszej liczby wiązań w układzie odniesienia. Dzięki czemu nasz szkic wygląda bardziej przejrzyście.

## Schemat optymalny: przede wszystkim wiązania geometryczne 

5\. Narysujemy ten sam kwadrat, w pełni związany i wyśrodkowany w punkcie początku układu współrzędnych. Podczas tworzenia nowego szkicu, upewnij się, że opcja **Automatyczne wiązania** jest wyłączona.

:   5.1. Kliknij na **<img src="images/Sketcher_CreatePolyline.svg" width=16px> [Utwórz polilinię ...](Sketcher_CreatePolyline/pl.md)**, a następnie wykreśl cztery linie w ogólnym kształcie prostokąta wokół punktu początku.
:   5.2. Zaznacz jedna z linii poziomych, i kliknij na przycisk **<img src=images/Constraint_Horizontal.svg style="width:16px"> [Utwórz wiązanie poziome](‎Sketcher_ConstrainHorizontal.md)**.
:   5.3. Zaznacz kolejna linię poziomą i powtórz tworzenie wiązania.
:   5.4. Zaznacz jedna z linii pionowych, i kliknij na przycisk **<img src=images/Constraint_Vertical.svg style="width:16px"> [Utwórz wiązanie pionowe](‎Sketcher_ConstrainVertical.md)**.
:   5.5. Zaznacz kolejna linię pionową i powtórz tworzenie wiązania.

<img alt="" src=images/03a_Sk02_Sketcher_Rectangle_constrained_horizontal-vertical.png  style="width:" height="400px;"> 
*Wiązania geometryczne poziome i pionowe.*

:   5.6. Wybierz jeden dolny narożnik *(a)*, a następnie górny narożnik, który znajduje się po przekątnej, oraz punkt początku szkicu. Następnie naciśnij **<img src=images/Constraint_Symmetric.svg style="width:16px"> [Utwórz wiąz symetrii](Sketcher_ConstrainSymmetric.md)**. Dwa wybrane narożniki zostaną ustawione w równej odległości od punktu środkowego.
:   5.7. Wybierz dwa przylegające boki prostokąta *(połączone w jednym rogu)* i naciśnij przycisk **<img src=images/Constraint_EqualLength.svg style="width:16px"> [Utwórz wiązanie równości](Sketcher_ConstrainEqual.md)**. Zauważ, że ze względu na symetrię punktów narożnych, wszystkie boki mają teraz tę samą długość.

<img alt="" src=images/03b_Sk02_Sketcher_Rectangle_constrained_symmetric.png  style="width:" height="400px;"> <img alt="" src=images/03c_Sk02_Sketcher_Rectangle_constrained_equal_length.png  style="width:" height="400px;"> 
*Po lewej: Wiązanie symetrii dla dwóch punktów narożnych. Po prawej: dodatkowo jednakowa długość tylko dla dwóch sąsiednich boków..*

:   5.8. Zaznacz jedna z poziomych linii i naciśnij przycisk **<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Ustal pozioma odległość ...](Sketcher_ConstrainDistanceX.md)**, wprowadź wartość {{Value|20mm}}. Ze względu na dodane wcześniej wiązania symetryczne i równości długości, widzimy, że wszystkie boki stają się równe w tym samym czasie.

<img alt="" src=images/03d_Sk02_Sketcher_Rectangle_constrained_length.png  style="width:" height="400px;"> 
*Zastosowano wszystkie wiązania geometryczne i jedno wiązanie wymiarowe dla długości boku.*

Jest to najlepszy sposób na związanie tego szkicu, ponieważ użyliśmy tylko jednego wiązania danych *(wymiarowego)*.

## Dodatkowe zasoby 

-   [Poradnik: Podstawy dla Środowiska pracy Sketcher](Basic_Sketcher_Tutorial/pl.md)
-   [Sketcher - powiązania](Sketcher_reference.md)
-   [Poradnik dla Środowiska pracy Sketcher](Sketcher_Tutorial/pl.md)


{{Tutorials navi

}} {{Sketcher Tools navi}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Micro Tutorial - Constraint Practices/pl
