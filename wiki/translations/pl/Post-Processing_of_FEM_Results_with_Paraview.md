---
 TutorialInfo:l
   Topic: Post-Processing wyników MES za pomocą ParaView
   Level: średnio zaawansowany
   Time: 120 minut
   Author: http://www.freecadweb.org/wiki/index.php?title=User: HarryvL
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/download/file.php?id=103403 belka i https://forum.freecadweb.org/download/file.php?id=103557 ściana znalezione w https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734 tym wątku na forum
---

# Post-Processing of FEM Results with Paraview/pl







## Wprowadzenie

Niektóre wpisy na forum i przykładu korzystają z Paraview (PV) do przeglądania i analizy wyników ze <img alt="" src=images/_Workbench_FEM.svg  style="width:24px;"> [środowiska pracy MES](FEM_Workbench/pl.md). Ten przykład wyjaśnia podstawy przenoszenia danych ze środowiska pracy MES do PV i pokazuje niektóre opcje i ustawienia do wyświetlania danych.



## Wymagania wstępne 

-   Wersja FreeCAD kompatybilna z podaną w tym przykładzie.
-   Program [Paraview](https://www.paraview.org) pobrany bezpośrednio z [jego strony](https://www.paraview.org/download/) lub preferowanego menedżera pakietów.
    -   Ten przykład jest oparty na wersji Paraview 5.8.0 dla Windows, która była najnowszą dostępną wersją w momencie opracowywania przykładu.
-   Pliki FreeCAD używane w tym przykładzie dostępne w [tym](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734) i [tym](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&p=368315#p368315) wątku na forum FreeCAD.



## Transfer danych ze środowiska MES 

W środowisku MES podświetl obiekt CCX_Results. Następnie skorzystaj z opcji **Plik > Eksport > Wyniki MES VTK (*.vtk *.vtu)** aby wyeksportować dane VTK.



## Import danych w Paraview 

Ekran startowy pokazuje pustą przeglądarkę filtrów. Tam widoczne będą zaimportowane obiekty danych VTK i zastosowane obiekty filtrów (dla geometrii lub danych).

<img alt="" src=images/PVPic1.png  style="width:500px;">

Skorzystaj z opcji **File > Open > *.vtk** aby otworzyć plik VTK, który został wygenerowany w środowisku pracy MES.

<img alt="" src=images/PVPic2.png  style="width:500px;">

Wciśnij **Apply** w zakładce właściwości. Domyślnie spowoduje to pokazanie widoku z góry (patrząc w dół wzdłuż osi Z) geometrii.

<img alt="" src=images/PVPic3.png  style="width:400px;"> \... <img alt="" src=images/PVPic0.png  style="width:550px;">

Szarą geometrię można obejrzeć obracając widok. Lewy przycisk myszy powoduje obrót, ale niestety w trudny do kontrolowania sposób (w porównaniu z FreeCAD). Aby uzyskać przewidywalny obrót, przytrzymaj klawisze **X**, **Y** lub **Z** podczas przeciągania myszą z wciśniętym lewym przyciskiem aby obracać model odpowiednio wokół osi X, Y lub Z

<img alt="" src=images/PVPic5.png  style="width:500px;"> 

## Zapisywanie/wczytywanie stanu 

Zamiast zapisywania danych, Paraview przechowuje status (stan) akcji przeprowadzonych na zaimportowanym obiekcie VTK. Zatem, aby zapisać swoją pracę, użyj opcji **File > Save State**. **Uwaga**: nie będzie ostrzeżenia przy opuszczaniu Paraview aby zapisać stan i można stracić całą pracę opuszczając program.

Aby kontynuować z ostatniego momentu poprzedniej sesji, użyj **File > Load State**. To wymusza wskazanie pliku VTK, co oznacza, że akcje przeprowadzone w ostatniej sesji mogą też być zastosowane do nowego pliku VTK. W ten sposób, dane z różnych analiz ze środowiska pracy MES można wyświetlać w dokładnie taki sam sposób, bez żadnego dodatkowego wysiłku.



## Zwizualizuj wyniki środowiska MES 

Paraview ma wiele opcji i ustawień do wyświetlania wyników. Najpierw przyjrzymy się wyświetlaniu bazowych danych z importu na oryginalnej geometrii a następnie zobaczymy jak stosować filtry aby modyfikować geometrię. Wreszcie, skorzystamy z filtrów kalkulatora i całkowania, aby uzyskać nowe wyniki z operacji na zaimportowanych danych.



## Podstawowe dane wyświetlane na oryginalnej geometrii 

Ponieważ przeglądarka filtrów może zawierać wiele obiektów VTK i filtrów, najpierw potwierdź, że wyświetlany w niej jest odpowiedni obiekt VTK. Wybory i ustawienia do wyświetlania tego obiektu VTK mogą teraz być znalezione w zakładce Properties (właściwości). Aby upewnić się, że wszystkie ustawienia są widoczne i zgodne z tym przykładem, wciśnij przycisk Advanced Settings (zaawansowane ustawienia - symbol koła zębatego na rysunku poniżej).

<img alt="" src=images/PVPic6.png  style="width:400px;">

Pierwsze ustawienie, które możemy zmienić to sposób w jaki dane są wyświetlane na geometrii. Jest to robione w menu rozwijanym Representations. Na razie skorzystamy tylko z opcji Surface i Wireframe.

<img alt="" src=images/PVPic7.png  style="width:400px;">

Póki co nie są wyświetlane żadne wyniki. Do tego musimy zmienić opcję Coloring. Domyślna wartość to Solid Color, ale menu rozwijane pokazuje wszystkie dane skalarne, które są dostępne w zaimportowanym pliku VTK.

<img alt="" src=images/PVPic8.png  style="width:400px;">

<img alt="" src=images/PVPic9.png  style="width:400px;">

Dla celów tego przykładu wybierzemy ReinforcementRatio_x, ale łatwo można zmienić typ danych na dowolny inny.

Okno RenderView pokaże teraz wykres izokonturów wybranego typu danych oraz legendę kolorów zakresu danych.

<img alt="" src=images/PVPic10.png  style="width:700px;">

Legendę kolorów można przesunąć po ekranie do bardziej wygodnej lokalizacji i zmieni ona orientację zbliżając się do dowolnej krawędzi okna.

<img alt="" src=images/PVPic11.png  style="width:700px;">

Alternatywnie, ustawienia legendy kolorów można kontrolować bardziej szczegółowo po otwarciu okna dialogowego Edit Color Legend Properties z zakładki Properties (wciśnij ostatnią ikonę po prawej stronie).

<img alt="" src=images/PVPic12.png  style="width:400px;">

Otworzy to następujące okno z ustawieniami legendy kolorów

<img alt="" src=images/PVPic13.png  style="width:400px;">

Kolorowanie mapy izokonturów można kontrolować poprzez okno Color Map Editor, które jest aktywowane po wciśnięciu przycisku Edit w zakładce Properties:

<img alt="" src=images/PVPic12.png  style="width:300px;"> . <img alt="" src=images/PVPic15.png  style="width:300px;">

Ustaienie Color Discretization jest przydatne do ograniczenia liczby izo wartości, tworząc bardziej praktyczne zakresy dla projektowania. Domyślna wartość to 256, ale tutaj jest to 10.

<img alt="" src=images/PVPic16.png  style="width:700px;"> 

## Stosowanie filtrów do wyników środowiska MES 

Aby zmodyfikować dane bazowe lub geometrię zaimportowaną ze środowiska MES, można skorzystać z filtrów.

Tutaj omówimy tylko filtry Slice i Warp. Filtry do tworzenia wyników zbiorczych z danych bazowych będą omówione w następnej sekcji.

Aby zastosować filtr Slice, podświetl obiekt VTK, który ma być przycięty i wciśnij przycisk Slice. Alternatywnie, znajdź filtr Slice w menu Filters \> Alphabetical. Dodaje to obiekt filtra Slice do przeglądarki filtrów a lokalizacja w drzewie pokazuje, że jest on zastosowany do obiektu VTK. Pozycja w drzewie jest istotna, ponieważ filtry można stosować do różnych obiektów VTK a nawet do innych obiektów filtrów. Obiekt filtra nie może być przeciągnięty w drzewie aby zmienić obiekt, do którego jest przypisany. Docelowy obiekt można zmienić tylko poprzez opcję z menu (lub kliknięcie prawym przyciskiem myszy) Edit \> Change Input.

<img alt="" src=images/PVPic17.png  style="width:700px;">

Położenie i orientacja płaszczyzny cięcia mogą być modyfikowane poprzez przesuwanie płaszczyzny i jej wektora normalnego myszą lub poprzez zakładkę Properties. Na rysunku poniżej, początek płaszczyzny został umieszczony w środku belki (nad środkową podporą) a kierunek normalny do płaszczyzny jest skierowany ku osi X.

<img alt="" src=images/PVPic18.png  style="width:400px;">

Aby pozbyć się ramki ograniczającej, odznacz opcję Show Plane w górnej części okna dialogowego Plane Parameters.

<img alt="" src=images/PVPic19.png  style="width:700px;">

Filtr Warp by Vector można wykorzystać do wyświetlania zdeformowanej geometrii. Podświetl obiekt VTK i wciśnij przycisk Warp by Vector. Dodaje to filtr do przeglądarki filtrów. Alternatywnie, poszukaj filtra w menu Filters \> Alphabetical. Następnie wybierz Displacement (przemieszczenie) w menu rozwijanym Vectors w zakładce Properties i ustaw odpowiedni współczynnik skali. Nie zapomnij wcisnąć przycisk Apply po zmianie ustawień.

<img alt="" src=images/PVPic20.png  style="width:400px;"> . <img alt="" src=images/PVPic21.png  style="width:700px;">

Maksymalna wartość przemieszczenia to 0.98 mm.

Aby pokazać zdeformowaną geometrię nałożoną na niezdeformowaną geometrię, po prostu włącz widoczność obiektów VTK i filtra Warp poprzez kliknięcie przycisku z symbolem oka przy nich. Na następnym rysunku ustawienie Representation dla obiektu VTK zostało zmienione na Wireframe a Opacity zmniejszone na 0.5 aby zapobiec zasłanianiu zdeformowanej geometrii.

<img alt="" src=images/PVPic22.png  style="width:700px;">

**Uwaga**: Gdy dodawanych jest więcej obiektów do przeglądarki filtrów i otwartych jest więcej okien, coraz bardziej istotne staje się sprawdzanie czy właściwy obiekt jest wybrany w przeglądarce i właściwe okno jest aktywne podczas wprowadzania zmian w zakładce Properties. W przeciwnym wypadku, można stracić dużo czasu na szukaniu odpowiedniej właściwości lub zmiany właściwości mogą sprawiać wrażenie braku efektu.



## Stosowanie filtrów do uzyskiwania wyników zbiorczych z zaimportowanych danych bazowych 

Jeśli chcemy znać całkowitą ilość stali zbrojeniowej w belce lub ilość w danym przekroju, musimy przeprowadzić całkowanie (sumowanie po geometrii) danych bazowych.

Przykładowo, całkowita objętość prętów zbrojeniowych w belce w kierunku x jest uzyskiwana z całki `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)` po całej geometrii a całkowite pole powierzchni prętów zbrojeniowych w danym przekroju belki można uzyskać z całki `INTEGRATE(ReinforcementRatio_x * dy * dz)` po przekroju.

W Paraview całkowanie można przeprowadzić przy pomocy filtra Integration. Ten filtr można zastosować do całego obiektu VTK (belki) lub do obiektu Slice (przekrój poprzeczny).

Uwaga: w związku z rozbieżnością w kolejności węzłów między środowiskiem pracy MES i Paraview, całkowanie po objętości daje ujemne wyniki, tzn. `INTEGRATE( 1.0 * dx * dy *dz)` = - Objętość zamiast + Objętość.

Aby obliczyć całki musimy zastosować filtr Integration, który można znaleźć w menu Filters \> Alphabetical. Podświetl obiekt VTK i zastosuj filtr.

<img alt="" src=images/PVPic23.png  style="width:700px;">

Wciśnij przycisk **Apply** w zakładce Properties a wyniki zostaną otwarte w osobnym oknie po prawej stronie Renderview.

<img alt="" src=images/PVPic24.png  style="width:700px;">

Zanim to uporządkujemy aby uzyskać pożądany wynik, czyli `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)`, najpierw sprawdźmy jak możemy kontrolować gdzie umieszczane jest okno i co zawiera.

Najpierw zamknij okno SpreadSheetView, które zostało otwarte po prawej stronie. Następnie wciśnij ikonę podziału poprzecznego w oknie Renderview a pojawi się nowe okno z menu opcji wyświetlania. Przed wybraniem opcji upewnij się, że obiekt filtra Integration jest podświetlony w przeglądarce filtrów.

<img alt="" src=images/PVPic25.png  style="width:700px;">

Aby wyświetlić numeryczne wyniki, musimy wybrać SpreadSheet View na dole listy Create View. To wygeneruje arkusz wszystkich dostępnych wyników obiektu VTK pocałkowanych po objętości.

<img alt="" src=images/PVPic26.png  style="width:400px;">

Aby sprawdzić `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)` moglibyśmy przewinąć w prawo w tabeli, ale możemy też usunąć wszystkie niepożądane wyniki poprzez odznaczenie ich - odznacz All Columns i zaznacz **ReinforcementRatio_x**.

<img alt="" src=images/PVPic27.png  style="width:300px;"> . <img alt="" src=images/PVPic28.png  style="width:500px;">

Teraz została tylko jedna wartość w tabeli z wynikami całkowania

<img alt="" src=images/PVPic29.png  style="width:300px;">

Jak wyjaśniono wcześniej, jest to ujemna wartość całki, której szukamy. Więc całkowita objętość stali wymagana w kierunku x to 2.27e+06 mm3 (= 2272 cm3) lub 2272 cm3 \* 7.6 g/cm3 = 17267 g (= 17.3 kg). W rzeczywistości, liczba ta będzie wyższa ze względu na aspekty praktyczne (np. wymogi kotwiczenia i minimalnego zbrojenia itd.). W każdym razie, z tego wyniku można skorzystać do porównania projektów koncepcyjnych

Powyżej przedstawiono przykład całkowania zmiennej bezpośrednio wyeksportowanej ze środowiska pracy MES. W niektórych przypadkach, możemy chcieć połączyć zmienne VTK aby uzyskać nowe wyniki. Można to zrobić na kilka sposobów, ale tutaj omówimy tylko najprostszy - filtr Calculator.

Przykładowo, jeśli chcemy znać całkowite wymagane zbrojenie we wszystkich 3 kierunkach, musielibyśmy zsumować ReinforcementRatio_x, ReinforcementRatio_y i ReinforcementRatio_z.

Filtr Calculator można znaleźć jako przycisk po lewej stronie paska filtrów lub poprzez menu Filters \> Alphabetical. Nazwę uzyskiwanej zmiennej można wprowadzić w polu Result Array Name. Tu nazwiemy ją Total_Reinforcement_Ratio. Wzór można wprowadzić w polu poniżej Result Array Name. Wartości wejściowe można wybrać z menu rozwijanego Scalars i mogą one być połączone w równanie dla wyniku przy pomocy podanych operatorów. Po wciśnięciu przycisku Apply, wynik będzie dostępy jako nowa zmienna we wszystkich dalszych operacjach (np. filtr Integration) lub widokach (np. RenderView lub SpreadSheetView, zobacz poniżej).

<img alt="" src=images/PVPic30.png  style="width:700px;">

Przykładowo, możemy zastosować filtr całkowania na nowej zmiennej Total Reinforcement Ratio

<img alt="" src=images/PVPic31.png  style="width:700px;">

Pokazuje to jak całkowite wymagane wzmocnienie ma się do tych w poszczególnych kierunkach



## Całkowanie po przekroju 

W poprzedniej części omówiliśmy filtr Integration i jego zastosowanie do całego obiektu VTK. Aby zademonstrować całkowanie po przekroju, określimy tu całkowite wymagane wzmocnienie i jego środek ciężkości dla środkowego przekroju belki. Wynik końcowy jest pokazany na rysunku poniżej. Interakcja różnych obiektów może być sprawdzona w przeglądarce filtrów. Filtr przycięcia jest stosowany do obiektu VTK belki a dwa filtry Calculator są stosowane na filtrze przycięcia aby uzyskać nowe zmienne "Reinforcement_ratio_x \* z" i "Reinforcement_ratio_x \* y" z danych bazowych. Te zmienne należy pocałkować aby określić środek cięzkości wzmocnienia. Finalnie, filtry Integration są stosowane do każdego filtru Calculator aby pocałkować wyniki po przekroju (Slice). Zobacz poprzednią część przykładu aby zrozumieć działanie i ustawienia filtra Integration.

<img alt="" src=images/PVPicSlice1.png  style="width:700px;">

Zastosuj następujące ustawienia w zakładce Properties obiektu VTK:

  Properties Tab Settings          Comment
   
  Representation: Wireframe        Aby widoczny był przekrój
  Coloring: ReinforcementRatio_x   Lub dowolny inny kolor
  Styling \> Line Width: 2         Lub dowolne inne ustawienie dające satysfakcjonujący wynik

<img alt="" src=images/PVPicSlice2.png  style="width:400px;">

Następnie podświetl obiekt VTK i zastosuj filtr Slice z poniższymi ustawieniami w zakładce Properties:

  Properties Tab Settings                        Comment
   
  Plane Parameters \> Show Plane: deselect       Usuń ramki ograniczające
  Plane Parameters \> Origin: 4000 / 100 / 200   Położenie środkowego przekroju
  Plane Parameters \> Normal: 1 /0 /0            Kierunek normalny przekroju jest zwrócony ku osi X
  Coloring: ReinforcementRatio_x                 Opcjonalne
  Styling \> Line Width: 2                       Lub dowolne inne ustawienie, które daje satysfakcjonujący wynik

<img alt="" src=images/PVPicSlice3.png  style="width:400px;">

\'\'\'Ustawienia kalkulatora 1

Kalkulator 1 oblicza nową zmienną ReinforcementRatio_x \* y, którą należy pocałkować aby uzyskać współrzędne y środka ciężkości zbrojenia.

<img alt="" src=images/PVPicSlice4.png  style="width:400px;">

Po wciśnięciu Apply, nowa zmienna nazwana "ReinforcementRatio_x \* y" staje się dostępna do wyświetlania lub dalszego przetwarzania.

\'\'\'Ustawienia kalkulatora 2

Kalkulator 2 oblicza nową zmienną ReinforcementRatio_x \* z, którą należy pocałkować aby uzyskać współrzędne z środka ciężkości zbrojenia.

<img alt="" src=images/PVPicSlice5.png  style="width:400px;">

Po wciśnięciu Apply, nowa zmienna nazwana "ReinforcementRatio_x \* z" staje się dostępna do wyświetlania lub dalszego przetwarzania.

Wreszcie, dwa filtry Integration są stosowane, jeden na obiekcie Calculator1 aby pocałkować zmienną ReinforcementRatio_x \* y a drugi na obiekcie Calculator2 aby pocałkować zmienną ReinforcementRatio_x \* z. Każdy jest wyświetlany we własnym oknie z wybranym SpreadSheetView. Sposób odznaczenia wszystkich innych wyników był wyjaśniony wcześniej.

<img alt="" src=images/PVPicSlice6.png  style="width:700px;">

Wreszcie, środek ciężkości można wyznaczyć z powyższych wyników jako:

CoG_y = 55744.2 / 556.277 = 100.2 mm (dokładna wartość: 100 mm)

CoG_z = 187144 / 556.277 = 336.4 mm (dokładna wartość: 5/6 \* 400 mm)



## Całkowanie po linii 

Aby zademonstrować wizualizację i całkowanie wyników po linii, skorzystamy z przykładu 2D ciężkiej ściany przedstawionego w [tym wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=33049). Plik FreeCAD dla tego przykładu można pobrać z [tego wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734). Wyzwaniem jest wizualizacja stosunku zbrojenia wzdłuż różnych pionowych przekrojów i określenie wymaganego pola powierzchni stali z całkowania tych wyników.

Techniki wprowadzone w poprzedniej części tego przykładu nie zostaną tu powtórzone. Należy również ponownie podkreślić, że wraz z dodawaniem kolejnych obiektów do przeglądarki filtrów i otwieraniem kolejnych okien, coraz bardziej istotne staje się upewnianie się, że wybrany jest właściwy obiekt w przeglądarce filtrów i aktywne jest odpowiednie okno podczas wprowadzania zmian w zakładce Properties. Inaczej traci się wiele czasu na szukanie odpowiedniej właściwości lub zmiany właściwości wydają się nie mieć efektu.

Począwszy od obiektu VTK zaimportowanego ze środowiska pracy MES, zauważamy, że sterowanie w Paraview działa nieco inaczej na obiekcie 2D. Lewy przycisk myszy przeciąga geometrię a środkowy ją obraca. Aby ułożyć geometrię w płaszczyźnie analizy (x-y), wciśnij przycisk, który ustawia widok w ujemnym kierunku osi z.

<img alt="" src=images/PVPicLine1.png  style="width:75px;">

Do rysunku poniżej właściwość Coloring w zakładce Properties dla obiektu VTK została ustawiona na ReinforcementRatio_x.

Jedyny dodatkowy obiekt wymagany do wizualizacji zmiennej wzdłuż linii prostej to filtr Plot Over Line. Można go aktywować przy pomocy paska filtrów lub opcji Filters \> Alphabetical.

Dalej chcemy wyświetlić wymagane wzmocnienie w kierunku poziomym w pionowym przekroju pod słupem. Aby to osiągnąć w sposób pokazany poniżej, następujące ustawienia muszą zostać zmienione w zakładce Properties filtra Plot Over Line (upewnij się, że okno LineChartView i obiekt Plot Over Line są aktywne)

  Properties Tab Settings                                                Comment
   
  Line Parameters \> Point 1: 4000 / 0 / 0                               Punkt na dole ściany pod słupem
  Line Parameters \> Point 2: 4000 / 4000 / 0                            Punkt na górze ściany pod słupem
  x Axis Parameters \> x Array Name: ReinforcementRatio_x                Wyświetla ReinforcementRatio_x na osi poziomej
  Series Parameters: zaznacz tylko "arc length"                          Jest to parametr długości wzdłuż linii
  Title \> Chart Title: Mid Section                                      
  Annotation \> Show Legend: odznacz                                     Bez znaczenia dla aktualnego wyboru osi pionowej
  Left Axis \> Left Axis Title: Height Across Beam                       
  Left Axis Range \> Use Custom Range: odznacz                           Odznacz aby zmaksymalizować zakres danych wzdłuż osi
  Bottom Axis \> Bottom Axis Title: Reinforcement Ratio in x-Direction   
  Bottom Axis Range \> Use Custom Range: odznacz                         Odznacz aby zmaksymalizować zakres danych wzdłuż

<img alt="" src=images/PVPicLine2.png  style="width:700px;">

Zauważ, że odległość wzdłuż linii (długość łuku) jest zwykle na osi poziomej a zmienna, którą chcemy wyświetlić (tutaj ReinforcementRatio_x) na osi pionowej. Jednak w tym przypadku przekrój ściany jest pionowy i chcemy zobaczyć wymagane wzmocnienie po wysokości ściany, więc bardziej naturalne jest odwrócenie osi. Wymaga to jednak znacznie więcej zmian w ustawieniach w zakładce Properties filtra Plot Over Line.

Na następnych dwóch rysunkach zmienione było tylko położenie linii. Zauważ jednak, że ta zmiana automatycznie zmieni ustawienie Left Axis Range \> Use Custom Range na "select". Może to oznaczać, że wykres nie mieści się prawidłowo w oknie LineChartView. Jest zatem konieczne odznaczenie tej opcji za każdym razem gdy zmieniane jest położenie linii. Inne ustawienia pozostają jak w tabeli powyżej.

  Properties Tab Settings                          Comment
   
  Line Parameters \> Point 1: 6700 / 0 / 0         Punkt na dole ściany pod lewą stroną wycięcia
  Line Parameters \> Point 2: 6700 / 4000 / 0      Punkt na górze ściany nad lewą stroną wycięcia
  Title \> Chart Title: Section left of Cut-out    
  Left Axis Range \> Use Custom Range: odznacz     Odznacz zakres danych wzdłuż osi
  Bottom Axis Range \> Use Custom Range: odznacz   Odznacz aby zmaksymalizować zakres danych wzdłuż osi

<img alt="" src=images/PVPicLine3.png  style="width:700px;">

  Properties Tab Settings                          Comment
   
  Line Parameters \> Point 1: 10950 / 0 / 0        Punkt na dole ściany na prawej podporze
  Line Parameters \> Point 2: 10950 / 4000 / 0     Punkt na górze ściany na prawej podporze
  Title \> Chart Title: Section at Support         
  Left Axis Range \> Use Custom Range: odznacz     Odznacz aby zmaksymalizować zakres danych wzdłuż osi
  Bottom Axis Range \> Use Custom Range: odznacz   Odznacz aby zmaksymalizować zakres danych wzdłuż osi

<img alt="" src=images/PVPicLine4.png  style="width:700px;">

Całkowite wymagane wzmocnienie poziome w ostatnim przekroju może być teraz po prostu uzyskane poprzez zastosowanie filtra Integration do obiektu Plot Over Line, tzn. podświetlenie obiektu Plot Over Line w przeglądarce filtrów i dodanie filtra Integration z menu Filters \> Alphabetical.

<img alt="" src=images/PVPicLine5.png  style="width:700px;">

W zwyczajowy sposób odznacz wszystkie wyniki oprócz ReinforcementRatio_x w SpreadSheetView i odczytaj wynik jako 23.11 mm2 / mm. Aby uzyskać całkowite pole przekroju poprzecznego stali, nadal musimy dokonać mnożenia przez grubość ściany, która w tym przypadku wynowi (imponujące) 600 mm. Więc całkowite pole przekroju poprzeczneg stali przechodzącej przez przekrój w pobliżu prawej podpory to 23.11 \* 600 = 13866 mm2 = 139 cm2

Aby uzyskać bardziej praktyczny rozkład zbrojenia, moglibyśmy pocałkować powyższy wykres w częściach. Przykładowo, jeśli chcemy znać wymagane pole przekroju poprzecznego stali w górnych 400mm ściany to powinniśmy dostosować właściwości obiektu Plot Over Line w następujący sposób

  Properties Tab Settings                           Comment
   
  Line Parameters \> Point 1: 10950 / 3600 / 0      Punkt w pobliżu górnej części ściany przy prawej podporze
  Line Parameters \> Point 2: 10950 / 4000 / 0      Punkt na górze ściany przy prawej podporze
  Left Axis Range \> Use Custom Range: odznacz      Odznacz aby zmaksymalizować zakres danych wzdłuż osi
  Bottom Axis Range \> Use Custom Range: deselect   Odznacz aby zmaksymalizować zakres danych wzdłuż osi

To daje następujący wynik

<img alt="" src=images/PVPicLine6.png  style="width:700px;">

Wynik dla górnych 400 mm ściany wynosi więc 8.436 mm2 / mm. Zatem górne 10% ściany wymaga 8.44 / 23.11 \* 100% = 37% stali zbrojenia.

Ta procedura może być powtórzona aby podzielić ścianę na strefy stałego wzmocnienia.



## Reprezentacja wyników wektorowych z filtrem Glyph 3D 

Do tej pory zajmowaliśmy się tylko wartościami skalarnymi, jak stosunek zbrojenia i wypadkowe przemieszczenie. Wizualizacja wyników wektorowych, jak wektory naprężeń głównych, jest dokonywana przy pomocy filtra Glyph.

Wróćmy do obiektu danych VTK dla belki ze środkową podporą i zwizualizujmy wektory maksymalnych i minimalnych naprężeń głównych.

Podświetl obiekt danych VTK w przeglądarce filtrów i wybierz filtr Glyph z paska filtrów lub menu Filter \> Alphabetical. Następnie zastosuj następujące ustawienia w zakładce Properties obiektu filtra Glyph (zobacz tabelę i rysunek):

  Properties Tab Settings                              Comment
   
  Glyph Source \> Glyph Type: Line                     Niestety nie ma opcji dwustronnych strzałek
  Orientation \> Orientation: Major Principal Stress   Filtr Glyph bierze kierunek naprężenie głównego
  Scale \> Scale Array: Major Principal Stress         Długość linii będzie reprezentować wartość naprężeń głównych
  Scale \> Vector Scale Mode: Scale by Magnitude       
  Scale \> Scale Factor: 100                           Lub dowolne inne ustawienie dające satysfakcjonujący wynik
  Masking \> Glyph Mode: All Points                    Aby upewnić się, że wyświetlane są naprężenia w każdym węźle
  Coloring \> Solid Color                              Pojedynczy kolor daje największą przejrzystość "przepływu naprężeń"
  Coloring \> Edit \> Green                            Lub dowolne inne ustawienie dające satysfakcjonujący wynik
  Styling \> Line Width \> 2                           Lub dowolne inne ustawienie dające satysfakcjonujący wynik

<img alt="" src=images/PVPic32.png  style="width:400px;">; <img alt="" src=images/PVPic33.png  style="width:400px;">

Jeśli wszystko pójdzie dobrze, powinieneś zobaczyć następujący wynik dla pliku przykładu.

<img alt="" src=images/PVPic34.png  style="width:700px;">

Następnie dodaj kolejny filtr Glyph z następującymi ustawieniami dla minimalnych naprężeń głównych (nie zapomnij najpierw podświetlić obiekt danych VTK w przeglądarce filtrów):

  Properties Tab Settings                              Comment
   
  Glyph Source \> Glyph Type: Line                     Niestety nie ma opcji dwustronnych strzałek
  Orientation \> Orientation: Minor Principal Stress   Filtr Glyph bierze kierunek naprężeń głównych
  Scale \> Scale Array: Minor Principal Stress         Długość linii będzie reprezentować wartość naprężeń głównych
  Scale \> Vector Scale Mode: Scale by Magnitude       
  Scale \> Scale Factor: 100                           Lub dowolne inne ustawienie dające satysfakcjonujący wynik
  Masking \> Glyph Mode: All Points                    Aby upewnić się, że wyietlane są naprężenia w każdym węźle
  Coloring \> Solid Color                              Pojedynczy kolor daje największą przejrzystość "przepływu naprężeń"
  Coloring \> Edit \> Red                              Lub dowolne inne ustawienie dające satysfakcjonujący wynik
  Styling \> Line Width \> 2                           Lub dowolne inne ustawienie dające satysfakcjonujący wynik

<img alt="" src=images/PVPic35.png  style="width:700px;">

Finalny wynik pokazuje wektory maksymalnych i minimalnych naprężeń głównych nałożone na belkę z ReinforcementRatio_x.



## Eksport wyników graficznych 

Aby wyeksportować okno RenderView, podświetl okno i użyj opcji **File > Save Screenshot**


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Post-Processing of FEM Results with Paraview/pl
