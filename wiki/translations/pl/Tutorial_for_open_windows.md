---
 TutorialInfo:l
   Topic: Architektura
   Level: Początkujący
   Time: 60 minut
   Author: https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx
   FCVersion: 0.18 lub nowszy
   Files: nie dołączono
---

# Tutorial for open windows/pl







## Wprowadzenie

Ten poradnik pokazuje, jak umieszczać [okna architektoniczne](Arch_Window/pl.md) i drzwi w modelu budynku, jak wyświetlać je jako otwarte w widoku 3D oraz jak tworzyć rysunek 2D *(projekcję planu i elewacji)* dla modelu. Wykorzystuje środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md) i [Rysunek Techniczny](TechDraw_Workbench/pl.md).

Często używanymi narzędziami są: [Siatka](Draft_Snap_Grid/pl.md), [Przyciągnij](Draft_Snap/pl.md), [Polilinia](Draft_Wire/pl.md) środowiska Rysunek roboczy, [Ściana](Arch_Wall/pl.md), [Okno](Arch_Window/pl.md), [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, oraz [Widok Architektoniczny](TechDraw_ArchView/pl.md) środowiska Rysunek Techniczny.

Zobacz również poniższą stronę, aby zobaczyć kilka filmów na temat pracy z oknami i drzwiami.

-   [Środowisko pracy używane do tworzenia projektów architektonicznych nosi nazwę Architektura](http://help-freecad-jpg87.fr/04_arch_ind.php).



## Konfiguracja

1\. Otwórz program FreeCAD, utwórz nowy pusty dokument i przejdź do środowiska [Architektura](Arch_Workbench/pl.md).

2\. Upewnij się, że jednostki są prawidłowo ustawione w menu **Edycja → Preferencje ... → Ogólne → Jednostki**. Na przykład {{Incode|MKS (m/kg/s/stopnie)}} jest dobre do radzenia sobie z odległościami w typowym budynku; co więcej, ustaw liczbę miejsc dziesiętnych na {{Incode|4}}, aby uwzględnić nawet najmniejsze ułamki metra.

3\. Użyj przycisku [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md), aby wyświetlić siatkę z wystarczającą rozdzielczością. Wygląd siatki można dostosować w menu **Edycja → Preferencje → Rysunek Roboczy → Siatka i przyciąganie → Siatka**. Ustaw linie co `50 mm`, z głównymi liniami co `20` linii *(co metr)* i `1000 linii` w sumie (siatka obejmuje obszar 50 m x 50 m).

4\. [Oddal](Std_ViewZoomOut/pl.md) widok 3D, jeśli znajdujesz się zbyt blisko siatki.

Teraz jesteśmy gotowi do stworzenia prostego budynku z zamkniętymi ścianami, dwoma drzwiami i dwoma oknami.



## Umieszczenie ściany 

5\. Użyj narzędzia [Polilinia](Draft_Wire/pl.md), aby utworzyć zamkniętą linię. Idź zgodnie z ruchem wskazówek zegara. 5.1. Pierwszy punkt w (0, 0, 0). W oknie dialogowym wprowadź **0** **m** **Enter**, **0** **m** **Enter**, **0** **m** **Enter**. 5.2. Drugi punkt w (3, 0, 0). Naciśnij **X**, aby ograniczyć ruch do osi X; wprowadź wartość **3** **m** **Enter**. 5.3. Trzeci punkt w (3, 4, 0). Naciśnij **Y**, aby ograniczyć ruch do osi Y; wprowadź wartość **4** **m** **Enter**. 5.4. Czwarty punkt w (0, 4, 0). Naciśnij **X**, aby ograniczyć ruch do osi X. Wprowadź wartość **-** **3** **m** **Enter**. 5.5. Naciśnij **O**, aby zamknąć linię i zakończyć narzędzie. 5.6. Na klawiaturze numerycznej naciśnij **0**, aby uzyskać [widok aksonometryczny](Std_ViewIsometric/pl.md) modelu. **Uwaga:** punkty można również zdefiniować za pomocą kursora myszki, wybierając przecięcia na siatce, przy pomocy paska narzędzi [przyciągania](Draft_Snap/pl.md) i metody [przyciągnij do siatki](Draft_Snap_Grid/pl.md).

6\. Wybierz {{Incode|DWire}} i zmień właściwość **Utwórz ścianę** na {{FALSE/pl}}.

7\. Wybierz {{Incode|DWire}} i kliknij narzędzie [Ściana](Arch_Wall/pl.md). Ściana zostanie natychmiast utworzona z domyślną szerokością *(grubością)* 0,2 m i wysokością 3 m. **Uwaga:** jeśli właściwość **Utwórz ściane** `DWire` ma wartość {{TRUE/pl}}, ten krok utworzy bryłę, zamiast używać tylko konturu `DWire`.

<img alt="" src=images/01_T01_wire_wall.png  style="width:600px;"> 
*align=center|Podstawowa polilinia dla ściany. To zamknięta linia, która nie tworzy powierzchni.*

<img alt="" src=images/02_T01_just_wall.png  style="width:600px;"> 
*align=center|Ściana utworzona z polilini*



## Umieszczanie drzwi i okien 

8\. Kliknij narzędzie [Okno](Arch_Window/pl.md). Jako wstępnie wybierz `Proste drzwi`, a wysokość zmień na 2 m.

:   8.1. Zmień przyciąganie na [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md) i spróbuj wybrać dolną krawędź ściany frontowej. W razie potrzeby ustaw [widok standardowy](Standard_view.md), aby wybrać krawędź, a nie lico ściany; gdy punkt środkowy jest aktywny, kliknij, aby umieścić drzwi.
:   8.2. Ponownie kliknij narzędzie [Okno architektoniczne](Arch_Window.md), i umieść kolejne drzwi, tym razem w środku tylnej ściany. Dostosuj [widok standardowy](Std_View_Menu/pl.md) według potrzeb.

<img alt="" src=images/03_T01_wall_place_door_rear.png  style="width:600px;"> 
*align=center|Przyciąganie do punktu środkowego dolnej krawędzi ściany w celu umieszczenia drzwi.*

9\. Kliknij narzędzie [Okno](Arch_Window/pl.md). Jako wstępnie wybierz `Otwarte jednoskrzydłowe`, a wysokość `Progu` zmień na 1 m.

:   9.1. Zachowaj przyciąganie do [punktu środkowego](Draft_Snap_Midpoint/pl.md), i spróbuj wybrać dolną krawędź lewej ściany.Obróć [widok standardowy](Std_View_Menu/pl.md) według potrzeb, aby pomóc w wybraniu krawędzi, a nie powierzchni ściany. Gdy środek odcinka jest aktywny, kliknij, aby umieścić okno.


**Uwaga:**

`Wysokość progu` to odległość od podłogi do dolnej krawędzi elementu. Dla drzwi `Wysokość progu` zazwyczaj wynosi 0 m, ponieważ drzwi zazwyczaj stykają się z podłogą. Natomiast okna zwykle mają odstęp od 0,5 m do 1,5 m od podłogi.

9.2. Kliknij ponownie narzędzie [Okno](Arch_Window/pl.md) i umieść kolejne okno, tym razem w środku prawej ściany. Obróć widok [standardowy](Std_View_Menu/pl.md), jeśli to konieczne. Tym razem szerokość okna *(długość)* ustaw na 1,5 m, a `Wysokość progu` ponownie na 1 m.

<img alt="" src=images/04_T01_wall_place_door_side_right.png  style="width:600px;"> 
*align=center|Przyciąganie do punktu środkowego dolnej krawędzi ściany w celu umieszczenia okna.*

:   
    **Uwaga:**parametr `Wysokość progu` można ustawić tylko podczas początkowego tworzenia okna z predefiniowaną konfiguracją. Po wstawieniu okna można zmienić jego położenie, edytując wektor `[x, y, z]` właściwości **Pozycja** podkładającego [szkicu](Sketcher_Workbench/pl.md).





:   9.3. Przesuń okno `Window001` trochę wyżej. Wybierz podkładający `Sketch003` i zmień jego właściwość **Pozycja** z `[3,1 m, 2,0 m, 1,0 m]` na `[3,1 m, 2,0 m, 1,6 m]`. Całe okno `Window001` powinno się przesunąć w górę. Ściana może wciąż pokazywać otwarcie w poprzednim miejscu. Jeśli tak się dzieje, kliknij prawym przyciskiem myszy element `Wall`, wybierz `Oznacz do przeliczenia` i następnie naciśnij klawisze **Ctrl** + **R**, aby [przeliczyć](Std_Refresh/pl.md) model.

<img alt="" src=images/04.1_T01_wall_built.png  style="width:600px;"> 
*align=center|Ściana z drzwiami i oknami.*


**Uwaga:**

Podczas umieszczania okna lub drzwi z ustawieniami wstępnymi, najedź na element nad [ścianą](Arch_Wall.md) i poczekaj, aż element obróci się tak, że będzie równoległy do tej ściany. Celuj w dolny brzeg ściany i użyj `Wysokość progu` do dostosowania odległości od podłogi. Jeśli to trudne, użyj trybu przyciągania [do najbliższego](Draft_Snap_Near/pl.md) z paska narzędzi [przyciągania](Draft_Snap/pl.md), aby wstawić element w dowolnym miejscu na powierzchni ściany, a następnie dostosuj jego właściwość **Pozycja** ręcznie, zgodnie z opisem powyżej. Posiadanie wielu aktywnych jednocześnie trybów [przyciągania](Draft_Snap/pl.md) może powodować problemy z umieszczeniem elementu, więc spróbuj korzystać z jednej opcji na raz.


**Uwaga 2:**

czasami okno może być umieszczone poza [ścianą](Arch_Wall/pl.md). O ile element jest równoległy do tej ściany, powinieneś być w stanie ręcznie poprawić jego położenie.



## Otwieranie drzwi 

10\. W widoku drzewa wybierz {{Incode|Sketch}} leżący pod {{Incode|Door}} i naciśnij **Space** lub zmień właściwość **Widoczność** na {{TRUE/pl}}.

11\. Kliknij dwukrotnie obiekt {{Incode|Door}} w widoku drzewa, aby rozpocząć edycję.

:   11.1. Wewnątrz ramy `elementów okna` znajdują się dwa panele, `Wire` i `Components`.
:   
    **Uwaga:**w przypadku prostego ustawienia drzwi są dwie polilinie, `Wire0` i `Wire1`, oraz dwa komponenty, `OuterFrame` i `Door`. Niestandardowo zaprojektowane [drzwi](Arch_Door/pl.md) mogą zawierać więcej polilinii i komponentów.





:   11.2. Kliknij na `Door` i kliknij przycisk **Edycja**. Spowoduje to wyświetlenie właściwości komponentu `Door`, takich jak `Name`, `Type`, `Wires`, `Thickness`, `Offset`, `Hinge` i `Opening mode`.
:   11.3. W widoku 3D wybierz tylko jedną pionową krawędź na widocznym szkicu drzwi, a następnie kliknij przycisk **Pobierz wybraną krawędź**. Przycisk powinien zmienić się na nazwę krawędzi, na przykład **Edge8**.
:   11.4. Zmień {{Incode|Opening mode}} na **Arc 90** lub dowolną inną opcję.
:   11.5. Kliknij przycisk **+Twórz/aktualizuj komponent**, a następnie **Zamknij**, aby zakończyć edycję drzwi. Szkic może zostać ponownie ukryty.

![](images/05_T01_window_edit.png ) 
*align=center|Okno dialogowe do edycji okna lub drzwi*

![](images/06_T01_window_edit_component.png ) 
*align=center|Okno dialogowe do edycji komponentów tworzących okno lub drzwi.*

<img alt="" src=images/06.1_T01_window_edit_wire_door_front.png  style="width:600px;"> 
*align=center|Pionowa krawędź szkicu wybrana jako zawias drzwi.*

12\. Wybierz {{Incode|Drzwi}} i nadaj właściwości **Otwarcie** wartość 45. Pełny panel drzwi powinien otwierać się do wewnątrz budynku.

13\. Wybierz {{Incode|Drzwi}} i zmień właściwość **Symbol Elevation** na {{TRUE/pl}}. Końcówka utworzonej linii wskazuje, z której strony otwierają się drzwi. Jest to łatwiejsze do zauważenia, jeśli widok zostanie zmieniony na [od przodu](Std_ViewFront/pl.md). Zmień właściwość **Symbol Plan** na {{TRUE/pl}}. Okrągły łuk powinien wskazywać zakres obrotu drzwi. Jest to łatwiejsze do zobaczenia, jeśli widok zostanie zmieniony na [od góry](Std_ViewTop/pl.md).

14\. Powtórz kroki z obiektem {{Incode|Drzwi001}} i obiektem bazowym {{Incode|Szkic001}}, aby drzwi otwierały się pod kątem 75° do wnętrza budynku. Włącz także symbole elewacji i planu.

![](images/07_T01_window_property_view.png ) 
*align=center|Widok właściwości drzwi umożliwiający zmianę wartości otwarcia, symbolu elewacji, symbolu planu i innych opcji.*

<img alt="" src=images/08_T01_window_symbol_elevation.png  style="width:600px;"> 
*align=center|Drzwi z symbolem otwarcia na rzucie elewacji, widok z przodu.*

<img alt="" src=images/09_T01_window_symbol_plan.png  style="width:600px;"> 
*align=center|Drzwi z symbolem planu, widok z góry.*



## Otwieranie drzwi 

15\. W widoku drzewa wybierz {{Incode|Sketch002}} leżący pod {{Incode|Oknem}} i naciśnij **Spacja** lub zmień właściwość **Widoczność** na {{TRUE/pl}}.

16\. Kliknij dwukrotnie obiekt {{Incode|Okno}} w widoku drzewa, aby rozpocząć edycję.

:   16.1. Kliknij komponent {{Incode|WewnętrznaRama}} i kliknij przycisk **Edytuj**.





:   16.2. W widoku 3D zaznacz tylko jedną pionową krawędź w `Szkic002`. Linie reprezentujące `ZewnętrznaRama` i `WewnętrznaRama` są bardzo blisko siebie, więc [prybliż](Std_ViewZoomIn.md) widok szkicu, aby wybrać odpowiednią linię. Następnie kliknij przycisk **Pobierz wybraną krawędź**. Przycisk powinien zmienić się na nazwę krawędzi, na przykład **Krawędź12**.


**Uwaga:**

gdy na ekranie znajduje się wiele brył, że trudno jest wybrać tylko jedną krawędź, przełącz się na widok [szkieletowy](Std_DrawStyle/pl#Szkieletowy.md), aby usunąć powierzchnie tych brył i zobaczyć tylko same linie, krawędzie i kontury.

:   16.3. Zmień `Tryb otwierania` na `Łuk 90 wew`, lub dowolną inną opcję.

17\. Wybierz {{Incode|Okno}} i nadaj właściwości **Otwarcie** wartość 45. Wewnętrzna rama zawierająca przezroczyste szkło powinna otwierać się do wnętrza budynku.

18\. Wybierz {{Incode|Okno}} i zmień właściwość **Symbol Elevation** na {{TRUE/pl}}. Końcówka utworzonej linii wskazuje, z której strony otwierają się drzwi. Jest to łatwiejsze do zauważenia, jeśli widok zostanie zmieniony na [od przodu](Std_ViewFront/pl.md). Zmień właściwość **Symbol Plan** na {{TRUE/pl}}. Okrągły łuk powinien wskazywać zakres obrotu drzwi. Jest to łatwiejsze do zobaczenia, jeśli widok zostanie zmieniony na [od góry](Std_ViewTop/pl.md).

19\. Powtórz kroki z obiektami {{Incode|Okno001}} i bazowym {{Incode|Szkic003}}, aby okno otwierało się pod kątem 75 stopni. Pokaż również symbole elewacji i planu. W tym przypadku nie wybieraj pionowej linii `WewnętrznaRama` jako zawiasu, ale wybierz górną linię poziomą. Oznacza to, że to okno będzie otwierać się inaczej niż pozostałe. Symbol elewacji będzie lepiej widoczny z [prawej strony](Std_ViewRight/pl.md). Symbol planu będzie lepiej widoczny od [przodu](Std_ViewFront/pl.md). Jednakże, ponieważ ściana zasłania widok, możesz zmienić jej właściwość **Przezroczystość** na wartość taką jak 85, aby przez nią widzieć. Alternatywnie możesz także zmienić jej właściwość **Tryb wyświetlania** na `Szkieletowy`, aby pokazać tylko jej krawędzie. <img alt="" src=images/06.2_T01_window_edit_wire_side_right.png  style="width:600px;"> 
*align=center|Pozioma krawędź szkicu wybrana jako zawias okna.*

<img alt="" src=images/10_T01_window_all_symbol_axonometric.png  style="width:600px;"> 
*align=center|Symbole elewacji i planu dla wszystkich elementów, widok aksonometryczny.*

<img alt="" src=images/11_T01_window_all_symbol_top.png  style="width:600px;"> 
*align=center|Symbole elewacji i planu dla wszystkich elementów, widok z góry.*



## Sporządzenie planu piętra budynku 

20\. Wciąż będąc w środowisku pracy [Architektura](Arch_Workbench/pl.md), zaznacz wszystkie komponenty w widoku drzewa, [ściana](Arch_Wall/pl.md), dwa [oknas](Arch_Window/pl.md) i dwoje [drzwis](Arch_Door/pl.md), a następnie użyj narzędzia [Płaszczyzna przekroju](Arch_SectionPlane/pl.md), aby utworzyć obiekt `Przekroju`.


**Uwaga:**

zmień właściwość **Wielkość strzałki** płaszczyzny przekroju na większą wartość, na przykład {{Value|200 mm}}, aby kierunek przekroju był wyraźnie widoczny w widoku 3D.

<img alt="" src=images/11.1_T01_Arch_SectionPlane_all.png  style="width:600px;"> 
*align=center|Płaszczyzna przekroju przecinająca obiekty stałe, w tym ściany, drzwi i okna.*

21\. Przełącz się na środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) i wstaw nową stronę za pomocą narzędzia [Wstaw nową domyślną stronę rysunku](TechDraw_PageDefault/pl.md). Zostanie utworzony nowy obiekt `Strona`, a widok zostanie przełączony na tę stronę. Wstawiona strona to standardowy arkusz formatu A4 w orientacji poziomej, z podstawowym obramowaniem. Użyj narzędzia [Wstaw nową stronę przy użyciu szablonu](TechDraw_PageTemplate/pl.md), jeśli potrzebujesz utworzyć nową stronę przy użyciu określonego szablonu [Svg](SVG/pl.md).

22\. Wybierz `Przekrój` i użyj narzędzia [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md), aby utworzyć obiekt {{Incode|Widok architektoniczny}} na stronie. Najprawdopodobniej nowy obiekt nie będzie widoczny na stronie, ponieważ ma bardzo dużą skalę {{value|1}}, czyli 1:1. Oznacza to, że każdy metr w widoku 3D jest wyświetlany jako metr w widoku strony. Ponieważ strona ma rozmiar zaledwie 0,297 m x 0,210 m, większość elementów jest zbyt duża, aby zmieścić się na tej stronie w ich naturalnej skali.

23\. Wybierz obiekt {{Incode|Widok architektoniczny}} i zmień właściwość **Skala** na {{Incode|0.02}}, co odpowiada skali 1:50, odpowiedniej dla typowych budynków. Oznacza to, że każdy metr w widoku 3D będzie wyświetlany jako 20 mm na stronie. Obiekt powinien pojawić się na środku strony i może zostać przesunięty w lepsze miejsce po lewej stronie. Dwoje drzwi powinno wyglądać na otwarte, ale tylko lewe okno powinno wyglądać na otwarte. Powodem, dla którego prawe okno nie pojawia się w rzucie, jest to, że płaszczyzna zdefiniowana przez `Przekrój` nie przecina tego prawego okna.

<img alt="Section view of the building, A4 sheet, scale 1:50" src=images/12_T01_TechDraw_window_all_symbols.png  style="width:600px;"> 
*align=center|Płaszczyzna przekroju przecinająca obiekty stałe, w tym ściany, drzwi i okna.*

24\. Wróć do środowiska pracy [Architektura](Arch_Workbench/pl.md). W widoku drzewa ponownie wybierz wszystkie komponenty i użyj narzędzia [Płaszczyzna przekroju](Arch_SectionPlane/pl.md), aby utworzyć drugi obiekt `Przekrój001`.

:   24.1. Wybierz {{Incode|Przekrój001}} i zmień właściwość **Pozycja** na {{Incode|[1.5 m, 2.0 m, 1.8 m]}}. Ta druga płaszczyzna przecina wszystkie obiekty Architektoniczne.
:   24.2. Wróć do środowiska [Rysunek Techniczny](TechDraw_Workbench/pl.md). Wybierz {{Incode|Przekrój001}}, użyj narzędzia [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md), aby utworzyć `ArchView001` i ustaw właściwość **Skala** na {{Value|0.02}}. Nowy widok na stronie Rysunku technicznego pokazuje teraz wszystkie otwory w [ścianie](Arch_Wall/pl.md) utworzone przez drzwi i okna.


**Uwaga:**

ustawienie właściwości **All On** na {{TRUE/pl}} dla obiektów [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md) powoduje, że wszystkie elementy przecięte przez płaszczyznę są widoczne na stronie, niezależnie od ich stanu widoczności w widoku 3D. Opcję **Pokaż wypełnienie** również można ustawić na {{TRUE/pl}}, aby pokazać cień na bryłach, które zostały przecięte przez płaszczyznę przekroju.

<img alt="" src=images/13_T01_TechDraw_window_all_symbols_higher.png  style="width:600px;"> 
*align=center|Widok przekroju budynku z wyciętą drugą płaszczyzną, arkusz A4, skala 1:50*



## Wykonanie rzutu elewacji budynku 

25\. Wróć do środowiska pracy [Architektura](Arch_Workbench/pl.md). W widoku drzewa zaznacz wszystkie komponenty, [ściana](Arch_Wall/pl.md), dwa [okna](Arch_Window/pl.md) i dwoje [drzwis](Arch_Door/pl.md), a następnie użyj narzędzia [Płaszczyzna przekroju](Arch_SectionPlane/pl.md), aby utworzyć trzeci element `Przektój002`.

:   25.1. Obróć {{Incode|Przektój002}}, tak aby przecinał pionowo budynek. Zmień właściwości **Oś** na `[1, 0, 0]` i **Kąt** na `90`.
:   25.2. Zmień właściwość **Pozycja** na `[1.5 m, -1 m, 1.5 m]`, aby płaszczyzna znajdowała się przed budynkiem.

<img alt="" src=images/14.1_T01_Arch_SectionPlane_three.png  style="width:600px;"> 
*align=center|Płaszczyzny przekroju, które przecinają lub patrzą na budynek i obiekty stałe.*

26\. Wróć do środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) i użyj narzędzia [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md) na obiektcie {{Incode|Przekrój002}}. Pamiętaj o dostosowaniu skali do {{Incode|0.02}} *(1:50)*. Zmień właściwość **Obrót** na `-90`, aby skorygować wygląd rzutów. Ułóż {{Incode|ArchView002}} obok innych widoków na stronie. Ten trzeci rzut przedstawia budynek od frontu.

<img alt="" src=images/14_T01_TechDraw_window_all_symbols_elevation.png  style="width:600px;"> 
*align=center|Widok przekroju budynku, dwa widoki z góry i jeden widok elewacji, arkusz A4, skala 1:50.*



## Współdziałanie środowiska Architektura i Rysunek Techniczny 

Na dzień pisania tego poradnika *(FreeCAD 0.18, listopad 2018)*, środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) może wyświetlać na swoich stronach tylko to, co środowisko [Architektura](Arch_Workbench/pl.md), zapewnia eksport jako [SVG](SVG/pl.md). Oznacza to, że wygląd elementów zawartych w narzędziu [Płaszczyzna przekroju](Arch_SectionPlane/pl.md), i wyświetlanych przez narzędzie [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md), jest kontrolowany przez środowisko [Architektura](Arch_Workbench/pl.md).

Środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) ma tylko minimalną kontrolę nad tym, jak wyświetla te obiekty [płaszczyzny przekroju](Arch_SectionPlane/pl.md) *(`ArchView`)*. Dlatego raporty o błędach i prośby o dodanie funkcji dotyczących wyświetlania elementów Architektury powinny być zgłaszane do obu środowisk pracy.

Bliska interakcja między środowiskami pracy jest planowana na przyszłe wersje FreeCAD. W tych wersjach oczekuje się rozwiązania długotrwałych problemów, takich jak kontrola cech linii i powierzchni *(grubość linii, kolor linii, kolor powierzchni, wzory kreskowania i inne)*.


 {{Draft_Tools_navi}} {{TechDraw_Tools_navi}}



---
⏵ [documentation index](../README.md) > Tutorial for open windows/pl
