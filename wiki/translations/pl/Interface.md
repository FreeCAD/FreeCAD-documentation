# Interface/pl
{{TOCright}}

## Wprowadzenie

[Interfejs](interface.md) FreeCAD oparty jest na Qt, znanym graficznym zestawie narzędzi interfejsu użytkownika *(GUI)*, szczególnie używanym w Linuksie, ale dostępnym również w systemie Windows i MacOS.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Standardowy interfejs w wersji 0.19.*

Główne okno aplikacji można podzielić z grubsza na 11 sekcji:

1.  [Widok 3D](3D_view.md).
2.  W górnej części [Widok połączony](combo_view.md), który zawiera [Widok drzewa](tree_view.md) oraz [Panel zadań](task_panel.md).
3.  W dolnej części [Widoku połączonoeg](combo_view.md), jest do dyspozycji [Edytor właściwości](property_editor.md).
4.  [Widok wyboru opcji](selection_view.md).
5.  [Widok raportu](report_view.md).
6.  [Python console](Python_console.md).
7.  [Pasek stanu pracy](status_bar.md).
8.  Obszar paska narzędzi, zobacz następujące informacje na pasku narzędziowym
9.  [Przełącznik Środowiska pracy](Std_Workbench.md), który sam w sobie jest paskiem narzędzi.
10. [Menu standardowe](Standard_Menu.md).

## Elementy interfejsu użytkownika 

Podobnie jak wiele innych programów, FreeCAD zawiera standardowy pasek menu, a następnie serię pasków narzędzi i paneli, w których znajdują się narzędzia użytkownika.

### Menu

Dostępne są następujące menu [standardowe menu](Standard_Menu.md): {{StdMenu|[**Plik**](Std_File_Menu.md)}}, {{StdMenu|[**Edycja**](Std_Edit_Menu.md)}}, {{StdMenu|[**Widok**](Std_View_Menu.md)}}, {{StdMenu|[**Narzędzia**](Std_Tools_Menu.md)}}, {{StdMenu|[**Makro**](Std_Macro_Menu.md)}}, {{StdMenu|[**Okna**](Std_Windows_Menu.md)}}, {{StdMenu|[**Pomoc**](Std_Help_Menu.md)}}.

### Paski narzędzi 

Standardowe paski narzędzi, które pojawiają się w interfejsie to:

-   Pasek narzędzi do plików: narzędzia do pracy z plikami, otwierania dokumentów, kopiowania, wklejania, cofania i ponownego wykonywania czynności.
-   [Pasek narzędzi Środowiska pracy](Std_Workbench.md): zawiera jeden widżet do wyboru aktywnego [Środowiska pracy](workbenches.md).
-   Pasek narzędzi Makro: narzędzia do nagrywania, edycji i wykonywania [Makrodefinicji](macros.md).
-   Pasek narzędzi widoku: narzędzia do kontrolowania wyglądu obiektów w [Widok 3D](3D_view.md).
-   Pasek narzędzi struktury: narzędzia do organizowania obiektów w dokumencie i tworzenia łączy do dodatkowych dokumentów.

Można je włączyć i wyłączyć klikając prawym przyciskiem myszy na puste miejsce na jednym z pasków narzędzi i wybierając żądany element, lub z menu **Widok → Paski narzędzi**.

### Panele

Panelami głównymi, które umożliwiają pracę z obiektami są:

-   [Widok 3D](3D_view/pl.md): obszar, na którym narysowana jest geometria 2D i 3D.
-   [Widok połączony](Combo_view/pl.md): panel, który zawiera [widok drzewa](Tree_view/pl.md), [panel zadań](Task_panel/pl.md), oraz [edytor właściwości](Property_editor/pl.md).
-   [Widok drzewa](Tree_view/pl.md): element, który pokazuje wszystkie obiekty w dokumencie i ich historię parametryczną.
-   [Panel zadań](Task_panel/pl.md): panel, który pokazuje różne działania i opcje w zależności od wybranego narzędzia do rysowania.
-   [Edytor właściwości](Property_editor/pl.md): miejsce, w którym właściwości obiektu są modyfikowane.
-   [Widok wyboru](Selection_view/pl.md): panel, który pokazuje aktualnie wybrane elementy.
-   [Widok raportu](Report_view/pl.md): pole tekstowe, które pokazuje różne wiadomości z aplikacji i jej narzędzi.
-   [Konsola Pythona](Python_console/pl.md): edytor, który umożliwia interaktywne uruchamianie kodu [Python](Python/pl.md), aby zobaczyć wyniki bezpośrednio w [widoku 3D](3D_view/pl.md).
-   [Pasek statusu](Status_bar/pl.md): pasek, który pokazuje pewne komunikaty z aplikacji i posiada selektor [nawigacja myszy](Mouse_navigation/pl.md).
-   [Widok DAG](DAG_view/pl.md): alternatywa dla [Widok drzewa](Tree_view/pl.md), który pokazuje relacje pomiędzy różnymi obiektami za pomocą wykresu.

Z wyjątkiem widoku 3D, wszystkie te elementy można włączać i wyłączać klikając prawym przyciskiem myszy na puste miejsce w jednym z górnych pasków narzędzi i wybierając żądany element. Innym sposobem jest wybór menu **Widok → Panele**.

Aby aktywować i dezaktywować pasek stanu, użyj menu **Widok → Pasek stanu**.

### Pozostałe elementy 

Inne użyteczne interfejsy i okna zawierają:

-   [Inspektor sceny](Std_SceneInspector/pl.md): panel, który pokazuje węzły Coin3D tworzące [scenogram](Scenegraph/pl.md). Dla zaawansowanych użytkowników i programistów pomocne może być rozwiązywanie problemów związanych z bezpośrednią manipulacją sceną i obiektami utworzonymi w [widok 3D](3D_view/pl.md).
-   [Wykres zależności](Std_DependencyGraph/pl.md): okno pokazujące wykres zależności wszystkich obiektów w dokumencie, utworzonych za pomocą programu pomocniczego [Graphviz](https://graphviz.org/). Pomocne jest rozpoznanie problemów w tworzeniu obiektów, takich jak zależności kołowe, które mogą nie być całkowicie widoczne z [widok drzewa](Tree_view/pl.md) lub [widok DAG](DAG_view/pl.md).

### Możliwość dostosowania 

Paski narzędzi mogą mieć więcej lub mniej przycisków. Niestandardowe paski narzędzi można tworzyć w celu przygotowania mieszanki różnych narzędzi i przechowywania opracowanych makrodefinicji.

Opcje te znajdują się w menu, **Narzędzia → Dostosuj**. Patrz [Dostosowywanie interfejsu](Interface_Customization.md).


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface/pl
