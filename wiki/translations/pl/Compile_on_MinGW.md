# Compile on MinGW/pl
Ten poradnik przeprowadzi przez kroki niezbędne do zbudowania FreeCAD w systemie Windows przy użyciu środowiska MSYS2 / MinGW. Podstawowa znajomość poleceń powłoki Bash będzie przydatna do zrozumienia, co robi każdy krok, ale podążanie za przewodnikiem na pamięć powinno zaowocować działającą kompilacją, nawet jeśli nie rozumiesz dokładnie, co zrobiłeś, aby ją uzyskać.



### Zanim zaczniesz 

Pobierz i zainstaluj [MSYS2](https://www.msys2.org), jeśli jeszcze tego nie zrobiłeś. Podczas uruchamiania MSYS2 użyj środowiska uruchomieniowego \"MSYS2 MinGW 64-bit\", chyba że wiesz, co robisz i masz konkretny powód, aby tego nie robić. Jeśli korzystasz z konsoli UCRT, upewnij się, że dostosowałeś swoją instalację do korzystania z pakietów UCRT.

    pacman -Syu

a następnie ponowne uruchomienie

    pacman -Su

przed kontynuowaniem.



### Zainstaluj podstawowe narzędzia programistyczne 

We wszystkich poniższych krokach, gdy pojawi się monit powłoki MSYS2, zaakceptuj domyślne instalacje wszystkich elementów, naciskając **Enter**, gdy zostaniesz o to poproszony.

Najpierw zainstaluj zestaw narzędzi GCC mingw-w64:

    pacman -S --needed base-devel mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja

Prawdopodobnie zajmie to kilka minut, ponieważ zestaw narzędzi kompilatora jest dość duży.

Zainstaluj Git:

    pacman -S git

Zamknij bieżące okno konsoli i ponownie uruchom konsolę MSYS2 MinGW 64 *(w standardowej instalacji będzie to menu Start w folderze MSYS2)*.



### Sprawdź źródła FreeCAD 

Aby uzyskać kod źródłowy FreeCAD, sklonuj go z głównego repozytorium Git:

    git clone https://github.com/FreeCAD/FreeCAD

Jeśli nie chcesz kompilować najnowszego HEAD, po uzyskaniu źródła możesz sprawdzić konkretny tag:

    cd FreeCAD
    git checkout tags/1.0 -b releases/FreeCAD-1-0

Lub konkretny \"pull request\" *(w tym przykładzie PR 1234)*:

    cd FreeCAD
    git fetch origin pull/1234/head:pr/1234
    git checkout pr/1234

Należy pamiętać, że nie wszystkie wersje mogą być kompilowane na MSYS2, kilka zmian było wymaganych, aby to umożliwić i nie były one obecne w wersji 0.19 lub wcześniejszych. Na przykład tag 0.19.3 nie będzie kompilowalny.



### Instalacja wymaganych bibliotek 

Funkcjonalność FreeCAD zależy od wielu zewnętrznych bibliotek. Mogą one być instalowane pojedynczo lub jako jedno ujednolicone polecenie.

Teraz zainstaluj następujące wymagane zależności za pomocą pacman:

-   mingw-w64-x86_64-opencascade
-   mingw-w64-x86_64-xerces-c
-   mingw-w64-x86_64-qt5
-   mingw-w64-x86_64-med
-   mingw-w64-x86_64-swig
-   mingw-w64-x86_64-qtwebkit
-   mingw-w64-x86_64-coin
-   mingw-w64-x86_64-python-pivy
-   mingw-w64-x86_64-python-ply
-   mingw-w64-x86_64-python-six
-   mingw-w64-x86_64-python-yaml
-   mingw-w64-x86_64-python-numpy
-   mingw-w64-x86_64-python-matplotlib
-   mingw-w64-x86_64-pyside2-qt5
-   mingw-w64-x86_64-python-markdown
-   mingw-w64-x86_64-python-pygit2

Poniżej znajduje się pojedyncze polecenie instalujące wszystko z powyższej listy:

    pacman -S mingw-w64-x86_64-opencascade mingw-w64-x86_64-xerces-c mingw-w64-x86_64-qt5 mingw-w64-x86_64-med mingw-w64-x86_64-swig mingw-w64-x86_64-qtwebkit mingw-w64-x86_64-coin mingw-w64-x86_64-python-pivy mingw-w64-x86_64-pyside2-qt5 mingw-w64-x86_64-python-ply mingw-w64-x86_64-python-six mingw-w64-x86_64-python-yaml mingw-w64-x86_64-python-numpy mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-markdown mingw-w64-x86_64-python-pygit2



### Kompilacja FreeCAD 

Utwórz katalog dla kompilacji: zwróć uwagę, że zazwyczaj nie jest to podkatalog katalogu źródłowego *(często przydatna jest możliwość niezależnego usunięcia katalogu źródłowego lub kompilacji)*.

    mkdir FreeCAD-build
    cd FreeCAD-build

Uruchom cMake:

    cmake ../FreeCAD

I wreszcie:

    cmake --build ./



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MinGW/pl
