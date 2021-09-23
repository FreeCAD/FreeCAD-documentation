# Navigation Cube/pl






{{TOCright}}

Sterowanie kostką nawigacyjną lub **kostka nawigacyjna** jest pomocą graficzną interfejsu użytkownika w celu zmiany orientacji widoku 3D. Domyślnie jest ona widoczny i znajduje się w prawym górnym rogu okna 3D. Jeśli patrzysz na standardowy widok 3D, wygląda to następująco:

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

Kostka nawigacyjna składa się z kilku części:

-   Strzałki kierunkowe.
-   Główny sześcian nawigacyjny.
-   Menu mini-kostki.

Najechanie kursorem myszki na element kostki nawigacyjnej zmienia kolor tego elementu na jasnoniebieski; kliknięcie spowoduje zmianę orientacji widoku 3D w sposób wskazany przez funkcję. W poniższym przykładzie widok 3D został obrócony na \"niestandardową\" orientację za pomocą [gestu myszki](Mouse_Model.md). Wskaźnik znajduje się nad narożnikiem *(oznaczonym kolorem niebieskim)*; kliknięcie spowoduje przekierowanie widoku 3D na standardowy widok przestrzenny z tym narożnikiem zwróconym w stronę użytkownika.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Strzałki kierunkowe 

Istnieje sześć strzałek kierunkowych: cztery trójkątne groty, jedna na górze, na dole, w lewo i w prawo; oraz dwie zakrzywione strzałki, po obu stronach górnego grotu.

Kliknięcie trójkątnych grotów spowoduje obrócenie widoku 3D o 45° wokół osi prostopadłej względem kierunku strzałki. Kliknięcie zakrzywionych strzałek spowoduje obrócenie widoku 3D wokół linii skierowanej w Twoją stronę.

## Główny sześcian nawigacyjny 

Główny sześcian nawigacyjny *(\"kostka nawigacyjna\" w pozostałej części tej sekcji)*, śledzi orientację rzeczywistego obiektu w głównej części okna widoku 3D. Każda operacja, która przekierowuje główny widok przestrzenny, zmieni również orientację kostki nawigacyjnej.

Kostka nawigacyjna jest zasadniczo widokiem przestrzennym kostki z jej trzema podstawowymi typami składowymi *(ścianki, krawędzie i narożniki)*, dzięki czemu można je łatwo kliknąć wskaźnikiem. Kliknięcie na konkretny komponent ustawia widok 3D w taki sposób, aby komponent był wyśrodkowany i zwrócony w stronę użytkownika. Wizerunek kostki jest nieco zgnieciony, jakby element najbardziej oddalony od Ciebie był większy niż element zwrócony bezpośrednio do Ciebie. Pozwala to na to, aby elementy sąsiadujące z elementem zwróconym w Twoją stronę były widoczne i aby można je było wybrać świadomie. Na przykład, w normalnym widoku regularnego sześcianu, gdy jedna ściana jest zwrócona do Ciebie, możesz również zobaczyć cztery krawędzie tej ścianki i cztery rogi tej ścianki. W zgniecionej wersji widoku kostki można również zobaczyć elementy reprezentujące każdą z sąsiadujących ze sobą ścian, cztery krawędzie łączące narożniki ściany zwróconej do Ciebie z przeciwległą ścianą oraz narożniki przeciwległej ściany. Pozwala to na wybór dowolnego z możliwych widoków standardowych z wyjątkiem przeciwległej ściany i jej krawędzi *(21 z 26 możliwych widoków)*:

-   Ściana zwrócona do ciebie *(nie robi nic, bo to jest aktualny widok)*.
-   Cztery krawędzie obecnej ściany.
-   Cztery rogi obecnej ściany.
-   Cztery sąsiednie ściany.
-   Cztery krawędzie prowadzące do przeciwległej ścian.
-   Cztery rogi przeciwległej ściany.

Nie ma możliwości wybrania:

-   Przeciwległej ściany.
-   Krawędzi przeciwległej ściany.

Uwaga: Począwszy od momentu napisania tego tekstu *(wersja 0.18)*, istnieją pewne problemy z kostką nawigacyjną; nie wszystkie funkcje są obecnie dostępne. W szczególności, nie można wybierać krawędzi, nie można też wybierać czterech narożników ściany zwróconej bezpośrednio do przodu.

### Wybór ściany 

Klikając na ścianę, można ustawić widok 3D z tą konkretną ścianą zwróconą w stronę użytkownika. Patrząc z perspektywy ściany, dostępne są inne punkty wyboru, jak wspomniano powyżej. Na każdej z zewnętrznych krawędzi znajdują się cztery cienkie paski, reprezentujące cztery sąsiadujące ze sobą ścianki. Kliknięcie ich spowoduje wybranie widoku odpowiadającego sąsiedniej ścianie. Do ustawienia odpowiedniego widoku przestrzennego można użyć czterech zaokrąglonych narożników. Istnieje również wewnętrzny zestaw krawędzi i narożników, które są obecnie nieaktywne.

### Wybór krawędzi 

Niestety, wybór krawędzi jest obecnie zepsuty. Próba wybrania krawędzi spowoduje wybranie powierzchni, która znajduje się za nią. Kliknięcie na krawędź powinno wyśrodkować tę krawędź tak, aby była skierowana w stronę użytkownika.

### Wybór narożnika 

Kliknięcie jednego z narożników daje widok przestrzenny widziany z tego narożnika. Jak wspomniano powyżej, obecnie, gdy ściana jest zwrócona bezpośrednio do Ciebie, narożniki tej ścianki nie są wybierane.

## Menu mini-kostki 

Po niżej prawego dolnego rogu sześcianu nawigacyjnego, znajduje się mały sześcian. Kliknięcie na ten sześcian spowoduje wyświetlenie menu, za pomocą którego można zmienić typ widoku *(na ortograficzny, perspektywiczny, izometryczny)*. Oraz wykonać jednym kliknięciem **Powiększanie i dopasowanie**.

## Przesuwanie sześcianu nawigacyjnego na ekranie 

Możesz przesunąć całą strukturę sterowania kostki nawigacyjnej w inne miejsce obrazu w oknie z widokiem 3D, naciskając myszką w dowolnym miejscu korpusu sześcianu nawigacyjnego i przeciągając go. Struktura nie zacznie się poruszać, dopóki kursor myszki nie przesunie się poza krawędź głównego sześcianu nawigacyjnego.

## Konfiguracja

Sześcian nawigacyjny jest konfigurowalny, włącznie z dostosowaniem jego rozmiaru: **Edycja → Preferencje → Wyświetlanie → Nawigacja → Kostka nawigacyjna** {{Version/pl|0.19}}.

Bardziej zaawansowana konfiguracja jest dostępna w tabeli - pozycja:**CubeMenu** [zewnętrznych środowisk pracy](External_workbenches/pl.md).







[Category:User Documentation](Category:User_Documentation.md)
