# Navigation Cube/pl
## Wprowadzenie

**Kostka nawigacyjna** daje wizualną informację o orientacji ujęcia widoku kamery w bieżącym [widoku 3D](3D_view/pl.md) i może być użyta do jej zmiany. Domyślnie jest ona widoczna i znajduje się w prawym górnym rogu okna.

![](images/Navigation_Cube_Example.png )

Kostka nawigacyjna składa się z kilku części:

-   [Główny sześcian nawigacyjny](#G.C5.82.C3.B3wny_sze.C5.9Bcian_nawigacyjny.md).
-   [Strzałki kierunkowe](#Strza.C5.82ki_kierunkowe.md).
-   [Przycisk widoku do tyłu](#Przycisk_widoku_do_ty.C5.82u.md) *(u góry po prawej)* {{Version/pl|0.20}}
-   [Menu mini-kostki](#Menu_mini-kostki.md) *(na dole po prawej)*.
-   Wskaźniki osi X, Y i Z

Wszystkie elementy, z wyjątkiem wskaźników osi, można klikać.



## Użycie



### Główny sześcian nawigacyjny 

Główny sześcian posiada 26 ścian: 6 ścian głównych, 12 prostokątnych ścian brzegowych ({{Version/pl|0.20}}) i 8 ścian narożnych. Kliknięcie dowolnej z nich spowoduje zmianę ujęcia widoku kamery tak, aby jej kierunek był prostopadły do wybranej ściany.



### Strzałki kierunkowe 

Istnieje sześć strzałek kierunkowych: cztery trójkątne groty, jedna na górze, na dole, w lewo i w prawo; oraz dwie zakrzywione strzałki. Kliknięcie jednej z trójkątnych strzałek spowoduje obrót [widoku 3D](3D_view/pl.md) wokół linii prostopadłej do kierunku strzałki. Kliknięcie zakrzywionej strzałki spowoduje obrót [widoku 3D](3D_view/pl.md) wokół kierunku widoku.



### Przycisk widoku do tyłu 

Kliknięcie okrągłego przycisku w prawym górnym rogu kostki nawigacyjnej spowoduje obrócenie [widoku 3D](3D_view/pl.md) o 180° wokół pionowej osi widoku.



### Menu mini-kostki 

Kliknięcie małego sześcianu w prawym dolnym rogu Kostki nawigacji spowoduje wyświetlenie menu z następującymi opcjami:

-   <img alt="" src=images/Std_OrthographicCamera.svg  style="width:16px;"> **[Ortogonalny](Std_OrthographicCamera/pl.md)**: przełącza na widok ortogonalny.

-   <img alt="" src=images/Std_PerspectiveCamera.svg  style="width:16px;"> **[Perspektywa](Std_PerspectiveCamera/pl.md)**: przełącza na widok perspektywiczny.

-   <img alt="" src=images/Std_ViewIsometric.svg  style="width:16px;"> **[Isometryczny](Std_ViewIsometric/pl.md)**: przełącza na widok izometryczny.

-   <img alt="" src=images/Std_ViewFitAll.svg  style="width:16px;"> **[Przybliż i dopasuj](Std_ViewFitAll/pl.md)**: powiększa i pochyla ujęcie widoku tak, aby wszystkie widoczne obiekty zmieściły się w aktualnym kadrze.

-    **Ruchoma kostka nawigacyjna**: jeśli to pole wyboru ({{Version/pl|0.21}}) jest zaznaczone, cała kostka nawigacji może zostać przesunięta poprzez przytrzymanie lewego przycisku myszy w dowolnym miejscu na głównej kostce i przeciągnięcie. Ma to na celu tymczasowe przesunięcie kostki z drogi. [Parametry zaawansowane](#Parametry_zaawansowane.md) OffsetX i OffsetY mogą być użyte do trwałej zmiany położenia kostki, patrz poniżej.



## Dostosowywanie



### Ustawienia

Sześcian nawigacyjny jest konfigurowalny, włącznie z dostosowaniem jego rozmiaru: **Edycja → Preferencje → Wyświetlanie → Nawigacja → Kostka nawigacyjna**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).



### Parametry zaawansowane 

Niektóre zaawansowane parametry kostki nawigacyjnej nie mogą być zmienione w [Edytorze ustawień](Preferences_Editor/pl#Nawigacja.md). Parametry te można ustawić ręcznie w [Edytorze parametrów](Std_DlgParameter/pl.md).

Aby samodzielnie ustawić kolory:

1.  Uruchom <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Edytor parametrów](Std_DlgParameter/pl.md).
2.  W panelu po lewej stronie przejrzyj **BaseApp → Preferences → NaviCube**.
3.  Kliknij prawym przyciskiem myszy na panelu po prawej stronie i wybierz z menu kontekstowego **Nowy element z liczbą całkowitą**.
4.  Wpisz nazwę jednego z tych kolorów:
    -   
        **BaseColor**
        
        : kolor bazowy wszystkich elementów, domyślnie jest to {{Value|3806916544}}. (hex: {{Value|e2e8efc0}}). Kolor ten można również ustawić w [Edytorze parametrów](Preferences_Editor#Navigation.md). {{Version/pl|0.21}}

    -   
        **EmphaseColor**
        
        : kolor tekstów i linii, domyślny zależy od **BaseColor**. Jest to albo czarny: {{Value|255}} (hex: {{Value|000000ff}}), lub biały: {{Value|4294967295}} (hex: {{Value|ffffff}}). {{Version/pl|0.21}}

    -   
        **HiliteColor**
        
        : kolor używany do podświetlania ścian i przycisków, domyślnie {{Value|2867003391}}. (hex: {{Value|aae2ffff}}).
5.  Wartość koloru musi być wprowadzona jako 32-bitowa liczba całkowita bez znaku. W postaci szesnastkowej ta liczba całkowita ma postać {{Value|RRGGBBAA}}. Gdzie {{Value|AA}} oznacza kanał alfa (miarę przezroczystości), a pozostałe trzy pary cyfr oznaczają kolor czerwony, zielony i niebieski. Aby przekonwertować wartość szesnastkową na liczbę całkowitą bez znaku, można użyć [konsoli Python](Python_console/pl.md), wpisując na przykład {{Incode|int("323232ff", 16)}}.
6.  Opcjonalnie ustaw więcej parametrów.
7.  Naciśnij przycisk **Zamknij**.

Poniższa tabela zawiera listę innych zaawansowanych parametrów Kostki nawigacyjnej, które można ustawić w podobny sposób. Użyj informacji z kolumny **Typ**, aby utworzyć prawidłowy nowy element w kroku 3.

+++++
| Nazwa                  | Opis                                                                                                                                               | Typ                       | Wartość domyślna |
+========================+====================================================================================================================================================+===========================+==================+
| Szerokość ramki        | Szerokość krawędzi sześcianu i obramowania wokół przycisków w pikselach.                                                                           | Liczba zmiennoprzecinkowa | 1.1              |
+++++
| Rozmiar fazowania      | Rozmiar krawędzi i narożników jako współczynnik rozmiaru sześcianu. Wartości powinny mieścić się w zakresie 0,05 - 0,18.                           | Liczba zmiennoprzecinkowa | 0.12             |
|                        |                                                                                                                                                    |                           |                  |
|                        |                                                                                                                                     |                           |                  |
|                        | {{Version/pl|0.21}}                                                                                                                                |                           |                  |
|                        |                                                                                                                                                 |                           |                  |
+++++
| Rozciągnięcie czcionki | Szerokość czcionki jako procent domyślnej szerokości. Użyj 0 lub 100 dla domyślnej szerokości czcionki.                                            | Liczba całkowita          | 0                |
+++++
| Grubość czcionki       | Grubość czcionki. Wyższe wartości sprawiają, że czcionka jest bardziej pogrubiona. Efekt może zależeć od czcionki. Domyślna grubość czcionki to 0. | Liczba całkowita          | 0                |
+++++
| Powiększenie czcionki  | Rozmiar etykiet:                                                                                                                                   | Liczba zmiennoprzecinkowa | 0.3              |
|                        |                                                                                                                                                    |                           |                  |
|                        | -                                                                                                                                   |                           |                  |
|                        |     {{Value|FontZoom &#61; 1.0}}                                                                                                                   |                           |                  |
|                        |                                                                                                                                                 |                           |                  |
|                        |     : Spraw, aby etykiety były jak największe indywidualnie.                                                                                       |                           |                  |
|                        |                                                                                                                                                    |                           |                  |
|                        | -                                                                                                                                   |                           |                  |
|                        |     {{Value|0.0 < FontZoom < 1.0}}                                                                                                                 |                           |                  |
|                        |                                                                                                                                                 |                           |                  |
|                        |     : Podobnie, ale ogranicz maksymalny rozmiar czcionki.                                                                                          |                           |                  |
|                        |                                                                                                                                                    |                           |                  |
|                        | -                                                                                                                                   |                           |                  |
|                        |     {{Value|FontZoom &#61; 0.0}}                                                                                                                   |                           |                  |
|                        |                                                                                                                                                 |                           |                  |
|                        |     : Tak samo, ale użyj tego samego rozmiaru czcionki dla wszystkich.                                                                             |                           |                  |
|                        |                                                                                                                                                    |                           |                  |
|                        | -                                                                                                                                   |                           |                  |
|                        |     {{Value|FontZoom < 0.0}}                                                                                                                       |                           |                  |
|                        |                                                                                                                                                 |                           |                  |
|                        |     : Użyj tego samego rozmiaru czcionki dla wszystkich, ale w mniejszej skali.                                                                    |                           |                  |
|                        |                                                                                                                                                    |                           |                  |
|                        |                                                                                                                                     |                           |                  |
|                        | {{Version/pl|0.21}}                                                                                                                                |                           |                  |
|                        |                                                                                                                                                 |                           |                  |
+++++
| OffsetX                | Przesunięcie sześcianu w kierunku X względem położenia narożnika w pikselach.                                                                      | Liczba całkowita          | 0                |
+++++
| OffsetY                | Przesunięcie sześcianu w kierunku Y względem położenia narożnika w pikselach.                                                                      | Liczba całkowita          | 0                |
+++++
| ShowCS                 | Włącza wyświetlanie układu współrzędnych *(wskaźniki osi X, Y i Z)*.                                                                               | Wartość logiczna          |   |
|                        |                                                                                                                                                    |                           | {{true|pl}}      |
|                        |                                                                                                                                                    |                           |               |
+++++
| Tekst na dole          | Tekst na dolnej ścianie kostki. Wartość domyślna powinna zostać przetłumaczona.                                                                    | Ciąg znaków               | BOTTOM           |
+++++
| Tekst z przodu         | Tekst na przedniej ścianie kostki. Analogicznie.                                                                                                   | Ciąg znaków               | FRONT            |
+++++
| Tekst po lewej         | Tekst na lewej ścianie kostki. Analogicznie.                                                                                                       | Ciąg znaków               | LEFT             |
+++++
| Tekst z tyłu           | Tekst na tylnej ścianie kostki. Analogicznie.                                                                                                      | Ciąg znaków               | REAR             |
+++++
| Tekst po prawej        | Tekst na prawej ścianie kostki. Analogicznie.                                                                                                      | Ciąg znaków               | RIGHT            |
+++++
| Tekst na górze         | Tekst na górnej ścianie kostki. Analogicznie.                                                                                                      | Ciąg znaków               | TOP              |
+++++



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/pl
