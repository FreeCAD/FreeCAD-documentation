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

1.  Create a copy of your wire-like object with **Ctrl**+**C**, **Ctrl**+**V**. This is so we can modify it but still keep one in its correct location
2.  Move and rotate it so it lies in the XY plane, using [Draft Move](Draft_Move.md) and [Draft Rotate](Draft_Rotate.md). This is not indispensable, but the next point sometimes fails otherwise
3.  Use [Draft Draft2Sketch](Draft_Draft2Sketch.md) to turn the wire into a sketch. Be warned, this can fail or take a very long time for huge wires. It is best to decompose your object into individual wires as shown above.
4.  If the command above fails, using [Draft Upgrade](Draft_Upgrade.md) twice on a wire-like object, to convert it to a Face then to a [Draft Wire](Draft_Wire.md), before using [Draft Draft2Sketch](Draft_Draft2Sketch.md), usually works better, because the Draft Wire keeps a better track of the order of vertices inside a wire.
5.  Curves are made of several small segments. They can be left as is, but they introduce a lot of endpoint constraints. It is better to replace them by arcs. It is fairly easy to do, just delete the small segments and replace them by an arc. The arc can then be made tangential to the neighbouring segments, but make sure the position of those segments is locked before doing this, as this operation will make them move.
6.  If you worked with several sketches, make a [Part Compound](Part_Compound.md) of them
7.  Create an [Arch Panel](Arch_Panel.md) from it
8.  Rotate/move it back into position with [Draft Move](Draft_Move.md) and [Draft Rotate](Draft_Rotate.md)

![](images/Arch_Wikihouse_12.jpg )



## Przebudowa Wikihouse i eksportowanie wyciętych arkuszy 

Also, make sure you don\'t redo any duplicated part. Instead, select the [Draft Clone](Draft_Clone.md) tool to duplicate parts based on the same profile, so they will all share one same profile object. Then, since we have the outline at the correct place to use as a guide, it is fairly easy to rotate and move the clone into its correct position with [Draft Rotate](Draft_Rotate.md) and [Draft Move](Draft_Move.md).

Po chwili cała sekcja Microhouse jest gotowa.

![](images/Arch_Wikihouse_01.jpg )

We can now easily create the cut sheets, which are DXF files that will be sent to the shop that will cut the actual panels. The easiest way to do this is to select everything in your document with **Ctrl**+**A**, and then use the [Arch Panel Cut](Arch_Panel_Cut.md) tool. This will produce one Panel Cut object for each Panel object found in the selection. By moving them apart, we get a clear view of all our pieces:

![](images/Arch_Wikihouse_02.jpg )

We must then \"nest\" our pieces, that is, move and rotate them so they occupy as much as possible to space of a given panel, to generate as little material loss as possible. This operation unfortunately needs to be done by hand, but if you are using a Wikihouse project that already has produced cut sheets, copying them goes pretty fast:

1.  To make sure everything will stay in the XY plane, it is advised to set the [Working Plane](Draft_SelectPlane.md) to XY (top)
2.  Create an [Arch Panel Sheet](Arch_Panel_Sheet.md)
3.  Give it the desired width and height values (Wikihouses are typically printed on 122x244cm plywood sheets)
4.  Move it to a convenient place with [Draft Move](Draft_Move.md)
5.  Optionally, set its margin values to help you position the cut pieces
6.  Move and rotate the individual [Arch Panel Cut](Arch_Panel_Cut.md) objects so they fit inside the Panel Sheet
7.  When you are more or less ready, select the Panel Sheet, and double click it in the [tree view](Tree_view.md) to enter Edit mode
8.  Select all the Panel Cuts you wish to insert in it (you may want to switch the tree view to the \"project\" tab to select in the tree)
9.  Select the \"group\" section in the Panel Sheet\'s Task view
10. Press the **Add** button
11. Press the **OK** button

In the Panel Sheet\'s Task view, there is also a button that allows you to move the individual Panel Cuts after they\'ve been inserted inside the sheet. After a while, we have our sheets ready:

![](images/Arch_Wikihouse_03.jpg )

The last step is simply to select all the sheets, then export them to DXF from menu File → Export. The sheets contents will be exported separated in different layers, with the same color coding commonly used by the Wikihouse project:

![](images/Arch_Wikihouse_04.jpg )

These files are ready to send to the shops that will do the actual cut. It would be possible to generate the G-Code to be sent to the CNC machine directly from FreeCAD too, but that is matter for another tutorial.



---
⏵ [documentation index](../README.md) > Wikihouse porting tutorial/pl
