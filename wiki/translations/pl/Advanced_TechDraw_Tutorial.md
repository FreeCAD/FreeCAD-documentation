





{{TutorialInfo/pl
|Topic=Modelowanie
|Level=Użytkownik zaawansowany
|Author=domad
|Time= nieokreślony
|FCVersion=0.19.23300 lub nowszy
|Files=brak
}}

## Krótko o celu 

Tworzenie punktów, linii, okręgów, łuków, itp. w widokach środowiska Rysunek Techniczny i / lub całych rysunkach \"kosmetycznych\" z absolutną precyzją, odpowiednią dla narzędzi wymiarujących, w które wyposażone jest środowisko pracy, w celu wygenerowania zgodnych i szczegółowych rysunków technicznych.

## Wprowadzenie

Ten poradnik wprowadza doświadczonego użytkownika do korzystania z zaawansowanych narzędzi i technik istniejących w innych środowiskach pracy, aby rozszerzyć funkcjonalność brakującą w środowisku <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md). Ten poradnik nie jest kompletnym i wyczerpującym przewodnikiem po środowisku Rysunek Techniczny i wiele narzędzi i możliwości nie jest w nim przedstawionych. Powinien jednak przyczynić się do przezwyciężenia trudności, które napotyka się podczas sporządzania kosztorysu i wzbogacania rysunku technicznego przy środowiska Rysunek Techniczny. Ten poradnik przeprowadzi zaawansowanych użytkowników przez etapy potrzebne do produkcji rysunków technicznych części z [Poradnikiem Podstawy dla Środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md) przy użyciu narzędzi rysunkowych środowiska Rysunek Techniczny.

1.  środowisko <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) *(linie, polilinie, obwody, łuki, krzywe złożone, krzywe Beziera, itd.)*, a w szczególności zatrzaski, aby stworzyć na obiekcie efektywnie precyzyjne \"punkty kosmetyczne\", które mogą być następnie użyte do wymiarowania w środowisku Rysunek Techniczny.
2.  Możliwe jest również użycie <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownika](Sketcher_Workbench/pl.md) jako
    -   generatora \"szkicu-bazowegoTD\" *(podstawy szkiców dla środowiska Rysunek Techniczny)* w 2D *(np. takie jak schemat systemu, plany pięter, elewacje, widoki części mechanicznych lub ogólnych, itp.)*
    -   używając bezpośrednio szkiców, które wygenerowały modele 3D, lub przez
    -   konwersję do szkicu \"łącznika kształtu\" wygenerowanego z Rysunków roboczych uzyskanych z powierzchni i / lub przekrojów modeli 3D.
3.  Aby uzyskać poszczególne przekroje *(przez cięcia na różnych płaszczyznach lub osiach)* do prezentacji na stronie w środowisku Rysunek Techniczny *(zaleca się użycie kopii oryginalnego obiektu przestrzennego)*, a następnie poprzez tworzenie płaszczyzn *(nawet na różnych osiach)* za pomocą środowiska <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [WorkFeatureDev](Workfeature_Workbench/pl.md), możliwe jest sekcjonowanie kopii obiektu 3D <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Pokroić na plasterki](Part_SliceApart/pl.md) właściwość w środowisku **Część**, aby uzyskać ściany do konwersji na szkic <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> [Rysunek Roboczy na szkic](Draft_Draft2Sketch.md) właściwość w środowisku **Rysunek Roboczy**, a następnie poprzez środowisko **Szkicownik** edytować je tak, aby nadawały się do rysunku technicznego, który chcemy wygenerować w środowisku Rysunek Techniczny. Środowisko pracy [Workfeature](Workfeature_Workbench/pl.md) *(oraz [Makro WorkFeatures](Macro_WorkFeatures/pl.md))* jest pełne wygodnych funkcji dodatkowych, które pozwalają nam w prosty sposób tworzyć płaszczyzny *(teoretycznie nieskończone w rozciągłości i ilości)* poprzez wybór trzech punktów *(wierzchołków)* *(pamiętajmy, że dla trzech punktów przechodzących, jedna i tylko jedna płaszczyzna przechodzi przez trzy nie wyrównane punkty)* jest aksjomatem geometrycznym, który potwierdza bez żadnych niejasności *(!)* zasadność i znaczenie narzędzia WorkFeatureDev do bardzo łatwego tworzenia precyzyjnych planów.

*(\*Jest to dość porównywalne z poleceniem AutoCAD Slice [1](https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Core/files/GUID-27593C5E-4B89-41F2-872B-927D69517CBF-htm.html), które bazuje na tym aksjomacie. Bez wstępnego budowania jakiejkolwiek nowej płaszczyzny, definiuje się płaszczyznę cięcia z wykorzystaniem trzech punktów).*

**Uwaga:** Płaszczyzny te mogą być połączone przez nałożenie / zbieżność dwóch krawędzi przy użyciu funkcji logicznej <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Złączenie](Part_Fuse/pl.md) w środowisku **Część**. Tak powstałe i odpowiednio ustawione *(zgodnie z naszymi przepisami)* płaszczyzny posłużą jako **ostrza tnące** <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Pokroić na plasterki](Part_SliceApart/pl.md) właściwość w środowisku **Część**, tnąc nasz obiekt 3D na kilka części zgodnie z wybranym planarnym potwierdzeniem.

## Nim zaczniesz 

Do wykonania rysunków z załączonych przykładów użyto następujących środowisk pracy:
\* <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md)

-   <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md)
-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md)
-   <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [Workfeature](Workfeature_Workbench/pl.md)
-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md)

## Zadanie

Etapy procedury:

1.  Tworzenie obiektu*(ów)* 3D zgodnie z kanonami tradycyjnego modelowania.
2.  możliwość tworzenia niezależnych lub prostych kopii, np. do wykorzystania przy tworzeniu specyficznych odcinków ciągłych umieszczonych na wielu płaszczyznach lub osiach, które następnie poprzez wykorzystanie funkcji \"łącznik kształtów\", \"Rysunek Roboczy na szkic\", Widok Kształtu 2D, itp. pozwolą nam na tworzenie doskonałych \"szkiców\", a następnie ich edycję, aby nadawały się *(poprzez tworzenie ad hoc \"punktów lub linii kosmetycznych\")* do wykorzystania w środowisku Rysunek Techniczny. Szkicom tym nadałem nazwę \"szkicu-bazowegoTD\".
3.  wstawianie / tworzenie \"szkicu-bazowegoTD\" w warstwach przynależności *(także metodą \"przeciągnij i upuść\")*.
4.  utworzenie strony rysunku za pomocą szablonu.
5.  tworzenie widoku w środowisku Rysunek Techniczny: wybierz warstwę lub folder grupujący *(który zawiera \"szkic-bazowyTD\")* ze struktury, a następnie kliknij na przycisk \"wstaw widok\". Środowisko Rysunek Techniczny wstawi zawartość warstwy lub folderu grupującego do widoku. Dla poprawnego utworzenia \"szkicu-bazowegoTD\" musi być prostopadły do widoku na ekranie. Zaznaczam, że cokolwiek dodamy później w warstwie lub w folderze grupującym, lub zmodyfikujemy \"szkic-bazowyTD\", Widok będzie aktualizowany w czasie rzeczywistym. Należy pamiętać, że aktualizacje i / lub modyfikacje mogą mieć wpływ na wymiary już wprowadzone lub linie kosmetyczne utworzone za pomocą konkretnego narzędzia środowiska Rysunek Techniczny w widoku.
6.  Po zdefiniowaniu \"szkicu-bazowegoTD\" w widoku, możemy przejść do wymiarowania odpowiednimi narzędziami środowiska Rysunek Techniczny.

Istnieje możliwość wstawienia \"szkicu-bazowegoTD\" również do widoków z grupy rzutowej:

-   wybierz widok rzutu -\> zakładka właściwości -\> Dane -\> sekcja rekordu \"Rzutowanie\" -\> Źródło kliknij na przycisk z trzema kropkami i bezpośrednio dodaj \"szkic-bazowyTD\" lub warstwę, która go zawiera.

Należy zwrócić uwagę, że \"szkic-bazowyTD\" musi być umieszczony na najwyższej płaszczyźnie modelu / obiektu, w przeciwnym razie zostanie ukryty i będzie niewidoczny w środowisku Rysunek Techniczny. Wydaje się, że przekroje uzyskane z widoków nie mają takiej możliwości. Wszędzie tam, gdzie zachodzi potrzeba stworzenia precyzyjnych punktów kosmetycznych nadających się do wymiarowania *(np. punktów stycznych)*, można je wygenerować:

-   w Szkicowniku poprzez linie konstrukcyjne i wstawianie na końcach okręgów o nieskończenie małych średnicach / promieniach *(0.00001)*, będą one widziane przez środowisko Rysunek Techniczny jako punkty / wierzchołki nadające się do wymiarowania.
-   w Rysunku Roboczym tą samą metodą wstawiamy do odpowiedniej warstwy lub folderu-grupy.

Po zmodyfikowaniu \"szkicu-bazowegoTD\" lub dodaniu obiektu Rysunku roboczego w warstwie lub folderze grupującym, środowisko Rysunek Techniczny automatycznie zaktualizuje widok, jeżeli tak się nie stanie, zaktualizuj go ręcznie odpowiednim poleceniem. Aby wstawić wypełnienie przekroju lub wzory:
zwróć uwagę na linie utworzone na powierzchniach, które przecinają dwie lub więcej krawędzi, są one widziane przez środowisko Rysunek Techniczny jako elementy oddzielające powierzchnie, które mają wpływ na tworzenie wypełnień lub wzorów. Ma to miejsce np. podczas tworzenia zewnętrznych linii definiujących gwint otworu, linia ta uniemożliwi wypełnienie lub wzór przed przedłużeniem, uniemożliwiając dotarcie do tego, który definiuje otwór wstępny. W tym przypadku lepiej jest utworzyć punkty kosmetyczne poprzez linie konstrukcyjne wstawiając okręgi o nieskończenie małym promieniu w wierzchołkach, które będą widziane przez środowisko Rysunek Techniczny jako punkty kosmetyczne, a następnie połączyć je w ty środowisku z utworzeniem linii kosmetycznej przez dwa punkty.
Wszystkie linie i / lub ścieżki *(w tym kosmetyczne)*, które są wyświetlane w widokach można edytować w formatowaniu poprzez polecenie \"Zmień wygląd wybranych linii\" w środowisku Rysunek Techniczny.
Aby utworzyć specyficzne ciągłe przekroje na różnych osiach lub płaszczyznach, użyłem narzędzia \"WorkFeatureDev\", które pozwala na tworzenie \"bryłowych\" płaszczyzn, o grubości \"0\", poprzez wybranie trzech wierzchołków. Płaszczyzny te mogą być łączone poprzez wspólną lub nakładającą się krawędź za pomocą funkcji logicznych środowiska pracy \"Część\", a następnie użyte do krojenia / rozcinania modelu bryłowego za pomocą polecenia \"Rozetnij\" w tym samym środowisku pracy. Powierzchnie przyciętych obiektów mogą być odpowiednio wykorzystane do tworzenia, za pomocą funkcji \"Łącznik kształtów\", \"szkiców-bazowychTD\" do tworzenia specyficznych widoków przekroju w środowisku Rysunek Techniczny i w ten sposób być w stanie je wymiarować i uszczegóławiać.
Wierzę, że upubliczniłem każdą \"sztuczkę\" *(lub raczej system)* eksperymentowałem, aby móc używać bardziej specyficznych narzędzi *(nie przewidzianych dla środowiska Rysunek Techniczny)* i tworzyć wysokiej jakości profesjonalne rysunki techniczne bez żadnych ograniczeń, dzięki czemu środowisko pracy Rysunek Techniczny jest bardziej wydajne i dostosowane do wszelkich potrzeb, najprawdopodobniej na równi *(jeśli nie bardziej elastyczne i potężne)* z komercyjnymi odpowiednikami.
. Należy powiedzieć, co nie jest bez znaczenia, że z tego systemu można tworzyć całe pliki 2D i cytować je ze środowiskiem Rysunek Techniczny w taki sam sposób jak \"LibreCad\" lub \"Autocad LT\" lub innych dwuwymiarowych programów CAD.
. Mam nadzieję, że wyraziłem się wystarczająco jasno *(tłumaczenie pozwala)* wyjaśniając procedurę *(\"trick / system\")*, która moim zdaniem jest \"łatwiejsza do zrobienia niż do powiedzenia\", ponieważ chodzi o możliwość wprowadzania rysunków 2D do widoków Rysunku Technicznego utworzonych za pomocą środowiska \"Rysunek Roboczy\" i / lub \"Szkicownik\" po prostu wybierając je ze struktury i tworząc widok w Rysunku Technicznym za pomocą odpowiedniego polecenia \"utwórz widok\"; ale myślałem o zrobieniu czegoś przyjemnego i bardziej technicznego opisując procedurę, na pewno, w \"uproszczony\" sposób, aby stworzyć minimum zorganizowanego przepływu pracy.
To zależy od każdego z nas, od wyobraźni i pomysłowości, aby zoptymalizować go do maksimum, aby uzyskać najlepszy wynik.
Załączam pliki niektórych przykładów przepływu pracy rysunków technicznych *(niemożliwe do wykonania tylko w środowisku Rysunek Techniczny)*, z których obrazy pokazane poniżej zostały podjęte.
W nadziei, że będzie przydatne, dobra praca i dobre eksperymenty!

## Uwagi

## Perspektywy na przyszłość 

Opisana ścieżka może jednak stanowić punkt wyjścia *(lub pomysł)* do napisania dodatkowego kodu automatyzującego system i zintegrowania go bezpośrednio ze środowiskiem Rysunek Roboczy za pomocą odpowiednich funkcji przycisków / poleceń.

## Odnośniki internetowe 

-   [Makrodefinicja: Właściwości użytkowe](https://wiki.freecadweb.org/Macro_WorkFeatures) witryna Wiki makrodefinicji
-   [środowisko FreeCAD WorkFeature](https://github.com/Rentlau/WorkFeature-WB) Repozytorium kodu źródłowego
-   [Rysunek Roboczy bez ograniczeń = Układ autocad](https://forum.freecadweb.org/viewtopic.php?t=54499) wątek na forum
-   [Rysunek Roboczy: -- jak używać narzędzi przyciągania środowiska Rysunek Roboczy do tworzenia \"wierzchołków / punktów kosmetycznych\"](https://forum.freecadweb.org/viewtopic.php?f=28&t=53329) Wątek na forum w języku włoskim.


{{Tutorials navi

}} {{TechDraw Tools navi}} 
