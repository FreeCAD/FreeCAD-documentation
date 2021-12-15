# Installing additional components/pl
{{TOCright}}

# Wprowadzenie

Po zainstalowaniu FreeCAD w swoim systemie operacyjnym *([Linux](Installing_on_Linux/pl.md), [Mac](Installing_on_Mac/pl.md), lub [ Windows](Installing_on_Windows/pl.md))*, możesz rozważyć zainstalowanie jednego lub więcej z następujących dodatkowych komponentów.

# Pliki pomocy 

Dokumentacja offline nie jest dostarczana ze wszystkimi instalatorami, ale jest dostępna jako oddzielny pakiet. Zobacz dokument [Instalacja dokumentacji pomocy](Installing_Helpfile/pl.md) aby uzyskać więcej informacji.

# Zewnętrzne Środowiska pracy 

Poza standardowymi [Środowiskami pracy](workbenches/pl.md) dołączonymi do programu FreeCAD, dostępna jest coraz większa kolekcja użytecznych [dodatkowych Środowisk pracy](External_workbenches/pl.md) wykonanych przez członków społeczności.

# Oprogramowanie zewnętrzne 

FreeCAD obsługuje kilka pakietów oprogramowania pochodzących od innych deweloperów. W wielu przypadkach wystarczy zainstalować oprogramowanie, a gdy FreeCAD zostanie zrestartowany, automatycznie znajdzie i będzie mógł z niego korzystać.
Ta sekcja ma na celu dostarczenie listy wszystkich takich pakietów oprogramowania wraz z informacjami, gdzie jest ono używane we FreeCAD i gdzie można je pobrać.

## Wspierane

### GitPython

_ może korzystać z tej biblioteki. GitPython jest zawarty w instalatorach FreeCAD dla systemów Windows i Mac.

### GraphViz

_.

### OpenCAMLib

_ programu FreeCAD . Zobacz [jego stronę](OpenCamLib.md), aby uzyskać instrukcje instalacji.

### OpenSCAD

_, a środowisko _.

## Formaty plików 

Wszystkie programy w tej sekcji będą używane przez narzędzia _.

### CAD Exchanger 

Komercyjna aplikacja [CADExchanger](https://cadexchanger.com) z zamkniętym źródłem kodu, do wymiany danych w różnych formatach plików używanych w CAD. Istnieje [zewnętrzne Środowisko pracy](https://github.com/yorikvanhavre/CADExchanger) do korzystania z tej aplikacji w programie FreeCAD.

### DXF Importer 

FreeCAD posiada własnego importera i eksportera plików DXF, który zaprogramowano w C++. Obecnie importer ten nie implementuje wszystkich funkcji formatu DXF. Dla tych funkcji dostępny jest nadal starszy importer eksporter Python. Wymaga on biblioteki _ aby uzyskać więcej informacji.

### Konwerter DWG 

FreeCAD nie może bezpośrednio odczytywać i zapisywać plików DWG. Aby przekonwertować pliki DXF na pliki DWG i odwrotnie, FreeCAD polega na zewnętrznych konwerterach. Istnieje wbudowane wsparcie dla następujących konwerterów DWG:

-   [LibreDWG](https://www.gnu.org/software/libredwg) *(open-source, brak wsparcia dla niektórych elementów DWG)*.
-   [Konwerter plików w formacie ODA](https://www.opendesign.com/guestfiles/oda_file_converter) *(bezpłatny)*.
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) *(komercyjny)*. {{Version/pl|0.20}}

Zobacz strony [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md) i [FreeCAD i import DWG](FreeCAD_and_DWG_Import/pl.md), aby uzyskać więcej informacji.

### IfcOpenShell

_. ({{VersionMinus/pl|0.18}}) oraz narzędzia [BIM: IfcExplorer](BIM_IfcExplorer.md). IfcOpenShell jest zawarty w instalatorach FreeCAD dla Windows i Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) jest to biblioteka wymagana przy eksporcie do pliku w formacie IFCJSON. IFCJSON jest nowym formatem IFC, który nie jest jeszcze obsługiwany przez wiele aplikacji.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), znana również jako python-collada, jest biblioteką Pythona do czytania i tworzenia plikówów COLLADA *(DAE)*. Pycollada jest zawarta w instalatorach FreeCAD dla systemów Windows i Mac.

## Renderowanie

### LuxCoreRender

_. Oficjalnie nie jest wspierany przez środowisko _ po więcej informacji i instrukcje instalacji.

### LuxRender

_. W 2013 roku projekt został reaktywowany jako _ może działać ze środowiskiem Raytracing, może warto spróbować. Zobacz stronę [LuxRender](LuxRender/pl.md) po więcej informacji i instrukcje instalacji, oraz [LuxCoreRender](LuxCoreRender/pl.md) jeśli chcesz wypróbować bardziej nowoczesne oprogramowanie.

### POVRay

_. Więcej informacji i instrukcje instalacji można znaleźć na stronie [POV-Ray](POV-Ray/pl.md).

## Element końcowy 

## CalculiX

_.

## Gmsh

_ i narzędzia [Mesh: FromPartShape](Mesh_FromPartShape.md).

### Elmer

_.

### FEniCS

_.

### Z88

_. FreeCAD wymaga pakietu otwarto źródłowego Z88OS.

### OpenFOAM

_ i _.

# Warto odwiedzić 

-   [Import eksport](Import_Export/pl.md)
-   [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md)
-   [Biblioteki zewnętrzne](Third_Party_Libraries/pl.md)




_

---
[documentation index](../README.md) > Installing additional components/pl
