# Third Party Libraries/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

### Prezentare generală 

Acestea sunt biblioteci care nu sunt modificate în proiectul FreeCAD. Ele sunt practic utilizate ca o bibliotecă dinamică de legătură (\* .so sau \* .dll). Dacă este nevoie de schimbare, sau a wrapper class este necesar , atunci codul wrapper sau biblioteca modificată trebuie mutat în pachetul de bază FreeCAD. Bibliotecile folosite sunt:


</div>

The dependencies need to be installed in the system before proceeding with compilation; see [compile on Linux](Compile_on_Linux.md), [compile on Windows](Compile_on_Windows.md), and [compile on MacOS](Compile_on_MacOS.md) for more information.


<div class="mw-translate-fuzzy">

Dacă utilizați Windows, luați în considerare folosirea[LibPack](#LibPack.md) în loc de a descărca și a instala tot felul de chestii pe cont propriu.


</div>


<div class="mw-translate-fuzzy">

## Legături


</div>


<div class="mw-translate-fuzzy">

  Lib name      Version needed     Link to get it
  ------------- ------------------ --------------------------------------------------------
  Python        \>= 2.5.x          <http://www.python.org/>
  OpenCasCade   \>= 5.2            <http://www.opencascade.org>
  Qt            \>= 4.1.x          <https://www.qt.io/>
  Coin3D        \>= 2.x            <http://www.coin3d.org>
  SoQt          \>= 1.2            <http://www.coin3d.org>
  Xerces-C++    \>= 2.7.x \< 3.0   <http://xml.apache.org/xerces-c/>
  Zlib          \>= 1.x.x          <http://www.zlib.net/>
  Boost         \>= 1.33.x         <http://www.boost.org/>
  Eigen3        \>= 3.0.1          <http://eigen.tuxfamily.org/index.php?title=Main_Page>
  Shiboken      \>= 1.1.2          <http://shiboken.readthedocs.org/en/latest/>
  libarea       N/A                <https://github.com/danielfalck/libarea>
                                   

  : Link table


</div>


<div class="mw-translate-fuzzy">

### Detalii


</div>


<div class="mw-translate-fuzzy">

#### Python

**Version:** 2.5 or higher


</div>


<div class="mw-translate-fuzzy">

**License:** Python 2.5 license


</div>


**Python 2 became obsolete in 2019. Further development of FreeCAD will use exclusively Python 3; compatibility with Python 2 won't be tested, so old workbenches and macros that use this version will have to be updated or they may stop working. Please post on the [https://forum.freecadweb.org/ FreeCAD forum] if you encounter problems with Python 3.**

Python is a popular all-purpose scripting language that is widely used in Linux and open source software. In FreeCAD, Python is used during compilation and also at runtime in different ways. It is used

-   to write test scripts to test for different conditions, such as memory leaks, to ensure functionality of the software after changes, for post build checks, and test coverage tests,
-   to write [macros](macros.md) and macro recording,
-   to implement application logic for standard packages,
-   to implement auxiliary tools such as the [Addon Manager](Std_AddonMgr.md),
-   to implement entire workbenches like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md),
-   to dynamically load packages,
-   to implement rules for design (knowledge engineering),
-   to do fancy Internet interactions like work groups and PDM


<div class="mw-translate-fuzzy">

Puteți folosi programul sursă sau binarul de la <http://www.python.org/> ori să utlizați alternativ ActiveState Python from <http://www.activestate.com/> deși este puțin greu să obțineți depanarea bibliotecilor/libs din ActiveState.


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

**License:** Boost Software License - Version 1.0


<div class="mw-translate-fuzzy">

Bibliotecile Boost C ++ sunt o colecție de biblioteci evaluate de colegi, care extind funcționalitatea C ++. Bibliotecile sunt licențiate sub licența Boost Software License, concepute pentru a permite ca Boost să fie utilizat atât cu proiecte deschise, cât și cu surse închise. Mulți dintre fondatorii lui Boost se află în comitetul standard C ++ și mai multe biblioteci Boost au fost acceptate pentru a fi încorporate în raportul tehnic 1 al C ++ 0x.


</div>

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.


<div class="mw-translate-fuzzy">

Pentru a asigura eficiența și flexibilitatea, Boost folosește pe scară largă șabloanele. Boost a fost o sursă de muncă și cercetări ample privind programarea generică și meta-programarea în C ++.


</div>


<div class="mw-translate-fuzzy">

#### OpenCasCade


</div>


<div class="mw-translate-fuzzy">

**Version:** 5.2 or higher


</div>


<div class="mw-translate-fuzzy">

**License:** v6.7.0 and later are governed by GNU Lesser General Public License (LGPL) version 2.1 with additional exception. <https://www.opencascade.com/content/licensing> Earlier versions use a slightly different license: <https://www.opencascade.com/content/occt-public-license>


</div>


<div class="mw-translate-fuzzy">

OCC este un kernel CAD complet echipat. Inițial, este dezvoltat de Matra Datavision în Franța pentru aplicațiile Strim (Styler) și Euclid Quantum și mai târziu l-au făcut Open Source. Este o bibliotecă cu adevărat imensă și face posibilă o aplicație CAO gratuită, oferind câteva pachete care ar fi greu sau imposibil de implementat într-un proiect Open Source:

-   Un nucleu geometric complet compatibil cu STEP
-   Un model topologic de date și toate funcțiile necesare pentru a lucra pe (tăiere, fuziune, extrudere, și așa mai departe \...)
-   Procese standard de import / export precum STEP, IGES, VRML
-   Viewer 3D și 2D cu selectare suport
-   O structura de document și a datelor unui proiect cu suport pentru salvare și restaurare, legătura externă a documentelor, recalcularea istoricului de desenului/proiectului (modelarea parametrică) și a unui centru de încărcare a datelor de tip nou, ca un modul de extensie dinamic.


</div>

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.


<div class="mw-translate-fuzzy">

To learn more about OpenCasCade take a look at the OpenCasCade page or <http://www.opencascade.org>.


</div>


<div class="mw-translate-fuzzy">

#### Qt


</div>


<div class="mw-translate-fuzzy">

**Version:** 4.1.x or higher


</div>


<div class="mw-translate-fuzzy">

**License:** GPL v2.0/v3.0 or Commercial (from version 4.5 on also LPGL v2.1)


</div>


<div class="mw-translate-fuzzy">

Nu cred că trebuie să spun foarte multe despre QT. Este unul dintre cele mai utilizate instrumente de GUI în proiectele Open Source. Pentru mine cel mai important punct de utilizare a Qt este designerul Qt și posibilitatea de a încărca toate casetele dialog ca resursă (XML) și care încorporează widget-uri specializate. Într-o aplicație CAX interacțiunea cu utilizatorul și casetele de dialog sunt de departe cea mai mare parte a codului și o bună proiectarea a dialogului ester foarte importantă pentru extinderea freeCAD cu noi funcționalități. Informații suplimentare și foarte bună documentație on line o veți găsi pe <http://www.qtsoftware.com>.


</div>

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).


<div class="mw-translate-fuzzy">

##### Shiboken and Pyside 

**Shiboken** (*Shi bō ken*, 死某剣)este generatorul de legare Python pe care îl utilizează Qt pentru Python pentru a crea modulul PySide, cu alte cuvinte, este sistemul pe care îl folosim pentru a expune API-ul Qt C ++ către Python.


</div>


<div class="mw-translate-fuzzy">

Numele de **Shiboken2** și **PySide2** face referire la compatibilitatea Qt 5, deoarece versiunile anterioare (fără **2**) se referă la Qt 4. Citiți mai multe despre Shiboken și Pyside pe [Qt for Python wiki page](https://wiki.qt.io/Qt_for_Python/Shiboken)


</div>

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).


<div class="mw-translate-fuzzy">

#### Coin3D


</div>


<div class="mw-translate-fuzzy">

**Version:** 2.0 or higher


</div>


<div class="mw-translate-fuzzy">

**License:** GPL v2.0 or Commercial


</div>


<div class="mw-translate-fuzzy">

Coin este o bibliotecă grafică 3D de nivel înalt cu o interfață de programare a aplicațiilor C ++Application Programming Interface. Coin utilizează structuri de date grafice de scenă pentru a oferi grafică în timp real potrivită pentru majoritatea aplicațiilor de vizualizare științifică și inginerie.


</div>


<div class="mw-translate-fuzzy">

Coin este construit pe standardul industrial OpenGL cu biblioteca de randare imediată și adaugă abstracții pentru primitive de nivel superior, oferă interactivitate 3D, îmbunătățește foarte mult confortul și productivitatea programatorului și conține multe funcții de optimizare complexe pentru randarea rapidă și în plus care este transparentă pentru programatorul de aplicații.


</div>


<div class="mw-translate-fuzzy">

Coin se bazează pe SGI Open Inventor API . Open Inventor, pentru cei care nu sunt familiarizați cu acesta, a devenit de mult timp biblioteca grafică standard de facto pentru vizualizarea 3D și software-ul de simulare vizuală în comunitatea științifică și de inginerie. Și-a demonstrat valoarea timp de peste 10 ani, maturitatea sa contribuind la succesul său ca o fundație majoră în mii de aplicații de inginerie la scară largă din întreaga lume.


</div>


<div class="mw-translate-fuzzy">

Vom folosi OpenInventor ca vizualizator 3D în FreeCAD, deoarece vizualizatorul OpenCasCade (AIS și Graphics3D) au limitele lor din cauza fluxului ridicat de date, mai ales atunci când intră în randarea inginerească la scară largă. Alte lucruri, cum ar fi texturile sau randarea volumetrică, nu sunt cu adevărat susținute și așa mai departe\....


</div>


<div class="mw-translate-fuzzy">

Software Coin este portabil pe o gamă largă de platforme: orice platformă UNIX / Linux / \* BSD, tot sistemul de operare Microsoft Windows și Mac OS X.


</div>


<div class="mw-translate-fuzzy">

#### SoQt


</div>

**Version:** 1.2.0 or higher


<div class="mw-translate-fuzzy">

**License:** GPL v2.0 or Commercial


</div>


<div class="mw-translate-fuzzy">

SoQt este Inventorul fr lrgături pentru Qt Gui Toolkit. Din păcate, nu mai este LGPL, deci trebuie să îl eliminăm din codul de bază a FreeCAD și să îl conectăm ca o bibliotecă. Are același model de licență ca și Coin. Și trebuie să îl compilați cu versiunea Qt.


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

#### Xerces-C++ 


</div>


<div class="mw-translate-fuzzy">

**Version:** 2.7.0 or higher


</div>

**License:** Apache Software License Version 2.0


<div class="mw-translate-fuzzy">

Xerces-C ++ este un analizor de validare (parser) XML scris într-un subset portabil de C ++. Cu Xerces-C ++ se ușurează oferirea aplicației dvs. abilității de a citi și scrie date în format XML. O bibliotecă partajată este prevăzută analizarea, generarea, manipularea și validarea documentelor XML.


</div>


<div class="mw-translate-fuzzy">

The parser is used for saving and restoring parameters in FreeCAD.


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

**License:** zlib License


</div>


<div class="mw-translate-fuzzy">

zlib este conceput pentru a fi gratuit, cu scop general, fără a fi limitat din punct de vedere juridic - adică nu este acoperit de nici un brevet- Biblioteca de compresie a datelor fără pierderi pentru utilizare pe orice hardware și sistem de operare. Formatul de date zlib este auto-portabil pe orice platformă. Spre deosebire de metoda de compresie LZW folosită în compresia Unix compress(1) și în formatul de imagine GIF, metoda de comprimare utilizată în mod curent în zlib nu extinde niciodată datele. (LZW poate dubla sau tripla mărimea fișierului în cazuri extreme). Amprenta de memorie a bibliotecii zlib este, de asemenea, independentă de datele de intrare și poate fi redusă, dacă este necesar, la un anumit raport de compresie.


</div>

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.


<div class="mw-translate-fuzzy">

#### libarea


</div>


<div class="mw-translate-fuzzy">

**Version:** N/A


</div>


<div class="mw-translate-fuzzy">

**License:** New BSD (BSD 3-Clause)


</div>


<div class="mw-translate-fuzzy">

Area is a piece of software created by Dan Heeks for HeeksCNC. It is employed as a library for generation of CAM related operations in the Path Workbench.


</div>

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.


<div class="mw-translate-fuzzy">

### LibPack

LibPack este un pachet convenabil cu toate bibliotecile de mai sus ambalate împreună. Este necesar doar dacă construiți pe Platforma Windows și îl puteți găsi la <https://github.com/FreeCAD/FreeCAD-ports-cache/releases>. Dacă lucrați sub Linux, trebuie să utilizați depozitele de pachete ale distribuției dvs. Linux, adică nu este nevoie de libPack și oferit pentru Linux.


</div>

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11


<div class="mw-translate-fuzzy">


{{docnav|Compiling (Speeding up)|Third Party Tools}}


</div>


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/ro
