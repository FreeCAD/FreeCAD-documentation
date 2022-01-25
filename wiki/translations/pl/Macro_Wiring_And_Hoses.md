# Macro Wiring And Hoses/pl
{{Macro/pl
|Name=Macro Wiring And Hoses
|Name/pl=Makrodefinicja: Okablowanie i rurociągi
|Description=Makra te wspierają tworzenie i obsługę kabli i rur.
|Author=Piffpoof
}}

**Od [User:Piffpoof](User_Piffpoof.md) Uwaga: pewne zmiany pomiędzy v 0.14 a v 0.15 wpłynęły na to makro, co opóźni jego wydanie**

Makra te wspierają tworzenie i obsługę sieci przewodów i rur.

![](images/Macro_Wiring_And_HosesCompletedHouse.jpg )

## Kontekst

Jako część naszych innych projektów FreeCAD potrzebowaliśmy sposobu na udokumentowanie okablowania i rur. Ten zestaw makr został stworzony aby sprostać tej potrzebie. Jest wiele rzeczy, których ten system nie robi, ale to co robi, to zapewnia wizualną reprezentację przewodów i rur, albo jako odizolowany system, albo z przewodami i rurami w kontekście modelu FreeCAD. Zapis wszystkich przewodów i rur jest przechowywany w pliku w formacie CSV poza programem FreeCAD. Plik ten może więc zostać wczytany do programu arkusza kalkulacyjnego lub wykorzystany przez inne oprogramowanie.

## Opis

W ramach projektu dokumentacji odkryliśmy, że potrzebujemy udokumentować przewody i rury. Wypróbowaliśmy kilka różnych scenariuszy takich jak tworzenie linii lub cylindrów jako część istniejącego modelu. Ze względu na problemy z ich używaniem lub utrzymaniem zdecydowaliśmy się zachować te informacje w innym formacie i poza programem FreeCAD. W ten sposób mogły być one tworzone samodzielnie lub w ramach istniejącego dokumentu. Ta decyzja pozwoliła użytkownikowi pracować z okablowaniem i rurami w sposób, który mu odpowiadał. Mógł również pracować z nimi na różne sposoby w różnych momentach, gdy zmieniały się potrzeby.

Początkowo nie byliśmy pewni, jak prowadzić listę rur i przewodów i próbowaliśmy różnych podejść. Najprostszym sposobem wydawało się użycie formatu pliku CSV, który istnieje od dawna. Istniały już także procedury napisane do zarządzania plikami CSV z poziomu Pythona. Niektóre z zalet były następujące:

-   czytelny dla człowieka,
-   może być załadowany do dowolnego arkusza kalkulacyjnego,
-   może być utrzymywany przy użyciu arkusza kalkulacyjnego lub prostego edytora tekstu,
-   możliwym przyszłym ulepszeniem byłoby użycie go z arkuszem kalkulacyjnym FreeCAD.

Kolejnymi decyzjami było \"jak\" zdefiniować takie przebiegi kabli. Ponieważ naszym celem była przede wszystkim dokumentacja, wybraliśmy prowadzenie odcinków linii od punktu do punktu. Kwestie takie jak promień skrętu nie są rozpatrywane. Również średnica kabla nie jest obsługiwana. Tabela z przebiegami kabli jest przechowywana w pliku CSV, ale takie rzeczy jak bliskość kabli *(dla kwestii zakłóceń elektrycznych)* i długość trasy nie są obsługiwane *(chociaż można by było dość łatwo dodać podstawową długość trasy kabla)*.

Ten zestaw makr jest w zasadzie \"dowodem koncepcji\", demonstruje pewne pomysły i ich wykonalność. Naszym głównym celem była dokumentacja, a nie fizyczne zarządzanie instalacją. Zdecydowaliśmy się na utrzymanie struktury danych punktów, które są punktami, przez które przebiegają przewody i rury. Po drugie utworzyliśmy strukturę danych, która definiuje kable i rury pod względem punktów, przez które przechodzą. Tak więc przewód może być poprowadzony tylko tam, gdzie zostały zdefiniowane dla niego punkty.

Dla tych dwóch struktur danych wybraliśmy następujące nazwy:

-   Węzeł - punkt, przez który może przechodzić kabel lub rura *(liczba mnoga to Nexi)*. Węzły są po prostu punktami w przestrzeni 3D, dla ułatwienia wizualizacji oprogramowanie umieszcza pierścienie wokół lokalizacji, ale służą tylko dla ułatwienia użycia. Widoczność Pierścieni może być wyłączona lub włączona w zależności od preferencji użytkownika.
-   Przepływy - ogólnie są to trasy składające się z Węzłów. Do każdego typu przypisany jest kod, domyślne kody to
    -   W - przewody elektryczne
    -   C - przewody, przeznaczone głównie dla kabli, ale mogące zawierać wszystko
    -   H - rury do przenoszenia różnych płynów
    -   G - przewody gazowe
    -   K - trasa kamery, to jest tak naprawdę zarezerwowane dla przyszłych eksploracji, jak w [Zwiedzanie ujęciem widoku](http://forum.freecadweb.org/viewtopic.php?f=24&t=8437).

Zarówno Węzły jak i Przepływ mają nazwy przypisane przez użytkownika, dodatkowo Węzły mają wewnętrznie przypisane ID w celu ułatwienia zarządzania. Będąc punktami lub lokalizacjami w przestrzeni Węzły nie mają kolorów, ale Przepływy mogą mieć jeden z 48 zdefiniowanych kolorów. Nacisk na kolory wiąże się z zamierzonym celem, jakim jest dokumentacja.

Ogólny przebieg pracy jest następujący

-   zdefiniuj i ustaw Węzeł,
-   zdefiniuj Przepływ*(y)* w odniesieniu do Węzłów,
-   dla celów konserwacyjnych edytuj zarówno Węzły, jak i Przepływy albo wizualnie za pomocą GUI FreeCAD, albo używając podejścia tabelarycznego i definicji CSV.

Ponieważ plik danych zawierający definicje Węzłów i Przepływu jest plikiem tekstowym, może być obsługiwany w dowolnym edytorze tekstu lub przez dowolny inny program, który chce uzyskać dostęp do danych.

### Tryby nawigacyjne 

Ponieważ duża część pracy z tymi makrami polega na manipulowaniu wyświetlanym modelem w celu umieszczenia i weryfikacji umieszczenia punktu w przestrzeni trójwymiarowej, niezbędna jest znajomość trybów nawigacyjnych programu FreeCAD, które są udokumentowane na stronie [Profil nawigacji myszką](Mouse_navigation/pl.md). Umiejętność obracania modelu w przestrzeni trójwymiarowej, a następnie wykonywania operacji na nieruchomym modelu jest niezbędna.

## Instalacja

Kod dla **Okablowania i rurociągów** znajduje się w wielu makrach i bibliotece. Instalacja polega więc na skopiowaniu kodu do odpowiedniego katalogu makr i wywołaniu narzędzia Build Utility z menu makr, konsoli Pythona lub przycisku na pasku narzędzi *(preferowana metoda)*.
-   zobacz stronę [Jak zainstalować makrodefinicję](How_to_install_macros/pl.md), aby uzyskać informacje, jak zainstalować ten kod makra
-   zobacz stronę [Dostosowanie pasków narzędzi](Customize_Toolbars/pl.md), aby uzyskać informacje, jak zainstalować jako przycisk na pasku narzędzi.

## Użycie

Istnieją naprawdę dwa różne podejścia do pracy z tymi makrodefinicjami: Węzły i Przepływy mogą być zdefiniowane samodzielnie przy użyciu współrzędnych przestrzennych, lub można użyć istniejącego dokumentu FreeCAD i zdefiniować Węzły i Przepływy w kontekście tego dokumentu. Nie jest to decyzja typu \"albo / albo\", ale raczej oba podejścia mogą być stosowane, gdy są najbardziej odpowiednie. Ponieważ definicje Węzłów i Przepływów są przechowywane w pliku w formacie CSV, który jest przechowywany poza programem FreeCAD, obecność lub brak dokumentu FreeCAD nie ma wpływu na pracę z Węzłami i Przepływami, ale ułatwia ją poprzez zapewnienie kontekstu wizualnego. Dla tego opisu użycia w przykładzie zostanie użyty wcześniej załadowany dokument FreeCAD jako kontekst, ponieważ łatwiej jest umieścić

Użycie tych makrodefinicji dzieli się na 3 części:

-   zdefiniuj Węzły,
-   zdefiniuj Przepływy,
-   edycja pliku w formacie CSV w celu zmiany lub dodania Wezła i Przepływów

Istnieją alternatywne sposoby wykonania niektórych z przedstawionych poniżej zadań, o których mogą decydować osobiste preferencje. Ten przykład dotyczy instalacji elektrycznej i zimnej wody w domu. Tak wygląda nasz pusty dom

![](images/Macro_Wiring_And_HosesEmptyHouse.jpg )

i czeka na zainstalowanie zimnej wody i prądu. Dla wygody wyjaśnienia wszystkie elementy elektryczne są w kolorze żółtym, a woda w kolorze niebieskim *(oprócz 2 zlewów)*.

### Określenie Węzłów 

Pierwszym krokiem jest utworzenie punktów w przestrzeni trójwymiarowej *(zwanych \"Węzłami\")*. Punkty te zostaną użyte w następnym kroku do zdefiniowania przepływu. Punkty te tworzymy klikając na *(tj. wybierając)* powierzchnię, a następnie podając nazwę dla Węzła. Ten opis dotyczy definiowania punktów Węzłów dla przepływu wody.

1.  kliknij na ikonę 
2.  pojawi się następujące okno dialogowe:

. To jest pytanie, czy chcesz otworzyć i załadować dokument FreeCAD, który zawiera model, do którego chcesz dodać Węzeł i przepływy. Nie jest konieczne wczytywanie żadnego, ale dla tego przykładu wczytamy nasz pusty dom.

1.  wybierz powierzchnię klikając na nią, zostanie ona podświetlona w oknie Widoku Drzewa i będzie miała kolor potwierdzający zaznaczenie an ekranie.
2.  kliknij na ikonę 
3.  pojawi się następujące okno dialogowe z pytaniem o nazwę dla nowego Węzła:



1.  Węzeł zostanie teraz zdefiniowany. Zostanie on umieszczony w przestrzeni trójwymiarowej tak, aby znajdował się na linii od wybranej ściany do obserwatora, tuż obok ściany, tak aby nie znajdował się wewnątrz obiektu. Chociaż węzeł może nie być w idealnym położeniu, zostaw go na razie, ponieważ będzie on edytowany w późniejszym kroku. Zostanie wyświetlony specjalny okrąg *(pierścień)*, który jest wyśrodkowany w punkcie węzła. Okrąg ten jest jedynie narzędziem wizualizacji, dzięki któremu można zidentyfikować położenie punktu. Pierścienie wizualizacji mogą być włączane/wyłączane w dowolnym momencie.
2.  zdefiniuj kolejne węzły w ten sam sposób, nadając każdemu z nich sensowną nazwę
3.  kliknij na ikonę 
4.  pojawi się następujące okno dialogowe:



1.  odpowiedz Tak, aby zapisać nowe węzły

Uwaga: w każdym momencie możesz dołączyć już istniejący projekt, aby mieć widoczny ogólny obraz sytuacji.

### Określenie przepływ 

Po zdefiniowaniu Węzły mogą być one użyte do zdefiniowania przepływu. Nasz dom wygląda teraz tak:

\< picture of house with nexi but not flows\>

Posiada Węzły zdefiniowane dla przepływu wody, ale teraz jeszcze nie ma przepływu.

1.  kliknij na ikonę .

pojawi się następujące okno dialogowe:



To jest prośba o wybranie Węzłów w kolejności, w jakiej mają one tworzyć przepływ.

1.  wybierz typ przepływu: Przewody, Kanalazacja, Rury, Linie gazowe
2.  używając drugiego okna, wybierz Węzły w kolejności, w jakiej chcesz je utworzyć



1.  podaj nazwę dla przepływu,
2.  wybierz kolor dla przepływu,
3.  kliknij przycisk **OK** lub **Anuluj**. Jeśli popełnisz błąd w wyborze Węzła *(albo w kolejności, albo włączając niewłaściwe Węzły)*, kliknij przycisk **Anuluj** i rozpocznij ten krok ponownie.

\< picture of house with water flow\>

![](images/Macro_Wiring_And_HosesFlowsOnly.jpg )

### Edycja Nexi i przepływów 

Istnieją 3 różne sposoby edycji Węzła. Ponieważ przepływy są zdefiniowane w kategoriach Węzłów, modyfikacja Węzła będzie miała wpływ na każdy przepływ, który je zawiera. Dla opisowych atrybutów przepływu, takich jak kolor i nazwa, istnieje jeden sposób na edycję.

Do tej pory w tym przykładzie wygenerowaliśmy następującą tabelę:







## Interfejs użytkownika 

Interfejs użytkownika jest kombinacją własnych ekranów oraz standardowych części GUI programu FreeCAD.

\<snapshot 1 defining Nexi\>

\<snapshot 2 defining flow\>

\<snapshot 3 editing CSV file\>

\<snapshot 4 editing Position\>

## Opcje

W chwili obecnej nie ma żadnych opcji dotyczących przewodów i rur.

## Przykładowe pliki 

## Uwagi

## Znane problemy 

## Przyszłe możliwości 

## Słowniczek

## Odnośniki internetowe 

## Skrypty



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Wiring And Hoses/pl
