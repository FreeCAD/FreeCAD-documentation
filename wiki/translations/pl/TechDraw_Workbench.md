# <img alt="Ikonka FreeCAD dla środowiska pracy Rysunek Techniczny" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/pl



## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) służy do tworzenia podstawowych rysunków technicznych z modeli 3D tworzonych przy użyciu innego środowiska pracy, takich jak [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md), lub importowanych z innych aplikacji. Każdy rysunek jest Stroną, która może zawierać różne widoki obiektów rysunkowych, takich jak Part::Features, PartDesign::Bodies, App::Part groups i Document Object groups. Powstałe w ten sposób rysunki mogą być wykorzystane do takich celów jak dokumentacja, instrukcje produkcyjne, umowy, pozwolenia, itp.

Wymiary, przekroje, zakreskowane obszary, adnotacje i symbole [SVG](SVG/pl.md) mogą być dodane do strony, która może być dalej eksportowana do różnych formatów, takich jak [DXF](DXF/pl.md), [SVG](SVG/pl.md), i [PDF](PDF/pl.md).

Jeśli Twoim głównym celem jest tworzenie złożonych rysunków 2D i plików [DXF](DXF/pl.md), a nie potrzebujesz modelowania 3D, FreeCAD może nie być właściwym wyborem dla Ciebie. Możesz rozważyć zastosowanie dedykowanego programu do tworzenia projektów technicznych, takiego jak [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), lub innego.




<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">



## Strony

Te narzędzia służą do tworzenia obiektów na stronie.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Wstaw nową stronę rysunku](TechDraw_PageDefault/pl.md): dodaje nową stronę przy użyciu domyślnego [Szablonu](TechDraw_Templates/pl.md).

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Wstaw nową stronę przy użyciu szablonu](TechDraw_PageTemplate/pl.md): dodaje nową stronę przy użyciu ustawienia z [szablonu](TechDraw_Templates/pl.md).

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Odśwież widok](TechDraw_RedrawPage/pl.md): wymusza aktualizację wybranej strony.

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width:32px;"> [Drukuj wszystkie strony](TechDraw_PrintAll/pl.md): drukuje wszystkie strony rysunku. {{Version/pl|0.21}}



## Widoki

Są to narzędzia do tworzenia obiektów widoku.

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Wstaw widok na stronę](TechDraw_View/pl.md): dodaje widok obiektu wyświetlany w formie projekcji 2D.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Wstaw aktywny widok](TechDraw_ActiveView/pl.md): wstawia kopię widoku z okna 3D do strony rysunku.

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Wstaw wiele połączonych widoków](TechDraw_ProjectionGroup/pl.md): otwiera okno dialogowe do tworzenia wielu widoków obiektu z róznych kierunków.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Wstaw widok przekroju:

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Wstaw widok przekroju](TechDraw_SectionView/pl.md): dodaje widok przekroju dla aktualnego widoku.

  - <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Wstaw przekrój złożony](TechDraw_ComplexSection/pl.md): wstawia widok przekroju istniejącego widoku na podstawie profilu. {{Version/pl|0.21}}

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Wstaw widok szczegółu](TechDraw_DetailView/pl.md): dodaje widok szczegółu części wybranego widoku.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Wstaw widok obiektu Rysunek Roboczy](TechDraw_DraftView/pl.md): dodaje do widoku strony obiekt ze środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Wstaw widok sekcji z planu Arch](TechDraw_ArchView/pl.md): dodaje widok obiektu [SectionPlane](Arch_SectionPlane/pl.md) ze środowiska pracy [Architektura](Arch_Workbench/pl.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Wstawia widok wybranego Arkusza](TechDraw_SpreadsheetView/pl.md): wstawia widok ze Środowiska pracy [Arkusz kalkulacyjny](Spreadsheet_Workbench/pl.md).

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Przenieś widok](TechDraw_MoveView/pl.md): przenosi widok i jego elementy zależne na inną stronę. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Udostępnij widok](TechDraw_ShareView/pl.md): współdzieli widok pomiędzy wieloma stronami. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:32px;"> [Rzut kształtu](TechDraw_ProjectShape/pl.md): tworzy rzut kształtu w oknie [widoku 3D](3D_view/pl.md). {{Version/pl|0.20}}



## Układanie widoków 

Są to narzędzia do zmiany kolejności układania, która kontroluje pozorną głębokość widoków na stronie.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dostosuj kolejność w wierszach:

  - <img alt="" src=images/TechDraw_StackTop.svg  style="width:32px;"> [Przesuń widok na górę](TechDraw_StackTop/pl.md): przesuwa widoki na górny poziom. {{Version/pl|0.21}}

  - <img alt="" src=images/TechDraw_StackBottom.svg  style="width:32px;"> [Przesuń widok na dół](TechDraw_StackBottom/pl.md): przesuwa widoki na dolny poziom. {{Version/pl|0.21}}

  - <img alt="" src=images/TechDraw_StackUp.svg  style="width:32px;"> [Przesuwa widoki w górę](TechDraw_StackUp/pl.md): przesuwa widoki o jeden poziom w górę. {{Version/pl|0.21}}

  - <img alt="" src=images/TechDraw_StackDown.svg  style="width:32px;"> [Przesuwa widoki w dół](TechDraw_StackDown/pl.md): przesuwa widoki o jeden poziom w dół. {{Version/pl|0.21}}



## Wycinki

Są to narzędzia do tworzenia i zarządzania obiektami wycinków *(przycięte widoki)*.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Wstaw grupę wycinków](TechDraw_ClipGroup/pl.md): wstawia do strony grupę wycinków.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Dodaj widok do grupy wycinków](TechDraw_ClipGroupAdd/pl.md): dodaje istniejący widok do grupy wycinków.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Usuń widok z grupy wycinków](TechDraw_ClipGroupRemove/pl.md): usuwa widok z grupy wycinków.



## Wystrój

Są to narzędzia do modyfikowania wyglądu stron lub widoków.

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Kreskowanie powierzchni \...](TechDraw_Hatch/pl.md): nakłada wzór kreskowania z pliku na ścianę.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Geometryczne kreskowanie \...](TechDraw_GeometricHatch/pl.md): stosuje wzór kreskowania na powierzchni przy użyciu specyfikacji Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [Wstaw symbol \...](TechDraw_Symbol/pl.md): wstawia do zawartości strony symbol [SVG](SVG/pl.md).

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Wstaw obraz](TechDraw_Image/pl.md): wstawia obrazek PNG lub JPG [bitmapy](Bitmap/pl.md) do zawartości strony.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Przełącz widoczność ramki](TechDraw_ToggleFrame/pl.md): włącza i wyłącza ramki oraz etykiety otaczające widok.



## Wymiary

Są to narzędzia do tworzenia i pracy z obiektami Wymiarowymi.

Wymiary liniowe mogą być wyznaczone w oparciu o dwa punkty, na jednej linii lub na dwóch liniach.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md): dodaje wymiar dotyczący odległości.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md): dodaje poziomy wymiar długości.

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Wstaw wymiar pionowy](TechDraw_VerticalDimension/pl.md): dodaje pionowy wymiar długości.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Wstaw wymiar promienia](TechDraw_RadiusDimension/pl.md): dodaje wymiar promienia do okręgu lub łuku.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Wstaw wymiar średnicy](TechDraw_DiameterDimension/pl.md): dodaje wymiar średnicy do okręgu lub łuku.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Wstaw wymiar kąta](TechDraw_AngleDimension/pl.md): dodaje wymiar kąta pomiędzy dwoma krawędziami prostymi.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Wymiaruj kąt na podstawie 3 punktów](TechDraw_3PtAngleDimension/pl.md): dodaje wymiar kąta na podstawie trzech podanych punktów.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Wstaw wymiary zakresu:

  - <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Zakres poziomy](TechDraw_HorizontalExtentDimension/pl.md): dodaje wymiar poziomy.

  - <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Zakres pionowy](TechDraw_VerticalExtentDimension/pl.md): dodaje wymiar pionowy.

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Powiąż wymiar z geometrią 3D](TechDraw_LinkDimension/pl.md): umożliwia połączenie istniejącego wymiaru z geometrią 3D.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Wstaw adnotację w formie dymka](TechDraw_Balloon/pl.md): dodaje na stronie adnotację w *baloniku*.

-   <img alt="" src=images/TechDraw_AxoLengthDimension.svg  style="width:32px;"> [Wymiar długości w aksonometrii](TechDraw_AxoLengthDimension/pl.md): dodaje aksonometryczny wymiar długości. {{Version/pl|0.21}}

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Wstaw wymiar przestrzenny - opcja EXPERYMENTALNA](TechDraw_LandmarkDimension/pl.md): dodaje wymiar dystansu.

-   <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:32px;"> [Napraw wymiar](TechDraw_DimensionRepair/pl.md): może dopasować odniesienia geometrii 2D lub 3D dla wymiaru. {{Version/pl|0.21}}



## Adnotacje

Narzędzia do nanoszenia adnotacji służą do \" oznaczania \" rysunku dodatkowymi informacjami.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Dodaj Adnotację](TechDraw_Annotation/pl.md): dodaje zwykły blok tekstowy, który służy jako adnotacja.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Dodaj linię odniesienia](TechDraw_LeaderLine/pl.md): narzędzie dodaje linię odniesienia do wyświetlanego widoku.

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Blok tekstu sformatowanego](TechDraw_RichTextAnnotation/pl.md): Narzędzie dodaje blok adnotacji tekstu sformatowanego do [Linii wiodącej](TechDraw_LeaderLine/pl.md) lub widoku.

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dodaj wierzchołki kosmetyczne:

  - <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Wstaw wierzchołek kosmetyczny](TechDraw_CosmeticVertex/pl.md): Narzędzie dodaje wierzchołek, który nie jest częścią geometrii źródłowej.

  - <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Dodaj wierzchołki punktu środkowego](TechDraw_Midpoints/pl.md): Narzędzie Punkty środkowe dodaje Punkty pomocnicze w punktach środkowych jednej lub kilku wybranych krawędzi.

  - <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Dodaj wierzchołki kwadrantu](TechDraw_Quadrants/pl.md): Narzędzie Kwadrant dodaje wierzchołki pomocnicze w punktach ćwiartki jednej lub więcej wybranych krawędzi *(okrągłych)*.

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dodaj oś:



  - <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Dodaj oś ściany](TechDraw_FaceCenterLine/pl.md): Narzędzie Oś ściany dodaje linię środkową do wybranej ściany *(ścian)*.

  - <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Dodaj oś dwóch krawędzi](TechDraw_2LineCenterLine/pl.md): Narzędzie Oś dwóch krawędzi dodaje linię środkową pomiędzy dwoma krawędziami.

  - <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Dodaj oś dwóch punktów](TechDraw_2PointCenterLine/pl.md): Narzędzie Oś dwóch punktów dodaje linię środkową pomiędzy 2 punktami.

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Dodaj linię kosmetyczną \...](TechDraw_2PointCosmeticLine/pl.md): dodaje linię estetyczną łączącą 2 wierzchołki.

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Usuń obiekt kosmetyczny](TechDraw_CosmeticEraser/pl.md): Narzędzie to usuwa obiekty kosmetyczne z danej strony.

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [Zmień wygląd wybranych linii](TechDraw_DecorateLine/pl.md): Narzędzie to zmienia wygląd krawędzi.

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Pokaż / ukryj niewidoczne krawędzie](TechDraw_ShowAll/pl.md): Narzędzie pokazuje / ukrywa niewidoczne krawędzie lub linie w widoku.

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Dodaj informacje spawalnicze](TechDraw_WeldSymbol/pl.md): Narzędzie dodaje specyfikacje dotyczące spawania do istniejącej linii odniesienia.

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbol.svg  style="width:32px;"> [Dodaj symbol wykończenia powierzchni](TechDraw_SurfaceFinishSymbol/pl.md): dodaje do strony symbol wykończenia powierzchni. {{Version/pl|0.21}}

-   <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:32px;"> [Pasowanie otworu / wału](TechDraw_HoleShaftFit/pl.md): dodaje do wymiaru tolerancje otworu lub wałka przy użyciu ISO 286. {{Version/pl|0.21}}



## Pakiet rozszerzeń 

Pakiet rozszerzeń zawiera wiele przydatnych narzędzi do ulepszenia Twoich rysunków technicznych.



### Atrybuty i modyfikacje 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:32px;"> [Wybierz atrybuty linii, odstęp kaskadowy i odległość delta](TechDraw_ExtensionSelectLineAttributes/pl.md): wybierz atrybuty *(styl, szerokość i kolor)* dla nowych linii pomocniczych i linii środkowych oraz określa odstęp kaskadowy i odległość delta. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Zmień atrybuty linii](TechDraw_ExtensionChangeLineAttributes/pl.md): zmienia wygląd *(styl, szerokość i kolor)* linii pomocniczych. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Zmiana długości linii geometrii pomocniczych:



  - <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Rozciągnij linię](TechDraw_ExtensionExtendLine/pl.md): przedłuża linie pomocnicze na obu końcach. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Skróć linię](TechDraw_ExtensionShortenLine/pl.md): skraca linie pomocnicze na obu końcach. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Zablokuj / odblokuj widok](TechDraw_ExtensionLockUnlockView/pl.md): blokuje / odblokowuje pozycję widoku. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Wyrównaj widok przekroju](TechDraw_ExtensionPositionSectionView/pl.md): wyrównaj widok przekroju ortogonalnie, do widoku źródłowego. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Wyrównanie wymiarów:

  - <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Wyrównaj ciąg wymiarów poziomych](TechDraw_ExtensionPosHorizChainDimension/pl.md): wyrównuje wymiary poziome, tworząc ciąg wymiarów. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Wyrównaj ciąg wymiarów pionowych](TechDraw_ExtensionPosVertChainDimension/pl.md): wyrównuje wymiary pionowe, tworząc ciąg wymiarów. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Wyrównaj ciąg wymiarów ukośnych](TechDraw_ExtensionPosObliqueChainDimension/pl.md): wyrównuje wymiary ukośne, tworząc ciąg wymiarów. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Równomierne rozmieszczenie wymiarów:



  - <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Wymiar poziomy kaskadowo](TechDraw_ExtensionCascadeHorizDimension/pl.md): równomiernie rozmieszczone wymiary poziome. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Wymiar pionowy kaskadowo](TechDraw_ExtensionCascadeVertDimension/pl.md): równomiernie rozmieszczone wymiary pionowe. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Wymiar ukośny kaskadowo](TechDraw_ExtensionCascadeObliqueDimension/pl.md): równomiernie rozmieszczone wymiary ukośne. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width:32px;"> [Oblicz pole powierzchni wybranych ścian](TechDraw_ExtensionAreaAnnotation/pl.md): oblicza pole powierzchni wybranych powierzchni i wstawia adnotację z opisem powierzchni. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:32px;"> [Dostosuj format etykiety](TechDraw_ExtensionCustomizeFormat/pl.md): umożliwia dostosowanie formatowania tekstu dymka lub tekstu wymiarowego. Można dodawać symbole GD&T i inne znaki specjalne. {{Version/pl|0.20}}



### Linie środka i gwinty 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dodaj oś otworu:



  - <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Oś otworu](TechDraw_ExtensionCircleCenterLines/pl.md): dodaje linie środkowe do okręgów i łuków. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Osie otworów w okręgu](TechDraw_ExtensionHoleCircle/pl.md): dodaje linie środkowe okręgów w szyku koła. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dodaj geometrię pomocniczą gwintu:



  - <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Geometria pomocnicza dla otworu gwintowanego, widok z boku](TechDraw_ExtensionThreadHoleSide/pl.md): dodaje linię geometrii pomocniczej do bocznego widoku otworu. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Geometria pomocnicza dla otworu gwintowanego, widok od dołu](TechDraw_ExtensionThreadHoleBottom/pl.md): dodaje symbol gwintu do widoku otworów od dołu lub z góry. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Geometria pomocnicza dla gwintu śruby, widok z boku](TechDraw_ExtensionThreadBoltSide/pl.md): dodaje symbol gwintu do widoku bocznego śruby / nakrętki / pręta gwintowanego. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Geometria pomocnicza dla gwintu śruby, widok od dołu](TechDraw_ExtensionThreadBoltBottom/pl.md): dodaje symbol gwintu do widoku od dołu dla śruby / nakrętki / pręta gwintowanego . {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Utwórz wierzchołki w przecięciu](TechDraw_ExtensionVertexAtIntersection/pl.md): tworzy wierzchołki pomocnicze w miejscu przecięcia wybranych krawędzi. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dodaj geometrię pomocniczą okręgu lub łuku:



  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [Geometria pomocnicza obwodu](TechDraw_ExtensionDrawCosmCircle/pl.md): rysuje symboliczną linię obwodu, używając dwóch wierzchołków. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width:32px;"> [Geometria pomocnicza łuku](TechDraw_ExtensionDrawCosmArc/pl.md): rysuje geometrię pomocniczą łuku w kierunku przeciwnym do ruchu wskazówek zegara oparty na trzech wierzchołkach. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width:32px;"> [Geometria pomocnicza okręgu przez trzy punkty](TechDraw_ExtensionDrawCosmCircle3Points/pl.md): dodaje geometrię pomocniczą okręgu opartego na trzech wierzchołkach. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dodaj geometrię pomocniczą linii równoległej lub prostopadłej:



  - <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Rysuj linie równoległą](TechDraw_ExtensionLineParallel/pl.md): rysuje pomocniczą prostą równoległą do innej prostej, przez wierzchołek. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Rysuj linię prostopadłą](TechDraw_ExtensionLinePerpendicular/pl.md): rysuje pomocniczą prostą prostopadłą do innej prostej, przez wierzchołek. {{Version/pl|0.20}}



### Wymiarowanie

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz ciąg wymiarów:



  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Seria poziomo](TechDraw_ExtensionCreateHorizChainDimension/pl.md): tworzy ciąg wymiarów wyrównanych poziomo. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Seria pionowo](TechDraw_ExtensionCreateVertChainDimension/pl.md): tworzy ciąg wymiarów wyrównanych pionowo. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Seria ukośnie](TechDraw_ExtensionCreateObliqueChainDimension/pl.md): tworzy ciąg wymiarów wyrównanych ukośnie. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz wymiary skoordynowane:



  - <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Seria kaskadowych wymiarów poziomo](TechDraw_ExtensionCreateHorizCoordDimension/pl.md): tworzy wiele wymiarów poziomych ułożonych wzdłuż jednej linii. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Seria kaskadowych wymiarów pionowo](TechDraw_ExtensionCreateVertCoordDimension/pl.md): tworzy wiele wymiarów pionowych ułożonych wzdłuż jednej linii. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Seria kaskadowych wymiarów ukośnie](TechDraw_ExtensionCreateObliqueCoordDimension/pl.md): tworzy wiele wymiarów ukośnych ułożonych wzdłuż jednej linii. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz wymiary fazki:



  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Wymiar poziomy fazki](TechDraw_ExtensionCreateHorizChamferDimension/pl.md): tworzy wymiar poziomy i wymiar kątowy dla sfazowania. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Wymiar pionowy fazki](TechDraw_ExtensionCreateVertChamferDimension/pl.md): tworzy wymiar pionowy i wymiar kątowy dla sfazowania. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Długość łuku](TechDraw_ExtensionCreateLengthArc/pl.md): tworzy wymiar długości łuku. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Wstaw prefiks:



  - <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [Symbol średnicy \"⌀\"](TechDraw_ExtensionInsertDiameter/pl.md): wstawia symbol \"⌀\" na początku tekstu wymiaru. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [Symbol \"〼\"](TechDraw_ExtensionInsertSquare/pl.md): wstawia symbol \"〼\" na początku tekstu wymiaru. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width:32px;"> [Usuń symbol wiodący](TechDraw_ExtensionRemovePrefixChar/pl.md): usuwa dowolne symbole na początku tekstu wymiaru. {{Version/pl|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Zmień ilość miejsc dziesiętnych:



  - <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Zwiększenie dokładności](TechDraw_ExtensionIncreaseDecimal/pl.md): zwiększa liczbe miejsc po przecinku. {{Version/pl|0.20}}

  - <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Zmniejszenie dokładności](TechDraw_ExtensionDecreaseDecimal/pl.md): zmniejsza liczbe miejsc po przecinku. {{Version/pl|0.20}}



## Eksport

Są to narzędzia do eksportu zawartości stron do innych programów.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Zapisz aktywną stronę w formacie SVG](TechDraw_ExportPageSVG/pl.md): eksport strony do pliku w formacie [SVG](SVG/pl.md).

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Zapisz aktywną stronę w formacie DXF](TechDraw_ExportPageDXF/pl.md): eksport strony do pliku w formacie [DXF](DXF/pl.md).



## Dodatkowe właściwości 

-   [Grupy linii](TechDraw_LineGroup/pl.md): domyślne wagi można przypisać do różnych typów linii.
-   [Szablony](TechDraw_Templates/pl.md): domyślne szablony zdefiniowane dla stron rysunku.
-   [Wypełnienie kreskowaniem](TechDraw_Hatching/pl.md): objaśnienie różnych technik kreskowania.

[Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl.md): wyjaśnienie, jak osiągnąć wymiarowanie geometrii i tolerancji.



## Ustawienia

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Ustawienia](TechDraw_Preferences/pl.md): ustawienia domyślnych wartości strony rysunku, takich jak kąt projekcji, kolory, rozmiary tekstu i style linii.



## Tworzenie skryptów 

Narzędzi środowiska Rysunek Techniczny można używać w [makrodefinicjach](Macros/pl.md) oraz w konsoli [Python](Python/pl.md). Więcej informacji można znaleźć na stronach:

-   [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/),
-   [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md),
-   [Pola tekstowe do edycji](TechDraw_PageDefault/pl#Pola_tekstowe_do_edycji.md).



## Ograniczenia

-   Nie wycinaj, kopiuj i wklejaj obiektów Rysunku Technicznego w okienku [Widoku drzewa](Tree_view/pl.md), ponieważ zazwyczaj nie wychodzi to dobrze.
-   Nie należy przeciągać obiektów Rysunku Technicznego w okienku [Widoku drzewa](Tree_view/pl.md) za pomocą myszy.



## Poradniki

-   [Poradnik: Podstawy dla Środowiska pracy Rysunek Techniczny](Basic_TechDraw_Tutorial/pl.md): wprowadzenie do tworzenia rysunków przy użyciu środowiska pracy Rysunek Techniczny.
-   [Rysunek Techniczny: Jak wykonać nowy szablon ramki](TechDraw_TemplateHowTo/pl.md): instrukcja tworzenia nowego szablonu strony w programie Inkscape do użycia w środowisku pracy Rysunek Techniczny.

-   [Generator szablonów](TechDraw_TemplateGenerator/pl.md): instrukcje tworzenia makra do generowania podstawowego szablonu.

:   Po dodaniu \"kilku\" wierszy kodu powstaje narzędzie takie jak [Makro Pomocnik szablonów](Macro_TemplateHelper/pl.md).

-   [Pomiar kątów na otworach](Measurement_Of_Angles_On_Holes/pl.md): instrukcje dotyczące dodawania linii centrujących i kolejnych oznaczeń kątowych na otworach.
-   [Rozmaitości](TechDraw_HowTo_Page/pl.md): instrukcje dotyczące różnych ustawień, takich jak znaki środka, itp.
-   [Tworzenie koła podziałowego](TechDraw_Pitch_Circle_Tutorial/pl.md): instrukcja dodawania koła podziałowego.

Wideo poradniki przygotowane przez użytkownika sliptonic

-   Środowisko pracy Rysunek Techniczny [Część 1 *(Podstawy)*](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Część 2 *(Wymiary)*](https://www.youtube.com/watch?v=z3w84RfvqaE), [Część 3 *(Wiele widoków)*](https://www.youtube.com/watch?v=uNjXg-m38aI).
-   Środowisko pracy Rysunek Techniczny [Part 4 *(Przekrój i detal)*](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 *(Dostosowanie szablonu)*](https://www.youtube.com/watch?v=kcmdJ7xa7gg).



## Opracowanie i rozwój 

Chcesz poznać przyszłość środowiska pracy Rysunek Techniczny? Odwiedź stronę [Mapa rozwoju środowiska Rysunek Techniczny](TechDraw_Roadmap/pl.md), aby dowiedzieć się więcej.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/pl
