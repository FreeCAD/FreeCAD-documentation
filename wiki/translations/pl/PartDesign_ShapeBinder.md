---
- GuiCommand:/pl
   Name:PartDesign ShapeBinder
   Name/pl:Projekt części: Łącznik kształtu
   MenuLocation:Part Design → Utwórz nowy łącznik kształtu
   Workbenches:[Projekt części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Projekt części: Podrzędny łącznik kształtu](PartDesign_SubShapeBinder.md), [Projekt części: Klon](PartDesign_Clone.md)
---

## Opis

Tworzy odniesienie **łącznik kształtu** wewnątrz aktywnej Zawartości. Łącznik kształtu to obiekt odniesienia, który łączy się z krawędziami lub ścianami z innego obiektu. Można go również użyć do połączenia szkicu z jednej bryły do drugiej. Obiekt łącznik kształtu jest wyświetlany w oknie [widoku 3D](3D_view/pl.md) jako półprzezroczysty żółty.

Przykładem zastosowania może być zbudowanie skrzynki z dopasowaną pokrywą w dwóch różnych korpusach lub wykonanie otworów, które są dopasowane pomiędzy różnymi korpusami.

<img alt="" src=images/Shapebinder_tree.png ) ![](images/Shapebinder_flow.png  style="width:600px;"> 
*Zostały wybrane dwa kształty z obiektu Body.Pad004, a ich obiekty punktów odniesienia są teraz dostępne w Body001.Sketch005 jako geometria zewnętrzna dzięki Body001.ShapeBinder.*

## Użycie

Ogólne zastosowanie:

1.  [Aktywuj obiekt](PartDesign_Body#Active_status.md), który ma przyjąć obiekt łącznika kształtu.
2.  Naciśnij przycisk **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [Utwórz nowy łącznik kształtu](PartDesign_ShapeBinder.md)**.
3.  Naciśnij przycisk **Obiekt** lub **Dodaj geometrię**.
4.  W oknie [widoku 3D](3D_view/pl.md) wybierz obiekt lub geometrię do skopiowania. **Obiekt** wybierze całą bryłę, **Dodaj geometrię** wybierze dowolny element *(wierzchołek, krawędź, ściana)*.
5.  Aby usunąć wybraną geometrię, naciśnij przycisk **Usuń geometrię** po czym wybierz element w oknie [widoku 3D](3D_view/pl.md). Aby anulować operację, należy ponownie nacisnąć przycisk .
6.  Alternatywnie, bryłę do skopiowania można wybrać przed uruchomieniem polecenia Łącznik kształtów.
7.  Naciśnij przycisk **OK**.

**Przykład**

:   W przykładzie wykorzystano funkcję Łącznik kształtów do wykonania otworu *(z gwintem lub bez)* przez więcej niż jedną bryłę. Normalnie funkcja Otwór w środowisku Projektowanie części jest ograniczona do jednej bryły. W przykładzie użyto dwóch sześcianów zwróconych do siebie, ale przesuniętych względem siebie w dowolny sposób. Otwory są tworzone za pomocą szkiców zawierających okrąg dla każdego otworu *(średnica jest ignorowana przez funkcję Otwór)*. Po skopiowaniu szkicu do drugiego sześcianu będzie on znajdował się w tej samej pozycji w lokalnym układzie współrzędnych sześcianu. Na rysunku widać to jako białe kółko na sześcianie znajdującym się z tyłu. Nie jest to zgodne z naszymi oczekiwaniami, ponieważ otwór w tym miejscu nie byłby wyrównany do otworu w pierwszym sześcianie.





:   

    :   ![](images/ShapeBinderThroughHole.png )
    :   *Przykładowa konfiguracja do pokazania jak wykonać otwory w różnych bryłach. Biały okrąg pokazuje, że kopiowanie szkiców nie jest wystarczające*

Oto jak użyć funkcji Łącznik kształtów, aby osiągnąć ten efekt:

1.  Przygotuj scenę jak na powyższym obrazku. Jeśli używasz sześcianów ze środowiska [Part](Part_Workbench/pl.md), pamiętaj, że musisz je umieścić w kontenerze *zawartość*. Każdy z nich w oddzielnym kontenerze *zawartość*. W przeciwnym razie funkcje środowiska pracy [Projekt części](PartDesign_Workbench/pl.md) nie działałyby. Jeśli budujesz je ze szkiców, system powinien domyślnie tworzyć kontenery typu *zawartość*.
2.  Wybierz zakładkę PropertiesDialog/Data, aby przesunąć drugi sześcian tak, by zetknął się z pierwszym z przemieszczeniem w bok.
3.  Wybierz środowisko pracy Projekt części.
4.  Utwórz szkic na powierzchni czołowej pierwszego sześcianu i umieść w dowolnym miejscu okrąg, a następnie zamknij szkic.
5.  Zaznacz szkic w drzewie i naciśnij przycisk funkcyjny [Utwórz otwór \...](PartDesign_Hole/pl.md). Najpierw upewnij się, że pierwsza bryła jest bryłą aktywną *(podwójne kliknięcie)*.
6.  Wybierz otwór w odpowiednim rozmiarze. Na powyższym rysunku wybrano również pogłębienie walcowe. Zamykamy funkcję [Utwórz otwór \...](PartDesign_Hole/pl.md).

    :   Teraz obrazek powinien wyglądać jak powyżej. Po ukryciu pierwszego sześcianu *(zaznaczamy i wciskamy spację)* widać, że otwór nie sięga do drugiego sześcianu. Nie dosięgnie, nawet jeśli wybierzesz opcję *Przez wszystkie* lub jeśli podasz naprawdę dużą odległość w oknie dialogowym [Utwórz otwór \...](PartDesign_Hole/pl.md). Funkcja otworu jest zawsze ograniczona do jednej bryły.
    :   Tutaj z pomocą przychodzi nasz łącznik kształtu.
7.  Najpierw wybierz tylną kostkę. To jest cel, do którego zostanie dodany łącznik kształtu. Musi on być aktywny, więc upewnij się, że został dwukrotnie kliknięty.
8.  W drzewie wybierz szkic, którego użyliśmy do wykonania otworu. Ważne jest, aby nie aktywować pierwszej bryły.
9.  Wybierz funkcję łączenia kształtów.

    :   Powinno się otworzyć okno dialogowe. W wierszu **Obiekt** powinna być widoczna nazwa naszego szkicu. Jeśli wybrałeś funkcję bez wybierania szkicu, możesz nacisnąć **Obiekt** i wybrać szkic z listy. Zalecane jest wybranie go najpierw, aby uzyskać właściwą nazwę, szczególnie jeśli mamy wiele szkiców z automatycznie generowanymi nazwami Sketch001, \... Funkcja **Dodaj geometrię** nie jest dla nas przydatna, ponieważ chcemy wybrać cały szkic. Opcja **Dodaj geometrię** jest używana, jeśli chcemy wybrać tylko części.
10. Naciśnij przycisk **OK**, aby zamknąć funkcję szkicu i sprawdzić, czy nowy element został dodany do drzewa drugiego sześcianu.

    :   Kiedy przełączasz widoczność segregatora kształtów, jest on wyświetlany na żółto w oknie [widoku 3D](3D_view/pl.md). Jest on jednak w złej pozycji, tak jak białe kółko na powyższym obrazku. Jest to spowodowane domyślnym ustawieniem parametru Śledzenia.
11. W widoku właściwości łącznika kształtu w zakładce **Dane** ustaw wartość parametru **Wsparcie śledzenia** na {{true}}. Domyślnie ustawiona była wartość {{false}}.

    :   Jeśli parametr **Wsparcie śledzenia** ma wartość {{true}}, na łącznik kształtu nie mają wpływu lokalne transformacje bryły docelowej, np. nasze translacje. Kształt pozostaje dokładnie tam, gdzie znajdował się oryginalny kształt obiektu przedniego. Spróbuj przesunąć przedni obiekt dookoła, a zobaczysz, że łącznik kształtu zawsze podąża do nowej pozycji.
    :   Niestety nie możemy wybrać funkcji łączenia kształtów dla funkcji [Utwórz otwór \...](PartDesign_Hole/pl.md). Dlatego tworzymy szkic lokalny i używamy go do naszego otworu w drugim sześcianie.
12. Zaznacz przednią ścianę tylnego sześcianu i utwórz nowy szkic *(kliknij w przycisk **OK** dla sugestii w oknie dialogowym)*.
13. Spraw, aby cała geometria była niewidoczna, a łącznik kształtów widoczny. Teraz możesz użyć funkcji geometrii zewnętrznej i wybrać okrąg w łączniku kształtów. Potrzebujemy punktu środkowego tego okręgu.
14. Utwórz nowy okrąg i umieść go w punkcie środkowym okręgu łącznika kształtu. Promień nie jest ważny. Funkcja [Utwórz otwór \...](PartDesign_Hole/pl.md) używa tylko punktów środkowych okręgów *(uwaga: pojedyncze punkty są ignorowane przez funkcję Otwór, musimy używać okręgów)*.
15. Zamknij szkic i kliknij [Utwórz otwór \...](PartDesign_Hole/pl.md). Ustaw w oknie dialogowym takie same wartości jak dla otworu pierwotnego i naciśnij **OK**.

**Zrobione.**

:   Teraz masz dwa połączone otwory w dwóch różnych bryłach. Jeśli zmienisz geometrię lub położenie tych otworów, oba zostaną dostosowane. Tylko gdy dodajesz nowy otwór, musisz zaktualizować szkic w drugim sześcianie dla drugiego otworu.





:   Uwagi

Jest jeszcze jeden sposób na utworzenie łącznika kształtów. Gdy tylny sześcian jest aktywny, kliknij w przednią ściankę pierwszego sześcianu i utwórz nowy szkic. Pojawi się okno dialogowe, w którym należy wybrać *Szkic zależny*. Spowoduje to utworzenie łącznika kształtów. Możesz zobaczyć parametr **Obsługa śledzenia** w oknie właściwości. Jest to kilka kliknięć mniej niż prezentuje nasza procedura. Pamiętaj też, że praca z funkcją łącznik kształtów na szkicach to tylko niewielka część jej możliwości. Możliwe jest również użycie wybranej części geometrii 3D, jak widać na powyższym przykładzie.

## Opcje

Kliknij dwukrotnie etykietę Łącznik kształtu w okienku [widoku drzewa](Tree_view/pl.md) lub kliknij prawym przyciskiem myszki i wybierz **Edytuj łącznik kształtu** z menu kontekstowego, aby edytować jego parametry.

## Właściwości

-    **Etykieta**: nazwa nadana obiektowi, nazwa ta może być zmieniona dla wygody.

-    **Wsparcie śledzenia**: Przy ustawieniu tej opcji na wartość {{true}}, Łącznik kształtów stosuje się do względnego rozmieszczenia części i brył. Wartość domyślna to {{false}}. Zobacz powyższy przykład, jak to działa i jak to jest używane {{Version/pl|0.18}}.

## Ograniczenia

-   Nie jest obsługiwany wybór wielokrotny. Przyciski **Dodaj geometrię** i **Usuń geometrię** muszą zostać naciśnięte dla każdego z poszczególnych wyborów.

Istnieje obejście dla wielokrotnego wyboru: Jeśli zaznaczysz wszystkie elementy, które chcesz mieć *przed* utworzeniem łącznika kształtów, pojawią się one na liście początkowej.

-   Segregator kształtów nie może służyć jako element bazowy.
-   Wybrana geometria na bryle musi być przyległa.
-   Jeśli przed uruchomieniem polecenia zostanie najpierw wybrana bryła, która ma zostać skopiowana, lub jeśli zostanie użyty przycisk **Obiekt**, nie jest już możliwe wybranie tylko określonych elementów geometrii.
-   Względne położenie bryły docelowej i kopiowanej nie jest brane pod uwagę. Łącznik kształtów przyjmie te same współrzędne wewnętrzne, jakie posiada skopiowana bryła. Od wersji **0.18** dostępna jest nowa właściwość *Trace Support*, która pozwala przełączyć to zachowanie tak, aby uwzględniało względne umiejscowienie.





{{PartDesign Tools navi

}} 
