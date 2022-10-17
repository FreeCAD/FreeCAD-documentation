# Flamingo Workbench/pl
**Środowisko pracy Flamingo (Python2/Qt4) zostało zastąpione przez środowisko pracy Dodo (Python3/Qt5). Ta strona wiki przedstawia różnice między tymi dwoma środowiskami. Obecnie [środowisko pracy Dodo](Dodo_Workbench/pl.md) odnosi się do tej strony.**

## Wprowadzenie

Jest to zestaw dostosowanych poleceń i obiektów programu FreeCAD, które pomagają przyspieszyć rysowanie ram i rurociągów.



   *   \"**Flamingo** jest przeznaczony dla wersji używających środowiska Python \> 2.7 i zestawu narzędzi Qt4.





   *   \"**Dodo** jest przeznaczony dla wersji używających środowiska Python \> 3.6 i zestawu narzędzi Qt5.



Dla wygody narzędzia Flamingo / Dodo są pogrupowane w trzy paski narzędziowe/menu + jeden zestaw narzędzi.

![](images/flamingoBlob.png )

![](images/dodoBlob.png )

-   **Narzędzia ram**   * służą do rozmieszczania ram, kratownic i podobnych elementów w programie FreeCAD przy użyciu obiektów Konstrukcji modułu Arch. \.../flamingo/tutorial/tutorialFrame.pdf
-   **Narzędzia rur**   * to logiczna kontynuacja narzędzia ram, ponieważ zajmuje się tworzeniem rurociągów i konstrukcji rurowych. Posiada również własne klasy Python do tworzenia obiektów rurociągów, takich jak rury, kolanka, kołnierze itp. \.../flamingo/tutorials/tutorialPype2.pdf
-   **Narzędzia Eagle**   * to w zasadzie dodatek i skrót do bardzo profesjonalnego programu [FreeCAD-PCB](https   *//github.com/marmni/FreeCAD-PCB) *(dostępnego także w repozytorium dodatków programu FreeCAD)* do importowania pozycji obiektów z pliku .brd programu Eagle na płytce drukowanej narysowanej w programie FreeCAD za pomocą programu a.m., odnoszący się tylko do ich nazw. Jest to także początek, a właściwie nazwa całego środowiska pracy. \.../flamingo/tutorial/tutorialEagle.pdf

   ** Pasek narzędzi **Przybory** umożliwia wyszukiwanie obiektów w modelu i ich odległości, przesuwanie / obracanie płaszczyzny roboczej oraz mały hack okna dialogowego [Linia łamana](Draft_Wire/pl.md) środowiska Rysunek Roboczy, który pozwala na zmianę położenia płaszczyzny roboczej w locie.

## Bibliografia

-   Autor   * oddtopus
-   Kod źródłowy na platformie GitHub   *

<https   *//github.com/oddtopus/flamingo>

<https   *//github.com/oddtopus/dodo>

## Instalacja

To środowisko pracy może być zainstalowane z <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md). Aby zainstalować je samodzielnie zobacz stronę [Instalacja zewnętrznych środowisk pracy](Installing_more_workbenches/pl.md).

## Narzędzia do ram 


<div class="center" style="width   * auto; margin-left   * auto; margin-right   * auto;">

![](images/Flamingos_frame2.jpg )


</div>


   *   1\) Umieść jedną belkę na jednej krawędzi *(klasa frameIt)*

W przypadku obiektu belki i krawędzi w modelu narzędzie to nakłada belkę na krawędź, zaznaczając je kolejno aż do naciśnięcia klawisza **ESC**.

   *   2\) Wypełnij ramę *(klasa fillFrame)*

Okno dialogowe służące do tworzenia na wielu krawędziach zaznaczonych w rzucie belek o typie wybranym wcześniej, spośród tych występujących w modelu.

Za pomocą przycisku **Wybierz** można zmienić typ belki.


**Dodo   * ta funkcja została zastąpiona w oknie dialogowym "Wstaw rozgałęzienie ramy" przyciskiem **Dodaj pojedynczy**.**


   *   3\) Wstaw ścieżkę *(klasa insertPath)*.

Narzędzie do tworzenia ciągłego obrysu na ścieżce zdefiniowanej przez krawędzie zaznaczone w rzutni, nawet jeśli nie stykają się one ze sobą, przecinają się w środku lub należą do różnych obiektów. Jedynym ograniczeniem jest istnienie przecięcia dwóch kolejnych krawędzi w kolejności, w jakiej zostały one wybrane. Również linia środkowa otrzymuje właściwości widoku linii środkowej, tj. pomarańczowy kolor i kreskowanie.

   *   4\) Wstaw przekrój *(klasa insertSection)*.

Okno dialogowe do tworzenia zestawu profili, które będą używane w modelu dla obiektu FrameLine.

-   Lista **Przekroje**   * zawiera wszystkie przekroje zdefiniowane w pliku .csv odpowiadającym wybranemu typowi przekroju.
-   Lista **Typy przekrojów**   * typy przekrojów zdefiniowane za pomocą plików .csv znajdujących się w folderze /tables
-   Przycisk **Wstaw**   * tworzy grupę \"Profile_zestaw\", jeśli jeszcze nie istnieje, i dodaje do niej obiekt wybranego profilu.

Inne tabele profili można tworzyć poprzez dodanie odpowiedniego pliku .csv w folderze /tables. Zasady tworzenia i dostosowywania takich tabel są podobne do tych, które obowiązują w przypadku linii rurowych.

Inne profile można szkicować w modelu i przeciągać do grupy \"Profile_zestaw\".

Orientacja dwuteowników może mieć wpływ na odwzorowanie belek.


**Dodo   * zmieniono zakres działania tej funkcji.
W dodo otwiera okno dialogowe, w którym można utworzyć 10 kształtów przekroju belki o niestandardowych wymiarach   *
* kwadrat wydrążony i pełny,
* okrąg wydrążony i pełny,
* T, I, C, L, Z,
* Ω ''(omega)''.
Możliwa jest także zmiana położenia środka lub edycja istniejącego przekroju..**


   *   5\) Menedżer linii ram *(klasa FrameLineManager)*.

Podobnie jak w przypadku obiektów \"linii rur\", jest to okno dialogowe do tworzenia i zmiany właściwości obiektów \"linii ram\".

Podobnie jak powyżej, linie ramy są obiektami, które gromadzą właściwości wspólne dla zestawu belek *(mianowicie przekrój belki)*, które są włączone do wspólnej grupy w drzewie modelu. Posiadają one również opcjonalną właściwość `.Base`, domyślnie ustawioną na wartość `None`, która jest linią środkową belek ramy. Po zdefiniowaniu ścieżki o aliasie .Base *(DWire lub Szkic)* można dodawać inne belki do linii ramy, ale zostaną one usunięte po wywołaniu polecenia **Przerysuj**. W oknie dialogowym dostępne są następujące funkcje   *

-   lista profili belek włączonych wcześniej do modelu przez okno dialogowe \"Wstaw przekroje standardowe\" *(czytaj dalej)*,
-   pole wyboru, aby wybrać aktywną linię ramy spośród już utworzonych lub wartość `nowa`, aby utworzyć nową,
-   pole tekstowe, w którym należy wpisać nazwę tworzonej linii szkieletowej. Jeśli nie zostanie wpisana żadna nazwa lub zostanie wpisane słowo `name`, linia szkieletowa zostanie nazwana domyślnie `Telaio00n`,
-   przycisk **Wstaw**   * tworzy nowy obiekt FrameLine lub dodaje nowe elementy do tego, który został wybrany w polu wyboru, jeśli w aktywnej rzutni zaznaczone są krawędzie,
-   przycisk **Przerysuj**   * tworzy nowe belki i umieszcza je nad wybraną ścieżką. Nowe belki zostaną zebrane wewnątrz grupy FrameLine. Opcja nie tworzy ani nie aktualizuje belek dodanych do linii FrameLine poza zdefiniowaną ścieżką,
-   przycisk **Wyczyść**   * usuwa wszystkie belki w grupie FrameLine. Dotyczy to również belek dodanych do linii FrameLine poza jej zdefiniowaną ścieżką,
-   przycisk **Pobierz ścieżkę**   * przypisuje wybrany dwuteownik do atrybutu Ścieżka obiektu FrameLine,
-   przycisk **Pobierz profil**   * zmienia atrybut Profil obiektu FrameLine na taki, jaki posiada belka wybrana w rzutni lub wybrany z listy,
-   pole wyboru {{CheckBox|TRUE|Kopiuj profil}}   * zaznaczenie tego pola powoduje wygenerowanie nowego obiektu profilu dla każdej belki, aby uniknąć wielokrotnych odniesień w modelu,
-   pole wyboru {{CheckBox|Przesuń do początku}}   * jeśli jest zaznaczone, przesuwa środek masy profilu do początku układu współrzędnych   * dzięki temu linia środkowa belki pokrywa się z punktem środkowym profilu.

Jeśli nazwa obiektu FrameLine zostanie zmieniona, automatycznie zmieni się także nazwa odpowiedniej grupy, ale nie odwrotnie.

   *   6\) Menedżer rozgałęzień ramy

Podobnie jak analogiczna funkcja w menu Rura, jest to kontener dla belek zbudowanych na bazie .Base. Bazą może być linia łamana, szkic lub krawędzie bryły. Gdy baza zostanie zmieniona, pozycja i długość belek również zostaną odpowiednio zmodyfikowane. Możliwe jest przycięcie / wydłużenie belek do dowolnej geometrii oraz obrócenie sekcji wokół linii środkowej za pomocą poleceń dostępnych w oknie dialogowym   * w ten sposób modyfikacje nie zostaną utracone podczas ponownego obliczania dokumentu.

-   **OK** tworzy jedną gałąź ramy nad wybraną geometrią.
-   **Anuluj** zamyka okno dialogowe.
-   pole tekstowe **** umożliwia wprowadzenie własnej nazwy elementu.
-   **Pole wyboru** pozwala określić typ przekroju, który będzie wyświetlany w **polu listy** *(zobacz ../Mod/flamingo/shapes lub ../Mod/dodo/shapez, aby dostosować)*.
-   **Dodaj belki** dodaje jeden element do zaznaczonej krawędzi ramy. Krawędź musi należeć do istniejącej gałęzi ramy.
-   **Usuń belki** usuwa wybraną belkę z odpowiadającej jej krawędzi.
-   **Zmień profil** zmienia profile w ramach. Aby zaznaczyć obramowanie, wystarczy wybrać w obszarze widoku jeden z jego elementów.
-   **Pobierz cele** wybiera geometrię z obszaru widoku do przycięcia / rozciągnięcia belki. Obiekty docelowe mogą nie należeć do żadnej gałęzi ramy.
-   **Przytnij / Wydłuż** zmienia długość wybranych prętów na docelową.
-   **Dodaj pojedynczy** tworzy jedną belkę, o określonej ****, niepołączoną z podstawą na żadnej wybranej krawędzi lub powierzchni.
-   **Przerysuj** odtwarza ramę, usuwając wszystkie przesunięcia i obroty.

Gdy w obszarze widoku zostanie zaznaczona jedna z belek należących do ramy, zostanie wizualnie podświetlony jej TYLNY koniec. Pozwala to na ręczną zmianę przesunięć ogona i głowy oraz obrotu przekroju za pomocą poleceń dostępnych w oknie dialogowym.

   *   7\) Łączenie belek pod kątem 45 stopni *(klasa spinSect)*

Narzędzie do obracania jednego obiektu wokół osi \"Z\" jego kształtu o 45 stopni.

   *   8\) Odwróć orientację *(klasa reverseBeam)*

Narzędzie do obracania jednego obiektu wokół osi \"X\" jego kształtu o 180 stopni. Uwaga   * Jeśli zaznaczona jest jedna krawędź obiektu, jest ona używana jako środek obrotu.

   *   9\) Przesuń belkę *(klasa shiftBeam)*

Okno dialogowe do przesuwania i kopiowania obiektów.

Pola tekstowe **X**, **Y** i **Z** do bezpośredniego wprowadzania wielkości przesunięcia w każdym kierunku.

Pole tekstowe **Wielokrotność** to współczynnik wielokrotności wartości przesunięcia.

Pole tekstowe **Kroki** jest mianownikiem ilości przesunięcia. Używa się go, gdy wartość przeliczenia ma być ujęta w kilku krokach.

Przycisk **Pobierz przemieszczenie** umożliwia określenie wielkości i kierunku przesunięcia na podstawie odległości między wybranymi obiektami *(punktami, krawędziami, ścianami)* lub nawet na podstawie pojedynczej krawędzi. W tym ostatnim przypadku wyświetlana jest zielona strzałka wskazująca kierunek.

**OK**, aby wykonać działanie, oraz **Anuluj**, aby zamknąć okno dialogowe.

   *   13\) Obracanie + dopasowywanie krawędzi *(klasa rotJoin)*

Narzędzie do przesuwania i obracania belek w celu dopasowania dwóch krawędzi. To samo, co powyżej, ale dodatkowo sprawia, że krawędzie są współliniowe.

   *   10\) pivot Belki *(class pivotBeam)*

Okno dialogowe służące do obracania belki lub innego obiektu wokół jednej z jego krawędzi.

**Kąt** - pole tekstowe umożliwiające wprowadzenie wartości obrotu w stopniach.

Przycisk \>\>Odwróć\<\< umożliwia w razie potrzeby obracanie w przeciwnym kierunku.

**OK**, aby wykonać działanie, oraz **Anuluj**, aby zamknąć okno dialogowe.

   *   11\) Zlicuj powierzchnie *(klasa LevelBeam)*

Narzędzie do wyrównywania równoległych powierzchni dwóch obiektów. W rzeczywistości polecenie to przenosi na ten sam poziom, z uwzględnieniem położenia i orientacji pierwszej zaznaczonej powierzchni, środek masy wszystkich zaznaczonych powierzchni. W ten sposób dokonuje przesunięcia obiektów, nawet jeśli ich powierzchnie nie są równoległe.

   *   12\) Wyrównaj krawędzie *(klasa alignEdge)*

Narzędzie do łączenia dwóch równoległych krawędzi. W rzeczywistości polecenie to przesuwa obiekty wzdłuż minimalnej odległości ich wybranej krawędzi od pierwszej. W ten sposób przesuwa obiekt, nawet jeśli krawędzie nie są równoległe, i jest to dobry sposób na umieszczenie obiektów w pożądanym położeniu. Możliwe jest również wybranie dwóch krawędzi tego samego obiektu. Dzięki tej metodzie można szybko przesuwać jeden obiekt o kroki zdefiniowane na jego własnej geometrii.

   *   14\) Wyrównaj kołnierz *(klasa alignFlange)*

Dialog umożliwiający obracanie belek tak, aby ich powierzchnie były równoległe do jednej płaszczyzny odniesienia.

Możliwe jest wstępne wybranie powierzchni odniesienia przed wywołaniem tego polecenia.

Trzy przyciski **XY**, **XZ** i **YZ** umożliwiają bezpośredni wybór orientacji płaszczyzn głównych jako odniesienia.

Można też bezpośrednio wprowadzić nową orientację powierzchni za pomocą trzech współrzędnych wektora normalnej i przycisku **Ustaw normalną**.

   *   15\) Rozciągnij belkę *(klasa stretchBeam)*

Okno dialogowe umożliwiające zmianę długości belek.

W polu tekstowym wpisz nową długość, która zostanie zastosowana do wybranych belek lub rur. W przeciwnym razie przycisk **Pobierz długość** pobiera nową długość z wybranej geometrii *(długość belki lub krawędzi albo odległość między obiektami geometrycznymi)*.

Za pomocą suwaka można zmieniać długość tekstu w polu tekstowym w zakresie od -100% do +100%.

Przyciski **Początek** i **Koniec** pozwalają wybrać stronę belki, która zostanie zmieniona.

   *   16\) Przedłuż belkę *(klasa extend)*.

Dialog umożliwiający przedłużenie jednej belki do jednego wybranego celu.

Jeśli przed wywołaniem tego polecenia zaznaczono wcześniej elementy, pierwszy z nich jest automatycznie wybierany jako obiekt docelowy, a obiekt do niego dołączony jest usuwany z zestawu wyboru. W każdym przypadku możliwa jest zmiana obiektu docelowego za pomocą przycisku **Wybierz**.

   *   17\) Dostosuj kąt nachylenia ramy *(class adjustFrameAngle)*

Narzędzie do ustawiania belek pod kątem prostym w ramach. Aby jak najlepiej zrozumieć działanie tego narzędzia, zapoznaj się z poprzednim samouczkiem.

## Narzędzia do rur 


<div class="center" style="width   * auto; margin-left   * auto; margin-right   * auto;">

![](images/Flamingos_pype2.jpg )


</div>


   *   1\) Wstaw rurę.

Otwiera okno dialogowe do wstawiania rur.

Kombinacja w prawym górnym rogu jest wspólna dla wszystkich okien dialogowych \"Wstaw \...\"   * zawiera listę obiektów linii rurowych zdefiniowanych w bieżącym dokumencie. Za jej pomocą można wybrać, do której linii rurowej przypisać nowo utworzone rury. Można również pozostawić ustawienie , aby obiekt był tworzony w linii głównej modelu części. W lewym górnym rogu wypisana jest aktualnie wybrana klasyfikacja rury, pobrana z pola listy w prawej kolumnie. Wymiary rur dla każdej klasy rur są zdefiniowane w plikach .csv, które można dodawać lub modyfikować, stosując kilka prostych zasad nazewnictwa, w zależności od potrzeb. Krzywe, redukcje itp. mają takie same zasady definiowania swoich tabel wymiarów   * patrz pliki w ../Mod/flamingo/Tabele. Przeczytaj także \"tutorialPype.pdf\", aby dowiedzieć się, jak je dostosować lub utworzyć.

Aby określić położenie i orientację rur, można wybrać następujące opcje   *

-   jedna lub więcej prostych krawędzi
-   jedna lub więcej krawędzi zakrzywionych
-   jeden lub więcej wierzchołków
-   nic; w tym przypadku rura zostanie umieszczona w punkcie początkowym.

Jeśli nie zostanie podana długość, domyślnie jest to 200 jednostek *(wygodna długość w mm)*.

Przycisk **Odwróć** umożliwia obrócenie o 180° ostatnio utworzonej lub aktualnie wybranej rury.

Przycisk **Zastosuj** umożliwia zastosowanie innej długości lub średnicy nominalnej do aktualnie wybranych rur.


**Dodo   * dodano menu kołowe ''(skrót klawiszowy   * "Z")'' do tworzenia obiektów typu "rura"   * ma to na celu szybsze wprowadzanie poprawek do rysunku**


   *   2\) Wstaw łuk.

Otwiera okno dialogowe umożliwiające wstawienie jednego kolanka.

Oprócz widżetów wspólnych z innymi oknami dialogowymi \"Wstaw\...\", przycisk **Przytnij / Przedłuż** umożliwia dostosowanie długości wybranych rur do wybranej krawędzi łuku. Aby określić położenie i orientację, można wybrać następujące opcje   *

-   jeden wierzchołek,
-   jedna krawędź łuku,
-   jedną rurę na jednym z jej końców.

W tym przypadku średnica i grubość łuku zostaną automatycznie dopasowane do średnicy i grubości wybranej rury.

-   para krawędzi, rur lub belek, również nie przylegających do siebie, ale przecinających się.

W tym przypadku właściwości krzywej zostaną automatycznie dopasowane do połączenia dwóch wybranych obiektów. Również wybrane rury zostaną automatycznie przycięte lub przedłużone do krawędzi krzywej

-   nic.

W tym przypadku krzywa zostanie umieszczona w punkcie początkowym. Jeśli nie określono kąta, domyślnie jest to 90 stopni.

   *   3\) Wstaw redukcję.

Otwiera okno dialogowe umożliwiające wstawienie zwężeń koncentrycznych.

Aby określić położenie i orientację, można wybrać następujące opcje   *

-   dwie rury równoległe *(ewentualnie współliniowe)*,
-   jedna rura na jednym z końców,
-   jedna rura,
-   jedna krawędź okręgu,
-   jedna prosta krawędź,
-   jeden wierzchołek,
-   nic *(utworzony w punkcie początkowym)*.

Jeśli zostanie wybrana jedna rura, jej właściwości zostaną zastosowane do redukcji.

Jeśli zostaną wybrane dwie rury, narzędzie spróbuje automatycznie połączyć je za pomocą odpowiedniej średnicy głównej i małej.

   *   4\) Wstaw zaślepkę.

Otwiera okno dialogowe do wstawiania zaślepek.

Aby określić położenie i orientację, można wybrać następujące opcje   *

-   jedna lub więcej krawędzi zakrzywionych *(oś i początek przez środek)*,
-   jeden lub więcej wierzchołków,
-   nic,

Jeśli zostanie wybrana krawędź rury, właściwości zaślepek zostaną automatycznie dopasowane do właściwości rury.

   *   5\) Wstaw zawór.

Utwórz \"obiekt zastępczy\" zaworu z tabeli .csv, jak powyżej. Oprócz wymiaru przesunięcia, jest on ważny, ponieważ definiuje również współczynnik Kv, który będzie używany do obliczania strat ciśnienia za pomocą odpowiedniego narzędzia w menu \"Narzędzia\". Zwróć uwagę, że oznaczenie symbolu zastępczego zmienia się w zależności od typu zaworu, jeśli w jego nazwie znajduje się jedno słowo kluczowe spośród \"ball\", \"butterfly\" lub \"globe\".

   *   6\) Wstaw kołnierz.

Otwiera okno dialogowe do wstawiania kołnierzy. Aby określić położenie i orientację, można wybrać następujące opcje   *

-   jedna lub więcej krawędzi okręgu,
-   jeden lub więcej wierzchołków,
-   nic.

Jeśli zostanie wybrana jedna rura, jej właściwości zostaną zastosowane do kołnierza.

   *   7\) Włóż śrubę w kształcie U.

Otwiera okno dialogowe do wstawienia śruby w kształcie litery U.

Aby określić położenie i orientację, można wybrać następujące opcje   *

-   jedna lub więcej krawędzi okręgu
-   jedna lub więcej rur
-   nic.

Jeśli zostanie wybrana jedna rura, jej właściwości zostaną zastosowane do śruby w kształcie litery U. Ponadto można wybrać umieszczenie śruby w kształcie litery U na jednym z końców lub \"Pośrodku\" rury, zaznaczając odpowiednie pole.

Za pomocą przycisku **Odniesienie do powierzchni** można wybrać powierzchnię podpory, względem której ma być ustawiona oś śruby w kształcie litery U.



*Tylko w **dodo**   * powyższe elementy rurociągów można wstawiać także z dedykowanego menu kołowego*.



   *   8\) Menedżer trasy rur

Przed omówieniem okna dialogowego warto przypomnieć, czym jest obiekt linia rurowa w kontekście środowiska pracy Flamingo.

Obiekt ten reprezentuje kolekcję obiektów \"PType\", które są aktualizowane za pomocą metod zdefiniowanych w samej klasie Python. Obecnie tworzy on, za pomocą metody \"obj.Proxy.update(obj,\[edges\])\", rury i łuki nad podanymi krawędziami i zbiera je w grupę o nazwie zgodnej z etykietą obiektu obj.Label. Dla krzywych stosowany jest standardowy promień gięcia \"3D\" *(tzn. 1,5xO.D.)*. Promień gięcia jest wspólną właściwością obiektu linia rurowa, dlatego można go zmienić, a następnie przerysować. W przypadku zmiany nazwy etykiety obiektu linia rurowa, nazwa jego grupy zostaje odpowiednio zmieniona.

Klasa PypeLine2 ma także opcjonalny atrybut \".Base\", który reprezentuje linię środkową rurociągu   *

-   Jeśli parametr Base ma wartość None, PypeLine2 zachowuje się jak pusty kontener obiektów, z możliwością ich automatycznego grupowania, przypisania jednego koloru i wyodrębnienia listy części.
-   .Base może być linią, szkicem lub dowolnym obiektem, który ma krawędzie w swoim kształcie.
-   Uruchamiając \"obj.Proxy.update(obj)\", bez żadnych \[krawędzi\], klasa próbuje renderować linię rurową *(obiekty Rura i Kolano)* na krawędziach \"obj.Base\"   * dla dobrze zdefiniowanych geometrii prowadzi to zwykle do pożądanego rezultatu. Jeśli podano \[krawędzie\], to rury i łuki będą rysowane wzdłuż nich.
-   Uruchomienie polecenia \"obj.Proxy.purge(obj)\" spowoduje usunięcie z modelu wszystkich rur i kolan należących do danej linii.
-   Należy pamiętać, że obiekt utworzony poza .Base nie zostanie zaktualizowany, gdy .Base zostanie zmienione i rurociąg zostanie narysowany na nowo, a także *(z wyjątkiem rur i łuków)* nie zostanie usunięty, gdy linia rurowa zostanie usunięta.

Tak rozumiane polecenie otwiera okno dialogowe umożliwiające utworzenie lub modyfikację jednego przewodu rurowego.

Okno dialogowe jest bardzo podobne do okna dialogowego wstawiania innych obiektów, które widzieliśmy wcześniej.

Tabele klasyfikacji rur, w których określa się średnicę zewnętrzną i grubość, są takie same jak tabele dla rur *(np. Pipe_SCH-STD.csv)*.

Gdy  znajduje się w kombi i zostanie naciśnięty klawisz **Wstaw**, w dokumencie zostanie utworzony nowy obiekt linii rurowej z odpowiednią grupą.

Jedną linię rurową można utworzyć na trzy sposoby, w zależności od obiektów zaznaczonych w rzutni w momencie naciśnięcia przycisku Wstaw   *

-   nic nie jest zaznaczone. Tworzona jest jedna linia rurowa z właściwością .Base = None i dołączana do swojej grupy z określoną nazwą i kolorem *(lub wartościami domyślnymi)*. Obiekty rurociągów, które mają ją wypełniać, można tworzyć pojedynczo za pomocą poleceń opisanych powyżej lub alternatywnie wybrać linię środkową za pomocą przycisków **Pobierz profil** i **Przerysuj**.
-   Wybrano jeden obiekt linii. Zostaje on automatycznie potraktowany jako Podstawa i przekształcony w Ścieżkę *(pomarańczowa kreska)*, a wzdłuż niego rysowane są rury i łuki.
-   wybrano zestaw krawędzi *(nawet nieprzylegających do siebie, ale mających przecięcia przedłużające ich końce)*. Tworzona jest jedna ścieżka łącząca wszystkie krawędzie *(patrz narzędzie Ścieżka na pasku narzędziowym Ramka)* i przypisywana jako .Baza do nowo utworzonej linii rurowej. Następnie rysowane są na niej rury i łuki w sposób opisany powyżej.

Potem można jeszcze dodać inne obiekty *(takie jak kołnierz, redukcja\...)*, używając odpowiednich poleceń wstawiania opisanych powyżej. Gdy obiekty są tworzone w obrębie linii rurowej, są one automatycznie włączane do odpowiedniej grupy modelu i stosowane są ich wspólne właściwości *(tj. średnica zewnętrzna, grubość, kolor, promień gięcia itd.)*.

Jeśli w modelu znajduje się już co najmniej jeden rurociąg, można go wybrać z pola kombi   * w takim przypadku polecenie Wstaw tworzy rury i łuki w sposób opisany powyżej, ale zamiast tworzyć nowy obiekt linii rurowej, dodaje je do wybranego istniejącego rurociągu. Należy pamiętać, że rurociągi utworzone w ten sposób zostaną usunięte podczas następnego **Przerysowania**.

Funkcje **Pobierz ścieżkę**, *Pobierz profil* i *Kolor* umożliwiają zmianę odpowiednio właściwości .Base, rozmiaru nominalnego i koloru obiektu.

**Przerysuj** - ponowne utworzenie rur i łuków wzdłuż .Bazy *(jeśli jest zdefiniowana)* po każdej modyfikacji ścieżki lub właściwości linii rurowej.

**Lista części** generuje plik .csv z zestawieniem materiałów obiektów rurociągowych wchodzących w skład linii rurowej wybranej w polu wyboru.

   *   9\) Wstaw odgałęzienie rury.

Ten obiekt rurowy zachowuje się jak linia rurowa, z tą różnicą, że jest automatycznie aktualizowany za każdym razem, gdy podstawa *(linia lub obiekt szkicu)* jest modyfikowana   * obejmuje to zmianę położenia, rozciąganie, przesuwanie, dodawanie lub usuwanie krawędzi. Jest on przeznaczony głównie do reprezentowania drugorzędnych gałęzi linii rurowej *(zobacz dedykowany samouczek)*, ale może również działać jako samodzielny obiekt. Jest to ważne zadanie, które pozwala szybko zmieniać układ rur, ale jego wadą jest to, że jego geometria jest bardziej sztywno zdefiniowana. Innymi słowy, rur nie można dzielić ani zmieniać ich rozmiarów niezależnie, ponieważ w końcu zostaną przerysowane na Podstawie. Zmiana średnicy zewnętrznej, grubości lub promienia gięcia odgałęzienia rury będzie dotyczyła wszystkich rur i ich łuków.

10\) Wstaw zbiornik.

[zobacz poradnik część 4 *(1/2)*](Flamingo_Workbench/pl#Odno.C5.9Bniki_internetowe.md)

   *   11\) Wstaw trasę rury

[zobacz poradnik część 4 *(2/2)*](Flamingo_Workbench/pl#Odno.C5.9Bniki_internetowe.md)

   *   12\) Przerwij rurę

Otwiera okno dialogowe, aby przerwać jedną rurę w określonym punkcie, opcjonalnie tworząc szczelinę między końcami dwóch części. Możliwy jest wybór wielokrotny.

W polu tekstowym **Punkt** wpisz długość, na której rura lub rury mają zostać przerwane   * może to być wartość bezwzględna lub tylko procent długości *(cyfra, po której następuje %)*. W niektórych przypadkach szybciej jest zmienić tę wartość za pomocą suwaka znajdującego się na dole.

Przycisk **Długość** pozwala zmierzyć długość wybranej rury i użyć jej jako odniesienia dla skali suwaka.

Jeśli jest to potrzebne tylko do rozdzielenia rur na dwie części, pozostaw pole tekstowe **Odstęp** ustawione na 0. W przeciwnym razie zdefiniuj długość odstępu. Jeśli wybrano długość referencyjną, można również zdefiniować szczelinę jako wartość procentową. Jak pokazano w [poradniku](https   *//github.com/oddtopus/flamingo/blob/master/tutorials), można zmierzyć szczelinę na podstawie geometrii w modelu za pomocą przycisku **Pobierz szczelinę**   * jest to odległość między dowolnymi elementami geometrycznymi lub nawet długość pojedynczej krawędzi.

Naciśnięcie przycisku **Przerwij** powoduje wykonanie akcji.

Przycisk wyboru, jak zwykle, pozwala wybrać grupę, do której mają być przypisane nowo utworzone obiekty.

   *   13\) Zrównaj krawędzie rur.

Gdy zaznaczone są dwie okrągłe krawędzie należące do różnych obiektów, naciśnięcie tego przycisku spowoduje, że drugi obiekt przesunie się, aby krawędzie były współśrodkowe i współpłaszczyznowe.

Funkcja działa nie tylko w przypadku rur.

   *   14\) Połącz rury.

Łączy porty różnych obiektów w sposób graficzny. Działa to tylko między obiektami rurowymi, także z różnych obszarów roboczych, gdzie właściwość Ports\[\] jest zdefiniowana w sposób spójny.

   *   15\) Zamontuj jedno kolanko.

Wybierz 2 przecinające się rury + 1 kolanko   * wykonując to polecenie, zostaną one połączone. Funkcja działa tylko między obiektami rurowymi, także z różnych obszarów roboczych.

   *   16\) Przedłuż rury do skrzyżowania.

Wybierając dwie rury, polecenie to przedłuża je do punktu przecięcia, jeśli taki istnieje.

   *   17\) Przedłuż rurę do skrzyżowania.

Wybierając dwie rury, polecenie to powoduje przedłużenie pierwszej z nich do punktu przecięcia z drugą, jeśli taka istnieje.

   *   18\) Ułóż rury.

Wybierając jedną ścianę i wiele rur, polecenie to powoduje przesunięcie rur wzdłuż normalnej ściany, tak aby leżały na jej płaszczyźnie.

   *   19\) Wznieś podporę.

Podobne do powyższego narzędzia, ale w tym przypadku jest to podpora, która jest podnoszona lub opuszczana, tak aby powierzchnia czołowa była styczna do rury.

   *   20\) Zamocuj do rury.

Przymocowuje na sztywno obiekt rurowy *(2, 3, 4, 5 lub 6)* do najbliższego końca rury *(1)*. Aby odłączyć, kliknij na przycisk, gdy dołączony obiekt jest zaznaczony indywidualnie.

   *   21\) Tworzenie rur punkt-punkt.

Otwiera okno dialogowe podobne do \"Rysuj linię\" wraz z oknem dialogowym \"Wstaw rurę\"   * pozwala to narysować sekwencję rur, połączonych krzywymi, wybierając po prostu jeden punkt za drugim. Można także w locie zmieniać właściwości rury i/lub linii rurowej.

   *   22\) Wstaw dowolny kształt.

Jest to narzędzie do tworzenia obiektu \"rury\" z pliku .STEP, .IGES lub .BREP. Wczytuje ono zaimportowany plik do właściwości Kształt w pliku FeaturePython.

## Narzędzia


<div class="center" style="width   * auto; margin-left   * auto; margin-right   * auto;">

![](images/Flamingos_utils.jpg )


</div>


   *   1\) Utwórz wielokąt.

Pierwsze dwa narzędzia z pakietu narzędzi są częścią osobnego projektu, którego celem jest stworzenie automatycznego skanera pomieszczeń z silnikiem krokowym i ultradźwiękowym miernikiem odległości. To narzędzie tworzy jeden regularny wielokąt wewnątrz szkicu.

   *   2\) Wielokąt z pliku.

Narzędzie do tworzenia dowolnego wielokąta wewnątrz szkicu, pobierając wierzchołki z pliku .csv, w którym są one zapisane w postaci współrzędnych biegunowych.

   *   3\) Tworzenie zapytań do modelu.

Narzędzie do uzyskiwania różnych informacji w zależności od wybranego obiektu lub obiektów. Oprócz długości i odległości, narzędzie to jest szczególnie przydatne do podawania informacji związanych z belkami i rurami *(długość, przekrój, kąt między nimi)*.

   *   4\) Wyrównaj płaszczyznę roboczą.

Narzędzie do ustawiania położenia i obrotu płaszczyzny roboczej zgodnie z wybraną istniejącą geometrią.

Normalna płaszczyzny roboczej jest określona przez skanowanie elementów w następującej kolejności   *

1.  normalna ściany,
2.  normalna płaszczyzny łuku,
3.  normalna płaszczyzny zawierającej dwa odcinki.

Początek płaszczyzny roboczej jest określony *(w kolejności)* przez   *

1.  jeden wierzchołek,
2.  środek krzywizny prostej,
3.  punkt przecięcia dwóch prostych,
4.  środek krawędzi.

   *   5\) Odsunięcie płaszczyzny roboczej.

Odsuwa płaszczyznę roboczą wzdłuż jej wektora normalnego. Aby pokazać kierunek przesunięcia, na ekranie wyświetlana jest tymczasowa zielona strzałka. Wyraźnie widać, że dozwolone są również wartości ujemne.

   *   6\) Obróć płaszczyznę roboczą.

Obraca płaszczyznę roboczą wokół jednej z jej osi. Również w tym przypadku w rzutni wyświetlana jest zielona strzałka określająca aktualną orientację narzędzia Płaszczyzny roboczej   * strzałka jest skierowana w kierunku Z, a długa podstawa strzałki znajduje się w kierunku X.

   *   7\) Narysuj linę.

Narzędzie to działa dokładnie tak samo, jak odpowiadające mu narzędzie w oknie środowiska Rysunek Roboczy, ale z kilkoma dodatkowymi opcjami dostępnymi u dołu okna dialogowego. Domyślnie początek płaszczyzny roboczej jest definiowany na nowo dla każdego dodanego punktu, ponieważ ułatwia to rysowanie odcinków o znanej długości i orientacji przy użyciu opcji przyciągania do siatki. Następnie dwa przyciski, wywoływane również za pomocą skrótu klawiszowego **Ctrl** + **Shift** + **(** **)**, pozwalają obracać i przesuwać płaszczyznę roboczą w sposób widoczny powyżej, bez przerywania pracy obiektu Linii. Ostatnie trzy przyciski pozwalają szybko zmienić obrót płaszczyzny roboczej tak, aby była ona równoległa do płaszczyzn głównych.

   *   8\) Szybkie przesuwanie obiektów.

Aby szybko przesunąć dowolną część, na przykład w celu uzyskania dostępu do obiektów znajdujących się pod nią, narzędzie to udostępnia uchwyt graficzny *(zielona strzałka)*, po kliknięciu którego można przesuwać i obracać wybrane obiekty.

   *   9\) Kalkulator strat ciśnienia.

Otwiera jedno okno dialogowe do obliczania strat ciśnienia na odcinkach rur zaznaczonych w rzutni lub na jednym odgałęzieniu rur. Współczynnik tarcia jest obliczany dla każdej rury prostej i kolana. Dla innych obiektów skupiona strata ciśnienia jest obliczana za pomocą współczynnika przepływu, pod warunkiem że atrybut Kv jest dostępny i ustawiony na wartość dodatnią.

## Odnośniki internetowe 

-   Forum   * [Nowe środowisko pracy dla konstrukcji metalowych](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=17035) *(ogłoszenie)*.
-   Forum   * [środowiska pracy Flamingo & Dodo - dyskusja na forum](https   *//forum.freecadweb.org/viewtopic.php?t=22711)
-   Poradniki   * [flamingo/tutorials](https   *//github.com/oddtopus/flamingo/tree/master/tutorials)

-   Poradniki wideo   *
    -   [Prosty samouczek wideo do tworzenia ram z rur](https   *//www.youtube.com/watch?v=_Or91gdBLMU).
    -   [Część 1   * jak tworzyć linie rur](https   *//www.youtube.com/watch?v=cBj0umlvzAk).
    -   [Część 2   * ramy, podpory, kołnierze i importowane komponenty](https   *//www.youtube.com/watch?v=e81PpWY5L00).
    -   [Część 3   * rysowanie jednego budynku za pomocą czterech szkiców *(i wiele innych funkcji)*](https   *//www.youtube.com/watch?v=IqEccmsg5dU).
    -   [Część 4 (1/2)   * Rozmieszczenie pompowni i plan rurociągów](https   *//www.youtube.com/watch?v=aPF8SS_1Aqo).
    -   [Część 4 (2/2)   * Import pompowni do budynku i trasa rurociągu](https   *//www.youtube.com/watch?v=iGnW88x9bKQ).
-   Zgłaszanie błędów   *
    -   [Flamingo kolejka zgłoszeń GitHub](https   *//github.com/oddtopus/flamingo/issues).
    -   [Dodo kolejka zgłoszeń GitHub](https   *//github.com/oddtopus/dodo/issues).

## Inne użyteczne odnośniki 

-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md)
-   [Przepisy na makropolecenia](Macros_recipes/pl.md)
-   [OSE-Piping-Workbench   * tworzenie dodatkowych złączy rurowych](https   *//wiki.opensourceecology.org/wiki/OSE_Piping_Workbench)

## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https   *//github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Flamingo Workbench/pl
