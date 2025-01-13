---
 TutorialInfo:l
   Topic: Poradnik jak przenieść Wikihouse
   Level: średnio zaawansowany / zaawansowany
   Time: 60 minut
   Author: -
   FCVersion: -
   Files: nie dołączono
---

# Wikihouse porting tutorial/pl







## Wprowadzenie

Ten samouczek pokaże ci, jak przekonwertować pliki [SketchUp](http://www.sketchup.com/) używane przez projekt [Wikihouse](http://wikihouse.cc/) do FreeCAD, korzystając z narzędzi [Arch Panel](Arch_Panel.md) w FreeCAD. Rezultatem jest pełna kopia oryginalnego pliku SketchUp, z wyjątkiem tego, że stał się on w pełni parametryczny. Poziom parametryczności ostatecznego pliku zależy od włożonej w niego pracy, jak wyjaśniono poniżej. Możliwe jest jednak robienie rzeczy krok po kroku i przebudowanie pliku Wikihouse dość szybko, pozostawiając bardziej długotrwałą konwersję profili bazowych na szkice, na później.

Ten samouczek będzie wymagał średnio zaawansowanej znajomości FreeCAD, to znaczy, że jesteś w stanie znaleźć drogę między różnymi środowiskami pracy i narzędziami, jesteś już w stanie modelować proste obiekty, a przede wszystkim czujesz się komfortowo używając narzędzi [Przesuń](Draft_Move/pl.md) i [Obróć](Draft_Rotate/pl.md). Będziemy używać głównie narzędzi środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) i [Architektura](Arch_Workbench/pl.md), ale znajomość [Szkicownika](Sketcher_Workbench/pl.md) będzie niezbędna podczas konwertowania profili bazowych na szkice.

Ponieważ projekt Wikihouse jest z natury otwarty, pliki można łatwo znaleźć na stronie internetowej projektu, ale także na [SketchUp 3D Warehouse](https://3dwarehouse.sketchup.com/search.html?q=wikihouse&backendClass=both) lub w repozytoriach projektu [github](https://github.com/wikihouseproject). Preferowanym formatem używanym przez projekt jest Sketchup, więc większość plików, które tam znajdziesz, jest w tym formacie.

W poniższym samouczku wykorzystaliśmy plik [Chassis](https://github.com/wikihouseproject/Microhouse/blob/master/microhouse_0.5_chassis.skp) z podprojektu Wikihouse Microhouse.



## Przygotowanie pliku Sketchup 

Pierwszą rzeczą, którą musisz zrobić, jest otwarcie pliku w SketchUp i usunięcie wszystkiego, czego nie chcesz eksportować. Wyeksportujemy tylko jedną sekcję mikrodomu, więc wszystko inne musi zostać usunięte.

![](images/Arch_Wikihouse_05.jpg )

Elementy Wikihouse w SketchUp są tworzone w specyficzny sposób: Poprzez dodawanie małych \"kawałków\" w celu stworzenia różnych komponentów:

![](images/Arch_Wikihouse_06.jpg )

Nie tak będziemy postępować w FreeCAD. Ponieważ jedną z najpotężniejszych funkcji FreeCAD są [wiązania szkicownika](Sketcher_Workbench/pl.md), lepiej skorzystajmy z tego i oprzyjmy wszystkie nasze elementy Wikihouse na Szkicach. W ten sposób modyfikacja dowolnej części może być wykonana w środowisku pracy [Szkicownik](Sketcher_Workbench/pl.md), co jest znacznie wygodniejsze.

Aby przekształcić nasze obiekty SketchUp w szkice FreeCAD, które można następnie wykorzystać do stworzenia obiektów [Panel](Arch_Panel/pl.md) środowiska pracy Architektura, musimy wyodrębnić jedną, płaską powierzchnię z każdego elementu Wikihouse. Grubość zostanie ponownie dodana później, we FreeCAD, bezpośrednio we właściwościach Arch Panel. W ten sposób zachowamy również parametryczność. Aby przekształcić każdy komponent Wikihouse w pojedynczą, płaską powierzchnię, wejdź do każdego komponentu, klikając go dwukrotnie, a następnie wybierz każdy podkomponent i kliknij prawym przyciskiem myszy → Rozbij, aż wszystkie podkomponenty zostaną rozbite, a komponent będzie składał się tylko z powierzchni i krawędzi:

![](images/Arch_Wikihouse_08.jpg )

Gdy to zrobisz, zaznacz wszystko w komponencie i odznacz, naciskając **Shift** + dwukrotnie kliknięcie myszką, każdą przednią ścianę komponentu. Upewnij się, że kliknąłeś dwukrotnie, a nie pojedynczo, ponieważ w przeciwnym razie odznaczysz tylko powierzchnię, a nie jej krawędzie *(które również będziemy musieli zachować)*. Następnie odznaczyliśmy już wszystko, co chcieliśmy zachować, więc wystarczy nacisnąć klawisz usuwania. Teraz nasz komponent jest tylko jedną dużą płaską powierzchnią.

![](images/Arch_Wikihouse_07.jpg )

Powtórz tę czynność dla każdego komponentu. Ponieważ wiele z nich jest zduplikowanych, nie jest to tak duże zadanie, na jakie wygląda. Poza tym, jeśli nie jesteś zaznajomiony z systemem Wikihouse, ten krok pozwoli ci całkiem dobrze zrozumieć, jak to działa.

Gdy nasz dom jest w pełni zbudowany z płaskich elementów, możemy zaznaczyć wszystko i wyeksportować do pliku .dae, a następnie zaimportować ten plik do FreeCAD. Pamiętaj, aby zaznaczyć opcję \"trianguluj wszystko\"



## Rozwiązanie błędu podwójnych ścian 

Jest pewien nieprzyjemny problem, na który nie znalazłem lepszego rozwiązania: Siatki wyeksportowane ze SketchUp do formatu .dae mają zduplikowane ściany. Każda ściana staje się w rzeczywistości dwiema ścianami. Najprostszym sposobem, jaki do tej pory znalazłem, jest otwarcie wyeksportowanego pliku w [Blender](http://www.blender.org) w celu naprawy:

1.  Otwórz plik dae w Blenderze (**File → Import → Collada**)
2.  Wybierz komponent i naciśnij **TAB**, aby przejść do trybu edycji.
3.  Naciśnij **A**, aby odznaczyć wszystko, a następnie **A** ponownie, aby zaznaczyć wszystko.
4.  Naciśnij **W** → Usuń podwójnie
5.  Naciśnij **TAB**, aby wyjść z trybu edycji.
6.  Powtórz dla wszystkich komponentów
7.  Zapisz nowy plik [DAE](Arch_DAE.md) (**File → Export → Collada**).

Zwykle powyższa operacja nie powinna zmienić skali, ale zawsze dobrze jest sprawdzić, używając narzędzi pomiarowych, czy zaimportowana geometria ma prawidłową skalę przed przejściem dalej. W razie potrzeby konieczne może być dostosowanie ustawień eksportu Collada w Blenderze.



## Import i konwersja do polilinii 

Należy pamiętać, że może być łatwiej przejść przez części i traktować + eksportować obiekty grupa po grupie, tak jak to zrobiliśmy poniżej, wyeksportowaliśmy tylko pierwszą warstwę, wykonaną z żółtych elementów w SketchUp. Elementy te pojawią się w FreeCAD jako obiekty [siatkowe](Mesh_Workbench/pl.md):

![](images/Arch_Wikihouse_09.jpg )

Następnym krokiem jest utworzenie polilinii z każdej z naszych siatek. Istnieje wygodna makrodefinicja o nazwie [Extract Wires from Mesh](Macro_Extract_Wires_from_Mesh/pl.md), które właśnie to robi. Zainstaluj je *(instrukcje znajdziesz na stronie [Makrodefinicje](Macros/pl.md))*, a następnie po kolei *(możesz zrobić wszystkie naraz, ale to makro zajmuje trochę czasu)* przekonwertuj wszystkie nasze siatki na obiekty polilinii:

![](images/Arch_Wikihouse_10.jpg )

Moglibyśmy teraz tworzyć obiekty typu [Panel](Arch_Panel/pl.md) z każdego z tych obiektów przypominających polilinię, po prostu wybierając je i naciskając przycisk [Panel](Arch_Panel/pl.md). Jednak ich podstawowy kształt nie byłby parametryczny. Mamy teraz kilka opcji: Możemy przekształcić każdy komponent w szkic, używając narzędzia [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md), ale będą to raczej dość złożone szkice i mogą nie być zbyt łatwe w zarządzaniu na wolnej maszynie, lub możemy przekształcić każdą pojedynczą polilinię *(kontur i każdy otwór)* szkicu w osobny szkic. Pozwoliłoby nam to na przykład na ponowne wykorzystanie typowego otworu, wykonanie go tylko raz, a następnie powielenie go za pomocą narzędzia [Klonuj](Draft_Clone/pl.md) w celu wykonania innych otworów. W ten sposób wystarczy edytować jeden otwór, aby edytować wszystkie.

Makrodefinicja [Wyodrębnij linie z siatki](Macro_Extract_Wires_from_Mesh/pl.md) również czasami zawodzi w znajdowaniu zamkniętych polilinii wewnątrz siatki, co nie daje poprawnych paneli. Prostym sposobem na ponowne skomponowanie polilinii komponentu jest następująca procedura:

1.  Wybierz komponent, opcjonalnie ukryj wszystko inne, aby był lepiej widoczny
2.  Użyj narzędzia [Rozbij](Draft_Downgrade/pl.md). Zostanie on przekształcony w serię pojedynczych krawędzi
3.  Rozpocznij zaznaczanie otworów z **Ctrl** lub używając **Shift** + **B**, aby zaznaczyć obszar.
4.  Naciśnij [Ulepsz](Draft_Upgrade/pl.md), aby przekształcić każdy otwór w pojedynczą krawędź.
5.  Na koniec zaznacz wszystkie pozostałe pojedyncze krawędzie w drzewie, które tworzą kontur, i wybierz [Rozbij](Draft_Upgrade/pl.md).
6.  Wybierz z menu **Część → Kształt złożony → Utwórz kształt złożony**\'\', aby połączyć wszystkie polilinie w jeden obiekt.
7.  Wybierz związek i naciśnij przycisk [Arch Panel](Arch_Panel/pl.md).

![](images/Arch_Wikihouse_11.jpg )

Istnieje wiele możliwych strategii, w zależności od tego, jak edytowalny i precyzyjny ma być rezultat. Obiekt [Panel](Arch_Panel/pl.md) potrzebuje obiektu bazowego wykonanego z polilinii. Nie ma znaczenia, w jaki sposób obiekt ten jest tworzony, czy jest to pojedynczy szkic, czy, jak w powyższym przykładzie, połączenie różnych szkiców lub obiektu środowiska Rysunek Roboczy.



## Konwersja do szkicu 

Tę część można również wykonać później, można już utworzyć panele z każdego z komponentów, ale zobaczmy już teraz, jak przekonwertować obiekt podobny do polilinii na szkic:

1.  Stwórz kopię obiektu polilinii za pomocą **Ctrl** + **C**, **Ctrl** + **V**. W ten sposób możemy go modyfikować, ale nadal utrzymywać w prawidłowej lokalizacji
2.  Przesuń i obróć go tak, aby leżał w płaszczyźnie XY, używając narzędzi [Przesuń](Draft_Move/pl.md) i [Obróć](Draft_Rotate/pl.md). Nie jest to konieczne, ale następny punkt czasami zawodzi w przeciwnym razie
3.  Użyj [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md), aby przekształcić przewód w szkic. Ostrzegam, że może się to nie udać lub zająć bardzo dużo czasu w przypadku złożonych polilinii. Najlepiej jest rozłożyć obiekt na pojedyncze polilinie, jak pokazano powyżej.
4.  Jeśli powyższe polecenie zawiedzie, dwukrotnie użyj narzędzia [Ulepsz](Draft_Upgrade/pl.md) na obiekcie podobnym do polilinii, aby przekonwertować go na ścianę, a następnie na [polilinię](Draft_Wire/pl.md), przed użyciem [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md), zwykle działa lepiej, ponieważ Draft Wire lepiej śledzi kolejność wierzchołków wewnątrz polilinii.
5.  Krzywe składają się z kilku małych segmentów. Można je pozostawić bez zmian, ale wprowadzają one wiele ograniczeń dotyczących punktów końcowych. Lepiej zastąpić je łukami. Jest to dość łatwe do zrobienia, wystarczy usunąć małe segmenty i zastąpić je łukiem. Łuk może być następnie styczny do sąsiednich segmentów, ale upewnij się, że pozycja tych segmentów jest zablokowana przed wykonaniem tej operacji, ponieważ spowoduje to ich przesunięcie.
6.  Jeśli pracowałeś z kilkoma szkicami, utwórz z nich [Utwórz kształt złożony](Part_Compound/pl.md).
7.  Utwórz na jego podstawie [Panel](Arch_Panel/pl.md).
8.  Obróć / przesuń go z powrotem na miejsce za pomocą narzędzi [Przesuń](Draft_Move/pl.md) i [Obróć](Draft_Rotate/pl.md).

![](images/Arch_Wikihouse_12.jpg )



## Przebudowa Wikihouse i eksportowanie wyciętych arkuszy 

Upewnij się również, że nie powielasz żadnej zduplikowanej części. Zamiast tego wybierz narzędzie [Klonuj](Draft_Clone/pl.md), aby zduplikować części oparte na tym samym profilu, dzięki czemu wszystkie będą miały ten sam obiekt profilu. Następnie, ponieważ mamy już kontur w odpowiednim miejscu, można go łatwo obrócić i przesunąć klon do właściwej pozycji za pomocą narzędzi [Obróć](Draft_Rotate/pl.md) i [Przesuń](Draft_Move/pl.md).

Po chwili cała sekcja Microhouse jest gotowa.

![](images/Arch_Wikihouse_01.jpg )

Możemy teraz łatwo utworzyć arkusze cięcia, które są plikami DXF, które zostaną wysłane do warsztatu, który wytnie rzeczywiste panele. Najprostszym sposobem na to jest zaznaczenie wszystkiego w dokumencie za pomocą **Ctrl** + **A**, a następnie użycie narzędzia [Panelizacja do cięcia](Arch_Panel_Cut/pl.md) środowiska Architektura. Spowoduje to utworzenie jednego obiektu Panel Cut dla każdego obiektu Panel znajdującego się w zaznaczeniu. Odsuwając je od siebie, uzyskamy przejrzysty widok wszystkich elementów:

![](images/Arch_Wikihouse_02.jpg )

Następnie musimy \"zagnieździć\" nasze elementy, czyli przesunąć i obrócić je tak, aby zajmowały jak najwięcej miejsca w danym panelu, aby wygenerować jak najmniejsze straty materiału. Ta operacja niestety musi być wykonana samodzielnie, ale jeśli korzystasz z projektu Wikihouse, który już wyprodukował pocięte arkusze, kopiowanie ich przebiega dość szybko:

1.  Aby upewnić się, że wszystko pozostanie w płaszczyźnie XY, zaleca się ustawienie [płaszczyzny roboczej](Draft_SelectPlane/pl.md) na XY *(góra)*.
2.  Utwórz [Arkusz panela](Arch_Panel_Sheet/pl.md).
3.  Nadaj mu żądane wartości szerokości i wysokości *(elementy Wikihouse są zazwyczaj drukowane na arkuszach sklejki 122x244cm)*.
4.  Przenieś go w dogodne miejsce za pomocą narzędzia [Przesuń](Draft_Move/pl.md) środowiska Rysunek roboczy.
5.  Opcjonalnie ustaw wartości marginesów, aby pomóc w pozycjonowaniu wyciętych elementów.
6.  Przesuń i obróć poszczególne obiekty [Panelizacji do cięcia](Arch_Panel_Cut/pl.md) tak, aby zmieściły się wewnątrz arkusza panelu.
7.  Gdy będziesz mniej więcej gotowy, wybierz arkusz panelu i kliknij go dwukrotnie w oknie [widoku drzewa](Tree_view/pl.md), aby przejść do trybu edycji.
8.  Wybierz wszystkie wycinki panelu, które chcesz w nim umieścić (możesz przełączyć widok drzewa na zakładkę \"projekt\", aby wybrać w drzewie).
9.  Wybierz sekcję \"grupa\" w widoku zadań arkusza paneli.
10. Naciśnij przycisk **Dodaj**.
11. Naciśnij przycisk **OK**.

W widoku zadań arkusza panelu znajduje się również przycisk umożliwiający przesuwanie poszczególnych wycinków panelu po ich wstawieniu do arkusza. Po chwili nasze arkusze są gotowe:

![](images/Arch_Wikihouse_03.jpg )

Ostatnim krokiem jest po prostu zaznaczenie wszystkich arkuszy, a następnie wyeksportowanie ich do formatu DXF z menu **Plik → Eksportuj**. Zawartość arkuszy zostanie wyeksportowana oddzielnie w różnych warstwach, z tym samym kodowaniem kolorów powszechnie używanym w projekcie Wikihouse:

![](images/Arch_Wikihouse_04.jpg )

Pliki te są gotowe do wysłania do warsztatów, które wykonają rzeczywiste cięcie. Możliwe byłoby również wygenerowanie kodu G do wysłania do maszyny CNC bezpośrednio z FreeCAD, ale to już temat na inny poradnik.



---
⏵ [documentation index](../README.md) > Wikihouse porting tutorial/pl
