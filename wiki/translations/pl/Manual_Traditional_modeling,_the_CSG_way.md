# Manual:Traditional modeling, the CSG way/pl
{{Manual:TOC}}

[CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) oznacza Constructive Solid Geometry i opisuje podstawowy sposób pracy z geometrią brył 3D. Polega on na tworzeniu złożonych obiektów poprzez dodawanie lub usuwanie elementów do / z brył przy użyciu operacji logicznych, takich jak łączenie, odejmowanie lub przecinanie.

Jak omówiono wcześniej w tym podręczniku, FreeCAD wspiera wiele typów geometrii. Jednak najbardziej preferowanym i przydatnym typem do projektowania rzeczywistych obiektów 3D we FreeCAD jest geometria bryłowa [BREP](https://en.wikipedia.org/wiki/Boundary_representation), obsługiwana głównie przez środowisko pracy [Część](Part_Workbench.md). Reprezentacja brzegowa BREP to metoda przedstawiania kształtów przy pomocy ich przestrzennych brzegów. Definiuje obiekt 3D określając jego powierzchnie, krawędzie i wierzchołki. Kluczowe aspekty BREP to ściany, które są powierzchniowymi elementami obiektów, krawędzie - linie brzegowe, w których spotykają się dwie ściany i wierzchołki - punkty, w któych spotykają się krawędzie.

BREP ma kilka zalet. Po pierwsze, definiuje powierzchnie przy pomocy równań matematycznych, pozwalając na precyzyjne modelowanie. Ta precyzja jest kluczowa do zastosowań inżynierskich, w których wymagane są dokładne wymiary. Ponadto, BREP zapewnia gładkie i szczegółowe powierzchnie, w przeciwieństwie do [siatek wielokątów](https://en.wikipedia.org/wiki/Polygon_mesh), które przybliżają zakrzywione powierzchnie za pomocą ścianek. Jest to zbliżone do różnicy między obrazami wektorowymi, które skalują się bez utraty jakości i bitmapami, które mogą wyglądać na rozpikselowane przy powiększaniu. BREP zawiera obszerne informacje topologiczne o obiekcie, wliczając zależności między ścianami, krawędziami i wierzchołkami, co jest kluczowe dla zaawansowanych operacji, jak przeliczenia logiczne i zaokrąglanie.

Siatki wielokątów składają się z wierzchołków, krawędzi i ścian, które tworzą trójkąty lub czworokąty. Są prostsze i szybsze w renderowaniu, ale brakuje im precyzji. Przy powiększeniu lub druku w większej skali siatki pokazują powierzchnie zbudowane ze ścianek a nie gładkich krzywych. BREP zaś korzysta z krzywych i powierzchni definiowanych matematycznie, oferując wyższą dokładność i gładkość. Modele BREP są preferowane do zastosowań CAD, gdzie precyzja jest bezwzględnie wymagana.

We FreeCAD geometria oparta na BREP jest zarządzana przez [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), otwartoźródłową bibliotekę programistyczną. Głównym interfejsem między FreeCAD a jądrem OpenCasCade jest środowisko pracy Część, które stanowi podstawę dla większości innych środowisk pracy, dostarczając niezbędne narzędzia do tworzenia i manipulowania obiektami BREP. Środowisko pracy Część obejmuje narzędzia do tworzenia prymitywów, takich jak podstawowe kształty, np. prostopadłościany, cylindry i sfery, wykonywania operacji logicznych, takich jak łączenie, przecinanie i odejmowanie kształtów, oraz przeprowadzania transformacji, w tym przesuwania, obracania, skalowania i klonowania obiektów.

Podczas gdy inne środowiska pracy w FreeCAD, takie jak środowiska pracy Projekt Części i Powierzchnia, oferują bardziej zaawansowane narzędzia do budowania i manipulowania geometrią, opierają się na podstawowym środowisku pracy Część. Zrozumienie, jak obiekty środowiska pracy Część działają wewnętrznie, oraz biegłość w obsłudze podstawowych narzędzi środowiska pracy Część są korzystne. Często te prostsze narzędzia mogą rozwiązać problemy, z którymi bardziej złożone narzędzia mogą sobie nie poradzić.

![](images/Mesh_vs_brep.jpg )

Różnicę między nimi można porównać do różnicy między obrazami bitmapowymi i wektorowymi. Podobnie jak w przypadku obrazów bitmapowych, siatki wielokątów mają zakrzywione powierzchnie podzielone na serię punktów. Jeśli przyjrzysz się im bliżej lub wydrukujesz je w bardzo dużym rozmiarze, zobaczysz nie zakrzywioną powierzchnię, ale powierzchnię podzieloną na ścianki. Zarówno w przypadku obrazów wektorowych, jak i danych BREP, położenie dowolnego punktu na krzywej nie jest przechowywane w geometrii, ale obliczane na bieżąco, z dokładną precyzją.

Aby zilustrować działanie środowiska Część, zamodelujemy ten stół, używając tylko operacji CSG *(z wyjątkiem śrub, dla których użyjemy jednego z dodatków, oraz wymiarów, które zobaczymy w następnym rozdziale)*:

![](images/Exercise_table_complete.jpg )

Utwórzmy nowy dokument *(**Ctrl+N** lub menu **Plik → Nowy**)*, aby przechowywać nasz projekt tabeli. Dokument jest początkowo nazywany \"nienazwanym\" w zakładce Model w panelu Widoku złożonego, ale jeśli zapiszesz dokument *(**Ctrl+Shift+S** lub menu **Plik → Zapisz jako**)* jako nowy dokument FreeCAD o nazwie \"table.FCStd\", nazwa dokumentu zostanie zmieniona na \"table\", co wyraźniej identyfikuje projekt. Będziemy pracować używając mm jako jednostki długości. Możesz to jednak dostosować do swoich preferencji przy pomocy menu w prawym dolnym rogu ekranu.

Teraz możemy przełączyć się do środowiska pracy Część i rozpocząć tworzenie naszej pierwszej nogi stołu.

-   Naciśnij przycisk <img alt="" src=images/Part_Box.svg  style="width:16px;"> **Sześcian**.
-   Wybierz sześcian, a następnie ustaw następujące właściwości *(w zakładce **Dane**)*:
    -   Długość: 80 mm
    -   Szerokość: 80 mm
    -   Wysokość: 750 mm
-   Zduplikuj sześcian, naciskając **Ctrl** + **C**, a następnie **Ctrl** + **V** *(lub menu **Edycja → Kopiuj i Wklej**)* *(żadna zmiana nie będzie widoczna, ponieważ drugi obiekt nakłada się na pierwszy)*.
-   Wybierz nowy obiekt o nazwie Cube001, który został utworzony *(kliknij na Cube001 w lewej zakładce Model)*.
-   Zmień jego położenie, edytując jego właściwość Placement:
    -   Pozycja x: 8 mm
    -   Pozycja y: 8 mm

Powinieneś otrzymać dwa wysokie sześciany, oddalone od siebie o 8mm:

![](images/Exercise_table_01.jpg )

-   Teraz możemy odjąć jeden od drugiego: Zaznaczamy **pierwszy**, czyli ten, który **zostanie**, następnie z wciśniętym klawiszem **CTRL** zaznaczamy **drugi**, który zostanie **odjęty** *(kolejność jest ważna)* i wciskamy przycisk <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Wytnij**:

![](images/Exercise_table_02.jpg )

Zauważ, że nowo utworzony obiekt o nazwie \"Cut\" nadal zawiera dwie kostki, których użyliśmy jako operandów. W rzeczywistości obie kostki nadal znajdują się w dokumencie, zostały jedynie ukryte i zgrupowane pod obiektem Cut w widoku drzewa. Nadal można je wybrać, rozwijając strzałkę obok obiektu Cut i, jeśli chcesz, ponownie je wyświetlić, klikając je prawym przyciskiem myszy lub zmieniając dowolną z ich właściwości.

Możesz użyć narzędzia Cut i innych narzędzi logicznych również poprzez \"Widok złożony\" z funkcji <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [logicznych](Part_Boolean/pl.md). Daje to bardziej przejrzysty, ale dłuższy sposób wykonania.

-   Teraz utwórzmy trzy pozostałe stopy, powielając nasz sześcian bazowy 6 razy. Ponieważ pozostaje on nadal skopiowany, można go po prostu wkleić *(**Ctrl** + **V**)* 6 razy. Zmień ich położenie w następujący sposób:
    -   Cube002: x: 0, y: 800mm
    -   Cube003: x: 8mm, y: 792mm
    -   Kostka004: x: 1200mm, y: 0
    -   Cube005: x: 1192mm, y: 8mm
    -   Cube006: x: 120mm, y: 800mm
    -   Cube007: x: 1192mm, y: 792mm

-   Teraz wykonajmy trzy pozostałe cięcia, wybierając najpierw sześcian \"główny\", a następnie sześcian, który ma zostać odcięty. Mamy teraz cztery obiekty Cut:

![](images/Exercise_table_03.jpg )

Być może myślisz, że zamiast powielać sześciokąt podstawy sześć razy, moglibyśmy powielić całą stopę trzy razy. To całkowita prawda, jak zawsze w FreeCAD, istnieje wiele sposobów na osiągnięcie tego samego rezultatu. Jest to cenna rzecz do zapamiętania, ponieważ w miarę jak będziemy przechodzić do bardziej złożonych obiektów, niektóre operacje mogą nie dać prawidłowego wyniku i często musimy wypróbować inne sposoby.

-   Teraz wykonamy otwory na śruby, używając tej samej metody cięcia. Ponieważ potrzebujemy 8 otworów, po dwa w każdej stopie, moglibyśmy wykonać 8 obiektów do odjęcia. Zamiast tego zbadajmy inne sposoby i stwórzmy 4 rurki, które zostaną ponownie wykorzystane przez dwie stopy. Utwórzmy więc cztery rurki za pomocą narzędzia <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Walec**. Możesz ponownie utworzyć tylko jeden i powielić go później. Nadaj wszystkim cylindrom promień 6 mm. Tym razem będziemy musieli je obrócić, co również odbywa się za pomocą właściwości **Umieszczenie** w zakładce Dane *(*Uwaga:*\' zmień właściwość Oś*przed*ustawieniem Kąta, w przeciwnym razie obrót nie zostanie zastosowany)*:
    -   Cylinder: wysokość: 1300 mm, kąt: 90°, oś: x:0,y:1,z:0, pozycja: x:-10 mm, y:40 mm, z:720 mm
    -   Cylinder001: wysokość: 1300 mm, kąt: 90°, oś: x:0,y:1,z:0, pozycja: x:-10 mm, y:840 mm, z:720 mm
    -   Cylinder002: wysokość: 900 mm, kąt: 90°, oś: x:-1,y:0,z:0, pozycja: x:40 mm, y:-10 mm, z:700 mm
    -   Cylinder003: wysokość: 900 mm, kąt: 90°, oś: x:-1,y:0,z:0, pozycja: x:1240 mm, y:-10 mm, z:700 mm

![](images/Exercise_table_04.jpg )

Zauważysz, że cylindry są nieco dłuższe niż to konieczne. Dzieje się tak dlatego, że podobnie jak we wszystkich aplikacjach 3D opartych na bryłach, operacje logiczne we FreeCAD są czasami nadwrażliwe na sytuacje powierzchnia-na-powierzchni i mogą zawieść. Robiąc to, stawiamy się po bezpiecznej stronie.

-   Teraz wykonajmy odejmowanie. Wybierz pierwszą stopę, a następnie, z wciśniętym klawiszem **CTRL**, wybierz jedną z rur, które ją przecinają i naciśnij przycisk **Wytnij**. Otwór zostanie wykonany, a rura ukryta. Znajdź ją w widoku drzewa, rozwijając przebitą stopę.
-   Wybierz inną stopę przebitą przez tę ukrytą rurkę, a następnie powtórz operację, tym razem **CTRL** + wybierając rurkę w widoku drzewa, ponieważ jest ona ukryta w widoku 3D *(możesz również uczynić ją ponownie widoczną i wybrać ją w widoku 3D)*. Powtórz tę czynność dla pozostałych stóp, aż każda z nich będzie miała dwa otwory:

![](images/Exercise_table_05.jpg )

Jak widać, każda stopa stała się dość długą serią operacji. Wszystko to pozostaje parametryczne i w każdej chwili można zmienić dowolny parametr dowolnej ze starszych operacji. We FreeCAD często nazywamy ten stos \"historią modelowania\", ponieważ w rzeczywistości zawiera on całą historię wykonanych operacji.

Inną szczególną cechą FreeCAD jest to, że pojęcie obiektu 3D i pojęcie operacji 3D mają tendencję do łączenia się w jedną rzecz. Cięcie jest jednocześnie operacją i obiektem 3D wynikającym z tej operacji. We FreeCAD nazywa się to \"cechą\", a nie obiektem lub operacją.

-   Teraz zróbmy blat, będzie to prosty blok drewna, zróbmy to z innym **Sześcianem**:
-   Prostopadłościan: długość: 1260 mm, szerokość: 860 mm, wysokość: 80 mm, pozycja: x: 10 mm, y: 10 mm, z: 670 mm.

W zakładce **Widok** możesz nadać mu ładny brązowawy, drewnopodobny kolor, zmieniając jego właściwość **Kolor kształtu**:

Teraz, gdy nasze pięć elementów jest kompletnych, nadszedł dobry czas, aby nadać im bardziej odpowiednie nazwy niż \"Cut015\". Klikając obiekty prawym przyciskiem myszy w widoku drzewa *(lub naciskając **F2**)*, możesz zmienić ich nazwę na coś bardziej znaczącego dla siebie lub innej osoby, która otworzy plik później. Często mówi się, że samo nadanie odpowiednich nazw obiektom jest znacznie ważniejsze niż sposób ich modelowania.

-   Umieścimy teraz kilka śrub. Obecnie istnieje niezwykle przydatny dodatek opracowany przez członka społeczności FreeCAD, który można znaleźć w repozytorium [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons), o nazwie [Elementy złączne](https://github.com/shaise/FreeCAD_FastenersWB), który bardzo ułatwia wstawianie śrub. Instalacja dodatkowych stołów roboczych jest łatwa i opisana na stronie [dodatków](Std_AddonMgr/pl.md).
-   Po zainstalowaniu środowiska [Elementy złączne](Fasteners_Workbench/pl.md) i ponownym uruchomieniu FreeCAD, pojawi się ono na liście środowisk pracy i możemy się do niego przełączyć. Dodanie śruby do jednego z naszych otworów odbywa się poprzez wybranie okrągłej krawędzi naszego otworu:

![](images/FastenerWorkbench.png )

-   Następnie możemy nacisnąć jeden z przycisków śrub w Fasteners Workbench, na przykład **EN 1665 Śruba sześciokątna z kołnierzami, seria wzmacniana**. Śruba zostanie umieszczona i wyrównana z naszym otworem, a średnica zostanie automatycznie dobrana do rozmiaru naszego otworu. Czasami śruba zostanie umieszczona odwrotnie, co możemy skorygować, odwracając jej właściwość \"\'odwróć\'\". Możemy również ustawić jej przesunięcie na 2 mm, aby postępować zgodnie z tą samą zasadą, której użyliśmy między blatem a nóżkami:

![](images/FastenerWorkbench_sel.png )

-   Powtórz tę czynność dla wszystkich otworów i nasz stół jest gotowy!

Jak wspomniano wcześniej, we FreeCAD można osiągnąć ten sam rezultat, wykonując różne kroki. Aby to zademonstrować, stwórzmy tę samą tabelę, korzystając z innej metodyki. Pamiętaj, że nie ma jednego właściwego lub niewłaściwego sposobu - liczy się indywidualna kreatywność.

Zaczniemy podobnie: tworząc sześcian o następujących wymiarach: długość 80 mm, szerokość 8 mm, wysokość 750 mm.

-   Utwórz sześcian, wybierając przycisk <img alt="" src=images/Part_Box.svg  style="width:16px;"> **Cube** i ustaw następujące właściwości (w zakładce **Data**):
    -   długość: 80 mm
    -   szerokość: 8 mm
    -   wysokość: 750 mm
-   Następnie utworzymy <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Cylinder** z następującymi właściwościami:
    -   promień: 6 mm, wysokość: 100 mm, kąt: 90°, oś: x: 1, y: 0, z: 0, pozycja: x: 40 mm, y: 40 mm, z: 720 mm
-   Następnie zastosujemy narzędzie do przycinania. Wybierz sześcian, a następnie, trzymając wciśnięty klawisz CTRL, wybierz cylinder. Pamiętaj, że kolejność wyboru jest istotna, aby określić, który element pozostaje. Następnie naciśnij przycisk <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Wytnij**.
-   Skopiujemy i wkleimy obiekt po przycięciu, naciskając **Ctrl+C**, a następnie **Ctrl+V** (lub menu **Edycja → Kopiuj** i **Wklej**):
    -   kąt: 90°, oś: x: 0, y: 0, z: 1, pozycja: x: 8 mm
-   Wybierz oba obiekty i zastosuj narzędzie <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> **Połączenie**. Teraz oba obiekty są połączone, tworząc jedną nogę.
-   Skopiuj i wklej połączoną nogę, ustawiając ją w pozycji:
    -   kąt: 90°, oś: x: 0, y: 0, z: 1, pozycja: y: 800 mm
-   Wybierz obie nogi i utwórz <img alt="" src=images/Part_Compound.svg  style="width:16px;"> **Kształt złożony**.
-   Skopiuj i wklej utworzony kształt złożony, ustawiając go w pozycji:
    -   kąt: 180°, oś: x: 0, y: 0, z: 1, pozycja: x: 1200 mm, y: 800 mm. W ten sposób uzyskaliśmy nogi stołu.

Teraz stworzymy blat stołu.

-   Utwórz sześcian o wymiarach:
    -   długość: 752 mm
    -   szerokość: 1184 mm
    -   wysokość: 784 mm
    -   pozycja: x: 8 mm, y: 8 mm, z: 670 mm

Postępujemy w podobny sposób, jeśli chcemy dodać śruby (a miejmy nadzieję, że chcemy!).

![](images/Tabble_alternative_complete.png )

**Wewnętrzna struktura obiektów Część**

Jak widzieliśmy powyżej, w FreeCAD możliwe jest zaznaczanie nie tylko całych obiektów, ale także ich części, takich jak okrągła krawędź naszego otworu na śrubę. To dobry moment, aby przyjrzeć się, jak wewnętrznie zbudowane są obiekty środowiska pracy Część. Każde środowisko pracy, które tworzy geometrię środowiska pracy Część, będzie się na nich opierać:

-   **Wierzchołki**: To punkty (zwykle końcowe), na których opiera się reszta konstrukcji. Na przykład linia ma dwa wierzchołki.
-   **Krawędzie**: Krawędzie to geometria liniowa, taka jak linie, łuki, elipsy lub [NURBS](https://pl.wikipedia.org/wiki/NURBS). Zwykle mają dwa wierzchołki, ale w niektórych szczególnych przypadkach mogą mieć tylko jeden (na przykład zamknięte koło).
-   **Linie**: Linia to sekwencja krawędzi połączonych swoimi końcami. Może zawierać krawędzie dowolnego typu i być zamknięta lub nie.
-   **Ściany**: Ściany mogą być płaskie lub zakrzywione i mogą być tworzone przez jeden zamknięty drut, który tworzy granicę ściany, lub więcej niż jeden, jeśli ściana ma otwory.
-   **Powłoki**: Powłoki to po prostu grupa ścian połączonych swoimi krawędziami. Mogą być otwarte lub zamknięte.
-   **Bryły**: Gdy powłoka jest szczelnie zamknięta, to znaczy, że nie ma żadnych \"wycieków\", staje się bryłą. Bryły mają pojęcie wnętrza i zewnętrza. Wiele środowisk pracy opiera się na tym, aby upewnić się, że obiekty, które tworzą, mogą być zbudowane w rzeczywistości.
-   **Kształty złożone**: Kształty złożone to po prostu agregaty innych kształtów, niezależnie od ich typu, połączone w jeden kształt.

W widoku 3D można wybrać poszczególne **wierzchołki**, **krawędzie** lub **ściany**. Wybranie jednego z nich powoduje również zaznaczenie całego obiektu.

**Uwaga na temat udostępnionego projektu**

Możesz spojrzeć na powyższy stół i pomyśleć, że jego konstrukcja nie jest dobra. Mocowanie nóżek do blatu jest prawdopodobnie zbyt słabe. Być może chciałbyś dodać elementy wzmacniające lub po prostu masz inne pomysły, aby go ulepszyć. W tym miejscu udostępnianie staje się interesujące. Możesz pobrać plik utworzony podczas tego ćwiczenia z linku poniżej i zmodyfikować go, aby był lepszy. Następnie, jeśli udostępnisz ten ulepszony plik, inni mogą być w stanie uczynić go jeszcze lepszym lub wykorzystać dobrze zaprojektowany stół w swoich projektach. Twój projekt może podsunąć inne pomysły innym ludziom, a ty być może przyczynisz się choć trochę do stworzenia lepszego świata\...

**Do pobrania**

-   Plik utworzony w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>

**Więcej informacji:**

-   [Środowisko pracy Część](Part_Workbench/pl.md)
-   [Repozytorium dodatków FreeCAD](https://github.com/FreeCAD/FreeCAD-addons)
-   [Środowisko pracy Elementy złączne](Fasteners_Workbench/pl.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/pl
