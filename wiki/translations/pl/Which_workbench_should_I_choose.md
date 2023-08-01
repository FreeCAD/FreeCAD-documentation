# Which workbench should I choose/pl
Jeśli jesteś nowy w FreeCAD, są duże szanse, że zastanawiasz się, od którego [środowiska pracy](Workbenches/pl.md) powinieneś zacząć. Ta strona pomoże Ci wybrać, od czego zacząć.

Środowiska pracy to zestawy narzędzi, przycisków, paneli i innych elementów interfejsu, które są zgrupowane razem. Pomyśl o tym jak o aplikacji wewnątrz aplikacji. W programie FreeCAD, obszary robocze zazwyczaj gromadzą zestaw narzędzi dostosowanych do konkretnego celu, takich jak rysowanie 2D, projektowanie obiektów 3D, projektowanie łodzi, projektowanie trajektorii robotów, projektowanie budynków i wiele innych.

FreeCAD jest dostarczany z kilkoma [wbudowanymi środowiskami roboczymi](Workbenches/pl.md), ale [mnóstwo więcej jest dostępnych](External_workbenches/pl.md) i mogą być łatwo zainstalowane poprzez [Menedżer dodatków](Std_AddonMgr/pl.md).

Nowi użytkownicy programu FreeCAD zazwyczaj zaczynają używać i uczyć się jednego lub dwóch specyficznych środowisk pracy, a następnie odkrywają inne obszary FreeCAD i dodają do swojego zestawu umiejętności narzędzia, które uznają tam za interesujące. Zanim jednak zanurzysz się w konkretnych środowiskach roboczych, upewnij się, że przeczytałeś strony [Jak zacząć](Getting_started/pl.md) i [Nawigacja w przestrzeni 3D](Manual_Navigating_in_the_3D_view.md), ponieważ dostarczają one ogólnej wiedzy, która będzie potrzebna wszędzie podczas pracy w FreeCAD. Podręcznik [Słowo wstępne](Manual:Introduction/pl.md) to kolejny dobry sposób na odkrywanie programu FreeCAD krok po kroku, w sposób liniowy.

Pierwsze środowisko pracy, którego powinieneś użyć, zależy od tego, co zamierzasz robić z FreeCAD. Zazwyczaj widzimy nowych użytkowników przychodzących z jednym z następujących wymagań:



## Nie mam żadnego doświadczenia z CAD, a chcę zaprojektować i wydrukować jakiś obiekt przestrzenny 

Jest to prawdopodobnie najczęstszy przypadek użycia wśród nowych użytkowników programu FreeCAD, i to w czym FreeCAD jest najlepszy. Posiada on specjalne stanowisko pracy do tego celu: [środowisko pracy Projekt Części](PartDesign_Workbench/pl.md). Projekt Części zawiera również wszystkie narzędzia z [Szkicownika](Sketcher_Workbench/pl.md), więc nauczysz się i będziesz używał dwóch środowisk w jednym.

Rozpoczynając nowy model w środowisku Projekt Części, zazwyczaj najpierw będziesz musiał stworzyć [Zawartość](PartDesign_Body/pl.md). Zawartość jest jednocześnie kontenerem dla kształtów podrzędnych i rezultatem, Twoim końcowym obiektem. Pomyśl o tym, że jeden obiekt = jedna zawartość. Zawartość, choć może składać się z kilku części, powinna zawsze reprezentować jeden złożony obiekt, bez żadnych luźnych części. Większość operacji wykonywanych na lub wewnątrz zawartości zapobiegnie tworzeniu luźnych części.

Najczęściej to, co zrobisz wewnątrz zawartości, to następująca sekwencja operacji:

1.  [Narysuj zamknięty kształt 2D](Sketcher_NewSketch/pl.md) *(zwany również [szkicem](Sketcher_Workbench/pl.md))* na jakiejś płaszczyźnie w przestrzeni 3D *(na przykład na płaszczyźnie gruntu (XY) lub na ścianie istniejącej części)*. Szkice są bardzo potężną funkcją FreeCAD. Mogą one zawierać liniowe lub zakrzywione odcinki, ale także złożone elementy, takie jak wiązania czy geometria konstrukcji.
2.  [Wyciągnięcie](PartDesign_Pad/pl.md) tworzy bryłę.
3.  Użyj tej bryły jako [uzupełnienie](PartDesign_Pad/pl.md) lub [odjęcie](PartDesign_Pocket/pl.md) innej bryły.
4.  Opcjonalnie zastosuj wykończenia takie jak [zaokrąglenie](PartDesign_Fillet/pl.md) na niektórych ścianach.

I powtarzaj ten proces, aż dojdziesz do swojego ukończonego obiektu. Zobacz listę poradników poniżej, aby uzyskać bardziej dogłębne informacje i przykłady typowych procesów modelowania. Kiedy skończysz modelować swój obiekt, nadszedł czas, aby wysłać go do drukarki 3D. Oznacza to zazwyczaj:

1.  Upewnij się, że masz ustawioną drukarkę 3D i gotową aplikację do krojenia *(aplikacja odpowiedzialna za przekształcenie obiektu 3D w polecenia dla drukarki, taka jak [slic3r](https://slic3r.org/) lub [cura](https://ultimaker.com/software/ultimaker-cura))*;
2.  Wybierz swoją zawartość *(twój finalny obiekt)*.
3.  Przejdź do menu Plik -\> Eksport i wyeksportuj swój obiekt do formatu obsługiwanego przez Twoją aplikację do krojenia, zazwyczaj jest to format STL
4.  Otwórz plik STL w programie do krojenia, ustaw odpowiednie parametry dla swojej drukarki i naciśnij przycisk \"drukuj\".

W tej dokumentacji jest wiele innych miejsc, w których można dowiedzieć się więcej o przepływie pracy w środowisku Projekt Części oraz o tym, jak używać Szkicownika:

-   Czytaj więcej na stronie [Projekt części](PartDesign_Workbench/pl.md)
-   Przeczytaj więcej na stronie [Szkicownik](Sketcher_Workbench/pl.md)
-   Poradnik: [Projekt Części: tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md)
-   Poradnik: [Poradnik: Podstawy dla środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md)
-   Poradnik: [Podręcznik:Modelowanie dla projektowania produktu](Manual_Modeling_for_product_design.md)
-   Poradnik: [Eksport do formatu STL lub OBJ](Export_to_STL_or_OBJ/pl.md)



## Mam jakieś doświadczenie z SolidWorks lub czymś podobnym. Chcę zajmować się projektowaniem produktów i złożeniami 

Pierwsza część twojego przypadku użycia jest dość podobna do tej powyżej. Zazwyczaj używasz środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md), który zawiera również wszystkie narzędzia [Szkicownika](Sketcher_Workbench/pl.md). Zazwyczaj będziesz projektował jedną bryłę dla każdej pojedynczej części twojego zespołu.

Kiedy masz już swoje różne części, musisz je złożyć razem. FreeCAD nie posiada w tej chwili domyślnego, unikalnego środowiska montażowego. Istnieje raczej kilka dodatków do tworzenia złożeń, które możesz łatwo zainstalować poprzez [Menedżer dodatków](Std_AddonMgr/pl.md):

-   Środowisko pracy [A2plus](A2plus_Workbench/pl.md) dostarcza narzędzi do tworzenia złożeń wieloelementowych. Jest to najstarsze środowisko złożeń, jakie mamy w FreeCAD. Powstało zanim zaawansowane funkcje takie jak obiekty App Link były dostępne w FreeCAD, dlatego jest bardziej podstawowe i prostsze, co może być problemem lub zaletą.
-   [Złożenie 3](Assembly3_Workbench/pl.md) służy do wykonywania montażu różnych brył zawartych w jednym pliku lub w wielu dokumentach. Był to testowy obiekt App Link, który ostatecznie został włączony do kodu głównego. Jest to najbardziej złożone rozwiązanie i obsługuje takie rzeczy jak interaktywna kinematyka.
-   [Założenie 4](Assembly4_Workbench/pl.md) to rozwiązanie oparte na ulepszonym silniku wyrażeń i obiekcie App Link opracowanym w gałęzi Assembly3. Assembly4 nie działa z właściwym solverem wiązań, zamiast tego wykorzystuje silnik wyrażeń do pozycjonowania ciał względem Lokalnych Układów Współrzędnych *(LCS)*.

Wybór najlepszego zależy od Twoich wymagań i nie jest łatwo stwierdzić z góry. Sugerujemy najpierw wypróbowanie Złożenie 4, a następnie wypróbowanie Złożenie 3, jeśli potrzebujesz czegoś bardziej złożonego, lub A2Plus jest zbyt złożony dla Twoich potrzeb.



## Mam jakieś doświadczenie z AutoCAD lub czymś podobnym. Chcę robić rysunki 2D 

Chociaż FreeCAD jest przede wszystkim aplikacją 3D, posiada wszystkie narzędzia do pełnego rysowania i dodawania adnotacji do złożonych projektów 2D, takich jak plany domów, oraz do ich drukowania, eksportowania jako dokumenty PDF lub eksportowania do innych formatów obsługiwanych przez inne tradycyjne aplikacje CAD 2D, takich jak DXF lub DWG.

Podstawowym narzędziem do tworzenia projektów 2D jest środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md). Posiada ono wszystkie narzędzia powszechnie spotykane w tradycyjnych aplikacjach CAD, takie jak linie, prostokąty, łuki, krzywe złożone, wypełnienia kreskowania, teksty czy wymiary, a także narzędzia do modyfikacji obiektów, takie jak przesuwanie, obracanie, rozszerzanie, skalowanie, przesuwanie i tak dalej.

Rysowane obiekty mogą być grupowane za pomocą grup lub warstw, a tworzone rysunki mogą być eksportowane jako pliki DXF / DWG lub umieszczane w określonej skali na arkuszu reprezentującym kartkę papieru. Arkusz ten można następnie wydrukować lub wyeksportować jako plik PDF.

W odróżnieniu jednak od tradycyjnych aplikacji CAD 2D, FreeCAD jest przede wszystkim aplikacją CAD 3D. Tak więc pierwszym krokiem, który będziesz musiał wykonać rozpoczynając pracę z narzędziami Rysunku Roboczego jest wybór płaszczyzny przestrzeni 3D, w której będziesz chciał narysować swój projekt. Tradycyjnie robi się to w płaszczyźnie XY, która byłaby poziomą płaszczyzną leżącą na ziemi, na wysokości zero.

W środowisku pracy Rysunek Roboczy robisz to poprzez ustawienie swojej [płaszczyzny roboczej](Draft_SelectPlane/pl.md). Płaszczyzna robocza to miejsce, w którym będą wykonywane kolejne operacje rysunkowe *(linia, prostokąt itp.)*. Możesz zmienić płaszczyznę roboczą w każdej chwili, ale możesz również skonfigurować program FreeCAD tak, aby zawsze rozpoczynał pracę z płaszczyzną roboczą ustawioną na płaszczyznę XY gruntu i nigdy więcej się tym nie przejmować.

Upewnij się, że przeczytałeś, jak [Nawigacja w oknie widoku 3D](Manual:Navigating_in_the_3D_view/pl.md), abyś wiedział, jak ustawić punkt widzenia, aby patrzeć bezpośrednio na płaszczyznę roboczą z góry, i wrócić do tego punktu, jeśli się od niego oddalisz. Zapewni Ci to wygodną przestrzeń roboczą, podobną do tej, którą znasz z aplikacji.

Po ustawieniu płaszczyzny roboczej, wszystko co musisz zrobić to zacząć rysować. Zapoznaj się z [listą dostępnych narzędzi](Draft_Workbench/pl.md) środowiska Rysunek Roboczy aby dowiedzieć się co tam jest, ale w zasadzie zachowują się one podobnie do innych aplikacji CAD 2D. Na przykład narysuj linie, które reprezentują granicę terenu, lub prostokąt, który reprezentuje dom.

Pracując w środowisku Rysunek Roboczy, zazwyczaj rysuje się w rozmiarze rzeczywistym. Jeden metr to jeden metr. Upewnij się, że ustawiłeś swoje [jednostki](Units/pl.md) zgodnie z Twoimi upodobaniami. Korzystaj również z [narzędzia przyciągania](Draft_Snap/pl.md), aby precyzyjnie pozycjonować swoje punkty.

Grupowanie obiektów może być wykonane przy użyciu [grup](Std_Group/pl.md) lub [warstw](Draft_Layer/pl.md). Warstwy to po prostu grupy, które mogą kontrolować kolor i inne aspekty obiektów umieszczonych wewnątrz nich.

Kiedy Twój rysunek jest gotowy do eksportu, po prostu zaznacz wszystko co chcesz wyeksportować *(lub grupy / warstwy je zawierające)* i użyj opcji z menu Plik -\> Eksportuj, oraz wybierz format DXF lub DWG. Zauważ, że możliwości DWG w FreeCAD zależą od [zewnętrznego oprogramowania](Draft_DXF/pl#DWG.md).

Aby wydrukować lub wyeksportować swój rysunek jako plik PDF, skorzystaj ze środowiska [Rysunek Techniczny](TechDraw_Workbench/pl.md). Rysunek Techniczny służy do tworzenia arkuszy do druku, umieszczania na nich szablonów i innych elementów graficznych stron oraz widoków Twoich modeli 2D lub 3D. Typowy przebieg pracy ze środowiskami Rysunek Roboczy i Rysunek Techniczny obejmuje:

1.  Ustaw swoją płaszczyznę roboczą jako płaszczyznę XY *(górną)*.
2.  Utwórz swój rysunek używając narzędzi Rysunku Roboczego.
3.  Upewnij się, że pogrupowałeś wszystkie elementy swojego rysunku w grupy lub warstwy i masz jedną grupę główną lub kontener warstw, który zawiera wszystkie warstwy lub podgrupy Twojego rysunku. Ułatwia to umieszczenie go w jednym miejscu na arkuszu. Zazwyczaj tworzysz inną grupę dla każdego rysunku, dzięki czemu możesz kontrolować ich pozycje i skale niezależnie na arkuszu.
4.  Przełącz się na środowisko pracy Rysunek Techniczny.
5.  Utwórz nową stronę.
6.  Ustaw lub dostosuj jej szablon.
7.  Dla każdego z rysunków roboczych użyj narzędzia [Wstaw widok rysunku](TechDraw_DraftView/pl.md) aby utworzyć jego widok na arkuszu.
8.  Dostosuj skalę i położenie każdego widoku.
9.  Wydrukuj lub zapisz arkusz jako plik PDF z menu Rysunek Techniczny.

Tutaj znajduje się więcej materiałów o środowisku pracy Rysunek Techniczny i rysowaniu 2D w FreeCAD:

-   Wszystkie narzędzia środowiska pracy[Rysunek Roboczy](Draft_Workbench/pl.md)
-   Poradnik: [Tradycyjne kreślenie 2D](Manual:Traditional_2D_drafting/pl.md)
-   Poradnik: [Poradnik dla środowiska pracy Rysunek Roboczy](Draft_tutorial/pl.md)
-   Poradnik: [Poradnik: Podstawy dla środowiska pracy Szkicownik](Basic_Sketcher_Tutorial/pl.md). Szkicownik może być użyty do tworzenia znacznie bardziej złożonych i zaawansowanych elementów 2D niż można to zrobić w środowisku Rysunek Roboczy.



## Mam jakieś doświadczenie z Revitem lub ArchiCADem lub inną aplikacją BIM. Chcę się zająć modelowaniem BIM 

Twoje środowisko pracy to [BIM](BIM_Workbench/pl.md). Nie jest on częścią wbudowanych narzędzi FreeCAD, musisz go zainstalować poprzez [Menadżer dodatków](Std_AddonMgr/pl.md). Środowisko pracy [Architektura](Arch_Workbench/pl.md), dołączone do programu FreeCAD, jest minimalnym podzbiorem narzędzi środowiska pracy BIM, który pozwoli na poprawne otwieranie modeli BIM na każdej instalacji FreeCAD, nawet bez środowiska pracy BIM.

Środowisko pracy BIM zawiera również większość narzędzi [Rysunku Roboczego](Draft_Workbench/pl.md), i używa tej samej koncepcji [płaszczyzny roboczej](Draft_SelectPlane/pl.md), gdzie twoje kolejne obiekty będą leżeć na bieżącej płaszczyźnie roboczej.

W programie FreeCAD nie ma obowiązkowej organizacji konstrukcji budynku *(np. piętra)*. Możesz wybrać grupowanie swoich obiektów BIM w [grupy](Std_Group/pl.md) lub [warstwy](Draft_Layer/pl.md), podobnie jak w Rysunku Roboczym, ale możesz również wykorzystać obiekt [Część budowli - piętro](Arch_BuildingPart/pl.md) do reprezentowania poziomów lub budynków i osiągnąć podobną organizację, jaką zwykle można znaleźć w innych aplikacjach BIM.

Większość narzędzi BIM, takich jak ściany i okna, stworzy obiekt samodzielnie, wybierając opcje w panelu zadań i klikając punkty w widoku 3D, ale wszystkie one mogą również działać poprzez wcześniejsze wybranie innych obiektów. Na przykład możesz narysować ścianę, wybierając narzędzie Ściana, a następnie klikając dwa punkty, ale możesz też najpierw narysować linię lub polilinię, a następnie, mając wybrany ten obiekt, nacisnąć przycisk Ściana. Ściana zostanie zbudowana na szczycie tej polilinii i użyje jej jako linii bazowej. Jeśli zmodyfikujesz polilinię, ściana zmieni się odpowiednio.

Różne narzędzia BIM, takie jak ściana, okno, kolumna, itd\... wyprodukują odpowiedni obiekt ściany, okna lub kolumny. Jednak typ wytworzonego obiektu jest określony przez i tylko przez jego właściwość **typ IFC**, którą można zmienić w dowolnym momencie. Można więc użyć narzędzia ściana do modelowania np. belki. Należy tylko zmienić jego typ IFC z \"ściana\" na \"belka\".

Podobnie, każdy obiekt utworzony za pomocą innego środowiska pracy lub nawet innej aplikacji może stać się obiektem BIM. Używając narzędzia [Komponent](Arch_Component/pl.md), można dodać właściwości BIM *(w tym właściwość IFC Type)* do dowolnego innego obiektu.

Po utworzeniu modelu BIM, który jest niczym innym jak modelem 3D, gdzie wszystkie obiekty mają zdefiniowane właściwości BIM/IFC, można wykonać kilka operacji takich jak:

-   Wyeksportowanie go do formatu [IFC](Arch_IFC/pl.md) poprzez wybranie swojego kontenera głównego modelu *(grupy lub części budynku)* i wybranie z menu opcji **Plik -> Eksport** oraz formatu IFC. Format IFC jest standardowym formatem wymiany dla modeli BIM i jest obsługiwany przez wszystkie aplikacje BIM.
-   Wyodrębnij rysunki 2D takie jak rzuty kondygnacji, przekroje lub elewacje. Można to zrobić umieszczając [płaszczyzny przekroju](Arch_SectionPlane/pl.md) w swoim modelu
-   Tworzenie rysunków z tych płaszczyzn przekroju. Jest to wykonywane albo *(i najlepiej)* jako krok pośredni, przy użyciu narzędzia [Widok 2D kształtu](Draft_Shape2DView/pl.md), które może być następnie opisane narzędziami środowiska Rysunek Roboczy, lub bezpośrednio umieszczone na arkuszu Rysunek Techniczny przy użyciu narzędzia [Widok architektoniczny](TechDraw_ArchView/pl.md).
-   Tworzenie harmonogramów lub tabel ilościowych przy użyciu narzędzia [Obmiar](Arch_Schedule/pl.md) i [Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md).
-   Eksportuj swój model do innej aplikacji do tworzenia renderingów 3D, takiej jak [Blender](https://blender.org). Zwykle robi się to poprzez zaznaczenie obiektów, które chcesz wyeksportować, i użycie opcji z menu **Plik -> Eksport** i wybranie formatu dobrze obsługiwanego przez te aplikacje, np. OBJ lub DAE. Należy pamiętać, że dla Blendera dostępny jest [importer FreeCAD](https://gist.github.com/yorikvanhavre/e873d51c8f0e307e333fe595c429ba87), który umożliwia mu bezpośrednie otwieranie plików FreeCAD.

Oto kolejne materiały do zapoznania się z modelowaniem BIM w programie FreeCAD:

-   Narzędzia środowiska pracy [BIM](BIM_Workbench/pl.md)
-   Poradniki: [Architektura i BIM](Tutorials/pl#Architektura_i_BIM.md)



## Nie mam planu na konkretne działanie. Chcę tylko poznać FreeCAD 

Najlepszym sposobem jest prawdopodobnie przejrzenie [Podręcznik FreeCAD](Manual:Introduction/pl.md). Podręcznik został zaprojektowany jako płynna, nadająca się do druku sekwencja rozdziałów, które delikatnie poprowadzą Cię przez wszystko, co trzeba wiedzieć o programie FreeCAD.



---
⏵ [documentation index](../README.md) > Which workbench should I choose/pl
