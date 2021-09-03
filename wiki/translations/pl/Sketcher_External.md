---
- GuiCommand:/pl
   Name:Sketcher External
   Name/pl:Szkicownik: Geometria zewnętrzna
   MenuLocation:Szkic → Elementy geometryczne szkicownika → Geometria zewnętrzna
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**X**
   SeeAlso:[Tryb konstrukcji](Sketcher_ToggleConstruction/pl.md)
---

## Opis

Użyj narzędzia**<img src="images/Sketcher_External.svg" width=16px> [Geometria zewnętrzna](Sketcher_External/pl.md)** kiedy musisz zastosować wiązanie pomiędzy geometrią szkicu a czymś na zewnątrz szkicu. To działa przez wstawienie do szkicu połączonej geometrii konstrukcyjnej. Domyślny kolor połączonych zewnętrznych krawędzi to magenta. Tak samo jak w przypadku standardowych, niepołączonej geometrii konstrukcyjnej *(niebieska)*, zewnętrznie połączona geometria jest widoczna tylko gdy szkic jest w trybie edycji i nie jest bezpośrednio wykorzystywana w późniejszym użyciu gotowego szkicu w innym narzędziu. Oba typy geometrii konstrukcyjnej mogą być używane jako odniesienie dla wiązań w szkicu.

Ostrzeżenie: użycie tego narzędzia do łączenia z wygenerowaną geometrią *(bryłą)* może prowadzić do nieoczekiwanych wyników z powodu [Problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md). Zobacz również [Porady dotyczące tworzenia stabilnych modeli](Feature_editing/pl#Porady_dotycz.C4.85ce_tworzenia_stabilnych_modeli.md).

<FILE:Sketcher_ExternalEsempio1.png>

## Użycie

-   Utwórz nowy szkic lub otwórz istniejący szkic.
-   Kliknij przycisk \"Geometria zewnętrzna\"
-   Wybierz krawędź lub wierzchołek, do którego chcesz łączyć w szkicu.
-   Naciśnij klawisz Esc lub wybierz inne narzędzie, aby zatrzymać importowanie geometrii do szkicu.

### Zasady wyboru {#zasady_wyboru}

-   Tylko krawędzie i wierzchołki z obiektów z tego samego układu współrzędnych są dozwolone.

Oznacza to, że szkic i obiekt muszą znajdować się w tej samej Zawartości *(podczas pracy w środowisku Projekt Części)*, lub w tej samej Części *(podczas pracy w środowisku Część)*, lub obie poza jakimikolwiek Częściami i Zawartościami.

Na przykład, jeśli otwarty szkic znajduje się w Zawartości, możesz użyć innego szkicu z Zawartości jako geometrii zewnętrznej, ale nie możesz użyć szkicu z Zawartości001 lub krawędzi z Prostopadłościanu z środowiska Część znajdującego się w najwyższym poziomie projektu. Użyj funkcji Łącznik kształtu, aby wprowadzić kopię obiektu do układu współrzędnych otwartego szkicu. Wtedy będziesz mógł użyć krawędzi / wierzchołków obiektu Łącznik kształtu.

-   Zależności kołowe nie są dozwolone.

Oznacza to, że nie można łączyć się z Kieszenią wykonaną za pomocą tego szkicu. Nie możesz przyłączyć do żadnego obiektu, który zależy od szkicu.

Szkic nie musi znajdować się na żadnej ścianie, aby móc korzystać z tego narzędzia. Łącza bezpośrednio między szkicami są możliwe i zalecane, ponieważ są one bardziej niezawodne.

### Wygląd po pomyślnym Łączeniu {#wygląd_po_pomyślnym_łączeniu}

Gdy krawędź zostanie pomyślnie połączona, zostanie na nią nałożona linia *(domyślnie w kolorze magenty, wierzchołki będą czerwone)*, która będzie widoczna w szkicu tylko wtedy, gdy szkic jest w trybie edycji.

### Podobieństwo do Linii Konstrukcyjnych {#podobieństwo_do_linii_konstrukcyjnych}

Linie geometrii zewnętrznej *(domyślnie w kolorze magenta)* są podobne *(domyślny kolor niebieski)* do [linii konstrukcyjnych](Sketcher_ToggleConstruction/pl.md) z tą różnicą, że linie geometrii zewnętrznej w kolorze magenta są parametrycznie połączone z elementem bryły, na której szkic jest mapowany. Geometria konstrukcyjna stanowi linie, które są liniami wewnętrznymi w szkicu i są widoczne tylko wtedy, gdy szkic znajduje się w trybie edycji, i będą używane tylko jako referencje wiązań, a nie bezpośrednio do późniejszych operacji na bryłach, takich jak Wyciągnięcie czy Kieszeń.

### Użycie Geometrii Zewnętrznej podczas pracy w Środowisku Projekt Części {#użycie_geometrii_zewnętrznej_podczas_pracy_w_środowisku_projekt_części}

Podczas pracy w środowisku Projekt Części, narzędzie Geometria Zewnętrzna jest używane do pomocy w pozycjonowaniu konstruowanej bryły w stosunku do poprzedniego etapu jej budowy. Środowisko Projekt Części jest przeznaczone do tworzenia pojedynczej bryły, dlatego te szkice w połączeniu z geometrią zewnętrzną są używane do tworzenia nowych cech tej samej bryły.

Geometria zewnętrzna może być na przykład użyta jako odniesienie dla wiązania używanego w celu umieszczenia otworu na obiekcie w określonym miejscu względem krawędzi lub wierzchołka tego obiektu.

### Użycie Geometrii Zewnętrznej podczas pracy w Środowisku Część {#użycie_geometrii_zewnętrznej_podczas_pracy_w_środowisku_część}

Można użyć dowolnej geometrii środowiska Część, która znajduje się w układzie współrzędnych szkicu. Zaleca się łączenie z najwcześniejszą możliwą cechą, ponieważ tworzy to bardziej stabilne połączenie.

## Przykład

Poniżej znajduje się szkic zmapowawany na górną ścianę bryły utworzonej z Wyciągnięcia poprzedniego szkicu. Linie w kolorze magenta to Geometria Zewnętrzna połączona z dwiema krawędziami tego wcześniej istniejącego Wyciągniecia.

W tym przypadku są one używane jako referencje dla wiązań stycznych z obwodami jednego okręgu. Są one również używane jako referencje dla wiązania poziomego i pionowego w celu umiejscowienia środka drugiego okręgu względem końca i góry Wyciągnięcia.

<FILE:Sketcher_ExternalEsempio2.png>

To jest ten sam szkic w trybie edycji, z ukrytym wyciągnięciem, na którym jest on zmapowany.

<FILE:Sketcher_ExternalEsempio4.png>

Gdy edycja szkicu jest zamknięta, zewnętrzne linie Geometrii nie są widoczne.

<FILE:Sketcher_ExternalEsempio3.png>





{{Sketcher Tools navi

}}  
