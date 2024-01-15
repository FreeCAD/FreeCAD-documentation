# Manual:Installing/pl
{{Manual:TOC}}

Program FreeCAD korzysta z licencji [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License); możesz pobierać, instalować, redystrybuować i używać FreeCAD w dowolny sposób, niezależnie od rodzaju pracy, jaką będziesz z nim wykonywać *(komercyjnej lub niekomercyjnej)*. Nie jesteś związany żadną klauzulą ani ograniczeniem, a pliki, które z nim tworzysz, są w pełni twoje. Jedyną rzeczą, której licencja zabrania, jest twierdzenie, że sam zaprogramowałeś FreeCAD!

FreeCAD zachowuje się tak samo w systemach Windows, Mac OS i Linux. Jednak sposób instalacji różni się nieznacznie w zależności od używanej platformy. W systemach Windows i Mac społeczność FreeCAD zapewnia wstępnie skompilowane pakiety *(instalatory)* gotowe do pobrania; podczas gdy w systemie Linux kod źródłowy jest udostępniany opiekunom dystrybucji Linuksa, którzy są następnie odpowiedzialni za pakowanie FreeCAD dla ich konkretnej dystrybucji. W rezultacie w systemie Linux FreeCAD można zazwyczaj zainstalować bezpośrednio z aplikacji menedżera oprogramowania.

Oficjalna strona pobierania FreeCAD dla systemów Windows i Mac OS znajduje się pod adresem <https://github.com/FreeCAD/FreeCAD/releases>.

**Wersje FreeCAD**

Oficjalne wydania FreeCAD, które można znaleźć na stronie wymienionej powyżej oraz w menedżerze oprogramowania dystrybucji, są wersjami stabilnymi. Jednak rozwój FreeCAD jest szybki! Nowe funkcje i poprawki błędów są dodawane niemal każdego dnia. Ponieważ między stabilnymi wydaniami często mija dużo czasu, możesz być zainteresowany wypróbowaniem bardziej zaawansowanej wersji FreeCAD. Te wersje rozwojowe lub wersje wstępne są od czasu do czasu przesyłane do [download page](https://github.com/FreeCAD/FreeCAD/releases) wspomnianej powyżej lub, jeśli używasz Ubuntu lub Fedory, społeczność FreeCAD utrzymuje również [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) i [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \"codzienne kompilacje\", które są regularnie aktualizowane o najnowsze zmiany.

Jeśli instalujesz FreeCAD na maszynie wirtualnej, pamiętaj, że wydajność może być niska *(w niektórych przypadkach bezużyteczna)* ze względu na ograniczenia obsługi [OpenGL](https://en.wikipedia.org/wiki/OpenGL) na większości maszyn wirtualnych.



## Instalacja w środowisku Windows 

1.  Pobierz pakiet instalacyjny *(.exe)* odpowiadający twojej wersji systemu Windows *(32bit lub 64bit)* ze strony [download page](https://github.com/FreeCAD/FreeCAD/releases). Instalatory FreeCAD powinny działać w każdej wersji systemu Windows, począwszy od Windows 7.
2.  Kliknij dwukrotnie pobrany instalator.
3.  Zaakceptuj warunki licencji LGPL, będzie to jeden z niewielu przypadków, w których możesz naprawdę, bezpiecznie kliknąć przycisk \"akceptuj\" bez czytania tekstu. Brak ukrytych klauzul: ![](images/Freecad-windows-install-01.jpg )
4.  Możesz pozostawić domyślną ścieżkę tutaj lub zmienić, jeśli chcesz: ![](images/Freecad-windows-install-02.jpg )
5.  Nie ma potrzeby ustawiania zmiennej PYTHONPATH, chyba że planujesz zaawansowane programowanie w Python, w którym to przypadku prawdopodobnie już wiesz, do czego służy: ![](images/Freecad-windows-install-03.jpg )
6.  Podczas instalacji zostanie zainstalowanych kilka dodatkowych komponentów, które są dołączone do instalatora: ![](images/Freecad-windows-install-04.jpg )
7.  To wszystko, FreeCAD jest zainstalowany. Znajdziesz go w menu start. ![](images/Freecad-windows-install-05.jpg )

**Instalacja wersji rozwojowej**

Pakowanie FreeCAD i tworzenie instalatora wymaga trochę czasu i poświęcenia, więc zazwyczaj wersje rozwojowe *(zwane również przedpremierowymi)* są dostarczane jako archiwa .zip *(lub .7z)*. Nie trzeba ich instalować; wystarczy je rozpakować i uruchomić FreeCAD, klikając dwukrotnie plik FreeCAD.exe, który znajdziesz w środku. Pozwala to również na przechowywanie zarówno stabilnych, jak i \"niestabilnych\" wersji na tym samym komputerze.



## Instalacja w środowisku Linux 

Na większości nowoczesnych dystrybucji Linuksa *(Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary itp.)*, FreeCAD można zainstalować jednym kliknięciem przycisku, bezpośrednio z aplikacji do zarządzania oprogramowaniem dostarczonej przez daną dystrybucję *(jej wygląd może różnić się od przedstawionego na poniższych obrazkach, każda dystrybucja korzysta z własnego narzędzia)*.

1.  Otwórz menedżera oprogramowania i wyszukaj \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Kliknij przycisk \"zainstaluj\" i to wszystko, FreeCAD zostanie zainstalowany. Nie zapomnij go później ocenić!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Alternatywne sposoby**

Jedną z największych radości korzystania z Linuksa jest mnogość możliwości dostosowania oprogramowania, więc nie ograniczaj się. Na Ubuntu i pochodnych, FreeCAD może być również zainstalowany z [PPA](https://launchpad.net/~freecad-maintainers) utrzymywanego przez społeczność FreeCAD *(zawiera zarówno wersje stabilne, jak i rozwojowe)*. Na Fedorze najnowsze wersje rozwojowe FreeCAD można zainstalować z [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), a ponieważ jest to oprogramowanie open source, można również łatwo [skompilować FreeCAD samodzielnie](Compiling/pl.md).



## Instalacja w środowisku Mac OS 

Instalacja FreeCAD na Mac OSX jest obecnie równie łatwa jak na innych platformach. Ponieważ jednak w społeczności jest mniej osób posiadających komputery Mac, dostępne pakiety czasami pozostają kilka wersji w tyle za innymi platformami.

1.  Pobierz spakowany pakiet odpowiadający Twojej wersji ze strony [pobierania](https://github.com/FreeCAD/FreeCAD/releases).
2.  Otwórz folder Pobrane i rozpakuj pobrany plik zip: ![](images/Freecad-mac-01.jpg )
3.  Przeciągnij aplikację FreeCAD z pliku zip do folderu Aplikacje: ![](images/Freecad-mac-02.jpg )
4.  To wszystko, FreeCAD jest zainstalowany! ![](images/Freecad-mac-03.jpg )

5\. Jeśli system uniemożliwia uruchomienie FreeCAD z powodu ograniczonych uprawnień dla aplikacji niepochodzących ze sklepu App Store, należy włączyć je w ustawieniach systemu: ![](images/Freecad-mac-04.jpg )



### Deinstalacja

Miejmy nadzieję, że nie będziesz chciał odinstalować FreeCAD, ale dobrze jest wiedzieć, jak to zrobić. W systemach Windows i Linux odinstalowanie FreeCAD jest bardzo proste. W systemie Windows użyj standardowej opcji \"usuń oprogramowanie\" znajdującej się w panelu sterowania; w systemie Linux usuń go za pomocą tego samego menedżera oprogramowania, którego użyłeś do instalacji. W systemie Mac OS wystarczy usunąć go z folderu Aplikacje



### Ustawianie podstawowych preferencji 

Po zainstalowaniu FreeCAD możesz go otworzyć i zmienić niektóre preferencje. Ustawienia preferencji w FreeCAD znajdują się w menu **Edycja → Preferencje ...**. Poniżej wymieniono kilka podstawowych ustawień, które możesz chcieć zmienić. Możesz przeglądać strony preferencji, aby sprawdzić, czy jest coś jeszcze, co chcesz zmienić.

1.  *Język*: (kategoria *Ogólne*, zakładka *Ogólne*) FreeCAD automatycznie wybierze język systemu operacyjnego, ale możesz chcieć to zmienić. FreeCAD jest prawie w pełni przetłumaczony na pięć lub sześć języków. Inne tłumaczenia są obecnie tylko częściowe. Możesz łatwo [pomóc w tłumaczeniu FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Moduł automatycznego ładowania**: (kategoria **Ogólne**, zakładka **Ogólne**) Normalnie FreeCAD uruchomi się, pokazując stronę startową. Można to pominąć i rozpocząć sesję FreeCAD bezpośrednio w wybranym środowisku pracy, wymienionym w sekcji *Uruchamianie*, *Automatyczne ładowanie modułu po uruchomieniu*. [Środowiska pracy](Workbenches/pl.md) zostaną szczegółowo wyjaśnione w [następnym rozdziale](Manual:The_FreeCAD_Interface/pl.md).
3.  **Utwórz nowy dokument przy uruchomieniu**: (kategoria *Ogólne*, zakładka *Dokument*) W połączeniu z powyższą opcją *Automatyczne ładowanie modułu*, jeśli jest zaznaczona, uruchamia FreeCAD gotowy do pracy. ![](images/Freecad-basic-options02.jpg )
4.  *Opcje przechowywania*: (kategoria *Ogólne*, zakładka *Dokument*) Podobnie jak w przypadku każdej złożonej aplikacji, FreeCAD prawdopodobnie zawiera błędy powodujące sporadyczne awarie. Tutaj można skonfigurować opcje, które pomogą odzyskać pracę w przypadku awarii.
5.  **Autorstwo i licencja**: (kategoria **Ogólne**, zakładka **Dokument**) Tutaj można ustawić wartości, które będą używane dla nowo tworzonych plików. Rozważ udostępnianie plików od samego początku, używając bardziej przyjaznej licencji [copyleft](https://en.wikipedia.org/wiki/Copyleft), takiej jak [Creative Commons](https://creativecommons.org/).
6.  **Przekieruj wewnętrzne komunikaty Pythona**: (kategoria *Ogólne*, zakładka *Okno wyjściowe*) Te dwie opcje są zawsze dobre do sprawdzenia, ponieważ spowodują, że komunikaty z wewnętrznego interpretera Python pojawią się w [Widoku raportu](Manual:The_FreeCAD_Interface/pl#Widok_raportu.md), gdy wystąpi problem z uruchomieniem skryptu Python. ![](images/Freecad-basic-options03.jpg )
7.  **Jednostki**: (kategoria *Ogólne*, zakładka *Jednostki*) Tutaj możesz ustawić domyślny system jednostek, którego chcesz używać. ![](images/Freecad-basic-options04.jpg )
8.  **Powiększ przy kursorze**: (kategoria **Wyświetlanie**, zakładka **3D**) Jeśli opcja ta jest ustawiona, operacje powiększania będą koncentrować się na kursorze myszki. Jeśli opcja nie jest ustawiona, środek bieżącego widoku jest punktem skupienia zoomu.
9.  **Odwróć powiększenie**: (kategoria *Wyświetlanie*, zakładka *3D*) Odwraca kierunek powiększania względem ruchu kursora myszki. ![](images/FreeCAD-v0-18-Preferences-Display.png )



### Instalacja dodatkowej zawartości 

Ponieważ projekt FreeCAD i jego społeczność szybko się rozwijają, a także dlatego, że jest on łatwy do rozszerzenia, zewnętrzne wkłady i projekty poboczne tworzone przez członków społeczności i innych entuzjastów zaczynają pojawiać się wszędzie w Internecie. Większość z tych zewnętrznych projektów to środowiska robocze lub makra, które można łatwo zainstalować bezpośrednio z poziomu FreeCAD poprzez [Menadżer dodatków](Std_AddonMgr/pl.md) znajdujący się w menu **Narzędzia**. Menedżer dodatków pozwoli ci zainstalować wiele interesujących komponentów, na przykład:

1.  Biblioteka [Części](https://github.com/FreeCAD/FreeCAD-library), która zawiera wszelkiego rodzaju przydatne modele lub fragmenty modeli stworzone przez użytkowników FreeCAD, które można swobodnie wykorzystywać w swoich projektach. Biblioteka może być używana i dostępna bezpośrednio z poziomu instalacji FreeCAD.
2.  [Dodatkowe środowiska pracy](https://github.com/FreeCAD/FreeCAD-addons), które rozszerzają funkcjonalność FreeCAD dla niektórych zadań, na przykład animacji części modeli lub obszarów, takich jak składanie blach lub BIM. Dalsze wyjaśnienia dotyczące każdego stołu warsztatowego i narzędzi, które zawiera, znajdują się na stronie każdego dodatku, którą można odwiedzić, klikając odpowiedni link w menedżerze dodatków.
3.  [Kolekcja makrodefinicji](https://github.com/FreeCAD/FreeCAD-macros), które są również dostępne [na Wiki dla FreeCAD](Macros_recipes/pl.md) wraz z dokumentacją dotyczącą ich użycia.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

Jeśli korzystasz z systemu operacyjnego Ubuntu, niektóre z powyższych dodatków są również dostępne jako pakiety w serwisie [dodatki FreeCAD PPA](https://launchpad.net/freecad-extras).

**Więcej informacji:**

-   [Więcej możliwości pobierania](Download/pl.md)
-   [FreeCAD PPA dla Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [dodatki FreeCAD PPA dla Ubuntu](https://launchpad.net/freecad-extras)
-   [Samodzielna kompilacja FreeCAD](Compiling/pl.md)
-   [tłumaczenie GUI FreeCAD](https://crowdin.com/project/freecad)
-   [GitHub dla FreeCAD](https://github.com/FreeCAD)
-   [Menadżer dodatków](Std_AddonMgr/pl.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/pl
