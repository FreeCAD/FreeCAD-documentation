# Compile on MacOS/ro
**There is an experimental FreeCAD Docker container that is being tested for FreeCAD development. Read more about it at [[Compile on Docker]]**


{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Această pagină descrie modul de compilare a celei mai recente surse FreeCAD pe macOS X. \'\' Latest \'\' înseamnă cel mai recent angajament al filialei principale a depozitului Github al FreeCAD.


</div>

These instructions have been tested on macOS Catalina with standard XCode 11.6. It is known to work on macOS BigSur Beta with XCode 12.0 beta. If you plan to use XCode Beta, please be sure to download Command Line Tools add on through a dmg package to workaround some libz dependency issues.

Această pagină servește ca un început rapid și nu intenționează să fie cuprinzătoare în ceea ce privește descrierea tuturor opțiunilor de compilare disponibile.

If you just want to evaluate the latest pre-release build of FreeCAD, you can download pre-built binaries [from here](https://github.com/FreeCAD/FreeCAD/releases).


<div class="mw-translate-fuzzy">

## Instalați cerințele preliminare 

Următorul software trebuie instalat pentru a sprijini procesul de construire.


</div>

The following software must be installed to support the build process.


<div class="mw-translate-fuzzy">

### Managerul de pachete Homebrew 

Homebrew este un manager de pachete de linie de comandă pentru MacOS. The [Homebrew main page](https://brew.sh/) furnizează o linie de comandă de instalare pe care pur și simplu o inserați într-o fereastră de terminal.


</div>

Homebrew is a command line based package manager for macOS. The [Homebrew main page](https://brew.sh/) provides an installation command line that you simply paste into a terminal window.


<div class="mw-translate-fuzzy">

### CMake

CMake este un instrument de complilare care construiește o configurație de complilare bazată pe variabilele pe care le specificați. Apoi, emiteți comanda \"make\" pentru a compila configurația respectivă. The command-line version of CMake is automatically installed as part of the Homebrew installation, above. If you prefer to use a GUI version of CMake, you can download it from [here](https://www.cmake.org/downloadDownload).


</div>

CMake is a build tool that generates a build configuration based on variables you specify. You then issue the \'make\' command to actually build that configuration. The command-line version of CMake is automatically installed as part of the Homebrew installation, above. If you prefer to use a GUI version of CMake, you can download it from [here](https://www.cmake.org/downloadDownload).


<div class="mw-translate-fuzzy">

## Instalarea dependențelor 

FreeCAD menține un \"robinet\" al Homebrew care instalează formulele și dependențele necesare. Eliberați următoarele comenzi de brew în terminalul dvs.


</div>

FreeCAD maintains a Homebrew \'tap\' which installs the required formulas and dependencies. Issue the following brew commands in your terminal.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad --with-packaging-utils
```


<div class="mw-translate-fuzzy">

Notes:

1.  \'brew install\' may take quite a while, so you may want go grab a beverage. :-)


</div>


<div class="mw-translate-fuzzy">

## Get the source 

În instrucțiunile de mai jos, sunt create soursă și folderele compilate unele sub altele


</div>

In the following instructions, the source and build folders are created side-by-side under


```python
/Users/username/FreeCAD
```

but you can use whatever folders you want.


```python
mkdir ~/FreeCAD
cd ~/FreeCAD
```

The following command will clone the FreeCAD git repository into a directory called FreeCAD-git.


```python
git clone https://github.com/FreeCAD/FreeCAD FreeCAD-git
```

Create the build folder.


```python
mkdir ~/FreeCAD/build
```

## Run CMake 

Next, we will run CMake to generate the build configuration. Several options must be passed to CMake. The following table describes the options and gives some background.

### CMake Options 


<div class="mw-translate-fuzzy">

+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Name                        | Value                                                | Notes                                                                                                                                      |
+=============================+======================================================+============================================================================================================================================+
| CMAKE\_BUILD\_TYPE          | Release (STRING)                                     | Release or Debug. Debug is generally used for developer-level testing but may also be required for user-level testing and troubleshooting. |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| BUILD\_QT5                  | 1 (BOOL)                                             | Required to build with Qt5.                                                                                                                |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| CMAKE\_PREFIX\_PATH         | \"/usr/local/Cellar/qt\@5.6/5.6.2/lib/cmake\" (PATH) | Required to build with Qt5. See note below.                                                                                                |
|                             |                                                      |                                                                                                                                            |
|                             |                                                      |                                                                                                                                  |
|                             |                                                      | </div>                                                                                                                                     |
|                             |                                                      |                                                                                                                                         |
|                             |                                                      |                                                                                                                                  |
|                             |                                                      | <div class="mw-translate-fuzzy">                                                                                                           |
|                             |                                                      |                                                                                                                                         |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| FREECAD\_CREATE\_MAC\_APP   | 1 (BOOL)                                             | Create a FreeCAD.app bundle at the location specified in CMAKE\_INSTALL\_PREFIX, when the \'make install\' command issued.                 |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| CMAKE\_INSTALL\_PREFIX      | \"./..\" (PATH)                                      | Path where you want to generate the FreeCAD.app bundle.                                                                                    |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| FREECAD\_USE\_EXTERNAL\_KDL | 1 (BOOL)                                             | Required.                                                                                                                                  |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| BUILD\_FEM\_NETGEN          | 1 (BOOL)                                             | Required.                                                                                                                                  |
+-----------------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+


</div>

Note: Command line to generate CMAKE\_PREFIX\_PATH:

ls -d $(brew list -1 | grep qt | tail -1 | xargs brew --cellar)/*/lib/cmake


<div class="mw-translate-fuzzy">

### CMake GUI 

Deschideți aplicația CMake și completați câmpurile sursă și construiți dosarul. În acest exemplu, ar fi **/Users/username/FreeCAD/FreeCAD-git**pentru sursă, și **/Users/username/FreeCAD/build** pentru construirea folderului .


</div>

Open the CMake app, and fill in the source and build folder fields. In this example, it would be **/Users/username/FreeCAD/FreeCAD-git** for the source, and **/Users/username/FreeCAD/build** for the build folder.

Next, click the **Configure** button to populate the list of configuration options. This will display a dialog asking you to specify what generator to use. Leave it at the default **Unix Makefiles.** Configuring will fail the first time because there are some options that need to be changed. Note: You will need to check the **Advanced** checkbox to get all of the options.

Set options from the table above, then click **Configure** again and then **Generate**.


<div class="mw-translate-fuzzy">

Set options from the table above, then click **Configure** again and then **Generate**.

### CMake command line 

Enter the following in the terminal.


</div>

Enter the following in the terminal.


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


<div class="mw-translate-fuzzy">

## Run make 

În cele din urmă, de la un terminal rulați **make** pentru a compila și a lega FreeCAD și a genera pachetul de aplicații.


</div>

Finally, from a terminal run **make** to compile and link FreeCAD, and generate the app bundle.


```python
cd ~/FreeCAD/build
make -j5 install
```

Opțiunea -j specifică câte procese de procesare se execută simultan. Unul plus numărul de nuclee CPU este, de obicei, un număr bun de utilizat. Cu toate acestea, dacă compilarea eșuează dintr-un motiv oarecare, este utilă reluarea efectuării fără opțiunea -j, astfel încât să puteți vedea exact unde a apărut eroarea.

A se vedea și [Compiling - Speeding up](Compiling_(Speeding_up).md).

Dacă ați finalizat fără erori, puteți lansa FreeCAD făcând dublu clic pe executabilul din Finder


<div class="mw-translate-fuzzy">

## Updating după Github 

Dezvoltarea FreeCAD are loc rapid; aproape în fiecare zi sunt bug fixe sau noi funcionalități. Pentru a obține cele mai recente modificări, utilizați git pentru a actualiza directorul sursă (consultați [Source code management](Source_code_management.md)), apoi re-executați CMake și parcurgeți pașii de mai sus. De obicei, nu este necesar să începeți cu un director de compliare curat în acest caz, iar compilatele ulterioare vor merge, în general, mult mai repede decât prima.


</div>

FreeCAD development happens fast; every day or so there are bug fixes or new features. To get the latest changes, use git to update the source directory (see [Source code management](Source_code_management.md)), then re-run the CMake and make steps above. It is not usually necessary to start with a clean build directory in this case, and subsequent compiles will generally go much faster than the first one.


<div class="mw-translate-fuzzy">

## Compilarea cu Qt4 

FreeCAD a trecut de la Qt 4 la Qt 5. Dacă trebuie să complilați cu Qt4, sunt necesari următorii pași suplimentari.


</div>

FreeCAD has transitioned from Qt 4 to Qt 5 as well as homebrew. Qt 4 is no longer available as an option for new build on macOS following Qt 5 transition. Python 2.7 has been deprecated within homebrew and upcoming macOS and we do not support it anymore for macOS build either.

## Depanare


<div class="mw-translate-fuzzy">

### Segfault on Qt5 launch 

În cazul în care Qt4 a fost instalat anterior via brew, și apoi ați construit cu Qt5, puteți obține o excepție EXC\_BAD\_ACCESS (SEGSEGV) atunci când lansați compilarea nouli Qt5 . Remedierea pentru aceasta este de a dezinstala manual Qt4.


</div>

If Qt4 was previously installed via brew, and you then build with Qt5, you may get a EXC\_BAD\_ACCESS (SEGSEGV) exception when launching the new Qt5 build. The fix for this is to manually uninstall Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```


<div class="mw-translate-fuzzy">

### Fortran

*\"No CMAKE\_Fortran\_COMPILER could be found.\"* în timpul configurației - versiunile mai vechi ale FreeCAD vor trebui să compileze instalate. Cu Homebrew, procedați la \"brew install gcc\" și încerdați configurarea din nou, dând lui cmake cale spre Fortran ie -DCMAKE\_Fortran\_COMPILER=/opt/local/bin/gfortran-mp-4.9 . Sau, de preferat, utilizați o versiune mai nouă a sursei FreeCAD!


</div>

*\"No CMAKE\_Fortran\_COMPILER could be found.\"* during configuration - Older versions of FreeCAD will need a fortran compiler installed. With Homebrew, do \"brew install gcc\" and try configuring again, giving cmake the path to Fortran ie -DCMAKE\_Fortran\_COMPILER=/opt/local/bin/gfortran-mp-4.9 . Or, preferably use a more current version of FreeCAD source!


<div class="mw-translate-fuzzy">

### OpenGL

A se vedea [OpenGL on MacOS](OpenGL_on_MacOS.md) pentru OpenGL issues atunci când Qt 4.8 și aneriarele sunt utilizate sub MacOS.


</div>

See [OpenGL on MacOS](OpenGL_on_MacOS.md) for OpenGL issues when Qt 4.8 and earlier are used on MacOS.


<div class="mw-translate-fuzzy">

### FreeType

Atunci când se utilizează versiuni CMake mai vechi de 3.1.0, este necesar să setați variabila CMake FREETYPE\_INCLUDE\_DIR\_freetype2 manually, eg /usr/local/include/freetype2


</div>

When using CMake versions older than 3.1.0, it\'s necessary to set CMake variable FREETYPE\_INCLUDE\_DIR\_freetype2 manually, eg /usr/local/include/freetype2

### Additional Build Instructions 

FreeCAD can be built against the latest git master hosted on github, and launched from a CLI using libraries provided by the homebrew-freecad tap. For a complete list of build instructions see [here](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).


<div class="mw-translate-fuzzy">


{{docnav|CompileOnUnix|Compiling (Speeding up)}}


</div>




_ _

---
[documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > Compile on MacOS/ro
