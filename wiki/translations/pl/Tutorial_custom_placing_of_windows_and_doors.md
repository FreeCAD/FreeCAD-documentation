---
 TutorialInfo:l
   Topic: Architektura
   Level: średnio zaawansowany
   Time: 60 minut
   Author: https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx
   FCVersion: 0.18 lub nowszy
   Files: nie dołączono
}}



## Wprowadzenie

Ten poradnik pokazuje, jak umieścić niestandardowe okno i drzwi w modelu budynku. Wykorzystuje on środowisko Rysunek Roboczy, Architektura i Szkicownik.

Często używanymi narzędziami są: siatka, narzędzia przyciągania, polilinia, ściana, okno i Utwórz szkic. Użytkownik powinien być zaznajomiony z tworzeniem szkiców z wiązaniami.

Ten poradnik został zainspirowany poradnikami autorstwa jpg87 opublikowanymi na forum FreeCAD.

-   Architektura: Tworzenie niestandardowego okna
-   Architektura: Jak używać niestandardowego okna

Zobacz także poniższy wątek, aby uzyskać więcej informacji na temat położenia okien i drzwi.

-   Dyskusja: Orientacja okien i drzwi.

Zobacz także poniższą stronę, aby zobaczyć kilka filmów na temat wyrównywania okien.

-   Środowisko pracy używane do tworzenia projektów architektonicznych nosi nazwę Architektura.



## Konfiguracja

1\. Otwórz program FreeCAD, utwórz nowy pusty dokument i przejdź do środowiska Architektura.

2\. Upewnij się, że jednostki są prawidłowo ustawione w menu **Edycja , Preferencje ... , Ogólne , Jednostki**. Na przykład {{Incode   MKS }}{: mediawiki} jest dobre do radzenia sobie z odległościami w typowym budynku; co więcej, ustaw liczbę miejsc dziesiętnych na {{Incode   4}}{: mediawiki}, aby uwzględnić nawet najmniejsze ułamki metra.

3\. Użyj przycisku Przełącz widoczność siatki, aby wyświetlić siatkę z wystarczającą rozdzielczością. Wygląd siatki można dostosować w menu **Edycja , Preferencje , Rysunek Roboczy , Siatka i przyciąganie , Siatka**. Ustaw linie co {{incode   50 mm}}{: mediawiki}, z głównymi liniami co {{incode   20}}{: mediawiki} linii ** i {{incode   1000 linii}}{: mediawiki} w sumie .

4\. Oddal widok 3D, jeśli znajdujesz się zbyt blisko siatki.

Teraz możemy stworzyć prostą ścianę, na której umieścimy okna i drzwi.



## Umieszczenie ściany 

5\. Użyj narzędzia Polilinia, aby utworzyć linie. Idź w kierunku przeciwnym do ruchu wskazówek zegara.

:   5.1. Najpierw wskaż punkt ; w oknie dialogowym wpisz **0** **m** **Enter**, **4** **m** **Enter**, **0** **m** **Enter**.
:   5.2. Drugi punkt w ; w oknie dialogowym wpisz **2** **m** **Enter**, **0** **m** **Enter**, **0** **m** **Enter**.
:   5.3. Trzeci punkt w ; w oknie dialogowym wpisz **4** **m** **Enter**, **0** **m** **Enter**, **0** **m** **Enter**.
:   5.4. Czwarty punkt w ; w oknie dialogowym wpisz **6** **m** **Enter**, **2** **m** **Enter**, **0** **m** **Enter**.
:   5.4. Piąty punkt w ; w oknie dialogowym wpisz **6** **m** **Enter**, **5** **m** **Enter**, **0** **m** **Enter**.
:   5.5. Na klawiaturze naciśnij **A**, aby zakończyć polilinię.
:   5.6. Na klawiaturze numerycznej naciśnij **0**, aby uzyskać widok aksonometryczny modelu.

Upewnij się, że pole wyboru **Względnie** jest wyłączone, jeśli podajesz współrzędne bezwzględne. **Uwaga 2:** punkty mogą być również definiowane za pomocą kursora myszki poprzez wybranie przecięć na siatce, przy pomocy paska narzędzi przyciągania i metody Przyciągnij do siatki. **Uwaga 3:** można również tworzyć kształty programowo za pomocą skryptów w Python. Należy pamiętać, że większość funkcji oczekuje danych wejściowych w milimetrach.


{{Code   code: 
import FreeCAD
import Draft

p = FreeCAD.Vector,
FreeCAD.Vector,
FreeCAD.Vector,
FreeCAD.Vector,
FreeCAD.Vector

w = Draft.makeWire
---

# Tutorial custom placing of windows and doors/pl

 
6\. Wybierz {{Incode|DWire}} i kliknij narzędzie [ściana](Arch_Wall/pl.md). Ściana zostanie natychmiast utworzona z domyślną szerokością *(grubością)* 0,2 m i wysokością 3 m.

<img alt="" src=images/01_T02_wire_wall.png  style="width:600px;">



*align=center|Linia bazowa dla ściany*

<img alt="" src=images/02_T02_just_wall.png  style="width:600px;">



*align=center|Ściana utworzona z polilini*



## Umieszczanie wstępnie ustawionych drzwi i okien 

7\. Kliknij narzędzie [okno](Arch_Window/pl.md). Jako ustawienie wstępne wybierz `Zwykłe drzwi` i zmień wysokość na 2 m.

:   7.1. Zmień przyciąganie na [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md) i spróbuj wybrać dolną krawędź ściany frontowej. W razie potrzeby ustaw [widok standardowy](standard_view.md), aby wybrać krawędź, a nie lico ściany; gdy punkt środkowy jest aktywny, kliknij, aby umieścić drzwi.
:   7.2. Kliknij ponownie narzędzie [okno](Arch_Window/pl.md) i umieść kolejne drzwi, ale tym razem w punkcie środkowym prawej ściany. Ustaw [widok standardowy](standard_view.md) w razie potrzeby.

<img alt="" src=images/03_T02_wall_place_doors.png  style="width:600px;">



*align=center|Przyciąganie do punktu środkowego dolnej krawędzi ściany w celu umieszczenia drzwi.*


:   
    **Uwaga:**`Wysokość parapetu` to odległość od podłogi do dolnej krawędzi elementu. W przypadku drzwi `Wysokość parapetu` wynosi zwykle 0 m, ponieważ drzwi zwykle dotykają podłog. Z drugiej strony okna mają zwykle odległość od 0,5 m do 1,5 m od podłogi. {{Incode|Wysokość parapetu}} można ustawić tylko podczas początkowego tworzenia okna lub drzwi z ustawienia wstępnego. Po wstawieniu okna lub drzwi można zmodyfikować ich położenie, edytując wektor **Pozycja** `[x, y, z]` bazowego [szkicu](Sketcher_Workbench/pl.md).



## Tworzenie niestandardowych drzwi i okien 

8\. Przejdź do [szkicownika](Sketcher_Workbench/pl.md). Wybierz część ściany po prawej stronie, która nie ma drzwi, kliknij na [utwórz szkic](Sketcher_NewSketch/pl.md). Wybierz **Płaska ściana** jako metodę mocowania. Jeśli istniejąca geometria zasłania widok, kliknij [Widok przekroju](Sketcher_ViewSection/pl.md), aby ją usunąć.

9\. Narysuj efektowny szkic zawierający trzy zamknięte krzywe. Upewnij się, że nałożysz wiązania na wszystkie krzywe.

  9.1. Zewnętrzna krzywa jest największa i definiuje główne wymiary obiektu okna oraz wielkość otworu tworzonego, gdy jest on osadzony w [ścianie](Arch_Wall/pl.md). Upewnij się, że wymiary są odpowiednio nazwane, na przykład `Szerokość` i `Wysokość`. Wiązanie również określa krzywiznę zewnętrznej krzywej. Nadaj mu odpowiednią nazwę, na przykład `HeightCurve`.
  9.2. Druga krzywa jest przesunięta od zewnętrznej krzywej, i razem z nią definiują szerokość stałej ramy okna. Nazwij przesunięcie odpowiednio, na przykład `FrameFixedOffset`. Będzie ono używane zarówno do górnego pionowego, jak i poziomego przesunięcia. Dolne przesunięcie, jeśli ustawione na zero, spowoduje dotknięcie stałej ramy dolnej krawędzi okna. Można to wykorzystać do modelowania drzwi zamiast okna. Nadaj mu odpowiednią nazwę, na przykład `FrameFixedBottom`.
  9.3. Trzecia, najbardziej wewnętrzna krzywa jest przesunięta od drugiej krzywej, i razem z nią definiują ramę okna, która może być otwierana. Najbardziej wewnętrzna krzywa również określa wielkość panelu szklanego. Ponownie, nadaj znaczące nazwy tym przesunięciom, na przykład `FrameInnerOffset` i `FrameInnerBottom`.
  9.4. Aby z powodzeniem zbudować szkic, użyj wiązań poziomych *([Wiązanie poziome](Sketcher_ConstrainHorizontal/pl.md))* i pionowych *([Wiązanie pionowe](Sketcher_ConstrainVertical/pl.md))* dla prostych boków; użyj pomocniczej geometrii konstrukcyjnej *([Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md))*, oraz wiązań styczności *([Wiązanie styczności](Sketcher_ConstrainTangent/pl.md))* do poprawnego umieszczenia łuków kołowych na górze. Ponieważ okno jest symetryczne, rozważ używanie wiązań równości *([Wiązanie równości](Sketcher_ConstrainEqual/pl.md))*, symetrii *([Wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md))*, oraz punktu na obiekcie *([Zwiąż punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md))* tam, gdzie to ma sens.

![](images/04_T02_window_constraints_outer_frame.png )



*align=center|Wiązania dla zewnętrznych linii szkicu tworzących okno.*

![](images/05_T02_window_constraints_inner_frame.png )



*align=center|Wiązania dla wewnętrznych linii szkicu tworzących okno.*

10\. Gdy szkic zostanie w pełni związany, naciśnij **Zamknij**, aby wyjść ze szkicu *([Zamknij szkic](Sketcher_LeaveSketch/pl.md))*.

:   10.1. Ponieważ powierzchnia ściany została wybrana podczas początkowego etapu tworzenia szkicu, szkic jest współpłaszczyznowy z tą powierzchnią. Może jednak znajdować się w niewłaściwym położeniu, z dala od ściany. W takim przypadku należy dostosować **Pozycję** w **Odsunięciu dołączenia**. Ustaw własciwość **Pozycja** na `[4 m, 1 m, 0 m]`, aby szkic był wyśrodkowany na ścianie i znajdował się metr nad poziomem podłogi.
:   10.2. Nazwane więzy można zobaczyć w **Wiązaniach**. Wartości można zmodyfikować, aby szkic natychmiast zmienił wymiary.

<img alt="" src=images/07_T02_window_sketch_in_wall.png  style="width:600px;">



*align=center|Szkic okna przesunięty do żądanej pozycji na ścianie.*

<img alt="" src=images/06_T02_window_sketch_properties_constraints.png  style="width:600px;">



*align=center|Nazwane wiązania szkicu, które można modyfikować bez wchodzenia do szkicu.*

11\. Wróć do środowiska pracy [Architektura](Arch_Workbench/pl.md) i po wybraniu nowego {{Incode|Sketch002}} użyj narzędzia [Okno](Arch_Window/pl.md). Okno zostanie utworzone i zrobi dziurę w ścianie. Okno zostało utworzone z niestandardowego szkicu, a nie z ustawienia wstępnego, więc należy je edytować, aby poprawnie wyświetlić jego komponenty, czyli stałą ramę, wewnętrzną ramę i szklany panel.

<img alt="" src=images/08_T02_window_basic_in_wall.png  style="width:600px;">



*align=center|Niestandardowe okno utworzone na podstawie szkicu. Nadal nie ma odpowiedniej ramy ani szyby.*



## Konfigurowanie okna niestandardowego 

12\. W widoku drzewa wybierz {{Incode|Sketch002}} leżący pod {{Incode|Oknem}} i naciśnij **Spacja** lub zmień właściwość **Widoczność** na {{TRUE/pl}}.

13\. Kliknij dwukrotnie {{Incode|Okno}} w widoku drzewa, aby rozpocząć jego edycję.

:   13.1. Wewnątrz okna dialogowego `Elementy okna` znajdują się dwa panele, `Polilinie` i `Komponent`. Dostępne są trzy polilinie `Wire0`, `Wire1` i `Wire2` oraz jeden komponent `Default`. Polilinie odnoszą się do zamkniętych pętli, które zostały narysowane w szkicu. Komponenty definiują obszary w szkicu, które zostaną wyciągnięte w celu utworzenia ramy lub szklanych paneli o rzeczywistej grubości. Obszary te są ograniczone przez polilinie. Okno utworzone z ustawienia wstępnego ma już dwa komponenty, `OuterFrame` i `Glass`. Okno niestandardowe musi być edytowane, aby miało podobną strukturę.

![](images/09_T02_window_edit_default.png )



*align=center|Okno dialogowe do edycji okna lub drzwi.*


:   13.2. Kliknij {{Incode|Default}} i kliknij przycisk **Usuń**, aby go usunąć.





:   13.3. Kliknij **Dodaj**. Zostaną wyświetlone właściwości nowego komponentu, takie jak `Nazwa`, `Typ`, `Polilinie`, `Grubość`, `Przesunięcie`, `Zawias` i `Tryb otwierania`. Nadaj nazwę, na przykład `OuterFrame`, wybierz `Rama` dla `Typu` i kliknij `Wire0`, a następnie `Wire1`; powinny one zostać podświetlone w oknie widoku 3D. Dodaj małą wartość dla `Grubość`, `15 mm` i zaznacz pole wyboru, aby dodać wartość domyślną. Wartość domyślna to długość przypisana do właściwości **Rama**. Podobną wartość domyślną można przypisać do właściwości **Odsunięcie**. Kliknij przycisk **+Utwórz/aktualizuj komponent**, aby zakończyć edycję komponentu.





:   13.4. Kliknij **Dodaj**. Nadaj inną nazwę, taką jak `InnerFrame`, wybierz `Rama` dla własciwości `Typ` i kliknij `Wire1`, a następnie `Wire2`. Dodaj odpowiednią wartość właściwości `Grubość`, `60 mm` i `Odsunięcie`, `15 mm`. Następnie kliknij przycisk **+Utwórz/aktualizuj komponent**.





:   13.5. Kliknij **Dodaj**. Nadaj inną nazwę, na przykład `Glass`, wybierz `Panel szklany` dla własciwości `Typ` i kliknij `Wire2`. Dodaj sensowną `Grubość`, `10 mm`, i `Odsunięcie`, `40 mm`. Następnie kliknij przycisk **+Utwórz / aktualizuj komponent**. Jeśli którykolwiek z trzech komponentów wymaga modyfikacji, wybierz go i naciśnij przycisk **Edycja**. Modyfikacje zostaną zapisane dopiero po naciśnięciu przycisku **+Utwórz / aktualizuj komponent**.

![](images/10_T02_window_edit_components.png )



*align=center|Edytowanie wcześniej zdefiniowanego elementu okna lub drzwi.*


:   13.6. Jeśli wszystko jest ustawione, kliknij **Zamknij**, aby zakończyć edycję okna. Szkic może zostać ponownie ukryty, ale w oknie będą widoczne różne elementy stałe dla `OuterFrame`, `InnerFrame` i `Glass`. Podaj wartość {{Incode|100 mm}} do **Frame**, aby przypisać domyślną grubość, która zostanie dodana do wartości określonej w elemencie {{Incode|OuterFrame}}.

![](images/11_T02_window_property_view.png )



*align=center|Widok właściwości okna, aby dodać domyślną długość ramki, długość przesunięcia i inne opcje.*

<img alt="" src=images/12_T02_window_finished.png  style="width:600px;">



*align=center|Gotowe okno z odpowiednimi elementami osadzonymi w ścianie.*



## Powielanie niestandardowego okna 

14\. W widoku drzewa wybierz `Okno` i jego bazowy `Szkic002`. Następnie przejdź do **Edycja → Powiel zaznaczony obiekt** i odpowiedz **Nie**, jeśli pojawi się pytanie o powielenie niezaznaczonych zależności. Nowe obiekty {{Incode|Okno001}} i {{Incode|Szkic003}} pojawią się w tym samym miejscu co oryginalne elementy.

Jeśli okno już istnieje i wymaga przeniesienia, jak miało to miejsce w przypadku zduplikowanego obiektu `Okno001`, szkic musi zostać przemapowany na inną płaszczyznę. Dokonanie tego przenosi zarówno szkic, jak i okno, ale to drugie nie aktualizuje automatycznie swojej normalnej, więc ma niewłaściwe informacje o ekstruzji. Normalna musi zostać obliczona ręcznie i wpisana do **Normalnej**.

![](images/13_T02_sketch_attachment_edit.png )



*align=center|Okno dialogowe do edycji płaszczyzny mocowania szkicu.*

16\. Możesz dostosować wymiary nowego okna, zmieniając nazwane parametry w `Sketch003` pod włąściwością **Wiązania**, na przykład ustaw wartość parametru `Wysokość` na `2 m`, a wartość parametru `Stała dolna część ramy` na `0 m`. Następnie naciśnij **Ctrl** + **R**, aby [przeliczyć](Recompute.md) model. Jeśli ściana nie pokazuje większego otworu dla nowego okna, wybierz ścianę w widoku drzewa, kliknij prawym przyciskiem myszy i wybierz `Zaznacz do przeliczenia`, a następnie ponownie naciśnij **Ctrl**+**R**.

17\. Operacje te zmieniły położenie nowego okna, ale otwór w ścianie nie wygląda prawidłowo. Jest pochylony, tzn. otwór nie jest prostopadły do lica ściany, a nawet może przecinać inne części ściany. Problem polega na tym, że {{Incode|Okno001}} zachował informacje **Normal** oryginalnego {{Incode|Okna}}.

<img alt="" src=images/14_T02_sketch_2_attached_slanted.png  style="width:600px;">



*align=center|Nieprawidłowy otwór w ścianie z powodu złej normalnej okna.*



## Normalne drzwi i okien 

18\. Każdy obiekt [okna](Arch_Window/pl.md) kontroluje wyciągnięcie swojego korpusu i otwór, który jest tworzony w ścianie hosta za pomocą **Normalnej**.

Normalna jest wektorem `[x, y, z]`, który wskazuje kierunek prostopadły do ściany. Gdy okno lub drzwi są tworzone za pomocą narzędzia [Okno](Arch_Window/pl.md) bezpośrednio nad obiektem [ściana](Arch_Wall/pl.md), normalna jest automatycznie obliczana, a powstałe okno lub drzwi są prawidłowo wyrównane. Pierwsze dwa obiekty, {{Incode|Drzwi}} i {{Incode|Drzwi001}}, zostały utworzone w ten sposób.

W podobny sposób, gdy szkic jest tworzony poprzez wybór powierzchni płaskiej, jest on orientowany na tej płaszczyźnie. Następnie, gdy używane jest narzędzie [Okno](Arch_Window/pl.md), okno będzie używać jako normalnej kierunku prostopadłego do szkicu. Tak było w przypadku trzeciego obiektu, niestandardowego okna.

Jeśli okno już istnieje i wymaga przeniesienia, jak miało to miejsce w przypadku zduplikowanego obiektu `Okno001`, szkic musi zostać przemapowany na inną płaszczyznę. Dokonanie tego przenosi zarówno szkic, jak i okno, ale to drugie nie aktualizuje automatycznie swojej normalnej, więc ma niewłaściwe informacje o ekstruzji. Normalna musi zostać obliczona ręcznie i wpisana do właściwości **Normal**.

Trzy wartości wektora normalnego są obliczane w następujący sposób. 
```python
x = -sin(kąt)
y = cos(kąt)
z = 0
``` Gdzie `angle` jest kątem lokalnej osi Z szkicu względem globalnej osi Y.

Kiedy szkic jest tworzony, zawsze posiada dwie osie: lokalną X *(czerwoną)* i lokalną Y *(zieloną)*. Jeśli szkic jest mapowany na globalną płaszczyznę roboczą XY, to te osie są wyrównane. Ale jeśli szkic jest mapowany na globalne płaszczyzny XZ lub YZ, jak ma to miejsce z oknami i drzwiami *(szkice stoją pionowo)*, to lokalna oś Z *(niebieska)* tworzy kąt ze globalną osią Y. Ten kąt zmienia się od -180 do 180°. Kąt jest uważany za dodatni, jeśli otwiera się przeciwnie do ruchu wskazówek zegara, a jest ujemny, jeśli otwiera się zgodnie z ruchem wskazówek zegara, zaczynając od globalnej osi Y.

<img alt="" src=images/15_T02_sketch_local_coordinates.png  style="width:600px;">



*align=center|Lokalne współrzędne szkicu, który jest usytuowany "na stojąco", czyli odwzorowany na globalną płaszczyznę XZ.*

<img alt="" src=images/16_T02_sketch_correct_normal_direction.png  style="width:600px;">



*align=center|Zamierzone kierunki normalnych dla każdych drzwi i okien.*

Jeśli spojrzymy na geometrię utworzoną do tej pory, zobaczymy następujące normy.

`Drzwi`
:   Lokalne Z jest wyrównane z globalnym Y, dlatego `angle` wynosi zero. Wektor normalny to:


```python
x = -sin(0) = 0
y = cos(0) = 1
z = 0
```

lub **Normal** to `[0, 1, 0]`.

`Drzwi001`
:   Lokalne Z jest obrócone o 90° względem globalnego Y, dlatego `angle` wynosi 90 *(dodatnie, ponieważ otwiera się przeciwnie do ruchu wskazówek zegara)*. Wektor normalny to:


```python
x = -sin(90) = -1
y = cos(90) = 0
z = 0
```

lub **Normal** to `[-1, 0, 0]`.

`Okno`
:   Lokalne Z jest obrócone o 45° względem globalnego Y, dlatego `angle` wynosi 45 *(dodatnie, ponieważ otwiera się przeciwnie do ruchu wskazówek zegara)*. Wektor normalny to


```python
x = -sin(45) = -0.7071
y = cos(45) = 0.7071
z = 0
```

lub **Normal** to `[-0.7071, 0.7071, 0]`.

`Okno001`
:   Kierunek lokalny Z jest określany za pomocą narzędzia [Wymiar](Draft_Dimension/pl.md), mierząc kąt, jaki ślad ściany tworzy *(`polilinia`)* z globalną osią Y lub dowolną linią wyrównaną do niej. Ten kąt wynosi `26,57`. Pożądany kąt jest dopełnieniem do tego, czyli 90 - 26,57 = 63,43.

Oznacza to, że lokalna oś Z jest obrócona o 63,43 stopnia w stosunku do globalnej osi Y, dlatego `angle` wynosi -63,46 *(ujemny, ponieważ otwiera się zgodnie z ruchem wskazówek zegara)*. Wektor normalny to 
```python
x = -sin(-63.43) = 0.8943
y = cos(-63.43) = 0.4472
z = 0
``` Dlatego **Normalna** powinien zostać zmieniona na `[0.8943, 0.4472, 0]`.

Po wprowadzeniu tych zmian ponownie przelicz model za pomocą **Ctrl** + **R**. Jeśli ściana nie zaktualizuje otworu, zaznacz ją w widoku drzewa, kliknij prawym przyciskiem myszy i wybierz `Zaznacz do przeliczenia`, a następnie ponownie naciśnij **Ctrl** + **R**.

19\. Orientacja wytłoczenia okna jest rozwiązana, wraz z otworem w ścianie.

<img alt="" src=images/17_T02_sketch_2_attached_correctly.png  style="width:600px;">



*align=center|Prawidłowy otwór w ścianie dzięki odpowiedniej normalności okna.*



## Uwagi końcowe 

20\. Jak pokazano, początkowe umieszczenie [Okna](Arch_Window/pl.md) jest bardzo ważne. Użytkownik powinien:

-   użyć narzędzia [Okna](Arch_Window/pl.md), aby wstawić i automatycznie wyrównać ustawienie wstępne do ściany, lub
-   zmapować szkic do żądanej ściany, a następnie zbudować okno.

Jeśli okno już istnieje i musi zostać przeniesione, szkic pomocniczy powinien zostać przemapowany na nową płaszczyznę, a **Normal** okna musi zostać ponownie przeliczone.

Nowy kierunek normalny można uzyskać, mierząc `angle` nowej ściany w odniesieniu do globalnej osi Y, biorąc pod uwagę, czy kąt ten jest dodatni *(przeciwnie do ruchu wskazówek zegara)* czy ujemny *(zgodnie z ruchem wskazówek zegara)* i używając prostego wzoru. 
```python
x = -sin(angle)
y = cos(angle)
z = 0
```

Aby potwierdzić poprawność operacji, bezwzględna wielkość wektora normalnego powinna wynosić jeden. To znaczy: 
```python
abs(N) = 1 = sqrt(x^2 + y^2 + z^2)
abs(N) = 1 = sqrt(sin^2(angle) + cos^2(angle) + z^2)
```


{{BIM_Tools_navi

}} {{Draft_Tools_navi}} {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > Tutorial custom placing of windows and doors/pl
