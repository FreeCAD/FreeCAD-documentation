# <img alt="Ikonka FreeCAD dla środowiska pracy Złożenie 3" src=images/Assembly3_workbench_icon.svg  style="width   *64px;"> Assembly3 Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *24px;"> [Złożenie 3](Assembly3_Workbench/pl.md) jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md), które jest używane do wykonywania złożeń różnych części zawartych w jednym lub wielu dokumentach. Środowisko to bazuje na kilku zmianach funkcji rdzenia FreeCAD w wersji 0.19 *(np. [App Link](App_Link/pl.md))*. Dlatego środowisko Złożenie 3 nie może być używane ze starszymi wersjami programu.

Głównymi cechami środowiska **Złożenie 3** są   *

-   **dynamiczny/interaktywny solver**. Oznacza to, że możesz przesuwać części myszką, podczas gdy solver będzie ograniczał ruch. To pozwala na przykład, na połączenie koła z osią i interaktywne poruszanie kołem przy pomocy myszki.
-   **łącza**. To oznacza, że możesz używać pojedynczej części, np wkrętu, wielokrotnie w złożeniu *(w różnych miejscach)* bez kopiowania geometrii.
-   **łącza zewnętrzne**. Możliwe jest posiadanie dokumentu FreeCAD zawierającego tylko złożenie, a nie części. Każda z części może być osobnym plikiem. Pliki mogą znajdować się nawet w bibliotece lub gdziekolwiek indziej w systemie plików. Jedynym wymogiem jest to, że ten plik musi być załadowany, kiedy tworzone jest łącze. Po utworzeniu łącza, plik musi być otwarty to wykonywania aktualizacji łączy dotyczących tego pliku. Assembly3 rozwiązuje to przez otwieranie plików w tle, gdy jest to konieczne.
-   **złożenia hierarchiczne**. W prawdziwym życiu złożenia mechaniczne mogą składać się z złożeń podrzędnych. One mogą składać się z kolejnych złożeń podrzędnych, a te z kolejnych, itd.
-   **zamrażanie złożeń**. Jako, że procesor potrafi obsługiwać tylko określoną liczbą wiązań w czasie rzeczywistym, zamrażanie złożeń pozwala na używanie wiązań nawet do wielkich złożeń. Po zamrożeniu ukończonych złożeń lub wiązań, które nie muszą pozostać dynamiczne *(np. spawane, skręcane lub klejone części)* są one wyłączane z aktualizacji obliczeń i uznawane przez solver Złożenie 3 za ustaloną geometrię.

       *   Zauważ inne podejścia rozwiązujące ten problem odmiennie, np. środowisko <img alt="" src=images/Assembly4_workbench_icon.svg  style="width   *24px;"> [Złożenie 4](Assembly4_Workbench/pl.md).


{{top}}

### Paski narzędzi 

Środowisko Złożenie 3 zawiera następujące paski narzędzi - stan na rok 2020.

#### Główny pasek narzędzi 

   *   <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_Import.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_Move.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_Trace.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   **Główny Pasek Narzędzi** zawiera narzędzia, które obejmują najczęściej używane funkcje programu. Skróty klawiaturowe są podawane przez podpowiedzi narzędzi.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *32px;"> [Utwórz złożenie](Assembly3_CreateAssembly/pl.md)   * Dodaj folder montażu.

   ** <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width   *32px;"> [Grupuj obiekty](Assembly3_GroupObjects/pl.md)   * Grupuje obiekty.

   ** <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width   *32px;"> [Utwórz element](Assembly3_CreateElement/pl.md)   * Tworzye element.

   ** Import z formatu STEP. Posiada dwa ustawienia

   **\* <img alt="" src=images/Assembly_Import.svg‎‎  style="width   *32px;"> [Importuj z formatu STEP](Assembly3_ImportFromSTEP/pl.md)   * Import plików w formacie STEP.

   **\* <img alt="" src=images/Assembly_ImportMulti.svg‎‎  style="width   *32px;"> [Importuj wiele dokumentów](Assembly3_ImportMultiDocument/pl.md)   * Import zespołów z dokumentu STEP do osobnych dokumentów.

   ** <img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width   *32px;"> [Rozwiąż wiązania](Assembly3_ResolveConstraints/pl.md)   * Rozwiązuje wiązania.

   ** <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width   *32px;"> [Rozwiąż szybko](Assembly3_QuickSolve/pl.md)   * Wstępnie rozwiązuje wiązania.

   ** <img alt="" src=images/Assembly_Move.svg‎‎  style="width   *32px;"> [Przenieś część](Assembly3_MovePart/pl.md)   * Przesuwanie części w przestrzeni 3D, jest to specyficzne dla środowiska Złożenie3.

   ** <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width   *32px;"> [Przesunięcie osiowe](Assembly3_AxialMove/pl.md)   * Przesuwanie w osi części w przestrzeni 3D, jest to klasyczne narzędzie dostępne w innych miejscach programu FreeCAD.

   ** <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width   *32px;"> [Szybkie przesunięcie](Assembly3_QuickMove/pl.md)   * Spowoduje to dołączenie części zaznaczonej w drzewie do kursora myszki. Przy kliknięciu zmieni pozycję części.

   **   * Często dodawane części są ułożone jedna na drugiej w miejscu początkowym. Użyj tej funkcji, aby chwycić część, której nie widzisz.

   ** <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width   *32px;"> [Zablokuj przesunięcie](Assembly3_LockMover/pl.md)   * Blokada ruchu dla ustalonej części. Przycisk przełączający. Gdy nie jest aktywny, można przesuwać części, które mają wiązanie \"Zablokowane\".

   ** <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width   *32px;"> [Przełącz widoczność części](Assembly3_TogglePartVisibility/pl.md)   * Włącza/wyłącza wyświetlanie wybranej części.

   **   * Należy zauważyć, że funkcja ta różni się od użycia klawisza **Space**. Użycie spacji z wybranymi elementami podzespołu w widoku 3D często nie zachowuje się zgodnie z oczekiwaniami. W takich przypadkach należy użyć tej funkcji *(lub skrótu **A** + **Space**)*.

   ** <img alt="" src=images/Assembly_Trace.svg‎‎  style="width   *32px;"> [Śledzenie ruchu części](Assembly3_TracePartMove/pl.md)   * Śledzenie ruchu części *(do ustalenia)*.

   ** <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width   *32px;"> [Przelicz automatycznie](Assembly3_AutoRecompute/pl.md)   * Automatyczne ponowne obliczanie. Zazwyczaj włączone.

   **   * Może być odznaczone podczas naprawiania wiązań lub naprawiania części, gdy solver daje komunikat *nie zbiega się* *(np. przez obrócenie części o 180 stopni)*.

   ** <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width   *32px;"> [Inteligentne przeliczanie](Assembly3_SmartRecompute/pl.md)   * Inteligentne ponowne obliczanie. Zazwyczaj włączone.

   ** <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width   *32px;"> [Napraw element automatycznie](Assembly3_AutoFixElement/pl.md)   * Automatyczne naprawianie elementów. Funkcja eksperymentalna w wersji 0.19\_pre.

   ** Styl elementu. Ma on dwa ustawienia

   **\* <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width   *32px;"> [Automatyczna widoczność elementów](Assembly3_AutoElementVisibility/pl.md)   * Automatyczne ustawianie widoczności elementów.

   **\* <img alt="" src=images/Assembly_ShowElementCS.svg‎‎  style="width   *32px;"> [Wyświetl układ współrzędnych elementu](Assembly3_ShowElementCS/pl.md)   * Wyświetla układ współrzędnych elementu.

   ** Płaszczyzna robocza i punkt odniesienia. Dodaje płaszczyznę roboczą, położenie lub punkt odniesienia. Część musi być wybrana. Opcja ta ma pięć ustawień.

   **\* <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width   *32px;"> [Dodaj płaszczyznę roboczą XY](Assembly3_AddWorkplane/pl.md)   * Dodaje płaszczyznę roboczą w płaszczyźnie.

-   -   <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width   *32px;"> [Dodaj płaszczyznę roboczą XZ](Assembly3_AddWorkplane/pl.md)   * Dodaje płaszczyznę roboczą.

   **\* <img alt="" src=images/Assembly_Add_WorkplaneZY.svg‎‎  style="width   *32px;"> [Dodaj płaszczyznę roboczą ZY](Assembly3_AddZYWorkplane/pl.md)   * Dodaje płaszczyznę roboczą w płaszczyźnie YZ.

   **\* <img alt="" src=images/Assembly_Add_Placement.svg‎‎  style="width   *32px;"> [Dodaj umiejscowienie](Assembly3_AddPlacement/pl.md)   * Dodaje umiejscowienie.

   **\* <img alt="" src=images/Assembly_Add_Origin.svg‎‎  style="width   *32px;"> [Dodaj odniesienie położenia](Assembly3_AddOrigin/pl.md)   * Dodaje odniesienie położenia.

   ** <img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width   *32px;"> [Przenieś pozycję w górę](Assembly3_MoveItemUp/pl.md)   * Przesuwa wybrany element na drzewie w górę.

   ** <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width   *32px;"> [Przenieś pozycję w dół](Assembly3_MoveItemDown/pl.md)   * Przesuwa wybrany element na drzewie w dół.

   **   * Umożliwia sortowanie Części, Elementów lub Wiązań w drzewie. Przewijanie elementów *(z góry na dół i odwrotnie)*. Działa tylko dla pojedynczego zaznaczenia.

   ** <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width   *32px;"> [Pomnóż więz](Assembly3_MultiplyConstraint/pl.md)   * Mnożenie wiązań. Można go wybrać, jeśli występuje wiele części i odpowiednich elementów.

   **   * Używa się go np. do przypisania wielu elementów złącznych tego samego typu do wielu otworów za pomocą jednego wiązania.


</div>


</div>

#### Główny pasek wiązań 

   *   <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   Niektóre narzędzia są w rzeczywistości menu dla kolejnych przyborów.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *32px;"> [Wiązanie zablokowania](Assembly3_ConstraintLock/pl.md)   * Dodaj wiązanie **Zablokowania**, aby zablokować jedną lub więcej części.

   **   * Musisz wybrać element geometrii części.

   **   * Jeśli unieruchomisz wierzchołek lub krawędź, część nadal może swobodnie obracać się wokół tego wierzchołka lub krawędzi.

   **   * Zablokowanie ściany spowoduje całkowite zablokowanie części.

   ** <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width   *32px;"> [Wiązanie wyrównania](Assembly3_ConstraintAlignment/pl.md)   * Dodaj wiązanie **Wyrównania płaszczyzn**, aby wyrównać płaszczyzny dwóch lub więcej części.

   **   * Powierzchnie czołowe stają się koplanarne lub równoległe z opcjonalną odległością.

   ** <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *32px;"> [Wiązanie zbieżności](Assembly3_ConstraintCoincidence/pl.md)   * Dodaj wiązanie \"Zbieżność płaszczyzn\", aby płaszczyzny dwóch lub więcej części były zbieżne.

   **   * Ściany są zbieżne w swoich środkach z opcjonalną odległością.

   ** <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *32px;"> [Wiązanie umocowania](Assembly3_ConstraintAttachment/pl.md)   * Dodaj wiązanie **Umocowania**, aby połączyć dwie części za pomocą wybranych elementów geometrii.

   **   * To wiązanie całkowicie unieruchamia części względem siebie.

   ** <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width   *32px;"> [Wiązanie wyrównanie do osi](Assembly3_ConstraintAxial.md)   * Dodaj wiązanie \"wyrównanie osiowe\", aby wyrównać krawędzie/ściany dwóch lub więcej części.

   **   * To wiązanie akceptuje.

   **   *   * krawędzie liniowe, które stają się współliniowe,

   **   *   * powierzchnie płaskie, które są wyrównywane przy użyciu osi normalnej ich powierzchni,

   **   *   * i powierzchnie cylindryczne, które są wyrównywane za pomocą kierunku osiowego.

   **   * Różne typy elementów geometrii mogą być mieszane.

   ** <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width   *32px;"> [Wiązanie identycznej orientacji](Assembly3_ConstraintSameOrientation/pl.md)   * Dodaj wiązanie \"Ta sama orientacja\", aby wyrównać powierzchnie dwóch lub więcej części.

   **   * Płaszczyzny są wyrównane, aby miały tę samą orientację *(tj. obrót)*.

   ** <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width   *32px;"> [Wiązanie wielu równoległości](Assembly3_ConstraintMultiParallel/pl.md)   * Dodaj wiązanie **Wielo równoległe**, aby powierzchnie płaskie lub krawędzie liniowe dwóch lub więcej części były równoległe.

   ** <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width   *32px;"> [Wiązanie kąta](Assembly3_ConstraintAngle/pl.md)   * Dodaj wiązanie **Kąta**, aby ustawić kąt powierzchni płaskich lub krawędzi liniowych dwóch części.

   ** <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width   *32px;"> [Wiązanie prostopadłości](Assembly3_ConstraintPerpendicular/pl.md)   * Dodaj wiązanie \"prostopadłe\", aby płaszczyzny lub krawędzie liniowe dwóch części były prostopadłe.

   ** <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width   *32px;"> [Wiązanie zbieżności punktów](Assembly3_ConstraintPointsCoincident/pl.md)   * Dodaj wiązanie \"Zbieżność punktów\", aby zrównać dwa punkty w przestrzeni 2D lub 3D.

   ** <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width   *32px;"> [Wiązanie punkt na płaszczyźnie](Assembly3_ConstraintPointInPlane/pl.md)   * Dodaj **Punkt na płaszczyźnie**, aby powiązać jeden lub więcej punktów z płaszczyzną.

   ** <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *32px;"> [Wiązanie punkt na linii](Assembly3_ConstraintPointOnLine/pl.md)   * Dodaj **Punkt na linii**, aby powiązać punkt z linią w przestrzeni 2D lub 3D.

   ** <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width   *32px;"> [Wiązanie punkt na okręgu](Assembly3_ConstraintPointOnCircle/pl.md)   * Dodaj \'\'\'Punkt na okręgu\", aby powiązać jeden lub więcej punktów z powierzchnią współśrodkową zdefiniowaną przez okrąg.

   **   * Zauważ, że musisz wybrać punkt *(każdy element geometrii może zdefiniować punkt)*, a następnie wybrać okrąg *(lub powierzchnię clyndryczną)*,

   **   * Po czym możesz dodać więcej punktów do zaznaczenia, jeśli chcesz.

   ** <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width   *32px;"> [Wiązanie odległości punktów](Assembly3_ConstraintPointsDistance/pl.md)   * Dodaj **Odległość punktów**, aby ustalić odległość dwóch lub więcej punktów.

   ** <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width   *32px;"> [Wiązanie odległość punktu od płaszczyzny](Assembly3_ConstraintPointPlaneDistance/pl.md)   * Dodaj \"Odległość punkt-płaszczyzna\", aby ustalić odległość pomiędzy jednym lub więcej punktami a płaszczyzną.

   ** <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width   *32px;"> [Wiązanie odległości punktu od linii](Assembly3_ConstraintPointLineDistance/pl.md)   * Dodaj **Odległość linii punktu**, aby określić odległość między punktem a krawędzią liniową w przestrzeni 2D lub 3D.

   ** <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width   *32px;"> [Wiązanie symetrii](Assembly3_ConstraintSymmetric/pl.md)   * Dodaj wiązanie \"Symetrii\", aby elementy geometrii z dwóch części były symetryczne względem płaszczyzny.

   **   * Obsługiwane elementy to krawędź liniowa i ściana planarna.

   ** <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width   *32px;"> [Więcej wiązań](Assembly3_ConstraintMore/pl.md)   * Przełącz paski narzędzi, aby uzyskać więcej wiązań

   **   * Tak naprawdę nie jest to żadne wiązanie, ale przełącznik pokazujący / ukrywający **Paski narzędzi dodatkowych wiązań**.


</div>


</div>

#### Dodatkowe paski narzędziowe wiązań 

   *   <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width   *28px;"> (Assembly3 Constraints2)





   *   <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width   *28px;"> (Assembly3 Sketch Constraints)


<div class="mw-collapsible mw-collapsed">


   *   Możesz je uruchomić przez wybranie przycisku **<img src="images/Assembly_ConstraintMore.svg‎‎" width=16px> [More](Assembly3_ConstraintMore/pl.md)** na Głównym pasku narzędzi.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width   *32px;"> [Odległość punktu](Assembly3_ConstraintPointDistance/pl.md)   * Dodaj **Odległość punktu**, aby ograniczyć odległość dwóch punktów w przestrzeni 2D lub 3D.

   ** <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width   *32px;"> [Równy kąt](Assembly3_ConstraintEqualAngle/pl.md)   * Dodaj \"Kąt równy\", aby zrównać kąty między dwiema liniami lub wektorami normalnej.

   ** <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width   *32px;"> [Symetria punktów](Assembly3_ConstraintPointsSymmetric/pl.md)   * Dodaj wiązanie \"Symetria punktów\", aby uczynić dwa punkty symetrycznymi względem płaszczyzny.

   ** <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *32px;"> [Symetria pozioma](Assembly3_ConstraintSymmetricHorizontal/pl.md)   * Symetrycznie poziomo.

   ** <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *32px;"> [Symetria pionowa](Assembly3_ConstraintSymmetricVertical/pl.md)   * Symetrycznie pionowo.

   ** <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width   *32px;"> [Symetria linii](Assembly3_ConstraintSymmetricLine/pl.md)   * Dodaj wiązanie **Symetria linii**, aby uczynić dwa punkty symetrycznymi względem linii.

   ** <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width   *32px;"> [Punkty poziomo](Assembly3_ConstraintPointsHorizontal/pl.md)   * Dodaj wiązanie **Punkty poziomo**, aby dwa punkty były względem siebie poziome podczas rzutowania na płaszczyznę.

   ** <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width   *32px;"> [Punkty pionowo](Assembly3_ConstraintPointsVertical/pl.md)   * Dodaj wiązanie **Punkty pionowo**, aby dwa punkty były względem siebie pionowe podczas rzutowania na płaszczyznę.

   ** <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width   *32px;"> [Linia poziomo](Assembly3_ConstraintLineHorizontal/pl.md)   * Dodaj wiązanie **Linia poziomo**, aby segment linii był poziomy podczas rzutowania na płaszczyznę.

   ** <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width   *32px;"> [Linia pionowo](Assembly3_ConstraintLineVertical/pl.md)   * Dodaj wiązanie **Linia pionowo**, aby segment linii był pionowy podczas rzutowania na płaszczyznę.

   ** <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width   *32px;"> [Stycznie do linii łuku](Assembly3_ConstraintArcLineTangent/pl.md)   * Dodaj wiązanie \"Stycznie do linii łuku\", aby linia była styczna do łuku w punkcie początkowym lub końcowym łuku.

   ** <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width   *32px;"> [Płaszczyzna szkicu](Assembly3_ConstraintSketchPlane/pl.md)   * Dodaj **Płaszczyznę szkicu**, aby zdefiniować płaszczyznę roboczą dowolnego elementu szkicu znajdującego się wewnątrz lub za tym wiązaniem.

   **   * Dodaj pustą **Płaszczyznę szkicu**, aby przedefiniować poprzednią płaszczyznę roboczą.

   ** <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width   *32px;"> [Długość linii](Assembly3_ConstraintLineLength/pl.md)   * Dodaj **Długość linii** określająca długość nie podzielonego Draft.Wire.

   ** <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width   *32px;"> [Równa długość](Assembly3_ConstraintEqualLength/pl.md)   * Dodaj ograniczenie **Równa długość**, aby utworzyć dwie linie o tej samej długości.

   ** <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width   *32px;"> [Stosunek długości](Assembly3_ConstraintLengthRatio/pl.md)   * Dodaj **Proporcje długości**, aby ustalić stosunek długości dwóch linii.

   ** <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width   *32px;"> [Różnica w długości](Assembly3_ConstraintLengthDifference/pl.md)   * Dodaj **Różnicę długości**, aby określić różnicę długości dwóch linii.

   ** <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width   *32px;"> [Odległość punktu równa długości linii](Assembly3_ConstraintLengthEqualPointLineDistance/pl.md)   * Dodaj **Długość równa odległości punktu od linii**, aby określić odległość

   **   * między punktem a prostą, aby była taka sama jak długość innej prostej.

   ** <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *32px;"> *(<img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width   *32px;"> )* [równa długość linii i łuku](Assembly3_ConstraintEqualLineArcLength/pl.md)   * Dodaj więzienie \"Równa długość łuku i linii\", aby linia miała taką samą długość jak łuk.

   ** <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width   *32px;"> [Punkt środkowy](Assembly3_ConstraintMidPoint/pl.md)   * Dodaj **Punkt środkowy**, aby przypisać punkt do punktu środkowego linii.

   ** <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width   *32px;"> [Średnica](Assembly3_ConstraintDiameter/pl.md)   * Dodaj **Średnicę**, aby ustalić średnicę okręgu / łuku.

   ** <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width   *32px;"> [Równy promień](Assembly3_ConstraintEqualRadius/pl.md)   * Dodaj wiązanie **Równy promień**, aby utworzyć dwa okręgi / łuki o tym samym promieniu.

   ** <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width   *32px;"> [Projekt odległości punktów](Assembly3_ConstraintPointsProjectDistance/pl.md)   * Dodaj **Projekt odległości punktów**, aby ustalić odległość dwóch punktów rzutowanych na prostą.

   ** <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width   *32px;"> [Równa odległość punktu i linii](Assembly3_ConstraintEqualPointLineDistance/pl.md)   * Dodaj \"Równa odległość punktu od linii\", aby ustalić odległość

   **   * między punktem a prostą, aby była taka sama jak odległość między innym punktem a prostą.

   ** <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width   *32px;"> [Współliniowo](Assembly3_ConstraintColinear/pl.md)   * Dodaj wiązanie **Współliniowo**, aby uczynić dwie linie współliniowymi.


</div>


</div>


   *   **Paski Narzędzi Wiązań** będą głównym interfejsem używanym podczas składania części.
   *   Są one domyślnie nie aktywe, i zostają aktywowane gdy przynajmniej jedna ściana, linia lub punkt części jest wybrana.
   *   Ogólnie wybierasz Elementy, które powinny zostać połączone a następnie wybierasz typ wiązania.
   *   Ramki w różnych barwach oznaczają różną charakterystykę wiązań   *

       *   czy to 2D / 3D albo czy więcej niż dwa Elementy mogą zostać dodane.
   *   Dokładny opis znajduje się w Wiki Githuba.

#### Pasek narzędzi nawigacji 


<div class="mw-collapsible mw-collapsed">


   *   Te funkcje są przydatne podczas pracy ze złożeniem z hierarchią połączonych plików zewnętrznych


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width   *32px;"> [Przejdź do zależności](Assembly3_GoToRelation/pl.md)   * Ujawnia grupę Zależności *(domyślnie ukryta)* i wybiera obiekt zależny.

   ** <img alt="" src=images/Std_LinkSelectLinked.svg  style="width   *32px;"> [Wybierz połączone odnośnikami](Std_LinkSelectLinked/pl.md)   * Zaznacza połączony obiekt i przełącza do jego dokumentu. {{Version/pl|0.19}}

   ** <img alt="" src=images/Std_LinkSelectLinkedFinal.svg  style="width   *32px;"> [Wybierz najgłębiej połączony obiekt](Std_LinkSelectLinkedFinal/pl.md)   * Wybiera najgłębiej powiązany obiekt i przełącza się na jego dokument. {{Version/pl|0.19}}


</div>


</div>

#### Pasek narzędzi pomiarowych 

   *   <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   Pasek narzędzi **Wymiarowanie** dodaje funkcje do mierzenia odległości lub kąta między dwoma obiektami.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width   *32px;"> [Pomiar odległości punktów](Assembly3_MeasurePoints/pl.md)   * Dodaj **Pomiar odległości punktów**, aby zmierzyć odległość dwóch punktów w przestrzeni 2D lub 3D.

   ** <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width   *32px;"> [Pomiar odległości punktu od krawędzi](Assembly3_MeasurePointLine/pl.md)   * Dodaj **Pomiar odległości punktu od linii**, aby zmierzyć odległość między punktem a linią krawędzi w przestrzeni 2D lub 3D.

   ** <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width   *32px;"> [Pomiar odległości punktu od płaszczyzny](Assembly3_MeasurePointPlane/pl.md)   * Dodaj **Pomiar odległości punktu od płaszczyzny**, aby zmierzyć odległość między punktem a płaszczyzną.

   ** <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width   *32px;"> [Pomiar kąta](Assembly3_MeasureAngle/pl.md)   * Dodaj **Pomiar kąta**, aby zmierzyć kąt między powierzchniami płaskimi lub krawędziami liniowymi dwóch części.

   *   Nie ma funkcji do pomiaru promienia lub średnicy.
   *   Narzędzia pomiarowe są odporne na modyfikacje części, np. odległość między krawędziami sześcianu po zmianie jego rozmiaru.
   *   Jako wiązania, obliczenia są wykonywane w czasie rzeczywistym i aktualizowane przy każdej zmianie. Za kulisami, funkcja jest bardzo podobna do [wiązań](#Wi.C4.85zania.md). Odległość lub kąt jest obliczany pomiędzy [elementami](#Elementy.md) w taki sam sposób jak dla [wiązań](#Wi.C4.85zania.md). Wyświetlanie w drzewie działa w ten sam sposób.


</div>


</div>

Jak zwykle możesz modyfikować paski narzędzi i dodawać lub usuwać poszczególne narzędzia. Pamiętaj, aby sprawdzić też obecność narzędzi w menu *Złożenie 3*, które mogą nie być obecne na paskach narzędzi.


{{top}}

### Wiązania

Projektant używa wiązań by uzyskać określony efekt relacji dwóch części. Sztuką jest wybranie właściwych wiązań dla najlepszego poradzenia sobie z danym problemem. Każdy usunięty stopień swobody w teorii powinien być usunięty tylko raz między dwoma obiektami, ale w praktyce wiele narzędzi CAD tworzy nadmiarowe kombinacje wiązań, często kompensowane przez skomplikowane algorytmy, a czasami nie. Assembly3 używa algorytmów do wykrycia i kompensacji nadmiarowych wiązań, ale zdecydowanie one nie są jeszcze dojrzałe. Dlatego w praktyce Assembly3 by uniknąć problemów należy być świadomym jak wiele stopni swobody *(DOF)* zostało użytych i które mogą być jeszcze zablokowane przez wiązania. Żadna część nie powinna być połączona przez wiązania używające więcej niż 6 stopni swobody.

   *   Uwaga   * Jeśli solver spotka kombinację której nie może rozwiązać, wyrzuci błąd. Jest bardzo trudno solverowi znaleźć co spowodowało problem, więc zwykle z tego wyrzuconego błędu nie będzie jasne *gdzie* jest ten problem. W skomplikowanych złożeniach może to prowadzić do uciążliwego poszukiwania problemu. Niestety nie ma prostego sposobu na uniknięcie tego. Jednak przydatna jest pełna świadomość jak działa system *(np. zobacz [Elementy](#Elementy.md) poniżej)*, używanie komunikatywnych nazw dla wszystkich biorących udział komponentów i dodawanie kolejnych wiązań tylko gdy solver już rozwiąże dotychczasowe złożenie. Bardzo przydatnym do wyśledzenia problemu jest funkcja \"Menu kontekstowe / Deaktywuj\" każdego z wiązań.

Wiązania środowiska Złożenie 3 określają więzy pozycji lub orientacji pomiędzy dwoma [Elementami](#Elementy.md). Niektóre wiązanie działają nawet więcej niż z dwoma [Elementami](#Elementy.md). [Elementem](#Elementy.md) może być ściana, linia lub krawędź lub punkt części. Ogólnie wiązania definiowane są przez wybranie żądanych [Elementów](#Elementy.md) i późniejsze wybranie wiązania z [paska narzędzi](#Paski_narz.C4.99dzi.md) Wiązań.

-   Rozwiązuje 6 stopni swobody, pozostawia 0 stopni swobody   *
    -   **Blokada**   * Wiązanie blokady ustala wszystkie stopni swobody dla danej ściany. Powinno być używane dla jednej części bazowej w każdym złożeniu. Można również włączyć funkcję \"Blokada przesunięcia\" *(w pasku narzędzi)*, aby część nie mogła być przypadkowo przesunięta. Zazwyczaj nie ma znaczenia, która ściana / linia / punkt zostanie użyta do naprawy części. Należy również pamiętać, że blokada działa tylko w bezpośrednim złożeniu, tzn. w przypadku złożenia podrzędnego złożenie nadrzędne nadal wymagałoby zablokowanej części.
    -   **Dołączenie**   * Sprawia, że układy współrzędnych obu elementów są zgodne dla wszystkich osi. Jest to najbardziej efektywna obliczeniowo funkcja i powinna być używana zawsze, gdy jest to możliwe. Zauważ, że możesz użyć właściwości elementu, aby skompensować przesunięcia i kąty, jeśli dwa [elementy](#Elementy.md) nie są idealnie wyrównane.
-   Rozwiązuje 5 stopni swobody, pozostawia 1 stopień swobody   *
    -   **Płaszczyzna zbieżna**   * ustala Tx,Ty,Tz, Rx,Ry. Tylko Rz jest wolne. Pozostaje obrót wokół normalnej przechodzącej przez *środek płaszczyzny*.
-   Rozwiązuje 4 stopnie swobody, pozostawia 2 stopnie swobody   *
    -   **Wyrównanie osiowe**   * ustala Tx,Ty, Rx,Ry. Tylko Tz, Rz są wolne. Pozostaje obrót wokół osi kształtu i translacja wzdłuż tej samej osi. Dwa wiązania *Punkt na linii* (jeśli dwa punkty są różne) dają ten sam rezultat. Wiązanie *Współliniowo* również.
    -   **Punkt na linii**   * Eliminuje przesunięcia i rotację wzdłuż normalnych do linii odniesienia. Dozwolone jest tylko przesunięcie i obrót wzdłuż osi linii.
-   Rozwiązuje 3 stopnie swobody, pozostawia 3 stopnie swobody   *
    -   **Identyczna orientacja**   * ustala Rx,Rz,Rz. Wszystkie T pozostają wolne.
    -   **Zbieżność punktów**   * ustawia Tx,Ty,Tz. Wszystkie punkty R pozostają wolne.
    -   **Punkt na punkcie** eliminuje 3 przesunięcia.
    -   **Wyrównanie płaszczyzny**   * ustala Tz, Rx,Ry *(w ruchu płaskim)*. Eliminuje to przesunięcia wzdłuż normalnej do płaszczyzny odniesienia oraz dwa obroty wokół osi tej płaszczyzny.
-   Rozwiązuje 2 stopnie swobody, pozostawia 4 stopnie swobody   *
    -   **Wielo równolegle**   * rozwiązuje Rx,Ry. wszystkie T i Rz pozostają. Eliminuje to dwa obroty wokół osi płaszczyzny odniesienia.
-   Rozwiązuje 1 stopień swobody, pozostawia 5 stopni swobody   *
    -   **Punkt na płaszczyźnie**   * rozwiązuje Tz. Eliminuje to przesunięcie wzdłuż normalnej do płaszczyzny odniesienia.
    -   **Odległość punktów**   * ustala odległość między początkami elementów.

           *   Daje to większą swobodę niż *Punkt na płaszczyźnie*.

Inne

-   **Punkty na okręgu**   * ustala Tz i częściowo Tx,Ty. Unieruchamia przesunięcie punktu *(lub kilku punktów)* na okręgu lub powierzchni okręgu. Musisz wybrać okrąg jako drugi. To umożliwia wszystkie obroty i daje ograniczone przesunięcie w płaszczyźnie odniesienia okręgu.

*   * Uwaga   * Na poniższej liście Tx,Ty,Tz i Rx,Ry,Rz są używane do opisania przesunięć i obrotów względem referencyjnych układów współrzędnych zaangażowanych Elementów. Nie zawsze jest to dokładne lub w pełni zdefiniowane, np. gdy mamy do czynienia z linią, nie jest określone, czy biegnie ona w kierunku X, Y czy pod jakimkolwiek kątem pomiędzy nimi. System ten jest używany dla zachowania powagi i łatwego porównania na korzyść poprawnej, ale bardziej złożonej definicji. Tak więc Z jest generalnie normalnym kierunkiem każdej zaangażowanej ściany. Proszę się nie krępować i zmodyfikować to, stosując lepsze podejście z poprawioną czytelnością.*


{{top}}

### Elementy

Elementy są specyficznym terminem w środowisku Assembly3 i ważne jest zrozumienie Elementów by zrozumieć jak Assembly3 powinno być używane.

Pomocne jest myślenie o Elementach jako ogólnym określeniu dla \'wybieralnej pozycji\' części, np. ściany, krawędzi, okręgu lub narożnika czy innego punktu. Pozycje które wybierasz aby związać je są tymi Elementami. W drzewie folderu Assembly znajdują się trzy podfoldery. Oprócz \"Parts\" i \"Constraints\" jest tam folder nazwany \"Elements\", który jest pusty tak długo jak nie ma dodanych żadnych wiązań. Podczas dodawania wiązania, samo wiązanie dostanie dwa *(lub więcej)* listki, są one wybranymi \"Elementami\". Dodatkowo zostają one dodane do folderu \"Elements\", który jest po prostu listą wszystkich Elementów użytych w złożeniu. Dobrym pomysłem jest zmiana ich nazw *(przyciskiem F2)*, szczególnie w większych złożeniach.

Spójrzmy na przykład

   *   Stwórz nowy plik i z środowiska Część dodaj prostopadłościan i walec. Ustawimy walec na prostopadłościanie. Najpierw utwierdzimy część bazową, w naszym przypadku prostopadłościan. Wybierz dolną ścianę prostopadłościanu i wybierz wiązanie \"blokady odległości\" *(pierwsza ikona na [pasku](#Toolbars.md) wiązania)*. Wybierz górną ścianę walca i górną ścianę prostopadłościanu. Następnie wybierz wiązanie \"Zbierzność płaszczyzn\". W tym momencie walec zostanie przesunięty na prostopadłościan i w drzewie, pod \"Constraints\", zostanie dodany nowy listek z dwoma węzłami podrzędnymi. Dodatkowo te same węzły podrzędne zostały dodane pod \"Elements\". Jeśli twój walec jest w środku prostopadłościanu zamiast na prostopadłościanie, poprawmy to najpierw   * wybierz węzeł podrzędny pod \"Constraints\", który wskazuje na ścianę walca i przy pomocy kliknięcia prawym przyciskiem myszy wybierz w menu kontekstowym \"Flip Part\". Teraz walec jest już ustawiony na prostopadłościanie.

Kluczową rzeczą do zrozumienia jest to, że wiązanie działa na łączach do Elementów z listy w folderze drzewa \"Elements\". To pozwala na utrzymywanie nienaruszonej struktury wiązań podczas zmiany części. To jest bardzo trudne do zrozumienia bez przywołania przykładu.

Spójrzmy ponownie na powyższy przykład

   *   Uwaga   * upewnij się, że dodałeś \"Wiązanie blokady odległości\" to prostopadłościanu, bo inaczej przykład będzie wyglądał myląco
   *   W oknie CAD wybierz inną ścianę prostopadłościanu. W tej chwili pracujemy tylko w widoku drzewa. Przesuń kursor myszki do drzewa, w miejsce gdzie prostopadłościan powinien zostać wybrany. Przeciągnij prostopadłościan do folderu \"Elements\". Upuść go na nazwę \"Elements\", a nie w żadne inne miejsce folderu - później zobaczymy dlaczego. Powinieneś zobaczyć kolejny Element dodany do listy \"Elements\". Teraz w folderze \"Constraints\" wybierz węzeł podrzędny dla ściany prostopadłościanu w wiązaniu \"Zbieżności płaszczyzn\" i usuń go. Wiązanie będzie pokazywać znak wykrzyknienia, ponieważ brakuje mu jednego Elementu. Zauważ, że usuwając Element w Wiązaniu *nie* usunęliśmy go z listy. Jest tak ponieważ wiązanie było tylko łączem do Elementu na liście. Teraz weźmy nowo dodany Element w liście \"Elements\" i przeciągnijmy go na wiązanie \"Zbieżności płaszczyzn\". W tym momencie walec przesunął się na drugą zaznaczoną ścianę Może być konieczne ponowne wybranie \"Flip Part\" z menu kontekstowego, jeśli walec znów znajduje się w środku prostopadłościanu.

Wcześniejszy przykład pokazał, że możliwa jest zmiana Elementów wykorzystywanych do wiązania bez konieczności usuwania samego wiązania. W ten sam sposób możemy przenieść walec do całkowicie innej części. Po nieco dłuższym eksperymentowaniu z tym przykładem, zauważysz inne rzeczy, jak   *

-   Jeśli zmienisz nazwę Elementu na liście, to nazwa ta zostanie zmieniona we wszystkich wiązaniach.
-   Możesz użyć jednego Elementu z listy w kilku wiązaniach.
-   Możesz użyć Okna Właściwości Elementu by dodać **Odsunięcie**. W naszym przykładzie pozwala to przesunąć walec w stosunku do ściany prostopadłościanu.
-   Możesz użyć przycisku \"Pokaż Układ Współrzędnych Elementu\" na głównym pasku narzędzi by zobaczyć co \"Menu kontekstowe / Flip Part\" i \"Menu kontekstowe / Flip Element\" robią. Upewnij się, że obserwujesz co się dzieje w Oknie Właściwości.
-   Możesz dodać wiązanie w całkowicie innej kolejności   * najpierw dodaj kilka Elementów do \"Listy Elementów\" *(nadawanie nazw jest przydatne, np. \"Górna Ściana Prostopadłościanu czy \"Przednia Ściana Prostopadłościanu\")* a następnie dodaj wiązanie bez zaznaczania czegokolwiek - będzie ono pustym wiązaniem. Potem przeciągnij Elementy z listy \"Elementów\". Wynik będzie takim sam jak po tym co zrobiliśmy w pierwszym przykładzie. Po wykonaniu tego ćwiczenia natura działania wiązań z Elementami powinna stać się jasna.
-   Możesz zmienić istniejące wiązanie pomiędzy istniejącymi Elementami po prostu przez wybranie innej pozycji w właściwości Okno Właściwości / ConstraintType.


{{top}}

## Zgodność

Złożenie 3 zostało zainspirowane przez [Złożenie 2](Assembly2_Workbench/pl.md), ale nie jest z nim kompatybilne. Jeśli masz starsze modele wykonane w środowisku Złożenie2, powinieneś zostać przy FreeCAD 0.16 i używać środowiska Złożenie 2.

Nowe modele wykonane przy użyciu środowiska Złożenie 3 powinny być otwierane i edytowane tylko w tym środowisku pracy.

Mimo, że mogą mieć podobne narzędzia, środowisko Złożenie 3 nie jest zgodne ze środowiskiem [A2plus](A2plus_Workbench/pl.md) ani [Złożenie 4](Assembly4_Workbench/pl.md). Modele stworzone w tych środowiskach powinny być otwierane tylko w odpowiadających im środowiskach.


{{top}}

## Instalacja

Środowisko pracy [Złożenie 3](Assembly3_Workbench/pl.md) jest dostępne *(od marca 2022)* poprzez [Menadżer dodatków](Std_AddonMgr/pl.md). Wszelkie zależności Złożenie 3 od stron trzecich powinny być zarządzane automatycznie przez menedżera dodatków.

#### Instalacje alternatywne 

Istnieją dwa alternatywne sposoby instalacji środowiska pracy Złożenie 3   *

-   Specjalny fork programu FreeCAD wykonany przez użytkownika realthunder; zobacz [FreeCAD\_assembly3 releases](https   *//github.com/realthunder/FreeCAD_assembly3/releases). Ten fork jest oparty o konkretnym commit z głównej gałęzi FreeCAD, ale posiada również dodatkowe funkcje, które obecnie nie są obecne w głównej gałęzi. Ze względu na to, że to rozwidlenie jest oparte na konkretnym zrzucie rozwojowym, nie posiada najnowszych funkcji scalanych codziennie do gałęzi głównej.
-   Rozwojowy [AppImage](AppImage/pl.md), jest oparty na aktualnej gałęzi głównej i zawiera zależności potrzebne do pracy ze środowiskiem Złożenie 3, takie jak solver SolveSpace.

Ponieważ AppImage działa tylko dla Linuksa, dla użytkowników Windows *(którzy chcą alternatywnie zainstalować to środowisko pracy)* jedyną możliwością przetestowania Złożenie 3 jest pierwsza opcja *(fork realthunder-a)*.


{{top}}

## Jak

## Zaczynamy

Istnieje wiele sposobów na stworzenie złożenia za pomocą środowiska Złożenie 3. Oto najprostszy z nich, który możesz zastosować.

   *   <img alt="" src=images/Assembly3_Example-GettingStarted.jpg  style="width   *600px;">
   *   *Wynik końcowy przykładu wprowadzającego. Na obrazku zaznaczono środowisko pracy Złożenie 3, więc widoczne są jego liczne paski narzędzi. Zwróć uwagę, że pionowy \"Pasek zakładek\" po lewej stronie widoku drzewa jest dodatkiem, który nie jest zawarty w standardowym FreeCAD (ale może być zainstalowany za pomocą Menadżera dodatków).*

-   Naciśnij przycisk **<img src="images/Std_New.svg" width=16px> [Nowy](Std_New/pl.md)**, aby utworzyć nowy plik FreeCAD.
-   Zmień środowisko pracy na <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Złożenie 3](Assembly3_Workbench/pl.md).
-   Wybierz przycisk **<img src="images/Assembly_New_Assembly.svg" width=16px> [Utwórz złożenie](Assembly3_CreateAssembly/pl.md)
**
-   Zmień środowisko pracy na <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> [Część](Part_Workbench/pl.md) i dodaj <img alt="" src=images/Part_Cylinder.svg  style="width   *16px;"> [walec](Part_Cylinder/pl.md) i <img alt="" src=images/Part_Box.svg  style="width   *16px;"> [sześcian](Part_Box/pl.md).
-   <img alt="" src=images/Std_Save.svg  style="width   *16px;"> [Zapisz](Std_Save.md) plik z dowolną nazwą, którą wybierzesz. <img alt="" src=images/Std_CloseActiveWindow.svg  style="width   *16px;"> [Zamknij](Std_CloseActiveWindow/pl.md) i <img alt="" src=images/Std_Open.svg  style="width   *16px;"> [Otwórz \...](Std_Open/pl.md) ponownie plik.

Widok drzewa powinien wyglądać tak jak poniżej *(0.20.pre i Link Branch)*   *

<img alt="" src=images/Assembly3_Example-Tree-01.png  style="width   *300px;"> <img alt="" src=images/Assembly3_Example-Tree-02.png  style="width   *280px;">

-   Teraz *Przeciągnij i upuść* za pomocą myszki oba obiekty **Walec** i **Sześcian** do folderu *\'Części*. Zostaną one przeniesione do tego folderu.

       *   Jest to najszybszy sposób i odpowiedni dla prostych przypadków, takich jak ten. Lepszym sposobem jest użycie obiektów łączących   *
       *   Wybierz obiekty **Sześcian** i **Walec**, a następnie **<img src="images/Std_LinkMake.svg" width=16px> [Utwórz łącze](Std_LinkMake/pl.md)** albo z **menu kontekstowego** *(-\> Akcje z łączami -\> Utwórz łącze)* lub panelu **Structure**.
       *   Powoduje to dodanie dwóch obiektów linków. Następnie *Przeciągnij i upuść* te obiekty do folderu **Części**.
-   Kliknij obie górne powierzchnie **Walca** i **Sześcianu** *(trzymając wciśnięty klawisz **Ctrl** (Cmd na Macu))*
-   Zmień środowisko pracy na <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Złożenie 3](Assembly3_Workbench/pl.md).
-   Wybierz przycisk **<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Zbieżność płaszczyzn](Assembly3_ConstraintCoincidence.md)** z [głównego paska narzędzi wiązań](#G.C5.82.C3.B3wny_pasek_wi.C4.85za.C5.84.md).

Teraz części powinny być połączone ze sobą i Twoje drzewo powinno wyglądać tak jak poniżej *(0.20.pre i Link Branch)*   *

<img alt="" src=images/Assembly3_Example-Tree-03.png  style="width   *300px;"> <img alt="" src=images/Assembly3_Example-Tree-04.png  style="width   *280px;">

-   Kliknij prawym przyciskiem myszy **\_Element** *(albo jeden z dwóch)* i wybierz opcję **Przerzuć część**.

Teraz **walec** powinien znajdować się na wierzchu **sześcianu**. Jeśli całość jest odwrócona do góry nogami, wróć i wybierz **Odwróć część** na drugim elemencie.

   *   Pominęliśmy jeden ważny krok, który powinien być wykonywany w większych złożeniach   * Zablokowanie części bazowej.
   *   Oznacza to zdefiniowanie jednej części, która nie powinna być przesuwana przez wiązania. W tym przykładzie używamy do tego celu **sześcianu**   *
    -   Wybierz dolną ścianę **sześcianu**. Tylko dolną ściankę, nie cały **sześcianu**\'.
    -   wybierz wiązanie **<img src="images/Assembly_ConstraintLock.svg" width=16px> [zablokowania](Assembly3_ConstraintLock/pl.md)** z menu [Główny pasek wiązań](#G.C5.82.C3.B3wny_pasek_wi.C4.85za.C5.84.md).

Gotowe.

Gotowe drzewo złożenia powinno wyglądać tak *(0.20.pre i Link Branch)*   *

<img alt="" src=images/Assembly3_Example-Tree-05.png  style="width   *300px;"> <img alt="" src=images/Assembly3_Example-Tree-06.png  style="width   *280px;">   *

Jeśli chcesz, możesz przesunąć wiązanie **Zablokowania** w górę drzewa. Użyj przycisku **<img src="images/Assembly_TreeItemUp.svg" width=16px> [Przesuń element do góry](Assembly3_MoveItemUp/pl.md)** na [Głównym pasku narzędzi](#G.C5.82.C3.B3wny_pasek_wi.C4.85za.C5.84.md).

**Uwaga   *** wszystkie nowe pliki zewnętrzne muszą być **zapisane**, **zamknięte** i ponownie **otworzone** przynajmniej raz, aby środowisko Złożenie 3 mogło je odnaleźć.

   *   Bez tego FreeCAD nie może przekazać uchwytu pliku do środowiska pracy Złożenie 3 i nie znajdzie on nowej części.
   *   Gdy wszystkie części znajdują się w tym samym pliku, należy **zapisać**, **zamknąć** i ponownie **otworzyć** również ten plik.


{{top}}

### Dodaj odsunięcie 

Złożenie 3 nie oferuje funkcji przesunięcia w stosunku do stałych w sposób, w jaki robi to środowisko [A2plus](A2plus_Workbench/pl.md) lub inne narzędzia CAD. Zamiast tego oferuje bardziej ogólny i elastyczny system do dodawania odsunięć, przemieszczeń, ale także kątów.

-   Dodaj odsunięcie we właściwościach jednego [elementu](#Elementy.md) [wiązania](#Wiązania.md).

       *   możesz wybrać, który z tych dwóch chcesz użyć.

Przykład   *

-   dodaj 2 sześciany do złożenia i wybierz ich powierzchnie boczne.
-   wybierz \"Zbieżność płaszczyzn\". Sześciany zostaną przymocowane wewnątrz siebie.
-   wybierz jeden element i *w menu podręcznym / Obróć część*. Sześciany zostaną dołączone obok siebie.
-   wybierz jedną właściwość elementu \"Odsunięcie / Pozycja / Zz\" i ustaw jej wartość na {{Value|5mm}}. Sześciany będą oddalone od siebie o 5mm.

Przetestuj z innymi osiami lub polami kąta / osi. Sprawdź również, czy uzyskasz ten sam rezultat używając drugiego elementu. Podobnie postępujemy dla wszystkich innych wiązań.


{{top}}

## Rozwiąż niepowodzenie solvera 

= Zdarza się to często, gdy części są nadmiernie związane, tzn. mają zablokowanych więcej niż 6 stopni swobody.

Najprostszym sposobem na znalezienie problemu jest kliknięcie odpowiednich wiązań w drzewie i wybranie z *menu podręcznego / Wyłącz* i ponowne obliczenie. Dobrze jest znać ostatnio dodane wiązania przed niepowodzeniem solvera i po prostu je wycofać.

Uwaga   * ponieważ Złożenie 3 próbuje kompensować nadmiernie związane elementy niejawnie, czasami problem jest wywoływany przez nowe wiązanie, ale przyczyna leży gdzie indziej. Zanim usuniesz wszystko i zaczniesz od nowa, pamiętaj, że możesz ponownie użyć elementów. Jeśli je nazwiesz, możesz zidentyfikować wymagane elementy i ponownie zbudować wiązania bez używania widoku 3D. Zobacz sekcję [elementy](#Elementy.md) powyżej.


{{top}}

### Zastępowanie części lub zmiana nazwy pliku 

W przypadku usunięcia części lub zmiany nazwy pliku, złożenie ulega uszkodzeniu i nie może być rozwiązane, a solver wyświetli komunikat \" Niespójne wiązania\". Solver oznacza niepoprawne Elementy i Wiązania znakiem zapytania w drzewie.

Jednym ze sposobów rozwiązania tego problemu jest po prostu usunięcie wszystkich niepoprawnych wiązań i elementów, zaimportowanie nowej części i ponowne wykonanie wszystkiego. Ale jest też lepszy sposób   *

-   Zmiana nazwy pliku.
    1.  Użyj menedżera plików i skopiuj plik, którego nazwę chcesz zmienić. Następnie nadaj nową nazwę kopii.
    2.  Otwórz kopię w programie FreeCAD. Złożenie i stary plik również powinny być otwarte.
    3.  Zaznacz stary obiekt w drzewie i kliknij, aby zmienić właściwość \"Połączony obiekt\" *(zawiera on starą nazwę pliku)*.
    4.  Zostanie otwarte okno dialogowe z listą wszystkich otwartych części. Pokazuje nazwy plików i obiektów każdej części. Stara część i obiekt są zaznaczone. Odszukaj w drzewie zmienioną część i wybierz ten sam obiekt w nowej części. Następnie zatwierdź wybór.
    5.  Usuń starą część w drzewie. Również plik może być teraz usunięty.
    6.  Wiązania i elementy starej części stały się nieprawidłowe. Otwórz listę wiązań lub elementów w drzewie. Następnie kolejno .
        -   wybierz każdą powierzchnię elementu na nowej części. Element w drzewie zostanie podświetlony.
        -   Weź ten element i przeciągnij go nad stary element *(albo na liście elementów, albo w jednym z wiązań, gdzie był używany)*. Ten element powinien stać się prawidłowy.
        -   Powtórz tę procedurę dla pozostałych elementów. Często wystarczy jeden element, aby środowisko Złożenie 3 automatycznie zidentyfikowało pozostałe elementy części.
        -   Jeżeli element został przypadkowo przypisany do niewłaściwej powierzchni, wystarczy powtórzyć czynność z właściwą powierzchnią.
    7.  Zmień nazwę obiektu w programie FreeCAD, jeśli chcesz.

-   Wymiana części na inną.

       *   *która jest na tyle podobna do oryginalnej części, że pierwotne wiązania nadal mają sens, oczywiście*.

    1.  Skasuj starą część w drzewie. Również plik może zostać usunięty.
    2.  Wiązania i elementy starej części stały się niepoprawne. Otwórz listę wiązań lub elementów w drzewie.
        -   Wybierz powierzchnię elementu na nowej części. Element w drzewie zostanie podświetlony.
        -   Wybierz ten element i przeciągnij go nad stary element *(albo na liście elementów, albo w jednym z wiązań, gdzie był używany)*. Ten element powinien stać się poprawny.
        -   Powtórz tę procedurę dla pozostałych elementów.
        -   Jeśli element został przypadkowo przypisany do niewłaściwej powierzchni, powtórz procedurę z właściwą powierzchnią.
    3.  Zmień nazwę obiektu w programie FreeCAD, jeśli chcesz.

\'\'\'Uwagi
\* Nie są one tak skomplikowane, jak mogłoby się wydawać. Po 2-3 razach powinny stać się drugą naturą i być naprawdę łatwe do wykonania.

-   To nie tylko zwykle sposoby szybsze niż usuwanie i ponowne wykonywanie wiązań, ale także bezpieczniejsze, ponieważ element mógł być użyty w złożeniu nadrzędnym. Usunięcie oryginału zniszczyłoby to powiązanie, ponowne przypisanie zachowałoby je.
-   Również ta procedura staje się naprawdę szybka i łatwa do wykonania, jeśli wiązania i elementy są nazwane. Nie ma potrzeby zgadywania, gdzie powierzchnie powinny być przeciągnięte i upuszczone, ponieważ nazwy mówią same za siebie *(zobacz sekcję [Wskazówki i porady](#Wskaz.C3.B3wki_i_porady.md))*.

\'\'\'


{{top}}

### Wskazówki i porady 

-   Używanie hierarchicznych złożeń pomaga uniknąć problemów z solverami i zachować płynność modelu. Można zamrozić podzespół jednym kliknięciem i w ten sposób łatwo zaoszczędzić zasoby procesora *(użyj menu kontekstowego w drzewie)*. Podczas wczytywania zespołu Assembly3 nie musi otwierać zewnętrznych plików dla zamrożonych podzespołów, dzięki czemu drzewo jest zwarte.
-   Bardzo pomocne jest wyrobienie sobie nawyku nadawania nazw elementom i wiązaniom. Użyj klawisza **F2** aby zrobić to szybko na drzewie. Bardzo przydatne są narzędzia do sortowania drzewa w głównym pasku narzędzi. Zespół z w pełni nazwanymi wiązaniami i elementami jest bardzo łatwy do zrozumienia dla innych osób lub dla siebie, gdy przeglądasz starszy plik.

       *   Przykłady dla nazw wiązań dla tabeli   * \"Align\_FrontLegs\", \"Align\_FrameBottom-LegTops\", a nazwami elementów mogą być \"Leg1\_Top\" lub \"TableTop\_Front\", \"TableTop\_Left\".
-   Należy pamiętać, że gdy zewnętrzne pliki zostaną otwarte przez złożenie, nie jest możliwe łatwe ich ponowne zamknięcie bez zamykania złożenia. Ponieważ złożenie utrzymuje otwarte pliki w tle, zakładka może zniknąć, ale plik pozostaje widoczny w drzewie. Jeśli masz kilka warstw podzespołów, staje się prawie niemożliwe, aby zamknąć pojedyncze pliki. To zachowanie może się zmienić, ale do tego czasu możliwym podejściem może być regularne używanie komend **Plik → Zapisz wszystkie** i **Plik → Zamknij wszystkie** w celu wyczyszczenia drzewa przed pracą nad innym złożeniem podrzędnym.

       *   \'\'Przykład   * Załóżmy, że masz dużą maszynę CNC z głównym złożeniem i złożeniem podrzędnym dla każdego modułu. Gdy główne złożenie jest otwarte, może otworzyć dosłownie setki plików aż do pojedynczego łożyska kulkowego. Przed rozpoczęciem pracy na złożeniu podrzędnym szafy elektroniki maszyny jest to dobry pomysł, aby zapisać i zamknąć wszystkie pliki, aby uzyskać puste drzewo. Następnie otwórz tylko złożenie podrzędne dla szafy elektroniki. To otworzy wszystkie pliki, których potrzebuje, ale tylko te.
-   Używanie zewnętrznych plików ułatwia ponowne użycie części lub wersjonowanie części za pomocą systemów takich jak git lub subversion. Przepływ pracy w FreeCAD ze Złożeniami jest całkiem taki sam jak z plikami, które mają wszystkie części w tym samym pliku. Przy częstej wymianie plików z innymi stronami, pojedyncze pliki mogą być wygodniejsze.
-   Mnożenie połączonych części. Jeśli dodałeś link do złożenia, będzie on miał wartość właściwości o nazwie \"Liczba elementów\", domyślnie 0. Jeśli ustawisz ją na wartość 3, otrzymasz 3 wystąpienia tej części. Będą one dodane do katalogu podrzędnego i mogą być używane jak w pełni oddzielne części. Użyj tej funkcji, aby utrzymać niski ślad danych w pliku, ponieważ część jest zapisywana tylko raz. Każde wystąpienie zawiera tylko różnice.
-   Wstawianie wielu części, np. śrub, za pomocą jednego kliknięcia. Sprawdź [Assembly3 Wiki](https   *//github.com/realthunder/FreeCAD_assembly3/wiki/Constraints-and-Solvers) na stronie Github. Jest to nie tylko oszałamiająca funkcja (nawet trochę magiczna), ale naprawdę bardzo przydatna.

-   Użycie [Paska zakładek](https   *//github.com/triplus/TabBar) przyspiesza pracę z montażem. Dzięki temu dodajemy pasek narzędzi z jednym przyciskiem dla każdego środowiska pracy. Możesz sortować pasek narzędzi i umieścić go gdziekolwiek chcesz. Wielu ludzi umieszcza go pionowo po lewej stronie, tuż obok widoku drzewa. Jeśli masz Złożenie 3, Część, Projekt Części i inne często używane narzędzia blisko góry, przełączanie się pomiędzy nimi staje się niezwykle proste.


{{top}}

## Odnośniki internetowe 

-   [App   * Odnośnik](App_Link/pl.md) obiekt, dzięki któremu działa środowisko Złożenie 3.
-   [FreeCAD assembly3](https   *//github.com/realthunder/FreeCAD_assembly3) repozytorium i dokumentacja.
-   [podgląd Złożenie 3](https   *//forum.freecadweb.org/viewtopic.php?f=20&t=25712), duży wątek dyskusyjny.
-   [Przewodnik dla środowiska Złożenie 3](http   *//help-freecad-jpg87.fr/02_ass_ind.php) autorstwa jpg87.
-   [Aktualny status Złożenia](https   *//forum.freecadweb.org/viewtopic.php?f=20&t=34583)
-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md)




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Assembly3 Workbench/pl
