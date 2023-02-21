# Release notes 1.0/pl
**FreeCAD 1.0 jest w trakcie rozwoju, nie ma jeszcze oczekiwanej daty wydania.**


{{Message|
Czy brakuje jakichś funkcji? Wspomnij o nich w wątku na forum [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Informacje o wydaniu v1.0].

Więcej informacji na temat sposobów przyczyniania się do rozwoju programu FreeCAD można znaleźć na stronie [Pomóż w rozwoju FreeCAD](Help_FreeCAD/pl.md).}}


{{Message|Wszystkie obrazy na tej stronie muszą używać przyrostka **_relnotes_1.0**.}}


{{TOCright}}

**FreeCAD 1.0** zostanie wydany w roku *2023*, pobranie będzie możliwe ze strony [Download](Download/pl.md). Ta strona jest podsumowaniem najciekawszych zmian i funkcji.

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).

Miejsce na przyciągający wzrok obrazek wybrany przez adminów z [galerii pokazowej użytkowników](https://forum.freecadweb.org/viewforum.php?f=24).



## Informacje ogólne 



## Interfejs użytkownika 

   
  ![](images/Navi_Cube_relnotes_1.0.gif )   Ściany narożników kostki nawigacyjnej są teraz sześciokątne i większe, dzięki czemu łatwiej je kliknąć. [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876) oraz [Pull request #8266](https://github.com/FreeCAD/FreeCAD/pull/8266).
   

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_1.0.gif  style="width:384px;">Trwały przekrój przecinających się obiektów.Kliknij w obraz, aby zobaczyć animację. | Narzędzie [Wycinek z przekroju](Part_SectionCut/pl.md) umożliwia teraz wycięcie przecinających się obiektów. Jest to przydatne w przypadku złożeń, w których czasami nie można uniknąć przecięć stykających się obiektów ze względu na problemy numeryczne. |
|                                                                                                                                                                                                                      | [Pull request #8252](https://github.com/FreeCAD/FreeCAD/pull/8252).                                                                                                                                                                                                 |
+++

   
  <img alt="" src=images/Measurement-Part_relnotes_1.0.png  style="width:384px;">   Styl wyświetlania wyników [pomiarów](Part_Module/pl#Pomiary.md) utworzonych przy użyciu środowiska [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) może być teraz zmieniony w [preferencjach](PartDesign_Preferences/pl#Pomiary.md). [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148)
   

   
  <img alt="" src=images/WbSelector_relnotes_1.0.png  style="width:300px;">   Pole wyboru środowiska pracy może być teraz opcjonalnie umieszczone na pasku menu zamiast w obszarze paska narzędzi. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679)
   



### Planowane ulepszenie dla interfejsu użytkownika 

-   Przycisk <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Tryb Edycji](Std_UserEditMode/pl.md) został usunięty ze standardowego paska narzędzi. Może zostać ponownie dodany przez [dostosowanie](Std_DlgCustomize/pl.md) Twojego paska narzędzi.[Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570)
-   Przyciski <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Drukuj](Std_Print/pl.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Kopiuj](Std_Copy/pl.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Wklej](Std_Paste/pl.md) i <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Wytnij](Std_Cut/pl.md) zostały usunięte ze standardowego paska narzędzi. Mogą zostać ponownie dodane przez [dostosowanie](Std_DlgCustomize/pl.md) Twojego paska narzędzi.[Pull request #7571](https://github.com/FreeCAD/FreeCAD/pull/7571) i [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e).
-   Dodano polecenia [Zachowaj widok](Std_StoreWorkingView/pl.md) i [Odtwórz widok](Std_RecallWorkingView/pl.md) dla tymczasowego widoku roboczego. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Zmiany wartości za pomocą kółka myszy w \"polach wejściowych\" *(typ widżetu używany do wprowadzania wartości w panelach zadań, na przykład przez [Linia](Draft_Line/pl.md))* środowiska Rysunek Roboczy są wyłączone, jeśli widżet nie jest aktywny i przełącznik [ComboBoxWheelEventFilter](Fine-tuning/pl.md) jest włączony. Dzięki temu unikniemy niechcianych zmian wartości podczas przewijania, co już miało miejsce w przypadku pól typu spinner i combo. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Możliwe jest teraz ustawienie domyślnej przezroczystości dla nowych obiektów środowiska [Część](Part_Module/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) w [preferencjach](PartDesign_Preferences/pl.md). [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103).
-   Pojawił się nowy styl orbitalny **Free Turntable**. Można go włączyć w [ustawianiach](Preferences_Editor/pl#Nawigacja.md) lub naciskając przycisk **[<img src=images/NavigationCAD_dark.svg style="width:16px">** [Paska statusu](Status_bar/pl.md), a następnie korzystając z menu **Ustawienia → Technika orbitalna**). [Pull Request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Panel zadań [Wygląd zewnętrzny](Std_SetAppearance/pl.md) ma teraz także przycisk do ustawiania właściwości Kolor punktu. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   Dodano przycisk do przełączania kolorów gradientu tła okna [widoku 3D](3D_view/pl.md) w [Ustawieniach](Preferences_Editor/pl#Kolory.md). [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Wszystkie ustawienia przezroczystości używają teraz jednolitego kroku przycisku typu spin o wartości 5%: Jedno kliknięcie przycisku w oknie dialogowym lub [Edytorze właściwości](Property_editor/pl.md) zmienia przezroczystość o 5%. Trzymaj przycisk wciśnięty, aby zmienić wartość o kilka kroków 5% jednocześnie. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   Okno wyjściowe zostało przemianowane na widok raportu dla ujednolicenia z UI. [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)



## System podstawowy i API 



### Rdzeń programu 



### API


<div class="mw-collapsible mw-collapsed toccolours">



#### Nowe skrypty Python 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy::scaleKnotsToBounds*: Skaluje listy węzłów U i V, aby dopasować je do podanych granic. [Pull request #7258](https://github.com/FreeCAD/FreeCAD/pull/7258) oraz [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy::scaleKnotsToBounds*: Skaluje listę węzłów, aby dopasować ją do podanych granic. [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*: Klasa podstawowa dla operacji naprawczych. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*: Naprawa nieprawidłowych krawędzi. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*: Odbudowuje połączenia między powierzchniami w powłoce. [commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*: Klasa umożliwiająca wykonywanie operacji na powierzchniach. [commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*: Klasa umożliwiająca przeprowadzenie operacji naprawczych na powierzchniach. [commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*: Naprawa brył o niewielkich rozmiarach. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
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



## Środowisko pracy Architektura 

-   Naprawiono kilka problemów z trybem edycji i poprawiono menu podręczne [widoku Drzewa](Tree_view.md) dla obiektów Łuku. Obiekty, które mogą być edytowane mają teraz opcję **Edytuj** w tym menu. Opcja **Ustaw kolor** została usunięta dla obiektów bez ściany lub mogących mieć tylko jedną ścianę. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)



### Planowane ulepszenie dla środowiska Architektura 

-   Obiekty [profilu architektonicznego](Arch_Profile/pl.md) obsługują teraz modyfikację typu profilu po jego utworzeniu. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)



## Środowisko pracy Rysunek Roboczy 

-   Naprawiono niedokładność narzędzia [Przyciąganij do najbliższego](Draft_Snap_Near/pl.md) podczas przyciągania do krzywych. Dodatkowo narzędzie, [Przyciągnij prostopadle](Draft_Snap_Perpendicular/pl.md) może teraz również przyciągać do powierzchni i znajdować wiele punktów. Aby przyciągnąć do wierzchołka *(np. [punktu](Draft_Point/pl.md))* narzędzie [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md) musi być teraz użyte zamiast dotychczasowego [Przyciąganij do najbliższego](Draft_Snap_Near/pl.md). [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132).
-   Aby ułatwić pracę z [warstwami](Draft_Layer/pl.md) zmodyfikowano ich zachowanie podczas przeciągania i upuszczania. Jeśli upuścisz obiekt z [grupy](Std_Group/pl.md) lub obiekt podobny do grupy, taki jak [Część budowli - piętro](Arch_BuildingPart/pl.md) środowiska Architektura, na warstwę, nie zostanie on już usunięty z grupy i odwrotnie. Działa to bez przytrzymywania klawisza **Ctrl**. [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   Polecenie [Szyk punktów](Draft_PointArray/pl.md) obsługuje teraz więcej typów obiektów punktowych. Można użyć dowolnego obiektu o kształcie i wierzchołkach, a także [siatki](Mesh_Workbench/pl.md) i [chmury punktów](Points_Workbench/pl.md). [Żądanie ściągnięcia #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   Poprawiono menu podręczne [Widoku Drzewa](Tree_view/pl.md) dla obiektów Rysunku Roboczego. Obiekty, które mogą być edytowane za pomocą polecenia [Edycja](Draft_Edit/pl.md), lub które mają dedykowane rozwiązanie do edycji, mają teraz opcję **Edytuj** w tym menu. Opcja **Ustaw kolor** została usunięta dla obiektów bez ściany lub mogących mieć tylko jedną ścianę. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   Ujednolicono właściwości obiektów adnotacji Rysunku Roboczego. Obiekty [tekst](Draft_Text/pl.md), [Wymiary](Draft_Dimension/pl.md) i [Etykieta](Draft_Label/pl.md) mają teraz wszystkie właściwości Nazwa czcionki, Rozmiar czcionki i Kolor tekstu. Uspójniono również opcje Tryb wyświetlania i są to teraz: Ekran i Świat. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) oraz [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081).
-   Narzędzie Cofnij / Przywróć nie działało poprawnie dla poleceń modyfikacji Rysunku Roboczego w systemie Windows. [Pull request #8267](https://github.com/FreeCAD/FreeCAD/pull/8267)



### Planowane ulepszenie dla środowiska Rysunek Roboczy 

-   Naprawiono kilka problemów związanych z [Szyk po ścieżce](Draft_PathArray/pl.md). [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) oraz [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662).
-   Polecenie [Edycja](Draft_Edit/pl.md) otrzymało kilka ulepszeń. Dla [linii łamanej](Draft_Wire/pl.md), [krzywej złożonej](Draft_BSpline/pl.md) i [krzywej Béziera](Draft_BezCurve/pl.md) dodano opcję Zamknij / Otwórz do menu podręcznego krawędzi. W przypadku krzywych złożonych i krzywych Béziera do tego samego menu dodano również opcję Odwróć. Panele zadań zostały wyczyszczone. [Żądanie ściągnięcia #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) i [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541).
-   Pasek narzędzi [Przyciągania](Draft_Snap/pl.md) został zmieniony na standardowy pasek narzędzi. Skróty klawiaturowe mogą być teraz przypisane do narzędzi przyciągania. Ale używanie ich podczas polecenia działa tylko wtedy, gdy żadne z pól wejściowych w panelu zadań nie jest aktywne, ponieważ \"łapią\" one tak zwane skróty wewnątrz polecenia. [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   W panelu zadań polecenie [Ustaw styl](Draft_SetStyle/pl.md) przycisk \"Tekst / wymiary\" został zastąpiony przyciskiem \"Adnotacje\". Naciśnięcie tego przycisku spowoduje przetworzenie wszystkich adnotacji, w tym [Etykieta](Draft_Label/pl.md). Naprawiono także kilka drobnych błędów. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195) oraz [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196).
-   Naprawiono kilka błędów narzędzia [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md) i dodano osobny przycisk Kolor tekstu. [Pull request #8207](https://github.com/FreeCAD/FreeCAD/pull/8207)
-   Właściwość Licznik została dodana do tablic, które jej nie posiadały: nieliniowe wersje [Szyk ortogonalny](Draft_OrthoArray/pl.md), [Szyk biegunowy](Draft_PolarArray/pl.md) i [Szyk kołowy](Draft_CircularArray/pl.md). [Pull request #8433](https://github.com/FreeCAD/FreeCAD/pull/8433)



## Środowisko pracy MES 

   
  <img alt="" src=images/FEM_PostFilterContours_relnotes_1.0.png  style="width:384px;">Izokontury przedstawiające składową Y bezwzględnego strumienia magnetycznego w przewodzie miedzianym i wokół niego, przez który przepływa prąd elektryczny o częstotliwości 100 kHz.Więcej informacji o tym modelu, zobacz sekcję 14 [poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dostępny jest nowy filtr <img alt="" src=images/FEM_PostFilterContours.svg  style="width:24px;"> [Conturów](FEM_PostFilterContours/pl.md), który umożliwia rysowanie izolinii lub izokonturów. Izokontury to połączone węzły siatki, które mają tę samą wartość zmiennej wynikowej. Typowym przykładem są linie pola elektrycznego. [Pull request #8462](https://github.com/FreeCAD/FreeCAD/pull/8462)
   

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_1.0.png  style="width:384px;">Wynik symulacji, w której widocznych jest osiem obszarów siatki *(jeden na każdy użyty rdzeń CPU)*.   Możliwe jest teraz uruchomienie solvera [Elmer](FEM_SolverElmer/pl.md) przy użyciu wielu rdzeni procesora. Więcej informacji o zastrzeżeniach można znaleźć w [tym wątku na forum](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617). [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic2D_relnotes_1.0.png  style="width:300px;">Wynik symulacji urojonej części gęstości prądu w tyglu, który był ogrzewany elektrycznie przez otaczającą go cewkę. Więcej informacji o tym modelu można znaleźć w sekcji 16 [poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dodano narzędzie <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> [Równanie magnetodynamiki 2D](FEM_EquationMagnetodynamic2D/pl.md). Dzięki temu możliwe jest przeprowadzenie symulacji elektromagnetycznych w 2D. [Pull request #8355](https://github.com/FreeCAD/FreeCAD/pull/8355)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic_relnotes_1.0.png  style="width:384px;">Wynik symulacji urojonej części gęstości strumienia magnetycznego w przewodzie miedzianym i wokół niego, przez który przepływa prąd elektryczny o częstotliwości 100 kHz.Więcej informacji na temat tego modelu można znaleźć w sekcji 14 [poradnika Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Dodano narzędzie <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> [równanie magnetodynamiczne](FEM_EquationMagnetodynamic/pl.md). Dzięki niemu możliwe jest przeprowadzenie symulacji elektromagnetycznych. [Pull request #8380](https://github.com/FreeCAD/FreeCAD/pull/8380)
   



### Planowane ulepszenie dla środowiska MES 

-   Dodano narzędzie <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [Ciśnienie początkowe](FEM_ConstraintInitialPressure/pl.md), aby ustawić początkowe ciśnienie wewnętrzne płynów. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   Narzędzie <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [Objętościowe źródło ciepła](FEM_ConstraintBodyHeatSource/pl.md) ma teraz panel zadań i możliwe jest ustawienie ciepła dla kilku ciał lub użycie kilku wiązań dla różnych ciał w jednej analizie. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   Teraz można otwierać *(i w ten sposób wizualizować)* pliki \*.pvtu *(partycjonowane niestrukturalne dane siatki VTK)*. Plik \*.pvtu jest również wynikiem symulacji [Elmer](FEM_SolverElmer/pl.md), w której zastosowano więcej niż jeden rdzeń procesora. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Critical Strain Ratio został dodany do potoku wyników VTK. Daje wskazanie rozerwania ciągliwego dla materiałów z obiektem „MaterialMechanicalNonlinear". [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   Narzędzie <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [Siatka MES na obiekt środowiska Siatka](FEM_FemMesh2Mesh/pl.md) posiadx nowy parametr *Skala* umożliwiający określenie skali deformowanej siatki przy użyciu środowiska Python. [Wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) oraz [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715).



## Eksport



## Środowisko pracy Siatka 



### Planowane ulepszenie dla środowiska Siatka 

-   Wsparcie dla dodawania przezroczystości do siatki. [temat na Forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) oraz [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e)



## Planowane ulepszenie dla środowiska OpenSCAD 



## Środowisko pracy Część 



### Planowane ulepszenie dla środowiska Część 



## Środowisko pracy Projekt Części 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_1.0.png  style="width:384px;">Otwór z pogłębieniem stożkowym.   Okno dialogowe [Otwór](PartDesign_Hole.md) obsługuje typ łba śruby *stożkowej*. [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                                       
   



### Planowane ulepszenia dla środowiska Projekt Części 

-   W oknie dialogowym [Otwór](PartDesign_Hole/pl.md) usunięto przestarzałe typy łbów śrub *(łeb serowy, śruba kapiszonowa itp.)*. Były one przestarzałe od wersji FreeCAD 0.19. Otwory wykorzystujące te typy są przekształcane w niestandardowe pogłębiacze/otwory o średnicy i głębokości używanej przez typy. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   Polecenie [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md) zostało dodane do paska narzędzi Helper. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Usunięto z menu nieużyteczne polecenia [Zamknij edycje szkicu](Sketcher_LeaveSketch/pl.md) i [Widok szkicu](Sketcher_ViewSketch/pl.md). Polecenia [Edycja szkicu](Sketcher_EditSketch/pl.md), [Łączenie szkiców](Sketcher_MergeSketches/pl.md) i [Odbicie lustrzane szkicu](Sketcher_MirrorSketch/pl.md) zostały dodane do menu. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Narzędzie [Koło zębate ewolwentowe](PartDesign_InvoluteGear/pl.md) ma nowe właściwości do zmiany długości zębów. Umożliwia to teraz dostosowanie do pewnych typów zakłóceń i wykorzystanie profilu do tworzenia [involute splines](https://en.wikipedia.org/wiki/Spline_(mechanical)). [Pull request #8184](https://github.com/FreeCAD/FreeCAD/pull/8184).



## Środowisko pracy Path 

-   Integracja Camotics. Jeśli zainstalowana jest aplikacja Camotics *(wersja 1.2.2 lub nowsza)*, do paska narzędzi Path zostanie dodana nowa ikona. Wybierz zadanie Path i naciśnij przycisk, aby otworzyć okno dialogowe Camotics. Następnie przeciągnij suwak, aby wygenerować symulowaną bryłę w dowolnym punkcie zadania. Można również uruchomić pełną aplikację Camotics, aby uruchomić animowaną symulację. Powoduje to uzyskanie cichego post-processingu zadania i utworzenie pliku projektu camotics. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Dodatkowe łańcuchy zastępcze do automatycznego nazywania wyjść. Jeśli dane wyjściowe są dzielone na wiele plików, nazwy plików mogą automatycznie zastępować etykietę kontrolera narzędzi, WCS lub etykietę operacji. Jest to dodatek do innych istniejących ciągów zastępczych, takich jak data, nazwa zadania itp.

-   Zaimplementowana opcja łamania wiórów dla cykli wiercenia w stylu dziobania. Łamanie wiórów emituje cykl **G73**, który powoduje, że kontroler wykonuje bardzo mały ruch wycofania, aby złamać wiór bez pełnego wycofania wiertła z otworu. G73 jest obsługiwany natywnie przez środowisko LinuxCNC. Inne postprocesory będą musiały interpretować G73 i emitować odpowiednie kody kontroli lub dekomponować retrakcję na ruchy G1/G0. Wsparcie postprocesora dla dekompozycji G73 została dodana do „refaktoryzowanych" postprocesorów.[Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469)



## Środowisko pracy Plot 



## Środowisko pracy Szkicownik 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_1.0.gif  style="width:384px;">Przeciąganie węzłów krzywej złożonej.Kliknij na obrazek, aby zobaczyć animację.   Węzły krzywej złożonej mogą być teraz przeciągane i związane jak każdy inny punkt szkicu. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                                       
   

+++
| <img alt="" src=images/sketcher-move-piece_relnotes_1.0.gif  style="width:384px;">Przeciąganie krzywej złożonej. | Operacja przeciągania krzywej złożonej przesuwa teraz tylko część między węzłami. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110) |
| Kliknij na obrazek, jeśli animacja się nie uruchomi.                                                                                      |                                                                                                                                                      |
+++
|                                                                                                                                           |                                                                                                                                                      |
+++

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_1.0.gif  style="width:384px;">Kliknij na obrazek, aby zobaczyć animację.   Możliwość płynnej edycji szkiców zarówno z przodu jak i z tyłu. Podczas pracy od tyłu, wierzchołki *(oraz wszystkie geometrie i ograniczenia)* są jednakowo wybieralne, a widok przekroju jest przełączany automatycznie. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                      
   

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_1.0.gif  style="width:384px;">Kliknij na obrazek, aby zobaczyć animację.   Widżet Element został przerobiony w celu uproszczenia interfejsu użytkownika i umożliwienia prostszego wyboru różnych części każdej geometrii: Krawędź, punkt początkowy, punkt końcowy i punkt środkowy. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                  
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_1.0.gif  style="width:384px;">Kliknij na obrazek, aby zobaczyć animację.   Dodano narzędzie [Połącz krzywe](Sketcher_JoinCurves/pl.md). Może ono łączyć wiele krzywych w jedną krzywą złożoną. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                            
   



### Planowane ulepszenia dla środowiska Szkicownik 

-   Przycisk paska narzędzi [Wiązanie prawo Snella](Sketcher_ConstrainSnellsLaw/pl.md) został usunięty. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   [Wiązania wymiarów](Sketcher_Workbench/pl#Wi.C4.85zania_wymiar.C3.B3w.md) i pola wyboru wartości obsługują teraz tą samą matematykę co [wyrażenia](Expressions/pl.md) *(obliczane na bieżąco)*. [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   Przyciski paska narzędzi [Wybierz zbędne wiązania](Sketcher_SelectRedundantConstraints/pl.md) i [Wybierz wiązania konfliktowe](Sketcher_SelectConflictingConstraints/pl.md) zostały usunięte. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Przycisk paska narzędzi dla [Przerwij operację](Sketcher_StopOperation/pl.md) został usunięty. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   Sekcja \'Edycja kontrolek\' w oknie dialogowym szkicownika stała się opcjonalna. [Pull request #7572](https://github.com/FreeCAD/FreeCAD/pull/7572)
-   Usunięto przycisk paska narzędzi dla [Wybierz elementy bez wiązań](Sketcher_SelectElementsWithDoFs/pl.md). [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   Pasek narzędzi Szkicownika został podzielony na dwa: \"Tryb edycji szkicownika\" i \"Szkicownik\" *(czyli \"nie tryb edycji\")*. Paski narzędzi Szkicownika przeznaczone tylko do trybu edycji są ukryte w trybie nieedytowania, a te przeznaczone tylko do trybu nieedytowania są ukryte w trybie edycji. Pasek narzędzi Konstrukcja jest również ukryty w szkicowniku. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   [Wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md) może teraz działać jako wiązanie koncentryczne podczas wybierania 2 lub więcej okręgów, łuków, elips lub łuków elips. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703)
-   [Kalka techniczna](Sketcher_CarbonCopy/pl.md), jeśli to możliwe, używa teraz nazw wiązań w tworzonych przez siebie wyrażeniach zamiast odniesienia opartego na indeksie, dzięki czemu jest bardziej niezawodny. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)



## Środowisko pracy Arkusz Kalkulacyjny 



### Planowane ulepszenia dla środowiska Arkusz Kalkulacyjny 



## Środowisko pracy Rysunek Techniczny 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_1.0.png  style="width:250px;">   Dodano nowe narzędzie [Symbol wykończenia powierzchni](TechDraw_SurfaceFinishSymbol/pl.md) pozwalające na tworzenie symboli wykończenia powierzchni opisujących chropowatość, ułożenie i falistość, ale także oznaczających rodzaj obróbki powierzchni. Obsługuje ono zarówno style ISO jak i ASME. Jak pokazano na obrazku, istniejące narzędzie [Linia odniesienia](TechDraw_LeaderLine/pl.md) może być użyte do prawidłowego odniesienia zorientowanych symboli do krawędzi obiektu. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227)
  <img alt="" src=images/TechDraw_ComplexSection_relnotes_1.0.png  style="width:250px;">               Dodano narzędzie [Przekrój złożony](TechDraw_ComplexSection/pl.md) umożliwiające tworzenie półprzekrojów oraz ich przesuwania i wyrównywania. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
                                                                                                                      
   



### Planowane ulepszenia środowiska Rysunek Techniczny 

-   Tryby nawigacji zostały zaktualizowane, aby dopasować je do tych używanych w oknie widoku 3D. [Pull request #7081](https://github.com/FreeCAD/FreeCAD/pull/7081) i [Pull request #7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Poprawiono kreskowanie bitmapami. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) i [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121).
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

-   Dodano narzędzie [Otwór - pasowanie wału](TechDraw_HoleShaftFit/pl.md). [Pull request #8455](https://github.com/FreeCAD/FreeCAD/pull/8455)
-   Dodano narzędzie [Wymiar długości w aksonometrii](TechDraw_AxoLengthDimension/pl.md). [Pull request #8359](https://github.com/FreeCAD/FreeCAD/pull/8359)
-   Wymiary 3D mogą być teraz tworzone w taki sam sposób jak wymiary 2D usuwając konieczność ręcznego łączenia ich z geometrią 3D. Ponadto dodano narzędzie [Napraw wymiar](TechDraw_DimensionRepair/pl.md). [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)



## Środowisko pracy Web 



## Zewnętrzne środowiska pracy 



### Środowisko pracy A2plus 



### Środowisko pracy Złożenie 3 



### Środowisko pracy Złożenie 4 



### FCGear



### Środowisko pracy Statek 



## Kompilacja

Od tego wydania FreeCAD może być kompilowany tylko przy użyciu środowiska Qt 5.x i Python 3.x. Najniższa wspierana wersja środowiska Python to 3.8 zgodnie z [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

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

Jeśli środowisko pracy [Start](Start_Workbench.md) pokazuje tylko pustą stronę, musisz włączyć opcję **Użyj programowego OpenGL** w menu **Edycja→ Preferencje ... → Wyświetlanie**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/pl
