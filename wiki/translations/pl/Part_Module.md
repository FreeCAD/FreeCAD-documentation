# <img alt="Ikonka FreeCAD dla środowiska pracy Część" src=images/Workbench_Part.svg  style="width   *64px;"> Part Module/pl


{{TOCright}}

## Wprowadzenie

Funkcje modelowania brył w FreeCAD są oparte na jądrze *(OCCT)* [Technologia Open Cascade](OpenCASCADE/pl.md), profesjonalnym systemie CAD, który oferuje możliwość zaawansowanego tworzenia i manipulacji geometrii 3D.
Środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Część](Part_Workbench/pl.md) jest warstwą umieszczoną nad bibliotekami OCCT, która daje użytkownikowi dostęp do geometrycznych brył pierwotnych i funkcji OCCT. Zasadniczo wszystkie funkcje rysowania 2D i 3D w każdym środowisku pracy *(<img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Szkicownik](Sketcher_Workbench/pl.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Projekt Części](PartDesign_Workbench/pl.md), itd.)*, są oparte na tych funkcjach, które zostały zaprezentowane przez Środowisko pracy Part. Dlatego też środowisko pracy Część jest uważane za kluczowy komponent umiejętności modelowania programu FreeCAD.

Bardziej szczegółowa dyskusja na temat środowisk Część kontra Projekt części znajduje się tutaj   * [Część i Projekt części](Part_and_PartDesign/pl.md).

Obiekty stworzone przy użyciu środowiska pracy Część są stosunkowo proste. Są przeznaczone do używania z operacjami typu logicznego *(łączenia i cięcia)* w celu budowania bardziej złożonych kształtów. **Ten wzorzec modelowania znany jest jako [Stereometria konstrukcyjna](constructive_solid_geometry.md) *(CSG)* i była to tradycyjna metodologia stosowana we wczesnych systemach CAD**. Z drugiej strony środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) zapewnia bardziej nowoczesny cykl roboczy służący konstruowaniu kształtów   * wykorzystuje szkic zdefiniowany parametrycznie, który jest wytłaczany w celu utworzenia podstawowej bryły, która następnie jest modyfikowana przez przekształcenia parametryczne *([edycja cech](feature_editing.md))*, aż do uzyskania ostatecznego obiektu.

Obiekty części są bardziej złożone niż obiekty siatkowe utworzone przy użyciu środowiska pracy [Siatka](Mesh_Workbench/pl.md), ponieważ pozwalają one na bardziej zaawansowane operacje, takie jak spójne operacje logiczne, historia modyfikacji i właściwości parametryczne.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width   *600px;">



*Środowisko pracy Część jest podstawową warstwą, która udostępnia funkcje rysowania '''OCCT''' dla każdego środowiska pracy w programie FreeCAD.*

## Narzędzia

Wszystkie narzędzia zostały umieszczone w menu głównym środowiska pracy **Część**, lub menu **Wymiarowanie**.

### Bryły pierwotne 

Są to narzędzia do tworzenia obiektów o charakterze elementarnym.

-   <img alt="" src=images/Part_Box.svg  style="width   *32px;"> [Sześcian](Part_Box/pl.md)   * rysuje sześcian.

-   <img alt="" src=images/Part_Cylinder.svg  style="width   *32px;"> [Walec](Part_Cylinder/pl.md)   * rysuje walec.

-   <img alt="" src=images/Part_Sphere.svg  style="width   *32px;"> [Kula](Part_Sphere/pl.md)   * rysuje sferę.

-   <img alt="" src=images/Part_Cone.svg  style="width   *32px;"> [Stożek](Part_Cone/pl.md)   * rysuje stożek.

-   <img alt="" src=images/Part_Torus.svg  style="width   *32px;"> [Torus](Part_Torus/pl.md)   * rysuje torus.

-   <img alt="" src=images/Part_Tube.svg  style="width   *32px;"> [Rura](Part_Tube.md)   * rysuje rurę. {{Version/pl|0.19}}

-   <img alt="" src=images/Part_Primitives.svg  style="width   *32px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md)   * Narzędzie do tworzenia jednego z następujących elementów pierwotnych   *
    -   <img alt="" src=images/Part_Plane.svg  style="width   *32px;"> [Płaszczyzna](Part_Plane/pl.md)   * tworzy płaszczyznę.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width   *32px;"> [Sześcian](Part_Box/pl.md)   * tworzy sześcian. Obiekt ten można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Box.svg  style="width   *32px;"> [Box](Part_Box/pl.md).
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width   *32px;"> [Walec](Part_Cylinder/pl.md)   * tworzy walec. Obiekt ten można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Cylinder.svg  style="width   *32px;"> [Walec](Part_Cylinder/pl.md).
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width   *32px;"> [Stożek](Part_Cone/pl.md)   * tworzy stożek. Obiekt ten można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Cone.svg  style="width   *32px;"> [Stożek](Part_Cone/pl.md).
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width   *32px;"> [Sfera](Part_Sphere/pl.md)   * tworzy sferę. Obiekt ten można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Sphere.svg  style="width   *32px;"> [Sfera](Part_Sphere/pl.md).
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width   *32px;"> [Elipsoida](Part_Ellipsoid/pl.md)   * tworzy elipsoidę.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width   *32px;"> [Torus](Part_Torus/pl.md)   * tworzy torus. Obiekt ten można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Torus.svg  style="width   *32px;"> [Torus](Part_Torus/pl.md) tool.
    -   <img alt="" src=images/Part_Prism.svg  style="width   *32px;"> [Graniastosłup](Part_Prism/pl.md)   * tworzy graniastosłup.
    -   <img alt="" src=images/Part_Wedge.svg  style="width   *32px;"> [Klin](Part_Wedge/pl.md)   * tworzy klin.
    -   <img alt="" src=images/Part_Helix.svg  style="width   *32px;"> [Helisa](Part_Helix/pl.md)   * tworzy helisę.
    -   <img alt="" src=images/Part_Spiral.svg  style="width   *32px;"> [Spirala](Part_Spiral/pl.md)   * tworzy spiralę.
    -   <img alt="" src=images/Part_Circle.svg  style="width   *32px;"> [Okrąg](Part_Circle/pl.md)   * tworzy łuk koła.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width   *32px;"> [Elipsa](Part_Ellipse/pl.md)   * tworzy łuk eliptyczny.
    -   <img alt="" src=images/Part_Point.svg  style="width   *32px;"> [Punkt](Part_Point/pl.md)   * tworzy punkt.
    -   <img alt="" src=images/Part_Line.svg  style="width   *32px;"> [Linia](Part_Line/pl.md)   * tworzy linę.
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width   *32px;"> [Wielokąt foremny](Part_RegularPolygon/pl.md)   * tworzy wielokąt foremny.

-   <img alt="" src=images/Part_Builder.svg  style="width   *32px;"> [Konstruktor kształtu \...](Part_Builder/pl.md)   * tworzy kształty z różnych elementów pierwotnych.

### Tworzenie i modyfikowanie obiektów 

Są to narzędzia do tworzenia i modyfikacji istniejących obiektów.

-   <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> [Wyciągnięcie](Part_Extrude/pl.md)   * wyciąga płaskie powierzchnie obiektu.

-   <img alt="" src=images/Part_Revolve.svg  style="width   *32px;"> [Obrót \...](Part_Revolve/pl.md)   * tworzy bryłę obracając inny obiekt *(nie będący bryłą)* wokół osi.

-   <img alt="" src=images/Part_Mirror.svg  style="width   *32px;"> [Odbicie lustrzane \...](Part_Mirror/pl.md)   * odtwarza wybrany obiekt na danej płaszczyźnie lustrzanej.

-   <img alt="" src=images/Part_Fillet.svg  style="width   *32px;"> [Zaokrąglenie \...](Part_Fillet/pl.md)   * zaokrągla krawędzie obiektu.

-   <img alt="" src=images/Part_Chamfer.svg  style="width   *32px;"> [Fazka \...](Part_Chamfer/pl.md)   * fazowanie krawędzi obiektu.

-   <img alt="" src=images/Part_MakeFace.svg  style="width   *32px;"> [Utwórz ścianę z linii łamanych](Part_MakeFace/pl.md)   * Tworzy ścinę z zestawu linii. {{Version/pl|0.19}}

-   <img alt="" src=images/Part_RuledSurface.svg  style="width   *32px;"> [Utwórz powierzchnię prostokreślną](Part_RuledSurface/pl.md)   * tworzy powierzchnie bazującą np. na łuku.

-   <img alt="" src=images/Part_Loft.png  style="width   *32px;"> [Wyciągnięcie przez profile](Part_Loft/pl.md)   * przeciąga jeden profil do drugiego.

-   <img alt="" src=images/Part_Sweep.svg  style="width   *32px;"> [Wyciągnięcie po ścieżce \...](Part_Sweep/pl.md)   * rozciąga jeden lub więcej profili wzdłuż ścieżki.

-   <img alt="" src=images/Part_Section.svg  style="width   *32px;"> [Przekrój](Part_Section/pl.md)   * tworzy przekrój, przecinając obiekt płaszczyzna przekroju.

-   <img alt="" src=images/Part_CrossSections.svg  style="width   *32px;"> [Wiele przekrojów\...](Part_SectionCross.md)   * tworzy jeden lub więcej przekrojów przez wybrany kształt.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width   *48px;"> [Narzędzie do odsunięcia \...](Part_CompOffsetTools.md)   *
    -   <img alt="" src=images/Part_Offset.svg  style="width   *32px;"> [3D Offset](Part_Offset.md)   * konstruuje kształt równoległy w pewnej odległości od oryginału.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width   *32px;"> [2D Offset](Part_Offset2D.md)   * konstruuje rzut równoległy w pewnej odległości od oryginału lub powiększa / zmniejsza powierzchnię płaską. {{Version/pl|0.17}}

-   <img alt="" src=images/Part_Thickness.svg  style="width   *32px;"> [Narzędzie do ustawiania grubości](Part_Thickness.md)   * wydrąża bryłę, nadaje powierzchni określoną grubość.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width   *32px;"> [Projekcja na powierzchni](Part_ProjectionOnSurface.md)   * Rzutuje logo, tekst lub dowolną ściankę, linie łamaną lub krawędź na powierzchnię. {{Version/pl|0.19}}

-   <img alt="" src=images/Part_EditAttachment.svg  style="width   *32px;"> [Edycja mocowania](Part_EditAttachment/pl.md)   * jest to narzędzie służące do dołączania obiektu do innego obiektu.

### Narzędzia do przeprowadzania operacji logicznych 

Narzędzia te wykonują operacje logiczne.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width   *48px;"> [Narzędzie złożone](Part_CompCompoundTools.md)   * działa z listą kształtów.
    -   <img alt="" src=images/Part_Compound.svg  style="width   *32px;"> [Utwórz kombinację](Part_Compound/pl.md)   * tworzy element złożony z wybranych obiektów.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width   *32px;"> [Rozłóż kombinację](Part_ExplodeCompound.md)   * dzieli element złożony na poszczególne kształty.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width   *32px;"> [Filtr kombinacji](Part_Compound‏‎Filter.md)   * filtr kombinacji może być używany do oddzielania poszczególnych elementów.

-   <img alt="" src=images/Part_Boolean.svg  style="width   *32px;"> [Operacje logiczne](Part_Boolean/pl.md)   * wykonuje operacje z użyciem funkcji logicznych na obiektach.

-   <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> [Wycięcie](Part_Cut/pl.md)   * Wycina *(odejmuje)* jeden obiekt z drugiego.

-   <img alt="" src=images/Part_Fuse.svg  style="width   *32px;"> [Łączenie](Part_Fuse/pl.md)   * zespaja *(dodaje)* dwa obiekty.

-   <img alt="" src=images/Part_Common.svg  style="width   *32px;"> [Część wspólna](Part_Common/pl.md)   * wyodrębnia wspólną *(krzyżującą się)* część dwóch obiektów.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width   *48px;"> [Łączenie elementów](Part_CompJoinFeatures.md)   * inteligentne funkcje logiczne dla obiektów posiadających ścianki *(np. rury)*.
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width   *32px;"> [Połącz](Part_JoinConnect.md)   * łączy elementy *(do wewnętrznych płaszczyzn)*.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width   *32px;"> [Wstaw](Part_JoinEmbed.md)   * osadza obiekt posiadający ścianki w innym obiekcie ze ściankami.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width   *32px;"> [Wytnij](Part_JoinCutout.md)   * tworzy wycięcie w ścianie obiektu dla innego obiektu ze ściankami.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width   *48px;"> [Narzędzia do rozdzielania](Part_CompSplittingTools/pl.md)   *
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width   *32px;"> [Fragmenty funkcji fogicznych](Part_BooleanFragments/pl.md)   * tworzy wszystkie elementy, które można uzyskać poprzez operacje logiczne pomiędzy obiektami.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width   *32px;"> [Pokrój część](Part_SliceApart/pl.md)   * Przecina i dzieli obiekt przez przecięcie go przez inne obiekty.
    -   <img alt="" src=images/Part_Slice.svg  style="width   *32px;"> [Rozkrój częścią](Part_Slice/pl.md)   * Dzieli obiekt na części, przecinając go innym obiektem.
    -   <img alt="" src=images/Part_XOR.svg  style="width   *32px;"> [XOR](Part_XOR/pl.md)   * usuwa przestrzeń współdzieloną elementów o parzystym numerze.

### Pomiary

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width   *32px;"> [Pomiar liniowy](Part_Measure_Linear/pl.md)   * pozwala na wykonywanie pomiarów wzdłuż linii.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width   *32px;"> [Pomiar kąta](Part_Measure_Angular/pl.md)   * pozwala na wykonywanie pomiarów nachylenia linii prostej.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width   *32px;"> [Odnów pomiary](Part_Measure_Refresh/pl.md)   * aktualizuje widok 3D, aby wyświetlić wszystkie utworzone pomiary.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width   *32px;"> [Wyczyść wszystko](Part_Measure_Clear_All/pl.md)   * usuwa wszystkie pomiary.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width   *32px;"> [Przełacz widoczność](Part_Measure_Toggle_All/pl.md)   * pokazuje lub ukrywa widoczność wszystkich pomiarów.

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width   *32px;"> [Pokaż wybrane](Part_Measure_Toggle_3D/pl.md)   * narzędzie to przełącza widoczność pomiarów liniowych *(kolor zielony)* i kątowych *(kolor niebieski)*.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width   *32px;"> [Przełącz deltę](Part_Measure_Toggle_Delta/pl.md)   * narzędzie to przełącza widoczność pomiarów delta *(kolor zielony)*.

### Pozostałe narzędzia 

-   <img alt="" src=images/Part_Import.svg  style="width   *32px;"> [Importuj CAD](Part_Import.md)   * narzędzie to umożliwia import pliku \*.IGES, \*.STEP, \*.BREP do bieżącego dokumentu.

-   <img alt="" src=images/Part_Export.svg  style="width   *32px;"> [Eksport CAD](Part_Export.md)   * narzędzie to umożliwia eksport do pliku \*.IGES, \*.STEP, \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width   *32px;"> [Pole wyboru](Part_BoxSelection/pl.md)   * dodaj do zaznaczenia powierzchnie czołowe bryły, które są objęte zaznaczeniem prostokątnym.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width   *32px;"> [Utwórz kształt z siatki](Part_ShapeFromMesh.md)   * tworzy bryłę z obiektu siatki.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width   *32px;"> [Punkty z siatki](Part_PointsFromMesh.md)   * tworzy kształt obiektu utworzonego na podstawie punktów z siatki. <small>(v0.19)</small> 

-   [Konwersja do bryły](Part_MakeSolid.md)   * konwertuje obiekt kształtu na bryłę.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width   *32px;"> [Odwróć kształty](Part_ReverseShapes.md)   * przerzuca normalne wszystkich powierzchni zaznaczonego obiektu.

-   Wykonaj duplikat   *
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width   *32px;"> [Create simple copy](Part_SimpleCopy.md)   * Creates a simple copy of the selected object.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width   *32px;"> [Utwórz przekształconą kopię](Part_TransformedCopy.md)   * tworzy przesuniętą kopię wybranego obiektu. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width   *32px;"> [Utworz kopię kształtu elementu](Part_ElementCopy.md)   * tworzy kopię z elementu *(wierzchołka, krawędzi, ścianki)* wybranego obiektu. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_RefineShape.svg  style="width   *32px;"> [Udoskonal kształt](Part_RefineShape.md)   * czyści ściany usuwając niepotrzebne linie.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width   *32px;"> [Analizuje geometrię \...](Part_CheckGeometry.md)   * sprawdza geometrię wybranych obiektów pod kątem błędów.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width   *32px;"> [Usuń właściwość z kształtu](Part_Defeaturing.md)   * Usuwa cechy z danego obiektu.

### Pozycje w menu kontekstowym 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width   *32px;"> [Wygląd zewnętrzny](Std_SetAppearance.md)   * określa wygląd całej części *(przezroczystość, kolor itp.)*.

-   <img alt="" src=images/Part_FaceColors.svg  style="width   *32px;"> [Ustaw kolor](Part_FaceColors.md)   * przypisuje kolory do poszczególnych powierzchni obiektu.

## Ustawienia

-   <img alt="" src=images/Preferences-part_design.svg  style="width   *32px;"> [Preferencje](PartDesign_Preferences/pl.md)   * preferencje dostępne dla narzędzi środowiska Część *(Środowisko Part korzysta również z Preferencji Projekt Części)*.
-   <img alt="" src=images/Preferences-import-export.svg  style="width   *32px;"> [Ustawienia import - eksport](Import_Export_Preferences/pl.md)   * preferencje dostępne przy imporcie z i eksporcie do różnych formatów plików.
-   [Dostrajanie parametrów](Fine-tuning/pl.md)   * kilka dodatkowych parametrów, aby dostosować zachowanie środowiska pracy Część.

## Tworzenie skryptów 

Zobacz również   * [skrypty dla środowiska Część](Part_scripting/pl.md)

## Poradniki

-   [Import formatu STL lub OBJ](Import_from_STL_or_OBJ/pl.md)    * w jaki sposób zaimportować plik STL/OBJ w programie FreeCAD.
-   [Eksport do formatu STL lub OBJ](Export_to_STL_or_OBJ/pl.md)    * w jaki sposób eksportować pliki STL/OBJ z programu FreeCAD.
-   [Poradnik   * Kula Whiffle](Whiffle_Ball_tutorial/pl.md)    * Jak korzystać ze środowiska pracy Część.





 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/pl
