---
 GuiCommand:
   Name: CAM Surface
   Name/pl: Path: Powierzchnia 3D
   MenuLocation: CAM , Powierzchnia 3D
   Workbenches: CAM_Workbench/pl
   Version: 0.19
---

# CAM Surface/pl



## Opis

Narzędzie to tworzy nową operację <img alt="" src=images/CAM_Surface.svg  style="width:24px;"> **Powierzchnia 3D** , która jest w stanie wygenerować ścieżki G-code dla całej górnej powierzchni modelu 3D (lub jest w stanie pracować z wybranymi ścianami) i pozwala na omijanie ścian. Operacja ta oferuje wiele wzorców skrawania: Line, Zygzak, Okrągły, Okrągły Zygzak, Przesunięcie i Spirala (podobny do wzorca adaptacyjnego). Od wersji 0.19 operacja ta oferuje wiele dostosowań umożliwiających zwiększenie wydajności.

Operacja <img alt="" src=images/CAM_Surface.svg  style="width:24px;"> **Powierzchnia 3D** jest zdolna również do generowania podstawowych obrotowych ścieżek powierzchni 3D. Możliwości rotacyjne są ograniczone do całego modelu i nie pozwalają na izolowanie konkretnych ścian lub regionów. Ścieżki obrotowe są również ograniczone do wzorów skrawania liniowego.

Narzędzie powierzchni 3D jest połączone z OCL.pyd, zewnętrznym modułem Open Source o nazwie [OpenCamLib](OpenCamLib/pl.md), który generuje ścieżki narzędzia z modelu 3D. Biblioteka OpenCamLib nie jest zintegrowana bezpośrednio z programem FreeCAD.

**Note:** Aby używać operacji Powierzchnia 3D, musisz:

1.  Prawidłowo zainstalować [OpenCamLib](OpenCamLib/pl.md).
2.  Włączyć [Funkcje eksperymentalne](CAM_experimental/pl.md) dla środowiska pracy CAM.
3.  Sprawdzić **Edycja → Preferencje... → CAM → Zaawansowane → Włącz funkcje zależne od OpenCamLib**.



## Użycie

Poniżej przedstawiono instrukcje użytkowania dla wielu wariantów operacji [Powierzchnia 3D](CAM_Surface/pl.md).



### Operacja podstawowa 

1.  Wciśnij ikonę **<img src="images/CAM_Surface.svg" width=24px> [Powierzchnia 3D](CAM_Surface/pl.md)** lub wybierz opcję **CAM → Powierzchnia 3D** z menu rozwijanego.
2.  Wybierz kontroler narzędzia dla operacji z okna dialogowego kontrolera narzędzia, jeśli się pojawi.
3.  W zakładce Geometria podstawowa wybierz konkretne powierzchnie, na których chcesz się skupić i/lub których chcesz uniknąć podczas operacji.
4.  Dostosuj głębokości operacji w zakładce Głębokość: Głębokość początkowa, Głębokość końcowa, Krok w dół.
5.  W razie potrzeby zmień ustawienia w zakładce Wysokości.
6.  Skonfiguruj ustawienia w zakładce Operacja według potrzeb:
    -   Wybierz tryb chłodziwa.
    -   Wybierz Ramkę otaczającą: Półfabrykat lub Punkt bazowy obiektu Ramki otaczającej.
    -   Ustaw Metodę skanowania dla operacji: Płaski lub Obrotowy.
    -   Wybierz Tryb warstw dla operacji: Pojedyncze przejście lub Wielokrotne przejście.
        1.  Pojedyncze przejście jest używane do przejścia wykończeniowego.
        2.  Wielokrotne przejście może być używane do usuwania materiału w połączeniu z użyciem Głębokości przesunięcia, aby pozostawić cienką warstwę materiału do wykończenia.
    -   Dodaj Dodatkowe odsunięcie X, Y obiektu Ramki otaczającej, jeśli to konieczne (*Tylko skanowanie obrotowe*).
    -   Ustaw Kierunek spuszczania freza: X lub Y. Jest to liniowy kierunek, w którym narzędzie (wrzeciono) będzie się poruszać. (*Tylko skanowanie obrotowe*).
    -   Dodaj wartość Głębokości przesunięcia, jeśli chcesz pozostawić określoną grubość materiału na powierzchni, na przykład do ostatniego przejazdu wykończeniowego.
    -   Ustaw Ostęp między próbkami używany do skanowania OCL.
    -   Ustaw wartość Szerokość skrawania jako procent średnicy narzędzia.
    -   Zaznacz pole wyboru Użyj punktu początkowego, jeśli chcesz podać punkt startowy dla operacji w widoku właściwości zakładki danych dla operacji.
    -   Ograniczenie dla brzegów jest włączone domyślnie. Wymusza to pozostanie narzędzia wewnątrz granic geometrii funkcji operacji, jak w operacji kieszeni. Wyłącz, aby pozwolić narzędziu na rozszerzenie poza granice geometrii funkcji. Właściwość Boundary Adjustment ma pierwszeństwo przed tą właściwością.
    -   Optymalizacja ścieżek liniowych jest włączona domyślnie. Wyłączenie spowoduje dłuższy wynik kodu G-code i prawdopodobnie zwiększy czas cięcia.
7.  Jeśli chcesz podglądnąć wynik przed zaakceptowaniem ustawień, kliknij **Zastosuj**.
8.  Kliknij przycisk **OK**, aby potwierdzić i wygenerować ścieżki.

Aby uzyskać inne lub bardziej złożone efekty, dostosuj dodatkowe właściwości operacji w zakładce Dane widoku właściwości dla operacji.



#### Skanowanie obrotowe (czwarta oś) 

1.  Rozpocznij [Podstawową operację](#Basic_Operation/pl.md) zgodnie z opisem powyżej i ustaw **Metodę skanowania** na **Obrotowy**.
2.  **Uwaga:** Wybór powierzchni jest niedostępny dla skanów obrotowych, więc zmiany w Geometrii podstawowej są ignorowane.
3.  Znajdź zakładkę Dane i Widok właściwości dla nowej operacji [Powierzchnia 3D](CAM_Surface/pl.md). Powinna być dostępna sekcja **Rotation** z dodatkowymi właściwościami do dostosowania, wymienionymi poniżej.
    Zaleca się ustawienie pożądanych właściwości obrotu jednocześnie przed przeliczeniem. Można to zrobić, naciskając klawisz ENTER bezpośrednio po zmianie ustawienia właściwości. Proces ten pozwala na zmianę i zapisanie wielu właściwości przed przeliczeniem operacji.
4.  Dostosuj następujące ustawienia według potrzeb:
    -   Ustaw **Cutter Tilt** na indeks (kąt) odsunięcia \[0-90\]. (Używane dla narzędzi kulowych)
    -   Zmień **Drop Cutter Dir** na oś ruchu dla narzędzia (wrzeciona).
    -   Zmień **Drop Cutter Extra Offset** na rozszerzenie ramki otaczającej w kierunkach X i Y.
    -   Ustaw **Rotation Axis** na żądaną oś.
    -   Dostosuj **Start Index** na indeks startowy (kąt) \[0-360\].
    -   Dostosuj **Stop Index** na indeks końcowy (kąt) \[0-360\].
5.  Kliknij ikonę **[<img src=images/View-refresh.svg style="width:16px"> [Odśwież](Std_Refresh.md)** na pasku narzędzi.
6.  Poczekaj na wyniki\...



##### Uwagi na temat skanów obrotowych 

-   **Skanowanie obrotowe** wymaga znacznie więcej czasu i przetwarzania niż **płaskie**. Czynniki wpływające na czas przetwarzania to: Odstęp między próbkami, Głębokość przesunięcia, średnica narzędzia i rozmiar modelu. Ponownie, skanowanie obrotowe może zająć dużo czasu. Niektóre skany tego typu mogą trwać 3, 5 lub 10 minut lub dłużej.
-   Dla oszczędności czasu lepiej nie przeliczać skanowania obrotowego po każdej zmianie właściwości; zamiast tego rozważ jedno z poniższych rozwiązań:
    -   użyj techniki \' *zmiana wszystkich ustawień za pomocą klawisza ENTER* \' wspomnianej w Kroku 2 powyżej, a następnie **[<img src=images/View-refresh.svg style="width:16px"> [Odśwież](Std_Refresh/pl.md)** operację.
    -   dezaktywuj operację za pomocą narzędzia **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Aktywny](CAM_OpActiveToggle/pl.md)**, wprowadź zmiany w właściwościach operacji, a następnie kliknij ikonę **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Aktywny](CAM_OpActiveToggle/pl.md)** ponownie, aby ponownie aktywować operację - co wywoła wewnętrzne przeliczenie.
-   Operacja **<img src="images/CAM_Surface.svg" width=16px> [Powierzchnia 3D](CAM_Surface/pl.md)** jest nadal uznawana za *funkcję eksperymentalną* od 25.06.2019. Może zawierać kilka błędów, które nie zostały jeszcze jednoznacznie zidentyfikowane. Prosimy zgłaszać błędy i problemy na [forum FreeCAD Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15).
-   Wbudowany **<img src="images/CAM_Simulator.svg" width=16px> [Symulator CAM](CAM_Simulator/pl.md)** NIE obsługuje symulacji 4-osiowej. Będziesz musiał użyć symulatora zewnętrznego, aby wizualnie sprawdzić lub zweryfikować ścieżki. Zobacz sekcję [Zasoby](#Zasoby.md) poniżej dla sugestii.
-   Prawdopodobnie zobaczysz czerwone linie obrotowe wokół swojego modelu w widoku. To normalne we FreeCAD w tym momencie.



##### Uwagi na temat skanów złożonych modeli 

Nadmiernie długie czasy przetwarzania (dłuższe niż 10 minut) mogą wystąpić przy przetwarzaniu dużych, złożonych modeli. Oprócz wcześniej wspomnianych czynników, poniższe kroki mogą pomóc w identyfikacji potencjalnych przyczyn i rozwiązań.

***Niska pamięć***
Sprawdź, ile pamięci jest dostępne podczas uruchamiania skanowania, używając narzędzia takiego jak **Menedżer zadań systemu Windows, zakładka Pamięć**. Jeśli ponad 90% pamięci jest stale używane, to mała wartość parametru **Linear Deflection** może generować siatkę, która jest zbyt duża dla dostępnej pamięci.
Aby to potwierdzić\...

1.  Utwórz nową operację **<img src="images/CAM_Surface.svg" width=24px> [Powierzchnia 3D](CAM_Surface/pl.md)**.
2.  Przełącz się na zakładkę Model i zwiększ wartość **Linear Deflection**. Na przykład zmień z 2,5 μm na 20 μm.
3.  Przełącz się z powrotem na zakładkę Zadania, aby dokończyć konfigurację operacji.
4.  Kliknij przycisk **OK**, aby potwierdzić i wygenerować ścieżki.

Aby ustawić tę wartość jako domyślną dla wszystkich nowych operacji **<img src="images/CAM_Surface.svg" width=24px> [Powierzchnia 3D](CAM_Surface/pl.md)**, zmień parametr **GeometryTolerance**.
**Narzędzia → Edytuj parametry ... → Preferences → Mod → CAM → GeometryTolerance **.
Uwaga: od wersji 0.19 domyślna wartość **Linear Deflection** = GeometryTolerance / 4

***Nieprawidłowa geometria***
Jeśli model zawiera nieprawidłową geometrię, czas skanowania może znacznie wzrosnąć. Model można sprawdzić, używając funkcji [Część: Sprawdź geometrię](Part_CheckGeometry/pl.md) w <img alt="" src=images/Workbench_Part.svg  style="width:24px;">**Środowisku pracy Część**.
Aby uruchomić narzędzie:

1.  Przełącz się na <img alt="" src=images/Workbench_Part.svg  style="width:24px;">**Środowisko pracy Część** i wybierz model do sprawdzenia.
2.  Kliknij przycisk **<img src="images/Part_CheckGeometry.svg" width=16px> [Część: Sprawdź geometrię](Part_CheckGeometry/pl.md)** dostępny na pasku narzędzi Środowiska pracy Części lub użyj opcji **Część → <img src="images/Part_CheckGeometry.svg" width=16px> Sprawdź geometrię** z górnego menu.
3.  Kliknij przycisk **Uruchom sprawdzanie** i obejrzyj wyniki.

Jeśli wyniki zawierają elementy takie jak *BOPAlgo SelfIntersect*, geometria jest nieprawidłowa i należy ją poprawić, dostosowując model.
(Wskazówka: Operacje logiczne i polecenia wyciągnięcia po profilach mogą czasami wprowadzać *Self Intersections*)



#### Dostępne kształty narzędzi 

Operacja Powierzchnia 3D aktualnie używa [OpenCamLib](OpenCamLib/pl.md) do wyciągania ścieżek z podstawy części. W związku z tym, wymagana jest translacja ustawień narzędzia między kontrolerem narzędzi FreeCAD a OCL, aby zakończyć skanowanie z wybranym kształtem narzędzia (frezu).

Te kształty narzędzi są wspierane i dostępne dla tej operacji Powierzchni 3D:

-   Frez trzpieniowy
-   Frez kulowy
-   frez walcowo-czołowy
-   Końcówka fazująca
-   Grawer

Jeśli zdecydujesz się uruchomić symulator ścieżek w środowisku pracy CAM, używa on tylko standardowego frezu końcowego do symulacji ścieżek. W związku z tym, nie zobaczysz usuwania materiału specyficznego dla kształtu narzędzia. Usuwanie materiału będzie pokazywane za pomocą kształtu frezu końcowego.

UWAGA: Od maja 2019 roku tylko frez końcowy ma jakiekolwiek testy do określenia dokładności translacji ustawień narzędzia FreeCAD do OCL. Prosimy przesłać wszelkie uwagi dotyczące użycia innych narzędzi do sekcji [Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) na forum FreeCAD.



## Właściwości: wersja 0.19 

***Uwaga***: Nie wszystkie z tych właściwości są dostępne w edytorze okna zadań. Niektóre są dostępne tylko na karcie Dane w panelu Widok właściwości dla tej operacji.


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[pozycja i rotacja\] obiektu - względem początku (lub początku kontenera obiektów nadrzędnych)

    -   
        **Angle**
        
        : Kąt w stopniach zastosowany do rotacji obiektu wokół wartości Axis

    -   
        **Axis**
        
        : Oś (jedna lub wiele), wokół której obraca się obiekt, ustawiana w pod-właściwościach: X, Y, Z

        -   
            **X**
            
            : Wartość osi X

        -   
            **Y**
            
            : Wartość osi Y

        -   
            **Z**
            
            : Wartość osi Z

    -   
        **Position**
        
        : Pozycja obiektu, ustawiana w pod-właściwościach: X, Y, Z - względem początku (lub początku kontenera obiektów nadrzędnych)

        -   
            **X**
            
            : Wartość odległości X

        -   
            **Y**
            
            : Wartość odległości Y

        -   
            **Z**
            
            : Wartość odległości Z

-    **Label**: Nazwa obiektu podana przez użytkownika (UTF-8)


{{TitleProperty|Opcje czyszczenia}}

-    **Bound Box**: Czy operacja powinna być ograniczona przez obiekt materiału czy przez ramkę otaczającą obiektu bazowego

-    **Cut Mode**: Kierunek, w jakim ścieżka narzędzia powinna obejść część: Climb (zgodnie z ruchem wskazówek zegara) lub Conventional (przeciwnie do ruchu wskazówek zegara)

-    **Cut Pattern**: Wzór usuwania

-    **Cut Pattern Reversed**: Odwróć kolejność cięcia ścieżek przejścia. Dla wzorów cięcia okrężnego, zacznij od zewnątrz i pracuj w kierunku środka

-    **Depth Offset**: Odsunięcie osi Z od powierzchni obiektu

-    **Layer Mode**: Tryb zakończenia operacji: pojedynczy lub wielokrotny

-    **Pattern Center At**: Wybierz lokalizację punktu centralnego dla rozpoczęcia wzoru cięcia

-    **Pattern Center Custom**: Ustaw punkt początkowy dla wzoru cięcia

-    **Profile Edges**: Profiluj krawędzie wyboru. Dostępne są następujące opcje (screeny można zobaczyć w tym poście na forum: <https://forum.freecad.org/viewtopic.php?p=676452#p676452>):

    -   
        **None**
        
        : Nie twórz profilu

    -   
        **Only**
        
        : Twórz tylko profil i brak ścieżek wewnętrznych

    -   
        **First**
        
        : Rozpocznij od profilu, a następnie wykonaj resztę

    -   
        **Last**
        
        : Rozpocznij od reszty, a następnie wykonaj profil

-    **Sample Interval**: Odstęp między próbkami. Małe wartości powodują długie czasy oczekiwania

-    **Step Over**: Procent przejścia ścieżki narzędzia


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Ostateczna głębokość narzędzia -- najniższa wartość w osi Z

-    **Safe Height**: Wysokość, powyżej której dozwolone są szybkie ruchy

-    **Start Depth**: Głębokość początkowa narzędzia -- pierwsza głębokość cięcia w osi Z

-    **Step Down**: Stopniowe zagłębianie narzędzia


{{TitleProperty|Mesh Conversion}}

-    **Angular Deflection**: Mniejsze wartości dają drobniejszą, dokładniejszą siatkę. Mniejsze wartości znacząco wydłużają czas przetwarzania

-    **Linear Deflection**: Mniejsze wartości dają drobniejszą, dokładniejszą siatkę. Mniejsze wartości nie wydłużają znacząco czasu przetwarzania, ale mogą zwiększać zużycie pamięci


{{TitleProperty|Optymalizacja}}

-    **Circular Use G2 G3**: Konwertuj współpłaszczyznowe łuki na polecenia G2/G3 w kodzie G dla wzorców cięcia \Circular\ i \CircularZigZag\

-    **Gap Sizes**: Informacja zwrotna: trzy najmniejsze przerwy zidentyfikowane w geometrii ścieżki

-    **Gap Threshold**: Współliniowe i współosiowe artefakty mniejsze niż ten próg są zamykane w ścieżce

-    **Optimize Linear Paths**: Włącz optymalizację ścieżek liniowych (współliniowych punktów). Usuwa niepotrzebne współliniowe punkty z wygenerowanego kodu G-code

-    **Optimize Step Over Transitions**: Włącz oddzielną optymalizację przejść pomiędzy i przerw w każdej ścieżce skoku


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu przez operację

-    **Base**: Podstawowa geometria dla tej operacji

-    **Comment**: Opcjonalny komentarz do tej operacji

-    **Coolant Mode**: Tryb chłodziwa dla tej operacji

-    **Cycle Time**: Szacowany czas cyklu operacji

-    **Tool Controller**: Definiuje kontroler narzędzia używany w operacji

-    **User Label**: Etykieta nadana przez użytkownika


{{TitleProperty|Obrót}}

-    **Cutter Tilt**: Ustaw kąt pochylenia wrzeciona (narzędzia).

-    **Drop Cutter Dir**: Kierunek, w którym tworzone są linie narzędzia dropcutter.

-    **Drop Cutter Extra Offset**: Dodatkowe odsunięcie do wybranej ramki otaczającej - użyj podwłaściwości, aby ustawić wartości.

    -   
        **X**
        
        : Wartość przesunięcia w osi X.

    -   
        **Y**
        
        : Wartość przesunięcia w osi Y.

    -   
        **Z**
        
        : Wartość przesunięcia w osi Z.

-    **Rotation Axis**: Ustaw oś dla rotacji modelu.

-    **Start Index**: Kąt początkowy rotacji (index).

-    **Stop Index**: Kąt końcowy rotacji (index).


{{TitleProperty|Wybrane ustawienia geometrii}}

-    **Avoid Last X Faces**: Unikaj obróbki ostatnich \'N\' powierzchni z listy wybranych powierzchni w geometrii podstawowej.

-    **Avoid Last X Internal Features**: Nie obrabiaj wewnętrznych cech na unikanych powierzchniach.

-    **Boundary Adjustment**: Dodatnie wartości przesuwają narzędzie w stronę lub poza granicę. Ujemne wartości cofają narzędzie od granicy.

-    **Boundary Enforcement**: Jeśli wartość to prawda, narzędzie pozostanie wewnątrz granic modelu lub wybranych powierzchni.

-    **Handle Multiple Features**: Wybierz sposób przetwarzania wielu cech geometrii bazowej.

-    **Internal Features Adjustment**: Dodatnie wartości przesuwają narzędzie w stronę lub do wnętrza cechy. Ujemne wartości cofają narzędzie od cechy.

-    **Internal Features Cut**: Obrabiaj obszary wewnętrznych cech w większej wybranej powierzchni.


{{TitleProperty|Punkt startowy}}

-    **Start Point**: Własny punkt początkowy ścieżki dla tej operacji, ustawiony w podwłaściwościach: X, Y, Z.

    -   
        **X**
        
        : Wartość osi X.

    -   
        **Y**
        
        : Wartość osi Y.

    -   
        **Z**
        
        : Wartość osi Z.

-    **Use Start Point**: Ustaw na \"True\", jeśli określasz punkt początkowy.


{{TitleProperty|Powierzchnia}}

-    **Scan Type**: Płaski: płaski skan powierzchni 3D. Obrotowy: obrotowy skan w czwartej osi.


{{TitleProperty|Odpady}}

-    **Ignore Waste**: Ignoruj obszary, które przekraczają określoną głębokość.

-    **Ignore Waste Depth**: Głębokość używana do identyfikacji obszarów odpadów do zignorowania.

-    **Release From Waste**: Przetnij przez odpady do głębokości na krawędzi modelu, uwalniając model.



## Układ edytora w oknie zadań 

*Opisy ustawień znajdują się na powyższej liście właściwości*.

Ta sekcja jest po prostu mapą układu ustawień w edytorze okien dla operacji.



### Lokalizacja podstawowa 

-   **Base Geometry import selection**: Użyj tej listy, aby wybrać geometrię podstawową do importu z wybranej, istniejącej operacji.
-   **Import**: Importuje geometrię podstawową wybranej operacji do listy geometrii bazowej bieżącej operacji.
-   **Base Geometry list for current operation**: Lista geometrii podstawowej dla bieżącej operacji, jeśli jakieś elementy zostały wybrane.
-   **Add**: Dodaje wybrany(e) element(y), które mają stanowić bazę dla ścieżki/ścieżek.
-   **Remove**: Usuwa wybrany(e) element(y) z listy lokalizacji bazy.
-   **Clear**: Czyści wszystkie elementy z listy lokalizacji bazy.



### Głębokość

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    



### Wysokość

-    **Safe Height**
    

-    **Clearance Height**
    



### Operacja

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **BoundBox**
    

-    **Scan Type**
    

-    **Layer Mode**
    

-    **BoundBox extra offset X**
    

-    **BoundBox extra offset Y**
    

-    **Drop Cutter Direction**
    

-    **Depth Offset**
    

-    **Step Over**
    

-    **Sample Interval**
    

-    **Optimize Output Enabled**
    

-    **Use Start Point**
    

-    **Boundary Enforcement**
    

-    **Optimize Linear Paths**
    



## Źródła

-   Symulator G-Code *(ścieżka)*: [NCViewer](https://ncviewer.com/)
-   Symulator G-code *(ścieżka)*: [CAMotics](https://www.camotics.org/)





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Surface/pl
