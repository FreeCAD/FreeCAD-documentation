# Fine-tuning/pl
{{TOCright}}

Na tej stronie znajdują się różne ustawienia i parametry, które można wykorzystać do precyzyjnego skonfigurowania instalacji programu FreeCAD lub do rozwiązywania problemów.

## Parametry opcjonalne 

[Edytor preferencji](Preferences_Editor/pl.md) FreeCAD w menu **Edycja → Preferencje** jest powszechnie używany do wprowadzania i edycji tabeli parametrów programu.

Jednak możliwy jest również dostęp, modyfikacja i ręczne tworzenie parametrów za pomocą [Edytora parametrów](Std_DlgParameter/pl.md) znajdującego się w menu **Narzędzia → Edycja parameterów**.

Poniższa lista przedstawia parametry, które nie są dostępne za pośrednictwem edytora preferencji, ale które można ustawić ręcznie *(w **BaseApp/Preferencje**)*:

-   **Bitmaps/Theme/ThemeSearchPaths** (boolean): Ustaw wartość opcji na `False` aby FreeCAD używał dołączonych ikon zamiast systemowego motywu ikon w Linuksie.
-   **DockWindows/TreeView/Enabled** *(boolean)*: Ustaw wartość opcji na `True` aby umożliwić dokowanie widżetu [Widok drzewa](Document_structure/pl.md) niezależnie od Widoku Połączonego. Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok połączony.
-   **DockWindows/PropertyView/Enabled** *(boolean)*: Ustaw wartość opcji na `True` aby umożliwić dokowanie widżetu [Widok właściwości](Property_editor/pl.md) niezależnie od Widoku Połączonego. Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok.
-   **DockWindows/DAGView/Enabled** *(boolean)*: Ustaw opcje na `True` aby włączyć wersję testową dokowanego widżetu [DAG view](DAG_view.md). Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok.
-   **Document/ChangeViewProviderTouchDocument** *(boolean)*: Ustaw wartość opcji na `False` aby zmiany widoczności elementów nie oznaczały dokumentu jako zmodyfikowany.
-   **Document/SaveThumbnailFix** *(boolean)*: Ustaw wartość opcji na `True` aby naprawić problem z Qt5, który uniemożliwia generowanie miniaturek plików `.FCStd`.
-   **General/RecentIncludesExported** *(boolean)*: Ustaw wartość opcji na `True` to include exported files in the Recent Files list. Defaults to `False`.
-   **General/RecentIncludesImported** *(boolean)*: Ustaw wartość opcji na `False` to exclude imported files from the Recent Files list. Defaults to `True`.
-   **Mod/Draft/defaultCameraHeight** *(int)*: Ustawia wysokość kamery, gdy w pustym dokumencie Draft zostanie uruchomiona edycja projektu. Wartość 0 wyłącz, wartość domyślna FreeCAD to 5, dobra przy pracy w milimetrach, dobra wysokość przy pracy w Środowisku pracy Arch to 4500.
-   **Mod/Part/ParametricRefine** *(boolean)*: Ustaw wartość opcji na `False`, aby funkcja [udoskonal kształt](Part_RefineShape/pl.md) utworzyła niezależną kopię, a nie linkowaną. Domyślną wartością jest `True` jeśli wartość nie jest dostępna.
-   **Mod/PartDesign/AdditiveHelixPreview** *(boolean)*: Ustaw wartość opcji na `True` aby zapewnić, że helisa addytywna, która nie przecina ciała, jest widoczna w podglądzie. Domyślną wartością jest `False`.
-   **Mod/PartDesign/SubtractiveHelixPreview** *(boolean)*: Ustaw wartość opcji na `True` aby upewnić się, że helisa odejmowana, która nie przecina ciała, jest widoczna w podglądzie. Wartością domyślną jest `True`.
-   **Mod/PartDesign/SwitchToTask** *(boolean)*: Ustaw wartość opcji na `False`, aby uniemożliwić przełączenie na panel zadań podczas uruchamiania Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md). Wartością domyślną jest `True`, jeśli wartość nie jest dostępna.
-   **Mod/PartDesign/SwitchToWB** *(boolean)*: Ustaw wartość opcji na `False`, aby zapobiec automatycznemu wywołaniu Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md), gdy aktywowana jest opcja [zawartość](PartDesign_Body/pl.md). Wartością domyślną jest `True`, jeśli wartość nie jest dostępna.
-   **PropertyView/AutoTransactionView** *(boolean)*: Ustaw wartość opcji na `True` więc zmiany właściwości zakładki Widok są dodawane do stosu Cofnij *(stąd są cofane)*. Domyślną wartością jest `False`.
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

## Powiązane z myszką 

-   **General/ComboBoxWheelEventFilter** *(boolean)*: Należy ustawić wartość `True`, aby widżety nie przechwytywały zdarzeń związanych z kółkiem myszy i uniemożliwiały przewijanie obszarów, które można przewijać.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** *(string)*: Komendy, które mają być wykonywane za pomocą gestów przewijania przycisków myszy w stylu nawigacji Gesture.
-   **View/GestureMoveThreshold** *(integer)*: Odległość, jaką musi pokonać kursor myszy *(px)*, aby wejść w tryb obrotu lub przesuwania w stylu nawigacji Gesture. Wartość domyślna 5.
-   **View/GestureTapHoldTimeout** *(integer)*: Określa jak długo trzeba czekać *(w milisekundach)*, aby wejść w tryb obrotu w stylu nawigacji Gesture. Pomocne może być zwiększenie wartości, jeśli przeciąganie geometrii w szkicowniku jest trudne. Domyślnie jest to wartość 700.

## Skróty klawiaturowe 

### Klawisz ESC 

### Klawisz ESC 

-   **General/TasksKeyEsc** *(boolean)*: Utwórz i ustaw wartość na `False`, aby wyłączyć wychodzenie klawiszem **ESC** z [Panelu zadań](Task_panel/pl.md) we wszystkich środowiskach pracy *(to znaczy, jeśli panel zadań jest aktywny)*. **Uwaga:** Zastąpiono przez [Preferencje szkicownika](Sketcher_Preferences/pl#Og.C3.B3lne.md).
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




[Category:Developer Documentation](Category:Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Fine-tuning/pl
