# Workbenches/pl
FreeCAD, podobnie jak wiele nowoczesnych aplikacji projektowych, takich jak [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit) lub [CATIA](https://en.wikipedia.org/wiki/CATIA), opiera się na koncepcji [Środowisk pracy](https://en.wikipedia.org/wiki/Workbench). Środowisko pracy może być traktowane jako zestaw narzędzi specjalnie pogrupowanych dla potrzeb realizacji konkretnego zadania. W tradycyjnym warsztacie meblowym miałbyś stół roboczy dla osoby pracującej z drewnem, inny dla osoby pracującej z metalowymi elementami, a może trzeci dla faceta, który montuje wszystkie elementy razem.

W programie **FreeCAD** stosuje się tę samą koncepcję. Narzędzia są pogrupowane w **Środowiska pracy** według zadań, które są z nimi związane.

Kiedy przełączasz się z jednego Środowiska pracy na drugie, zmieniają się narzędzia dostępne z poziomu interfejsu. Paski narzędzi, paski poleceń i ewentualnie inne części interfejsu przełączają się na nowe Środowisko pracy, ale zawartość Twojej sceny się nie zmienia. Możesz, na przykład, rozpocząć rysowanie kształtów 2D w Draft, a następnie pracować nad nimi dalej w Środowisku pracy Part.

Należy pamiętać, że czasami środowisko pracy jest nazywane **modułem**. Jednak środowiska pracy i moduły są różnymi częściami składowymi. Moduł to dowolne rozszerzenie FreeCAD, natomiast Środowisko pracy to specjalna konfiguracja GUI *(moduł)* grupująca niektóre paski narzędzi i menu.



## Wbudowane Środowiska pracy 



### Aktualne

Poniższe środowiska pracy są dostępne w każdej instalacji FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std: Base](Std_Base/pl.md). To nie jest tak naprawdę środowisko pracy, ale raczej kategoria \"standardowych\" poleceń i narzędzi, które mogą być używane we wszystkich środowiskach pracy.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Architektura](Arch_Workbench/pl.md) do pracy z elementami architektonicznymi.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) zawiera narzędzia 2D oraz podstawowe operacje CAD 2D i 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [MES](FEM_Workbench/pl.md) zapewnia przepływ pracy w zakresie analizy elementów skończonych *(Finite Element Analysis FEA)*.

-   <img alt="" src=images/_Workbench_Inspection.svg  style="width:32px;"> [Inspekcja](Inspection_Workbench/pl.md) ma na celu udostępnienie narzędzi do badania kształtów. Nadal jest w fazie rozwoju.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Siatka](Mesh_Workbench/pl.md) do pracy z siatkami o trójkątnych oczkach.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Workbench/pl.md) dla interoperacyjności z OpenSCAD i naprawiania historii modeli typu [konstrukcyjnej geometrii bryły](Constructive_solid_geometry/pl.md) *(CSG)*.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Część](Part_Workbench/pl.md) do pracy z pierwotnymi obiektami geometrycznymi i operacjami logicznymi.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Projekt Części](PartDesign_Workbench/pl.md) do budowy kształtów części ze szkiców.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Path](Path_Workbench/pl.md) jest używany do tworzenia operacji G-Code.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Punkty](Points_Workbench/pl.md) do pracy z chmurami punktów.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Inżynieria Wsteczna](Reverse_Engineering_Workbench/pl.md) ma na celu dostarczenie specyficznych narzędzi do konwersji kształtów/brył/siatek na parametryczne elementy kompatybilne z FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [Robot](Robot_Workbench/pl.md) do badania ruchów robotów. Obecnie nie jest utrzymywany.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Szkicownik](Sketcher_Workbench/pl.md) do pracy na szkicach z zachowaniem wiązań geometrii.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md) do tworzenia i manipulowania danymi w arkuszu kalkulacyjnym.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> [Start](Start_Workbench/pl.md) pozwala na szybkie przejście do jednego z najczęściej stosowanych stołów warsztatowych.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Powierzchnia](Surface_Workbench/pl.md) dostarcza narzędzi do tworzenia i modyfikowania powierzchni. Jest on podobny do narzędzia [konstruktora kształtu części](Part_Builder/pl.md) środowiska Część, z krawędzi.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) do tworzenia rysunków technicznych dla modeli przestrzennych. Jest to następca środowiska [Kreślenie](Drawing_Workbench/pl.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Test Framework](Testing/pl.md) służy do debugowania programu FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;">[Web](Web_Workbench/pl.md) udostępnia okno przeglądarki w oknie [widoku 3D](3D_view/pl.md) dla programiu FreeCAD.



### Przestarzałe

Następujące środowiska pracy nie są już zawarte w instalacji podstawowej po wersji 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> [Kreślenie](Drawing_Workbench/pl.md) został stworzony do przygotowania rysunku technicznego. Zobacz środowisko [Rysunek Techniczny](TechDraw_Workbench/pl.md), które jest bardziej zaawansowanym zamiennikiem.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> [Obraz](Image_Workbench/pl.md) służyło do pracy z grafikami bitmapowymi. Jego funkcjonalność została zintegrowana w [Narzędziach standardowych](Std_Base/pl.md).

Zobacz strony [Std: Import](Std_Import/pl.md) i [Std: Otwórz widok obrazu](Std_ViewLoadImage/pl.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> [Raytracing](Raytracing_Workbench/pl.md) do pracy z ray-tracingiem *(renderingiem)*. Zamiast tego należy użyć zewnętrznego środowiska [Render](https://github.com/FreeCAD/FreeCAD-render).



## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w [Python](Python.md). Dlatego też, wiele osób opracowuje dodatkowe stoły robocze wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera listę wszystkich, które są znane tej społeczności. Większość z nich można łatwo zainstalować z poziomu FreeCAD, używając [Menadżera dodatków](Std_AddonMgr/pl.md), znajdującego się w menu **Narzędzia → <img src="images/Std_AddonMgr.svg" width=24px> Menadżer dodatków**.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/pl
