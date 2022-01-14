# Release notes 0.11/pl
To jest podsumowanie najważniejszych zmian i nowych funkcji dostępnych w wydaniu 0.11 FreeCAD. Pełną listę można znaleźć na stronie [dziennika zmian](http://www.freecadweb.org/tracker/changelog_page.php).

<img alt="" src=images/FreeCAD011.png  style="width:800px;">

Widok ekranu z wersji 0.11.

### Informacje ogólne 

-   [Projekt tłumaczenia FreeCAD](http://crowdin.net/project/freecad) otrzymał ogromną pomoc od wielu ludzi z całego świata i FreeCAD jest teraz dostępny w nie mniej niż 15 językach: Angielski, niemiecki, francuski, włoski, szwedzki, hiszpański, portugalski, rosyjski, ukraiński, norweski, afrikaans, fiński, chiński uproszczony, chorwacki i holenderski. A wiele więcej języków jest w trakcie opracowywania dla następnych wydań.

![](images/release011-translation.jpg )

-   Kilka ulepszeń zostało wprowadzonych dla całego FreeCAD, na przykład drzewo hierarchii pozwala teraz na złożone stosy obiektów, utrzymując całą historię geometrii w czystości, łatwo dostępną i modyfikowalną. Nowe ulepszenia Python API pozwalają również na lepszą interakcję obiektów z drzewem, definiując ich własne zachowanie, ikony, itp.

![](images/release011-dependency.jpg )

-   Mechanizm kopiuj / wklej został również znacznie ulepszony, umożliwiając teraz łatwe kopiowanie / wklejanie obiektów pomiędzy dokumentami.
-   W środowisku pracy [Część](Part_Workbench/pl.md) pojawiły się nowe narzędzia, takie jak odbicie lustrzane oraz zaokrąglenia i sfazowania krawędzi.

### Szkicownik i Projekt Części 

-   Środowisko pracy do rozwiązywania wiązań [Szkicownik](Sketcher_Workbench/pl.md) został całkowicie przerobiony i nawet jeśli Szkicownik nie jest jeszcze kompletny, posiada już dobry zestaw narzędzi, takich jak linie, prostokąty i wiązania, takie jak zbieżność punktów, równoległość, stała długość lub ograniczenia poziome i pionowe.

-   Oprócz Szkicownika, nowy stół roboczy Projekt Części pozwala na szybkie budowanie brył na wierzchu szkiców. Zasadą w FreeCAD jest, że wszystko jest parametryczne, możesz wrócić w każdej chwili i zmienić swój szkic, a cała geometria, która od niego zależy zostanie automatycznie dostosowana.

![](images/release011-sketcher.jpg )

![](images/Movie.png ) Przykład: [demo Szkicownik](http://www.youtube.com/watch?v=hvXupH5bA0E) • [demo Projekt Części](http://www.youtube.com/watch?v=7ih9Jp3OAwA)

### Robot simulation 

-   Środowisko pracy [Robot](Robot_Workbench/pl.md) zostało rozszerzone o wiele narzędzi GUI i jest obecnie dość funkcjonalne i pozwala na łatwe symulowanie ruchów robotów przemysłowych.

![](images/release011-robot.jpg )

### Kreślenie 2D 

-   Przyciąganie zostało znacznie zoptymalizowane i teraz działa całkiem szybko, nawet na złożonych obiektach.
-   Narzędzie \"Przytnij/wydłuż\" można teraz nazwać \" Przytnij/Wydłuż/Wyciągnij\", ponieważ pozwala ono na szybkie wyciągnięcie pojedynczych powierzchni, oferując wygodny skrót do standardowego narzędzia Wyciągnięcie środowiska Część.
-   Udoskonalono również przepływ pracy z arkuszem Draft-to-Drawing, wszystkie obiekty środowiska pracy Rysunek Roboczy można teraz umieścić na stronie rysunku i wszystkie oferują ten sam poziom komfortu, co standardowe obiekty środowiska Część, oferując możliwość zmiany ich pozycji, obracanie i skalowanie w locie. Oferują również dodatkowe funkcje, takie jak wypełnienia wzorem kreskowania

![](images/release011-draft-drawing.jpg )

-   Środowisko pracy Rysunek Roboczy oferuje również nowe narzędzia, takie jak wielokąty foremne i linie złożone
-   Dostępne jest również nowe narzędzie Edycja, pozwalające na edycję geometrii większości obiektów środowiska Rysunek Roboczy.

![](images/release011-draft.jpg )

-   Wymiary mogą teraz mieć edytowany i przesuwany tekst, a linie mogą mieć strzałkę końcową, co pozwala na używanie ich jako linii odniesienia.
-   Kilka poleceń, takich jak przesuń, obróć lub wymiarowanie, pozwala teraz na wykonanie kilku kopii bez opuszczania narzędzia.
-   Środowisko pracy Rysunek Roboczy zyskało również [API](Draft_API/pl.md) środowiska [Python](Python/pl.md).
-   Importer DXF obsługuje teraz atrybuty bloków

![](images/Movie.png ) Przykład: [Demo środowiska Rysunek Roboczy](http://www.youtube.com/watch?v=Q7cG-LQK8Ps)

### Obrazy

-   Środowisko pracy [Obraz](Image_Workbench/pl.md) posiada teraz obiekt ImagePlane, pozwalający na wyświetlenie pliku obrazu wewnątrz sceny 3D, który może być użyty na przykład do konstrukcji geometrii na podstawie zeskanowanych planów.


{{Top}}

### Documentacja

-   Podręcznik [FreeCAD](Online_Help_Toc/pl.md) posiada teraz kilka zaawansowanych tłumaczeń. Sprawdź stronę główną!


{{languages/pl | {{en|Release_notes_0.11}} {{de|Release_notes_0.11/de}} {{es|Release_notes_0.11/es}} {{fr|Release_notes_0.11/fr}} {{it|Release_notes_0.11/it}} {{ru|Release_notes_0.11/ru}} }}

[<img src="images/Property.png" style="width:16px"> News](Category_News.md) [<img src="images/Property.png" style="width:16px"> Documentation](Category_Documentation.md) [<img src="images/Property.png" style="width:16px"> Releases](Category_Releases.md)

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.11/pl
