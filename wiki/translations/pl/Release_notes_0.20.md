# Release notes 0.20/pl




{{VeryImportantMessage|Ta strona zawiera nowe funkcje, które są dodawane do wersji deweloperskiej FreeCAD, aktualnie oznaczonej numerem '''0.20'''. Gdy nastąpi zamrożenie funkcjonalności wersji 0.20, usuń ten komunikat i nie dodawaj więcej funkcji do tej strony. Oczekuje się, że FreeCAD 0.20 zostanie wydany po roku 2021.}}


{{VeryImportantMessage|Wszystkie obrazy na tej stronie muszą używać przyrostka {{FileName|_relnotes_0.20}} !!!}}


<div style="text-align:center; background:#e0e0ee; margin:1em 7em; padding:0.5em 2em; border:2px solid #bb7736;">

Czy brakuje jakichś funkcji? Wspomnij o nich w wątku na forum [Informacje o wydaniu v0.20](https://forum.freecadweb.org/viewtopic.php?f=10&t=56135).

Zobacz artykuł [Pomóż w rozwoju FreeCAD](Help_FreeCAD.md), aby dowiedzieć się więcej na temat sposobów wspierania FreeCAD.


</div>


{{TOCright}}

**FreeCAD 0.19** zostanie wydany w roku *2020*, pobranie będzie mozliwe ze strony [Download](Download.md). Jest to podsumowanie najciekawszych zmian. Pełna lista zmian znajduje się w [MantisBT bugtracker FC 0.20 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78).

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).

## Najważniejsze informacje 

## Informacje ogólne 

### Python 3 oraz Qt5 

### Znane problemy 

### W rozwoju 

Aby przeprowadzić [kompilację w systemie Windows](Compile_on_Windows/pl.md), dostępne są różne Libpacki *(wstępnie spakowane biblioteki)*:

-   Libpack dla Windows z Qt xx, OCC yy, i Python zz

Inne wiadomości dotyczące rozwoju:

### Dokumentacja

### Znane problemy 

## Interfejs użytkownika 

+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Navi_Cube_relnotes_0.20.gif ) | Kostka nawigacyjna została przerobiona, aby umożliwić korzystanie z tych nowych funkcji:                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                | -   Istnieją teraz krawędzie umożliwiające oglądanie ujęcia pod kątem 45°.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | -   Nowa opcja [Obróć do najbliższego](Preferences_Editor/pl#Nawigacja.md) pozwala na oglądanie sceny w najbliższym sensownym stanie. Gdy jest ona wyłączona, kliknięcie na ścianę sześcianu spowoduje, że będzie ona zawsze w tej samej pozycji, niezależnie od tego, w jakiej pozycji kostki się znajdowałeś, gdy klikałeś na tę ścianę. Kliknij na obrazek po lewej stronie, aby zobaczyć, co to oznacza. Wypróbuj tę samą sekwencję kliknięć, jak na obrazku bez opcji *Obróć do najbliższego*, aby doświadczyć różnicy. |
|                                                                | -   Klikając na kropkę umieszczoną na górze po prawej stronie kostki, można szybko zobaczyć widok z tyłu aktualnego ujęcia.                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                | -   Rozmiar sześcianu można dostosować za pomocą opcji [Rozmiar kostki](Preferences_Editor/pl#Nawigacja.md).                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                | [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=52118), [pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

  -------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Improved_tooltips_relnotes_0.20.gif )   Tooltipy wyświetlają teraz nazwę polecenia w tytule, ułatwiając nowym użytkownikom szukanie pomocy. Na końcu podpowiedzi, pomiędzy nawiasami, użytkownik może również przeczytać *(Std\_WhatsThis)*, które dokładnie odpowiadają nazwie strony wiki. [dyskusja na Forum](https://forum.freecadweb.org/viewtopic.php?f=34&t=58747), [pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4978).
  -------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Std_UserEditMode_relnotes_0.20.gif )   Nowe polecenie [Std UserEditMode](Std_UserEditMode/pl.md) pozwala użytkownikowi wybrać tryb edycji, który będzie używany, gdy obiekt zostanie dwukrotnie kliknięty w [Widoku drzewa](Tree_view/pl.md). Jeśli wybrany tryb edycji nie ma zastosowania, zostanie użyty domyślny tryb edycji obiektu.
  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Dalsze ulepszenia interfejsu użytkownika 

-   Możliwe jest teraz przesuwanie widoku [dependency graph](Std_DependencyGraph.md) za pomocą myszy. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Naprawiono błąd, który powodował, że korzystanie z urządzeń wyposażonych w pióro (np. z tabletu Wacom) było powolne do tego stopnia, że było całkowicie nieużyteczne. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [pull request \#4687](https://github.com/FreeCAD/FreeCAD/pull/4687).

## Aplikacja::Łączenie i montaż 

## System podstawowy, App, baza i przestrzenie nazw GUI 

  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Object_selection_relnotes_0.20.png )   When using **Edit → Copy** or **Edit → Duplicate selection** for an object with dependencies there is a new **Use Original Selections** button in the object selection dialog. Click this button to copy/duplicate only the objects you originally selected prior to opening the dialog, ignoring dependencies and ignoring any actions you might have taken while the dialog was open, such as checking or unchecking some of the checkboxes. The effect is the same as if you had unchecked all the checkboxes next to the objects you did not originally select and pressed OK. Note: special care should be taken when copying/duplicating TechDraw Pages. It is recommended to also copy/duplicate all of the children of the Page (Templates, Views, Dimensions, etc.). Otherwise changes to one of the Pages will also impact the other page, for example, deleting one of the Views in one Page also removes it from the other Page. Deleting one of the pages will also remove all the content from the other Page if copies of the content are not also made.
  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Menadżer dodatków 

## Środowisko pracy Architektura 

## Środowisko pracy Rysunek Roboczy 

### Kolejne ulepszenia dla środowiska Rysunek Roboczy 

-   Jest teraz możliwe odwrócenie [linii łamanej](Draft_Wire/pl.md) poprzez menu kontekstowe [edycja](Draft_Edit/pl.md). [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [pull request \#4811](https://github.com/FreeCAD/FreeCAD/pull/4811).

## Środowisko pracy MES 

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width:384px;">Efekt funkcji *Rozmiar siatki na podstawie krzywizny*, po lewej: ustawiona na 12, po prawej: wyłączona                 Pojawiła się nowa właściwość generatora siatki [Gmsh](FEM_MeshGmshFromShape/pl.md). Można określić liczbę elementów siatki na $2\pi$ razy promień krzywizny. Domyślnie jest to 12 i aby uzyskać drobniejszą siatkę na małych rogach lub otworach, wartość ta może być zwiększona dla lepszych rezultatów. Ta funkcja wymaga wersji Gmsh 4.8 lub nowszej. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=56401), [pull request \#4596](https://github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width:384px;">Efekt działania algorytmu rekombinacji; po lewej: przy użyciu *Simple*, po prawej: przy użyciu *Simple full-quad*.   FreeCAD pozwala teraz wybrać algorytm, jak również metodę rekombinacji siatki 3D dla generatora siatek [Gmsh](FEM_MeshGmshFromShape/pl.md). Więcej szczegółów na temat rekombinacji elementów siatki można znaleźć na tej stronie [Rekombinacja elementów](FEM_MeshGmshFromShape/pl#Rekombinacja_element.C3.B3w.md). [Pull request \#4706](https://github.com/FreeCAD/FreeCAD/pull/4706)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Dalsze ulepszenia MES 

-   Kolejność elementów w generatorze siatek [Gmsh](FEM_MeshGmshFromShape/pl.md) może być zmieniona poprzez okno dialogowe siatki [PR \#4660](https://github.com/FreeCAD/FreeCAD/pull/4660).
-   Karty materiałowe mogą teraz zawierać wartości przewodności elektrycznej [PR \#4647](https://github.com/FreeCAD/FreeCAD/pull/4647).
-   Dodano karty materiałowe dla Azotu i Argonu [PR \#4649](https://github.com/FreeCAD/FreeCAD/pull/4649)
-   Dodano wsparcie dla [Gmsh](FEM_MeshGmshFromShape/pl.md) algorytmów siatkowych \"HXT\" *(3D)* i \"Packing Parallelograms\" *(2D)* [PR \#4654](https://github.com/FreeCAD/FreeCAD/pull/4654).
-   Umożliwiono ustawienie dla [Gmsh](FEM_MeshGmshFromShape#Properties/pl.md) właściwości **Optymalizacja wysokiego poziomu** określonego algorytmu [PR \#4705](https://github.com/FreeCAD/FreeCAD/pull/4705).

## Import

## Postępowanie z materiałami 

## Środowisko pracy Siatka 

### Planowane ulepszenia 

## Środowisko pracy OpenSCAD 

Ulepszono współdziałanie z OpenSCAD, dodając obsługę kilku operacji, których brakowało we wcześniejszych wersjach (wyciągnięcia liniowe z obrotem, wyciągnięcia obrotowe). Kilka operacji zostało zmodyfikowanych, aby zapewnić ulepszone odpowiedniki obiektów FreeCAD, szczególnie w przypadku skręconych wyciągnięć. Zmodyfikowano generowanie powierzchni z danych dyskretnych, aby uzyskać wyniki bardziej podobne do OpenSCAD, niż powierzchnie wielowypustowe.

**Add OpenSCAD element** - now has additional options

Load    - load a scad file
Save    - save a scad file
Refresh - Update FreeCAD view
Clear   - Clear text input

There is also a text box for feedback of OpenSCAD errors.

## Środowisko pracy Część 

### Planowane ulepszenia 

-   Okno dialogowe do edycji [walców](Part_Cylinder/pl.md) pozwala teraz na określenie kąta względem wektora normalnego wybranej płaszczyzny mocowania. W ten sposób można tworzyć przechylone walce. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)

## Środowisko pracy Projekt Części 

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Efekt działania nowej opcji *Długość wzdłuż wektora normalnego szkicu*.Kliknij na obrazek, aby wyświetlić animację.   Pojawiła się nowa opcja dopasowywania określonej długości wzdłuż kierunku. Długość jest mierzona wzdłuż wektora normalnego szkicu lub wzdłuż kierunku niestandardowego. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [pull request \#3893](https://github.com/FreeCAD/FreeCAD/pull/3893)
  <img alt="" src=images/PartDesign_Cylinder_direction.png  style="width:384px;">                                                                                                                                                                                Okno dialogowe do edycji [walca](PartDesign_AdditiveCylinder/pl.md) *(addytywny i subtraktywny)* pozwala teraz na określenie kąta względem wektora normalnego wybranej płaszczyzny mocowania. W ten sposób można tworzyć skośne walce. [pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Planowane ulepszenia 

-   Funkcja [Helisa](PartDesign_AdditiveHelix/pl.md) posiada nowy tryb **Wysokość - liczba obrotów - poszerzenie** do tworzenia płaskich spiral [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [PR \#4590](https://github.com/FreeCAD/FreeCAD/pull/4590)
-   Funkcja [Koło łańcuchowe](PartDesign_Sprocket/pl.md) może teraz tworzyć również koła łańcuchowe zgodne z normami ISO [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [PR \#4478](https://github.com/FreeCAD/FreeCAD/pull/4478)

## Środowisko pracy Path 

## Środowisko pracy Render 

## Środowisko pracy Szkicownik 

  --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/SketcherSplitExample2_relnotes_0.20.png )                                                  Nowa funkcja do ![](images/Sketcher_Split.svg  style="width:24px;"> [rozdzielania](Sketcher_Split/pl.md) istniejących linii lub łuków. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=9&t=55412) [pull request \#4420](https://github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample_relnotes_0.20.png )                  Nowe narzędzie ![](images/Sketcher_CreateOblong.svg  style="width:24px;"> [zaokrąglony prostopadłościan](Sketcher_CreateOblong/pl.md) do tworzenia prostokątów z zaokrąglonymi rogami. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main pull request \#4835](https://github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample_relnotes_0.20.png  style="width:384px;">   Nowe narzędzie <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:24px;">. [Centered rectangle](Sketcher_CreateRectangle_Center/pl.md) do definiowania prostokątów poprzez punkt środkowy. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim_relnotes_0.20.gif  style="width:384px;">                                                         Nowa funkcja <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Radiam](Sketcher_ConstrainRadiam/pl.md) do automatycznego przypisywania wagi do bieguna B-splajnu, średnicy do pełnego okręgu lub promienia do łuku. Obsługa wielokrotnego wyboru jako narzędzia średnicy / promienia. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Main pull request \#4855](https://github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult_relnotes_0.20.png )                          Nowe narzędzie ![](images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Usuń wyrównanie osi](Sketcher_RemoveAxesAlignment/pl.md) do usuwania wyrównania osi przy jednoczesnej próbie zachowania relacji wiązań zaznaczenia. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
  --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Planowane ulepszenia 

-   Zaktualizowana obsługa przycinania [Pull Request](https://github.com/FreeCAD/FreeCAD/pull/4330) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=10&t=54441) \<\-- Potrzebuje prezentacji ekranów
-   Zachowanie funkcji <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [rowek](Sketcher_CreateSlot/pl.md) uległo zmianie. Rowki mogą być teraz tworzone poprzez zdefiniowanie środka obu półokręgów. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4843) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   Automatyzacja widoczności pozwala na otwarcie Szkicownika w [trybie przekroju](Sketcher_ViewSection/pl.md) po wejściu do trybu edycji. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4742) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   Automatyzacja widoczności pozwala na wymuszenie pracy ujęcia widoku w [trybie ortogonalnym](Std_OrthographicCamera/pl.md) przy wejściu w tryb edycji. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4778) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44747)
-   Opcja wyświetlania nazwy wiązania wymiarowego i użycia dla niej niestandardowego formatu. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4966) [Dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?t=61153)
-   Podczas szkicowania [3-punktowego łuku](Sketcher_Create3PointArc/pl.md) z włączoną opcją automatycznego wiązania, [wiązanie stycznej](Sketcher_ConstrainTangent/pl.md) jest proponowane dla wszystkich 3 punktów podczas najechania na linię/krzywą. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4945) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=60596&p=520217#p520209).

### Poprawki błędów 

-   Naprawiono opcję „Odniesienie" niedziałającą dla promienia/średnicy w czasie tworzenia [PR dla promienia](https://github.com/FreeCAD/FreeCAD/pull/4744) [4832 PR dla średnicy](https://github.com/FreeCAD/FreeCAD/pull/) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584)

## Środowisko pracy Arkusz Kalkulacyjny 

-   W menu kontekstowym wiersza / kolumny można teraz wybrać, w jakich pozycjach będą wstawiane nowe wiersze / kolumny. Ponadto, przy zaznaczeniu kilku wierszy / kolumn, menu kontekstowe wiersza / kolumny oferuje teraz możliwość wstawienia tylu nowych wierszy / kolumn, ile zostało zaznaczonych. [pull request \#4704](https://github.com/FreeCAD/FreeCAD/pull/4704).

## Środowisko pracy Start 

## Środowisko pracy Surface 

## Środowisko pracy Rysunek Techniczny 

### Kolejne ulepszenia dla środowiska Rysunek Techniczny 

## Środowisko pracy Web 

## Moduły dodatkowe 

### Narzędzia do druku 3D 

### Środowisko pracy A2plus 

### Środowisko pracy Złożenie 3 

## Środowisko pracy Złożenie 4 

### Tekstury architektoniczne 

### BOLTSFC

### Środowisko pracy CurvedShapes 

### Środowisko pracy Dodo *(wcześniej Flamingo)* 

### Środowisko pracy Elementy Złączne 

### Środowisko pracy MeshRemodel 

### Środowisko pracy MOOC 

### NodeEditor *(PyFlow)* 

### Trails PyTrails, Turns oraz pivy\_trackers i Geomatics 

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)
