# Fine-tuning/pl
## Wprowadzenie

[Edytor preferencji](Preferences_Editor/pl.md) FreeCAD w menu **Edycja → Preferencje** jest powszechnie używany do wprowadzania i edycji tabeli parametrów programu.

Jednak możliwy jest również dostęp, modyfikacja i ręczne tworzenie parametrów za pomocą [Edytora parametrów](Std_DlgParameter/pl.md) znajdującego się w menu **Narzędzia → Edycja parameterów**.

Poniższa strona przedstawia listę parametrów, które nie są dostępne za pośrednictwem edytora preferencji aby dopracować instalację FreeCAD lub pokonać problemy. Wszystkie parametry można ustawić ręcznie w **BaseApp/Preferencje/**:



## Informacje ogólne 

-   **Addons/developerMode** (boolean): Ustaw wartość opcji na {{TRUE/pl}} aby włączyć tryb deweloperski [Menadżera dodatków](Std_AddonMgr.md). Zobacz stronę [Metadane pakietu](Package_Metadata/pl#Sprawdzanie_poprawno.C5.9Bci.md).

-   **Bitmaps/Theme/ThemeSearchPaths** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}} aby FreeCAD używał dołączonych ikon zamiast systemowego motywu ikon w Linuksie.

-   **Dialog/DontUseNativeColorDialog** *(boolean)*: Ustawienie okna dialogowego selektora kolorów. Ustaw wartość na {{FALSE/pl}}, jeśli chcesz, aby FreeCAD używał natywnego okna dialogowego koloru w twoim systemie, a nie okna Qt Color. Wartość domyślna to {{TRUE/pl}}.

-   **Dialog/DontUseNativeDialog** *(boolean)*: Ustawienie okna dialogowego pliku. Ustaw wartość na {{FALSE/pl}}, jeśli chcesz używać natywnego okna dialogowego Plik podczas otwierania plików lub {{TRUE/pl}}, aby używać okna dialogowego Qt File Picker. Domyślne zależy od ustawienia podczas kompilacji: #define (USE_QT_FILEDIALOG).

-   **Dialog/DontUseNativeFontDialog** *(boolean)*: Używane przez polecenie [Kształt z tekstu](Draft_ShapeString/pl.md). Ustaw wartość na {{FALSE/pl}}, aby użyć natywnego okna dialogowego Czcionka. Wartość domyślna to {{TRUE/pl}}.

-   **DockWindows/TreeView/Enabled** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby umożliwić dokowanie widżetu [Widok drzewa](Document_structure/pl.md) niezależnie od Widoku Połączonego. Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok połączony.

-   **DockWindows/PropertyView/Enabled** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby umożliwić dokowanie widżetu [Widok właściwości](Property_editor/pl.md) niezależnie od Widoku Połączonego. Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok.

-   **DockWindows/DAGView/Enabled** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby włączyć wersję testową dokowanego widżetu [DAG view](DAG_view/pl.md). Po zmianie wartości parametru potrzebny jest restart programu FreeCAD, aby widżet był dostępny na liście Panelu - Widok.

-   **Document/AutoNameDynamicProperty** *(boolean)*: Ustaw na wartość {{TRUE/pl}}, aby FreeCAD automatycznie zmieniał nazwy właściwości dynamicznych z niepoprawnie podaną nazwą zamiast wyrzucać wyjątek. Zwróć uwagę, że kod Pythona nie będzie miał dostępu do nowej nazwy.

-   **Document/ChangeViewProviderTouchDocument** *(boolean)*: Ustaw wartość opcji na `False` aby zmiany widoczności elementów nie oznaczały dokumentu jako zmodyfikowany.

-   **Document/SaveThumbnailFix** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby naprawić problem z Qt5, który uniemożliwia generowanie miniaturek plików `.FCStd`.

-   **General/LockToolBars** *(boolean)*: Ustaw wartość na {{TRUE/pl}}, aby uniemożliwić przeciąganie pasków narzędzi i ukryć małe uchwyty do przeciągania. Najczęściej używane w połączeniu z arkuszami stylów, które sprawiają, że paski narzędzi są pionowe.

-   **General/RecentIncludesExported** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} to include exported files in the Recent Files list. Defaults to {{FALSE/pl}}.

-   **General/RecentIncludesImported** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}} to exclude imported files from the Recent Files list. Defaults to {{TRUE/pl}}.

-   **Macro/DuplicateFrom001** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby zawsze rozpoczynać poszukiwanie sugerowanej nazwy pliku z duplikatem makra od \@001 zamiast aktualnego \@NNN *(jeśli dotyczy)*. Domyślna wartość {{FALSE/pl}}.

-   **Macro/DuplicateIgnoreExtraNote** *(boolean)*: Ustaw wartość na {{TRUE/pl}}, aby zignorować dodatkową notatkę podczas sugerowania zduplikowanej nazwy pliku makra. Dodatkowa uwaga to tekst w nazwie pliku po \"@NNN\" i przed \".FCMacro\". Przykład: \"my_macro@005.my_note.FCMacro\". Jeżeli ustawiono wartość {{TRUE/pl}}, następną sugerowaną nazwą pliku będzie \"my_macro@006.FCMacro\". Jeżeli {{FALSE/pl}}, to następną sugerowaną nazwą pliku jest \"my_macro@006.my_note.FCMacro\". Aby tekst został rozpoznany jako dodatkowa notatka, powinien zaczynać się od kropki (\".\") po członie \"@NNN\". W przeciwnym razie, na przykład \"my_macro@006_my_note.FCMacro\" otrzyma \"my_macro@006_my_note@001.FCMacro\" jako sugerowaną nową nazwę pliku, co może być pożądane w niektórych przypadkach. Domyślną wartością jest {{FALSE/pl}}.

-   **Macro/ReplaceSpaces** *(boolean)*: Ustaw wartość na {{FALSE/pl}}, jeśli nie chcesz, aby spacje w nazwach plików były automatycznie zamieniane na podkreślenia podczas tworzenia, zmiany nazwy lub powielania makra. Nie ma to wpływu na istniejące pliki, ma znaczenie tylko przy tworzeniu nowego pliku, zmianie nazwy lub powielaniu istniejącego. Domyślną wartością jest {{TRUE/pl}}.

-   **MainWindow/ClearMenuBar** (boolean): Ustaw wartość na {{TRUE/pl}} aby wyczyścić pasek menu przy zmianie środowiska pracy, przydatne gdy używasz globalnego menu, gdyż może ono nie aktualizować się przy zmianie środowiska pracy i szybko stać się zagracone wpisami w menu każdego środowiska. Domyślna wartość to {{FALSE/pl}}. Na macOS jest oczyszczane w każdym przypadku, aby obejść błąd w Qt.

-   **MainWindow/ToolBarNameAsToolTip** (boolean): Ustaw wartość na {{FALSE/pl}}, aby nie wyświetlać nazwy paska narzędzi jako etykiety. Domyślnie {{TRUE/pl}}.

-   **PropertyView/AutoTransactionView** *(boolean)*: Ustawienie wartość opcji na {{TRUE/pl}} powoduje, że zmiany właściwości karty Widok są dodawane do stosu cofania *(a więc można je cofnąć)*. Domyślną wartością jest {{FALSE/pl}}.

-   **Selection/AutoShowSelectionView** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby panel Widok zaznaczenia wyświetlał się automatycznie po wybraniu obiektu. Domyślnie {{FALSE/pl}}.

-   **Selection/singleClickFeatureSelect** *(boolean)*: Ustaw opcję na wartość {{FALSE/pl}}, aby wyłączyć możliwość wyboru elementu jednym kliknięciem w środowisku Projekt Części. Domyślnie {{TRUE/pl}}.

-   **TreeView/HideColumn** *(boolean)*: Ustaw wartość parametru na {{True/pl}}, aby ukryć kolumnę **Opis** w oknie [Widoku drzewa](Tree_view.md). Domyślnie {{FALSE/pl}}.

-   **TreeView/TreeViewStretchDescription** (boolean): Ustaw opcję na wartość {{FALSE/pl}}, aby rozciągnąć kolumnę \"Opis\" w oknie [widoku drzewa](Tree_view/pl.md) do prawej krawędzi panelu. Wartość domyślna to {{FALSE/pl}}.

-    {{VersionMinus/pl|0.20}}
    

-   **View/Dimensions3dColor** (ciąg znaków): Ustaw wartość koloru w formacie szesnastkowym `#RRGGBB`, aby zmienić kolor wyświetlania wymiarów bezpośrednich w narzędziu [Część: Wymiarowanie liniowe](Part_Measure_Linear/pl.md).

Dla {{VersionPlus/pl|0.21}} patrz [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Pomiary.md).

-    {{VersionMinus/pl|0.20}}
    

-   **View/DimensionsAngularColor** (ciąg znaków): Ustaw wartość koloru w formacie heksadecymalnym `#RRGGBB`, aby zmienić kolor wyświetlania wymiaru kątowego w narzędziu [Część: Wymiarowanie kątowe](Part_Measure_Angular/pl.md).

Dla {{VersionPlus/pl|0.21}} patrz [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Pomiary.md).

-    {{VersionMinus/pl|0.20}}
    

-   **View/DimensionsDeltaColor** (ciąg znaków): Ustaw wartość koloru heksadecymalnego w formacie `#RRGGBB`, aby zmienić kolor wyświetlania wymiarów ortogonalnych w narzędziu [Część: Wymiarowanie liniowe](Part_Measure_Linear/pl.md).

Dla {{VersionPlus/pl|0.21}} patrz [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Pomiary.md).

-   **View/NavigationDebug** *(boolean)*: Włącza debugowanie stylów nawigacji *(od wersji v0.19 tylko styl nawigacji Gesture ma coś do powiedzenia)*.
-   **View/NavigationDebug** *(boolean)*: Udostępnia możliwość debugowania stylów nawigacji *(od v0.19, tylko styl nawigacji Gesture znajduje zastosowanie)*.
-   **View/SavePicture** *(string)*: Ustaw wartość opcji na **FramebufferObject**, **PixelBuffer** lub **CoinOffscreenRenderer** dla różnych metod tworzenia obrazów w oknie widoku 3D.



## Domyślna nazwa pliku eksportu 

-   **General/ExportDefaultFilenameMultiple** *(string)*: Ustaw domyślną nazwę pliku, która będzie używana podczas eksportu wielu obiektów. Domyślną wartością jest \"**%F**\".
-   **General/ExportDefaultFilenameSingle** *(string)*: Ustaw domyślną nazwę pliku, która będzie używana podczas eksportu pojedynczego obiektu. Domyślną wartością jest \"**%F-%P-**\".

Obie te opcje umożliwiają automatyczne wstawianie do nazwy pliku różnych informacji, przy użyciu następujących znaków formatu:

-   %F - nazwa pliku .FCStd *(lub etykieta, jeśli nie jest jeszcze zapisana)*
-   %Lx - etykieta wybranego obiektu *(obiektów)*, oddzielona znakiem \'x\'
-   %Px - etykieta zaznaczonego obiektu*(ów)* i ich pierwszego rodzica, oddzielona znakiem \'x\'
-   %U - data i godzina, w UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - data i czas, w lokalnej strefie czasowej, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

Wszelkie inne znaki traktowane są dosłownie. Jeśli wynikowa nazwa pliku jest nieprawidłowa, zostanie zmieniona przy zapisie, a nieprawidłowe znaki zostaną zastąpione znakiem podkreślenia *\' **\_** \'*.



## Powiązane z myszką 

-   **General/ComboBoxWheelEventFilter** *(boolean)*: Należy ustawić wartość `True`, aby widżety nie przechwytywały zdarzeń związanych z kółkiem myszy i uniemożliwiały przewijanie obszarów, które można przewijać. Wymaga uwzględnienia ponownego uruchomienia programu FreeCAD.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** *(string)*: Komendy, które mają być wykonywane za pomocą gestów przewijania przycisków myszy w stylu nawigacji Gesture.
-   **View/GestureMoveThreshold** *(integer)*: Odległość, jaką musi pokonać kursor myszy *(px)*, aby wejść w tryb obrotu lub przesuwania w stylu nawigacji Gesture. Wartość domyślna 5.
-   **View/GestureTapHoldTimeout** *(integer)*: Określa jak długo trzeba czekać *(w milisekundach)*, aby wejść w tryb obrotu w stylu nawigacji Gesture. Pomocne może być zwiększenie wartości, jeśli przeciąganie geometrii w szkicowniku jest trudne. Domyślnie jest to wartość 700.



## Skróty klawiaturowe 



### Klawisz ESC 

-   **General/TasksKeyEsc** *(boolean)*: Utwórz i ustaw wartość na `False`, aby wyłączyć wychodzenie klawiszem **ESC** z [Panelu zadań](Task_panel/pl.md) we wszystkich środowiskach pracy *(to znaczy, jeśli panel zadań jest aktywny)*.



## Kostka nawigacyjna 

Zobacz stronę [Kostka nawigacyjna](Navigation_Cube/pl#Parametry_zaawansowane.md).



## Szczególne środowiska pracy 



### <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [środowisko pracy BIM](BIM_Workbench/pl.md) 

-   **Mod/BIM/DefaultPageScale** *(float)*: Domyślne skalowanie dla nowych stron Rysunku Technicznego utworzonych z poziomu środowiska pracy BIM, w przypadku gdy szablon nie zawiera żadnego edytowalnego pola tekstowego \"Skala\" lub \"Skalowanie\" *(wielkość liter nie ma znaczenia)*.



### <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md) 

-   **Mod/Draft/defaultCameraHeight** *(int)*: Ustawia wysokość kamery, gdy w pustym dokumencie Draft zostanie uruchomiona edycja projektu. Wartość 0 wyłącz, wartość domyślna FreeCAD to 5, dobra przy pracy w milimetrach, dobra wysokość przy pracy w Środowisku pracy Arch to 4500.



### <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [środowisko pracy Część](Part_Workbench/pl.md) 

-   **Mod/Part/ParametricRefine** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby funkcja [udoskonal kształt](Part_RefineShape/pl.md) utworzyła niezależną kopię, a nie linkowaną. Domyślną wartością jest {{TRUE/pl}} jeśli wartość nie jest dostępna.



### <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [środowisko pracy Projekt Części](PartDesign_Workbench/pl.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby zapewnić, że helisa addytywna, która nie przecina ciała, jest widoczna w podglądzie. Domyślną wartością jest {{FALSE/pl}}.
-   **Mod/PartDesign/SubtractiveHelixPreview** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby upewnić się, że helisa odejmowana, która nie przecina ciała, jest widoczna w podglądzie. Wartością domyślną jest {{TRUE/pl}}.
-   **Mod/PartDesign/SwitchToTask** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby uniemożliwić przełączenie na panel zadań podczas uruchamiania Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md). Wartością domyślną jest {{TRUE/pl}}, jeśli wartość nie jest dostępna.
-   **Mod/PartDesign/SwitchToWB** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby zapobiec automatycznemu wywołaniu Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md), gdy aktywowana jest opcja [zawartość](PartDesign_Body/pl.md). Wartością domyślną jest {{TRUE/pl}}, jeśli wartość nie jest dostępna.



### <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [środowisko pracy Path](Path_Workbench/pl.md) 

-   Środowisko pracy[Path](Path_Workbench/pl.md) posiada przełącznik umożliwiający włączenie eksperymentalnych funkcji udokumentowanych na stronie [Funkcje eksperymentalne](Path_experimental/pl.md).



### <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [środowisko pracy Szkicownik](Sketcher_Workbench/pl.md) 

-   **Mod/Sketcher/RadiusDiameterConstraintDisplayAngleRandomness** *(float)*: Ustawia losowość kąta na powyższej wartości. Wartość to zakres losowego kąta, wyśrodkowany na kącie bazowym. Domyślnie jest to 0 stopni.
-   **Mod/Sketownik/RadiusDiameterConstraintDisplayBaseAngle** *(float)*: Ustawia kąt *(od poziomu)* używany do wyświetlania wiązań promienia/średnicy w Szkicowniku w czasie tworzenia. Domyślnie 15 stopni *(jeśli nie ustawiono wartości)*.
-   **Mod/Sketcher/RoundRectangleSuggConstraints** *(boolean)*: Ustaw na wartość {{FALSE/pl}}, aby wyłączyć dodawanie dwóch dodatkowych punktów konstrukcyjnych podczas tworzenia zaokrąglonego prostokąta. {{Version/pl|0.21}}



#### Kolory etykiet wiązań 

Etykieta w Szkicowniku, która wyświetla aktualny stan wiązań (np. \" Nie w pełni wiązany\", \" W pełni wiązany\" itd.) jest stylizowana dla każdego stanu za pomocą arkusza stylów Qt lub preferencji użytkownika. Preferencje użytkownika mają pierwszeństwo, jeśli zostały ustawione *(w **Mod/Szkicownik/Ogólne**)*:

-   Kolor komunikatu **Pustego szkicu** - domyślnie czarny z 50% kryciem.
-   Kolor komunikatu **Nie w pełni związany** - domyślnie czarny.
-   Kolor komunikatu **Nieprawidłowo sformułowane wiązanie** - domyślnie czerwony.
-   Kolor komunikatu **Wiązanie konfliktowe** - domyślnie czerwony.
-   Kolor komunikatu **Wiązanie nadmiarowe** - domyślnie czerwony.
-   Kolor komunikatu **Wiązanie częściowo nadmiarowe** - domyślnie królewski niebieski.
-   Kolor komunikatu **Błąd solwera** - domyślnie czerwony.
-   Kolor komunikatu **Związany w pełni** - domyślnie zielony.



### <img alt="" src=images/Workbench_Start.svg  style="width:24px;"> [środowisko pracy Start](Start_Workbench/pl.md) 

-   **Mod/Start/DefaultImportXXX** *(string)*: Gdzie XXX to rozszerzenie pliku pisane małymi literami. Na przykład DefaultImportifc dla plików .IFC. Umożliwia ustawienie domyślnego modułu importu, który będzie używany po kliknięciu ikony na stronie startowej, gdy dostępnych jest kilka importerów. Na przykład ustawienie DefaultImportifc = ifc_import spowoduje użycie importera NativeIFC, jeśli jest dostępny. {{Version/pl|0.21}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/pl
