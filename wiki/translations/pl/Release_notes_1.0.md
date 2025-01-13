# Release notes 1.0/pl
**FreeCAD 1.0** został wydany **18 listopada 2024 r.**, moźna go pobrać ze strony [Pobieranie programu](Download/pl.md). Ta strona jest podsumowaniem najciekawszych zmian i funkcji.

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).



## Ku pamięci: Bradley McLean (bgbsww) 

Mimo że bardzo cieszymy się z nowej wersji programu FreeCAD, z przykrością oznajmiamy, że nasz znajomy i bardzo aktywny deweloper [bgbsww](https://github.com/bgbsww) zmarł kilka tygodni przed tym wydaniem. Był jednym z głównych twórców implementacji kodu łagodzącego problem gubienia odniesień, napisał wiele dodatkowych części kodu i testów i stał się specjalistą od problemu TNP we FreeCAD. Pomógł też praktycznie wszystkim pozostałym deweloperom w adaptacji do nowego algorytmu. To wydanie jest dedykowane jemu.



## Informacje ogólne 

+++
| <img alt="" src=images/TNP_fix_relnotes_1.0.PNG  style="width:320px;"> | Długotrwały [Problem nazewnictwa topologicznego](Topological_naming_problem/pl.md) został w końcu rozwiązany dzięki wspólnemu wysiłkowi i ciężkiej pracy kilku programistów. [Algorytm Realthundera](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) został starannie zaimplementowany i ulepszony, aby działał w głównej wersji FreeCAD. Projekt trwał ponad rok, a wstępna implementacja została sfinalizowana wraz z następującym PR umożliwiającym ulepszenia. Problem nazewnictwa topologicznego nie jest całkowicie rozwiązany i w kolejnej wersji pojawią się dalsze usprawnienia w tym zakresie. [Pull request #13705](https://github.com/FreeCAD/FreeCAD/pull/13705) |
+++

+++
| <img alt="" src=images/AssemblyExample_relnotes_1.0.png  style="width:320px;"> | FreeCAD ma nowe wbudowane [środowisko pracy Złożenie](Assembly_Workbench/pl.md), oparte na oryginalnym projekcie, który zwykliśmy nazywać \"[tym drugim FreeCAD\'em](https://www.askoh.com/freecad/what_is_freecad/index.html)\", innym oprogramowaniu, również nazwanym FreeCAD, z możliwościami symulacji ruchu, utworzonym w tym samym czasie co nasz projekt. Przeniesienia dokonał sam autor tego drugiego FreeCAD\'a, [Dr. Aik-Siong Koh](https://www.askoh.com) i z tym kluczowym momentem oba programy FreeCAD są w końcu zjednoczone. Poniżej znajdziesz [więcej informacji](#Środowisko_pracy_Złożenie.md). [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427) |
+++

+++
| <img alt="" src=images/Freecad.svg  style="width:320px;"> | FreeCAD ma nowe logo. Zostało ono wybrane spośród 5 zwycięzców publicznego konkursu. Wytyczne dotyczące użycia i zestaw logo można znaleźć na stronie [wytyczne dot. marki FreeCAD](https://fpa.freecad.org/handbook/process/logo.html). [Pull request #14284](https://github.com/FreeCAD/FreeCAD/pull/14284) |
+++



## Interfejs użytkownika 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_1.0.gif  style="width:320px;"> | Dodano wskaźnik środka obrotu. Wskaźnik ten jest wyświetlany po obróceniu widoku przez przeciągnięcie myszą. Opcjonalnie można go wyłączyć w preferencjach. Dostępne są również ustawienia koloru, przezroczystości i rozmiaru. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) oraz [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_1.0.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano [filtry wyboru](Part_SelectFilter/pl.md), ułatwiające wybór wierzchołków, krawędzi i ścian. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_1.0.png  style="width:320px;"> | Dla większej elastyczności panel zadań jest teraz samodzielnym widżetem. Może być [dokowany](Combo_view/pl#Zadokuj_Panel_zadań_w_górnej_części_Widoku_połączonego.md) w górnej części widoku połączonego aby uzyskać kompaktowy układ z poprzednich wersji. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) oraz [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_1.0.png  style="width:320px;"> | Poprawiono wygląd przeciągacza narzędzia [Przemieszczenie](Std_TransformManip/pl.md). Narzędzie posiada teraz także zestaw planarnych uchwytów do przesuwania obiektów wzdłuż 3 domyślnych płaszczyzn. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_1.0.png  style="width:320px;"> | Dodano funkcję dewelopera Realthunder umożliwiającą nakładanie widżetów docka *(przezroczystość widoku drzewa i zadań)*. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_1.0.png  style="width:320px;"> | Położenie źródła światła można teraz ustawić w preferencjach *(Preferencje \... → Wyświetlanie)*. [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) i [Pull request #15877](https://github.com/FreeCAD/FreeCAD/pull/15877) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_1.0.png  style="width:320px;"> | Okno preferencji zostało przeprojektowane, aby zastąpić zakładki widokiem drzewa. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++

+++
| <img alt="" src=images/TabBar_relnotes_1.0.png  style="width:320px;"> | Dodano nowy sposób przełączania środowisk pracy - przyciski zamiast listy rozwijanej. Można to włączyć i skonfigurować w menu *Preferencje → Środowiska pracy*. [Pull request #12270](https://github.com/FreeCAD/FreeCAD/pull/12270) |
+++

+++
| <img alt="" src=images/Unified_measurement_relnotes_1.0.PNG  style="width:320px;"> | Dodano nowe [uniwersalne narzędzie pomiarowe](Std_Measure/pl.md), zastępujące stare narzędzia z grupy [Pomiary](Part_Workbench/pl#Pomiary.md). [Pull request #9750](https://github.com/FreeCAD/FreeCAD/pull/9750) i następne |
+++

   
  <img alt="" src=images/Normal_view_relnotes_1.0.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Narzędzie [Wyrównaj do zaznaczenia](Std_AlignToSelection/pl.md) zostało dodane, umożliwiając przechodzenie do widoków prostopadłych do ścian i zgodnych z kierunkiem krawędzi. [Pull request #13906](https://github.com/FreeCAD/FreeCAD/pull/13906)
   



### Pozostałe ulepszenia interfejsu użytkownika 

-   Wprowadzono układ jednostek projektu. [Pull request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   Narzędzie \[\[Part_SectionCut/pl\|Wycinek z przekroju

\]\] działa teraz również w widoku perspektywicznym. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143).

-   Dodano opcję sortowania środowisk pracy alfabetycznie *(dostępną po kliknięciu prawym przyciskiem myszy w Preferencje → Środowiska pracy)*.

[Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)

-   Filtr *Znajdź plik* i filtr *Znajdź w plikach* zostały dodane do okna dialogowego [Makrodefinicje](Std_DlgMacroExecute/pl.md). [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   [Menu Widok](Std_View_Menu/pl.md) i pasek narzędzi Widok zostały poprawione. [Pull request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   Przycisk stop został usunięty z [paska narzędzi Makro](Macros/pl.md). Przycisk [przycisk nagrywania](Std_DlgMacroRecord/pl.md) został teraz przełączony w przycisk zatrzymania, gdy trwa nagrywanie. [Pull request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   Przycisk resetowania w Preferencjach wyświetla teraz menu z opcjami resetowania ustawień na różnych poziomach: wszystkich, w bieżącej grupie lub w bieżącej zakładce. [Pull request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) i [Pull request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   Moduł pomocy został połączony, dzięki czemu nie jest już konieczne pobieranie dodatku, aby z niego korzystać. [Pull request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Dodano preferencje umożliwiające dostosowanie bieżącego motywu. [Pull request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Zmieniono domyślne ustawienia zaznaczania, aby ułatwić zaznaczanie obiektów w oknie widoku 3D. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   Dodano schemat jednostek tylko dla metrów o nazwie **Krotność dziesiętna metra**, ponieważ system MKS *(m/kg/s/stopień)* nie zawsze powoduje wyświetlanie wymiarów w metrach - milimetry są nadal używane dla wartości poniżej 0,1 m, podczas gdy w niektórych zastosowaniach *(np. inżynieria lądowa)* przydatny jest system jednostek, który faktycznie zmienia wyświetlanie wszystkich wymiarów na metry. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Dodano dodatkowe rozmiary znaczników *(20, 25 i 30px)* do *Preferencje \... → Wyświetlanie → Widok 3D → Rozmiar znacznika*, aby pomóc użytkownikom ekranów 4K. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   Dodano opcję \"Przełącz przezroczystość\" do menu widoku i menu kontekstowego, aby szybko włączyć lub wyłączyć przezroczystość dla wybranych obiektów. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)
-   Dodano polecenie Zablokuj paski narzędzi. Za jego pomocą można zablokować lub odblokować pozycje pasków narzędzi. Jest ono dostępne w menu Widok i menu podręcznym obszaru paska narzędzi. [Pull request #11596](https://github.com/FreeCAD/FreeCAD/pull/11596)
-   Dostosowano domyślny kolor kształtu, aby poprawić wygląd modeli. [Pull request #12380](https://github.com/FreeCAD/FreeCAD/pull/12380) i [Pull request #12488](https://github.com/FreeCAD/FreeCAD/pull/12488)
-   Obiekty w kontenerach Część i Grupa można teraz sortować przeciągając je i upuszczając. [Pull request #12293](https://github.com/FreeCAD/FreeCAD/pull/12293)
-   Ikony widoczności (symbol oka) są dodawane do obiektów w drzewie jeśli opcja Pokaż ikonkę widoczności jest zaznaczona w *Preferencje → Wyświetlanie → Interfejs użytkownika*. [Pull request #12298](https://github.com/FreeCAD/FreeCAD/pull/12298)
-   Dodano status [zamrożony](Std_ToggleFreeze/pl.md) *(opcja*Włącz / wyłącz przeliczanie*w menu kontekstowym w drzewie)*, umożliwiając wyłączanie parametrycznego zachowania obiektu *(co sprawia, że nie zmienia się on nawet jeśli zmienią się obiekty, od których jest zależny)*. [Pull request #12580](https://github.com/FreeCAD/FreeCAD/pull/12580)
-   Dodano właściwość *Suppressed* do tymczasowego wyłączania cechy. Obecnie jest ukryta w środowisku Projekt Części (kliknij prawym przyciskiem myszy w [edytorze właściwości](Property_editor/pl.md) i wybierz *Wyświetl wszystko* aby ją zobaczyć) dopóki naprawa [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md) nie zostanie ukończona. [Pull request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) i [Pull request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   Animacje nawigacji zostały usprawnione. Korzystają teraz z ułatwiającej funkcji i mają stały czas trwania, który można zmienić w menu *Preferencje → Wyświetlanie → Nawigacja*. [Pull request #10881](https://github.com/FreeCAD/FreeCAD/pull/10881) i [Pull request #12205](https://github.com/FreeCAD/FreeCAD/pull/12205)
-   Przyciski do domyślnych widoków są teraz zgrupowane pod pojedynczym przyciskiem. Pojedyncze przyciski są nadal dostępne jako dodatkowy pasek narzędzi *Indywidualne widoki*. [Pull request #12878](https://github.com/FreeCAD/FreeCAD/pull/12878)
-   Nazwa bieżącego aktywnego dokumenty jest teraz też wyświetlana na pasku tytułowym okna programu. [Pull request #12035](https://github.com/FreeCAD/FreeCAD/pull/12035)
-   Dodano polecenie wyświetlające panel [Widok właściwości](Property_editor/pl.md). [Pull request #12024](https://github.com/FreeCAD/FreeCAD/pull/12024)
-   Poprawiono integrację urządzeń 3Dconnexion z FreeCAD w systemie Windows. [Pull request #12929](https://github.com/FreeCAD/FreeCAD/pull/12929)
-   Dodano funkcję szybkiego pomiaru. Wykorzystuje ona [Pasek statusu](Status_bar/pl.md) do wyświetlania kluczowych informacji pomiarowych *(długość krawędzi, powierzchnia, odległość / kąt między punktami / krawędziami i promień okrągłych krawędzi / cylindrycznych powierzchni)* o bieżącym zaznaczeniu w widoku 3D. [Pull request #12217](https://github.com/FreeCAD/FreeCAD/pull/12217).
-   Paski narzędzi można teraz przeciągać i upuszczać na paski stanu i menu. [Pull request #13571](https://github.com/FreeCAD/FreeCAD/pull/13571).
-   Dodano przycisk *Przeładuj arkusz stylów*, aby ułatwić tworzenie arkuszy stylów. Nie należy on domyślnie do żadnego paska narzędzi, musi zostać dodany ręcznie z poziomu *Przybory → Dostosuj → Paski narzędzi → Widok*. [Pull request #13982](https://github.com/FreeCAD/FreeCAD/pull/13982).
-   Poprawiono i ujednolicono ikony dokumentów *(w tym między innymi [Otwórz](Std_Open/pl.md) i [Zapisz](Std_Save/pl.md))*. [Pull request #13865](https://github.com/FreeCAD/FreeCAD/pull/13865)
-   Ikona [Dopasuj wszystko](Std_ViewFitAll/pl.md) została zastąpiona dla przejrzystości. [Pull request #14180](https://github.com/FreeCAD/FreeCAD/pull/14180)
-   Poprawiono wiele głównych ikon *(takich jak [Nowy](Std_New/pl.md))*. [Pull request #14278](https://github.com/FreeCAD/FreeCAD/pull/14278) i [Pull request #14434](https://github.com/FreeCAD/FreeCAD/pull/14434) oraz [Pull request #14154](https://github.com/FreeCAD/FreeCAD/pull/14154)
-   Poprawiono ikony nagłówków panelu zadań środowisk pracy Szkicownik i Projekt Części. [Pull request #13968](https://github.com/FreeCAD/FreeCAD/pull/13968)
-   W trybie [bez GUI](Headless_FreeCAD/pl.md), interaktywna konsola Pythona ma teraz autouzupełnianie jeśli dostępny jest moduł [readline](https://docs.python.org/3/library/readline.html). [Pull request #14213](https://github.com/FreeCAD/FreeCAD/pull/14213)
-   Dodano opcję wyświetlania wewnętrznych nazw w widoku drzewa. Domyślnie jest wyłączona i można ją aktywować w *Preferencje → Wyświetlanie → Interfejs użytkownika → Hide Internal Names*. [Pull request #14237](https://github.com/FreeCAD/FreeCAD/pull/14237)
-   Przycisk Pomoc został usunięty z Preferencji, ponieważ był niefunkcjonalny. [Pull request #14695](https://github.com/FreeCAD/FreeCAD/pull/14695)
-   Domyślne arkusze stylów zostały znacznie ulepszone i są teraz oferowane w dwóch wariantach innych niż klasyczny - jasnym i ciemnym. [Pull request #13772](https://github.com/FreeCAD/FreeCAD/pull/13772)
-   Strony Motyw i Interfejs użytkownika w grupie Wyświetlanie w Preferencjach zostały zreorganizowane i połączone. Niektóre preferencje zostały przeniesione na nową stronę Zaawansowane. [Pull request #14974](https://github.com/FreeCAD/FreeCAD/pull/14974)
-   Preferencje Część / Projekt Części sprawdź i udoskonal są teraz domyślnie aktywowane. [Pull request #14406](https://github.com/FreeCAD/FreeCAD/pull/14406)
-   Dodano nowy parametr - **BaseApp/Preferences/Bitmaps/Theme/UseIconTheme** (bool): Ustaw go na prawda aby wymusić w Qt użycie ikon z motywu systemowego. Domyślna wartość to fałsz, co oznacza, że FreeCAD będzie używał własnych ikon. Nie ma to wpływu na inne mechanizmy motywów Qt, takie jak okna systemowe, przyciski itp. Powinny one zawsze używać ikon z motywu systemowego. [Pull request #16018](https://github.com/FreeCAD/FreeCAD/pull/16018).
-   Dodano nowy parametr - **BaseApp/Preferences/Bitmaps/Theme/UseIconTheme** *(boolean)*: Ustaw na wartość {{true/pl}}, aby zmusić Qt do używania ikon z systemowego motywu ikon. Domyślnie ma wartość {{false/pl}}, więc FreeCAD będzie używał własnych ikon. Nie ma to wpływu na inne mechanizmy motywów ikon Qt, takie jak systemowe okna dialogowe, przyciski i inne. Powinny one zawsze używać ikon z motywu systemowego. [Pull request #16018](https://github.com/FreeCAD/FreeCAD/pull/16018).
-   Informacje o arkuszu stylów, motywie i QtStyle są teraz zawarte w *Pomoc → O FreeCAD*. [Pull request #16281](https://github.com/FreeCAD/FreeCAD/pull/16281).
-   Ekran powitalny jest teraz wybierany losowo podczas uruchamiania z wielu obrazów, w tym modeli użytkownika i prezentacji niektórych dodatkowych środowisk pracy. [Pull request #16071](https://github.com/FreeCAD/FreeCAD/pull/16071).
-   Dodano tryb bezpieczny, który można aktywować za pomocą opcji *Pomoc → Restart in safe mode*. Tymczasowo dezaktywuje on konfiguracje użytkownika, motywy i inne niestandardowe ustawienia aby uruchomić FreeCAD w stanie po \"przywróceniu do ustawień fabrycznych\" w celu rozwiązywania problemów. [Pull request #16858](https://github.com/FreeCAD/FreeCAD/pull/16858)



## Zmiany formatu plików 

Pomimo prób zapewnienia kompatybilności plików utworzonych w nowej wersji 1.0 ze starszymi wersjami, niektóre zmiany wprowadzone w 1.0 nie mogą być rozpoznane przez wcześniejsze wersje i mogą psuć modele zapisane w 1.0 lub powodować problemy po ich otwarciu we wcześniejszych wersja programu FreeCAD. Oto podsumowanie błędów jakie można napotkać i ich rozwiązania. Społeczność na forum również może pomóc w problemach z kompatybilnością.

-   właściwość **Attachment** została zmieniona na **AttachmentSupport**. To oznacza, że cechy o nią oparte (szczególnie modele korzystające z dodatku Assembly4) będą wymagały naprawy aby je otworzyć we wcześniejszych wersjach programu FreeCAD. [To makro](Macro_Convert_021.md) pozwala je naprawić.



## Rdzeń i API 



### Rdzeń programu 

-   Funkcje wektorowe pochodzące ze [skryptów](Vector_API/pl.md) mogą być teraz używane w [wyrażeniach](Expressions/pl.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237)
-   Edytor Python dopasowuje teraz wcięcie poprzedniej linii po naciśnięciu klawisza Enter. [Pull request #11356](https://github.com/FreeCAD/FreeCAD/pull/11356)
-   Nazwa właściwości przechowującej obiekt(y) referencyjny(e) dołączenia została zmieniona z **Support** na **AttachmentSupport**. [Pull request #12714](https://github.com/FreeCAD/FreeCAD/pull/12714)
-   Kontener właściwości, App::VarSet, został wprowadzony jako podstawowa funkcja. VarSet pozwala użytkownikom definiować właściwości, które mogą być używane w modelach, podobnie jak aliasy arkuszy kalkulacyjnych i inne poprzednie kontenery właściwości *(Dynamic Data, Path PropertyBags i Assembly 4 Variables)*. [Pull Request #12135](https://github.com/FreeCAD/FreeCAD/pull/12135)



### API



#### Nowe skrypty Python 

-    {{Incode|getUpDirection}}: Pobiera kierunek w górę z widoku View3DInventor. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### Zmienione API Pythona 

-   Aby zapisać/przywrócić dane użytkownika z funkcji Pythona, metody wywoływane dotychczas jako {{Incode|__getstate__}}/{{Incode|__setstate__}} zostały zmienione na {{Incode|dumps}}/{{Incode|loads}}. Wynika to z wewnętrznych zmian w Python-3.11. [Pull request #10769](https://github.com/FreeCAD/FreeCAD/pull/10769) i [Pull request #12243](https://github.com/FreeCAD/FreeCAD/pull/12243).



## Środowisko pracy Start 

Środowisko pracy Start zostało zastąpione przez stronę Start, aplikację opartą o QtWidgets. Można ją wyświetlić korzystając z opcji *Pomoc → Start*. [Pull request #13134](https://github.com/FreeCAD/FreeCAD/pull/13134)

Pierwsze dwa pull requesty wspomniane poniżej należą do środowiska pracy Start, ale wpłynęły na projekt strony Start.

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_1.0.png  style="width:384px;"> | Na stronie startowej dodano sekcję **Nowy plik**, która zawiera szereg przycisków szybkiego uruchamiania. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_1.0.png  style="width:384px;"> | Projekt wizualny strony startowej został zmieniony. Wygląda teraz bardziej nowocześnie i spójnie. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++

+++
| <img alt="" src=images/First_start_relnotes_1.0.png  style="width:384px;"> | Dodano prosty widżet pierwszego uruchomienia, który zostanie rozszerzony w najbliższej przyszłości. [Pull request #13650](https://github.com/FreeCAD/FreeCAD/pull/13650) |
+++



## Środowisko pracy Złożenie 

+++
| <img alt="" src=images/Assembly_relnotes_1.0.png  style="width:384px;"> | Wbudowane [środowisko do pracy na złożeniach](Assembly_Workbench/pl.md) zostało w końcu dodane do FreeCAD. Korzysta z otwartego [solvera Ondsel](https://github.com/Ondsel-Development/OndselSolver). Podstawowe funkcje (złącza) są już dostępne. Dalszy rozwój trwa. [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427), [Pull request #10764](https://github.com/FreeCAD/FreeCAD/pull/10764), [Pull request #12406](https://github.com/FreeCAD/FreeCAD/pull/12406) i więcej |
+++



### Pozostałe ulepszenia środowiska Złożenie 

-   Dodano [Widok rozłożenia](Assembly_CreateView/pl.md). [Pull request #12419](https://github.com/FreeCAD/FreeCAD/issues/12419)
-   Ikony w środowisku Złożenie zostały zaktualizowane i uwidoczniono eksperymentalne narzędzia. [Pull request #13866](https://github.com/FreeCAD/FreeCAD/pull/13866)
-   Dodano połączenia kątowe, prostopadłe i równoległe. [Pull request #14008](https://github.com/FreeCAD/FreeCAD/pull/14008)
-   Dodano funkcję [zestawienia materiałów](Assembly_CreateBom/pl.md). [Pull request #14198](https://github.com/FreeCAD/FreeCAD/pull/14198)
-   Dodano obsługę kodu łagodzącego [TNP](Topological_naming_problem/pl.md). [Pull request #14674](https://github.com/FreeCAD/FreeCAD/pull/14674)
-   Dodano wsparcie dla elastycznych podzłożeń. Podzłożenia dodane do nadrzędnego złożenia mogą być zdefiniowane jako sztywne (jednostka bryłowa) lub elastyczne (pozwalają na ruch ich poszczególnych komponentów). Ręczne kroki są wymagane dla tych podzłożeń dodanych w czasie cyklu rozwoju przed dodaniem tej funkcji. Te złożenia będą musiały zostać usunięte i ponownie dodane do złożenia nadrzędnego. [Pull request #15629](https://github.com/FreeCAD/FreeCAD/pull/15629)



## Środowisko pracy BIM 

+++
| <img alt="" src=images/bim_relnotes_1.0.png  style="width:384px;"> | Środowisko pracy Architektura zostało w końcu połączone ze środowiskiem pracy [BIM](BIM_Workbench/pl.md), tworząc nowy moduł BIM. Posiada on wszystkie narzędzia ze środowiska Architektura i dodaje kilka nowych oraz wprowadza wiele usprawnień do całego przepływu pracy BIM i architektonicznego plus lepsze narzędzia do ustawień i zarządzania oraz lepsze wsparcie dla IFC. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783) |
+++



### Pozostałe ulepszenia środowiska BIM 

-   Wychodząc ze środowiska pracy BIM, niektóre narzędzia modułu Architektura typu \"wszystko w jednym\" zostały podzielone na różne przypadki użycia: Narzędzie [Architektura: Część budynku - piętro](Arch_BuildingPart/pl.md) zostało rozdzielone na narzędzia [BIM Budynek](Arch_Building/pl.md) i [BIM Kondygnacja](Arch_Floor/pl.md), narzędzie [Architektura: Konstrukcja](Arch_Structure/pl.md) zostało podzielone na narzędzia [BIM Słup](BIM_Column/pl.md), [BIM Belka](BIM_Beam/pl.md) i [BIM Płyta](BIM_Slab/pl.md) zaś narzędzie [Architektura: Okno](Arch_Window/pl.md) zostało podzielone na narzędzia [BIM Okno](Arch_Window/pl.md) i [BIM Drzwi](BIM_Door/pl.md). Wewnętrznie te narzędzia nadal tworzą ten sam obiekt tylko z zastosowaniem różnych typów IFC i presetów. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   [NativeIFC](https://github.com/yorikvanhavre/FreeCAD-NativeIFC) również zostało włączone do nowego środowiska pracy BIM. Z NaiveIFC, można teraz pracować natywnie na plikach IFC we FreeCAD, bez potrzeby konwersji do i z formatu plików programu FreeCAD. Zobacz więcej na stronie [Natywne IFC](NativeIFC/pl.md). [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   Polecenie [Płaszczyzna cięcia](Arch_CutPlane/pl.md) zostało ulepszone. Uwzględnia ono teraz zagnieżdżanie i łącza, a wybór jest bardziej elastyczny. Można również wybierać krawędzie, dzięki czemu polecenie Architektura: Linia cięcia staje się przestarzałe. [Pull request #11254](https://github.com/FreeCAD/FreeCAD/pull/11254) i [Pull request #11792](https://github.com/FreeCAD/FreeCAD/pull/11792)
-   Preferencje środowiska BIM zostały sprawdzone i poprawione. Strony w [edytorze preferencji](Preferences_Editor/pl.md) mają nowy układ. [Pull request #11940](https://github.com/FreeCAD/FreeCAD/pull/11940) i [Pull request #12038](https://github.com/FreeCAD/FreeCAD/pull/12038).
-   Do polecenia [okno](Arch_Window/pl.md) dodano ustawienie wstępne *Tylko otwieranie*. [Pull request #12209](https://github.com/FreeCAD/FreeCAD/pull/12209)
-   Obiekt [dach](Arch_Roof/pl.md) ma teraz właściwość *\'Objętość podrzędna*. Pozwala to na użycie niestandardowego obiektu bryłowego jako objętości odejmowanej dla dachu. [Pull request #12346](https://github.com/FreeCAD/FreeCAD/pull/12346).
-   Ponadto dla obiektu [dach](Arch_Roof/pl.md), który używa obiektu bryłowego jako swojej **podstawy**, automatycznie generowana jest teraz odpowiednia objętość odejmowania. Podobnie jak dach oparty na poliliniach, taki obiekt dachu można odjąć od ścian budynku za pomocą narzędzia [Usuń komponent](Arch_Remove/pl.md). [Pull request #13221](https://github.com/FreeCAD/FreeCAD/pull/13221)
-   Narzędzie [Odniesienie](Arch_Reference/pl.md) zostało zaktualizowane: obiekty referencyjne mogą teraz używać całej zawartości pliku zamiast konieczności wybierania części, dodano obsługę plików DXF i IFC. [Pull request #13287](https://github.com/FreeCAD/FreeCAD/pull/13287)
-   FreeCAD ma teraz nowy plik z przykładem BIM. [Pull request #14937](https://github.com/FreeCAD/FreeCAD/pull/14937)
-   Nowe środowisko pracy BIM oferuje też szereg nowych narzędzi do zarządzania wspierających ustawianie projektu lub grupowe zarządzanie właściwościami IFC obiektów. Zobacz więcej na stronie [Środowisko pracy BIM](BIM_Workbench/pl.md).
-   [IfcOpenShell](IfcOpenShell/pl.md), kolejne oprogramowanie open-source potrzebne do pracy z plikami IFC we FreeCAD, jest teraz dostarczane we wszystkich oficjalnych pakietach instalacyjnych oferowanych przez zespół FreeCAD. Jeśli masz FreeCAD od innego dostawcy, takiego jak Twoja dystrybucja Linuxa, gdzie IfcOpenShell nie jest jeszcze uwzględniony jako oficjalny pakiet, środowisko pracy BIM oferuje narzędzie do pobrania i zainstalowania IfcOpenShell. A jeśli nie korzystasz z IFC, środowisko pracy BIM nadal działa w pełni bez IfcOpenShell.
-   Paski narzędzi i menu środowiska BIM zostały przerobione. [Pull request #14087](https://github.com/FreeCAD/FreeCAD/pull/14087)



## Środowisko pracy CAM 

-   Oryginalną nazwę środowiska zmieniono z Path na CAM. [Pull request #12665](https://github.com/FreeCAD/FreeCAD/pull/12665)



### Pozostałe ulepszenia środowiska CAM 

-   Obróbka spoczynkowa została ponownie zaimplementowana, aby pobierać dane wejściowe z G-code wcześniejszych operacji *(zamiast używać wewnętrznych elementów operacji [Obszar](CAM_Area/pl.md))*. Umożliwia to obsługę obróbki spoczynkowej w operacjach Obszaru po operacjach nieobszarowych *(w szczególności Adaptacyjnych)*. [Pull request #11939](https://github.com/FreeCAD/FreeCAD/pull/11939)
-   Kompensacja wysokości narzędzia G43 została dodana do postprocesora CAM centroid. [Pull request #12652](https://github.com/FreeCAD/FreeCAD/pull/12652)
-   Do ustawień operacji wiercenia dla rozwiercania i wytaczania dodano opcję \"Cofania posuwu\". [Pull request #13254](https://github.com/FreeCAD/FreeCAD/pull/13254)
-   Dodano nowy symulator CAM oparty na niskopoziomowych funkcjach OpenGL *(szybszy i bardziej precyzyjny)*. [Pull request #13884](https://github.com/FreeCAD/FreeCAD/pull/13884) oraz [Pull request #15597](https://github.com/FreeCAD/FreeCAD/pull/15597)
-   Operacja [Wycięcie V](CAM_Vcarve/pl.md) została przebudowana aby uwzględniać funkcje powszechnie dostępne w innych środowiskach CAM (tzw. Step down, Finishing pass, Head movement optimization i metoda debugVoronoi), umożliwiając znaczne ulepszenie jakości powierzchni nacięcia przy jednoczesnym zwiększeniu prędkości operacji aż do 50%. [Pull request #14093](https://github.com/FreeCAD/FreeCAD/pull/14093)
-   Dodano modele materiałów obrabialnych wraz z kilkoma materiałami. [Pull request #14460](https://github.com/FreeCAD/FreeCAD/pull/14460), [Pull request #15910](https://github.com/FreeCAD/FreeCAD/pull/15910) i [Pull request #16021](https://github.com/FreeCAD/FreeCAD/pull/16021)



## Środowisko pracy Rysunek Roboczy 

-   Dodano opcję wyrównania i kilka powiązanych właściwości do funkcji [Kształt z tekstu](Draft_ShapeString/pl.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Wymiar promieniowy](Draft_Dimension/pl#Zastosowanie_wymiaru_promieniowego.md) pokazuje teraz tylko pojedynczą strzałkę. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Właściwość Kąt nachylenia została dodana do [Kształt z tekstu](Draft_ShapeString/pl.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Dodano obsługę hiperłączy. Hiperłącza do lokalnych i zdalnych plików oraz adresów URL w [tekście](Draft_Text/pl.md) i [etykiecie](Draft_Label/pl.md) można otworzyć z ich menu kontekstowego [Widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md). [Pull request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   Kod [płaszczyzny roboczej](Draft_SelectPlane/pl.md) został przerobiony. W każdym widoku 3D istnieje teraz płaszczyzna robocza. [Pull request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   Udoskonalono funkcję historii i opcje wyrównywania polecenia [wybór płaszczyzny](Draft_SelectPlane/pl.md). [Pull request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   Poprawiono zachowanie [siatki](Draft_ToggleGrid/pl.md). Jej widoczność jest teraz zapisywana dla każdego widoku 3D. Podczas przełączania do innego środowiska pracy wszystkie siatki są ukryte *(dostępny jest parametr [fine-tuning](Fine-tuning/pl.md), aby to wyłączyć)*. [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Preferencje Draft zostały sprawdzone i poprawione. Niektóre preferencje zostały dodane, przestarzałe preferencje zostały usunięte. Strony w [Edytorze Preferencji](Preferences_Editor.md) mają nowy układ i pokazują jednostki tam, gdzie ma to zastosowanie. Ponowne uruchomienie FreeCAD po zmianie preferencji Draft nie jest już wymagane. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) oraz [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Dodano nowe ustawienie *Mouse delay* do preferencji Ogólne. Jeśli ma wartość inną niż zero *(domyślnie 1)*, po wprowadzeniu liczby w jednym z pól wejściowych panelu zadań, ruch myszy zostanie wyłączony uniemożliwiając przypadkową zmianę wartości w polu wejściowym przez określony czas *(1s)*. Ustawienie bardzo dużego opóźnienia praktycznie wyłącza ruch myszy dopóki polecenie nie zostanie zakończone. [Pull request #12624](https://github.com/FreeCAD/FreeCAD/pull/12624)
-   Przycisk do szybkiej zmiany koloru siatki został dodany do panelu zadań polecenia [Wybór płaszczyzny](Draft_SelectPlane/pl.md). [Pull request #13051](https://github.com/FreeCAD/FreeCAD/pull/13051).
-   Dodano właściwość *Fuse* do narzędzi [Szyk z punktów](Draft_PointArray/pl.md), [Szyk po ścieżce](Draft_PathArray/pl.md) i Draft_PathTwistedArrays. [Pull request #13172](https://github.com/FreeCAD/FreeCAD/pull/13172) i [Pull request #13191](https://github.com/FreeCAD/FreeCAD/pull/13191)
-   Przycisk polecenia [Przełącz siatkę](Draft_ToggleGrid/pl.md) zachowuje się teraz jak przycisk przełączania, zapewniając wizualną informację zwrotną o stanie siatki *(widoczna lub ukryta)*. [Pull request #14452](https://github.com/FreeCAD/FreeCAD/pull/14452)



### Pozostałe ulepszenia środowiska Rysunek Roboczy 

-   [Łącznik kształtu](Draft_Facebinder/pl.md) może teraz obsługiwać ściany należące do łączy i ściany zagnieżdżone w obiekcie [Część](Std_Part/pl.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Kilka ustawień zostało dodanych do polecenia [Ustaw styl](Draft_SetStyle/pl.md). [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593) i [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) oraz [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Ustawienia zostały również dodane do polecenia [Zastosuj bieżący styl](Draft_ApplyStyle.md). [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610) i [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Przyciąganie, edycja i znaczniki śledzenia używają teraz preferencji [Promień kliknięcia](https://wiki.freecad.org/Preferences_Editor/pl#Widok_3D.md). [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688) i [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Niektóre ikony tego środowiska zostały zmienione aby poprawić ich wygląd. [Pull request #13585](https://github.com/FreeCAD/FreeCAD/pull/13585)
-   Obiekt [Warstw](Draft_Layer/pl.md) został zaktualizowany dla nowego systemu obsługi materiałów. Ma on teraz właściwość *Wygląd kształtu* i właściwość *Nadpisywanie wyglądu kształtu elementu podrzędnego*. [Pull request #13949](https://github.com/FreeCAD/FreeCAD/pull/13949)
-   [Draft Fillets](Draft_Fillet/pl.md) można teraz stosować również do łuków. [Pull request #14774](https://github.com/FreeCAD/FreeCAD/pull/14774)



## Środowisko pracy MES 

+++
| <img alt="" src=images/FEM_better_legend_labels_relnotes_1.0.JPG  style="width:384px;"> | Dostosowano położenie etykiet legendy kolorów, aby zmniejszyć prawdopodobieństwo zakrycia górnych etykiet przez kostkę nawigacyjną. Zmieniono domyślną czcionkę i kolor etykiet, aby zwiększyć ich widoczność, a także dodano preferencje umożliwiające modyfikację koloru i rozmiaru etykiet. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_1.0.png  style="width:384px;"> | Polecenie [Wykres linearyzacji naprężeń](FEM_PostFilterLinearizedStresses/pl.md) może teraz używać składowych tensora naprężeń do obliczeń naprężeń zlinearyzowanych. Wcześniej można było używać tylko naprężeń Von Misesa, Tresca i głównych \'\'(głównych / pośrednich / małych). [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++

+++
| <img alt="" src=images/Cyclic_symmetry_relnotes_1.0.jpg  style="width:384px;"> | Dodane wsparcie dla symetrii cyklicznej definiowanej za pośrednictwem [wiązania tie](FEM_ConstraintTie/pl.md) w CalculiX, umożliwiając symulacje modeli z obrotową symetrią periodyczną przy pomocy pojedynczego reprezentatywnego sektora. [Pull request #12289](https://github.com/FreeCAD/FreeCAD/pull/12289) |
+++

+++
| <img alt="" src=images/2D_analyses_relnotes_1.0.png  style="width:384px;"> | Dodano obsługę analizy 2D *(naprężenia płaskie, odkształcenia płaskie i osiowosymetryczne)* dla solwera [CalculiX](FEM_SolverCalculixCxxtools/pl.md). Konfigurują się one w taki sam sposób jak symulacje z elementami powłokowymi, ale istnieją pewne dodatkowe ograniczenia opisane na wspomnianej wyżej stronie wiki. Nowa opcja *Przestrzeń modelu* musi być odpowiednio ustawiona. [Pull request #12562](https://github.com/FreeCAD/FreeCAD/pull/12562) |
+++

+++
| <img alt="" src=images/Hex_subdivision_relnotes_1.0.png  style="width:384px;"> | Jako pierwszy krok w kierunku obsługi elementów heksagonalnych, ich generacja za pomocą techniki podziału Gmsh jest teraz możliwa dzięki nowej właściwości Gmsh o nazwie *Subdivision Algorithm*. Może ona również być używana do tworzenia elementów czworokątnych. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) |
+++

+++
| <img alt="" src=images/Pipeline_colors_relnotes_1.0.png  style="width:384px;"> | Nowe właściwości w zakładce Widok zostały dodane do obiektu prezentacji graficznej wyników. Kolor i grubość krawędzi siatki można teraz zmienić dla trybu wyświetlania *Surface with Edges*. Z kolei dla trybu *Nodes* możliwa jest zmiana rozmiaru węzłów. Dodano też ustawienie przezroczystości dla wszystkich trybów. [Pull request #13066](https://github.com/FreeCAD/FreeCAD/pull/13066) |
+++

+++
| <img alt="" src=images/Constraint_suppress_relnotes_1.0.png  style="width:384px;"> | Cechy analizy można teraz wygasić (kliknij prawym przyciskiem myszy na obiekcie i wybierz *Wstrzymaj*), a co za tym idzie - sprawić by były ignorowane przez solvery. Dzięki temu możliwe jest modyfikowanie ustawień analizy bez potrzeby usuwania aktualnie niepotrzebnych cech. [Pull request #12359](https://github.com/FreeCAD/FreeCAD/pull/12359) |
+++

+++
| <img alt="" src=images/Rigid_body_relnotes_1.0.JPG  style="width:384px;"> | Dodano wsparcie dla [wiązania ciała sztywnego](FEM_ConstraintRigidBody/pl.md) solvera CalculiX, w końcu umożliwiając m.in. symulowanie skręcania dowolnych komponentów i przykładanie sił zdalnych. [Pull request #13900](https://github.com/FreeCAD/FreeCAD/pull/13900) |
+++



### Pozostałe ulepszenia środowiska MES 

-   Pozycje z menu **Model → Wiązania bez solvera** zostały usunięte z GUI, ponieważ nie dało się z nich skorzystać.
-   Słowo \"wiązanie\" zostało usunięte z nazw i opisów większości funkcji w środowisku roboczym FEM, aby zapewnić prawidłowe nazewnictwo. Nazwy zostały zmienione w taki sposób, aby pasowały do standardów w branży analiz MES i były intuicyjne dla nowych użytkowników. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) i [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799).
-   Dodano nowe ikony dla narzędzi [Standardowy solver CalculiX](FEM_SolverCalculixCxxtools/pl.md), [Kontrola pracy solvera](FEM_SolverControl/pl.md) i [Uruchom obliczenia solvera](FEM_SolverRun/pl.md) dla większej intuicyjności.
-   Solver CalculiX *(nowy framework)* został usunięty z GUI, ponieważ jest niedokończony i niepotrzebny w tej chwili. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823)
-   Poprawiono układ niektórych paneli zadań narzędzi do postprocessingu, aby zmniejszyć rozmiar zajmowanej przez nie poziomej przestrzeni. [Pull request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   Panel zadań [Zdefiniuj temperaturę początkową](FEM_ConstraintTemperature/pl.md) został przerobiony, aby rozwiązać problemy występujące podczas edycji tej funkcji. [Pull request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   Naprawiono stary problem polegający na tym, że [Flitr przycięcia linią](FEM_PostFilterDataAlongLine/pl.md) umożliwiał wykreślenie tylko wielkości, a nie składowych wektorowych wybranej zmiennej wyjściowej. [Pull request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   [Obciążenie siłą](FEM_ConstraintForce/pl.md) i [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md) zostały przebudowane, aby lepiej działały po stronie kodu źródłowego. [Pull request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) i [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   [Filtr danych w punkcie](FEM_PostFilterDataAtPoint/pl.md) ma teraz właściwość PointSize, która umożliwia ustawienie rozmiaru symbolu punktu w celu zwiększenia widoczności. [Pull request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   Dla przejrzystości polecenie [Obszar siatki MES](FEM_MeshRegion/pl.md) zostało przemianowane w GUI na MES Ulepsz \\(nazwa polecenia w kodzie pozostała niezmieniona)\\. [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)
-   Dla jasności, w GUI polecenie [Obszar siatki](FEM_MeshRegion/pl.md) zostało przemianowane na *Ulepsz siatkę* *(nazwa polecenia pozostaje niezmieniona)*. [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)
-   Wielkość przyspieszenia grawitacyjnego można teraz zmienić za pomocą właściwości narzędzia [Obciążenie grawitacją](FEM_ConstraintSelfWeight/pl.md). [Pull request #12044](https://github.com/FreeCAD/FreeCAD/pull/12044)
-   [Kontakt](FEM_ConstraintContact/pl.md) i [Wiązanie tie](FEM_ConstraintTie/pl.md) zostały znacznie ulepszone. Sztywność kontaktu ma teraz poprawną jednostkę, a wartość nachylenia krzywej zależności między naprężeniami stycznymi a przemieszczeniem stycznym w zakresie przylegania może być określona dla tarcia w kontakcie. Co więcej, odległość dociągania węzłów może być zdefiniowana dla kontaktu, podczas gdy wiązanie tie może mieć włączone lub wyłączone dociąganie. [Pull request #12133](https://github.com/FreeCAD/FreeCAD/pull/12133)
-   Solvery macierzowe PaStiX i Pardiso zostały dodane do wspieranych [solverów CalculiX\'a](FEM_SolverCalculixCxxtools/pl#Właściwości.md). Są one najszybsze, ale możliwość ich użycia zależy od wersji CalculiX\'a i dostępności dodatkowych bibliotek. [Pull request #12478](https://github.com/FreeCAD/FreeCAD/pull/12478)
-   Właściwość *Beam Reduced Integration* (ustawiona domyślnie na {{true/pl}}) została dodana do [ustawień solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md). Aktywuje ona zredukowany schemat całkowania dla elementów belkowych, umożliwiając m.in. użycie przekroju rurowego i eliminację problemów z dokładnością wyników w analizach z plastycznością. [Pull request #12513](https://github.com/FreeCAD/FreeCAD/pull/12513)
-   Niedokończone narzędzie [Zestaw węzłów](FEM_CreateNodesSet/pl.md) zostało usunięte z interfejsu. Nie można było z niego skorzystać. [Pull request #12611](https://github.com/FreeCAD/FreeCAD/pull/12611)
-   Procedura analizy CalculiX Sprawdź siatkę generuje teraz prawidłowo siatkę wyników. [Pull request #12612](https://github.com/FreeCAD/FreeCAD/pull/12612)
-   W panelu zadań doprecyzowano, że średnica używana przez przekrój belkowy rurowy to średnica zewnętrzna. [Pull request #12609](https://github.com/FreeCAD/FreeCAD/pull/12609)
-   Właściwość *Beam Shell Result Output 3D* [solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md) jest teraz domyślnie ustawiona na *prawda* aby zapewnić wyniki dla elementów belkowych i sensowne wyniki dla elementów powłokowych. [Pull request #12493](https://github.com/FreeCAD/FreeCAD/pull/12493)
-   Symbole cech analizy są teraz prawidłowo umieszczone gdy Zawartość (lub kontener Część) ma zmienioną właściwość położenia. [Pull request #12527](https://github.com/FreeCAD/FreeCAD/pull/12527)
-   [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md) działa teraz prawidłowo dla powłok niezależnie od ustawienia grup siatki. To ustawienie można zmienić w preferencjach. [Pull request #12437](https://github.com/FreeCAD/FreeCAD/pull/12437)
-   Proste wzmocnienie w [MES: Nieliniowy materiał mechaniczny](FEM_MaterialMechanicalNonlinear/pl.md) nazwano wzmocnieniem izotropowym. Dodano również wzmocnienie kinematyczne. [Pull request #12666](https://github.com/FreeCAD/FreeCAD/pull/12666)
-   Od teraz nieliniowość geometryczna nie jest automatycznie włączana i wymagana gdy używany jest nieliniowy model materiałowy. Są to niezależne formy nieliniowości. [Pull request #12703](https://github.com/FreeCAD/FreeCAD/pull/12703)
-   Mieszane siatki składające się zarówno z elementów trójkątnych jak i prostokątnych są teraz prawidłowo wyświetlane w obiekcie prezentacji graficznej wyników. [Pull request #12740](https://github.com/FreeCAD/FreeCAD/pull/12740)
-   Właściwość *Output Frequency* została dodana do [ustawień solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md). Definiuje częstotliwość zapisywania wyników w przyrostach. [Pull request #12672](https://github.com/FreeCAD/FreeCAD/pull/12672)
-   Elementy prostokątne drugiego rzędu mogą być teraz prawidłowo generowane. Do tej pory ustawienie drugiego rzędu w generatorze Gmsh tworzyło elementy prostokątne pierwszego rzędu przez brak polecenia *SecondOrderIncomplete* Gmsh, które jest teraz używane wewnętrznie. Te elementy mogą być również użyte do analiz 2D. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) i [Pull request #12774](https://github.com/FreeCAD/FreeCAD/pull/12774)
-   Wyznaczanie orientacji przekroju belkowego zostało częściowo naprawione. W związku z błędem w aktualnym wydaniu solvera CalculiX, nadal mogą występować problemy przy niektórych orientacjach. [Pull request #12833](https://github.com/FreeCAD/FreeCAD/pull/12833)
-   Przykłady analiz MES belki wspornikowej na stronie startowej zostały zaktualizowane i uzupełnione o nowy przykład z wykorzystaniem elementów 1D. [Pull request #12871](https://github.com/FreeCAD/FreeCAD/pull/12871)
-   Format w jakim FreeCAD zapisuje [obciążenie siłą](FEM_ConstraintForce/pl.md) jest teraz zgodny z formatem solvera CalculiX, co eliminuje rzadkie problemy ze zbyt długimi liczbami. [Pull request #12932](https://github.com/FreeCAD/FreeCAD/pull/12932)
-   Możliwe jest teraz eksportowanie [obiektu prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md) do formatu VTK. [Pull request #12987](https://github.com/FreeCAD/FreeCAD/pull/12987)
-   Nowe właściwości kontroli inkrementacji zostały dodane do [ustawień solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md). Obecnie, oprócz początkowego rozmiaru przyrostu i czasu trwania kroku analizy, można zdefiniować minimalny i maksymalny rozmiar przyrostu. Ponadto, właściwość *Iterations Thermo Mech Maximum* jest teraz nazwana *Iterations Maximum*, ponieważ można z niej już korzystać również w analizach statycznych (nie tylko termomechanicznych). [Pull request #12662](https://github.com/FreeCAD/FreeCAD/pull/12662)
-   Domyślna [grubość elementów 2D](FEM_ElementGeometry2D/pl.md) została zmieniona z 20 mm na 1 mm, ponieważ ma to więcej sensu w praktyce. [Pull request #13077](https://github.com/FreeCAD/FreeCAD/pull/13077)
-   Wiele ikon w tym środowisku pracy zostało znacznie usprawnionych aby zredukować ich podobieństwo i sprawić by było bardziej jasne do czego służą te narzędzia. [Pull request #13130](https://github.com/FreeCAD/FreeCAD/pull/13130)
-   Właściwość *Thermo Mech Type* została dodana do [ustawień solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md). Umożliwia przełączanie zwykłej (sprzężonej) analizy termomechanicznej na analizę niesprzężoną lub czysto termiczną. [Pull request #13296](https://github.com/FreeCAD/FreeCAD/pull/13296)
-   Stary problem z niedziałającą właściwością skali symboli dla wiązań MES został w końcu naprawiony, a właściwość *Scale* może być teraz używana do dostosowywania rozmiaru symboli wybranego wiązania. [Pull request #13274](https://github.com/FreeCAD/FreeCAD/pull/13274)
-   Poprawiono automatyczne skalowanie wiązań MES, aby lepiej radzić sobie z bardzo małymi i bardzo dużymi obiektami. [Pull request #13586](https://github.com/FreeCAD/FreeCAD/pull/13586)
-   [Obciążenie strumieniem ciepła](FEM_ConstraintHeatflux/pl.md) ma teraz tryb strumienia promieniowania cieplnego do modelowania promieniowania powierzchni do otoczenia. [Pull request #13466](https://github.com/FreeCAD/FreeCAD/pull/13466)
-   Usunięto kilka nieużywanych właściwości widoku symbolu wiązania. [Pull request #13569](https://github.com/FreeCAD/FreeCAD/pull/13569)
-   Nowe właściwości widoku (głównie *Color Mode*) zostały dodane do obiektów siatki MES, aby możliwe było zapisywanie i przywracanie własnych ustawień koloru i przezroczystości siatek. [Pull request #13698](https://github.com/FreeCAD/FreeCAD/pull/13698)
-   Teraz tylko ostatni dodany filtr pod każdym obiektem prezentacji graficznej wyników jest domyślnie widoczny. [Pull request #13820](https://github.com/FreeCAD/FreeCAD/pull/13820)
-   Wskazówki w panelach zadań kilku narzędzi zostały zmienione aby podpowiadać prawidłowe zasady wskazywania geometrii dla tych narzędzi. [Pull request #13921](https://github.com/FreeCAD/FreeCAD/pull/13921) and [Pull request #14002](https://github.com/FreeCAD/FreeCAD/pull/14002)
-   Wsparcie dla strumienia ciepła w wynikach analiz termomechanicznych zostało dodane do obiektu prezentacji graficznej wyników. [Pull request #14019](https://github.com/FreeCAD/FreeCAD/pull/14019)
-   [Funkcja zapisu wyników z przekroju](FEM_ConstraintSectionPrint/pl.md) została usprawniona - dodano wsparcie dla wyników w postaci strumienia ciepła i naprężeń od siły oporu (te ostatnie nie są na razie dostępne, ponieważ analizy 3D z CalculiX nie zostały jeszcze zaimplementowane). [Pull request #14046](https://github.com/FreeCAD/FreeCAD/pull/14046)
-   [Objętościowe źródło ciepła](FEM_ConstraintBodyHeatSource/pl.md) może być teraz używane z solverem CalculiX i ma dwa tryby do wprowadzania danych wejściowych - szybkość dyssypacji \[W/kg\] i moc całkowita \[W\]. [Pull request #14417](https://github.com/FreeCAD/FreeCAD/pull/14417)
-   Właściwości obrotu [Lokalnego układu współrzędnych](FEM_ConstraintTransform/pl.md) zostały zastąpione pojedynczą właściwością *Rotation* dla konsekwencji. [Pull request #14353](https://github.com/FreeCAD/FreeCAD/pull/14353)
-   Dodano narzędzie [Usuń elementy](FEM_CreateElementsSet/pl.md), aby umożliwić ukrywanie elementów siatki wybranych za pomocą wielokąta. [Pull request #11492](https://github.com/FreeCAD/FreeCAD/pull/11492).
-   Trzy przykłady MES na stronie startowej zostały zastąpione jednym, zawierającym wszystkie trzy warianty modelu belki wspornikowej *(1D, 2D i 3D)* w kontenerach [Grup](Std_Group/pl.md). [Pull request #15786](https://github.com/FreeCAD/FreeCAD/pull/15786)
-   Usunięto zbędne właściwości i pola wyboru *Fix* z [warunku brzegowego przemieszczenia](FEM_ConstraintDisplacement/pl.md). [Pull request #15531](https://github.com/FreeCAD/FreeCAD/pull/15531).
-   Poprawiono zachowanie przycisków Anuluj w panelach zadań generatorów siatek [Gmsh](FEM_MeshGmshFromShape/pl.md) i [Netgen](FEM_MeshNetgenFromShape/pl.md), aby można było ich użyć do przerwania trwającego procesu tworzenia siatki, co jest szczególnie ważne, gdy początkowo wybrany rozmiaru elementów jest zbyt mały. Ponadto zaimplementowano generator siatek Netgen, umożliwiając wreszcie korzystanie z niego na wszystkich systemach, w tym Linux. [Pull request #16515](https://github.com/FreeCAD/FreeCAD/pull/16515) i [Pull request #16433](https://github.com/FreeCAD/FreeCAD/pull/16433).
-   Dodano brakujący w generatorze siatek Gmsh algorytm 2D *Quasi-structured Quad* wraz z innymi poprawkami. [Pull request #15624](https://github.com/FreeCAD/FreeCAD/pull/15624).



## Środowisko pracy Materiał 

+++
| <img alt="" src=images/Materials_relnotes_1.0.png  style="width:384px;"> | System obsługi materiałów, w tym edytor, został całkowicie przerobiony. W przyszłości nastąpią dalsze ulepszenia w tym zakresie. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_1.0.png  style="width:384px;"> | Dodano podgląd wyglądu, aby pokazać materiały w taki sam sposób, w jaki będą wyświetlane w dokumentach. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++

+++
| <img alt="" src=images/Material_appearance_relnotes_1.0.jpg  style="width:384px;"> | Nowy system materiałów jest teraz używany do właściwości wyglądu modeli. [Pull request #13294](https://github.com/FreeCAD/FreeCAD/pull/13294) |
+++



### Planowane ulepszenia środowiska Materiał 

-   Dodano okna dialogowe do przeglądania właściwości wyglądu i materiału obiektu, które są dostępne jako narzędzia *Sprawdź wygląd* i *Sprawdź Materiał*. [Pull request #13967](https://github.com/FreeCAD/FreeCAD/pull/13967)



## Środowisko pracy Część 

+++
| <img alt="" src=images/Part_scale_relnotes_1.0.png  style="width:384px;"> | Dodano narzędzie [Skaluj](Part_Scale/pl.md), aby umożliwić łatwe skalowanie kształtów bez konieczności używania narzędzi ze środowiska Rysunku Roboczego. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_1.0.png  style="width:384px;"> | [Odbicie lustrzane](Part_Mirror/pl.md) teraz obsługuje obiekty referencyjne, takie jak [płaszczyzna](Part_Plane/pl.md), aby zdefiniować dowolną płaszczyznę lustrzaną oprócz standardowych płaszczyzn XY, XZ i YZ. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Pozostałe ulepszenia środowiska Część 

-   Właściwość **Frenet** jest teraz domyślnie włączona dla narzędzia [Wyciągnięcie po ścieżce](Part_Sweep/pl.md), aby uniknąć powszechnego problemu z renderowaniem. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)
-   Nowy [tryb dołączania](Part_EditAttachment/pl#Tryby_dołączania.md) o nazwie *Przecięcie* został dodany do Silnika Linia. Znajduje przecięcie dwóch płaskich ścian. [Pull request #12328](https://github.com/FreeCAD/FreeCAD/pull/12328)
-   Narzędzie [Rzutowanie na powierzchnię](Part_ProjectionOnSurface/pl.md) jest teraz parametryczne. [Pull request #13158](https://github.com/FreeCAD/FreeCAD/pull/13158)
-   Teraz wszystkie ikony środowiska Część używają niebieskiego motywu, a elementy pierwotne używają tej samej ikony dla paska narzędzi i drzewa. [Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   Polecenie [Utwórz szkic](Sketcher_NewSketch/pl.md) zostało dodane do paska narzędzi i menu środowiska Część, ponieważ operacje takie jak wyciągnięcie zwykle są oparte na szkicach. [Pull request #14318](https://github.com/FreeCAD/FreeCAD/pull/14318)
-   Nowy [tryb dołączenia](Part_EditAttachment/pl#Tryby_dołączenia.md) o nazwie *XY równolegle do płaszczyzny* został dodany do Silnika Płaszczyzna i Silnika 3D. Jego efekt jest podobny do *XY obiektu*, ale z płaszczyzną XY przesuniętą aby przechodziła przez wskazany wierzchołek. W przeciwieństwie do trybu *Przekształcenia położenia odniesienia*, nowy tryb nie przesuwa środka w 2D/szkicowniku. Może być używany z płaszczyznami odniesienia i konstrukcyjnymi oraz szkicami, ale też dowolnymi obiektami z właściwością *Umiejscowienie*. [Pull request #14372](https://github.com/FreeCAD/FreeCAD/pull/14372)



## Środowisko pracy Projekt Części 

+++
| <img alt="" src=images/Revolve_options_relnotes_1.0.png  style="width:384px;"> | Dodano więcej trybów do [wyciągnięcia przez obrót](PartDesign_Revolution/pl.md) i [rowka](PartDesign_Groove/pl.md) - do pierwszego/ostatniego, do ściany i dwa wymiary. [Pull request #7193](https://github.com/FreeCAD/FreeCAD/pull/7193) |
+++

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_1.0.png  style="width:384px;"> | Ulepszono panel zadań funkcji [wyciągnięcie](PartDesign_Pad/pl.md) oraz [kieszeń](PartDesign_Pocket/pl.md) *(zmieniona kolejność elementów interfejsu użytkownika, opcja*Wybierz ścianę*pozostaje ukryta, gdy jest niepotrzebna itd.)*. [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_1.0.png  style="width:384px;"> | Tryb odsunięcia został dodany dla [szyku liniowego](PartDesign_LinearPattern/pl.md) i [szyku biegunowego](PartDesign_PolarPattern/pl.md). Poprzedni tryb został przemianowany na **Długość całkowita**.. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++

+++
| <img alt="" src=images/Single_solid_rule_relnotes_1.0.PNG  style="width:384px;"> | Dodano eksperymentalne wsparcie dla wielu brył w ramach jednej [Zawartości](PartDesign_Body/pl.md). Można je włączyć w preferencjach *(dla nowych Zawartości)* lub we właściwościach istniejącego obiektu tego typu. [Pull request #13960](https://github.com/FreeCAD/FreeCAD/pull/13960) |
+++

+++
| <img alt="" src=images/Pad_up_to_shape_relnotes_1.0.PNG  style="width:384px;"> | Tryb *Up to shape* został dodany do Wyciągnięcia i Kieszeni, umożliwiając kończenie ich na wielu ścianach, w przeciwieństwie do trybu *Do powierzchni*, który pozwala na wskazanie tylko jednej ściany. [Pull request #11392](https://github.com/FreeCAD/FreeCAD/pull/11392) i [Pull request #14433](https://github.com/FreeCAD/FreeCAD/pull/14433) |
+++



### Pozostałe ulepszenia środowiska Projekt Części 

-   Opcja *Stwórz grubość do wewnątrz* jest teraz domyślnie włączona dla narzędzia [Grubość](PartDesign_Thickness/pl.md). [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)
-   Punkty konstrukcyjne zmieniają teraz kolor gdy są podświetlone lub zaznaczone *(jak inne obiekty konstrukcyjne)*. [Pull request #12439](https://github.com/FreeCAD/FreeCAD/pull/12439)
-   Ikonki środowiska Projekt Części zostały nieznacznie ulepszone w celu zapewnienia spójności. [Pull request #13109](https://github.com/FreeCAD/FreeCAD/pull/13109)
-   Dodano właściwość \"Wycisz\", aby tymczasowo wyłączyć funkcję. [Pull request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) i [Pull request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   Paski narzędzi środowiska Projekt Części zostały zaktualizowane - układy odniesienia i akcje oparte na szkicach są teraz zgrupowane, narzędzie [Part CheckGeometry](Part_CheckGeometry.md) zostao dodane do paska narzędzi i menu, a paski narzędzi zostały podzielone na osobne, aby umożliwić ich uporządkowanie. [Pull request #13833](https://github.com/FreeCAD/FreeCAD/pull/13833)
-   Teraz wszystkie cechy używają tej samej ikony dla paska narzędzi i drzewa. [Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   Do odbicia lustrzanego i szyków dodano nowy tryb *Transform body*, który pozwala przekształcać cały kształt części zamiast pojedynczych kształtów narzędzi operacji addytywnych i subtraktywnych. [Pull request #12589](https://github.com/FreeCAD/FreeCAD/pull/12589)
-   Poprawiono układ okna dialogowego narzędzia [Otwór](PartDesign_Hole/pl.md). [Pull request #14031](https://github.com/FreeCAD/FreeCAD/pull/14031)
-   Narzędzie [Przenieś ze starszej wersji](PartDesign_Migrate/pl.md) zostało usunięte z interfejsu graficznego programu, ponieważ nadawało się tylko do przenoszenia plików między wersjami, które obecnie są wysoce przestarzałe. [Pull request #15196](https://github.com/FreeCAD/FreeCAD/pull/15196)



## Środowisko pracy Szkicownik 

+++
| <img alt="" src=images/Arc_helper_relnotes_1.0.png  style="width:384px;"> | Implementacja nakładki okręgu dla łuków *(aby rozwiązać problem ograniczeń pojawiających się z dala od nich)* została uzupełniona o [polecenie](Sketcher_ArcOverlay/pl.md) do ich przełączania. [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano [kontekstowe wiązanie wymiarowe](Sketcher_Dimension/pl.md), aby umożliwić szybkie i intuicyjne wymiarowanie za pomocą jednego wszechstronnego narzędzia. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   [Parametry narzędzia](Sketcher_Workbench#On-View-Parameters/pl.md) zostały dodane, aby umożliwić wymiarowanie w ruchu (podczas rysowania kształtów). W zależności od ustawienia preferencji On-View-Parameters, mogą one być wyłączone, ograniczone tylko do wymiarów (bez współrzędnych początkowych) lub w pełni włączone. Ponadto dodano tryby dla narzędzi kształtów. Można je wybrać za pomocą klawisza M lub listy rozwijanej w panelu zadań. Niektóre narzędzia mają dodatkowe ustawienia w postaci pól wyboru w panelu zadań i dodatkowych skrótów klawiaturowych. Obecnie nowe funkcje są dostępne dla punktów, linii, łuków, elips, prostokątów, wielokątów i szczelin oraz krzywych złożonych. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) i kolejne
   

+++
| <img alt="" src=images/Offset_relnotes_1.0.png  style="width:384px;"> | Dodano narzędzie [odsunięcia](Sketcher_Offset/pl.md), aby umożliwić przesunięcie krzywych. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_1.0.png  style="width:384px;"> | Tryb trzypunktowego [prostokąta](Sketcher_CompCreateRectangles/pl.md) został dodany w dwóch wersjach - trzy narożniki lub środek i dwa narożniki. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_1.0.png  style="width:384px;"> | Dodano narzędzie [szczeliny na łuku](Sketcher_CreateArcSlot/pl.md) z dwoma trybami *(końce łuku i płaskie końce)*, aby umożliwić tworzenie zakrzywionych szczelin [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano [wiązanie poziomo / pionowo](Sketcher_ConstrainHorVer/pl.md). Automatycznie stosowane jest wiązanie poziome, jeśli linia jest bliższa orientacji poziomej lub ograniczenie pionowe, jeśli jest bliższa orientacji pionowej. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_1.0.png  style="width:384px;"> | Poprawiono renderowanie wiązań kąta i promienia. Wiązania kątowe mają teraz pełne linie przedłużające. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_1.0.png  style="width:384px;"> | Dodano narzędzie [transformacji biegunowej](Sketcher_Rotate/pl.md), aby umożliwić obracanie i kołowe szyki geometrii szkicownika. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++

   
  <img alt="" src=images/Sketcher_copy-cut-paste_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie uruchomi się.   Możliwe jest teraz kopiowanie / wycinanie i wklejanie geometrii szkicu *(z wiązaniami)* przy użyciu typowych skrótów klawiaturowych: Ctrl+C, Ctrl+X i Ctrl+V. Nie tylko w obrębie jednego szkicu, ale także pomiędzy różnymi szkicami lub nawet różnymi instancjami FreeCAD. Geometria jest kopiowana w postaci poleceń Python, dzięki czemu może być również wykorzystywana w inny sposób *(np. udostępniana na forum)*. [Pull request #11537](https://github.com/FreeCAD/FreeCAD/pull/11537)
   

+++
| <img alt="" src=images/Scale_transform_relnotes_1.0.png  style="width:384px;"> | Narzędzie [Skaluj](Sketcher_Scale/pl.md) zostało dodane, umożliwiając skalowanie geometrii w szkicu przy pomocy wskazanego punktu środkowego i współczynnika skali lub dwóch punktów referencyjnych. [Pull request #11265](https://github.com/FreeCAD/FreeCAD/pull/11265) |
+++

   
  <img alt="" src=images/B-spline_tangency_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   Styczność do krawędzi krzywej złożonej została dodana, eliminując konieczność korzystania z punktów końcowych i różnych obejść. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

+++
| <img alt="" src=images/Sketcher_translate_relnotes_1.0.png  style="width:384px;"> | Narzędzia [Szyk prostokątny](Sketcher_RectangularArray/pl.md), [Przesuń](Sketcher_Move/pl.md), [Kopiuj](Sketcher_Copy/pl.md) i [Klonuj](Sketcher_Clone/pl.md) zostały zastąpione pojedynczym [narzędziem do transformacji liniowej](Sketcher_Translate/pl.md). [Pull request #11267](https://github.com/FreeCAD/FreeCAD/pull/11267) |
+++

+++
| <img alt="" src=images/Sketcher_chamfer_relnotes_1.0.png  style="width:384px;"> | Dodano narzędzie [Sfazowanie](Sketcher_CreateChamfer/pl.md) z opcją przełączenia do trybu [zaokrąglenie](Sketcher_CreateFillet/pl.md). Co więcej, nie ma już osobnego narzędzia do zaokrąglania z zachowaniem narożnika. Opcja *Zachowaj narożnik* *(domyślnie aktywna)* została dodana do narzędzia [Zaokrąglenie](Sketcher_CreateFillet/pl.md). [Pull request #12898](https://github.com/FreeCAD/FreeCAD/pull/12898) |
+++

   
  <img alt="" src=images/New_symmetry_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie uruchomi się.   Narzędzie [Symetria](Sketcher_Symmetry/pl.md) zostało przebudowane. Należy teraz najpierw wskazać geometrię, uruchomić narzędzie i wybrać linię lub punkt do wykonania odbicia lustrzanego. Podgląd jest pokazywany po najechaniu kursorem na taki obiekt. Zachowanie narzędzia można kontrolować w panelu zadań. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

   
  <img alt="" src=images/Auto_midpoint_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie uruchomi się.   [Wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md) jest teraz dodawane automatycznie gdy używane jest przyciąganie do punktu środkowego linii. [Pull request #13147](https://github.com/FreeCAD/FreeCAD/pull/13147)
   

+++
| <img alt="" src=images/Sketcher_arc_length_relnotes_1.0.png  style="width:384px;"> | [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md) może być teraz używane do tworzenia wiązań długości łuku (łuk kołowy należy wskazać przed uruchomieniem narzędzia). [Pull request #12602](https://github.com/FreeCAD/FreeCAD/pull/12602) |
+++

+++
| <img alt="" src=images/Point_color_relnotes_1.0.png  style="width:384px;"> | Kolor renderowania punktów jest teraz różny w zależności od tego czy jest to normalny punkt lub punkt końcowy (biały, teraz tworzone domyślnie przez narzędzie [Utwórz punkt](Sketcher_CreatePoint/pl.md)), punkt konstrukcyjny lub środkowy (niebieski) bądź punkt zbieżny z innym (czerwony). [Pull request #13098](https://github.com/FreeCAD/FreeCAD/pull/13098) |
+++

   
  <img alt="" src=images/Trim_drag_relnotes_1.0.gif  style="width:384px;">Kliknij obraz, jeśli animacja nie została uruchomiona.   Narzędzie [Przytnij krawędź](Sketcher_Trimming/pl.md) może być teraz używane w trybie przytrzymaj i przeciągnij. [Pull request #13188](https://github.com/FreeCAD/FreeCAD/pull/13188)
   



### Pozostałe ulepszenia środowiska Szkicownik 

-   Dodano tryb ramki dla narzędzia Prostokąt. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Dodano dwa nowe tryby dla narzędzia Linia: *Punkt, długość, kąt* i *Punkt, szerokość, wysokość*. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Zmieniono wygląd ikonek [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md) i [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md). Teraz ta pierwsza nie jest już tak podobna do [Utwórz kalkę techniczną](Sketcher_CarbonCopy/pl.md) i obie ikony przełączania zmieniają się po kliknięciu. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Ikony Szkicownika zostały przebudowane w celu ujednolicenia ich wyglądu *(szerokości obrysu, kolorów i rozmiarów punktów)*. [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785).
-   Wprowadzono opcjonalne [zunifikowane wiązanie zbieżności](Sketcher_ConstrainCoincidentUnified/pl.md). Łączy ono wiązania [zbieżności](Sketcher_ConstrainCoincident/pl.md) i [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)
-   Poprawiono renderowanie wiązań kąta łuku, kąta linii i odległości łuku. [Pull request #12012](https://github.com/FreeCAD/FreeCAD/pull/12012).
-   Typy krawędzi można teraz dostosowywać nie tylko poprzez zmianę koloru, ale także wzoru i rozmiaru. Pozwala to np. na tworzenie przerywanych linii konstrukcyjnych. [Pull request #11996](https://github.com/FreeCAD/FreeCAD/pull/11996).
-   Menu prawego przycisku myszy jest teraz kontekstowe i zawiera również polecenia B-spline. [Pull request #11884](https://github.com/FreeCAD/FreeCAD/pull/11884) i [Pull request #11973](https://github.com/FreeCAD/FreeCAD/pull/11973)
-   Podwójne kliknięcie krawędzi zaznacza całą połączoną geometrię. [Pull request #11925](https://github.com/FreeCAD/FreeCAD/pull/11925)
-   Narzędzia [linia](Sketcher_CreateLine/pl.md) i [polilinia](Sketcher_CreatePolyline/pl.md) są teraz zgrupowane razem, a polilinia jest wyświetlana jako pierwsza. [Pull request #13509](https://github.com/FreeCAD/FreeCAD/pull/13509)
-   Paski narzędzi Szkicownika zostały nieznacznie zreorganizowane w celu zapewnienia przejrzystości i spójności. [Pull request #13407](https://github.com/FreeCAD/FreeCAD/pull/13407) i [Pull request #13763](https://github.com/FreeCAD/FreeCAD/pull/13763)
-   Poprawiono ikony narzędzia [Kalka techniczna](Sketcher_CarbonCopy/pl.md), aby były lepiej widoczne. [Pull request #15074](https://github.com/FreeCAD/FreeCAD/pull/15074)



## Środowisko pracy Arkusz Kalkulacyjny 



### Pozostałe ulepszenia środowiska Arkusz Kalkulacyjny 

-   Podwójne kliknięcie na arkuszu kalkulacyjnym w widoku drzewa teraz przełącza do tego środowiska pracy. [Pull request #13137](https://github.com/FreeCAD/FreeCAD/pull/13137)
-   Ikony tego środowiska zostały ulepszone. [Pull request #13996](https://github.com/FreeCAD/FreeCAD/pull/13996)



## Środowisko pracy Rysunek Techniczny 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_1.0.png  style="width:250px;"> | Narzędzie [Okrąg kosmetyczny](TechDraw_CosmeticCircle/pl.md) zostało dodane, aby umożliwić tworzenie geometrii pomocniczych w postaci okręgów poprzez wybranie środka i wprowadzenie promienia. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_1.0.png  style="width:250px;"> | Dodano narzędzie [Rozszerzenie Etykieta długości łuku](TechDraw_ExtensionArcLengthAnnotation/pl.md) do tworzenia wymiarowych adnotacji długości łuku wybranych krawędzi. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_1.0.png  style="width:250px;"> | Dodano narzędzie [Dodaj odsunięcie wierzchołka](TechDraw_CommandAddOffsetVertex/pl.md) do tworzenia wierzchołków kosmetycznych jako przesunięć od wybranych wierzchołków. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++

+++
| <img alt="" src=images/Broken_view_relnotes_1.0.png  style="width:250px;"> | Narzędzie [Widok przerwania](TechDraw_BrokenView/pl.md) zostało dodane aby łatwo przedstawiać długie obiekty. [Pull request #13331](https://github.com/FreeCAD/FreeCAD/pull/13331) |
+++

   
  <img alt="" src=images/Techdraw_smart_dimension_relnotes_1.0.gif  style="width:320px;">Kliknij obraz, jeśli animacja nie zostanie uruchomiona.   Dodano nowe narzędzie do wymiarowania kontekstowego, oparte o [to wprowadzone w szkicowniku](Sketcher_Dimension/pl.md). [Pull request #13525](https://github.com/FreeCAD/FreeCAD/pull/13525)
   



### Pozostałe ulepszenia środowiska Rysunek Techniczny 

-   Przekroje oparte na innych przekrojach używają teraz domyślnie oryginalnego *(nieprzyciętego)* kształtu. Można to zmienić w ustawieniach przekroju, aby zamiast tego użyć poprzedniego przekroju. [Pull request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281).
-   Obiekty kosmetyczne i linie środka można teraz usuwać, zaznaczając je i naciskając klawisz **Delete**. Wcześniej powodowało to usunięcie całego widoku. [Pull request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) oraz [Pull request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   Dodano nową, bardziej intuicyjną ikonę dla narzędzia [Symbol spawalniczy](TechDraw_WeldSymbol/pl.md). [Pull request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   Poprawiono zachowanie trybu punkt + krawędź narzędzia [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md). [Pull request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   Dodano sprawdzanie stanu dla przycisku [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md), aby użytkownik mógł zobaczyć, czy przycisk jest aktywny, czy nie. [Pull request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   Poprawiono zachowanie narzędzia [Zmień wygląd linii](TechDraw_DecorateLine/pl.md). Teraz dwukrotne kliknięcie linii wywołuje to narzędzie. Style linii są poprawnie przywracane, jeśli użytkownik naciśnie przycisk *Anuluj*. Wcześniej nie było różnicy między naciśnięciem przycisku *OK* i *Anuluj*. [Pull request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188).
-   Kolor i przezroczystość ścian można teraz ustawić dla każdego widoku. [Pull request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   Dodano tryb wielokrotnego wyboru, który można włączyć w Preferencjach. W tym trybie można wybrać wiele wierzchołków, krawędzi i ścian, klikając je lewym przyciskiem myszy, bez konieczności trzymania wciśniętego klawisza Ctrl. [Pull request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   [Rozszerzenie Oblicz obszar wybranych powierzchni](TechDraw_ExtensionAreaAnnotation.md) może teraz obliczać obszary dowolnych powierzchni. [Pull request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Linie nieciągłe będą teraz zgodne ze standardami ISO / ANSI zamiast stylu linii Qt. Dodano nową preferencję do wyboru standardu. [Pull request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   Poprawiono działanie narzędzia [Wstaw wymiar długości w aksonometrii](TechDraw_AxoLengthDimension/pl.md). Teraz, podczas wymiarowania krawędzi równoległych do osi globalnego układu współrzędnych, rzeczywista wartość *(3D)* jest obliczana automatycznie i wstawiana do właściwości Format Spec *(jako tekst)*. [Pull request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   Narzędzie [Rozszerzenie Wyrównaj widok przekroju](TechDraw_ExtensionPositionSectionView/pl.md) może być teraz używane poprzez wybranie krawędzi w widoku przekroju i wierzchołka w widoku źródłowym. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)
-   Dodano narzędzie [Rozszerzenie Dodaj przedrostek \"n×\"](TechDraw_ExtensionInsertRepetition/pl.md) do wstawiania liczby powtarzających się elementów. [Pull request #12509](https://github.com/FreeCAD/FreeCAD/pull/12509).
-   Wprowadzono małe, ale istotne usprawnienia użytkowe - podwójne kliknięcie na stronie środowiska Rysunek techniczny powoduje przejście do tego modułu a narzędzie *Przesuń widok* zostało zastąpione prostym przeciągnięciem i upuszczeniem w [drzewie](Tree_view/pl.md). Narzędzia *Dodaj widok do grupy wycinków* i *Usuń widok z grupy wycinków* również zastąpiono przeciąganiem i upuszczaniem w drzewie. [Pull request #13063](https://github.com/FreeCAD/FreeCAD/pull/13063)
-   Tabele szablonów rysunków są teraz automatycznie wypełniane dostępnymi informacjami *(jak data i tytuł)*. [Pull request #13005](https://github.com/FreeCAD/FreeCAD/pull/13005)
-   Narzędzie [Rzutowanie kształtów](TechDraw_ProjectShape/pl.md) zostało usunięte z środowiska Rysunek Techniczny, ponieważ zostało odziedziczone po starym środowisku roboczym Kreślenie i nie ma nic wspólnego ze stroną Rysunku technicznego. [Pull request #13655](https://github.com/FreeCAD/FreeCAD/pull/13655).
-   Narzędzie [Wstaw widok](TechDraw_View/pl.md) zostało ulepszone, aby mogło obsługiwać więcej typów obiektów i ustawień. Pozwoliło to na usunięcie następujących narzędzi z paska narzędzi: [Wstaw widok Arkusza kalkulacyjnego](TechDraw_SpreadsheetView/pl.md), [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md), [Wstaw symbol SVG](TechDraw_Symbol/pl.md), [Wstaw obraz bitmapy](TechDraw_Image/pl.md) i [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md). [Pull request #13219](https://github.com/FreeCAD/FreeCAD/pull/13219)
-   Dodano przyciąganie, aby umożliwić automatyczne wyrównanie widoków i wymiarów. Przyciąganie można tymczasowo wyłączyć za pomocą modyfikatora klawiszem Alt. [Pull request #13659](https://github.com/FreeCAD/FreeCAD/pull/13659)
-   Poprawiono obsługę elementów linii pomocniczych *(kosmetycznych)* na różne sposoby. [Pull request #14216](https://github.com/FreeCAD/FreeCAD/pull/14216)
-   Poprawiono wiele ikon środowiska Rysunek Techniczny. [Pull request #14873](https://github.com/FreeCAD/FreeCAD/pull/14873) i następujące
-   Panel zadań narzędzia [Dodaj symbol wykończenia powierzchni](TechDraw_SurfaceFinishSymbols/pl.md) został znacznie ulepszony wizualnie. [Pull request #16147](https://github.com/FreeCAD/FreeCAD/pull/16147)



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/pl
