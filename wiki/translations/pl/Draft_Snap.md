# Draft Snap/pl
{{TOCright}}



## Opis

W środowisku pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) i <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektura](Arch_Workbench/pl.md) możesz tworzyć geometrię przez wybieranie punktów w oknie [widoku 3D](3D_view/pl.md) lub przez wprowadzanie współrzędnych w poleceniach [panelu zadań](Task_panel/pl.md). Innym sposobem dokładnego wybierania punktów jest przyciąganie. Przyciąganie pozwala na wybranie dokładnych punktów geometrycznych na lub zdefiniowanych przez istniejące obiekty lub siatkę. Można na przykład przyciągnąć do punktu końcowego prostej, środka okręgu lub przecięcia dwóch krawędzi.

Przyciąganie jest dostępne z większością poleceń środowisk [Rysunek Roboczy](Draft_Workbench/pl.md) i [Architektura](Arch_Workbench/pl.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Przyciąganie do punktu końcowego krawędzi*



## Narzędzia przyciągania 

Narzędzia te są dostępne na pasku narzędzi *Rysunek Roboczy - Przyciąganie* oraz w [Widżet przyciągania](Draft_snap_widget/pl.md) środowiska Rysunek Roboczy.

Zauważ, że koliste krawędzie nie muszą być pełnymi okręgami.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Przełącz przyciąganie](Draft_Snap_Lock.md): przełącza globalnie [przyciąganie](Draft_Snap/pl.md) obiektów na włączone lub wyłączone.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Punkt końcowy](Draft_Snap_Endpoint/pl.md): Przyciąga do punktów końcowych odcinków linii, łuku i krzywej złożonej.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Punkt środkowy](Draft_Snap_Midpoint/pl.md): Przyciąga do punktu środkowego krawędzi.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Środek](Draft_Snap_Center.md): przyciąga do punktu środkowego powierzchni i krawędzi kołowych, a także do punktu {{PropertyData/pl|Umiejscowienia}} [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy/pl.md) i [Arch BuildingParts](Arch_BuildingPart/pl.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Kąt](Draft_Snap_Angle.md): Przyciąga do specjalnych punktów odniesienia kół i łuków, przy wielokrotnościach 30° i 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Przecięcie](Draft_Snap_Intersection.md): Przyciąga do przecięcia dwóch odcinków linii lub łuku. Najedź kursorem myszki na dwa pożądane obiekty, aby aktywować przyciąganie ich przecięcia.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Prostopadle](Draft_Snap_Perpendicular/pl.md): Na odcinkach linii i łuku, przyciąga prostopadle do ostatniego punktu ściany *({{Version/pl|0.21}})* oraz krawędzi.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Rozszerzenie](Draft_Snap_Extension/pl.md): Przyciąga do umownej linii, która rozciąga się poza punkty końcowe segmentów linii. Aby uaktywnić przyciąganie rozszerzenia, należy najechać myszką na żądany obiekt.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Równolegle](Draft_Snap_Parallel.md): Przyciąga do umownej linii równoległej do odcinka linii. Przesuń kursor myszy nad żądanym obiektem, aby aktywować jego przyciągnięcie równoległe.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Specjalne](Draft_Snap_Special/pl.md): Przyciąga na punktach specjalnych zdefiniowanych przez obiekt. {{Version/pl|0.17}}

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Najbliższy](Draft_Snap_Near/pl.md): Przyciąga do najbliższego punktu oraz krawędzi najbliższego obiektu.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortogonalnie](Draft_Snap_Ortho/pl.md): przyciąga na umownych liniach, które przecinają ostatni punkt pod wielokrotnością kąta 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Siatka](Draft_Snap_Grid/pl.md): Przyciąga na przecięciach linii siatki, jeśli siatka jest widoczna.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Płaszczyzna robocza](Draft_Snap_WorkingPlane/pl.md): zawsze umieszcza przyciągane punkty na aktualnej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Wymiary](Draft_Snap_Dimensions/pl.md): Prezentuje tymczasowe wymiary X i Y podczas przyciągania.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md): włącza lub wyłącza widoczność siatki.



## Przyciąganie zaawansowane 

-   Dodatkowe punkty przyciągania można uzyskać poprzez połączenie dwóch metod przyciągania, takich jak np [Ortho](Draft_Snap_Ortho/pl.md) i [Extension](Draft_Snap_Extension/pl.md), które dadzą Ci punkt przyciągania na przecięciu ich umownych linii.
-   Przyciąganie może być połączone z [wiązaniami](Draft_Constrain/pl.md).
-   Naciśnij **Q**, aby wstawić \"punkt zatrzaśnięcia\" w miejscu, w którym aktualnie znajduje się kursor myszki. Możesz przyciągać do osi ortogonalnych punktów zatrzaśnięcia, oraz do przecięć tych osi. Jeśli aktywna jest opcja [przyciągnij do środkowego](Draft_Snap_Midpoint/pl.md), możesz także przyciągnąć do punktu środkowego między dwoma punktami zatrzaśnięcia.
-   Naciśnij **** jeden lub więcej razy, aby przyciągnąć obiekt, który jest zasłonięty przez inną geometrię. Nazywa się to \"cyklicznym przyciąganiem\". Zauważ, że musisz przesunąć kursor o niewielką wartość w oknie [widoku 3D](3D_view/pl.md) po wciśnięciu klawisza.

![](images/Draft_Snap_example_cycling_1.png ) 
*Przyciąganie cykliczne 1: Czerwony prostokąt został utworzony jako pierwszy, dlatego ma on pierwszeństwo przyciągania. Bez cyklicznego przyciągania nie można przyciągnąć zielonego prostokąta, który jest nakładany na czerwony prostokąt.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Przyciąganie cykliczne 2: Po jednokrotnym użyciu klawisza cyklu przyciągania zielony prostokąt otrzymuje priorytet przyciągania. Możliwe jest teraz przyciąganie do punktu środkowego nałożonej zielonej krawędzi.*



## Uwagi

-   Wiele opcji przyciągania może być aktywnych w tym samym czasie, ale zaleca się, aby aktywować tylko te opcje, które są naprawdę potrzebne. Aktywowanie zbyt wielu może spowolnić działanie.
-   Nie jest dobrym pomysłem posiadanie na stałe aktywnej opcji [przyciągnij do najbliżeszgo](Draft_Snap_Near/pl.md), ponieważ ma ona pierwszeństwo przed wieloma innymi opcjami przyciągania.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

Należy pamiętać, że po zmianie niektórych preferencji należy ponownie uruchomić program FreeCAD.

-   Gdy aktywne jest środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md) wymagające wprowadzenia punktu, maksymalna odległość, przy której narzędzie [przyciągnij do siatki](Draft_Snap_Grid/pl.md) wykrywa przecięcia linii siatki, może być zmieniana w locie przez naciśnięcie klawisza **[** *(klawisz zwiększania)* lub klawisza **]** *(klawisz zmniejszania)*. To ustawienie jest zapisywane w: **Przybory → Edycja parametrów → BaseApp → Preferences → Mod → Draft → snapRange**. Można je również zmienić w panelu zadań polecenia [Wybór płaszczyzny](Draft_SelectPlane/pl.md).
-   Aby przyciągać tylko wtedy, gdy przytrzymany jest klawisz **modyfikator przyciągania**:
    -   Odznacz opcję: **Edycja → Preferencje → Rysunek Roboczy → Siatka i przyciąganie → Przyciąganie → Zawsze przyciągaj ''(wyłącz modyfikator przyciągania)''**.
    -   Domyślny klawisz **modyfikatora przyciągania**, **Ctrl**, można zmienić w opcji: **Edycja → Preferencje → Rysunek Roboczy → Siatka i przyciąganie → Przyciąganie → Modyfikator ograniczania**.
-   Aby pokazać pasek narzędzi Przyciągania tylko wtedy, gdy polecenie jest aktywne:
    -   Wybierz: **Edycja → Preferencje → Rysunek Roboczy→ Siatka i przyciąganie → Przyciąganie → Pokaż pasek narzędzi Przyciągania środowiska Rysunek Roboczy**.
    -   Wybierz: **Edycja → Preferencje → Rysunek Roboczy → Siatka i przyciąganie → Przyciąganie → Ukryj pasek narzędzi Przyciągania środowiska Rysunek Roboczy po użyciu**.
-   Symbole przyciągania można zmienić w: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia wyglądu → Styl symboli przyciągania**.
-   Kolor symboli przyciągania oraz rozmiar [Draft Snap Dimensions](Draft_Snap_Dimensions.md) można zmienić w: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia wyglądu → Kolor**
-   Wspomniane skróty klawiaturowe dla pojedynczych znaków można zmienić w: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia interfejsu użytkownika → Skróty klawiszowe**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/pl
