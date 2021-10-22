# Fine-tuning/pl
{{TOCright}}

Na tej stronie znajdują się różne ustawienia i parametry, które można wykorzystać do precyzyjnego skonfigurowania instalacji programu FreeCAD lub do rozwiązywania problemów.

## Parametry opcjonalne 

[Edytor preferencji](Preferences_Editor/pl.md) FreeCAD w menu **Edycja → Preferencje** jest powszechnie używany do wprowadzania i edycji tabeli parametrów programu.

Jednak możliwy jest również dostęp, modyfikacja i ręczne tworzenie parametrów za pomocą [Edytora parametrów](Std_DlgParameter/pl.md) znajdującego się w menu **Narzędzia → Edycja parameterów**.

Poniższa lista przedstawia parametry, które nie są dostępne za pośrednictwem edytora preferencji, ale które można ustawić ręcznie *(w **BaseApp/Preferencje**)*:

-   **Bitmaps/Theme/ThemeSearchPaths** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}} aby FreeCAD używał dołączonych ikon zamiast systemowego motywu ikon w Linuksie.
-   **DockWindows/TreeView/Enabled** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby umożliwić dokowanie widżetu [Widok drzewa](Document_structure/pl.md) niezależnie od Widoku Połączonego. Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok połączony.
-   **DockWindows/PropertyView/Enabled** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby umożliwić dokowanie widżetu [Widok właściwości](Property_editor/pl.md) niezależnie od Widoku Połączonego. Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok.
-   **DockWindows/DAGView/Enabled** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby włączyć wersję testową dokowanego widżetu [DAG view](DAG_view/pl.md). Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok.
-   **Document/ChangeViewProviderTouchDocument** *(boolean)*: Ustaw wartość opcji na `False` aby zmiany widoczności elementów nie oznaczały dokumentu jako zmodyfikowany.
-   **Document/SaveThumbnailFix** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby naprawić problem z Qt5, który uniemożliwia generowanie miniaturek plików `.FCStd`.
-   **General/LockToolBars** *(boolean)*: Ustaw wartość na {{TRUE/pl}}, aby uniemożliwić przeciąganie pasków narzędzi i ukryć małe uchwyty do przeciągania. Najczęściej używane w połączeniu z arkuszami stylów, które sprawiają, że paski narzędzi są pionowe.
-   **General/RecentIncludesExported** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} to include exported files in the Recent Files list. Defaults to {{FALSE/pl}}.
-   **General/RecentIncludesImported** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}} to exclude imported files from the Recent Files list. Defaults to {{TRUE/pl}}.
-   **General/SubstituteDecimalSeparator** *(boolean)*: Jeśli opcja jest ustawiona na wartość {{TRUE/pl}},znak kropki / przecinka będzie zastępowany regionalnym separatorem dziesiętnym podczas wprowadzania liczby w polu numerycznym. Zastąpienie nastąpi tylko wtedy, gdy kropka nie jest regionalnym separatorem dziesiętnym i spełniony jest co najmniej jeden z następujących warunków: kropka nie jest regionalnym separatorem tysięcy lub kropka została wprowadzona z klawiatury numerycznej. Domyślna wartość {{FALSE/pl}}.
-   **Macro/DuplicateFrom001** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby zawsze rozpoczynać poszukiwanie sugerowanej nazwy pliku z duplikatem makra od \@001 zamiast aktualnego \@NNN *(jeśli dotyczy)*. Domyślna wartość {{FALSE/pl}}.
-   **Macro/DuplicateIgnoreExtraNote** *(boolean)*: Ustaw wartość na {{TRUE/pl}}, aby zignorować dodatkową notatkę podczas sugerowania zduplikowanej nazwy pliku makra. Dodatkowa uwaga to tekst w nazwie pliku po \"\@NNN\" i przed \".FCMacro\". Przykład: \"my\_macro\@005.my\_note.FCMacro\". Jeżeli ustawiono wartość {{TRUE/pl}}, następną sugerowaną nazwą pliku będzie \"my\_macro\@006.FCMacro\". Jeżeli {{FALSE/pl}}, to następną sugerowaną nazwą pliku jest \"my\_macro\@006.my\_note.FCMacro\". Aby tekst został rozpoznany jako dodatkowa notatka, powinien zaczynać się od kropki (\".\") po członie \"\@NNN\". W przeciwnym razie, na przykład \"my\_macro\@006\_my\_note.FCMacro\" otrzyma \"my\_macro\@006\_my\_note\@001.FCMacro\" jako sugerowaną nową nazwę pliku, co może być pożądane w niektórych przypadkach. Domyślną wartością jest {{FALSE/pl}}.
-   **Macro/ReplaceSpaces** *(boolean)*: Ustaw wartość na {{FALSE/pl}}, jeśli nie chcesz, aby spacje w nazwach plików były automatycznie zamieniane na podkreślenia podczas tworzenia, zmiany nazwy lub powielania makra. Nie ma to wpływu na istniejące pliki, ma znaczenie tylko przy tworzeniu nowego pliku, zmianie nazwy lub powielaniu istniejącego. Domyślną wartością jest {{TRUE/pl}}.
-   **Mod/Draft/defaultCameraHeight** *(int)*: Ustawia wysokość kamery, gdy w pustym dokumencie Draft zostanie uruchomiona edycja projektu. Wartość 0 wyłącz, wartość domyślna FreeCAD to 5, dobra przy pracy w milimetrach, dobra wysokość przy pracy w Środowisku pracy Arch to 4500.
-   **Mod/Part/ParametricRefine** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby funkcja [udoskonal kształt](Part_RefineShape/pl.md) utworzyła niezależną kopię, a nie linkowaną. Domyślną wartością jest {{TRUE/pl}} jeśli wartość nie jest dostępna.
-   **Mod/PartDesign/AdditiveHelixPreview** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby zapewnić, że helisa addytywna, która nie przecina ciała, jest widoczna w podglądzie. Domyślną wartością jest {{FALSE/pl}}.
-   **Mod/PartDesign/SubtractiveHelixPreview** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby upewnić się, że helisa odejmowana, która nie przecina ciała, jest widoczna w podglądzie. Wartością domyślną jest {{TRUE/pl}}.
-   **Mod/PartDesign/SwitchToTask** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby uniemożliwić przełączenie na panel zadań podczas uruchamiania Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md). Wartością domyślną jest {{TRUE/pl}}, jeśli wartość nie jest dostępna.
-   **Mod/PartDesign/SwitchToWB** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby zapobiec automatycznemu wywołaniu Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md), gdy aktywowana jest opcja [zawartość](PartDesign_Body/pl.md). Wartością domyślną jest {{TRUE/pl}}, jeśli wartość nie jest dostępna.
-   **PropertyView/AutoTransactionView** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} więc zmiany właściwości zakładki Widok są dodawane do stosu Cofnij *(stąd są cofane)*. Domyślną wartością jest {{FALSE/pl}}.
-   **Selection/AutoShowSelectionView** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby panel Widok zaznaczenia wyświetlał się automatycznie po wybraniu obiektu. Domyślnie {{FALSE/pl}}.
-   **View/NavigationDebug** *(boolean)*: Włącza debugowanie stylów nawigacji *(od wersji v0.19 tylko styl nawigacji Gesture ma coś do powiedzenia)*.
-   **View/NavigationDebug** *(boolean)*: Udostępnia możliwość debugowania stylów nawigacji *(od v0.19, tylko styl nawigacji Gesture znajduje zastosowanie)*.
-   **View/SavePicture** *(string)*: Ustaw wartość opcji na **FramebufferObject**, **PixelBuffer** lub **CoinOffscreenRenderer** dla różnych metod tworzenia obrazów w oknie widoku 3D.

### Domyślna nazwa pliku eksportu 

-   **General/ExportDefaultFilenameMultiple** *(string)*: Ustaw domyślną nazwę pliku, która będzie używana podczas eksportu wielu obiektów. Domyślną wartością jest \"**%F**\".
-   **General/ExportDefaultFilenameSingle** *(string)*: Ustaw domyślną nazwę pliku, która będzie używana podczas eksportu pojedynczego obiektu. Domyślną wartością jest \"**%F-%P-**\".

Obie te opcje umożliwiają automatyczne wstawianie do nazwy pliku różnych informacji, przy użyciu następujących znaków formatu:

-   %F - nazwa pliku .FCStd *(lub etykieta, jeśli nie jest jeszcze zapisana)*
-   %Lx - etykieta wybranego obiektu *(obiektów)*, oddzielona znakiem \'x\'
-   %Px - etykieta zaznaczonego obiektu*(ów)* i ich pierwszego rodzica, oddzielona znakiem \'x\'
-   %U - data i godzina, w UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - data i czas, w lokalnej strefie czasowej, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

Wszelkie inne znaki traktowane są dosłownie. Jeśli wynikowa nazwa pliku jest nieprawidłowa, zostanie zmieniona przy zapisie, a nieprawidłowe znaki zostaną zastąpione znakiem podkreślenia \'\' \' **\_** \' \'\'.

### Sketcher Constraint Label Colors 

The label in Sketcher that displays the current status of the constraints (e.g. \"Underconstrained,\" \"Overconstrained,\" \"Fully Constrained,\" etc.) is styleable on a per-state basis either using the Qt stylesheet, or via user preferences. User preferences take precedence if they have been set (in **Mod/Sketcher/General**):

-   **EmptySketchMessageColor** - Defaults to 50% opacity black
-   **UnderconstrainedMessageColor** - Defaults to black
-   **MalformedConstraintMessageColor** - Defaults to red
-   **ConflictingConstraintMessageColor** - Defaults to red
-   **RedundantConstraintMessageColor** - Defaults to orange red
-   **PartiallyRedundantConstraintMessageColor** - Defaults to royal blue
-   **SolverFailedMessageColor** - Defaults to red
-   **FullyConstrainedMessageColor** - Defaults to green

## Powiązane z myszką 

-   **General/ComboBoxWheelEventFilter** *(boolean)*: Należy ustawić wartość `True`, aby widżety nie przechwytywały zdarzeń związanych z kółkiem myszy i uniemożliwiały przewijanie obszarów, które można przewijać.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** *(string)*: Komendy, które mają być wykonywane za pomocą gestów przewijania przycisków myszy w stylu nawigacji Gesture.
-   **View/GestureMoveThreshold** *(integer)*: Odległość, jaką musi pokonać kursor myszy *(px)*, aby wejść w tryb obrotu lub przesuwania w stylu nawigacji Gesture. Wartość domyślna 5.
-   **View/GestureTapHoldTimeout** *(integer)*: Określa jak długo trzeba czekać *(w milisekundach)*, aby wejść w tryb obrotu w stylu nawigacji Gesture. Pomocne może być zwiększenie wartości, jeśli przeciąganie geometrii w szkicowniku jest trudne. Domyślnie jest to wartość 700.

## Skróty klawiaturowe 

### Klawisz ESC 

-   **General/TasksKeyEsc** *(boolean)*: Utwórz i ustaw wartość na `False`, aby wyłączyć wychodzenie klawiszem **ESC** z _.
-   **Mod/Sketcher/ViewKeyEsc** *(boolean)*: Utwórz i ustaw wartość na `False`, aby wyłączyć problemy z klawiszami **ESC** przy naciskaniu od jednego do wielu razy, podczas wychodzenia z trybu kontynuacji tworzenia geometrii / wiązań szkicownika.
    -   Źródło: [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=42207&start=60#p367584)

## Szczególne Środowiska pracy 

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw](TechDraw_Workbench/pl.md) ma kilka ukrytych przełączników opisanych w \[\[TechDraw\_Preferences/pl\#

Ustawienia ukryte\|Tech Draw: Preferencje\]\].

-   <img alt="" src=images/Workbench_Path.svg  style="width:16px;"> [Path](Path_Workbench/pl.md) posiada przełącznik pozwalający na włączenie funkcji eksperymentalnych opisanych w dokumencie [Path experimental](Path_experimental.md).
-   <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM](BIM_Workbench/pl.md):
    -   **Mod/BIM/DefaultPageScale** *(float)*: Domyślne skalowanie dla nowych stron TechDraw utworzonych w środowisku pracy BIM, w przypadku gdy szablon nie zawiera żadnego edytowalnego pola tekstowego „Skala" lub „Skalowanie" *(niewrażliwe na tekst)*.

## Powiązane

-   [Edytor parametrów](Std_DlgParameter/pl.md)
-   [Edytor ustawień](Preferences_Editor/pl.md)




_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/pl
