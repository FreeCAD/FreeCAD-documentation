# Compile on Windows/pl
Ta strona wyjaśnia krok po kroku **jak skompilować FreeCAD 0.19 lub nowszy w systemie Windows** przy użyciu kompilatora MSVC firmy Microsoft. Informacje na temat korzystania z MSYS2/MinGW można znaleźć na stronie [Kompilacja z MinGW](Compile_on_MinGW/pl.md). Dla innych platform zobacz opis [kompilacji](Compiling/pl.md).



## Wymagania wstępne 

Kompilacja FreeCAD w systemie Windows wymaga kilku narzędzi i bibliotek.



### Niezbędne

-   Kompilator. FreeCAD jest testowany z Visual Studio (MSVC) - inne kompilatory mogą działać, ale instrukcje użytkowania nie są tutaj zawarte. Więcej szczegółów można znaleźć w sekcji [Kompilator](#Kompilator.md) poniżej.

-   [Git](http://git-scm.com/) (dostępne są również interfejsy GUI dla Git, patrz następna sekcja)

-   [CMake](https://cmake.org/download/) version 3.11.x or newer.  *Wskazówka:* Wybranie opcji *Add CMake to the system PATH for all users* podczas instalacji CMake sprawi, że CMake będzie dostępny z wiersza poleceń systemu Windows, co może być przydatne.

-   [LibPack](https://github.com/FreeCAD/FreeCAD-LibPack). Jest to pojedynczy pakiet zawierający wszystkie biblioteki niezbędne do kompilacji FreeCAD na Windows. Pobierz wersję LibPack odpowiadającą wersji FreeCAD, którą chcesz skompilować. Aby skompilować FreeCAD 0.20 pobierz [LibPack w wersji 2.6](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/2.6), a dla FreeCAD 0.19 pobierz [LibPack w wersji 1.0](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/1.0). Wypakuj LibPack do wygodnej lokalizacji (jeśli twój komputer nie rozpoznaje rozszerzenia .7z, musisz zainstalować program [7-zip](https://www.7-zip.org)) **Uwaga**: Zdecydowanie zaleca się kompilację FreeCAD za pomocą wersji kompilatora, dla której zaprojektowano LibPack. Na przykład, możesz napotkać problemy podczas kompilacji FreeCAD 0.20 używając MSVC 2017, ponieważ LibPack jest zaprojektowany do kompilacji za pomocą MSVC 2019 lub nowszego.Aby zaktualizować swój LibPack później, zobacz sekcję [Aktualizacja LibPack](#Aktualizacja_LibPack.md).



### Programy opcjonalne 

-   GUI dla Git. Istnieje kilka dostępnych interfejsów, zobacz [tę listę](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs). Główną zaletą interfejsu graficznego jest to, że nie musisz uczyć się komend Git, aby uzyskać kod źródłowy FreeCAD lub wysyłać poprawki do repozytorium FreeCAD na GitHub.

W poniższym opisie przedstawiamy obsługę kodu źródłowego za pomocą interfejsu [TortoiseGit](https://tortoisegit.org/). Ten interfejs integruje się bezpośrednio z eksploratorem plików Windows i ma dużą społeczność użytkowników, która może pomóc w przypadku napotkania problemów.

[NSIS](http://sourceforge.net/projects/nsis/) jest używany do generowania instalatora FreeCAD dla systemu Windows.



### Kod źródłowy 

Teraz możesz pobrać kod źródłowy programu FreeCAD:



#### Używanie interfejsu 

Korzystając z [interfejsu Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Utwórz nowy folder, do którego zostanie pobrany kod źródłowy.
2.  Kliknij prawym przyciskiem myszy na tym folderze w eksploratorze plików Windows i wybierz **Git Clone** w menu kontekstowym.
3.  Pojawi się okno dialogowe. Wprowadź w nim adres URL repozytorium Git programu FreeCAD.

*<https://github.com/FreeCAD/FreeCAD.git>*

i kliknij **OK**.

Najnowszy kod źródłowy zostanie pobrany z repozytorium Git programu FreeCAD, a folder będzie śledzony przez Git.



#### Używanie wiersza poleceń 

Aby utworzyć lokalną gałąź śledzącą i pobrać kod źródłowy, otwórz terminal (wiersz poleceń) i przejdź do katalogu, w którym chcesz umieścić kod źródłowy, a następnie wpisz:


```python
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
```



### Kompilator

Domyślnym (zalecanym) kompilatorem jest MS Visual Studio (MSVC). Choć możliwe jest użycie innych kompilatorów, na przykład gcc za pośrednictwem Cygwin lub MinGW, nie jest to testowane ani opisane w tym miejscu.

Możesz uzyskać darmową wersję MSVC (do użytku indywidualnego), pobierając [edycję *Community* oprogramowania MS Visual Studio](https://visualstudio.microsoft.com/vs/community/).

Jeśli chcesz uniknąć instalacji ogromnego MSVC tylko w celu posiadania kompilatora, zobacz [Kompilacja w Windows OS - zmniejszanie zajętości dysku](CompileOnWindows_-_Reducing_Disk_Footprint/pl.md).

**Uwaga:** Choć edycja *Community* MSVC jest darmowa, aby korzystać z IDE przez więcej niż 30 dni, musisz stworzyć konto Microsoft. Jeśli zamierzasz jedynie kompilować za pomocą wiersza poleceń, nie potrzebujesz IDE i tym samym nie musisz tworzyć konta Microsoft.

Jako darmową i otwarto-źródłową alternatywę IDE możesz użyć [KDevelop](https://www.kdevelop.org/download). Możesz używać KDevelop do modyfikowania i pisania kodu C++, ale kompilację musisz przeprowadzać za pomocą wiersza poleceń.



### Opcjonalna konfiguracja ścieżek systemowych 

Opcjonalnie możesz dodać ścieżki do niektórych folderów do zmiennej systemowej PATH. Jest to przydatne, jeśli chcesz uzyskać dostęp do programów w tych folderach z poziomu wiersza poleceń/powershell lub jeśli chcesz, aby specjalne programy były odnajdywane przez kompilator lub CMake. Poza tym dodanie folderów do PATH może być konieczne, jeśli nie użyłeś odpowiednich opcji podczas instalacji programu.

-   Możesz dodać folder swojego LibPack do zmiennej systemowej PATH. Jest to przydatne, jeśli planujesz budować wiele konfiguracji/wersji FreeCAD.
-   Jeśli nie użyłeś opcji dodania CMake do PATH podczas instalacji, dodaj jego folder instalacyjny.

*C:\\Program Files\\CMake\\bin* do PATH.

-   Jeśli nie użyłeś opcji dodania TortoiseGit do PATH podczas instalacji, dodaj jego folder instalacyjny.

*C:\\Program Files\\TortoiseGit\\bin* do PATH.

Aby dodać ścieżki folderów do zmiennej PATH:

1.  W menu Start systemu Windows kliknij prawym przyciskiem myszy na *Komputer* i wybierz *Właściwości*.
2.  W pojawiającym się oknie kliknij na *Zaawansowane ustawienia systemu*.
3.  Otworzy się kolejne okno. Kliknij tam na zakładkę *Zaawansowane* i wybierz **Zmienne środowiskowe**.
4.  Otworzy się następne okno. Wybierz zmienną *Path* i kliknij **Edytuj**.
5.  Otworzy się kolejne okno. Kliknij tam na **Nowy** i dodaj ścieżkę do folderu Git lub LibPack.
6.  Na koniec naciśnij **OK** i zamknij wszystkie okna, klikając **OK**.



## Konfiguracja

Gdy masz już wszystkie niezbędne narzędzia, biblioteki i kod źródłowy FreeCAD, możesz przystąpić do procesu konfiguracji i kompilacji. Proces ten przebiega w pięciu krokach:

1.  Uruchom CMake, aby sprawdzić system i rozpocząć proces konfiguracji (początkowo zgłosi błąd).
2.  Dostosuj odpowiednie ustawienia CMake, aby ustawić lokalizacje LibPack i włączyć Qt5.
3.  Uruchom ponownie CMake, aby zakończyć konfigurację (tym razem powinno się udać).
4.  Użyj CMake do wygenerowania systemu budowania Visual Studio.
5.  Użyj Visual Studio do zbudowania FreeCAD.

### CMake

Najpierw skonfiguruj środowisko budowania za pomocą CMake:

1.  Otwórz interfejs graficzny CMake.
2.  Wskaż folder źródłowy FreeCAD.
3.  Wskaż folder budowania. Może to być **build** w folderze, do którego sklonowano repozytorium, ponieważ ta ścieżka jest ignorowana przez git. Nie używaj folderu źródłowego. CMake utworzy ten folder, jeśli nie istnieje.
4.  Kliknij **Configure**.
5.  W pojawiającym się oknie dialogowym wskaż generator, który chcesz użyć: w większości przypadków będziesz używać domyślnych opcji w tym oknie. Dla standardowego MS Visual Studio wybierz *Visual Studio xx 2yyy*, gdzie xx to wersja kompilatora, a 2yyy rok jego wydania. Zaleca się użycie domyślnej opcji *Use default native compilers*.

**Uwaga:** Ważne jest, aby określić odpowiednią wersję bitową. Jeśli masz 64-bitową wersję LibPack, musisz również używać kompilatora x64.

To rozpocznie konfigurację i *nie powiedzie się* z powodu brakujących ustawień. Jest to normalne, ponieważ jeszcze nie określiłeś lokalizacji LibPack. Jednak mogą wystąpić inne błędy, które będą wymagały dodatkowych działań z Twojej strony.

Jeśli pojawi się komunikat o błędzie, że Visual Studio nie może zostać znalezione, oznacza to, że wsparcie CMake w MSVC nie jest jeszcze zainstalowane. Aby to zrobić:

1.  Otwórz IDE MSVC.
2.  Użyj menu Narzędzia → Pobierz narzędzia i funkcje.
3.  W zakładce *Obciążenia* zaznacz *Rozwój aplikacji na desktopie w C++*.
4.  Po prawej stronie powinieneś teraz zobaczyć, że komponent *Narzędzia Visual C++ dla CMake* zostanie zainstalowany.
5.  Zainstaluj go.

Jeśli pojawi się błąd dotyczący nieprawidłowej wersji Pythona lub braku Pythona, wtedy:

1.  Użyj pola \"Search:\" w CMake, aby wyszukać ciąg \"Python\".
2.  Jeśli zobaczysz ścieżkę taką jak *C:/Program Files/Python38/python.exe*, CMake rozpoznał Pythona, który jest już zainstalowany na twoim komputerze, ale ta wersja jest niekompatybilna z LibPack. Ponieważ LibPack zawiera kompatybilną wersję Pythona, zmodyfikuj następujące ustawienia Pythona w CMake na jego ścieżki (zakładając, że LibPack znajduje się w folderze *D:/FreeCAD-build/FreeCADLibs_2_8_x64_VC2019*):

![](images/CMake_Python_settings.png )

Jeśli nie występują błędy dotyczące Visual Studio lub Pythona, wszystko jest w porządku, ale CMake nadal nie zna wszystkich niezbędnych ustawień. Dlatego teraz:

1.  W CMake wyszukaj zmienną **FREECAD_LIBPACK_DIR** i wskaż lokalizację folderu LibPack, który pobrałeś wcześniej.
2.  (*Jeśli budujesz FreeCAD 0.19*) Wyszukaj zmienną **BUILD_QT5** i włącz tę opcję.
3.  (*Jeśli planujesz uruchamianie bezpośrednio z folderu budowania, na przykład do debugowania*) Wyszukaj i włącz następujące opcje:
    -   **FREECAD_COPY_DEPEND_DIRS_TO_BUILD**
    -   **FREECAD_COPY_LIBPACK_BIN_TO_BUILD**
    -   **FREECAD_COPY_PLUGINS_BIN_TO_BUILD**
4.  Kliknij **Configure** ponownie.

Nie powinno już być żadnych błędów. Jeśli nadal napotykasz błędy, których nie możesz zdiagnozować, odwiedź forum [Install/Compile](https://forum.freecadweb.org/viewforum.php?f=4) na stronie forum FreeCAD. Jeśli CMake przebiegł poprawnie, kliknij **Generate**. Po zakończeniu możesz zamknąć CMake i rozpocząć kompilację FreeCAD za pomocą Visual Studio. Jednak podczas pierwszej kompilacji trzymaj CMake otwarte, na wypadek gdybyś chciał lub musiał zmienić niektóre opcje procesu kompilacji.



### Opcje kompilacji 

System kompilacji CMake daje Ci kontrolę nad niektórymi aspektami procesu kompilacji. W szczególności możesz włączać i wyłączać niektóre funkcje lub moduły za pomocą zmiennych CMake.

Oto opis niektórych z tych zmiennych:

  Nazwa zmiennej                      Opis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Domyślna wartość
    
  BUILD_XXX                           Kompiluj FreeCAD z komponentem XXX. Jeśli nie chcesz/nie musisz kompilować np. środowiska pracy *OpenSCAD*, wyłącz zmienną *BUILD_OPENSCAD*. FreeCAD nie będzie wtedy miał tego środowiska pracy. **Uwaga:** Niektóre komponenty są wymagane dla innych komponentów. Jeśli na przykład odznaczysz *BUILD_ROBOT*, CMake poinformuje Cię, że komponent *Path* nie może być poprawnie skompilowany. Dlatego sprawdź wynik CMake po zmianie opcji BUILD_XXX!                                                                                                                                                                                                                 zależy
  BUILD_ENABLE_CXX_STD                Wersja standardu języka C++. **C++14** jest najwyższą możliwą wersją dla FreeCAD 0.19, podczas gdy dla FreeCAD 0.20 wymagana jest przynajmniej **C++17**. Zobacz także uwagi w sekcji [Kompilacja z Visual Studio 15 (2017) i 16 (2019)](#Kompilacja_Release.md)                                                                                                                                                                                                                                                                                                                                                                                                 zależy
  BUILD_DESIGNER_PLUGIN               Aby zbudować wtyczkę Qt Designer, zobacz [tę sekcję poniżej](Compile_on_Windows/pl#Plugin_Qt_Designer.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        OFF
  BUILD_FLAT_MESH                     Konieczne do uzyskania kompilacji zawierającej funkcję [Projekt Siatki: Rozwiń siatkę](MeshPart_CreateFlatMesh/pl.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            OFF
  CMAKE_INSTALL_PREFIX                Folder wyjściowy podczas kompilacji celu *INSTALL*, zobacz także sekcję [Uruchamianie i instalowanie FreeCAD](#Uruchamianie_i_instalowanie_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Domyślny folder instalacji programów w Windows
  FREECAD_COPY_DEPEND_DIRS_TO_BUILD   Kopiuje potrzebne biblioteki zależne do folderu budowania, aby uruchomić FreeCAD.exe. Zobacz także sekcję [Uruchamianie i instalowanie FreeCAD](#Uruchamianie_i_instalacja_FreeCAD.md). **Uwaga:** opcje FREECAD_COPY_XXX pojawiają się tylko wtedy, gdy biblioteki nie zostały już skopiowane. Jeśli potrzebujesz tylko zaktualizować/zamienić wersję LibPack, zobacz sekcję [Aktualizacja LibPack](#Aktualizacja_LibPack.md). Jeśli chcesz przywrócić opcje z jakiegoś powodu, musisz usunąć wszystkie foldery w folderze budowania, oprócz folderu LibPack. W CMake usuń pamięć podręczną i rozpocznij jak przy pierwszej kompilacji.   OFF
  FREECAD_COPY_LIBPACK_BIN_TO_BUILD   Kopiuje pliki binarne LibPack potrzebne do uruchomienia FreeCAD.exe do folderu budowania. Zobacz także sekcję [Uruchamianie i instalowanie FreeCAD](#Uruchamianie_i_instalowanie_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    OFF
  FREECAD_COPY_PLUGINS_BIN_TO_BUILD   Kopiuje pliki wtyczek Qt potrzebne do uruchomienia FreeCAD.exe do folderu budowania. Zobacz także sekcję [Uruchamianie i instalowanie FreeCAD](#Uruchamianie_i_instalowanie_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                         OFF
  FREECAD_LIBPACK_USE                 Włącza lub wyłącza użycie LibPack FreeCAD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ON
  FREECAD_LIBPACK_DIR                 Katalog, w którym znajduje się LibPack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Folder z kodem źródłowym FreeCAD
  FREECAD_RELEASE_PDB                 Tworzy biblioteki debugowania (\*.pdb) również dla kompilacji wersji release. Nie wpływa na prędkość (jak prawdziwa kompilacja debug) i może być bardzo przydatne do lokalizowania awarii w kodzie FreeCAD. W przypadku awarii FreeCAD zostanie utworzony plik *crash.dmp*, który można załadować w MSVC, a jeśli masz odpowiednie pliki PDB i kod źródłowy tej wersji, możesz debugować kod. Bez plików PDB nie można debugować kodu, a wszystko, co pokazuje debugger, to nazwa DLL, w której wystąpiła awaria.                                                                                                                                                        ON
  FREECAD_USE_MP_COMPILE_FLAG         Dodaje opcję /MP (multiprocessor) do projektów Visual Studio, co umożliwia przyspieszenie na wielordzeniowych CPU. Może to znacznie przyspieszyć kompilacje na nowoczesnych procesorach.**Uwaga:** Jeśli wyłączysz **FREECAD_USE_PCH**, kompilacja może szybko przeciążyć pamięć operacyjną, nawet jeśli masz 16 GB RAM.                                                                                                                                                                                                                                                                                                                                   ON
  FREECAD_USE_PCH                     [Prekompiluje nagłówki](https://en.wikipedia.org/wiki/Precompiled_header) w celu zaoszczędzenia czasu kompilacji.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  FREECAD_USE_PYBIND11                Włącza bibliotekę [PyBind11](https://github.com/pybind/pybind11). Konieczne do uzyskania kompilacji zawierającej funkcję [Projekt Siatki: Rozwiń siatkę](MeshPart_CreateFlatMesh/pl.md).**Uwaga:** po włączeniu tej opcji możesz otrzymać błąd konfiguracji. Wystarczy skonfigurować ponownie, a problem powinien zniknąć.                                                                                                                                                                                                                                                                                                                         OFF



## Kompilacja FreeCAD 

W zależności od używanego kompilatora proces kompilacji FreeCAD może się nieco różnić. W poniższych sekcjach opisane są znane podejścia. Jeśli kompilujesz za pomocą Qt Creator, przejdź do [Kompilacja z Qt Creator (nieaktualne)](#Kompilacja_z_Qt_Creator_(niekatualne).md), w przeciwnym razie kontynuuj bezpośrednio:



### Kompilacja z linii poleceń cmd.exe 

Jeśli chcesz kompilować z wiersza poleceń, dane wyjściowe z CMake pokażą Ci odpowiednie polecenie do uruchomienia (które zależy od skonfigurowanego katalogu wydania). Jednak to polecenie spowoduje wykonanie kompilacji *Debug*, która nie działa w systemie Windows i skutkuje błędem importu Numpy w FreeCAD (co jest znanym problemem, ale trudnym do naprawienia). Musisz określić opcję *\--config Release*, aby wymusić kompilację *Release*:


```python
cmake --build E:/release --config Release
```

Należy pamiętać, że ustawienie zmiennych CMake, takich jak *CMAKE_BUILD_TYPE*, nie ma żadnego wpływu; jedynie określenie opcji *\--config* jak pokazano powyżej działa.


<div class="mw-collapsible mw-collapsed toccolours">



### Kompilacja w Visual Studio 15 (2017) lub nowszym 


<div class="mw-collapsible-content">



#### Kompilacja Release 

1.  Uruchom IDE Visual Studio. Można to zrobić, klikając przycisk *Open Project* w GUI CMake lub klikając dwukrotnie na plik *FreeCAD.sln*, który znajdziesz w swoim folderze kompilacji.
2.  Na pasku narzędzi IDE MSVC upewnij się, że dla pierwszej kompilacji wybrana jest opcja *Release*.
3.  Istnieje okno o nazwie *Solution Explorer*. Wyświetla ono wszystkie możliwe cele kompilacji. Aby rozpocząć pełną kompilację, kliknij prawym przyciskiem myszy na cel **ALL_BUILD** i wybierz **Build**.

To potrwa dość długo.

Aby skompilować gotowy do użycia FreeCAD, skompiluj cel *INSTALL*, zobacz sekcję [Uruchamianie i instalowanie FreeCAD](#Uruchamianie_i_instalowanie_FreeCAD.md).

Jeśli nie napotkałeś żadnych błędów, skończyłeś. **Gratulacje!** Możesz zamknąć MSVC lub pozostawić je otwarte.

**Ważne:** Od wersji Visual Studio 17.4 nie można używać optymalizacji kodu, która jest domyślnie włączona dla celu **SketcherGui**. Jeśli to zrobisz, wiązania kątowe będą źle umieszczone w szkicach. Aby to naprawić, kliknij prawym przyciskiem myszy na ten cel w eksploratorze rozwiązań MSVC i wybierz ostatnią pozycję **Properties** w menu kontekstowym. W pojawiającym się oknie przejdź do C/C++ → Optimization i tam wyłącz ustawienie **Optimization**. Na koniec zbuduj cel **ALL_BUILD** ponownie.



#### Kompilacja Debug 

Aby przeprowadzić kompilację Debug, konieczne jest użycie Pythona, który jest dołączony do LibPack. Aby to zapewnić:

1.  W GUI CMake wyszukaj \"Python\".
2.  Jeśli zobaczysz tam ścieżkę, taką jak *C:/Program Files/Python38/python.exe*, CMake rozpoznał Pythona zainstalowanego na Twoim komputerze, a nie tego z LibPack. W takim wypadku dostosuj te różne ustawienia Pythona w CMake do tego (zakładając, że LibPack znajduje się w folderze *D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17*):

![](images/CMake_Python_settings.png )

Jako warunek wstępny dla kompilacji Debug, musisz wykonać następujące kroki:

1.  Skopiuj zawartość folderu LibPack *bind* do folderu *bin* w folderze kompilacji FreeCAD (nadpisz istniejące pliki).
2.  Skopiuj zawartość folderu LibPack *libd* do folderu *lib* w folderze kompilacji FreeCAD.

Teraz możesz przystąpić do kompilacji:

1.  Uruchom IDE Visual Studio. Można to zrobić, klikając przycisk *Open Project* w GUI CMake lub klikając dwukrotnie na plik *FreeCAD.sln*, który znajdziesz w swoim folderze budowania.
2.  Na pasku narzędzi IDE MSVC upewnij się, że dla pierwszej kompilacji wybrana jest opcja *Debug*.
3.  Istnieje okno o nazwie *Solution Explorer*. Wyświetla ono wszystkie możliwe cele kompilacji. Aby rozpocząć pełną kompilację, kliknij prawym przyciskiem myszy na cel **ALL_BUILD** i wybierz **Build** w menu kontekstowym.

To potrwa dość długo.

Jeśli nie było błędów kompilacji, a opcje **FREECAD_COPY\_\*** wspomniane w [kroku konfiguracji CMake](#CMake.md) były włączone, możesz rozpocząć kompilację Debug:

1.  Kliknij prawym przyciskiem myszy na cel **FreeCADMain** i wybierz **Set as Startup Project** w menu kontekstowym.
2.  Na koniec kliknij na pasku narzędzi przycisk z zielonym trójkątem o nazwie **Local Windows Debugger**.

To rozpocznie kompilację Debug programu FreeCAD i będziesz mógł używać IDE MSVC do debugowania.

#### Materiał wideo 

Dostępny jest anglojęzyczny samouczek, który zaczyna się od konfiguracji w CMake Gui i kontynuuje do polecenia \Build\ w Visual Studio 16 2019. Jest on dostępny jako niepubliczny film na YouTube pod adresem [Tutorial: Build FreeCAD from source on Windows 10](https://youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Kompilacja z Qt Creator (nieaktualne) 


<div class="mw-collapsible-content">



#### Instalacja i konfiguracja Qt Creator 

-   Pobierz i zainstaluj [Qt Creator](https://www.qt.io/offline-installers)
-   Tools → Options → Text Editor → Behavior:
    -   File Encodings → Default Encodings:
    -   Ustaw na: **ISO-8859-1 /\...csISOLatin1** (Niektóre znaki powodują błędy/ostrzeżenia w Qt Creator, jeśli pozostaną ustawione na UTF-8. To powinno rozwiązać problem.)
-   Tools → Options → Build & Run:
    -   Zakładka CMake
        -   Wypełnij pole Executable ścieżką do cmake.exe
    -   Zakładka Kits
        -   Name: MSVC 2008
        -   Compiler: Microsoft Visual C++ Compiler 9.0 (x86)
        -   Debugger: Automatycznie wykryty\...
        -   Qt version: Brak
    -   Zakładka General
        -   Odznacz: Always build project before deploying it
        -   Odznacz: Always deploy project before running it



#### Import projektu i kompilacja 

-   File → Open File or Project
-   Otwórz **CMakeLists.txt** znajdujący się na najwyższym poziomie źródła
-   To uruchomi CMake
-   Wybierz katalog kompilacji i kliknij next
-   Ustaw generator na **NMake Generator (MSVC 2008)**
-   Kliknij Run CMake. Postępuj zgodnie z instrukcjami opisanymi powyżej, aby skonfigurować CMake według własnych potrzeb.

Teraz FreeCAD można skompilować

-   Build → Build All
-   To zajmie dużo czasu\...

Po zakończeniu można uruchomić: W lewym dolnym rogu znajdują się dwa zielone trójkąty. Jeden to debug. Drugi to run. Wybierz ten, który chcesz.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Kompilacja z linii poleceń 


<div class="mw-collapsible-content">

Kroki, jak skompilować z linii poleceń, zależą od kompilatora. Dla MSVC 2017 kroki są następujące:

1.  W menu Start systemu Windows przejdź do **Visual Studio 2017 → Visual Studio Tools** i wybierz **Developer Command Prompt for VS 2017**
2.  Przejdź do folderu kompilacji.
3.  Wykonaj polecenie


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

lub


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```

Te kroki można również zautomatyzować. Oto przykład rozwiązania dla MSVC 2017:

1.  Pobierz skrypt [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Zmień nazwę na *compile-FC.bat*
3.  W Eksploratorze plików Windows, przytrzymaj Shift+prawy przycisk myszy na swoim folderze kompilacji i użyj opcji *Wiersz poleceń tutaj* z menu kontekstowego.
4.  Wykonaj polecenie


```pythoncompile-FC install```

Zamiast wywoływać **compile-FC** z opcją *install*, możesz również użyć *debug* lub *release*:

*debug*   - kompiluje FreeCAD w konfiguracji debugowania

*release* - kompiluje FreeCAD w konfiguracji release

*install*    - kompiluje FreeCAD w konfiguracji release i tworzy instalator


</div>


</div>



## Uruchamianie i instalowanie FreeCAD 

Istnieją 2 metody uruchamiania skompilowanego programu FreeCAD:

*Metoda 1*: Uruchomiasz FreeCAD.exe, który znajdziesz w folderze kompilacji w podfolderze *bin*

*Metoda 2*: Kompilujesz cel *INSTALL*

Metoda 2 jest prostsza, ponieważ automatycznie zapewnia, że wszystkie biblioteki potrzebne do uruchomienia FreeCAD.exe znajdują się w odpowiednim folderze. FreeCAD.exe i biblioteki zostaną zapisane w folderze, który określiłeś w zmiennej CMake *CMAKE_INSTALL_PREFIX*.

W przypadku Metody 1 musisz włączyć opcje **FREECAD_COPY\_\*** wspomniane w [kroku konfiguracji CMake](#CMake.md) powyżej.



### Rozwiązywanie problemów 

Podczas uruchamiania FreeCAD możesz napotkać brakujące pliki DLL przy korzystaniu z niektórych środowisk pracy lub funkcji środowisk pracy. Komunikat o błędzie w konsoli FreeCAD nie wskaże, które DLL jest brakujące. Aby się dowiedzieć, musisz użyć zewnętrznego narzędzia:

-   Pobierz najnowszą wersję programu **Dependencies**: <https://github.com/lucasg/Dependencies/releases> (wybierz plik *Dependencies_x64_Release.zip*)
-   W [konsoli Pythona](Python_console/pl.md) progrmau FreeCAD wykonaj te polecenia:

import os
os.system(r"~\DependenciesGui.exe")

**Uwaga**: Zamiast \~ musisz podać pełną ścieżkę do *DependenciesGui.exe* w swoim systemie.

-   Teraz przeciągnij plik \*.pyd środowiska pracy, dla którego zgłaszane są brakujące pliki DLL.



## Aktualizacja kompilacji 

FreeCAD jest bardzo aktywnie rozwijany. Dlatego jego kod źródłowy zmienia się niemal codziennie. Nowe funkcje są dodawane, a błędy naprawiane. Aby skorzystać z tych zmian w kodzie źródłowym, musisz ponownie zbudować FreeCAD. Obejmuje to dwa kroki:

1.  Aktualizacja kodu źródłowego
2.  Rekompilacja



### Aktualizacja kodu źródłowego 



#### Używanie interfejsu 

Korzystając z [interfejsu Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Kliknij prawym przyciskiem myszy na folder z kodem źródłowym programu FreeCAD w Eksploratorze plików Windows i wybierz **Pull** w menu kontekstowym.
2.  Pojawi się okno dialogowe. Wybierz tam, którą gałąź rozwojową chcesz pobrać. **master** to główna gałąź, więc używaj jej, chyba że chcesz skompilować specjalną nową funkcję z gałęzi, która nie została jeszcze scalona z *master*. (Aby uzyskać więcej informacji o gałęziach Git, zobacz [Proces rozwoju w Git](Source_code_management/pl#Proces_rozwoju_w_Git.md).)

Wreszcie kliknij **OK**.



#### Używanie wiersza poleceń 

Otwórz terminal (wiersz poleceń) i przejdź do katalogu źródłowego. Następnie wpisz:


```python
git pull https://github.com/FreeCAD/FreeCAD.git master
```

gdzie *master* to nazwa głównej gałęzi rozwojowej. Jeśli chcesz pobrać kod z innej gałęzi, użyj jej nazwy zamiast *master*.



### Rekompilacja

1.  Otwórz IDE MSVC, klikając dwukrotnie na plik *FreeCAD.sln* lub na plik *ALL_BUILD.vcxproj* w folderze kompilacji.
2.  Kontynuuj od kroku 2 z sekcji [Kompilacja w Visual Studio 15 (2017) lub nowszym](#Kompilacja_w_Visual_Studio_15_(2017)_lub_nowszym.md).



## Aktualizacja LibPack 

Jeśli zostanie wydana nowa duża wersja zależności zewnętrznej, takiej jak Open Cascade, lub jeśli zależność zewnętrzna otrzyma ważne poprawki błędów, zostanie wydana nowa wersja LibPack. Najnowszą wersję można znaleźć [tutaj](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

Aby zaktualizować swój LibPack, najlepiej postępować zgodnie z poniższymi krokami:

1.  Usuń folder *bin* w folderze kompilacji.
2.  Przejdź do lokalnego folderu LibPack i usuń z niego wszystkie pliki.
3.  Wypakuj zawartość nowego pliku ZIP LibPack do istniejącego, ale teraz pustego lokalnego folderu LibPack.
4.  Otwórz CMake, kliknij przycisk **Configure**, a następnie przycisk **Generate**. Spowoduje to ponowne utworzenie folderu *bin*, który właśnie usunąłeś, oraz skopiowanie nowych plików LibPack do tego folderu.
5.  W CMake kliknij przycisk **Open Project**, a IDE MSVC zostanie otwarte.
6.  W IDE MSVC zbuduj cel *INSTALL*.



## Przybory

Aby dołączyć do rozwoju FreeCAD, należy skompilować i zainstalować następujące narzędzia:



### Plugin Qt Designer 

FreeCAD używa [Qt](https://en.wikipedia.org/wiki/Qt_(software)) jako narzędzia do budowy interfejsu użytkownika. Wszystkie okna dialogowe są definiowane w plikach UI, które można edytować za pomocą programu [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html), będącego częścią każdej instalacji Qt i również zawartego w LibPack. FreeCAD posiada własny zestaw widżetów Qt, które zapewniają specjalne funkcje, takie jak dodawanie jednostek do pól wejściowych i ustawianie właściwości preferencji.



#### Kompilacja

Wtyczka nie może być załadowana przez Qt Designer, jeśli została skompilowana przy użyciu innej wersji Qt niż ta, na której oparty jest Twój Qt Designer/Qt Creator. Dlatego wtyczka musi być kompilowana razem z FreeCAD.

-   W opcjach CMake (zobacz [tę sekcję powyżej](Compile_on_Windows/pl#Opcje_kompilacji.md)) włącz opcję BUILD_DESIGNER_PLUGIN i przeprowadź rekonfigurację.
-   Otwórz MSVC i zbuduj cel **FreeCAD_widgets**

W wyniku tego otrzymasz plik wtyczki **FreeCAD_widgets.dll** w folderze*\~\\src\\Tools\\plugins\\widget\\Release*



#### Instalacja

Aby zainstalować wtyczkę, skopiuj plik DLL do jednego z poniższych folderów:

-   Jeśli używasz LibPack: do folderu*\~\\FreeCADLibs_2_8_x64_VC2019\\plugins\\designer*
-   Jeśli masz pełną instalację Qt: możesz wybrać jeden z folderów:*C:\\Qt\\5.15.2\\msvc2019_64\\plugins\\designer*lub*C:\\Qt\\5.15.2\\msvc2019_64\\bin\\designer* (musisz najpierw utworzyć podfolder *designer*).(dostosuj ścieżki do swojej instalacji!).

Na koniec (ponownie) uruchom Qt Designer i sprawdź jego menu **Help → Plugins**. Jeśli wtyczka **FreeCAD_widgets.dll** jest wymieniona jako załadowana, możesz teraz projektować i zmieniać pliki .ui FreeCAD. Jeśli nie, musisz [skompilować](#Kompilacja.md) DLL samodzielnie.

Jeśli wolisz używać [Qt Creatora](https://en.wikipedia.org/wiki/Qt_Creator) zamiast Qt Designera, plik wtyczki należy umieścić w tym folderze:*C:\\Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer* Następnie (ponownie) uruchom Qt Creator, przełącz się na tryb **Design**, a następnie sprawdź menu **Tools → Form Editor → About Qt Designer Plugins**. Jeśli wtyczka **FreeCAD_widgets.dll** jest wymieniona jako załadowana, możesz teraz projektować i zmieniać pliki .ui programu FreeCAD. Jeśli nie, musisz [skompilować](#Kompilacja.md) DLL samodzielnie.

### Thumbnail Provider 

FreeCAD ma funkcję zapewniania podglądu miniatur dla plików \*.FCStd. Oznacza to, że w Eksploratorze Windows pliki \*.FCStd są wyświetlane ze zrzutem ekranu modelu, który zawierają. Aby zapewnić tę funkcję, FreeCAD musi mieć plik **FCStdThumbnail.dll** zainstalowany w Windows.



#### Instalacja 

DLL jest instalowany w następujący sposób:

1.  Pobierz [ten plik ZIP](https://forum.freecadweb.org/download/file.php?id=13404) i rozpakuj go.
2.  Otwórz wiersz poleceń Windows z uprawnieniami administratora (te uprawnienia są wymagane).
3.  Przejdź do folderu, w którym znajduje się DLL.
4.  Wykonaj to polecenie 
```pythonregsvr32 FCStdThumbnail.dll```

Aby sprawdzić, czy to działa, upewnij się, że w programie FreeCAD preferencja **[Zapisz miniaturę do pliku projektu podczas zapisywania dokumentu](Preferences_Editor/pl#Dokument.md)** jest włączona i zapisz model. Następnie, w Eksploratorze Windows, otwórz folder zapisanych modeli używając widoku symboli. Powinieneś teraz zobaczyć zrzut ekranu modelu w widoku folderu.



#### Kompilacja 

Aby skompilować plik FCStdThumbnail.dll:

1.  Przejdź do folderu źródłowego FreeCAD:*\~\\src\\Tools\\thumbs\\ThumbnailProvider*
2.  Otwórz GUI CMake
3.  Jako folder źródłowy wskaż bieżący folder.
4.  Użyj tego samego folderu jako folderu kompilacji.
5.  Kliknij **Configure**
6.  W pojawiającym się oknie dialogowym wybierz generator zgodnie z tym, który chcesz użyć. Dla standardowego MS Visual Studio użyj *Visual Studio xx 2yyy*, gdzie xx to wersja kompilatora, a 2yyy to rok wydania. Zaleca się użycie domyślnej opcji *Use default native compilers*.**Uwaga:** Ważne jest, aby określić prawidłowy wariant bitowy. Jeśli masz 64-bitowy wariant LibPack, musisz również użyć kompilatora x64.
7.  Kliknij **Generate**.
8.  Powinieneś teraz mieć plik **ALL_BUILD.vcxproj** w folderze *\~\\src\\Tools\\thumbs\\ThumbnailProvider*. Kliknij na niego dwukrotnie, aby otworzyć MSVC IDE.
9.  W pasku narzędzi MSVC IDE upewnij się, że używasz celu kompilacji *Release*.
10. W oknie *Solution Explorer* kliknij prawym przyciskiem myszy na **ALL_BUILD** i wybierz **Build**.
11. W wyniku kompilacji powinieneś teraz mieć plik **FCStdThumbnail.dll** w folderze *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release*, który możesz zainstalować zgodnie z opisem powyżej.



## Kompilacja Open Cascade 

LibPack zawiera wersję [Open Cascade](https://en.wikipedia.org/wiki/Open_Cascade) odpowiednią do ogólnego użytku. Jednak w pewnych okolicznościach możesz chcieć skompilować program z użyciem innej wersji Open Cascade, na przykład jednej z ich oficjalnych wersji lub zmodyfikowanej wersji.

Podczas kompilacji Open Cascade dla FreeCAD należy pamiętać, że nie ma gwarancji, iż FreeCAD będzie działać ze wszystkimi wersjami Open Cascade. Należy również pamiętać, że jeśli używasz biblioteki Netgen, musisz używać wersji Netgen zatwierdzonej do kompilacji z wersją Open Cascade, której chcesz użyć do kompilacji.

Aby skompilować:

-   Najpierw zdobądź kod źródłowy Open Cascade, bezpośrednio z [repozytorium git Open Cascade](https://github.com/Open-Cascade-SAS/OCCT) lub klonując inne repozytorium, na przykład [fork \"blobfish\"](https://gitlab.com/blobfish/occt) utrzymywany przez członka forum FreeCAD [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).

-   Następnie otwórz GUI CMake, aby skonfigurować system kompilacji w sposób podobny do kompilacji FreeCAD. Te opcje CMake muszą być ustawione (lub jawnie nie ustawione):

  Nazwa zmiennej                     Opis                                                                                                                                                                                                                                                                                                                Domyślna wartość
    
  3RDPARTY_DIR                       Ścieżka do komponentów zewnętrznych. Zaleca się używanie folderu, w którym znajduje się używany LibPack. Jawnie pozostaw to pole puste.                                                                                                                                                                             puste
  3RDPARTY_DOXYGEN_EXECUTABLE        Ścieżka do pliku wykonywalnego komponentu zewnętrznego [Doxygen](https://en.wikipedia.org/wiki/Doxygen). Zaleca się zainstalowanie Doxygen. CMake znajdzie go automatycznie.                                                                                                                                        puste
  3RDPARTY_FREETYPE_DIR              Ścieżka do niezbędnego komponentu zewnętrznego [Freetype](https://en.wikipedia.org/wiki/FreeType). Zaleca się używanie folderu, w którym znajduje się używany LibPack.                                                                                                                                              puste
  3RDPARTY_RAPIDJSON_DIR             Dostępne tylko jeśli **USE_RAPIDJSON** jest używane. Ścieżka do komponentu zewnętrznego [RapidJSON](https://rapidjson.org/). Zaleca się NIE używać istniejącego folderu LibPack jako wejścia. Możesz użyć folderu RapidJSOn z LibPack, ale skopiuj go do nowego folderu i użyj tego nowego folderu jako wejścia.    puste
  3RDPARTY_TCL_DIR                   Ścieżka do niezbędnego komponentu zewnętrznego [TCL](https://en.wikipedia.org/wiki/Tcl). Zaleca się NIE używać istniejącego folderu LibPack jako wejścia. Wybierz na przykład jedno z [tych wydań](https://github.com/teclab-at/tcltk/releases), rozpakuj je i użyj tego folderu jako wejścia dla CMake.            puste
  3RDPARTY_TK_DIR                    Ścieżka do niezbędnego komponentu zewnętrznego [TK](https://en.wikipedia.org/wiki/Tk_(software)). Zaleca się NIE używać istniejącego folderu LibPack jako wejścia. Wybierz na przykład jedno z [tych wydań](https://github.com/teclab-at/tcltk/releases), rozpakuj je i użyj tego folderu jako wejścia dla CMake.   puste
  3RDPARTY_VTK_DIR                   Dostępne tylko jeśli **USE_VTK** jest używane. Ścieżka do niezbędnego komponentu zewnętrznego [VTK](https://en.wikipedia.org/wiki/VTK). Zaleca się używanie folderu, w którym znajduje się używany LibPack. Jeśli używasz innego folderu, upewnij się, że nie używasz VTK 9.x lub nowszego.                         puste
  BUILD_RELEASE_DISABLE_EXCEPTIONS   Wyłącza obsługę wyjątków dla kompilacji wydania. Dla FreeCAD musisz ustawić na **OFF**.                                                                                                                                                                                                                             ON
  INSTALL_DIR                        Folder wyjściowy przy budowaniu celu *INSTALL*. Jeśli kompilacja zakończyła się sukcesem, weź pliki z tego folderu, aby zaktualizować swój LibPack.                                                                                                                                                                 domyślny folder instalacji programów w systemie Windows
  INSTALL_DIR_BIN                    Podfolder wyjściowy dla DLL przy budowaniu celu *INSTALL*. Musisz zmienić na **bin**                                                                                                                                                                                                                                win64/vc14/bin
  INSTALL_DIR_LIB                    Podfolder wyjściowy dla plików .lib przy budowaniu celu *INSTALL*. Musisz zmienić na **lib**                                                                                                                                                                                                                        win64/vc14/lib
  USE_RAPIDJSON                      Kompilacja Open Cascade z obsługą RapidJSON. Włączenie tej opcji jest obowiązkowe, aby uzyskać wsparcie dla formatu pliku [glTF](https://en.wikipedia.org/wiki/Gltf).                                                                                                                                               OFF
  USE_VTK                            Kompilacja Open Cascade z obsługą VTK. Włączenie tej opcji jest optymalne. Możesz użyć tego do budowy VTK Open Cascade bridge.                                                                                                                                                                                      OFF

-   Otwórz projekt w Visual Studio i najpierw zbuduj cele ALL_BUILD, a następnie INSTALL w trybie **Release**.
-   Powtórz budowanie obu celów w trybie **Debug**.

Aby zbudować FreeCAD przy użyciu samodzielnie skompilowanego Open Cascade, należy wykonać następujące kroki:

-   Skopiuj wszystkie foldery z INSTALL_DIR do folderu LibPack (nadpisz istniejące pliki).
-   Przejdź do folderu LibPack i wejdź do podfolderu *cmake*.
-   Otwórz plik *OpenCASCADEDrawTargets.cmake* w edytorze tekstu.
-   Wyszukaj tam bezwzględne ścieżki do folderu LibPack i usuń je. Na przykład bezwzględna ścieżka *D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib* zmienia się na *freetype.lib*.
-   Zrób to samo dla pliku *OpenCASCADEVisualizationTargets.cmake*.



## Kompilacja Netgen 

LibPack zawiera wersję [Netgen](https://ngsolve.org), która była testowana pod kątem zgodności z wersją Open Cascade LibPack. Problem polega na tym, że każda nowa wersja Netgen zmienia API. Każda nowa wersja Open Cascade również to robi. Dlatego nie można łatwo zmienić wersji Netgen.

Możesz jednak spróbować zbudować Netgen samodzielnie. To stosunkowo łatwe zadanie:

-   Najpierw pobierz kod źródłowy Netgen, bezpośrednio z [repozytorium Git Netgen](https://github.com/NGSolve/netgen).
-   Następnie otwórz GUI CMake, aby skonfigurować system kompilacji w sposób podobny do kompilacji FreeCAD. Należy ustawić następujące opcje CMake:

  Nazwa zmiennej         Opis                                                                                                                                                                                                                                                                                                                                                                                                                                                Domyślna wartość
    
  CMAKE_INSTALL_PREFIX   Folder wyjściowy podczas kompilacji celu *INSTALL*. Jeśli kompilacja zakończyła się sukcesem, przenieś pliki z tego folderu, aby zaktualizować swój LibPack.                                                                                                                                                                                                                                                                                        C:/netgen
  OpenCasCade_DIR        Ścieżka do plików CMake Open Cascade. Jeśli zbudowałeś Open Cascade zgodnie z opisem w sekcji [Kompilacja Open Cascade](#Kompilacja_Open_Cascade.md), możesz użyć podfolderu *cmake* folderu, który użyłeś jako INSTALL_DIR. Jeśli nie, użyj podfolderu *cmake* swojego LibPack. Niezależnie od używanego folderu, musisz również stworzyć podfolder *lib* i skopiować do niego pliki *freetype.lib* i *freetyped.lib* z Twojego LibPack.   puste
  USE_GUI                ustaw na **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                    ON
  USE_NATIVE_ARCH        ustaw na **OFF**; jest to ważne tylko w celu wsparcia starszych CPU, które nie obsługują zestawu instrukcji [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)                                                                                                                                                                                                                                                                        ON
  USE_OCC                ustaw na **ON**                                                                                                                                                                                                                                                                                                                                                                                                                                     OFF
  USE_PYTHON             ustaw na **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                    ON
  USE_SUPERBUILD         ustaw na **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                    ON
  ZLIB_INCLUDE_DIR       Ścieżka do niezbędnego komponentu zewnętrznego [zlib](https://en.wikipedia.org/wiki/Zlib). Zaleca się użycie folderu, w którym znajduje się Twój używany LibPack.                                                                                                                                                                                                                                                                                   puste
  ZLIB_LIBRARY_DEBUG     Ścieżka do pliku ZLib *zlibd.lib*. Znajduje się w podfolderze *lib* Twojego folderu LibPack.                                                                                                                                                                                                                                                                                                                                                        puste
  ZLIB_LIBRARY_RELEASE   Ścieżka do pliku ZLib *zlib.lib*. Znajduje się w podfolderze *lib* Twojego folderu LibPack.                                                                                                                                                                                                                                                                                                                                                         puste

-   Dodatkowo musisz dodać nowy wpis CMake: nazwa: *CMAKE_DEBUG_POSTFIX*, typ: *string*, zawartość: **\_d**

To zapewnia, że nazwy plików bibliotek debugujących będą miały inny nazwę niż biblioteki release, co zapobiega przypadkowemu zamienieniu ich później.

-   Naciśnij przycisk *Configure* w CMake, aby wygenerować pliki \*.cmake.
-   Tylko jeśli starsze CPU, które nie posiadają zestawu instrukcji AVX2, mają być obsługiwane:
    -   Poszukaj w folderze kompilacji Netgen pliku *netgen-targets.cmake* i otwórz go w edytorze tekstu. Usuń ustawienie *;/arch:AVX2* w opcji INTERFACE_COMPILE_OPTIONS.
    -   Naciśnij przycisk *Configure* w CMake ponownie.
-   Naciśnij przycisk *Generate* w CMake.
-   Otwórz projekt w Visual Studio i najpierw zbuduj cele ALL_BUILD, a następnie INSTALL w trybie **Release**.
-   Powtórz budowanie dwóch celów w trybie **Debug**.

Aby zbudować FreeCAD przy użyciu samodzielnie skompilowanego Netgen, musisz wykonać następujące kroki:

-   Skopiuj wszystkie foldery z CMAKE_INSTALL_PREFIX do folderu LibPack (nadpisując istniejące pliki).



## Źródła

Zobacz też

-   [Kompilacja (przyspieszamy)](Compiling_(Speeding_up)/pl.md)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/pl
