# Compile on Linux/pl
**Istnieje eksperymentalny kontener FreeCAD Docker, który jest testowany pod kątem rozwoju FreeCAD. Przeczytaj więcej na ten temat na stronie [Kompilacja w Docker](Compile_on_Docker/pl.md)**


{{TOCright}}



## Informacje ogólne 

W ostatnich dystrybucjach Linuksa FreeCAD jest ogólnie łatwy do zbudowania, ponieważ wszystkie zależności są zwykle dostarczane przez menedżera pakietów. Zasadniczo obejmuje 3 kroki:

1.  Pobierz kod źródłowy FreeCAD.
2.  Pobierz zależności lub pakiety, od których zależy FreeCAD.
3.  Skonfiguruj za pomocą `cmake` i skompiluj za pomocą `make`.

Poniżej znajdziesz szczegółowe wyjaśnienia całego procesu, niektóre [skrypty do kompilacji](#Skrypty_automatycznej_kompilacji.md) oraz szczegóły, które możesz napotkać. Jeśli znajdziesz w poniższym tekście coś błędnego lub nieaktualnego *(dystrybucje Linuksa często się zmieniają)*, lub jeśli używasz dystrybucji, której nie ma na liście, przedyskutuj ten problem na [forum](https://forum.freecadweb.org/index.php) i pomóż nam go poprawić.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width:800px;">



*Ogólny proces kompilacji programu FreeCAD z kodu źródłowego. Zależności stron trzecich muszą znajdować się w systemie, podobnie jak sam kod źródłowy FreeCAD. CMake konfiguruje system tak, aby za pomocą jednej instrukcji make cały projekt został skompilowany.*



## Pobieranie kodu źródłowego 



### Git

Najlepszym sposobem uzyskania kodu jest sklonowanie repozytorium tylko do odczytu [Git](https://github.com/FreeCAD/FreeCAD). Do tego celu potrzebny jest program `git`, który można łatwo zainstalować w większości dystrybucji Linuksa. Można go również uzyskać z [oficjalnej strony](http://git-scm.com/).

Program Git można zainstalować za pomocą następującego polecenia:


{{Code|lang=bash|code=
sudo apt install git
}}

Poniższe polecenie umieści kopię najnowszej wersji kodu źródłowego programu FreeCAD w nowym katalogu o nazwie `freecad-source`.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

Więcej informacji na temat używania środowiska Git i wnoszenia kodu do projektu można znaleźć na stronie [Zarządzanie kodem źródłowym](Source_code_management/pl.md).



### Archiwum źródeł 

Alternatywnie można pobrać źródło w postaci [archiwów](https://github.com/FreeCAD/FreeCAD/releases/latest), pliku `.zip` lub `.tar.gz`, a następnie rozpakować je w wybranym katalogu.



## Pobranie zależności 

Aby skompilować FreeCAD musisz zainstalować wymagane zależności wymienione w dokumencie [biblioteki zewnętrzne](Third_Party_Libraries/pl.md). Pakiety, które zawierają te zależności są wymienione poniżej dla różnych dystrybucji Linuksa. Proszę zauważyć, że nazwy i dostępność bibliotek zależą od konkretnej dystrybucji; jeśli dystrybucja jest stara, niektóre pakiety mogą być niedostępne lub mieć inną nazwę. W takim przypadku należy zajrzeć do sekcji [starsze i niekonwencjonalne dystrybucje](Compile_on_Linux/pl#Dystrybucje_starsze_i_niekonwencjonalne.md) poniżej.

Gdy masz już zainstalowane wszystkie zależności, przejdź do sekcji [kompilacja programu](Compile_on_Linux/pl#Kompilacja_programu.md).

Należy pamiętać, że kod źródłowy programu FreeCAD ma rozmiar około 500 MB; może on być trzykrotnie większy, jeśli sklonujesz repozytorium Git z całą historią modyfikacji. Pobranie wszystkich zależności może wymagać pobrania 500 MB lub więcej nowych plików. Kiedy te pliki zostaną rozpakowane, mogą wymagać 1500 MB lub więcej miejsca. Należy również pamiętać, że proces kompilacji może wygenerować do 1500 MB dodatkowych plików, ponieważ system kopiuje i modyfikuje cały kod źródłowy. Dlatego przed przystąpieniem do kompilacji należy upewnić się, że na dysku twardym jest wystarczająco dużo wolnego miejsca, co najmniej 4 GB.


<div class="mw-collapsible mw-collapsed toccolours">



### Debian oraz Ubuntu 


<div class="mw-collapsible-content">

W systemach opartych na Debianie *(Ubuntu, Mint itd.)* dość łatwo jest zainstalować wszystkie potrzebne zależności. Większość bibliotek jest dostępna za pośrednictwem `apt` lub menedżera pakietów Synaptic.

Jeśli zainstalowałeś już FreeCAD z oficjalnych repozytoriów, możesz zainstalować jego zależności za pomocą tej jednej linijki kodu w terminalu:


```python
sudo apt build-dep freecad
```

Jednakże, jeśli wersja FreeCAD w repozytoriach jest stara, zależności mogą być niewłaściwe do skompilowania najnowszej wersji programu FreeCAD. Dlatego należy sprawdzić, czy zostały zainstalowane następujące pakiety.

Pakiety te są niezbędne do pomyślnego przeprowadzenia jakiejkolwiek kompilacji:

-    `build-essential`, instaluje kompilatory C i C++, biblioteki programistyczne C oraz program `make`.

-    `cmake`, niezbędne narzędzie do konfiguracji źródeł programu FreeCAD. Możesz również zainstalować `cmake-gui` i `cmake-curses-gui`, aby uzyskać opcję graficzną.

-    `libtool`, podstawowe narzędzia do tworzenia bibliotek współdzielonych.

-    `lsb-release`, standardowe narzędzie do raportowania bazy danych jest zwykle już zainstalowane w systemie Debian i pozwala na programowe rozróżnienie między czystą instalacją Debiana a jego odmianą, taką jak Ubuntu czy Linux Mint. Nie należy usuwać tego pakietu, ponieważ wiele innych pakietów systemowych może od niego zależeć.

Kompilacja programu FreeCAD wykorzystuje język Python, jest on także używany w czasie pracy jako język skryptowy. Jeśli używasz dystrybucji opartej na Debianie, interpreter Python jest zazwyczaj już zainstalowany.

-    `python3`
    

-    `swig`, narzędzie, które tworzy interfejsy między kodem C++ a Python.

Sprawdź, czy masz zainstalowany Python 3. Python 2 został wycofany z użycia w 2019 r, więc nowe środowiska w programie FreeCAD nie są testowane z tą wersją języka.

Konieczne jest zainstalowanie bibliotek Boost:

-    `libboost-dev`
    

-    `libboost-date-time-dev`
    

-    `libboost-filesystem-dev`
    

-    `libboost-graph-dev`
    

-    `libboost-iostreams-dev`
    

-    `libboost-program-options-dev`
    

-    `libboost-python-dev`
    

-    `libboost-regex-dev`
    

-    `libboost-serialization-dev`
    

-    `libboost-thread-dev`
    

Konieczne jest zainstalowanie bibliotek Coin:

-    `libcoin80-dev`, dla Debian Jessie, Stretch, Ubuntu 16.04 do 18.10, lub

-    `libcoin-dev`, dla Debiana Buster, Ubuntu 19.04 i nowszych, a także dla Ubuntu 18.04/18.10 z [freecad-stable/freecad-daily PPAs](Installing_on_Linux/pl#Wersja_stabilna_PPA.md) dodane do źródeł oprogramowania.

Kilka bibliotek zajmujących się matematyką, powierzchniami triangulowanymi, sortowaniem, siatkami, obrazowaniem komputerowym, projekcjami kartograficznymi, wizualizacją 3D, systemem okien X11, parsowaniem XML i odczytywaniem plików Zip:

-    `libeigen3-dev`
    

-    `libgts-bin`
    

-    `libgts-dev`
    

-    `libkdtree++-dev`
    

-    `libmedc-dev`
    

-    `libopencv-dev`or `libcv-dev`

-    `libproj-dev`
    

-    `libvtk7-dev`or `libvtk6-dev`

-    `libx11-dev`
    

-    `libxerces-c-dev`
    

-    `libzipios++-dev`
    


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">



### Python 2 oraz Qt4 

Nie jest to zalecane w przypadku nowszych instalacji, ponieważ zarówno Python 2, jak i Qt4 są przestarzałe. Od wersji 0.20 FreeCAD nie obsługuje ich już.


<div class="mw-collapsible-content">

Aby skompilować FreeCAD dla Debiana Jessie, Stretch, Ubuntu 16.04, używając Pythona 2 i Qt4, należy zainstalować następujące zależności.

-    `qt4-dev-tools`
    

-    `libqt4-dev`
    

-    `libqt4-opengl-dev`
    

-    `libqtwebkit-dev`
    

-    `libshiboken-dev`
    

-    `libpyside-dev`
    

-    `pyside-tools`
    

-    `python-dev`
    

-    `python-matplotlib`
    

-    `python-pivy`
    

-    `python-ply`
    

-    `python-pyside`
    


</div>


</div>



### Python 3 oraz Qt5 

Aby skompilować FreeCAD dla Debiana Buster, Ubuntu 19.04 i nowszych oraz Ubuntu 18.04/18.10 z [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) dodanymi do źródeł oprogramowania, zainstaluj następujące zależności.

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `qtwebengine5-dev`
    

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

-    `python3-packaging`
    

-    `python3-pivy`
    

-    `python3-ply`
    

-    `python3-pyside2.qtcore`
    

-    `python3-pyside2.qtgui`
    

-    `python3-pyside2.qtsvg`
    

-    `python3-pyside2.qtwidgets`
    

-    `python3-pyside2.qtnetwork`
    

-    `python3-pyside2.qtwebengine`
    

-    `python3-pyside2.qtwebenginecore`
    

-    `python3-pyside2.qtwebenginewidgets`
    

-    `python3-pyside2.qtwebchannel`
    

-    `python3-pyside2uic`
    



#### kernel OpenCascade 

Jądro OpenCascade jest podstawową biblioteką graficzną służącą do tworzenia kształtów 3D. Istnieje w wersji oficjalnej OCCT oraz w wersji społecznościowej OCE. Wersja społecznościowa nie jest już zalecana, ponieważ jest przestarzała.

W przypadku Debiana Buster i Ubuntu 18.10 i nowszych, a także Ubuntu 18.04 z [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) dodanymi do źródeł oprogramowania, należy zainstalować oficjalne pakiety.

-    `libocct*-dev`-   
        `libocct-data-exchange-dev`
        

    -   
        `libocct-draw-dev`
        

    -   
        `libocct-foundation-dev`
        

    -   
        `libocct-modeling-algorithms-dev`
        

    -   
        `libocct-modeling-data-dev`
        

    -   
        `libocct-ocaf-dev`
        

    -   
        `libocct-visualization-dev`
        

-    `occt-draw`
    

W przypadku Debiana Jessie, Stretch, Ubuntu 16.04 i nowszych należy zainstalować pakiety edycji społecznościowej.

-    `liboce*-dev`-   
        `liboce-foundation-dev`
        

    -   
        `liboce-modeling-dev`
        

    -   
        `liboce-ocaf-dev`
        

    -   
        `liboce-ocaf-lite-dev`
        

    -   
        `liboce-visualization-dev`
        

-    `oce-draw`
    

Biblioteki można instalować pojedynczo lub przy użyciu rozszerzenia asterisk. Zmień `occ` na `oce`, jeśli chcesz zainstalować biblioteki społecznościowe.


```python
sudo apt install libocct*-dev
```



#### Pakiety opcjonalne 

Opcjonalnie można również zainstalować te dodatkowe pakiety:

-    `libsimage-dev`, aby Coin obsługiwał dodatkowe formaty plików graficznych.

-    `doxygen`i `libcoin-doc` *(lub `libcoin80-doc` dla starszych systemów)*, jeśli chcesz generować dokumentację kodu źródłowego.

-    `libspnav-dev`, dla obsługi [maniopulatorów przestrzennych](3D_input_devices/pl.md), takich jak \"Space Navigator\" lub \"Space Pilot\" firmy 3Dconnexion.

-    `checkinstall`, jeśli chcesz zarejestrować zainstalowane pliki w systemowym menedżerze pakietów, aby móc je później odinstalować.

-    `python3-markdown`, aby Menadżer dodatków wyświetlał natywnie pliki README.md w formacie Markdown.

-    `python3-git`, aby Menadżer dodatków używał repozytorium Git do pobierania i aktualizowania środowisk pracy i makrodefinicji.



#### Pojedyncze polecenie dla środowisk Python 3 i Qt5 

Wymaga Pyside2 dostępnego w Debian buster oraz [freecad-stable/freecad-daily PPA](Installing_on_Linux/pl#Wersja_stabilna_PPA.md).


{{Code|lang=bash|code=
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev qtwebengine5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-packaging python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig
}}

UWAGA: W niektórych wersjach Ubuntu i niektórych wersjach Qt pojawi się błąd, że nie udało się znaleźć pakietu python3-pyside2uic - w tych systemach można go bezpiecznie pominąć. W Ubuntu 20.04 trzeba będzie dodać `pyqt5-dev-tools`. Więcej informacji można znaleźć na stronie [this dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">



#### Pojedyncze polecenie dla środowisk Python 2 i Qt4 

Nie jest to zalecane w przypadku nowszych instalacji, ponieważ zarówno Python 2, jak i Qt4 są przestarzałe.


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
}}

Użytkowników Ubuntu 16.04 prosimy o zapoznanie się również z dyskusją na temat kompilacji na forum: [Compile on Linux (Kubuntu): CMake can\'t find VTK](http://forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Raspberry Pi 


<div class="mw-collapsible-content">

Wykonaj te same kroki, co w przypadku dystrybucji Debian i Ubuntu.

Zgłaszane są problemy podczas próby kompilacji w systemie v przy użyciu Pythona 3 i Qt5, ale kombinacja Pythona 3 i Qt4 wydaje się działać ze starszymi wersjami programu FreeCAD *(z drobnymi problemami)*.

W przypadku nowszych wersji *(od 0.20)* programu FreeCAD kompilacja z Py3/Qt5 powiedzie się, jeśli zainstalowanym systemem operacyjnym jest Raspberry Pi OS 64-bit lub Ubuntu 20.04.

Z powodu różnych problemów z Qt, w Ubuntu 20.04 nie będzie można znaleźć normalnych narzędzi PySide. {{Code|lang=bash|code=
E: Unable to locate package python3-pyside2uic
}}

W tym przypadku możemy zainstalować pakiety z PyQt i utworzyć dowiązania symboliczne do potrzebnych narzędzi. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Teraz można przystąpić do kompilacji. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

Opcja `-j` w poleceniu `make` nie powinna mieć parametru powyżej 3, ponieważ Raspberry Pi ma ograniczoną pamięć. Kompilacja zajmie kilka godzin, więc lepiej zrobić to w nocy.

Więcej informacji, [FreeCAD i Raspberry Pi 4](https://forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Fedora


<div class="mw-collapsible-content">

W cmake dystrybuowanym przez Fedorę 34/35 jest błąd, który powoduje, że cmake nie znajduje bibliotek opencascade. Można to łatwo naprawić, wprowadzając jedną drobną zmianę do głównego poziomu pliku cmake programu opencascade zainstalowanego na Fedorze. Szczegóły tutaj: <https://bugzilla.redhat.com/show_bug.cgi?id=2083568>.

W górnej części pliku **OpenCASCADEConfig.cmake** zmień następujący wiersz, aby użyć {{Incode|REAL_PATH()}}. Usuwa to błąd wprowadzony przez użycie linka symbolicznego z {{Incode|/lib}} do {{Incode|/usr/lib}} w Fedorze, co powodowało błąd w cmake.

Ten plik jest zwykle instalowany w **/usr/lib64/cmake/opencascade/OpenCASCADEConfig.cmake**.


{{Code|lang=bash|code=
get_filename_component (OpenCASCADE_INSTALL_PREFIX "${OpenCASCADE_INSTALL_PREFIX}" PATH)
}}

zmień to na:


{{Code|lang=bash|code=
file (REAL_PATH ${OpenCASCADE_INSTALL_PREFIX} OpenCASCADE_INSTALL_PREFIX)
}}

Tę trywialną zmianę należy wprowadzić w katalogu kompilacji po uruchomieniu cmake i niepowodzeniu. Ponowne uruchomienie cmake spowoduje prawidłowe wykrycie bibliotek OCCT w normalny sposób.

Potrzebne są następujące pakiety:

-   gcc-c++ (or possibly another C++ compiler?)
-   cmake
-   doxygen
-   swig
-   gettext
-   dos2unix
-   desktop-file-utils
-   libXmu-devel
-   freeimage-devel
-   mesa-libGLU-devel
-   opencascade-devel
-   openmpi-devel
-   python3
-   python3-devel
-   python3-pyside2
-   python3-pyside2-devel
-   pyside2-tools
-   boost-devel
-   tbb-devel
-   eigen3-devel
-   qt-devel
-   qt5-qtwebengine-devel
-   qt5-qtxmlpatterns
-   qt5-qtxmlpatterns-devel
-   qt5-qtsvg-devel
-   qt5-qttools-static
-   ode-devel
-   xerces-c
-   xerces-c-devel
-   opencv-devel
-   smesh-devel
-   Coin3
-   Coin3-devel

*(kwiecień 2021, Coin4 i Coin4-devel są dostępne)* *(jeśli coin2 jest najnowszą dostępną wersją dla twojej wersji Fedory, użyj pakietów z <http://www.zultron.com/rpm-repo/>)*

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk
-   vtk-devel
-   med
-   med-devel

I opcjonalnie:

-   libspnav-devel *(do obsługi urządzeń 3Dconnexion, takich jak Space Navigator czy Space Pilot)*,
-   python3-pivy *(https://bugzilla.redhat.com/show_bug.cgi?id=458975 Pivy nie jest obowiązkowy, ale jest wymagany dla środowiska Rysunek Roboczy)*,
-   python3-markdown *(aby Menadżer dodatków natywny markdown)*,
-   python3-GitPython *(aby Menadżer dodatków używał repozytorium Git do sprawdzania i aktualizowania środowisk pracy i makrodefinicji)*.


<div class="mw-translate-fuzzy">

Aby zainstalować wszystkie zależności naraz *(testowane w systemie Fedorze 36)*:


</div>


{{Code|lang=bash|code=
sudo dnf install gcc-c++ cmake doxygen swig gettext dos2unix desktop-file-utils libXmu-devel freeimage-devel mesa-libGLU-devel opencascade-devel openmpi-devel python3 python3-devel python3-pyside2 python3-pyside2-devel pyside2-tools boost-devel tbb-devel eigen3-devel qt-devel qt5-qtwebengine-devel qt5-qtxmlpatterns qt5-qtxmlpatterns-devel qt5-qtsvg-devel qt5-qttools-static ode-devel xerces-c xerces-c-devel opencv-devel smesh-devel Coin3 Coin3-devel SoQt-devel freetype freetype-devel vtk vtk-devel med med-devel libspnav-devel python3-pivy python3-markdown python3-GitPython
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Gentoo


<div class="mw-collapsible-content">

Najprostszym sposobem sprawdzenia, które pakiety są potrzebne do skompilowania programu FreeCAD, jest sprawdzenie ich przez portage:

emerge -pv freecad

Powinno to spowodować wyświetlenie listy dodatkowych pakietów, które należy zainstalować w systemie.

Gdy FreeCAD nie jest dostępny przez portage, jest dostępny na repozytorium [waebbl overlay](https://github.com/waebbl/waebbl-gentoo). Narzędzie do śledzenia problemów na nakładce waebbl Github może pomóc w rozwiązaniu niektórych z nich. Nakładka zapewnia szeroki licznik freecad-9999, dzięki temu możesz wybrać potrzebny numer do skompilowania lub po prostu użyć do pobrania zależności.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### openSUSE


<div class="mw-collapsible-content">



#### Tumbleweed

Następujące polecenia zainstalują pakiety wymagane do zbudowania FreeCAD z Qt5 i środowiskiem Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

Następujące polecenie zainstaluje program Qt Creator i GNU Project Debugger.


```pythonzypper in libqt5-creator gdb```

Jeśli brakuje jakichś pakietów, można sprawdzić plik Tumbleweed [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec) na stronie [Open Build Service](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD).

Należy również sprawdzić, czy nie ma jakichś poprawek, które należy zastosować (np. [0001-find-openmpi2-include-files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).



#### Leap

Jeśli istnieje różnica między pakietami dostępnymi w programach Tumbleweed i Leap, można przeczytać plik [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec) programu Leap w [Open Build Service](https://build.opensuse.org/), aby określić wymagane pakiety.

Zobacz poradnik [piano_jonas unnofficial \"Compile On openSUSE\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Arch Linux 


<div class="mw-collapsible-content">

Potrzebne będą następujące biblioteki z oficjalnych repozytoriów:

-   boost
-   curl
-   desktop-file-utils
-   glew
-   hicolor-icon-theme
-   jsoncpp
-   libspnav
-   opencascade
-   shiboken2
-   xerces-c
-   pyside2
-   python-matplotlib
-   python-netcdf4
-   python-packaging
-   qt5-svg
-   qt5-webengine
-   cmake
-   eigen
-   git
-   gcc-fortran
-   pyside2-tools
-   swig
-   qt5-tools
-   shared-mime-info
-   coin
-   python-pivy
-   med


```python
sudo pacman -S boost curl desktop-file-utils glew hicolor-icon-theme jsoncpp libspnav opencascade shiboken2 xerces-c pyside2 python-matplotlib python-netcdf4 python-packaging qt5-svg qt5-webengine cmake eigen git gcc-fortran pyside2-tools swig qt5-tools shared-mime-info coin python-pivy med
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Dystrybucje starsze i niekonwencjonalne 


<div class="mw-collapsible-content">

Dla innych dystrybucji mamy bardzo mało informacji zwrotnych od użytkowników, więc znalezienie potrzebnych pakietów może być trudniejsze.

Spróbuj najpierw znaleźć wymagane biblioteki wymienione w [bibliotekach zewnętrznych](Third_Party_Libraries/pl.md) w swoim menedżerze pakietów. Zwróć uwagę, że niektóre z nich mogą mieć nieco inną nazwę pakietu. Szukaj według `name`, ale także `libname`, `name-dev`, `name-devel` i podobnych. Jeśli to nie jest możliwe, spróbuj skompilować te biblioteki samodzielnie.

FreeCAD wymaga kompilatora GNU g++ w wersji nie mniejszej niż 3.0.0, ponieważ FreeCAD jest napisany głównie w języku C++. Podczas kompilacji wykonywane są niektóre skrypty Pythona, więc interpreter Python musi działać prawidłowo. Aby uniknąć problemów z linkerem, dobrze jest umieścić ścieżki dostępu do bibliotek w zmiennej `LD_LIBRARY_PATH` lub w pliku `ld.so.conf`. W nowoczesnych dystrybucjach Linuksa jest to już zrobione, ale w starszych może być konieczne ustawienie tej zmiennej


</div>


</div>



### Pivy

[Pivy](Pivy/pl.md) *(pakiet Pythona do Coin3d)* nie jest potrzebny do zbudowania programu FreeCAD ani do jego uruchomienia, ale jest wymagany jako zależność runtime przez [Rysunek Roboczy](Draft_Workbench/pl.md). Jeśli nie zamierzasz używać tego środowiska pracy, nie będziesz potrzebował Pivy. Należy jednak pamiętać, że środowisko pracy Rysunek Roboczy jest używane wewnętrznie przez inne środowiska pracy, takie jak [Architektura](Arch_Workbench/pl.md) i [BIM](BIM_Workbench/pl.md), więc Pivy jest wymagane do korzystania z tych narzędzi.

W listopadzie 2015 roku przestarzała wersja Pivy dołączona do kodu źródłowego FreeCAD nie będzie już kompilowana na wielu systemach. Nie jest to duży problem, ponieważ zazwyczaj powinieneś pobrać Pivy z menedżera pakietów swojej dystrybucji; jeśli nie możesz znaleźć Pivy, być może będziesz musiał skompilować go samodzielnie, zobacz [Instrukcje kompilacji Pivy](Extra_python_modules/pl#Pivy.md).



### Symbole debugowania 

W celu rozwiązywania problemów z awariami w programie FreeCAD, warto wprowadzić symbole debugowania ważnych bibliotek zależnych, takich jak Qt. W tym celu spróbuj zainstalować pakiety zależności, których nazwy kończą się na `-dbg`, `-dbgsym`, `-debuginfo` lub podobne, w zależności od dystrybucji Linuksa.

Dla Ubuntu, może być konieczne włączenie specjalnych repozytoriów, aby móc zobaczyć i zainstalować te pakiety debugowania za pomocą menedżera pakietów. Zapoznaj się ze stroną [Debug Symbol Packages](https://wiki.ubuntu.com/Debug_Symbol_Packages), aby uzyskać więcej informacji.



## Kompilacja programu 


**Kompilacja z użyciem środowiska Python 2 i Qt4 nie jest już dobrze wspierana, a od wersji 0.20 nie jest już w ogóle wspierana. Powinieneś przeprowadzić kompilację w środowisku Python 3 i Qt5. Wersja 0.20 wymaga środowiska Python w wersji co najmniej 3.6 i Qt w wersji 5.9.**

FreeCAD używa CMake jako głównego systemu kompilacji, ponieważ jest on dostępny we wszystkich głównych systemach operacyjnych. Kompilacja za pomocą CMake jest zazwyczaj bardzo prosta i przebiega w dwóch krokach.

1.  CMake sprawdza, czy wszystkie potrzebne programy i biblioteki są obecne w systemie, a następnie generuje plik `Makefile`, który jest skonfigurowany do drugiego kroku. FreeCAD ma kilka opcji konfiguracyjnych do wyboru, ale posiada rozsądne ustawienia domyślne. Poniżej opisano kilka alternatywnych rozwiązań.
2.  Sama kompilacja, która jest wykonywana przez program `make`, który generuje pliki wykonywalne programu FreeCAD.

Ponieważ FreeCAD jest dużą aplikacją, kompilacja całego kodu źródłowego może zająć od 10 minut do godziny, w zależności od wydajności Twojego procesora i liczby rdzeni procesora użytych do kompilacji.

Kod można budować zarówno w katalogu źródłowym, jak i poza nim. Generalnie najlepszym rozwiązaniem jest budowanie poza katalogiem źródłowym.



### Kompilacja poza źródłami 

Budowanie w osobnym folderze jest wygodniejsze niż budowanie w tym samym katalogu, w którym znajduje się kod źródłowy, ponieważ za każdym razem, gdy aktualizujesz kod źródłowy, CMake może inteligentnie określić, które pliki uległy zmianie, i przekompilować tylko to, co jest potrzebne. Jest to bardzo przydatne podczas testowania różnych gałęzi Git, ponieważ nie trzeba dezorientować systemu kompilacji.

Aby budować poza źródłem, po prostu utwórz katalog budowania, `freecad-build`, oddzielny od folderu źródłowego FreeCAD, `freecad-source`. Następnie z tego katalogu wskaż `cmake` właściwy folder źródłowy. W poniższych instrukcjach możesz również użyć `cmake-gui` lub `ccmake` zamiast `cmake`. Gdy `cmake` zakończy konfigurowanie środowiska, użyj `make`, aby rozpocząć właściwą kompilację.


{{Code|lang=bash|code=
mkdir freecad-build
cd freecad-build
cmake ../freecad-source
make -j$(nproc --ignore=2)
}}

Uwaga: jeśli kompilujesz gałąź wydania 0.19, musisz jawnie określić, że kompilujesz z użyciem pakietów Qt5 i Python 3 \-- zamień powyższe polecenie cMake na: {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

Opcja `-j` programu `make` kontroluje, ile zadań (plików) jest kompilowanych równolegle. Program `nproc` wypisuje liczbę rdzeni procesora w twoim systemie. Używając go razem z opcją `-j` możesz wybrać przetwarzanie tylu plików, ile masz rdzeni, aby przyspieszyć ogólną kompilację programu. W powyższym przykładzie, użyje on wszystkich rdzeni w systemie z wyjątkiem dwóch. Dzięki temu Twój komputer będzie mógł być wykorzystany do innych celów, podczas gdy kompilacja będzie przebiegać w tle. Plik wykonywalny programu FreeCAD pojawi się ostatecznie w katalogu `freecad-build/bin`. Zobacz także stronę [Kompilacja *(przyspieszamy)*](Compiling_(Speeding_up)/pl.md), aby poprawić szybkość kompilacji.



### Rozwiązywanie problemów z cmake 

Jeśli już wcześniej wykonałeś kompilację poza źródłem i utknąłeś na zależności, która nie została rozpoznana lub nie można jej rozwiązać, spróbuj wykonać następujące czynności:

-   Usuń zawartość katalogu kompilacji przed ponownym uruchomieniem cmake. FreeCAD jest szybko zmieniającym się celem, możesz natknąć się na zbuforowane informacje cmake, które wskazują na starszą wersję niż ta, której może użyć nowy serwer repozytorium. Wyczyszczenie pamięci podręcznej może pozwolić cmake odzyskać i rozpoznać wersję, której rzeczywiście potrzebujesz.

-   Jeśli `cmake` skarży się na brak konkretnego pliku, użyj narzędzia takiego jak `apt-file search` lub jego odpowiednika w innych systemach pakietów, aby dowiedzieć się, do jakiego pakietu należy ten plik i zainstalować go. Pamiętaj, że prawdopodobnie będziesz potrzebował wersji `-dev` pakietu, która zawiera pliki nagłówkowe lub konfiguracyjne wymagane do korzystania z pakietu przez FreeCAD.



### Kompilacja z GNU libc 2.34 i nowszymi 

GNU libc 2.34 wprowadza zmianę w bibliotece, która może spowodować, że kompilacja w niektórych systemach Linux nie powiedzie się powodując następujący błąd:


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

Aby temu zaradzić, należy ręcznie utworzyć dowiązanie symboliczne z *(pustego teraz)* systemowego libdl.so.\* do miejsca, w którym kompilator mówi, że szuka tego pliku. Na przykład (jeśli faktycznie zainstalowaną kopią libdl.so w systemie jest /usr/lib/x86_64-linux-gnu/libdl.so.2):


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Dostosuj to polecenie do struktury swojego systemu, wyszukując libdl.so\* i umieszczając je w odpowiedniej lokalizacji.



### Kompilacja na bazie źródeł 

Kompilacje źródłowe są dobre, jeśli chcesz szybko skompilować wersję FreeCAD i nie zamierzasz często aktualizować kodu źródłowego. W takim przypadku możesz usunąć skompilowany program i źródło, usuwając tylko jeden folder.

Zmień katalog na źródłowy i wskaż `cmake` na obecny katalog *(oznaczony pojedynczym punktem)*:


{{Code|lang=bash|code=
cd freecad-source
cmake . -DPYTHON_EXECUTABLE=/usr/bin/python3
make -j$(nproc --ignore=2)
}}

Plik wykonywalny programu FreeCAD będzie wtedy znajdował się w katalogu `freecad-source/bin`.



### Jak naprawić swój katalog z kodem źródłowym 

Jeśli przypadkowo wykonałeś kompilację wewnątrz katalogu z kodem źródłowym lub dodałeś niepotrzebne pliki i chcesz przywrócić jego zawartość tylko do oryginalnego kodu źródłowego, możesz wykonać następujące czynności.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

Pierwszy wiersz usuwa zawartość pliku `.gitignore`. Zapewnia to, że kolejne polecenia clean i reset będą dotyczyły wszystkiego w katalogu i nie będą ignorowały elementów pasujących do wyrażeń z `.gitignore`. Druga linia usuwa wszystkie pliki i katalogi, które nie są śledzone przez repozytorium git. Następnie ostatnia komenda resetuje wszelkie zmiany w śledzonych plikach, w tym pierwszą komendę, która wyczyściła plik `.gitignore`.

Jeśli nie wyczyścisz katalogu źródłowego, kolejne uruchomienia `cmake` mogą nie wychwycić nowych opcji systemu, jeśli kod ulegnie zmianie.



### Konfiguracja

Przekazując różne opcje do `cmake`, możesz zmienić sposób, w jaki FreeCAD jest kompilowany. Składnia jest następująca.


```python
cmake -D <var>:<type>=<value> $SOURCE_DIR
```

Gdzie `$SOURCE_DIR` jest katalogiem zawierającym kod źródłowy. Opcję `<type>` można w większości przypadków pominąć. Można też pominąć spację po opcji `-D`.

Na przykład, aby uniknąć kompilacji środowiska [MES](FEM_Workbench/pl.md):


{{Code|lang=bash|code=
cmake -D BUILD_FEM:BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

Wszystkie możliwe zmienne są wymienione w pliku `InitializeFreeCADBuildOptions.cmake`, znajdującym się w katalogu `cMake/FreeCAD_Helpers`. W pliku tym należy wyszukać słowo `option`, aby przejść do zmiennych, które można ustawić, i przejrzeć ich wartości domyślne.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Alternatywnie można użyć polecenia `cmake -LH`, aby wyświetlić listę bieżącej konfiguracji, a więc wszystkich zmiennych, które można zmienić. Można również zainstalować i użyć `cmake-gui`, aby uruchomić interfejs graficzny pokazujący wszystkie zmienne, które można modyfikować. W następnych sekcjach wymienimy niektóre z ważniejszych opcji, których możesz chcieć użyć.



#### Dla debugowania kompilacji 

Utwórz kompilację `Debug` do rozwiązywania problemów z awariami w programie FreeCAD. Zwróć uwagę, że w tej wersji kompilacji środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) przy złożonych szkicach staje się bardzo powolne.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}



#### Dla kompilacji Wydania 

Utwórz kompilację `Release`, aby przetestować kod, który nie ulega awarii. Kompilacja `Release` będzie działać znacznie szybciej niż kompilacja `Debug`.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}



#### Kompilacja w oparciu o Python 3 i Qt5 

Wsparcie dla środowiska Python 2 i Qt4 zostało wycofane w FreeCAD 0.20 i nie jest konieczne wyraźne włączenie Qt5 i Python 3, jeśli kompilujemy najnowsze wersje. Obsługa Qt6 jest obecnie w fazie rozwoju i jeszcze nie działa. Jeśli nie planujesz pomagać w migracji Qt6, parametr FREECAD_QT_VERSION powinien być ustawiony na wartość \"Auto\" *(domyślnie)* lub jawnie na \"5\".

dla wersji 0.20_dev oraz 0.21_dev: {{Code|lang=bash|code=
cmake ../freecad-source
}}

Należy pamiętać, że przy przechodzeniu między kompilacją 0.20 i 0.21_dev może być konieczne usunięcie pliku CMakeCache.txt przed uruchomieniem cmake.



#### Kompilacja dla określonej wersji Pythona 

Jeśli domyślny plik wykonywalny `python` w Twoim systemie jest dowiązaniem symbolicznym do Pythona 2, `cmake` będzie próbował skonfigurować FreeCAD dla tej wersji. Musisz wybrać inną wersję środowiska Python, podając ścieżkę do konkretnego pliku wykonywalnego:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Jeśli to nie zadziała, być może trzeba będzie zdefiniować dodatkowe zmienne wskazujące na żądane biblioteki Python i katalogi include:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

Możliwe jest posiadanie kilku niezależnych wersji Python w tym samym systemie, dlatego lokalizacja i numery wersji plików Python będą zależały od konkretnej dystrybucji Linuksa. Użyj `python3 -V`, aby wyświetlić wersję Python, której aktualnie używasz. Istotne są tylko dwie pierwsze liczby. Na przykład, jeśli wynikiem jest `Python 3.6.8`, musisz podać katalogi, które odnoszą się do wersji 3.6. Jeśli nie znasz odpowiednich katalogów, spróbuj poszukać ich za pomocą polecenia `locate`.


```python
locate python3.6
```

Możesz użyć `python3 -m site` w terminalu, aby określić katalog `site-packages` lub `dist-packages` dla systemów Debian.

Niektóre komponenty FreeCAD, takie jak PySide, próbują automatycznie wykryć najnowszą wersję Pythona zainstalowaną w systemie, co może się nie udać, jeśli jest ona inna niż podana powyżej. Dodanie następującej opcji cMake może rozwiązać ten problem:


{{Code|lang=bash|code=
-DPython3_FIND_STRATEGY=LOCATION
}}



#### Kompilacja za pomocą Qt Creator + Python 3 i Qt5 

1\. Uruchom Qt Creator.

2\. Kliknij przycisk **Otwórz Projekt**.

3\. Przejdź do katalogu, w którym znajduje się kod źródłowy, `freecad-source/`, i wybierz najwyżej położony plik `CMakeLists.txt`.

4\. Wybranie pliku spowoduje automatyczne uruchomienie na nim programu `cmake`, ale może się to nie powieść, jeśli odpowiednie opcje nie zostaną poprawnie ustawione.

5\. Przejdź do **Projects → Build & Run → Imported Kit → Build → Build Settings → CMake**. Ustaw odpowiedni katalog kompilacji, `freecad-build/`.

6\. Ustaw odpowiednie zmienne w oknie dialogowym Key-Value, typu `String` i `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
```

7\. Jeżeli zmienne nie załadują projektu poprawnie, być może będziesz musiał przejść do **Projects → Manage Kits → Kits → Default (lub Imported Kit lub podobne) → CMake Configuration**. Następnie naciśnij przycisk **Change** i dodaj odpowiednią konfigurację, jak opisano powyżej. Być może trzeba będzie dodać więcej zmiennych dotyczących ścieżek dla środowiska Python, jeśli systemowy Python nie zostanie znaleziony. 
```python
PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
```

7.1. Naciśnij przycisk **Apply**, a następnie **OK**.

7.2. Upewnij się, że pozostałe opcje są prawidłowo ustawione, na przykład **Qt version** powinno być aktualną wersją zainstalowaną w systemie, taką jak `Qt 5.9.5 w PATH (qt5)`.

Naciśnij **Apply**, a następnie **OK**, aby zamknąć konfigurację.

Program `cmake` powinien ponownie uruchomić się automatycznie i wypełnić całe okno dialogowe Key-Value wszystkimi zmiennymi, które można skonfigurować.

8\. Przejdź do **Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration** i wybierz `FreeCADMain`, aby skompilować graficzną wersję FreeCAD, lub `FreeCADMainCMD`, aby skompilować wersję wiersza poleceń.

9\. Na koniec przejdź do menu **Build → Build Project "FreeCAD"**. Jeśli jest to nowa kompilacja, powinna ona potrwać kilka minut, a nawet godzin, w zależności od liczby dostępnych procesorów.



#### Wtyczka Qt designer 

Jeśli chcesz opracować kod Qt dla programu FreeCAD, będziesz potrzebował wtyczki Qt Designer, która zapewnia wszystkie niestandardowe widżety programu FreeCAD.

Przejdź do katalogu pomocniczego z kodem źródłowym, uruchom `qmake` ze wskazanym plikiem projektu, aby utworzyć plik `Makefile`. Mastępnie uruchom `make`, aby skompilować wtyczkę.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Jeśli kompilujesz dla Qt5, upewnij się, że binarka `qmake` jest tą dla tej wersji, aby wynikowy plik `Makefile` zawierał niezbędne informacje dla Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

gdzie `$QT_DIR` to katalog, w którym przechowywane są biblioteki binarne Qt, na przykład `/usr/lib/x86_64-linux-gnu/qt5`.

Utworzona biblioteka to `libFreeCAD_widgets.so`, którą należy skopiować do `$QT_DIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}



#### Pivy zewnętrzne lub wewnętrzne 

Wcześniej wersja Pivy była zawarta w kodzie źródłowym FreeCAD *(wewnętrznym)*. Jeśli chcesz użyć systemowej kopii Pivy *(zewnętrznej)*, musisz użyć -DFREECAD_USE_EXTERNAL_PIVY=1.

Użycie zewnętrznego Pivy stało się domyślne podczas tworzenia FreeCAD 0.16, dlatego tej opcji nie trzeba już ustawiać samodzielnie.



#### Dokumentacja Doxygen 

Jeśli masz zainstalowany program Doxygen, możesz zbudować dokumentację kodu źródłowego. Przeczytaj stronę [dokumentacja dla źródeł](Source_documentation/pl.md), aby uzyskać instrukcje.



### Dokumentacja dodatkowa 

Kod źródłowy programu FreeCAD jest bardzo obszerny, a za pomocą CMake można skonfigurować wiele opcji. Nauczenie się pełnego wykorzystania CMake może być przydatne do wybrania odpowiednich opcji dla twoich szczególnych potrzeb.

-   [CMake Reference Documentation](https://cmake.org/documentation/) autorstwa Kitware.
-   [How to Build a CMake-Based Project](https://preshing.com/20170511/how-to-build-a-cmake-based-project/) *(blog)* autorstwa Preshinga na temat programowania.
-   [Learn CMake\'s Scripting Language in 15 Minutes](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) *(blog)* autorstwa Preshinga na temat programowania.



### Tworzenie paczki Debian 

Jeśli planujesz zbudować pakiet systemu Debian ze źródeł, musisz najpierw zainstalować wybrane pakiety:


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Przejdź do katalogu FreeCAD i wywołaj


{{Code|lang=bash|code=
debuild
}}

Po zbudowaniu pakietu można użyć polecenia `lintian`, aby sprawdzić, czy pakiet zawiera błędy


{{Code|lang=bash|code=
lintian freecad-package.deb
}}



#### Pakiety \*.deb z checkinstall 

Skrypt Debiana `checkinstall` pozwala na stworzenie pakietu \*.deb, który może być zainstalowany i usunięty za pomocą standardowych poleceń `dpkg`. Może wymagać wcześniejszej instalacji *(na Ubuntu użyj `sudo apt install checkinstall`)*. Jest on interaktywny i pyta o wymagane informacje podając użyteczne domyślne ustawienia. W trakcie procesu pakiet jest instalowany i tworzony jest plik \*.deb oraz archiwum zapasowe.

Dobrym pomysłem jest zdefiniowanie nazwy i krótkiego opisu dla pakietu. Nazwa musi być wpisana, aby ponownie go odinstalować, a opis będzie wyszczególniony przez `dpkg -l`. Domyślna użyta nazwa \"build\" nie jest zbyt informacyjna.

Przykład:


{{Code|lang=bash|code=
cd freecad-source/freecad-build
cmake ..
make
sudo checkinstall                                  # e.g. name=freecad-test1
}}

Wynikiem jest plik \*.deb w folderze freecad-build. Skrypt `checkinstall` domyślnie zainstaluje ten build. W ten sposób można go zainstalować lub odinstalować:


{{Code|lang=bash|code=
cd freecad-source/freecad-build
 ls <nowiki>|</nowiki>grep freecad
        freecad-test1_20220814-1_amd64.deb
 sudo dpkg -i freecad-test1_20220814-1_amd64.deb   # install
 dkpg -l <nowiki>|</nowiki>grep freecad                             # find by name
 sudo dpkg -r freecad-test1                        # uninstall by name
}}



## Aktualizacja kodu źródłowego 

System CMake pozwala na inteligentne aktualizowanie kodu źródłowego i rekompilowanie tylko tego, co uległo zmianie, dzięki czemu kolejne kompilacje przebiegają szybciej.

Przejdź do lokalizacji, w której po raz pierwszy został pobrany kod źródłowy programu FreeCAD, i pobierz nowy kod:


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Następnie należy przejść do katalogu build, w którym kod został pierwotnie skompilowany, i uruchomić `cmake`, podając obecny katalog *(oznaczony kropką)*. Po czym wywołać ponowną kompilację za pomocą `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}



## Odinstalowanie kodu źródłowego 

W przypadku, gdy skompilowany kod źródłowy został zainstalowany za pomocą polecenia `sudo make install` *(dla dystrybucji Debian)* pliki zostały skopiowane do folderu **/usr/local** w kilku podfolderach. Do deinstalacji można użyć pliku **install_manifest.txt**. Został on utworzony w folderze build podczas kompilacji i zawiera wszystkie zainstalowane pliki. Tak długo jak ten plik istnieje, pakiet może zostać odinstalowany.


{{Code|lang=bash|code=
cd freecad-source/freecad-build
xargs sudo rm < install_manifest.txt
}}



## Rozwiązywanie problemów 



### W systemach 64bit 

Podczas kompilacji programu FreeCAD dla 64-bitów występuje znany problem z 64-bitowym pakietem OpenCASCADE (OCCT). Aby FreeCAD działał poprawnie, może być konieczne uruchomienie skryptu `configure` i ustawienie dodatkowych `CXXFLAGS`:


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

W systemach opartych na Debianie opcja ta nie jest potrzebna, gdy używamy gotowych pakietów OpenCASCADE, ponieważ te ustawiają wewnętrznie właściwe `CXXFLAGS`.



## Skrypty automatycznej kompilacji 

Tutaj znajdziesz wszystko, czego potrzebujesz, aby zbudować kompletny program FreeCAD. Jest to podejście oparte na jednym skrypcie i działa na świeżo zainstalowanej dystrybucji Linuksa. Polecenia poproszą o podanie hasła roota w celu zainstalowania pakietów i nowych repozytoriów online. Skrypty te powinny działać w wersjach 32- i 64-bitowych. Zostały napisane dla różnych wersji, ale prawdopodobnie będą działać także na nowszych wersjach z większymi zmianami lub bez nich.

Jeśli masz taki skrypt dla swojej preferowanej dystrybucji, omów go na forum [FreeCAD](https://forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134), abyśmy mogli go uwzględnić.


<div class="mw-collapsible mw-collapsed toccolours">



### Ubuntu


<div class="mw-collapsible-content">

Skrypty te zapewniają niezawodny sposób na zainstalowanie prawidłowego zestawu zależności wymaganych do zbudowania i uruchomienia programu FreeCAD w systemie Ubuntu. Wykorzystują one osobiste archiwa pakietów Ubuntu (PPA) i powinny działać na każdej wersji Ubuntu, dla której przeznaczone jest PPA. Wersja [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) PPA jest przeznaczona dla najnowszych wersji Ubuntu, podczas gdy [freecad-stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA jest przeznaczone dla oficjalnie wspieranych wersji Ubuntu.

Ten skrypt instaluje codziennie kompilowaną wersję FreeCAD i jego zależności. Dodaje codzienne repozytorium, pobiera zależności potrzebne do zbudowania tej wersji i instaluje wymagane pakiety. Następnie zaciąga kod źródłowy do określonego katalogu, tworzy katalog build i wprowadza do niego zmiany, konfiguruje środowisko kompilacji za pomocą `cmake`, a na koniec buduje cały program za pomocą `make`. Zapisz skrypt do pliku, uczyń go wykonywalnym i uruchom go, ale nie używaj `sudo`. Uprawnienia superużytkownika będą wymagane tylko dla wybranych poleceń.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

Jeśli chcesz, możesz odinstalować prekompilowaną wersję programu FreeCAD (`freecad-daily`), pozostawiając zależności na miejscu, jednak pozostawienie zainstalowanego pakietu pozwoli menedżerowi pakietów na aktualizowanie jego zależności. Jest to szczególnie przydatne, jeśli zamierzasz śledzić rozwój programu FreeCAD i stale aktualizować oraz kompilować źródła z repozytorium Git.

Poprzedni skrypt zakłada, że chcesz skompilować najnowszą wersję programu FreeCAD, więc używasz \"codziennego\" repozytorium, aby uzyskać zależności. Zamiast tego możesz jednak pobrać zależności kompilacji ze \"stabilnej\" wersji dla aktualnego wydania Ubuntu. W takim przypadku należy zastąpić górną część poprzedniego skryptu następującymi instrukcjami. W przypadku Ubuntu 12.04 należy pominąć `--enable-source` w poleceniu.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Po zainstalowaniu pakietu `freecad` z repozytorium `freecad-stable`, zastąpi on plik wykonywalny FreeCAD, który jest dostępny w repozytorium Universe Ubuntu. Plik wykonywalny będzie się nazywał po prostu `freecad`, a nie `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### openSUSE 


<div class="mw-collapsible-content">

Do kompilacji programu FreeCAD nie są potrzebne żadne zewnętrzne repozytoria. Istnieje jednak niezgodność z python3-devel, która musi zostać usunięta. FreeCAD może być skompilowany z GIT.


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone https://github.com/FreeCAD/FreeCAD.git free-cad
 
# Now you will have a subfolder in this location called free-cad. It contains the source
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build1
cd FreeCAD-Build1 
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}

Ponieważ używasz Git, następnym razem, gdy będziesz chciał skompilować, nie musisz wszystkiego klonować, wystarczy, pobierzesz i skompilujesz ponownie:


{{Code|lang=bash|code=
# go into free-cad dir created earlier
cd free-cad
 
# pull
git pull
 
# get back to previous dir
cd ..
 
# Now repeat last few steps from before.
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build2
cd FreeCAD-Build2
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Debian Squeeze 


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
# get the needed tools and libs
sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
libqt4-dev qt4-dev-tools python2.5-dev \
libsimage-dev libopencascade-dev \
libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
libtool autotools-dev automake gfortran
 
# checkout the latest source
git clone https://github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Fedora 27/28/29 


<div class="mw-collapsible-content">

Wysłane przez użytkownika [http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) na forum.


{{Code|lang=bash|code=
#!/bin/bash

ARCH=$(arch)

MAIN_DIR=FreeCAD
BUILD_DIR=build

#FEDORA_VERSION=27
#FEDORA_VERSION=28
FEDORA_VERSION=29

PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
 freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"

FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"

if [ "$FEDORA_VERSION" = "29" ]; then
    PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
fi

echo "Installing packages required to build FreeCAD"
sudo dnf -y install $PACKAGES
cd ~
mkdir $MAIN_DIR <nowiki>||</nowiki> { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
cd $MAIN_DIR
git clone https://github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Arch using AUR 


<div class="mw-collapsible-content">

[Arch User Repository (AUR)](https://aur.archlinux.org/) to zbiór stworzonych przez użytkowników receptur do kompilacji pakietów, które nie są oficjalnie wspierane przez opiekunów dystrybucji / społeczność. Zazwyczaj są one bezpieczne. Możesz zobaczyć kto i jak długo opiekował się danym pakietem. Zalecane jest sprawdzenie plików konstrukcyjnych. W tym obszarze dostępne jest także oprogramowanie nie będące oprogramowaniem open source, nawet jeśli jest utrzymywane przez oficjalną firmę będącą właścicielem.

Wymagania wstępne: Git

Kroki do wykonania:

1.  Otwórz terminal. Opcjonalnie utwórz katalog, np. {{incode | mkdir git}}. Opcjonalnie zmień katalog np. `cd git`.
2.  Sklonuj repozytorium AUR : `git clone https://aur.archlinux.org/freecad-git.git`.
3.  Wejdź do katalogu repozytorium AUR : `cd freecad-git`.
4.  Kompiluj używając [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. Flaga -s lub \--syncdeps zainstaluje również wymagane zależności.
5.  Instaluj utworzony pakiet: `makepkg --install` lub kliknij dwukrotnie na pkgname-pkgver.pkg.tar.xz w przeglądarce plików.

Aby zaktualizować FreeCAD do najnowszej wersji, powtórz kroki z punktu 3. Zaktualizuj repo AUR, gdy w przepisie pojawią się jakieś zmiany lub nowe funkcje, używając `git checkout -f` wewnątrz folderu.


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/pl
