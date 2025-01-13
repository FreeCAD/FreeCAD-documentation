# Feature editing/pl
## Wprowadzenie

Ta strona wyjaśnia podejście do edycji cech w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Projekt Części](PartDesign_Workbench/pl.md).



## Zawartość

Praca w środowisku Projekt Części wymaga najpierw stworzenia obiektu <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> **[Zawartości](PartDesign_Body/pl.md)**. Zawartość jest kontenerem przeznaczonym do przechowywania pojedynczej ciągłej bryły. Gdy Zawartość jest tworzona, automatycznie dodawany jest obiekt Origin, lokalny układ współrzędnych skłądający się ze standardowych płaszczyzn odniesienia (XY, XZ, YZ) i osi (X, Y, Z). Bryła jest następnie budowana poprzez dodawanie cech. Każda [cecha](PartDesign_Feature/pl.md) jest kulumatywna i dodaje lub odejmuje się od wyniku poprzedniej cechy.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:400px;">



*Edycja cech w praktyce. Od lewej do prawej:<br>
Zawartość z cechą [prostopadłościan](PartDesign_AdditiveBox/pl.md).<br>
Zawartość z cechami prostopadłościan i [sfazowanie](PartDesign_Chamfer/pl.md).<br>
Zawartość z cechami prostopadłościan, sfazowanie i [kieszeń](PartDesign_Pocket/pl.md).*

Dokument może zawierać wiele Zawartości, ale tylko jedna może być aktywna. Nowe cechy są dodawane do aktywnej Zawartości. Zawartość można aktywować i dezaktywować klikając na niej dwukrotnie w [widoku drzewa](Tree_view/pl.md). Aktywowana Zawartość jest podświetlona w widoku drzewa.

![](images/PartDesign_Body_tree.png )



### Czym jest ciągła bryła? 

Ciągła bryła to obiekt taki jak odlew lub coś obrobionego z jednego kawałka metalu. Jeśli obiekt wymaga użycia gwoździ, śrub lub kleju, nie jest wtedy ciągłą bryłą. Jako praktyczny przykład, drewniane krzesło byłoby wykonane z wielu Zawartości, po jednej dla każdej z jego części składowych *(nogi, listwy, siedzisko, itp.)*.

We FreeCAD 1.0 została wprowadzona eksperymentalna właściwość pozwalająca Zawartości na przechowywanie nieciągłych brył. Można to również ustawić w [Preferencjach](PartDesign_Preferences/pl#Ogólne.md) jako domyślne dla nowo utworzonych Zawartości. Nie jest to przeznaczone do użycia do budowania, jak w przykładzie, krzesła w jednej Zawartości. Ma to pozwolić na cechy, które mogą tworzyć rodzielone bryły, które zostaną uciąglone przez kolejne cechy.

Gdy model wymaga wielu Zawartości, jak w poprzednim przykładzie z drewnianym krzesłem, można użyć <img alt="" src=images/Std_Part.svg  style="width:16px;"> [kontenera](Std_Part/pl.md) ogólnego przeznaczenia, może być on użyty do zgrupowania ich i poruszania całością jako jedną całością.



### Zarządzanie widocznością Zawartości 

Domyślnie Zawartość prezentuje na zewnątrz swoją najnowszą cechę. Ta cecha to Wierzchołek Zawartości. Wierzchołek oznacza też położenie, w którym dodawane są nowe cechy. Możliwe jest tymczasowe przedefiniowanie Wierzchołka do cechy w środku Zawartości aby wstawić tam nowe obiekty (cechy, szkice lub geometrię konstrukcyjną). Gdy nowa cecha jest dodawana do struktury, widoczność poprzedniej cechy jest wyłączana, a nowa cecha staje się Wierzchołkiem.

W danym momencie może być widoczna tylko jedna cecha. Możliwe jest [przełączenie widoczności](Std_ToggleVisibility/pl.md) dowolnej cechy w Zawartości, przez wybranie jej w widoku drzewa i naciśnięcie klawisza **Space**, w efekcie cofając się w historii zawartości. Zauważ, że zmiana widoczności cechy nie zmienia Wierzchołka Zawartości.



### Przesuwanie i zmiana kolejności obiektów 

Cechy Zawartości mogą być przestawione lub przesunięte do innej Zawartości. Zaznacz cechę i kliknij prawym przyciskiem myszy, aby uzyskać menu kontekstowe, które oferuje obie opcje. Operacja może zostać uniemożliwiona, jeśli obiekt posiada zależności w bryle źródłowej, np. jest dołączony do powierzchni. Aby przenieść szkic do innej bryły, nie powinien on zawierać powiązań z zewnętrzną geometrią.

<img alt="" src=images/PartDesign_workflow.svg  style="width:400px;">



*Schematyczna reprezentacja przepływu pracy w środowisku Projekt Części.*



## Odniesienie geometrii 

Geometria odniesienia składa się z niestandardowych płaszczyzn, linii, punktów lub zewnętrznie powiązanych kształtów. Mogą one być tworzone jako odniesienie dla szkiców i elementów. Istnieje wiele możliwości [dołączania](Part_EditAttachment/pl.md) do obiektów odniesienia.

W programie FreeCAD płaszczyzny odniesienia mają sens w przypadku umieszczania szkiców w niestandardowych orientacjach, to znaczy w płaszczyznach przesuniętych lub obróconych wokół trzech głównych osi. Ale ponieważ szkice można również umieszczać w niestandardowych orientacjach i mają takie same opcje dołączania jak płaszczyzny odniesienia, często nie ma potrzeby używania płaszczyzn odniesienia. Płaszczyzny odniesienia mają najwięcej sensu gdy jest więcej niż jeden szkic z taką samą niestandardową orientacją. Dostosowanie orientacji płaszczyzny odniesienia dostosuje wtedy wszystkie powiązane z nią szkice i cechy z nich utworzone.

Chciaż wersja 1.0 programu FreeCAD ma już kod łagodzący [problem gubienia odniesień](Topological_naming_problem/pl.md), nadal najlepszą praktyką jest dołączanie zarówno szkiców jak i płaszczyzn konstrukcyjnych do płaszczyzn bazowych globalnego układu współrzędnych Zawartości gdy tylko jest to możliwe. Tworzenie odniesień do istniejącej geometrii (geometrii, która jest wynikiem operacji cechy, np. wyciągnięcia lub wycięcia) może skutkować mniejszą stabilnością modeli. Zobacz stronę [Porady dotyczące tworzenia stabilnych modeli](#Porady_dotyczące_tworzenia_stabilnych_modeli.md) poniżej.



## Porady dotyczące tworzenia stabilnych modeli 

Idea modelowania parametrycznego zakłada, że można zmieniać wartości pewnych parametrów, a kolejne kroki są zmieniane zgodnie z nowymi wartościami. Jednakże, gdy dokonywane są poważne zmiany, model może zostać uszkodzony z powodu [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md). Uszkodzenia można zminimalizować jeśli przestrzega się następujących zasad projektowania:

-   Unikaj dołączania szkiców i własnych geometri konstrukcyjnych do istniejącej geometrii, czyli jakiejkolwiek ściany, krawędzi lub wierzchołka bryły modelu. Zamiast tego dołączaj je do standardowych płaszczyzn/osi. Szkice dołączone do standardowych płaszczyzn/osi lub do geometrii konstrukcyjnej dołączonej do standardowych płaszczyzn/osi nie będą się niespodziewanie przestawiać na inne odniesienia. Używaj odsunięć dołączenia jeśli są potrzebne.
-   Używaj \"szkicu głównego\". Ponieważ szkic główny jest tworzony przed resztą modelu, może mieć odniesienia tylko do standardowych płaszczyzn/osi.
    -   Szkic główny powinien być tak prosty jak to możliwe, zawierając podstawowe elementy geometryczne twojego modelu.
    -   Możesz tworzyć odniesienia do elementów szkicu głównego modelując kolejne cechy.
    -   Szkic główny może być pierwszym szkicem w Zawartości lub może być całkowicie poza zawartością. W pierwszym przypadku, można się do niego odnosić bezpośrednio przy pomocy geometrii zewnętrznej a w drugim można skorzystać z <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [Łącznika kształtów](PartDesign_ShapeBinder/pl.md) lub <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [Łącznika kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md).
-   Nie twórz łączników kształtów (podrzędnych) z istniejącej geometrii. Pamiętaj, że mogą one stanowić problem jeśli geometria zostanie usunięta ze szkicu, na którym jest oparta.
-   Zawsze najpierw próbuj odnosić się do szkicu lub geometrii szkicu zamiast do istniejącej (wygenerowanej) geometrii. Jeśli koniecznie musisz odnieść się do istniejącej geometrii, użyj pierwszej cechy, w której występuje element, do którego chcesz się odnieść. Wtedy zmiany w dalszych krokach nie zepsują modelu.
-   Używaj cech wykańczających, takich jak zaokrąglenia i sfazowania tak późno w drzewie cech jak to możliwe.



## Poradniki

Strona [Poradniki](Tutorials/pl.md) zawiera kilka przykładów użycia metody edycji cech w środowisku [PartDesign_Workbench/pl](PartDesign_Workbench/pl.md).

-   [Projekt części: tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md)
-   [Poradnik: Podstawy dla Środowiska pracy Projekt Części 019](Basic_Part_Design_Tutorial_019/pl.md)
-   [Poradnik: Podstawy dołączania](Basic_Attachment_Tutorial/pl.md)



## Powiązane

-   [Konstrukcyjna geometria bryły](Constructive_solid_geometry/pl.md)


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/pl
