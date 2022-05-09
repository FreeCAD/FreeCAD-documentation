# Compile on Linux/pl
**Istnieje eksperymentalny kontener FreeCAD Docker, który jest testowany pod kątem rozwoju FreeCAD. Przeczytaj więcej na ten temat na stronie [Kompilacja w Docker](Compile_on_Docker/pl.md)**


{{TOCright}}

## Informacje ogólne 

W ostatnich dystrybucjach Linuksa FreeCAD jest ogólnie łatwy do zbudowania, ponieważ wszystkie zależności są zwykle dostarczane przez menedżera pakietów. Zasadniczo obejmuje 3 kroki   *

1.  Pobierz kod źródłowy FreeCAD.
2.  Pobierz zależności lub pakiety, od których zależy FreeCAD.
3.  Skonfiguruj za pomocą `cmake` i skompiluj za pomocą `make`.

Poniżej znajdziesz szczegółowe wyjaśnienia całego procesu, niektóre [skrypty do kompilacji](#Skrypty_automatycznej_kompilacji.md) oraz szczegóły, które możesz napotkać. Jeśli znajdziesz w poniższym tekście coś błędnego lub nieaktualnego *(dystrybucje Linuksa często się zmieniają)*, lub jeśli używasz dystrybucji, której nie ma na liście, przedyskutuj ten problem na [forum](https   *//forum.freecadweb.org/index.php) i pomóż nam go poprawić.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width   *800px;">



*Ogólny proces kompilacji programu FreeCAD z kodu źródłowego. Zależności stron trzecich muszą znajdować się w systemie, podobnie jak sam kod źródłowy FreeCAD. CMake konfiguruje system tak, aby za pomocą jednej instrukcji make cały projekt został skompilowany.*

## Pobieranie kodu źródłowego 

### Git

Najlepszym sposobem uzyskania kodu jest sklonowanie repozytorium tylko do odczytu [Git](https   *//github.com/FreeCAD/FreeCAD). Do tego celu potrzebny jest program `git`, który można łatwo zainstalować w większości dystrybucji Linuksa. Można go również uzyskać z [oficjalnej strony](http   *//git-scm.com/).

Program Git można zainstalować za pomocą następującego polecenia   *


{{Code|lang=bash|code=
sudo apt install git
}}

Poniższe polecenie umieści kopię najnowszej wersji kodu źródłowego programu FreeCAD w nowym katalogu o nazwie `freecad-source`.


{{Code|lang=bash|code=
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
}}

Więcej informacji na temat używania środowiska Git i wnoszenia kodu do projektu można znaleźć na stronie [Zarządzanie kodem źródłowym](Source_code_management/pl.md).

### Archiwum źródeł 

Alternatywnie można pobrać źródło w postaci [archiwów](https   *//github.com/FreeCAD/FreeCAD/releases/latest), pliku `.zip` lub `.tar.gz`, a następnie rozpakować je w wybranym katalogu.

## Pobranie zależności 

Aby skompilować FreeCAD musisz zainstalować wymagane zależności wymienione w dokumencie [biblioteki zewnętrzne](Third_Party_Libraries/pl.md). Pakiety, które zawierają te zależności są wymienione poniżej dla różnych dystrybucji Linuksa. Proszę zauważyć, że nazwy i dostępność bibliotek zależą od konkretnej dystrybucji; jeśli dystrybucja jest stara, niektóre pakiety mogą być niedostępne lub mieć inną nazwę. W takim przypadku należy zajrzeć do sekcji [starsze i niekonwencjonalne dystrybucje](Compile_on_Linux/pl#Dystrybucje_starsze_i_niekonwencjonalne.md) poniżej.

Gdy masz już zainstalowane wszystkie zależności, przejdź do sekcji [kompilacja programu](Compile_on_Linux/pl#Kompilacja_programu.md).

Należy pamiętać, że kod źródłowy programu FreeCAD ma rozmiar około 500 MB; może on być trzykrotnie większy, jeśli sklonujesz repozytorium Git z całą historią modyfikacji. Pobranie wszystkich zależności może wymagać pobrania 500 MB lub więcej nowych plików. Kiedy te pliki zostaną rozpakowane, mogą wymagać 1500 MB lub więcej miejsca. Należy również pamiętać, że proces kompilacji może wygenerować do 1500 MB dodatkowych plików, ponieważ system kopiuje i modyfikuje cały kod źródłowy. Dlatego przed przystąpieniem do kompilacji należy upewnić się, że na dysku twardym jest wystarczająco dużo wolnego miejsca, co najmniej 4 GB.


<div class="mw-collapsible mw-collapsed toccolours">

### Debian oraz Ubuntu 


<div class="mw-collapsible-content">

On Debian-based systems (Debian, Ubuntu, Mint, etc.) it is quite easy to get all needed dependencies installed. Most of the libraries are available via `apt` or the Synaptic package manager.

If you already installed FreeCAD from the official repositories, you can install its build dependencies with this single line of code in a terminal   *


```python
sudo apt build-dep freecad
```

However, if the version of FreeCAD in the repositories is old, the dependencies may be the wrong ones to compile a recent version of FreeCAD. Therefore, please verify that you have installed the following packages.

These packages are essential for any sort of compilation to succeed   *

-    `build-essential`, installs the C and C++ compilers, the C development libraries, and the `make` program.

-    `cmake`, essential tool to configure the source of FreeCAD. You may also wish to install `cmake-gui` and `cmake-curses-gui` for a graphical option.

-    `libtool`, essential tools to produce shared libraries.

-    `lsb-release`, the standard base reporting utility is normally already installed in a Debian system, and allows you to programmatically distinguish between a pure Debian installation or a variant, such as Ubuntu or Linux Mint. Do not remove this package, as many other system packages may depend on it.

Compilation of FreeCAD uses the Python language, and it\'s also used at runtime as a scripting language. If you are using a Debian based distribution the Python interpreter is normally already installed.

-    `python3`
    

-    `swig`, the tool that creates interfaces between C++ code and Python.

Please check that you have Python 3 installed. Python 2 was obsoleted in 2019, so new development in FreeCAD is not tested with this version of the language.

The Boost libraries need to be installed   *

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
    

The Coin libraries need to be installed   *

-    `libcoin80-dev`, for Debian Jessie, Stretch, Ubuntu 16.04 to 18.10, or

-    `libcoin-dev`, for Debian Buster, Ubuntu 19.04 and newer, as well as for Ubuntu 18.04/18.10 with the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) added to your software sources.

Several libraries that deal with mathematics, triangulated surfaces, sorting, meshes, computer vision, cartographic projections, 3D visualization, the X11 Window system, XML parsing, and Zip file reading   *

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
    


<div class="mw-collapsible mw-collapsed" style="background-color   *#e0e0e0">

### Python 2 oraz Qt4 

This is not recommended for newer installations as both Python 2 and Qt4 are obsolete. As of version 0.20, FreeCAD no longer supports them.


<div class="mw-collapsible-content">

To compile FreeCAD for Debian Jessie, Stretch, Ubuntu 16.04, using Python 2 and Qt4, install the following dependencies.

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
    

-    `libqt5webkit5-dev`or `qtwebengine5-dev`

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

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

The OpenCascade kernel is the core graphics library to create 3D shapes. It exists in an official version OCCT, and a community version OCE. The community version is no longer recommended, as it\'s outdated.

For Debian Buster and Ubuntu 18.10 and newer, as well as Ubuntu 18.04 with the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) added to your software sources, install the official packages.

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
    

For Debian Jessie, Stretch, Ubuntu 16.04 and newer, install the community edition packages.

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
    

You may install the libraries individually, or using asterisk expansion. Change `occ` for `oce` if you want to install the community libraries.


```python
sudo apt install libocct*-dev
```

#### Pakiety opcjonalne 

Opcjonalnie można również zainstalować te dodatkowe pakiety   *

-    `libsimage-dev`, aby Coin obsługiwał dodatkowe formaty plików graficznych.

-    `doxygen`i `libcoin-doc` *(lub `libcoin80-doc` dla starszych systemów)*, jeśli chcesz generować dokumentację kodu źródłowego.

-    `libspnav-dev`, dla obsługi [maniopulatorów przestrzennych](3D_input_devices/pl.md), takich jak \"Space Navigator\" lub \"Space Pilot\" firmy 3Dconnexion.

-    `checkinstall`, jeśli chcesz zarejestrować zainstalowane pliki w systemowym menedżerze pakietów, aby móc je później odinstalować.

-    `python3-markdown`, aby Menadżer dodatków wyświetlał natywnie pliki README.md w formacie Markdown.

-    `python3-git`, aby Menadżer dodatków używał repozytorium Git do pobierania i aktualizowania środowisk pracy i makrodefinicji.

#### Single command for Python 3 and Qt5 

Requires Pyside2 available in Debian buster and the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md).


```python
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev libqt5webkit5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig
```

NOTE   * On some versions of Ubuntu and some versions of Qt, you will get an error that python3-pyside2uic cannot be found \-- on those systems you can safely omit it. On Ubuntu 20.04 you will need to add `pyqt5-dev-tools`. More information can be found in [this forum discussion](https   *//forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color   *#e0e0e0">

#### Single command for Python 2 and Qt4 

This is not recommended for newer installations as both Python 2 and Qt4 are obsolete.


<div class="mw-collapsible-content">


```python
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
```

Ubuntu 16.04 users please see also the compilation discussion in the forum   * [Compile on Linux (Kubuntu)   * CMake can\'t find VTK](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Wykonaj te same kroki, co w przypadku dystrybucji Debian i Ubuntu.

Zgłaszane są problemy podczas próby kompilacji w systemie Raspbian przy użyciu Pythona 3 i Qt5, ale kombinacja Pythona 3 i Qt4 wydaje się działać ze starszymi wersjami programu FreeCAD.

W przypadku nowszych wersji programu FreeCAD kompilacja z Py3/Qt5 powiedzie się, jeśli zainstalowanym systemem operacyjnym jest Ubuntu 20.04.

Z powodu różnych problemów z Qt, w tej wersji nie będzie można znaleźć normalnych narzędzi PySide. {{Code|lang=bash|code=
E   * Unable to locate package python3-pyside2uic
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

Więcej informacji, [FreeCAD i Raspberry Pi 4](https   *//forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

Potrzebne są następujące pakiety   *

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
-   OCE-devel
-   python
-   python-devel
-   python-pyside-devel
-   pyside-tools
-   boost-devel
-   tbb-devel
-   eigen3-devel
-   qt-devel
-   qt-webkit-devel
-   qt5-qtxmlpatterns
-   qt5-qttools-static
-   ode-devel
-   xerces-c
-   xerces-c-devel
-   opencv-devel
-   smesh-devel
-   Coin3
-   Coin3-devel

*(kwiecień 2021, Coin4 i Coin4-devel są dostępne)* *(jeśli coin2 jest najnowszą dostępną wersją dla twojej wersji Fedory, użyj pakietów z <http   *//www.zultron.com/rpm-repo/>)*

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk
-   med
-   med-devel

I opcjonalnie   *

-   libspnav-devel *(do obsługi urządzeń 3Dconnexion, takich jak Space Navigator czy Space Pilot)*,
-   python3-pivy *(https   *//bugzilla.redhat.com/show\_bug.cgi?id=458975 Pivy nie jest obowiązkowy, ale jest wymagany dla środowiska Rysunek Roboczy)*,
-   python3-markdown *(aby Menadżer dodatków natywny markdown)*,
-   python3-git *(aby Menadżer dodatków używał repozytorium Git do sprawdzania i aktualizowania środowisk pracy i makrodefinicji)*.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Najprostszym sposobem sprawdzenia, które pakiety są potrzebne do skompilowania programu FreeCAD, jest sprawdzenie ich przez portage   *

emerge -pv freecad

Powinno to spowodować wyświetlenie listy dodatkowych pakietów, które należy zainstalować w systemie.

Gdy FreeCAD nie jest dostępny przez portage, jest dostępny na repozytorium [waebbl overlay](https   *//github.com/waebbl/waebbl-gentoo). Narzędzie do śledzenia problemów na nakładce waebbl Github może pomóc w rozwiązaniu niektórych z nich. Nakładka zapewnia szeroki licznik freecad-9999, dzięki temu możesz wybrać potrzebny numer do skompilowania lub po prostu użyć do pobrania zależności.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

The following commands will install the packages required for building FreeCAD with Qt5 and Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

The following command will install Qt Creator and the GNU Project Debugger.


```pythonzypper in libqt5-creator gdb```

If any packages are missing, then you can check the Tumbleweed [\"FreeCAD.spec\"](https   *//build.opensuse.org/package/view_file/openSUSE   *Factory/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https   *//build.opensuse.org/package/show/openSUSE   *Factory/FreeCAD).

Also, check to see if there are any patches you need to apply (such as [0001-find-openmpi2-include-files.patch](https   *//build.opensuse.org/package/view_file/openSUSE   *Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

If there is a difference between the available packages on Tumbleweed and Leap, then you can read the Leap [\"FreeCAD.spec\"](https   *//build.opensuse.org/package/view_file/openSUSE   *Leap   *15.0/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https   *//build.opensuse.org/) to determine the required packages.

See [piano\_jonas unofficial \"Compile On openSUSE\" guide](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

You will need the following libraries from the official repositories   *

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
-   qt5-svg
-   qt5-webkit
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
sudo pacman -S boost curl desktop-file-utils glew hicolor-icon-theme jsoncpp libspnav opencascade shiboken2 xerces-c pyside2 python-matplotlib python-netcdf4 qt5-svg qt5-webkit qt5-webengine cmake eigen git gcc-fortran pyside2-tools swig qt5-tools shared-mime-info coin python-pivy med
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

Dla Ubuntu, może być konieczne włączenie specjalnych repozytoriów, aby móc zobaczyć i zainstalować te pakiety debugowania za pomocą menedżera pakietów. Zapoznaj się ze stroną [Debug Symbol Packages](https   *//wiki.ubuntu.com/Debug_Symbol_Packages), aby uzyskać więcej informacji.

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

Uwaga   * jeśli kompilujesz gałąź wydania 0.19, musisz jawnie określić, że kompilujesz z użyciem pakietów Qt5 i Python 3 \-- zamień powyższe polecenie cMake na   * {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

Opcja `-j` programu `make` kontroluje, ile zadań (plików) jest kompilowanych równolegle. Program `nproc` wypisuje liczbę rdzeni procesora w twoim systemie. Używając go razem z opcją `-j` możesz wybrać przetwarzanie tylu plików, ile masz rdzeni, aby przyspieszyć ogólną kompilację programu. W powyższym przykładzie, użyje on wszystkich rdzeni w systemie z wyjątkiem dwóch. Dzięki temu Twój komputer będzie mógł być wykorzystany do innych celów, podczas gdy kompilacja będzie przebiegać w tle. Plik wykonywalny programu FreeCAD pojawi się ostatecznie w katalogu `freecad-build/bin`. Zobacz także stronę [Kompilacja *(przyspieszamy)*](Compiling_(Speeding_up)/pl.md), aby poprawić szybkość kompilacji.

### Rozwiązywanie problemów z cmake 

Jeśli już wcześniej wykonałeś kompilację poza źródłem i utknąłeś na zależności, która nie została rozpoznana lub nie można jej rozwiązać, spróbuj wykonać następujące czynności   *

-   Usuń zawartość katalogu kompilacji przed ponownym uruchomieniem cmake. FreeCAD jest szybko zmieniającym się celem, możesz natknąć się na zbuforowane informacje cmake, które wskazują na starszą wersję niż ta, której może użyć nowy serwer repozytorium. Wyczyszczenie pamięci podręcznej może pozwolić cmake odzyskać i rozpoznać wersję, której rzeczywiście potrzebujesz.

-   Jeśli `cmake` skarży się na brak konkretnego pliku, użyj narzędzia takiego jak `apt-file search` lub jego odpowiednika w innych systemach pakietów, aby dowiedzieć się, do jakiego pakietu należy ten plik i zainstalować go. Pamiętaj, że prawdopodobnie będziesz potrzebował wersji `-dev` pakietu, która zawiera pliki nagłówkowe lub konfiguracyjne wymagane do korzystania z pakietu przez FreeCAD.

### Kompilacja z GNU libc 2.34 i nowszymi 

GNU libc 2.34 wprowadza zmianę w bibliotece, która może spowodować, że kompilacja w niektórych systemach Linux nie powiedzie się powodując następujący błąd   *


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

Aby temu zaradzić, należy ręcznie utworzyć dowiązanie symboliczne z *(pustego teraz)* systemowego libdl.so.\* do miejsca, w którym kompilator mówi, że szuka tego pliku. Na przykład (jeśli faktycznie zainstalowaną kopią libdl.so w systemie jest /usr/lib/x86\_64-linux-gnu/libdl.so.2)   *


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Dostosuj to polecenie do struktury swojego systemu, wyszukując libdl.so\* i umieszczając je w odpowiedniej lokalizacji.

### Kompilacja na bazie źródeł 

Kompilacje źródłowe są dobre, jeśli chcesz szybko skompilować wersję FreeCAD i nie zamierzasz często aktualizować kodu źródłowego. W takim przypadku możesz usunąć skompilowany program i źródło, usuwając tylko jeden folder.

Zmień katalog na źródłowy i wskaż `cmake` na obecny katalog *(oznaczony pojedynczym punktem)*   *


{{Code|lang=bash|code=
cd freecad-source
cmake . -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
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
cmake -D <var>   *<type>=<value> $SOURCE_DIR
```

Gdzie `$SOURCE_DIR` jest katalogiem zawierającym kod źródłowy. Opcję `<type>` można w większości przypadków pominąć. Można też pominąć spację po opcji `-D`.

Na przykład, aby uniknąć kompilacji środowiska [MES](FEM_Workbench/pl.md)   *


{{Code|lang=bash|code=
cmake -D BUILD_FEM   *BOOL=OFF ../freecad-source
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

#### Do debugowania kompilacji 

Utwórz kompilację `Debug` do rozwiązywania problemów z awariami w programie FreeCAD. Zwróć uwagę, że w tej wersji kompilacji środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) przy złożonych szkicach staje się bardzo powolne.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}

#### For a Release build 

Utwórz kompilację `Release`, aby przetestować kod, który nie ulega awarii. Kompilacja `Release` będzie działać znacznie szybciej niż kompilacja `Debug`.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}

#### Kompilacja w oparciu o Python 3 i Qt5 

By default, FreeCAD 0.19 and earlier build for Python 2 and Qt4. Since these two packages are obsolete, it is better to build for Python 3 and Qt5. Support for Python 2 and Qt4 has been removed in FreeCAD 0.20 and it is not necessary to explicitly enable Qt5 and Python 3 if compiling the latest development versions.

In a modern Linux distribution you only need to provide two variables specifying the use of Qt5, and the path to the Python interpreter.

For 0.19   * {{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

For 0.20\_dev   * {{Code|lang=bash|code=
cmake ../freecad-source
}}

Note that when switching between 0.19 and the 0.20 builds, it may be necessary to delete CMakeCache.txt prior to running cmake.

#### Building for a specific Python version 

If the default `python` executable in your system is a symbolic link to Python 2, `cmake` will try to configure FreeCAD for this version. You can choose another version of Python by giving the path to a specific executable   *


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

If that doesn\'t work, you may have to define additional variables pointing to the desired Python libraries and include directories   *


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

It is possible to have several independent versions of Python in the same system, so the locations and version numbers of your Python files will depend on your particular Linux distribution. Use `python3 -V` to display the version of Python that you are using currently; only the first two numbers are necessary; for example, if the result is `Python 3.6.8`, you need to specify the directories that relate to the 3.6 version. If you don\'t know the right directories, try searching for them with the `locate` command.


```python
locate python3.6
```

You may use `python3 -m site` in a terminal to determine the `site-packages` directory, or `dist-packages` for Debian systems.

#### Building with Qt Creator against Python 3 and Qt5 

1\. Launch Qt Creator.

2\. Click on **Open Project**.

3\. Navigate to the directory where the source code is, `freecad-source/`, and choose the topmost `CMakeLists.txt` file.

4\. By selecting the file, it will automatically run `cmake` on it, but it may fail if the appropriate options aren\'t correctly set.

5\. Go to **Projects → Build & Run → Imported Kit → Build → Build Settings → CMake**. Set the appropriate build directory, `freecad-build/`.

6\. Set the appropriate variables in the Key-Value dialog, of types `String` and `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
BUILD_QT5=ON
```

7\. If the variables do not load the project correctly, you may have to go to **Projects → Manage Kits → Kits → Default (or Imported Kit or similar) → CMake Configuration**. Then press **Change**, and add the appropriate configuration as described above. You may have to add more variables about the Python paths, if the system Python is not found. 
```python
PYTHON_EXECUTABLE   *STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR   *STRING=/usr/include/python3.7m
PYTHON_LIBRARY   *STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH   *STRING=/usr/lib/python3.7/site-packages
BUILD_QT5   *BOOL=ON
```

7.1. Press **Apply**, then **OK**.

7.2. Make sure the rest of the options are correctly set, for example, **Qt version** should be a present version installed in the system, like `Qt 5.9.5 in PATH (qt5)`.

Press **Apply**, then **OK** to close the configuration.

The `cmake` program should run automatically again, and it should fill the entire Key-Value dialog with all the variables that can be configured.

8\. Go to **Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration** and choose `FreeCADMain` to compile the graphical version of FreeCAD, or `FreeCADMainCMD` to compile only the command line version.

9\. Finally, go to the menu **Build → Build Project "FreeCAD"**. If this is a new compilation, it should take several minutes, inclusive hours, depending on the number of processors that you have available.

#### Qt designer plugin 

If you want to develop Qt code for FreeCAD, you\'ll need the Qt Designer plugin that provides all custom widgets of FreeCAD.

Go into an auxiliary directory of the source code, the run `qmake` with the indicated project file to create a `Makefile`; then run `make` to compile the plugin.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

If you are compiling for Qt5, make sure the `qmake` binary is the one for this version, so that the resulting `Makefile` contains the necessary information for Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

where `$QT_DIR` is the directory that stores Qt binary libraries, for example, `/usr/lib/x86_64-linux-gnu/qt5`.

The library created is `libFreeCAD_widgets.so`, which needs to be copied to `$QT_DIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}

#### External or internal Pivy 

Previously, a version of Pivy was included in the source code of FreeCAD (internal). If you wanted to use your system\'s copy of Pivy (external), you needed to use -DFREECAD_USE_EXTERNAL_PIVY=1.

Using external Pivy became the default during development of FreeCAD 0.16, therefore this option does not need to be set manually anymore.

#### Doxygen documentation 

If you have Doxygen installed you can build the source code documentation. See [source documentation](source_documentation.md) for instructions.

### Additional documentation 

The source code of FreeCAD is very extensive, and with CMake it\'s possible to configure many options. Learning to use CMake fully may be useful to choose the right options for your particular needs.

-   [CMake Reference Documentation](https   *//cmake.org/documentation/) by Kitware.
-   [How to Build a CMake-Based Project](https   *//preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) by Preshing on programming.
-   [Learn CMake\'s Scripting Language in 15 Minutes](https   *//preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (blog) by Preshing on programming.

### Making a debian package 

If you plan to build a Debian package out of the sources you need to install certain packages first   *


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Go to the FreeCAD directory and call


{{Code|lang=bash|code=
debuild
}}

Once the package is built, you can use `lintian` to check if the package contains errors


{{Code|lang=bash|code=
lintian freecad-package.deb
}}

## Updating the source code 

The CMake system allows you to intelligently update the source code, and only recompile what has changed, making subsequent compilations faster.

Move to the location where the FreeCAD source code was first downloaded, and pull the new code   *


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Then move into the build directory where the code was compiled initially, and run `cmake` specifying the present directory (denoted by a dot); then trigger the re-compilation with `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}

## Troubleshooting

### For 64 bit systems 

When building FreeCAD for 64-bit there is a known issue with the OpenCASCADE (OCCT) 64-bit package. To get FreeCAD running properly you might need to run the `configure` script and set additional `CXXFLAGS`   *


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

For Debian based systems this option is not needed when using the pre-built OpenCASCADE packages because these ones set the proper `CXXFLAGS` internally.

## Skrypty automatycznej kompilacji 

Here is all what you need for a complete build of FreeCAD. It\'s a one-script-approach and works on a freshly installed Linux distribution. The commands will ask for the root password for installation of packages and new online repositories. These scripts should run on 32 and 64 bit versions. They are written for different versions, but are also likely to run on a later version with or without major changes.

If you have such a script for your preferred distribution, please discuss it on the [FreeCAD forum](https   *//forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134) so we can incorporate it.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

These scripts provide a reliable way to install the correct set of dependencies required to build and run FreeCAD on Ubuntu. They make use of the Ubuntu personal package archives (PPA), and should work on any version of Ubuntu targeted by the PPA. The [freecad-daily](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) PPA targets recent versions of Ubuntu, while the [freecad-stable](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA targets officially supported versions of Ubuntu.

This script installs the daily compiled snapshot of FreeCAD and its dependencies. It adds the daily repository, gets the dependencies to build this version, and installs the required packages. Afterwards it proceeds to pull the source code into a particular directory, creates a build directory and changes into it, configures the compilation environment with `cmake`, and finally builds the entire program with `make`. Save the script to a file, make it executable, and run it, but don\'t use `sudo`; superuser privileges will be asked only for selected commands.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa   *freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

If you wish, you can uninstall the pre-compiled version of FreeCAD (`freecad-daily`) while leaving the dependencies in place, however, leaving this package installed will allow the package manager to keep its dependencies up to date as well; this is mostly useful if you intend to follow the development of FreeCAD, and constantly update and compile the sources from the Git repository.

The previous script assumes that you want to compile the latest version of FreeCAD, so you are using the \"daily\" repository to get the dependencies. However, you can instead get the build dependencies of the \"stable\" version for your current Ubuntu release. If this is the case, replace the top part of the previous script with the following instructions. For Ubuntu 12.04, omit `--enable-source` from the command.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa   *freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Once you install the `freecad` package from the `freecad-stable` repository, it will supersede the FreeCAD executable that is available from the Universe Ubuntu repository. The executable will be named simply `freecad`, and not `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">

No external Repositories are needed to compile FreeCAD. However, there is an imcompatability with python3-devel which needs to be removed. FreeCAD can be compiled from GIT


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone https   *//github.com/FreeCAD/FreeCAD.git free-cad
 
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

Since you are using git, next time you wish to compile you do not have to clone everything, just pull from git and compile once more


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
# Note   * to speed up build use all CPU cores   * make -j$(nproc)
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
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note   * to speed up build use all CPU cores   * make -j$(nproc)
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

Posted by user [http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) in the forum.


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
git clone https   *//github.com/FreeCAD/FreeCAD.git
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

[Arch User Repository (AUR)](https   *//aur.archlinux.org/) is a collection user made recipes to build packages which are not officially supported by distribution maintainers / community. They are usually safe. You can see who maintain the package and for how long he did. It is recommended to check construction files. Also non open source software are available in this area even if maintained by the official owning company.

Prerequisite    * git

Steps    *

1.  Open a terminal. Optionally create a directory eg. {{incode | mkdir git}}. Optionally change directory eg. `cd git`.
2.  Clone the AUR repository    * `git clone http   *//aur.archlinux.org/packages/freecad-git`
3.  Enter AUR repository folder    * `cd freecad-git`
4.  Compile using [Arch makepkg](https   *//wiki.archlinux.org/index.php/Makepkg)    * `makepkg -s`. The -s or \--syncdeps flag will also install required dependencies.
5.  Install created package    * `makepkg --install` or double click on the pkgname-pkgver.pkg.tar.xz inside your file browser.

To update FreeCAD to latest build just repeat from step 3. Update AUR repo when there is some breaking change in the recipe or new features using `git checkout -f` inside the folder.







[Category   *Developer\_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/pl
