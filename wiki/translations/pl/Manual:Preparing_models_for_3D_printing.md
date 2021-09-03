





{{Manual:TOC/pl}}

Jednym z głównych zastosowań programu FreeCAD jest produkcja rzeczywistych obiektów. Mogą one być zaprojektowane w FreeCAD, a następnie urzeczywistnione na różne sposoby, takie jak przekazanie ich innym ludziom, którzy następnie je zbudują, lub, coraz częściej, przesłanie ich bezpośrednio do [drukarki 3D](https://en.wikipedia.org/wiki/3D_printing) lub [frezarki CNC](https://en.wikipedia.org/wiki/Milling_%28machining%29). W tym rozdziale dowiesz się, jak przygotować swoje modele do przesłania do tych maszyn.

Jeśli byłeś ostrożny podczas modelowania, większość trudności, które możesz napotkać podczas drukowania modelu w 3D została już uniknięta. Wiąże się to w zasadzie z:

-   Upewnieniem się, że twoje obiekty 3D są **bryłowe**. Obiekty świata rzeczywistego są bryłami, model 3D również musi być bryłą. We wcześniejszych rozdziałach widzieliśmy, że FreeCAD bardzo pomaga w tej kwestii, a środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) powiadomi Cię, jeśli wykonasz operację, która uniemożliwi zachowanie bryły modelu. Środowisko pracy [Część](Part_Workbench/pl.md) zawiera również narzędzie <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Sprawdź geometrię](Part_CheckGeometry/pl.md), które jest przydatne do dalszego sprawdzania występowania możliwych wad.
-   Upewnij się co do **wymiarów** swoich obiektów. Jeden milimetr będzie jednym milimetrem w prawdziwym życiu. Każdy wymiar ma znaczenie.
-   Kontrolowanie **degradacji**. Żaden system druku 3D lub frezowania CNC nie może przyjmować plików FreeCAD bezpośrednio. Większość z nich rozumie tylko język maszynowy zwany [G-Code](https://en.wikipedia.org/wiki/G-code). G-kod ma dziesiątki różnych dialektów, każda maszyna lub sprzedawca zazwyczaj ma swój własny. Konwersja twoich modeli do G-Code może być łatwa i automatyczna, ale możesz też zrobić to ręcznie, z pełną kontrolą nad wynikiem. W każdym przypadku, nie można uniknąć utraty jakości modelu podczas tego procesu. Podczas drukowania w 3D, musisz zawsze upewnić się, że ta utrata jakości pozostaje poniżej Twoich minimalnych wymagań.

Poniżej założymy, że pierwsze dwa kryteria są spełnione i że jesteś już w stanie tworzyć obiekty bryłowe o prawidłowych wymiarach. Zobaczymy teraz, jak rozwiązać trzeci punkt.

### Eksport do krajalnicy 

Jest to technika najczęściej stosowana w druku 3D. Obiekt 3D jest eksportowany do innego programu *(slicera)*, który wygeneruje G-kod z obiektu, poprzez pocięcie go na cienkie warstwy (stąd nazwa), które będą odtwarzać ruchy, jakie wykona drukarka 3D. Ponieważ wiele z tych drukarek jest budowanych domowym sposobem, często występują niewielkie różnice pomiędzy nimi. Programy te zazwyczaj oferują zaawansowane możliwości konfiguracyjne, które pozwalają na dostosowanie wydruku dokładnie do możliwości Twojej drukarki 3D.

Rzeczywiste drukowanie 3D jest jednak zbyt obszernym tematem dla tego podręcznika. Zobaczymy jednak jak wyeksportować i użyć tych slicerów, aby sprawdzić czy dane wyjściowe są poprawne.

### Konwersja obiektów do siatek 

Żaden ze slicerów nie będzie, w tym momencie, bezpośrednio przyjmował geometrii bryłowej, jaką produkujemy w FreeCAD. Będziemy więc musieli najpierw przekonwertować każdy obiekt, który chcemy wydrukować na drukarce 3D do postaci [siatki](https://en.wikipedia.org/wiki/Polygon_mesh), którą slicer może otworzyć. Na szczęście, o ile konwersja siatki na bryłę jest skomplikowaną operacją, o tyle konwersja bryły na siatkę jest bardzo prosta. Jedyne na co musimy uważać, to fakt, że to właśnie tutaj nastąpi pogorszenie, o którym wspomnieliśmy powyżej. Musimy sprawdzić, czy utrzymuje się ona w akceptowalnych granicach.

Cała obsługa siatek w programie FreeCAD jest wykonywana przez inne, specyficzne środowisko pracy, [Siatka](Mesh_Workbench/pl.md). Zawiera ono, poza najważniejszymi narzędziami do konwersji pomiędzy obiektami typu Część i Siatka, kilka narzędzi przeznaczonych do analizy i naprawy siatek. Chociaż praca z siatkami nie jest głównym celem programu FreeCAD, podczas pracy z modelowaniem 3D, często musisz mieć do czynienia z obiektami siatkowymi, ponieważ ich użycie jest bardzo rozpowszechnione wśród innych aplikacji. To środowisko pracy pozwala na ich pełną obsługę w programie FreeCAD.

-   Przekształćmy jeden z obiektów, które modelowaliśmy w poprzednich rozdziałach, na przykład klocek lego *(który można pobrać z końca poprzedniego rozdziału)*.
-   Otwórz plik FreeCAD zawierający klocek lego.
-   Przełącz się do środowiska [Siatka](Mesh_Workbench/pl.md).
-   Zaznacz klocek lego.
-   Wybierz menu **Siatki → Utwórz siatkę z kształtu**
-   Otworzy się panel zadań z kilkoma opcjami. Niektóre dodatkowe algorytmy generowania siatek *(Mefisto lub Netgen)* mogą nie być dostępne, w zależności od tego, jak Twoja wersja programu FreeCAD została skompilowana. Standardowy algorytm siatkowania będzie zawsze obecny. Oferuje on mniej możliwości niż dwa pozostałe, ale jest całkowicie wystarczający dla małych obiektów, które mieszczą się w maksymalnym rozmiarze wydruku drukarki 3D.

![](images/Exercise_meshing_01.jpg )

-   Wybierz generator siatki **Standardowy**, i pozostaw wartość odchylenia na wartości domyślnej **0.10**. Naciśnij przycisk **Ok**.
-   Zostanie utworzony obiekt siatki, dokładnie na naszym obiekcie bryły. Albo ukryj bryłę, albo odsuń jeden z obiektów na bok, aby móc porównać oba.
-   Zmień właściwość **Widok → Tryb wyświetlania** nowego obiektu siatki na **Linie płaskie**, aby zobaczyć jak przebiegała triangulacja.
-   Jeśli nie jesteś zadowolony i uważasz, że wynik jest zbyt gruby, możesz powtórzyć operację, obniżając wartość odchylenia. W przykładzie poniżej, dla siatki lewej użyto domyślnej wartości **0.10**, natomiast dla prawej **0.01**:

![](images/Exercise_meshing_02.jpg )

Niemniej jednak w większości przypadków wartości domyślne dadzą zadowalający rezultat.

-   Możemy teraz wyeksportować naszą siatkę do formatu siatek, takiego jak [STL](https://en.wikipedia.org/wiki/STL_%28file_format%29), który jest obecnie najczęściej używanym formatem w druku 3D, poprzez użycie menu **Plik → Eksportuj** i wybranie formatu pliku STL.

Jeśli nie posiadasz drukarki 3D, zazwyczaj bardzo łatwo jest znaleźć komercyjne serwisy, które wydrukują i wyślą Ci wydrukowane obiekty pocztą. Do najbardziej znanych należą [Shapeways](http://www.shapeways.com/) i [Sculpteo](http://www.sculpteo.com/), ale zazwyczaj znajdziesz wiele innych w swoim mieście. We wszystkich większych miastach można obecnie znaleźć [Fab labs](https://en.wikipedia.org/wiki/Fab_lab), czyli warsztaty wyposażone w szereg maszyn do produkcji 3D, w tym prawie zawsze w co najmniej jedną drukarkę 3D. Fab laboratoria są zazwyczaj przestrzeniami społecznymi, które pozwolą Ci korzystać z ich maszyn, za opłatą lub za darmo, w zależności od Fab laboratorium, ale także nauczą Cię jak z nich korzystać i będą promować inne działania wokół produkcji 3D.

### Użycie Slic3r 

[Slic3r](http://slic3r.org/) to aplikacja, która konwertuje obiekty STL na G-code, który może być wysłany bezpośrednio do drukarek 3D. Podobnie jak FreeCAD, jest darmowy, open source\'owy i działa na systemach Linux, Mac OS i Windows. Poprawne skonfigurowanie rzeczy do druku 3D jest skomplikowanym procesem, w którym musisz mieć dobrą znajomość swojej drukarki 3D, więc generowanie G-kodu przed faktycznym wydrukiem nie jest zbyt użyteczne *(Twój plik G-code może nie działać dobrze na innej drukarce)*, ale i tak jest to dla nas użyteczne, aby sprawdzić czy nasz plik STL będzie można bez problemu wydrukować.

To jest nasz wyeksportowany plik STL otwarty w programie Slic3r. Używając zakładki **podgląd** i przesuwając prawy suwak, możemy zwizualizować ścieżkę, którą będzie podążać głowica drukarki 3D, aby zbudować nasz obiekt.

![](images/Exercise_meshing_03.jpg )

### Używanie dodatku Cura 

[Cura](https://ultimaker.com/en/products/cura-software) jest kolejną darmową i otwartoźródłową aplikacją dla Linuksa, Mac i Windows, utrzymywaną przez producenta drukarek 3D [Ultimaker](https://ultimaker.com). Niektórzy użytkownicy programu FreeCAD stworzyli środowisko pracy [Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin), które wewnętrznie korzysta z Cury. Środowisko robocze Cura jest dostępne w repozytorium [dodatków do FreeCAD](https://github.com/FreeCAD/FreeCAD-addons). Aby korzystać z środowiska Cura, musisz również zainstalować samą Curę, która nie jest dołączona.

Po zainstalowaniu zarówno programu Cura, jak i środowiska pracy Cura, będziesz mógł używać go do tworzenia pliku G-code bezpośrednio z obiektów Części, bez potrzeby konwertowania ich na siatki i bez potrzeby otwierania zewnętrznej aplikacji. Wytworzenie kolejnego pliku G-code z naszego klocka Lego, tym razem przy użyciu środowiska Cura, przebiega w następujący sposób:

-   Wczytaj plik zawierający nasze klocki Lego *(można go pobrać na końcu poprzedniego rozdziału)*.
-   Przełącz się na [środowisko Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Ustawiamy miejsce na drukarkę, wybierając z menu **Druk 3D → Utwórz definicję drukarki 3D**. Ponieważ nie zamierzamy drukować w rzeczywistości, możemy pozostawić te ustawienia takimi, jakie są. Geometria łoża drukującego i dostępnej przestrzeni zostanie pokazana w widoku 3D.
-   Przesuń klocek Lego w odpowiednie miejsce, np. na środek łoża drukującego. Pamiętaj, że obiektów środowiska Projekt Części nie można przesuwać bezpośrednio, więc musisz albo przesunąć jego pierwszy szkic *(pierwszy prostokąt)*, albo przesunąć *(i wydrukować)* kopię, którą można wykonać za pomocą narzędzia [Część -\> szybka kopia](Part_SimpleCopy/pl.md). Kopia może być przenoszona, na przykład za pomocą funkcji <img alt="" src=images/Draft_Move.svg  style="width:24px;"> [Rysunek Roboczy → Przesuń](Draft_Move/pl.md).
-   Zaznacz obiekt, który ma zostać wydrukowany i wybierz menu **Druk 3D → Pokrój za pomocą silnika Cura**.
-   W panelu zadań, który się otworzy, upewnij się, że ścieżka do pliku wykonywalnego programu Cura jest poprawnie ustawiona. Ponieważ nie zamierzamy tak naprawdę drukować, możemy pozostawić wszystkie inne opcje tak jak są. Naciśnij przycisk **Ok**. Zostaną wygenerowane dwa pliki w tym samym katalogu co Twój plik FreeCAD, plik STL oraz plik G-code.

![](images/Exercise_meshing_05.jpg )

-   Wygenerowany G-code może być również ponownie zaimportowany do FreeCAD *(przy użyciu preprocesora slic3r)* w celu sprawdzenia.

## Generowanie G-kodu 


{{VeryImportantMessage|'''Ostrzeżenie:''' Ta sekcja została stworzona dla FreeCAD v0.16. Zostały wprowadzone znaczące zmiany w tworzeniu ścieżek. Proszę zapoznać się z dokumentacją środowiska pracy [Path](Path_Workbench/pl.md) ogólnie lub z poradnikiem na przykład [przejście po ścieżce](Path_Walkthrough_for_the_Impatient/pl.md)!}}

FreeCAD oferuje również bardziej zaawansowane sposoby bezpośredniego generowania G-kodu. Jest to często o wiele bardziej skomplikowane niż używanie automatycznych narzędzi, jak widzieliśmy powyżej, ale ma tę zaletę, że pozwala na pełną kontrolę wyjścia. Zazwyczaj nie jest to potrzebne przy korzystaniu z drukarek 3D, ale staje się bardzo ważne, gdy mamy do czynienia z frezowaniem CNC, jako że maszyny te są znacznie bardziej skomplikowane.

Generowanie ścieżek G-kodu w programie FreeCAD odbywa się za pomocą [Path](Path_Workbench/pl.md). Zawiera on narzędzia, które generują pełne ścieżki maszynowe oraz inne, które generują tylko części projektu G-kodu, które mogą być następnie złożone w całość operacji frezowania.

Generowanie ścieżek frezowania CNC to kolejny temat, który jest zbyt obszerny, aby zmieścić się w tym podręczniku, więc pokażemy jak zbudować prosty projekt Path, nie przejmując się zbytnio większością szczegółów prawdziwej obróbki CNC.

-   Wczytaj plik zawierający nasz element lego i przełącz się na środowisko pracy [Path](Path_Workbench/pl.md).
-   Ponieważ końcowy element nie zawiera już prostokątnej górnej powierzchni, ukryj końcowy klocek lego i pokaż pierwszą sześcienną bryłę, którą zrobiliśmy, a która ma prostokątną górną powierzchnię.
-   Zaznacz górną ścianę i naciśnij przycisk <img alt="" src=images/Path_Profile.svg  style="width:24px;"> [Kontur](Path_Profile/pl.md).
-   Ustaw jego właściwość **Przesunięcie** na {{Value|1mm}}.

![](images/Exercise_path_01.jpg )

-   Następnie powielmy tę pierwszą pętlę kilka razy, aby narzędzie wyrzeźbiło cały blok. Zaznacz ścieżkę Profil i naciśnij przycisk <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Szyk](Path_Array/pl.md).
-   Ustaw właściwość **Kopie** szyku na {{Value|8}}, a jej **Przesunięcie** na {{Value|-2mm}} w kierunku Z, i przesuń położenie tablicy o 2mm w kierunku Z, tak aby cięcie zaczęło się nieco powyżej wyciągnięcia, i uwzględniło również wysokość kropek.

![](images/Exercise_path_02.jpg )

-   Teraz zdefiniowaliśmy ścieżkę, którą frezarka będzie podążać, aby wyciąć prostokątną objętość z bloku materiału. Teraz musimy wyciąć przestrzeń pomiędzy kropkami, aby je odsłonić. Ukryj wyciągnięcie i pokaż ponownie końcowy element, abyśmy mogli wybrać ścianę, która znajduje się pomiędzy kropkami.
-   Wybierz górną część ściany i naciśnij przycisk <img alt="" src=images/Path_Pocket_Shape.svg  style="width:24px;"> [Kształt kieszeni](Path_Pocket_Shape/pl.md). Ustaw właściwość **Przesunięcie** na {{Value|1mm}}, a **wysokość wciągania** na {{Value|20mm}}. Jest to wysokość, do której nóż będzie się przemieszczał podczas przechodzenia z jednej pętli do drugiej. W przeciwnym razie narzędzie tnące mogłoby przeciąć jedną z naszych kropek:

![](images/Exercise_path_03.jpg )

-   Po raz kolejny utwórz szyk. Zaznacz obiekt Kieszeń i naciśnij przycisk <img alt="" src=images/Path_Array.svg  style="width:24px;"> [Szyk](Path_Array/pl.md). Ustaw ilość **Kopii** na {{Value|1}}, a **Przesunięcie** na {{Value|-2mm}} w kierunku Z. Przesuń umieszczenie tablicy o {{Value|2mm}} w kierunku Z. Nasze dwie operacje zostały wykonane:

![](images/Exercise_path_04.jpg )

-   Teraz pozostaje tylko połączyć te dwie operacje w jedną. Można to zrobić za pomocą [zadania](Path_Job/pl.md). Naciśnij przycisk <img alt="" src=images/Path_Job.svg  style="width:24px;"> [Zadanie](Path_Job/pl.md).
-   Ustaw właściwość **Użyj umieszczenia** projektu na wartość {{True/pl}}, ponieważ zmieniliśmy rozmieszczenie szyku i chcemy, aby zostało to uwzględnione w projekcie.
-   W [widoku drzewa](Tree_view/pl.md) przeciągnij i upuść dwa szyki do projektu. W razie potrzeby można zmienić kolejność szyków wewnątrz projektu, klikając ich pozycje dwukrotnie.
-   Projekt można teraz wyeksportować do G-code, zaznaczając go, wybierając menu **Plik -\> Eksport**, wybierając format G-code i w oknie dialogowym, które się otworzy, wybierając skrypt post-processingowy odpowiedni dla twojego urządzenia.

Istnieje wiele aplikacji do symulacji realnej obróbki skrawaniem, jedną z nich, która jest również wieloplatformowa i otwartoźródłowa, podobnie jak FreeCAD, aplikacja [Camotics](http://camotics.org/).

**Do pobrania**

-   Plik STL wygenerowany w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   Plik projektu wygenerowany w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Plik G-code wygenerowany w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Więcej informacji**

-   Środowisko pracy [Siatka](Mesh_Workbench/pl.md)
-   [format plików STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   Środowisko pracy [Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Środowisko pracy [Path](Path_Workbench/pl.md)
-   [Camotics](http://camotics.org/)

### Filmy

-   [How To Use FreeCAD For 3D Printing - Używanie gałęzi Realthunder](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Lista odtwarzania wideo przygotowana przez Maker Tales o tym jak używać programu FreeCAD do druku 3D.




[Category:Path{{\#translation:}}](Category:Path.md) [Category:Mesh{{\#translation:}}](Category:Mesh.md) [Category:Tutorials{{\#translation:}}](Category:Tutorials.md)
