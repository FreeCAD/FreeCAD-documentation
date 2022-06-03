# PythonOCC/pl
## Opis

[PythonOCC](PythonOCC/pl.md) jest projektem, który ma na celu dostarczenie całej gamy funkcji OpenCASCADE Technology *(OCCT)* poprzez moduł [Python](Python/pl.md) `OCC`. Stanowi to zupełnie inne podejście niżwe FreeCAD, gdzie tylko niektóre komponenty OCCT są eksponowane poprzez środowisko pracy [Część](Part_Workbench/pl.md).

PythonOCC, z kolei, ze względu na to, że zapewnia dostęp do wszystkich klas i funkcji OCCT, jest bardzo złożony, ale również bardzo potężny. Dlatego też jest to bardzo dobry dodatek do FreeCAD. Dlatego, gdy jesteś ograniczony funkcjonalnością OCCT FreeCAD, używanie `OCC` jest dobrą alternatywą.

## Użycie

Obecnie w środowisku pracy [Część](Part_Workbench/pl.md) mamy metody `Part.__toPythonOCC__()` i `Part.__fromPythonOCC__()` do wymiany `TopoDS_Shape` ([Część   * Kształt topologiczny](Part_TopoShape/pl.md)) podmiotów do i z PythonOCC. Metody te pozwalają nam na wykorzystanie pełnej mocy OCCT w środowisku Python, a następnie ponowne umieszczenie powstałych kształtów w obiektach FreeCAD.

PythonOCC jest wewnętrznie używany przez przeglądarkę [IFC](Arch_IFC.md) dołączoną do bibliotek [IfcOpenShell](IfcOpenShell.md). IfcOpenShell jest używany do odczytu i zapisu dokumentów [IFC](Arch_IFC/pl.md) przy użyciu FreeCAD, poprzez Środowiska pracy [Arch](Arch_Workbench/pl.md) i [BIM](BIM_Workbench/pl.md). PythonOCC jest potrzebny tylko do uruchomienia zintegrowanej przeglądarki IfcOpenShell, w innym przypadku w ogóle nie jest wykorzystywany przez FreeCAD.

## Instalacja

PythonOCC musi być skompilowany ze źródła. W tym celu musisz pobrać odpowiednie pliki programistyczne dla technologii [OpenCASCADE Technology](OpenCASCADE.md) *(OCCT)* i SWIG. Starsza wersja PythonOCC miała obejmować OCE 0.18, społeczną edycję OCCT 6.9.x, która obecnie nie jest utrzymywana. Najnowsza wersja PythonOCC jest teraz przeznaczona do współpracy z najnowszą, oficjalną wersją OCCT 7.4.

Wraz z OCCT 7.4, PythonOCC wymaga stosunkowo najnowszych zależności takich jak Python 3.7, CMake 3.12 i SWIG 3.0.11. Python 2 nie jest już obsługiwany.

Wraz z OCCT 7.4, PythonOCC wymaga stosunkowo najnowszych zależności takich jak   * Python 3.7, CMake 3.12 i SWIG 3.0.11. Python 2 nie jest już obsługiwany.

Możliwe jest również zainstalowanie prekompilowanych bibliotek PythonOCC przy użyciu Conda. Więcej informacji i instrukcji kompilacji można znaleźć w repozytorium projektu głównego, [tpaviot/pythonocc-core](https   *//github.com/tpaviot/pythonocc-core).

## Kompilacja

Możesz także samodzielnie skompilować pythonOCC *(zobacz [instrukcję](https   *//github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md))*. Poniżej znajduje się procedura dla Debiana/Ubuntu z użyciem pakietów opencascade dostarczonych przez distro   *

    git clone git   *//github.com/tpaviot/pythonocc-core.git pythonocc
    cd pythonocc
    mkdir build
    cd build
    cmake -DOCE_INCLUDE_PATH=/usr/include/opencascade -DOCE_LIB_PATH=/usr/lib/x86_64-linux-gnu ..
    make

## Informacje dodatkowe 

-   Strona projektu   * [pythonocc.org](http   *//www.pythonocc.org/)
-   Nowsza wersja kompatybilna z OCCT 7.4, [tpaviot/pythonocc-core](https   *//github.com/tpaviot/pythonocc-core).
-   Starsza wersja zgodna z OCE 0.18, społecznym wydaniem OCCT 6.9.x, [tpaviot/pythonocc](https   *//github.com/tpaviot/pythonocc).
-   [IfcPlusPlus skompilowany na Gentoo - pytania i alternatywy?](https   *//forum.freecadweb.org/viewtopic.php?f=39&t=33254)


 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > PythonOCC/pl
