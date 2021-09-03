





{{TOCright}}


<div class="mw-translate-fuzzy">

### Översikt

Detta är bibliotek som inte har förändrats i FreeCAD projektet. De används som de är som ett dynamiskt länkbibliotek (\*.so or \*.dll). Om en ändring är nödvändig eller om en wrapper klass behövs, så måste wrapperns kod eller den förändrade bibliotekskoden flyttas till FreeCADs baspaket.

De använda biblioteken är:


</div>

The dependencies need to be installed in the system before proceeding with compilation; see [compile on Linux](Compile_on_Linux.md), [compile on Windows](Compile_on_Windows.md), and [compile on MacOS](Compile_on_MacOS.md) for more information.


<div class="mw-translate-fuzzy">

Överväg att använda [LibPack](#LibPack/sv.md) istället för att ladda ned och installera alla saker själv.


</div>


<div class="mw-translate-fuzzy">

### Länkar


</div>


<div class="mw-translate-fuzzy">

  Biblioteksnamn   Nödvändig version   Länk till den
  ---------------- ------------------- --------------------------------------------------------
  Python           \>= 2.5.x           <http://www.python.org/>
  OpenCasCade      \>= 5.2             <http://www.opencascade.org>
  Qt               \>= 4.1.x           <http://www.qtsoftware.com>
  Coin3D           \>= 2.x             <http://www.coin3d.org>
  ODE              \>= 0.10.x          <http://www.ode.org>
  SoQt             \>= 1.2             <http://www.coin3d.org>
  Xerces-C++       \>= 2.7.x \< 3.0    <http://xml.apache.org/xerces-c/>
  GTS              \>= 0.7.x           <http://gts.sourceforge.net/>
  Zlib             \>= 1.x.x           <http://www.zlib.net/>
  Boost            \>= 1.33.x          <http://www.boost.org/>
  Eigen3           \>= 3.0.1           <http://eigen.tuxfamily.org/index.php?title=Main_Page>

  : Länktabell


</div>


<div class="mw-translate-fuzzy">

### Detaljer


</div>


<div class="mw-translate-fuzzy">

#### Python

**Version:** 2.5 eller högre


</div>


<div class="mw-translate-fuzzy">

**License:** Python 2.5 licens


</div>


{{VeryImportantMessage|Python 2 became obsolete in 2019. Further development of FreeCAD will use exclusively Python 3; compatibility with Python 2 won't be tested, so old workbenches and macros that use this version will have to be updated or they may stop working. Please post on the [https://forum.freecadweb.org/ FreeCAD forum] if you encounter problems with Python 3.}}

Python is a popular all-purpose scripting language that is widely used in Linux and open source software. In FreeCAD, Python is used during compilation and also at runtime in different ways. It is used

-   to write test scripts to test for different conditions, such as memory leaks, to ensure functionality of the software after changes, for post build checks, and test coverage tests,
-   to write [macros](macros.md) and macro recording,
-   to implement application logic for standard packages,
-   to implement auxiliary tools such as the [Addon Manager](Addon_Manager.md),
-   to implement entire workbenches like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md),
-   to dynamically load packages,
-   to implement rules for design (knowledge engineering),
-   to do fancy Internet interactions like work groups and PDM


<div class="mw-translate-fuzzy">

Du kan använda käll- eller binärkod från <http://www.python.org/> eller alternativt använda ActiveState Python från <http://www.activestate.com/> fast det kan vara svårt att få avbuggningsbiblioteken från ActiveState.


</div>

Python was chosen as the scripting language for FreeCAD for different reasons:

-   It is more object oriented than Perl and Tcl.
-   The code is more readable than Perl and Visual Basic.
-   It is easier to embed in another application, unlike, say, Java.

In summary, Python is well documented, and it\'s easy to embed and extend in a C++ application. It is also well tested and has strong support from the open source community. Read more about Python and browse the official documentation at [Python.org](http://www.python.org).


<div class="mw-translate-fuzzy">

#### Boost


</div>


<div class="mw-translate-fuzzy">

**Version:** 1.33.x


</div>

**Licens:** Boost Software License - Version 1.0


<div class="mw-translate-fuzzy">

Boost C++ biblioteken är en samling av granskade, öppen källkodsbibliotek som utökar C++ funktionalitet. Biblioteken är licensierade under Boost Software License, som är anpassad för att Boost ska tillåtas att användas med både sluten och öppen källkodsprojekt. Många av Boosts grundare är med i C++ standardkommiten och flera Boost bibliotek har accepterats for integrering i Teknisk Rapport 1 av C++0x.


</div>

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.


<div class="mw-translate-fuzzy">

För att försäkra effektivitet och flexibilitet, så använder Boost en hel del mallar. Boost har varit en källa för extensivt arbete och forskning i allmän programmering och meta-programmering i C++.


</div>


<div class="mw-translate-fuzzy">

#### OpenCasCade


</div>


<div class="mw-translate-fuzzy">

**Version:** 5.2 eller högre


</div>


<div class="mw-translate-fuzzy">

**Licens:** OCTPL


</div>


<div class="mw-translate-fuzzy">

OCC är en fullödig CAD Kärna. Från början utvecklades den av Matra Datavision i Frankrike för Strim (Styler) och Euclid Quantum applikationerna och ändrades senare till öppen källkod. Det är verkligen ett stort bibliotek, och gör en fri cad applikation möjlig, genom att erbjuda några paket som skulle vara svåra eller omöjliga att implementera i ett öppen källkodsprojekt:

-   En komplett STEP kompliant geometrikärna
-   En topologisk datamodell och alla nödvändiga funktioner att arbeta med (klipp, förena, extrudera, och så vidare. . . )
-   Standard Import- / Export processorer som STEP, IGES, VRML
-   3D och 2D visare med markeringssupport
-   En dokument och projektdatastruktur med support för spara och återställa, extern länkning av dokument, omberäkning av designhistoria (parametrisk modellering) och en facilitet för att ladda nya datatyper dynamiskt som ett utökningspaket


</div>

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.


<div class="mw-translate-fuzzy">

För att lära dig mer om OpenCasCade, ta en titt på OpenCasCade sidan eller <http://www.opencascade.org>.


</div>


<div class="mw-translate-fuzzy">

#### Qt


</div>


<div class="mw-translate-fuzzy">

**Version:** 4.1.x eller högre


</div>


<div class="mw-translate-fuzzy">

**Licens:** GPL v2.0/v3.0 eller Kommersiell (från version 4.5 och framåt även v2.1)


</div>


<div class="mw-translate-fuzzy">

Jag tror inte jag behöver berätta så mycket om Qt. Det är en av de mest använda verktygsseten för grafiskt gränssnitt i öppen källkodsprojekt. För mig är den viktigaste anledningen att använda Qt är Designer och möjligheten att ladda hela dialogrutor som en (XML) resurs och integrera specialiserade widgets. I en CAX applikation så är användarinteraktionen och dialogrutorna den absolut största delen av koden och för en bra dialogkonstruktör är dett mycket viktigt att lätt kunna utöka FreeCAD med ny funktionalitet. Ytterligare information och en mycket bra online dokumentation hittar du på <http://www.qtsoftware.com>.


</div>

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 {#shiboken2_and_pyside2}

Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words, it is the system that is used to expose the Qt C++ API to the Python language.

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).


<div class="mw-translate-fuzzy">

#### Coin3D


</div>


<div class="mw-translate-fuzzy">

**Version:** 2.0 eller högre


</div>


<div class="mw-translate-fuzzy">

**Licens:** GPL v2.0 eller Kommersiell


</div>


<div class="mw-translate-fuzzy">

Coin är ett högnivå 3D grafikbibliotek med ett C++ Applikationsprogrammeringsgränssnitt. Coin använder scengraf datastrukturer för att rendera realtidsgrafik som passar för de flesta vetenskapliga och konstruktions visualiserings applikationer.


</div>


<div class="mw-translate-fuzzy">

Coin är byggt på industristandard OpenGL direktrenderingsbiblioteket, och adderar abstraktioner för högnivåprimitiver, erbjuder 3D interaktivitet, ökar bekvämligheten och produktiviteten för programmeraren, och innehåller många komplexa optimeringsfunktioner för snabb rendering som är transparent för programmeraren.


</div>


<div class="mw-translate-fuzzy">

Coin är baserat på SGI Open Inventor API. Open Inventor, för de som inte vet vad det är, har sedan länge varit de facto standard grafikbibliotek för 3D visualisering och visuell simuleringsmjukvara i vetenskapliga och konstruktörssammanhang. Det har bevisat sitt värde i mer än 10 år, dess mogenhet bidrar till dess framgång som ett huvudsakligt byggblock i tusentals storskaliga ingenjörsapplikationer världen runt.


</div>


<div class="mw-translate-fuzzy">

Vi kommer att använda OpenInventor som 3D visare i FreeCAD eftersom OpenCasCade visaren (AIS och Graphics3D) har allvarliga begränsningar och prestandaflaskhalsar, speciellt när det gäller storskalig konstruktionsrendering. Andra saker som texturer eller volymetrisk rendering är inte väl stödda, och så vidare \....


</div>


<div class="mw-translate-fuzzy">

Coin kan portas över många plattformar: alla UNIX / Linux / \*BSD plattformar, alla Microsoft Windows operativsystem, och Mac OS X.


</div>


<div class="mw-translate-fuzzy">

#### SoQt


</div>

**Version:** 1.2.0 eller högre


<div class="mw-translate-fuzzy">

**Licens:** GPL v2.0 eller Kommersiell


</div>


<div class="mw-translate-fuzzy">

SoQt är Inventor bindningen till Qt gränssnittsverktygsset. Olyckligtvis så är det inte längre LGPL så vi måste ta bort det från FreeCADs kodbas och länka den som ett bibliotek. Den har samma licensmodell som Coin. Och du måste kompilera den med din Qt version.


</div>

SoQt is no longer used in FreeCAD, it was replaced by Quarter which is a more recent Qt binding.

#### Quarter

**Version:** 1.0 or higher

**License:** BSD 3-clause license

Quarter is a newer Coin3D binding to the Qt toolkit. A version of it is included in the source code of FreeCAD so it is compiled together with it.

#### Pivy

**Version:** 0.6.3 or higher

**License:** BSD 3-clause license

[Pivy](Pivy.md) is a library that wraps the Coin3d library for use in [Python](Python.md). It is not needed to build FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft Workbench](Draft_Workbench.md), and by other workbenches that use it internally, like [Arch](Arch_Workbench.md) and [BIM](BIM_Workbench.md).

If you are not going to use these workbenches, you won\'t need Pivy.

### Ply

**Version:** 3.11 or higher

**License:** BSD 3-clause license

Ply is the Python-Lex-Yacc parser. It is used as a runtime dependency by the [OpenSCAD Workbench](OpenSCAD_Workbench.md). If you don\'t use this workbench, you may not need this package.

For more information see [Ply homepage](https://www.dabeaz.com/ply/)


<div class="mw-translate-fuzzy">

#### Xerces-C++ {#xerces_c}


</div>


<div class="mw-translate-fuzzy">

**Version:** 2.7.0 eller högre


</div>

**Licens:** Apache Software License Version 2.0


<div class="mw-translate-fuzzy">

Xerces-C++ är en validerande XML läsare som är skriven i C++ portabla delset. Xerces-C++ gör det lätt att ge din applikation möjligheten att läsa och skriva XML data. Ett delat bibliotek erbjuds för läsning, generering, manipulering, och validering av XML dokument.


</div>


<div class="mw-translate-fuzzy">

Läsaren används för att spara och återkalla parametrar i FreeCAD.


</div>

### Eigen3

**Version:** 3.0 or higher

**License:** Starting from the 3.1.1 version, it is licensed under the [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Earlier versions were licensed under the [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

If you just want to use Eigen, you can use the header files right away. There is no binary library to link to, and no configured header file. Eigen is a pure template library defined in the headers.

Eigen is used in FreeCAD for many vector operations in 3D space. To learn more, visit [Eigen homepage](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Version:** 0.1.5 or higher

**License:** GNU Lesser General Public License 2.1

Zipios++ is a C++ library for reading and writing `.zip` files. Access to individual entries is provided through standard C++ iostreams. A simple read-only virtual file system that mounts regular directories and `.zip` files is also provided. The structure and public interface of Zipios++ are loosely based on the `java.util.zip` package of Java.

FreeCAD\'s native file format `.FCstd` is in reality a `.zip` file that stores and compresses other types of data within it, such as BREP and XML files. Therefore, Zipios++ is used to save and open compressed archives, including FreeCAD files.

A copy of Zipios++ is included in the source code of FreeCAD so it is compiled together with it. If you want to use an external Zipios++ library, provided by your operating system, you may set -DFREECAD_USE_EXTERNAL_ZIPIOS=ON with `cmake`.

Zipios++ uses the Zlib library to perform the actual decompression of files.


<div class="mw-translate-fuzzy">

#### Zlib


</div>


<div class="mw-translate-fuzzy">

**Version:** 1.x.x


</div>


<div class="mw-translate-fuzzy">

**Licens:** zlib Licens


</div>


<div class="mw-translate-fuzzy">

zlib är designat att vara ett fritt, allmänt, juridiskt obegränsat \-- vilket innebär, ej begränsat av några patent \-- förlustfritt datakompressionsbibliotek som kan användas på i stort sett all datorhårdvara och operativsystem. zlib dataformat är i sig själv portabelt över olika plattformar. Till skillnad från kompressionsmetoden LZW som används i Unix compress(1) och i bildformatet GIF, så expanderar aldrig den kompressionsmetod som för närvarande används i zlib datan. (LZW kan dubblera eller tredubbla filstorleken i extrema fall.) zlib\'s storlek i minnet är också oberoende av inmatningsdatan och kan om nödvändigt reduceras, till en kostnad av kompressionsgrad.


</div>

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version:** 0.0.20140514-1 or higher

**License:** BSD 3-clause license

Libarea is a software library to compute profile and pocket operations which are used in computer aided manufacturing (CAM) software. It was created by Dan Heeks for his HeeksCNC project.

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.


<div class="mw-translate-fuzzy">

### LibPack

LibPack är ett smidigt paket med alla ovanstående bibliotek ihoppackade. Det är för närvarande tillgängligt för

Windows plattformen på [Nedladdningssidan](Download/sv.md)! Om du arbetar under Linux så behöver du inte LibPack, istället ska du använda paketförråden för din Linux distribution.


</div>

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 {#freecad_12.1.2}

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11


<div class="mw-translate-fuzzy">


{{docnav/sv|CompileOnMac/sv|Third Party Tools/sv}}


</div>


 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
