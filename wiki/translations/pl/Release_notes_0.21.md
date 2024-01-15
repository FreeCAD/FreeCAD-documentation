# Release notes 0.21/pl
**FreeCAD 0.21** został wydany *2 sierpnia 2023*, pobranie będzie możliwe ze strony [Download](Download/pl.md). Ta strona jest podsumowaniem najciekawszych zmian i funkcji.

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).

<img alt="" src=images/FreeCAD_relnotes_0.21.png  style="width:720px;">



## Informacje ogólne 

-   Domyślny schemat nazewnictwa plików kopii zapasowych to teraz **FCBak**. Starszy format (**FCStd#**) jest przestarzały i zostanie usunięty w przyszłej wersji. Użytkownicy z włączonym starym schematem będą ostrzegani podczas uruchamiania. [Pull request #9668](https://github.com/FreeCAD/FreeCAD/pull/9668).



## Interfejs użytkownika 

+++
| ![](images/Navi_Cube_relnotes_0.21.png ) | Zaktualizowano [Kostka nawigacyjna](Navigation_Cube/pl.md). Sześcian nie jest już wyświetlany w perspektywie, jeśli [Widok 3D](3D_view/pl.md) jest w trybie widoku prostokątnego. Narożne ściany stały się sześciokątne i większe, aby łatwiej było je kliknąć. Wokół przycisków dodano ramki. Poprawiono domyślny wybór i rozmiar czcionki. Menu minikostki zawiera teraz pole wyboru do przełączania ruchomości kostki. Dodano kilka nowych parametrów, zobacz stronę [Kostka nawigacyjna](Navigation_Cube/pl.md), aby uzyskać więcej informacji. |
|                                                                | [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876), [Pull request #8266](https://github.com/FreeCAD/FreeCAD/pull/8266), [Pull request #8646](https://github.com/FreeCAD/FreeCAD/pull/8646) i [Pull request #9356](https://github.com/FreeCAD/FreeCAD/pull/9356).                                                                                                                                                                                                                                                                                            |
+++

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.21.gif  style="width:384px;">Trwały przekrój przecinających się obiektów.Kliknij w obraz, aby zobaczyć animację. | Narzędzie [Wycinek z przekroju](Part_SectionCut/pl.md) umożliwia teraz wycięcie przecinających się obiektów. Jest to przydatne w przypadku złożeń, w których czasami nie można uniknąć przecięć stykających się obiektów ze względu na problemy numeryczne. |
|                                                                                                                                                                                                                        | [Pull request #8252](https://github.com/FreeCAD/FreeCAD/pull/8252).                                                                                                                                                                                                 |
+++

+++
| <img alt="" src=images/Measurement-Part_relnotes_0.21.png  style="width:384px;"> | Styl wyświetlania wyników [pomiarów](Part_Module/pl#Pomiary.md) utworzonych przy użyciu środowiska [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) może być teraz zmieniony w [preferencjach](PartDesign_Preferences/pl#Pomiary.md). [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148) |
+++

+++
| <img alt="" src=images/WbSelector_relnotes_0.21.png  style="width:384px;"> | Pole wyboru środowiska pracy może być teraz opcjonalnie umieszczone na pasku menu zamiast w obszarze paska narzędzi. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679) |
+++



### Kolejne ulepszenia interfejsu użytkownika 

-   Przyciski <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Drukuj](Std_Print/pl.md) oraz<img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Tryb Edycji](Std_UserEditMode/pl.md) zostały usunięty ze standardowego paska narzędzi. Może zostać ponownie dodany przez [dostosowanie](Std_DlgCustomize/pl.md) Twojego paska narzędzi. [Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570) oraz [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   Pasek narzędzi Plik został podzielony. Przyciski <img alt="" src=images/Std_Undo.svg  style="width:24px;"> [Cofnij](Std_Undo/pl.md), <img alt="" src=images/Std_Redo.svg  style="width:24px;"> [Ponów](Std_Redo/pl.md) and <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Odśwież](Std_Refresh/pl.md)

przeniesiono do nowego paska narzędzi Edycji. Przyciski <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Kopiuj](Std_Copy/pl.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Wklej](Std_Paste/pl.md) i <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Wytnij](Std_Cut/pl.md) zostały przeniesione do nowego paska narzędzi Schowka. Przycisk <img alt="" src=images/Std_WhatsThis.svg  style="width:24px;"> [Co to jest](Std_WhatsThis/pl.md) został przeniesiony do nowego paska narzędzi Pomoc. [Pull request #7620](https://github.com/FreeCAD/FreeCAD/pull/7620).

-   Dodano polecenia [Zachowaj widok](Std_StoreWorkingView/pl.md) i [Odtwórz widok](Std_RecallWorkingView/pl.md) dla tymczasowego widoku roboczego. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Zmiany wartości za pomocą kółka myszy w \"polach wejściowych\" *(typ widżetu używany do wprowadzania wartości w panelach zadań, na przykład przez [Linia](Draft_Line/pl.md) środowiska Rysunek Roboczy)* są wyłączone, jeśli widżet nie jest aktywny i przełącznik [ComboBoxWheelEventFilter](Fine-tuning/pl#Powiązane_z_myszką.md) jest włączony. Dzięki temu unikniemy niechcianych zmian wartości podczas przewijania, co już miało miejsce w przypadku pól typu spinner i combo. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Możliwe jest teraz ustawienie domyślnej przezroczystości dla nowych obiektów środowiska [Część](Part_Module/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) w [preferencjach](PartDesign_Preferences/pl.md). [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   Pojawił się nowy styl orbitalny Free Turntable. Można go włączyć w [ustawianiach](Preferences_Editor/pl#Nawigacja.md) lub naciskając przycisk **[<img src=images/NavigationCAD_dark.svg style="width:16px">** [Paska statusu](Status_bar/pl.md), a następnie korzystając z menu **Ustawienia → Technika orbitalna**. [Pull Request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Panel zadań [Wygląd zewnętrzny](Std_SetAppearance/pl.md) ma teraz także przycisk do ustawiania właściwości Kolor punktu. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   Dodano przycisk do przełączania kolorów gradientu tła okna [widoku 3D](3D_view/pl.md) w [Ustawieniach](Preferences_Editor/pl#Kolory.md). [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Wszystkie ustawienia przezroczystości używają teraz jednolitego kroku przycisku typu spin o wartości 5%: Jedno kliknięcie przycisku w oknie dialogowym lub [Edytorze właściwości](Property_editor/pl.md) zmienia przezroczystość o 5%. Trzymaj przycisk wciśnięty, aby zmienić wartość o kilka kroków 5% jednocześnie. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   Okno wyjściowe zostało przemianowane na widok raportu dla ujednolicenia z UI. [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)
-   Usunięto środowisko pracy Obraz. Do wstawienia płaszczyzny obrazu można teraz użyć polecenia [Import](Std_Import/pl.md). Podwójne kliknięcie Płaszczyzny Obrazu zmienia jej orientację i skalę. Nowe polecenie [Otwórz widok obrazu](Std_ViewLoadImage/pl.md) zastępuje polecenie Otwórz obraz. [Pull Request #8955](https://github.com/FreeCAD/FreeCAD/pull/8955)
-   Przestarzałe środowisko Raytracing zostało usunięte. Zamiast tego należy użyć zewnętrznego [Render](https://github.com/FreeCAD/FreeCAD-render). [Pull Request #9420](https://github.com/FreeCAD/FreeCAD/pull/9420)



## System podstawowy i API 



### Rdzeń programu 

-   Dodano funkcję **cbrt(x)** dla pierwiastków sześciennych do wykorzystania w [wyrażeniach](Expressions/pl#Funkcje_wykładnicze_i_logarytmiczne.md). [Pull request #8629](https://github.com/FreeCAD/FreeCAD/pull/8629)
-   Wiele nowych [właściwości](Property/pl#Wszystkie_rodzaje_właściwości.md) jest dostępnych dla skryptów. [Pull request #6717](https://github.com/FreeCAD/FreeCAD/pull/6717)
-   Do użycia z [wyrażenami](Expressions/pl.md) dodano funkcje tworzenia obiektów {{Incode|vector}}, {{Incode|matrix}}, {{Incode|rotation}}, {{Incode|placement}}, jak również funkcje macierzowe {{Incode|mrotate}}, {{Incode|mrotatex}}, {{Incode|mrotatey}}, {{Incode|mrotatez}}, {{Incode|mtranslate}}. [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/8603)



### API


<div class="mw-collapsible mw-collapsed toccolours">



#### Nowe skrypty Python 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy::scaleKnotsToBounds*: Skaluje listy węzłów U i V, aby dopasować je do podanych granic. [Pull request #7258](https://github.com/FreeCAD/FreeCAD/pull/7258) oraz [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy::scaleKnotsToBounds*: Skaluje listę węzłów, aby dopasować ją do podanych granic. [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy* Skaluje listy węzłów U i V, aby dopasować je do podanych granic. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy* Skaluje listę węzłów, aby dopasować ją do podanych granic. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*: Klasa podstawowa dla operacji naprawczych. [commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*: Naprawa nieprawidłowych krawędzi. [commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*: Odbudowuje połączenia między powierzchniami w powłoce. [commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*: Klasa umożliwiająca wykonywanie operacji na powierzchniach. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)

   ShapeFix_FixSmallFacePy: Klasa umożliwiająca przeprowadzenie operacji naprawczych na powierzchniach. commit 4c2946c8

-   \'\'ShapeFix_FixSmallSolidPy: Naprawa brył o niewielkich rozmiarach. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*: Przeznaczone do wyprowadzania swobodnych granic kształtu. [commit 1ee1aee1](https://github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*: Klasa podstawowa dla operacji naprawczych. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*: Klasa do przeprowadzania operacji naprawczych na kształtach. [commit 87db9dcc](https://github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*: Modyfikuje tolerancje kształtów podrzędnych *(wierzchołków, krawędzi, ścian)*. [commit 125d5b63](https://github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*: Klasa podstawowa dla operacji naprawczych. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*: Klasa podstawowa dla operacji naprawczych. [commit 8d568793](https://github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*: Klasa do przeprowadzania operacji naprawczych na kształtach. [commit 4b44c54c](https://github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*: Narzędzie do rozszczepiania i cięcia krawędzi. [commit bbecc3f2](https://github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*: Przedstawia metody naprawiania szkieletu kształtu. [commit 6843a461](https://github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*: Klasa do przeprowadzania operacji naprawczych na poliliniach. [commit 94f6279a](https://github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*: Naprawia rozłączone krawędzie w linii łamanej. [commit 8c6ffc99](https://github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>



#### Usunięte skrypty API 

-   *FreeCAD.EndingAdd*: zastąpiony przez *FreeCAD.addImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*: zastąpiony przez *FreeCAD.getImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)


</div>



## Menadżer dodatków 

-   Dodano podstawowe zarządzanie pakietami Pythona w celu aktualizacji i usuwania automatycznie instalowanych zależności.
-   Dodano \"tryb deweloperski\", aby pomóc w tworzeniu pliku metadanych wymaganego w każdym dodatku.



## Środowisko pracy Architektura 

-   Dodano kilka kategorii [profilu architektonicznego](Arch_Profile/pl.md): IS RHS, IS SHS, IS Kątownik oraz IS Trójnik. [Pull request #7181](https://github.com/FreeCAD/FreeCAD/pull/7181) i [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217).
-   Obiekty [profilu architektonicznego](Arch_Profile/pl.md) obsługują teraz modyfikację typu profilu po jego utworzeniu. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   Naprawiono kilka problemów z trybem edycji i poprawiono menu podręczne [widoku Drzewa](Tree_view.md) dla obiektów Łuku. Obiekty, które mogą być edytowane mają teraz opcję **Edytuj** w tym menu. Opcja **Ustaw kolor** została usunięta dla obiektów bez ściany lub mogących mieć tylko jedną ścianę. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)
-   Obiekty [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) obsługują teraz obiekty niestałe tak samo jak obiekty stałe. [Pull request #8688](https://github.com/FreeCAD/FreeCAD/pull/8688).



### Kolejne ulepszenia środowiska Architektura 

-   Poprawiono działanie narzędzia **Odwróć pozycję zawiasów**. Dla wszystkich prostokątnych polilinii przeciwległa krawędź jest teraz poprawnie wykrywana. [Pull request #8199](https://github.com/FreeCAD/FreeCAD/pull/8199)
-   [Teren](Arch_Site/pl.md) może być teraz również bryłą. [Pull request #8409](https://github.com/FreeCAD/FreeCAD/pull/8409)
-   [Teren](Arch_Site/pl.md) nie pokazuje już fantomowej reprezentacji obiektów w swojej grupie. [Pull request #8409](https://github.com/FreeCAD/FreeCAD/pull/8409)



## Środowisko pracy Rysunek Roboczy 

-   Naprawiono niedokładność narzędzia [Przyciąganij do najbliższego](Draft_Snap_Near/pl.md) podczas przyciągania do krzywych. Dodatkowo narzędzie, [Przyciągnij prostopadle](Draft_Snap_Perpendicular/pl.md) może teraz również przyciągać do powierzchni i znajdować wiele punktów. Aby przyciągnąć do wierzchołka *(np. [punktu](Draft_Point/pl.md))* narzędzie [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md) musi być teraz użyte zamiast dotychczasowego [Przyciąganij do najbliższego](Draft_Snap_Near/pl.md). [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   Aby ułatwić pracę z [warstwami](Draft_Layer/pl.md) zmodyfikowano ich zachowanie podczas przeciągania i upuszczania. Jeśli upuścisz obiekt z [grupy](Std_Group/pl.md) lub obiekt podobny do grupy, taki jak [Część budowli](Arch_BuildingPart/pl.md) - piętro środowiska Architektura, na warstwę, nie zostanie on już usunięty z grupy i odwrotnie. Działa to bez przytrzymywania klawisza **Ctrl**. [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   Polecenie [Szyk punktów](Draft_PointArray/pl.md) obsługuje teraz więcej typów obiektów punktowych. Można użyć dowolnego obiektu o kształcie i wierzchołkach, a także [siatki](Mesh_Workbench/pl.md) i [chmury punktów](Points_Workbench/pl.md). [Pull request #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   Poprawiono menu podręczne [Widoku drzewa](Tree_view/pl.md) dla obiektów Rysunku Roboczego. Obiekty, które mogą być edytowane za pomocą polecenia [Edycja](Draft_Edit/pl.md), lub które mają dedykowane rozwiązanie do edycji, mają teraz opcję **Edytuj** w tym menu. Opcja **Ustaw kolor** została usunięta dla obiektów bez ściany lub mogących mieć tylko jedną ścianę. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   Ujednolicono właściwości obiektów adnotacji Rysunku Roboczego. Obiekty [tekst](Draft_Text/pl.md), [Wymiary](Draft_Dimension/pl.md) i [Etykieta](Draft_Label/pl.md) mają teraz wszystkie właściwości Nazwa czcionki, Rozmiar czcionki i Kolor tekstu. Uspójniono również opcje Tryb wyświetlania i są to teraz: Ekran i Świat. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) oraz [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)
-   W panelu zadań polecenia [Ustaw styl](Draft_SetStyle/pl.md) przycisk **Tekst / wymiary** został zastąpiony przyciskiem **Adnotacje**. Naciśnięcie tego przycisku powoduje przetworzenie wszystkich adnotacji, w tym [Etykiet](Draft_Label/pl.md). Dodano parametry **Przekroczenie wymiaru**, **Linie pomocnicze** i **Przedłużenie linii pomocniczej**. Naprawiono także kilka drobnych dodatkowych błędów. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195), [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196) oraz [Pull request #9514](https://github.com/FreeCAD/FreeCAD/pull/9514)
-   Narzędzie Cofnij / Przywróć nie działało poprawnie dla poleceń modyfikacji Rysunku Roboczego w systemie Windows. [Pull request #8267](https://github.com/FreeCAD/FreeCAD/pull/8267)
-   Polecenie [Menadżer warstw](Draft_LayerManager/pl.md) zostało przeniesione z środowiska pracy BIM do środowiska pracy Rysunek Roboczy. [Pull request #8795](https://github.com/FreeCAD/FreeCAD/pull/8795).



### Kolejne ulepszenia środowiska Rysunek Roboczy 

-   Podczas wyrównywania płaszczyzny roboczej z ścianą była ona obracana w celu dopasowania do osi globalnych tylko wtedy, gdy ściana była elementem czworokątnym. [Pull request #7249](https://github.com/FreeCAD/FreeCAD/pull/7249)
-   Naprawiono kilka problemów związanych z funkcją [Szyk po ścieżce](Draft_PathArray/pl.md). [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) oraz [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   Polecenie [Edycja](Draft_Edit/pl.md) otrzymało kilka ulepszeń. Dla [linii łamanej](Draft_Wire/pl.md), [krzywej złożonej](Draft_BSpline/pl.md) i [krzywej Béziera](Draft_BezCurve/pl.md) dodano opcję Zamknij / Otwórz do menu podręcznego krawędzi. W przypadku krzywych złożonych i krzywych Béziera do tego samego menu dodano również opcję Odwróć. Panele zadań zostały wyczyszczone. [Pull request #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) oraz [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   Użycie klawisza **Esc** do wyjścia z polecenia nie wyłącza już trybu kontynuacji. [Pull request #7611](https://github.com/FreeCAD/FreeCAD/pull/7611)
-   Pasek narzędzi [Przyciągania](Draft_Snap/pl.md) został zmieniony na standardowy pasek narzędzi. Skróty klawiaturowe mogą być teraz przypisane do narzędzi przyciągania. Ale używanie ich podczas polecenia działa tylko wtedy, gdy żadne z pól wejściowych w panelu zadań nie jest aktywne, ponieważ \"łapią\" one tak zwane skróty wewnątrz polecenia. [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   Naprawiono kilka błędów narzędzia [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md) i dodano parametry **Kolor tekstu** oraz **Odstęp od tekstu**. [Pull request #8207](https://github.com/FreeCAD/FreeCAD/pull/8207)
-   Właściwości Początek i Koniec Odsunięcia zostały dodane do obiektów [Szyk po ścieżce](Draft_PathArray/pl.md). [Pull request #8295](https://github.com/FreeCAD/FreeCAD/pull/8295)
-   Właściwość Licznik została dodana do tablic, które jej nie posiadały: nieliniowe wersje [Szyk ortogonalny](Draft_OrthoArray/pl.md), [Szyk biegunowy](Draft_PolarArray/pl.md) i [Szyk kołowy](Draft_CircularArray/pl.md). [Pull request #8433](https://github.com/FreeCAD/FreeCAD/pull/8433)
-   Poprawiono zachowanie włączania/wyłączania [siatki](Draft_Snap_Grid/pl.md). [Pull request #8818](https://github.com/FreeCAD/FreeCAD/pull/8818).
-   Poprawiono obsługę konwerterów DWG. [Pull request #9444](https://github.com/FreeCAD/FreeCAD/pull/9444) oraz [Pull request #9830](https://github.com/FreeCAD/FreeCAD/pull/9830)



## Środowisko pracy MES 

   
  <img alt="" src=images/FEM_PostFilterContours_relnotes_0.21.png  style="width:384px;">Izokontury przedstawiające składową Y bezwzględnego strumienia magnetycznego w przewodzie miedzianym i wokół niego, przez który przepływa prąd elektryczny o częstotliwości 100 kHz. Więcej informacji o tym modelu, zobacz sekcję 14 [poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dostępny jest nowy filtr <img alt="" src=images/FEM_PostFilterContours.svg  style="width:24px;"> [Konturów](FEM_PostFilterContours/pl.md), który umożliwia rysowanie izolinii lub izokonturów. Izokontury to połączone węzły siatki, które mają tę samą wartość zmiennej wynikowej. Typowym przykładem są linie pola elektrycznego. [Pull request #8462](https://github.com/FreeCAD/FreeCAD/pull/8462)
   

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_0.21.png  style="width:384px;">Wynik symulacji *(podgrzewania przepływającej wody)*, w której widocznych jest osiem obszarów siatki *(jeden na każdy użyty rdzeń CPU)*.   Możliwe jest teraz uruchomienie solvera [Elmer](FEM_SolverElmer/pl.md) przy użyciu wielu rdzeni procesora. Więcej informacji o zastrzeżeniach można znaleźć w [tym wątku na forum](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617). [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic2D_relnotes_0.21.png  style="width:300px;">Wynik symulacji urojonej części gęstości prądu w tyglu, który był ogrzewany elektrycznie przez otaczającą go cewkę. Model ten jest dostępny poprzez stronę [Przykłady dla środowiska MES](FEM_Examples/pl.md).Więcej informacji o tym modelu można znaleźć w sekcji 16 [poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dodano narzędzie <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> [Równanie magnetodynamiki 2D](FEM_EquationMagnetodynamic2D/pl.md). Dzięki temu możliwe jest przeprowadzenie symulacji elektromagnetycznych w 2D. [Pull request #8355](https://github.com/FreeCAD/FreeCAD/pull/8355)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic_relnotes_0.21.png  style="width:384px;">Wynik symulacji urojonej części gęstości strumienia magnetycznego w przewodzie miedzianym i wokół niego, przez który przepływa prąd elektryczny o częstotliwości 100 kHz./br\>Model ten jest dostępny poprzez stronę [Przykłady środowiska dla pracy MES](FEM_Examples/pl.md).Więcej informacji na temat tego modelu można znaleźć w sekcji 14 [poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dodano narzędzie <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> [równanie magnetodynamiczne](FEM_EquationMagnetodynamic/pl.md). Dzięki niemu możliwe jest przeprowadzenie symulacji elektromagnetycznych. [Pull request #8380](https://github.com/FreeCAD/FreeCAD/pull/8380)
   

   
  <img alt="" src=images/FEM_EquationDeformation_relnotes_0.21.png  style="width:384px;">W wyniku symulacji żelazny drut o kształcie litery U został zdeformowany poprzez ściśnięcie jego końców. Więcej informacji na temat tego modelu można znaleźć w sekcji 8 [Poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dodano narzędzie <img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> [Równanie deformacji](FEM_EquationDeformation/pl.md). Dzięki niemu można wykonywać analizy nieliniowej sprężystości (deformacji). [Pull request #8981](https://github.com/FreeCAD/FreeCAD/pull/8981)
   



### Dalsze ulepszenia MES 

-   Podczas wykonywania analiz przy użyciu <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> [solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md), jest teraz również tworzona [prezentacja graficzna](FEM_PostPipelineFromResult/pl.md) wyników w celu wizualizacji wyników. [Pull request #8525](https://github.com/FreeCAD/FreeCAD/pull/8525) oraz [Pull request #8903](https://github.com/FreeCAD/FreeCAD/pull/8903)
-   Możliwe jest teraz wykonanie [analizy przejściowej](FEM_SolverElmer_SolverSettings/pl#Przechodzenie_w_czasie_(analizy_przejściowe).md) podczas korzystania z <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solvera Elmer](FEM_SolverElmer/pl.md). [Pull request #9056](https://github.com/FreeCAD/FreeCAD/pull/9056)
-   Dodano narzędzie <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [Ciśnienie początkowe](FEM_ConstraintInitialPressure/pl.md), aby ustawić początkowe ciśnienie wewnętrzne płynów. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   Dodano narzędzie <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [Zdefiniuj gęstość prądu](FEM_ConstraintCurrentDensity/pl.md) aby ustawić aktualne gęstości dla brył i ścian. [Pull request #8348](https://github.com/FreeCAD/FreeCAD/pull/8348)
-   Dodano narzędzie <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [Warunek magnetyzacji](FEM_ConstraintMagnetization/pl.md) aby ustawić magnetyzację dla ciał i ścian. [Pull request #8393](https://github.com/FreeCAD/FreeCAD/pull/8393)
-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:24px;"> [Ograniczenie prędkości przepływu](FEM_ConstraintFlowVelocity/pl.md) i <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:24px;"> [Ograniczenie początkowej prędkości przepływu](FEM_ConstraintInitialFlowVelocity/pl.md) zostały całkowicie przepisane. Teraz możliwe jest również określenie prędkości za pomocą wzoru matematycznego *(w celu zdefiniowania profilu prędkości)*. [Pull request #8963](https://github.com/FreeCAD/FreeCAD/pull/8963) i [Pull request #8964](https://github.com/FreeCAD/FreeCAD/pull/8964)**Uwaga:** To przełomowa zmiana. Analizy z istniejącymi ograniczeniami prędkości przepływu i początkowej prędkości przepływu nie będą już działać. Musisz utworzyć nowe ograniczenia prędkości przepływu w analizie, aby istniejące analizy działały.**Zauważ również:** aż do FreeCAD 0.21 wyniki solwera przepływu były błędne *(gęstość i lepkość płynu były współczynnikiem 1000 za wysoko)*. Dlatego konieczne odtworzenie ograniczenia prędkości również zapewnia, że wyniki będą poprawne.
-   Narzędzia <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:24px;"> [Zdefiniuj prędkość przepływu](FEM_ConstraintFlowVelocity/pl.md) oraz <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:24px;"> [Zdefiniuj warunek początkowy prędkości przepływu](FEM_ConstraintInitialFlowVelocity/pl.md) zostały całkowicie przepisane. Obecnie możliwe jest również określenie prędkości za pomocą formuły matematycznej *(w celu zdefiniowania profilu prędkości)*. [Pull request #8963](https://github.com/FreeCAD/FreeCAD/pull/8963) oraz [Pull request #8964](https://github.com/FreeCAD/FreeCAD/pull/8964)

   Uwaga: Jest to zmiana przełomowa. Analizy z istniejącymi wiązaniami prędkości przepływu i początkowej prędkości przepływu nie będą już działać. Musisz utworzyć nowe wiązania prędkości przepływu w analizie, aby istniejące analizy działały.
   Uwaga: do wersji FreeCAD 0.20.3 wyniki solwera przepływowego były błędne *(gęstość płynu i lepkość były o czynnik 1000 za wysokie)*. Dlatego konieczne odtworzenie ograniczenia prędkości zapewnia, że wyniki będą poprawne.

-   Możliwe jest teraz definiowanie <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:24px;"> [przemieszczenia](FEM_ConstraintDisplacement/pl.md) jako równania *(przemieszczenie według aktualnego czasu solvera)*.
-   Narzędzie <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [Objętościowe źródło ciepła](FEM_ConstraintBodyHeatSource/pl.md) ma teraz panel zadań i możliwe jest ustawienie ciepła dla kilku ciał lub użycie kilku wiązań dla różnych ciał w jednej analizie. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:24px;"> [Wiązanie sprężynowe](FEM_ConstraintSpring/pl.md) nie było używane przez żaden solwer. Teraz może być używane przez [solwer Elmer](FEM_SolverElmer/pl.md) poprzez równania [deformacji](FEM_EquationDeformation/pl.md) i [elastyczności](FEM_EquationElasticity/pl.md). [Pull request #9005](https://github.com/FreeCAD/FreeCAD/pull/9005)
-   Została dodana funkcja cięcia siatki wynikowej <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> [Filtr funkcyjny walca](FEM_PostCreateFunctionCylinder/pl.md). [Pull request #8735](https://github.com/FreeCAD/FreeCAD/pull/8735)
-   Została dodana funkcja cięcia siatki wynikowej <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> [Filtr funkcyjny sześcianu](FEM_PostCreateFunctionBox/pl.md). [Pull request #8825](https://github.com/FreeCAD/FreeCAD/pull/8825)
-   Teraz można otwierać *(i w ten sposób wizualizować)* pliki \*.pvtu *(partycjonowane niestrukturalne dane siatki VTK)*. Plik \*.pvtu jest również wynikiem symulacji [Elmer](FEM_SolverElmer/pl.md), w której zastosowano więcej niż jeden rdzeń procesora. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Critical Strain Ratio został dodany do potoku wyników VTK. Daje wskazanie rozerwania ciągliwego dla materiałów z obiektem „MaterialMechanicalNonlinear". [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   Narzędzie <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [Siatka MES na obiekt środowiska Siatka](FEM_FemMesh2Mesh/pl.md) posiada nowy parametr *Skala* umożliwiający określenie skali deformowanej siatki przy użyciu środowiska Python. [wątek na Forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) oraz [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715)
-   [Preferencje](FEM_Preferences/pl.md) mają nową opcję definiowania, który solver powinien być automatycznie dodawany podczas tworzenia nowej analizy.
-   Ulepszenia użyteczności:
    -   Jeśli podczas wczytywania pliku FreeCAD zawierającego analizę znajdujesz się w oknie środowisku pracy MES, analiza zostaje aktywowana automatycznie *(masz natychmiastowy dostęp do wszystkich przycisków paska narzędzi FEM)*.
    -   Na pasku narzędziowym znajdują się tylko przyciski dla solwerów zainstalowanych w Twoim systemie. Niedostępne solwery nie są już wyświetlane.
-   Poprzez stronę [Przykłady dla środowiska pracy MES](FEM_Examples/pl.md) dostępne są nowe pliki przykładów dla następujących równań: [Równanie deformacji](FEM_EquationDeformation/pl.md), [Równanie przepływu](FEM_EquationFlow/pl.md), [Równanie strumienia](FEM_EquationFlux/pl.md), [Równanie ciepła](FEM_EquationHeat/pl.md), [Równanie magnetodynamiczne](FEM_EquationMagnetodynamic/pl.md) oraz [Równanie magnetodynamiczne 2D](FEM_EquationMagnetodynamic2D/pl.md). Pull requests [#8550](https://github.com/FreeCAD/FreeCAD/pull/8550), [#8569](https://github.com/FreeCAD/FreeCAD/pull/8569), [#8579](https://github.com/FreeCAD/FreeCAD/pull/8579), [#8597](https://github.com/FreeCAD/FreeCAD/pull/8597) i [#8630](https://github.com/FreeCAD/FreeCAD/pull/8630) oraz [#9004](https://github.com/FreeCAD/FreeCAD/pull/9004)
-   Nowa karta materiału dla dwutlenku węgla i stopu tytanu. [Pull request #8332](https://github.com/FreeCAD/FreeCAD/pull/8332) oraz [Pull request #8636](https://github.com/FreeCAD/FreeCAD/pull/8636)



## Środowisko pracy Siatka 

-   Wsparcie dla dodawania przezroczystości do siatki. [temat na Forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) oraz [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e)



## Środowisko pracy Część 

Narzędzie [Punkty z siatki](Part_PointsFromMesh/pl.md) zostało rozszerzone, aby akceptować dowolny obiekt geometryczny jako dane wejściowe. [Pull request #8730](https://github.com/FreeCAD/FreeCAD/pull/8730).



## Środowisko pracy Projekt Części 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_0.21.png  style="width:384px;">Otwór z pogłębieniem stożkowym.   Okno dialogowe [Otwór](PartDesign_Hole.md) obsługuje typ łba śruby *stożkowej*. [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                                         
   

+++
| <img alt="" src=images/PartDesign_task_dialog_relnotes_0.21.png  style="width:384px;"> | Ulepszono interfejs użytkownika w oknach dialogowych wielu zadań środowiska pracy Projekt Części do wybierania geometrii, który nie wymaga już używania oddzielnych przycisków do dodawania lub usuwania geometrii do wyboru. [Pull request #8990](https://github.com/FreeCAD/FreeCAD/pull/8990) |
+++
|                                                                                                       |                                                                                                                                                                                                                                                                                                  |
+++



### Kolejne ulepszenia środowiska Projekt Części 

-   W oknie dialogowym [Otwór](PartDesign_Hole/pl.md) usunięto przestarzałe typy łbów śrub *(łeb serowy, śruba kapiszonowa itp.)*. Były one przestarzałe od wersji FreeCAD 0.19. Otwory wykorzystujące te typy są przekształcane w niestandardowe pogłębiacze/otwory o średnicy i głębokości używanej przez typy. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   W oknach dialogowych [Uzupełnianie wyciągnięciem przez profile](PartDesign_AdditiveLoft/pl.md) i [Odejmowanie wyciągnięciem przez profile](PartDesign_SubtractiveLoft/pl.md), wcześniej niefunkcjonalna opcja **Zamknięty** tworzy teraz zamknięte wyciągnięcie przez profile *(jak pierścień)*. [Pull request #8748](https://github.com/FreeCAD/FreeCAD/pull/8748)
-   Polecenie [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md) zostało dodane do paska narzędzi Pomoc. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Usunięto z menu nieużyteczne polecenia [Zamknij edycje szkicu](Sketcher_LeaveSketch/pl.md) i [Widok szkicu](Sketcher_ViewSketch/pl.md). Polecenia [Edycja szkicu](Sketcher_EditSketch/pl.md), [Łączenie szkiców](Sketcher_MergeSketches/pl.md) i [Odbicie lustrzane szkicu](Sketcher_MirrorSketch/pl.md) zostały dodane do menu. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Narzędzie [Koło zębate ewolwentowe](PartDesign_InvoluteGear/pl.md) ma nowe właściwości do zmiany długości zębów. Umożliwia to teraz dostosowanie do pewnych typów zakłóceń i wykorzystanie profilu do tworzenia [involute splines](https://en.wikipedia.org/wiki/Spline_(mechanical)). [Pull request #8184](https://github.com/FreeCAD/FreeCAD/pull/8184)
-   Narzędzie [Koło zębate ewolwentowe](PartDesign_InvoluteGear/pl.md) oferuje teraz zmianę profilu. [Issue #5618](https://github.com/FreeCAD/FreeCAD/issues/5618) oraz [Pull request #8934](https://github.com/FreeCAD/FreeCAD/pull/8934)
-   Podczas tworzenia [klona](PartDesign_Clone/pl.md) będzie on teraz dziedziczył kolory klonowanego obiektu. [Pull request #9547](https://github.com/FreeCAD/FreeCAD/pull/9547).



## Środowisko pracy Path 

-   Integracja Camotics. Jeśli zainstalowana jest aplikacja Camotics *(wersja 1.2.2 lub nowsza)*, do paska narzędzi Path zostanie dodana nowa ikona. Wybierz zadanie Path i naciśnij przycisk, aby otworzyć okno dialogowe Camotics. Następnie przeciągnij suwak, aby wygenerować symulowaną bryłę w dowolnym punkcie zadania. Można również uruchomić pełną aplikację Camotics, aby uruchomić animowaną symulację. Powoduje to uzyskanie cichego post-processingu zadania i utworzenie pliku projektu camotics. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Dodatkowe łańcuchy zastępcze do automatycznego nazywania wyjść. Jeśli dane wyjściowe są dzielone na wiele plików, nazwy plików mogą automatycznie zastępować etykietę kontrolera narzędzi, Work Coordinate Systems (WCS) lub etykietę operacji. Jest to dodatek do innych istniejących ciągów zastępczych, takich jak data, nazwa zadania itp.

-   Zaimplementowana opcja łamania wiórów dla cykli wiercenia w stylu dziobania. Łamanie wiórów emituje cykl **G73**, który powoduje, że kontroler wykonuje bardzo mały ruch wycofania, aby złamać wiór bez pełnego wycofania wiertła z otworu. G73 jest obsługiwany natywnie przez środowisko LinuxCNC. Inne postprocesory będą musiały interpretować G73 i emitować odpowiednie kody kontroli lub dekomponować retrakcję na ruchy G1/G0. Wsparcie postprocesora dla dekompozycji G73 zostało dodane do „refaktoryzowanych" postprocesorów. [Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469)



## Środowisko pracy Szkicownik 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_0.21.gif  style="width:384px;">Przeciąganie węzłów krzywej złożonej.Kliknij na obrazek, aby zobaczyć animację.   Węzły krzywej złożonej mogą być teraz przeciągane i związane jak każdy inny punkt szkicu. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                                         
   

+++
| <img alt="" src=images/sketcher-move-piece_relnotes_0.21.gif  style="width:384px;">Przeciąganie krzywej złożonej. | Operacja przeciągania krzywej złożonej przesuwa teraz tylko część między węzłami. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110) |
| Kliknij na obrazek, jeśli animacja się nie uruchomi.                                                                                        |                                                                                                                                                      |
+++
|                                                                                                                                             |                                                                                                                                                      |
+++

+++
| <img alt="" src=images/Sketcher_Join_Curves_relnotes_0.21.gif  style="width:384px;"> | Dodano narzędzie [Połącz krzywe](Sketcher_JoinCurves/pl.md). Może ono łączyć dwie krzywe w jedną krzywą złożoną. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507) |
| Kliknij na obrazek, aby zobaczyć animację.                                                        |                                                                                                                                                                                             |
+++
|                                                                                                   |                                                                                                                                                                                             |
+++

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_0.21.gif  style="width:384px;">Kliknij na obrazek, aby zobaczyć animację.   Szkice mogą być teraz płynnie edytowane z przodu lub z tyłu. Podczas pracy od tyłu, wierzchołki *(oraz wszystkie geometrie i ograniczenia)* są jednakowo wybieralne, a widok przekroju jest przełączany automatycznie. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                        
   

+++
| <img alt="" src=images/Sketcher_Grid_Rework_relnotes_0.21.png  style="width:384px;"> | Siatka szkicownika została przerobiona. Dodano narzędzie [Siatka](Sketcher_Grid/pl.md). Dodano opcję automatycznego przeskalowania siatki. [Pull request #8473](https://github.com/FreeCAD/FreeCAD/pull/8473) |
+++
|                                                                                                   |                                                                                                                                                                                                                       |
+++

+++
| <img alt="" src=images/Sketcher_Constraint_Widget_relnotes_0.21.png  style="width:384px;"> | Widżet szkicownika Wiązania został przerobiony w celu uproszczenia interfejsu użytkownika. [Pull request #7566](https://github.com/FreeCAD/FreeCAD/pull/7566) |
+++
|                                                                                                               |                                                                                                                                                               |
+++

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_0.21.gif  style="width:384px;">Kliknij na obrazek, aby zobaczyć animację.   Widżet Element został przerobiony w celu uproszczenia interfejsu użytkownika i umożliwienia prostszego wyboru różnych części każdej geometrii: Krawędź, punkt początkowy, punkt końcowy i punkt środkowy. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                    
   

   
  [384px](Sketcher_Grid_relnotes_1.0.gif.md)   Wprowadzono funkcję automatycznej zmiany rozmiaru siatki w zależności od stopnia powiększenia oraz inne usprawnienia. [Pull request #8473](https://github.com/FreeCAD/FreeCAD/pull/8473)
                                                       
   

+++
| <img alt="" src=images/Sketcher_layers_relnotes_0.21.gif  style="width:384px;"> | Wprowadzono podstawową funkcjonalność warstw wizualnych, na razie obsługiwane są tylko 3 zakodowane na stałe warstwy. Spodziewajcie się dalszych ulepszeń w przyszłości. Ten PR usuwa również widżet \"Edytuj kontrolki\" z panelu zadań, ponieważ cała jego zawartość została przeniesiona w inne miejsca lub usunięta. Opcje kolejności renderowania zostały przeniesione na pasek narzędzi edycji Szkicownika. [Pull request #8716](https://github.com/FreeCAD/FreeCAD/pull/8716) oraz [Pull request #9590](https://github.com/FreeCAD/FreeCAD/pull/9590) |
+++
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+++

+++
| <img alt="" src=images/Sketcher_Circle2CircleConstraint_relnotes_0.21.png  style="width:384px;"> | Wprowadzono wiązanie [odległości między okręgami](Sketcher_ConstrainDistance/pl.md). [Pull request #8896](https://github.com/FreeCAD/FreeCAD/pull/8896) |
+++
|                                                                                                                           |                                                                                                                                                                 |
+++

+++
| <img alt="" src=images/Sketcher_Circle2LineConstraint_relnotes_0.21.png  style="width:384px;"> | Wprowadzono [wiązanie odległości](Sketcher_ConstrainDistance/pl.md) dla krąg do linii. [Pull request #9044](https://github.com/FreeCAD/FreeCAD/pull/9044) |
+++
|                                                                                                                       |                                                                                                                                                                   |
+++

   
  <img alt="" src=images/Sketcher-snap2_relnotes_0.21.gif  style="width:384px;">Kliknij na obrazek, aby obejrzeć animację.   Dodano menedżera przyciągania, przyciąganie pod kątem i przyciąganie w punkcie środkowym. [Pull request #8387](https://github.com/FreeCAD/FreeCAD/pull/8387)
                                                                                                                                                  
   

+++
| <img alt="" src=images/Sketcher-concentric_relnotes_0.21.gif  style="width:384px;"> | [Wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md) może teraz działać jako wiązanie koncentryczne przy wyborze 2 lub więcej okręgów, łuków, elips lub łuków elips. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703) |
+++
|                                                                                                 |                                                                                                                                                                                                                                                      |
+++

+++
| <img alt="" src=images/Sketcher-B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;"> | Dodano narzędzie [Krzywa złożona przez węzły](Sketcher_CreateBSplineByInterpolation/pl.md). [Pull request #8530](https://github.com/FreeCAD/FreeCAD/pull/8530) |
+++
|                                                                                                                     |                                                                                                                                                                        |
+++

+++
| <img alt="" src=images/Sketcher-periodic_B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;"> | Dodano narzędzie [Okresowa krzywa złożona przez węzły](Sketcher_CreatePeriodicBSplineByInterpolation/pl.md). |
|                                                                                                                                       |                                                                                                                      |
|                                                                                                                                       | [Pull request #8530](https://github.com/FreeCAD/FreeCAD/pull/8530)                                                 |
+++
|                                                                                                                                       |                                                                                                                      |
+++



### Kolejne ulepszenia środowiska Szkicownik 

-   Przycisk paska narzędzi [Wiązanie prawo Snella](Sketcher_ConstrainSnellsLaw/pl.md) został usunięty. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   [Rozdziel](Sketcher_Split/pl.md) obsługuje teraz więcej krzywych *(elipsy, parabole, hiperbolę i krzywe złożone)*. [Pull request #6971](https://github.com/FreeCAD/FreeCAD/pull/6971)
-   [Wiązania wymiarów](Sketcher_Workbench/pl#Wiązania_wymiarów.md) i pola wyboru wartości obsługują teraz tą samą matematykę co [wyrażenia](Expressions/pl.md) *(obliczane na bieżąco)*. [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   Przyciski paska narzędzi [Wybierz zbędne wiązania](Sketcher_SelectRedundantConstraints/pl.md) i [Wybierz wiązania konfliktowe](Sketcher_SelectConflictingConstraints/pl.md) zostały usunięte. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Przycisk paska narzędzi dla [Przerwij operację](Sketcher_StopOperation/pl.md) został usunięty. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   Usunięto przycisk paska narzędzi dla [Wybierz elementy bez wiązań](Sketcher_SelectElementsWithDoFs/pl.md). [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   Pasek narzędzi Szkicownika został podzielony na dwa: \"Tryb edycji szkicownika\" i \"Szkicownik\" *(czyli \"nie tryb edycji\")*. Paski narzędzi Szkicownika przeznaczone tylko do trybu edycji są ukryte w trybie nieedytowania, a te przeznaczone tylko do trybu nieedytowania są ukryte w trybie edycji. Pasek narzędzi Konstrukcja jest również ukryty w szkicowniku. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   [Kalka techniczna](Sketcher_CarbonCopy/pl.md), jeśli to możliwe, używa teraz nazw wiązań w tworzonych przez siebie wyrażeniach zamiast odniesienia opartego na indeksie, dzięki czemu jest bardziej niezawodny. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)
-   Usunięto narzędzie \"Wiązanie wyrównania wewnętrznego\". Było ono przestarzałe od czasu wprowadzenia narzędzia [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry.md). [Pull request #8863](https://github.com/FreeCAD/FreeCAD/pull/8863)
-   Uproszczono okienko zadań szkicownika \"Komunikaty solvera\". Pole wyboru Usuń wiązania nadmiarowe automatycznie zostało przeniesione do przycisku w menu panelu ustawień wiązań. Pole wyboru aktualizacji automatycznej zostało przeniesione do przycisku w menu aktualizacji. [Pull request #8864](https://github.com/FreeCAD/FreeCAD/pull/8864)



## Środowisko pracy Powierzchnia 3D 

+++
| <img alt="" src=images/Surface_BlendCurve_relnotes_0.21.png  style="width:250px;"> | Dodano narzędzie [Krzywa łącząca](Surface_BlendCurve/pl.md). [Pull request #7339](https://github.com/FreeCAD/FreeCAD/pull/7339) |
+++
|                                                                                               |                                                                                                                                         |
+++



## Środowisko pracy Rysunek Techniczny 

+++
| <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_0.21.png  style="width:250px;">           | Dodano nowe narzędzie [Symbol wykończenia powierzchni](TechDraw_SurfaceFinishSymbol/pl.md) pozwalające na tworzenie symboli wykończenia powierzchni opisujących chropowatość, ułożenie i falistość, ale także oznaczających rodzaj obróbki powierzchni. Obsługuje ono zarówno style ISO jak i ASME. Jak pokazano na obrazku, istniejące narzędzie [Linia odniesienia](TechDraw_LeaderLine/pl.md) może być użyte do prawidłowego odniesienia zorientowanych symboli do krawędzi obiektu. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227) |
+++
| <img alt="" src=images/TechDraw_ComplexSection_relnotes_0.21.png  style="width:250px;">                       | Dodano narzędzie [Przekrój złozony](TechDraw_ComplexSection/pl.md) umożliwiające tworzenie półprzekrojów oraz ich przesuwania i wyrównywania. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)                                                                                                                                                                                                                                                                                                                                                   |
+++
| <img alt="" src=images/TechDraw_HoleShaftFitExample_relnotes_0.21.png  style="width:250px;">             | Dodano narzędzie [Dodaj pasowanie otworu lub wału](TechDraw_HoleShaftFit/pl.md). [Pull request #8455](https://github.com/FreeCAD/FreeCAD/pull/8455)                                                                                                                                                                                                                                                                                                                                                                                                                |
+++
| <img alt="" src=images/TechDraw_AxoLengthDimensionExample_relnotes_0.21.png  style="width:250px;"> | Dodano narzędzie [Wymiar długości w aksonometrii](TechDraw_AxoLengthDimension/pl.md). [Pull request #8359](https://github.com/FreeCAD/FreeCAD/pull/8359)                                                                                                                                                                                                                                                                                                                                                                                                           |
+++
|                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+++



### Kolejne ulepszenia środowiska Rysunek Techniczny 

-   Tryby nawigacji zostały zaktualizowane, aby dopasować je do tych używanych w oknie widoku 3D. [Pull request #7081](https://github.com/FreeCAD/FreeCAD/pull/7081) and [Pull request #7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Poprawiono kreskowanie bitmapami. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) and [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121)
-   Dodano wsparcie dla regulowanych odstępów dla linii przedłużających [wymiary](TechDraw_Preferences/pl#Wymiary.md). [Pull request #7133](https://github.com/FreeCAD/FreeCAD/pull/7133)
-   Wprowadzono wielowątkowość dla usuwania ukrytych linii i znajdowania ścian. [Pull request #7377](https://github.com/FreeCAD/FreeCAD/pull/7377)
-   Poprawiono algorytm wykrywania ścian. [Pull request #7448](https://github.com/FreeCAD/FreeCAD/pull/7448)
-   Dodano narzędzie [Drukuj wszystkie strony](TechDraw_PrintAll/pl.md). [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   Dodano [Cztery narzędzia](TechDraw_StackGroup/pl.md) do kontroli kolejności układania widoków w stos. [Issue #6012](https://github.com/FreeCAD/FreeCAD/issues/6012) oraz [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   Narzędzie [Aktywny widok](TechDraw_ActiveView/pl.md) tworzy teraz zrzut ekranu zamiast obrazu SVG. [Pull request #7471](https://github.com/FreeCAD/FreeCAD/pull/7471)
-   Wszystkie szablony skryptów łacińskich zostały przekonwertowane na \"plain svg\". [Pull request #7472](https://github.com/FreeCAD/FreeCAD/pull/7472)
-   Dodano podgląd do panelu zadań narzędzia [Widok przekroju](TechDraw_SectionView/pl.md). [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
-   Usunięto przestarzałe funkcje:

replaceCenterLine, replaceCosmeticEdge, replaceCosmeticVertex oraz replaceGeomFormat.

-   Wymiary 3D mogą być teraz tworzone w taki sam sposób jak wymiary 2D, *(oprócz tego, że geometria musi być wybrana w widoku 3D i wartość właściwości \"Typ pomiaru\" musi być przełączona na Prawda)*. Eliminuje to konieczność ręcznego łączenia ich z geometrią 3D. Napraw wymiar. [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   Dodano narzędzie [Napraw wymiar](TechDraw_DimensionRepair/pl.md). [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   Dodano funkcję usuwania nakładających się krawędzi zwracanych przez algorytm usuwania ukrytych linii, w tym nowe ustawienie *(w preferencjach zaawansowanych)* liczby przebiegów tej funkcji. [Pull request #9280](https://github.com/FreeCAD/FreeCAD/pull/9280)



## Kompilacja

Od tego wydania FreeCAD może być kompilowany tylko przy użyciu środowiska Qt 5.x i Python 3.x. Najniższa wspierana wersja Qt to 5.12, najniższa wspierana wersja środowiska Python to 3.8.

Aby skompilować program FreeCAD, zapoznaj się z instrukcjami dla systemów: [Linux](Compile_on_Linux/pl.md), [MacOS](Compile_on_MacOS/pl.md) oraz [Windows](Compile_on_Windows/pl.md).

Obsługiwane systemy operacyjne:

-   Linux Ubuntu Focal Fossa (20.04) i nowsze,
-   MacOS: wersja minimalna 10.12 Sierra lub nowszy,
-   Windows 7, 8, 10 i 11



## Znane ograniczenia 



### Windows 32bit 

Już od wersji 0.19 FreeCAD oficjalnie nie obsługuje 32-bitowych systemów Windows. Może działać na nich, ale nie zapewniamy wsparcia dla tych systemów.



### Pulpit zdalny w systemie Windows 

W zależności od możliwości graficznych OpenGL komputera, może się zdarzyć, że podczas uruchamiania programu FreeCAD za pośrednictwem pulpitu zdalnego wystąpi awaria. Aby to naprawić, zaktualizuj sterownik OpenGL. Jeśli to nie pomoże:

-   Pobierz [bibliotekę OpenGL](https://downloads.fdossena.com/geth.php?r=mesa64-latest) dla 64-bitowego systemu Windows i rozpakuj ją.
-   Zmień nazwę pliku DLL na *opengl32sw.dll* i skopiuj go do podfolderu *bin* w folderze instalacyjnym FreeCADa (nadpisz tam istniejącą bibliotekę DLL).



### MacOS: Środowisko pracy Start pokazuje pustą stronę 

Jeśli środowisko pracy [Start](Start_Workbench.md) pokazuje tylko pustą stronę, musisz włączyć opcję **Użyj programowego OpenGL** w menu **FreeCAD-0.21 →Edycja→ Preferencje ... → Wyświetlanie**.



## Pozostałe zasoby 

-   [Mango Jelly Video about 0.21 Features](https://www.youtube.com/watch?v=rPxr0yvNgxo)



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.21/pl
