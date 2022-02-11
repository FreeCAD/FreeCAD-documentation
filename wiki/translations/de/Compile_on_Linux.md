# Compile on Linux/de
**Es gibt einen experimentellen FreeCAD Docker Container, der für die FreeCAD Entwicklung getestet wird. Lies mehr darüber unter [Kompilieren auf Docker](Compile_on_Docker/de.md)**


{{TOCright}}

## Überblick

Auf neuesten Linux Distributionen ist FreeCAD in der Regel einfach zu erstellen, da alle Abhängigkeiten in der Regel vom Paketmanager bereitgestellt werden. Es schliesst im Wesentlichen 3 Schritte ein:

1.  Besorgen des FreeCAD Quellcodes
2.  Ermittlung der Abhängigkeiten oder Pakete, von denen FreeCAD abhängt
3.  Konfigurieren mit `cmake` und kompilieren mit `make`.

Nachfolgend finden sich detaillierte Erklärungen des gesamten Prozesses, einige [Bauskripte](#Automatic_build_scripts/de.md) und Besonderheiten, denen man begegnen könnte. Wenn Du im folgenden Text etwas Falsches oder Veraltetes findest (Linux-Distributionen ändern sich oft), oder wenn Du eine Distribution verwendest, die nicht aufgeführt ist, diskutieren das Problem im [Forum](https://forum.freecadweb.org/index.php) und hilf uns, es zu korrigieren.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width:800px;">



*Allgemeiner Arbeitsablauf zur Kompilierung von FreeCAD aus der Quelle. Die Abhängigkeiten von Drittanbietern müssen im System vorhanden sein, ebenso wie der FreeCAD-Quellcode selbst. CMake konfiguriert das System so, dass mit einer einzigen make Anweisung das gesamte Projekt kompiliert wird.*

## Abruf der Quelle 

### Git

Der beste Weg, den Code zu bekommen, ist, das schreibgeschützte [Git Repositorium](https://github.com/FreeCAD/FreeCAD) zu klonen. Dazu benötigst du das `git` Programm, das in den meisten Linux Distributionen einfach installiert werden kann. Er kann auch über die [offizielle Webseite](http://git-scm.com/) bezogen werden.

Git kann mit dem folgenden Befehl installiert werden:


{{Code|lang=bash|code=
sudo apt install git
}}

Der folgende Befehl legt eine Kopie der letzten Version des FreeCAD Quellcodes in einem neuen Verzeichnis namens `freecad-source` ab.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

Weitere Informationen über die Verwendung von Git und das Einbringen von Code in das Projekt siehe [Quellcodeverwaltung](Source_code_management/de.md).

### Quellarchiv

Alternativ kannst du den Quellcode als [1](https://github.com/FreeCAD/FreeCAD/releases/latest-Archiv), eine `.zip` oder `.tar.gz` Datei herunterladen und in das gewünschte Verzeichnis entpacken.

## Erhalten der Abhängigkeiten 

Um FreeCAD zu kompilieren, musst du die unter [Third Party Libraries](Third_Party_Libraries.md) genannten Abhängigkeiten installieren; die Pakete, die diese Abhängigkeiten enthalten, sind unten für verschiedene Linux-Distributionen aufgeführt. Bitte beachte, dass die Namen und die Verfügbarkeit der Bibliotheken von eurer jeweiligen Distribution abhängen; wenn eure Distribution alt ist, können einige Pakete nicht verfügbar sein oder einen anderen Namen haben. Schaue in diesem Fall im nachfolgenden Abschnitt [older and non-conventional distributions](#Older_and_non-conventional_distributions/de.md)

Sobald du alle Abhängigkeiten installiert hast, gehe weiter zu [kompiliere FreeCAD](#FreeCAD_kompilieren.md).

Bitte beachte, dass der Quellcode von FreeCAD ca. 500 MB groß ist; er kann dreimal so groß sein, wenn Du das Git-Repository mit seiner gesamten Änderungshistorie klonst. Das Erhalten aller Abhängigkeiten kann das Herunterladen von 500 MB oder mehr neuer Dateien erfordern; wenn diese Dateien entpackt werden, können sie 1500 MB oder mehr Speicherplatz benötigen. Beachten auch, dass der Kompilierungsprozess bis zu 1500 MB zusätzliche Dateien erzeugen kann, wenn das System den gesamten Quellcode kopiert und ändert. Stelle daher sicher, dass genügend freier Speicherplatz auf Deiner Festplatte vorhanden ist, mindestens 4 GB, wenn Du mit dem Kompilieren beginnst.


<div class="mw-collapsible mw-collapsed toccolours">

### Debian und Ubuntu 


<div class="mw-collapsible-content">

Auf Debian-basierten Systemen (Debian, Ubuntu, Mint, etc.) ist es recht einfach, alle benötigten Abhängigkeiten zu installieren. Die meisten Bibliotheken sind über `apt` oder den Synaptic Package Manager verfügbar.

Wenn du FreeCAD bereits aus den offiziellen Repositories installiert hast, kannst du seine Build Abhängigkeiten mit dieser einzigen Zeile Code in einem Terminal installieren:


```python
sudo apt build-dep freecad
```

Wenn die Version von FreeCAD in den Repositorien jedoch alt ist, können die Abhängigkeiten die falschen sein, um eine aktuelle Version von FreeCAD zu erstellen. Bitte überprüfe daher, ob Du die folgenden Pakete installiert hast.

Diese Pakete sind unerlässlich für jede Art von Kompilierung, um erfolgreich zu sein:

-    `build-essential`, installiert die C- und C++-Compiler, die C-Entwicklungsbibliotheken und das Programm `make`.

-    `cmake`, ein unverzichtbares Werkzeug zur Konfiguration der Quelle von FreeCAD. Du kannst auch `cmake-gui` und `cmake-curses-gui` für eine grafische Option installieren.

-    `libtool`, essentielle Werkzeuge zur Erstellung von gemeinsamen Bibliotheken.

-    {{Incode|lsb-release}}, das Standard Basis Reporting Dienstprogramm ist normalerweise bereits in einem Debian System installiert und ermöglicht es Dir, programmgesteuert zwischen einer reinen Debian Installation und einer Variante wie Ubuntu oder Linux Mint zu unterscheiden. Entferne dieses Paket nicht, da viele andere Systempakete davon abhängen können.

Die Kompilierung von FreeCAD verwendet die Python Sprache, und sie wird auch zur Laufzeit als Skriptsprache verwendet. Wenn du eine Debian basierte Distribution verwendest, ist der Python Interpreter normalerweise bereits installiert.

-    `python3`
    

-    `swig`, das Werkzeug, das Schnittstellen zwischen C++ Code und Python schafft.

Bitte überprüfe, ob Du Python 3 installiert bist. Python 2 war 2019 veraltet, so dass die Neuentwicklung in FreeCAD mit dieser Sprachversion nicht getestet wird.

Die Verstärker Bibliotheken müssen installiert sein:

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
    

Die Coin Bibliotheken müssen installiert sein:

-    `libcoin80-dev`, für Debian Jessie, Stretch, Ubuntu 16.04 bis 18.10, oder

-    `libcoin-dev`, für Debian Buster, Ubuntu 19.04 und neuer, sowie für Ubuntu 18.04/18.10 mit dem [freecad-stable/freecad-daily PPAs](Installing_on_Linux/de#Official_Ubuntu_repository.md) zu Deinen Softwarequellen hinzugefügt.

Einige Bibliotheken, die sich mit Mathematik, dreieckigen Oberflächen, Sortieren, Netzen, Computer Vision, kartographischen Projektionen, 3D Visualisierung, dem X11-Window-System, XML-Parsing und dem Lesen von Zip-Dateien befassen:

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

#### Python 2 und Qt4 

Dies wird für neuere Installationen nicht empfohlen, da sowohl Python 2 als auch Qt4 veraltet sind. Ab der Version 0.20 werden sie von FreeCAD nicht mehr unterstützt.


<div class="mw-collapsible-content">

Um FreeCAD für Debian Jessie, Stretch, Ubuntu 16.04 mit Python 2 und Qt4 zu kompilieren, installiere die folgenden Abhängigkeiten.

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

#### Python 3 und Qt5 

Um FreeCAD für Debian Buster, Ubuntu 19.04 und neueren, sowie Ubuntu 18.04/18.10 mit dem [freecad-stable/freecad-daily PPAs](Installing_on_Linux/de#Official_Ubuntu_repository.md) zu deinen Softwarequellen hinzuzufügen, installiere die folgenden Abhängigkeiten.

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
    

#### OpenCascade Kernel 

Der OpenCascade Kern ist die zentrale Grafikbibliothek zur Erstellung von 3D-Formen. Es existiert in einer offiziellen Version OCCT und einer Community-Version OCE. Die Community-Version wird nicht mehr empfohlen, da sie veraltet ist.

Für Debian Buster und Ubuntu 18.10 und neuer, sowie Ubuntu 18.04 mit dem [freecad-stable/freecad-daily PPAs](Install_on_Linux/de#Official_Ubuntu_repository.md) zu deinen Softwarequellen hinzugefügt, installiere die offiziellen Pakete.

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
    

Für Debian Jessie, Stretch, Ubuntu 16.04 und neuer, installiere die Gemeinschafts Editionspakete.

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
    

Du kannst die Bibliotheken einzeln oder mit Hilfe der Sternchen-Erweiterung installieren. Ändere `occ` für `oce`, wenn Du die Gemeinschaftsbibliotheken installieren möchtest.


```python
sudo apt install libocct*-dev
```

#### Optionale Pakete 


<div class="mw-translate-fuzzy">

Optional kannst du diese zusätzlichen Pakete auch installieren:

-    `libsimage-dev`, damit Coin zusätzliche Bilddateiformate unterstützt.

-    `doxygen`und `libcoin-doc` (oder `libcoin80-doc` für ältere Systeme), wenn du beabsichtigst, Quellcode Dokumentation zu generieren.

-    `libspnav-dev`, für [3D-Eingabegeräte](3D_input_devices/de.md) Unterstützung, wie die 3D Verbindung \"Space Navigator\" oder \"Space Pilot\".

-    `checkinstall`, wenn Du vorhast, Deine installierten Dateien im Paketmanager Deines Systems zu registrieren, damit Du sie später deinstallieren kannst.


</div>

#### Einzelbefehl für Python 3 und Qt5 

Erfordert Pyside2, das in Debian Buster und dem [freecad-stable/freecad-daily PPAs](Installing_on_Linux/de#Official_Ubuntu_repository.md) verfügbar ist.


```python
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev libqt5webkit5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig
```

HINWEIS: Auf einigen Versionen von Ubuntu und einigen Versionen von Qt erhälst du eine Fehlermeldung, dass python3-pyside2uic nicht gefunden werden kann - auf diesen Systemen kannst du es getrost weglassen. Unter Ubuntu 20.04 musst du `pyqt5-dev-tools`. hinzufügen. Weitere Informationen findest du in [diese Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">

#### Einziger Befehl für Python 2 und Qt4 

Dies wird für neuere Installationen nicht empfohlen, da sowohl Python 2 als auch Qt4 veraltet sind.


<div class="mw-collapsible-content">


```python
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
```

Ubuntu 16.04 Benutzer sehen bitte auch die Kompilierungsdiskussion im Forum: [Compile on Linux (Kubuntu): CMake can\'t find VTK](http://forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Folge den gleichen Schritten wie in Debian und Ubuntu.

Es wurde von Problemen berichtet, wenn man versucht, in Raspbian mit Python 3 und Qt5 zu kompilieren, aber die Kombination Python 3 und Qt4 scheint für ältere Versionen von FreeCAD zu funktionieren.

Für neuere Versionen von FreeCAD ist die Kompilierung mit Py3/Qt5 erfolgreich, wenn das installierte Betriebssystem Ubuntu 20.04 ist.

Aufgrund verschiedener Probleme mit Qt werden in dieser Version die normalen PySide Werkzeuge nicht gefunden. {{Code|lang=bash|code=
E: Unable to locate package python3-pyside2uic
}}

In diesem Fall können wir die Pakete von PyQt installieren und symbolische Links zu den benötigten Werkzeugen erstellen. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Nun kann die Kompilierung fortgesetzt werden. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

Die `-j` Option für `make` sollte nicht mehr als 3 sein, da das Raspberry Pi einen begrenzten Speicher hat. Die Kompilierung wird mehrere Stunden dauern, daher ist es besser, sie über Nacht durchzuführen.

Weitere Informationen, [FreeCAD und Raspberry Pi 4](https://forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

Du benötigst die folgenden Pakete:

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

(April 2021, Coin4 und Coin4-devel sind verfügbar ) (wenn coin2 die neueste verfügbare Version für deine Fedora Version ist, verwende Pakete von <http://www.zultron.com/rpm-repo/>)

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk
-   med
-   med-devel

Und optional:


<div class="mw-translate-fuzzy">

-   libspnav-devel (für 3Dconnexion Geräte mit Unterstützung wie Space Navigator oder Space Pilot)
-   python3-pivy ( <https://bugzilla.redhat.com/show_bug.cgi?id=458975> Pivy ist nicht obligatorisch, wird aber für den Draft Arbeitsbereich benötigt)


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Der einfachste Weg, um zu überprüfen, welche Pakete für die Kompilierung von FreeCAD benötigt werden, ist die Überprüfung über Portage:

emerge -pv freecad

Dies sollte eine schöne Liste von zusätzlichen Paketen liefern, die Du auf Deinem System installieren musst.

Wenn FreeCAD auf Portage nicht verfügbar ist, ist es auf dem [waebbl overlay](https://github.com/waebbl/waebbl-gentoo) verfügbar. Der Issue Tracker auf dem Waebbl Overlay Github kann Dir helfen, einige Probleme zu lösen, auf die Du stoßen könntest. Das Overlay bietet freecad-9999, das Du kompilieren oder einfach verwenden kannst, um die Abhängigkeiten zu erhalten.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

Die folgenden Befehle installieren die Pakete, die für die Erstellung von FreeCAD mit Qt5 und Python 3 erforderlich sind.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

Der folgende Befehl installiert den Qt Creator und den GNU Project Debugger.


```pythonzypper in libqt5-creator gdb```

Wenn Pakete fehlen, dann kannst du die Datei Tumbleweed [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec) auf dem [Open Build Service](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD) überprüfen.

Überprüfe auch, ob es Patches gibt, die Du installieren musst (z.B.[0001-find-openmpi2-include-files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

Wenn es einen Unterschied zwischen den verfügbaren Paketen auf Tumbleweed und Leap gibt, dann kannst du die Leap [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec) Datei auf dem [Open Build Service](https://build.opensuse.org/) lesen, um die benötigten Pakete zu ermitteln.

Siehe [piano\_jonas unofficial \"Kompiliren Unter openSUSE\" Leitfaden](https://forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

Du benötigst die folgenden Bibliotheken aus den offiziellen Repositorien:

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

### Ältere und unkonventionelle Distributionen 


<div class="mw-collapsible-content">

Bei anderen Distributionen haben wir nur sehr wenig Feedback von Benutzern, so dass es schwieriger sein könnte, die benötigten Pakete zu finden.

Versuche zuerst, die erforderlichen Bibliotheken zu finden, die in [third party libraries](Third_Party_Libraries.md) in deinem Paketmanager erwähnt werden. Beachte, dass einige von ihnen einen etwas anderen Paketnamen haben könnten; suche nach `name`, aber auch `libname`, `name-dev`, `name-devel` und ähnlichem. Wenn das nicht möglich ist, versuche, diese Bibliotheken selbst zu kompilieren.

FreeCAD benötigt die GNU g++ Kompiliererversion gleich oder über 3.0.0, da FreeCAD meist in C++ geschrieben ist. Während der Kompilierung werden einige Python Skripte ausgeführt, so dass der Python Interpreter ordnungsgemäß funktionieren muss. Um Probleme mit dem Linker zu vermeiden, ist es auch eine gute Idee, die Bibliothekspfade in der Variablen `LD_LIBRARY_PATH` oder in der Datei `ld.so.conf` zu haben. Dies geschieht bereits in modernen Linux-Distributionen, muss aber möglicherweise in älteren eingestellt werden.


</div>


</div>

### Pivy

[Pivy](Pivy/de.md) (Python Wrapper zu Coin3d) wird nicht benötigt, um FreeCAD zu bauen oder zu starten, aber es wird als Laufzeitabhängigkeit von der [Draft Arbeitsbereich](Draft_Workbench/de.md) benötigt. Wenn Du diesen Arbeitsbereich nicht benutzt, benötigst Du Pivy nicht. Beachte jedoch, dass der Entwurfs-Arbeitsbereich intern von anderen Arbeitsbereich wie [Arch Arbeitsbereich](Arch_Workbench/de.md) und [BIM Arbeitsbereich](BIM_Workbench/de.md) verwendet wird, so dass Pivy installiert werden muss, um diese Arbeitsbereiche ebenfalls zu verwenden.

Bis November 2015 wird die im FreeCAD-Quellcode enthaltene veraltete Version von Pivy auf vielen Systemen nicht mehr kompiliert. Dies ist kein großes Problem, da Du normalerweise Pivy über den Paketmanager Deiner Distribution beziehen solltest; wenn Du Pivy nicht finden kannst, musst Du es möglicherweise selbst kompilieren, siehe [Pivy compilation instructions](Extra_python_modules#Pivy.md)

### Fehlersuch Symbole 

Um Abstürze in FreeCAD zu beheben, ist es sinnvoll, die Fehlersuche Symbole wichtiger Abhängigkeitsbibliotheken wie Qt zu haben. Versuche dazu, die Abhängigkeitspakete zu installieren, die mit `-dbg`, `-dbgsym`, `-debuginfo` oder ähnlichem enden, abhängig von Deiner Linux-Distribution.

Unter Ubuntu musst Du möglicherweise spezielle Repositorien aktivieren, um diese Fehlersuch Pakete mit dem Paketmanager sehen und installieren zu können. Siehe [Fehlersuch Symbol Pakete](https://wiki.ubuntu.com/Debug_Symbol_Packages) für weitere Informationen.

## Kompiliere FreeCAD 


**Das Kompilieren gegen Python 2 und Qt4 wird nicht mehr gut unterstützt, und ab 0.20 überhaupt nicht mehr unterstützt. Du solltest gegen Python 3 und Qt5 kompilieren. 0.20 benötigt mindestens Python3.6 und Qt 5.9.**

FreeCAD verwendet CMake als Hauptbuild-System, da es auf allen gängigen Betriebssystemen verfügbar ist. Die Kompilierung mit CMake ist in der Regel sehr einfach und erfolgt in zwei Schritten.

1.  CMake überprüft, ob alle benötigten Programme und Bibliotheken auf Ihrem System vorhanden sind und erzeugt eine `Makefile`, die für den zweiten Schritt konfiguriert ist. FreeCAD hat mehrere Konfigurationsoptionen zur Auswahl, aber es wird mit sinnvollen Standardeinstellungen ausgeliefert. Einige Alternativen werden im Folgenden beschrieben.
2.  Die Kompilierung selbst, die mit dem Programm `make` durchgeführt wird, das die FreeCAD-Ausführungsdateien erzeugt.

Da FreeCAD eine große Anwendung ist, kann die Kompilierung des gesamten Quellcodes je nach CPU und Anzahl der für die Kompilierung verwendeten CPU-Kerne zwischen 10 Minuten und einer Stunde dauern.

Du kannst den Code entweder in oder aus dem Quellverzeichnis erstellen. Aus dem Quelltext heraus Erstellung ist in der Regel die beste Option.

### Aus-der-Quelle Bau 

Das Erstellen in einem separaten Ordner ist bequemer als das Erstellen in demselben Verzeichnis, in dem sich der Quellcode befindet, da CMake bei jeder Aktualisierung des Quellcodes intelligent feststellen kann, welche Dateien sich geändert haben, und nur das neu kompilieren kann, was benötigt wird. Dies ist sehr nützlich, wenn Sie verschiedene Git-Zweige testen, da Sie das Build-System nicht verwirren.

Um Out-of-Source zu erstellen, erstelle einfach ein Build-Verzeichnis, `freecad-build`, das sich von Deinem FreeCAD-Quellordner unterscheidet, `freecad-source`; dann von diesem Build-Verzeichnis-Punkt `cmake` zum richtigen Quellordner. Du kannst `cmake-gui` oder `ccmake` anstelle von `cmake` auch in den folgenden Anweisungen verwenden. Sobald `cmake` die Konfiguration der Umgebung abgeschlossen hat, verwende `make`, um die eigentliche Kompilierung zu starten.


{{Code|lang=bash|code=
mkdir freecad-build
cd freecad-build
cmake ../freecad-source
make -j$(nproc --ignore=2)
}}

Hinweis: Wenn du den 0.19er Release Zweig kompilierst, musst du explizit angeben, dass du mit Qt5 und Python 3 kompilierst \-- ersetze den obigen cMake Befehl durch: {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

Die Option `-j` von `make` steuert, wie viele Aufträge (Dateien) parallel kompiliert werden. Das Programm `nproc` druckt die Anzahl der CPU-Kerne in Deinem System; indem Du es zusammen mit der Option `-j` verwendest, kannst Du wählen, ob Du so viele Dateien wie möglich verarbeiten möchtest, um die Gesamtübersetzung des Programms zu beschleunigen. Im obigen Beispiel verwendet es alle Kerne in Deinem System mit Ausnahme von zwei; dies hält Deinen Computer für andere Anwendungen reaktionsschnell, während die Kompilierung im Hintergrund abläuft. Die FreeCAD-Ausführdatei wird schließlich im Verzeichnis `freecad-build/bin` erscheinen. Siehe auch [Kompilieren (Beschleunigen)](Compiling_(Speeding_up)/de.md), um die Kompilierungsgeschwindigkeit zu verbessern.

### Behebung von cmake Problemen 

Wenn du schon einmal einen Aus-der-Quelle Bau durchgeführt hast und an einer Abhängigkeit hängen bleibyt, die nicht erkannt wird oder nicht aufgelöst werden kann, versuche Folgendes:

-   Lösche die Inhalte des Bau Verzeichnisses, vor dem erneuten ausführen von cmake. FreeCAD ist ein sich schnell veränderndes Ziel, möglicherweise stolperst du über zwischengespeicherte cmake Informationen, die auf eine ältere Version verweisen, als der neue Repositoriumdkopf verwenden kann. Leeren des Zwischenspeichers, kann cmake erlauben sich zu erholen und die Version erkennen, die du tatsächlich benötigst.

-   Wenn sich cmake darüber beschwert, dass eine bestimmte Datei fehlt, verwende ein Werkzeug wie \"apt-file search\" oder ein entsprechendes Werkzeug in anderen Paketsystemen, um herauszufinden, zu welchem Paket diese Datei gehört und installiere sie. Denke daran, dass du wahrscheinlich die -dev-Version des Pakets benötigst, die Kopf- oder Konfigurationsdateien enthält, die FreeCAD benötigt, um das Paket zu verwenden.

### Im Quellcode Bau 

In-source builds sind in Ordnung, wenn du eine Version von FreeCAD schnell kompilieren möchtest und nicht vorhast, den Quellcode häufig zu aktualisieren. In diesem Fall kannst Du das kompilierte Programm und die Quelle einfach durch Löschen eines einzelnen Ordners entfernen.

Wechsle in das Quellverzeichnis und zeige `cmake` auf das aktuelle Verzeichnis (gekennzeichnet durch einen einzelnen Punkt):


{{Code|lang=bash|code=
cd freecad-source
cmake . -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
make -j$(nproc --ignore=2)
}}

Die FreeCAD Ausführdatei befindet sich dann im `freecad-source/bin` Verzeichnis.

### Wie Du dein Quellcode Verzeichnis reparieren kannst 

Wenn du versehentlich eine Kompilierung im Quellcode Verzeichnis durchgeführt oder seltsame Dateien hinzugefügt hast und den Inhalt nur im ursprünglichen Quellcode wiederherstellen möchtest, kannst du die folgenden Schritte durchführen.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

Die erste Zeile löscht die Datei `.gitignore`. Dadurch wird sichergestellt, dass die folgenden Clean und Reset Befehle sich auf alles im Verzeichnis auswirken und keine Elemente ignorieren, die den Ausdrücken in `.gitignore` entsprechen. Die zweite Zeile löscht alle Dateien und Verzeichnisse, die nicht vom git Repository verfolgt werden; dann setzt der letzte Befehl alle Änderungen an den überwachten Dateien zurück, einschließlich des ersten Befehls, der die Datei `.gitignore` gelöscht hat.

Wenn du das Quellverzeichnis nicht löschst, können nachfolgende Durchläufe von `cmake` keine neuen Optionen für das System erfassen, wenn sich der Code ändert.

### Konfiguration

Durch die Übergabe verschiedener Optionen an `cmake` kannst Du ändern, wie FreeCAD kompiliert wird. Die Syntax ist wie folgt.


```python
cmake -D <var>:<type>=<value> $SOURCE_DIR
```

Wobei `$SOURCE_DIR` das Verzeichnis ist, das den Quellcode enthält. Der `<type>` kann in den meisten Fällen weggelassen werden. Das Leerzeichen nach der Option `-D` kann ebenfalls weggelassen werden.

Zum Beispiel, um den Bau der [FEM Arbeitsbereich](FEM_Workbench/de.md) zu vermeiden:


{{Code|lang=bash|code=
cmake -D BUILD_FEM:BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

Alle möglichen Variablen sind in der `InitializeFreeCADBuildOptions.cmake` Datei aufgelistet, die sich im `cMake/FreeCAD_Helpers` Verzeichnis befindet. Suche in dieser Datei nach dem Wort `option`, um zu den einstellbaren Variablen zu gelangen und deren Standardwerte zu sehen.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Alternativ kannst Du den Befehl `cmake -LH` verwenden, um die aktuelle Konfiguration und damit alle Variablen aufzulisten, die geändert werden können. Du kannst auch `cmake-gui` installieren und verwenden, um eine grafische Oberfläche zu starten, die alle Variablen anzeigt, die geändert werden können. In den nächsten Abschnitten listen wir einige der wichtigsten Optionen auf, die du vielleicht verwenden möchtest.

#### Für einen Fehlersuch Bau 

Erstelle einen `Debug` Build, um Abstürze in FreeCAD zu beheben. Beachte, dass mit diesem Build die [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) bei komplexen Skizzen sehr langsam wird.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}

#### Für ein Veröffentlichungs Bau 

Erstelle einen `Release` Build, um Code zu testen, der nicht abstürzt. Ein `Release` Build wird viel schneller ausgeführt als ein `Debug` Build.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}

#### Bauen gegen Python 3 und Qt5 

Standardmäßig wird FreeCAD 0.19 und früher für Python 2 und Qt4 gebaut. Seit diese beiden Pakete veraltet sind, ist es besser, für Python 3 und Qt5 zu bauen. Die Unterstützung für Python 2 und Qt4 wurde in FreeCAD 0.20 entfernt und es ist nicht notwendig, Qt5 und Python 3 explizit zu aktivieren, wenn die neuesten Entwicklungsversionen kompiliert werden.

In einer modernen Linux Distribution müsse nur zwei Variablen angegeben werden, die die Verwendung von Qt5 und den Pfad zum Python Interpreter angeben.

Für 0.19: {{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Für 0.20\_dev: {{Code|lang=bash|code=
cmake ../freecad-source
}}

Beachte, dass es beim Wechsel zwischen 0.19 und den 0.20 Builds notwendig sein kann, CMakeCache.txt zu löschen, bevor cmake ausgeführt wird.

#### Bauen für eine bestimmte Python Version 

Wenn die standardmäßige `python` ausführbare Datei in Deinem System ein symbolischer Link zu Python 2 ist, wird `cmake` versuchen, FreeCAD für diese Version zu konfigurieren. Du kannst eine andere Version von Python wählen, indem du den Pfad zu einer bestimmten ausführbaren Datei angibst:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Wenn das nicht funktioniert, musst Du möglicherweise zusätzliche Variablen definieren, die auf die gewünschten Python Bibliotheken und Include Verzeichnisse verweisen:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

Es ist möglich, mehrere unabhängige Versionen von Python im selben System zu haben, so dass die Speicherorte und Versionsnummern deiner Python Dateien von deiner jeweiligen Linux Distribution abhängen. Verwende `python3 -V`, um die Version von Python anzuzeigen, die Du gerade verwendest; nur die ersten beiden Zahlen sind notwendig; wenn das Ergebnis beispielsweise `Python 3.6.8` ist, musst Du die Verzeichnisse angeben, die sich auf die Version 3.6 beziehen. Wenn Du die richtigen Verzeichnisse nicht kennst, versuche mit dem Befehl `locate` nach ihnen zu suchen.


```python
locate python3.6
```

Du kannst `python3 -m site` in einem Terminal verwenden, um das Verzeichnis `site-packages` zu bestimmen, oder `dist-packages` für Debian Systeme.

#### Bauen mit Qt Creator gegen Python 3 und Qt5 

1\. Qt Creator starten.

2\. Klicke auf {{MenuCommand/de|Projekt öffnen}}.

3\. Wechsle zu dem Verzeichnis, in dem sich der Quellcode befindet, `freecad-source/`, und wähle die oberste `CMakeLists.txt` Datei.

4\. Durch Wahl der Datei, wird automatisch `cmake` darauf ausgeführt, aber es kann fehlschlagen, wenn die geeigneten Optionen nicht korrekt eingestellt sind.

5\. Gehe zu {{MenuCommand/de|Projekte → Bauen & Ausführen → Importierter Bausatz → Bau → Build Einstellungen → CMake}}. Setze das entsprechende Build Verzeichnis, `freecad-build/`.

6\. Setze die geeigneten Variablen im Schlüssel-Wert Dialogfeld `String` und `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
BUILD_QT5=ON
```

7\. Wenn die Variablen das Projekt nicht korrekt laden, musst du möglicherweise zu {{MenuCommand/de|Projekte → Bausätze verwalten → Bausätze → Standard (oder importierter Bausatz oder ähnliches) → CMake Konfiguration}} gehen. Drücke dann **Change** und füge die geeignete Konfiguration wie oben beschrieben hinzu. Möglicherweise musst du weitere Variablen über die Python Pfade hinzufügen, falls das System Python nicht gefunden wird. 
```python
PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
BUILD_QT5:BOOL=ON
```

7.1. Drücke **Apply**, dann **OK**.

7.2. Stelle sicher, dass die restlichen Optionen korrekt eingestellt sind, z.B. sollte {{MenuCommand/de|Qt Version}} eine im System installierte aktuelle Version sein, wie `Qt 5.9.5 in PATH (qt5)`.

Drücke **Apply**, dann **OK** um die Konfiguration zu schließen.

Das `cmake` Programm sollte wieder automatisch ausgeführt werden, und es sollte das gesamte Schlüssel Wert Dialogfeld mit allen konfigurierbaren Variablen füllen.

8\. Gehe zu {{MenuCommand/de|Projekte → Bauen & Ausführen → Importierter Bausätze → Ausführen → Ausführen → Ausführen Einstellungen → Ausführen → Ausführen → Konfiguration Ausführen}} und wähle `FreeCADMain`, um die grafische Version von FreeCAD zu kompilieren, oder `FreeCADMainCMD`, um nur die Befehlszeilenversion zu kompilieren.

9\. Abschließend gehe zum Menü {{MenuCommand/de|Bau → Bau Projekt "FreeCAD"}}. Wenn es sich um eine neue Kompilierung handelt, sollte sie je nach Anzahl der zur Verfügung stehenden Prozessoren mehrere Minuten, inklusive Stunden, dauern.

#### Qt Designer Zusatzprogramm 

Wenn du Qt Code für FreeCAD entwickeln möchtest, benötigst du die Qt Designer Zusatzprogramm, das alle benutzerdefinierten Widgets von FreeCAD bereitstellt.

Gehe in ein Hilfsverzeichnis des Quellcodes, den Run `qmake` mit der angegebenen Projektdatei, um eine `Makefile` zu erstellen; führe dann `make` aus, um das Zusatzprogramm zu kompilieren.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Wenn du für Qt5 kompilierst, stelle sicher, dass die Binärdatei `qmake` diejenige für diese Version ist, so dass die resultierende `Makefile` die notwendigen Informationen für Qt5 enthält.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

wobei `$QT_DIR` das Verzeichnis ist, das Qt Binärbibliotheken speichert, z.B. `/usr/lib/x86_64-linux-gnu/qt5`.

Die erstellte Bibliothek ist `libFreeCAD_widgets.so`, die nach `$QT_DIR/plugins/designer` kopiert werden muss.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}

#### Externes oder internes Pivy 

Bisher wurde eine Version von Pivy in den Quellcode von FreeCAD (intern) aufgenommen. Wenn Du die Kopie von Pivy (extern) Deines Systems verwenden möchtest, musst Du Folgendes verwenden -DFREECAD_USE_EXTERNAL_PIVY=1.

Die Verwendung von externem Pivy wurde bei der Entwicklung von FreeCAD 0.16 zum Standard, so dass diese Option nicht mehr manuell gesetzt werden muss.

#### Doxygen-Dokumentation 

Wenn Du Doxygen installiert hast, kannst Du die Quellcode Dokumentation erstellen. Siehe [source documentation/de](source_documentation/de.md) für Anweisungen.

### Zusätzliche Dokumentation 

Der Quellcode von FreeCAD ist sehr umfangreich, und mit CMake ist es möglich, viele Optionen zu konfigurieren. Das Erlernen der vollständigen Nutzung von CMake kann nützlich sein, um die richtigen Optionen für Ihre speziellen Bedürfnisse auszuwählen.

-   [CMake Referenzdokumentation](https://cmake.org/documentation/) von Kitware.
-   [Wie man ein CMake-basiertes Projekt erstellt](https://preshing.com/20170511/how-to-build-a-cmake-based-project/) (Blog) durch Preshing auf Programmierung.
-   [CMakes Skriptsprache in 15 Minuten lernen](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (Blog) durch Preshing auf Programmierung.

### Ein Debian Paket erstellen 

Wenn Du planst, ein Debian-Paket aus den Quellen zu erstellen, musst Du zuerst bestimmte Pakete installieren:


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Gehe in das FreeCAD Verzeichnis und wähle


{{Code|lang=bash|code=
debuild
}}

Sobald das Paket erstellt ist, kannst Du mit `lintian` prüfen, ob das Paket Fehler enthält.


{{Code|lang=bash|code=
lintian freecad-package.deb
}}

## Aktualisierung des Quellcodes 

Das CMake System ermöglicht es Dir, den Quellcode intelligent zu aktualisieren und nur die Änderungen neu zu kompilieren, was spätere Kompilierungen beschleunigt.

Gehe an den Speicherort, an dem der FreeCAD Quellcode zuerst heruntergeladen wurde, und ziehe den neuen Code:


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Gehe dann in das Build Verzeichnis, in dem der Code ursprünglich kompiliert wurde, und führe `cmake` unter Angabe des aktuellen Verzeichnisses (gekennzeichnet durch einen Punkt) aus; löse dann die Neukompilierung mit `make` aus.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}

## Fehlerbehebung

### Für 64 Bit Systeme 

Beim Erstellen von FreeCAD für 64-Bit gibt es ein bekanntes Problem mit dem OpenCASCADE (OCCT) 64-Bit Paket. Um FreeCAD richtig zum Laufen zu bringen, musst du möglicherweise das Skript `configure` ausführen und zusätzlich `CXXFLAGS` einstellen:


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

Für Debian basierte Systeme wird diese Option nicht benötigt, wenn die vorkompilierten OpenCASCADE Pakete verwendet werden, da diese intern die richtigen `CXXFLAGS` setzen.

## Automatische Build Skripte 

Hier findest du alles, was du für einen vollständigen Aufbau von FreeCAD benötigst. Es ist ein Ein-Skript-Ansatz und funktioniert auf einer frisch installierten Linux Distribution. Die Befehle fragen nach dem Root Passwort für die Installation von Paketen und neuen Online Repositorien. Diese Skripte sollten auf 32 und 64 Bit Versionen laufen. Sie sind für verschiedene Versionen geschrieben, werden aber wahrscheinlich auch auf einer späteren Version mit oder ohne größere Änderungen laufen.

Wenn du ein solches Skript für deine bevorzugte Distribution hast, diskutiere es bitte auf dem [FreeCAD Forum](https://forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134), damit wir es einbauen können.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

Diese Skripte bieten eine zuverlässige Möglichkeit, die richtigen Abhängigkeiten zu installieren, die für die Erstellung und Ausführung von FreeCAD auf Ubuntu erforderlich sind. Sie nutzen die Ubuntu Personal Package Archives (PPA) und sollten an jeder Version von Ubuntu arbeiten, die von der PPA erfasst wird. Die [freecad-tages freecad-tages](https://launchpad.net/~freecad-tainers/+archive/ubuntu/freecad-tages) PPA zielt auf aktuelle Versionen von Ubuntu ab, während die [freecad-stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA zielt auf offiziell unterstützte Versionen von Ubuntu ab.

Dieses Skript installiert den täglich erstellten Schnappschuss von FreeCAD und seinen Abhängigkeiten. Es fügt das tägliche Repository hinzu, holt die Abhängigkeiten, um diese Version zu erstellen, und installiert die erforderlichen Pakete. Anschließend wird der Quellcode in ein bestimmtes Verzeichnis gezogen, ein Build-Verzeichnis erstellt und in dieses gewechselt, die Kompilierungsumgebung mit `cmake` konfiguriert und schließlich das gesamte Programm mit `make` erstellt. Speichere das Skript in einer Datei, mache es ausführbar und führe es aus, verwende aber nicht `sudo`; Superuser Rechte werden nur für ausgewählte Befehle abgefragt.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

Wenn du möchtest, kannst du die vorkompilierte Version von FreeCAD (`freecad-daily`) deinstallieren, während du die Abhängigkeiten an Ort und Stelle lässt, aber wenn du dieses Paket installiert lässt, kann der Paketmanager seine Abhängigkeiten auch auf dem neuesten Stand halten; dies ist vor allem nützlich, wenn du die Entwicklung von FreeCAD verfolgen und die Quellen aus dem Git Repository ständig aktualisieren und kompilieren willst.

Das vorherige Skript geht davon aus, dass du die neueste Version von FreeCAD kompilieren möchtest, also benutzt du das \"tägliche\" Repository, um die Abhängigkeiten zu erhalten. Du kannst jedoch stattdessen die Build Abhängigkeiten der \"stabilen\" Version für deine aktuelle Ubuntu-Version erhalten. Wenn dies der Fall ist, ersetze den oberen Teil des vorherigen Skripts durch die folgenden Anweisungen. Für Ubuntu 12.04 lasse `---enable-source` vom Befehl aus.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Sobald du das Paket `freecad` aus dem Repository `freecad-stable` installiert hast, ersetzt es die FreeCAD Ausführdatei, die im Universe Ubuntu Repository verfügbar ist. Die ausführbare Datei wird einfach `freecad` genannt und nicht `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">

Für die Kompilierung von FreeCAD werden keine externen Repositorien benötigt. Es gibt jedoch eine Inkompatibilität mit python3-devel, die entfernt werden muss. FreeCAD kann aus GIT kompiliert werden.


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

Da Du git verwendest, musst Du beim nächsten Mal, wenn Du kompilieren möchtest, nicht alles klonen, sondern ziehst einfach von git ab und kompilierst erneut.


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

Veröffentlicht von Benutzer [http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) im Forum.


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

### Bogen mit AUR 


<div class="mw-collapsible-content">

[Arch User Repository (AUR)](https://aur.archlinux.org/) ist eine Sammlung von benutzerdefinierten Rezepten zum Erstellen von Paketen, die nicht offiziell von Distributionsmoderatoren / Gemeinschaft unterstützt werden. Sie sind in der Regel sicher. Du kannst sehen, wer das Paket gepflegt hat und wie lange. Es wird empfohlen, die Konstruktionsdateien zu überprüfen. Auch nicht quelloffene Software ist in diesem Bereich verfügbar, auch wenn sie von der offiziellen Eigentümerfirma gepflegt wird.

Voraussetzung: git

Schritte :

1.  Öffne ein Terminal. Optional kann ein Verzeichnis erstellt werden, z.B. {{incode | mkdir git}}. Optional kann das Verzeichnis geändert werden, z.B. `cd git`.
2.  Klone das AUR-Repository : `git clone http://aur.archlinux.org/packages/freecad-git`
3.  Gib den AUR Repository Ordner ein: `cd freecad-git`
4.  Kompiliere mit [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. Das Flag -s oder \--syncdeps installiert auch die erforderlichen Abhängigkeiten.
5.  Installiere das erstellte Paket : `makepkg --install` oder doppelklicke auf das pkgname-pkgver.pkg.tar.xz in Deinem Dateibrowser.

Um FreeCAD auf den neuesten Stand zu bringen, wiederhole einfach ab Schritt 3. Aktualisiere AUR repo, wenn es eine Bruchänderung im Rezept oder neue Funktionen gibt, indem Du `git checkout -f` im Ordner verwendest.


{{docnav/de
|[Kompilieren unter Windows](Compile_on_Windows/de.md)
|[Kompilieren unter MacOS](Compile_on_MacOS/de.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/de
