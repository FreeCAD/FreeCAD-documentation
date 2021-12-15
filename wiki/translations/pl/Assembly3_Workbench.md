# <img alt="Ikonka FreeCAD dla środowiska pracy Złożenie 3" src=images/Assembly3_workbench_icon.svg  style="width:64px;"> Assembly3 Workbench/pl


{{TOCright}}

## Wprowadzenie

<img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Złożenie 3](Assembly3_Workbench/pl.md) jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md), które jest używane do wykonywania złożeń różnych części zawartych w jednym lub wielu dokumentach. Środowisko to bazuje na kilku zmianach funkcji rdzenia FreeCAD w wersji 0.19 *(np. [App Link](App_Link/pl.md))*. Dlatego środowisko Złożenie 3 nie może być używane ze starszymi wersjami programu.

Głównymi cechami środowiska **Złożenie 3** są:

-   **dynamiczny/interaktywny solver**. Oznacza to, że możesz przesuwać części myszką, podczas gdy solver będzie ograniczał ruch. To pozwala na przykład, na połączenie koła z osią i interaktywne poruszanie kołem przy pomocy myszki.
-   **łącza**. To oznacza, że możesz używać pojedynczej części, np wkrętu, wielokrotnie w złożeniu *(w różnych miejscach)* bez kopiowania geometrii.
-   **łącza zewnętrzne**. Możliwe jest posiadanie dokumentu FreeCAD zawierającego tylko złożenie, a nie części. Każda z części może być osobnym plikiem. Pliki mogą znajdować się nawet w bibliotece lub gdziekolwiek indziej w systemie plików. Jedynym wymogiem jest to, że ten plik musi być załadowany, kiedy tworzone jest łącze. Po utworzeniu łącza, plik musi być otwarty to wykonywania aktualizacji łączy dotyczących tego pliku. Assembly3 rozwiązuje to przez otwieranie plików w tle, gdy jest to konieczne.
-   **złożenia hierarchiczne**. W prawdziwym życiu złożenia mechaniczne mogą składać się z złożeń podrzędnych. One mogą składać się z kolejnych złożeń podrzędnych, a te z kolejnych, itd.
-   **zamrażanie złożeń**. Jako, że procesor potrafi zarządzać tylko określoną liczbą wiązań w czasie rzeczywistym, zamrażanie złożeń pozwala na używanie wiązań nawet do wielkich złożeń. Po zamrożeniu ukończonych złożeń lub wiązań, które nie muszą pozostać dynamiczne *(np. spawane, skręcane lub klejone części)* są one wyłączane z aktualizacji obliczeń i uznawane przez solver Złożenie 3 za ustaloną geometrię.

    :   Zauważ inne podejścia rozwiązujące ten problem odmiennie, np. środowisko <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Złożenie 4](Assembly4_Workbench/pl.md).


{{top}}

### Paski narzędzi 

Środowisko Złożenie 3 zawiera następujące paski narzędzi - stan na rok 2020.

#### Główny pasek narzędzi 

:   <img alt="" src=images/Assembly3_ToolbarMain.png  style="width:700px;">


<div class="mw-collapsible mw-collapsed">


:   **Główny Pasek Narzędzi** zawiera narzędzia, które obejmują najczęściej używane funkcje programu. Skróty klawiaturowe są podawane przez podpowiedzi narzędzi.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:32px;"> [Utwórz złożenie](Assembly3_CreateAssembly/pl.md): Dodaj folder montażu.

:\* <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width:32px;"> [Grupuj obiekty](Assembly3_GroupObjects/pl.md): Grupuje obiekty.

:\* <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width:32px;"> [Utwórz element](Assembly3_CreateElement/pl.md): Tworzye element.

:\* Import z formatu STEP. Posiada dwa ustawienia

:\*\* <img alt="" src=images/Assembly_Import.svg‎‎  style="width:32px;"> [Importuj z formatu STEP](Assembly3_ImportFromSTEP/pl.md): Import plików w formacie STEP.

:\*\* <img alt="" src=images/Assembly_ImportMulti.svg‎‎  style="width:32px;"> [Importuj wiele dokumentów](Assembly3_ImportMultiDocument/pl.md): Import zespołów z dokumentu STEP do osobnych dokumentów.

:\* <img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width:32px;"> [Rozwiąż wiązania](Assembly3_ResolveConstraints/pl.md): Rozwiązuje wiązania.

:\* <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width:32px;"> [Rozwiąż szybko](Assembly3_QuickSolve/pl.md): Wstępnie rozwiązuje wiązania.

:\* <img alt="" src=images/Assembly_Move.svg‎‎  style="width:32px;"> [Przenieś część](Assembly3_MovePart/pl.md): Przesuwanie części w przestrzeni 3D, jest to specyficzne dla środowiska Złożenie3.

:\* <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:32px;"> [Przesunięcie osiowe](Assembly3_AxialMove/pl.md): Przesuwanie w osi części w przestrzeni 3D, jest to klasyczne narzędzie dostępne w innych miejscach programu FreeCAD.

:\* <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:32px;"> [Szybkie przesunięcie](Assembly3_QuickMove/pl.md): Spowoduje to dołączenie części zaznaczonej w drzewie do kursora myszki. Przy kliknięciu zmieni pozycję części.

:\*: Często dodawane części są ułożone jedna na drugiej w miejscu początkowym. Użyj tej funkcji, aby chwycić część, której nie widzisz.

:\* <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width:32px;"> [Zablokuj przesunięcie](Assembly3_LockMover/pl.md): Blokada ruchu dla ustalonej części. Przycisk przełączający. Gdy nie jest aktywny, można przesuwać części, które mają wiązanie \"Zablokowane\".

:\* <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width:32px;"> [Przełącz widoczność części](Assembly3_TogglePartVisibility/pl.md): Włącza/wyłącza wyświetlanie wybranej części.

:\*: Należy zauważyć, że funkcja ta różni się od użycia klawisza **Space**. Użycie spacji z wybranymi elementami podzespołu w widoku 3D często nie zachowuje się zgodnie z oczekiwaniami. W takich przypadkach należy użyć tej funkcji *(lub skrótu **A** + **Space**)*.

:\* <img alt="" src=images/Assembly_Trace.svg‎‎  style="width:32px;"> [Śledzenie ruchu części](Assembly3_TracePartMove/pl.md): Śledzenie ruchu części *(do ustalenia)*.

:\* <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width:32px;"> [Przelicz automatycznie](Assembly3_AutoRecompute/pl.md): Automatyczne ponowne obliczanie. Zazwyczaj włączone.

:\*: Może być odznaczone podczas naprawiania wiązań lub naprawiania części, gdy solver daje komunikat *nie zbiega się* *(np. przez obrócenie części o 180 stopni)*.

:\* <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width:32px;"> [Inteligentne przeliczanie](Assembly3_SmartRecompute/pl.md): Inteligentne ponowne obliczanie. Zazwyczaj włączone.

:\* <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width:32px;"> [Napraw element automatycznie](Assembly3_AutoFixElement/pl.md): Automatyczne naprawianie elementów. Funkcja eksperymentalna w wersji 0.19\_pre.

:\* Styl elementu. Ma on dwa ustawienia

:\*\* <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width:32px;"> [Automatyczna widoczność elementów](Assembly3_AutoElementVisibility/pl.md): Automatyczne ustawianie widoczności elementów.

:\*\* <img alt="" src=images/Assembly_ShowElementCS.svg‎‎  style="width:32px;"> [Wyświetl układ współrzędnych elementu](Assembly3_ShowElementCS/pl.md): Wyświetla układ współrzędnych elementu.

:\* Płaszczyzna robocza i punkt odniesienia. Dodaje płaszczyznę roboczą, położenie lub punkt odniesienia. Część musi być wybrana. Opcja ta ma pięć ustawień.

:\*\* <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width:32px;"> [Dodaj płaszczyznę roboczą XY](Assembly3_AddXYWorkplane/pl.md): Dodaje płaszczyznę roboczą w płaszczyźnie XY.

:\*\* <img alt="" src=images/Assembly_Add_WorkplaneXZ.svg‎‎  style="width:32px;"> [Dodaj płaszczyznę roboczą XZ](Assembly3_AddXZWorkplane/pl.md): Dodaje płaszczyznę roboczą w płaszczyźnie XZ.

:\*\* <img alt="" src=images/Assembly_Add_WorkplaneZY.svg‎‎  style="width:32px;"> [Dodaj płaszczyznę roboczą ZY](Assembly3_AddZYWorkplane/pl.md): Dodaje płaszczyznę roboczą w płaszczyźnie YZ.

:\*\* <img alt="" src=images/Assembly_Add_Placement.svg‎‎  style="width:32px;"> [Dodaj umiejscowienie](Assembly3_AddPlacement/pl.md): Dodaje umiejscowienie.

:\*\* <img alt="" src=images/Assembly_Add_Origin.svg‎‎  style="width:32px;"> [Dodaj odniesienie położenia](Assembly3_AddOrigin/pl.md): Dodaje odniesienie położenia.

:\* <img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width:32px;"> [Przenieś pozycję w górę](Assembly3_MoveItemUp/pl.md): Przesuwa wybrany element na drzewie w górę.

:\* <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width:32px;"> [Przenieś pozycję w dół](Assembly3_MoveItemDown/pl.md): Przesuwa wybrany element na drzewie w dół.

:\*: Umożliwia sortowanie Części, Elementów lub Wiązań w drzewie. Przewijanie elementów *(z góry na dół i odwrotnie)*. Działa tylko dla pojedynczego zaznaczenia.

:\* <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width:32px;"> [Pomnóż więz](Assembly3_MultiplyConstraint/pl.md): Mnożenie wiązań. Można go wybrać, jeśli występuje wiele części i odpowiednich elementów.

:\*: Używa się go np. do przypisania wielu elementów złącznych tego samego typu do wielu otworów za pomocą jednego wiązania.


</div>


</div>

#### Główny pasek wiązań 

:   <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Niektóre narzędzia są w rzeczywistości menu dla kolejnych przyborów.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:32px;"> [Wiązanie zablokowania](Assembly3_ConstraintLock/pl.md): Dodaj wiązanie **Zablokowania**, aby zablokować jedną lub więcej części.

:\*: Musisz wybrać element geometrii części.

:\*: Jeśli unieruchomisz wierzchołek lub krawędź, część nadal może swobodnie obracać się wokół tego wierzchołka lub krawędzi.

:\*: Zablokowanie ściany spowoduje całkowite zablokowanie części.

:\* <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:32px;"> [Wiązanie wyrównania](Assembly3_ConstraintAlignment/pl.md): Dodaj wiązanie **Wyrównania płaszczyzn**, aby wyrównać płaszczyzny dwóch lub więcej części.

:\*: Powierzchnie czołowe stają się koplanarne lub równoległe z opcjonalną odległością.

:\* <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:32px;"> [Wiązanie zbieżności](Assembly3_ConstraintCoincidence/pl.md): Dodaj wiązanie \"Zbieżność płaszczyzn\", aby płaszczyzny dwóch lub więcej części były zbieżne.

:\*: Ściany są zbieżne w swoich środkach z opcjonalną odległością.

:\* <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:32px;"> [Wiązanie umocowania](Assembly3_ConstraintAttachment/pl.md): Dodaj wiązanie **Umocowania**, aby połączyć dwie części za pomocą wybranych elementów geometrii.

:\*: To wiązanie całkowicie unieruchamia części względem siebie.

:\* <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:32px;"> [Wiązanie wyrównanie do osi](Assembly3_ConstraintAxial.md): Dodaj wiązanie \"wyrównanie osiowe\", aby wyrównać krawędzie/ściany dwóch lub więcej części.

:\*: To wiązanie akceptuje.

:\*:: krawędzie liniowe, które stają się współliniowe,

:\*:: powierzchnie płaskie, które są wyrównywane przy użyciu osi normalnej ich powierzchni,

:\*:: i powierzchnie cylindryczne, które są wyrównywane za pomocą kierunku osiowego.

:\*: Różne typy elementów geometrii mogą być mieszane.

:\* <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:32px;"> [Wiązanie identycznej orientacji](Assembly3_ConstraintSameOrientation/pl.md): Dodaj wiązanie \"Ta sama orientacja\", aby wyrównać powierzchnie dwóch lub więcej części.

:\*: Płaszczyzny są wyrównane, aby miały tę samą orientację *(tj. obrót)*.

:\* <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:32px;"> [Wiązanie wielu równoległości](Assembly3_ConstraintMultiParallel/pl.md): Dodaj wiązanie **Wielo równoległe**, aby powierzchnie płaskie lub krawędzie liniowe dwóch lub więcej części były równoległe.

:\* <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:32px;"> [Wiązanie kąta](Assembly3_ConstraintAngle/pl.md): Dodaj wiązanie **Kąta**, aby ustawić kąt powierzchni płaskich lub krawędzi liniowych dwóch części.

:\* <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:32px;"> [Wiązanie prostopadłości](Assembly3_ConstraintPerpendicular/pl.md): Dodaj wiązanie \"prostopadłe\", aby płaszczyzny lub krawędzie liniowe dwóch części były prostopadłe.

:\* <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:32px;"> [Wiązanie zbieżności punktów](Assembly3_ConstraintPointsCoincident/pl.md): Dodaj wiązanie \"Zbieżność punktów\", aby zrównać dwa punkty w przestrzeni 2D lub 3D.

:\* <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:32px;"> [Wiązanie punkt na płaszczyźnie](Assembly3_ConstraintPointInPlane/pl.md): Dodaj **Punkt na płaszczyźnie**, aby powiązać jeden lub więcej punktów z płaszczyzną.

:\* <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:32px;"> [Wiązanie punkt na linii](Assembly3_ConstraintPointOnLine/pl.md): Dodaj **Punkt na linii**, aby powiązać punkt z linią w przestrzeni 2D lub 3D.

:\* <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:32px;"> [Wiązanie punkt na okręgu](Assembly3_ConstraintPointOnCircle/pl.md): Dodaj \'\'\'Punkt na okręgu\", aby powiązać jeden lub więcej punktów z powierzchnią współśrodkową zdefiniowaną przez okrąg.

:\*: Zauważ, że musisz wybrać punkt *(każdy element geometrii może zdefiniować punkt)*, a następnie wybrać okrąg *(lub powierzchnię clyndryczną)*,

:\*: Po czym możesz dodać więcej punktów do zaznaczenia, jeśli chcesz.

:\* <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:32px;"> [Wiązanie odległości punktów](Assembly3_ConstraintPointsDistance/pl.md): Dodaj **Odległość punktów**, aby ustalić odległość dwóch lub więcej punktów.

:\* <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:32px;"> [Wiązanie odległość punktu od płaszczyzny](Assembly3_ConstraintPointPlaneDistance/pl.md): Dodaj \"Odległość punkt-płaszczyzna\", aby ustalić odległość pomiędzy jednym lub więcej punktami a płaszczyzną.

:\* <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:32px;"> [Wiązanie odległości punktu od linii](Assembly3_ConstraintPointLineDistance/pl.md): Dodaj **Odległość linii punktu**, aby określić odległość między punktem a krawędzią liniową w przestrzeni 2D lub 3D.

:\* <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:32px;"> [Wiązanie symetrii](Assembly3_ConstraintSymmetric/pl.md): Dodaj wiązanie \"Symetrii\", aby elementy geometrii z dwóch części były symetryczne względem płaszczyzny.

:\*: Obsługiwane elementy to krawędź liniowa i ściana planarna.

:\* <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:32px;"> [Więcej wiązań](Assembly3_ConstraintMore/pl.md): Przełącz paski narzędzi, aby uzyskać więcej wiązań

:\*: Tak naprawdę nie jest to żadne wiązanie, ale przełącznik pokazujący / ukrywający **Paski narzędzi dodatkowych wiązań**.


</div>


</div>

#### Dodatkowe paski narzędziowe wiązań 

:   <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:28px;"> (Assembly3 Constraints2)





:   <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:28px;"> (Assembly3 Sketch Constraints)


<div class="mw-collapsible mw-collapsed">


:   Możesz je uruchomić przez wybranie przycisku **<img src="images/Assembly_ConstraintMore.svg‎‎" width=16px> [More](Assembly3_ConstraintMore/pl.md)** na Głównym pasku narzędzi.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:32px;"> [Odległość punktu](Assembly3_ConstraintPointDistance/pl.md): Dodaj **Odległość punktu**, aby ograniczyć odległość dwóch punktów w przestrzeni 2D lub 3D.

:\* <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:32px;"> [Równy kąt](Assembly3_ConstraintEqualAngle/pl.md): Dodaj \"Kąt równy\", aby zrównać kąty między dwiema liniami lub wektorami normalnej.

:\* <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:32px;"> [Symetria punktów](Assembly3_ConstraintPointsSymmetric/pl.md): Dodaj wiązanie \"Symetria punktów\", aby uczynić dwa punkty symetrycznymi względem płaszczyzny.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> [Symetria pozioma](Assembly3_ConstraintSymmetricHorizontal/pl.md): Symetrycznie poziomo.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> [Symetria pionowa](Assembly3_ConstraintSymmetricVertical/pl.md): Symetrycznie pionowo.

:\* <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:32px;"> [Symetria linii](Assembly3_ConstraintSymmetricLine/pl.md): Dodaj wiązanie **Symetria linii**, aby uczynić dwa punkty symetrycznymi względem linii.

:\* <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:32px;"> [Punkty poziomo](Assembly3_ConstraintPointsHorizontal/pl.md): Dodaj wiązanie **Punkty poziomo**, aby dwa punkty były względem siebie poziome podczas rzutowania na płaszczyznę.

:\* <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:32px;"> [Punkty pionowo](Assembly3_ConstraintPointsVertical/pl.md): Dodaj wiązanie **Punkty pionowo**, aby dwa punkty były względem siebie pionowe podczas rzutowania na płaszczyznę.

:\* <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:32px;"> [Linia poziomo](Assembly3_ConstraintLineHorizontal/pl.md): Dodaj wiązanie **Linia poziomo**, aby segment linii był poziomy podczas rzutowania na płaszczyznę.

:\* <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:32px;"> [Linia pionowo](Assembly3_ConstraintLineVertical/pl.md): Dodaj wiązanie **Linia pionowo**, aby segment linii był pionowy podczas rzutowania na płaszczyznę.

:\* <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:32px;"> [Stycznie do linii łuku](Assembly3_ConstraintArcLineTangent/pl.md): Dodaj wiązanie \"Stycznie do linii łuku\", aby linia była styczna do łuku w punkcie początkowym lub końcowym łuku.

:\* <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:32px;"> [Sketch plane](Assembly3_ConstraintSketchPlane.md): Add a \"Sketch plane\" to define the work plane of any draft element inside or following this constraint.

:\*: Add an empty \"Sketch plane\" to undefine the previous work plane.

:\* <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:32px;"> [Line length](Assembly3_ConstraintLineLength.md): Add a \"Line length\" constrain the length of a non-subdivided Draft.Wire.

:\* <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:32px;"> [Equal length](Assembly3_ConstraintEqualLength.md): Add an \"Equal length\" constraint to make two lines of the same length.

:\* <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:32px;"> [Length ratio](Assembly3_ConstraintLengthRatio.md): Add a \"Length ratio\" to constrain the length ratio of two lines.

:\* <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:32px;"> [Length difference](Assembly3_ConstraintLengthDifference.md): Add a \"Length difference\" to constrain the length difference of two lines.

:\* <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:32px;"> [Length Equal Point Line Distance](Assembly3_ConstraintLengthEqualPointLineDistance.md): Add a \"Length Equal Point Line Distance\" to constrain the distance

:\*: between a point and a line to be the same as the length of a another line.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> ( <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:32px;"> )[Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength.md): Add an \"Equal Line Arc Length\" constraint to make a line of the same length as an arc.

:\* <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:32px;"> [Mid point](Assembly3_ConstraintMidPoint.md): Add a \"Mid point\" to constrain a point to the middle point of a line.

:\* <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:32px;"> [Diameter](Assembly3_ConstraintDiameter.md): Add a \"Diameter\" to constrain the diameter of a circle/arc.

:\* <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:32px;"> [Equal radius](Assembly3_ConstraintEqualRadius.md): Add an \"Equal radius\" constraint to make two circles/arcs of the same radius.

:\* <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:32px;"> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md): Add a \"Points project distance\" to constrain the distance of two points projected on a line.

:\* <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:32px;"> [Equal point line distance](Assembly3_ConstraintEqualPointLineDistance.md): Add an \"Equal point line distance\" to constrain the distance

:\*: between a point and a line to be the same as the distance between another point and line.

:\* <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:32px;"> [Colinear](Assembly3_ConstraintColinear.md): Add a \"Colinear\" constraint to make two lines collinear.


</div>


</div>


:   **Paski Narzędzi Wiązań** będą głównym interfejsem używanym podczas składania części.
:   Są one domyślnie wyszarzone, i zostają aktywowane gdy przynajmniej jedna ściana, linia lub punkt części jest wybrana.
:   Ogólnie wybierasz Elementy, które powinny zostać połączone a następnie wybierasz typ wiązania.
:   Ramki w różnych barwach oznaczają różną charakterystykę wiązań:

    :   czy to 2D/3D albo czy więcej niż dwa Elementy mogą zostać dodane.
:   Dokładny opis znajduje się w Wiki na Githubie.

#### Pasek narzędzi nawigacji 


<div class="mw-collapsible mw-collapsed">


:   Theses functions are useful when working with an assembly with a hierarchy of linked external files


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width:32px;"> [Go to relation](Assembly3_GoToRelation.md): Reveals the Relations group (hidden by default) and selects a relation object.

:\* <img alt="" src=images/Std_LinkSelectLinked.svg  style="width:32px;"> [Select linked object](Std_LinkSelectLinked.md): Selects the linked object and switches to its document. <small>(v0.19)</small> 

:\* <img alt="" src=images/Std_LinkSelectLinkedFinal.svg  style="width:32px;"> [Select linked final](Std_LinkSelectLinkedFinal.md): Selects the deepest linked object and switches to its document. <small>(v0.19)</small> 


</div>


</div>

#### Pasek narzędzi pomiarowych 

:   <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   The **Measurement toolbar** adds functions to measure the distance or the angle between two objects


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:32px;"> [Measure points](Assembly3_MeasurePoints.md): Add a \"Measure points\" to measure the distance of two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:32px;"> [Measure point to line](Assembly3_MeasurePointLine.md): Add a \"Measure point to line\" to measure the distance between a point and a linear edge in 2D or 3D.

:\* <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:32px;"> [Measure point to plane](Assembly3_MeasurePointPlane.md): Add a \"Measure point to plane\" to measure the distance between a point and a plane.

:\* <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:32px;"> [Measure angle](Assembly3_MeasureAngle.md): Add a \"Measure angle\" to measure the angle of planar faces or linear edges of two parts.

:   There is no function to measure a radius or diameter.
:   The measurement tools survive part changes, e.g. the distance between edges of a cube when the cube is re-sized.
:   As the constraints the calculations are done in real time and updated upon any change. Behind the scenes, the function is very similar to the [constraints](#Constraints.md). The distance or angle is calculated between [Elements](#Elements.md) in the same way as for [constraints](#Constraints.md). The display in the tree works in the same way.


</div>


</div>

As usual you can modify the tool bars and add or remove single tools. Be sure to check the menu Assembly3 for functions that may not be present in the tool bars.


{{top}}

### Wiązania

Projektant używa wiązań by uzyskać określony efekt relacji dwóch części. Sztuką jest wybranie właściwych wiązań dla najlepszego poradzenia sobie z danym problemem. Każdy usunięty stopień swobody w teorii powinien być usunięty tylko raz między dwoma obiektami, ale w praktyce wiele narzędzi CAD tworzy nadmiarowe kombinacje wiązań, często kompensowane przez skomplikowane algorytmy, a czasami nie. Assembly3 używa algorytmów do wykrycia i kompensacji nadmiarowych wiązań, ale zdecydowanie one nie są jeszcze dojrzałe. Dlatego w praktyce Assembly3 by uniknąć problemów należy być świadomym jak wiele stopni swobody (DOF) zostało użytych i które mogą być jeszcze zablokowane przez wiązania. Żadna część nie powinna być połączona przez wiązania używające więcej niż 6 stopni swobody.

:   Note: Jeśli solwer spotka kombinację której nie może rozwiązać, wyrzuci błąd. Jest bardzo trudno solwerowi znaleźć co spowodowało problem, więc zwykle z tego wyrzuconego błędu nie będzie jasne *gdzie* jest ten problem. W skomplikowanych złożeniach może to prowadzić do uciążliwego poszukiwania problemu. Niestety nie ma prostego sposobu na uniknięcie tego. Jednak przydatna jest pełna świadomość jak działa system *(np. zobacz [Elementy](#Elements.md) poniżej)*, używanie komunikatywnych nazw dla wszystkich biorących udział komponentów i dodawanie kolejnych wiązań tylko gdy solwer już rozwiąże dotychczasowe złożenie. Bardzo przydatnym do wyśledzenia problemu jest funkcja \"Menu kontekstowe/Deaktywuj\" każdego z Wiązań.

Wiązania Assembly3 określają ograniczenia pozycji lub orientacji pomiędzy dwoma [Elementami](#Elements.md). Niektóre wiązanie działają nawet więcej niż z dwoma [Elementami](#Elements.md). [Elementem](#Elements.md) może być ściana, linia lub krawędź lub punkt części. Ogólnie wiązania definiowane są przez wybranie żądanych [Elementów](#Elements.md) i późniejsze wybranie wiązania z [paska narzędzi](#Toolbars.md) Wiązań.

-   Fixes 6 DOF, leaves 0 DOF:
    -   **Lock**: The lock constraint fixes all DOFs for a face. It should be used for one base part in each assembly. You may also want to enable the \"MoveLock\" function (in the tool bar) so that the part can not be moved accidentially. Normally it does not matter which face/line/point you use to fix a part. Also note that the lock is only valid for the direct assembly, i.e. in case of a sub-assembly the parent assembly would still require a locked part on its own.
    -   **Attachment**: Makes both elements coordinate systems equal for all axes. This is computation wise the most inexpensive function and should be used where ever possible. Note that you could use the element properties to compensate for offsets and angles if the two [elements](#Elements.md) are not perfectly aligned.
-   Fixes 5 DOF, leaves 1 DOF:
    -   **Plane Coincident**: fixes Tx,Ty,Tz, Rx,Ry. Only Rz is free. There remains the rotation around the normal passing through the ''center of the plane''.
-   Fixes 4 DOF, leaves 2 DOF:
    -   **Axial Alignment**: fixes Tx,Ty, Rx,Ry. Only Tz, Rz are free. There remains the rotation around the axis of the shape and the translation along this same axis. Two *PointOnLine* constraints (if the two points are different) give the same result. The \''Colinear\'' constraint too.
    -   **PointOnLine**: This eliminates the translation and rotation along the normals to the reference line. Only the translation and rotation along the line axis is allowed.
-   Fixes 3 DOF, leaves 3 DOF:
    -   **Same Orientation**: fixes Rx,Rz,Rz. All T\'s remain free.
    -   **Points Coincident**: fixes Tx,Ty,Tz. All R\'s remain free.
    -   **PointOnPoint** constraint eliminates the 3 translations.
    -   **Plane Alignment**: fixes Tz, Rx,Ry. In plane motion and Rz. This eliminates the translation along the normal to the reference plane and the two rotations around the axes of this plane.
-   Fixes 2 DOF, leaves 4 DOF:
    -   **Multi Parallel**: fixes Rx,Ry. all T\'s and Rz remain. This eliminates the two rotations around the axes of the reference plane.
-   Fixes 1 DOF, leaves 5 DOF:
    -   **Points in Plane**: Fixes Tz. This eliminates the translation along the normal to the reference plane.
    -   **Points Distance**: fixes the distance between the Element origins.

        :   This gives you more freedom than *Points in Plane*

Other

-   **Points on Circle**: fixes Tz and partially Tx,Ty. Freezes the point translation (or several points) on a circle or disk area. You must pick the circle second. This leaves all rotations free and gives limited translation in the circle reference plane.

*: Note: In the following list Tx,Ty,Tz and Rx,Ry,Rz are used to describe translations and rotations about the reference coordinate systems of the involved Element\'s. This is not always exact or fully defined, e.g. when a line is involved it is not defined if it runs in X, Y or any angle in betweeen. The system is used for bevity and easy comparison in favour of a correct but more complex definition. So Z is generally the normal direction of any faces involved. Please feel free to modify this with a better approach with improved readability.*


{{top}}

### Elementy

Elementy są specyficznym terminem w środowisku Assembly3 i ważne jest zrozumienie Elementów by zrozumieć jak Assembly3 powinno być używane.

Pomocne jest myślenie o Elementach jako ogólnym określeniu dla \'wybieralnej pozycji\' części, np. ściany, krawędzi, okręgu lub narożnika czy innego punktu. Pozycje które wybierasz aby związać je są tymi Elementami. W drzewie folderu Assembly znajdują się trzy podfoldery. Oprócz \"Parts\" i \"Constraints\" jest tam folder nazwany \"Elements\", który jest pusty tak długo jak nie ma dodanych żadnych wiązań. Podczas dodawania wiązania, samo wiązanie dostanie dwa *(lub więcej)* listki, są one wybranymi \"Elementami\". Dodatkowo zostają one dodane do folderu \"Elements\", który jest po prostu listą wszystkich Elementów użytych w złożeniu. Dobrym pomysłem jest zmiana ich nazw *(przyciskiem F2)*, szczególnie w większych złożeniach.

Spójrzmy na przykład

:   Stwórz nowy plik i z środowiska Część dodaj prostopadłościan i walec. Ustawimy walec na prostopadłościanie. Najpierw utwierdzimy część bazową, w naszym przypadku prostopadłościan. Wybierz dolną ścianę prostopadłościanu i wybierz wiązanie \"Locked\" (pierwsza ikona na [pasku](#Toolbars.md) Wiązania). Wybierz górną ścianę walca i górną ścianę prostopadłościanu. Następnie wybierz wiązanie \"Plane Coincident\". W tym momencie walec zostanie przesunięty na prostopadłościan i w drzewie, pod \"Constraints\", zostanie dodany nowy listek z dwoma węzłami podrzędnymi. Dodatkowo te same węzły podrzędne zostały dodane pod \"Elements\". Jeśli twój walec jest w środku prostopadłościanu zamiast na prostopadłościanie, poprawmy to najpierw: wybierz węzeł podrzędny pod \"Constraints\", który wskazuje na ścianę walca i przy pomocy kliknięcia prawym przyciskiem myszy wybierz w menu kontekstowym \"Flip Part\". Teraz walec jest już ustawiony na prostopadłościanie.

Kluczową rzeczą do zrozumienia jest to, że wiązanie działa na łączach do Elementów z listy w folderze drzewa \"Elements\". To pozwala na utrzymywanie nienaruszonej struktury wiązań podczas zmiany części. To jest bardzo trudne do zrozumienia bez przywołania przykładu.

Spójrzmy ponownie na powyższy przykład

:   Uwaga: upewnij się, że dodałeś \"Wiązanie blokady odległości\" to prostopadłościanu, bo inaczej przykład będzie wyglądał myląco
:   W oknie CAD wybierz inną ścianę prostopadłościanu. W tej chwili pracujemy tylko w widoku drzewa. Przesuń kursor myszki do drzewa, w miejsce gdzie prostopadłościan powinien zostać wybrany. Przeciągnij prostopadłościan do folderu \"Elements\". Upuść go na nazwę \"Elements\", a nie w żadne inne miejsce folderu - później zobaczymy dlaczego. Powinieneś zobaczyć kolejny Element dodany do listy \"Elements\". Teraz w folderze \"Constraints\" wybierz węzeł podrzędny dla ściany prostopadłościanu w wiązaniu \"Plane Coincident\" i usuń go. Wiązanie będzie pokazywać znak wykrzyknienia, ponieważ brakuje mu jednego Elementu. Zauważ, że usuwając Element w Wiązaniu *nie* usunęliśmy go z listy. Jest tak ponieważ wiązanie było tylko łączem do Elementu na liście. Teraz weźmy nowo dodany Element w liście \"Elements\" i przeciągnijmy go na wiązanie \"Plane Coincident\". W tym momencie walec przesunął się na drugą zaznaczoną ścianę Może być konieczne ponowne wybranie \"Flip Part\" z menu kontekstowego, jeśli walec znów znajduje się w środku prostopadłościanu.

Wcześniejszy przykład pokazał, że możliwa jest zmiana Elementów wykorzystywanych do wiązania bez konieczności usuwania samego wiązania. W ten sam sposób możemy przenieść walec do całkowicie innej części. Po nieco dłuższym eksperymentowaniu z tym przykładem, zauważysz inne rzeczy, jak:

-   Jeśli zmienisz nazwę Elementu na liście, to nazwa ta zostanie zmieniona we wszystkich wiązaniach.
-   Możesz użyć jednego Elementu z listy w kilku wiązaniach.
-   Możesz użyć Okna Właściwości Elementu by dodać **Odsunięcie**. W naszym przykładzie pozwala to przesunąć walec w stosunku do ściany prostopadłościanu.
-   Możesz użyć przycisku \"Pokaż Układ Współrzędnych Elementu\" na głównym pasku narzędzi by zobaczyć co \"Menu kontekstowe / Flip Part\" i \"Menu kontekstowe / Flip Element\" robią. Upewnij się, że obserwujesz co się dzieje w Oknie Właściwości.
-   Możesz dodać wiązanie w całkowicie innej kolejności: najpierw dodaj kilka Elementów do \"Listy Elementów\" *(nadawanie nazw jest przydatne, np. \"Górna Ściana Prostopadłościanu czy \"Przednia Ściana Prostopadłościanu\")* a następnie dodaj wiązanie bez zaznaczania czegokolwiek - będzie ono pustym wiązaniem. Potem przeciągnij Elementy z listy \"Elementów\". Wynik będzie takim sam jak po tym co zrobiliśmy w pierwszym przykładzie. Po wykonaniu tego ćwiczenia natura działania wiązań z Elementami powinna stać się jasna.
-   Możesz zmienić istniejące wiązanie pomiędzy istniejącymi Elementami po prostu przez wybranie innej pozycji w właściwości Okno Właściwości/ConstraintType.


{{top}}

## Zgodność

Złożenie 3 zostało zainspirowane przez [Złożenie 2](Assembly2_Workbench/pl.md), ale nie jest z nim kompatybilne. Jeśli masz starsze modele wykonane w środowisku Złożenie2, powinieneś zostać przy FreeCAD 0.16 i używać środowiska Złożenie 2.

Nowe modele wykonane przy użyciu środowiska Złożenie 3 powinny być otwierane i edytowane tylko w tym środowisku pracy.

Mimo, że mogą mieć podobne narzędzia, środowisko Złożenie 3 nie jest zgodne ze środowiskiem [A2plus](A2plus_Workbench/pl.md) ani [Złożenie 4](Assembly4_Workbench/pl.md). Modele stworzone w tych środowiskach powinny być otwierane tylko w odpowiadających im środowiskach.


{{top}}

## Testowanie

The [Assembly3 Workbench](Assembly3_Workbench.md) is under development and is not yet available (April 2020) through the [Addon Manager](Std_AddonMgr.md), but it is expected that this will happen at some point.

You can test it in two ways:

-   A special fork of FreeCAD made by realthunder; see [FreeCAD\_assembly3 releases](https://github.com/realthunder/FreeCAD_assembly3/releases). This fork is based on a particular commit of the master branch of FreeCAD, but it also has additional features currently not present in the master branch. Due to this fork being based on a particular development snapshot, it does not have the latest features merged daily to the master branch.
-   The development [AppImage](AppImage.md); this is based on the current master branch, and includes the dependencies needed for working with Assembly3 such as the SolveSpace solver.

Since the AppImage only works for Linux, for Windows users at the moment the only option to test Assembly3 is the first option (realthunder\'s fork).


{{top}}

## HowTo

### Get Started 

There are many ways to create an assembly with Assembly3. Here is the most simple one you can do.

:   <img alt="" src=images/Assembly3_Example-GettingStarted.jpg  style="width:600px;">
:   *Final Result of the Getting Started Example. In the image the Assembly3 Worksbench is selected, so its multiple toolbars are visible. Note that the vertical \"TabBar\" left of the tree view is an AddOn Workbench that is not contained in standard FreeCAD (but can be installed with the Addon-Manager).*

-   Press **<img src="images/Std_New.svg" width=16px> [New](Std_New.md)** to create a new FreeCAD file
-   Change to <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) workbench
-   Select **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly.md)
**
-   Change to <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> _ and a <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Cube](Part_Box.md)
-   <img alt="" src=images/Std_Save.svg  style="width:16px;"> _ and <img alt="" src=images/Std_Open.svg  style="width:16px;"> [Open\...](Std_Open.md) the file again

The tree view should look like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-01.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-02.png  style="width:280px;">

-   Now *Drag&Drop* with the mouse both **Cylinder** and **Cube** onto the **Parts** folder. They are moved into that folder.

    :   That is the quickest way and suitable for simple cases like this. A better way is via the use of link objects:
    :   Select **Cube** and **Cylinder** and then **<img src="images/Std_LinkMake.svg" width=16px> [Make link](Std_LinkMake.md)** either from the **Context menu** (-\> LinkActions -\> MakeLink) or the **Structure** panel.
    :   This adds two link objects. Then *Drag&Drop* the link objects to the **Parts** folder.
-   Click both top surfaces of **Cylinder** and **Cube** (keep Ctrl pressed (Cmd on a Mac))
-   Change to <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) workbench
-   Select **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Plane Coincidence](Assembly3_ConstraintCoincidence.md)** from the [Main constraints toolbar](#Main_Constraints_Toolbar.md).

Now the parts should be joined into each other and your tree should look like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-03.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-04.png  style="width:280px;">

-   Right click **\_Element** (either of the two) and select **Flip Part**.

Now the **Cylinder** should be on top of the **Cube**. If the whole thing is upside down, go back and select **Flip Part** on the other element.

:   We omitted one important step that should be done in larger assemblies: Locking a base part.
:   That means to define one part that should not be moved by constraints. In this example we use the **Cube** for that:
    -   Select the lower face of the **Cube**. Only the lower face, not the whole **Cube**
    -   select the **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Locked](Assembly3_ConstraintLock.md)** constraint from the [Main constraints toolbar](#Main_Constraints_Toolbar.md)

Done.

The finished assembly tree should look like (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-05.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-06.png  style="width:280px;">:

If you like you can move the **Locked** constraint upwards in the tree. Use the **<img src="images/Assembly_TreeItemUp.svg‎‎" width=16px> [Move item up](Assembly3_MoveItemUp.md)** button on the [Main toolbar](#Main_Toolbar.md) for that.

**Note:** all new external files must be **saved**, **closed** and re-**opend** at least once, so that Assembly3 can find it.

:   Without doing that FreeCAD can not give a file handle to the Assembly3 Workbench and it can not find the new part.
:   When all parts are in the same file, you should **save**, **close** and re-**open** this file, too.


{{top}}

### Add an Offset 

Assembly3 does not offer Offset with the constaints in the way the [A2plus Workbench](A2plus_Workbench.md) or other CAD tools do. Instead it offers a more general and flexible system to add offsets translations but also angles.

-   Add the offset in the properties of one [Elements](#Elements.md) of a [Constraint](#Constraint.md).

    :   you can choose which one of the two you want to use.

Example:

-   Add 2 cubes to an assembly and select their side faces.
-   select \"PlaneCoincident\". The cubes will be attached inside each other.
-   select one Element and *ContextMenu/Flip Part*. The cubes will be attached side-by-side.
-   select one Element property Offset/Position/Zz and set to 5mm. The cubes will be 5mm apart.

:\* Test with other axes or the angle/axis fields. Also verify that you get the same result when using the other Element. This is the same approach for all other constraints.


{{top}}

### Solve a Solver Failure 

This often happens when parts are over-constrained, i.e. more than 6 DOF are locked.

The easiest way to find the problem is to click relevant constraints in the tree and select *ContextMenu/Disable* and re-calculate. It is helpful to know the last added constraints before the solver failed and just undo them.

Note: as Assembly3 tries to compensate for over-constraint parts behind the scenes, sometimes the problem is just triggered by a new constraint but the root cause is somewhere different. Before deleting all and starting again, remember that you can re-use Elements. If you named them you can identify the required elements and re-build the constraints without using the 3D view at all. See [Elements](#Elements.md) seciton above.


{{top}}

### Replace a part or rename a filename 

When a part is removed or when a filename changes, the assembly breaks, it can not longer be solved and the solver will issue the message \"Inconsistent constraints\". The solver marks invalid Elements and Constrains with a question mark in the tree.

One way to solve this is to just delete all invalid constraints and elements, import the new part and redo everything. But there is a better way:

-   Rename a file
    1.  Use a file manager and copy the file you want renamed. Then give the new name to the copy.
    2.  Open the copy in FreeCAD. The assembly and the old file should also be open
    3.  Select the old object in the tree and click to change the propery \"Linked object\" (it does contain the old filename)
    4.  A list dialog will open containing all open parts. It shows the filenames and objects of each part. The old part and object is selected. Locate the renamed part in the tree and select the same object in the new part. Then confim the selection.
    5.  Delete the old part in the tree. Also the file can be deleted now.
    6.  Constraints and elements of te old part became invalid. Open the constraint or Elements list in the tree. Then sequentially
        -   select each element surface on the new part. An item in the tree will be highliged.
        -   Take that item and drag&drop it over the old element (either in the element list or in one of the constraints where it was used). That element should become valid.
        -   Repeat the procedure for the remaining elements. Often a single element is enough to allow Assembly3 to identify the remaining elements of the part automatically.
        -   If an element was assigned to the wrong surface by accident, just repeat with the correct surface.
    7.  Change the object name in FreeCAD, if desired

-   Replace a part with another part

    :   *which is simular enough to the original part that the original constraints still make sense, of course*

    1.  Delete the old part in the tree. Also the file can be deleted.
    2.  Constraints and elements of te old part became invalid. Open the constraint or Elements list in the tree.
        -   Select an element surface on the new part. An item in the tree will be highliged.
        -   Take that item and drag&drop it over the old element (either in the element list or in one of the constraints where it was used). That element should become valid.
        -   repeat the procedure for the remaining elements.
        -   If an element was assigned to the wrong surface by accident, just repeat with the correct surface.
    3.  Change the object name in FreeCAD, if desired

\'\'Notes
\* They are not as complicated as it may seem here. After 2-3 times they should become second nature and feel really easy to do.

-   Its not only usually ways quicker than deleting and re-doing constraints, its also safer because an element could have been used in a parent assembly. Deleting the original would destroy that link, re-assingning would keep it.
-   Also this procedure becomes really quick and easy to do if constraints and elements are named. There is no guessing where the surfaces should be dragged&dropped to because the names tell it (see [Tips & Tricks](#Tips_.26_Tricks.md)).

\'\'


{{top}}

### Tips & Tricks 

-   Using hierarchical assemblies helps in avoiding solver issues and keeping you model fluid. You can freeze a subassembly with one click and save CPU resources easily (use the context menu in the tree). When loading an assembly Assembly3 does not need to open external files for frozen subassemblies which keeps the tree compact.
-   Is very helpful to make it a habit to name the elements and constraints. Use the **F2** key to do this quickly in the tree. You will find the tree sorting tools in the main toolbar very useful. An assembly with fully named constraints and elements is very easy to understand for other people or for oneself when looking at an older file.

    :   Examples for constraint names for a table could be \"Align\_FrontLegs\", \"Align\_FrameBottom-LegTops\" and element names could be \"Leg1\_Top\" or \"TableTop\_Front\", \"TableTop\_Left\".
-   Please note that once external files are opened by an assembly its not possible easy to close them again without closing the assembly. Since the assembly keeps open those files in the backgound, the tab may disappear but the file remains visible in the tree. If you have several layers of subassemblies it becomes close to impossible to close single files. This behaviour may change, but until then a possible approach could be to regulary use the commands *File/Save All* and *File/Close All* to clean up the tree before working on another sub-assembly.

    :   \'\'Example: consider you have a large CNC machine with a main assembly and a subassembly for each module. Once you have the main assembly open it may open literally hundreds of files down to a single ball bearing. Before working on the subassembly of the electronics cabinet of the machine it is a good idea to save and close all files to get an empty tree. Then open just the subassembly for the electronics cabinet. This will open all file it needs but ony those.
-   Using external files makes it easier to re-use a parts or do part versioning with systems like git or subversion. The workflow in FreeCAD with Assembly feels quite the same as with files that have all parts in the same file. For exchanging files often with other parties, single files might be more convenient.
-   Multiply linked parts. If you added a link into the assembly, it will have a property value named \"Element Count\", default 0. If you set this to 3 you get 3 instances of that part. They will be added into a subfolder and can be used like fully separte parts. Use this feature to keep the data footprint of your file low, because the part is saved only once. Each instance only contain the differences.
-   Insert multiple parts, e.g. Screws, with one click. Check out the [Assembly3 Wiki](https://github.com/realthunder/FreeCAD_assembly3/wiki/Constraints-and-Solvers) on the Github site. This is not only a stunning function (even a bit magic), but really really useful.

-   Using the [TabBar Workbench](https://github.com/triplus/TabBar) speeds up working with assembly. This adds a Toolbar with one button for each workbench. You can sort the toolbar and can put it where every you want it. Many people put it vertically on the left side just beside the tree view. Of you have Assembly3, Part, PartDesign and other often used workbenches close to the top switching between them becomes extremely easy.


{{top}}

## Odnośniki internetowe 

-   [App Link](App_Link.md) object that makes Assembly3 work.
-   [FreeCAD\_assembly3](https://github.com/realthunder/FreeCAD_assembly3) repository and documentation.
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712), big discussion thread.
-   [Test tutorial for Assembly 3 Workbench](https://forum.freecadweb.org/viewtopic.php?f=36&t=29562) by jpg87.
-   [Current Assembly Status](https://forum.freecadweb.org/viewtopic.php?f=20&t=34583)
-   [External workbenches](External_workbenches.md)
-   [Old Assembly project](Assembly_project.md) development plan, to get acquainted with the history of the issue.




_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Assembly3 Workbench/pl
