---
- GuiCommand:/pl
   Name:Part Compound‏‎Filter
   Name/pl:Część: Filtr złożeń
   MenuLocation:Część → Złożenie → Filtr złożeń
   Workbenches:[Część](Part_Workbench/pl.md)
   Version:0.17
---

# Part CompoundFilter/pl

![](images/CompoundFilter.png )



## Opis

Narzędzie **Filtr złożeń** może być użyte do wyodrębnienia poszczególnych części składowych wyniku np. operacji [Krojenie](Part_Slice/pl.md), za pomocą której podzielono obiekt.

Umożliwia wyodrębnianie elementów podrzędnych na podstawie ich indeksów, testowanie elementów pod kątem kolizji z kształtem szablonu oraz filtrowanie elementów podrzędnych na podstawie ich właściwości, takich jak długość, powierzchnia czy objętość.

Jeśli w wyniku znajduje się tylko jeden element podrzędny, wynikiem jest ten element podrzędny. Jeśli w wyniku jest więcej niż jeden element podrzędny, wynikiem jest nowe złożenie.



## Użycie

1.  Wybierz pocięty obiekt
2.  Zastosuj **Część → Złożenie → Filtr złożeń**
3.  Wybierz obiekt *FiltrZłożeń* w Widoku drzewa
4.  W zakładce właściwości ustaw **Typ Filtra** na **Wybrana pozycja**.
5.  Ustaw pozycję na elementy, które chcesz wyodrębnić
    1.  Dla pojedynczego elementu jest to liczba zaczynająca się od 0, tj. jeśli chcesz wyodrębnić pierwszy element, wpisz 0 w tym polu, 1 dla następnego elementu \...
    2.  Jeżeli chcesz wyodrębnić więcej niż jeden element na raz, oddziel liczby znakiem **;**, np. wartość {{Value|0;2}} spowoduje wyodrębnienie pierwszego i trzeciego elementu.
    3.  Ogólnie przyjętym przypadkiem - który obejmuje również możliwości wymienione powyżej - jest lista zakresów indeksów, określona w notacji Pythona, ale bez nawiasów. Przedziały można łączyć w łańcuchy za pomocą średnika. Na przykład:
        -   7:10 pobierz elementy podrzędne o indeksach 7, 8 i 9 *(indeksy numerowane są od zera; indeks od zakresu do indeksu jest wykluczony)*.
        -   1;2 pobierz elementy podrzędne o indeksach 1 i 2 *(pierwszy indeks oznacza element podrzędny 2, drugi indeks to element 3, zakresy połączone średnikiem)*,
        -   0;-1 weź pierwszy element podrzędny *(indeks 0)* i ostatni *(indeks -1 oznacza ostatni element, -2 - jeden przedostatni itd.)*,
        -   1: weź wszystko poza pierwszym elementem *(brak indeksu oznacza „do końca")*,
        -   ::-1 pobierz wszystkie elementy podrzędne w odwrotnej kolejności.
        -   ::2 pobierz wszystkie elementy z indeksami nieparzystymi, tj. indeksy, 1,3,5,\..., które są elementami 2,4,6, \...
        -   :;: powiel dwa razy złożony element wejściowy
6.  Jeśli chcesz wyodrębnić kolejny element, ponownie wybierz pocięty obiekt. Jest teraz umieszczony pod obiektem o nazwie **CompoundFilter** w Widoku drzewa
7.  Powtórz procedurę wyboru od góry. Plasterek i jego elementy podrzędne zostaną wyświetlone pod obydwoma filtrami **CompoundFilters**. Oczywiście nie powtarzają się one w modelu. Bardzo szybkim sposobem wyodrębnienia kolejnego fragmentu jest skopiowanie obiektu *CompoundFilter**. Ale**uważaj**: Zostaniesz zapytany, czy chcesz skopiować również elementy pod CompoundFilter, musisz odpowiedzieć**nie*\', nie chcesz ich kopiować, tylko się do nich odwołujesz.



## Właściwości

-    **Baza**: Obiekt do filtrowania.

-    **Typ Filtra**opcje do wyboru:

    -   **Omiń**: brak filtra. Oryginalne złożenie jest wyprowadzane bez zmian.
    -   **Wybrana pozycja**: wyodrębnia elementy wymienione we właściwości **pozycje**.
    -   **kolizja-przebieg**: wyodrębnia elementy, które dotykają lub przecinają się z kształtem **Wzór**.
    -   **okno-objętość**: *(domyślnie)*: wyodrębnia wszystkie elementy, które mają objętość między \"Okno od\" i \"Okno do\", gdzie 100% to największy element - a nie nieobcięty obiekt. Wartość 100% jest wartością referencyjną, która może zostać zastąpiona przez \"Nadpisz wartość Max\".
    -   **okno-obszar**: to samo co okno-objętość, gdzie wycięty obszar określa wybór zamiast objętości.
    -   **okno-długość**: to samo co okno-objętość, gdzie długość krawędzi określa wybór zamiast objętości.
    -   **okno-odległość**: wyodrębnia elementy podrzędne, których odległość od kształtu \"Wzór\" mieści się w oknie wartości, zdefiniowanym przez właściwości \"Okno od\", \"Okno do\", \"Nadpisz wartość Max\".

-    **Odwróć**: Jeśli wartość jest ustawiona na {{true|/pl}} lista opisana powyżej zostanie wykluczona zamiast uwzględniona.

-    **Nadpisz wartość Max**: Zakres okna wartości jest określony w procentach wartości maksymalnej. Wartość maksymalna jest obliczana zgodnie z następującym zestawem reguł:

    -   jeśli parametr \"Nadpisz wartość Max\" jest niezerowy - użyj go.
    -   w przeciwnym razie, jeśli podano łącze \"Wzór\" - oblicz odpowiednią wartość kształtu szablonu *(nie dotyczy odległości okna \"Typ Filtra\")*,
    -   w przeciwnym razie, weź maksymalną wartość z elementów podrzędnych w złożeniu, które ma zostać przefiltrowane.

-    **Wzór**: Link do kształtu szablonu. W przypadku filtrów typu \"kolizja-przebieg\" i \"okno-odległość\" szablon jest obiektem, względem którego testowana jest kolizja / odległość. W przypadku innych typów filtrów \"okno-\*\*\*\" szablon jest używany do zapewnienia wartości odniesienia dla wartości procentowych okna *(nadpisanie wartości maksymalnej)*. We wszystkich innych trybach \"Wzór\" jest ignorowany.

-    **Okno Od**: Górny próg procentowy wyboru elementów, wartość 100% odnosi się do największego elementu.

-    **Okno Do**: Dolny próg procentowy wyboru elementów, wartość 100% odnosi się do największego elementu.

-    **Pozycja**: Lista lub zakres elementów do wybrania, jeśli typ filtra to \"określone elementy\".



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CompoundFilter/pl
