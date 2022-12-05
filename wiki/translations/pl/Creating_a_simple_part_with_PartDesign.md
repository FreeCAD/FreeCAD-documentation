---
- TutorialInfo:/pl
   Topic:Modelowanie
   Level:Początkujący
   Author:GlouGlou
   Time:1 godzina
   FCVersion:0.17 lub nowszy
   Files:nie dołączono
   SeeAlso:[Projekt Części: Tworzenie prostej części](Creating_a_simple_part_with_Part_WB/pl.md), [Tworzenie prostej części za pomocą środowiska pracy Rysunek Roboczy i Część](Creating_a_simple_part_with_Draft_and_Part_WB/pl.md)
---

# Creating a simple part with PartDesign/pl





![](images/GGTuto1_Vue.PNG )

Ten samouczek ma na celu nauczenie początkujących użytkowników FreeCAD kilku podstawowych funkcji, na przykładzie. Po omówieniu podstaw w [Centrum użytkownika](User_hub/pl.md), będziesz mógł modelować pierwszą część krok po kroku.

**W tym Poradniku omówimy w szczegółach:**

-   Używanie [Środowiska pracy Projekt Części](PartDesign_Workbench/pl.md), rysowanie szkicu.
-   Używanie funkcji wyciągnięcia *(Pad)* i kieszeni *(Pocket)*.
-   Zmiana koloru i przezroczystości.
-   Ręczne przenoszenie części.
-   Wyświetlanie przypisanych wymiarów w szkicu.
-   Edycja jednego lub wielu wymiarów.
-   Korzystanie z funkcji geometrii zewnętrznej i użycie płaszczyzny odniesienia do wyśrodkowania otworu.

### Używanie [Środowiska pracy Projekt Części](PartDesign_Workbench/pl.md), rysowanie szkicu 

Stwórz nowy dokument i wybierz Środowisko pracy **[<img src=images/Workbench_PartDesign.svg style="width:24px"> '''Projekt Części'''** używając [okienka wyboru](Getting_started/pl#Poznawaj_interfejs_użytkownika.md) *(numer 10 na obrazku)* lub przez menu *Widok → Środowiska pracy*. FreeCAD uruchamia się z paskami narzędzi u góry, \"widokiem łączonym\" po lewej, i widokiem 3d po prawej.

**Tworzenie nowej zawartości (body):**

Wciśnij przycisk <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Stwórz nową zawartość i ustaw ją jako aktywną](PartDesign_Body/pl.md). ***Uwaga:**nie pomyl tej ikony która jest niebieska, z ikoną od Part Container która jest żółta.*. W zakładce*\'Model** pod paskiem bocznym z widokiem łączonym pojawi się nowy obiekt nazwany **Body**. Pojawi się on pod nazwą dokumentu, która jest \"Nienazwany\" do czasu aż dokument nie zostanie zapisany. Zawartość jest pojemnikiem / kontenerem, w którym elementy środowiska Projekt Części są kolejno rozmieszczane w celu utworzenia pojedynczej bryły. Zawiera własne osie odniesienia i płaszczyzny. Zostanie oznaczony na niebiesko w drzewie modelu, co oznacza że jest aktywna, czyli możemy edytować elementy które zawiera jak również dodawać nowe elementy do niej. Jeśli nie jest podświetlona na niebiesko, kliknij na nią dwukrotnie, lub wciśnij prawy przycisk myszy i w menu kontekstowym wybierz opcję **Przełącz na aktywną zawartość**. Przed nazwą \"Body\" znajduje się niebieska ikona identyczna z tą, za pomocą której stworzyłeś obiekt \"Body\". Klikając w strzałkę lub znak plusa znajdujący się przed \"Body\" możesz rozwinąć jego zawartość. W tej chwili zawiera on jedynie element nazwany **Odniesienie położenia***(origin)\'\'. Przed**odniesieniem położenia\'\'\' także znajduje się znak strzałki lub plusa. Kliknij na niego aby rozwinąć jego zawartość. Odsłania to wyżej wymienione osie i płaszczyzny odniesienia, jak pokazano na poniższym obrazku:

![](images/PartDesign_Body_tree_Unnamed.png ) *Nowo stworzone aktywne \"Body\" z jego zawartością* Odniesienie połóżenia *(Origin)* jest niedostępne, co oznacza, że jego zawartość nie jest widoczna w oknie widoku 3D. Możesz przełączyć jego widoczność w widoku 3D zaznaczając obiekt Origin i wciskając spacje na klawiaturze. \"Origin\" teraz będzie oznaczone na czarno na drzewie. Wciśnij spacje ponownie aby ukryć \"Origin\" w widoku 3D. Naciśnij ponownie na klawisz strzałki lub znak plusa przed \"Origin\" aby zwinąć jego zawartość.

Zanim będziemy kontynuować, skorzystajmy z okazji do zmiany nazwy Body.

**Zmiana nazwy \"Zawartości\" (Body):**

Na drzewie modelu kliknij prawym przyciskiem myszki na Body. Wybierz Zmień nazwę i wpisz nazwę, na przykład \"Body part1\" i naciśnij **Enter**, aby potwierdzić.

**Tworzenie szkicu:**

Teraz będziemy zajmować się szkicem, określającym ogólny kształt części. Szkic jest rysunkiem opisującym profil, który należy zastosować dla elementu w celu uzyskania kształtu. Może być albo \"dodatni\" lub \" dodawany\", jak np. wyciągnięcie; albo \"ujemny\" lub \"odejmowalny\", jak kieszeń.

Ponieważ w tym przypadku ogólny kształt części jest regularny wzdłuż osi Y, stworzymy wyciągnięcie wzdłuż tej osi.

Wciśnij przycisk <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Utwórz nowy szkic](Sketcher_NewSketch/pl.md). Okienko widok połączony przełącza się teraz na zakładkę **Zadania** i wyświetla okno dialogowe **Wybierz funkcję**. To okno dialogowe oczekuje wyboru płaszczyzny, do której ma zostać dołączony nasz szkic i wyświetla listę dostępnych płaszczyzn. Wybierz *XZ_Plane (płaszczyzna podstawowa)*\' i naciśnij **OK**. Interfejs teraz się zmienia, Szkicownik przejmuje kontrolę, a jego paski narzędzi pojawiają się nad widokiem okna 3D. Znajdujemy się na płaszczyźnie XZ bryły, aby można było utworzyć szkic.

Aby ułatwić szkicowanie, można ustawić następujące opcje w polu **Edycja elementów sterujących** w panelu Zadania po lewej stronie:

-   Pokaż siatkę: zaznaczone.
-   Rozmiar siatki: 10 mm.
-   Automatyczne wiązania: zaznaczone.

Narysujemy poniższy szkic:

![](images/GGTuto1_0.PNG )

**Zacznijmy od pierwszego segmentu:**

Wybierz narzędzie <img alt="" src=images/Sketcher_Line.svg  style="width:24px;">[Utwórz linię na szkicu](Sketcher_CreateLine/pl.md). Kliknij na punkt początkowy, upewniając się najpierw, że obok i po prawej stronie kursora myszy pojawi się mała czerwona kropka. Kliknij następnie na oś X około 10 kwadratów w prawo lub około 100mm. Jeśli odcinek nie ma dokładnie 100 m w tym miejscu, nie ma to znaczenia, później nadamy mu stały wymiar, który będzie limitował tę długość.

Zrób to samo dla innych segmentów, spróbuj wycelować w punkty, które stworzyłeś i które muszą się rozjaśnić na żółto. Co oznacza, że punkty te będą zbieżne. Powinieneś otrzymać praktycznie tyle:

![](images/GGTuto1_1.PNG )

Zwróć uwagę na małe czerwone linie powyżej i obok narysowanych odcinków: są to ograniczenia poziome i pionowe. Twoje linie są zmuszone do pozostania w pozycji poziomej lub pionowej. Zauważ również symbol w postaci małego łuku po lewej stronie: oznacza to, że punkt jest przyczepiony do osi Z.

Teraz wybierz różne segmenty linii lewym przyciskiem myszy i trzymając wciśnięty lewy przycisk myszy, przeciągnij myszką, aby spróbować je przesunąć: niektóre są swobodne, inne nie.

**Nakładanie wiązań:**

W górnej części pola wyboru, w panelu Zadania, można odczytać liczbę stopni swobody już naszkicowanych elementów: musi to być około 6, celem ograniczeń jest zmniejszenie liczby stopni swobody do zera.

Skośna linia powinna się teraz swobodnie obracać: będziemy ją wiązać kątowo.

Kliknij na linię ukośną, następnie linię u dołu. Po wybraniu tych linii ich kolor zmieni na ciemnozielony. Następnie kliknij przycisk <img alt="" src=images/Constraint_InternalAngle.svg  style="width:24px;"> [Ustaw kąt linii](Sketcher_ConstrainAngle/pl.md).

![](images/GGTuto1_2.PNG )

Wpisz wartość 30°. Obie linie mają teraz sztywny wybrany przez nas kąt. Wiązanie zostało stworzone po lewej stronie szkicu. Za pomocą myszki przesuń stworzone ograniczenie do wewnątrz szkicu.

Teraz zwiążemy dolną linie konkretnym wymiarem. Wybierz tą linie i kliknij <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:24px;"> [Ustal poziomą odległość](Sketcher_ConstrainDistanceX.md).

Wpisz wartość 100mm. Pionowa linia po prawej stronie wyrównuje się teraz dokładnie z dziesiątym kwadratem siatki po prawej stronie.od jej początku.

Ustawmy całkowitą wysokość profilu, wybierając najwyższy punkt po lewej stronie, potem punkt początkowy. Kliknij na <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:24px;"> [Ustal pionową odległość](Sketcher_ConstrainDistanceY.md), wprowadź wartość 50mm.

Czynności te należy powtórzyć dla poziomej długości pochylonej linii z dodatkowym ograniczeniem odległości poziomej 50 mm.

Odsuń wymiary od profilu, aby zapewnić lepszą widoczność. Teraz powinieneś mieć coś takiego:

![](images/GGTuto1_3.PNG )

Zauważ, że ilość stopni swobody zmniejszyła się do 2. Powodują to wciąż otwarte końce.

**Rysowanie łuku**

Kliknij na przycisk <img alt="" src=images/Sketcher_Arc.svg  style="width:24px;"> [utwórz łuk w szkicowniku](Sketcher_CreateArc/pl.md), ustaw kursor na współrzędnych około x = 80 y = 30; następnie kliknij, aby zdefiniować pierwszy punkt początkowy łuku w prawym górnym punkcie końcowym linii poziomej. Kolejnie kliknij, aby zdefiniować koniec łuku w górnym punkcie końcowym linii pionowej po prawej stronie *(upewnij się, że punkty są podświetlone na żółto przed kliknięciem)*.

Nadaj promień wiązania łuku: wybierz łuk, a następnie kliknij na przycisk <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Zwiąż łuk](Sketcher_ConstrainRadius/pl.md), po czym wprowadź wartość 20mm.

Teraz wybierzmy kształt łuku jako styczną do połączonych z nim linii: wybierzmy łuk, następnie górną linię, a następnie kliknijmy na <img alt="" src=images/Constraint_Tangent.svg  style="width:24px;"> [Utwórz styczną \...](Sketcher_ConstrainTangent/pl.md). Pojawia się komunikat *Zastępowanie wiązań*, kliknij w przycisk **OK**. To samo dotyczy wiązań stycznej po drugiej stronie łuku.

Wykonaliśmy dwa etapy tworzenia szkicu, ale mogliśmy również całkowicie prześledzić profil, aby całkowicie go związać.

**Szkic w pełni związany**

Jeśli działałeś sprawnie, to powinieneś otrzymać to samo:

![](images/GGTuto1_4.PNG )

Szkic zmienił kolor na zielony, co oznacza, że cały został ograniczony. Nie ma w nim żadnych dwuznaczności, wszystko jest perfekcyjnie zdefiniowane. Potwierdza to komunikat solwera w lewym górnym rogu. Zwróć także uwagę na to, że środek łuku lekko się przemieścił, tak naprawdę podając te trzy ostatnie ograniczenia, FreeCAD obliczył poprawną pozycję punktu środka.

Jeśli Twój szkic nie jest jeszcze prezentowany w kolorze zielonym, oznacza to, że jeden lub więcej punktów nie zbiega się we właściwym miejscu *(2 punkty mogą być jeszcze nie zbieżne, ale znajduja sie w sąsiedztwie)*. Zrób małe okno *(okno przechwytywania)* wokół punktu, aby wybrać i utworzyć <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:24px;"> [Wiązanie zgodności na wybranym elemencie](Sketcher_ConstrainCoincident/pl.md). Uwaga: nie myl **Wiązanie zgodności*z*Utwórz punkt na szkicu**. Ich ikony są bardzo podobne, jednak drugie narzędzie ma większą ikonę i dodaje indywidualny punkt w szkicu.

Czynności należy przeprowadzić w ten sam sposób w odniesieniu do wszystkich punktów.

Jeśli Twój szkic nadal nie jest wyświetlany na zielono, sprawdź, czy wszystkie linie *(z wyjątkiem ukośnej)* mają zdefiniowane albo <img alt="" src=images/Constraint_Horizontal.svg  style="width:24px;"> [wiązania poziome](Sketcher_ConstrainHorizontal/pl.md) lub <img alt="" src=images/Constraint_Vertical.svg  style="width:24px;"> [wiązania pionowe](Sketcher_ConstrainVertical/pl.md). W razie potrzeby dodaj je.

### Używanie funkcji wyciągnięcia i kieszeni 

Kliknij w przycisk **Close** w zakładce **zadania**. Środowisko pracy Sketcher zostanie automatycznie zamknięte, a Part Design ponownie wybrane. **Widok złozony** powróci do zakładki **Model**. Jeśli zostawiłeś element \"Body part1\" rozwinięty na drzewku, to zobaczysz nowy element obok **Origin**, zagnieżdżony w elemencie **Body**.

W tym momencie zapisujemy nasz dokument. Nadaj mu nazwę *(na przykład \"tutorial1\" lub jakąkolwiek nazwę, którą uznasz za odpowiednią)*. Dobrą praktyką jest częste zapisywanie dokumentu, na przykład po wykonaniu szkicu lub funkcji.

Kliknij w przycisk <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> **Ustaw widok izometryczny** a następnie <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Dopasuj widok do okna](Std_ViewFitAll.md), co daje wyśrodkowany widok izometryczny 3D.

Kliknij w przycisk <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Wyciągnij wybrany szkic](PartDesign_Pad/pl.md), podaj długość 30mm. Kliknij w przycisk **OK**, kształt jest teraz gotowy. W drzewie modelu obiekt **Pad** *(nazywany właściwość)* pojawi się zamiast szkicu. W rzeczywistości jest to zatwierdzony szkic, ponieważ kształt opiera się na nim. Teraz kliknij na strzałkę lub plusa przy elemencie **Pad** aby rozwinąć go. Poniżej pojawi się nasz szkic, jest on automatycznie ukrywany w widoku 3D *(jego etykieta jest szara)*.

Zauważ, że utworzony kształt jest bryłą.

![](images/GGTuto1_5.PNG )

### Tworzenie otworu 

Ustaw kursor myszki na górnej powierzchni elementu i kliknij, kolejnie użyj narzędzia <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> **Utwórz nowy szkic**. FreeCAD automatycznie stworzy szkic związany do tej powierzchni. Znajdujemy się więc na płaszczyźnie równoległej do płaszczyzny bezwzględnej XY, ale z przesunięciem wysokości o wysokość elementu, tj. 50mm.

Możesz przełączyć widok okna 3D na widok izometryczny <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> lub pozostawić model w widoku od góry <img alt="" src=images/Std_ViewTop.svg  style="width:24px;">. W każdej chwili można powrócić do widoku szkicu *(widok jest zorientowany na płaszczyznę szkicu)* za pomocą <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:24px;"> ikonki [Widok szkicu](Sketcher_ViewSketch/pl.md).

Zauważ, że **źródłem** tego nowego **szkicu** jest bryła. Oczywiście mogą się one różnić, jednak tutaj są mylone z pochodzeniem bezwzględnym.

Za pomocą narzędzia <img alt="" src=images/Sketcher_Circle.svg  style="width:24px;"> [Utwórz okrąg w szkicowniku](Sketcher_CreateCircle/pl.md) narysuj okrąg mniej więcej na środku powierzchni. Okrąg może mieć dowolny promień.

Wybierz okrąg i stwórz wiązanie za pomocą narzędzia <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Zwiąż łuk lub okrąg](Sketcher_ConstrainRadius/pl.md), jako miarę promienia podaj 5mm.

Wybierz punkt będący środkiem okręgu, a następnie <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Utwórz blokadę wiązania dla wybranego elementu](Sketcher_ConstrainLock.md); kliknij dwukrotnie na pole z wymiarem poziomym i wpisz wartość **-65**mm *(tutaj wskazujemy pozycję względem pochodzenia szkicu)*. To samo dotyczy wymiaru pionowego *(-15mm)*. Okrąg zajmuje właściwą pozycję, a szkic staje się zielony, co oznacza, że jest w pełni związany:

![](images/GGTuto1_6.PNG )

Zamknij szkic, w drzewie modelu pojawił się nowy o obiekt o nazwie **Sketch001**. Podczas gdy szkic jest cały czas zaznaczony, kliknij przycisk narzędzia <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Utwórz kieszeń z wybranego szkicu](PartDesign_Pocket.md).

Kieszeń jest właściwością zwaną \"substrakcyjną\", usuwa materiał z naszej części, tutaj w formie cylindra, ponieważ szkic jest kołem. Ustaw jako Typ wartość **Przez wszystkie**, aby całkowicie wyciąć część. Wciśnij przycisk **OK**, aby zakończyć operację. W drzewie modelu na dole części Body1 pojawia się nowy element oznaczony **Pocket** i wskazuje Sketch001.

### Zmiana koloru i przezroczystości 

Istnieje możliwość zmiany koloru części, często przydatne jest wyróżnienie części spośród innych. Również można modyfikować przeźroczystość detalu, co jest pomocne przy prezentacji jego wnętrza.

Wybierz bryłę **Body part1** i przejdź do najniższej części widoku połączonego, kliknij na zakładkę **Widok**; znajdź właściwość **Kolor kształtu** *(Shape color)*. Może okazać się konieczne użycie pionowego paska przewijania w prawo, aby ją znaleźć. Możesz również poszerzyć kolumnę Właściwość: przesuń wskaźnik myszki nad linię rozdzielającą nagłówki **Właściwości** i **Wartość**; gdy kursor zmieni się w dwustronną strzałkę, naciśnij i przytrzymaj lewy przycisk myszy i przeciągnij go na bok, a następnie puść.
W prawej kolumnie kliknij na szary kwadrat, który otwiera okno dialogowe **Wybierz kolor**. Wybierz inny kolor, a następnie kliknij w przycisk OK. Ponownie w zakładce **Widok**, zmień wartość opcji **Przeźroczystość** *(Transparency)*, na przykład na 50 i naciśnij klawisz **Enter**, aby zakończyć *(0=całkowicie nieprzezroczysty, 100=całkowicie przezroczysty)*.

Otwór jest teraz widoczny wewnątrz części. Jest to często przydatne przy oglądaniu ukrytych lub wewnętrznych ścian modelu.

Można również zmieniać kolor linii i szerokość linii, aby zmienić grubość i kolor konturu części.

### Ręczne przesuwanie części 

Przejdź do zakładki menu głównego **Widok** i wybierz pozycję **Przełącz oś przekroju**
To są osie absolutne. Powinieneś teraz zobaczyć w oknie widoku 3D trzy osie X, Y i Z w kolorach czerwonym, zielonym i niebieskim.
Ten punkt orientacyjny pomoże nam odnaleźć się w przestrzeni. Ten punkt orientacyjny jest stały i niezmienny, jest to widok, który się obraca lub obiekt, który obraca się w tej przestrzeni.

W drzewie modelu wybierz **Body**, kolejnie w dolnej części **Widoku połączonego** zwróć uwagę na zakładkę **Dane** *(zakładka **Dane** musi znajdować się na pierwszym planie, być może będziesz musiał kliknąć na nią, aby stała widoczna jej treść)*:

![](images/GGTuto1_10.PNG )

Kliknij na mały trzykropek właściwości **Placement** *(jeśli jest niewidoczny kliknij w pole **Placement**)*. Zostanie wyświetlona nowa treść zakładki **Zadania**. Używając strzałek możesz zmienić pozycje i kąt usytuowania bryły. To właśnie pozycja bryły *(a więc jej początek)* przemieszcza się w przestrzeni, orientacja widoku 3D nie ulega zmianie.

Kolejna metoda: w widoku połączonym wybierz **Body** i kliknij prawym przyciskiem myszy, a następnie wybierz opcje **Przekształć**. Pojawia się następujący widok:

![](images/GGTuto1_11.PNG )

Przytrzymaj i przeciągnij wierzchołek na osi lub kulę, aby bryłą ciałem w dowolnym kierunku.

Potwierdź.
Następnie zresetuj kąty i współrzędne do wartości 0.

### Wyświetlanie wymiarów w szkicu 

Przydatna może okazać się znajomość wymiarów niektórych fragmentów szkicu, na podstawie wewnętrznych obliczeń FreeCAD. Informacje te mogą być użyte tylko do celów poglądowych lub można wykorzystać je później np. do zdefiniowania innych wymiarów.

Na drzewie modelu, *(w razie potrzeby)* należy rozwinąć gałąź **Body part1**, a następnie **Pad**, aby pokazać pierwszy szkic. Kliknij tą pozycję dwukrotnie *(lub kliknij prawym przyciskiem myszy i wybierz **Edytuj szkic** w menu kontekstowym)*, a następnie kliknij na <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:24px;"> [Przełącz tryb wiązań](Sketcher_ToggleDrivingConstraint.md). *(**Uwaga:** w zależności od rozdzielczości ekranu, ta ikona może nie być widoczna. Na prawym końcu paska narzędzi **Wiązań**, możesz znaleźć przycisk **»**. Kliknij na niego, aby rozwinąć i uzyskać dostęp do ukrytych ikon narzędzi).* Od teraz możemy tworzyć wymiary referencyjne zamiast wymiarów konstrukcyjnych. Będą one kreślone w kolorze niebieskim i nie będą miały wpływu na kształty szkicu, z którego pochodzą, będą wyliczane automatycznie.

Na przykład można wyświetlić informacje o tych wymiarach:

![](images/GGTuto1_7.PNG )

Widzimy na przykład, że długość łuku wynosi 20, ponieważ jest on styczny do krawędzi.

Widzimy również, że FreeCAD dokonuje obliczeń lewego boku *(50-50xTAN 30°)*, jak również wymiaru odległości osi łuku wraz z jego początkiem.

### Edycja jednego lub wielu wymiarów 

Podczas modelowania można dowolnie modyfikować wymiary detalu. Jest to bardzo proste: w przypadku grubości elementu kliknij dwukrotnie ikonę **Wyciągnięcia**, a następnie wprowadź nową wartość, na przykład 40mm. W dolnej części **widoku złożonego** możesz również zmienić daną wartość. Zatwierdź ją, kształt bryły obiektu zostanie zmieniony.

To samo dotyczy całkowitej długości elementu: kliknij dwukrotnie na **Szkic**, następnie kliknij dwukrotnie na linijkę wymiarową 100mm. Zmień wartość na 110mm, a następnie zaakceptuj.

Widzimy, że fragment ten został powiększony, ale otwór nie jest już wyśrodkowany na górze ściany. Dzieje się tak dlatego, że został on związany z pochodzeniem szkicu. Co niekoniecznie odpowiada temu, co chcielibyśmy osiągnąć. Otwór powinien pozostać po środku, niezależnie od wielkości ściany.

### Wyśrodkowanie otworu 

#### Metoda pierwsza, z wykorzystaniem geometrii zewnętrznej. 

Edytuj ponownie szkic otworu i usuń jego poziome i pionowe wiązania odległości.

Teraz kliknij narzędzie <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Utwórz krawędź związaną z zewnętrzną geometrią](Sketcher_External/pl.md).

Teraz stworzymy dwie linie w szkicu, ale wyodrębnione z kształtu *(lub elementu)* zewnętrznego, w stosunku do tego i wcześniej zdefiniowanego: kształtu Wyciagnięcia.

Kliknij na pionową krawędź znajdującą się u góry części. Na przykład: krawędź przy pochyłej ścianie.

Nad krawędzią pojawi się nowa purpurowa linia. Powtórz tą czynność dla drugiej krawędzi, po zaokrąglonej stronie ściany.

Teraz można wykorzystać te linie *(a zwłaszcza ich punkty końcowe)* do wyśrodkowania okręgu, jednak musimy dodać kolejne dwie linie konstrukcyjne: na przykład przekątne.

W tym celu kliknij narzędzie <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md): linie będą miały kolor niebieski i nie będą uwzględniane w trybie edycji szkicu detalu. Pozwalają one ustalić punkt środkowy okręgu. Utwórz przekątne w ten sam sposób, w jaki narysowałeś pierwsze linie. Upewnij się, że wszystkie punkty są zbieżne.

Po czym należy zaznaczyć środek okręgu, kolejnie dwie niebieskie linie po przekątnej\' i kliknąć na ikonę narzędzia <img alt="" src=images/Constraint_PointOnObject.svg  style="width:24px;"> [Ustaw punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Okrąg zostanie umieszczony w punkcie przecięcia przekątnych, czyli po środku ściany.
Szkic musi być zielony, całkowicie związany *(jest to niezbędne)*. Zauważ, że oprócz promienia okręgu, nie jest już niezbędne tworzenie wiązań wymiarów.

Proszę zauważyć, że oprócz przełączenia paska narzędzi w tryb konstruowania, <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> Przycisk [Construction Mode](Sketcher_ToggleConstruction/pl.md) może również przełączać poszczególne elementy Sketchera w tryb konstrukcyjny, jeśli zostały one wcześniej wybrane. Jeśli przypadkowo przełączysz element w tryb konstrukcyjny, może pojawić się błąd po zakończeniu szkicu.

![](images/GGTuto1_8.PNG )

Opuść ten szkic, przekonamy się, że krąg jest prawidłowo wyśrodkowany. *(Funkcja kieszeni nie została usunięta, ale zmodyfikowana)*. Jeśli ponownie zmienisz wymiary części, grubość lub długość, okrąg będzie pozostawał na środku ściany.

#### Unikaj linii konstrukcyjnych: 

Często można uniknąć tworzenia linii konstrukcyjnych. Możesz ponownie edytować szkic, i usunąć linie konstrukcyjne. Następnie należy posłużyć się funkcją <img alt="" src=images/Constraint_Symmetric.svg  style="width:24px;"> [Utwórz wiązanie symetrii \...](Sketcher_ConstrainSymmetric/pl.md) pomiędzy dwoma przeciwległymi wierzchołkami zewnętrznych linii geometrii, a środkiem okręgu *(punkty należy wybrać w tej kolejności)*:

![](images/GGTuto1_12.PNG )

Uzyskamy identyczny wynik dla położenia środka otworu. W rzeczywistości, dzięki dostępnym wiązaniom w Środowisku pracy Sketcher, istnieje wiele możliwych dróg postępowania.
/Ten przykład pokazuje, że często lepiej jest wybrać najprostszą metodę, ograniczając w ten sposób liczbę utworzonych obiektów oraz liczbę błędów, które mogą się pojawić.

#### Metoda druga z płaszczyzną odniesienia 

Oto kolejna, szybsza metoda, możliwa do zastosowania od wersji **0.17**.
Użycie płaszczyzny odniesienia i jej dołączenie.

Zacznij od skasowania efektu działania funkcji **Kieszeń** oraz szkicu otworu. Wybierz górną ścianę i kliknij przycisk <img alt="" src=images/PartDesign_Point.svg  style="width:24px;"> [Utwórz nowy punkt odniesienia](PartDesign_Point.md): dla aktywnej części bryły. Wybranym trybem dołączenia powinien być \"Środek ciężkości\".

Ponieważ ściana jest prostokątna, jej środek masy odpowiada punktowi przecięcia przekątnych. Zatwierdź, a punkt odniesienia zostanie utworzony.
Wybierz górną ścianę ponownie i trzymając wciśnięty klawisz **CTRL**, na drzewie modelu wybierz punkt odniesienia, który właśnie utworzyłeś. Puść klawisz CTRL i kliknij w przycisk <img alt="" src=images/PartDesign_Plane.svg  style="width:24px;"> [Utwórz nowa płaszczyznę odniesienia](PartDesign_Plane.md). Płaszczyzna odniesienia zostanie utworzona na podstawie pochodzenia punktu. Kliknij przycisk OK.

Teraz bardzo łatwo jest umieścić okrąg w samym środku! Z drzewa modelu lub w widoku 3D, wybierz płaszczyznę którą stworzyłeś, i kliknij <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Utwórz nowy szkic](Sketcher_NewSketch/pl.md), szkic zostanie stworzony z podaniem miejsca początkowego. Następnie wystarczy narysować okrąg o promieniu 5mm na podstawie punktu początku, po czym zatwierdzić *(szkic musi być zielony bezwzględnie)*.

Za pomocą funkcji **Kieszeń**, jak poprzednio, utwórz otwór, który zawsze będzie wyśrodkowany.

![](images/GGTuto1_9.PNG )

Ten poradnik jest zakończony, zapisz ten plik, możesz się dobrze bawić badając różne funkcje. Zmień wymiary, zmodyfikuj kształty, umieść nowe otwory na innych ścianach, to właśnie podczas popełniania błędów robimy postępy!

Możesz również kontynuować ćwiczenie umiejętności w kolejnym poradniku o nieco bardziej skomplikowanej części:

[Podstawy dla Środowiska pracy Projekt Części](Basic_Part_Design_Tutorial.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Creating a simple part with PartDesign/pl
