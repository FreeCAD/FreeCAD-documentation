# Manual:Using spreadsheets/pl
{{Manual:TOC}}

Środowisko pracy [Arkusz kalkulacyjny](Spreadsheet_Workbench.md) we FreeCAD umożliwia użytkownikom tworzenie i zarządzanie [arkuszami kalkulacyjnymi](https://en.wikipedia.org/wiki/Spreadsheet), takimi jak te tworzone w [Excelu](https://en.wikipedia.org/wiki/Microsoft_Excel) lub [Calc z LibreOffice](https://en.wikipedia.org/wiki/LibreOffice_Calc) bezpośrednio w ich projektach. Pozwala na wprowadzanie, organizowanie i manipulowanie danymi w formacie tabelarycznym, który można następnie połączyć z różnymi parametrami i modelami w projekcie.

Jedną z kluczowych zalet jest zastosowanie w modelowaniu parametrycznym. Arkusze kalkulacyjne można powiązać z wymiarami i właściwościami modeli 3D, co czyni je niezbędnym narzędziem do dynamicznych zmian w projekcie. Na przykład zmiana wartości w arkuszu kalkulacyjnym automatycznie aktualizuje odpowiadający jej wymiar w modelu.

Oprócz zarządzania wartościami środowisko pracy doskonale sprawdza się w zarządzaniu danymi, przechowując kluczowe informacje, takie jak właściwości materiałów, wymiary czy parametry globalne projektu. Jest to szczególnie przydatne w złożonych projektach, gdzie konieczne jest odwoływanie się do wielu wartości lub ich dostosowywanie.

Arkusze kalkulacyjne umożliwiają także wprowadzanie formuł do obliczeń i zarządzania danymi. Formuły te mogą odnosić się do innych komórek arkusza lub parametrów modelu 3D, co sprawia, że cały proces projektowania jest elastyczny i reaguje na zmiany.

Może być bezproblemowo zintegrowane z innymi środowiskami pracy FreeCAD, umożliwiając interakcję między danymi a komponentami modelu. Ta integracja centralizuje kontrolę nad różnymi aspektami projektu, ułatwiając zarządzanie. Interfejs jest prosty, przypominający tradycyjne oprogramowanie arkuszy kalkulacyjnych, co sprawia, że jest znajomy i łatwy w użyciu dla osób przyzwyczajonych do programów takich jak Excel czy LibreOffice Calc.

W praktyce środowisko pracy Arkusz Kalkulacyjny jest wszechstronne i sprawdza się w różnych zastosowaniach, takich jak definiowanie parametrów globalnych projektu, zarządzanie zestawieniami materiałów (BOM) oraz wykonywanie niestandardowych obliczeń wpływających na decyzje projektowe. Upraszcza złożone projekty poprzez centralizację kontroli parametrów w jednym miejscu.

W poniższym przykładzie utworzymy kilka obiektów, pobierzemy niektóre z ich właściwości do arkusza kalkulacyjnego, a następnie użyjemy arkusza kalkulacyjnego do bezpośredniego sterowania właściwościami innych obiektów.



### Odczyt właściwości 

-   Zacznij od przełączenia się do <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [środowiska pracy Część](Part_Workbench/pl.md) i utworzenia kilku obiektów: <img alt="" src=images/Part_Box.svg  style="width:16px;"> [prostopadłościanu](Part_Box/pl.md), <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [walca](Part_Cylinder/pl.md) i <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [kuli](Part_Sphere/pl.md).
-   Edytuj ich właściwość **Umiejscowienie** (lub użyj narzędzia <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Przesuń](Draft_Move/pl.md)), aby rozmieścić je nieco dalej od siebie, co pozwoli lepiej zobaczyć efekty naszych działań:

![](images/Exercise_spreadsheet_01.jpg )

-   Teraz wyciągnijmy pewne informacje o tych obiektach. Przełącz się do <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [środowiska pracy Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md).
-   Naciśnij przycisk <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> **Nowy arkusz kalkulacyjny**.
-   Kliknij dwukrotnie nowy obiekt Arkusza Kalkulacyjnego w widoku drzewa. Otworzy się edytor arkusza kalkulacyjnego:

![](images/FreeCAD_Spreedsheet.png )

Choć edytor arkuszy kalkulacyjnych w FreeCAD nie jest tak rozbudowany jak dedykowane aplikacje, takie jak Excel czy LibreOffice Calc, oferuje niezbędne narzędzia do większości zadań projektowych. Użytkownicy mogą dostosowywać właściwości komórek, takie jak rozmiar, kolor i wyrównanie, a także scalać lub dzielić komórki w celu lepszej organizacji. Obsługiwane są podstawowe formuły oraz odniesienia do innych komórek, co umożliwia prostą manipulację danymi. To, co go wyróżnia, to głęboka integracja ze środowiskiem modelowania FreeCAD, gdzie zmiany w arkuszu kalkulacyjnym mogą automatycznie aktualizować wymiary modelu w czasie rzeczywistym. Chociaż brakuje mu zaawansowanych funkcji, takich jak tabele przestawne czy wykresy, jego ukierunkowanie na projektowanie sterowane parametrami czyni go potężnym narzędziem do zarządzania danymi projektowymi bezpośrednio w FreeCAD.

W FreeCAD, poza standardowymi funkcjami arkusza kalkulacyjnego, istnieje szczególnie użyteczna funkcja: możliwość odwoływania się nie tylko do innych komórek, ale także do obiektów w dokumencie i pobierania wartości z ich właściwości. Na przykład możesz uzyskać właściwości obiektów 3D widoczne na karcie **Dane** w **Edytorze właściwości** po wybraniu obiektu. To umożliwia bezproblemową integrację między arkuszem kalkulacyjnym a modelem 3D, ułatwiając powiązanie i automatyzację zmian w oparciu o parametry obiektów w projekcie. Dzięki temu praca staje się bardziej dynamiczna i zintegrowana, co sprzyja efektywnemu projektowaniu.

-   Zacznijmy od wpisania kilku tekstów w komórkach A1, A2 i A3, aby później łatwiej było zapamiętać, co reprezentują. Na przykład: **Długość sześcianu**, **Promień walca** i **Promień kuli**. Aby wpisać tekst, wystarczy skorzystać z pola \"Zawartość\" nad arkuszem kalkulacyjnym lub kliknąć dwukrotnie w wybraną komórkę.
-   Teraz pobierzmy rzeczywistą długość naszego sześcianu. W komórce B1 wpisz **=Cube.Length**. Zauważysz, że arkusz kalkulacyjny posiada mechanizm autouzupełniania, który jest taki sam jak edytor wyrażeń używany w poprzednim rozdziale.
-   Zrób to samo dla komórki B2 (**=Cylinder.Radius**) oraz B3 (**=Sphere.Radius**).

![](images/FreeCAD_Spreedsheet_Autocomplete.png )

-   Chociaż wyniki są wyrażone wraz z jednostkami, wartości te można manipulować jak dowolnymi liczbami. Spróbuj na przykład wpisać w komórce C1: **=B1\*2**.
-   Teraz możemy zmienić jedną z tych wartości w edytorze właściwości, a zmiana natychmiast zostanie odzwierciedlona w arkuszu kalkulacyjnym. Na przykład zmień długość naszego sześcianu na **20 mm**:

![](images/FreeCAD_Spreedsheet_Multipl.png )

Strona <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [środowiska pracy Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md) opisuje bardziej szczegółowo wszystkie możliwe operacje i funkcje dostępne w arkuszach kalkulacyjnych.



### Zapis właściwości 

Kolejną potężną funkcją środowiska pracy Arkusz Kalkulacyjny w FreeCAD jest możliwość nie tylko odczytywania wartości z właściwości obiektów 3D, ale także przypisywania im wartości. Umożliwia to bezpośrednie sterowanie wymiarami i atrybutami obiektów z poziomu arkusza kalkulacyjnego. Jednak jedną z fundamentalnych zasad FreeCAD jest zakaz tworzenia zależności cyklicznych -- oznacza to, że arkusz kalkulacyjny nie może zarówno odczytywać, jak i zapisywać do tego samego obiektu. Zrobienie tego spowodowałoby sytuację, w której obiekt zależy od arkusza kalkulacyjnego, podczas gdy arkusz zależy od obiektu, co prowadzi do nieprawidłowej konfiguracji. Aby tego uniknąć, zwykle tworzy się drugi arkusz kalkulacyjny do obsługi zapisywania wartości, zapewniając wyraźne oddzielenie procesów odczytu i zapisu.

-   Teraz możemy zamknąć kartę arkusza kalkulacyjnego (pod widokiem 3D). Nie jest to obowiązkowe, nie ma problemu z utrzymywaniem kilku okien arkuszy kalkulacyjnych otwartych jednocześnie.
-   Naciśnij ponownie przycisk <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> **Nowy arkusz kalkulacyjny**.
-   Zmień nazwę nowego arkusza kalkulacyjnego na bardziej znaczącą, na przykład **Wejście** (zrób to, klikając prawym przyciskiem myszy na nowy obiekt arkusza i wybierając **Zmień nazwę**).
-   Kliknij dwukrotnie arkusz Wejście, aby otworzyć edytor arkusza kalkulacyjnego.
-   W komórce A1 wpisz tekst opisowy, na przykład: \"Wymiary sześcianu\".
-   W komórce B1 wpisz **=5mm** (użycie znaku = sprawia, że wartość jest interpretowana jako wartość jednostkowa, a nie tekst).
-   Teraz, aby móc używać tej wartości poza arkuszem kalkulacyjnym, musimy nadać nazwę lub alias komórce B1. Kliknij prawym przyciskiem myszy na komórkę, wybierz **Właściwości** i przejdź do zakładki **Alias**. Nadaj jej nazwę, na przykład **cubedims**:

![](images/FreeCAD_Spreedsheet_Alias.png )

-   Naciśnij **OK**, a następnie zamknij kartę arkusza kalkulacyjnego.
-   Wybierz obiekt sześcianu.
-   W edytorze właściwości kliknij małą ikonkę <img alt="" src=images/Bound-expression-unset.svg  style="width:16px;"> **wyrażenie** po prawej stronie pola **Długość**. Otworzy to [edytor wyrażeń](Expressions/pl.md), gdzie możesz wpisać **Spreadsheet001.cubedims**. Powtórz to dla pól **Wysokość** i **Szerokość**:

![](images/FreeCAD_SpreedSheet_Dim.png )

Powodem, dla którego używamy \"Spreadsheet001\" zamiast \"Wejście\" w wyrażeniu, jest to, że każdy obiekt w dokumencie FreeCAD ma unikalną nazwę wewnętrzną i bardziej przyjazną nazwę wyświetlaną. Nazwa wyświetlana to ta, która pojawia się w widoku drzewa, podczas gdy nazwa wewnętrzna służy do unikalnej identyfikacji obiektów w dokumencie. FreeCAD pozwala przypisać tę samą nazwę wyświetlaną do wielu obiektów, jeśli dostosujesz ustawienia, ale nazwa wewnętrzna pozostaje unikalna. Do każdej operacji wymagającej jednoznacznej identyfikacji obiektu FreeCAD używa nazwy wewnętrznej, a nie nazwy wyświetlanej, ponieważ ta ostatnia może odnosić się do więcej niż jednego obiektu. Aby znaleźć nazwę wewnętrzną obiektu, warto mieć otwarty panel Wybór (dostępny poprzez Widok → Panele). Panel ten zawsze wyświetla nazwę wewnętrzną wybranego obiektu, co zapewnia, że używasz właściwego odniesienia w swoich wyrażeniach.

![](images/FreeCAD_SpreedSheet_SelectionView.png )

Dzięki używaniu aliasów komórek w środowisku pracy Arkusz Kalkulacyjny FreeCAD, możliwe jest przechowywanie \"wartości głównych\" w dokumencie, co ułatwia zarządzanie i modyfikowanie kluczowych parametrów. Na przykład arkusz kalkulacyjny może przechowywać wymiary modelu, umożliwiając odwoływanie się do tych wartości w całym projekcie. Takie podejście upraszcza proces aktualizacji modelu; jeśli wymagane są nowe wymiary, wystarczy otworzyć arkusz, dostosować wartości, a model automatycznie zaktualizuje się, aby odzwierciedlić te zmiany. Ta metoda upraszcza wersjonowanie i poprawia efektywność, szczególnie w modelowaniu parametrycznym, gdzie wymiary często się zmieniają w zależności od wymagań projektu.

Na koniec, warto zauważyć, że ograniczenia w szkicu mogą również przyjmować wartość komórki arkusza kalkulacyjnego:

Można również nadawać aliasy wiązaniom wymiarowym (poziomym, pionowym lub odległości) w szkicu *(można następnie użyć tej wartości również spoza szkicu)*:

![](images/FreeCAD_SpreedSheet_Rectangle.png )

**Do pobrania**

-   Plik utworzony w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/spreadsheet.FCStd>

**Więcej informacji:**

-   [Arkusz kalkulacyjny](Spreadsheet_Workbench/pl.md)
-   [Silnik wyrażeń](Expressions/pl.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Using spreadsheets/pl
