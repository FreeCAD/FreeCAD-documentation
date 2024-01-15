# DAG view/pl
## Wprowadzenie




Widok DAG jest [skierowanym grafem acyklicznym](https://en.wikipedia.org/wiki/Directed_acyclic_graph) *(**D**irected **A**cyclic **G**raph)*, który pokazuje relacje między różnymi obiektami w dokumencie. Służy przede wszystkim do pokazania, w jaki sposób niektóre obiekty zależą od innych w złożonym modelu z wieloma funkcjami i odniesieniami, takimi jak te, które można utworzyć za pomocą środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Widok DAG przypomina graf, który można utworzyć z repozytorium Git i jego gałęzi. Wraz ze standardowym [widokiem drzewa](Tree_view/pl.md) i [grafem zależności](Std_DependencyGraph/pl.md), widok DAG jest narzędziem do sprawdzania parametrycznej historii obiektów w dokumencie.



## Przykład

Przedstawiony zostanie prosty model z różnymi widokami.

![](images/FreeCAD_DAG_view_3D.png ) 
*Modelowanie za pomocą kształtów 2D i 3D.*

<img alt="" src=images/FreeCAD_DAG_view_Tree_view.png ) ![](images/FreeCAD_DAG_view.png  style="width:" height="500px;">



*Po lewej: obiekty pokazane w standardowym [widoku drzewa](Tree_view/pl.md). Po prawej: obiekty pokazane w widoku DAG.*

![](images/FreeCAD_DAG_view_Std_DependencyGraph.png )



*Relacje między obiektami pokazanymi w [grafie zależności](Std_DependencyGraph/pl.md).*



## Aktywowanie widoku DAG 

Widok DAG został wprowadzony w wersji 0.17 jako funkcja eksperymentalna dla zaawansowanych użytkowników i programistów, aby mogli rozwiązywać problemy ze złożonymi modelami; dlatego widok DAG nie jest domyślnie dostępny.

Aby użyć tego widoku, użyj [edytora parametrów](Std_DlgParameter.md). Utwórz następującą podgrupę, jeśli jeszcze nie istnieje

-    `BaseApp/Preferences/DockWindows/DAGView`.

następnie dodaj parametr `Enabled` typu `Boolean`, i ustaw jego wartość na {{TRUE/pl}}.

Uruchom ponownie FreeCAD i aktywuj widok DAG: **{{StdMenu|[Widok](Std_View_Menu.md)** → Panele → Widok DAG}}.

W [edytorze parametrów](Std_DlgParameter/pl.md) można również zmienić niektóre właściwości w następującej podgrupie

-    `BaseApp/Preferences/DAGView`
    

-   FontPointSize - Ustawia rozmiar czcionki tekstu i może pomóc w czytelności na wyświetlaczach o wysokim DPI. Ustaw na 0 dla domyślnego rozmiaru czcionki.

-   SelectionMode
    -   0 - pojedyncze kliknięcie zaznacza element. Kliknięcie z wciśniętym klawiszem Ctrl dodaje elementy do zaznaczenia.
    -   1 - każde kliknięcie dodaje/usuwa element do zaznaczenia.

-   Direction - kolejność wyświetlania elementów.
    -   1 - element podrzędny na górze, element nadrzędny pod nim
    -   -1 - element nadrzędny na górze, dzieci pod nim



## Odnośniki internetowe 

-   [DAGView](https://forum.freecadweb.org/viewtopic.php?f=20&t=11276), wątek na forum prezentujący nowe narzędzie.
-   [pisanka PartDesign Next: widok DAG](https://forum.freecadweb.org/viewtopic.php?t=15375), obejmujący widok wraz z aktualizacją obiektu.


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > DAG view/pl
