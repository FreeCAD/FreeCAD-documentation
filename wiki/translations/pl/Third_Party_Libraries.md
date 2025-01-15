# Third Party Libraries/pl
## Informacje ogólne 

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
-   implementacji całych środowisk pracy, takich jak [Rysunek Roboczy](Draft_Workbench/pl.md) i [BIM](BIM_Workbench/pl.md),
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

OCCT to duży i złożony zestaw bibliotek C++, które zapewniają funkcjonalność wymaganą przez aplikacje CAD:

-   Kompletne jądro geometrii zgodne ze standardem STEP.
-   Topologiczny model danych oraz funkcje niezbędne do pracy z kształtami *(wycinanie, łączenie, wyciskanie i wiele innych)*.
-   Standardowe procesory importu i eksportu dla plików takich jak STEP, IGES, VRML.
-   Przeglądarka 2D i 3D z obsługą selekcji.
-   Struktura danych dokumentu i projektu z obsługą zapisywania i przywracania, zewnętrznego łączenia dokumentów, przeliczania historii projektu (modelowanie parametryczne) oraz możliwość dynamicznego wczytywania nowych typów danych jako pakietów rozszerzeń.

Przetłumaczono z www.DeepL.com/Translator (wersja darmowa)

Istnieją dwie główne wersje OpenCASCADE w różnych dystrybucjach Linuksa. Jedna z nich jest dystrybuowana przez oryginalnych twórców; znana jest jako OCCT i występuje pod nazwami `occ` lub `occt`. Druga wersja to \"community edition\", w skrócie OCE, i zwykle występuje pod nazwą `oce`. FreeCAD może kompilować się z każdą z tych wersji, jednak od 2016 roku FreeCAD zaleca kompilację z oficjalnymi bibliotekami OCCT, a nie z bibliotekami OCE. Powodem jest to, że w edycji społecznościowej brakuje ważnych poprawek błędów i funkcji, które sprawiają, że korzystanie z programu FreeCAD jest lepsze.

Aby dowiedzieć się więcej, odwiedź stronę [OpenCASCADE](http://www.opencascade.org).



### Qt

**Wersja:** 4.1 lub nowsza

**Licencja:** GPL v2.0/v3.0 lub komercyjna, od wersji 4.5 także LPGL v2.1.

Qt jest jednym z najpopularniejszych zestawów narzędzi graficznego interfejsu użytkownika *(GUI)* dostępnych w świecie open source. FreeCAD używa tego zestawu narzędzi do rysowania interfejsu programu. Do tego celu bardzo przydatna jest aplikacja Qt Designer, która pozwala programistom szybko rysować okna dialogowe i okna, eksportować je jako pliki zasobów XML, a następnie wczytywać te interfejsy w czasie pracy.

Więcej informacji o bibliotekach Qt i ich dokumentacji programistycznej można znaleźć na stronie [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).



#### Shiboken2 i Pyside2 

Shiboken jest generatorem wiązań Python, którego Qt dla Python używa do tworzenia modułu PySide, innymi słowy, jest to system używany do eksponowania API Qt C++ na język Python.

Oryginalne pakiety Shiboken i PySide były przeznaczone do użycia ze środowiskiem Python 2 i Qt4. Ponieważ te dwie wersje są uważane za przestarzałe w 2019 roku, proszę użyć Shiboken2 i PySide2, które działają ze środowiskiem Python 3 i Qt5. Nowe wersje FreeCAD są tworzone w środowisku Python 3 i Qt5, więc kompatybilność z Python 2 i Qt4 nie jest gwarantowana po wydaniu FreeCAD 0.18.

Więcej o Shiboken i Pyside można przeczytać na stronie [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).



### Coin3D

**Wersja:** 3.0 lub nowsza

**Licencja:** 3-klauzulowa licencja BSD

Coin3D jest wysokopoziomową biblioteką grafiki 3D z interfejsem programowania aplikacji w języku C++. Wykorzystuje struktury danych scenegrafu do renderowania grafiki w czasie rzeczywistym, odpowiedniej dla wszelkiego rodzaju zastosowań naukowych i inżynieryjnych.

Coin3D jest zbudowany na standardowej bibliotece renderingu trybu natychmiastowego OpenGL i dodaje abstrakcje dla prymitywów wyższego poziomu, zapewnia interaktywność 3D i zawiera wiele złożonych funkcji optymalizacyjnych dla szybkiego renderingu, które są przezroczyste dla programisty aplikacji.

Coin3D jest kompatybilny z Open Inventor 2.1 API firmy SGI. API to stało się de facto standardowym interfejsem graficznym dla wizualizacji 3D w środowisku naukowym i inżynieryjnym. Od 2000 roku udowodnił swoją wartość jako główny element tysięcy aplikacji inżynierskich na całym świecie.

Coin3D *(Open Inventor)* jest używany jako przeglądarka 3D w FreeCAD, ponieważ przeglądarka OpenCASCADE *(AIS i Graphics3D)* ma ograniczenia i wąskie gardła wydajności, zwłaszcza w przypadku renderowania inżynierskiego na dużą skalę. Inne rzeczy, takie jak tekstury czy renderowanie objętościowe, nie są w pełni obsługiwane przez przeglądarkę OpenCASCADE.

Coin3D jest przenośny na szeroką gamę platform: UNIX, Linux, BSD, MacOS X oraz systemy operacyjne Microsoft Windows. Aby dowiedzieć się więcej o tej bibliotece, odwiedź stronę [domową Coin3D](https://github.com/coin3d/coin).



#### SoQt *(obecnie przestarzałe)* 

**Wersja:** 1.2.0 lub nowsza

**Licencja:** 3-klauzulowa licencja BSD

SoQt jest powiązaniem Coin3D *(Open Inventor)* z zestawem narzędzi GUI Qt.

SoQt nie jest już używany w programie FreeCAD, został zastąpiony przez Quarter, który jest nowszą oprawą Qt.



#### Quarter

**Wersja:** 1.0 lub nowsza

**Licencja:** 3-klauzulowa licencja BSD

Quarter to nowsze powiązanie Coin3D z zestawem narzędzi Qt. Jego wersja jest zawarta w kodzie źródłowym FreeCAD, więc jest kompilowana razem z nim.



#### Pivy

**Wersja:** 0.6.3 lub nowsza

**Licencja:** 3-klauzulowa licencja BSD

[Pivy](Pivy/pl.md) jest biblioteką, która opakowuje bibliotekę Coin3d do użytku w środowisku [Python](Python/pl.md). Nie jest potrzebna do zbudowania programu FreeCAD ani do jego uruchomienia, ale jest wymagana jako zależność runtime przez [Rysunek Roboczy](Draft_Workbench/pl.md) i przez inne środowiska pracy, które używają jej wewnętrznie, jak [Architektura](Arch_Workbench/pl.md) i [BIM](BIM_Workbench/pl.md).

Jeśli nie zamierzasz korzystać z tych środowisk pracy, nie potrzebujesz Pivy.



### Ply

**Wersja:** 3.11 lub nowsza

**Licencja:** 3-klauzulowa licencja BSD

Ply jest parserem Python-Lex-Yacc. Jest on używany jako zależność runtime przez środowisko [OpenSCAD](OpenSCAD_Workbench/pl.md). Jeśli nie używasz tego środowiska pracy, możesz nie potrzebować tego pakietu.

Więcej informacji można znaleźć na stronie [domowej Ply](https://www.dabeaz.com/ply/).



### Xerces-C++ 

**Wersja:** 3.0 lub nowsza

**Licencja:** Licencja oprogramowania Apache wersja 2.0

Xerces-C++ jest sprawdzającym poprawność parserem XML napisanym w przenośnym podzbiorze języka C++. Xerces-C++ ułatwia nadanie aplikacji możliwości odczytu i zapisu danych XML. Udostępnia bibliotekę współdzieloną do parsowania, generowania, manipulowania i sprawdzania poprawności dokumentów XML. Xerces-C++ jest wierny zaleceniu XML 1.0 i związanym z nim standardom.

Parser jest używany do zapisywania i przywracania parametrów w programie FreeCAD. Więcej informacji można znaleźć na stronie [domowej Xerces-C++](https://xerces.apache.org/xerces-c/).



### Eigen3

**Wersja:** 3.0 lub nowsza

**Licencja:** Począwszy od wersji 3.1.1, program jest objęty licencją [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Wcześniejsze wersje były licencjonowane na podstawie [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen jest biblioteką szablonów C++ dla algebry liniowej: macierzy, wektorów, rozwiązań numerycznych i związanych z nimi algorytmów.

Jeśli użytkownik chce tylko używać programu Eigen, może od razu korzystać z plików nagłówkowych. Nie ma biblioteki binarnej, z którą trzeba by się łączyć, ani skonfigurowanego pliku nagłówkowego. Eigen jest czystą biblioteką szablonową zdefiniowaną w nagłówkach.

Program Eigen jest używany w programie FreeCAD do wielu operacji na wektorach w przestrzeni 3D. Aby dowiedzieć się więcej, odwiedź stronę [domową Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page).



### Zipios++

**Wersja:** 0.1.5 lub nowsza

**Licencja:** GNU Lesser General Public License 2.1

Zipios++ jest biblioteką C++ służącą do odczytywania i zapisywania plików `.zip`. Dostęp do poszczególnych wpisów jest zapewniony przez standardowe strumienie iostream w C++. Udostępniono także prosty wirtualny system plików tylko do odczytu, który montuje zwykłe katalogi i pliki `.zip`. Struktura i interfejs publiczny programu Zipios++ są luźno oparte na pakiecie `java.util.zip` języka Java.

Rodzimy format plików FreeCAD `.FCstd` jest w rzeczywistości plikiem `.zip`, który przechowuje i kompresuje inne typy danych, takie jak pliki BREP i XML. Dlatego program Zipios++ służy do zapisywania i otwierania skompresowanych archiwów, w tym plików FreeCAD.

Kopia Zipios++ jest zawarta w kodzie źródłowym FreeCAD, więc jest kompilowana razem z nim. Jeśli chcesz użyć zewnętrznej biblioteki Zipios++, dostarczanej przez system operacyjny, możesz ustawić parametr -DFREECAD_USE_EXTERNAL_ZIPIOS=ON za pomocą `cmake`.

Do dekompresji plików Zipios++ używa biblioteki Zlib.



#### Zlib

**Wersja:** 1.0 lub nowsza

**Licencja:** licencja zlib

Zlib został zaprojektowany jako bezpłatna biblioteka ogólnego przeznaczenia do bezstratnej kompresji danych, przeznaczona do użytku na dowolnym sprzęcie komputerowym i w dowolnym systemie operacyjnym. Implementuje ona algorytm kompresji `DEFLATE` powszechnie stosowany w plikach `.zip` i `.gzip`.

Kopia tej biblioteki jest dołączona do kodu źródłowego programu FreeCAD, więc jest z nim kompilowana.



### libarea

**Wersja:** 0.0.20140514-1 lub nowsza

**Licencja:** 3-klauzulowa licencja BSD

Libarea to biblioteka oprogramowania do obliczania profili i operacji kieszeni, które są używane w oprogramowaniu do komputerowego wspomagania wytwarzania *(CAM)*. Została ona stworzona przez Dana Heeksa dla jego projektu HeeksCNC.

Kopia biblioteki jest dołączona do kodu źródłowego środowiska pracy [CAM](CAM_Workbench/pl.md), więc jest kompilowana razem z nim.



## LibPack

LibPack jest wygodnym pakietem z zebranymi razem zależnościami kompilacji programu FreeCAD. Jest on potrzebny tylko wtedy, gdy kompilujesz program FreeCAD w systemie Windows za pomocą Visual Studio 2015 lub nowszego. Najnowszy LibPack można znaleźć na stronie [releases page](https://github.com/FreeCAD/FreeCAD/releases).

Jeśli pracujesz pod Linuksem, nie potrzebujesz LibPacka, ponieważ możesz pobrać zależności z repozytoriów swojej dystrybucji, jak wspomniano na stronie [Kompilacja w systemie Linux](Compile_on_Linux/pl.md).



### FreeCAD 12.1.2 

Zobacz ogłoszenie na forum: [Nowe pakiety libpacks dla Windows z Qt5.12, OCC7.3 i Pythonem 3.6 autorstwa apeltauera](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

Zawiera on między innymi: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Third Party Libraries/pl
