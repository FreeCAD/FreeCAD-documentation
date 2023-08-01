# B-Splines/pl
{{TOCright}}

Ta strona opisuje jak używać krzywych złożonych *(typu B-spline)* w programie FreeCAD. Podaje również podstawowe informacje czym są krzywe złożone i do jakich zastosowań są przydatne.

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

Krzywe Béziera są wielomianami opisującymi połączenie między dwoma punktami. Najprostszym wielomianem łączącym dwa punkty jest prosta *($A*x^1+B$)*, zatem liniowe krzywe Béziera są również odcinkami linii:

![](images/Bezier_linear_anim.gif ) 
*Animacja 1: Liniowa krzywa Béziera.*

Jednak wielomian staje się użyteczny, gdy możemy go kontrolować. Powinien więc istnieć punkt pomiędzy dwoma punktami końcowymi, który pozwala nam określić jak punkty końcowe są połączone. Tak jak w powyższym przykładzie w opcji trzeciej krzywa jest przydatna, gdy zaczyna się i kończy stycznie do linii przecinających punkty końcowe. I to jest główna cecha krzywych Béziera. Dodajmy więc punkt kontrolny pomiędzy punktami końcowymi. Krzywa zacznie się stycznie do tego punktu kontrolnego, co oznacza, że jest styczna do linii, którą możemy narysować pomiędzy punktem początkowym a punktem kontrolnym. Idąc wstecz od punktu końcowego krzywa będzie również styczna do linii, którą możemy narysować pomiędzy punktem kontrolnym a punktem końcowym. Animacja numer 2 pokazuje jak wygląda taka krzywa.

![](images/Bezier_quadratic_anim.gif ) 
*Animacja 2: Kwadratowa krzywa Béziera. Punktem kontrolnym jest tutaj punkt P1.*

Animacja jasno pokazuje, czym w zasadzie jest krzywa - przejściem od punktu P0 do punktu P2 poprzez obrócenie linii P0-P1 tak, aby stała się linią P1-P2. W ten sposób otrzymujemy ładną cechę stycznego początku / końca.

Taka krzywa może być opisana tylko wielomianem kwadratowym. *(Liczba lewych / prawych obrotów + 1 to konieczny rząd wielomianu. Wielomian kwadratowy to jeden zwrot, wielomian sześcienny ma dwa zwroty, itd.)* Dlatego krzywa Béziera z jednym punktem kontrolnym jest kwadratową *(drugiego rzędu)* krzywą Béziera.

Posiadanie tylko jednego punktu kontrolnego często nie jest wystarczające. Weźmy powyższy motywujący przykład. Tam w opcji 3 kończymy krzywą stycznie w kierunku x. Ale jak można połączyć punkty *(20, 0)* i *(80, 40)* tak, aby krzywa kończyła się stycznie w kierunku y? Aby to osiągnąć potrzebny jest najpierw zwrot w prawo, a potem w lewo, a więc wielomian sześcienny *(trzeciego rzędu)*. A to oznacza, że dla krzywej Béziera potrzebujemy *(lub można powiedzieć, że zyskujemy)* drugi punkt kontrolny. Animacja 3 pokazuje sześcienną krzywą Béziera.

![](images/Bezier_cubic_anim.gif ) 
*Animacja 3: Sześcienna krzywa Béziera.*

Aby odpowiedzieć na pytanie, rozwiązaniem z zakończeniem stycznym w kierunku y dla przykładu jest:

<img alt="" src=images/B-splines_Motivation-cubic-bezier.png  style="width:450px;">

### Zasady

W pochodnej mogłeś już zauważyć pewne \"reguły\" dla krzywych Béziera:

-   Stopień wielomianu jest jednocześnie stopniem krzywych.
-   Jeśli potrzebujesz $n$ skrętów, potrzebujesz co najmniej $n+1$ stopnia krzywej Béziera.
-   Krzywa Béziera zawsze zaczyna się stycznie do linii między punktem początkowym a pierwszym punktem kontrolnym *(i kończy się stycznie do linii między ostatnim punktem kontrolnym a punktem końcowym)*.

### Matematyka

Jeśli jesteś zainteresowany, aby zrozumieć matematykę w tle, oto podstawy.

Krzywą Béziera oblicza się według poniższego wzoru:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{polynomial term}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{polynomial term}}\; \underbrace{P_{i}}_{\text{point coordinate}}$

\"n\" jest niniejszym stopniem krzywej. Zatem krzywa Béziera stopnia *n* jest wielokątem rzędu *n*. Współczynniki $P_{i}$ są więc współrzędnymi punktów kontrolnych krzywych Béziera. Wizualizację można znaleźć na stronie [kontrolowanie krzywizn Béziera](https://pomax.github.io/bezierinfo/#control).

Jeśli jesteś dalej zainteresowany, spójrz na stronę [Matematyka krzywych Béziera](https://pomax.github.io/bezierinfo/#explanation) z ładnie animowanym wyprowadzeniem matematyki dla krzywych Béziera.

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

#### Zasady 

Ponieważ przedstawimy tylko podstawy teorii krzywej złożonej *B-spline*, nie wchodzimy tutaj w szczegóły.

Podstawą jest konstrukcja krzywej typu splajn. Patrząc na definicję krzywych Béziera w dziale [Matematyka](#Matematyka.md) pamiętamy, że krzywa Béziera jest liniową kombinacją wielomianów, których współczynnikiem jest współrzędna x/y każdego z punktów kontrolnych. Wielomiany te nazywane są wielomianami Bernsteina.

Ponieważ kilka krzywych Béziera jest łączonych w celu utworzenia splajnu, otrzymujemy zbiór wielomianów Bernsteina tworzących splajn (są one podstawą). Ponieważ chcemy pokonać wspomniane ograniczenia krzywych Béziera, nie łączymy geometrycznie różnych wielomianów Bernsteina z krzywych Béziera, ale definiujemy wielomian Bernsteina w całym zakresie geometrycznym splajnu. Zatem **nie łączymy** krzywych Béziera z ich wielomianami Bernsteina, który byłby:

$$\textrm{Bezier-combination}=\begin{cases}
  \sum_{i=0}^{n}P_{i}\cdot B_{i,n}(t),  & 0\le t\le1\\
  \sum_{i=0}^{n}P_{i+n}\cdot B_{i,n}(t-1), & 1\le t\le2\\
\cdots
\end{cases}$$

natomiast $B_{i,n}(t)$ jest i-tym wielomianem Bernsteina o rzędzie $n$, a współczynniki $P_{i}$ są współrzędnymi punktów kontrolnych krzywej Béziera. My jednak używamy **innego zestawu funkcji**, które są zdefiniowane na całym zakresie splajnu:

$$\textrm{B-spline}= \sum_{i=0}^{n}p_{i}\cdot N_{i,n}(t)$$.

Zauważ, że ogólnie $N_{i,n}(t) \ne B_{i,n}(t)$, a punkty kontrolne Beziera $\{P_1, P_2,\dots\}$ różnią się od punktów kontrolnych B-spline $\{p_1, p_2,\dots\}$.

Różne $N_{i,n}(t)$ są zdefiniowane fragmentarycznie, gdzie przedział każdego fragmentu jest przedziałem fragmentu Béziera.

Gdy długości wszystkich odcinków $N_{i,n}$ są równe, mówimy o jednolitym splajnie. *(W literaturze często oznacza się to jako równy czas podróży $t$ na kawałek)*.

Aby zrozumieć, w jaki sposób $p_{i}$ są współrzędnymi punktów kontrolnych krzywej B-spline, zobacz pierwszą minutę filmu [tego wideo](https://www.youtube.com/watch?v=dPPTCy4L4rY&list=PL8bSwVy8_IcMvtI70tZoYesCS0hGVO5qd).

#### Wektor węzła 

Jak wywnioskowano powyżej, B-splajny są utworzone z $N_{i,n}$ wielomianów kawałkowych o ciągłości do pewnej pochodnej między kawałkami. Punkty końcowe przedziału definicyjnego kawałka nazywane są węzłami. Dla splajnu zdefiniowanego na $k$ kawałkach istnieje $k+1$ węzłów podanych przez tzw. *wektor węzłów*: $\{t_0, t_1, t_2,\dots, t_k\}$ natomiast $t_0 < t_1 < t_2 < \dots < t_k$

Wektor węzłów zawiera węzły $N_{i,n}$ funkcji bazowych, które definiują B-spline, zobacz film [Węzły krzywej B-spline](https://www.youtube.com/watch?v=ni5NNPCVvDY). Funkcje bazowe B-spline mogą być obliczone przy użyciu wektora węzłów i algorytmu tworzenia, zobacz film [Generowanie funkcji bazowych. Wzór Coxa-de Boora](https://www.youtube.com/watch?v=hrsO45AHtbs).

Pochodna, do której istnieje ciągłość, jest określona przez krotność $m$. Dlatego możemy określić wektor z krotnością dla każdego węzła: $\{m_0, m_1,\dots, m_k\}$. Węzeł na splajnie o stopniu „d" i krotności „m" mówi, że krzywa po lewej i prawej stronie węzła ma co najmniej równą pochodną rzędu „n" *(zwaną „C"\< sup\>*n* ciągłość)*, podczas gdy $n=d-m$.

### Niejednorodne krzywe B-spline 

Wywodzenie krzywych złożonych z krzywych Béziera ma tę matematyczną konsekwencję, że w krzywych złożonych każdy wielomian ma taką samą długość. Takie krzywe złożone nazywane są *jednorodnymi*. Bardziej ogólny przypadek jest taki, że mogą, ale nie muszą mieć tej samej długości. Takie *niejednolite* splajny mają tę zaletę, że można kontrolować, jak blisko splajny przecinają swój punkt kontrolny.

Matematycznie osiąga się to przez zdefiniowanie różnych $N_{i,n}$ elementów w różnych przedziałach. Jeśli na przykład B-splajn jest zdefiniowany dla przedziału \[0, 1\], to jest jednolity, jeśli wszystkie jego np. 5 fragmentów są również zdefiniowane w tym przedziale. Jeśli teraz $N_{1,4}$ jest zdefiniowany tylko w przedziale \[0, 0.6\] *(poza tym przedziałem jest ustawiony na zero)*, to jest krótszy, a więc splajn staje się niejednolity.

Jak opisano powyżej parametry węzłów są opisane przez wektor węzłów. Tak więc wektor węzłów przechowuje przedziały definicyjne. Kiedy teraz jeden kawałek dostaje inny interwał, również wektor węzłów zmienia się, zobacz film [Niejednolite krzywe B-spline i ich funkcje bazowe](https://www.youtube.com/watch?v=w-l5R70y6u0) dla wizualizacji.

### Relacyjne krzywe B-splajn 

Dalsze uogólnienie dla krzywych złożonych może być dokonane poprzez wprowadzenie wag dla punktów kontrolnych. W ten sposób można kontrolować \"jak ważny\" jest dany punkt kontrolny.

Równanie dla takiego splajnu to:

$$c(n, t)=\cfrac{\sum_{i=0}^{n}d_{i}N_{i, n}(t)\cdot w_i}{\sum_{i=0}^{n}N_{i, n}(t)\cdot w_i}$$

Zauważ, że funkcja nie jest już wielomianem, ale funkcją racjonalną, a takie splajny nazywamy racjonalnymi krzywymi złożonymi. Zauważ, że gdy wszystkie $w_i$ są równe, to równanie sprowadza się do regularnej nieracjonalnej krzywej złożonej. Zatem nieracjonalne krzywe złożone są podzbiorem racjonalnych krzywych złożonych.

Te niejednorodne i racjonalne *(z powodu podziału)* krzywe B-spline są często nazywane **[NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline)** i są szeroko stosowane w modelowaniu geometrycznym.

## Krzywe złożone w programie FreeCAD 

FreeCAD oferuje możliwość tworzenia jednolitych lub niejednolitych krzywych złożonych dowolnego stopnia w przestrzeni 2D, za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).

### Tworzenie

Aby utworzyć krzywe złożone, przejdź do szkicu i użyj przycisku na pasku narzędzi **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Utwórz krzywą złożoną](Sketcher_CreateBSpline/pl.md)**. Następnie kliknij lewym przyciskiem myszy, aby ustawić punkt kontrolny, przesuń kursor w lewo, aby ustawić następny punkt kontrolny i tak dalej. Na koniec kliknij prawym przyciskiem myszy, aby zakończyć definicję i utworzyć krzywą.

Domyślnie tworzone są jednolite krzywe sześcienne, ale nie ma wystarczającej ilości punktów kontrolnych, aby to zrobić. Tak więc, gdy tworzysz krzywą złożona z tylko 2 punktami kontrolnymi, otrzymujesz oczywiście krzywą, która jest pojedynczą liniową krzywą Béziera, dla 3 punktów kontrolnych otrzymujesz kwadratową krzywą Béziera, a dla 5 punktów kontrolnych otrzymujesz sześcienną krzywą złożoną z 2 segmentów Béziera. {{Version/pl|0.20}} Możesz również użyć klawisza D podczas tworzenia krzywej B-spline, aby ustawić jej stopień *(nadal będzie ona opadać do niższego stopnia, jeśli podano mniej punktów)*.

Aby utworzyć periodyczne krzywe złożone *(B-splajny, które tworzą zamkniętą krzywą)*, użyj przycisku na pasku narzędzi **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Okresowa krzywa złożona ...](Sketcher_CreatePeriodicBSpline/pl.md)**. Nie jest konieczne ustawianie ostatniego punktu kontrolnego na pierwszym, ponieważ linia krzywej zostanie automatycznie zamknięta:

![](images/Sketcher_Periodic-B-spline-creation.gif )

Krzywe złożone mogą być również generowane z istniejących segmentów szkicu. Aby to zrobić, zaznacz elementy i naciśnij przycisk paska narzędzi **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Konwertuj geometrię na krzywą złożoną](Sketcher_BSplineApproximate/pl.md)**.

Podczas tworzenia krzywej złożonej można określić jej stopień, naciskając klawisz **D**. Dzięki temu można zastąpić domyślne ustawienie tworzenia sześciennej krzywej złożonej, jeśli jest to możliwe. {{Version/pl|0.20}}

### Zmiana stopni 

Aby zmienić stopień, wybierz krzywą złożoną i użyj przycisku z paska narzędzi **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> [Zwiększ stopień krzywej złożonej](Sketcher_BSplineIncreaseDegree/pl.md)** lub **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> [Zmniejsz stopień krzywej złożonej](Sketcher_BSplineDecreaseDegree/pl.md)**.

**Uwaga:** Zmniejszanie stopnia nie może odwrócić wcześniejszego zwiększenia stopnia, zobacz stronę Wiki [Zmniejsz stopień krzywej złożonej](Sketcher_BSplineDecreaseDegree/pl.md), aby uzyskać wyjaśnienie.

### Zmiana wielokrotności węzłów 

Punkty, w których dwie krzywe Béziera łączą się tworząc krzywą złożoną nazywane są węzłami. Mnogość węzłów określa sposób łączenia części Béziera, zobacz stronę Wiki [Zwiększ liczebność węzłów](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md), aby poznać szczegóły.

Aby zmienić krotność węzłów, użyj przycisków paska narzędzi **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:24px"> [Zwiększ krotności węzłów](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md)** lub **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [Zmniejsz krotności węzłów](Sketcher_BSplineDecreaseKnotMultiplicity/pl.md)**.

**Uwaga:** Tworzenie dwóch krzywych złożonych, które są ze sobą połączone, nie połączy się w jedną nową krzywą złożoną. Zatem ich punkt połączenia nie jest węzłem. Jedynym sposobem na uzyskanie nowego węzła w istniejącej krzywej jest zmniejszenie jej stopnia. Jednakże, możesz uzyskać wiele nowych węzłów. Dlatego lepszym wyborem jest przerysowanie krzywej z większą liczbą punktów kontrolnych.

### Zmiana wagi 

Wokół każdego punktu kontrolnego znajduje się ciemnożółte koło. Jego promień określa wagę dla danego punktu kontrolnego. Domyślnie wszystkie okręgi mają promień równy *1*. Jest to oznaczone za pomocą wiązania promienia dla pierwszego okręgu punktu kontrolnego.

Aby utworzyć racjonalną krzywą złożoną, wagi muszą być niezależne. Aby to osiągnąć, można usunąć wiązanie, że wszystkie okręgi są równe, a następnie ustawić różne wiązania promienia dla okręgów.

Jeśli nie ustawiono żadnego wiązania promienia, można również zmienić promień, przeciągając go:

![](images/Sketcher_Changing-control-point-weigth-dragging.gif )

W przykładzie przeciągania widać, że duża waga przyciąga krzywą do punktu kontrolnego, podczas gdy bardzo mała waga zmienia krzywą tak, jakby punkt kontrolny prawie nie istniał.

Kiedy spojrzysz na [funkcję tworzenia](B-Splines/pl#Niejednorodne_krzywe_B-spline.md) dla niejednorodnych racjonalnych krzywych złożonych zobaczysz, że waga równa zero doprowadziłaby do dzielenia przez zero. Ujemne wagi są teoretycznie możliwe, ale nie są wspierane. Dlatego możesz określić tylko wagi większe od zera.

**Uwaga:** Podczas przeciągania punktów, węzłów lub szerokości, średnice okręgów oznaczających wagę będą się zmieniać. Dzieje się tak dlatego, że ze względów wizualizacyjnych średnica zależy od całkowitej długości krzywej złożonej. Rzeczywista waga nie ulega zmianie.

### Edycja węzłów 

Nowe węzły można dodawać za pomocą przycisku **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:24px"> [Dodaj węzeł krzywej złozonej](Sketcher_BSplineInsertKnot/pl.md)**. {{Version/pl|0.20}}

Węzeł jest usuwany przez zmniejszenie jego stopnia do 0 *(tj. zastosowanie **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [Zmniejsz krotność węzła krzywej złożonej](Sketcher_BSplineDecreaseKnotMultiplicity/pl.md)**, gdy jego stopień wynosi 1)*.

Zmiana wartości parametru węzła nie jest jeszcze obsługiwana.

### Wyświetlanie informacji 

Ponieważ postać krzywej B-splajnu nie mówi wiele o jej właściwościach, FreeCAD oferuje [różne narzędzia](Sketcher_Workbench/pl#Narz.C4.99dzia_szkicownika_dla_krzywych_z.C5.82o.C5.BConych.md) do wyświetlania tych właściwości:

+++
| Właściwość               | Przycisk narzędzia                                                                                                                                   |
+++
| **Stopień**              |                                                                                                                                       |
|                          | **[<img src=images/Sketcher_BSplineDegree.svg style="width:16px"> [Pokaż / ukryj stopnie krzywej złożonej](Sketcher_BSplineDegree/pl.md)**                             |
|                          |                                                                                                                                                   |
+++
| **Ramka kontrolna**      |                                                                                                                                       |
|                          | **[<img src=images/Sketcher_BSplinePolygon.svg style="width:16px"> [Pokaż / ukryj ramkę kontrolną krzywej złożonej](Sketcher_BSplinePolygon/pl.md)**                   |
|                          |                                                                                                                                                   |
+++
| **Grzebień krzywizny**   |                                                                                                                                       |
|                          | **[<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [Pokaż / ukryj grzebień krzywizny krzywej złożonej](Sketcher_BSplineComb/pl.md)**                      |
|                          |                                                                                                                                                   |
+++
| **Wielokrotność węzłów** |                                                                                                                                       |
|                          | **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:16px"> [Pokaż / ukryj krotność węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md)** |
|                          |                                                                                                                                                   |
+++
| **Waga**                 |                                                                                                                                       |
|                          | **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Pokaż / ukryj wagi krzywej złożonej](Sketcher_BSplinePoleWeight/pl.md)**                        |
|                          |                                                                                                                                                   |
+++

### Ograniczenia

W chwili obecnej *(FreeCAD v0.20)* istnieją pewne ograniczenia podczas używania krzywych złożonych, które powinieneś znać:

1.  Nie można ustawić wiązań stycznych.W tym przykładzie <img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width:450px;"> chcesz zapewnić, że krzywa dotknie niebieskiej krzywej 2 razy stycznie. Byłoby to użyteczne, ponieważ niebieska linia może być na przykład przestrzenną granicą dla twojego projektu.
2.  Nie można utworzyć krzywej odsunięcia dla linii krzywej złożonej używając narzędzia środowiska Rysunek Roboczy [Odsunięcie](Draft_Offset/pl.md).

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



---
![](images/Button_right.svg) [documentation index](../README.md) > B-Splines/pl
