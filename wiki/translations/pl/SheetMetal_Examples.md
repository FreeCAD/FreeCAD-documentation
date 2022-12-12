# SheetMetal Examples/pl
{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:24px;"> [Arkusz Blachy](SheetMetal_Workbench/pl.md) *(jest [zewnętrznym środowiskiem](External_workbenches/pl.md) dostępnym poprzez [Menadżer dodatków](Std_AddonMgr/pl.md))* stało się bardzo rozbudowane i wymaga odpowiedniej dokumentacji.

Aby uniknąć przepełnienia stron narzędziowych przykładami, dodano tę stronę w celu zebrania części pokazujących i wyjaśniających specjalne możliwości środowiska Arkusz Blachy.

Zaplanowane etapy tworzenia treści:

1.  Zbieranie zdjęć
2.  Dodawanie opisów przepływów pracy
3.  Dodawanie bardziej szczegółowych samouczków

## Zawias

<img alt="" src=images/SheetMetal_Example-01.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width:200px;"> 
*Przepływ pracy Zawias:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [Projekt części: Kieszeń](PartDesign_Pocket/pl.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [Projekt Części: Otwór](PartDesign_Hole/pl.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Zawias - krok po kroku 


<div class="mw-collapsible-content toccolours">

1.  Utwórz profil *(linię i łuk styczny)*, najlepiej korzystając ze środowiska <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicownik](Sketcher_Workbench/pl.md).
2.  Aktywuj funkcję <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md), aby utworzyć obiekt bazowy wyginania.
3.  Edytuj parametry obiektu bazowego wyginania:
    -   Ustaw wartość parametru **Płaszczyzna środkowa** na {{TRUE/pl}}, aby profil rozciągał się symetrycznie na obie strony płaszczyzny szkicu.
    -   Ustaw parametry **promień** i **grubość** na wybrane wartości.
4.  Utwórz kontur do wycięcia za pomocą środowiska <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicownik](Sketcher_Workbench/pl.md).
5.  Użyj funkcji <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Projekt Części: Kieszeń](PartDesign_Pocket/pl.md), aby odciąć jedną połowę okrągłego kawałka.
6.  Utwórz wzór otworu za pomocą środowiska <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicownik](Sketcher_Workbench.md).
7.  Użyj polecenia <img alt="" src=images/PartDesign_Hole.svg  style="width:16px;"> [Projekt Części: Otwór](PartDesign_Hole.md). Unikaj opcji pogłębiania i pogłębiania stożkowego, aby zachować możliwość rozłożenia korpusu.
8.  Aktywuj polecenie <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md), aby uzyskać obiekt w rozwinięciu.
9.  Gotowe!


</div>


</div>

## Klips do papieru 

<img alt="" src=images/SheetMetal_Example-02.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width:200px;"> 
*Przepływ pracy Klips do papieru:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Arkusz Blachy: Szkic na arkuszu](SheetMetal_SketchOnSheet/pl.md)**,
klonowanie, odwracanie i łączenie,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Klips do papieru - krok po kroku 


<div class="mw-collapsible-content toccolours">

1.  Utwórz profil na płaszczyźnie XZ, najlepiej używając środowiska <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicownik](Sketcher_Workbench/pl.md).
    <img alt="Szkic profilu" src=images/SheetMetal_Example-02e.png  style="width:300px;">
2.  Aktywuj funkcję: <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Dodaj element bazowy](SheetMetal_AddBase/pl.md) , aby utworzyć obiekt bazowy wyginania.
3.  Edytuj parametry obiektu bazowego wyginania w panelu ustawień:
    <img alt="Obiekt bazowy wyginania z podświetlonym szkicem." src=images/SheetMetal_Example-02f.png  style="width:200px;">
    -   Ustaw wartość parametru **Płaszczyzna środkowa** na {{TRUE/pl}} aby profil rozciągał się symetrycznie na obie strony płaszczyzny szkicu.
    -   Ustaw wartość parametru **Długość** na {{Value|32 mm}}.
    -   Ustaw wartość parametru **Promień** na {{Value|2 mm}}.
    -   Ustaw wartość parametru **Grubość** na {{Value|0.3 mm}}.
4.  Wybierz powierzchnię pomiędzy okrągłymi sekcjami i aktywuj środowisko pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicownik](Sketcher_Workbench/pl.md).
    <img alt="Płaszczyzna do umieszczenia szkicu." src=images/SheetMetal_Example-02g.png  style="width:200px;">
5.  Aby ukryć zawiniętą część użyj funkcji <img alt="" src=images/Sketcher_ViewSection.svg  style="width:16px;"> [Widok przekroju](Sketcher_ViewSection/pl.md).
6.  Utwórz kontur wycięcia.
    <img alt="Kontur wycięcia." src=images/SheetMetal_Example-02h.png  style="width:" height="240px;"> <img alt="Wycięty kontur lekko dotykający wybranej powierzchni" src=images/SheetMetal_Example-02i.png  style="width:" height="240px;">
7.  Zakończ rysowanie używając funkcji <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Opuść szkic](Sketcher_LeaveSketch/pl.md).
8.  Ponownie wybierz powierzchnię ściany i dodaj do zaznaczenia szkic wycięcia.
    <img alt="Powierzchnia z zaznaczonym szkicem." src=images/SheetMetal_Example-02j.png  style="width:200px;">
9.  Użyj polecenia <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Szkic na arkuszu](SheetMetal_SketchOnSheet/pl.md), aby wykonać wycięcie wzdłuż zakręconego fragmentu.
    <img alt="Zakończona pierwsza połowa." src=images/SheetMetal_Example-02b.png  style="width:200px;">
10. Jedna strona jest skończona. Teraz musimy znaleźć sposób na lustrzane odbicie korpusu.

**Potencjalne opcje wykonania odbicia lustrzanego:**

-   Polecenie <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [Projekt Części: Odbicie lustrzane](PartDesign_Mirrored/pl.md) polecenie kończy się niepowodzeniem, ponieważ z jakiegoś powodu nie może obsługiwać elementów środowiska Arkusz Blachy. Tak więc to nie działa.
-   Polecenie <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [Część: Odbicie lustrzane](Part_Mirror/pl.md) polecenie tworzy część w odbiciu lustrzanym, ale nie jest ona już rozkładana. Więc to też nie działa.
-   Jednym sposobem, który działa, jest użycie klonu. To nadal nie jest odbicie lustrzane, ale może używać symetrii osiowej *(obróć go o 180°)*.
-   Innym sposobem, który działa, jest użycie obiektu odnośnika.

**Odbicie lustrzane z zastosowaniem klonu:**

1.  Zaznacz Zawartość z widoku drzewa.
2.  Skorzystaj z polecenia <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [Projekt Części: Utwórz klon](PartDesign_Clone/pl.md). Doda nową Zawartość z obiektem klonu.

Aby zastosować obrót o 180°, ustaw parametr **Kąt** we właściwości Umiejscowienie Zawartości lub klonu na wartość {{Value|180°}}. *(Oś Z jest domyślna i powinna być odpowiednia, jeśli zacząłeś na płaszczyźnie XZ, jak zalecano na wstępie)*.
<img alt="Klonowana połowa" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="Odwrócona sklonowana połowa" src=images/SheetMetal_Example-02l.png  style="width:200px;">

1.  Mając wciąż aktywną Zawartość, użyj polecenia <img alt="link" src=images/PartDesign_Boolean.svg  style="width:16px;"> [Projekt Części: Funkcje logiczne](PartDesign_Boolean/pl.md) aby dodać Zawartość klonu i połączyć obie połówki.
    <img alt="Połączone połówki" src=images/SheetMetal_Example-02c.png  style="width:200px;">
2.  Uruchom funkcję <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Rozwiń](SheetMetal_Unfold/pl.md) aby otrzymać obiekt rozwinięcia.
    <img alt="Obiekt wycięty i rozwinięty" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Obiekt rozwinięty" src=images/SheetMetal_Example-02d.png  style="width:200px;">
3.  Gotowe!

**Odbicie lustrzane z zastosowaniem obiektu łącza:**

1.  Wybierz Zawartość z widoku drzewa.
2.  Użyj narzędzia <img alt="" src=images/Std_LinkMake.svg  style="width:16px;"> [Utwórz łącze](Std_LinkMake/pl.md). Stworzy to nowy obiekt łącza.
3.  Powiel obiekt łącza, ustawiając wartość właściwości **Liczba elementów** na {{Value|2}}.
4.  Aby zastosować obrót o 180° ustaw wartość właściwości **Kąt** pod właściwością Umiejscowienia któregokolwiek z obiektów łącza podrzędnego na {{Value|180°}}. *(Oś Z jest domyślna i powinna być odpowiednia, jeśli zacząłeś na płaszczyźnie XZ, jak zalecano na wstępie)*.


</div>


</div>

## Klamra Omega 

<img alt="" src=images/SheetMetal_Example-03.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width:200px;"> 
*Przepływ pracy Klamra Omega:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [Projekt Części: Otwór](PartDesign_Hole/pl.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [Projekt Części: Zaokrąglenie](PartDesign_Fillet/pl.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}

## Sześciokątna miska 

<img alt="" src=images/SheetMetal_Example-04.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width:200px;"> 
*Przepływ pracy Sześciokątna misa:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Arkusz Blachy: Dodaj ścianę](SheetMetal_AddWall/pl.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Arkusz Blachy: Dodaj podcięcie w narożniku](SheetMetal_AddCornerRelief/pl.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width:200px;">

Po dodaniu podcięcia narożnego *(prawa strona)* może być konieczne dostosowanie wartości właściwości **Rozmiar**.

## Klips do długopisu 

<img alt="" src=images/SheetMetal_Example-05.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width:200px;"> 
*Przepływ pracy Klips do długopisu:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [Projekt Części: Kieszeń](PartDesign_Pocket/pl.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Arkusz Blachy: Dodaj ścianę](SheetMetal_AddWall/pl.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}

## Przykład przedłużenia ściany 

<img alt="" src=images/SheetMetal_Example-06.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width:200px;"> 
*Przepływ pracy Przykład przedłużenia ściany:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Arkusz Blachy: Dodaj ścianę](SheetMetal_AddWall/pl.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Arkusz Blachy: Wyciągnij](SheetMetal_Extrude/pl.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Arkusz Blachy: Wyciągnij](SheetMetal_Extrude/pl.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}

Przy drugim użyciu **Wyciągnięcia ściany** do kształtu przedłużenia (przedłużeń) używany jest szkic z dwoma konturami, a przy wartości parametru \"użyj odjęcia\" ustawionej na wartość {{true/pl}} zapewnia on kształt dla wycięć, jak również

## Korpus złącza USB 

<img alt="" src=images/SheetMetal_Example-07.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width:200px;"> 
*Przepływ pracy Korpus złącza USB:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Arkusz Blachy: Wyciągnij](SheetMetal_Extrude/pl.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [Projekt Części: Kieszeń](PartDesign_Pocket/pl.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Arkusz Blachy: Wyciągnij](SheetMetal_Extrude/pl.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Arkusz Blachy: Dodaj ścianę](SheetMetal_AddWall/pl.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Arkusz Blachy: Rozwiń](SheetMetal_Unfold/pl.md)**.
}}

*(Płaskorzeźba jest tylko artystycznym wyrazem tego, co może być ukryte wewnątrz prawdziwej wtyczki)*.

## Właściwości środowiska pracy Arkusz Blachy 

W tym rozdziale staramy się wyjaśnić właściwości każdego obiektu środowiska Arkusz Blachy za pomocą prostych obrazków, jeśli to możliwe.


<div class="mw-collapsible mw-collapsed">

### Obiekt bazowy wyginania <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

<img alt="" src=images/SheetMetal_Example-08a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08b.png  style="width:200px;">



*Wybrany szkic + 
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Arkusz Blachy: Dodaj element bazowy](SheetMetal_AddBase/pl.md)* 
→ Obiekt bazowy wyginania z domyślnymi nastawami**

<img alt="" src=images/SheetMetal_Example-08b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08c.png  style="width:200px;">



*Edycja **Długość*: Długość domyślnie → Długość skrócona**

<img alt="" src=images/SheetMetal_Example-08d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08h.png  style="width:200px;">



*Przełącznik **Płaszczyzna środkowa* z {{False/pl** na {{TRUE/pl}}: Wyciągnięcie w jednym kierunku → Wyciągnięcie symetryczne}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;">



*Pezełącznik **Odwrócony* z {{False/pl** na {{TRUE/pl}}: Kierunek domyślny → Kierunek przeciwny}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08f.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08g.png  style="width:200px;">



*Wybór **Strona wygięcia*: {{value|Na zewnątrz** ''(domyślnie)'' → {{value|Do wewnątrz}} → {{value| Pośrodku}}}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08i.png  style="width:200px;">



*Edycja **Promień*: Promień domyślnie → Promień powiększony.<br>
Właściwość ta, to wewnętrzny promień zagięć tworzonych w wierzchołkach, w których dwie krawędzie w szkicu mają przejście nie styczne.**

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08j.png  style="width:200px;">



*Edycja **Grubość*: Grubość domyślnie → Grubość powiększona**


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Obiekt wyginania <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Obiekt Wyginania składa się z zestawów składających się z jednego cylindrycznego zgięcia i jednej płaskiej ścianki. Każda para rozciąga się od wybranej krawędzi półfabrykatu.

<img alt="" src=images/SheetMetal_Example-09a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09b.png  style="width:200px;">



*Wybrane krawędzie + 
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Dodaj ścianę](SheetMetal_AddWall/pl.md)* 
→ Obiekt <br> wyginania z ustawieniami domyślnymi
''(Dwa obiekty wyginania w dwóch oddzielnych Zawartościach)''.**

Edycja **Promień** aby zmienić wewnętrzny promień wszystkich zagięć dostarczonych przez obiekt wyginania. *(Patrz obiekt bazowy wyginania powyżej.)*

Edycja **Długość** aby zmienić długość wszystkich płaskich pasków wystających z zagięć obiektu wyginania.

:   Nie mylić właściwości **Długość** z długością kołnierza, która jest sumą tej długości, promienia i grubości *(tylko 90°)*.

<img alt="" src=images/SheetMetal_Example-09b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;">



*Przełcznik **Odwrócony* z {{FALSE/pl** na {{TRUE/pl}}: Kołnierze domyślnie ''(obiekty typu wygięcie)'' → Kołnierze odwrócone}}

<img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09e.png  style="width:200px;">



*Edycja **Kąt*: Kąt domyślnie ''(90°)'' → Kąt powiększony → Kąt zmniejszony**

Nie musimy się przejmować przycinaniem krawędzi, ponieważ opcja **Automatyczne ukosowanie** jest domyślnie włączona.
Gdyby była wyłączona, wynik wyglądałby następująco:

<img alt="" src=images/SheetMetal_Example-09m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09f.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09g.png  style="width:200px;">



*Przełącznik **Automatyczne ukosowanie* z {{TRUE/pl** na {{FALSE/pl}}: Kąt domyślny ''(90°)'' → Kąt powiększony → Kąt zmniejszony<br>
''(Właściwość Automatyczne ukosowanie nie ma wpływu na pojedyncze kołnierze)''}}

Aby ręcznie ściąć krawędź obrzeża stosuje się właściwość **KątŚcięcia1** i **KątŚcięcia2**:

<img alt="" src=images/SheetMetal_Example-09m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09n.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09o.png  style="width:200px;">



*Edycja **KątŚcięcia1* oraz {{PropertyData|KątŚcięcia2**: Brak ścięcia ''(domyślnie)'' → Różnie ścięte krawędzie, kąt dodatni → Symetrycznie ścięte krawędzie, kąt ujemny}}

Ścinanie działa tylko na płaskie ścianki, a nie na zagięcia.

:   *(Uwzględnia całą krawędź i dlatego nie może być stosowane do ukosowania krawędzi kołnierzy)*.

Aby pokazać różne możliwości wyboru **typu zagięcia** wprowadzamy pomocniczy prostopadłościan, który wycina się z tego samego obrysu co półfabrykat i ma taką samą wysokość jak obiekt Wygięcia *(jego długość kołnierza)*.

<img alt="" src=images/SheetMetal_Example-09h.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09i.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09j.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09k.png  style="width:200px;">



*Wybór **Typ zagięcia*: {{Value|Materiał na zewnątrz** ''(domyślnie)'' → {{Value|Materiał do wewnątrz}} → {{Value|Grubość na zewnątrz}} → {{Value|Odsunięcie}}}}

-   Materiał na zewnątrz: Wygięcie zaczyna się od wybranej krawędzi *(Cały obiekt Wygięcia leży poza prostopadłościanem)*.
-   Materiał do wewnątrz: Zewnętrzna strona zgięcia kończy się na powierzchni prostopadłościanu *(Cały obiekt Wygięcia leży wewnątrz prostopadłościanu)*.
-   Grubość na zewnątrz: Wewnętrzna strona zagięcia kończy się na powierzchni prostopadłościanu *(z powierzchni prostopadłościanu wystaje tylko pasek planarny)*.
-   Odsunięcie: Zgodnie z wartością właściwości **Odsunięcie** zgięcie jest przesuwane w kierunku zewnętrznym od jego domyślnej pozycji.

:   Wstawiono rozszerzenie dla wartości dodatnich *(podświetlony pasek)*.
:   Dla wartości ujemnych dopuszcza się przesunięcie zgięcia do wewnątrz.

Jeśli nie chcemy wykorzystywać całej długości krawędzi możemy użyć właściwości **Przerwa1** i **Przerwa2**.

<img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09l.png  style="width:200px;">



*Edycja **Przerwa1* and {{PropertyData|Przerwa1**: Kołnierze domyślnie → Kołnierze z różnymi wartościami dla właściwości Przerwa1 i Przerwa2}}

Jeśli długość przerwy osiągnie lub przekroczy wartość **min podcięcia przerwy**, do przerwy zostanie dodane podcięcie.
Podcięcia są kontrolowane przez właściwości **Typ podcięcia**, **PodcięcieD** *(głębokość podcięcia)*, oraz **PodcięcieW** *(szerokość podcięcia)*, które są włączone tylko wtedy, gdy ustawiona jest wartość przerwy.

<img alt="" src=images/SheetMetal_Example-09p.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09q.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09r.png  style="width:200px;">



*Edycja **PodcięcieD* oraz {{PropertyData|PodcięcieW**: Wartości domyślne → Powiększona głębokość podcięcia→ Powiększona głębokość i szerokość podcięcia}}

<img alt="" src=images/SheetMetal_Example-09r.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09s.png  style="width:200px;">



*Przełącznik **Typ podcięcia* z {{value|Prostokątny** na {{value|Zaokrąglony}}: Domyślnie Podcięcie prostokątne → Podcięcie zaokrąglone}}

Opcja zaokrąglenia zostanie zastosowana tylko wtedy, gdy głębokość podcięcia jest większa niż jego szerokość.

Przełącz wartość właściwości **Użyj współczynnika szczeliny** z {{FALSE/pl}} *(domyślnie)* na {{TRUE/pl}}, aby automatycznie ustawić wartości **SzczelinaD** i **SzczelinaW**. Obie są ustawione na grubość *(dziedziczoną)* obiektu pomnożoną przez wartość **Współczynnik szczeliny**.

:   W tym przypadku opcja zaokrąglenia jest bezużyteczna, ponieważ głębokość szczeliny jest tak duża, jak jej szerokość. *(Patrz wyżej)*

Nowa właściwość **DługośćSpec** {{Version/pl|1.0}} umożliwia nam wybór sposobu pomiaru długości obiektu wygięcia:

<img alt="" src=images/SheetMetal_Example-09t.png  style="width:500px;"> 
*Widok z boku czterech kołnierzy 120° o domyślnej długości {{Value|10 mm* i różnych wartościach **Length Spec**: <br> {{value|Leg}} ''(domyślnie)'', {{value|Outer Sharp}}, {{value|Inner Sharp}}, {{value|Tangential}}}}

Przy wybranej opcji {{value|Tangential}} właściwość **Długość** jest odpowiednikiem długości kołnierza.

Wartości {{value|Outer Sharp}} i {{value|Tangential}} są identyczne dla kątów 90°.


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Obiekt wydłużenia <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Obiekt Wydłużenia rozciąga blachę na jednej lub kilku wybranych krańcach ściany lub krawędziach.

<img alt="" src=images/SheetMetal_Example-10a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10b.png  style="width:200px;">



*Wybrane krańce ściany lub krawędzie + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Wyciągnij](SheetMetal_Extrude/pl.md)* 
→ Jeden wydłużony obiekt z domyślnymi ustawieniami**

Pojawia się tu pierwszy problem: Mimo że wartość właściwości **Ulepsz** jest ustawiona na {{TRUE/pl}} dwa przedłużenia nadal pokazują swoje linie szwów. Tylko przedłużenie ostatniego wybranego elementu zostaje udoskonalone.

Aby ulepszyć wszystkie przedłużenia trzeba je utworzyć indywidualnie:

<img alt="" src=images/SheetMetal_Example-10c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10f.png  style="width:200px;">



*W trzech krokach wybrane krańce ściany lub krawędzie + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Wyciągnij](SheetMetal_Extrude/pl.md)* 
→ Trzy wydłużone obiekty z domyślnymi ustawieniami.**

Zmienione właściwości dotyczą wszystkich krawędzi wymienionych w powiązanym **Obiekcie bazowym** obiektu Wydłużenia.

Edytuj **długość** aby wyregulować długość przedłużenia.

<img alt="" src=images/SheetMetal_Example-10h.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-10g.png  style="width:200px;">



*Edytuj wartość parametru **szcelina1* oraz {{PropertyData|szczelina2** aby zmniejszyć szerokość rozszerzenia.<br>
Po lewej: Obiekt rozszerzenia z 3 krawędziami. Po prawej: Jeden z obiektów rozszerzenia z jedną pojedynczą krawędzią.}}

Połącz szkic z właściwością **Szkic**, aby nadać kształt przedłużeniu. Właściwości **długość**, **szczelina1** i **szczelina2** będą ignorowane po powiązaniu szkicu. *(Wydaje się, że nie działa to w przypadku wciąż niezgiętych półfabrykatów)*.

<img alt="" src=images/SheetMetal_Example-10i.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10j.png  style="width:200px;">



*Wybrany szkic leżący na kołnierzu, który ma być poszerzony → Uzyskane poszerzenie.*

Widać wyraźnie, że nie ma znaczenia, która krawędź została wybrana dla obiektu Rozszerzenie, kształt kołnierza jest zmieniany wszędzie tam, gdzie wystaje geometria szkicu, nowy kształt może nawet zawierać części, które są odłączone od oryginalnego kołnierza. Wielokrotne kontury nie stanowią problemu, ale kołnierz nie jest przycinany wgłąb.

Ten przykład pokazuje, że projektanci są odpowiedzialni za swoje konstrukcje i nie powinni polegać na wynikach swoich narzędzi, które w tym przypadku nie mają sensu. Szkic przymocowany do ściany kołnierza jest problematyczny również ze względu na problem związany z topologią nazw, ale dla tego przypadku rozwiązanie znajduje się w zasięgu wzroku.

Istnieją jednak lepsze przypadki użycia tego narzędzia obejmujące prawie zamknięte kształty, takie jak jeden z przykładów na stronie [Arkusz Blachy: Wyciągnij](SheetMetal_Extrude/pl.md):

<img alt="" src=images/SheetMetal_Example-10k.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10l.png  style="width:200px;">



*Prawie zamknięty profil → Dodana domyślna część jest połączona z przeciwległą stroną tworząc zamknięty profil ''(rurę)'', który nie jest rozkładalny.*

<img alt="" src=images/SheetMetal_Example-10l.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10m.png  style="width:200px;">



*Powiązanie prostokątnego szkicu z właściwością **Szkic*: Profil zamknięty → Profil z przedłużeniem prostokątnym, jeszcze wtopiony.**

<img alt="" src=images/SheetMetal_Example-10m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10n.png  style="width:200px;">



*Przełącz parametr **Użyj odejmowania* na wartość {{True/pl**, aby zapewnić (mało widoczną) domyślną przerwę między obiektem Rozszerzenia a przeciwległą stroną, a następnie zwiększ **Odsunięcie**, aby poszerzyć tę przerwę:<br>
Profil łączony → Profil z zazębiającym się przedłużeniem, ten efekt końcowy jest rozkładalny.}}


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/pl
