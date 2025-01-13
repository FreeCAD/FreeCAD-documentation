# Manual:Modeling for product design/pl
{{Manual:TOC}}

Środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) we FreeCAD to wszechstronne narzędzie do tworzenia parametrycznych modeli 3D, szczególnie przydatne przy projektowaniu brył. Pozwala rozpocząć od szkiców 2D, które można przekształcić w obiekty 3D za pomocą operacji takich jak <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [wyciągnięcie](PartDesign_Pad/pl.md), <img alt="" src=images/PartDesign_Revolution.svg  style="width:16px;"> [obrót](PartDesign_Revolution/pl.md) oraz <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [kieszeń](PartDesign_Pocket/pl.md). Środowisko to jest niezbędne przy projektowaniu części wymagających precyzji i kontroli parametrycznej, ponieważ zmiany w szkicach lub cechach automatycznie aktualizują cały model.

Jedną z kluczowych zalet środowiska pracy Projekt Części jest jego przydatność do tworzenia części przeznaczonych do druku 3D. Ponieważ drukarki 3D wymagają bryłowych, szczelnych modeli, środowisko pracy Projekt Części zapewnia, że wszystkie cechy pozostają w obrębie jednego spójnego obiektu. Eliminuje to typowe problemy, takie jak przerwy czy nakładające się powierzchnie, które mogą powodować problemy podczas przygotowywania modelu w programie do cięcia warstw. Po ukończeniu projektu można łatwo wyeksportować model jako plik STL - format szeroko obsługiwany przez drukarki 3D. Dzięki temu środowisko pracy Projekt Części jest idealnym wyborem do tworzenia wysokiej jakości obiektów gotowych do druku, niezależnie od tego, czy prototypujesz, projektujesz funkcjonalne części, czy tworzysz skomplikowane modele przeznaczone do druku 3D.

Aby zilustrować działanie środowiska Projekt Części, zamodelujmy ten dobrze znany element [Lego](https://en.wikipedia.org/wiki/Lego). Możesz też sprawdzić [Poradnik: Podstawy dla środowiska pracy Projekt Części 019](Basic_Part_Design_Tutorial_019/pl.md) jeśli chcesz spróbować z innym obiektem.

![](images/FreeCAD_Exercise1_RedBrick.png )

Będziemy teraz korzystać wyłącznie z narzędzi [środowiska pracy Szkicownik](Sketcher_Workbench/pl.md) i [środowiska pracy Projekt Części](PartDesign_Workbench/pl.md). Ponieważ wszystkie narzędzia ze środowiska pracy Szkicownik są również zawarte w środowisku pracy Projekt Części, możemy pozostać w Projekt Części i nie będzie konieczności przełączania się między tymi dwoma środowiskami.

W środowisku pracy Projekt Części we FreeCAD obiekty są głównie budowane na podstawie szkiców, czyli profili 2D składających się z segmentów liniowych, takich jak linie, łuki czy elipsy, wraz z zestawem więzów. Więzy te określają konkretne reguły geometryczne dla szkicu i mogą być stosowane zarówno do samych segmentów, jak i ich kluczowych punktów, takich jak punkty końcowe czy środki. Na przykład można użyć wiązania pionowego, aby linia pozostała idealnie pionowa, lub wiązania pozycji (blokady), aby unieruchomić punkt końcowy, uniemożliwiając jego przesuwanie.

Szkic jest uznawany za w pełni związany, gdy każdy punkt jest zablokowany w odpowiedniej pozycji za pomocą odpowiedniej liczby więzów, co oznacza, że żadna część szkicu nie może być swobodnie przesuwana. Osiągnięcie w pełni związanego szkicu jest idealne, ponieważ zapewnia dobrze zdefiniowany i stabilny projekt, umożliwiając przewidywalne zmiany na dalszych etapach projektowania. Z drugiej strony, jeśli zostanie dodanych więcej więzów niż to konieczne --- określane jako nadmiarowe więzy - może to powodować konflikty geometryczne. FreeCAD ostrzega przed nadmiarowymi lub sprzecznymi więzami, ponieważ nadmiarowe związanie może prowadzić do problemów w dalszych operacjach, takich jak wyciągnięcia czy wycięcia.

Dodanie odpowiednich więzów jest kluczowe dla stworzenia stabilnego, parametrycznego modelu. Dzięki starannemu zrównoważeniu więzów można łatwo modyfikować lub dostosowywać szkice bez naruszania geometrii. Taka kontrola sprawia, że środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) jest potężnym narzędziem do precyzyjnego modelowania parametrycznego, szczególnie w zadaniach takich jak druk 3D, gdzie utrzymanie właściwych relacji geometrycznych ma kluczowe znaczenie dla uzyskania dokładnych i funkcjonalnych części.

Szkice posiadają tryb edycji, w którym można zmieniać ich geometrię i wiązania. Gdy zakończysz edycję i opuścisz tryb edycji, szkice zachowują się jak każdy inny obiekt w programie FreeCAD i mogą być używane jako elementy konstrukcyjne we wszystkich narzędziach środowiska pracy Projekt Części, ale także w innych środowiskach pracy, takich jak [Part](Part_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md). Środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) posiada również narzędzie, które konwertuje obiekty Szkicownika na obiekty Rysunku Roboczego, oraz w przeciwnym kierunku.

-   Przełącz się na <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [środowisko pracy Projekt Części](PartDesign_Workbench/pl.md).
-   Kliknij przycisk <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Nowy szkic](PartDesign_NewSketch/pl.md) i wybierz płaszczyznę **XY**, czyli płaszczyznę \"podłoża\". Szkic zostanie utworzony, a następnie automatycznie przełączony w tryb edycji, a widok zostanie obrócony, aby patrzeć na szkic ortogonalnie.
-   Narysuj prostokąt, wybierając narzędzie <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Prostokąt](Sketcher_CreateRectangle/pl.md) i klikając dwa punkty narożne. Możesz umieścić te dwa punkty dowolnie, ponieważ ich właściwa lokalizacja zostanie ustalona w następnym kroku.
-   Zauważysz, że do naszego prostokąta automatycznie dodano kilka więzów: pionowe segmenty otrzymały więzy pionowe, poziome segmenty - wiązania poziome, a każdy narożnik --- więzy punkt-na-punkcie, które łączą segmenty. Możesz eksperymentować z przesuwaniem prostokąta, przeciągając jego linie myszą --- cała geometria będzie przestrzegać nałożonych więzów.
-   W tym momencie nasz szkic jest niedostatecznie związany, ponieważ brakuje mu czterech więzów: jego długości, szerokości oraz położenia względem osi X i Y. Ten brak więzów pozwala swobodnie przesuwać szkic wzdłuż osi X i Y. Dopóki te więzy nie zostaną zdefiniowane, geometria nie jest w pełni zablokowana, co oznacza, że rozmiar i pozycja szkicu pozostają modyfikowalne. Aby w pełni zdefiniować szkic, musimy zastosować więzy, które określą te wartości i unieruchomią szkic w odpowiednim położeniu.

![](images/FreeCAD_Exercise1_re_UC.png )

-   Teraz dodajmy trzy kolejne wiązania:
    -   Wybierz jeden z pionowych segmentów i zastosuj wiązanie <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [Wymiar](Sketcher_Dimension/pl.md), aby ustawić jego długość na 23,7 mm.
    -   Podobnie wybierz poziomy segment i ustaw jego długość na 47,7 mm za pomocą tego samego narzędzia wymiarowego.
    -   Na koniec wybierz górny lewy punkt narożny prostokąta, następnie punkt początkowy (kropkę, w której przecinają się czerwone i zielone osie) oraz dolny prawy punkt narożny. Użyj wiązania <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [symetrii](Sketcher_ConstrainSymmetric/pl.md), aby uczynić prostokąt symetrycznym względem osi X i Y. Zapewni to, że prostokąt pozostanie wyśrodkowany względem punktu początkowego, ograniczając jego ruch i zapewniając symetrię względem obu osi.
-   Zauważysz teraz, że nasz prostokąt zmienił kolor na zielony, co oznacza, że jest w pełni związany. Oznacza to, że każdy aspekt szkicu, w tym jego pozycja, rozmiar i kształt, jest teraz w pełni zdefiniowany i zablokowany na miejscu. Warto stosować dobrą praktykę, jaką jest pełne wiązanie szkiców, ponieważ pomaga to utrzymać kontrolę nad projektem i zapobiega niezamierzonym zmianom podczas kolejnych operacji.

![](images/FreeCAD_Exercise1_re.png )

-   Nasz podstawowy szkic jest teraz gotowy, możemy opuścić tryb edycji, naciskając przycisk **Zamknij** na górze panelu zadań, lub po prostu naciskając klawisz **Escape**. Jeśli będzie to konieczne później, możemy powrócić do trybu edycji w każdej chwili, klikając dwukrotnie na szkicu w widoku drzewa lub klikając prawym przyciskiem myszy i wybierając opcję edycji szkicu.
-   Wyciągniemy go, korzystając z narzędzia <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Wyciągnij](PartDesign_Pad/pl.md), i nadając mu odległość {{Value|14.4mm}}. Pozostałe opcje można zostawić domyślne:

![](images/FreeCAD_Exercise1_padding.png )

-   Narzędzie **Wyciągnięcie** jest podobne do <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Wyciągnięcia](Part_Extrude/pl.md) ze środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md), ale z kluczową różnicą: wyciągnięcie zawsze jest powiązane ze swoim szkicem i nie może być przemieszczane niezależnie. Aby zmienić położenie wyciągnięcia, należy przesunąć bazowy szkic, co zapewnia, że wyciągnięcie pozostanie do niego trwale przyłączone. Wyciągnięcie zawsze pozostaje częścią tego samego obiektu Zawartości, co utrzymuje spójność projektu. Jest to szczególnie przydatne przy tworzeniu złożonych części, w których cechy muszą być budowane stopniowo i w odpowiednim wyrównaniu względem siebie. Taka organizacja dodaje stabilności projektowi, zwłaszcza gdy konieczne jest zachowanie właściwego położenia i wzajemnego dopasowania wszystkich elementów.

-   Stwórzmy teraz osiem walców na górnej powierzchni bloku. Najpierw wybierz górną powierzchnię bloku, a następnie kliknij opcję <img alt="" src=images/Std_AlignToSelection.svg  style="width:16px;"> [Wyrównaj do zaznaczenia](Std_AlignToSelection/pl.md), aby wyrównać widok do tej powierzchni. Umożliwi to przejrzysty i bezpośredni widok, co ułatwi dokładne umieszczenie walców.
-   Kliknij przycisk <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Nowy szkic](PartDesign_NewSketch/pl.md). Nowy szkic zostanie utworzony bezpośrednio na górnej powierzchni.
-   Utwórz dwa <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [okręgi](Sketcher_CreateCircle/pl.md) w dowolnym miejscu.
-   Wybierz środki obu okręgów oraz oś X (czerwona linia), a następnie kliknij opcję <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md).
-   Wybierz oba okręgi i zastosuj wiązanie <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [równości](Sketcher_ConstrainEqual/pl.md).
-   Korzystając z narzędzia <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [Wymiar](Sketcher_Dimension/pl.md), ustaw średnicę jednego z okręgów na 7,2 mm. Ponieważ zastosowaliśmy wcześniej wiązanie równości, średnica drugiego okręgu dostosuje się automatycznie.
-   Teraz musimy ustalić położenie okręgów względem krawędzi powierzchni. Możesz jednak zauważyć, że nie da się bezpośrednio wybrać żadnych punktów ani krawędzi. Aby rozwiązać ten problem, użyj narzędzia <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [Geometria zewnętrzna](Sketcher_External/pl.md), aby odwołać się do krawędzi powierzchni, co pozwoli dokładnie ograniczyć położenie okręgów względem tej powierzchni. Kliknij przycisk i wybierz lewą krawędź powierzchni. Krawędź zostanie podświetlona na czerwono, a Ty będziesz mógł utworzyć punkty odniesienia, które umożliwią zastosowanie więzów do precyzyjnego pozycjonowania okręgów względem granic powierzchni.
-   Teraz możesz ustawić odległości środka jednego z okręgów w osiach X i Y na 6 mm. Ponieważ okręgi są powiązane ze sobą, drugi okrąg dostosuje się odpowiednio.

![](images/FreeCAD_Exercise1_TopFaceSketch.png )

-   Zauważ, że ponownie, gdy zablokujesz położenie i wymiary wszystkich elementów szkicu, stanie się on w pełni związany. Dzięki temu zawsze pozostajesz po bezpiecznej stronie. Możesz teraz zmodyfikować pierwszy szkic, a wszystko, co zrobiliśmy później, pozostanie spójne.
-   Opuść tryb edycji, wybierz nowy szkic i utwórz <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Wyciągnięcie](PartDesign_Pad/pl.md) o wysokości 2,7 mm.

![](images/FreeCAD_Exercise1_topCylPad.png )

-   Ponieważ użyliśmy górnej powierzchni naszego podstawowego bloku jako podstawy do tego nowego szkicu, każda operacja Part Design zastosowana do niego będzie poprawnie zbudowana na bazowej formie. Dwa okręgi nie są niezależnymi obiektami; będą wyciągnięte bezpośrednio z istniejącego bloku. To kluczowa zaleta pracy w środowisku pracy [Projekt Części](PartDesign_Workbench/pl.md) --- dopóki upewniasz się, że każdy krok jest budowany na podstawie poprzedniego, efektywnie tworzysz jeden, spójny obiekt bryłowy.
-   Teraz możemy skopiować nasze dwa punkty cztery razy. Wybierz ostatnie wyciągnięcie, które właśnie utworzyliśmy.
-   Kliknij przycisk <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [Szyk liniowy](PartDesign_LinearPattern/pl.md).
-   Ustaw długość na 36 mm (co odpowiada całkowitej \"rozciągłości\", w jakiej chcemy umieścić nasze kopie), w kierunku \"poziomej osi szkicu\", i ustaw liczbę wystąpień na 4.

![](images/FreeCAD_Exercise1_topPattern.png )

-   Teraz wycinamy wnętrze bloku, używając narzędzia <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Kieszeń](PartDesign_Pocket/pl.md), które jest wersją [Wycięcia](Part_Cut/pl.md) w środowisku pracy [Projekt Części](PartDesign_Workbench/pl.md). Aby wykonać kieszeń, utworzymy szkic na dolnej powierzchni naszego bloku, który będzie użyty do usunięcia części bloku.
-   Zaznacz dolną powierzchnię, a następnie kliknij przycisk <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Nowy szkic](PartDesign_NewSketch/pl.md).
-   Narysuj <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [prostokąt](Sketcher_CreateRectangle/pl.md) na powierzchni.
-   Zastosuj <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md), wybierając górny lewy punkt narożny prostokąta, następnie punkt początkowy (kropkę, w której przecinają się czerwone i zielone osie), oraz dolny prawy punkt narożny.
-   Używając narzędzia <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [Geometria zewnętrzna](Sketcher_External/pl.md), wybierz lewą krawędź dolnej powierzchni. Ponownie zauważ, że zostanie podświetlona na czerwono.
-   Ustaw poziomą i pionową odległość prostokąta względem górnego prawego punktu na 1,8 mm, używając <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [Wymiaru](Sketcher_Dimension/pl.md).

![](images/FreeCAD_Exercise1_BottomRec.png )

-   Utwórz trzy <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [okręgi](Sketcher_CreateCircle/pl.md), upewniając się, że ich środek znajduje się na osi X (czerwona linia).
-   Wybierz wszystkie trzy okręgi i zastosuj <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [wiązanie równości](Sketcher_ConstrainEqual/pl.md).
-   Ustaw średnicę jednego okręgu na 9,765 mm.
-   Ustaw odległość środka lewego okręgu względem dolnej krawędzi prostokąta, który utworzyliśmy wcześniej, na 10,2 mm.
-   Ustaw odległość między lewym a środkowym okręgiem na 12 mm. Powtórz ten krok, aby ustawić tę samą odległość 12 mm między środkowym a prawym okręgiem.

![](images/FreeCAD_Exercise1_BottomOuterCirc.png )

-   Prawie skończyliśmy.
-   Utwórz trzy dodatkowe <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [okręgi](Sketcher_CreateCircle/pl.md), upewniając się, że każdy nowy okrąg jest współśrodkowy z jednym z wcześniej narysowanych okręgów. Alternatywnie, możesz umieścić nowe okręgi w dowolnym miejscu szkicu i użyć narzędzia <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [wiązania zbieżności punktów](Sketcher_ConstrainCoincident/pl.md), aby wyrównać ich środki z środkami istniejących okręgów.
-   Wybierz wszystkie trzy okręgi i zastosuj <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [wiązanie równości](Sketcher_ConstrainEqual/pl.md).
-   Ustaw średnicę jednego okręgu na 7,2 mm.
-   Teraz możesz opuścić szkic.

![](images/FreeCAD_Exercise1_bottomSketchCom.png )

-   Wybierając ukończony szkic, użyj narzędzia <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Kieszeń](PartDesign_Pocket/pl.md), ustawiając długość na 12 mm.

![](images/FreeCAD_Exercise1_BottomPad.png )

-   To już wszystko. Nasza kostka jest gotowa. Jeśli chcesz zmienić jej kolor, możesz to zrobić, przechodząc do zakładki **Widok**.

![](images/FreeCAD_Exercise1_redBrick2.png )

Możesz zauważyć, że historia modelowania w widoku drzewa stała się dość rozbudowana. Jest to niezwykle cenne, ponieważ umożliwia nam powrót do każdego etapu procesu projektowania i jego modyfikację w dowolnym momencie. Na przykład dostosowanie tego modelu, aby stworzyć cegłę 2x2 zamiast 2x4, będzie dziecinnie proste - wystarczy kilka zmian w wymiarach i liczbie wystąpień wzoru. Ta sama elastyczność pozwala na projektowanie większych, niestandardowych elementów, które nie są częścią oryginalnego zestawu Lego. Parametryczna natura programu FreeCAD ułatwia modyfikowanie istniejących modeli, dając pełną kontrolę nad dostosowywaniem lub rozszerzaniem projektu w razie potrzeby.

Ale możemy też chcieć pozbyć się historii, na przykład jeśli zamierzamy modelować zamek z tej cegły i nie chcemy, aby cała historia była powtarzana 500 razy w naszym pliku.

Istnieją dwa proste sposoby na pozbycie się historii, jednym z nich jest użycie narzędzia [Utwórz prostą kopię](Part_SimpleCopy/pl.md) ze środowiska [Część](Part_Workbench/pl.md), które utworzy kopię naszego elementu, która nie będzie już zależna od historii *(możesz później usunąć całą historię)*, drugim sposobem jest wyeksportowanie elementu jako pliku STEP i ponowne zaimportowanie go.

**Do pobrania**

-   The model produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Więcej informacji:**

-   Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md)
-   Środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md)
-   Środowisko pracy [Złożenie 2](https://github.com/hamish2014/FreeCAD_assembly2)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/pl
