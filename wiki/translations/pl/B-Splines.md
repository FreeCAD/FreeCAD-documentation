 {{TOCright}}

Ta strona opisuje jak używać krzywych złożonych w programie FreeCAD. Podaje również podstawowe informacje czym są krzywe złożone i do jakich zastosowań są przydatne.

## Motywacja

Jeśli posiadasz już wiedzę na temat krzywych złożonych typu B-splines i ich zastosowania, możesz przejść bezpośrednio do rozdziału [Krzywe złożone w programie FreeCAD](B-Splines/pl#Krzywe_z.C5.82o.C5.BCone_w_programie_FreeCAD.md).

Załóżmy, że chcesz zaprojektować część, która powinna być wytworzona za pomocą drukarki 3D. Część musi mieć krawędź zaprojektowaną w ten sposób:

<img alt="" src=images/B-splines_Motivation-start.png  style="width:450px;">

Musisz wydrukować część w kierunku od dołu szkicu do góry. Zewnętrzne konstrukcje wsporcze mogą nie być rozwiązaniem. Dlatego musisz dodać podporę bezpośrednio do swojej części. Jakie masz opcje?

-   Opcja 1: możesz dodać linię od punktu *(20, 0)* do punktu *(80, 40)*:

<img alt="" src=images/B-splines_Motivation-line.png  style="width:450px;">

Jednak takie rozwiązanie wymaga dużej objętości, a co za tym idzie wagi i ilości materiału.

-   Opcja 2: możesz połączyć te dwa punkty łukiem okręgu. Aby zaoszczędzić na objętości, łuk powinien kończyć się stycznie w punkcie *(80,40)*. Wtedy twoje rozwiązanie będzie wyglądać następująco:

<img alt="" src=images/B-splines_Motivation-circle.png  style="width:450px;">

W PORZĄDKU. Ale na dole nie potrzebujesz bezpośredniego wsparcia.

-   Opcja 3: możesz zaoszczędzić trochę więcej objętości, jeśli połączenie między dwoma punktami jest krzywą, która zaczyna się stycznie w punkcie o współrzędnych *(0, 20)* i kończy stycznie w *(80, 40)*:

<img alt="" src=images/B-splines_Motivation-bezier.png  style="width:450px;">

Tak więc krzywa, za pomocą której można połączyć dwa punkty stycznie do punktu odniesienia, może być bardzo przydatna w konstrukcjach. Krzywe Béziera zapewniają tę cechę.

## Krzywe Béziera 

### Pochodne

Krzywe Béziera są wielomianami opisującymi połączenie między dwoma punktami. Najprostszym wielomianem łączącym dwa punkty jest prosta *($A*x^1+B$)*, zatem również liniowe krzywe Béziera są liniowe:

![](images/Bezier_linear_anim.gif ) *Animacja 1: Liniowa krzywa Béziera.*

Jednak wielomian staje się użyteczny, gdy możemy go kontrolować. Powinien więc istnieć punkt pomiędzy dwoma punktami końcowymi, który pozwala nam określić jak punkty końcowe są połączone. Tak jak w powyższym przykładzie w opcji trzeciej krzywa jest przydatna, gdy zaczyna się i kończy stycznie do linii przecinających punkty końcowe. I to jest główna cecha krzywych Béziera. Dodajmy więc punkt kontrolny pomiędzy punktami końcowymi. Krzywa zacznie się stycznie do tego punktu kontrolnego, co oznacza, że jest styczna do linii, którą możemy narysować pomiędzy punktem początkowym a punktem kontrolnym. Idąc wstecz od punktu końcowego krzywa będzie również styczna do linii, którą możemy narysować pomiędzy punktem kontrolnym a punktem końcowym. Animacja numer 2 pokazuje jak wygląda taka krzywa.

![](images/Bezier_quadratic_anim.gif ) *Animacja 2: Kwadratowa krzywa Béziera. Punktem kontrolnym jest tutaj punkt P1.*

Animacja jasno pokazuje, czym w zasadzie jest krzywa - przejściem od punktu P0 do punktu P2 poprzez obrócenie linii P0-P1 tak, aby stała się linią P1-P2. W ten sposób otrzymujemy ładną cechę stycznego początku / końca.

Taka krzywa może być opisana tylko wielomianem kwadratowym. *(Liczba lewych / prawych obrotów + 1 to konieczny rząd wielomianu. Wielomian kwadratowy to jeden zwrot, wielomian sześcienny ma dwa zwroty, itd.)* Dlatego krzywa Béziera z jednym punktem kontrolnym jest kwadratową *(drugiego rzędu)* krzywą Béziera.

Posiadanie tylko jednego punktu kontrolnego często nie jest wystarczające. Weźmy powyższy motywujący przykład. Tam w opcji 3 kończymy krzywą stycznie w kierunku x. Ale jak można połączyć punkty *(20, 0)* i *(80, 40)* tak, aby krzywa kończyła się stycznie w kierunku y? Aby to osiągnąć potrzebny jest najpierw zwrot w prawo, a potem w lewo, a więc wielomian sześcienny *(trzeciego rzędu)*. A to oznacza, że dla krzywej Béziera potrzebujemy *(lub można powiedzieć, że zyskujemy)* drugi punkt kontrolny. Animacja 3 pokazuje sześcienną krzywą Béziera.

![](images/Bezier_cubic_anim.gif ) *Animacja 3: Sześcienna krzywa Béziera.*

Aby odpowiedzieć na pytanie, rozwiązaniem z zakończeniem stycznym w kierunku y dla przykładu jest:

<img alt="" src=images/B-splines_Motivation-cubic-bezier.png  style="width:450px;">

### Matematyka

Jeśli jesteś zainteresowany, aby zrozumieć matematykę w tle, oto podstawy.

Krzywą Béziera oblicza się według poniższego wzoru:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{polynomial term}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{polynomial term}}\; \underbrace{P_{i}}_{\text{point coordinate}}$

\"n\" jest niniejszym stopniem krzywej. Zatem krzywa Béziera stopnia *n* jest wielokątem rzędu *n*. Współczynniki $P_{i}$ są więc współrzędnymi punktów kontrolnych krzywych Béziera. Wizualizację można znaleźć na stronie [kontrolowanie krzywizn Béziera](https://pomax.github.io/bezierinfo/#control).

Jeśli jesteś dalej zainteresowany, spójrz na stronę [Matematyka krzywych Béziera](https://pomax.github.io/bezierinfo/#explanation) z ładnie animowanym wyprowadzeniem matematyki dla krzywych Béziera.

### Zasady

W powyższym tekście mogłeś już zauważyć pewne \"reguły\" dotyczące krzywych Béziera:

-   Stopień wielomianu jest jednocześnie stopniem krzywych.
-   Jeśli potrzebujesz $n$ skrętów, potrzebujesz co najmniej $n+1$ stopnia krzywej Béziera.
-   Krzywa Béziera zawsze zaczyna się stycznie do linii między punktem początkowym a pierwszym punktem kontrolnym *(i kończy się stycznie do linii między ostatnim punktem kontrolnym a punktem końcowym)*.

## Krzywe złożone 

### Podstawy

[Ten film](https://www.youtube.com/watch?v=bE1MrrqBAl8) wymienia na początku praktyczne problemy z krzywymi Béziera. Na przykład, że dodanie lub zmiana punktu kontrolnego zmienia całą krzywą. Te problemy mogą być rozwiązane przez połączenie kilku krzywych Béziera. Wynikiem jest tak zwany *splajn*, w szczególności B-splajn *(basis spline)*. Film wyjaśnia również, że złożenie kwadratowych krzywych Béziera tworzy jednolity kwadratowy B-splajn, oraz że złożenie sześciennych krzywych Béziera tworzy jednolity sześcienny B-splajn.

Z filmów możemy zebrać przydatne \"zasady\" dla krzywych złożonych *(B-spline)*:

-   Pierwszy i ostatni punkt kontrolny jest punktem końcowym / początkowym krzywej.
-   Podobnie jak dla krzywych Béziera, krzywe złożone zawsze zaczynają się stycznie do linii pomiędzy punktem początkowym a pierwszym punktem kontrolnym *(i kończą się stycznie do linii pomiędzy ostatnim punktem kontrolnym a punktem końcowym)*.
-   Połączenie $S$ krzywych Béziera o stopniu $D$ posiada $S+D$ punktów kontrolnych.
    -   Ponieważ w większości przypadków pracujemy z sześciennymi krzywymi złożonymi, możemy stwierdzić, że $N$ punktów kontrolnych prowadzi do $N-3$ segmentów Béziera, i z kolei $N-4$ punktów węzłowych segmentów.
-   Krzywa złożona o stopniu $D$ oferuje w każdym punkcie ciągłą pochodną rzędu $D-1$.
    -   Dla sześciennej krzywej złożonej oznacza to, że krzywizna *(pochodna drugiego rzędu)* nie zmienia się podczas przechodzenia z jednego odcinka do następnego. Jest to bardzo użyteczna cecha, jak zobaczymy później.

Jeśli interesuje Cię więcej szczegółów na temat właściwości krzywych złożonych, zajrzyj na film [Krzywe MOOC 8.2: Właściwości krzywych B-spline](https://www.youtube.com/watch?v=xXJylM2S72s).

### Zasady 

Nazwa *B-spline* oznacza *Basis spline*. Zamiast tworzyć splajn jako kombinację krzywych Béziera, podejście polega na modelowaniu **tego samego splajnu** w inny sposób. Idea polega na użyciu innego zestawu wielomianów jako podstawy. Liniowa kombinacja tych wielomianów $B_D(t)$ o rzędzie $D$ tworzy B-spline. Film [Krzywe MOOC 8.3: Wyrażenia analityczne dla krzywych B-spline](https://www.youtube.com/watch?v=dPPTCy4L4rY) wyjaśnia przejście od punktów kontrolnych Béziera do wielomianowych funkcji bazowych opisujących splajn. Matematycznie możemy opisać B-spline za pomocą poniższego wzoru:

$\quad
c(t)=\sum_{k=0}^{N}p_{k}B_{k, D}(t)$

W ten sposób $p_k$ jest $k$-tym punktem kontrolnym krzywej złożonej i jednocześnie współczynnikiem dla $k$-tego wielomianu bazowego $B_{k, D}(t)$. Każdy wielomian bazowy opisuje krzywą spline w pewnym regionie i dlatego przesunięcie punktu kontrolnego nie wpływa na całą krzywą spline. Aby to zrozumieć, zalecane jest obejrzenie filmu [Krzywe MOOC 8.4: Wpływ funkcji bazowych na krzywą](https://www.youtube.com/watch?v=vjTyWIKviNc) od minuty 2:23.

Jak wyjaśniono w filmie, wielomiany bazowe są wielomianami Bernsteina. Zbiór wielomianów bazowych dla pewnego B-splajnu można zwizualizować w następujący sposób:

![](images/Bernstein_Polynomials.svg ) *Zestaw wielomianów Bernsteina o rzędzie 4. Opisują one B-splajnę 4 rzędu z 5 punktami kontrolnymi.*

W każdej pozycji splajnu $t$ suma wielomianów wynosi 1 (zaznaczona pomarańczową linią). Na początku tylko czerwony wielomian ma wpływ, ponieważ wszystkie inne wielomiany są tam równe 0. Przy większych $t$ krzywa jest opisywana przez kombinację liniową różnych wielomianów bazowych. Na powyższym obrazku każdy wielomian jest większy od 1 dla całego zakresu $0 < t < 1$. Niekoniecznie musi tak być w rzeczywistości. Jak pokazano na filmie, wielomiany bazowe są w zasadzie większe od 0 tylko dla pewnego zakresu pozycji krzywej. Przedział, w którym wielomian bazowy jest większy od 0, jest opisywany przez *wektor węzłów*. Jeśli jesteś zainteresowany poznaniem wektora węzłów, zajrzyj na film [Krzywe MOOC 8.5: Węzły krzywej B-spline](https://www.youtube.com/watch?v=ni5NNPCVvDY).

### Niejednorodne krzywe B-spline 

Własnością wielomianów Bernsteina jest to, że patrząc na różne części krzywej Béziera, długość ścieżki każdej części jest taka sama. *(Długość ścieżki jest często nazywana **czasem podróży**)*\'. Jak można sobie wyobrazić, użyteczne może być posiadanie krzywych B-spline, których części Béziera mają różne długości ścieżek. Można to osiągnąć poprzez ważenie różnych wielomianów:

$\quad
c(t)=\sum_{k=0}^{N}d_{k}B_{k, D}(t)w_k$

$w_k$ jest niniejszą wagą $k$ - tego punktu kontrolnego. Gdy wagi nie są równe, krzywa B-spline jest nazywana **niejednorodną**.

Szczególnie w przypadku, gdy krzywe B-spline powinny być używane do modelowania 3D, konieczne jest stosowanie znormalizowanych, niejednolitych krzywych B-spline. Normalizacja odbywa się poprzez podział przez ważone funkcje bazowe. W ten sposób, gdy wszystkie $w_k$ są równe, otrzymujemy jednorodną krzywą B-spline, niezależną od samej wagi:

$\quad
c(t)=\cfrac{\sum_{k=0}^{N}d_{k}B_{k, D}(t)w_k}{\sum_{k=0}^{N}B_{k, D}(t)w_k}$

Te niejednorodne i racjonalne *(z powodu podziału)* krzywe B-spline są często nazywane **NURBS**. Patrząc na ich wzór widzimy, że są one w rzeczywistości krzywymi B-spline o ważonej podstawie $R_{k, D}(t)$:

$\quad
c(t)=\sum_{k=0}^{N}d_{k}R_{k, D}(t)$

mając na uwadze, że

$\quad
R_{k, D}=\cfrac{B_{k,D}(u)w_k}{\sum_{l=1}^N B_{l,D}(t)w_l}$

## Krzywe złożone w programie FreeCAD 

FreeCAD oferuje możliwość tworzenia jednolitych lub niejednolitych krzywych złożonych dowolnego stopnia w przestrzeni 2D, za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).

### Tworzenie

Aby utworzyć krzywe złożone, przejdź do szkicu i użyj przycisku na pasku narzędzi **<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Utwórz krzywą złożoną](Sketcher_CreateBSpline/pl.md)**. Następnie kliknij lewym przyciskiem myszy, aby ustawić punkt kontrolny, przesuń kursor w lewo, aby ustawić następny punkt kontrolny i tak dalej. Na koniec kliknij prawym przyciskiem myszy, aby zakończyć definicję i utworzyć krzywą.

Domyślnie tworzone są jednolite krzywe sześcienne, ale nie ma wystarczającej ilości punktów kontrolnych, aby to zrobić. Tak więc, gdy tworzysz krzywą złożona z tylko 2 punktami kontrolnymi, otrzymujesz oczywiście krzywą, która jest pojedynczą liniową krzywą Béziera, dla 3 punktów kontrolnych otrzymujesz kwadratową krzywą Béziera, a dla 5 punktów kontrolnych otrzymujesz sześcienną krzywą złożoną z 2 segmentów Béziera.

Aby utworzyć periodyczne krzywe złożone *(B-splajny, które tworzą zamkniętą krzywą)*, użyj przycisku na pasku narzędzi **<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Okresowa krzywa złożona ...](Sketcher_CreatePeriodicBSpline/pl.md)**. Nie jest konieczne ustawianie ostatniego punktu kontrolnego na pierwszym, ponieważ linia krzywej zostanie automatycznie zamknięta:

![](images/Sketcher_Periodic-B-spline-creation.gif )

Krzywe złożone mogą być również generowane z istniejących segmentów szkicu. Aby to zrobić, zaznacz elementy i naciśnij przycisk paska narzędzi **<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Konwertuj geometrię na krzywą złożoną](Sketcher_BSplineApproximate/pl.md)**.

### Zmiana stopni 

Aby zmienić stopień, wybierz krzywą złożoną i użyj przycisku z paska narzędzi **<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> <img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:Zwiększ stopień krzywej złożonej](Sketcher_BSplineIncreaseDegree/pl.md)** lub **[24px"> [Zmniejsz stopień krzywej złożonej](Sketcher_BSplineDecreaseDegree/pl.md)**.

**Uwaga:** Zmniejszanie stopnia nie może odwrócić wcześniejszego zwiększenia stopnia, zobacz stronę Wiki [Zmniejsz stopień krzywej złożonej](Sketcher_BSplineDecreaseDegree/pl.md), aby uzyskać wyjaśnienie.

### Zmiana wielokrotności węzłów 

Punkty, w których dwie krzywe Béziera łączą się tworząc krzywą złożoną nazywane są węzłami. Mnogość węzłów określa sposób łączenia części Béziera, zobacz stronę Wiki [Zwiększ liczebność węzłów](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md), aby poznać szczegóły.

Aby zmienić krotność węzłów, użyj przycisków paska narzędzi **<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:24px"> <img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:Zwiększ krotności węzłów](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md)** lub **[24px"> [Zmniejsz krotności węzłów](Sketcher_BSplineDecreaseKnotMultiplicity/pl.md)**.

**Uwaga:** Tworzenie dwóch krzywych złożonych, które są ze sobą połączone, nie połączy się w jedną nową krzywą złożoną. Zatem ich punkt połączenia nie jest węzłem. Jedynym sposobem na uzyskanie nowego węzła w istniejącej krzywej jest zmniejszenie jej stopnia. Jednakże, możesz uzyskać wiele nowych węzłów. Dlatego lepszym wyborem jest przerysowanie krzywej z większą liczbą punktów kontrolnych.

### Zmiana wagi 

Wokół każdego punktu kontrolnego znajduje się ciemnożółte koło. Jego promień określa wagę dla danego punktu kontrolnego. Domyślnie wszystkie okręgi mają promień równy *1*. Jest to oznaczone za pomocą wiązania promienia dla pierwszego okręgu punktu kontrolnego.

Aby utworzyć niejednolitą krzywą złożoną, wagi muszą być różne. Aby to osiągnąć, możesz albo zmienić [wiązanie promienia](Sketcher_ConstrainRadius/pl.md) pierwszego punktu okręgu kontrolnego:

![](images/Sketcher_Changing-control-point-weigth-constraint.gif )

lub usunąć wiązanie, równości wszystkich okręgów, a następnie ustawić odrębne wiązania promienia dla okręgów.

Jeśli nie ustawiono żadnego wiązania promienia, można również zmienić promień, przeciągając go:

![](images/Sketcher_Changing-control-point-weigth-dragging.gif )

W przykładzie przeciągania widać, że duża waga przyciąga krzywą do punktu kontrolnego, podczas gdy bardzo mała waga zmienia krzywą tak, jakby punkt kontrolny prawie nie istniał.

Kiedy spojrzysz na [funkcję tworzenia](B-Splines/pl#Niejednorodne_krzywe_B-spline.md) dla niejednorodnych racjonalnych krzywych złożonych zobaczysz, że waga równa zero doprowadziłaby do dzielenia przez zero. Dlatego możesz określić tylko wagi większe od zera.

### Wyświetlanie informacji 

Ponieważ postać krzywej B-splajnu nie mówi wiele o jej właściwościach, FreeCAD oferuje [różne narzędzia](Sketcher_Workbench/pl#Narz.C4.99dzia_szkicownika_dla_krzywych_z.C5.82o.C5.BConych.md) do wyświetlania tych właściwości:

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Właściwość               | Przycisk narzędzia                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Stopień**              |                                                                                                                                       |
|                          | **<img src=images/Sketcher_BSplineDegree.svg style="width:16px"> [Pokaż / ukryj stopnie krzywej złożonej](Sketcher_BSplineDegree/pl.md)**                             |
|                          |                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Ramka kontrolna**      |                                                                                                                                       |
|                          | **<img src=images/Sketcher_BSplinePolygon.svg style="width:16px"> [Pokaż / ukryj ramkę kontrolną krzywej złożonej](Sketcher_BSplinePolygon/pl.md)**                   |
|                          |                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Grzebień krzywizny**   |                                                                                                                                       |
|                          | **<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [Pokaż / ukryj grzebień krzywizny krzywej złożonej](Sketcher_BSplineComb/pl.md)**                      |
|                          |                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Wielokrotność węzłów** |                                                                                                                                       |
|                          | **<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:16px"> [Pokaż / ukryj krotność węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md)** |
|                          |                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Waga**                 |                                                                                                                                       |
|                          | **<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Pokaż / ukryj wagi krzywej złożonej](Sketcher_BSplinePoleWeight/pl.md)**                        |
|                          |                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

### Ograniczenia

W chwili obecnej *(FreeCAD v0.19)* istnieją pewne ograniczenia podczas używania krzywych złożonych, które powinieneś znać:

1.  Nie można ustawić wiązań stycznych.W tym przykładzie <img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width:450px;"> chcesz zapewnić, że krzywa dotknie niebieskiej krzywej 2 razy stycznie. Byłoby to użyteczne, ponieważ niebieska linia może być na przykład przestrzenną granicą dla twojego projektu.
2.  Nie można wstawić nowego punktu kontrolnego pomiędzy dwa wybrane istniejące punkty kontrolne. Nie ma innego sposobu niż przerysowanie linii krzywej.
3.  Nie można usunąć punktu kontrolnego. Również w tym przypadku musisz przerysować krzywą.
4.  Nie można utworzyć krzywej odsunięcia dla linii krzywej złożonej używając narzędzia środowiska Rysunek Roboczy [Odsunięcie](Draft_Offset/pl.md).

## Przypadki typowego zastosowania 

Zgodnie z właściwościami linii krzywych złożonych, istnieją trzy główne przypadki zastosowań:

1.  Krzywe, które zaczynają się / kończą stycznie do pewnego kierunku. Przykładem tego jest przykład motywacyjny [powyżej](#Motywacja.md).
2.  Krzywe opisujące większe projekty i zapewniające swobodę lokalnych zmian. Zobacz [przykład projektowania](#Projektowanie.md) poniżej.
3.  Krzywe zapewniające pewną ciągłość *(pochodną)*. Zobacz [przykład ciągłości](#Ci.C4.85g.C5.82o.C5.9B.C4.87_w_przej.C5.9Bciach_geometrycznych.md) poniżej.

### Projektowanie

Rozważmy przypadek, w którym projektujemy obudowę baterii kuchennej. Jej pożądany kształt powinien wyglądać tak jak ten:

![](images/Sketcher_spline-exmple-mixer-shell.png )

Do zdefiniowania formy zewnętrznej korzystne jest użycie krzywej złożonej, ponieważ po zmianie punktu kontrolnego w celu zmiany krzywizny u dołu, krzywizna z boku i u góry nie ulegnie zmianie:

![](images/Sketcher_spline-exmple-mixer-sketch.gif )

### Ciągłość w przejściach geometrycznych 

Istnieje kilka przypadków, w których fizycznie konieczne jest zachowanie pewnej ciągłości powierzchni na przejściach geometrycznych. Weźmy na przykład wewnętrzne ścianki kanału z płynem. Kiedy mamy zmianę średnicy kanału, nie chcemy mieć krawędzi, ponieważ krawędzie wprowadziłyby turbulencje. Dlatego, tak jak w przykładzie motywacyjnym [powyżej](#Motywacja.md), używamy do tego celu krzywych złożonych.

Rozwój krzywych Béziera został zapoczątkowany przez francuski przemysł samochodowy. Oprócz oszczędności materiału i zmniejszenia oporów przepływu powietrza, należało również poprawić wygląd samochodów. Patrząc na fantazyjny design francuskich samochodów z lat 60-tych i 70-tych można zauważyć, że krzywe Béziera dały impuls do rozwoju designu samochodów.

Weźmy na przykład to zadanie w projektowaniu samochodów: Błotnik samochodu powinien \"ładnie wyglądać\". Oto podstawowy szkic do tego zadania:

<img alt="" src=images/Spline-Fender-sketch1.svg  style="width:250px;">

\"Ładny wygląd\" oznacza, że *(potencjalny)* klient patrzy na błotnik i nie widzi niespodziewanych refleksów świetlnych, a także w ogóle żadnych nagłych zmian w odbiciu od lakieru samochodowego. Czego więc potrzebujesz, aby uniknąć zmian w odbiciach? Dokładne przyjrzenie się błotnikowi:

<img alt="" src=images/Spline-Fender-sketch2.svg  style="width:300px;"> 
*W obszarze przestrzennym nad krawędzią intensywność światła odbitego jest niska ''(oznaczona czerwoną elipsą)'', ponieważ w kierunku od krawędzi do oka nie odbija się bezpośrednio żadne światło.*

Widzisz, kiedy jest krawędź, istnieje obszar przestrzenny, w którym odbite światło ma mniejszą intensywność i to jest to, co zauważysz patrząc na błotnik. Aby tego uniknąć potrzebna jest ciągła zmiana nachylenia elementów powierzchni. Nachylenie jest pochodną pierwszego rzędu i jak wyjaśniono w sekcji [Podstawy](#Podstawy.md), krzywa złożona drugiego stopnia *(kwadratowa)* oferuje w każdym punkcie ciągłą pochodną pierwszego rzędu.

Ale czy to naprawdę wystarczy? W punkcie przejścia geometrycznego mamy teraz po obu stronach to samo nachylenie, ale nachylenie to może się zmieniać w różny sposób po obu stronach. Wtedy mamy taką sytuację:

<img alt="" src=images/Spline-Fender-sketch3.svg  style="width:300px;">

Mamy więc również obszary przestrzenne, w których natężenie światła odbitego jest różne. Aby tego uniknąć, potrzebujemy w geometrycznym punkcie przejścia również ciągłości pochodnej drugiego rzędu, a więc sześciennej krzywej złożonej.
