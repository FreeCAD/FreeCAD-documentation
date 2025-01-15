# BIM Workbench/pl
**W wersji 1.0 środowiska robocze BIM, Native-IFC i [Architektura](Arch_Workbench/pl.md) zostały połączone w zintegrowane środowisko pracy BIM.<br>
Ta strona została zaktualizowana dla tej wersji.**

<img alt="Ikonka FreeCAD dla zewnętrznego Środowiska pracy BIM" src=images/Workbench_BIM.svg  style="width:128px;">






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektura](Arch_Workbench/pl.md) zapewnia nowoczesny przepływ pracy dla FreeCAD [Building **B**uilding **I**nformation **M**odelling](https://en.wikipedia.org/wiki/Building_information_modeling) *(BIM)*, z obsługą funkcji takich jak w pełni parametryczne obiekty architektoniczne, takie jak ściany, belki, dachy, okna, schody, rury i meble. Obsługuje pliki [**I**ndustry **F**oundation **C**lasses](Arch_IFC/pl.md) *(IFC)* oraz tworzenie planów pięter 2D w połączeniu z środowiskiem pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md).

Środowisko pracy BIM importuje wszystkie narzędzia środowiska <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), ponieważ używa obiektów 2D do budowy swoich przestrzennych obiektów architektonicznych. Niemniej jednak może używać kształtów brył utworzonych w innych środowiskach pracy, takich jak <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) i <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Zobacz [Przewodnik migracji FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) aby uzyskać szybki przegląd, jeśli jesteś już użytkownikiem innej aplikacji BIM.

Twórcy środowisk Rysunek Roboczy i BIM współpracują również z większą [społecznością OSArch](https://osarch.org), mając na uwadze ostateczny cel, jakim jest poprawa projektowania budynków przy użyciu całkowicie wolnego oprogramowania.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">



## Rozpoczęcie pracy 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Przy pierwszym uruchomieniu środowiska pracy BIM wyświetlane jest okno powitalne, który umożliwia szybki przegląd działania środowiska pracy i pozwala użytkownikowi na rozpoczęcie [Poradnika: Obsługa BIM](BIM_ingame_tutorial/pl.md). Okno powitalne jest również dostępne z menu **pomoc**. Gdy ekran powitalny zostanie zamknięty przez kliknięcie OK, pojawi się okno dialogowe [Konfiguracja środowiska BIM](BIM_Setup/pl.md), które pozwala użytkownikowi na szybkie ustawienie niektórych z najczęściej używanych preferencji programu FreeCAD, związanych z BIM bez potrzeby przeglądania pełnych [stron preferencji FreeCAD](Preferences_Editor/pl.md).

Narzędzie [Konfiguracja środowiska](BIM_Setup/pl.md) pozwala na szybką konfigurację projektu BIM poprzez wypełnienie kilku podstawowych informacji o projekcie. Następnie można, na przykład, użyć różnych narzędzi kreślarskich 2D do szkicowania wytycznych i linii bazowych, a następnie użyć różnych narzędzi do modelowania 3D, aby automatycznie zbudować z nich obiekty 3D BIM. Na przykład linia może stać się ścianą, wystarczy ją wybrać i nacisnąć przycisk [Ściana](Arch_Wall/pl.md).

Powszechne elementy budowlane, takie jak [ściany](Arch_Wall/pl.md) lub [kolumny](BIM_Column/pl.md) można łatwo tworzyć wciskając odpowiedni przycisk z paska narzędzi i klikając punkty w widoku 3D. Mogą one być przesuwane, obracane i edytowane po utworzeniu. Większość elementów BIM jest tworzonych na bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md), więc typowe podejście uwzględnia umieszczenie najpierw płaszczyzny roboczej a następnie utworzenie elementu BIM. Więcej złożonych elementów można tworzyć rysując najpierw elementy 2D a następnie korzystając z jednego z odpowiednich narzędzi BIM aby przekształcić je w pożądane elementy.

Elementy projektów budowlanych mogą być organizowane przy pomocy [terenów](Arch_Site/pl.md), [budynków](Arch_Building/pl.md) i [poziomów](Arch_BuildingPart/pl.md), aby odtworzyć to, co jest zwykle robione w innych programach BIM. We FreeCAD jednak te struktury nie są obowiązkowe i masz wolność organizowania elementów modelu tak jak uważasz, np. używając [grup](Std_Group/pl.md).

Rysunki 2D można generować z modelu aby przedstawić widok planu, sekcji lub elewacji. Aby generować takie rysunki, [płaszczyzny przekroju](Arch_SectionPlane/pl.md) są umieszczane w modelu, aby wskazać gdzie powinien on być przecięty lub skąd oglądany. Gdy płaszczyzny przekroju są na miejscu, możliwe są dwa podejścia:

1.  Utwórz rzutowane widoki w dokumencie przy pomocy [widoków kształtów](Draft_Shape2DView/pl.md), następnie dodaj wszystkie niezbędne adnotacje, takie jak teksty i wymiary a potem umieść to wszystko na stronie. To zalecany sposób, ponieważ oferuje więcej swobody.
2.  Utwórz widok na stronie bezpośrednio z płaszczyzny przekroju. Następnie wszystkie niezbędne adnotacje 2D muszą albo być dodane do tej płaszczyzny przekroju albo wykonane bezpośrednio na stronie. To mniej swobodna opcja.

Wreszcie, plany ilościowe można tworzyć przy pomocy narzędzia [Obmiar](Arch_Schedule/pl.md).

Jeśli jesteś przyzwyczajony do innej aplikacji BIM, sprawdź naszą [tabela zgodności zastosowań BIM](BIM_application_compatibility_table/pl.md), aby uzyskać swoje oceny podczas rozpoczynania pracy z FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Samouczek [Obsługa BIM](BIM_ingame_tutorial/pl.md) jest łatwym sposobem na szybkie rozpoczęcie pracy ze środowiskiem BIM.



## Przybory

Środowisko pracy BIM gromadzi narzędzia z kilku innych środowisk pracy FreeCAD, głównie [Rysunek Roboczy](Draft_Workbench/pl.md) i [Część](Part_Workbench/pl.md), z grubsza zreorganizowane w logiczne kategorie.

Dodatkowo, jeżeli są zainstalowane [dodatki](External_workbenches/pl.md), narzędzia ze środowiska [Zbrojenie](Reinforcement_Workbench/pl.md) *(dodatkowe narzędzia do prętów zbrojeniowych)*, [Elementy złączne](Fasteners_Workbench/pl.md) *(śruby i wkręty)*, [Flamingo / Dodo](Flamingo_Workbench/pl.md) *(narzędzia do konstrukcji stalowych i rurociągów)* oraz [Biblioteka podzespołów](Parts_Library_Workbench/pl.md) są automatycznie dołączane do środowiska BIM.

Środowisko pracy BIM dodaje również serię pozycji w *pasku statusu* programu FreeCAD, oraz kilka pozycji *menu kontekstowego*, dostępnych po kliknięciu prawym przyciskiem myszy w widoku 3D lub w widoku drzewa.



### Rysunki 2D 

Obiekty 2D są powszechnie używane jako pomoce kreślarskie, lub do rysowania linii bazowych i profili, na których można budować obiekty BIM. Mogą być również używane do kreślenia symboli i adnotacji w modelu. Oprócz szkiców, które używają swojego własnego układu współrzędnych, obiekty 2D będą rysowane na bieżącej [płaszczyżnie roboczej](Draft_SelectPlane/pl.md).

-   <img alt="" src=images/BIM_Sketch.svg‎‎  style="width:32px;"> [Szkic](BIM_Sketch/pl.md): Tworzy nowy szkic i przechodzi do trybu edycji szkicu. Szkice są zaawansowanymi obiektami 2D z obsługą wiązań.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linia](Draft_Line/pl.md): tworzy linię prostą.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinia](Draft_Wire/pl.md): tworzy polilinię, czyli sekwencję kilku połączonych segmentów linii.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Okrąg](Draft_Circle/pl.md): tworzy okrąg na podstawie środka i promienia.

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Łuk](Draft_Arc/pl.md): tworzy łuk kołowy z punktu środka, promienia, kąta początkowego i kąta rozwarcia.

-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Łuk przez trzy punkty](Draft_Arc_3Points/pl.md): tworzy łuk okręgu z trzech punktów, które definiują jego przebieg.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Zaokrąglenie](Draft_Fillet/pl.md): tworzy zaokrąglenie, zaokrąglony narożnik, lub fazę, prostą krawędź, pomiędzy dwoma [liniami](Draft_Line/pl.md).

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipsa](Draft_Ellipse/pl.md): tworzy elipsę z dwóch punktów definiujących prostokąt, w którym elipsa będzie wpisana.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Wielokąt](Draft_Polygon/pl.md): tworzy wielokąt foremny o zadanym punkcie środkowym i promieniu.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Prostokąt](Draft_Rectangle/pl.md): tworzy prostokąt z dwóch punktów.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [Krzywa złożona](Draft_BSpline/pl.md): tworzy krzywą złożoną z kilku punktów.

-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Krzywa Bezier\'a](Draft_BezCurve/pl.md): tworzy krzywą Béziera z kilku punktów.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Sześcienna krzywa Beziera](Draft_CubicBezCurve/pl.md): tworzy krzywą Béziera trzeciego stopnia.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/pl.md): tworzy zwykły punkt.



### 3D / BIM 

Obiekty 3D i BIM są elementami świata rzeczywistego, które składają się na Twój projekt BIM.

-   <img alt="" src=images/BIM_Project.svg  style="width:32px;"> [Projekt](BIM_Project/pl.md): Tworzy projekt IFC zawierający wybrane obiekty.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Teren](Arch_Site/pl.md): Tworzy teren z uwzględnieniem wybranych obiektów.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Budynek](Arch_Building/pl.md): Tworzy budynek wraz z wybranymi obiektami.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piętro](Arch_Floor/pl.md): Tworzy piętro obejmujące wybrane obiekty.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Kubatura](Arch_Space/pl.md): Tworzy obiekt kubatury.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Ściana](Arch_Wall/pl.md): Tworzy ścianę od podstaw lub używając wybranego obiektu jako podstawy.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Ściana kurtynowa](Arch_CurtainWall/pl.md): Tworzy ścianę kurtynową od podstaw lub używając wybranego obiektu jako bazy.

-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Słup](BIM_Column/pl.md): Tworzy pionowy element [konstrukcji](Arch_Structure/pl.md) w danym punkcie, opcjonalnie używając wybranego obiektu jako profilu.

-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Belka](BIM_Beam/pl.md): Tworzy poziomy element [konstrukcji](Arch_Structure/pl.md) pomiędzy dwoma punktami, opcjonalnie używając wybranego obiektu jako profilu.

-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Płyta](BIM_Slab/pl.md): Tworzy płaski element [konstrukcji](Arch_Structure/pl.md) poprzez wyciągnięcie wybranego płaskiego obiektu.

-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Drzwi](BIM_Door/pl.md): Tworzy obiekt [Okno](Arch_Window/pl.md) przy użyciu ustawień wstępnych drzwi.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Okno](Arch_Window/pl.md): Tworzy okno od podstaw lub używając wybranego obiektu jako bazy.

-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Rura](Arch_Pipe/pl.md): Tworzy rurę.

-   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Kształtka](Arch_PipeConnector/pl.md): Tworzy połączenie kolankiem lub połączenie typu trójnik między dwoma lub trzema wybranymi rurami.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Schody](Arch_Stairs/pl.md): Tworzy obiekt schodów.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/pl.md): Tworzy spadzisty dach z wybranych linii łamanych.

-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel/pl.md): Tworzy obiekt panelu z wybranego obiektu 2D.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ramy](Arch_Frame/pl.md): Tworzy obiekt ramy na podstawie wybranego układu.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Ogrodzenie](Arch_Fence/pl.md): Tworzy obiekt ogrodzenia z wybranego słupka i ścieżki.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Kratownica](Arch_Truss/pl.md): Tworzy kratownicę na podstawie wybranej linii lub od podstaw.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Wyposażenie](Arch_Equipment/pl.md): Tworzy obiekt wyposażenia lub mebli.

-   Narzędzia zbrojenia:

:   Narzędzia te, z wyjątkiem pierwszego, są dostępne tylko po zainstalowaniu środowiska pracy [Zbrojenie](Reinforcement_Workbench/pl.md).

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): Tworzy niestandardowy pręt zbrojeniowy w wybranym elemencie konstrukcyjnym za pomocą szkicu.

  -<img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Pręty zbrojeniowe proste](Reinforcement_StraightRebar/pl.md): Tworzy prosty pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [Pręty zbrojeniowe typu U](Reinforcement_UShapeRebar/pl.md): Tworzy pręt zbrojeniowy w kształcie litery U w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [Pręty zbrojeniowe typu L](Reinforcement_LShapeRebar/pl.md): Tworzy pręt zbrojeniowy w kształcie litery L w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Strzemiona zbrojeniowe](Reinforcement_StirrupRebar/pl.md): Tworzy pręt zbrojeniowy strzemion w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Pręty zbrojeniowe wygięte](Reinforcement_BentShapeRebar/pl.md): Tworzy pręt zbrojeniowy typu wygiętego w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Pręty zbrojeniowe spiralne](Reinforcement_HelicalRebar/pl.md): Tworzy spiralny pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Zbrojenie słupa](Reinforcement_ColumnRebars/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa prostokątnego.

  - <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Zbrojenie belki](Reinforcement_BeamRebars/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym belki.

  - <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Zbrojenie płyty](Reinforcement_SlabRebars/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym płyty.

  - <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Zbrojenie stóp fundamentowych](Reinforcement_FootingRebars/pl.md): Tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcyjnego ławy fundamentowej.

-   Ogólne narzędzia 3D:

:   Narzędzia te tworzą ogólne obiekty 3D, które można przekształcić lub wykorzystać w komponentach BIM.

  - <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/pl.md): Tworzy parametryczny profil 2D.

  - <img alt="" src=images/BIM_Box.svg  style="width:32px;"> [Prostopadłościan](BIM_Box.md): Tworzy prostopadłościan poprzez graficzne określenie jego wymiarów.

  - <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Konstruktor kształtu \...](Part_Builder/pl.md): Tworzy bardziej złożone kształty z różnych pierwotnych elementów geometrycznych.

  - Polecenie <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Łącznik kształtów](Draft_Facebinder/pl.md): tworzy obiekt powierzchni z wybranych ścian.

  - <img alt="" src=images/BIM_Library.svg  style="width:32px;"> [Biblioteka obiektów](BIM_Library/pl.md): Wstawia obiekt wyposażenia lub mebla. Wymaga dodatku [Środowisko pracy biblioteka podzespołów](Parts_Library/pl.md).

  - <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Komponent](Arch_Component/pl.md): Tworzy nieparametryczny komponent architektury.

  - <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Odniesienie](Arch_Reference/pl.md): Łączy obiekty z innego pliku FreeCAD do bieżącego dokumentu.



### Adnotacje

Adnotacje są wizualnymi obiektami pomocniczymi, które mogą być umieszczone wewnątrz Twojego modelu. Mogą one być użyte do eksportu modelu bezpośrednio do formatu 2D jak [DXF](Draft_DXF/pl.md), lub ponownie użyte podczas tworzenia widoków 2D Twojego modelu za pomocą środowiska [Rysunek Techniczny](TechDraw_Workbench/pl.md).

-   <img alt="" src=images/BIM_Text.svg  style="width:32px;"> [Tekst](BIM_Text/pl.md): Tworzy tekst 2D w dokumencie lub na stronie środowiska Rysunek Techniczny.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Kształt z tekstu](Draft_ShapeString/pl.md): Tworzy kształt złożony, który reprezentuje ciąg tekstowy.

-   <img alt="" src=images/BIM_DimensionAligned.svg  style="width:32px;"> [Wymiar dopasowany](BIM_DimensionAligned/pl.md): Tworzy wymiar wyrównany z dwoma punktami lub wybraną krawędzią.

-   <img alt="" src=images/BIM_DimensionHorizontal.svg  style="width:32px;"> [Wymiar poziomy](BIM_DimensionHorizontal/pl.md): Tworzy poziomy wymiar między dwoma punktami lub ze wskazanej krawędzi.

-   <img alt="" src=images/BIM_DimensionVertical.svg  style="width:32px;"> [Wymiar pionowy](BIM_DimensionVertical/pl.md): Tworzy pionowy wymiar między dwoma punktami lub z wybranej krawędzi.

-   <img alt="" src=images/BIM_Leader.svg  style="width:32px;"> [Linia odniesienia](BIM_Leader/pl.md): Tworzy polilinię 2-segmentową ze strzałką na końcu, do użycia jako linia odniesienia w połączeniu z [tekstem](BIM_Text/pl.md).

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etykieta](Draft_Label/pl.md): tworzy tekst wielowierszowy z dwu-segmentową linią wiodącą i strzałką.

-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Osie](Arch_Axis/pl.md): Dodaje zestaw osi jednokierunkowych.

-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Układ osi](Arch_AxisSystem/pl.md): Dodaje układ osi składający się z kilku osi.

-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Siatka](Arch_Grid/pl.md): Dodaje obiekt przypominający siatkę.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Płaszczyzna przekroju](Arch_SectionPlane/pl.md): Dodaje obiekt płaszczyzny przekroju.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Kreskowanie](Draft_Hatch/pl.md): Tworzy kreskowania na płaskich powierzchniach wybranego obiektu.

-   <img alt="" src=images/BIM_TDPage.svg  style="width:32px;"> [Strona](BIM_TDPage/pl.md): Tworzy [stronę środowiska Rysunek Techniczny](TechDraw_PageTemplate/pl.md) z pliku szablonu SVG.

-   <img alt="" src=images/BIM_TDView.svg  style="width:32px;"> [Widok](BIM_TDView/pl.md): Tworzy widok wybranego obiektu/obiektów, takich jak [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) lub Grupa zawierająca różne elementy widoku 2D.

-   <img alt="" src=images/BIM_Shape2DView.svg  style="width:32px;"> [Widok oparty o kształt](BIM_Shape2DView/pl.md): Tworzy widok rzutowany 2D z wybranego obiektu, takiego jak [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) lub [Poziom](Arch_BuildingPart/pl.md).



### Przyciąganie

To menu zawiera narzędzia [Przyciągania](Draft_Snap/pl.md) środowiska Rysunek Roboczy, a także następujące narzędzia:

-   <img alt="" src=images/BIM_SetWPTop.svg  style="width:32px;"> [Płaszczyzna robocza z góry](BIM_SetWPTop/pl.md): Ustawia płaszczyznę roboczą na globalnej płaszczyźnie XY (podłoże).

-   <img alt="" src=images/BIM_SetWPFront.svg  style="width:32px;"> [Płaszczyzna robocza z przodu](BIM_SetWPFront/pl.md): Ustawia płaszczyznę roboczą na globalnej płaszczyźnie XZ (przód).

-   <img alt="" src=images/BIM_SetWPSide.svg  style="width:32px;"> [Płaszczyzna robocza z boku](BIM_SetWPSide/pl.md): Ustawia płaszczyznę roboczą na globalnej płaszczyźnie YZ (bok).



### Modyfikacja

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Przesuń](Draft_Move/pl.md): przesuwa lub kopiuje wybrane obiekty z jednego punktu do drugiego.

-   <img alt="" src=images/BIM_Copy.svg  style="width:32px;"> [Kopiuj](BIM_Copy/pl.md): Kopiuje wybrane obiekty z jednego punktu do drugiego.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Obróć](Draft_Rotate/pl.md): obraca lub kopiuje wybrane obiekty wokół punktu środka o zadany kąt.

-   <img alt="" src=images/BIM_Clone.svg  style="width:32px;"> [Klon](BIM_Clone/pl.md): Klonuje wybrane obiekty.

-   <img alt="" src=images/BIM_SimpleCopy.svg  style="width:32px;"> [Utwórz prostą kopię](BIM_SimpleCopy/pl.md): Tworzy nieparametryczną kopię wybranego obiektu. Jest to to samo narzędzie co [Utwórz prostą kopię](Part_SimpleCopy/pl.md) środowiska Część.

-   <img alt="" src=images/BIM_Compound.svg  style="width:32px;"> [Utwórz kształt złożony](BIM_Compound/pl.md): Tworzy obiekt złożony z wybranych obiektów. Jest to to samo narzędzie co [Utwórz kształt złożony](Part_Compound/pl.md) środowiska Część.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Odsunięcie](Draft_Offset/pl.md): Odsuwa każdy segment wybranego obiektu na określoną odległość lub tworzy odsuniętą kopię wybranego obiektu.

-   <img alt="" src=images/BIM_Offset2D.svg  style="width:32px;"> [Odsunięcie 2D \...](BIM_Offset2D/pl.md): Konstruuje równoległą linię w danej odległości od oryginału lub powiększa/zwęża płaską powierzchnię (wersja parametryczna). Jest to to samo narzędzie co [Odsunięcie 2D \...](Part_Offset2D/pl.md) środowiska Część.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Przytnij](Draft_Trimex/pl.md): Przycina lub wydłuża wybrany obiekt.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Połącz](Draft_Join/pl.md): Łączy [linie](Draft_Line/pl.md) oraz [polilinie](Draft_Wire/pl.md) w pojedynczą polilinię.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Rozdziel](Draft_Split/pl.md): Dzieli [Linie](Draft_Line/pl.md) lub [polilinie](Draft_Wire/pl.md) w określonym punkcie lub krawędzi.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skaluj](Draft_Scale/pl.md): Skaluje lub kopiuje wybrane obiekty wokół punktu bazowego.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Rozciągnij](Draft_Stretch/pl.md): Rozciąga obiekty poprzez przesuwanie wybranych punktów.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md): Konwertuje obiekty rysunku roboczego na [szkic](Sketcher_NewSketch/pl.md) i odwrotnie.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Ulepsz kształt](Draft_Upgrade/pl.md): Powoduje zwiększenie stopnia zaawansowania wybranych obiektów.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rozbij obiekt na elementy](Draft_Downgrade/pl.md): Powoduje redukcję stopnia zaawansowania wybranych obiektów.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Dodaj komponent](Arch_Add/pl.md): Dodaje obiekty do komponentu.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Usuń komponent](Arch_Remove/pl.md): Odejmuje lub usuwa obiekty z komponentu.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Szyk](Draft_OrthoArray/pl.md): Tworzy szyk ortogonalny z wybranego obiektu. Opcjonalnie może utworzyć również szyk [powiązań](App_Link/pl.md).

-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Szyk po ścieżce](Draft_PathArray/pl.md): Tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż ścieżki.

-   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Szyk kołowy](Draft_CircularArray/pl.md): Tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż obwodu okręgu. Opcjonalnie może utworzyć szyk [powiązań](App_Link/pl.md).

-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Szyk z punktów](Draft_PointArray/pl.md): Tworzy szyk z wybranego obiektu poprzez umieszczenie kopii w punktach ze zbioru punktów.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Przetnij płaszczyzną](Arch_CutPlane/pl.md): Przycina obiekt według płaszczyzny.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Odbicie lustrzane](Draft_Mirror/pl.md): Tworzy kopie w odbiciu lustrzanym z wybranych obiektów.

-   <img alt="" src=images/BIM_Extrude.svg  style="width:32px;"> [Wyciągnięcie \...](BIM_Extrude/pl.md): Wyciąga płaskie powierzchnie obiektu. Jest to to samo narzędzie co [Wyciągnięcie](Part_Extrude/pl.md) środowiska Część.

-   <img alt="" src=images/BIM_Cut.svg  style="width:32px;"> [Różnica](BIM_Cut/pl.md): Odejmuje jeden obiekt od drugiego. Jest to to samo narzędzie co [Wytnij](Part_Cut/pl.md) środowiska Część.

<img alt="BIM_Fuse.svg" src=images/BIM_Fuse.svg  style="width:32px;"> [Połączenie](BIM_Fuse/pl.md): Łączy dwa obiekty. Jest to to samo narzędzie co [połącz](Part_Fuse/pl.md) środowiska Część.

-   <img alt="" src=images/BIM_Common.svg  style="width:32px;"> [Przecięcie](BIM_Common/pl.md): Wyodrębnia część wspólną dwóch obiektów. Jest to to samo narzędzie co [Przecięcie](Part_Common/pl.md) środowiska Część.



### Zarządzanie

-   <img alt="" src=images/BIM_Setup.svg  style="width:32px;"> [Ustawienia BIM \...](BIM_Setup/pl.md): Konfiguruje niektóre z preferencji FreeCAD najczęściej używanych w środowisku pracy BIM.

-   <img alt="" src=images/BIM_Views.svg  style="width:32px;"> [Menadżer widoków](BIM_Views/pl.md): Zarządzanie różnymi widokami i poziomami projektu.

-   <img alt="" src=images/BIM_ProjectManager.svg  style="width:32px;"> [Zarządzaj projektem \...](BIM_ProjectManager/pl.md): Umożliwia tworzenie podstawowych obiektów, takich jak [teren](Arch_Site/pl.md), [budynek](Arch_Building/pl.md) i [osie](Arch_Axis/pl.md) poprzez wypełnienie podstawowych informacji o projekcie.

-   <img alt="" src=images/BIM_Windows.svg  style="width:32px;"> [Zarządzaj drzwiami i oknami \...](BIM_Windows/pl.md): Zarządzanie drzwiami i oknami w projekcie.

-   <img alt="" src=images/BIM_IfcElements.svg  style="width:32px;"> [Zarządzaj elementami IFC \...](BIM_IfcElements/pl.md): Zarządzaj sposobem eksportowania różnych elementów projektu do IFC.

-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Edytuj ilości IFC \...](BIM_IfcQuantities/pl.md): Zarządzanie sposobem eksportowania ilości obiektów do standardu IFC.

-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Edytuj właściwości IFC \...](BIM_IfcProperties/pl.md): Zarządzaj właściwościami IFC dołączonymi do każdego z obiektów.

-   <img alt="" src=images/BIM_Classification.svg  style="width:32px;"> [Zarządzaj klasyfikacją \...](BIM_Classification/pl.md): Zarządzaj sposobem, w jaki obiekty i materiały projektu odnoszą się do systemów klasyfikacji, takich jak [Uniclass](https://en.wikipedia.org/wiki/Uniclass).

-   <img alt="" src=images/BIM_Layers.svg  style="width:32px;"> [Zarządzaj warstwami \...](BIM_Layers/pl.md): Zarządzanie warstwami dokumentu.

-   <img alt="" src=images/BIM_Material.svg  style="width:32px;"> [Materiał](BIM_Material/pl.md): Zarządza [materiałami](Arch_SetMaterial/pl.md) lub [materiałami wielowarstwowymi](Arch_MultiMaterial/pl.md) wybranych obiektów.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Obmiar](Arch_Schedule/pl.md): Tworzenie różnych typów obmiaru.

-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Kontrola wstępna \...](BIM_Preflight/pl.md): Przed wyeksportowaniem do IFC należy przeprowadzić różne operacje sprawdzające model.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md): pozwala zdefiniować style, które wpływają na właściwości wizualne obiektów związanych z adnotacjami.



### Narzędzia

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Przełącz dolne panele](BIM_TogglePanels/pl.md): Pokazuje lub ukrywa okna wyników (widok raportu i konsola Pythona).

-   <img alt="" src=images/BIM_Trash.svg  style="width:32px;"> [Przenieś do kosza](BIM_Trash/pl.md): Przenosi wybrane obiekty do grupy kosz, która jest tworzona w razie potrzeby

-   <img alt="" src=images/BIM_WPView.svg  style="width:32px;"> [Widok płaszczyzny roboczej](BIM_WPView/pl.md): Ustawia kamerę na wprost bieżącej płaszczyzny roboczej

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Wybierz grupę](Draft_SelectGroup/pl.md): Wybiera zawartość [warstwy](Draft_Layer/pl.md), [Grupy](Std_Group/pl.md) lub obiektów zbliżone do grupy [Architektury](Arch_Workbench/pl.md).

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Nachylenie](Draft_Slope/pl.md): Powoduje nachylenie wybranych [linii](Draft_Line/pl.md) lub [polilinii](Draft_Wire/pl.md) poprzez zwiększenie lub zmniejszenie współrzędnej Z, dla wszystkich punktów po pierwszym.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md): Tworzy zastępczą płaszczyznę roboczą, aby zapisać bieżącą [płaszczyznę robocza projektu](Draft_SelectPlane/pl.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Dodaj do grupy konstrukcyjnej](Draft_AddConstruction/pl.md): Przenosi obiekty do [trybu konstrukcji](Draft_ToggleConstructionMode/pl.md).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Podziel siatkę](Arch_SplitMesh/pl.md): Dzieli wybraną siatkę na osobne elementy.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Siatka na kształt](Arch_MeshToShape/pl.md): Przekształca siatkę w kształt, ujednolicając współpłaszczyznowe powierzchnie.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Zaznacz siatki niebryłowe](Arch_SelectNonSolidMeshes/pl.md): Wybiera wszystkie siatki typu non-manifold z bieżącego zaznaczenia lub z dokumentu.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Usuń kształt](Arch_RemoveShape/pl.md): Zmienia obiekt architektury oparty na kształcie sześciennym w całkowicie parametryczny.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Zamknij otwory](Arch_CloseHoles/pl.md): Zamyka otwory w wybranym obiekcie opartym na kształcie.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Połącz ściany](Arch_MergeWalls/pl.md): Łączy ściany.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Sprawdź](Arch_Check/pl.md): Sprawdza, czy wybrane obiekty są bryłami i nie zawierają defektów.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Przełącz flagę Brep IFC](Arch_ToggleIfcBrepFlag/pl.md): Wymusza wyeksportowanie wybranego obiektu jako obiektu [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Przełącz widoczność elementów podrzędnych](Arch_ToggleSubs/pl.md): Pokazuje lub ukrywa elementy podrzędne obiektu architektury.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Spis wymiarów](Arch_Survey/pl.md): Włącza lub wyłącza tryb pomiaru.

-   <img alt="" src=images/BIM_Diff.svg  style="width:32px;"> [Różnice IFC](BIM_Diff/pl.md): Pokazuje wizualne różnice między dwoma plikami IFC

-   <img alt="" src=images/BIM_IfcExplorer.svg  style="width:32px;"> [Przeglądarka IFC](BIM_IfcExplorer/pl.md): Otwiera okno do eksploracji struktury pliku IFC przed importem

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Utwórz arkusz IFC\...](Arch_IfcSpreadsheet/pl.md): To narzędzie tworzy arkusz do przechowywania właściwości IFC obiektu.

-   <img alt="" src=images/BIM_ImagePlane.svg  style="width:32px;"> [Płaszczyzna rysunku](BIM_ImagePlane/pl.md): Wstawia płaszczyznę rysunku do dokumentu.

-   <img alt="" src=images/BIM_Unclone.svg  style="width:32px;"> [Przekształć z klona](BIM_Unclone/pl.md): Tworzy klon niezależny od oryginalnego obiektu

-   <img alt="" src=images/BIM_Rewire.svg  style="width:32px;"> [Odtwórz polilinię](BIM_Rewire/pl.md):

-   <img alt="" src=images/BIM_Glue.svg  style="width:32px;"> [Sklej](BIM_Glue/pl.md):

-   <img alt="" src=images/BIM_Reextrude.svg  style="width:32px;"> [Wyciągnij ponownie](BIM_Reextrude/pl.md): Odtwarza wyciągnięcie z kształtu, który stracił swoje parametryczne wyciągnięcie poprzez wskazanie ściany bazowej

-   Narzędzia panelu:

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel/pl.md): Tworzy obiekt panelu z wybranego obiektu 2D.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panelizacja do cięcia](Arch_Panel_Cut/pl.md): Tworzy widok wycięcia 2D z panelu.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Arkusz panela](Arch_Panel_Sheet/pl.md): Tworzy arkusz cięcia 2D zawierający wycięcia paneli lub innych obiektów 2D.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Zagnieżdżanie](Arch_Nest/pl.md): Umożliwia zagnieżdżenie kilku płaskich obiektów wewnątrz kształtu kontenera.

-   Narzędzia konstrukcyjne:

  - <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Konstrukcja](Arch_Structure/pl.md): Tworzy element konstrukcyjny od podstaw lub używając wybranego obiektu jako podstawy.

  - <img alt="" src=images/Arch_StructuralSystem.svg  style="width:32px;"> [Układ konstrukcyjny](Arch_StructuralSystem/pl.md):

  - <img alt="" src=images/Arch_StructuresFromSelection.svg  style="width:32px;"> [Wiele konstrukcji](Arch_StructuresFromSelection/pl.md):

-   <img alt="" src=images/IFC_Diff.svg  style="width:32px;"> [Różnice IFC \...](IFC_Diff/pl.md):

-   <img alt="" src=images/IFC_Expand.svg  style="width:32px;"> [Rozwiń IFC](IFC_Expand/pl.md):

-   <img alt="" src=images/IFC_MakeProject.svg  style="width:32px;"> [Utwórz projekt IFC](IFC_MakeProject/pl.md):

-   <img alt="" src=images/IFC_UpdateIOS.svg  style="width:32px;"> [Aktualizacja IfcOpenShell](IFC_UpdateIOS/pl.md):

-   Małe przemieszczenie:

  - [Przełącz krok](BIM_Nudge_Switch/pl.md):

  - [Przesuń w górę](BIM_Nudge_Up/pl.md):

  - [Przesuń w dół](BIM_Nudge_Down/pl.md):

  - [Przesuń w lewo](BIM_Nudge_Left/pl.md):

  - [Przesuń w prawo](BIM_Nudge_Right/pl.md):

  - [Przesuń obracając w lewo](BIM_Nudge_RotateLeft/pl.md):

  - [Przesuń obracając w prawo](BIM_Nudge_RotateRight/pl.md):

  - [Zwiększ krok](BIM_Nudge_Extend/pl.md):

  - [Zmniejsz krok](BIM_Nudge_Shrink/pl.md):



### Pasek stanu 

Pasek statusu zawiera kilka przycisków, które pozwalają na łatwą zmianę różnych stanów:

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Przełącz panele](BIM_TogglePanels/pl.md): Pokazuje lub ukrywa [widok raportu](Report_view.md) i [konsolę Pythona](Python_console.md).

-   <img alt="" src=images/BIM_ToggleViews.svg  style="width:32px;"> Przełącz widoki: Pokazuje lub ukrywa panel [widoków BIM](BIM_Views/pl.md).

-   <img alt="" src=images/BIM_ToggleBackground.svg  style="width:32px;"> Cykliczne tło: Przełącza cyklicznie między gradientem pionowym i promieniowym oraz pojedynczym kolorem tła. Można z tego skorzystać do przełączania między ciemnym tłem do modelowania i białym tłem do rysunków 2D.

-   <img alt="" src=images/IFC.svg  style="width:32px;"> Blokada IFC: Przełącza między [trybem zablokowanym i odblokowanym IFC](NativeIFC/pl#Tryby_zablokowane_i_odblokowane.md).



## Menu kontekstowe Widoku drzewa 

Do opracowania.



## Menu kontekstowe okna widoku 3D 

Do opracowania.



### Narzędzia przestarzałe 

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Trzy widoki z siatki](Arch_3Views/pl.md): Tworzy widoki z góry, przodu i boku z [siatki](Mesh_Workbench/pl.md). Niedostępne w {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Część budynku - piętro](Arch_BuildingPart/pl.md): Tworzy część budynku włączając wybrane obiekty. Niedostępne w {{VersionPlus/pl|1.0}}. Użyj narzędzia [Kondygnacja](Arch_Floor/pl.md) zamiast tego.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Klonuj komponent](Arch_CloneComponent/pl.md): Tworzy komponenty Arch, które są klonami wybranych obiektów Arch. Niedostępne w {{VersionPlus/pl|1.0}}. Użyj narzędzia [Rysunek Roboczy: Klonuj](Draft_Clone/pl.md) zamiast tego.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Linie cięcia](Arch_CutLine/pl.md): Wycina obiekt zgodnie z linią. Niedostępne w {{VersionPlus/pl|1.0}}. Zamiast tego należy użyć [Płaszczyzna cięcia](Arch_CutPlane/pl.md).

-   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Materiał wielowarstwowy](Arch_MultiMaterial/pl.md): Tworzy materiał wielowarstwowy i przypisuje go do wybranych obiektów, jeśli jakiekolwiek są. Niedostępne w {{VersionPlus/pl|1.0}}. Użyj [Materiału BIM](BIM_Material/pl.md) zamiast tego.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Arch Projekt](Arch_Project/pl.md): Tworzy projekt zawierający wybrane obiekty. Niedostępne w {{VersionPlus/pl|1.0}}. Zamiast tego należy użyć [Projekt BIM](BIM_Project/pl.md).

-   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Ustaw materiał](Arch_SetMaterial/pl.md): Tworzy materiał i przypisuje go do wybranych obiektów, jeśli jakiekolwiek są. Niedostępne w {{VersionPlus/pl|1.0}}. Użyj narzędzia [Materiał BIM](BIM_Material/pl.md) zamiast tego.



## Ustawienia

-   <img alt="" src=images/Preferences-bim.svg  style="width:32px;"> [Ustawienia](BIM_Preferences/pl.md): Ogólne preferencje dla środowiska pracy BIM.
-   [Dostrajanie](Fine-tuning/pl#środowisko_pracy_BIM.md): Dodatkowe parametry do dostrajania zachowania BIM.



## Praca z IFC 

Środowisko pracy BIM działa natywnie z plikami [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC). Natywność oznacza, że nie ma więcej konwersji między zawartościami IFC a programem FreeCAD: zawartości IFC są bezpośrednio renderowane we FreeCAD i każda zmiana wpływa na nie bezpośrednio. Przeczytaj więcej na stronie [Natywne IFC](NativeIFC/pl.md).

Jeśli nie planujesz współpracować z innymi użytkownikami i nie masz potrzeby używania IFC, nadal możesz korzystać z narzędzi środowiska pracy BIM i po prostu ignorować wszystko związane z IFC. Nadal możesz wyeksportować swój model do IFC w dowolnej chwili.

Stary importer [Arch IFC](Arch_IFC/pl.md) jest domyślnie wyłączony we FreeCAD, ale nadal dostępny z poziomu Pythona.



## Formaty plików 

-   [IFC](Arch_IFC/pl.md) : Industry foundation Classes.
-   [DAE](Arch_DAE/pl.md) : format Collada dla siatek.
-   [OBJ](Arch_OBJ/pl.md) : format OBJ dla siatek *(tylko eksport)*.
-   [JSON](Arch_JSON/pl.md) : format zapisu obiektu w JavaScript *(tylko eksport)*.
-   [3DS](Arch_3DS/pl.md) : format 3DS *(tylko import)*.
-   [SHP](Arch_SHP/pl.md): GIS Shapefiles *(tylko import)*.



## API

Moduł Arch może być używany w skryptach [Python](Python.md) i [makrodefiniacjach](Macros/pl.md) za pomocą funkcji [Arch Python API](Arch_API/pl.md).



## Poradniki i nauka 

-   [Migracja do FreeCAD z Revit](Migrating_to_FreeCAD_from_Revit/pl.md)
-   [Poradniki Wiki - Arch & BIM](Tutorials/pl#Architektura_i_BIM/pl.md)
-   [\"BIM with FreeCAD\" seria wideo przygotowana przez Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" seria wideo przygotowana przez Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" seria wideo przygotowana przez by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)
-   [Kanał YouTube \"HRCompacta\" (w większości po portugalsku)](https://www.youtube.com/@HRCompacta)
-   [Kanał YouTube \"FreeCADBIM\" (w większości po portugalsku)](https://www.youtube.com/@FreeCadBIM)



## Przykładowe pliki 

-   FreeCAD zawiera przykładowy plik BIM na stronie Start.
-   Więcej przykładowych plików BIM można znaleźć na stronie <https://github.com/yorikvanhavre/FreeCAD-BIM-examples>. Z poziomu programu FreeCAD, użyj menu Pomoc -\> Przykłady BIM.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [BIM](Category_BIM.md) > BIM Workbench/pl
