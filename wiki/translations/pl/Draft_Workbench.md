


 

<img alt="Ikonka FreeCAD dla Środowiska pracy Rysunek roboczy" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Rysunek roboczy](Draft_Workbench/pl.md) umożliwia rysowanie prostych obiektów 2D i oferuje kilka narzędzi do ich późniejszej modyfikacji. Dostarcza również narzędzi do definiowania płaszczyzny roboczej, siatki i systemu zatrzasków/wiązań do precyzyjnej kontroli położenia geometrii.

Utworzone obiekty 2D mogą być wykorzystywane do sporządzania ogólnych szkiców w sposób podobny jak w przypadku Inkscape\'a lub Autocada. Te kształty 2D mogą być również wykorzystywane jako podstawowe komponenty obiektów 3D tworzonych z innymi Środowiskami pracy, na przykład <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Część](Part_Workbench/pl.md) i <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Architektura](Arch_Workbench/pl.md). Możliwa jest również konwersja obiektów roboczych na <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [szkice](Sketcher_Workbench/pl.md), co oznacza, że kształty mogą być również używane w Środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Projekt części](PartDesign_Workbench/pl.md) do tworzenia brył.

FreeCAD jest przede wszystkim aplikacją do modelowania 3D, a zatem jego narzędzia 2D nie są tak zaawansowane jak w innych programach do rysowania. Jeśli Twoim głównym celem jest tworzenie złożonych rysunków 2D i plików [DXF](DXF/pl.md), a nie potrzebujesz modelowania 3D, możesz rozważyć zastosowanie dedykowanego programu do tworzenia projektów technicznych, takiego jak [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), lub innego.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

### Obiekty rysunku 

Narzędzia do tworzenia obiektów.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Dwupunktowa linia](Draft_Line/pl.md): Rysuje odcinek pomiędzy dwoma punktami
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [wielopunktowa linia (Polilinia)](Draft_Wire/pl.md): Rysuje łamaną składającą się z wielu odcinków (pomiędzy wieloma punktami)
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Fillet](Draft_Fillet.md): Rysuje zaokrąglenie *(zaokrąglony narożnik)* lub fazę *(prosta linia)* pomiędzy dwoma prostymi [Lines](Draft_Line.md). {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Łuk](Draft_Arc/pl.md): Rysuje łuk na bazie środka, promienia, kąta początkowego i kąta końcowego.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Łuk 3 Punkty](Draft_Arc_3Points.md): rysuje odcinek łuku okręgu z trzech punktów znajdujących się w obrębie obwodu. {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Elipa](Draft_Ellipse/pl.md): Rysuje elipsę na podstawie dwóch punktów narożnych.
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Okrąg](Draft_Circle/pl.md): Rysuje okrąg bazując na środku i promieniu.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Prostokąt](Draft_Rectangle/pl.md): Rysuje prostokąt na bazie dwóch przeciwległych punktów.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Wielokąt](Draft_Polygon.md): Rysuje wielokąt foremny na podstawie punktu centralnego i promienia.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline/pl.md): Rysuje obiekt B-Spline z serii punktów.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bezier Curve](Draft_CubicBezCurve.md): rysuje krzywą Beziera trzeciego stopnia, przeciągając dwa punkty. {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Krzywa Beziera](Draft_BezCurve/pl.md): Rysuje krzywą Beziera z serii punktów.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point.md): Wstawia obiekt typu punkt.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Grupa powierzchnii](Draft_Facebinder/pl.md): Na istniejących obiektach z wybranych ścian tworzy nowy obiekt.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Ksztalt z tekstu](Draft_ShapeString/pl.md): Tworzy złożony kształt reprezentujący łańcuch tekstowy w danym punkcie.

## Obiekty z adnotacją 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Tekst](Draft_Text/pl.md): tworzy komentarz tekstowy w wielu wierszach.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Wymiar](Draft_Dimension/pl.md): tworzy adnotację zawierającą wymiary.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etykieta](Draft_Label/pl.md): umieszcza etykietę ze strzałką wskazującą na wybrany element. {{Version/pl|0.17}}
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Edytor stylów notatek](Draft_AnnotationStyleEditor/pl.md): otwiera edytor, aby zmienić styl tych obiektów. {{Version/pl|0.19}}

## Modyfikowanie obiektów 

Są to narzędzia do modyfikowania istniejących obiektów. Działają one na wybranych obiektach, ale jeśli żaden z nich nie zostanie wybrany, zostaniesz poproszony o jego wybranie.

Wiele narzędzi operacyjnych *(przesuwanie, obracanie, szyk itp.)* działa również na obiektach brył *([Część](Part_Workbench/pl.md), [Projekt części](PartDesign_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md), itp.)*.

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Przesuń](Draft_Move/pl.md): Przesuwa obiekty z jednego miejsca do drugiego.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Obróć](Draft_Rotate/pl.md): Obraca obiekty od kąta początkowego do końcowego.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skaluj](Draft_Scale/pl.md): Skaluje zaznaczone obiekty wokół punktu bazowego.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): Tworzy lustrzane odbicie wybranych obiektów.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Odsuń](Draft_Offset/pl.md): Przenosi segmenty obiektu o określoną odległość.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Przytnij/Wydłuż *(Trimex)*](Draft_Trimex/pl.md): Przycina lub wydłuża obiekt.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): Rozciąga wybrane obiekty. {{Version/pl|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): Powiela wybrany obiekt.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Narzędzia do tworzenia szyków.
-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Ortho Array](Draft_OrthoArray.md): tworzy tablicę ortogonalną z wybranego obiektu. Może również tworzyć kopie [App: Link](App_Link.md).{{Version/pl|0.19}}
-   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [PolarArray](Draft_PolarArray.md): Tworzy szyk w postaci przebiegu promieni polarnych, czyli w postaci przesunięcia kąta. {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [CircularArray](Draft_CircularArray.md): Tworzy tablicę w układzie kołowym, czyli zaczynając od środka i wychodząc promieniście na zewnątrz. Może również tworzyć kopie [App: Link](App_Link.md). {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path: Array](Draft_PathArray.md): Tworzy tablicę obiektów, umieszczając ich kopie na trasie przejścia.
-   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path: LinkArray](Draft_PathLinkArray.md): podobnie jak <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path: Array](Draft_PathArray.md) ale tworzy [App: Links](App_Link.md) zamiast zwykłych kopii. {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point: Array](Draft_PointArray.md): Tworzy tablicę obiektów, umieszczając kopie w określonych miejscach. {{Version/pl|0.18}}
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point LinkArray](Draft_PointLinkArray.md): podobnie jak <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point: Array](Draft_PointArray.md), ale tworzy [App: Links](App_Link.md) zamiast zwykłych kopii. {{Version/pl|0.19}}

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edycja](Draft_Edit/pl.md): Edycja wybranego obiektu.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): wchodzi w tryb edycji, który umożliwia edycję różnych obiektów. {{Version/pl|0.19}}

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Połącz](Draft_Join.md): Łączy linie w jeden ciąg. {{Version/pl|0.18}}
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Podziel](Draft_Split.md): Podzieli ciąg w danym punkcie, na części. {{Version/pl|0.18}}
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade/pl.md): Łączy obiekty do obiektu wyższego poziomu.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade/pl.md): Rozbija obiekt na obiekty niższego poziomu.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Zapisz w formie BSpline](Draft_WireToBSpline.md): Przekształca ciąg linii w linię BSpline i odwrotnie.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): konwertuje obiekt Draft na szkic Środowiska pracy [Sketcher](Sketcher_Workbench.md) i odwrotnie.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope.md): zmienia nachylenie elewacji aktualnie wybranego obiektu [Draft: Linia](Draft_Line.md) lub [Draft: Linia łamana](Draft_Wire.md). {{Version/pl|0.17}}
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip Dimension](Draft_FlipDimension.md): odwraca orientację tekstu obiektu [Draft: Wymiar](Draft_Dimension.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): tworzy obiekt 2D, który jest spłaszczonym widokiem obiektu przestrzennego.

## Pasek narzędzi Draft: Tray 

Pasek narzędzi zasobnika środowiska [Rysunek Roboczy](Draft_Tray/pl.md) pojawia się po uruchomieniu stołu warsztatowego i umożliwia wybór płaszczyzny roboczej, wraz z niektórymi właściwościami wizualnymi, takimi jak kolor linii, kolor kształtu, szerokość linii, rozmiar tekstu oraz grupa automatyczna.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Ustaw płaszczyznę roboczą](Draft_SelectPlane.md): ustawia płaszczyznę roboczą z widoku standardowego lub wybranej powierzchni.
-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Ustaw styl](Draft_SetStyle/pl.md): ustawia domyślny styl dla nowych obiektów i opcjonalnie stosuje ten styl do wybranych obiektów i grup.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Przełączanie trybu konstrukcyjnego](Draft_ToggleConstructionMode.md): włącza lub wyłącza tryb konstrukcji szkicu.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): automatycznie umieszcza nowe obiekty w danej <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Grupie Std](Std_Group.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [ warstwie Draft](Draft_Layer.md), lub jednym z grupopodobnych obiektów Środowiska pracy [Arch](Arch_Workbench/pl.md) jak <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch BuildingPart](Arch_BuildingPart.md).. {{Version/pl|0.17}}

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Widżet skali adnotacji 

Za pomocą widżetu [skali anotacji](Draft_annotation_scale_widget/pl.md) można określić skalę adnotacji. Widżet ten znajduje się na [paseku statusu](Status_bar/pl.md).

![](images/Draft_annotation_scale_widget_button.png )

## Widżet przyciągania 

Widżet [przyciągania](Draft_snap_widget/pl.md) może być używany jako alternatywa dla [paska narzędzi przyciągania](#Pasek_narz.C4.99dzi_Rysunek_roboczy:_Przyci.C4.85gnij.md). Widżet ten znajduje się na [pasku statusu](Status_bar/pl.md).

![](images/Draft_snap_widget_button.png )

## Pasek narzędzi Rysunek roboczy: Przyciągnij 

Pasek narzędzi [Rysunek roboczy: Przyciągnij](Draft_Snap/pl.md) umożliwia wybranie bieżącego trybu przyciągania. Jego przycisk pozostaje wciśnięty, gdy tryb jest aktywny.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md): przełącza globalnie [przyciąganie obiektów](Draft_Snap/pl.md) na włączone lub wyłączone.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Punkt końcowy](Draft_Snap_Endpoint/pl.md): Przyciąga do punktów końcowych odcinków linii, łuku i splajnu.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Punkt środkowy](Draft_Snap_Midpoint/pl.md): Przyciąga do punktu środkowego linii i odcinków łuku.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Środek](Draft_Snap_Center/pl.md): Przyciąga do środkowego punktu okręgów i ścian, [Pośrednik płaszczyzny roboczej](Draft_WorkingPlaneProxy/pl.md) oraz [Część budowli](Arch_BuildingPart/pl.md)
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Kąt](Draft_Snap_Angle/pl.md): Przyciąga do specjalnych punktów odniesienia kół i łuków, pod kątem 45° i 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Przecięcie](Draft_Snap_Intersection/pl.md): Przyciąga do przecięcia dwóch odcinków linii lub łuku. Najedź kursorem myszki na dwa pożądane obiekty, aby aktywować przyciąganie ich przecięcia.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Prostopadle](Draft_Snap_Perpendicular/pl.md): Na odcinkach linii i łuku, przyciąga prostopadle do ostatniego punktu.
-   <img alt="" src=images/Draft_Snap_Extension.png  style="width:32px;"> [Rozszerzenie](Draft_Snap_Extension/pl.md): Przyciąga do umownej linii, która rozciąga się poza punkty końcowe segmentów linii. Aby uaktywnić przyciąganie rozszerzenia, należy najechać myszką na żądany obiekt.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Równolegle](Draft_Snap_Parallel/pl.md): Przyciąga do umownej linii równoległej do odcinka linii. Przesuń kursor myszy nad żądanym obiektem, aby aktywować jego przyciągnięcie równoległe.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Specjalne](Draft_Snap_Special/pl.md): Przyciąga na punktach specjalnych zdefiniowanych przez obiekt. {{Version/pl|0.17}}
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Najbliższy](Draft_Snap_Near/pl.md): Przyciąga do najbliższego punktu lub krawędzi najbliższego obiektu.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Snap_Ortho/pl.md): Przyciąga na umownych liniach, które przecinają ostatni punkt i dochodzą pod kątem 0°, 45° i 90°.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Siatka](Draft_ToggleGrid.md): Przyciąga na przecięciach linii siatki, jeśli siatka jest widoczna.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Płaszczyzna robocza](Draft_Snap_WorkingPlane/pl.md): Zawsze umieszcza przyciągany punkt na aktualnej [płaszczyźnie roboczej](Draft_SelectPlane.md), nawet jeśli przyciągany punkt znajduje się poza tą płaszczyzną roboczą.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Wymiary](Draft_Snap_Dimensions/pl.md): Prezentuje tymczasowe wymiary X i Y podczas przyciągania.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Przełącz widoczność siatki](Draft_Snap_Grid/pl.md): włącza lub wyłącza widoczność siatki.

### Pasek narzędzi użytkowych 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Warstwa](Draft_Layer/pl.md): tworzy warstwę w bieżącym dokumencie, do której można dodawać obiekty w celu kontrolowania widoczności i koloru obiektu. {{Version/pl|0.19}}
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Pośrednik płaszczyzny rboczej](Draft_WorkingPlaneProxy/pl.md): utworzyć obiekt zastępczy do przechowywania aktualnej pozycji [Planu roboczego](Draft_SelectPlane/pl.md). {{Version/pl|0.17}}
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Przełącz tryb wyświetlania](Draft_ToggleDisplayMode/pl.md): przełącza tryb wyświetlania wybranych obiektów pomiędzy *Flat Lines* i *szkielet*..
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Dodaj do grupy](Draft_AddToGroup/pl.md): szybko dodaje wybrane obiekty do istniejącej [grupy Std](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Wybierz zawartość grupy](Draft_SelectGroup.md): wybiera zawartość wybranej [grupy Std](Std_Group.md) lub [warstwy](Draft_Layer/pl.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Dodaj do grupy konstrukcyjnej](Draft_AddConstruction/pl.md): Dodaj wybrane obiekty do grupy konstrukcyjnej. {{Version/pl|0.17}}
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Napraw](Draft_Heal/pl.md): naprawia problematyczne obiekty Draft znalezione w bardzo starych dokumentach.

## Dodatkowe narzędzia 

Menu środowiska Rysunek Roboczy **Narzędzia** zawiera kilka narzędzi. Większość z nich jest dostępna również z pasków narzędziowych i została już wymieniona powyżej. W przypadku poniższych narzędzi nie jest to regułą.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Przełącz tryb kontynuacji](Draft_ToggleContinueMode/pl.md): włącza lub wyłącza tryb kontynuacji szkicu.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Zastosuj aktualny styl](Draft_ApplyStyle/pl.md): stosuje aktualny styl do wybranych obiektów i grup.
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Pokaż przybornik przyciągania](Draft_ShowSnapBar/pl.md): Pokazuje pasek narzędzi [przyciągania](Draft_Snap/pl.md).

## Dodatkowe właściwości 

-   [Constraining](Draft_Constrain.md): Ograniczenie ruchu kursora do ruchów poziomych lub pionowych względem poprzedniego punktu.
-   [Przyciąganie (Snapping)](Draft_Snap/pl.md): Pozwala umieszczać nowe punkty w specjalnych miejscach istniejących obiektów.
-   [Copy Mode](Draft_Copying.md): Wszystkie narzędzia modyfikacji mogą też modyfikować lub tworzyć zmodyfikowane kopie zaznaczonych obiektów.
    Przytrzymując klawisz **Alt** gdy obiekt jest modyfikowany, np. przesuwany lub obracany, tworzy kopię z chwilą puszczenia klawisza.
-   [Tryb konstrukcji](Draft_ToggleConstructionMode/pl.md): Pozwala na tworzenie geometrii oddzielonych od reszty poprzez proste włączanie i wyłączanie opcji.
-   [Working plane](Draft_SelectPlane.md): Umożliwia wybranie powierzchni, na której można budować swoje kształty.

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Narzędzia przestarzałe 

Polecenia te są przestarzałe, ale nadal dostępne.

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Utwórz szyk](Draft_Array/pl.md): tworzy tablicę polarną lub prostokątną z wybranych obiektów. {{Obsolete/pl|0.19}}
-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Projekt rysunku](Draft_Drawing/pl.md): zapisuje wybrane obiekty na stronie środowiska [Rysunek Roboczy](Drawing_Workbench/pl.md). {{Obsolete/pl|0.17}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Zamknij linię](Draft_CloseLine/pl.md): Kończy rysowanie aktualnego obiektu [Polilinia](Draft_Wire/pl.md) lub [Krzywa złożona](Draft_BSpline/pl.md), i zamyka go.
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Zakończ linię](Draft_FinishLine/pl.md): Kończy rysowanie aktualnego ciągu lub linii B-spline, bez zamykania go.
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Cofnij kreślenie linii](Draft_UndoLine/pl.md): Cofnie rysowanie ostatniego segmentu [polilinii](Draft_Wire/pl.md).

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Ustawienia

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Ustawienia](Draft_Preferences.md): ogólne ustawienia płaszczyzny roboczej i narzędzi do rysowania.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md): Ustawienia dostępne dla importu i eksportu do różnych formatów plików.

### Formaty plików 

Są to funkcje otwierania, importowania lub eksportowania innych formatów plików. Otworzenie spowoduje otwarcie nowego dokumentu z zawartością pliku, podczas gdy import doda zawartość pliku do bieżącego dokumentu. Eksport zapisuje wybrane obiekty do pliku. Jeśli nic nie zostanie zaznaczone, wszystkie obiekty zostaną wyeksportowane. Należy pamiętać, że celem modułu roboczego jest praca z obiektami 2D, więc te procedury importu skupiają się tylko na obiektach 2D i chociaż formaty DXF i OCA obsługują również definicje obiektów w przestrzeni 3D (obiekty niekoniecznie są płaskie), nie będą importować obiektów wolumetrycznych, takich jak siatki, powierzchnie 3D itp. Obecnie obsługiwane są formaty plików:

-   [Autodesk .DXF](Draft_DXF.md): Import i eksport plików [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) utworzonych za pomocą aplikacji 2D CAD. Zobacz również [FreeCAD i import DXF](FreeCAD_and_DXF_Import.md).
-   [Autodesk .DWG](Draft_DXF.md): Import i eksport plików DWG przez importer DXF, gdy jest zainstalowany [ODA Converter](Extra_python_modules#ODA_Converter_(previously_Teigha_Converter).md). Zobacz również [FreeCAD i import DWG](FreeCAD_and_DWG_Import.md).
-   [SVG](Draft_SVG.md): Import i eksport plików [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) utworzonych za pomocą aplikacji do rysowania wektorowego.
-   [Open Cad format .OCA](Draft_OCA.md): Import i eksport plików OCA/GCAD, jest to potencjalnie nowy [open CAD format plików](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT.md): Import plików DAT opisujących [profil Airfoil](http://www.ae.illinois.edu/m-selig/ads/coord_database.html).

### Instalacja importerów 

-   [FreeCAD, impoort formatu DWG](FreeCAD_and_DWG_Import.md): Importuje i eksportuje pliki DWG.
-   [FreeCAD, impoort formatu DXF](FreeCAD_and_DXF_Import.md): Importuje i eksportuje pliki DXF.

## Test jednostek 


**Zobacz również:**

[Środowisko pracy Test](Test_Workbench.md).

Aby przeprowadzić testy jednostek w Środowisku pracy, należy wykonać następujące czynności z terminala systemu operacyjnego. 
```python
freecad -t TestDraft
```

## Tworzenie skryptów 

Narzędzia Draft mogą być używane w [Makrach](macros.md) i z konsoli [Python](Python.md) przy użyciu [Draft API](Draft_API.md).

Środowisko pracy zawiera moduł do tworzenia przykładów wszystkich obiektów w nowym dokumencie. {{Version/pl|0.19}}

Użyj tego, aby sprawdzić, czy wszystkie obiekty są prawidłowo utworzone. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Sprawdzenie kodu tego modułu jest przydatne, aby zrozumieć, jak korzystać z interfejsu programowania. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Gdzie `$INSTALLDIR` jest katalogiem wyższego poziomu, w którym zainstalowano oprogramowanie; na przykład, w Linuksie może to być `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Obiekty testowe dla Środowiska pracy [Draft](Draft_Workbench.md).*

## Poradniki

-   [Poradnik dla Środowiska pracy Draft](Draft_tutorial/pl.md)
-   [Poradnik dla Środowiska pracy Draft przestarzały](Draft_tutorial_Outdated/pl.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
