# <img alt="Ikonka FreeCAD dla Std: Narzędzia standardowe" src=images/Freecad.svg  style="width:64px;"> Std Base/pl






## Wprowadzenie

Środowisko pracy **Narzędzia standardowe** nie jest tak naprawdę środowiskiem pracy, ale raczej kategorią *podstawowych* poleceń i narzędzi, które mogą być używane we wszystkich środowiskach pracy.



## Przybory

Większość **narzędzi Głównych** jest dostępna z [menu standardowego](Standard_Menu/pl.md), i standardowy pasek narzędzi. Te, które są dostępne tylko poprzez pasek narzędzi lub menu kontekstowe, są wymienione w sekcjach [Struktura](#Structure_toolbar/pl.md) i [Narzędzia dodatkowe](#Narzędzia_dodatkowe.md) poniżej.



### Memu narzędzia Standardowe 

Istnieje siedem standardowych menu podrzędnych. Każde podmenu ma dedykowaną stronę. Wystarczy kliknąć na dowolną z poniższych nazw.


{{StdMenu
|
[Plik](Std_File_Menu/pl.md)
&nbsp;&nbsp;&nbsp;
[Edycja](Std_Edit_Menu/pl.md)
&nbsp;&nbsp;&nbsp;
[Widok](Std_View_Menu/pl.md)
&nbsp;&nbsp;&nbsp;
[Przybory](Std_Tools_Menu/pl.md)
&nbsp;&nbsp;&nbsp;
[Makrodefinicje](Std_Macro_Menu/pl.md)
&nbsp;&nbsp;&nbsp;
[Okna](Std_Windows_Menu/pl.md)
&nbsp;&nbsp;&nbsp;
[Pomoc](Std_Help_Menu/pl.md)
}}



### Menu Struktura 

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Utwórz Część](Std_Part/pl.md): Tworzy nową część i czyni ją aktywną.

-   <img alt="" src=images/Part_CoordinateSystem.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz geometrie odniesienia: 

  - <img alt="" src=images/Part_CoordinateSystem.svg  style="width:32px;"> [Utwórz układ współrzędnych odniesienia](Part_CoordinateSystem/pl.md): Tworzy obiekt układu współrzędnych, który może być zamocowany do innych obiektów. {{Version/pl|1.1}}

  - <img alt="" src=images/Part_DatumPlane.svg  style="width:32px;"> [Utwórz płaszczyznę odniesienia](Part_DatumPlane/pl.md): Tworzy obiekt płaszczyzny odniesienia, który może być zamocowany do innych obiektów. {{Version/pl|1.1}}

  - <img alt="" src=images/Part_DatumLine.svg  style="width:32px;"> [Utwórz linię odniesienia](Part_DatumLine/pl.md): Tworzy obiekt linii odniesienia, który może być zamocowany do innych obiektów. {{Version/pl|1.1}}

  - <img alt="" src=images/Part_DatumPoint.svg  style="width:32px;"> [Utwórz punkt odniesienia](Part_DatumPoint/pl.md): Tworzy obiekt punktu odniesienia, który może być zamocowany do innych obiektów. {{Version/pl|1.1}}

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Utwórz grupę](Std_Group/pl.md): Tworzy nową grupę.

-   <img alt="" src=images/Std_LinkMake.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Narzędzia Łączy:

  - <img alt="" src=images/Std_LinkMake.svg  style="width:32px;"> [Utwórz łącze](Std_LinkMake/pl.md): Tworzy łącze.

  - <img alt="" src=images/Std_LinkMakeRelative.svg  style="width:32px;"> [Utwórz łącze względne](Std_LinkMakeRelative/pl.md): Tworzy łącze obiektu podrzędnego lub elementu podrzędnego.

  - <img alt="" src=images/Std_LinkReplace.svg  style="width:32px;"> [Zastąp przez łącze](Std_LinkReplace/pl.md): Zastępuje obiekt nowym łączem, lub wiele obiektów łączami.

  - <img alt="" src=images/Std_LinkUnlink.svg  style="width:32px;"> [Usuń powiązanie](Std_LinkUnlink/pl.md): Zastępuje łącza powiązanymi z nimi obiektami.

  - <img alt="" src=images/Std_LinkImport.svg  style="width:32px;"> [Importuj łącza](Std_LinkImport/pl.md): Importuje wybrane łącza zewnętrzne.

  - <img alt="" src=images/Std_LinkImportAll.svg  style="width:32px;"> [Importuj wszystkie łącza](Std_LinkImportAll/pl.md): Importuje wszystkie łącza zewnętrzne.

-   <img alt="" src=images/Std_VarSet.svg  style="width:32px;"> [Utwórz zestaw zmiennych](Std_VarSet/pl.md): Tworzy zestaw właściwości, które mogą zostać użyte jako zmienne w [wyrażeniach](Expressions/pl.md). {{Version/pl|1.0}}



### Narzędzia dodatkowe 

-   <img alt="" src=images/Std_LinkMakeGroup.svg  style="width:32px;"> [Stwórz grupę łączy](Std_LinkMakeGroup/pl.md): Tworzy grupę łączy.

-   [Akcje z wyrażeniami](Std_Expressions/pl.md):

  - [Kopiuj wybrane](Std_Expressions/pl#Kopiuj_wybrane.md): kopiuje dane wyrażeń z wybranych obiektów do schowka.

  - [Kopiuj aktywny dokument](Std_Expressions/pl#Kopiuj_aktywny_dokument.md): kopiuje dane wyrażeń z aktywnego dokumentu do schowka.

  - [Kopiuj wszystkie dokumenty](Std_Expressions/pl#Kopiuj_wszystkie_dokumenty.md): kopiuje dane wyrażeń ze wszystkich dokumentów do schowka.

  - [Wklej](Std_Expressions/pl#Wklej.md): wkleja dane wyrażeń ze schowka.

-   <img alt="" src=images/Part_SelectFilter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> [Filtr wyboru](Part_SelectFilter/pl.md): {{Version/pl|1.0}}

  - <img alt="" src=images/Vertex-selection.svg  style="width:32px;"> [Wybór wierzchołków](Part_SelectFilter/pl#Wybór_wierzchołków.md):: Umożliwia wybór wyłącznie wierzchołków.

  - <img alt="" src=images/Edge-selection.svg  style="width:32px;"> [Wybór krawędzi](Part_SelectFilter/pl#Wybór_krawędzi.md): Umożliwia wybór wyłącznie krawędzi.

  - <img alt="" src=images/Face-selection.svg  style="width:32px;"> [Wybór ścian](Part_SelectFilter/pl#Wybór_ścian.md): Umożliwia wybór wyłącznie ścian.

  - <img alt="" src=images/Clear-selection.svg  style="width:32px;"> [Wszystkie filtry wyboru wyczyszczone](Part_SelectFilter/pl#Wszystkie_filtry_wyboru_wyczyszczone.md): Umożliwia wybór wszystkich elementów podrzędnych.

-   <img alt="" src=images/Std_TreeSelectAllInstances.svg  style="width:32px;"> [Wybierz wszystkie wystąpienia](Std_TreeSelectAllInstances/pl.md): Wybiera wszystkie wystąpienia obiektu w [widoku drzewa](Tree_view/pl.md).

-   <img alt="" src=images/Std_ToggleFreeze.svg  style="width:32px;"> [Włącz / wyłącz przeliczanie](Std_ToggleFreeze/pl.md): Przełącza stan zamrożenia obiektów. {{Version/pl|1.0}}



### Narzędzia przestarzałe 

-   <img alt="" src=images/View_Measure_Clear_All.svg  style="width:32px;"> [Usuń wszystkie pomiary widoku](View_Measure_Clear_All/pl.md): Usuwa pomiary [środowiska Część](Part_Workbench/pl.md). Niedostępne w {{VersionPlus/pl|1.0}}. Użyj [Std: Pomiary](Std_Measure/pl.md) zamiast tego.

-   <img alt="" src=images/View_Measure_Toggle_All.svg  style="width:32px;"> [Przełącz widoczność wymiarów](View_Measure_Toggle_All/pl.md): Przełącza widoczność wymiarów środowiska pracy Część. Niedostępne w {{VersionPlus/pl|1.0}}. Użyj [Std: Pomiary](Std_Measure/pl.md) zamiast tego.

-   <img alt="" src=images/Std_MeasureDistance.svg  style="width:32px;"> [Std: Wymiarowanie odległości](Std_MeasureDistance/pl.md): Tworzy obiekt do pomiaru i wyświetlania odległości. Niedostępne w {{VersionPlus/pl|1.0}}. Użyj [Std: Pomiary](Std_Measure/pl.md) zamiast tego.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Std Base/pl
