# Release notes 1.0/pl
**FreeCAD 1.0 jest w trakcie rozwoju, nie ma jeszcze oczekiwanej daty wydania.**


{{Message|
Czy brakuje jakichś funkcji? Wspomnij o nich w wątku na forum [https   *//forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Informacje o wydaniu v1.0].

Więcej informacji na temat sposobów przyczyniania się do rozwoju programu FreeCAD można znaleźć na stronie [Pomóż w rozwoju FreeCAD](Help_FreeCAD/pl.md).}}


{{Message|Wszystkie obrazy na tej stronie muszą używać przyrostka **_relnotes_1.0**.}}


{{TOCright}}

**FreeCAD 1.0** was released on **DD MM 2023**, get it from the [Download](Download.md) page. This page lists all new features and changes.

Older FreeCAD release notes can be found in the [Feature list](Feature_list#Release_notes.md).

Placeholder for an eye-catching image selected by the admins from the [user showcases forum](https   *//forum.freecadweb.org/viewforum.php?f=24).

## Informacje ogólne 

## Interfejs użytkownika 

### Planowane ulepszenie dla interfejsu użytkownika 

## System podstawowy i API 

### Rdzeń programu 

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### Nowe skrypty Python 


<div class="mw-collapsible-content">

-   *ShapeFix\_EdgeConnectPy*   * Klasa podstawowa dla operacji naprawczych. [commit 4d4adb93](https   *//github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix\_EdgePy*   * Naprawa nieprawidłowych krawędzi. [commit 4089cbfb](https   *//github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix\_FaceConnectPy*   * Odbudowuje połączenia między powierzchniami w powłoce. [commit a0eb2e9d](https   *//github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix\_FacePy*   * Klasa umożliwiająca wykonywanie operacji na powierzchniach. [commit b6cd635c](https   *//github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix\_FixSmallFacePy*   * Klasa umożliwiająca przeprowadzenie operacji naprawczych na powierzchniach. [commit 4c2946c8](https   *//github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix\_FixSmallSolidPy*   * Naprawa brył o niewielkich rozmiarach. [commit b70d8d37](https   *//github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix\_FreeBoundsPy*   * Przeznaczone do wyprowadzania swobodnych granic kształtu. [commit 1ee1aee1](https   *//github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix\_RootPy*   * Klasa podstawowa dla operacji naprawczych. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_ShapePy*   * Klasa do przeprowadzania operacji naprawczych na kształtach. [commit 87db9dcc](https   *//github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix\_ShapeTolerancePy*   * Modyfikuje tolerancje kształtów podrzędnych *(wierzchołków, krawędzi, ścian)*. [commit 125d5b63](https   *//github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix\_ShellPy*   * Klasa podstawowa dla operacji naprawczych. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_SolidPy*   * Klasa podstawowa dla operacji naprawczych. [commit 8d568793](https   *//github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix\_SplitCommonVertexPy*   * Klasa do przeprowadzania operacji naprawczych na kształtach. [commit 4b44c54c](https   *//github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix\_SplitToolPy*   * Narzędzie do rozszczepiania i cięcia krawędzi. [commit bbecc3f2](https   *//github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix\_WireframePy*   * Przedstawia metody naprawiania szkieletu kształtu. [commit 6843a461](https   *//github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix\_WirePy*   * Klasa do przeprowadzania operacji naprawczych na poliliniach. [commit 94f6279a](https   *//github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix\_WireVertexPy*   * Naprawia rozłączone krawędzie w linii łamanej. [commit 8c6ffc99](https   *//github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>

#### Zmienione API Phyton 


</div>

## Menadżer dodatków 

## Środowisko pracy Architektura 

## Środowisko pracy Rysunek Roboczy 

### Planowane ulepszenie dla środowiska Rysunek Roboczy 

## Środowisko pracy MES 

### Planowane ulepszenie dla środowiska MES 

## Eksport

## Środowisko pracy Siatka 

### Planowane ulepszenie dla środowiska Siatka 

## Planowane ulepszenie dla środowiska OpenSCAD 

## Środowisko pracy Część 

### Planowane ulepszenie dla środowiska Część 

## Środowisko pracy Projekt Części 

### Planowane ulepszenia dla środowiska Projekt Części 

## Środowisko pracy Path 

-   Integracja Camotics. Jeśli zainstalowana jest aplikacja Camotics *(wersja 1.2.2 lub nowsza)*, do paska narzędzi Path zostanie dodana nowa ikona. Wybierz zadanie Path i naciśnij przycisk, aby otworzyć okno dialogowe Camotics. Następnie przeciągnij suwak, aby wygenerować symulowaną bryłę w dowolnym punkcie zadania. Można również uruchomić pełną aplikację Camotics, aby uruchomić animowaną symulację. Powoduje to uzyskanie cichego post-processingu zadania i utworzenie pliku projektu camotics. [Pull request \#6637](https   *//github.com/FreeCAD/FreeCAD/pull/6637)

-   Dodatkowe łańcuchy zastępcze do automatycznego nazywania wyjść. Jeśli dane wyjściowe są dzielone na wiele plików, nazwy plików mogą automatycznie zastępować etykietę kontrolera narzędzi, WCS lub etykietę operacji. Jest to dodatek do innych istniejących ciągów zastępczych, takich jak data, nazwa zadania itp.

## Środowisko pracy Plot 

## Środowisko pracy Szkicownik 

### Planowane ulepszenia dla środowiska Szkicownik 

## Środowisko pracy Arkusz Kalkulacyjny 

### Planowane ulepszenia dla środowiska Arkusz Kalkulacyjny 

## Środowisko pracy Rysunek Techniczny 

### Planowane ulepszenia środowiska Rysunek Techniczny 

## Środowisko pracy Web 

## Zewnętrzne Środowiska pracy 

### Środowisko pracy A2plus 

### Środowisko pracy Złożenie 3 

### Środowisko pracy Złożenie 4 

### FCGear

### Środowisko pracy Statek 

## Kompilacja

Since this release FreeCAD can only be compiled using Qt 5.x and Python 3.x. The lowest supported Python version is 3.8 according to the [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

To compile FreeCAD see the instructions for [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [MacOS](Compile_on_MacOS.md).

The supported operating systems are   *

-   Windows 7, 8, 10 and 11
-   Linux Ubuntu Focal Fossa (20.04) and newer
-   MacOS   * 10.12 Sierra or newer

## Znane ograniczenia 

### Windows 32bit 

Już od wersji 0.19 FreeCAD oficjalnie nie obsługuje 32-bitowych systemów Windows. Może działać na nich, ale nie zapewniamy wsparcia dla tych systemów.

### Pulpit zdalny w systemie Windows 

W zależności od możliwości graficznych OpenGL komputera, może się zdarzyć, że podczas uruchamiania programu FreeCAD za pośrednictwem pulpitu zdalnego wystąpi awaria. Aby to naprawić, zaktualizuj sterownik OpenGL. Jeśli to nie pomoże   *

-   Pobierz [bibliotekę OpenGL](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) dla 64-bitowego systemu Windows i rozpakuj ją.
-   Zmień nazwę pliku DLL na *opengl32sw.dll* i skopiuj go do podfolderu *bin* w folderze instalacyjnym FreeCADa (nadpisz tam istniejącą bibliotekę DLL).

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/pl
