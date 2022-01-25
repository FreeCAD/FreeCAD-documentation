---
- TutorialInfo:/pl
   Topic:Modelowanie
   Level:średniozaawansowany
   Time:...
   Author:[Yorik](User_Yorik.md)
   FCVersion:0.14
---

# Arch tutorial/pl





![](images/Arch_tutorial_00.jpg )

## Wprowadzenie

Ten poradnik ma na celu przekazać Państwu podstawy do pracy z środowiskiem pracy [Architektura](Arch_Workbench/pl.md). Postaram się uczynić go wystarczająco łatwym, abyś nie potrzebował żadnego wcześniejszego doświadczenia z programem FreeCAD, ale posiadanie doświadczenia z aplikacjami 3D lub [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) będzie pomocne. W każdym razie, powinieneś być przygotowany na poszukiwanie dalszych informacji o tym jak działa program FreeCAD w [Dokumentacji FreeCAD na Wiki](Main_Page/pl.md). Strona [Jak zacząć](Getting_started/pl.md) stanowi minimum do zapoznania się, jeśli nie miałeś wcześniej doświadczenia z programem FreeCAD. Sprawdź również naszą sekcję [poradniki](Tutorials/pl.md), a na stronie [youtube](http://www.youtube.com/results?search_query=freecad) znajdziesz również dużo więcej wideo poradników dla FreeCAD.

Celem środowiska pracy [Architektura](Arch_Workbench/pl.md) jest zaoferowanie kompletnego dla [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) przepływu pracy wewnątrz FreeCAD. Ponieważ jest on wciąż rozwijany, nie oczekuj, że znajdziesz tutaj te same narzędzia i poziom ukończenia, co w przypadku rozwiniętych alternatyw komercyjnych, takich jak [Revit](http://en.wikipedia.org/wiki/Revit) lub [ArchiCAD](http://en.wikipedia.org/wiki/Archicad), ale z drugiej strony, FreeCAD jest używany w znacznie większym zakresie niż te aplikacje. [Architektura](Arch_Workbench/pl.md) znacząco wykorzystuje inne dziedziny, do których FreeCAD się odwołuje i oferuje niektóre funkcje rzadko spotykane w tradycyjnych aplikacjach BIM.

Oto, przykładowo prezentuję, kilka interesujących funkcji FreeCAD w środowisku [Architektura](Arch_Workbench/pl.md), które trudno znaleźć w innych aplikacjach BIM:

-   Obiekty architektoniczne są zawsze bryłami. Z silnego mechanicznego zaplecza FreeCAD nauczyliśmy się, jak ważna jest praca z obiektami brył. Zapewnia to znacznie bardziej bezbłędny przepływ pracy i bardzo niezawodne działanie funkcji logicznych. Ponieważ wycinanie obiektów 3D płaszczyzną 2D, w celu wyodrębnienia przekrojów, jest również operacją logiczną, można od razu dostrzec znaczenie tego punktu.

-   Obiekty architektoniczne zawsze mogą mieć dowolny kształt. Bez żadnych ograniczeń. Ściany nie muszą być pionowe, płyty nie muszą wyglądać jak płyty. Każdy obiekt bryły może zawsze stać się dowolnym obiektem architektonicznym. Bardzo złożone rzeczy, zwykle trudne do zdefiniowania w innych aplikacjach BIM, jak płyta podłogowa wyginająca się i stająca się ścianą *(tak Zaha Hadid, to o Tobie mówimy)*, nie stanowią żadnego szczególnego problemu w FreeCAD.

-   Cała moc FreeCAD jest w zasięgu twojej ręki. Możesz projektować obiekty architektoniczne za pomocą dowolnego innego narzędzia programu FreeCAD, takiego jak [Projekt Części](PartDesign_Workbench/pl.md), a kiedy będą gotowe, przekonwertuj je na obiekty architektoniczne. Nadal zachowają one swoją pełną historię modelowania i będą w pełni edytowalne. Również Środowisko pracy [Architektura](Arch_Workbench/pl.md) odziedziczyło wiele z funkcji środowiska [Rysunek Roboczy](Draft_Workbench/pl.md), takich jak [przyciąganie](Draft_Snap/pl.md) i [płaszczyzny robocze](Draft_SelectPlane/pl.md).

-   Środowisko pracy [Architektura](Arch_Workbench/pl.md) jest bardzo przyjazne dla [siatek](Mesh_Workbench/pl.md). Możesz łatwo zaprojektować model architektoniczny w aplikacji opartej na siatce, takiej jak [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) lub [SketchUp](http://en.wikipedia.org/wiki/Sketchup) i zaimportować go we FreeCAD. Jeśli zadbałeś o jakość swojego modelu, a jego obiekty to różnorodne bryły, przekształcenie ich w obiekty architektoniczne wymaga jedynie naciśnięcia przycisku.

W czasie, gdy piszę ten artykuł, środowisko pracy [Architektura](Arch_Workbench/pl.md), podobnie jak reszta programu FreeCAD, cierpi na pewne ograniczenia. Większość z nich jest jednak ciągle dopracowywana i zniknie w przyszłości.

-   FreeCAD nie jest aplikacją 2D. Jest on przygotowany do pracy z elementami 3D. Istnieje rozsądny zestaw narzędzi do rysowania i edycji obiektów 2D w środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) i [Szkicownik](Sketcher_Workbench/pl.md), ale nie jest on stworzony do obsługi bardzo dużych *(i czasami źle narysowanych*) plików 2D CAD. Zazwyczaj można z powodzeniem importować pliki 2D, ale nie oczekuj bardzo wysokiej wydajności, jeśli chcesz nadal pracować nad nimi w 2D.
    Ostrzeżono Cię.

-   Brak wsparcia dla materiałów. FreeCAD będzie posiadał kompletny system [Materiał](Material/pl.md), zdolny do definiowania bardzo złożonych materiałów, ze wszystkimi dobrami, których możesz się spodziewać *(niestandardowe właściwości, rodziny materiałów, właściwości renderowania i wizualne aspekty, itd.)*, a [Architektura](Arch_Workbench/pl.md) będzie oczywiście używał go, kiedy będzie gotowy.

-   Bardzo wstępne wsparcie dla [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). Możesz już [importować pliki IFC](Arch_IFC.md), całkiem niezawodnie, pod warunkiem, że [IfcOpenShell](http://ifcopenshell.org) jest zainstalowany w Twoim systemie, ale eksport nie jest jeszcze oficjalnie obsługiwany. Pracują nad tym zarówno deweloperzy FreeCAD jak i IfcOpenShell, i w przyszłości możemy spodziewać się pełnego wsparcia standardu IFC.

-   Większość narzędzi Arch jest nadal w fazie rozwoju. Oznacza to, że automatyczne narzędzia **kreatora**, które tworzą złożoną geometrię, takie jak [Dach](Arch_Roof/pl.md) lub [Schody](Arch_Stairs/pl.md) mogą tworzyć tylko niektóre typy obiektów, a inne narzędzia, takie jak [Konstrukcja](Arch_Structure/pl.md) lub [Okna](Arch_Window/pl.md) mają tylko kilka podstawowych ustawień. To oczywiście będzie narastać wraz z upływem czasu.

-   [Relacje pomiędzy obiektami](Assembly_project/pl.md) w FreeCAD nadal nie są oficjalnie dostępne. Przykładem może być relacja pomiędzy oknem a jego ścianą hosta, która jest obecnie zaimplementowana w środowisku [Architektura](Arch_Workbench/pl.md) za pomocą metod tymczasowych *(a zatem nieco ograniczonych)*. Wiele nowych możliwości pojawi się, gdy funkcja ta będzie w pełni dostępna.

-   [Jednostki](Units.md) są wdrażane w FreeCAD, co pozwoli ci pracować z każdą jednostką, jaką zechcesz *(nawet jednostki imperialne, wy chłopaki z USA możecie być za to wiecznie wdzięczni Jürgenowi, ojcu chrzestnemu i dyktatorowi FreeCAD)*. Ale w tej chwili realizacja nie jest jeszcze zakończona, a warsztat Arch nadal ich nie wspiera. Powinniście to potraktować jako **bezjednostkowe**.


{{Note|Wymagana jest wersja FreeCAD minimum 0.14|Ten poradnik został napisany przy użyciu [FreeCAD 0.14](Release_notes_0.14.md). Do wykonania tego ćwiczenia potrzebna więc jest co najmniej ta wersja. Wcześniejsze wydania mogą nie zawierać wszystkich potrzebnych narzędzi, lub mogą nie posiadać przedstawionych tutaj opcji.}}

## Typowy proces pracy 

Środowisko pracy [Architektura](Arch_Workbench/pl.md) wykonane jest głównie dla dwóch rodzajów schematów pracy:

-   Zbuduj swój model za pomocą szybszej, opartej na siatce aplikacji, takiej jak [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) lub [SketchUp](http://en.wikipedia.org/wiki/Sketchup), i zaimportuj go do FreeCAD w celu wyodrębnienia planów i widoków sekcji. FreeCAD jest stworzony do precyzyjnego modelowania, na znacznie wyższym poziomie niż to, czego zazwyczaj potrzebujemy w modelowaniu architektonicznym, budowanie twoich modeli bezpośrednio w FreeCAD może być uciążliwe i wolne. Z tego powodu, taki przepływ pracy ma duże zalety. Opisałem to w [tym artykule](http://yorik.uncreated.net/guestblog.php?2012=180) na swoim blogu. Jeśli zależy Ci na prawidłowym i precyzyjnym modelowaniu *(czyste, solidne, niezłożone siatki)*, ten proces pracy daje Ci taki sam poziom wydajności i precyzji jak inne.

-   Zbuduj swój model bezpośrednio w FreeCAD. To właśnie zaprezentuję w tym poradniku. Będziemy używać głównie trzech stanowisk pracy: [Architektura](Arch_Workbench/pl.md), oczywiście, ale także [Rysunek Roboczy](Draft_Workbench/pl.md), którego narzędzia są zawarte w Arch, więc nie ma potrzeby przełączania stołów roboczych, oraz [Szkicownik](Sketcher_Workbench/pl.md). Wygodnie możesz zrobić to, co zwykle robię, czyli stworzyć własny pasek narzędzi w swoim Środowisku pracy Arch, z menu Narzędzia → Dostosuj, i dodać często używane narzędzia ze szkicownika. To jest mój **niestandardowy** zestaw narzędzi Arch:

![](images/Arch_tutorial_01.jpg )

W tym poradniku będziemy modelować dom w 3D, na podstawie rysunków 2D, które pobierzemy z sieci, a następnie wydobędziemy z niego dokumenty 2D, takie jak plany, elewacje i przekroje.

## Przygotowania

Zamiast tworzyć projekt od podstaw, weźmy przykładowy projekt do modelowania, to zaoszczędzi nam trochę czasu. Wybrałem ten wspaniały dom słynnej architektki [Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) *(zobacz serię \[zdjęć <http://www.leonardofinotti.com/projects/architects-second-house/image/40409-130405-010d>\] Leonarda Finottiego)*, ponieważ jest on blisko mojego miejsca zamieszkania, jest prosty, jest wspaniałym przykładem niesamowitej modernistycznej architektury São Paulo, a rysunki DWG są [łatwo dostępne](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#).

Do budowy naszego modelu wykorzystamy rysunki 2D DWG uzyskane z powyższego linku *(aby pobrać, musisz się zarejestrować na powyższej stronie, ale jest ona darmowa, lub skorzystać bezpośrednio z wersji DXF [tutaj](http://yorik.uncreated.net/archive/scripts/artigas.dxf))*.
Tak więc pierwszą rzeczą, którą będziesz chciał zrobić, jest pobranie pliku, rozpakowanie go i otwarcie pliku DWG znajdującego się wewnątrz, za pomocą aplikacji DWG, takiej jak [DraftSight](http://www.3ds.com/products-services/draftsight/overview/). Alternatywnie, możesz przekonwertować go na DXF za pomocą darmowego narzędzia, takiego jak [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter). Jeśli masz zainstalowany ODA Converter *(i jego ścieżkę ustawioną w ustawieniach preferencji Arch)*, FreeCAD potrafi również [wykonać bezpośrednio import plików DWG](Draft_DXF.md). Ale ponieważ te pliki mogą być czasami złej jakości i bardzo ciężkie, zazwyczaj lepiej jest najpierw otworzyć je za pomocą aplikacji 2D CAD i trochę oczyścić.

Usunąłem tutaj wszystkie rysunki szczegółowe, wszystkie bloki tytułowe i układy stron, dokonałem **czyszczenia** *(oczyszczenia w slangu programu AutoCAD)* w celu usunięcia wszystkich nieużywanych elementów, przeorganizowałem sekcje w logicznym miejscu w stosunku do widoku planu i przesunąłem wszystko do punktu (0,0). Następnie nasz plik można dość sprawnie otworzyć w programie FreeCAD. Sprawdź różne opcje dostępne w manu Edycja → Preferencje → Draft → Import/Eksport, mogą mieć wpływ na to jak *(i jak szybko)* importowane są pliki DXF/DWG.

Tak wygląda plik po otwarciu go, we FreeCAD. Zmieniłem również grubość ścian *(zawartość grupy **muros**)*, a także obróciłem kilka drzwi, które zostały zaimportowane z niewłaściwą skalą X, za pomocą narzędzia [Skala](Draft_Scale/pl.md):

![](images/Arch_tutorial_02.jpg )

Importer [DXF importer](Draft_DXF/pl.md) *(który zajmuje się również plikami DWG, ponieważ podczas importu plików DWG są one po prostu najpierw konwertowane do DXF)* grupuje importowane obiekty według warstw. W FreeCAD nie ma żadnej warstwy, ale są [grupy](Std_Group/pl.md). [Grupy](Std_Group/pl.md) oferują podobny sposób porządkowania obiektów w plikach, ale nie mają specyficznych właściwości, takich jak warstwy programu AutoCAD, które mają zastosowanie do ich zawartości. Można je jednak umieszczać wewnątrz innych grup, co jest bardzo przydatne. Pierwszą rzeczą, którą możemy chcieć tutaj zrobić, jest utworzenie nowej [grupy](Std_Group/pl.md) w widoku [drzewa](Document_structure/pl.md), kliknięcie prawym przyciskiem myszy na ikonę dokumentu, dodanie grupy, kliknięcie jej prawym przyciskiem myszy w celu zmiany jej nazwy na *podstawowe plany 2D* i przeciągnięcie do niej wszystkich innych obiektów.

## Budowa ścian 

Podobnie jak większość obiektów środowiska [Architektura](Arch_Workbench/pl.md), obiekt[ściany](Arch_Wall/pl.md) może być zbudowany na dużej ilości innych obiektów: [linia](Draft_Line/pl.md), [ciąg linii](Draft_Wire.md) *(polilinie)*, [ szkice](Sketcher_Workbench/pl.md), powierzchnie lub bryły *(lub nawet na niczym, w tym przypadku są one określone przez wysokość, szerokość i długość)*. Wynikowa geometria ściany zależy od geometrii bazowej i od właściwości, które wypełnisz, takich jak szerokość i wysokość. Jak możesz się domyślać, ściana bazująca na linii będzie używała tej linii jako linii wyrównania, podczas gdy ściana bazująca na powierzchni czołowej będzie używała tej powierzchni jako powierzchni podstawy, a ściana bazująca na bryle po prostu przyjmie kształt tej bryły. Dzięki temu każdy kształt, jaki można sobie wyobrazić, staje się ścianą

Istnieją różne możliwe strategie budowy ścian w FreeCAD. Można zbudować kompletny **plan piętra** ze [Szkicownikiem](Sketcher_Workbench/pl.md) i zbudować z niego jeden, duży, ścienny obiekt. Ta technika działa, ale można podać tylko jedną grubość dla wszystkich ścian projektu. Albo możesz zbudować każdy kawałek ściany z oddzielnych odcinków linii. Albo, to jest to co zrobimy tutaj, połączenie obu: Zbudujemy kilka [szkiców ciągów linii](Draft_Wire/pl.md) na importowanym planie, po jednym dla każdego typu ściany:

![](images/Arch_tutorial_03.jpg )

Jak widać, narysowałem na czerwono linie, które staną się betonowymi ścianami *(wyszukiwanie [zdjęć](http://www.google.com/search?tbm=isch&q=casa+artigas+brooklin) domu może pomóc zobaczyć różne rodzaje ścian)*, zielone to ściany zewnętrzne z cegły, a niebieskie to ściany wewnętrzne. Przechodzę przez te linie przez drzwi, ponieważ drzwi zostaną później wstawione w ściany i automatycznie stworzą ich otwory. Ściany mogą być również wyrównane w lewo, w prawo lub centralnie na ich linii podstawowej, więc nie ma znaczenia, po której stronie narysujesz linię podstawową. Dołożyłem również wszelkich starań, aby unikać skrzyżowań, ponieważ nasz model będzie w ten sposób czystszy. Ale tymi skrzyżowaniami zajmiemy się później.

Kiedy to zrobisz, umieść wszystkie te linie w nowej [grupie](Std_Group/pl.md), jeśli chcesz, wybierz każdą linię jedna po drugiej i naciśnij narzędzie [Ściana](Arch_Wall/pl.md), aby zbudować ścianę z każdej z nich. Możesz również wybrać kilka linii na raz. Po wykonaniu tej czynności i skorygowaniu szerokości *(ściany zewnętrzne mają 25cm szerokości, wewnętrzne 15cm szerokości)* oraz wprowadzeniu kilku poprawek, mamy gotowe nasze ściany:

![](images/Arch_tutorial_04.jpg )

Mogliśmy też zbudować nasze mury od podstaw. Jeśli wciśniesz przycisk [Tworzy obiekt ściana \...](Arch_Wall/pl.md) bez zaznaczonego obiektu, będziesz mógł kliknąć dwa punkty na ekranie, aby narysować ścianę. Ale jednocześnie wewnątrz muru, narzędzie do rysowania ścian narysuje linię i zbuduje na niej ścianę. W tym przypadku uważam, że jest to bardziej dydaktyczne, ponieważ pokazuje, jak to funkcjonuje.

Zauważyłeś, że bardzo się starałem, by nie przecinać murów? Zaoszczędzi nam to trochę bólu głowy później, na przykład jeśli wyeksportujemy naszą pracę do innych aplikacji, którym może się to nie spodobać. Mam tylko jedno skrzyżowanie, na którym byłem zbyt leniwy, by narysować dwa małe odcinki linii, i narysowałem jeden duży ciąg przechodzący przez drugi. To musi być naprawione. Na szczęście wszystkie obiekty Arch mają świetną cechę: można dodawać jedne do drugich. W ten sposób połączą się ich geometrie, ale nadal można je edytować niezależnie od siebie. Aby dodać jedną z naszych krzyżujących się ścian do drugiej, wystarczy wybrać jedną, przytrzymać klawisz **CTRL** + wybrać drugą, a następnie użyć narzędzie [Dodaj](Arch_Add/pl.md):

![](images/Arch_tutorial_05.jpg )

Po lewej stronie znajdują się dwie przecinające się ściany, po prawej stronie wynik po dodaniu jednej do drugiej.


{{Note|Ważna uwaga o obiektach parametrycznych|Coś należy już rozważyć. Jak widzisz, w FreeCAD wszystko jest parametryczne: Nasza nowa '''zespolona''' ściana jest zrobiona z dwóch ścian, każda oparta na linii bazowej. Kiedy rozwiniesz je w widoku [drzewa](Document_structure/pl.md), możesz zobaczyć cały ten łańcuch zależności. Jak możesz sobie wyobrazić, ta mała gra może szybko stać się bardzo złożona. Co więcej, jeśli już wiesz jak pracować ze środowiskiem pracy [Szkicownik](Sketcher_Workbench/pl.md), być może chciałbyś narysować linie bazowe używając związanych szkiców. Ta cała złożoność ma swój koszt: zwiększa wykładniczo liczbę obliczeń, które FreeCAD musi wykonać, aby utrzymać aktualną geometrię modelu. Tak więc, pomyśl o tym, nie dodawaj niepotrzebnej złożoności gdy jej nie potrzebujesz. Zachowaj równowagę pomiędzy prostymi i złożonymi obiektami i zachowaj te elementy na wypadek, gdybyś ich naprawdę potrzebował.}}

Na przykład, mogłem narysować wszystkie moje linie bazowe powyżej bez zwracania uwagi na to, co przecina co, i naprawić rzeczy za pomocą narzędzia [Dodaj](Arch_Add/pl.md) później. Ale znacznie zwiększyłbym złożoność mojego modelu, bez żadnego zysku. Lepiej sprawić, aby były one poprawne od samego początku, i utrzymywać je jako bardzo proste elementy geometrii.

Teraz, gdy nasze ściany są w porządku, musimy podnieść ich wysokość, żeby się mogły zetknąć z dachem. Następnie, ponieważ obiekt na ścianie nadal nie może zostać automatycznie przecięty przez dachy *(co jednak kiedyś nastąpi)*, zbudujemy *atrapę* obiektu, która będzie odpowiadała kształtowi dachu, do późniejszego odjęcia od naszych ścian.

Po pierwsze, patrząc na nasze rysunki 2D widzimy, że najwyższy punkt dachu znajduje się na wysokości 5,6m nad ziemią. Nadajmy więc wszystkim naszym ścianom wysokość 6m, więc upewnimy się, że zostaną one przecięte przez naszą atrapę dachu. Dlaczego 6m, a nie 5,6m? Możesz zapytać. Cóż, jeśli już pracowałeś z operacjami logicznymi *(dodawanie, odejmowanie, krzyżowanie)*, musisz już wiedzieć, że te operacje zazwyczaj nie lubią sytuacji *na styk*. Wolą one wyraźnie, szczerze mówiąc przecinające się obiekty. Czyniąc to, trzymamy się więc po bezpiecznej stronie.

Aby zwiększyć wysokość naszych ścian, po prostu wybierz je wszystkie *(nie zapomnij o tej, którą dodaliśmy do drugiej)* w widoku drzewa i zmień wartość ich właściwości **wysokość**.

Przed wykonaniem dachu i wycięciem ścian, wykonajmy pozostałe elementy, które będą musiały zostać wycięte: Ściany powyższej pracowni i kolumny. Ściany pracowni są wykonane tak samo jak nasze, na najwyższym planie, ale zostaną podniesione do poziomu 2,6m. Tak więc damy im potrzebną wysokość, aby ich wierzchołek znajdował się również na poziomie 6m, czyli 3,4m. Kiedy już to zrobimy, przesuńmy nasze ściany o 2,6 m w górę: Wybierzmy je obie, ustawiamy się w widoku od przodu *(Widok → Widoki standardowe → Przód)*, naciskamy przycisk [Przesuń](Draft_Move/pl.md), wybieramy pierwszy punkt, następnie wprowadzamy 0, 2.6, 0 jako współrzędne, i naciskamy enter. Twoje obiekty skoczyły teraz na wysokość 2,6 m. Wciśnij przycisk [Przesuń](Draft_Move/pl.md), wybierz pierwszy punkt, następnie wprowadź 0, 2,6, 0 jako współrzędne i naciśnij enter:

![](images/Arch_tutorial_06.jpg )


{{Note|Informacje o współrzędnych|Obiekty środowiska [Rysunek Roboczy](Draft_Workbench/pl.md), a także większość obiektów [Architektura](Arch_Workbench/pl.md), są zgodne z systemem szkicowym zwanym [płaszczyzny robocze](Draft_SelectPlane/pl.md). Ten system definiuje płaszczyznę 2D, na której będą wykonywane następne operacje. Jeśli nie określisz żadnej, to płaszczyzna robocza zaadaptuje się do bieżącego widoku. Dlatego przełączyliśmy się na widok czołowy i widzisz, że wskazaliśmy ruch w X na 0 i w Y na 2.6m. Mogliśmy również zmusić płaszczyznę roboczą do pozostania na powierzchni, używając narzędzia [Wybór płaszczyzny](Draft_SelectPlane/pl.md). Wtedy wprowadzilibyśmy ruch X o wartości 0, Y o wartości 0 i Z o wartości 2.6. }}

Teraz przenieśmy nasze mury poziomo, na ich właściwe miejsce. Skoro mamy punkty, do których trzeba się zatrzasnąć, to jest to łatwiejsze: Wybierz obie ściany, naciśnij narzędzie [Przesuń](Draft_Move/pl.md) i przenieś je z jednego punktu do drugiego:

![](images/Arch_tutorial_07.jpg )

W końcu zmieniłem kolor niektórych ścian na ceglany *(dzięki czemu łatwiej jest je rozpoznać)* i wprowadziłem niewielką korektę: Niektóre ściany nie zachodzą na dach, ale zatrzymują się na wysokości 2,60m. Ja skorygowałem wysokość tych ścian.

## Podnoszenie konstrukcji 

Teraz, ponieważ będziemy musieli wyciąć nasze ściany z odejmowaną objętością, równie dobrze możemy zobaczyć, czy nie ma innych obiektów, które będą musiały być wycięte w ten sposób. Są, niektóre z kolumn. Jest to dobra okazja, aby wprowadzić drugi obiekt architektury: [konstrukcja](Arch_Structure/pl.md). Obiekty Struktury zachowują się mniej więcej jak ściany, ale nie są przystosowane do podążania za linią odniesienia. Wolą raczej pracować z profilem, który jest wyciągany *(wzdłuż linii profilu lub nie)*. Każdy płaski obiekt może być profilem dla danej konstrukcji, z jednym tylko wymogiem: muszą one tworzyć kształt zamknięty.

W przypadku naszych słupów będziemy stosować inną strategię niż w przypadku ścian. Zamiast rysować je na planach 2D, będziemy bezpośrednio korzystać z obiektów pochodzących z tej strategii: kółek, które reprezentują słupy w widoku planu. Teoretycznie możemy po prostu wybrać jedno z nich i wcisnąć przycisk [Konstrukcja](Arch_Structure/pl.md). Jeśli jednak to zrobimy, stworzymy pusty obiekt strukturalny. Dzieje się tak, ponieważ nigdy nie można być zbyt pewnym, jak dobrze obiekty zostały narysowane w pliku DWG, a często nie są to kształty zamknięte. Tak więc, zanim zamienimy je na rzeczywiste kolumny, zamieńmy je na płaszczyzny, używając na nich dwukrotnie narzędzia [Ulepsz kształt](Draft_Upgrade/pl.md). Za pierwszym podejściem zamieniamy je na zamknięte ciągi linii *(polilinie)*, za drugim zamieniamy je na powierzchnie. Ten drugi krok nie jest obowiązkowy, ale jeśli masz powierzchnię, to jesteś w 100% pewien, że jest ona zamknięta *(w przeciwnym razie nie można wykonać powierzchni)*.

Po przekonwertowaniu wszystkich naszych kolumn na płaszczyzny, możemy użyć na nich narzędzia [Konstrukcja](Arch_Structure/pl.md) i dostosować wysokość *(niektóre mają wysokość 6m, inne tylko 2.25m)*:

![](images/Arch_tutorial_08.jpg )

Na powyższym obrazku widać dwie kolumny, które są nadal takie same jak w pliku DWG, dwie, które zostały zaktualizowane do postaci powierzchni czołowych i dwie, które zostały przekształcone w obiekty konstrukcyjne, a ich wysokość została ustawiona na 6m i 2,25m.

Zauważ, że te różne obiekty Arch *(mury, konstrukcje i wszystkie inne, które odkryjemy)* mają wiele wspólnego *(na przykład wszystkie mogą być dodane do siebie, jak już widzieliśmy w przypadku ścian, a każdy z nich może być przekształcony w inny)*. Jest to więc bardziej kwestia gustu, mogliśmy zrobić nasze kolumny również za pomocą narzędzia do budowania ścian i przekształcić je w razie potrzeby. W rzeczywistości, niektóre z naszych ścian są betonowymi ścianami, moglibyśmy chcieć później przekształcić je w konstrukcje.

## Operacja odcięcia 

Teraz nadszedł czas, aby zbudować naszą przestrzeń przeznaczoną do odjęcia. Najprostszym sposobem będzie narysowanie jej profilu na górze widoku przekroju. Następnie obrócimy go i ustawimy we właściwej pozycji. Widzisz, dlaczego umieściłem profile i elewacje w ten sposób przed rozpoczęciem? To będzie bardzo przydatne do rysowania elementów tam, a następnie przesunięcia ich do właściwej pozycji na modelu.

Narysujmy objętość, większą niż dach, która zostanie odjęta od naszych ścian. W tym celu narysowałem dwie linie na podstawie dachu, a następnie przedłużyłem je nieco dalej narzędziem [Przytnij](Draft_Trimex/pl.md). Następnie narysowałem [polilinia](Draft_Wire/pl.md), zatrzaskując się na tych liniach, i idąc znacznie powyżej naszych 6 metrów. Narysowałem też niebieską linię na poziomie ziemi (0.00), która będzie naszą osią obrotu.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

Teraz jest trudna sprawa: Użyjemy narzędzia [Obróć](Draft_Rotate/pl.md), aby obrócić nasz profil o 90 stopni w górę, we właściwej pozycji do wyciągnięcia. Aby to zrobić, musimy najpierw zmienić płaszczyznę [roboczą](Draft_SelectPlane/pl.md) na płaszczyznę YZ. Gdy to zrobimy, obrót nastąpi w tej płaszczyźnie. Jeśli jednak zrobimy tak, jak zrobiliśmy to trochę wcześniej, i ustawimy widok na bok, trudno będzie zobaczyć i wybrać nasz profil, a także wiedzieć, gdzie jest punkt bazowy, wokół którego musi się obracać, prawda? Wtedy musimy ręcznie ustawić płaszczyznę roboczą: Wcisnąć przycisk [Wybór płaszczyzny](Draft_SelectPlane/pl.md) *(znajduje się w zakładce **Zadania** widoku drzewa)*, i ustawić go na YZ *(który jest płaszczyzną **boczną**)*. Po ręcznym ustawieniu płaszczyzny roboczej, w ten sposób nie zmieni się ona w zależności od widoku. Możesz teraz obracać swój widok, aż będziesz miał dobry widok wszystkich rzeczy, które musisz wybrać. Aby później przełączyć płaszczyznę roboczą z powrotem do trybu **automatycznego**, należy ponownie nacisnąć przycisk [Wybór płaszczyzny](Draft_SelectPlane/pl.md) i ustawić go na **Brak**.

Teraz rotacja będzie łatwa do wykonania: Wybierz profil, naciśnij przycisk [Obróć](Draft_Rotate/pl.md), kliknij na punkt niebieskiej linii, wprowadź 0 jako kąt początkowy, a 90 jako obrót:

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

Teraz wystarczy tylko przesunąć profil nieco bliżej modelu *(w razie potrzeby ustawić płaszczyznę roboczą na XY)*, a następnie go wyciągnąć. Można to zrobić za pomocą narzędzia [Wyciągnij wybrany szkic](Part_Extrude/pl.md), lub [Przytnij](Draft_Trimex/pl.md), które również posiada specjalną ukrytą moc umożliwiającą wytłoczenie powierzchni. Upewnij się, że twoje elementy do wyciągnięcia są większe niż wszystkie ściany, od których będą odejmowane, aby uniknąć sytuacji typu na styk:

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

Teraz, tutaj przychodzi do działania w przeciwieństwie do narzędzia [Dodaj](Arch_Add/pl.md) narzędzie: [Usuń](Arch_Remove/pl.md). Jak można się było domyślać, czyni on również obiekt potomkiem innego, ale jego kształt jest odejmowany od obiektu głównego, zamiast być zespolonym. Więc teraz wszystko jest proste: Wybierz objętość do odjęcia *(zmieniłem jej nazwę na **Objętość dachu do odjęcia** w widoku drzewa, aby łatwo ją było dostrzec)*, naciśnij klawisz **CTRL** + wybierz ścianę, a następnie naciśnij przycisk [Usuń](Arch_Remove/pl.md). Zobaczysz, że po odjęciu objętość do odjęcia zniknęła zarówno z widoku 3D, jak i z widoku drzewa. Dzieje się tak, ponieważ została ona oznaczona jako dziecko ściany i połknięta przez tę ścianę. Wybierz ścianę, rozwiń ją w widoku drzewa, tam jest nasza objętość.

Teraz wybierz objętość w oknie drzewa, klawisz **CTRL** + wybierz następną ścianę, naciśnij [Usuń](Arch_Remove/pl.md). Powtarzaj tę czynność dla kolejnych ścian, aż do momentu, gdy wszystko zostanie prawidłowo wycięte:

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Pamiętaj, że zarówno dla [Dodaj](Arch_Add/pl.md) jak i [Usuń](Arch_Remove/pl.md) ważna jest kolejność wybierania obiektów. Główny obiekt jest zawsze ostatni, jak w *Usuń X z Y* lub *Dodaj X do Y*.


{{Note|Notatka o dodawaniu i odejmowaniu|Obiekty Architertury, które obsługują takie operacje dodania i odjęcia ''(wszystkie z wyjątkiem '''wizualnych''' obiektów pomocniczych, takich jak osie)'' pozwalają na kontrolowanie takich obiektów poprzez posiadanie dwóch właściwości, odpowiednio '''Additions''' i '''Subtractions''', które zawierają listę linków do innych obiektów, które mają być odejmowane lub dodawane. Ten sam obiekt może znajdować się na listach kilku innych obiektów. Jak to ma miejsce w przypadku naszej objętości odejmowania tutaj. Każdy z ojców będzie jednak chciał go połknąć w widoku drzewa, więc zwykle będzie mieszkał w ostatnim z nich. Ale zawsze możesz edytować te listy dla dowolnego obiektu, klikając dwukrotnie na nie w widoku drzewa, który w FreeCAD przechodzi w tryb edycji. Naciśnięcie klawisza **ESC** powoduje wyjście z trybu edycji.}}

## Wykonywanie dachów 

Teraz jedyne, co musimy zrobić, aby ukończyć konstrukcję, to wykonać dach i mniejsze płyty wewnętrzne. Ponownie, najłatwiej jest narysować ich profile na górze sekcji, za pomocą narzędzia [Polilinia](Draft_Wire/pl.md). Tutaj narysowałem 3 profile jeden na drugim *(odsunąłem je na obrazku poniżej, aby lepiej je było widać)*. Zielony będzie służył do bocznych krawędzi płyty dachowej, następnie niebieski do części bocznych, a czerwony do części środkowej, która znajduje się nad blokiem łazienki:

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Następnie musimy powtórzyć powyższą operację rotacji, aby obrócić obiekty w pozycji pionowej, a następnie przesunąć je w odpowiednie miejsca i skopiować niektóre z nich, które będą musiały być wyciągnięte dwukrotnie, za pomocą narzędzia [Przesuń](Draft_Move/pl.md), z wciśniętym klawiszem **ALT**, który tworzy kopie zamiast przesuwać bieżący obiekt. Dodałem także dwa kolejne profile do bocznych ścian otworu w łazience.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

Kiedy wszystko jest na swoim miejscu, jest to tylko kwestia użycia narzędzia [Przytnij](Draft_Trimex/pl.md) do wyciągnięcia, a następnie przekształcenia ich na obiekty [Konstrukcja](Arch_Structure/pl.md).

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

Następnie widzimy pojawiające się problemy: dwie kolumny po prawej stronie są za krótkie *(powinny wejść na dach)*, a pomiędzy płytą a ścianami pracowni po prawej stronie znajduje się szczelina *(symbol 2,60 poziomu na widoku przekroju był oczywiście błędny)*. Dzięki zastosowaniu obiektów parametrycznych, wszystko to jest bardzo łatwe do rozwiązania: W przypadku słupów wystarczy zmienić ich wysokość na 6m, odjąć objętość dachu z widoku drzewa i odjąć ją do słupów. W przypadku ścian, jest to jeszcze łatwiejsze: przesuń je trochę w dół. Ponieważ odejmowana objętość pozostaje w tym samym miejscu, geometria ścian dostosuje się automatycznie.

Teraz trzeba naprawić jeszcze jedną, ostatnią rzecz, jest mała płyta w łazience, która przecina niektóre ściany. Naprawmy to, tworząc nową objętość odejmowania, i odejmijmy ją od tych ścian. Inną cechą narzędzia [Przytnij](Draft_Trimex/pl.md), którego używamy do wyciągania elementów, jest to, że może ono również wyciągnąć jedną powierzchnię z istniejącego obiektu. Tworzy to nowy, oddzielny obiekt, więc nie ma ryzyka uszkodzenia drugiego obiektu. Możemy więc wybrać podstawową powierzchnię małej płyty (spójrz na nią od dołu modelu, zobaczysz ją), a następnie wcisnąć przycisk [Przytnij](Draft_Trimex/pl.md) i wyciągnąć ją aż do wysokości dachów. Następnie odejmij ten element od dwóch wewnętrznych ścian łazienki za pomocą narzędzia [Usuń](Arch_Remove/pl.md):

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">

## Posadzki, schody i komin 

Teraz, nasza struktura jest kompletna, mamy tylko kilka mniejszych obiektów do wykonania.

### Komin

Zacznijmy od komina. Teraz już wiesz, jak to działa, prawda? Narysuj kilka zamkniętych [ciągów linii](Draft_Wire/pl.md), przesuń je na odpowiednią wysokość za pomocą narzędzia [Przesuń](Draft_Move/pl.md), wyciągnij je za pomocą narzędzia [Przytnij](Draft_Trimex/pl.md), przekształć w większą [konstrukcję](Arch_Structure/pl.md), i odejmij mniejsze. Zauważ, że rura kominowa nie została narysowana na widoku planu, ale znalazłem jej położenie przeciągając niebieskie linie z widoków przekroju.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">

### Posadzki

Posadzki nie są dobrze udokumentowane na rysunkach podstawowych. Patrząc na przekroje, nie można wiedzieć, gdzie i jak grube są płyty podłogowe. Przypuszczam więc, że ściany znajdują się na blokach fundamentowych, na poziomie 0.00, i że na tych blokach znajdują się płyty posadzkowe, także te o grubości 15 cm. Więc płyty posadzkowe nie przebiegają pod ścianami, ale obok nich. Moglibyśmy to zrobić, tworząc dużą prostokątną płytę, a następnie odjąć ściany, ale pamiętajmy, że operacje odejmowania są dla nas bardzo zasobochłonne. Lepiej zrobić to w mniejszych częściach, to będzie lżejsze pod względem obliczeniowym, a także jeśli zrobimy to inteligentnie, pomieszczenie po pomieszczeniu, przydadzą się one również później do obliczenia powierzchni podłogi:

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Po przeciągnięciu linii, wystarczy zamienić je w [konstrukcje](Arch_Structure/pl.md) i dać im wysokość {{Value|0.15m}}:

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">

### Schody

Teraz schody. Poznajcie następne z narzędzi Architektury, [Schody](Arch_Stairs/pl.md). Narzędzie to jest jeszcze w bardzo wczesnej fazie rozwoju w czasie gdy to piszę, więc nie oczekuj od niego zbyt wiele. Ale jest już całkiem przydatne, aby zrobić proste, nieskomplikowane schody. Ważna jest jedna koncepcja, narzędzie schody ma za zadanie budować schody od płaskiej podłogi aż do ściany. Innymi słowy, patrząc z góry, obiekt schody zajmuje dokładnie tyle miejsca, ile zajmuje na planie, więc nie rysuje się ostatniego pionu *(ale oczywiście jest on brany pod uwagę przy obliczaniu wysokości)*.

W tym przypadku wolałem zbudować schody na widoku przekroju, ponieważ będziemy potrzebowali wielu pomiarów, które są łatwiejsze do uzyskania z tego widoku. Tutaj narysowałem kilka czerwonych wytycznych, następnie dwie niebieskie linie, które będą podstawą naszych dwóch części schodów, oraz dwa zielone zamknięte kształty, które będą tworzyć brakujące części. Teraz wybierzcie pierwszą niebieską linię, wciśnijcie narzędzie [Schody](Arch_Stairs/pl.md), ustawcie ilość stopni na {{Value|5}}, wysokość na 0.875m, szerokość na {{Value|1.30m}}, typ konstrukcji na masywną i grubość konstrukcji na {{Value|0.12m}}. Powtórz tę czynność dla drugiego elementu.

Następnie należy wyciągnąć oba zielone kształty do 1.30m, obrócić je i ustawić we właściwej pozycji:

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

Na widoku elewacji narysuj *(a następnie obróć)* krawędź:

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Potem przenieś wszystko na miejsce:

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

Nie zapomnij również przyciąć kolumny przechodzącej przez schody, ponieważ w BIM zawsze źle jest mieć przecinające się obiekty. Budujemy jak w realnym świecie, pamiętaj, gdzie nie mogą przecinać się obiekty stałe. Tutaj nie chciałem odejmować kolumny bezpośrednio od schodów *(w przeciwnym razie obiekt z kolumny zostałby połknięty przez obiekt ze schodów w widoku drzewa, a mi to nie odpowiadało)*, więc wziąłem powierzchnię, na której zbudowano kolumnę i ponownie ją wyciągnąłem. To nowe wyciągnięcie zostało następnie odjęte od schodów.

Tak! Cała ta mozolna praca jest już wykonana, kontynuujmy tę bardzo ciężką pracę!

## Drzwi oraz okna 

[Okna](Arch_Window/pl.md) to dość skomplikowane obiekty. Są one używane do tworzenia wszelkiego rodzaju wstawianych obiektów, takich jak okna czy drzwi. Tak, w FreeCAD, drzwi są po prostu specjalnym rodzajem okna. W prawdziwym życiu też, jeśli o tym pomyśleć, prawda? Narzędzie [Okna](Arch_Window/pl.md) może być jeszcze trochę trudne w użyciu, ale uważaj to za kompromis, ponieważ zostało zbudowane dla maksymalnej mocy. Prawie każdy rodzaj okna, które możesz sobie wyobrazić, może być za jego pomocą zrealizowany. Ale ponieważ narzędzie to zyska więcej nastaw, sytuacja ta z pewnością stanie się bardziej dogodna w przyszłości.

Obiekt [Architektura](Arch_Workbench/pl.md) działa w następujący sposób: Jest on oparty na planie 2D, dowolnym obiekcie 2D, ale najlepiej [szkicu](Sketcher_Workbench/pl.md), który zawiera zamknięte kształty *(polilinie)*. Te linie definiują różne części okna: ramy zewnętrzne, ramy wewnętrzne, panele szklane, panele pełne, itp. Obiekty okienne mają zatem właściwość, która przechowuje co należy zrobić z każdym z tych ciągów linii: wytłoczyć go, umieścić na pewnym przesunięciu, itp. Wreszcie, okno może być wstawione do obiektu głównego, takiego jak ściana lub konstrukcja, i automatycznie utworzy w nim otwór. Otwór ten zostanie obliczony przez wyciągnięcie największego kształtu znajdującego się w układzie 2D.

Istnieją dwa sposoby na tworzenie takich obiektów w FreeCAD: używając wstępnie zdefiniowanego lub rysując układ okna od podstaw. Obu metodom przyjrzymy się tutaj. Ale pamiętaj, że metoda predefiniowana nie robi nic poza stworzeniem obiektu układu i zdefiniowaniem niezbędnych dla Ciebie wyciągnięć.

### Korzystanie z ustawień wstępnych 

Po naciśnięciu narzędzia [Okna](Arch_Window/pl.md) bez zaznaczonego obiektu, zostaniesz poproszony o wybranie układu 2D lub użycie jednego z ustawień wstępnych. Użyjmy ustawienia **Proste drzwi**, aby umieścić główne drzwi wejściowe w naszym modelu. Nadajmy mu szerokość 1m, wysokość {{Value|2.45m}}, rozmiar W1 0.15m, a pozostałe parametry pozostawmy na wartości 0.05m. Następnie kliknij w lewy dolny róg ściany, a Twoje nowe drzwi zostaną utworzone:

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

Zauważysz, że twoje nowe drzwi nie pojawią się w widoku drzewa. To dlatego, że klikając na ścianę, wskazaliśmy ją jako obiekt gospodarza. W związku z tym zostały połknięte przez ten mur. Kliknij na nie prawym przyciskiem myszy → Przejdź do wyboru, a znajdziesz je w drzewie dokumentu.

W tym przypadku, ponieważ nasze okno nie jest włożone w żadną ścianę *(otwór już tam był)*, możemy równie dobrze oderwać nasze okno od jego ściany. Dokonujemy tego klikając dwukrotnie na tą ścianę w widoku drzewa, aby wejść do trybu jej edycji. Tam pojawi się okno w grupie \"Odejmowania\". Po prostu zaznaczamy tam okno, naciskamy przycisk \"Usuń element\", a następnie \"OK\". Nasze okno zostało teraz usunięte ze swojej ściany głównej i znajduje się na dole widoku drzewa.

Mamy drugie drzwi, dokładnie takie same jak te, trochę na lewo. Zamiast tworzyć nowe drzwi od podstaw, mamy dwa sposoby na zrobienie kopii poprzednich: Za pomocą narzędzia [Przesuń](Draft_Move/pl.md), z wciśniętym klawiszem **ALT**, które, jak już wiesz, kopiuje obiekt zamiast go przesuwać. Albo, jeszcze lepiej, możemy użyć narzędzia [Klonuj](Draft_Clone/pl.md). Narzędzie do klonowania tworzy klon wybranego obiektu, który można przesuwać, ale który zachowuje kształt oryginalnego obiektu. Jeśli oryginalny obiekt ulegnie zmianie, klon również się zmieni.

Tak więc wszystko, co musimy teraz zrobić, to wybrać drzwi, wcisnąć narzędzie [Klonuj](Draft_Clone/pl.md), a następnie przesunąć klon na jego właściwą pozycję za pomocą narzędzia [Przesuń](Draft_Move/pl.md).

### Porządkowanie modelu 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Teraz byłby dobry czas na odrobinę porządkowania projektu domu. Ponieważ mamy już dwa okna, jest to dobry moment, aby zrobić trochę czyszczenia w widoku drzewa: Stwórz nową [grupę](Std_Group.md), zmień jej nazwę na okna i przesuń do niego 2 okna. Polecam również oddzielenie w ten sposób innych elementów, takich jak ściany i konstrukcje. Ponieważ możesz również tworzyć [grupy](Std_Group.md) wewnętrzne, możesz organizować je dalej, na przykład umieszczając wszystkie elementy tworzące dach w osobnej grupie, dzięki czemu łatwo je włączać i wyłączać *(przełączenie widoczności grupy robi to samo ze wszystkimi obiektami w jej wewnętrzu)*.

W środowisku pracy [Architektura](Arch_Workbench/pl.md) znajdują się dodatkowe narzędzia do organizacji modelu: [Teren](Arch_Site/pl.md), [Budowla](Arch_Building/pl.md) i [Piętro](Arch_Floor/pl.md). Te 3 obiekty są oparte na standardowej grupie FreeCAD, więc zachowują się dokładnie jak grupy, ale mają kilka dodatkowych właściwości. Na przykład, [piętro](Arch_Floor/pl.md) ma możliwość ustawienia i zarządzania wysokością osadzonych w nich ścian i konstrukcji, a gdy są one przenoszone, przesuwana jest również cała ich zawartość.

Ale tutaj, ponieważ mamy tylko jeden budynek z jednym *(i pół)* piętrem, nie ma rzeczywistej potrzeby korzystania z takich obiektów, więc trzymajmy się prostych grup.




A teraz wracajmy do pracy. Wyłączcie grupę dachową, żebyśmy mogli lepiej widzieć przestrzeń wewnątrz, i przełączcie tryb wyświetlania obiektów piętrowych na Wireframe *(lub użyjcie narzędzia [Przełącz tryb wyświetlania](Draft_ToggleDisplayMode/pl.md))*, żebyśmy nadal mogli na nie patrzeć, ale poniżej możemy zobaczyć widok planu. Jednak możesz również całkowicie wyłączyć podłogi, następnie umieścić drzwi na poziomie 0, a następnie podnieść je o 15cm za pomocą narzędzia [Przesuń](Draft_Move/pl.md).

Ustawmy drzwi wewnętrzne. Użyj ponownie nastawy wstępnej **Simple Door**, wykonaj drzwi o wymiarach {{Value|1,00m}} i {{Value|0,70m}} szerokości x 2,10m wysokości, o wielkości W1 {{Value|0,1m}}. Upewnij się, że przy ich umieszczaniu zatrzasnąłeś się do odpowiedniej ściany, aby automatycznie utworzyły w niej otwór. Jeśli trudno jest umieścić je prawidłowo, można je umieścić w łatwiejszym miejscu, na przykład w rogu ściany, a następnie przenieść. Otwór przesunie się jednocześnie.

Jeśli przez pomyłkę umieściłeś okno w niewłaściwej ścianie, to łatwo jest to naprawić: Usuń okno z grupy **Subtraction** ściany głównej w trybie edycji, jak widzieliśmy powyżej, a następnie dodaj je do grupy **Subtraction** właściwej ściany, tą samą metodą, lub po prostu za pomocą narzędzia [Usuń](Arch_Remove/pl.md).

Trochę pracy, później, wszystkie nasze drzwi są na miejscu:

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

Po bliższym przyjrzeniu się widokowi elewacji, wykryłem teraz kolejny błąd: Górna część murów ceglanych nie jest 2,60m, ale 17,5cm niższa, czyli 2,425m. Na szczęście okna bazujące na ustawieniach fabrycznych mają swoje zalety: Można zmieniać ich ogólne wymiary (szerokość i wysokość) w zależności od ich właściwości. Zmieńmy więc ich wysokość na 2,425 - 0,15, czyli 2,275. Drugie okno, ponieważ jest klonem pierwszego, dostosuje się również. Tu w zasadzie pojawia się prawdziwa magia konstrukcji parametrycznej.

Teraz możemy spojrzeć na naprawdę ciekawe rzeczy: Jak zaprojektować własne okna na miarę.

### Tworzenie okien według własnych upodobań 

Jak wyjaśniłem powyżej, obiekty [Arch: Okno](Arch_Window/pl.md) są tworzone z planów 2D, wykonanych z zamkniętych elementów *(ciągów linii (polilinii), okręgów, prostokątów, czegokolwiek)*. Ponieważ obiekty środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) nie mogą pomieścić więcej niż jednego z tych elementów, preferowanym narzędziem do rysowania planów okien jest [Szkicownik](Sketcher_Workbench/pl.md). Niestety, przy pomocy szkicownika nie jest możliwe przyciągnięcie do zewnętrznych obiektów, jak w przypadku Środowiska pracy Draft, które byłoby tutaj użyteczne, ponieważ nasze elewacje są już narysowane. Na szczęście istnieje narzędzie do konwersji obiektów Draft do szkicu: Narzędzie [rysunek roboczy na szkic](Draft_Draft2Sketch/pl.md).

Więc, zacznijmy od zbudowania naszego pierwszego projektu okna. Narysowałem go na elewacji, używając kilku [prostokątów](Draft_Rectangle/pl.md): Jeden dla linii zewnętrznej, i 4 dla wewnętrznej. Zatrzymałem się przed drzwiami, bo, pamiętaj, nasze drzwi mają już tam ramę:

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Następnie zaznacz wszystkie prostokąty i naciśnij przycisk [rysunek roboczy na szkic](Draft_Draft2Sketch/pl.md) *(i usuń prostokąty, ponieważ to narzędzie nie usuwa oryginalnych obiektów, w przypadku gdy coś pójdzie nie tak)*. Następnie, po wybraniu nowego szkicu, naciśnij przycisk [Okna](Arch_Window/pl.md)

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

Narzędzie wykryje, że układ posiada jedną obwiednię zewnętrzną i kilka wewnętrznych i automatycznie zaproponuje Ci domyślną konfigurację: Jedna ramka, wykonana przez odjęcie ciągu linii wewnętrznych od zewnętrznych, wyciągniętych o 1m. Zmieńmy to, wchodząc w tryb edycji okna, poprzez dwukrotne kliknięcie na nim w widoku drzewa:

Zobaczysz komponent *Domyślny*, który został utworzony automatycznie przez narzędzie Okno, który wykorzystuje 5 linii *(zawsze odejmując pozostałe od największej)* i ma wartość wyciągnięcia 1m. Zmieńmy jego wartość wyciągnięcia na 0.1, aby dopasować go do tego, co zostało zastosowane w drzwiach.

Następnie dodajmy 4 nowe panele szklane, każdy za pomocą jednegociągu linii, i nadajmy im wartość wyciągnięcia 0,01, i przesunięcie 0,05, tak aby były umieszczone na środku ramy. Tak będzie wyglądać Twoje okno, gdy skończysz:

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

Przypuszczam, że teraz musiałeś poznać moc tego systemu: Każda kombinacja ram i paneli o dowolnym kształcie jest możliwa do uzyskania. Jeśli możesz narysować ją w układzie 2D, może ona istnieć jako w pełni poprawny obiekt 3D.

Teraz narysujmy inne fragmenty, a potem przeniesiemy wszystko razem na miejsce. Ale najpierw musimy zrobić kilka poprawek do podstawowego rysunku 2D, ponieważ brakuje niektórych linii w miejscu, gdzie okna stykają się ze schodami. Możemy to naprawić przesuwając linię schodów o 2,5 cm za pomocą narzędzia [Odsunięcie](Draft_Offset/pl.md) *(oczywiście z wciśniętym klawiszem **ALT**, aby skopiować nasze linie zamiast je przesuwać)*. Teraz możemy narysować nasz układ, za pomocą narzędzia [Polilinia](Draft_Wire/pl.md), a następnie przekonwertować go do szkicu, aby w końcu zrobić z niego okno.

Po zrobieniu tego wielokrotnie *(zrobiłem to w 4 oddzielnych kawałkach, ale decyzja należy do Ciebie)*, mamy naszą fasadę kompletną:

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Teraz, tak jak poprzednio, chodzi tylko o obracanie elementów i przesuwanie ich do właściwej pozycji:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

Ostatni brakujący element, to fragment ściany, który nie pojawił się na widoku planu, więc musimy go dodać. Mamy na to kilka możliwości, zdecydowałem się narysować linię na płaszczyźnie podłoża, aby przesunąć ją na odpowiednią wysokość, a następnie stworzyć z niej ścianę. Następnie musimy wyłowić naszą dachową objętość odejmowania *(pozostała pewnie w ostatniej kolumnie)*, a następnie odjąć ją. Teraz ta strona budynku jest już gotowa:

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Gotowy? Niezupełnie. Spójrz na obrazek powyżej, zrobiliśmy drzwi z ramką 5cm, pamiętaj *(była to domyślna wartość z ustawień domyślnych)*. Ale pozostałe okna mają ramki 2,5cm. To musi zostać poprawione.

### Edycja parametrów okien 

Widzieliśmy już, jak budować i aktualizować komponenty okna, poprzez tryb edycji okna, ale możemy również edytować szkic bazowy. Zaprogramowane okna nie różnią się od niestandardowych okien, narzędzie [Okna](Arch_Window/pl.md) utworzyło tylko podstawowy szkic dla Ciebie. Wybierz nasz obiekt drzwi *(oryginał, nie kopię, pamiętaj, zrobiliśmy klon)*, i rozwiń go w widoku drzewa. Tam znajduje się nasz szkic. Kliknij dwukrotnie na niego, aby przejść do trybu edycji.

Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) jest niezwykle wydajnym narzędziem. Nie posiada ono niektórych z udogodnień środowiska [Rysunek Roboczy](Draft_Workbench/pl.md), takich jak przyciąganie czy obróbka płaszczyzn, ale posiada wiele innych zalet. We programie FreeCAD często będziesz używał jednego lub drugiego, w zależności od potrzeby. Najważniejszą cechą szkicownika są wiązania. Ograniczenia pozwalają na automatyczne ustalanie położenia niektórych elementów względem innych. Na przykład, możesz wymusić, aby odcinek był zawsze pionowy, lub aby zawsze znajdował się w pewnej odległości od innego.

Kiedy edytujemy nasz szkic drzwi, widzimy, że jest on wykonany na całkowicie związanym szkicu:

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Teraz jedyne co musimy zrobić, to edytować dystans 5cm pomiędzy linią zewnętrzną a wewnętrzną, klikając dwukrotnie i zmieniając wartość na 2.5cm *(Pamiętaj, że w momencie pisania tego, jednostki nadal nie są w pełni funkcjonalne)*. Po kliknięciu przycisku OK, nasze drzwi *(i ich klon)* zostaną zaktualizowane.

## Praca bez obsługi 2D 

Do tej pory pracowało się stosunkowo łatwo, ponieważ mieliśmy do dyspozycji rysunki 2D, na których opierały się nasze prace. Teraz jednak musimy wykonać przeciwległą fasadę i szklane atrium, a wszystko staje się coraz bardziej skomplikowane: Rysunek przeciwległej fasady ma wiele niedociągnięć, w ogóle nie obrazuje atrium, a my po prostu nie mamy rysunku wewnętrznych ścian atrium. Będziemy więc musieli sami wymyślić kilka rzeczy. Upewnij się, że spojrzałeś na [ilustracje źródłowe](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/), by dowiedzieć się, jak wszystko jest zrobione. Albo zrób to jak chcesz!

Jedno możemy już zrobić: zduplikować skomplikowane okno schodów za pomocą narzędzia [Przesuń](Draft_Move/pl.md), ponieważ jest ono identyczne po obu stronach:

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Zauważ, że teraz wolałbym zduplikować za pomocą narzędzia [Przesuń](Draft_Move/pl.md) zamiast używać [kolonowania](Draft_Clone/pl.md), ponieważ obecnie klon nie obsługuje różnych kolorów wewnątrz obiektów. Różnica polega na tym, że klon jest kopią ostatecznego kształtu oryginalnego obiektu, podczas gdy jeśli skopiujesz obiekt, tworzysz nowy obiekt i nadajesz mu wszystkie te same właściwości co oryginał *(a więc również jego szkic bazowy i definicję komponentów okna, które są przechowywane jako właściwości)*.

Teraz musimy ogarnąć te części, które nigdzie nie są rysowane. Zacznijmy od szklanej ściany między salonem i atrium. Łatwiej będzie ją narysować na widoku elewacji, bo uzyskamy odpowiednią wysokość zadaszenia. Gdy znajdziesz się w widoku planu, możesz obracać widok z menu Widok → Widoki standardowe → Obracaj w lewo lub w prawo, aż do uzyskania wygodnego widoku do pracy, w ten sposób:

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Zauważ, że na powyższym obrazku wykonałem linię od modelu do lewej części, aby uzyskać dokładną szerokość okna. Następnie odtworzyłem tę szerokość na widoku elewacji i podzieliłem ją na 4 części. Następnie zbudowałem jeden główny element okna, plus 4 dodatkowe okna do drzwi przesuwnych. Szkicownik ma czasem trudności z nakładaniem się na siebie linii, dlatego wolałem, aby były one tak rozdzielone:

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

Po wykonaniu niezbędnych obrotów, wszystko idealnie się układa:

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

Potrzebujemy tam jeszcze kawałek narożnika. Mała przydatna sztuczka z narzędziem [Wybór płaszczyzny](Draft_SelectPlane/pl.md), jeśli po naciśnięciu przycisku mamy wybraną płaszczyznę, płaszczyzna robocza pasuje do tej płaszczyzny *(przynajmniej jej położenie, a jeśli jest prostokątna, to stara się również dopasować jej osie)*. Jest to przydatne do rysowania obiektów 2D bezpośrednio na modelu, np. tutaj możemy narysować prostokąt, który ma być wyciągnięty bezpośrednio w jego prawidłowym położeniu:

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

Następnie zróbmy dwie pozostałe części. Pierwsza jest łatwa, jest kopią tego, co jest po drugiej stronie, więc możemy po prostu skorzystać z rysunku 2D:

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">

Drugi element jest nieco skomplikowany, patrząc na zdjęcia widzimy, że ma wiele pionowych podziałów, jak okna schodów. Przez przypadek *(lub bardzo dobry projekt z Vilanova Artigas)*, szerokość naszego okna, 4,50m, jest dokładnie taka sama jak okna schodowego, więc możemy użyć dokładnie takiego samego podziału: 15 sztuk 30cm. Tutaj użyłem narzędzia [Rysunek roboczy: Szyk ortogonalny](Draft_OrthoArray/pl.md), aby przekopiować dwie linie 15 razy, a na nich narysowałem prostokąty:

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Kiedy już to zrobimy, możemy stworzyć nasze okno tą samą metodą, którą już znamy. Kolejna mała użyteczna sztuczka, na wypadek, gdybyś sam jeszcze jej nie znalazł: Podczas edycji okna, jeśli zmienisz nazwę komponentu, w rzeczywistości tworzy on jego duplikat. Tak więc, aby utworzyć 15 wewnętrznych paneli szklanych, zamiast klikać 15 razy przycisk dodaj i wypełniać 15 razy dane, możesz po prostu kontynuować edycję jednego z nich i zmieniać jego nazwę i linie, w efekcie będzie on za każdym razem tworzył kopię.

Po obróceniu okna i przesunięciu go na miejsce atrium jest gotowe:

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">

## Edycje i poprawki 

Teraz, gdy patrzymy na naszą tylną elewację i porównujemy ją z planem, widzimy, że są pewne różnice, które trzeba naprawić. Mianowicie, okna w sypialni są mniejsze niż początkowo myślałem i będziemy musieli dodać jeszcze kilka ścian. Aby to zrobić właściwie, niektóre podłogi muszą zostać skrócone:

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">

Mamy oczywiście kilka sposobów, aby to zrobić, odejmowanie objętości byłoby łatwym sposobem, ale niepotrzebnie skomplikowałoby model. Lepiej zmontować linię główną każdego z pięter. Tutaj właśnie zaczyna działać tryb [Draft Edit](Draft_Edit/pl.md). Rozwijając zawartość tych pięter w widoku drzewa, a następnie czyniąc ich linie bazowe widocznymi, możemy je następnie kliknąć dwukrotnie, aby wejść w tryb edycji. Tam możemy przenieść ich punkty, lub dodać nowe albo usunąć wybrane punkty. Dzięki temu, edycja naszych płyt podłogowych staje się łatwa.

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

Po dodatkowym wysiłku fizycznym *(osoba, która wykonała te rysunki, stała się oczywiście dość leniwa, skoro ta ostatnia elewacja, często jest źle narysowana)*, mamy w końcu nasz cały dom:

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Zwróć uwagę na rurę kominową, która jest wykonana z koła, które wykorzystałem do wykonania otworu w bloku kominowym, który wyciągnąłem, a następnie zamieniłem na rurę za pomocą narzędzia [Part: Odsunięcie](Part_Offset/pl.md).


{{Note|Problemy w obiektach|Czasami przedmiot, który stworzyłeś, może mieć problemy. Na przykład, obiekt, na którym się opierał, został usunięty, a zatem nie może ponownie obliczyć swojego kształtu. Zazwyczaj są one sygnalizowane przez mały czerwony znak na ikonie i/lub ostrzeżenie w oknie wyjściowym. Nie istnieje żaden ogólny przepis na rozwiązanie tych problemów, ponieważ mogą one mieć wiele źródeł. Jednak najprostszym sposobem na ich rozwiązanie często jest ich usunięcie, a jeśli nie usunąłeś ich podstawowych obiektów, odtwórz je.}}

## Rezultat

Teraz, po całej ciężkiej pracy, przez którą przeszliśmy, aby zbudować ten model, przychodzi nagroda: Co możemy z nim zrobić? Zasadniczo, jest to duża zaleta pracy z BIM, wszystkie nasze tradycyjne potrzeby architektoniczne, takie jak rysunki 2d *(plany, przekroje, itp.)*, renderingi i obliczenia *(rachunki ilościowe, itp.)* mogą być pobierane z modelu. I jeszcze lepiej, regenerowane za każdym razem, gdy model się zmienia. Pokażę Ci tutaj, jak uzyskać te różne dokumenty.

### Przygotowania 

Zanim zaczniemy eksportować rzeczy, warto się zastanowić, co zrobić: Jak widzieliście, nasz model staje się coraz bardziej złożony, z wieloma relacjami pomiędzy obiektami. Może to spowodować, że kolejne operacje obliczeniowe, takie jak przecięcie modelu, staną się bardzo skomplikowane. Jednym z szybkich sposobów, aby magicznie uprościć swój model, jest usunięcie całej tej złożoności, poprzez wyeksportowanie go do formatu [STEP](http://en.wikipedia.org/wiki/ISO_10303-21). Format ten zachowa całą twoją geometrię, ale odrzuci wszystkie zależności i konstrukcje parametryczne, zachowując tylko ostateczny kształt. Kiedy ponownie zaimportujesz ten plik STEP do programu FreeCAD, otrzymasz model, który nie posiada żadnych relacji i o wiele mniejszy rozmiar pliku. Pomyśl o tym jako o pliku wyjściowym, który możesz odtworzyć w dowolnym momencie z pliku głównego:

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">

### Eksportowanie do IFC i innych aplikacji 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

Jedną z bardzo podstawowych rzeczy, których potrzebujesz podczas pracy z BIM, jest możliwość importu i eksportu plików [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). W dalszym ciągu jest to praca na etapie tworzenia FreeCAD. Format [IFC](Arch_IFC/pl.md) jest już obsługiwany, a importowanie plików IFC do FreeCAD jest dość niezawodne. Eksportowanie jest jednak nadal procesem eksperymentalnym i ma obecnie wiele ograniczeń. Jednak sytuacja jest dobra i wkrótce powinniśmy uzyskać możliwość niezawodnego eksportu do formatu IFC.

[Eksport IFC](Arch_IFC/pl.md) po zainstalowaniu niezbędnych bibliotek oprogramowania, wymaga bardzo niewielkiej konfiguracji. Musisz tylko odtworzyć strukturę budynku, która jest potrzebna we wszystkich plikach IFC, dodając [budowlę](Arch_Building/pl.md) do pliku, a następnie [podłogę](Arch_Floor.md), a następnie przenosząc wszystkie grupy obiektów, które składają się na Twój model. Upewnij się, że pominąłeś geometrię konstrukcji *(wszystkie elementy 2D, które rysowaliśmy)*, aby uniknąć niepotrzebnego obciążania pliku IFC.

Kolejną rzeczą do ustawienia, jest sprawdzenie właściwości **Role** elementów konstrukcyjnych. Ponieważ IFC nie posiada uniwersalnego elementu konstrukcyjnego, jak FreeCAD, musimy przypisać im role *(kolumna, belka itp.)* Po to aby eksporter wiedział jaki element stworzyć w pliku IFC.

W tym przypadku potrzebujemy całego naszego systemu architektonicznego, więc eksporter IFC może wiedzieć, czy obiekt musi być eksportowany jako ściana lub kolumna, więc używamy naszego głównego modelu, a nie naszego wyjściowego modelu.

Kiedy to zrobisz, po prostu wybierz swój obiekt budowlany i wybierz format **Industry Foundation Classes**. Eksportowanie do aplikacji innych niż BIM, takich jak [Sketchup](http://www.sketchup.com/) jest również łatwe, masz do dyspozycji kilka formatów eksportu, takich jak [Collada](Arch_DAE/pl.md), STEP, IGES lub OBJ.




### Renderowanie

FreeCAD posiada również moduł renderujący, środowisko pracy [Raytracing](Raytracing_Workbench/pl.md). Tee środowisko obsługuje obecnie dwa silniki renderujące, [PovRay](http://www.povray.org/) i [LuxRender](http://www.luxrender.net). Ponieważ FreeCAD nie jest przeznaczony do renderowania obrazów, funkcje, które oferuje to Środowisko pracy Raytracing, są nieco ograniczone. Najlepszym sposobem działania, gdy chcesz uzyskać dobry rendering, jest wyeksportowanie modelu do formatu opartego na siatce, takiego jak OBJ lub STL, i otwarcie go w aplikacji właściwszej do tego celu, takiej jak [blender](http://www.blender.org). Poniższy obrazek został wyrenderowany przy użyciu silnika cykli blendera:

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

Ale dla potrzeb szybkiego renderowania, Środowisko pracy Raytracing może już wykonać dobrą robotę, z tą zaletą, że jest bardzo łatwe w konfiguracji, dzięki systemowi szablonów. Jest to rendering naszego modelu w pełni wykonany w programie FreeCAD, z silnikiem Luxrender, przy użyciu wbudowanego szablonu.

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

Środowisko pracy Raytracing nadal oferuje bardzo ograniczoną kontrolę nad materiałami, ale oświetlenie i otoczenie są zdefiniowane w szablonach, dzięki czemu można je w pełni dostosować do indywidualnych potrzeb.

### Rysunki 2D 

Z pewnością najważniejszym zastosowaniem BIM jest automatyczne tworzenie rysunków 2D. Robi się to w programie FreeCAD za pomocą narzędzia [wybór płaszczyzny](Arch_SectionPlane/pl.md). Narzędzie to pozwala na umieszczenie płaszczyzny przekroju obiektu w widoku 3D, który można zorientować w celu utworzenia planów, przekrojów i elewacji. Płaszczyzny przekroju muszą wiedzieć, jakie obiekty muszą być brane pod uwagę, więc po ich utworzeniu należy dodać do nich obiekty za pomocą narzędzia [Dodaj](Arch_Add/pl.md). Możesz dodać pojedyncze obiekty, lub, co wygodniejsze, grupę, piętro lub cały budynek. Pozwala to na późniejszą łatwą zmianę zakresu danej płaszczyzny przekroju, poprzez dodawanie lub usuwanie obiektów do/z tej grupy. Każda zmiana tych obiektów zostanie odzwierciedlona w widokach tworzonych przez płaszczyznę przekroju.

Płaszczyzna przekroju automatycznie generuje widoki cięcia obiektów, które przecina. Innymi słowy, w celu utworzenia widoków zamiast przekrojów, wystarczy umieścić płaszczyznę przekroju na zewnątrz obiektów.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">

Płaszczyzny przekroju mogą wytwarzać dwa różne rezultaty: Obiekty [kształtu](Part_Workbench/pl.md), które znajdują się w tym samym dokumencie co model 3D, lub [widoki rysunku](Drawing_Workbench/pl.md), które są wykonane do użycia na arkuszu rysunkowym utworzonym przez środowisko pracy [Kreślenie](Drawing_Workbench/pl.md). Każdy z nich zachowuje się inaczej i ma swoje własne zalety.

**Widoki kształtu**

Powyższe wyniki są generowane za pomocą narzędzia [kształt na widok](Draft_Shape2DView.md) z wybraną płaszczyzną przekroju. Tworzysz widok 2D modelu bezpośrednio w przestrzeni 3D, jak na obrazie powyżej. Główną zaletą jest to, że możesz na nich pracować używając narzędzi środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) *(lub innego standardowego narzędzia FreeCAD)*, dzięki czemu możesz dodawać teksty, wymiary, symbole, itp:

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

Na obrazku powyżej, dla każdego przekroju stworzono dwa widoki [Shape2D](Draft_Shape2DView.md), z których jeden pokazuje wszystko, a drugi tylko linie cięcia. To pozwala nam nadać mu inną wagę linii i włączyć kreskowanie. Następnie dodano wymiary, teksty i symbole, a także zaimportowano kilka bloków DXF, które reprezentują meble. Te widoki można następnie łatwo wyeksportować do DXF lub DWG i otworzyć w swojej ulubionej aplikacji 2D CAD, takiej jak [LibreCAD](http://www.librecad.org) lub [DraftSight](http://www.3ds.com/products-services/draftsight/overview/), gdzie można nad nimi dalej pracować:

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Zauważ, że niektóre funkcje nadal nie są obsługiwane przez [DXF/DWG exporter](Draft_DXF.md), więc wynik w Twojej aplikacji 2D może się nieco różnić. Na przykład, na powyższym obrazku musiałem przerobić kreskowanie i poprawić położenie niektórych tekstów wymiarowych. Jeśli umieścisz swoje obiekty w FreeCAD w różnych grupach, staną się one warstwami w Twojej aplikacji 2D CAD.

**Rysunki widoków**

Innym rodzajem rezultatu, który może być uzyskany z [Płaszczyzny przekroju](Arch_SectionPlane/pl.md) jest [Widok](Drawing_Workbench/pl.md). Wygenerowany jest on za pomocą narzędzia [Draft: Drawing](Draft_Drawing/pl.md) z wybraną płaszczyzną przekroju. Ta metoda ma jedno duże ograniczenie w porównaniu do poprzedniej: masz ograniczone możliwości edycji wyników, a w tej chwili takie rzeczy jak wymiarowanie czy kreskowanie nadal nie są obsługiwane automatycznie.

Z drugiej strony, ostateczny wynik jest łatwiejszy do operowania, a możliwości graficzne formatu SVG są ogromne, w przyszłości bez wątpienia będzie to preferowana metoda. W tej chwili jednak lepsze wyniki osiągniesz korzystając z poprzedniej.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">

Na powyższym obrazie geometria jest bezpośrednim wyjściem płaszczyzny przekroju, ale dodano kilka innych obiektów Draft, takich jak wymiary i zakreskowane wielokąty, i utworzono z nich inny obiekt widoku o tej samej skali i wartościach przesunięcia za pomocą [Draft: Drawing](Draft_Drawing.md). W przyszłości takie operacje będą wykonywane bezpośrednio na stronie rysunku, pozostawiając całkowicie czysty model.

### Wydobywanie danych o ilości 

Jest to kolejne bardzo ważne zadanie do wykonania na modelach BIM. W FreeCAD wszystko wygląda dobrze od samego początku, ponieważ jądro OpenCasCade FreeCAD zajmuje się już obliczaniem długości, powierzchni i objętości dla wszystkich produkowanych przez siebie kształtów. Ponieważ wszystkie obiekty środowiska [Architektura](Arch_Workbench/pl.md) są bryłami, zawsze masz gwarancję, że będziesz w stanie uzyskać z nich objętość.

**Używanie arkusza kalkulacyjnego**

Aby wypełnić arkusz kalkulacyjny wartościami pobranymi z modelu, można użyć narzędzia [Harmonogram](Arch_Schedule/pl.md).

![](images/Arch_schedule_example03.jpg )

**Tryb badania**

Innym sposobem na badanie modelu i uzyskanie wartości, jest użycie trybu [Przegląd](Arch_Survey/pl.md). W tym trybie możesz kliknąć na punkty, krawędzie, powierzchnie lub kliknąć dwukrotnie aby wybrać całe obiekty. Otrzymasz w ten sposób wartości dotyczące wysokości, długości, powierzchni lub objętości, pokazane na modelu, wydrukowane w oknie wyjściowym FreeCAD i skopiowane do schowka. Dzięki temu możesz łatwo wybrać i wkleić wartości w innej uruchomionej aplikacji.

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">

## Podsumowanie

Mam nadzieję, że poradnik dostarczy Państwu dobrego przeglądu dostępnych narzędzi, proszę odnieść się do dokumentacji środowiska pracy [Architrktura](Arch_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md) po dalsze informacje *(jest więcej narzędzi, o których tutaj nie wspomniałem)*, oraz, bardziej ogólnie, do reszty dokumentacji [FreeCAD](Main_Page/pl.md). Odwiedź również [forum](http://forum.freecadweb.org), wiele problemów można tam zazwyczaj rozwiązać w mgnieniu oka i śledź mój [blog](http://yorik.uncreated.net/guestblog.php?tag=freecad), aby uzyskać informacje o rozwoju Środowiska pracy Arch.

Plik utworzony podczas tego ćwiczenia można znaleźć [ze strony yorik-a](http://yorik.uncreated.net/archive/projects/casa_artigas.fcstd).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Arch](Arch_Workbench.md) > Arch tutorial/pl
