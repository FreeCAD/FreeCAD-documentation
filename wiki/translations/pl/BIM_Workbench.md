
{{UnfinishedDocu

}} 

<img alt="Ikonka FreeCAD dla zewnętrznego Środowiska pracy BIM" src=images/IFC.svg  style="width:128px;">


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/pl.md) jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md) mającym na celu implementację kompletnych [informacji o modelowaniu budynku](https://en.wikipedia.org/wiki/Building_information_modeling) *(BIM)* narzędzi i przepływu pracy w programie FreeCAD. Można go zainstalować z poziomu <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).

Środowisko pracy BIM jest oparte na wbudowanym środowisku <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> \|[Architektura](Arch_Workbench/pl.md), a oba będą prawdopodobnie połączone w przyszłości. Środowisko pracy BIM jest \"meta środowiskiem\", którego celem jest zebranie wielu przydatnych narzędzi z innych środowisk w jednym miejscu i stworzenie przepływu pracy, który jest bardziej wygodny i przyjazny zarówno dla doświadczonych użytkowników BIM jak i początkujących. BIM posiada również specyficzne narzędzia, głównie kreatory i narzędzia do zarządzania, znajdujące się w menu **Zarządzanie**.

Zobacz [Przewodnik migracji FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) aby uzyskać szybki przegląd, jeśli jesteś już użytkownikiem innej aplikacji BIM.

Twórcy środowisk Rysunek Roboczy, Architektura i BIM współpracują również z większą [społecznością OSArch](https://osarch.org), mając na uwadze ostateczny cel, jakim jest poprawa projektowania budynków przy użyciu całkowicie wolnego oprogramowania.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">

## Instalacja

Środowisko pracy BIM nie jest dołączone do domyślnego pakietu FreeCAD, ale może być łatwo zainstalowane poprzez <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md). Wywołaj go z menu **Przybory → [Menadżer dodatków](Std_AddonMgr/pl.md)**. Kod środowiska pracy BIM jest [hostowany i rozwijany na Github](https://github.com/yorikvanhavre/BIM_Workbench) i może być również zainstalowany ręcznie poprzez skopiowanie go do katalogu {{FileName|MOD}} programu FreeCAD.

**Uwaga**

Środowisko pracy BIM jest w trakcie opracowywania i będzie się często zmieniać. Upewnij się, że aktualizujesz go regularnie! Jeśli masz zainstalowany moduł [Python-Git](https://github.com/chidimo/python-git), środowisko pracy BIM automatycznie wyszuka dostępne aktualizacje przy starcie i wyświetli ikonę na pasku stanu, jeśli aktualizacja jest dostępna.

Narzędzia wymienione poniżej mogą również nie być wszystkie obecne, jeśli Twoja wersja FreeCAD nie jest w pełni aktualna. Środowisko pracy BIM powinno jednak działać bezproblemowo na wszystkich wersjach FreeCAD, będzie tylko pomijać narzędzia, które nie są dostępne.

## Rozpoczęcie pracy 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Przy pierwszym uruchomieniu środowiska pracy BIM wyświetlany jest dialog powitalny, który umożliwia szybki przegląd działania środowiska pracy i pozwala użytkownikowi na rozpoczęcie [Poradnika: Obsługa BIM](BIM_ingame_tutorial/pl.md). Okno powitalne jest również dostępne z menu **pomoc**. Gdy ekran powitalny zostanie zamknięty przez kliknięcie OK, pojawi się okno dialogowe [Konfiguracja środowiska BIM](BIM_Setup/pl.md), które pozwala użytkownikowi na szybkie ustawienie niektórych z najczęściej używanych preferencji programu FreeCAD, związanych z BIM bez potrzeby przeglądania pełnych stron preferencji FreeCAD.

Narzędzie [BIM: Projekt](BIM_Project/pl.md) pozwala na szybką konfigurację projektu BIM poprzez wypełnienie kilku podstawowych informacji o projekcie. Następnie można, na przykład, użyć różnych narzędzi kreślarskich 2D do szkicowania wytycznych i linii bazowych, a następnie użyć różnych narzędzi do modelowania 3D, aby automatycznie zbudować z nich obiekty 3D BIM. Na przykład linia może stać się ścianą, wystarczy ją wybrać i nacisnąć przycisk [Ściana](Arch_Wall/pl.md).

Jeśli jesteś przyzwyczajony do innej aplikacji BIM, sprawdź naszą [tabela zgodności zastosowań BIM](BIM_application_compatibility_table/pl.md), aby uzyskać swoje oceny podczas rozpoczynania pracy z FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Samouczek [Obsługa BIM](BIM_ingame_tutorial/pl.md) jest łatwym sposobem na szybkie rozpoczęcie pracy ze środowiskiem BIM.

## Przybory

Środowisko pracy BIM gromadzi narzędzia z kilku innych środowisk programu FreeCAD, głównie [Rysunek Roboczy](Draft_Part_Workbench/pl.md), [Architektura](Arch_Part_Workbench/pl.md) i [Część](Part_Part_Workbench/pl.md), z grubsza zreorganizowane w logiczne kategorie: **rysowanie 2D**, **modelowanie 3D**, **adnotacje** i *\'modyfikacje*. Kategoria **zarządzanie** zawiera narzędzia, które są specyficzne dla środowiska BIM.

Dodatkowo, jeżeli są zainstalowane [dodatki](External_workbenches/pl.md), narzędzia ze środowiska [Zbrojenie](Arch_Rebar/pl.md) *(dodatkowe narzędzia do prętów zbrojeniowych)*, [Elementy złączne](Fasteners_Workbench/pl.md) *(śruby i wkręty)*, [Flamingo / Dodo](Flamingo_Workbench/pl.md) *(narzędzia do konstrukcji stalowych i rurociągów)* oraz [Biblioteka podzespołów](Parts_Library_Workbench/pl.md) są automatycznie dołączane do środowiska BIM.

Środowisko pracy BIM dodaje również serię pozycji w *pasku statusu* programu FreeCAD, oraz kilka pozycji *menu kontekstowego*, dostępnych po kliknięciu prawym przyciskiem myszy w widoku 3D lub w widoku drzewa.

### Rysunki 2D 

Obiekty 2D są powszechnie używane jako pomoce kreślarskie, lub do rysowania linii bazowych i profili, na których można budować obiekty BIM. Mogą być również używane do kreślenia symboli i adnotacji w modelu. Oprócz szkiców, które używają swojego własnego układu współrzędnych, obiekty 2D będą rysowane na bieżącej [płaszczyżnie roboczej](Draft_SelectPlane/pl.md).

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Utwórz nowy szkic](Sketcher_NewSketch/pl.md): Tworzy nowy szkic i przechodzi do trybu rysowania. Szkice są zaawansowanymi obiektami 2D z obsługą wiązań.
-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linia](Draft_Line/pl.md): Rysuje odcinek pomiędzy dwoma punktami.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Linia łamana](Draft_Wire/pl.md): Rysuje linię łamaną złożoną z wielu segmentów prostych *(polilinia)*.
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Okrąg](Draft_Circle/pl.md): Rysuje okrąg na podstawie środka i promienia.
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Łuk](Draft_Arc/pl.md): Rysuje odcinek łuku na podstawie środka, promienia, kąta początkowego i końcowego.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Łuk przez trzy punkty](Draft_Arc_3Points/pl.md): rysuje odcinek łuku kołowego na podstawie trzech punktów, znajdujących się na obwodzie.
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Elipsa](Draft_Ellipse/pl.md): Rysuje elipsę na podstawie dwóch punktów narożnych.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Wielokąt foremny](Draft_Polygon/pl.md): Rysuje wielokąt foremny na podstawie środka i promienia.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Prostokąt](Draft_Rectangle/pl.md): Rysuje prostokąt o podstawie dwóch przeciwległych punktów.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [Krzywa złożona](Draft_BSpline/pl.md): Rysuje krzywą złożoną z serii punktów.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Sześcienna krzywa Beziera](Draft_CubicBezCurve/pl.md): rysuje krzywą Beziera trzeciego stopnia poprzez przeciągnięcie dwóch punktów.
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Krzywa Beziera](Draft_BezCurve/pl.md): Rysuje krzywą Beziera z serii punktów.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/pl.md): Wstawia obiekt punktu.

### Adnotacje

Adnotacje są wizualnymi obiektami pomocniczymi, które mogą być umieszczone wewnątrz Twojego modelu. Mogą one być użyte do eksportu modelu bezpośrednio do formatu 2D jak [DXF](Draft_DXF/pl.md), lub ponownie użyte podczas tworzenia widoków 2D Twojego modelu za pomocą środowiska [Rysunek Techniczny](TechDraw_Workbench/pl.md).

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Tekst](Draft_Text/pl.md): Rysuje wielowierszową adnotację tekstową.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Kształt z tekstu](Draft_ShapeString/pl.md): Rysuje linię tekstu jako geometrię.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Wymiarowanie](Draft_Dimension/pl.md): Rysuje wymiar liniowy, kątowy, promieniowy lub średnicy.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etykieta](Draft_Label/pl.md): Umieszcza etykietę ze strzałką wskazującą na wybrany element.
-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Osie](Arch_Axis/pl.md): Tworzy pojedynczą oś lub jednokierunkowy szereg osi dla dokumentu.
-   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Układ osi](Arch_AxisSystem/pl.md): Tworzy układ osi składający się z maksymalnie trzech serii osi.
-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Siatka](Arch_Grid/pl.md): Tworzy obiekt typu kratka w dokumencie.
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Płaszczyzna przekroju](Arch_SectionPlane/pl.md): Dodaje obiekt płaszczyzny przekroju w dokumencie. Płaszczyzny przekroju definiują widoki 2D, takie jak plany, przekroje i elewacje.
-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Strona](TechDraw_PageDefault/pl.md): Tworzy nową stronę [Rysunku Technicznego](TechDraw_Workbench/pl.md) z [szablonu SVG](TechDraw_Templates/pl.md).
-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Widok](TechDraw_ArchView/pl.md): Wstawia widok płaszczyzny przekroju na stronie.

### Modelowanie 3D / BIM 

Obiekty 3D i BIM są elementami świata rzeczywistego, które składają się na Twój projekt BIM.

**Konstrukcja budowli**: Te narzędzia pomogą Ci zorganizować Twój model

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/pl.md): Tworzy projekt zawierający wybrane obiekty.
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Teren](Arch_Site/pl.md): Tworzy teren z wybranymi obiektami.
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Budowla](Arch_Building/pl.md): Tworzy budynek wraz z wybranymi obiektami.
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Piętro](Arch_BuildingPart/pl.md) *(Część budowli)*: Tworzy część budynku zawierającą wybrane obiekty. Części budynku są często używane do reprezentowania pięter.
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Kubatura](Arch_Space/pl.md): Tworzy obiekt przestrzeni w dokumencie.
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Odnośnik](Arch_Reference/pl.md): Łączy obiekty z innego pliku projektu FreeCAD do tego dokumentu.

**Narzędzia BIM**: Narzędzia te budują komponenty BIM.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Ściana](Arch_Wall/pl.md): Tworzy ścianę od podstaw lub używając wybranego obiektu jako podstawy.
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Ściana osłonowa](Arch_CurtainWall/pl.md): tworzy ścianę osłonową od podstaw lub wykorzystując wybrany obiekt jako podstawę.
-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Kolumna](Arch_Structure/pl.md): Tworzy pionowy element [konstrukcji](Arch_Structure/pl.md) w podanym punkcie, opcjonalnie używając wybranego obiektu jako profilu.
-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Belka](Arch_Structure/pl.md): Tworzy poziomy element [konstrukcji](Arch_Structure/pl.md) w podanym punkcie, opcjonalnie używając wybranego obiektu jako profilu.
-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Płyta](Arch_Structure/pl.md): Tworzy płaski element [konstrukcji](Arch_Structure/pl.md) poprzez wyciąganie wybranego płaskiego obiektu.
-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): Tworzy pręt zbrojeniowy w wybranym elemencie konstrukcyjnym za pomocą szkicu. Wymaga dodatku [Zbrojenie](Reinforcement_Addon/pl.md).
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Okno](Arch_Window/pl.md): Tworzy okno używając wybranego obiektu jako podstawy.
-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Drzwi](Arch_Window/pl.md): Tworzy obiekt [okna](Arch_Window/pl.md) z wykorzystaniem ustawień wstępnych drzwi.
-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Rury](Arch_Pipe/pl.md): Tworzy rury i połączenia narożne lub trójniki pomiędzy dwoma lub trzema wybranymi rurami.
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Schody](Arch_Stairs/pl.md): Tworzy obiekt schodów w dokumencie.
-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/pl.md): Tworzy spadzisty dach z wybranej powierzchni.
-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel](Arch_Panel/pl.md): Tworzy obiekty paneli oraz wycięcia 2D z tych paneli.
-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Rama](Arch_Frame/pl.md): Tworzy obiekt szkieletowy z wybranego układu.
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Ogrodzenie](Arch_Fence/pl.md): Tworzy obiekt ogrodzenia z wybranego obiektu słupka i trasy.
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Kratownica](Arch_Truss/pl.md): Tworzy kratownicę z wybranej linii od podstaw.
-   <img alt="" src=images/BIM_Library.png  style="width:32px;"> [Biblioteka BIM](BIM_Library/pl.md): Wstawia obiekt wyposażenia lub mebli. Wymaga dodatku [biblioteka podzespołów](Parts_Library_Workbench/pl.md).
-   <img alt="" src=images/Arch_Component.png  style="width:32px;"> [Komponent BIM](Arch_Component/pl.md): Przekształca dowolny wybrany obiekt w obiekt BIM, z pełną obsługą IFC.

**Ogólne narzędzia 3D**: Narzędzia te budują uniwersalne obiekty 3D, które mogą być przekształcone lub wykorzystane w komponentach BIM.

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/pl.md): Tworzy parametryczny profil 2D do wykorzystania np. w procesie wyciągania.
-   <img alt="" src=images/BIM_Box.png  style="width:32px;"> [Prostopadłościan](BIM_Box/pl.md): Rysuje sześcian poprzez graficzne określenie jego wymiarów
-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Konstruktor kształtu](Part_Builder/pl.md): Narzędzie do tworzenia bardziej złożonych kształtów z różnych parametrycznych brył pierwotnych.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Łącznik ścian](Draft_Facebinder/pl.md): Tworzy nowy obiekt z wybranych ścian na istniejących obiektach.

### Narzędzia do modyfikacji 

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Przesuń](Draft_Move/pl.md): Przenosi obiekty z jednej lokalizacji do drugiej.
-   <img alt="" src=images/BIM_Copy.png  style="width:32px;"> [Kopiuj](BIM_Copy/pl.md): Kopiuje obiekty z jednej lokalizacji do drugiej.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Obróć](Draft_Rotate/pl.md): Obraca obiekty pod kątem od wartości początkowej do wartości końcowej.
-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klonuj](BIM_Clone/pl.md): Klonuje wybrane obiekty.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Odsunięcie](Draft_Offset/pl.md): Przesuwa segmenty obiektu o określoną odległość
-   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Odsunięcie 2D](Part_Offset2D/pl.md): Konstruuje równoległą linię w pewnej odległości od oryginału lub powiększa/zmniejsza płaską ścianę *(wersja parametryczna)*.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Przytnij / wydłuż](Draft_Trimex/pl.md): Przycina lub wydłuża obiekt.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skaluj](Draft_Scale/pl.md): Skaluje wybrane obiekty na podstawie punktu bazowego.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Rozciągnij](Draft_Stretch/pl.md): Rozciąga wybrane obiekty.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Szyk](Draft_Array/pl.md): Tworzy szyk biegunowy lub prostokątny z wybranych obiektów.
-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Szyk po ścieżce](Draft_PathArray/pl.md): Tworzy szyk obiektów poprzez umieszczenie ich kopii wzdłuż ścieżki.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Odbicie lustrzane](Draft_Mirror/pl.md): Tworzy odbicie lustrzane wybranych obiektów.
-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Wyciągnij](Part_Extrude/pl.md): Wytłacza płaskie powierzchnie obiektu.
-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Wytnij](Part_Cut/pl.md): Wycina *(odejmuje)* jeden obiekt od drugiego
-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Scalenie](Part_Fuse/pl.md): Łączy *(scala)* dwa obiekty.
-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Część wspólna](Part_Common/pl.md): Wyodrębnia część wspólną *(przecięcie)* dwóch obiektów.
-   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Utwórz złożenie](Part_Compound/pl.md): Tworzy złożenie z wybranych obiektów.
-   <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Szybka kopia](Part_SimpleCopy/pl.md): Creates a non-parametric copy of a selected object
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Ulepsz kształt](Draft_Upgrade/pl.md): Łączy obiekty w obiekt wyższego poziomu.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rozbij obiekt na elementy](Draft_Downgrade/pl.md): Rozbija obiekty na obiekty niższego poziomu.
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Widok 2D kształtu](Draft_Shape2DView/pl.md): Tworzy obiekt 2D, który jest rzutem widoku 2D obiektu przestrzennego.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md): Konwertuje obiekt Rysunku Roboczego na Szkic i odwrotnie.
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Płaszczyzna cięcia](Arch_CutPlane/pl.md): Przytnij przedmiot zgodnie z płaszczyzną.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Dodaj komponentt](Arch_Add/pl.md): Dodaje obiekty do komponentu.
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Usuń komponent](Arch_Remove/pl.md): Odejmuje lub usuwa obiekty z komponentu.

### Narzędzia do zarządzania 

-   <img alt="" src=images/BIM_Setup.png  style="width:32px;"> [Konfiguracja środowiska BIM](BIM_Setup/pl.md): Konfiguruje niektóre z preferencji FreeCAD najczęściej używane dla BIM.
-   <img alt="" src=images/BIM_Project.png  style="width:32px;"> [Projekt](BIM_Project/pl.md): Pozwala na tworzenie podstawowych obiektów takich jak [Teren](Arch_Site/pl.md), [Budowla](Arch_Building/pl.md) i [Osie](Arch_Axis/pl.md) poprzez wypełnienie podstawowych informacji o projekcie.
-   <img alt="" src=images/BIM_Views.png  style="width:32px;"> [Widoki](BIM_Views/pl.md): Zarządzaj różnymi widokami i poziomami projektu.
-   <img alt="" src=images/BIM_Windows.png  style="width:32px;"> [Okna i drzwi](BIM_Windows/pl.md): Zarządzaj drzwiami i oknami swojego projektu.
-   <img alt="" src=images/BIM_IfcElements.png  style="width:32px;"> [Menadżer elementów IFC](BIM_IfcElements/pl.md): Zarządzaj, w jaki sposób poszczególne elementy projektu będą eksportowane do IFC.
-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Menadżer właściwości IFC](BIM_IfcProperties/pl.md): Zarządzaj właściwościami IFC dołączonymi do każdego z obiektów.
-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Menadżer ilości IFC](BIM_IfcQuantities/pl.md): Zarządzaj, w jaki sposób dane o ilości obiektów są eksportowane do IFC.
-   <img alt="" src=images/BIM_Classification.png  style="width:32px;"> [Menadżer klasyfikacji](BIM_Classification/pl.md): Zarządzaj sposobem, w jaki obiekty i materiały Twojego projektu odnoszą się do systemów klasyfikacji, takich jak [Uniclass](https://en.wikipedia.org/wiki/Uniclass).
-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [Menadżer warstw](BIM_Layers/pl.md): Zarządzaj warstwami dokumentu.
-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Materiał](Arch_SetMaterial/pl.md): Zarządza materiałami lub [materiałami złozonymi](Arch_MultiMaterial/pl.md) wybranych obiektów.
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Harmonogram](Arch_Schedule/pl.md): Tworzenie różnych typów planów pracy.
-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Kontrola wstępna](BIM_Preflight/pl.md): Wykonaj różne testy modelu przed wyeksportowaniem do IFC.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md): Zarządza stylami adnotacji używanymi przez teksty i wymiary.

## Poradniki i nauka 

-   [Poradniki Wiki - Arch & BIM](Tutorials/pl#Architektura_i_BIM/pl.md)
-   [\"BIM with FreeCAD\" seria wideo przygotowana przez Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" seria wideo przygotowana przez Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" seria wideo przygotowana przez by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)

## Zewnętrzne Środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!




[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md) [Category:BIM{{\#translation:}}](Category:BIM.md)
