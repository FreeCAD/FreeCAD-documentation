# Release notes 0.22/pl
**FreeCAD 0.22 jest w trakcie rozwoju, nie ma jeszcze oczekiwanej daty wydania.**


{{Message|
Czy brakuje jakichś funkcji? Wspomnij o nich w wątku na forum [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;80197 Informacje o wydaniu v0.22].

Więcej informacji na temat sposobów przyczyniania się do rozwoju programu FreeCAD można znaleźć na stronie [Pomóż w rozwoju FreeCAD](Help_FreeCAD/pl.md).}}


{{Message|Wszystkie obrazy na tej stronie muszą używać przyrostka **_relnotes_0.22**.}}




**FreeCAD 0.22** zostanie wydany w roku *2024*, pobranie będzie możliwe ze strony [Pobieranie programu](Download/pl.md). Ta strona jest podsumowaniem najciekawszych zmian i funkcji.

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).

Miejsce na przyciągający wzrok obrazek wybrany przez adminów z [galerii pokazowej użytkowników](https://forum.freecadweb.org/viewforum.php?f=24).



## Informacje ogólne 



## Interfejs użytkownika 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_0.22.gif  style="width:320px;"> | Dodano wskaźnik środka obrotu. Wskaźnik ten jest wyświetlany po obróceniu widoku przez przeciągnięcie myszą. Opcjonalnie można go wyłączyć w preferencjach. Dostępne są również ustawienia koloru, przezroczystości i rozmiaru. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) oraz [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_0.22.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano filtry wyboru, ułatwiające wybór wierzchołków, krawędzi i ścian. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_0.22.png  style="width:320px;"> | Dla większej elastyczności panel zadań jest teraz samodzielnym widżetem z możliwością dokowania, ale stary układ jest domyślnie zachowany. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) oraz [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_0.22.png  style="width:320px;"> | Poprawiono wygląd przeciągacza narzędzia [Przemieszczenie](Std_TransformManip/pl.md). Narzędzie posiada teraz także zestaw planarnych uchwytów do przesuwania obiektów wzdłuż 3 domyślnych płaszczyzn. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_0.22.png  style="width:320px;"> | Dodano funkcję dewelopera Realthunder umożliwiającą nakładanie widżetów docka *(przezroczystość widoku drzewa i zadań)*. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_0.22.PNG  style="width:320px;"> | Położenie źródła światła można teraz ustawić w preferencjach (Preferencje \... → Wyświetlanie). [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_0.22.png  style="width:320px;"> | Okno preferencji zostało przeprojektowane, aby zastąpić zakładki widokiem drzewa. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++



### Pozostałe ulepszenia interfejsu użytkownika 

-   Wprowadzono układ jednostek projektu. [Pull request nr 9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   Narzędzie \[\[Part_SectionCut/pl\|Wycinek z przekroju

\]\] działa teraz również w widoku perspektywicznym. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143).

-   Dodano opcję sortowania środowisk pracy alfabetycznie *(dostępną po kliknięciu prawym przyciskiem myszy w Preferencje → Środowiska pracy)*.

[Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)

-   Filtr *Znajdź plik* i filtr *Znajdź w plikach* zostały dodane do okna dialogowego [Makrodefinicje](Std_DlgMacroExecute/pl.md). [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   [Menu Widok](Std_View_Menu/pl.md) i pasek narzędzi Widok zostały poprawione. [Pull request nr 10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   Przycisk stop został usunięty z [paska narzędzi Makro](Macros/pl.md). Przycisk [przycisk nagrywania](Std_DlgMacroRecord/pl.md) został teraz przełączony w przycisk zatrzymania, gdy trwa nagrywanie. [Pull request nr 10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   Przycisk resetowania w Preferencjach wyświetla teraz menu z opcjami resetowania ustawień na różnych poziomach: wszystkich, w bieżącej grupie lub w bieżącej zakładce. [Pull request nr 10688](https://github.com/FreeCAD/FreeCAD/pull/10688) i [Pull request nr 11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   Moduł pomocy został połączony, dzięki czemu nie jest już konieczne pobieranie dodatku, aby z niego korzystać. [Pull request nr 11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Dodano preferencje umożliwiające dostosowanie bieżącego motywu. [Pull request nr 10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Zmieniono domyślne ustawienia zaznaczania, aby ułatwić zaznaczanie obiektów w oknie widoku 3D. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   Dodano schemat jednostek tylko dla metrów o nazwie **Krotność dziesiętna metra**, ponieważ system MKS *(m/kg/s/stopień)* nie zawsze powoduje wyświetlanie wymiarów w metrach - milimetry są nadal używane dla wartości poniżej 0,1 m, podczas gdy w niektórych zastosowaniach *(np. inżynieria lądowa)* przydatny jest system jednostek, który faktycznie zmienia wyświetlanie wszystkich wymiarów na metry. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Dodano dodatkowe rozmiary znaczników *(20, 25 i 30px)* do *Preferencje \... → Wyświetlanie → Widok 3D → Rozmiar znacznika*, aby pomóc użytkownikom ekranów 4K. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   Dodano opcję \"Przełącz przezroczystość\" do menu widoku i menu kontekstowego, aby szybko włączyć lub wyłączyć przezroczystość dla wybranych obiektów. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)



## Rdzeń i API 



### Rdzeń programu 

-   Funkcje wektorowe pochodzące ze [skryptów](Vector_API/pl.md) mogą być teraz używane w [wyrażeniach](Expressions/pl.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   Lista plików w oknie dialogowym [Wykonaj makrodefinicję](Std_DlgMacroExecute/pl.md) może być teraz filtrowana zarówno według nazwy pliku, jak i jego zawartości. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/10714).
-   Edytor Python dopasowuje teraz wcięcie poprzedniej linii po naciśnięciu klawisza Enter. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/11356).



### API



#### Nowe skrypty Python 

-    {{Incode|getUpDirection}}: Pobiera kierunek w górę z widoku View3DInventor. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### Usunięte skrypty API 



## Menadżer dodatków 



## Środowisko pracy Architektura 



### Pozostałe ulepszenia środowiska Architektura 



## Środowisko pracy Rysunek Roboczy 

-   Dodano opcję wyrównania i kilka powiązanych właściwości do funkcji [Kształt z tekstu](Draft_ShapeString/pl.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Wymiar promieniowy](Draft_Dimension/pl#Zastosowanie_wymiaru_promieniowego.md) pokazuje teraz tylko pojedynczą strzałkę. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Właściwość Kąt nachylenia została dodana do [Kształt z tekstu](Draft_ShapeString/pl.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Dodano obsługę hiperłączy. Hiperłącza do lokalnych i zdalnych plików oraz adresów URL w [tekście](Draft_Text/pl.md) i [etykiecie](Draft_Label/pl.md) można otworzyć z ich menu kontekstowego [Widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md). [Pull request nr 10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   Kod [płaszczyzny roboczej](Draft_SelectPlane/pl.md) został przerobiony. W każdym widoku 3D istnieje teraz płaszczyzna robocza. [Pull request nr 11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   Udoskonalono funkcję historii i opcje wyrównywania polecenia [wybór płaszczyzny](Draft_SelectPlane/pl.md). [Pull request nr 11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   Poprawiono zachowanie [siatki](Draft_ToggleGrid.md). Jej widoczność jest teraz zapisywana dla każdego okna widoku 3D. Podczas przełączania do innego środowiska roboczego wszystkie siatki są ukryte parametr *([dostrajanie](Fine-tuning/pl.md) jest dostępny, aby wyłączyć tą nastawę)*. [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Poprawiono zachowanie [siatki](Draft_ToggleGrid/pl.md). Jej widoczność jest teraz zapisywana dla każdego widoku 3D. Podczas przełączania do innego środowiska pracy wszystkie siatki są ukryte *(dostępny jest parametr [fine-tuning](Fine-tuning/pl.md), aby to wyłączyć)*. [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Preferencje Draft zostały sprawdzone i poprawione. Niektóre preferencje zostały dodane, przestarzałe preferencje zostały usunięte. Strony w [Edytorze Preferencji](Preferences_Editor.md) mają nowy układ i pokazują jednostki tam, gdzie ma to zastosowanie. Ponowne uruchomienie FreeCAD po zmianie preferencji Draft nie jest już wymagane. [Żądanie ściągnięcia #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Żądanie ściągnięcia #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Żądanie ściągnięcia #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Żądanie ściągnięcia #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Żądanie ściągnięcia #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Żądanie ściągnięcia #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677) oraz [Żądanie ściągnięcia #11694](https://github.com/FreeCAD/FreeCAD/pull/11694).



### Pozostałe ulepszenia środowiska Rysunek Roboczy 

-   [Łącznik kształtu](Draft_Facebinder/pl.md) może teraz obsługiwać ściany należące do łączy i ściany zagnieżdżone w obiekcie [Część](Std_Part/pl.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Niektóre ustawienia zostały dodane do polecenia [Ustaw styl](Draft_SetStyle/pl.md). [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593) i [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)
-   Ustawienia zostały również dodane do polecenia [Zastosuj bieżący styl](Draft_ApplyStyle.md). [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610)
-   Przyciąganie, edycja i znaczniki śledzenia używają teraz preferencji [Promień kliknięcia](https://wiki.freecad.org/Preferences_Editor/pl#Widok_3D.md). [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688)



## Środowisko pracy MES 

+++
| <img alt="" src=images/FEM_legend_labels_relnotes_0.22.PNG  style="width:384px;"> | Dostosowano położenie etykiet legendy kolorów, aby zmniejszyć prawdopodobieństwo zakrycia górnych etykiet przez kostkę nawigacyjną. Zmieniono domyślną czcionkę i kolor etykiet, aby zwiększyć ich widoczność, a także dodano preferencje umożliwiające modyfikację koloru i rozmiaru etykiet. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_0.22.png  style="width:384px;"> | Polecenie [Wykres linearyzacji naprężeń](FEM_PostFilterLinearizedStresses/pl.md) może teraz używać skłądowych tensora naprężeń do obliczeń naprężeń zlinearyzowanych. Wcześniej można było używać tylko naprężeń Von Misesa, Tresca i głównych \'\'(głównych / pośrednich / małych). [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++



### Pozostałe ulepszenia środowiska MES 

-    **Model → Wiązania bez solwera**[\"wiązania bez solwera\"](FEM_Workbench/pl#Constraints_without_solver.md) zostały usunięte z GUI. The listed constraints could not be used. Nie można zastosować wymienionych wiązań.

-   Słowo \"wiązanie\" zostało usunięte z nazw i opisów większości funkcji w środowisku roboczym FEM, aby zapewnić prawidłowe nazewnictwo. Nazwy zostały zmienione w taki sposób, aby pasowały do standardów w branży analiz metodą elementów skończonych i były intuicyjne dla nowych użytkowników. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) i [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799).

-   Dodano nowe ikony dla [Standardowy solver CalculiX](FEM_SolverCalculixCxxtools/pl.md), [Kontrola pracy solvera](FEM_SolverControl/pl.md) i [Uruchom obliczenia solvera](FEM_SolverRun/pl.md) dla większej intuicyjności.

-   Solver CalculiX *(nowy framework)* został usunięty z GUI, ponieważ jest niedokończony i niepotrzebny w tej chwili. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823)

-   Poprawiono układ niektórych paneli zadań narzędzi do postprocessingu, aby zmniejszyć rozmiar zajmowanej przez nie poziomej przestrzeni. [Pull request nr 11066](https://github.com/FreeCAD/FreeCAD/pull/11066)

-   Panel zadań [Zdefiniuj temperaturę początkową](FEM_ConstraintTemperature/pl.md) został przerobiony, aby rozwiązać problemy występujące podczas edycji tej funkcji. [Pull request nr 11126](https://github.com/FreeCAD/FreeCAD/pull/11126)

-   Naprawiono stary problem polegający na tym, że [Flitr przycięcia linią](FEM_PostFilterDataAlongLine/pl.md) umożliwiał wykreślenie tylko wielkości, a nie składowych wektorowych wybranej zmiennej wyjściowej. [Pull request nr 10992](https://github.com/FreeCAD/FreeCAD/pull/10992)

-   [Obciążenie siłą](FEM_ConstraintForce/pl.md) i [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md) zostały przebudowane, aby lepiej działały po stronie kodu źródłowego. [Pull request nr 10935](https://github.com/FreeCAD/FreeCAD/pull/10935) i [Pull request nr 10923](https://github.com/FreeCAD/FreeCAD/pull/10923)

-   [Filtr danych w punkcie](FEM_PostFilterDataAtPoint/pl.md) ma teraz właściwość PointSize, która umożliwia ustawienie rozmiaru symbolu punktu w celu zwiększenia widoczności. [Pull request nr 11054](https://github.com/FreeCAD/FreeCAD/pull/11054)

-   Dla przejrzystości polecenie [Obszar siatki MES](FEM_MeshRegion/pl.md) zostało przemianowane w GUI na MES Ulepsz \\(nazwa polecenia w kodzie pozostała niezmieniona)\\. [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)

-   Dla jasności, w GUI polecenie [Obszar siatki](FEM_MeshRegion/pl.md) zostało przemianowane na *Ulepsz siatkę* *(nazwa polecenia pozostaje niezmieniona)*. [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)



## Eksport



### Materiał

+++
| <img alt="" src=images/Materials_relnotes_0.22.PNG  style="width:384px;"> | System obsługi materiałów, w tym edytor, został całkowicie przerobiony. W przyszłości nastąpią dalsze ulepszenia w tym zakresie. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_0.22.png  style="width:384px;"> | Dodano podgląd wyglądu, aby pokazać materiały w taki sam sposób, w jaki będą wyświetlane w dokumentach. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++



## Środowisko pracy Siatka 



### Pozostałe ulepszenia środowiska Siatka 



## Środowisko pracy OpenSCAD 



### Pozostałe ulepszenia środowiska OpenSCAD 



## Środowisko pracy Część 

+++
| <img alt="" src=images/Part_scale_relnotes_0.22.PNG  style="width:384px;"> | Dodano narzędzie [Skaluj](Part_Scale/pl.md), aby umożliwić łatwe skalowanie kształtów bez konieczności używania narzędzi ze środowiska Rysunku Roboczego. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_0.22.png  style="width:384px;"> | [Odbicie lustrzane](Part_Mirror/pl.md) Teraz obsługuje obiekty referencyjne, takie jak [płaszczyzna](Part_Plane/pl.md), aby zdefiniować dowolną płaszczyznę lustrzaną oprócz standardowych płaszczyzn XY, XZ i YZ. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Pozostałe ulepszenia środowiska Część 

-   Właściwość **Frenet** jest teraz domyślnie włączona dla narzędzia [Wyciągnięcie po ścieżce](Part_Sweep/pl.md), aby uniknąć powszechnego problemu z renderowaniem. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590).



## Środowisko pracy Projekt Części 

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_0.22.png  style="width:384px;"> | Ulepszono panel zadań funkcji [wyciągnięcie](PartDesign_Pad/pl.md) oraz [kieszeń](PartDesign_Pocket/pl.md) *(zmieniona kolejność elementów interfejsu użytkownika, opcja*Wybierz ścianę*pozostaje ukryta, gdy jest niepotrzebna itd.)*. [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_0.22.png  style="width:384px;"> | Tryb odsunięcia został dodany dla [szyku liniowego](PartDesign_LinearPattern/pl.md) i [szyku biegunowego](PartDesign_PolarPattern/pl.md). Poprzedni tryb został przemianowany na **Długość całkowita**.. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++



### Pozostałe ulepszenia środowiska Projekt Części 

-   Opcja *Stwórz grubość do wewnątrz* jest teraz domyślnie włączona dla narzędzia [Grubość](PartDesign_Thickness/pl.md). [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488).



## Środowisko pracy CAM 



### Pozostałe ulepszenia środowiska CAM 



## Środowisko pracy Wykres 



## Środowisko pracy Punkty 



### Pozostałe ulepszenia środowiska Punkty 



## Środowisko pracy Szkicownik 

+++
| <img alt="" src=images/Arc_helper_relnotes_0.22.png  style="width:384px;"> | Implementacja nakładki okręgu dla łuków (aby rozwiązać problem ograniczeń pojawiających się z dala od nich) została uzupełniona o polecenie ich przełączania. [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_0.22.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano kontekstowe wiązanie wymiaru, aby umożliwić szybkie i intuicyjne wymiarowanie za pomocą jednego wszechstronnego narzędzia. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_0.22.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Parametry narzędzia zostały dodane, aby umożliwić wymiarowanie w ruchu (podczas rysowania kształtów). W zależności od ustawienia preferencji On-View-Parameters, mogą one być wyłączone, ograniczone tylko do wymiarów (bez współrzędnych początkowych) lub w pełni włączone. Ponadto dodano tryby dla narzędzi kształtów. Można je wybrać za pomocą klawisza M lub listy rozwijanej w panelu zadań. Niektóre narzędzia mają dodatkowe ustawienia w postaci pól wyboru w panelu zadań i dodatkowych skrótów klawiaturowych. Obecnie nowe funkcje są dostępne dla punktów, linii, łuków, elips, prostokątów, wielokątów i szczelin. Prace nad nimi są w toku. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) i kolejne
   

+++
| <img alt="" src=images/Offset_relnotes_0.22.png  style="width:384px;"> | Dodano narzędzie [odsunięcia](Sketcher_Offset/pl.md), aby umożliwić przesunięcie krzywych. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_0.22.png  style="width:384px;"> | Tryb trzypunktowego [prostokąta](Sketcher_CompCreateRectangles/pl.md) został dodany w dwóch wersjach - trzy narożniki lub środek i dwa narożniki. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_0.22.png  style="width:384px;"> | Dodano narzędzie szczeliny na łuku z dwoma trybami *(końce łuku i płaskie końce)*, aby umożliwić tworzenie zakrzywionych szczelin [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_0.22.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano wiązanie poziome / pionowe. Automatycznie stosowane jest wiązanie poziome, jeśli linia jest bliższa orientacji poziomej lub ograniczenie pionowe, jeśli jest bliższa orientacji pionowej. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_0.22.png  style="width:384px;"> | Poprawiono renderowanie wiązań kąta i promienia. Wiązania kątowe mają teraz pełne linie przedłużające. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_0.22.png  style="width:384px;"> | Dodano narzędzie transformacji biegunowej, aby umożliwić obracanie i kołowe szyki geometrii szkicownika. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++



### Pozostałe ulepszenia środowiska Szkicownik 

-   Dodano tryb ramki dla narzędzia Prostokąt. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Dodano dwa nowe tryby dla narzędzia Linia: *Punkt, długość, kąt* i *Punkt, szerokość, wysokość*. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Zmieniono wygląd ikonek [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md) i [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md). Teraz ta pierwsza nie jest już tak podobna do [Utwórz kalkę techniczną](Sketcher_CarbonCopy/pl.md) i obie ikony przełączania zmieniają się po kliknięciu. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Ikony Szkicownika zostały przebudowane w celu ujednolicenia ich wyglądu *(szerokości obrysu, kolorów i rozmiarów punktów)*. [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785).
-   Wprowadzono opcjonalną *(domyślnie nieaktywną)* unifikację wiązań [zbieżności](Sketcher_ConstrainCoincident/pl.md) i [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)



## Środowisko pracy Arkusz Kalkulacyjny 



### Pozostałe ulepszenia środowiska Arkusz Kalkulacyjny 



## Środowisko pracy Start 

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_0.22.PNG  style="width:384px;"> | Na stronie startowej dodano sekcję **Nowy plik**, która zawiera szereg przycisków szybkiego uruchamiania. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_0.22.png  style="width:384px;"> | Projekt wizualny strony startowej został zmieniony. Wygląda teraz bardziej nowocześnie i spójnie. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++



### Pozostałe ulepszenia środowiska Start 

-   Strona preferencji Start Workbench została zreorganizowana. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520).
-   Dostępna jest teraz opcja \"\'Własny CSS\'\" dla strony startowej, która umożliwia dostosowanie stylu CSS strony startowej z poziomu preferencji środowiska Start. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520).
-   Usunięto preferencję **Ukryj paski przewijania**. Paski przewijania na stronie startowej są teraz stylizowane zgodnie z motywem i są znacznie cieńsze. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520).
-   Dostępne są teraz preferencje ukrywania i zmiany rozmiaru ikon miniatur plików na Stronie startowej. [Pull request #10410](https://github.com/FreeCAD/FreeCAD/pull/10410)



## Środowisko pracy Powierzchnia 3D 



### Pozostałe ulepszenia środowiska Powierzchnia 3D 



## Środowisko pracy Rysunek Techniczny 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_0.22.png  style="width:250px;"> | Narzędzie [Okrąg kosmetyczny](TechDraw_CosmeticCircle/pl.md) zostało dodane, aby umożliwić tworzenie geometrii pomocniczych w postaci okręgów poprzez wybranie środka i wprowadzenie promienia. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_0.22.PNG  style="width:250px;"> | Dodano narzędzie [Rozszerzenie Etykieta długości łuku](TechDraw_ExtensionArcLengthAnnotation/pl.md) do tworzenia wymiarowych adnotacji długości łuku wybranych krawędzi. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_0.22.png  style="width:250px;"> | Dodano narzędzie [Dodaj odsunięcie wierzchołka](TechDraw_CommandAddOffsetVertex/pl.md) do tworzenia wierzchołków kosmetycznych jako przesunięć od wybranych wierzchołków. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++



### Pozostałe ulepszenia środowiska Rysunek Techniczny 

-   Przekroje oparte na innych przekrojach używają teraz domyślnie oryginalnego *(nieprzyciętego)* kształtu. Można to zmienić w ustawieniach przekroju, aby zamiast tego użyć poprzedniego przekroju. [Pull request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281).
-   Obiekty kosmetyczne i linie środka można teraz usuwać, zaznaczając je i naciskając klawisz **Delete**. Wcześniej powodowało to usunięcie całego widoku. [Pull request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) oraz [Pull request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   Dodano nową, bardziej intuicyjną ikonę dla narzędzia [Symbol spawalniczy](TechDraw_WeldSymbol/pl.md). [Pull request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   Poprawiono zachowanie trybu punkt + krawędź narzędzia [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md). [Pull request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   Dodano sprawdzanie stanu dla przycisku [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md), aby użytkownik mógł zobaczyć, czy przycisk jest aktywny, czy nie. [Pull request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   Poprawiono zachowanie narzędzia [Zmień wygląd linii](TechDraw_DecorateLine/pl.md). Teraz dwukrotne kliknięcie linii wywołuje to narzędzie. Style linii są poprawnie przywracane, jeśli użytkownik naciśnie przycisk *Anuluj*. Wcześniej nie było różnicy między naciśnięciem przycisku *OK* i *Anuluj*. [Pull request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188).
-   Kolor i przezroczystość ścian można teraz ustawić dla każdego widoku. [Pull request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   Dodano tryb wielokrotnego wyboru, który można włączyć w Preferencjach. W tym trybie można wybrać wiele wierzchołków, krawędzi i ścian, klikając je lewym przyciskiem myszy, bez konieczności trzymania wciśniętego klawisza Ctrl. [Pull request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   [Rozszerzenie Oblicz obszar wybranych powierzchni](TechDraw_ExtensionAreaAnnotation.md) może teraz obliczać obszary dowolnych powierzchni. [Pull request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Linie nieciągłe będą teraz zgodne ze standardami ISO / ANSI zamiast stylu linii Qt. Dodano nową preferencję do wyboru standardu. [Pull request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   Poprawiono działanie narzędzia [Wstaw wymiar długości w aksonometrii](TechDraw_AxoLengthDimension/pl.md). Teraz, podczas wymiarowania krawędzi równoległych do osi globalnego układu współrzędnych, rzeczywista wartość *(3D)* jest obliczana automatycznie i wstawiana do właściwości Format Spec *(jako tekst)*. [Pull request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   Narzędzie [Rozszerzenie Wyrównaj widok przekroju](TechDraw_ExtensionPositionSectionView/pl.md) może być teraz używane poprzez wybranie krawędzi w widoku przekroju i wierzchołka w widoku źródłowym. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797).



## Środowisko pracy WEB 



### Pozostałe ulepszenia środowiska WEB 



## Kompilacja



## Znane ograniczenia



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.22/pl
