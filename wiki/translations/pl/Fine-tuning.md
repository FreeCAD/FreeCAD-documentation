# Fine-tuning/pl
## Wprowadzenie

[Edytor preferencji](Preferences_Editor/pl.md) FreeCAD w menu **Edycja → Preferencje** jest powszechnie używany do wprowadzania i edycji tabeli parametrów programu.

Jednak możliwy jest również dostęp, modyfikacja i ręczne tworzenie parametrów za pomocą [Edytora parametrów](Std_DlgParameter/pl.md) znajdującego się w menu **Narzędzia → Edycja parameterów**.

Poniższa strona przedstawia listę parametrów, które nie są dostępne za pośrednictwem edytora preferencji aby dopracować instalację FreeCAD lub pokonać problemy. Wszystkie parametry można ustawić ręcznie w **BaseApp/Preferencje/**:



## Informacje ogólne 

-   **Bitmaps/Theme/Name** (string): Wprowadź nazwę motywu ikon do nadpisania systemowego motywu ikon używanego przez FreeCAD. Stosowane tylko jeśli **Bitmaps/Theme/UseIconTheme** jest ustawione na {{TRUE/pl}}.
-   **Bitmaps/Theme/ThemeSearchPaths** (boolean): Ustaw na {{FALSE/pl}} aby FreeCAD korzystał ze swoich ikon zamiast motywu ikon systemowych na Linux. {{VersionMinus/pl|0.21}}. Dla starszych wersji użyj **Bitmaps/Theme/UseIconTheme** zamiast tego.
-   **Bitmaps/Theme/UseIconTheme** (boolean): Ustaw na {{TRUE/pl}} aby zmusić Qt do używania ikon z motywu systemowego. Domyślnie ustawienie to {{FALSE/pl}}, co sprawia, że FreeCAD korzysta ze swoich ikon. Nie ma to wpływu na inne mechanizmy motywów ikon Qt, takie jak okna systemowe, przyciski itp. Powinny one zawsze używać ikon z motywu systemowego. {{Version/pl|1.0}}
-   **Dialog/DontUseNativeColorDialog** *(boolean)*: Ustawienie okna dialogowego selektora kolorów. Ustaw wartość na {{FALSE/pl}}, jeśli chcesz, aby FreeCAD używał natywnego okna dialogowego koloru w twoim systemie, a nie okna Qt Color. Wartość domyślna to {{TRUE/pl}}.
-   **Dialog/DontUseNativeDialog** *(boolean)*: Ustawienie okna dialogowego pliku. Ustaw wartość na {{FALSE/pl}}, jeśli chcesz używać natywnego okna dialogowego Plik podczas otwierania plików lub {{TRUE/pl}}, aby używać okna dialogowego Qt File Picker. Domyślne zależy od ustawienia podczas kompilacji: #define *(USE_QT_FILEDIALOG)*.
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
-   **General/ShowSplasherMessages** *(boolean)*: Ustaw wartość {{FALSE/pl}}, aby pominąć wyświetlanie komunikatów na ekranie powitalnym. Może to skrócić czas uruchamiania FreeCAD. Wartość domyślna to {{TRUE/pl}}.
-   **Macro/DuplicateFrom001** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby zawsze rozpoczynać poszukiwanie sugerowanej nazwy pliku z duplikatem makra od \@001 zamiast aktualnego \@NNN *(jeśli dotyczy)*. Domyślna wartość {{FALSE/pl}}.
-   **Macro/DuplicateIgnoreExtraNote** *(boolean)*: Ustaw wartość na {{TRUE/pl}}, aby zignorować dodatkową notatkę podczas sugerowania zduplikowanej nazwy pliku makra. Dodatkowa uwaga to tekst w nazwie pliku po \"@NNN\" i przed \".FCMacro\". Przykład: \"my_macro@005.my_note.FCMacro\". Jeżeli ustawiono wartość {{TRUE/pl}}, następną sugerowaną nazwą pliku będzie \"my_macro@006.FCMacro\". Jeżeli {{FALSE/pl}}, to następną sugerowaną nazwą pliku jest \"my_macro@006.my_note.FCMacro\". Aby tekst został rozpoznany jako dodatkowa notatka, powinien zaczynać się od kropki *(\".\")* po członie \"@NNN\". W przeciwnym razie, na przykład \"my_macro@006_my_note.FCMacro\" otrzyma \"my_macro@006_my_note@001.FCMacro\" jako sugerowaną nową nazwę pliku, co może być pożądane w niektórych przypadkach. Domyślną wartością jest {{FALSE/pl}}.
-   **Macro/ReplaceSpaces** *(boolean)*: Ustaw wartość na {{FALSE/pl}}, jeśli nie chcesz, aby spacje w nazwach plików były automatycznie zamieniane na podkreślenia podczas tworzenia, zmiany nazwy lub powielania makra. Nie ma to wpływu na istniejące pliki, ma znaczenie tylko przy tworzeniu nowego pliku, zmianie nazwy lub powielaniu istniejącego. Domyślną wartością jest {{TRUE/pl}}.
-   **MainWindow/ClearMenuBar** *(boolean)*: Ustaw wartość na {{TRUE/pl}} aby wyczyścić pasek menu przy zmianie środowiska pracy, przydatne gdy używasz globalnego menu, gdyż może ono nie aktualizować się przy zmianie środowiska pracy i szybko stać się zagracone wpisami w menu każdego środowiska. Domyślna wartość to {{FALSE/pl}}. Na macOS jest oczyszczane w każdym przypadku, aby obejść błąd w Qt.
-   **MainWindow/ToolBarNameAsToolTip** *(boolean)*: Ustaw wartość na {{FALSE/pl}}, aby nie wyświetlać nazwy paska narzędzi jako etykiety. Domyślnie {{TRUE/pl}}.
-   **PropertyView/AutoTransactionView** *(boolean)*: Ustawienie wartość opcji na {{TRUE/pl}} powoduje, że zmiany właściwości karty Widok są dodawane do stosu cofania *(a więc można je cofnąć)*. Domyślną wartością jest {{FALSE/pl}}.
-   **Selection/AutoShowSelectionView** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby panel Widok zaznaczenia wyświetlał się automatycznie po wybraniu obiektu. Domyślnie {{FALSE/pl}}.
-   **Selection/singleClickFeatureSelect** *(boolean)*: Ustaw opcję na wartość {{FALSE/pl}}, aby wyłączyć możliwość wyboru elementu jednym kliknięciem w środowisku Projekt Części. Domyślnie {{TRUE/pl}}.
-   **TreeView/HideColumn** *(boolean)*: Ustaw wartość parametru na {{True/pl}}, aby ukryć kolumnę **Opis** w oknie [Widoku drzewa](Tree_view/pl.md). Domyślnie {{FALSE/pl}}.
-   **TreeView/TreeViewStretchDescription** *(boolean)*: Ustaw opcję na wartość {{FALSE/pl}}, aby rozciągnąć kolumnę \"Opis\" w oknie [widoku drzewa](Tree_view/pl.md) do prawej krawędzi panelu. Wartość domyślna to {{FALSE/pl}}.
-   **View/AxisLetterColor** *(unsigned)*: Kolor liter układu współrzędnych wyświetlanych w prawym dolnym rogu widoku 3D. Domyślnie {{Value|255}}. Zobacz stronę [Kostka nawigacyjna](Navigation_Cube/pl#Dostosowywanie.md), aby uzyskać informacje na temat wartości koloru.
-   **View/AxisXColor** *(unsigned)*: Kolor dla elementów osi X gizma [Std: Przemieszczenie](Std_TransformManip/pl.md). Domyślnie {{Value|3425907456}}. Zobacz stronę [Kostka nawigacyjna](Navigation_Cube/pl#Dostosowywanie.md), aby uzyskać informacje na temat wartości koloru.
-   **View/AxisYColor** *(unsigned)*: Analogicznie dla elementów osi Y. Domyślnie {{Value|869020416}}.
-   **View/AxisZColor** *(unsigned)*: Analogicznie dla elementów osi Z. Domyślnie {{Value|859032576}}.
-   **View/LocalCoordinateSystemSize** (float): Rozmiar lokalnych układów współrzędnych. Domyślnie {{Value|2.0}}.
-   **View/NavigationDebug** *(boolean)*: Włącza debugowanie stylów nawigacji *(od wersji v0.19 tylko styl nawigacji Gesture ma coś do powiedzenia)*.
-   **View/NavigationDebug** *(boolean)*: Udostępnia możliwość debugowania stylów nawigacji *(od v0.19, tylko styl nawigacji Gesture znajduje zastosowanie)*.
-   **View/SavePicture** *(string)*: Ustaw wartość opcji na **FramebufferObject**, **PixelBuffer** lub **CoinOffscreenRenderer** dla różnych metod tworzenia obrazów w oknie widoku 3D.



## Domyślna nazwa pliku eksportu 

.

-   **General/ExportDefaultFilenameMultiple** *(string)*: Ustaw domyślną nazwę pliku, która będzie używana podczas eksportu wielu obiektów. Domyślną wartością jest {{Value|%F}}.
-   **General/ExportDefaultFilenameSingle** *(string)*: Ustaw domyślną nazwę pliku, która będzie używana podczas eksportu pojedynczego obiektu. Domyślną wartością jest {{Value|%F-%P-}}.

Obie te opcje umożliwiają automatyczne wstawianie do nazwy pliku różnych informacji, przy użyciu następujących znaków formatu:

-   %F - nazwa pliku .FCStd *(lub etykieta, jeśli nie jest jeszcze zapisana)*
-   %Lx - etykieta wybranego obiektu *(obiektów)*, oddzielona znakiem \'x\'
-   %Px - etykieta zaznaczonego obiektu*(ów)* i ich pierwszego rodzica, oddzielona znakiem \'x\'
-   %U - data i godzina, w UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - data i czas, w lokalnej strefie czasowej, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

Wszelkie inne znaki traktowane są dosłownie. Jeśli wynikowa nazwa pliku jest nieprawidłowa, zostanie zmieniona przy zapisie, a nieprawidłowe znaki zostaną zastąpione znakiem podkreślenia *\' **\_** \'*.



## Powiązane z myszką 

.

-   **General/ComboBoxWheelEventFilter** *(boolean)*: Należy ustawić wartość `True`, aby widżety nie przechwytywały zdarzeń związanych z kółkiem myszy i uniemożliwiały przewijanie obszarów, które można przewijać. Wymaga uwzględnienia ponownego uruchomienia programu FreeCAD.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** *(string)*: Komendy, które mają być wykonywane za pomocą gestów przewijania przycisków myszy w stylu nawigacji Gesture.
-   **View/GestureMoveThreshold** *(integer)*: Odległość, jaką musi pokonać kursor myszy *(px)*, aby wejść w tryb obrotu lub przesuwania w stylu nawigacji Gesture. Wartość domyślna {{Value|5}}.
-   **View/GestureTapHoldTimeout** *(integer)*: Określa jak długo trzeba czekać *(w milisekundach)*, aby wejść w tryb obrotu w stylu nawigacji Gesture. Pomocne może być zwiększenie wartości, jeśli przeciąganie geometrii w szkicowniku jest trudne. Domyślnie jest to wartość {{Value|700}}.



## Skróty klawiaturowe 



### Klawisz ESC 

-   **General/TasksKeyEsc** *(boolean)*: Utwórz i ustaw wartość na `False`, aby wyłączyć wychodzenie klawiszem **ESC** z [Panelu zadań](Task_panel/pl.md) we wszystkich środowiskach pracy *(to znaczy, jeśli panel zadań jest aktywny)*.



## Kostka nawigacyjna 

Zobacz stronę [Kostka nawigacyjna](Navigation_Cube/pl#Parametry_zaawansowane.md).



## Szczególne środowiska pracy 



### <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [środowisko pracy BIM](BIM_Workbench/pl.md) 

-   **Mod/BIM/DefaultPageScale** *(float)*: Domyślne skalowanie dla nowych stron Rysunku Technicznego utworzonych z poziomu środowiska pracy BIM, w przypadku gdy szablon nie zawiera żadnego edytowalnego pola tekstowego \"Skala\" lub \"Skalowanie\" *(wielkość liter nie ma znaczenia)*.



### <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [środowisko pracyCAM](CAM_Workbench/pl.md) 

-   Środowisko pracy[CAM](CAM_Workbench/pl.md) posiada przełącznik umożliwiający włączenie eksperymentalnych funkcji udokumentowanych na stronie [Funkcje eksperymentalne](CAM_experimental/pl.md).



### <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md) 

-   **Mod/Draft/DefaultAnnoDisplayMode** *(liczba całkowita)*: Ustaw wartość {{Value|1}}, aby tworzyć adnotacje Rysunku Roboczego *([tekst](Draft_Text/pl.md), [wymiar](Draft_Dimension/pl.md) i [etykieta](Draft_Label/pl.md))* z ich właściwością **Tryb wyświetlania** ustawionym na {{Value|Ekran}}. Ustaw na {{Value|0}} dla nowych adnotacji z tą właściwością ustawioną na {{Value|Świat}}. Domyślnie {{Value|0}}. {{Version/pl|1.0}}
-   **Mod/Draft/GridHideInOtherWorkbenches** *(boolean)*: Ustaw wartość {{FALSE/pl}}, aby utrzymać [siatkę](Draft_ToggleGrid/pl.md) podczas przełączania na inne środowiska pracy niż [BIM](BIM_Workbench/pl.md) lub [Rysunek Roboczy](Draft_Workbench/pl.md). Wartością domyślną jest {{TRUE/pl}}. {{Version/pl|1.0}}
-   **Mod/Draft/useSupport** (wartość logiczna): Ustaw wartość {{TRUE/pl}}, aby ustawić właściwość **Support** obiektów Rysunku Roboczego utworzonych na powierzchni wychodzącego obiektu bazowego na ten obiekt bazowy. Było to standardowe zachowanie przed wersją FreeCAD 0.19. Należy pamiętać, że parametr ten może nie być obsługiwany w przyszłych wersjach. Wartością domyślną jest {{FALSE/pl}}.



### <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [środowisko pracy Część](Part_Workbench/pl.md) 

-   **Mod/Part/ParametricRefine** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby funkcja [udoskonal kształt](Part_RefineShape/pl.md) utworzyła niezależną kopię, a nie linkowaną. Domyślną wartością jest {{TRUE/pl}} jeśli wartość nie jest dostępna.



### <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [środowisko pracy Projekt Części](PartDesign_Workbench/pl.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby zapewnić, że helisa addytywna, która nie przecina ciała, jest widoczna w podglądzie. Domyślną wartością jest {{FALSE/pl}}.
-   **Mod/PartDesign/DefaultDatumColor** *(unsigned)*: kolor i przezroczystość dla [geometrii konstrukcyjnych środowiska Projekt Części](PartDesign_CompDatums/pl.md), [Łącznika kształtu](PartDesign_ShapeBinder/pl.md) i [Łącznika kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md). Domyślna wartość to {{Value|4292280473}}. Zobacz [tutaj](Navigation_Cube/pl#Dostosowywanie.md) aby uzyskać informacje o wartości koloru.
-   **Mod/PartDesign/SubtractiveHelixPreview** *(boolean)*: Ustaw wartość opcji na {{TRUE/pl}} aby upewnić się, że helisa odejmowana, która nie przecina ciała, jest widoczna w podglądzie. Wartością domyślną jest {{TRUE/pl}}.
-   **Mod/PartDesign/SwitchToTask** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby uniemożliwić przełączenie na panel zadań podczas uruchamiania Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md). Wartością domyślną jest {{TRUE/pl}}, jeśli wartość nie jest dostępna.
-   **Mod/PartDesign/SwitchToWB** *(boolean)*: Ustaw wartość opcji na {{FALSE/pl}}, aby zapobiec automatycznemu wywołaniu Środowiska pracy [Projekt części](PartDesign_Workbench/pl.md), gdy aktywowana jest opcja [zawartość](PartDesign_Body/pl.md). Wartością domyślną jest {{TRUE/pl}}, jeśli wartość nie jest dostępna.



### <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [środowisko pracy Szkicownik](Sketcher_Workbench/pl.md) 

-   **Mod/Sketcher/RadiusDiameterConstraintDisplayAngleRandomness** *(float)*: Ustawia losowość kąta na powyższej wartości. Wartość to zakres losowego kąta, wyśrodkowany na kącie bazowym. Domyślnie jest to {{Value|0°}}.
-   **Mod/Sketownik/RadiusDiameterConstraintDisplayBaseAngle** *(float)*: Ustawia kąt *(od poziomu)* używany do wyświetlania wiązań promienia/średnicy w Szkicowniku w czasie tworzenia. Domyślnie {{Value|15°}} *(jeśli nie ustawiono wartości)*.
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

Środowisko pracy Start nie jest już dołączane po wersji 0.21.

-   **Mod/Start/DefaultImportXXX** *(string)*: Gdzie XXX to rozszerzenie pliku pisane małymi literami. Na przykład DefaultImportifc dla plików .IFC. Umożliwia ustawienie domyślnego modułu importu, który będzie używany po kliknięciu ikony na stronie startowej, gdy dostępnych jest kilka importerów. Na przykład ustawienie DefaultImportifc = ifc_import spowoduje użycie importera NativeIFC, jeśli jest dostępny. {{Version/pl|0.21}}
-   **Mod/Start/TimeFormat** *(string)*: Ciąg formatu czasu, taki jak {{Value|%m/%d/%Y %H:%M:%S}} używany dla daty w podpowiedzi wyświetlanej po najechaniu kursorem na element na stronie startowej.



### [Moduł pomocy](Help_Module/pl.md) 

-   **Mod/Help/UseWebModule** (boolean): Pozwala wymusić użycie modułu Web do otwierania zakładek MDI *(Multiple Document Interface)*. Może to być przydatne do obejścia problemów QWebEngine w niektórych wersjach Qt5. Domyślnie {{False/pl}}. {{Version/pl|1.0}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/pl
