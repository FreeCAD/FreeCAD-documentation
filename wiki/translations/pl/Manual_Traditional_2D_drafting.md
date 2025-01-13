# Manual:Traditional 2D drafting/pl
{{Manual:TOC}}

Środowisko pracy Rysunek Roboczy we FreeCAD pełni rolę mostu między rysowaniem 2D a modelowaniem 3D, co czyni je unikalnym w porównaniu do tradycyjnych systemów CAD 2D, takich jak AutoCAD. Choć FreeCAD działa w pełni w środowisku 3D, środowisko pracy Rysunek Roboczy zostało zaprojektowane, aby zapewnić użytkownikom znane narzędzia do rysowania 2D, oferując jednocześnie elastyczność płynnego przejścia między szkicami 2D a obiektami 3D. Na przykład, możesz ustawić niestandardowe płaszczyzny robocze, aby rysować na określonych powierzchniach lub w określonych orientacjach, umożliwiając budowanie modeli parametrycznych. Ponieważ FreeCAD jest parametryczny, wszelkie zmiany dokonane w wymiarach są automatycznie aktualizowane w całym projekcie.

Jedną z zalet środowiska pracy Rysunek Roboczy jest jego wszechstronny zestaw narzędzi, który obejmuje zarówno podstawowe narzędzia do rysowania, jak i zaawansowane narzędzia do modyfikacji. Narzędzia te mogą być używane nie tylko do rysowania 2D, ale także do manipulowania obiektami w przestrzeni 3D. Możesz ustawić płaszczyzny robocze, zdefiniować siatki i zastosować ograniczenia, aby zapewnić, że zależności geometryczne pozostaną nienaruszone w całym projekcie. Obiekty Rysunku Roboczego mogą być modyfikowane i przemieszczane za pomocą trybów przyciągania oraz różnych ograniczeń, co znacznie ułatwia precyzyjne rysowanie.

Niektóre z narzędzi dostępnych w środowisku pracy Rysunek Roboczy:

1.  Narzędzia do rysowania:

-   <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linia](Draft_Line/pl.md), <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [polilinia](Draft_Wire/pl.md): Te narzędzia pozwalają na tworzenie prostych odcinków linii lub ciągłych polilinii, które mogą być ograniczane i przekształcane w obiekty 3D.
-   <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Okrąg](Draft_Circle/pl.md), <img alt="" src=images/Draft_Ellipse.svg  style="width:16px;"> [Elipsa](Draft_Ellipse/pl.md), oraz <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Łuk](Draft_Arc/pl.md): Służą do definiowania podstawowych kształtów okrągłych i eliptycznych, z możliwością dalszej manipulacji.

1.  Narzędzia do manipulacji:

-   <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Przesuń](Draft_Move/pl.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Obróć](Draft_Rotate/pl.md) lub <img alt="" src=images/Draft_Scale.svg  style="width:16px;"> [Skaluj](Draft_Scale/pl.md): Operacje te działają zarówno w przestrzeni 3D, jak i 2D, oferując elastyczność w pozycjonowaniu obiektów.
-   <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Odsunięcie](Draft_Offset/pl.md): Podobnie jak w tradycyjnych systemach CAD, umożliwia tworzenie równoległych linii lub krzywych.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Przytnij](Draft_Trimex/pl.md) oraz <img alt="" src=images/Draft_Stretch.svg  style="width:16px;"> [Rozciągnij](Draft_Stretch/pl.md): Modyfikują linie i kształty poprzez przycinanie lub ich wydłużanie, aby przecinały lub spotykały się z innymi obiektami.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:16px;"> [Odbicie lustrzane](Draft_Mirror/pl.md) oraz <img alt="" src=images/Draft_Array.svg  style="width:16px;"> [Szyk](Draft_Array/pl.md): Te narzędzia powielają i tworzą wzory obiektów, idealne do komponentów powtarzalnych.

System przyciągania w środowisku pracy Rysunek Roboczy w FreeCAD został zaprojektowany z myślą o precyzji. Niezależnie od tego, czy pracujesz w 2D, czy 3D, możesz przyciągać do kluczowych punktów, takich jak końce, środki odcinków i środki okręgów, co ułatwia precyzyjne ustawianie elementów względem siebie. Tryby przyciągania, takie jak prostopadłość, styczność i przecięcie, dodatkowo poprawiają precyzję. Połączone z płaszczyzną roboczą i systemem siatek, te narzędzia zapewniają dokładne wyrównanie obiektów i komponentów.

Parametryczna natura FreeCAD umożliwia stosowanie ograniczeń do elementów rysunku, zapewniając, że zależności geometryczne pozostaną nienaruszone. Na przykład, możesz ustawić linie równoległe lub prostopadłe oraz określić stałe odległości między elementami. Ograniczenia te mogą być później dostosowane, co sprawia, że zmiany w projekcie są płynne i spójne w całym projekcie. Środowisko pracy Rysunek Roboczy integruje się także bezproblemowo z innymi środowiskami pracy FreeCAD, takimi jak Szkicownik, które jest przeznaczone do bardziej ograniczonego parametrycznego projektowania 2D, oraz Rysunek Techniczny, który służy do tworzenia technicznych rysunków 2D do celów dokumentacyjnych.

Zaawansowane funkcje środowiska pracy Rysunek Roboczy obejmują możliwość importowania i eksportowania plików w formatach takich jak DXF i SVG, co pozwala na pracę z projektami lub ich udostępnianie użytkownikom innych programów CAD. Skrypty Pythona dodatkowo rozszerzają możliwości FreeCAD, umożliwiając automatyzację zadań lub tworzenie niestandardowych procesów roboczych. Możesz pisać skrypty, które generują obiekty rysunkowe na podstawie określonych zasad geometrycznych, upraszczając powtarzalne zadania.

Aby zaprezentować sposób pracy i możliwości środowiska Rysunek Roboczy, przejdziemy przez proste ćwiczenie, którego wynikiem będzie ten mały rysunek, przedstawiający plan piętra niewielkiego domu, który zawiera tylko blat kuchenny *(to dosyć absurdalny plan piętra, ale możemy tu robić co chcemy, prawda?)*:

![](images/Exercise_cabin_01.jpg )

-   Przejdź do środowiska pracy **Rysunek Roboczy**
-   Jak we wszystkich programach do rysunków technicznych, warto prawidłowo ustawić swoje środowisko, co pozwoli zaoszczędzić dużo czasu. Jeśli chcesz spersonalizować swoje doświadczenie ze środowiskiem pracy Rysunek Roboczy, możesz to łatwo zrobić dostosowując różne ustawienia w panelu preferencji środowiska pracy Rysunek Roboczy wchodząc w **Edycja → Preferencje → Rysunek Roboczy**. W tym ćwiczeniu jednak będziemy działać tak, jakby te ustawienia były pozostawione z domyślnymi wartościami.

![](images/FreeCAD_DraftPreferences.png )

-   Panel preferencji Rysunek Roboczy w FreeCAD umożliwia dostosowanie różnych aspektów środowiska rysowania 2D. W **Ustawieniach ogólnych** możesz zdefiniować domyślną płaszczyznę roboczą, dostosować precyzję dziesiętną oraz ustawić domyślną szerokość linii, styl i kolor obiektów. Sekcja **Siatka i przyciąganie** pozwala na kontrolowanie widoczności siatki, odstępów oraz trybów przyciągania, umożliwiając precyzyjne wyrównanie i pozycjonowanie elementów. Opcje **Styl wizualny** pozwalają na dostosowanie wyglądu obiektów i siatki, w tym kolorów linii i wypełnienia. W sekcji **Tekst i wymiary** możesz skonfigurować domyślny rozmiar czcionki, czcionkę i kolor dla adnotacji, zapewniając przejrzystość rysunków technicznych.

![](images/Draft_toolbars.png )

-   Włączenie wszystkich przycisków przyciągania jest wygodne, ale też spowalnia rysowanie, ponieważ potrzeba więcej obliczeń przy przesuwaniu kursora myszy. Często lepiej zostawić tylko te, z których będzie się faktycznie korzystało.

-   Zacznijmy od włączenia **trybu konstrukcyjnego**, który pozwoli nam rysować linie pomocnicze, na podstawie których narysujemy naszą finalną geometrię. Można to zrobić, naciskając przycisk <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> [Przełącz tryb konstrukcyjny](Draft_ToggleConstructionMode/pl.md).
-   Jeśli wolisz, możesz ustawić płaszczyznę roboczą na XY. Zablokuje to płaszczyznę roboczą, zapewniając, że pozostanie na płaszczyźnie XY, niezależnie od tego, jak zmienisz widok. Jeśli zdecydujesz się tego nie robić, płaszczyzna robocza automatycznie dostosuje się do bieżącego widoku, co oznacza, że będziesz musiał upewnić się, że jesteś w widoku z góry, kiedy chcesz rysować na płaszczyźnie XY (podłoża), aby uniknąć niezamierzonych zmian orientacji.

Teraz możemy przełączyć się do środowiska pracy Część i rozpocząć tworzenie naszej pierwszej nogi stołu.

-   Naciśnij przycisk <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> **Prostokąt**.
-   Narysuj prostokąt o wymiarach 2 metry na 2 metry, zaczynając od punktu (0,0,0), pozostawiając współrzędną Z na zero. Cały proces możesz wykonać efektywnie przy użyciu klawiatury, bez potrzeby korzystania z myszy. Po prostu wpisz:
    -   **re**, **Enter**, **Enter**, **Enter**, 2m, **Enter**, 2m, **Enter**, 0 oraz **Enter**.

Ten sposób pracy oparty na klawiaturze przyspiesza rysowanie, szczególnie przy powtarzalnych zadaniach lub precyzyjnych wprowadzaniach, co sprawia, że jest idealny dla użytkowników chcących uprościć swój proces roboczy. Możesz zobaczyć sekwencję klawiszy dla każdego obiektu, najeżdżając kursorem na odpowiedni przycisk.

-   Zduplikuj ten prostokąt o 15 cm do wewnątrz, używając narzędzia <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Odsunięcie](Draft_Offset/pl.md), włączając tryb kopiowania i ustawiając odległość na 15 cm.

![](images/Exercise_cabin_02.png )

-   Dalej możemy narysować kilka pionowych linii aby zdefiniować położenie dzrwi i okien, korzystając z narzędzia <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linia](Draft_Line/pl.md) (zauważ, że pole \"względne\" powinno być odznaczone dla tego kroku). Przecięcie tych linii z dwoma prostokątami da nam przydatne przecięcia do przyciągania ścian. Narysuj pierwszą linię definiując następujące punkty:
    -   **P1** (15cm, 1m, 0) i **P2** (15cm, 3m, 0).
-   Teraz zduplikujemy tę linię 5 razy. Naciśnij narzędzie <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Przesuń](Draft_Move/pl.md) z włączonym trybem <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> [Klonuj](Draft_Clone/pl.md). Upewnij się, że **Tryb względny** jest włączony. Tryb kopiowania zapewnia, że każde przesunięcie tworzy nową linię zamiast przesuwać oryginalną, podczas gdy Tryb względny pozwala na definiowanie ruchów na podstawie odległości względnych, co ułatwia pozycjonowanie bez konieczności obliczania dokładnych współrzędnych. Zacznij od wybrania oryginalnej linii i rozpocznij operację przesunięcia, wybierając dowolny punkt początkowy, na przykład (0,0,0). Po każdym przesunięciu wykonaj kolejną operację na nowo utworzonej linii, dzięki czemu każda kopia będzie oparta na poprzedniej. Zdefiniuj względne punkty końcowe dla każdej nowej linii.
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

![](images/Exercise_cabin_03.jpg )

-   To wszystko czego potrzebujemy na ten moment, więc możemy wyłączyć tryb konstrukcyjny. Sprawdź czy cała geometria konstrukcyjna została umieszczona w grupie \"Construction\", co ułatwia schowanie wszystkiego na raz lub nawet późniejsze usunięcie.
-   Teraz narysujmy nasze dwie części ściany używając narzędzia <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polilinia](Draft_Wire/pl.md). Upewnij się, że <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [przyciąganie do przecięcia](Draft_Snap/pl.md) jest włączone, ponieważ będziemy musieli przyciągnąć się do przecięć naszych linii i prostokątów. Narysuj dwie polilinie w następujący sposób, klikając wszystkie punkty ich konturów. Aby je zamknąć, kliknij ponownie na punkcie początkowym lub wciśnij przycisk **Zamknij**:

![](images/Exercise_cabin_04.jpg )

-   Możemy nadać ścianom ładne kreskowanie. Wybierz obie ściany, upewnij się, że ich właściwość **Make Face** (w zakładce Dane) jest ustawiona na **{{TRUE/pl}}**, następnie ustaw ich właściwość **Pattern** (w zakładce Widok) na **Simple** a **Pattern size** według uznania, np. **0.005**.

![](images/Draft_Pattern.png )

-   Możemy teraz schować geometrię konstrukcyjną poprzez kliknięcie prawym przyciskiem myszy na grupie Construction i wybranie **Ukryj zaznaczone**.
-   Narysujmy teraz okna i drzwi. Upewnij się, że <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [przyciąganie do punktu środkowego](Draft_Snap/pl.md) jest włączone i narysuj sześć linii w następujący sposób:

![](images/Exercise_cabin_06.jpg )

-   Zmienimy teraz linię drzwi aby utworzyć symbol otwartych drzwi. Zacznij od obrócenia linii przy pomocy narzędzia <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Obróć](Draft_Rotate/pl.md). Wskaż punkt końcowy linii jako środek obrotu, nadaj kąt początkowy **0** i kąt obrotu **-90**.
-   Następnie utwórz łuk symbolizujący otwarcie drzwi przy pomocy narzędzia <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Łuk](Draft_Arc/pl.md). Wybierz ten sam punkt, który był środkiem obrotu w poprzednim kroku jako środek, kliknij na drugim punkcie linii aby nadać promień a następnie punkty początkowe i końcowe jak poniżej:

![](images/Exercise_cabin_07.jpg )

-   Możemy teraz zacząć umieszczać jakieś meble. Na początek umieśćmy blat rysując prostokąt z górnego lewego narożnika wewnętrznego i nadając mu szerokość 170cm i wysokość -60cm. Na rysunku poniżej, właściwość **Transparency** prostokąta jest ustawiona na 80%, aby nadać mu wygląd mebla.
-   Następnie dodajmy zlew i płytę kuchenki. Rysowanie takich symboli ręcznie może być bardzo uciążliwe i zwykle łatwo je znaleźć w internecie, np. na stronie <http://www.cad-blocks.net> . W sekcji **Do pobrania** poniżej, dla wygody wydzieliliśmy zlew i płytę kuchenki z tego projektu i zapisaliśmy je jako pliki DXF. Możesz pobrać te dwa pliki odwiedzając witryny przy pomocy linków poniżej i klikając prawym przyciskiem myszy przycisk **Raw** a następnie wybierając **Zapisz link jako**.
-   Wstawienia pliku DXF do otwartego dokumentu FreeCAD można dokonać poprzez wybranie opcji **Plik → Import** z menu lub przeciągnięcie i upuszczenie pliku z eksploratora plików do okna programu FreeCAD. Zawartość plików DXF może nie pojawić się w samym środku Twojego bieżącego widoku, w zależności od tego gdzie była w pliku DXF. Możesz skorzystać z opcji **Widok → Widoki standardowe → Dopasuj wszystko** aby oddalić widok i znaleźć zaimportowane obiekty. Wstaw dwa pliki DXF a następnie przesuń je do odpowiedniej lokalizacji na blacie:

![](images/Exercise_cabin_08.jpg )

-   Teraz możemy umieścić kilka wymiarów, używając narzędzia <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Wymiar](Draft_Dimension/pl.md). Aby utworzyć wymiar, zaczynasz od wybrania trzech punktów: pierwszy punkt ustawia początek pomiaru, drugi punkt definiuje punkt końcowy, a trzeci punkt określa, gdzie zostanie umieszczona linia wymiaru i tekst. Starannie klikając te punkty, zapewniasz, że wymiar dokładnie reprezentuje odległość między dwoma wybranymi punktami. Jeśli chcesz wymusić, aby wymiar był idealnie poziomy lub pionowy, nawet jeśli punkty początkowy i końcowy nie są wyrównane, przytrzymaj klawisz **Shift** podczas klikania drugiego punktu. Zablokuje to wymiar w żądanej orientacji. Możesz dalej dopracować wymiar, dostosowując właściwości takie jak rozmiar tekstu, precyzję i kolor w panelu właściwości, zapewniając, że wymiary pasują do wizualnych i technicznych standardów twojego projektu.
-   Możesz zmienić położenie tekstu wymiaru klikając dwukrotnie na wymiarze w widoku drzewa. Punkt kontrolny pozwoli Ci przesunąć tekst graficznie. W naszym ćwiczeniu, teksty \"0.15\" zostały przesunięte dalej dla większej czytelności.
-   Możesz zmienić zawartości tekstów wymiarów poprzez edycję ich właściwości **Override**. W naszym przykładzie, teksty wymiarów drzwi i okien zostały edytowane aby wskazać ich wysokości:

![](images/Exercise_cabin_09.jpg )

-   Dodajmy trochę tekstów z opisem przy pomocy narzędzia <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Tekst](Draft_Text/pl.md). Wskaż punkt aby spozycjonować tekst a następnie wpisz linie tekstu, wciskając Enter po każdej linii. Aby skończyć, wciśnij Enter dwukrotnie.
-   Linie wskazujące, które łączą tekst z opisywanym obiektem są tworzone przy pomocy narzędzia Polilinia. Narysuj polilinie, zaczynając od pozycji tekstu, do miejsca, które opisuje. Po dokonaniu tego możesz dodać kropkę lub strzałkę na końcu polilinii, ustawiając właściwość **End Arrow** na **TRUE/pl**

![](images/Exercise_cabin_10.jpg )

-   Nasz rysunek jest teraz ukończony! Z uwagi na liczbę obiektów w projekcie, warto przeprowadzić porządkowanie i reorganizację przed uznaniem go za zakończony. Organizowanie wszystkiego w jasne, logiczne grupy nie tylko pomoże utrzymać projekt w porządku, ale także znacznie ułatwi innym nawigację i zrozumienie pliku. Grupując powiązane elementy---takie jak meble, urządzenia czy elementy architektoniczne---możesz uprościć układ i poprawić czytelność projektu. To również sprawi, że przyszłe modyfikacje lub zmiany będą znacznie łatwiejsze do przeprowadzenia, szczególnie jeśli projekt musi zostać udostępniony lub współtworzony. Dodatkowo, czysta struktura zapewnia, że każda osoba przeglądająca rysunek szybko znajdzie konkretne elementy, bez konieczności przeszukiwania zatłoczonego obszaru roboczego, co w końcu przyczyni się do bardziej profesjonalnego i dopracowanego finalnego produktu. Poświęcenie dodatkowego czasu na organizację teraz, może zaoszczędzić znacznie więcej czasu i wysiłku w przyszłości.

![](images/Draft_Organised.png )

-   Możemy teraz wydrukować naszą pracę umieszczając ją na arkuszu rysunkowym, który pokażemy później w tym poradniku lub wyeksportować nasz rysunek bezpośrednio do innych programów CAD przy pomocy formatu DXF. Po prosty zaznacz grupę \"Floor plan\", wybierz opcję **Plik → Eksport** i wskaż format **Autodesk DXF**. Plik można wtedy otworzyć w dowolnym innym programie CAD 2D, takim jak [LibreCAD](http://www.librecad.org). Możesz zauważyć pewne różnice, w zależności od konfiguracji danego programu.

![](images/Exercise_cabin_12.jpg )

-   Najważniejszą kwestią dotyczącą środowiska Rysunek Roboczy jest jednak to, że geometria 2D, którą tworzysz, może służyć jako podstawa do tworzenia obiektów 3D. Możesz łatwo wyciągnąć te kształty do 3D za pomocą narzędzia <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Wyciągnij](Part_Extrude/pl.md) znajdującego się w [środowisku pracy Część](Part_Workbench/pl.md). Alternatywnie, jeśli wolisz pozostać w środowisku Rysunek Roboczy, możesz użyć narzędzia <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Przytnij](Draft_Trimex/pl.md), które łączy funkcje przycinania, wydłużania i wyciągania. Narzędzie Przytnij zasadniczo wykonuje wyciągnięcie za kulisami, ale robi to w sposób \"typowy dla Rysunku Roboczego\", pozwalając na wizualne wskazanie i przyciągnięcie długości wyciągnięcia, dając większą kontrolę i precyzję podczas pracy bezpośrednio w środowisku rysunkowym. Ta elastyczność sprawia, że przejście z 2D do 3D jest płynne i intuicyjne, szczególnie dla osób zaznajomionych z podejściem 2D, oferując jednocześnie zaawansowane możliwości modelowania 3D.
-   Wciskając przycisk <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [płaszczyzny roboczej](Draft_SelectPlane/pl.md) po wybraniu ściany obiektu, możesz też umieścić płaszczyznę roboczą w dowolnym miejscu, a zatem rysować obiekty środowiska Rysunek Roboczy na innych płaszczyznach, np. na górze ścian. Można je potem wyciągnąć aby utworzyć inne bryły 3D. Poćwicz z ustawieniami płaszczyzny roboczej na jednej z górnych powierzchni ścian a następnie narysuj tam jakieś prostokąty.

![](images/Exercise_cabin_13.jpg )

-   Wszystkie typy otwarć można też łatwo utworzyć rysując obiekty środowiska Rysunek Roboczy na powierzchniach ścian, wyciągając je i korzystając z operacji boolowskich w środowisku Część aby odjąć je od innych brył, jak w poprzednim rozdziale.

Podstawowo, środowisko Rysunek Roboczy oferuje bardziej graficzne i intuicyjne podejście do tworzenia podstawowych operacji, podobne do tych znajdujących się w środowisku pracy Część. W środowisku pracy Część, pozycjonowanie obiektów często polega na ręcznym dostosowywaniu parametrów, takich jak wartości umiejscowienia (pozycja, obrót itd.), co daje precyzyjną kontrolę, ale może być mniej intuicyjne, szczególnie podczas szybkich edycji. W przeciwieństwie do tego, środowisko Rysunek Roboczy umożliwia wykonanie tych samych operacji wizualnie na ekranie, co ułatwia przemieszczanie, obracanie i manipulowanie obiektami bezpośrednio w przestrzeni roboczej za pomocą narzędzi przyciągania i opcji względnego pozycjonowania.

Ta różnica sprawia, że środowiska pracy wzajemnie się uzupełniają. Środowisko Rysunek Roboczy jest idealne do szybkiego, interaktywnego projektowania, umożliwiając rysowanie i pozycjonowanie obiektów bez konieczności ciągłego wprowadzania precyzyjnych wartości numerycznych. Z drugiej strony, środowisko Część oferuje bardziej szczegółową, parametryczną kontrolę nad właściwościami obiektów, co sprawia, że jest lepsze do dokładnych regulacji, szczególnie w projektach inżynieryjnych lub technicznych.

Piękno FreeCAD polega na tym, że nie musisz wybierać między jednym a drugim. Możesz tworzyć [niestandardowe paski narzędzi](Interface_Customization/pl.md) łącząc narzędzia zarówno ze środowiska pracy Rysunek Roboczy, jak i Część, co daje Ci elastyczność przełączania się między metodami graficznymi i parametrycznymi w zależności od potrzeb. Dzięki temu możesz cieszyć się najlepszymi cechami obu światów --- szybkimi, na ekranie dostosowaniami ze środowiska Rysunek Roboczy oraz precyzją środowiska Część --- w zależności od wymagań projektu. Dodatkowo, korzystanie ze skrótów klawiszowych i niestandardowych pasków narzędzi może przyspieszyć Twoje tempo pracy, ułatwiając przejście między różnymi operacjami bez zakłócania procesu projektowania.



## Do pobrania 

-   Plik utworzony podczas tego ćwiczenia: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   Plik DXF zlewu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   Plik DXF płyty kuchenki: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   Finalny plik DXF tworzony podczas tego ćwiczenia: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>



## Powiązane

-   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md)
-   [Przyciąganie](Draft_Snap/pl.md)
-   [Płaszczyzna robocza](Draft_SelectPlane/pl.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/pl
