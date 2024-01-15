---
 TutorialInfo:l
   Topic: Modelowanie
   Level: Początkujący
   Author: Carlo Dormeletti <br>Ed Williams <br>Roy 043 
   Time: 1 godzina
   FCVersion: 0.19 lub nowszy
   SeeAlso: Basic_Part_Design_Tutorial/pl
---

# Basic Part Design Tutorial 019/pl







## Wprowadzenie

*Poradnik ten to jest uaktualniona wersja poradnika [Podstawy dla środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md)*.

![](images/Pd_tut_final_solid.png )

Ten poradnik wprowadza użytkowników do środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md). W tym poradniku stworzymy model przestrzennej bryły części pokazanej na powyższym obrazku. W [rysunku](TechDraw_Workbench/pl.md) na końcu tego akapitu podane są wszystkie niezbędne wymiary do wykonania zadania.

Rozpoczniemy od utworzenia podstawowego kształtu bryły ze szkicu bazowego, a następnie będziemy rozbudowywać ten kształt, dodając tzw. cechy. Cechy te będą dodawać materiał do bryły lub usuwać go z niej za pomocą dodatkowych szkiców i towarzyszących im operacji.

Zastosujemy niektóre z technik opisanych w artykule [Porady dotyczące tworzenia stabilnych modeli](Feature_editing/pl#Porady_dotycz.C4.85ce_tworzenia_stabilnych_modeli.md)

-   Użyjemy **szkicu głównego**
-   **Nazwane wiązania** posłużą do przechowywania wymiarów, do których będzie można się odwołać w dalszej części budowy modelu.
    Na przykład, aby zmienić szerokość modelu z 53 mm, jak na rysunku technicznym, na 55mm wystarczy zmodyfikować wartość **Długość**\' odpowiedniego **nazwanego wiązania** w **szkicu głównym**, a cały model odpowiednio się zmodyfikuje. Jest to projektowanie \"parametryczne\" w działaniu.
-   **Geometrie zewnętrzne** są potencjalnie objęte [Problemom nazewnictwa topologicznego](Topological_naming_problem/pl.md). Będziemy ich używać tylko wtedy, gdy będzie to absolutnie konieczne i będziemy starali się odwoływać do najbardziej **stabilnych** dostępnych elementów. Odwoływanie się do krawędzi i wierzchołków szkiców jest zwykle bardziej stabilne niż odwoływanie się do krawędzi i wierzchołków wygenerowanej geometrii bryłowej.

Ten poradnik nie będzie wykorzystywał wszystkich funkcji i narzędzi dostępnych w środowisku pracy Projekt Części, ale zapewni podstawy, na których użytkownicy mogą budować swoją wiedzę i umiejętności.

Zapraszamy do sygnalizowania wszelkich błędów i problemów w tym wątku na forum: [Nowy poradnik środowiska Projekt Części dla FC 019 i 020](https://forum.freecad.org/viewtopic.php?f=36&t=73235).

<img alt="" src=images/Tutorial_Drawing_Sheet.png  style="width:900px;">



## Uwagi wstępne 

-   Ten poradnik zawiera szczegółowe instrukcje, gdy opisuje daną operację po raz pierwszy. Kolejne operacje będą miały bardziej zwięzły opis. W razie wątpliwości należy znaleźć operację, która zawiera bardziej szczegółowy opis. Na przykład podczas tworzenia szkicu po raz pierwszy proces wyboru płaszczyzny szkicu będzie szczegółowo wyjaśniony, dla kolejnych szkiców nie będzie.
-   Wszystkie wymienione narzędzia są dostępne z pasków narzędziowych oraz z menu.
-   Ten poradnik zakłada, że opcja {{CheckBox|TRUE|Wiązania automatyczne}} w oknie **Edycja kontrolek** Szkicownika jest zaznaczona. Dzięki temu niektóre wiązania zostaną zastosowane automatycznie. W przeciwnym razie trzeba będzie zastosować je samodzielnie.
-   Jeśli solver szkicownika wykryje zbędne wiązanie, zmieni kolor szkicu na pomarańczowy. Przed dodaniem kolejnych wiązań należy usunąć nadmiarowe wiązania. Nadmiarowe wiązania są widoczne w panelu zadań, kliknij niebieskie odniesienie i naciśnij **Usuń**.
-   Kolor wymieniony powyżej jest kolorem domyślnym, można go zmienić w preferencjach. To samo dotyczy innych kolorów wymienionych w tym poradniku.
-   Z narzędzia do rysowania Szkicownik wychodzimy naciskając klawisz **Esc** lub klikając prawym przyciskiem myszy pusty obszar okna [widoku 3D](3D_view/pl.md). Kursor myszki zmieni swój wygląd na standardowy kursor ze strzałką. Jeśli naciśniesz **Esc** jeszcze raz, wyjdziesz z trybu edycji szkicu. Aby powrócić do edytora, kliknij zakładkę Model, a następnie kliknij dwukrotnie element Szkic w [Widoku drzewa](Tree_view/pl.md) lub kliknij go prawym przyciskiem myszki i wybierz **Edycja szkicu** z menu kontekstowego. Aby uniknąć opuszczania trybu edycji po zbyt częstym naciskaniu klawisza **Esc**, zmień preferencje **Klawisz Esc umożliwia wyjście z trybu edycji szkicu**, zobacz stronę [Ustawienia szkicownika](Sketcher_Preferences/pl#Og.C3.B3lne.md).
-   Możliwe jest, że niektóre elementy w panelu zadań, na przykład przycisk **OK**, nie są widoczne, jeśli panel nie jest wystarczająco szeroki. Możesz go poszerzyć, przeciągając jego prawy brzeg. Umieść kursor myszki nad krawędzią, gdy kursor zmieni wygląd na dwukierunkową strzałkę, przytrzymaj lewy przycisk myszki i przeciągnij.
-   Przycisk **&gt;&gt;** na pasku narzędzi wskazuje, że pasek narzędzi jest skrócony. Możesz użyć wspomnianego przycisku, aby rozwinąć, lub przenieść pasek narzędzi w miejsce, gdzie jest więcej miejsca. Aby przesunąć pasek narzędziowy umieść kursor myszki nad uchwytem przed pierwszą ikoną na pasku narzędziowym, przytrzymaj lewy przycisk myszki i przeciągnij.
-   W trakcie cyklu rozwoju v0.21 wprowadzono nową ikonę dla narzędzia [Utwórz polilinię](Sketcher_CreatePolyline/pl.md): <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;">. Stara ikona wygląda tak: <img alt="" src=images/Sketcher_CreatePolyline_rel_0.20.svg  style="width:24px;">. W tym poradniku będziemy używać nowej ikony.
-   Zapoznaj się z informacjami na stronie [Koncepcje środowiska Projekt Części](Part_and_PartDesign/pl#Koncepcje_.C5.9Brodowiska_Projekt_Cz.C4.99.C5.9Bci.md), aby zapoznać się z pewnymi podstawami koncepcyjnymi.
-   Zapoznaj się z informacjami na stronie [środowisko pracy Szkicownik](Sketcher_Workbench/pl.md), aby uzyskać bardziej szczegółowe wyjaśnienie niektórych terminów używanych tutaj.



## Rozpoczynamy

Najpierw upewnij się, że właśnie jesteś w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md). W razie potrzeby wybierz go z listy rozwijanej [Środowisk pracy](Std_Workbench/pl.md). Po uruchomieniu go należy utworzyć nowy dokument, jeśli jeszcze tego nie zrobiłeś. Dobrym nawykiem jest częste zapisywanie swojej pracy, dlatego najpierw zapisz nowy dokument, nadając mu dowolną nazwę.

Cała praca w ramach środowiska pracy Projekt Części zaczyna się od [Zawartości](Glossary#Body.md). Kliknij <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Utwórz zawartość](PartDesign_Body/pl.md), aby ją utworzyć i aktywować. Zauważ, że możliwe jest również pominięcie tego kroku: podczas tworzenia szkicu za pomocą narzędzia środowiska Projekt Części <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md), jeśli nie zostanie znaleziona żadna istniejąca zawartość, nowa zostanie automatycznie utworzona i aktywowana.



## Szkic główny 

Szkic główny zawiera prostokątny kształt podstawy modelu oraz dwa *nazwane wiązania*, które dostarczą prawidłowe wymiary do innych części modelu: **długość**, która będzie zawierać 53 mm *(wynik dodania wymiaru 39 mm do dwóch boków 7 mm)*, oraz **szerokość**, która będzie zawierać 26 mm. Aby móc wykorzystać symetrię modelu w dalszych krokach, górna krawędź prostokąta zostanie wyśrodkowana względem punktu odniesienie położenia za pomocą wiązania symetrycznego.

**Sketch**

<img alt="Fig: MS1" src=images/Pd_start_00.png  style="width:300px;"> <img alt="Fig: MS2" src=images/Pd_tut_sketch_start.png  style="width:300px;"> <img alt="Fig: MS3" src=images/Pd_tut_sel_points_h.png  style="width:300px;"> <img alt="Fig: MS4" src=images/Pd_tut_rect_h_dim_end.png  style="width:300px;"> <img alt="Fig: MS5" src=images/Pd_tut_rect04.png  style="width:300px;"> <img alt="Fig: MS6" src=images/Pd_tut_rect_v3.png  style="width:300px;">

**Krok A: Utwórz szkic**

1.  Kliknij <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md). Spowoduje to utworzenie szkicu w obrębie właśnie utworzonej bryły. Będzie on nosił nazwę **Szkic**.
2.  Otworzy się panel zadań podobny do tego z **Rys. MS1**, w którym należy wybrać, do której płaszczyzny zostanie dołączony szkic.
    1.  Wybierz **XY_Plane** z listy lub wybierz tę płaszczyznę w oknie [widoku 3D](3D_view/pl.md).
    2.  Kliknij **OK**.
3.  FreeCAD automatycznie przełączy się na środowisko pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md)
4.  Szkic jest otwierany w trybie edycji: zobaczysz coś w rodzaju **Rys: MS2**. Wskazane są osie X *(linia czerwona)* i Y *(linia zielona)* szkicu oraz jego punkt odniesienia położenia *(czerwony punkt)*.

**Krok B: Dodaj geometrię**

1.  Kliknij <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Utwórz prostokąt](Sketcher_CreateRectangle/pl.md).
2.  Podczas gdy narzędzie jest aktywne kursor ma następujący wygląd:
    ![](images/Pd_tut_rec_cursor.png )
3.  Wybierz dwa punkty, aby utworzyć prostokąt z grubsza wyśrodkowany wokół **osi Y** podobnie jak na **Rys: MS3**. Uwaga:
    -   Nie umieszczaj punktów na osi, ponieważ Solver automatycznie zastosuje wiązania, które później stworzą problemy.
    -   Wymiary prostokąta są w tym momencie nieistotne. Zostaną one przypisane za pomocą więzów w późniejszym kroku.
4.  Po zakończeniu naciśnij **Esc** lub kliknij prawym przyciskiem myszy, aby zakończyć pracę z narzędziem.

**Krok C: Przypisz wiązanie poziome**

1.  Wybierz linię zdefiniowaną przez **P2** i **P3** w **Rys: MS3**.
2.  Kliknij <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md):
    1.  Pomiędzy punktami końcowymi wybranej linii pojawi się wymiar. Ten wymiar to aktualna wartość długości.
    2.  Dodatkowo pojawi się okno dialogowe:

![](images/Pd_tut_rect03.png )

1.  1.  Przypisz **Długość = 53 mm**
    2.  Aby można było później odwołać się do tego wymiaru potrzebna jest jego nazwa. Możesz użyć dowolnej nazwy, musi być ona tylko unikalna w obrębie szkicu. Przypisz **Nazwę = długość**.
    3.  Kliknij **OK**.

2.  Wynik powinien być podobny do **Rys. MS4**

**Krok D: Przypisz wiązanie symetrii**

1.  Wybierz punkty **P2** i **P3** prostokąta.
2.  Wybierz **punkt odniesienia położenia** szkicu. Uwaga: kolejność wyboru punktów jest ważna.
3.  Kliknij <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md).
4.  W końcu otrzymasz coś, co wygląda jak **rysunek: MS5**.

*\'Krok E: Przypisz wiązanie pionowe*

:   Przypisz pionowe wiązanie odległości, stosując tę samą procedurę, która została użyta dla poprzednio zastosowanego poziomego wiązania odległości:

1.  Wybierz linię zdefiniowaną przez **P3** i **P4** w **Rys: MS3**.
2.  Kliknij <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md):
    1.  Przypisz **Długość = 26 mm**
    2.  Przypisz **Nazwę = szerokość**.
    3.  Kliknij **OK**.
3.  Wynik powinien odpowiadać **rysunkowi: MS6**.
4.  Szkic jest teraz w pełni związany:
    -   Linie w szkicu są jasnozielone.
    -   W sekcji **Komunikaty Solvera** w panelu zadań wyświetlany jest komunikat **W pełni związany**.
    -   Jeśli wybierzesz dowolną linię lub wierzchołek szkicu i spróbujesz go przeciągnąć, pozostanie on nieruchomy.

**Krok F: Zamknij szkic**

:   Kliknij **Zamknij** u góry panelu [Zadań](Task_panel/pl.md), aby wyjść z trybu edycji szkicu.







## Profil główny 

Profil główny jest tworzony przez [wyciągnięcie](PartDesign_Pad/pl.md) nowego szkicu.

**Sketch001**

<img alt="Fig. MP1" src=images/OffsetSketch001.png  style="width:240px;"> <img alt="Fig: MP2" src=images/Pd_tut_side_fc.png  style="width:240px;">

**Krok A: Utwórz szkic**

:   Kliknij <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md) i utwórz szkic dołączony do płaszcyzny **YZ_Plane**. FreeCAD przypisze nazwę **Szkic001**.

**Krok B: Dodaj geometrię**

1.  Kliknij <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Utwórz polilinię](Sketcher_CreatePolyline/pl.md) i utwórz kształt jak na **Rys: MP1**.
2.  Etykiety P1, P2 itd. nie pojawią się w szkicu. Zostały one dodane w celach informacyjnych.
3.  Dla ostatniego punktu końcowego odcinka upewnij się, że wybierasz pierwszy punkt kształtu. Punkt zmieni kolor i zobaczysz symbol <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [wiązania zbieżności](Sketcher_ConstrainCoincident/pl.md) w pobliżu kursora. Wiązania zbieżności muszą być jawne. Nie wystarczy, że dwa punkty pokrywają się wizualnie.
4.  Naciśnij klawisz **Esc** lub kliknij prawym przyciskiem myszy, aby opuścić narzędzie.

**Krok C: Przypisz wiązania**

1.  Trzy pionowe i poziome wiązania, które widzisz na obrazku, powinny zostać dodane automatycznie, o ile narysowałeś te linie w ten sposób. Jeśli tego nie zrobiłeś, musisz je dodać.
2.  Wybierz punkt **P2** oraz oś **Y** szkicu i zastosuj <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [wiązanie punktu na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Ponieważ szkic jest dołączony do YZ_Plane, oś Y szkicu nie pokrywa się z osią Y obiektu Zawartości.
3.  Wybierz *punkt odniesienia położenia* i punkt *P1* i zastosuj <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [wiązanie poziome](Sketcher_ConstrainHorizontal/pl.md). Możesz zapytać dlaczego nie <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md)?. Więc spróbuj *(i cofnij)*. Szkic zmieni kolor na pomarańczowy i pojawi się komunikat solvera **Wiązania nadmiarowe**. Ponieważ linia od P1 do P2 została już związana w pionie, jedynym pozostałym stopniem swobody jest współrzędna Y linii P1. Wiązanie zbieżności ustawia zarówno współrzędną X jak i Y na zero, ale współrzędna X jest już określona. Z kolei wiązanie poziome ustawia na zero tylko współrzędną Y, co jest wystarczające.
4.  Wybierz linię zdefiniowaną przez punkty **P2** i **P3**, zastosuj <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md), i przypisz jej **Długość = 5 mm**.
5.  Wybierz linię zdefiniowaną przez punkty **P1** i **P2**, zastosuj <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md), i przypisz jej **Długość = 26 mm**.
6.  Wybierz linię zdefiniowaną przez punkty **P1** i **P4** i zastosuj <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md):
    1.  Dla tej wartości użyjesz *wiązania z określeniem nazwy* za pomocą [wyrażeń](Expressions/pl.md).

Aby to zrobić, kliknij mały przycisk w polu tekstowym „Długość": <img alt="" src=images/Bound-expression.svg  style="width:24px;">.

1.  1.  Zostanie wyświetlone nowe okno dialogowe o nazwie „Edytor formuł" zawierające pole wprowadzania i etykietę „Wynik:", podobne do poniższego obrazka:
        ![](images/Pd_tut_expressions.png )
        Kiedy zaczniesz pisać w polu wejściowym, zobaczysz kilka automatycznych uzupełnień.
    2.  Wybierz etykietę szkicu. W naszym przypadku potrzebujemy **>.**. Zwróć uwagę na kropkę po etykiecie.
    3.  Aby wybrać **wiązanie z określeniem nazwy** \"szerokość\", należy najpierw wpisać **Constraints.** z kropką.

Tutaj działa automatyczne uzupełnianie.

1.  1.  Aby dodać \"szerokość\", automatyczne upełnianie nie jest jeszcze dostępne, więc wypełnij komórkę, aby przeczytać **>.Constraints.szerokość**. Jeśli wszystko poszło dobrze, czerwony komunikat o błędzie po **Wynik:** został zastąpiony poprawną wartością, jak na poniższym obrazku:
        ![](images/Pd_tut_expression_end.png )
    2.  Kliknij **OK**, aby zamknąć okno dialogowe **Edytor formuł**.
    3.  Kliknij **OK**, aby zamknąć okno dialogowe **Wstaw długość**.

2.  Powinieneś mieć w pełni związany szkic podobny do tego na **Rys.: MP2**.

3.  Zwróć uwagę na różne kolory używane dla wiązań odległości przypisywanych za pomocą wyrażeń oraz te przypisywane z podaniem długości.

**Krok D: Zamknij szkic**

:   Kliknij **Zamknij** u góry panelu [Zadań](Task_panel/pl.md), aby wyjść z trybu edycji szkicu.

**Wyciągnięcie**

<img alt="Fig: MP3" src=images/Pd_tut_pad1.png  style="width:240px;">

1.  Upewnij się, że wybrano **Sketch001**.
2.  Kliknij <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Wyciągnij](PartDesign_Pad/pl.md):
    1.  Otworzy się panel zadań **Parametry wyciągnięcia**.
    2.  Aby określić **Typ** wybierz {{ComboBox|Wymiar}}.
    3.  Dla okreśenia parametru **Długość** ponownie użyj wyrażenia, ale tym razem wpisz **>.Constraints.długość**. To powinno dać wynik 53 mm.
    4.  Zaznacz {{CheckBox|TRUE|Symetrcznie do płaszczyzny}}.
    5.  Kliknij **OK**, aby zamknąć panel zadań.
3.  Powinieneś teraz otrzymać bryłę jak pokazano na **Rys: MP3**.







## Wycięcia w narożnikach 

W przypadku wycięć narożnych do modelu dodawane są dwa elementy. Do utworzenia pierwszego wycięcia użyto funkcji [kieszeń](PartDesign_Pocket/pl.md), opartej na innym szkicu, a następnie cecha ta jest modyfikowana [odbiciem lustrzanym](PartDesign_Mirrored/pl.md).

**Sketch002**

<img alt="Fig: CC1" src=images/Pd_tut_sk2_start.png  style="width:300px;"> <img alt="Fig: CC2" src=images/Pd_tut_sk2_eg01.png  style="width:300px;"> <img alt="Fig: CC3" src=images/Pd_tut_sk2_end.png  style="width:300px;">

**Krok A: Ukryj bryłę**

:   Ukryj właśnie utworzoną bryłę: Wybierz obiekt **Pad** i kliknij klawisz **Spacja**.

**Krok B: Utwórz szkic**

:   Kliknij <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md) i utwórz szkic dołączony do płaszcyzny **XZ_Plane**. Szkic będzie nosił nazwę **Sketch002**.

**Krok C: Dodaj geometrię**

1.  Wybierz <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Utwórz prostokąt](Sketcher_CreateRectangle/pl.md), i narysuj prostokąt. Nie twórz go zbyt blisko osi, aby uniknąć wygenerowania automatycznych więzów, które utrudniałyby późniejsze przesunięcie go do właściwej pozycji.
2.  Zakończ pracę z narzędziem.

**Krok D: Przypisanie więzów wymiarowych**

1.  Wybierz jedną z poziomych linii, zastosuj <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md), i przypisz wartość **11 mm**.
2.  Wybierz jedną z pionowych linii, zastosuj <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md), i przypisz wartość **5 mm**.
3.  Powinieneś otrzymać rozwiązanie podobne jak na **Rys: CC1**.

**Krok E: Zamknij szkic**

:   Kliknij **Zamknij**. **Sketch002** na tym etapie nie jest w pełni związany.

**Krok F: Wyświetl poprzednie szkice**

:   Aby skorzystać z narzędzia [geometria zewnętrzna](Sketcher_External/pl.md), szkice, do których elementów chcemy się odwołać, muszą być widoczne. Upewnij się, że **Sketch** i **Sketch001** są widoczne. Użyj klawisza **Spacja** do przełączania widoczności w razie potrzeby. Rozwiń węzeł *Pad* w [Widoku drzewa](Tree_view/pl.md), aby uzyskać dostęp do obiektu*Sketch001*.

**Krok G: Dodaj geometrię zewnętrzną i w pełni zwiąż szkic**

1.  Kliknij dwukrotnie **Sketch002**, aby wejść w tryb edycji.
2.  Obróć widok tak, aby wyraźnie widzieć punkty, jak pokazano na **Rys: CC2**. Ułatwi to kolejne kroki. Zauważ, że początkowe położenie prostokąta może być inne w Twoim szkicu.
3.  Kliknij narzędzie <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Geometria zewnętrzna](Sketcher_External/pl.md).
4.  Podczas gdy narzędzie jest aktywne kursor ma następujący wygląd:
    ![](images/Pd_tut_eg_cursor.png )
5.  Wybierz punkt **P1** w **Rys: CC2**. Wybrany punkt zostaje dodany do szkicu jako geometria zewnętrzna. Będzie on wyświetlany w sekcji **Elementy** w panelu zadań z fioletową ikoną X lub, {{Version/pl|0.21}}, ikoną fioletowej kropki.
6.  Mając wciąż aktywne narzędzie wybierz punkt **P2** na **Rys: CC2**. Ta zewnętrzna geometria powinna również pojawić się w sekcji **Elementy**.
7.  Zakończ pracę z narzędziem.
8.  Wybierz punkt **P1** i punkt **P3** i zastosuj <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> [zwiąż odległość pionową](Sketcher_ConstrainVertical/pl.md). Prostokąt zostanie wyrównany do pozycji X punktu **P1**.
9.  Wybierz punkt **P2** i punkt **P3** i zastosuj <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [zwiąż odległość poziomą](Sketcher_ConstrainHorizontal/pl.md). Prostokąt zostanie wyrównany do pozycji Y **P2**.
10. Twój szkic powinien być w pełni związany, tak jak na **Rys. CC3**.

**Krok H: Zamknij szkic**

:   Kliknij **Zamknij**.

**Kieszeń**

<img alt="Fig: CC4" src=images/Pd_tut_pck01.png  style="width:300px;"> <img alt="Fig: CC5" src=images/Pd_tut_pck02-mir.png  style="width:300px;">

Do stworzenia wycięcia użyjemy narzędzia <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Kieszeń](PartDesign_Pocket/pl.md). Narzędzie to jest przeciwieństwem narzędzia Wyciągnij. Podczas gdy narzędzie Wyciągnij dodaje materiał, narzędzie Kieszeń usuwa materiał.

1.  Wybierz **Sketch002**.
2.  Kliknij <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Kieszeń](PartDesign_Pocket/pl.md):
    1.  Otworzy się panel zadań **Parametry kieszeni**.
    2.  Wybierz **Typ** {{ComboBox|Przez wszystkie}}.
    3.  Zaznacz opcję {{CheckBox|TRUE|Zaznaczony}}
    4.  Kliknij **OK**.
3.  Powinieneś uzyskać efekt przypominający ten z **Rys: CC4**

**Odbicie lustrzane**

Zamiast tworzyć kolejny szkic i kieszeń, wykorzystujemy symetrię modelu względem płaszczyzny YZ i użyjemy narzędzia <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [odbicie lustrzane](PartDesign_Mirrored/pl.md) do stworzenia drugiego wycięcia.

1.  Wybierz **Kieszeń**.
2.  Kliknij narzędzie <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [odbicie lustrzane](PartDesign_Mirrored/pl.md):
    1.  Otwiera się panel zadań **Parametry odbicia lustrzanego**.
    2.  Z menu rozwijanego wybierz **Płaszczyznę** {{ComboBox|Pionowa oś szkicu}}. Płaszczyzna zostanie zdefiniowana przez tę oś *(oś Y)*, a także przez oś Z szkicu. Zauważ, że wybranie **Płaszczyzny bazowej YZ** dałoby ten sam efekt.
    3.  Kliknij **OK**.
3.  Powinieneś mieć teraz część, która wygląda jak ta na **Rys: CC5**.







## Boki

Boki tworzymy w podobny sposób, ale zamiast usuwać materiał będziemy dodawać materiał za pomocą funkcji [wyciągnij](PartDesign_Pad/pl.md).

**Sketch003**

<img alt="Fig: SD1" src=images/Pd_tut_sk3_1.png  style="width:300px;"> <img alt="Fig: SD2" src=images/Pd_tut_pad001.png  style="width:300px;"> <img alt="Fig: SD3" src=images/Pd_tut_pad02-mir.png  style="width:300px;">

1.  Upewnij się, że **Szkic** jest widoczny, a obiekt **Mirrored** jest ukryty.
2.  Kliknij narzędzie <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [utwórz szkic](PartDesign_NewSketch/pl.md) i wygeneruj nowy szkic dołączony do płaszczyzny **XY_Plane**. Szkic będzie nosił nazwę **Sketch003**.
3.  Kliknij <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [utwórz prostokąt](Sketcher_CreateRectangle/pl.md) i utwórz prostokąt podobny do mniejszego prostokąta na **Rys: SD1**. Ponieważ prostokąt jest przesunięty względem osi X, nie powinno to wywołać automatycznego <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [dowiązania punktu na obiekcie](Sketcher_ConstrainPointOnObject/pl.md).
4.  Zamknij narzędzie.
5.  Kliknij narzędzie <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [geometria zewnętrzna](Sketcher_External/pl.md).
6.  Wybierz punkt **P1** jak pokazano na **Rys: CC2**.
7.  Zamknij narzędzie.
8.  Zastosuj następujące wiązania:
    1.  Wybierz jedną z poziomych linii, zastosuj narzędzie <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md), i przypisz wartość **7 mm**.
    2.  Wybierz jedną z pionowych linii, zastosuj narzędzie <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md) i przypisz to wyrażenie: **\<\>.Constraints.szerokosc**.
    3.  Wybierz punkt **lewy górny** utworzonego prostokąta *(oznaczony **TL** na **Rys.: SD1**)* i nowo dodany **punkt geometrii zewnętrznej** i zastosuj narzędzie <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md).
9.  Szkic powinien być teraz w pełni związany.
10. Kliknij **Zamknij**.

**Pad001**

1.  Wybierz **Sketch003**\'.
2.  Kliknij <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad.md):
    1.  Przypisz **Typ =** {{ComboBox|Wymiar}}.
    2.  Przypisz **Długość = 16.7 mm**.
    3.  Kliknij **OK**.
3.  Powinieneś uzyskać wynik jak pokazano na **Rys: SD2**.

**Mirrored001**

1.  Wybierz obiekt **Pad001**.
2.  Kliknij narzędzie<img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [odbicie lustrzane](PartDesign_Mirrored/pl.md):
    1.  Upewnij się, że **Płaszczyzna** {{ComboBox|Pionowa oś szkicu}} jest zaznaczona.
    2.  Kliknij **OK**.
3.  Powinieneś teraz mieć część, która wygląda jak na **Rys: SD3**.

**Uwaga**

Nasze dwie operacje odbicia lustrzanego mają wspólną płaszczyznę symetrii, więc moglibyśmy nieco uprościć nasz model łącząc je. W tym celu:

1.  Pomiń pierwszą operację **odbicia lustrzanego**.
2.  Wybierz zarówno **Pad001** jak i **Pocket** w kroku 1 powyższej operacji **Mirrored001**.

Podkreśla to ważną koncepcję, że odzwierciedlamy wybrane cechy *(operacje, które wykonaliśmy na bryle, w wybranej kolejności)*, a nie samą bryłę.







## Środkowy otwór 

Teraz czas na najtrudniejszą część naszego modelowania, wyzwanie, które pojawia się, ponieważ niektóre wymiary otworu centralnego są zdefiniowane wzdłuż skośnej ściany. Jeśli użyjesz tej ściany, powstałej w wyniku wyciągnięcia obiektu **Sketch001**, jako odniesienia dla następnego szkicu, narazisz się na [problem nazewnictwa topologicznego](Topological_naming_problem/pl.md). Lepszym rozwiązaniem jest odwołanie się do samego obiektu **Sketch001**.

**Sketch004**

<img alt="Fig: CH1" src=images/Pd_tut_cen01.png  style="width:240px;"> <img alt="Fig: CH2" src=images/Pd_tut_cen02.png  style="width:240px;">

1.  Spraw, aby **Sketch001** był widoczny, a ukryj **Sketch** i **Mirrored001**.
2.  Kliknij <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [utwórz szkic](PartDesign_NewSketch/pl.md) i utwórz nowy szkic dołączony do **YZ_Plane**. Szkic będzie nosił nazwę **Sketch004**.
3.  Kliknij <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [utwórz polilinie](Sketcher_CreatePolyline/pl.md) i wyznacz polilinię taką, jaką wskazują punkty **P1**, **P2**, **P3** i **P4** na **Rys: CH1**.
4.  Pamiętaj, aby zamknąć polilinię wybierając pierwszy punkt. Dzięki temu powstanie wymagane <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md).
5.  Zamknij narzędzie.
6.  Sprawdź zastosowane wiązania:
    -   Usuń zbędne <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> [więzy pionowe](Sketcher_ConstrainVertical/pl.md) zastosowane do linii zdefiniowanej przez **P1** i **P2**.
    -   Upewnij się, że <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [więz poziomy](Sketcher_ConstrainHorizontal/pl.md) został zastosowany do linii zdefiniowanych przez **P1** i **P4** oraz **P2** i **P3**.
    -   Upewnij się, że wiązanie <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [punktu na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) zostało zastosowane do **P1** i **osi Y** oraz do **P2** i **osi Y**.
7.  Kliknij narzędzie <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [geometria zewnętrzna](Sketcher_External/pl.md)
8.  Wybierz linię zdefiniowaną przez **EGP1** i **EGP2** w **Sketch001**, wskazaną przez fioletowy kolor na **Rys: CH2**.
9.  Zamknij narzędzie.
10. Zastosuj wiązanie <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) do **P3** i **geometrii zewnętrznej**, a następnie powtórz tę operację dla **P4**. To sprawi, że linia zdefiniowana przez **P3** i **P4** będzie pokrywać się z linią zdefiniowaną przez **EGP1** i **EGP2**.
11. Wybierz linię **P3** do **P4**, zastosuj <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [wiązanie odległości](Sketcher_ConstrainDistance/pl.md), i przypisz 
**Długość = 17 mm**
12. Wybierz punkty **EGP2** i **P4**, zastosuj <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [wiązanie odległości](Sketcher_ConstrainDistance/pl.md), i przypisz **Długość = 7 mm**.
13. W ten sposób powstanie w pełni związany szkic, taki jak na **Rys: CH2**.
14. Kliknij **Close**.
15. Ukryj **Sketch001**.

**Pocket001**

1.  Wybierz obiekt **Sketch004**.
2.  Kliknij <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [kieszeń](PartDesign_Pocket/pl.md):
    1.  Wybierz **Typ** {{ComboBox|Dwa wymiary}}.
    2.  Przypisz **8,5 mm** do **długości** i **drugiej długości**.
    3.  Kliknij **OK**.
3.  Wybierz nowo utworzony **Pocket001**.
4.  W zakładce Dane [Edytora właściwości](Property_editor/pl.md) zmień wartość właściwości **Ulepsz** na {{True/pl}}. Edytor właściwości znajduje się w zakładce Model w [Widoku złożonego](Combo_view/pl.md).

**Uwagi**

1.  Dla **Pocket001** mogliśmy alternatywnie użyć opcji **Typ** {{ComboBox|Wymiar}}, zaznaczyć **Symetrycznie do płaszczyzny** i wpisać wartość **17 mm** dla **Długości**.
2.  **Udoskonal** spróbuje usunąć szwy pozostawione przez poprzednie operacje. Zaleca się, aby dopracować tylko bryłę ostateczną, ponieważ niektóre operacje mogą się nie powieść, jeśli poprzednia cecha została dopracowana. Jednakże są też przypadki, w których funkcja ulepsz może sprawić, że operacja się powiedzie. Dlatego w razie problemów należy sprawdzić tę właściwość i przetestować. Niestety nie ma jeszcze ogólnej zasady, którą należałoby się kierować.







## Wynik

Model jest kompletny. Powinien wyglądać jak na poniższym obrazku.

Na koniec wybieramy **Szkic** w [Widoku Drzewa](Tree_view/pl.md) i na zakładce Dane w [Edytorze właściwości](Property_editor/pl.md) szukamy **Szkic → Wiązania**. Rozwiń ten węzeł i zmień wiązania **długość** i **szerokość**. Model powinien ulec zmianie parametrycznej.

![](images/Pd_tut_final_solid.png )


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Basic Part Design Tutorial 019/pl
