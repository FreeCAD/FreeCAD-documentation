# <img alt="Ikonka FreeCAD dla Środowiska pracy Rysunek Roboczy" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **Rysunek Roboczy** skupia się przede wszystkim na tworzeniu i modyfikacji obiektów 2D w programie FreeCAD. Nie jest jednak ograniczone do płaszczyzny XY globalnego układu współrzędnych. Jego obiekty mogą mieć dowolną orientację i położenie w przestrzeni, a niektóre obiekty Rysunku Roboczego mogą być zarówno płaskie jak i przestrzenne.

Obiekty Rysunku Roboczego mogą być używane do ogólnego szkicowania, podobnie jak w programie Inkscape lub AutoCAD. Ale mogą one również stanowić podstawę do tworzenia obiektów 3D w innych środowiskach pracy. A [polilinia](Draft_Wire/pl.md) może zdefiniować ścieżkę dla [ściany](Arch_Wall/pl.md) środowiska Architektura, [wielokąt](Draft_Polygon/pl.md) środowiska Rysunek Roboczy może być wciągany za pomocą funkcji [wyciągnięcia](Part_Extrude/pl.md) środowiska Część, itd. Wiele z [narzędzi modyfikujących](#Modyfikacja.md) środowiska pracy Rysunek Roboczy może być zastosowanych do obiektów płaskich oraz przestrzennych stworzonych za pomocą innych środowisk pracy. Możesz, na przykład, [przesunąć](Draft_Move/pl.md) [szkic](Sketcher_Workbench/pl.md) lub stworzyć [szyk ortogonalny](Draft_OrthoArray/pl.md) z obiektu [Części](Part_Workbench/pl.md).

Środowisko pracy Rysunek Roboczy dostarcza również narzędzi do definiowania [płaszczyzny roboczej](Draft_SelectPlane/pl.md), [siatki](Draft_Snap_Grid/pl.md) oraz [systemu przyciągania](Draft_Snap/pl.md) do precyzyjnego sterowania położeniem geometrii.

Jeśli Twoim głównym celem jest tworzenie złożonych rysunków 2D i plików [DXF](DXF/pl.md), a nie potrzebujesz modelowania 3D, FreeCAD może nie być właściwym wyborem dla Ciebie. Możesz rozważyć zastosowanie dedykowanego programu do tworzenia projektów technicznych, takiego jak [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), lub innego.

![](images/Draft_Workbench_Example.png ) 
*Obrazek przedstawia [siatkę](Draft_Snap_Grid/pl.md) wyrównaną do płaszczyzny XY.<br>
Po lewej stronie, na biało, kilka obiektów planarnych.<br>
Po prawej nieplanarny obiekt [polilinii](Draft_Wire/pl.md) użyty jako obiekt ścieżki w [wyciąganiu pop ścieżce](Draft_PathArray/pl.md).*

## Kreślenie

-   Polecenie <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linia](Draft_Line.md): tworzy linię prostą.

-   Polecenie <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinia](Draft_Wire/pl.md): tworzy polilinię, czyli sekwencję kilku połączonych segmentów linii.

-   Polecenie <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> _. {{Version/pl|0.19}}

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> Narzędzia łuku

:\* Polecenie <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Łuk](Draft_Arc/pl.md): tworzy łuk kołowy z punktu środka, promienia, kąta początkowego i kąta rozwarcia.

:\* Polecenie <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Łuk przez trzy punkty](Draft_Arc_3Points/pl.md): tworzy łuk okręgu z trzech punktów, które definiują jego obwód. {{Version/pl|0.19}}

-   Polecenie <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Okrąg](Draft_Circle/pl.md): tworzy okrąg na podstawie środka i promienia.

-   Polecenie <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipsa](Draft_Ellipse/pl.md): tworzy elipsę z dwóch punktów definiujących prostokąt, w którym elipsa będzie dopasowana.

-   Polecenie <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Prostokąt](Draft_Rectangle/pl.md): tworzy prostokąt z dwóch punktów.

-   Polecenie <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Wielokąt](Draft_Polygon/pl.md): tworzy wielokąt foremny o zadanym punkcie środkowym i promieniu.

-   Polecenie <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [Krzywa złożona](Draft_BSpline/pl.md): tworzy krzywą złożoną z kilku punktów.

-   Komponent <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> narzędzia Bézier\'a

:\* Polecenie <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Sześcienna krzywa Beziera](Draft_CubicBezCurve/pl.md): tworzy krzywą Béziera trzeciego stopnia. {{Version/pl|0.19}}

:\* Polecenie <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Krzywa Bezier\'a](Draft_BezCurve/pl.md): tworzy krzywą Béziera z kilku punktów.

-   Polecenie <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/pl.md): tworzy zwykły punkt.

-   Polecenie <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Łącznik kształtów](Draft_Facebinder/pl.md): tworzy obiekt powierzchni z wybranych ścian.

-   Polecenie <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Kształt z tekstu](Draft_ShapeString/pl.md): tworzy kształt złożony, który reprezentuje ciąg tekstowy.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Kreskowanie](Draft_Hatch/pl.md): tworzy kreskowanie na powierzchniach wybranego obiektu. {{Version/pl|0.20}}

## Adnotacja

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Adnotacja wieloliniowa](Draft_Text/pl.md): tworzy wielowierszowy obiekt tekstu w zadanym punkcie.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Wymiarowanie](Draft_Dimension/pl.md): tworzy wymiar liniowy, wymiar kątowy lub wymiar promieniowy.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etykieta](Draft_Label/pl.md): tworzy tekst wielowierszowy z dwu-segmentową linią wiodącą i strzałką.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md): pozwala zdefiniować style, które wpływają na właściwości wizualne obiektów związanych z adnotacjami. {{Version/pl|0.19}}

## Modyfikacja

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Przesuń](Draft_Move/pl.md): przesuwa lub kopiuje wybrane obiekty z jednego punktu do drugiego.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Obróć](Draft_Rotate/pl.md): obraca lub kopiuje wybrane obiekty wokół punktu środka o zadany kąt.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skaluj](Draft_Scale/pl.md): skaluje lub kopiuje wybrane obiekty wokół punktu bazowego.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Odbicie lustrzane](Draft_Mirror/pl.md): tworzy kopie w odbiciu lustrzanym z wybranych obiektów.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Odsunięcie](Draft_Offset/pl.md): odsuwa każdy segment wybranego obiektu o zadaną odległość lub tworzy przesuniętą kopię wybranego obiektu.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Przytnij](Draft_Trimex/pl.md): przycina lub wydłuża wybrany obiekt.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Rozciągnij](Draft_Stretch/pl.md): rozciąga obiekty poprzez przesuwanie wybranych punktów.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klonuj](Draft_Clone/pl.md): tworzy połączone kopie, klony, wybranych obiektów.

-   Komponent <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> Narzędzia szyku

:\* <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> _. {{Version/pl|0.19}}

:\* <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> _. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> _. {{Version/pl|0.19}}

:\* <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Szyk po ścieżce](Draft_PathArray/pl.md): tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż ścieżki.

:\* <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> _ zamiast zwykłego szyku. {{Version/pl|0.19}}

:\* <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Szyk z punktów](Draft_PointArray/pl.md): tworzy szyk z wybranego obiektu poprzez umieszczenie kopii w punktach ze zbioru punktów.

:\* <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> _ zamiast zwykłego szyku. {{Version/pl|0.19}}

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edycja](Draft_Edit/pl.md): umieszcza wybrane obiekty w trybie edycji szkicu. W tym trybie właściwości obiektów mogą być edytowane graficznie.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Podświetl element podrzędny](Draft_SubelementHighlight/pl.md): tymczasowo podświetla wybrane obiekty lub obiekty bazowe wybranych obiektów.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> _ oraz [Polilinies](Draft_Wire/pl.md) w pojedynczą polilinę.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> _ lub [polilinie](Draft_Wire/pl.md) w określonym punkcie lub krawędzi.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Ulepsz kształt](Draft_Upgrade/pl.md): aktualizuje wybrane obiekty.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rozbij obiekt na elementy](Draft_Downgrade/pl.md): powoduje redukcję stopnia zaawansowania wybranych obiektów.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> _ na [krzywą złożoną](Draft_BSpline/pl.md) i vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> _ na [szkics](Sketcher_NewSketch/pl.md) środowiska Szkicownik, oraz vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> _ lub [polilinii](Draft_Wire/pl.md) poprzez zwiększenie lub zmniejszenie współrzędnej Z, dla wszystkich punktów po pierwszym.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> _ o 180° wokół linii wymiaru.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Widok 2D kształtu](Draft_Shape2DView/pl.md): tworzy rzuty 2D z wybranych obiektów.

## Pasek narzędzi Draft: Tray 

Pasek narzędzi zasobnika środowiska [Rysunek Roboczy](Draft_Tray/pl.md) pojawia się po uruchomieniu stołu warsztatowego i umożliwia wybór płaszczyzny roboczej, wraz z niektórymi właściwościami wizualnymi, takimi jak kolor linii, kolor kształtu, szerokość linii, rozmiar tekstu oraz grupa automatyczna.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Bieżąca płaszczyzna robocza](Draft_SelectPlane/pl.md): wybiera bieżącą płaszczyznę roboczą Rysunku Roboczego. Funkcja dostępna jest również w menu: **Narzędzia → <img src="images/Draft_SelectPlane.svg" width=16px> Wybierz płaszczyznę**.

-   ![](images/Draft_tray_button_style.png ) [Ustaw styl](Draft_SetStyle/pl.md): ustawia domyślny styl dla nowych obiektów. Dostępne również w menu: **Rysunek Roboczy → Narzędzia → <img src="images/Draft_SetStyle.svg" width=16px> Ustaw styl**. {{Version/pl|0.19}}

-   ![](images/Draft_tray_button_construction.png ) [Przełącz tryb konstrukcyjny](Draft_ToggleConstructionMode/pl.md): włącza lub wyłącza tryb konstrukcji szkicu. Dostępne również w menu: **Rysunek Roboczy → Narzędzia → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Przełącz tryb konstrukcyjny**.

-   !_ lub, opcjonalnie, aktywną [grupę](Std_Group/pl.md) lub grupę obiektów [architektury](Arch_Workbench/pl.md).

## Widżet skali adnotacji 

Za pomocą widżetu [skali anotacji](Draft_annotation_scale_widget/pl.md) można określić skalę adnotacji. Widżet ten znajduje się na [paseku statusu](Status_bar/pl.md).

![](images/Draft_annotation_scale_widget_button.png )

## Widżet przyciągania 

Widżet _. {{Version/pl|0.19}}

![](images/Draft_snap_widget_button.png )

## Pasek narzędzi Rysunek roboczy: Przyciągnij 

Pasek narzędzi [Rysunek roboczy: Przyciągnij](Draft_Snap/pl.md) umożliwia wybranie bieżącego trybu przyciągania. Jego przycisk pozostaje wciśnięty, gdy tryb jest aktywny.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> _ obiektów na włączone lub wyłączone.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Punkt końcowy](Draft_Snap_Endpoint/pl.md): przyciąga do punktów końcowych odcinków lub krawędzi.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Punkt środkowy](Draft_Snap_Midpoint/pl.md): przyciąga do punktu środkowego linii i odcinków łuku.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> _ i [Arch BuildingParts](Arch_BuildingPart/pl.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Kąt](Draft_Snap_Angle.md): przyciąga do specjalnych punktów odniesienia kół i łuków, przy wielokrotnościach 30° i 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Przecięcie](Draft_Snap_Intersection/pl.md): przyciąga do przecięcia dwóch krawędzi.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Prostopadle](Draft_Snap_Perpendicular/pl.md): przyciąga prostopadle w punkcie prostopadłym na krawędziach.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Rozszerzenie](Draft_Snap_Extension/pl.md): przyciąga do umownej linii, która rozciąga się poza punkty końcowe segmentów linii.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Równolegle](Draft_Snap_Parallel/pl.md): przyciąga do umownej linii równoległej do odcinka linii.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Specjalne](Draft_Snap_Special/pl.md): przyciąga na punktach specjalnych zdefiniowanych przez obiekt.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Najbliższy](Draft_Snap_Near/pl.md): przyciąga do najbliższego punktu lub krawędzi najbliższego obiektu.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortogonalnie](Draft_Snap_Ortho/pl.md): przyciąga na umownych liniach, które przecinają ostatni punkt pod kątem 0°, 45° i 90°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Siatka](Draft_Snap_Grid/pl.md): przyciąga na przecięciach linii siatki.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Wymiary](Draft_Snap_Dimensions/pl.md): prezentuje tymczasowe wymiary X i Y podczas przyciągania.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md): włącza lub wyłącza widoczność siatki.

### Pasek narzędzi użytkowych 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> _ środowiska Rysunek Roboczy. {{Version/pl|0.19}}

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> _ i przenosi wybrane obiekty do tej grupy. {{Version/pl|0.20}}

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> _. Może również usuwać grupy obiektów.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> _, [Grupy](Std_Group/pl.md) lub obiektów zbliżone do grupy [Architektury](Arch_Workbench/pl.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Przełącz tryb wyświetlania](Draft_ToggleDisplayMode/pl.md): przełącza {{PropertyView/pl|Tryb wyświatlania}} właściwości wybranych obiektów pomiędzy {{Value|cieniowany z krawędziami}} oraz {{Value|szkielet}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> _.

## Dodatkowe narzędzia 

Menu środowiska Rysunek Roboczy **Narzędzia** zawiera kilka narzędzi. Większość z nich jest dostępna również z pasków narzędziowych i została już wymieniona powyżej. W przypadku poniższych narzędzi nie jest to regułą.

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Zastosuj bieżący styl](Draft_ApplyStyle/pl.md): stosuje bieżące ustawienia stylu do wybranych obiektów.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Uleczenie](Draft_Heal/pl.md): leczy problematyczne obiekty Rysunku Roboczego znajdujące się w bardzo starych plikach.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Przełącz tryb kontynuacji](Draft_ToggleContinueMode/pl.md): włącza lub wyłącza tryb kontynuacji.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> _.

## Dodatkowe właściwości 

-   _, na której można budować swoje kształty.
-   [Przyciąganie](Draft_Snap/pl.md): Pozwala wybierać dokładne punkty geometryczne na, lub zdefiniowane przez, istniejące obiekty lub siatkę.
-   [Wiązania](Draft_Constrain/pl.md): Dla każdego kolejnego punktu można ograniczyć ruch kursora do kierunku X, Y lub Z.
-   [Tryb konstrukcji](Draft_ToggleConstructionMode/pl.md): Umieszcza nowe obiekty Rysunku Roboczego w dedykowanej grupie, ułatwiając ich ukrywanie lub usuwanie.
-   [Wzór](Draft_Pattern/pl.md): Obiekty Rysunku Roboczego z właściwością {{PropertyData/pl|Utwórz ścianę}} mogą wyświetlać wzór SVG zamiast jednolitego koloru ściany.

## Menu kontekstowe widoku drzewa 

W menu kontekstowym [Widoku drzewa](Tree_view/pl.md) dostępne są następujące dodatkowe opcje:

### Opcje domyślne 

Jeśli istnieje aktywny dokument, menu kontekstowe zawiera jedno dodatkowe podmenu:

-    **Narzędzia**: podzbiór narzędzi dostępnych w głównym menu Narzędzia Rysunku Roboczego.

### Opcje polilinii 

Ta dodatkowa opcja jest dostępna dla [polilinii](Draft_Wire/pl.md), [linii złożonej](Draft_BSpline/pl.md), [sześciennej krzywej Beziera](Draft_CubicBezCurve/pl.md) i [krzywej Beziera](Draft_BezCurve/pl.md):

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Spłaszcz tą polilinię: spłaszcza polilinię na podstawie jej wewnętrznej geometrii. Ta opcja obecnie nie działa poprawnie.

### Opcje kontenera warstw 

Dla narzędzi [Kontenera warstw](Draft_Layer/pl.md) dostępne są te dodatkowe opcje:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Scal duplikaty warstw: ta opcja obecnie nie działa.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Warstwa](Draft_Layer/pl.md): dodaje nową warstwę do bieżącego dokumentu.

### Opcje warstw 

Dla narzędzi [Warstw](Draft_Layer/pl.md) dostępne są te dodatkowe opcje:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Grupowanie automatyczne](Draft_AutoGroup/pl.md): aktywuje wybraną warstwę.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Wybierz grupę](Draft_SelectGroup/pl.md): zaznacza obiekty znajdujące się wewnątrz wybranej warstwy.

### Opcje tymczasowej płaszczyzny roboczej 

Dla narzędzi [Pośredniej płaszczyzny roboczej](Draft_WorkingPlaneProxy/pl.md) dostępne są te dodatkowe opcje:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Zapisz stan obiektów](Draft_WorkingPlaneProxy/pl#Menu_podr.C4.99czne.md): aktualizuje właściwość {{PropertyView/pl|Mapa widoczności}} pośrednika płaszczyzny roboczej z aktualnym stanem widoczności obiektów w dokumencie.

## Menu kontekstowe okna widoku 3D 

W menu kontekstowym okna [widoku 3D](3D_view/pl.md) dostępne są następujące dodatkowe opcje:

### Opcje domyślne 

Jeśli istnieje aktywny dokument, menu kontekstowe zawiera jedno dodatkowe podmenu:

-    **Narzędzia**: podzbiór narzędzi dostępnych w głównym menu Narzędzia Rysunku Roboczego.

## Narzędzia przestarzałe 

Polecenia te są przestarzałe, ale nadal dostępne.

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> _ lub [szyk kołowy](Draft_CircularArray/pl.md) poprzez zmianę jej właściwości {{PropertyData/pl|Typ szyku}}. {{Obsolete/pl|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> _. {{Obsolete/pl|0.17}}

## Ustawienia

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Ustawienia](Draft_Preferences/pl.md): ogólne ustawienia dla środowiska pracy Rysunek Roboczy.

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md): Ustawienia dostępne dla importu i eksportu do różnych formatów plików.

### Formaty plików 

Środowisko pracy Rysunek Roboczy dostarcza programowi FreeCAD narzędzia do importu i eksportu dla kilku formatów plików. Są one używane przez polecenia [Import](Std_Import/pl.md) i [Eksport](Std_Export/pl.md).

-   _.
-   _. Zobacz również [FreeCAD i import DWG](FreeCAD_and_DWG_Import/pl.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG/pl.md): Import i eksport plików [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) utworzonych za pomocą aplikacji do rysowania wektorowego.
-   [Open Cad format .OCA](Draft_OCA/pl.md): Import i eksport plików [OCA/GCAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/pl.md): Import plików DAT opisujących profil Airfoil.

## Test jednostek 

Zobacz również: [Środowisko pracy Test](Testing/pl.md)

Aby przeprowadzić testy jednostek w środowisku pracy, należy wykonać następujące czynności z terminala systemu operacyjnego:


```python
freecad -t TestDraft
```

## Tworzenie skryptów 

Zobacz również stronę: _.

Środowisko pracy zawiera moduł do tworzenia przykładów wszystkich obiektów w nowym dokumencie. {{Version/pl|0.19}}

Użyj tego, aby sprawdzić, czy wszystkie obiekty są prawidłowo utworzone:


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Sprawdzenie kodu tego modułu jest pomocne, aby zrozumieć interfejs programowania.

## Poradniki

-   [Poradnik dla Środowiska pracy Draft](Draft_tutorial/pl.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)





 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Draft Workbench/pl
