# Feature editing/pl
{{TOCright}}

## Wprowadzenie

Ta strona wyjaśnia sposób, w jaki środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Projekt Części](PartDesign_Workbench/pl.md) jest przeznaczone do użycia począwszy od FreeCAD w wersji 0.17.

Podczas gdy środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> _ używa **[cech](PartDesign_Feature/pl.md)**. [Cecha](https://en.wikipedia.org/wiki/Feature_recognition) jest operacją, która modyfikuje kształt modelu.

## Techniki edycji cech 

Pierwsza cecha jest powszechnie nazywana \"cechą bazową\". W miarę jak kolejne cechy są dodawane do modelu, każda z nich przyjmuje kształt poprzedniej i dodaje lub usuwa materię, tworząc liniowe zależności od jednej cechy do następnej. W efekcie, ta metodyka naśladuje zwykły proces produkcyjny: blok jest cięty z jednej strony, potem z drugiej, dodawane są otwory, potem zaokrąglenia, itd.

Wszystkie cechy są wymienione kolejno w drzewie modelu i mogą być edytowane w dowolnym momencie, przy czym ostatnia cecha na dole reprezentuje wynik końcowy.

Cechy mogą być posortowane w różnych kategoriach:

-   **Oparte na profilu**: te cechy rozpoczynają się od profilu, aby zdefiniować kształt materiału, który ma zostać dodany lub usunięty. Profil może być szkicem, planarną powierzchnią na istniejącej geometrii *(profil zostanie wyodrębniony z jej krawędzi)*, obiektem Łącznik Kształtu lub obiektem Rysunek Roboczy, który został włączony do aktywnej bryły.

-   **Dodanie**: powoduje dodanie materiału do istniejącego modelu. Cechy addytywne posiadają żółte ikony.

-   **Odjęcie**: powoduje usunięcie materiału z istniejącego modelu. Cechy subtraktywne mają czerwone i niebieskie ikony.

-   **Oparte na elementach pierwotnych**: oparte na geometrycznych prymitywach *(sześcian, walec, stożek, torus\...)*. Mogą być zarówno addytywne, jak i subtraktywne.

-   **Cechy transformacji**: stosują one przekształcenia do istniejących cech *(odbicie lustrzane, wzór liniowy, wzór biegunowy, transformacja wielokrotna)*.

-   **Ulepszenie**: cechy, które stosują obróbkę do krawędzi lub powierzchni, takie jak zaokrąglenia, fazowania i przeciągnięcia.

-   **Proceduralne**: można tak powiedzieć o funkcjach, które nie są oparte na szkicach, takich jak funkcje transformacji i ulepszenia.

## Zawartość

Praca w środowisku Projekt Części wymaga najpierw stworzenia obiektu <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[Zawartości](PartDesign_Body/pl.md)**. Zawartość Projekt Części jest kontenerem, który grupuje sekwencję obiektów cech tworzących pojedynczą, ciągłą bryłę.

![](images/PartDesign_Body_tree.png )

**Co to jest pojedyncza ciągła bryła?** Jest to obiekt taki jak odlew lub coś obrobionego z jednego kawałka metalu. Jeśli obiekt wymaga użycia gwoździ, śrub, kleju lub spawania, nie jest wtedy pojedynczą ciągłą bryłą. Jako praktyczny przykład, drewniane krzesło byłoby wykonane z wielu Zawartości, po jednej dla każdej z jego części składowych *(nogi, listwy, siedzisko, itp.)*.

W dokumencie programu FreeCAD można utworzyć wiele Zawartości. Można je również połączyć w jedną ciągłą bryłę.

Tylko jedna Zawartość może być aktywna w dokumencie. Aktywna Zawartość otrzymuje nowo utworzone elementy. Korpus może być aktywowany lub dezaktywowany poprzez dwukrotne kliknięcie na nim. Aktywna Zawartość jest podświetlona na jasnoniebiesko. Kolor podświetlenia można ustawić w preferencjach w sekcji **Edycja → Preferencje → Wyświetlanie → Kolory → Widok drzewa → Aktywna Zawartość**, od wersji 0.18.

Gdy model wymaga wielu zawartości, jak w poprzednim przykładzie z drewnianym krzesłem, można użyć <img alt="" src=images/Std_Part.svg  style="width:24px;"> [kontenera](Std_Part/pl.md) ogólnego przeznaczenia, może być on użyty do zgrupowania ich i poruszania całością jako jedną całością.

### Zarządzanie widocznością Zawartości 

Zawartość domyślnie prezentuje na zewnątrz swoją najnowszą cechę. Cecha ta jest domyślnie zdefiniowana jako wierzchołek. Dobrą analogią jest wyrażenie *czubek góry lodowej*: tylko czubek jest widoczny nad wodą, większość masy góry lodowej (inne cechy) jest ukryta. Gdy nowa cecha jest dodawana do struktury, widoczność poprzedniej cechy jest wyłączana, a nowa cecha staje się wierzchołkiem.

W danym momencie może być widoczna tylko jedna cecha. Możliwe jest [przełączenie widoczności](Std_ToggleVisibility/pl.md) dowolnej cechy w zawartości, przez wybranie jej w drzewie modelu i naciśnięcie klawisza **Space**, w efekcie cofając się w historii zawartości.

### Odniesienie położenia Zawartości 

Zawartość posiada obiekt Odniesienie położenia, który składa się z płaszczyzn odniesienia *(XY, XZ, YZ)* i osi *(X, Y, Z)*, które mogą być używane przez szkice i cechy. Szkice mogą być dołączane do płaszczyzn Odniesienia położenia i nie muszą już być mapowane na płaszczyzny, aby cechy na nich oparte mogły być dodawane lub odejmowane z modelu.

### Przesuwanie i zmiana kolejności obiektów 

Można tymczasowo zmienić definicję czubka elementu w środku drzewa zawartości w celu wstawienia nowych obiektów *(elementów, szkiców lub geometrii punktów odniesienia)*. Możliwa jest również zmiana kolejności elementów zawartości lub przeniesienie ich do innej zawartości. Zaznacz obiekt i kliknij prawym przyciskiem myszy, aby uzyskać menu kontekstowe, które oferuje obie opcje. Operacja może zostać uniemożliwiona, jeśli obiekt posiada zależności w bryle źródłowej, np. jest dołączony do powierzchni. Aby przenieść szkic do innej bryły, nie powinien on zawierać powiązań z zewnętrzną geometrią.

### Różnice względem innych systemów CAD 

Fundamentalną różnicą pomiędzy programem FreeCAD a innymi programami, takimi jak Catia, jest to, że FreeCAD nie pozwala na posiadanie wielu rozłączonych brył w tej samej <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[zawartości](PartDesign_Body/pl.md)**. Oznacza to, że nowa cecha powinna być zawsze zbudowana na poprzedniej. Lub mówiąc inaczej, nowy element powinien \"dotykać\" poprzedniego, tak aby oba elementy były połączone razem i stały się jedną bryłą. Nie można mieć \"unoszących się\" brył.

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">



*Różnica pomiędzy programami Catia i FreeCAD. <br>Po lewej: Catia pozwala na rozłączenie zawartości od poprzedzających ją cech zawartości. W programie FreeCAD powoduje to błąd. <br>Po prawej: nowsza cecha powinna zawsze stykać się lub przecinać poprzednią cechę tak, aby została z nią stopiona i stała się jedną przylegającą bryłą.*

## Odniesienie geometrii 

Geometria odniesienia składa się z niestandardowych płaszczyzn, linii, punktów lub zewnętrznie powiązanych kształtów. Mogą one być tworzone jako odniesienie dla szkiców i elementów. Istnieje wiele możliwości dołączania do obiektów punktów odniesienia.

W niektórych systemach CAD można zdefiniować płaszczyznę odniesienia, która jest odsunięta od poprzedniej zawartości i można utworzyć bryłę rozłączną. Tak więc umieszczenie wielu płaszczyzn odniesienia i budowanie na nich obiektów jest w porządku i nie spowoduje błędu. Zazwyczaj ostatecznie dopasowujesz płaszczyzny do ich ostatecznych pozycji, tak aby poszczególne obiekty były połączone ze sobą.

W programie FreeCAD, jak wspomniano w poprzednim rozdziale, rozłączone bryły są **NIE** dozwolone, więc tworzenie szkicu na płaszczyźnie odniesienia, który utworzyłby niejednolitą bryłę, nie powiedzie się.

W programie FreeCAD płaszczyzny odniesienia mają sens w przypadku umieszczania szkiców *(oraz wypełnień, kieszeni itp.)* w niestandardowych orientacjach, to znaczy w płaszczyznach przesuniętych lub obróconych wokół trzech głównych osi. Ponieważ szkice można również umieszczać w niestandardowych orientacjach w taki sam sposób jak płaszczyzny odniesienia, często nie ma potrzeby używania płaszczyzn odniesienia.

Płaszczyzny odniesienia mają również zastosowanie, jeżeli będzie więcej niż jeden szkic w tej samej niestandardowej orientacji. W takim przypadku można użyć płaszczyzny odniesienia, a orientacja musi zostać dostosowana tylko dla płaszczyzny odniesienia, aby dostosować wszystkie powiązane szkice i elementy utworzone ze szkiców.

Zarówno szkice jak i płaszczyzny odniesienia powinny być dołączone do płaszczyzn bazowych. Należy unikać odwoływania się do geometrii wygenerowanej (geometrii, która jest wynikiem operacji tworzenia elementu, na przykład wyciągnięcia lub kieszeni), ponieważ powierzchnie i krawędzie otrzymują nowe nazwy i numeracje, a odwołania nie odnoszą się już do tej samej rzeczy. Jest to nazywane topologiczną niestabilnością i jest spowodowane sposobem w jaki FreeCAD używa niektórych zewnętrznych bibliotek geometrycznych. Miejmy nadzieję, że zostanie to poprawione w przyszłości. *(Zobacz porady dotyczące tworzenia stabilnych modeli poniżej)*.

Nawet jeśli nie są używane do dołączania szkiców, obiekty punktów odniesienia są nadal pomocne jako wskaźniki wizualne, aby zwrócić uwagę na ważne cechy lub odległości w procesie modelowania. *(Chociaż zwykłe dodanie geometrii do szkicu również zapewnia podobną wizualną informację zwrotną)*.

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">



*Różnica pomiędzy Catia a FreeCAD. Po lewej: Catia pozwala na rozłączenie zawartości od poprzednich cech. W programie FreeCAD powoduje to błąd.<br> Po prawej: nowsza bryła powinna zawsze stykać się lub przecinać z poprzednią, tak aby została z nią połączona i stała się jedną przylegającą bryłą. W tym przykładzie nowa bryła jest oparta na płaszczyźnie odniesienia, która jest obrócona wokół osi Y.*

## Wzajemne odniesienia 

Możliwe jest powiązanie elementów z jednej zawartości w innej zawartości poprzez układy odniesienia. Na przykład łącznik kształtu układu odniesienia pozwala na kopiowanie powierzchni z jednej zawartości jako odniesienia do drugiej. Powinno to ułatwić zbudowanie obudowy z dopasowaną pokrywą w dwóch różnych zawartościach. FreeCAD pomaga uniknąć przypadkowego powiązania z innymi zawartościami, pytając o potwierdzenie chęci wykonania operacji.

## Dołączenie

Narzędzie Dołączenie obiektów nie jest specyficznym narzędziem środowiska Projekt Części, ale raczej narzędziem środowiska Część wprowadzonym w v0.17, które można znaleźć w pasku menu Część. Jest ono bardzo często używane w środowisku Projekt Części, do dołączania szkiców i geometrii odniesienia, do standardowych płaszczyzn i osi Zawartości. Dostępne są bardzo rozbudowane sposoby tworzenia punktów bazowych, linii i płaszczyzn. Opcjonalne parametry przesunięcia mocowania sprawiają, że narzędzie to jest bardzo uniwersalne.

Więcej informacji można znaleźć na stronie _.

## Porady dotyczące tworzenia stabilnych modeli 


<div class="mw-translate-fuzzy">

Idea modelowania parametrycznego zakłada, że można zmieniać wartości pewnych parametrów, a kolejne kroki są zmieniane zgodnie z nowymi wartościami. Jednakże, gdy dokonywane są poważne zmiany, model może zostać uszkodzony z powodu [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md), który jest wciąż nierozwiązany w FreeCAD. Uszkodzenia można zminimalizować, jeśli przestrzega się następujących zasad projektowania:


</div>

-   Unikaj dołączania szkiców i obiektów odniesienia do wygenerowanej geometrii modelu. *(Wygenerowana geometria to każda powierzchnia lub krawędź utworzona w wyniku zastosowania wyciągnięcia, kieszeni itp.)*.
-   Umieszczaj szkice na standardowych płaszczyznach współrzędnych lub na niestandardowych płaszczyznach odniesienia dołączonych do płaszczyzn standardowych.
    -   Szkice dołączone do podstawowych płaszczyzn/osi współrzędnych lub do płaszczyzn odniesienia dołączonych do płaszczyzn/osi współrzędnych nie zostaną nieoczekiwanie ponownie dołączone do innego odniesienia.
-   Podczas tworzenia geometrii odniesienia nie dołączaj jej do wygenerowanej geometrii.
    -   Dołącz ją do standardowych płaszczyzn / osi i / lub szkiców lub obiektów punktów odniesienia, które wykorzystują przesunięcia dołączenia do standardowych płaszczyzn lub osi.
-   Użyj \"szkicu głównego\". Ponieważ szkic główny jest wykonywany przed resztą modelu, posiada on tylko odniesienia do płaszczyzn lub osi współrzędnych.
    -   Szkic główny powinien być jak najprostszy, powinien zawierać podstawowe elementy geometryczne modelu.
    -   Do elementów szkicu głównego można nawiązywać podczas modelowania kolejnych elementów.
    -   Szkic główny może być pierwszym szkicem w Zawartości lub całkowicie poza nią.
    -   Do szkicu głównego można się odwoływać jako do zewnętrznej geometrii lub poprzez Łącznik kształtu.
-   Nie twórz Łącznika kształtu z wygenerowanej geometrii.
-   Należy pamiętać, że Łącznik kształtu może stanowić problem, gdy geometria zostanie usunięta ze szkicu, na którym jest oparta.
-   Jeśli nieuchronnie musisz odwołać się do elementu pośredniego, np. wyniku operacji grubości.
    -   Użyj pierwszego możliwego odniesienia na liście kolejnych cech, w których występuje element geometryczny, do którego się odwołujesz.
    -   Jeśli jako referencję przyjmiesz wcześniejszą cechę, wszystkie zmiany w pośrednich etapach nie spowodują uszkodzenia modelu.
    -   Staraj się odwoływać do szkicu lub geometrii szkicu, a nie do wygenerowanej geometrii.
-   Używaj \"ulepszeń\", takich jak zaokrąglenia i fazki, tak późno w drzewie elementów, jak to możliwe.
-   Uwaga, używanie arkuszy kalkulacyjnych, danych dynamicznych, szkiców głównych itp. generalnie tworzy bardziej parametryczne modele i pomaga uniknąć problemu nazewnictwa topologicznego.

## Przebieg pracy przy budowie zawartości 


<div class="mw-translate-fuzzy">

Istnieje kilka przepływów pracy, które są dostępne w środowisku [Projekt Części](PartDesign_Workbench/pl.md). To co powinno być zawsze zauważone to fakt, że wszystkie cechy utworzone wewnątrz [zawartości](PartDesign_Body/pl.md) zostaną połączone razem aby otrzymać końcowy obiekt.


</div>

### Różne szkice 

Szkice muszą być osadzone na płaszczyźnie. Płaszczyzna ta może być jedną z głównych płaszczyzn *(XY, XZ lub YZ)* zdefiniowanych przez Odniesienie położenia Zawartości. Szkic jest albo wyciągany w wystającą bryłę *(addytywnie)*, za pomocą narzędzia takiego jak <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _. Pierwszy z nich dodaje objętość do ostatecznego kształtu zawartości, a drugi odcina ją od ostatecznego kształtu. W ten sposób można utworzyć dowolną liczbę szkiców i częściowych brył, a ostateczny kształt *(czubek)* jest wynikiem połączenia tych operacji w całość. Oczywiście bryła nie może składać się wyłącznie z operacji odejmowania, gdyż ostateczny kształt powinien być bryłą o dodatniej, niezerowej objętości.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Cechy sekwencyjne 


<div class="mw-translate-fuzzy">

Szkice mogą być oparte na powierzchniach poprzednich operacji na bryłach. Może to być konieczne, jeśli trzeba uzyskać dostęp do powierzchni, która jest dostępna tylko po utworzeniu pewnego elementu. Jednakże, ten sposób pracy nie jest zalecany, ponieważ, jeśli oryginalny element zostanie zmodyfikowany, kolejne elementy w sekwencji mogą zostać uszkodzone. Jest to [problem nazewnictwa topologicznego](Topological_naming_problem/pl.md).


</div>

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Wykorzystanie płaszczyzn odniesienia do podparcia 

Płaszczyzny bazowe są przydatne do oparcia szkiców. Te pomocnicze płaszczyzny powinny być dołączone do płaszczyzn bazowych bryły.

*Uwaga: W wielu przypadkach szkic dołączony do płaszczyzny bazowej z przesunięciami dołączenia może spełnić tę samą funkcję. Układy odniesienia są szczególnie przydatne, gdy wiele szkiców lub innych konstrukcji będzie korzystało z tego układu odniesienia. Oznacza to, że wszystkie zmiany w układzie odniesienia zostaną zastosowane do dołączonych szkiców itp. Dodanie pojedynczego szkicu do układu odniesienia, zamiast używania przesunięć dołączenia we właściwościach szkicu, stanowi dodatkowy krok i jest w zasadzie zbędne.*

Podobnie jak w przypadku szkiców, możliwe jest dołączanie płaszczyzn odniesienia do generowanej geometrii *(krawędzi, powierzchni wcześniej utworzonych brył)*, **\'\' ale nie jest to zalecane**\'\', gdyż może powodować problem z nazewnictwem topologicznym.


<div class="mw-translate-fuzzy">

Dodatkowo, <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [łącznik kształtów](PartDesign_ShapeBinder/pl.md) może być użyty do zaimportowania zewnętrznej geometrii do bryły, aby służyła jako odniesienie; następnie szkice mogą być dołączone do tej pomocniczej zawartości, używając płaszczyzn odniesienia lub nie.


</div>

*Ponownie, Łącznik kształtów powinien bazować na Szkicach z poprzedniej bryły, a nie na wygenerowanej geometrii.*

Używanie obiektów odniesienia jest często najlepszym sposobem na tworzenie stabilnych modeli, gdy są one używane z płaszczyznami bazowymi i przesunięciami dołączania, chociaż wymaga to nieco więcej pracy od użytkownika. Szczegóły na temat podstawowego dołączania można znaleźć na stronie: [Poradnik: Podstawy dołączania](Basic_Attachment_Tutorial/pl.md) *Uwaga: podczas gdy ten poradnik mówi o szkicach, dołączanie elementów odniesienia jest wykonywane w podobny sposób.*.

## Poradniki


<div class="mw-translate-fuzzy">

Strona _.

-   [Projekt części: tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md)
-   [Poradnik: Podstawy dla Środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md)
-   [Poradnik: Podstawy dołączania](Basic_Attachment_Tutorial/pl.md)


</div>

## Related


<div class="mw-translate-fuzzy">

## Powiązane

-   [Konstrukcyjna geometria bryły](Constructive_solid_geometry/pl.md)


</div>

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}} 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Feature editing/pl
