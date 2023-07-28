# Part Loft Technical Details/pl
Ta strona wyjaśnia szczegóły tworzenia powierzchni funkcją [wyciągnięcie przez profile](Part_Loft/pl.md). Jest to również istotne dla funkcji [wyciągnięcie po ścieżce](Part_Sweep/pl.md) wykonywanego wzdłuż prostej ścieżki, chociaż istnieją różnice.

Podane informacje są specyficzne dla implementacji i mogą ulec zmianie. Obecny stan dotyczy programu FreeCAD 0.15.4119, wersja OCC: 6.7.0.



## Etapy powstawania wyciągnięcia 

Aby wyjaśnić proces wyciągnięcia przez profile, wygodnie jest podzielić go na etapy:

1.  wyrównać liczbę segmentów w profilach *(jeśli jeszcze nie są)*,
2.  ustalić zgodność między segmentami,
3.  wykonanie powierzchni wyciągnięcia.



## Krok 1. Dopasowanie liczby segmentów w profilach 

Operacja ta wymaga dopasowania liczby segmentów, aby utworzyć powierzchnie pomiędzy odpowiadającymi im segmentami. Jeśli ilość segmentów zgadza się we wszystkich profilach, ten krok jest pomijany.

Jeśli przynajmniej jeden z profili ma inną liczbę segmentów, stosuje się następującą procedurę. Dla uproszczenia procedura została tu wyjaśniona dla przypadku tylko dwóch profili.

1.  Profile są tymczasowo wyrównane tak, że są współpłaszczyznowe, a ich środki mas\* są zgodne.
2.  *(patrz rysunek)* dla każdego wierzchołka w jednym profilu, drugi profil jest krojony pod tym samym kątem biegunowym *(środek biegunowy to środek masy)*. Jeśli jest więcej niż jeden plasterek możliwy lub nie jest możliwy żaden plasterek w ogóle *(może się to zdarzyć na bardzo wypukłych profilach)*, wyciągnięcie zazwyczaj się nie udaje.
3.  to samo jest wykonywane w przeciwnym kierunku.

Operację tę rozszerzamy na wszystkie profile, by uzyskać równą liczbę odcinków. Całkowita liczba odcinków w każdym profilu będzie równa sumie wszystkich liczb odcinków wszystkich profili *(pod warunkiem, że żaden z wierzchołków nie znajdzie się pod tym samym kątem polarnym)*.

   
  <img alt="Proces krojenia profilu2 *(biały półksiężyc)* w celu utworzenia połączeń odpowiadających wierzchołkom profilu1 *(fioletowy pięciokąt)*. Wstawione złącza są oznaczone żółtymi strzałkami." src=images/Loft-vertex-insertion.png  style="width:300px;">   <img alt="Wynik wyciągnięcia odpowiedni dla rysunku po lewej stronie." src=images/Loft_crescent_pentagon.png  style="width:300px;">
   



### Krok 2. Ustalenie zależności między segmentami 

<img alt="Demonstracja wyciągnięcia przez profile zachowującego liczbę segmentów w profilach, gdy są one dopasowane. Zauważ jak 3 krawędzie górnego kwadratu \"zapadają się\" w mały wielokątny kawałek dolnego profilu." src=images/Loft_Number_of_verts_match.png  style="width:300px;"> W przypadku, gdy liczby segmentów we wszystkich profilach nie były równe, krojenie zostało wykonane w kroku 1, a korespondencja jest trywialna. W przypadku, gdy liczby odcinków we wszystkich profilach były równe, wykorzystano istniejące odcinki *(patrz rysunek)* i wtedy należy ustalić zgodność.

Dokładny algorytm znajdowania odpowiednich segmentów jest skomplikowany, ale generalnie dąży do zminimalizowania skręcenia wynikowego wyciągnięcia przez profile. Oznacza to, że jeśli ktoś robi wyciągnięcie pomiędzy dwoma kwadratami, maksymalny możliwy skręt to \<45°. Dalszy obrót jednego z kwadratów spowoduje, że wyciągnięcie będzie przeskakiwało do innych wierzchołków.

Korespondencja pomiędzy sąsiednimi profilami odbywa się niezależnie. Oznacza to, że dodatkowe skręcenie można uzyskać poprzez dodanie kolejnych profili.

Kolejną rzeczą, którą należy zauważyć jest to, że gdy liczby segmentów w profilach są równe, otrzymane wyciągnięcie jest znacznie bardziej wytrzymałe w odniesieniu do złożonych profili, zwłaszcza tych niewypukłych. 



### Krok 3. Wykonanie powierzchni wyciągnięcia 

<img alt="Krzywa interpolacji spline *(czerwona)*, która podąża za powierzchnią wyciągnięcia. Punkty, przez które należy interpolować, są pokazane jako czerwone kwadraty." src=images/Loft_B-spline.png  style="width:400px;"> Jeśli istnieją tylko dwa profile, utworzone powierzchnie są powierzchniami rządzonymi pomiędzy odpowiadającymi im segmentami profili. Krawędzie proste są tworzone w celu połączenia odpowiednich wierzchołków profili.

Jeśli istnieją więcej niż dwa profile, powierzchnie są tworzone przez krzywe złożone w taki sam sposób, w jaki linie proste tworzą powierzchnie regulowane. Wyimaginowane krzywe złożone, z których \"zbudowana\" jest powierzchnia, są rysowane przez odpowiednie punkty odpowiednich odcinków profili.

Krzywe są interpolacją krzywych złożonych.

-   Jeśli liczba profili jest mniejsza niż 10, interpolacja odbywa się za pomocą krzywej złożonej o maksymalnym możliwym stopniu *(tj. stopień = number_of_profiles - 1)*.
-   Jeśli liczba profili przekracza 10, interpolacja jest przełączana na krzywą złożoną 3 stopnia.

Stosowana metoda węzłów to \"approximate chord length\". Approximate oznacza, że wektor węzłów jest dokładnie taki sam dla każdej krzywej w wyciągnięciu. Więcej informacji o tym, czym jest interpolacja krzywej złozonej, wektor węzłów, metoda długości cięciwy, można znaleźć na przykład w poradniku [cs.mtu.edu Curve Global Interpolation](http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/INT-APP/CURVE-INT-global.html).

Zauważ, że Wyciągnięcie ma właściwość \"Prostokreślnie\". Jeśli jest ona ustawiona na wartość {{True/pl}}, to pomiędzy sąsiednimi profilami tworzone są powierzchnie regulowane, nawet jeśli jest więcej niż jeden profil. Oznacza to, że interpolacja krzywej złożonej jest zastępowana przez interpolację liniową kawałkową. 



## Główny punkt 

-   Wyciągnięcie wykonuje interpolację krzywej złożonej między dostarczonymi profilami. Interpolacja jest przełączana na liniową, gdy właściwość \"Prostokreślnie\" jest ustawiona na {{True/pl}}.
-   Gdy liczba profili przekracza 9, stopień interpolacji spada do 3. To przełączenie może znacznie zmniejszyć drgania.
-   Dopasowanie liczby segmentów *(względem liczby wierzchołków)* w profilach pozwala na lekkie skręcenie wyciągnięcia i zwykle pozwala na użycie bardziej złożonych profili.
-   Kiedy liczba segmentów nie jest dopasowana, najlepiej jest zachować profile, aby były reprezentowane przez odpowiednią funkcję r*(phi)* we współrzędnych biegunowych.



## Uwagi dodatkowe 

-   Nie jest wymagane, aby profile były równoległe *(patrz zdjęcie poniżej)*.
-   W przypadku wyciągnięcia nie jest wymagane, aby profile były rozdzielone *(patrz zdjęcie poniżej)*. Mogą być koplanarne, ale nie powinny się przecinać.
-   Gdy właściwość \"zamknięty\" wyciągnięcia ma wartość {{True/pl}}, we wszystkich krzywych tworzących wyciągnięcie po profilach znajduje się połączenie wierzchołkowe *(patrz rysunek poniżej)*. Nie ma teraz niezawodnego sposobu na płynne zamknięcie wyciągnięcia.

    
  <img alt="Nie jest wymagane, aby profile były równoległe." src=images/Loft_nonparallel.png  style="width:300px;">   <img alt="W wyciągnięciu, profile mogą być współosiowe. W tym przykładzie dwa z trzech profili są współpłaszczyznowe." src=images/Loft_Coplanar.png  style="width:300px;">   <img alt="Przykład zamkniętego wyciągnięcia pomiędzy trzema pięciokątnymi profilami (biały). Należy zwrócić uwagę na niezbyt gładką spoinę na skrajnym profilu. Jest to pierwszy profil w zamkniętym poddaszu." src=images/Loft-closed.png  style="width:300px;">



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft Technical Details/pl
