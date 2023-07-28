# Compile on MacOS/de
**Es gibt einen experimentellen FreeCAD Docker Container, der für die FreeCAD Entwicklung getestet wird. Lies mehr darüber unter [[Compile on Docker/de|
Kompilieren unter Docker]]**


{{TOCright}}



## Übersicht

Diese Seite beschreibt, wie der neueste FreeCAD-Quellcode unter macOS kompiliert wird. Für andere Plattformen, siehe [Kompilieren](Compiling/de.md).

Diese Anleitung wurde auf macOS Catalina mit Standard XCode 11.6 getestet. Es ist bekannt, dass sie auf macOS BigSur Beta mit XCode 12.0 Beta funktioniert. Wenn du planst, XCode Beta zu verwenden, stelle bitte sicher, dass du die Befehlszeilenwerkzeuge add on über ein dmg Paket herunterlädst, um einige libz Abhängigkeitsprobleme zu umgehen.

Diese Seite dient als Schnellstart und ist nicht als umfassende Beschreibung aller verfügbaren Build-Optionen gedacht.

Wenn du nur die neueste Vorabversion von FreeCAD evaluieren möchtest, kannst du vorgefertigte Binärdateien [von hier](https://github.com/FreeCAD/FreeCAD/releases) herunterladen.



## Installationsvoraussetzungen

Die folgende Software muss installiert sein, um den Bauprozess zu unterstützen.



### Homebrew Paketverwalter 

Homebrew ist ein kommandozeilenbasierter Paketmanager für macOS. Die [Homebrew Hauptseite](https://brew.sh/) bietet eine Installations Befehlszeile, die du einfach in ein Terminalfenster einfügst.

### CMake

CMake ist ein Kompilierwerkzeug, das eine Kompilierkonfiguration auf der Grundlage von Variablen erzeugt, die du angibst. Du gibst dann den Befehl \"make\" aus, um diese Konfiguration tatsächlich zu erstellen. Die Kommandozeilenversion von CMake wird automatisch als Teil der Homebrew Installation (siehe oben) installiert. Wenn du es vorziehst, eine GUI Version von CMake zu verwenden, kannst du es von [hier](https://www.cmake.org/downloadDownload) herunterladen.



## Abhängigkeiten einrichten 

FreeCAD unterhält eines Homebrew-\"Fass\" (Homebrew-Cask), das die erforderlichen Formeln und Abhängigkeiten installiert. Gib die folgenden Brau-Befehle in deinem Terminal ein.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad
```


{{Incode|brew install}}

kann eine ganze Weile dauern, also genug Zeit, um sich ein Getränk zu holen :-).

Alternativ können die einzelnen Abhängigkeiten manuell hinzugefügt werden; dafür werden die folgenden Pakete mit {{Incode|brew install ...}} installiert:

-    `cmake`
    

-    `swig`
    

-    `boost`
    

-    `boost-python3`
    

-    `eigen`
    

-    `gts`
    

-    `vtk`
    

-    `xerces-c`
    

-    `qt@5`\- Zurzeit wird nur Qt5 unterstützt, Unterstützung für Qt6 ist in Arbeit

-    `opencascade`
    

-    `doxygen`
    

-    `pkgconfig`
    

-    `coin3d`\- Zur Zeit des Schreibens (Nov. 2022) installiert dies nur eine unbrauchbare Version von pyside@2 als Abhängigkeit.

Es gibt Pakete, die nur zur Verfügung stehen, wenn das FreeCAD-Fass angezapft wurde (you tapped the freecad cask): Dafür muss (`brew tap freecad/freecad`) ausgeführt werden. Einigen historischen Fehlerumgehungen zur Zeit des Schreibens (Nov. 2022) ist geschuldet, dass die von Homebrew installierten Versionen von PySide2 und Shiboken2 unbrauchbar sind, da sie die Verwendung von Py_Limited_API erzwingen, das FreeCAD nicht unterstützt. Es ist zu erwarten, das diese Umgehung in den nächsten Monaten entfernt wird, aber in der Zwischenzeit müssen die Versionen PySide und Shiboken aus dem FreeCAD-Fass verwendet werden. Mit `brew install ...` werden die folgenden Pakete installiert:

-    `freecad/freecad/pyside2@5.15.5`
    

-    `freecad/freecad/shiboken2@5.15.5`
    

-    `freecad/freecad/med-file`
    

-    `freecad/freecad/netgen`
    

Außerdem müssen PySide und Shiboken noch \"verknüpft\" werden:


```python
brew link freecad/freecad/pyside2@5.15.5 freecad/freecad/shiboken2@5.15.5
```

In manchen Fällen verwenden die von Homebrew installierten Pakete nicht dieselbe Python-Version: Zur Zeit des Schreibens verwendet z.B. PySide2 Python 3.10, aber boost-python3 verwendet Python 3.11. Während ein \"roll back\" der fortschrittlicheren Version möglich ist (so dass in diesem Falle boost-python3 Python 3.10 verwendet), bleibt es eine fortschrittlichere Version und in vielen Fällen ist es am besten, auf die nächste Aktualisierung des anderen Pakets zu warten. Wenn man trotzdem diesen Weg gehen möchte, sollte man sich den Befehl \"brew extract\" ansehen, den man zum Extrahieren einer Formel in ein neues Fass (typischerweise freecad/freecad) verwenden kann. Die Formel kann dann nach belieben bearbeitet werden.

Der Pfad zu Qt muss angegeben werden: Qt5 wird derzeit unterstützt, während die Unterstützung von Qt6 noch in Arbeit ist. FREECAD_QT_VERSION auf \"Auto\" oder \"5\" setzen, um Qt5 (die Voreinstellung) auszuwählen. Auf der Komandozeile gibt man etwas ein, wie:


```python
cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DQt5_DIR="/usr/local/Cellar/qt@5/5.15.7/lib/cmake/Qt5" \
  -DPySide2_DIR="/usr/local/Cellar/pyside2@5.15.5/5.15.5/lib/cmake/PySide2-5.15.5" \
  -DShiboken2_DIR="/usr/local/Cellar/shiboken2@5.15.5/5.15.5_1/lib/cmake/Shiboken2-5.15.5" \
  ../freecad-source
```



## Quellcode beziehen 

In den folgenden Anweisungen werden die Quell- und Kompilier-Ordner nebeneinander erstellt unter


```python
/Users/username/FreeCAD
```

aber du kannst beliebige Ordner verwenden.


```python
mkdir ~/FreeCAD
cd ~/FreeCAD
```

Der folgende Befehl wird das FreeCAD git Repositorium in ein Verzeichnis namens FreeCAD-git klonen.


```python
git clone https://github.com/FreeCAD/FreeCAD FreeCAD-git
```

Erstelle den Kompilierordner.


```python
mkdir ~/FreeCAD/build
```



## CMake ausführen 

Zunächst führen wir CMake aus, um die Kompilierkonfiguration zu erzeugen. Mehrere Optionen müssen an CMake übergeben werden. Die folgende Tabelle beschreibt die Optionen und gibt einige Hintergrundinformationen.



### CMake Optionen 

  Name                       Wert                                     Anmerkungen
    
  CMAKE_BUILD_TYPE           Release (STRING)                         Release oder Debug. Debug wird im Allgemeinen für Tests auf Entwicklerebene verwendet, kann aber auch für Tests auf Benutzerebene und zur Fehlersuche erforderlich sein.
  CMAKE_PREFIX_PATH          \"/usr/local/opt/qt5152;\" \... (PATH)   Erforderlich für die Erstellung mit Qt5. Siehe Hinweis unten. Du musst auch den Pfad zu den VTK Bibliotheken und NGLIB Bibliotheken der cmake Konfigurationsdatei hinzufügen.
  FREECAD_CREATE_MAC_APP     1 (BOOL)                                 Erzeugt ein FreeCAD.app Bündel an dem in CMAKE_INSTALL_PREFIX angegebenen Ort, wenn der Befehl \'make install\' ausgegeben wird.
  CMAKE_INSTALL_PREFIX       \"./..\" (PATH)                          Pfad, wo du das FreeCAD.app Bündel erzeugen möchtest.
  FREECAD_USE_EXTERNAL_KDL   1 (BOOL)                                 Erforderlich, falls die FEM-Werkzeuge kompiliert werden sollen.
  BUILD_FEM_NETGEN           1 (BOOL)                                 Erforderlich.

Hinweis: Kommandozeile zum Erzeugen von CMAKE_PREFIX_PATH:

ls -d $(brew list -1 | grep qt | tail -1 | xargs brew --cellar)/*/lib/cmake

### CMake GUI 

Open the CMake app, and fill in the source and build folder fields. In this example, it would be **/Users/username/FreeCAD/FreeCAD-git** for the source, and **/Users/username/FreeCAD/build** for the build folder.

Next, click the **Configure** button to populate the list of configuration options. This will display a dialog asking you to specify what generator to use. Leave it at the default **Unix Makefiles.** Configuring will fail the first time because there are some options that need to be changed. Note: You will need to check the **Advanced** checkbox to get all of the options.

Set options from the table above, then click **Configure** again and then **Generate**.



### CMake Befehlszeile 

Gib das Folgende in das Terminal ein.


```python
export PREFIX_PATH="/usr/local/opt/qt5152;\
/usr/local/Cellar/nglib/v6.2.2007/Contents/Resources;\
/usr/local/Cellar/vtk@8.2/8.2.0_1/lib/cmake;"
```


```python
$cd ~/FreeCAD/build
$cmake \
  -DCMAKE_BUILD_TYPE="Release"   \
  -DBUILD_QT5=1                  \
  -DWITH_PYTHON3=1               \
  -DCMAKE_PREFIX_PATH="$PREFIX_PATH" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DFREECAD_USE_EXTERNAL_KDL=1   \
  -DCMAKE_CXX_FLAGS='-std=c++14' \
  -DBUILD_FEM_NETGEN=1           \
  -DFREECAD_CREATE_MAC_APP=1     \
  -DCMAKE_INSTALL_PREFIX="./.."  \
  ../FreeCAD-git/

```



## make ausführen 

Finally, from a terminal run **make** to compile and link FreeCAD, and generate the app bundle.


```python
cd ~/FreeCAD/build
make -j5 install
```

The -j option specifies how many make processes to run at once. One plus the number of CPU cores is usually a good number to use. However, if compiling fails for some reason, it is useful to rerun make without the -j option, so that you can see exactly where the error occurred.

Siehe auch [Kompilierung - Beschleunigen](Compiling_(Speeding_up)/de.md).

Wenn das Kompilieren ohne Fehler abgeschlossen ist, kannst du FreeCAD nun durch einen Doppelklick auf die ausführbare Datei im Finder starten.



## Aktualisierung von Github 

FreeCAD development happens fast; every day or so there are bug fixes or new features. To get the latest changes, use git to update the source directory (see [Source code management](Source_code_management.md)), then re-run the CMake and make steps above. It is not usually necessary to start with a clean build directory in this case, and subsequent compiles will generally go much faster than the first one.



## Kompilieren mit Qt4 und Python 2.7 

FreeCAD hat von Qt 4 auf Qt 5 sowie Homebrew umgestellt. Qt 4 ist nach der Umstellung auf Qt 5 nicht mehr als Option für neue Builds unter macOS verfügbar. Python 2.7 ist für Homebrew und das kommenden macOS veraltet und wird von uns auch für macOS Bau nicht mehr unterstützt.



## Fehlersuche



### Segfault beim Start von Qt5 

If Qt4 was previously installed via brew, and you then build with Qt5, you may get a EXC_BAD_ACCESS (SEGSEGV) exception when launching the new Qt5 build. The fix for this is to manually uninstall Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```

### Fortran

*\"No CMAKE_Fortran_COMPILER could be found.\"* during configuration - Older versions of FreeCAD will need a fortran compiler installed. With Homebrew, do \"brew install gcc\" and try configuring again, giving cmake the path to Fortran ie -DCMAKE_Fortran_COMPILER=/opt/local/bin/gfortran-mp-4.9 . Or, preferably use a more current version of FreeCAD source!

### FreeType

When using CMake versions older than 3.1.0, it\'s necessary to set CMake variable FREETYPE_INCLUDE_DIR_freetype2 manually, eg /usr/local/include/freetype2

### Additional Build Instructions 

FreeCAD can be built against the latest git master hosted on github, and launched from a CLI using libraries provided by the homebrew-freecad tap. For a complete list of build instructions see [here](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MacOS/de
