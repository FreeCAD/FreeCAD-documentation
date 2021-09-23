# Units/pl


Oto kilka lektur na temat jednostek:

-   [Metrologia](http://en.wikipedia.org/wiki/Metrology)
-   [System SI](http://en.wikipedia.org/wiki/International_System_of_Units)
-   [Jednostki brytyjskie](http://en.wikipedia.org/wiki/Imperial_units)
-   [Jednostki pochodne SI](http://en.wikipedia.org/wiki/SI_derived_unit)
-   [jednostki kątowe](http://en.wikipedia.org/wiki/Degree_%28angle%29)
-   [jednostka wdrożona w OCC](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Przykłady


```python
# -- some examples of the FreeCAD unit translation system --
# make a shortcut for the examples
pq = FreeCAD.Units.parseQuantity

# 10 meters in internal numbers
pq('10 m')

# doing math
pq('3/8 in')

# combined stuff
pq('100 km/h')

# transfer to other units
pq('100 km/h')/tu('m/s')

# derived units (Ohm)
pq('m^2*kg*s^-3*A^-2')

# or
pq('(m^2*kg)/(A^2*s^3)')

# angles 
pq('2*pi rad') # full circle

# as gon
pq('2*pi rad') / tu('gon')

# more imperial
tu('1ft (3+7/16)in')

# or 
pq('1\' (3+7/16)"') # the ' we have to escape because of python

# trigonometry
pq('sin(pi)')

# Using translated units as parameters, this command will create a 50.8mm x 20mm x 10mm box
b = Part.makeBox(pq('2in'), pq('2m')/100, 10)
```

## Obsługiwane jednostki 

Pełna lista wszystkich obsługiwanych jednostek znajduje się [na tej stronie](Expressions/pl#Units.md).

## Cel i zasady: propozycja rozszerzenia systemu zarządzania jednostką 

W kolejnych sekcjach zaproponowano system zarządzania jednostkami rozszerzającymi, rozwijający koncepcję **systemu jednostek**, aktywowanego podczas uruchomionej instancji FreeCAD. Zainteresowanie zdefiniowaniem takiego nowego pojęcia polega na łatwiejszej pracy z tyloma typami jednostek **fizycznych**, ile się chce *(nawet tych tworzonych przez użytkowników)*, bez zwiększania złożoności zarządzania jednostkami dla użytkownika, ani dla programistów FreeCAD.

W skrócie, skalowanie jednostek jest precyzyjnie lokalizowane i przeprowadzane w sposób ogólny.

Osiągnięcie takiej elastyczności jest szczególnie wymagane, gdy zaczyna się zajmować właściwościami materiałów, które mogą mieć bardzo różne jednostki, trudne do zarządzania pojedynczo.

Proponowane rozumowanie umożliwia obsługę jednostek takich jak opisane w [Przewodnik dotyczący stosowania międzynarodowego systemu jednostek *(SI)*](http://physics.nist.gov/cuu/pdf/sp811.pdf) i [Międzynarodowy system jednostek *(SI)*](http://physics.nist.gov/Pubs/SP330/sp330.pdf) obydwóch pochodzących z NIST.

W tej propozycji, w sekcji [Burza mózgów](Units/pl#Burza_mózgów.md) po raz pierwszy przypomina się, jakie są możliwe konteksty, dla których wymagane jest zarządzanie jednostkami.

W sekcji [Organizowanie](Units/pl#Organizing.md) przedstawiamy model danych zachowany w celu osiągnięcia zarządzania jednostkami, oparty na 3 obiektach, *unit*, *unit dictionary* oraz *unit system*. Na koniec przedstawiamy również krótkie API 4. obiektu o nazwie *unit manager*.

## Wynik

Dzięki temu rozszerzeniu dąży się do ułatwienia skalowania jednostek, które może występować pomiędzy różnymi zadaniami biznesowymi. Na przykład, rysunki techniczne mogą być wykonywane w standardowym systemie jednostek, podczas gdy modelowanie FE może być zarządzane w bardziej odpowiednim dla niego systemie jednostek.

Dzięki temu rozszerzeniu wymiana danych między tymi dwoma rodzajami działań staje się łatwiejsza.

## Burza mózgów 

W tej sekcji podkreślone są konteksty stosowania takiego systemu zarządzania jednostkami. Na podstawie tych uwarunkowań jesteśmy w stanie określić jego specyfikacje techniczne.

Zasadniczo podane są 2 przykładowe sytuacje.

### Kontekst 1: otwarcie pliku z danymi 

Otrzymujesz plik zawierający na przykład model geometryczny lub opisujący materiał o dość wielu właściwościach. Model geometryczny jest określony w metrach lub właściwościach materiału zgodnie z międzynarodowym systemem jednostek miar.

Niestety\...

Jesteś ekspertem w modelowaniu FE, i zazwyczaj pracujesz z milimetrami na długość, Mega Pascalem na naprężenia, toną na masę\...

W tym przypadku, zarządzanie jednostkami jest wymagane do skalowania danych z początkowego systemu jednostek zdefiniowanego w pliku wejściowym do systemu jednostek docelowych zdefiniowanego przez użytkownika.

### Kontekst 2: przełączanie układu jednostek w czasie pracy 

W tym przypadku, możesz być jednocześnie facetem, który sporządza rysunek, i facetem, który będzie zarządzał modelowaniem FE. Podobnie jak w poprzednim przypadku, systemy jednostkowe dla tych 2 zadań nie są takie same i musisz przełączyć początkowy system jednostek w czasie pracy na swój ulubiony.

## Organizowanie

### Logika skalowania jednostek 

#### Spójność jednostek w całej bieżącej instancji FreeCAD 

Proponowany system oparty jest na podstawowym założeniu: użytkownik pracuje w jednolitym systemie jednostek. Na przykład, oznacza to, że jeśli użytkownik wyraża długość w milimetrach, to koniecznie powierzchnie będą wyrażone w milimetrach kwadratowych, a nie w metrach kwadratowych. To jest **hipoteza pierwsza**.

#### System jednostek 

Ze względu na \"hipotezę pierwszą\", możliwe i istotne jest zdefiniowanie systemu jednostkowego. System jednostkowy odnosi się do:

-   uruchomionej instancji FreeCAD, w której pracujesz
-   lub może mieć również ogólne zastosowanie do zawartości pliku wejściowego

Według [Przewodnika dotyczącego stosowania międzynarodowego systemu jednostek *(SI)*](http://physics.nist.gov/cuu/pdf/sp811.pdf) z NIST, jest to siedem fizycznych jednostek bazowych. Zdecydowaliśmy się wyrazić układ jednostek w kategoriach tych 7 jednostek bazowych.

Pracując w instancji FreeCAD, użytkownik musi więc najpierw zdefiniować system jednostek, według którego pracuje, zanim zdecyduje się na przejście na inny system jednostek lub przed zaimportowaniem danych z pliku wejściowego.

Ten system urządzeń będzie obowiązywał do momentu, gdy użytkownik zdecyduje się na jego zmianę. Jeśli to zrobi, wszystkie dane z wymiarami będą skalowane.

Biorąc pod uwagę założenie pierwsze zakłada się, że wszystkie dane, które użytkownik wprowadzi ręcznie w FreeCAD są spójne z wybranym systemem jednostek.

Korzyścią wynikającą z pracy z systemem jednostek zdefiniowanch na poziomie instancji uruchomionego programu FreeCAD lub na poziomie plików danych *(zamiast jednostek, które są zdefiniowane na poziomie danych)* byłoby wówczas znaczącym uproszczeniem zarządzania jednostkami.

Oto kilka przykładów systemów jednostek.

-   metr, kilogram, sekunda, amper, kelwin, mol, kandel,
-   milimetr, tona, milisekunda, amper, kelwin, mol, kandel,
-   milimetr, kilogram, milisekunda, amper, kelwin, mol, kandel,
-   \...

#### Jednostki bazowe i pochodne 

Jednostki pochodne są tworzone przez zestawienie jednostek bazowych. Na przykład, przyspieszenie (m/s) łączy w sobie jednocześnie długość i czas. Ciekawy obraz przedstawiający relacje pomiędzy jednostkami bazowymi i pochodnymi można zobaczyć [tutaj](http://physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf) również z NIST.

Dzięki definicji \"systemu jednostek\", użytkownik może pracować z dowolnym rodzajem jednostek pochodnych, bez konieczności uprzedniego ich przewidywania przez programistów FreeCAD.

Zgodnie z [Międzynarodowym Układem Jednostek Miar *(SI)*](http://physics.nist.gov/Pubs/SP330/sp330.pdf), symbole określające jednostki są oficjalnie zatwierdzone. Można z tego wyróżnić dwie konsekwencje.

-   nie jest łatwo programowi komputerowemu pracować z symbolami jednostek, ponieważ niektóre z nich to na przykład greckie litery. Dlatego mogą być one nieco trudne do przetworzenia przez program.
-   choć niektóre jednostki i ich symbole mogą być powszechnie stosowane, mogą nie być oficjalnie zatwierdzone, jak na przykład jednostka \"tona\" (zob. p32 [Międzynarodowy Układ Jednostek Miar *(SI)*](http://physics.nist.gov/Pubs/SP330/sp330.pdf)).

Aby przezwyciężyć te ograniczenia i zachować elastyczność, proponowany system preferuje użycie wielkości jednostkowych zamiast symboli jednostkowych, które mimo to są dostępne ze względów ergonomicznych.

### Model danych 

Przedstawiono trzy podstawowe obiekty systemu zarządzania jednostkami, a mianowicie **jednostkę**, **słownik jednostek** i **system jednostek**.

#### Jednostki

Na wstępie należy podkreślić, że obiekt \" jednostki\" sam w sobie oznacza tylko **wymiar**, jak długość, masa, czas\... Nie określa on *\'wielkości* jak metr, milimetr, kilometr\... Ta ostatnia informacja jest określona przez system jednostek.

##### Wymiar

Obowiązkowy ciąg znaków wskazujący „wymiar" urządzenia. „Wymiar" 7 jednostek podstawowych podano poniżej (według [Przewodnika korzystania z Międzynarodowego Układu Jednostek Miar *(SI)*](http://physics.nist.gov/cuu/pdf/sp811.pdf)).

-   DŁUGOŚĆ
-   MASA
-   CZAS
-   PRĄD ELEKTRYCZNY
-   TERMODYNAMICZNA TEMPERATURA
-   ILOŚĆ SUBSTANCJI
-   NATĘŻENIE ŚWIATŁA

Atrybut *Wymiar* umożliwia identyfikację jednostki. Dwie jednostki nie mogą mieć tego samego *wymiaru*.

##### Oznaczenie

Obowiązkowa tablica zawierająca liczbę całkowitą o wymiarze 7 (liczba jednostek bazowych), która określa, co to za jednostka. Oznaczeniem tych 7 jednostek bazowych jest:

-   DŁUGOŚĆ: \[1,0,0,0,0,0,0\]
-   MASA: \[0,1,0,0,0,0,0\]
-   CZAS: \[0,0,1,0,0,0,0\]
-   PRĄD ELEKTRYCZNY: \[0,0,0,1,0,0,0\]
-   TEMPERATURA TERMODYNAMICZNA: \[0,0,0,0,1,0,0\]
-   ILOŚĆ SUBSTANCJI: \[0,0,0,0,0,1,0\]
-   NATĘŻENIE ŚWIATŁA: \[0,0,0,0,0,0,1\]

Z tych 7 jednostek jesteśmy w stanie wyrazić wszystkie jednostki pochodne zdefiniowane w [Przewodnik dotyczący stosowania międzynarodowego systemu jednostek *(SI)*](http://physics.nist.gov/cuu/pdf/sp811.pdf) i w razie potrzeby stworzyć nowe, takie jak np:

-   GĘSTOŚĆ MASY: \[-3,1,0,0,0,0,0\]
-   OBSZAR: \[0,2,0,0,0,0,0\]

*Oznaczenie* jest atrybutem, dzięki któremu można osiągnąć skalowanie jednostkowe w sposób ogólny.

##### Symbole

Tablica **\[real, string\]** (oznaczająca *\[wielkość, symbol\])*, która wymienia wszystkie *symbole* znane przez FreeCAD. Dzięki tej tablicy, API skalowania jednostek staje się bardziej ergonomiczne, ponieważ *symbole* i związane z nimi *wielkości* są połączone.

Tablica ta może być rozszerzana w miarę potrzeb.

Na przykład wykaz *symboli* jednostki DŁUGOŚĆ i związanych z nimi *wielkości* stanowi:

[1e+12,"Tm"],[1e+09,"Gm"],[1e+06,"Mm"],
[1e+03,"km"],[1e+02,"hm"],[1e+01,"dam"],
[1e+00,"m"],[1e-01,"dm"],[1e-02,"cm"],
[1e-03,"mm"],[1e-06,"µm"],[1e-09,"nm"],
[1e-12,"pm"],[1e-15,"fm"]

Standardowe *symbole* można znaleźć na stronie internetowej [NIST](http://physics.nist.gov/cuu/Units/units.html) oraz na str. 23-26 i str. 32 (\"tona metryczna\" lub \"tona\") z [Międzynarodowy Układ Jednostek Miar *(SI)*](http://physics.nist.gov/Pubs/SP330/sp330.pdf).

#### Słownik jednostek 

Wszystkie jednostki dostępne w programie FreeCAD, jak również nowe utworzone przez użytkownika, powinny być przechowywane w *słowniku jednostek*, który jest plikiem XML *(plik konfiguracyjny FreeCAD)*, tak aby można je było pobrać w razie potrzeby, tj. w momencie uzyskania skalowania jednostek.

##### Jednostki 

Zestaw jednostek, zawartych w słowniku jednostek.

#### System jednostek 

System jednostek to obiekt, który pozwala użytkownikowi zdefiniować aktualną *wielkość* każdej jednostki podstawowej, z którą on pracuje. Na przykład wiedząc, że użytkownik pracuje z milimetrami, tonami i sekundami, dzięki zastosowaniu systemu jednostek, FreeCAD może wiedzieć, że energia wyrażana jest w mililijulach, siła w odniesieniu do newtona i naprężenia w odniesieniu do megapascali.

##### Nazwa

Łańcuch pozwalający użytkownikowi na określenie, jaki jest system jednostek.

##### Wielkości

Określając wielkość 7 jednostek podstawowych, definiuje się system jednostek.

Na przykład \[1e-03, 1e+03, 1, 1, 1, 1, 1\], czyli milimetr, tona, sekunda, amperomierz, kelwin, mol, kandela

#### Zarządzanie jednostką w API 

Przedstawiono tylko logikę niektórych metod, aby podkreślić niektóre cechy. Metody te mogą należeć do obiektu zwanego **menedżerem jednostki**.

##### Sprawdzanie słownika jednostek 

###### isValid

Słownikiem jednostek może być plik XML *(plik konfiguracyjny FreeCAD)*. Zawiera on listę zdefiniowanych jednostek. Taki słownik jest niezbędny do działania proponowanego systemu zarządzania jednostkami.

Musi on spełniać pewne warunki, które należy sprawdzić przed uruchomieniem systemu zarządzania jednostkami. Warunki te są następujące:

-   sprawdź, czy wszystkie jednostki bazowe są zdefiniowane,
-   sprawdzić, czy *wymiar* nie jest zdefiniowany dwukrotnie poprzez jednostki,
-   sprawdź, czy *symbol* nie jest dwukrotnie zdefiniowany we wszystkich istniejących symbolach,
-   sprawdzić, czy oznaczenia wszystkich jednostek mają ten sam zakres,
-   symbol, który jest zdefiniowany jako standardowy symbol *(dla którego wielkość wynosi 1)* dla wszystkich jednostek.

###### isCompatibleWithThisSignature

Słownik jednostek definiuje zbiór jednostek i ich znanych wielkości. Podczas zarządzania jednostką należy sprawdzić, czy jej oznaczenie jest zgodne z zestawem jednostek zarejestrowanych w słowniku jednostek, aby móc go przetwarzać. Sprawdzenie to obejmuje:

-   sprawdzenie, czy długość danych wejściowych oznaczenia jest takiej samej wielkości jak jednostka w słowniku oznaczenia.

##### Jednostki skalujące 

###### scaleUnitFromSymbolToSymbol

Znając wartość początkową, jej jednostkę *(po symbolu)* oraz jednostkę docelową, przeskaluj wartość.

###### scaleUnitFromSymbolToUnitSystem

Znając wartość początkową, jej jednostkę *(po symbolu)* oraz docelowy system jednostek, przeskaluj wartość.

###### scaleUnitFromUnitSystemToSymbol

Znając wartość początkową, jej system jednostek oraz docelową jednostkę *(po symbolu)*, przeskaluj wartość.

#### Motywacje do takiego zarządzania: przykład zastosowania 

Załóżmy, że będziemy ustawiać model elementów skończonych. Aby zbudować nasz model, potrzebujemy siatki, właściwości materiału oraz zdefiniować parametry numeryczne. Biorąc pod uwagę, że mogą to być dziesiątki właściwości materiałowych do zarządzania, wyrażonych różnymi jednostkami, czasami nie zawsze bardzo powszechnymi, interesujące jest dla użytkownika jedynie określenie globalnego systemu jednostek, bez zbytniego przejmowania się nimi.

FreeCAD wykona to po prostu.

Ponieważ programiści i użytkownicy FreeCADa niekoniecznie znają wszystkie jednostki, które można zdefiniować w plikach właściwości materiału, ciekawe wydaje się poleganie na ogólnym systemie.

Załóżmy, że w takim pliku mamy sporą ilość egzotycznych właściwości materiału wyrażonych za pomocą egzotycznych jednostek, i że chcemy pracować w określonym systemie jednostek.

Dzięki proponowanemu rozszerzeniu można łatwo skalować każdą z tych właściwości, znając ich oznaczenia, wielkości i system jednostek docelowych.

Dla każdej z tych właściwości skalowanie uzyskuje się przez pomnożenie początkowej wartości właściwości przez współczynnik $\frac{initialMagnitude}{targetMagnitude}$.

Następnie *targetMagnitude* jest po prostu uzyskiwany w wyniku operacji $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, *bu* oznacza jednostkę bazową.

W ten sposób bardzo łatwo jest zarządzać dowolną liczbą właściwości przy użyciu dowolnego rodzaju jednostek, ze skromnym kodem Pythona.

## Zobacz również 

-   Strona [Wyrażenia](Expressions/pl#Jednostki.md) zawierająca listę wszystkich znanych jednostek.
-   Dokumentacja [Ilość](Quantity.md),
-   Narzędzie [Std\_UnitsCalculator](Std_UnitsCalculator.md)


{{Powerdocnavi

}} 
