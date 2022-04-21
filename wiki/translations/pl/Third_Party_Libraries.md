# Third Party Libraries/pl
{{TOCright}}

## Przegląd

Są to biblioteki, których FreeCAD używa jako zależności od innych dostawców podczas kompilacji. Zazwyczaj są to \[<https://en.wikipedia.org/wiki/Dynamic_loading>. Biblioteki dynamicznie łączone\] i mają rozszerzenie `.so` w Linuksie/MacOSie i `.dll` w Windowsie, a towarzyszą im pliki nagłówkowe `.h` lub `.hpp` lub podobne. Jeśli potrzebna jest zmodyfikowana biblioteka lub klasa opakowująca, kod zmodyfikowanej biblioteki lub klasy opakowującej musi stać się częścią kodu źródłowego programu FreeCAD i zostać razem z nim skompilowany.

Przed przystąpieniem do kompilacji należy najpierw zadbać☻ o rozwiązanie zależności. Więcej informacji na ten temat można znaleźć na stronach [Kompilacja w systemie Linux](Compile_on_Linux/pl.md), [Kompilacja w systemie MacOS](Compile_on_MacOS/pl.md) oraz [Kompilacja w systemie Windows](Compile_on_Windows/pl.md).

Jeśli kompilujesz w systemie Windows, rozważ użycie [paczki bibliotek](#LibPack.md) zamiast próbować instalować biblioteki pojedynczo.

## Odnośniki internetowe 

++++
| Biblioteka            | wymagana wersja         | Link do pobrania                                                              |
+=======================+=========================+===============================================================================+
| Python                | \>= 3.6                 | <http://www.python.org/>                                                      |
++++
| Boost                 | \>= 1.33                | <http://www.boost.org/>                                                       |
++++
| OpenCASCADE           | \>= 7.3                 | <http://www.opencascade.org>                                                  |
++++
| Qt                    | \>= 5.4                 | <https://www.qt.io/>                                                          |
++++
| Shiboken2             |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                       | **tak jak Qt** |                                                                               |
|                       |                      |                                                                               |
++++
| PySide2               |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                       | **tak jak Qt** |                                                                               |
|                       |                      |                                                                               |
++++
| Coin3D                | \>= 3.x                 | <https://github.com/coin3d/coin>                                              |
++++
| SoQt *(przestarzałe)* | \>= 1.2                 | <https://github.com/coin3d/soqt>                                              |
++++
| Quarter               | \>= 1.0                 | <https://github.com/coin3d/quarter>                                           |
++++
| Pivy                  | \>= 0.6.5               | <https://github.com/coin3d/pivy/>                                             |
++++
| FreeType              | \>= XXX                 | XXX                                                                           |
++++
| PyCXX                 | \>= XXX                 | XXX                                                                           |
++++
| KDL                   | \>= XXX                 | <https://orocos.org/wiki/orocos/kdl-wiki.html>                                |
++++
| Point Cloud Library   | \>= XXX                 | XXX                                                                           |
++++
| Salome SMESH          | \>= XXX                 | XXX                                                                           |
++++
| VTK                   | \>= 6.0                 | XXX                                                                           |
++++
| Ply                   | \>= 3.11                | <https://www.dabeaz.com/ply/>                                                 |
++++
| Xerces-C++            | \>= 3.0                 | <https://xerces.apache.org/xerces-c/>                                         |
++++
| Eigen3                | \>= 3.0                 | <http://eigen.tuxfamily.org/index.php?title=Main_Page>                        |
++++
| Zipios++              | \>= 0.1.5               | <https://snapwebsites.org/project/zipios>, <https://github.com/Zipios/Zipios> |
++++
| Zlib                  | \>= 1.0                 | <http://www.zlib.net/>, <https://github.com/madler/zlib>                      |
++++
| libarea               | \>= 0.0.20140514-1      | <https://github.com/danielfalck/libarea>                                      |
++++
|                       |                         |                                                                               |
++++

## Szczególy

### Python

**Wersja:** 3.3 lub nowsza

**Licencja:** Python 3.3


**Python 2 stał się przestarzały w 2019 roku. W dalszym rozwoju FreeCAD będzie korzystać wyłącznie z wersji Python 3; kompatybilność z Python 2 nie będzie testowana, więc stare środowiska pracy i makra, które korzystają z tej wersji, będą musiały zostać zaktualizowane lub mogą przestać działać. Jeśli napotkasz problemy z wersją środowiska Python 3, napisz na [https://forum.freecadweb.org/ forum FreeCAD].**

Python to popularny uniwersalny język skryptowy, który jest szeroko stosowany w systemie Linux i oprogramowaniu open source. W FreeCAD Python jest używany podczas kompilacji, a także w czasie pracy na różne sposoby. Jest on używany do:

-   tworzenia skryptów testowych do testowania różnych warunków, takich jak wycieki pamięci, do zapewnienia funkcjonalności oprogramowania po zmianach, do sprawdzania po kompilacji oraz do testowania poprawności działania,
-   tworzenia [makrodefinicji](macros/pl.md) i nagrywania makrodefinicji,
-   implementacji logiki aplikacji dla pakietów standardowych,
-   implementacji narzędzi pomocniczych, takich jak [Menadżer dodatków](Std_AddonMgr/pl.md),
-   implementacji całych środowisk pracy, takich jak [Rysunek Roboczy](Draft_Workbench/pl.md) i [Architektura](Arch_Workbench/pl.md),
-   dynamicznego ładowania pakietów,
-   implementacji reguł projektowania *(inżynieria wiedzy)*,
-   wykonywania wymyślnych interakcji internetowych, takich jak grupy robocze i PDM.

W systemie Linux Python jest zwykle już zainstalowany w dystrybucji. W systemie Windows można pobrać prekompilowaną wersję binarną z [Python.org](http://www.python.org/) lub użyć [ActiveState Python](http://www.activestate.com/), choć w tym drugim przypadku trudniej jest uzyskać biblioteki debugowania.

Python został wybrany jako język skryptowy dla FreeCAD z różnych powodów:

-   Jest bardziej zorientowany obiektowo niż Perl i Tcl.
-   Kod jest bardziej czytelny niż w Perlu i Visual Basic.
-   Jest łatwiejszy do osadzenia w innej aplikacji, w przeciwieństwie do, na przykład, Javy.

Podsumowując, Python jest dobrze udokumentowany, łatwo go osadzić i rozszerzyć w aplikacji napisanej w języku C++. Jest też dobrze przetestowany i ma silne wsparcie ze strony społeczności open source. Więcej informacji na temat środowiska Python oraz oficjalną dokumentację można znaleźć na stronie [Python.org](http://www.python.org).

### Boost

**Wersja:** 1.33 lub nowsza

**Licencja:** Boost Software License - wersja 1.0

Biblioteki Boost C++ są kolekcją recenzowanych bibliotek o otwartym kodzie źródłowym, które rozszerzają funkcjonalność języka C++. Są one przeznaczone do szerokiego zastosowania w szerokim spektrum aplikacji oraz do współpracy z biblioteką standardową C++. Licencja Boost została tak zaprojektowana, aby zachęcać do ich używania zarówno w projektach open source, jak i zamkniętych.

Ze względu na ich popularność i stabilność wiele bibliotek Boost zostało zaakceptowanych do włączenia do standardu C++11, a kolejne są planowane do włączenia w kolejnych standardach C++.

W celu zapewnienia wydajności i elastyczności, Boost szeroko korzysta z szablonów. Boost stał się źródłem wielu prac i badań nad programowaniem ogólnym i metaprogramowaniem w C++. Więcej o Boost można przeczytać na stronie [domowej Boost](http://www.boost.org/).

### Technologia OpenCASCADE 

**Wersja:** 6.7 lub nowsza

**Licencja:** wersja 6.7.0 i późniejsze są objęte [GNU Lesser General Public License *(LGPL)* wersja 2.1 z dodatkowymi wyjątkami](https://www.opencascade.com/content/licensing). Wcześniejsze wersje korzystają z licencji [Open CASCADE Technology Public License](https://www.opencascade.com/content/occt-public-license).

OpenCASCADE Technology *(OCCT)* to w pełni funkcjonalne jądro CAD klasy profesjonalnej. Zostało ono opracowane w 1993 roku i pierwotnie nazwane CAS.CADE przez firmę Matra Datavision we Francji dla aplikacji Strim *(Styler)* i Euclid Quantum. W 1999 roku zostało udostępnione jako oprogramowanie open source i od tego czasu nosi nazwę OpenCASCADE.

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.

To learn more visit the [OpenCASCADE website](http://www.opencascade.org).

### Qt

**Version:** 4.1 or higher

**License:** GPL v2.0/v3.0 or Commercial; from version 4.5 on also LPGL v2.1.

Qt is one of the most popular graphical user interface (GUI) toolkits available in the open source world. FreeCAD uses this toolkit to draw the interface of the program. For this, the Qt Designer application is very useful as it allows developers to quickly draw the dialogs and windows, export them as XML resource files, and then load these interfaces at runtime.

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 

Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words, it is the system that is used to expose the Qt C++ API to the Python language.

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).

### Coin3D

**Version:** 3.0 or higher

**License:** BSD 3-clause license

Coin3D is a high-level 3D graphics library with a C++ application programming interface. It uses scenegraph data structures to render real-time graphics suitable for all kinds of scientific and engineering visualization applications.

Coin3D is built on the industry-standard OpenGL immediate mode rendering library, and adds abstractions for higher-level primitives, provides 3D interactivity, and contains many complex optimization features for fast rendering that are transparent for the application programmer.

Coin3D is compatible with SGI\'s Open Inventor 2.1 API. This API has become the de facto standard graphics interface for 3D visualization in the scientific and engineering community. It has proved its worth since the year 2000 as a major building block in thousands of engineering applications around the world.

Coin3D (Open Inventor) is used as the 3D viewer in FreeCAD because the OpenCASCADE viewer (AIS and Graphics3D) has limitations and performance bottlenecks, especially with large-scale engineering rendering; other things like textures or volumetric rendering are not entirely supported by the OpenCASCADE viewer.

Coin3D is portable over a wide range of platforms: UNIX, Linux, BSD, MacOS X, and Microsoft Windows operating systems. To read more about this library visit [Coin3D homepage](https://github.com/coin3d/coin).

#### SoQt (deprecated) 

**Version:** 1.2.0 or higher

**License:** BSD 3-clause license

SoQt is the Coin3D (Open Inventor) binding to the Qt GUI toolkit.

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

### Xerces-C++ 

**Version:** 3.0 or higher

**License:** Apache Software License Version 2.0

Xerces-C++ is a validating XML parser written in a portable subset of C++. Xerces-C++ makes it easy to give your application the ability to read and write XML data. A shared library is provided for parsing, generating, manipulating, and validating XML documents. Xerces-C++ is faithful to the XML 1.0 recommendation and associated standards.

The parser is used for saving and restoring parameters in FreeCAD. For more information see [Xerces-C++ homepage](https://xerces.apache.org/xerces-c/).

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

#### Zlib

**Version:** 1.0 or higher

**License:** zlib license

Zlib is designed to be a free, general-purpose, lossless data-compression library for use on any computer hardware and operating system. It implements the `DEFLATE` compression algorithm commonly used in `.zip` and `.gzip` files.

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version:** 0.0.20140514-1 or higher

**License:** BSD 3-clause license

Libarea is a software library to compute profile and pocket operations which are used in computer aided manufacturing (CAM) software. It was created by Dan Heeks for his HeeksCNC project.

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.

## LibPack

LibPack jest wygodnym pakietem z zebranymi razem zależnościami kompilacji programu FreeCAD. Jest on potrzebny tylko wtedy, gdy kompilujesz program FreeCAD w systemie Windows za pomocą Visual Studio 2015 lub nowszego. Najnowszy LibPack można znaleźć na stronie [releases page](https://github.com/FreeCAD/FreeCAD/releases).

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 

Zobacz ogłoszenie na forum: [Nowe pakiety libpacks dla Windows z Qt5.12, OCC7.3 i Pythonem 3.6 autorstwa apeltauera](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

Zawiera on między innymi: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/pl
