---
 GuiCommand:
   Name: Path Waterline
   Name/pl: Path: Linia poziomu
   MenuLocation: Ścieżka , Linia poziomu
   Workbenches: Path_Workbench/pl
   Version: 0.19
---

# Path Waterline/pl



## Opis

Narzędzie <img alt="" src=images/Path_Waterline.svg  style="width:24px;"> **Linia poziomu** tworzy nową operację Linii poziomu. Od wersji 0.19_pre operacja działa na całym modelu, generując G-code dla zadania. Obecnie w ustawieniach operacji nie ma funkcji wyboru określonych obszarów, powierzchni lub regionów modelu.

Operacja Linii poziomu ma dwa algorytmy: OCL Drop Cutter i Experimental.

-   Algorytm OCL Drop Cutter łączy się z OCL.pyd, zewnętrznym modułem Open Source o nazwie [OpenCamLib](OpenCamLib/pl.md), który generuje ścieżki narzędzia z modelu 3D. OpenCamLib nie jest zintegrowany bezpośrednio z FreeCAD.
-   Eksperymentalny algorytm wykorzystuje wbudowaną klasę Path.Area().

***Uwaga***: Aby skorzystać z operacji Linia poziomu powinieneś:

1.  Prawidłowo zainstalować [OpenCamLib](OpenCamLib/pl.md).
2.  Włączyć [funkcje eksperymentalne](Path_experimental/pl.md) dla środowiska pracy CAM.
3.  Sprawdzić nastawy **Edycja → Preferencje ... → CAM → Zaawansowane → Włącz funkcje zależne od OpenCamLib**.



## Użycie

Poniżej przedstawiono instrukcje użytkowania dla wielu wariantów operacji **Linii poziomu**.



#### Operacje podstawowe 

1.  Naciśnij **<img src="images/Path_Waterline.svg" width=24px> Linia poziomu** lub wybierz narzędzie **Linia poziomu** z menu **CAM**.
2.  Wybierz kontroler narzędzia dla operacji z okna dialogowego Kontroler narzędzia.
3.  Dostosuj głębokość operacji zgodnie z potrzebami w zakładce Głębokość: Głębokość początkowa, Głębokość końcowa, Krok w dół.
4.  W razie potrzeby dostosuj ustawienia w zakładce Wysokość.
5.  Skonfiguruj ustawienia w zakładce Operacje w oparciu o wybrany algorytm:
    1.  OCL Dropcutter
        1.  Wybierz pole Ramka otaczająca: Przygotówka lub Punkt bazowy obiektu Ramki otaczającej.
        2.  Ustaw tryb warstwy: Pojedyncze przejście lub Wielokrotne przejście.
        3.  Ustaw interwał próbkowania używany do skanowania OCL.
    2.  Eksperymentalne
        1.  Wybierz Ramka otaczająca: Przygotówka lub Punkt bazowy obiektu Ramki otaczającej.
        2.  Ustaw tryb warstwy: Pojedyncze przejście lub Wielokrotne przejście.
        3.  Ustaw wzorzec cięcia, jeśli chcesz wyczyścić każdą warstwę.
        4.  Ustaw dostosowanie granic *(naddatek materiału)*.
6.  Jeśli chcesz wyświetlić podgląd wyniku przed zaakceptowaniem ustawień, kliknij przycisk Zastosuj.
7.  Kliknij przycisk *OK*, aby potwierdzić i wygenerować ścieżki.

Aby uzyskać inne lub bardziej złożone efekty, należy dostosować dodatkowe właściwości operacji na karcie Dane w widoku Właściwości operacji.



##### Uwagi o algorytmie eksperymentalnym 

-   Nie obsługuje prawidłowo nawisów.
-   Zwraca ścieżki tylko dla frezów typu End Mill *(bit narzędziowy)*.
-   Może nie wychwytywać poprawnie wszystkich elementów wewnętrznych.
-   Jest po prostu eksperymentalna i nie jest gotowa na integrację z głównym nurtem. Prosimy o sprawdzanie ścieżek za pomocą wbudowanego narzędzia **<img src="images/Path_Simulator.svg" width=16px> [Symulator CAM](Path_Simulator/pl.md)** lub innych narzędzi do kontroli G-Code innych firm, przed rozpoczęciem procesu obróbki.



#### Dostępne kształty narzędzi (frezów) 

W przypadku korzystania z algorytmu \"OCL Dropcutter\", operacja Waterline wykorzystuje OpenCamLib \[OCL/pl\|OCL\] do wyodrębniania ścieżek z podstawy części. W związku z tym wymagana jest translacja narzędzia między kontrolerem narzędzi FreeCAD a OCL w celu zakończenia skanowania wybranym kształtem narzędzia *(frezu)*. Te kształty narzędzi są *(powinny być)* respektowane i dostępne dla OCL Dropcutter, o ile używane są wbudowane kształty narzędzi, zarówno narzędzia starszego typu, jak i narzędzia typu ToolBit:

-   Frez trzpieniowy
-   Frez kulowy
-   frez walcowo-czołowy
-   Końcówka fazująca
-   Grawer



#### Uwagi dodatkowe 

-   Jeśli zdecydujesz się uruchomić symulator **<img src="images/Path_Simulator.svg" width=16px> [CAM symulator](Path_Simulator/pl.md)**, w środowisku pracy Path możesz nie zobaczyć usuwania materiału specyficznego dla kształtu narzędzia. Zachowaj ostrożność. Zaleca się wykonanie małego zadania próbnego przy użyciu pianki lub innego bardzo niegęstego materiału w celu sprawdzenia poprawności ścieżek z wybranym kontrolerem narzędzia.
-   Od maja 2020 r. tylko frez walcowo-czołowy jest testowany w celu określenia dokładności translacji ustawień narzędzia z FreeCAD doOCL. Prosimy o przesyłanie wszelkich opinii dotyczących użycia frezów innych niż frezy walcowo-czołowe do sekcji [Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) na forum FreeCAD.



## Właściwości

***Uwaga***: Nie wszystkie z tych właściwości są dostępne w edytorze okna zadań. Niektóre są dostępne tylko na karcie Dane w panelu Widok właściwości dla tej operacji.


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania ścieżki.

-    **Umiejscowienie**: Ogólne położenie *(pozycja i obrót)* obiektu - w odniesieniu do punktu odniesienie położenia *(lub punktu odniesienie położenia kontenera obiektu nadrzędnego)*.

    -   
        **Kąt**
        
        : Kąt w stopniach zastosowany do obrotu obiektu wokół wartości właściwości Oś.

    -   
        **Oś**
        
        : Oś *(jedna lub wiele)*, wokół której ma zostać obrócony obiekt, ustawiona we właściwościach podrzędnych: X, Y, Z

        -   
            **X**
            
            : Wartość osi X.

        -   
            **Y**
            
            : Wartość osi Y.

        -   
            **Z**
            
            : Wartość osi Z.

    -   
        **Pozycja**
        
        : Pozycja obiektu, ustawiona we właściwościach podrzędnych: X, Y, Z - względem początku *(lub początku kontenera obiektu nadrzędnego)*.

        -   
            **X**
            
            : Wartość odległości X.

        -   
            **Y**
            
            : wartość odległości Y.

        -   
            **Z**
            
            : wartość odległości Z.

-    **Etykieta**: Nazwa obiektu podana przez użytkownika *(UTF-8)*.


{{TitleProperty|Opcje czyszczenia}}

-    **Algorytm**: Biblioteka używana do generowania ścieżki.

-    **Ramka otaczająca**: Czy operacja powinna być ograniczona przez obiekt podstawowy, czy przez obwiednię obiektu podstawowego?

-    **Wyczyść ostatnią warstwę**: Ustawia czyszczenie ostatniej warstwy w operacji wieloprzebiegowej.

-    **Tryb obróbki**: Kierunek, w którym ścieżka narzędzia powinna przebiegać wokół części: Wspinanie *(zgodnie z ruchem wskazówek zegara)* lub Konwencjonalny *(przeciwnie do ruchu wskazówek zegara)*.

-    **Wzorzec obróbki**: Wzorzec czyszczenia do użycia.

-    **Odsunięcie głębokości**:

-    **Ignoruj zewnętrzne powyżej**:

-    **Tryb warstwy**: Tryb zakończenia operacji: jedno- lub wieloprzebiegowy.

-    **Krok powyżej**:


{{TitleProperty|Głębokość}}

-    **Wysokość prześwitu**: Wysokość potrzebna do usunięcia zacisków i przeszkód.

-    **Głębokość końcowa**: Głębokość końcowa narzędzia - najniższa wartość w Z.

-    **Wysokość bezpieczna**: Wysokość, powyżej której dozwolone są szybkie ruchy.

-    **Głębokość początkowa**: Głębokość początkowa narzędzia - pierwsza głębokość cięcia w Z.

-    **Krok w dół**: Przyrostowy krok w dół narzędzia.


{{TitleProperty|Ścieżka}}

-    **Aktywny**: Ustaw wartość {{False/pl}}, aby zapobiec generowaniu kodu przez operację.

-    **Baza**: Geometria bazowa dla tej operacji.

-    **Komentarz**: Opcjonalny komentarz dla tej operacji.

-    **Tryb chłodzenia**:

-    **Czas cyklu**:

-    **Kontroler narzędzi**: Określa kontroler narzędzia używany w operacji.

-    **Etykieta użytkownika**: Etykieta przypisana przez użytkownika.


{{TitleProperty|Punkt początkowy}}

-    **Punkt początkowy**: Niestandardowy punkt początkowy dla ścieżki tej operacji.

    -   
        **X**
        
        : wartość odległości X.

    -   
        **Y**
        
        : wartość odległości Y.

    -   
        **Z**
        
        : wartość odległości Z.

-    **Użyj punktu początkowego**: Ustaw wartość {{True/pl}}, jeśli określono punkt początkowy.



## Układ edytora w oknie zadań 

*Opisy ustawień znajdują się na powyższej liście właściwości*.

Ta sekcja jest po prostu mapą układu ustawień w edytorze okien dla operacji.



### Lokalizacja bazowa 

-   **Dodaj**: Dodaje wybrane elementy, które powinny być bazą dla ścieżek.
-   **Usuń**: Usuwa wybrane elementy z listy Lokalizacja bazowa.
-   **Edytuj**: Czyści wszystkie elementy na liście Lokalizacja bazowa.



### Głębokości

-    **Głębokość początkowa**
    

-    **Głębokość końcowa**
    

-    **Krok w dół**
    



### Wysokości

-    **Wysokość bezpieczna**
    

-    **Wysokość prześwitu**
    



### Operacja

-    **Kontroler narzędzi**.

-    **Tryb chłodzenia**
    

-    **Algorytm**
    

-    **Ramka otaczająca**
    

-    **Tryb warstwy**
    

-    **Wzór obróbki**\~.

-    **Regulacja granic**\~.

-    **Odstęp między próbkami**\~.

\~Widoczność zmienia się wraz z innymi ustawieniami.



## Zasoby

-   Symulator G-Code *(ścieżka)*: [NCViewer](https://ncviewer.com/)
-   Symulator G-code *(ścieżka)*: [CAMotics](https://www.camotics.org/)





{{Path Tools navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Waterline/pl
