---
- TutorialInfo   */pl
   Topic   *Modelowanie
   Level   *Początkujący
   Author   *heda
   Time   *1.5 godziny
   FCVersion   *0.19 lub nowszy
   Files   *nie dołączono
   SeeAlso   *[Środowisko Część   * Tworzenie prostej części](Creating_a_simple_part_with_Part_WB/pl.md), [Tworzenie prostej części za pomocą środowiska pracy Rysunek Roboczy i Część](Creating_a_simple_part_with_PartDesign/pl.md)
---

# Creating a simple part with Draft and Part WB/pl





## Wprowadzenie

Ten poradnik ma na celu wykorzystanie go jako pierwsze wprowadzenie do środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) ![](images/Switch_DraftWorkbench.JPG ) w programie FreeCAD. Poradnik wykorzystuje *kształt 2D* do stworzenia *bryły 3D*, co jest realizowane za pomocą środowiska [Część](Part_Workbench/pl.md). Zaleca się, aby czytelnik najpierw zapoznał się z poradnikiem *[Środowisko Część   * Tworzenie prostej części](Creating_a_simple_part_with_Part_WB/pl.md)*, który tworzy ten sam model przy użyciu innej techniki, jednocześnie obejmując więcej podstaw interfejsu użytkownika programu FreeCAD. Ten poradnik oczekuje od użytkownika krótkiej znajomości zarówno interfejsu użytkownika jak i niektórych przepływów pracy dostępnych w FreeCAD. Poradnik jest tak skomponowany, że jego celem nie jest koniecznie pokazanie najbardziej efektywnego sposobu korzystania z programu, ale raczej uświadomienie czytelnikowi różnych funkcjonalności dostępnych w FreeCAD, jak z nich korzystać i gdzie je znaleźć.

### Przewodnik zawiera następujące zagadnienia 

-   Model do wykonania,
-   Tworzenie profilu 2D,
-   Dlaczego wyciąganie może się nie udać,
-   Wyciskanie profilu,
-   Tworzenie otworu przelotowego,
-   Tworzenie szkicu z profilu 2D,
-   Jakość modeli,
-   Zakończenie.

## Model do wykonania 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width   *372px;">

![](images/T101pwb01-02_dims.png )

## Tworzenie profilu 2D 

Utwórz nowy dokument i zapisz go odrazu pod nową nazwą. Zmień widok na <img alt="" src=images/Std_ViewTop.svg  style="width   *24px;"> [Od góry](Std_ViewTop/pl.md) i uruchom środowisko pracy <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), Twój ekran powinien wyglądać jak poniżej. Jeśli siatka nie jest widoczna, przełącz ją za pomocą przycisku <img alt="" src=images/Draft_ToggleGrid.svg  style="width   *24px;"> [Pokaż / ukryj siatkę](Draft_ToggleGrid/pl.md).

![](images/T101dwb01-01draftgrid.png )

Aby rozpocząć profil, narysuj dowolny <img alt="" src=images/Draft_Rectangle.svg  style="width   *24px;"> [Prostokąt](Draft_Rectangle/pl.md) na płaszczyźnie XY, klikając 2 punkty w oknie [widoku 3D](3D_view/pl.md) tworzące dowolną przekątną prostokąta. Po wywołaniu polecenia otworzy się *panel zadań*, tym razem nie będziemy z niego korzystać, ale możesz oczywiście bezpośrednio wprowadzić współrzędne prostokąta. Twój widok 3D powinien mieć teraz narysowany prostokąt, podobny do tego z poniższego obrazka.

![](images/T101dwb01-02rectangleraw.png )

Podczas pracy w środowisku *Rysunek Roboczy* prawie zawsze rysuje się na płaszczyźnie 2D. Ta płaszczyzna 2D nazywana jest *[Płaszczyzną roboczą](Draft_SelectPlane/pl.md)* i jeśli użyjemy ustawień domyślnych, zawsze automatycznie wyrówna się do aktualnego widoku 3D. Tak więc, dopóki profil 2D nie zostanie ukończony, najlepiej jest po prostu zachować widok Od góry (pozycję kamery) i nie bawić się w obracanie widoku. Jeśli zdarzyło Ci się go już przestawić, to przed rozpoczęciem jakiegokolwiek nowego polecenia w środowisku *Rysunek Roboczy* po prostu zmień z powrotem na widok Od góry.

Widok z boku naszego finalnego modelu ma zewnętrzny obrys 100 x 50 mm i dobrze by było, gdyby lewy dolny róg był umieszczony w globalnej pozycji zerowej. Można to osiągnąć poprzez *edytor właściwości*. Upewnij się, że utworzony *Prostokąt* jest zaznaczony, następnie zmień *Położenie* prostokąta na *(0, 0, 0)*, zmień *Wysokość* na {{Value|50mm}} i *Długość* na {{Value|100mm}} jak na poniższych obrazkach.

![](images/T101dwb01-03rectangleprops.png )

**Prostokąt** jest skończony i powinien wyglądać tak po zastosowaniu narzędzia <img alt="" src=images/Std_ViewFitAll.svg  style="width   *24px;"> [Dopasuj wszystko](Std_ViewFitAll/pl.md) do widoku.

![](images/T101dwb01-04rectangledone.png )

Następnie rozbijemy prostokąt na jego cztery krawędzie, zrobimy to wybierając najpierw **Prostokąt**, a następnie wywołując polecenie <img alt="" src=images/Draft_Downgrade.svg  style="width   *24px;"> [Rozbij kształt](Draft_Downgrade/pl.md), wypełnienie ściany zniknie, a obiekt w *Widoku drzewa* ma teraz nazwę **Wire** zamiast **Rectangle**, co widać na lewym obrazku poniżej. Ponowne wywołanie funkcji **Rozbij kształt** spowoduje rozbicie obiektu *Wire* na jego *Krawędzie*, co widać na środkowym obrazku poniżej.

![](images/T101dwb01-05rectangledowngrade.png )

Osoby spostrzegawcze zauważą, że ikona obiektu w widoku drzewa już dla krzywej łamanej zmieniła się na *niebieski sześcian*. Ten niebieski sześcian to ikona używana dla ogólnych obiektów geometrycznych *(konkretnie obiektów geometrycznych środowisku pracy Projekt Części, ale to dla zaawansowanych czytelników)*. Zaznacz lewą pionową krawędź i wywołaj polecenie <img alt="" src=images/Draft_Upgrade.svg  style="width   *24px;"> [Ulepsz kształt](Draft_Upgrade/pl.md), dawna *krawędź* będzie miała teraz inną ikonę i zmieniła *etykietę* na *Linia*. Jest to teraz obiekt środowiska *Rysunek Roboczy*, w którym można edytować na przykład *punkt początkowy* i *punkt końcowy* poprzez *Edytor właściwości*, nie jest to możliwe w przypadku obiektów *krawędzi*.

### Tworzenie zaokrąglenia 

Zacznij od zaznaczenia prawego górnego rogu krawędzi, użyj polecenia z menu **Edycja →  <img alt="" src=images/)_[Zaznacz_obszar](Std_BoxSelection/pl.md)**, przytrzymaj ![](images/Mouse_LMB.svg  style="width   *24px;"> **Lewy Przycisk Myszy** *(Left Mouse Button)* i przeciągnij **od prawej do lewej**, a następnie zwolnij **LMB**. Podczas przeciągania *od prawej do lewej* wynikowy wybór obejmuje wszystko w całości lub częściowo w obszarze zaznaczenia. Przy przeciąganiu *od lewej do prawej*, w wynikowym zaznaczeniu znajdują się tylko obiekty w całości objęte obszarem zaznaczenia. Faktyczne zaznaczenie następuje po zwolnieniu lewego przycisku myszy i nie ma możliwości podglądu tego, co zostanie zaznaczone.

![](images/T101dwb02-01filletboxselection.png )

Mając zaznaczone krawędzie w prawym górnym rogu, wywołaj polecenie <img alt="" src=images/Draft_Fillet.svg  style="width   *24px;"> [Zaokrąglenie](Draft_Fillet/pl.md) w środowisku pracy **Rysunek Roboczy**. Zaznacz *Usuń oryginalne obiekty* i zmień wartość parametru *promień* na {{Value|20 mm}} i naciśnij klawisz **Enter**.

![](images/T101dwb02-02fillettaskpanel.png )

**Zaokrąglenie** zostało utworzone, a twój model powinien teraz wyglądać jak poniżej   *

![](images/T101dwb02-03filletdone.png )

### Tworzenie sfazowania 

Aby wykonać *fazkę* musimy mieć linię o odpowiednim nachyleniu, a także umieć ją ustawić w odpowiednim miejscu. Zacznijmy od pozycji, która znajduje się na współrzędnej *(50, 50, 0)*. W obecnym profilu nie mamy tam punktu, więc stwórzmy go poprzez wykonanie *tymczasowej linii pomocniczej*. Najpierw wybierz lewą pionową **Linię**, następnie utwórz linię pomocniczą narzędziem <img alt="" src=images/Std_DuplicateSelection.svg  style="width   *24px;"> [Powiel zaznaczone](Std_DuplicateSelection/pl.md) z menu **Edycja → Powiel zaznaczone**, zostanie utworzony obiekt **Linia001**. Użyj *Edytora właściwości* i przesuń *Linię001* o {{Value|50 mm}} w kierunku X, używając właściwości *Umiejscowienie*. Następnie powielamy *dolną krawędź poziomą* i zmieniamy *kąt* krawędzi na {{Value|30 stopni}}, ponownie używając właściwości *Umiejscowienie*. Model powinien teraz wyglądać jak na poniższym obrazku.

![](images/T101dwb03-01chamferhelp.png )

Następnie należy przesunąć *skośną linię* na właściwą pozycję. W tym celu użyjemy narzędzia <img alt="" src=images/Draft_Move.svg  style="width   *24px;"> [Przesuń](Draft_Move/pl.md) wraz z funkcją *przyciągania* w środowisku pracy **Rysunek Roboczy**, a dokładniej przyciągania *punktu końcowego*. Najpierw upewnij się, że twój pasek narzędzi przyciągania wygląda jak poniżej.

![](images/T101pwb03-02_snap.png )

Następnie wybierz *linię skośną*, obiekt *Krawędź001*, naciśnij *Przesuń* i otworzy się *panel zadań*.

![](images/T101dwb03-03_movetaskpanel.png )

Upewnij się, że opcja *Kopiuj* jest odznaczona. Najedź kursorem myszki na *górną ćwiartkę* linii pomocniczej, gdy w odpowiednim miejscu pojawi się *biała kropka* i pokaże się symbol *punktu końcowego*, kliknij <img alt="" src=images/Mouse_LMB.svg  style="width   *24px;"> **LMB**. Przesuń kursor myszki do górnej ćwiartki linii pomocy, gdy pojawi się biała kropka i symbol punktu końcowego, kliknij **LMB**. Sekwencja jest zilustrowana poniżej.

![](images/T101dwb03-04_moveline.png )

Linia znajduje się teraz we właściwej pozycji, ale jest zbyt długa. Aby dostosować długość użyjemy narzędzia <img alt="" src=images/Draft_Trimex.svg  style="width   *24px;"> [Przytnij](Draft_Trimex/pl.md). Wybierz *skośną linię*, **Krawędź001**, naciśnij przycisk Przytnij, a następnie kliknij dolną część *najbardziej lewej pionowej linii*, obiektu **Linia**, aby użyć jej jako krawędzi cięcia. Rzut punktu, w którym wybrano krawędź cięcia na krawędź, która ma zostać wycięta, określa wynik. Jeśli wybierzesz najbardziej lewą pionową linię w pobliżu jej górnego końca, niewłaściwa część skośnej linii zostanie przycięta. Poniższy obrazek pokazuje wywołane polecenie **Przytnij**, wybraną wcześniej linię pionową oraz kursor znajdujący się nad niewłaściwym końcem tej linii. Jeśli przyjrzysz się uważnie, możesz zobaczyć podgląd wyniku.

![](images/T101dwb03-05_trimline.png )

Przytnij również najbardziej lewą pionową linię, aby utworzyć dolny róg fazy. Wybierz *skośną linię*, obiekt **Krawędź001**, blisko jej prawego górnego punktu końcowego, aby uzyskać prawidłowy rezultat. Jeśli popełnisz błąd podczas przycinania, po prostu użyj przycisku <img alt="" src=images/Std_Undo.svg  style="width   *24px;"> [Cofnij](Std_Undo/pl.md) oraz <img alt="" src=images/Std_Refresh.svg  style="width   *24px;"> [Odświerz](Std_Refresh/pl.md) *(ten ostatni często nazywany jest*przelicz*)* i spróbuj ponownie.

![](images/T101dwb03-06_chamferlowercornerdone.png )

Aby przyciąć *górną krawędź poziomą*, należy *rozbić kształt* **zaokrąglenia**, tak aby górna krawędź była własnym obiektem w widoku drzewa. Jeśli spróbujesz ją przyciąć bez uprzedniego rozbicia kształtu, funkcja przycinania spróbuje przyciąć łuk w zaokrągleniu. Ponieważ krawędź przycinania, *środkowa linia pionowa*, jest prostopadła do przycinanej krawędzi, nie można kontrolować wyniku przycinania, wybierając odpowiedni punkt na krawędzi przycinania. Tutaj musisz odwrócić domyślne rozwiązanie poprzez przytrzymanie klawisza **Alt** podczas wybierania krawędzi cięcia.

Profil jest gotowy i pokazany poniżej z krawędziami zorganizowanymi w <img alt="" src=images/Std_Group.svg  style="width   *24px;"> [Grupy](Std_Group/pl.md) o nazwie **Profil** *(lub **etykietowany**, aby być precyzyjnym w lingwistyce FreeCAD)*, wraz z usuniętą linią pomocniczą. Grupy mogą być używane do porządkowania cech w Twoich *dokumentach FreeCAD*, ich użycie jest podobne do struktury folderów w systemie plików komputera. Aby przenieść obiekty do i z grupy, użyj funkcjonalności*przeciągnij i upuść* w widoku drzewa.

![](images/T101dwb03-07_profiledone.png )

## Dlaczego wyciągnięcie może się nie udać 

Zapisz dokument. W tym akapicie będziemy eksperymentować i chcemy mieć możliwość powrotu do aktualnego modelu.

Zacznijmy bez zwłoki   * zaznacz wszystkie krawędzie w *grupie* **Profil**, a w środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Część](Part_Workbench/pl.md) wywołujemy polecenie <img alt="" src=images/Part_Extrude.svg  style="width   *24px;"> [Wyciągnięcie \...](Part_Extrude/pl.md). Otworzy się *panel zadań*, zaakceptuj wszystkie domyślne ustawienia i kliknij **OK**.

![](images/T101dwb04-01_extrudelineserror.png )

To nie zadziałało, ale brzmi wystarczająco łatwo, aby naprawić błąd, musimy tylko określić kierunek. Kliknij **OK**, aby wrócić do *panelu zadań* i wybierz *niestandardowy kierunek*.

![](images/T101dwb04-02_extrudelineszaxis.png )

Zaakceptuj domyślną oś z i jeszcze raz kliknij **OK**.

![](images/T101dwb04-03_extrudelinessheets.png )

Udało nam się zrobić strukturę przypominającą ogrodzenie, sądząc po widoku drzewa każda krawędź jest traktowana oddzielnie. To nie jest wypełniona bryła, o którą nam chodzi. Naciśnij [Cofnij](Std_Undo/pl.md), i spróbujmy czegoś innego.

Przewijając do samego dołu okna **Wyciągnięcia** *panelu zadań* znajduje się opcja *Utwórz bryłę*, zaznacz tę opcję i kliknij **OK**.

![](images/T101dwb04-04_extrudelinesfilled.png )

Wszystko zniknęło, widocznie to też nie zadziałało. Prześledźmy, dlaczego żaden z tych sposobów nie działa. W pierwszym przypadku dostaliśmy błąd, że nie można określić kierunku. Płaska ściana ma normalną, czyli kierunek, linia nie. Ponieważ z naszej drugiej próby wiemy, że działało to przy podaniu kierunku, błąd wynika po prostu z próby wyciągnięcia linii bez znajomości kierunku. Spostrzegawczy powiedzą, że łuk ma normalną *(kierunek)*, jest to prawda. Jeśli wybierzemy tylko krawędź będącą łukiem, FreeCAD dokona wyciągnięcia, również z domyślnymi ustawieniami.

W drugim przypadku zadziałało, ale otrzymaliśmy również wytłoczenie dla każdej krawędzi, którą mieliśmy w naszym wyborze. Wynikowe cechy jednak nie są tym, czego oczekujemy, czyli bryłą.

W trzecim przypadku zaznaczyliśmy opcję *Utwórz bryłę* i skończyło się na tym, że wszystko zniknęło. Obiekty w widoku drzewa mają też inną ikonę, jest to *biały wykrzyknik* na czerwonym tle, ta konkretna *ikona nakładki* oznacza, że obiekt ma błąd, który trzeba naprawić. O różnych typach [ikonek](Tree_view/pl#Ikonki_dodatk.C3.B3w.md) można poczytać na wiki.

Po najechaniu kursorem na dowolny obiekt w widoku drzewa z ikoną nakładki wyświetlana jest podpowiedź z napisem *Polilinia nie jest zamknięta*.

![](images/T101dwb04-05_extrudelineserrortooltip.png )

W naszym przypadku błąd jest nie do naprawienia. Utworzenie bryły z wyciągnięcia pojedynczej linii jest *geometrycznie niemożliwe*. Wytłoczona linia staje się po prostu arkuszem, lub *powłoką* w języku FreeCAD. Innymi słowy, nie jest to ograniczenie programu FreeCAD, jest to podstawowy wynik teorii geometrii. Powodem, dla którego widok 3D jest całkowicie pusty jest to, że utworzone cechy, lub obiekty w widoku drzewa, mają błędy w wytworzonym *kształcie*, a więc nie zawierają nic do renderowania. FreeCAD tworzy jednak nowe obiekty dokumentu *(w tym przypadku wyciągania)* i dlatego ukrywa wszelkie geometrie/obiekty użyte do tworzenia nowych obiektów dokumentu. To dlatego ekran jest pusty, gdy próbujemy stworzyć bryłę z linii lub wielu linii.

Wskazówka narzędzia mówi wszystko, aby wykonać wyciągnięcie w bryłę potrzebujemy zamkniętej polilinii, czyli ściany. Ściana jest z definicji po prostu zamkniętą linią łamaną, która została wypełniona. Jednym ze sposobów na stworzenie zamkniętej linii z naszych krawędzi profilu jest wybranie ich wszystkich i zastosowanie funkcji <img alt="" src=images/Draft_Upgrade.svg  style="width   *24px;"> [Ulepsz](Draft_Upgrade/pl.md). Jeśli zostanie zastosowana raz, obiekt stanie się polilinią, jednocześnie zużywając poszczególne krawędzie z widoku drzewa. Jeśli zastosowany dwukrotnie staje się ścianą, każdy z tych obiektów pozwala na przeprowadzenie udanego wytłoczenia bryły.

Przed przejściem do kolejnego akapitu   * otwórz poprzednio zapisaną wersję dokumentu.

## Wyciąganie profilu 

Innym sposobem na stworzenie zamkniętej lini jest użycie polecenia <img alt="" src=images/Part_Builder.svg  style="width   *24px;"> [Konstruktor kształtu \...](Part_Builder/pl.md) ze środowiska Część, które pozwala na stworzenie polilinii bez zużywania poszczególnych krawędzi. **Konstruktor kształtu** środowiska Część jest potężnym narzędziem do tworzenia dowolnych brył geometrycznych w FreeCAD, które mogą być wykorzystane dalej do tworzenia złożonych brył, najprostszym przykładem jest utworzenie linii pomiędzy dwoma wierzchołkami. Kliknij **Konstruktor kształtu \...** aby wywołać *panel zadań*.

![](images/T101dwb05-01_shapebuildertaskpanel.png )

Możemy użyć opcji *Polilinia z krawędzi* albo *Ściana z krawędzi*. Wielokrotnego wyboru krawędzi należy dokonać z wciśniętym klawiszem **Ctrl**. Użyjmy opcji *Ściana z krawędzi*, po wybraniu tej opcji można również wybrać *Płaski\', zrób to również. Następnie zaznacz wszystkie krawędzie w profilu, kolejność nie ma znaczenia*(w tym przypadku)\'\' i kliknij na przycisk **Utwórz**, a następnie **Zamknij**, aby wrócić do widoku drzewa. Ściana została utworzona.

![](images/T101dwb05-02_shapebuilderfacedone.png )

Wybierz **Ścianę** i wywołaj funkcję **Wyciągnij \...**, ustaw wartość długości wyciągnięcia na {{Value|30 mm}} i kliknij w **OK**.

![](images/T101dwb05-03_extrusiondone.png )

## Tworzenie otworu przelotowego 

Aby wykonać otwór przelotowy potrzebujemy *walca* prawidłowo *ustawionego*, z którym wykonamy operacje logicznego *wycięcia*.

Utwórz walec i umieść go w odpowiedniej pozycji. W tym przypadku *promień* wynosi {{Value|5 mm}}, a *wysokość* {{Value|60}} mm. Aby go umieścić, najpierw obracamy go o {{Value|90 stopni}} wokół osi X, a następnie ustawiamy w punkcie *(65, -5, 15)*. Ujemna wartość 5 w kierunku y wynika z tego, że wysokość jest o 10 mm większa niż potrzeba.

![](images/T101dwb05-04_cylinderplaced.png )

Nie zaszkodzi zrobić wysokość walca dłuższą niż jest to konieczne. Dla tak prostego modelu nie będzie miało znaczenia, czy walec ma dokładną wysokość profilu. Dobrą praktyką jest jednak unikanie współpłaszczyznowych ścian, aby zapobiec błędom numerycznym w jądrze geometrycznym, które czasami mogą skutkować dziwnymi efektami, lub niepowodzeniami w kolejnych operacjach.

Po wykonaniu ostatecznej operacji wycięcia logicznego, oraz po zmianie wyglądu powstałego obiektu, model jest zakończony.

![](images/T101dwb05-05_modelcomplete.png )

## Tworzenie szkicu z profilu 2D 

Korzystanie ze środowiska pracy **Rysunek Roboczy** jest jednym ze sposobów tworzenia profilu 2D. W środowisku **Rysunek Roboczy** polilinia może być wykonana w przestrzeni 3D. FreeCAD dostarcza innego narzędzia do tworzenia profili 2D - jest nim środowisko pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Szkicownik](Sketcher_Workbench/pl.md). Używanie *szkicu* jest bardziej uniwersalnym sposobem tworzenia profilu 2D. Każdy profil 2D wykonany w środowisku **Rysunek Roboczy** może zostać przekształcony w **niezwiązany** szkic.

Zacznij od ukrycia cechy **Wycięcie** i spraw, aby krawędzie w profilu były widoczne. Zaznacz krawędzie i w środowisku **Rysunek Roboczy** naciśnij przycisk paska narzędzi <img alt="" src=images/Draft_Draft2Sketch.svg  style="width   *24px;"> [Rysunek Roboczy do szkicu](Draft_Draft2Sketch/pl.md). Powinieneś zobaczyć to samo, co na poniższym obrazku   *

![](images/T101dwb06-01_draft2sketch.png )

Następnie należy ukryć oryginalne krawędzie i dwukrotnie kliknąć obiekt **Szkic** w widoku drzewa, co spowoduje przejście do następującego stanu, czyli otwarcia panelu zadań *Szkicownika*.

![](images/T101dwb06-02_sketchedit.png )

Tak to wygląda, gdy ktoś *edytuje szkic*. Ponieważ nie jest to poradnik dotyczący używania Szkicownika, po prostu przejdź dalej i zamknij go. Jeśli chcesz poznać zasady szkicowania, które jest podstawą pracy w każdym parametrycznym CAD 3D, skorzystaj z siostrzanego poradnika *[Projekt Części   * tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md)*.

Mając zamknięty szkicownik i wybrany obiekt *Szkic*, w środowisku pracy **Część** użyj funkcji Wyciągnij w taki sam sposób jak poprzednio. Podstawowy blok prostego modelu jest ponownie gotowy.

![](images/T101dwb06-03_sketchextruded.png )

## Jakość modelu 

Pracując z parametrycznym CAD 3D prędzej czy później natkniesz się na uszkodzony model, czy to wykonany samodzielnie, czy też zaimportowany. Zepsuty model może działać zgodnie ze swoim przeznaczeniem, ale częściej zdarzają się kolejne operacje, które po prostu nie będą działać. Aby naprawić uszkodzony model trzeba wiedzieć co naprawić, w tym miejscu z pomocą przychodzą wbudowane w FreeCAD narzędzia do sprawdzania jakości.

Najpierw sprawdźmy jakość niedawno utworzonego obiektu **Extrude001**. Mając aktywne środowisko pracy **Część**, najpierw wybierz **Extrude001**, a następnie użyj polecenia <img alt="" src=images/Part_CheckGeometry.svg  style="width   *24px;"> [Sprawdź geometrię](Part_CheckGeometry/pl.md). Zaznacz wszystkie pola wyboru ustawień oprócz górnego i kliknij przycisk **Uruchom sprawdzanie**.

![](images/T101dwb07-01_geocheck.png )

Nasz model jest OK, nie są zgłaszane żadne błędy. Jest tam również lista zawartości modelu, czyli w języku FreeCAD zawartość *kształtu*, która mówi jak jest on złożony od podstaw. Widać tu, że najwyraźniej do stworzenia bryły potrzebna jest jeszcze *powłoka*, która składa się ze *ścian* itd. Innymi słowy, można utworzyć dowolną bryłę zaczynając od punktów, czyli *wierzchołków*, z nich tworzy się *krawędzie*, z nich tworzy się *polilinie*, a z polilinii tworzy się *ściany*. Te następnie zszywa się w *powłokę*, z której w ostatecznie otrzymuje się *bryłę*. Bryła może powstać tylko z wodoszczelnej powłoki. Nieszczelna powłoka jest częstym źródłem kłopotów w modelach CAD, może się to zdarzyć np. w przypadku importu geometrii stworzonej w innym programie, zwłaszcza gdy używamy powszechnie dostępnych uniwersalnych formatów plików.

Kolejne sprawdzenie, jakie można wykonać, jest związane ze **szkicem**. Zamknij *panel zadań* dla sprawdzania geometrii. Wybierz obiekt **Szkic**, rozwiń obiekt *Extrude001* w widoku drzewa, jeśli to konieczne, aby zobaczyć obiekt szkicu. Przełącz się do środowiska pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Szkicownik](Sketcher_Workbench/pl.md), użyj polecenia <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width   *24px;"> [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md), otworzy się *panel zadań*. W *panelu zadań* kliknij przycisk **Znajdź** dla *Brakujących wiązań*. Podświetla on i zgłasza *6* z nich, czyli wszystkie punkty, w których spotykają się krawędzie.

![](images/T101dwb07-02_sketchvalidate.png )

Kliknij przycisk **OK** w wyskakującym oknie dialogowym, a następnie kliknij przycisk **Napraw**, aby uzdrowić *Brakujące zbieżności*. Jeśli zamkniesz *panel zadań*, i przejdziesz do *trybu edycji* **Szkicu**, zgłosi on *12 stopni swobody*, w przeciwieństwie do wcześniejszych *24*. Zostało to osiągnięte poprzez dodanie *zbieżnych wiązań* do punktów końcowych krawędzi.

Uważny czytelnik zauważy, że podczas używania krawędzi ze środowiska pracy Rysunek Roboczy te musiały być połączone w zamkniętą łamaną, aby stworzyć wyciągnięcie bryły, podczas gdy w Szkicowniku nie było to najwyraźniej potrzebne. Logika jest taka, że szkic jest jednym obiektem, a wyciągnięcie jednego obiektu jest traktowane tak, jakby było zamkniętą łamaną *(w tym przypadku)*.

Na koniec warto zaznaczyć, że choć tworzenie kolejnych obiektów ze szkiców z *otwartymi wierzchołkami* może działać, to najlepszą praktyką jest *nie mieć żadnych*, jak również mieć *w pełni związany szkic* *(w przeciwieństwie do szkicu z niepełnym związaniem)*. Powodem, dla którego to działa jest to, że *szkic* jest tworzony z profilu Rysunku Roboczego skonstruowanego w taki sposób, że punkty końcowe krawędzi pasują do siebie bez żadnych przerw. Jeśli narysujesz ręcznie szkic i również spróbujesz dopasować punkty końcowe ręcznie, jest praktycznie gwarantowane, że punkty końcowe nie będą pasować, tj. luki *(chociaż nie są naprawdę widoczne na ekranie)* będą na tyle duże, że jądro geometryczne nie może uznać krawędzi za geometrycznie połączone.

## Zakończenie

Po zakończeniu tego poradnika zapoznałeś się z podstawową funkcjonalnością programu FreeCAD, wraz z podstawowymi środowiskami pracy *Część* i *Rysunek Roboczy*. Jesteś również świadomy istnienia środowiska pracy **Szkicownik**, które dla wielu doświadczonych użytkowników jest jedynym narzędziem używanym do tworzenia profili 2D wykorzystywanych później w operacjach na elementach bryłowych. Używanie *szkiców* jest podstawową koncepcją środowiska **Projekt Części**. Sugeruje się, abyś nauczył się *szkiców* i środowiska *Projekt Części* w następnej kolejności, jeśli skupiasz się na tworzeniu brył. Siostrzany poradnik *[Projekt Części   * tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md)* tworzy ten sam model. Jeśli skupiasz się na modelowaniu budynków, powinieneś zapoznać się ze środowiskami pracy roboczymi **Rysunek Roboczy** i **Architektura**.

W końcu FreeCAD jest tworzony przez wolontariuszy w ich wolnym czasie. Jeśli chcesz dalej rozwijać możliwości programu, rozważ [pomoc w rozwoju FreeCAD](Help_FreeCAD/pl.md), na przykład poprzez poprawę dokumentacji.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Creating a simple part with Draft and Part WB/pl
