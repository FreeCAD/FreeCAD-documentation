# <img alt="Ikonka FreeCAD dla Środowiska pracy Rysunek Roboczy" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **Rysunek Roboczy** skupia się przede wszystkim na tworzeniu i modyfikacji obiektów 2D w programie FreeCAD. Nie jest jednak ograniczone do płaszczyzny XY globalnego układu współrzędnych. Jego obiekty mogą mieć dowolną orientację i położenie w przestrzeni, a niektóre obiekty Rysunku Roboczego mogą być zarówno płaskie jak i przestrzenne.

Obiekty Rysunku Roboczego mogą być używane do ogólnego szkicowania, podobnie jak w programie Inkscape lub AutoCAD. Ale mogą one również stanowić podstawę do tworzenia obiektów 3D w innych środowiskach pracy. A [polilinia](Draft_Wire/pl.md) może zdefiniować ścieżkę dla [ściany](Arch_Wall/pl.md) środowiska Architektura, [wielokąt](Draft_Polygon/pl.md) środowiska Rysunek Roboczy może być wciągany za pomocą funkcji [wyciągnięcia](Part_Extrude/pl.md) środowiska Część, itd. Wiele z [narzędzi modyfikujących](#Modyfikacja.md) środowiska pracy Rysunek Roboczy może być zastosowanych do obiektów płaskich oraz przestrzennych stworzonych za pomocą innych środowisk pracy. Możesz, na przykład, [przesunąć](Draft_Move/pl.md) [szkic](Sketcher_Workbench/pl.md) lub stworzyć [szyk ortogonalny](Draft_OrthoArray/pl.md) z obiektu [Części](Part_Workbench/pl.md).

Środowisko pracy Rysunek Roboczy dostarcza również narzędzi do definiowania [płaszczyzny roboczej](Draft_SelectPlane/pl.md), [siatki](Draft_Snap_Grid/pl.md) oraz [systemu przyciągania](Draft_Snap/pl.md) do precyzyjnego sterowania położeniem geometrii.

Jeśli Twoim głównym celem jest tworzenie złożonych rysunków 2D i plików [DXF](DXF/pl.md), a nie potrzebujesz modelowania 3D, FreeCAD może nie być właściwym wyborem dla Ciebie. Możesz rozważyć zastosowanie dedykowanego programu do tworzenia projektów technicznych, takiego jak [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), lub innego.

![](images/Draft_Workbench_Example.png ) 
*Obrazek przedstawia [siatkę](Draft_Snap_Grid/pl.md) wyrównaną do płaszczyzny XY.<br>
Po lewej stronie, na biało, kilka obiektów planarnych.<br>
Po prawej nieplanarny obiekt [polilinii](Draft_Wire/pl.md) użyty jako obiekt ścieżki w [wyciąganiu po ścieżce](Draft_PathArray/pl.md).*



## Kreślenie

-   Polecenie <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linia](Draft_Line/pl.md): tworzy linię prostą.

-   Polecenie <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinia](Draft_Wire/pl.md): tworzy polilinię, czyli sekwencję kilku połączonych segmentów linii.

-   Polecenie <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Zaokrąglenie](Draft_Fillet/pl.md): tworzy zaokrąglenie, zaokrąglony narożnik, lub fazę, prostą krawędź, pomiędzy dwoma [liniami](Draft_Line/pl.md).

-   <img alt="" src=images/Draft_Arc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Narzędzia łuku:

  - Polecenie <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Łuk](Draft_Arc/pl.md): tworzy łuk kołowy z punktu środka, promienia, kąta początkowego i kąta rozwarcia.

  - Polecenie <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Łuk przez trzy punkty](Draft_Arc_3Points/pl.md): tworzy łuk okręgu z trzech punktów, które definiują jego przebieg.

-   Polecenie <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Okrąg](Draft_Circle/pl.md): tworzy okrąg na podstawie środka i promienia.

-   Polecenie <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipsa](Draft_Ellipse/pl.md): tworzy elipsę z dwóch punktów definiujących prostokąt, w którym elipsa będzie wpisana.

-   Polecenie <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Prostokąt](Draft_Rectangle/pl.md): tworzy prostokąt z dwóch punktów.

-   Polecenie <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Wielokąt](Draft_Polygon/pl.md): tworzy wielokąt foremny o zadanym punkcie środkowym i promieniu.

-   Polecenie <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [Krzywa złożona](Draft_BSpline/pl.md): tworzy krzywą złożoną z kilku punktów.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Narzędzia Béziera:

  - Polecenie <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Sześcienna krzywa Béziera](Draft_CubicBezCurve/pl.md): tworzy krzywą Béziera trzeciego stopnia.

  - Polecenie <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Krzywa Béziera](Draft_BezCurve/pl.md): tworzy krzywą Béziera z kilku punktów.

-   Polecenie <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/pl.md): tworzy zwykły punkt.

-   Polecenie <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Łącznik kształtu](Draft_Facebinder/pl.md): tworzy obiekt powierzchni z wybranych ścian.

-   Polecenie <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Kształt z tekstu](Draft_ShapeString/pl.md): tworzy kształt złożony, który reprezentuje ciąg tekstowy.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Kreskowanie](Draft_Hatch/pl.md): tworzy kreskowanie na planarnych powierzchniach wybranego obiektu.



## Adnotacja

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Adnotacja wieloliniowa](Draft_Text/pl.md): tworzy wielowierszowy obiekt tekstu w zadanym punkcie.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Wymiarowanie](Draft_Dimension/pl.md): tworzy wymiar liniowy, wymiar kątowy lub wymiar promieniowy.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etykieta](Draft_Label/pl.md): tworzy tekst wielowierszowy z dwu-segmentową linią wiodącą i strzałką.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md): pozwala zdefiniować style, które wpływają na właściwości wizualne obiektów związanych z adnotacjami.



## Modyfikacja

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Przesuń](Draft_Move/pl.md): przesuwa lub kopiuje wybrane obiekty z jednego punktu do drugiego.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Obróć](Draft_Rotate/pl.md): obraca lub kopiuje wybrane obiekty wokół punktu środka o zadany kąt.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skaluj](Draft_Scale/pl.md): skaluje lub kopiuje wybrane obiekty wokół punktu bazowego.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Odbicie lustrzane](Draft_Mirror/pl.md): tworzy kopie w odbiciu lustrzanym z wybranych obiektów.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Odsunięcie](Draft_Offset/pl.md): odsuwa każdy segment wybranego obiektu o zadaną odległość lub tworzy przesuniętą kopię wybranego obiektu.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Przytnij](Draft_Trimex/pl.md): przycina lub wydłuża wybrany obiekt.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Rozciągnij](Draft_Stretch/pl.md): rozciąga obiekty poprzez przesuwanie wybranych punktów.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klonuj](Draft_Clone/pl.md): tworzy połączone kopie, klony wybranych obiektów.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Narzędzia szyku:

  - <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Szyk](Draft_OrthoArray/pl.md): tworzy szyk ortogonalny z wybranego obiektu. Opcjonalnie może utworzyć również szyk [powiązań](App_Link/pl.md).

  - <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Szyk biegunowy](Draft_PolarArray/pl.md): tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż obwodu. Opcjonalnie może utworzyć szyk [powiązań](App_Link/pl.md).

  - <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Szyk kołowy](Draft_CircularArray/pl.md): tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż obwodu okręgu. Opcjonalnie może utworzyć szyk [powiązań](App_Link/pl.md).

  - <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Szyk po ścieżce](Draft_PathArray/pl.md): tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż ścieżki.

  - <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Szyk powiązań po ścieżce](Draft_PathLinkArray/pl.md): podobnie, ale utwórz szyk [powiązań](App_Link/pl.md) zamiast zwykłego szyku.

  - <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Szyk z punktów](Draft_PointArray/pl.md): tworzy szyk z wybranego obiektu poprzez umieszczenie kopii w punktach ze zbioru punktów.

  - <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Szyk powiązań w punktach](Draft_PointLinkArray/pl.md): podobnie, ale utwórz szyk [powiązań](App_Link/pl.md) zamiast zwykłego szyku.

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edycja](Draft_Edit/pl.md): umieszcza wybrane obiekty w trybie edycji szkicu. W tym trybie właściwości obiektów mogą być edytowane graficznie.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Podświetl element podrzędny](Draft_SubelementHighlight/pl.md): tymczasowo podświetla wybrane obiekty lub obiekty bazowe wybranych obiektów.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Połącz](Draft_Join/pl.md): łączy [linie](Draft_Line/pl.md) oraz [polilinie](Draft_Wire/pl.md) w pojedynczą polilinię.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Rozdziel](Draft_Split/pl.md): dzieli [Linie](Draft_Line/pl.md) lub [polilinie](Draft_Wire/pl.md) w określonym punkcie lub krawędzi.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Ulepsz kształt](Draft_Upgrade/pl.md): aktualizuje wybrane obiekty.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rozbij obiekt na elementy](Draft_Downgrade/pl.md): powoduje redukcję stopnia zaawansowania wybranych obiektów.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Polilinia na krzywą złożoną](Draft_WireToBSpline/pl.md): konwertuje [polilinię](Draft_Wire/pl.md) na [krzywą złożoną](Draft_BSpline/pl.md) i vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md): konwertuje obiekt [rysunek roboczy](Draft_Workbench/pl.md) na [szkic](Sketcher_NewSketch/pl.md) środowiska Szkicownik, oraz vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Nachylenie](Draft_Slope/pl.md): powoduje nachylenie wybranych [linii](Draft_Line/pl.md) lub [polilinii](Draft_Wire/pl.md) poprzez zwiększenie lub zmniejszenie współrzędnej Z, dla wszystkich punktów po pierwszym.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Obróć wymiar](Draft_FlipDimension/pl.md): obraca tekst wymiaru dla wybranych [wymiarów](Draft_Dimension/pl.md) o 180° wokół linii wymiaru.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Widok 2D kształtu](Draft_Shape2DView/pl.md): tworzy rzuty 2D z wybranych obiektów.



## Tacka narzędziowa 

Tacka narzędziowa środowiska [Rysunek Roboczy](Draft_Tray/pl.md) pojawia się po uruchomieniu stołu warsztatowego i umożliwia definiowanie ustawień stylu, przełączanie trybu konstrukcji i określanie aktywnej warstwy lub grupy.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Bieżąca płaszczyzna robocza](Draft_SelectPlane/pl.md): definiuje bieżącą płaszczyznę roboczą Rysunku Roboczego. Funkcja dostępna jest również w menu: **Narzędzia → <img src="images/Draft_SelectPlane.svg" width=16px> Wybierz płaszczyznę**.

-   ![](images/Draft_tray_button_style.png ) [Ustaw styl](Draft_SetStyle/pl.md): ustawia domyślny styl dla nowych obiektów. Dostępne również w menu: **Rysunek Roboczy → Narzędzia → <img src="images/Draft_SetStyle.svg" width=16px> Ustaw styl**.

-   ![](images/Draft_tray_button_construction.png ) [Przełącz tryb konstrukcyjny](Draft_ToggleConstructionMode/pl.md): włącza lub wyłącza tryb konstrukcji szkicu. Dostępne również w menu: **Rysunek Roboczy → Narzędzia → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Przełącz tryb konstrukcyjny**.

-   ![](images/Draft_tray_button_layer.png ) [Grupowanie automatyczne](Draft_AutoGroup/pl.md): zmienia aktywną [warstwę](Draft_Layer/pl.md) lub, opcjonalnie, aktywną [grupę](Std_Group/pl.md) lub grupę obiektów [BIM](BIM_Workbench/pl.md).



## Widżet skali adnotacji 

Za pomocą widżetu [skali adnotacji](Draft_annotation_scale_widget/pl.md) można określić skalę wyświetlanej adnotacji.

![](images/Draft_annotation_scale_widget_button.png )



## Widżet przyciągania 

Widżet [przyciągania](Draft_snap_widget/pl.md) może być używany jako alternatywa dla [paska narzędzi przyciągania](#Pasek_narz.C4.99dzi_Rysunek_roboczy:_Przyci.C4.85gnij.md).

![](images/Draft_snap_widget_button.png )



## Pasek narzędzi Rysunek roboczy: Przyciągnij 

Pasek narzędzi Rysunek Roboczy: Przyciągnij, umożliwia wybór aktywnych opcji przyciągania. Przyciski należące do aktywnych opcji pozostają wciśnięte. Ogólne informacje na temat przyciągania zobacz: [Rysunek roboczy: Przyciągnij](Draft_Snap/pl.md).

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md): przełącza globalnie [przyciąganie](Draft_Snap/pl.md) obiektów na włączone lub wyłączone.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md): przyciąga do punktów końcowych odcinków lub krawędzi.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md): przyciąga do punktu środkowego krawędzi.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Przyciągnij do środka](Draft_Snap_Center/pl.md): przyciąga do punktu środkowego powierzchni i krawędzi kołowych, a także do punktu {{PropertyData/pl|Umiejscowienia}} [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md) i [Architektura: Część budowli - piętro](Arch_BuildingPart/pl.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Przyciągnij do kąta](Draft_Snap_Angle/pl.md): przyciąga do specjalnych punktów odniesienia okręgów i łuków, przy wielokrotnościach 30° i 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Przyciągnij do punktu przecięcia](Draft_Snap_Intersection/pl.md): przyciąga do przecięcia dwóch krawędzi.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Przyciągnij prostopadle](Draft_Snap_Perpendicular/pl.md): przyciąga prostopadle do ostatniego punktu na ścianie *({{Version/pl|0.21}})* oraz krawędzi.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Przyciągnij na wydłużeniu](Draft_Snap_Extension/pl.md): przyciąga do umownej linii, która rozciąga się poza punkty końcowe odcinka.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Przyciągnij równolegle](Draft_Snap_Parallel/pl.md): przyciąga do umownej linii równoległej do odcinka linii.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Przyciągnij specjalnie](Draft_Snap_Special/pl.md): przyciąga na punktach specjalnych zdefiniowanych przez obiekt.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Przyciągnij do najbliższego](Draft_Snap_Near/pl.md): przyciąga do najbliższego punktu oraz krawędzi najbliższego obiektu.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Przyciągnij ortogonalnie](Draft_Snap_Ortho/pl.md): przyciąga na umownych liniach, które przecinają ostatni punkt pod wielokrotnością kąta 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Przyciągnij do siatki](Draft_Snap_Grid/pl.md): przyciąga na przecięciach linii siatki.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Przyciągnij do płaszczyzny roboczej](Draft_Snap_WorkingPlane/pl.md): zawsze umieszcza przyciągane punkty na aktualnej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Przyciągnij do wymiaru](Draft_Snap_Dimensions/pl.md): prezentuje tymczasowe wymiary X i Y podczas przyciągania.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md): włącza lub wyłącza widoczność siatki.



### Pasek narzędzi użytkowych 

-   <img alt="" src=images/Draft_LayerManager.svg  style="width:32px;"> [Zarządzaj warstwami \...](Draft_LayerManager/pl.md): Umożliwia zarządzanie warstwami w dokumencie. {{Version/pl|0.21}}

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> [Dodaj grupe o nazwie](Draft_AddNamedGroup/pl.md): tworzy nazwaną [Grupę Std](Std_Group/pl.md) i przenosi wybrane obiekty do tej grupy.

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Dodaj do grupy](Draft_AddToGroup/pl.md): przenosi obiekt do określonej [Grupy](Std_Group/pl.md). Może również usuwać grupy obiektów.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Wybierz grupę](Draft_SelectGroup/pl.md): wybiera zawartość [warstwy](Draft_Layer/pl.md), [Grupy](Std_Group/pl.md) lub obiektów zbliżone do grupy [BIM](BIM_Workbench/pl.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Dodaj do grupy konstrukcyjnej](Draft_AddConstruction/pl.md): przenosi obiekty do [trybu konstrukcji](Draft_ToggleConstructionMode/pl.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Przełącz tryb wyświetlania](Draft_ToggleDisplayMode/pl.md): przełącza {{PropertyView/pl|Tryb wyświatlania}} właściwości wybranych obiektów pomiędzy {{Value|cieniowany z krawędziami}} oraz {{Value|szkielet}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md): tworzy zastępczą płaszczyznę roboczą, aby zapisać bieżącą [płaszczyznę robocza projektu](Draft_SelectPlane/pl.md).



## Dodatkowe narzędzia 

Menu środowiska Rysunek Roboczy **Narzędzia** zawiera kilka narzędzi. Większość z nich jest dostępna również z pasków narzędziowych i została już wymieniona powyżej. W przypadku poniższych narzędzi nie jest to regułą.

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Zastosuj bieżący styl](Draft_ApplyStyle/pl.md): stosuje bieżące ustawienia stylu do wybranych obiektów.

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Warstwa](Draft_Layer/pl.md): tworzy [warstwę](Draft_Layer/pl.md) środowiska Rysunek Roboczy.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Uleczenie](Draft_Heal/pl.md): leczy problematyczne obiekty Rysunku Roboczego znajdujące się w bardzo starych plikach.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Pokaż przybornik przyciągania](Draft_ShowSnapBar/pl.md): wyświetla [pasek narzędzi przyciągania](#Pasek_narz.C4.99dzi_Rysunek_roboczy:_Przyci.C4.85gnij.md).



## Dodatkowe właściwości 

-   [Płaszczyzna robocza](Draft_SelectPlane/pl.md): Umożliwia wybranie powierzchni w oknie [widoku 3D](3D_view.md), na której można budować swoje kształty.
-   [Przyciąganie](Draft_Snap/pl.md): Pozwala wybierać dokładne punkty geometryczne na, lub zdefiniowane przez, istniejące obiekty lub siatkę.
-   [Wiązania](Draft_Constrain/pl.md): Dla każdego kolejnego punktu można ograniczyć ruch kursora do kierunku X, Y lub Z.
-   [Tryb konstrukcji](Draft_ToggleConstructionMode/pl.md): Umieszcza nowe obiekty Rysunku Roboczego w dedykowanej grupie, ułatwiając ich ukrywanie lub usuwanie.
-   [Wzór](Draft_Pattern/pl.md): Obiekty Rysunku Roboczego z właściwością {{PropertyData/pl|Utwórz ścianę}} mogą wyświetlać wzór SVG zamiast jednolitego koloru ściany.



## Menu kontekstowe widoku drzewa 

W menu kontekstowym [Widoku drzewa](Tree_view/pl.md) dostępne są następujące dodatkowe opcje:



### Opcje domyślne 

Dla większości obiektów Rysunku Roboczego dostępna jest następująca opcja:

-   Edycja: edytuje obiekt. W zależności od typu obiektu używana jest albo funkcja [Edytuj](Draft_Edit/pl.md) albo dedykowane rozwiązanie edycyjne. {{Version/pl|0.21}}

Jeśli istnieje aktywny dokument, menu kontekstowe zawiera dodatkowe menu podrzędne:

-   Narzędzia: podzbiór narzędzi dostępnych w głównym menu Narzędzia Rysunku Roboczego.



### Opcje kontenera warstw 

Dla narzędzi [Kontenera warstw](Draft_Layer/pl.md) dostępne są te dodatkowe opcje:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Scal duplikaty warstw](Draft_Layer/pl#Opcje_kontenera_warstw.md): łączy wszystkie warstwy z tą samą etykietą bazową.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Warstwa](Draft_Layer/pl#Opcje_kontenera_warstw.md): dodaje nową warstwę do bieżącego dokumentu.



### Opcje warstw 

Dla narzędzi [Warstw](Draft_Layer/pl.md) dostępne są te dodatkowe opcje:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Grupowanie automatyczne](Draft_AutoGroup/pl.md): aktywuje wybraną warstwę.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Wybierz grupę](Draft_SelectGroup/pl.md): zaznacza obiekty znajdujące się wewnątrz wybranej warstwy.



### Opcje tekstu 

Dla [tekstów](Draft_Text/pl.md) i [etykiet](Draft_Label/pl.md), które zawierają jeden lub więcej hiperłączy do lokalnego lub zdalnego pliku lub adresu URL, dostępna jest ta dodatkowa opcja:

-   Otwórz hiperłącza: hiperłącza są otwierane w odpowiedniej aplikacji *(zdefiniowanej przez system operacyjny)*. W przypadku wielu hiperłączy pojawia się ostrzeżenie. {{Version/pl|1.0}}



### Opcje polilinii 

Ta dodatkowa opcja jest dostępna dla [linii](Draft_Line/pl.md), [polilinii](Draft_Wire/pl.md),:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Spłaszcz tę polilinię: spłaszcza polilinię na bieżącej [Płaszczyźnie roboczej](Draft_SelectPlane/pl.md). Ta opcja nie działa poprawnie w {{VersionMinus/pl|0.19}}.



### Opcje tymczasowej płaszczyzny roboczej 

Dla narzędzi [Pośredniej płaszczyzny roboczej](Draft_WorkingPlaneProxy/pl.md) dostępne są te dodatkowe opcje:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Zapisz ujęcie widoku](Draft_WorkingPlaneProxy/pl#Menu_podr.C4.99czne.md): aktualizuje właściwość {{PropertyView/pl|Dane widoku}} pośrednika płaszczyzny roboczej o bieżące ustawienia ujęcia widoku okna [widoku 3D](3D_view/pl.md).

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Zapisz stan obiektów](Draft_WorkingPlaneProxy/pl#Menu_podr.C4.99czne.md): aktualizuje właściwość {{PropertyView/pl|Mapa widoczności}} pośrednika płaszczyzny roboczej z aktualnym stanem widoczności obiektów w dokumencie.



## Menu kontekstowe okna widoku 3D 

W menu kontekstowym okna [widoku 3D](3D_view/pl.md) dostępne są następujące dodatkowe opcje:



### Opcje domyślne 

Jeśli istnieje aktywny dokument, menu kontekstowe zawiera jedno dodatkowe menu podrzędne:

-   Narzędzia: podzbiór narzędzi dostępnych w głównym menu Narzędzia Rysunku Roboczego.



### Opcje tekstu 

Zobacz akapit [Opcje tekstu](#Opcje_tekstu.md).



## Narzędzia przestarzałe 

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Utwórz szyk](Draft_Array/pl.md): tworzy ortogonalną tablicę z wybranego obiektu. Utworzona tablica może zostać przekształcona w [szyk biegunowy](Draft_PolarArray/pl.md) lub [szyk kołowy](Draft_CircularArray/pl.md) poprzez zmianę jej właściwości {{PropertyData/pl|Typ szyku}}. Niedostępne {{VersionPlus/pl|0.21}}.

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Projekt rysunku](Draft_Drawing/pl.md): wstawia widoki obiektów na stronie środowiska [Rysunek Roboczy](Drawing_Workbench/pl.md). Niedostępne {{VersionPlus/pl|0.21}}.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Przełącz tryb kontynuacji](Draft_ToggleContinueMode/pl.md): włącza lub wyłącza tryb kontynuacji. Nie dostępne w {{VersionPlus/pl|1.0}}.



## Ustawienia

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Ustawienia](Draft_Preferences/pl.md): ogólne ustawienia dla środowiska pracy Rysunek Roboczy.

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md): Ustawienia dostępne dla importu i eksportu do różnych formatów plików.



### Formaty plików 

Środowisko pracy Rysunek Roboczy dostarcza programowi FreeCAD narzędzia do importu i eksportu dla kilku formatów plików. Są one używane przez polecenia [Import](Std_Import/pl.md) i [Eksport](Std_Export/pl.md).

-   [Autodesk .DXF](Draft_DXF/pl.md): Import i eksport plików [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) utworzonych za pomocą aplikacji 2D CAD. Zobacz również [FreeCAD i import DXF](FreeCAD_and_DXF_Import/pl.md).
-   [Autodesk .DWG](Draft_DXF/pl.md): Import i eksport plików DWG przez zewnętrzny konwerter DXF. Zobacz również [FreeCAD i import DWG](FreeCAD_and_DWG_Import/pl.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG/pl.md): Import i eksport plików [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) utworzonych za pomocą aplikacji do rysowania wektorowego.
-   [Open Cad format .OCA](Draft_OCA/pl.md): Import i eksport plików [OCA/GCAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/pl.md): Import plików DAT opisujących profil Airfoil.



## Testy jednostkowe 

Zobacz również: [Środowisko pracy Test](Testing/pl.md)

Aby przeprowadzić testy jednostek w środowisku pracy, należy wykonać następujące czynności z terminala systemu operacyjnego:


```python
freecad -t TestDraft
```



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Środowisko pracy zawiera moduł do tworzenia przykładów wszystkich obiektów w nowym dokumencie.

Użyj tego, aby sprawdzić, czy wszystkie obiekty są prawidłowo utworzone:


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Sprawdzenie kodu tego modułu jest pomocne, aby zrozumieć interfejs programowania.



## Poradniki

-   [Poradnik dla Środowiska pracy Draft](Draft_tutorial/pl.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Draft](Category_Draft.md) > Draft Workbench/pl
