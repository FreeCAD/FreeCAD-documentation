# TechDraw Preferences/pl
## Wprowadzenie

Ekran preferencji środowiska pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) znajduje się w [Edytorze preferencji](Preferences_Editor/pl.md). W menu wybierz **Edycja → Preferencje...** a następnie **<img src="images/Workbench_TechDraw.svg" width=16px> Rysunek Techniczny**. Ta grupa jest dostępna tylko gdy środowisko Rysunek Roboczy zostało załadowane podczas bieżącej sesji programu FreeCAD.

Dostępnych jest siedem stron: [Ogólne](#General/pl.md), [Skala](#Scale/pl.md), [Wymiarowanie](#Dimensions/pl.md), [Adnotacja](#Annotation/pl.md), [Kolory](#Colors/pl.md), [HLR](#HLR/pl.md) and [Zaawansowane](#Advanced/pl.md).

Wszystkie preferencje z etykietami pisanymi *kursywą* są wartościami domyślnymi dla nowo tworzonych obiektów rysunku. Nie mają one żadnego wpływu na już istniejące obiekty.

Ta strona została zaktualizowana do wersji 1.0.



## Ogólne

<img alt="Ogólne preferencje" src=images/Preferences_TechDraw_Page_General.png  style="width:350px;">



#### Aktualizacje rysunków 

-   **Aktualizuj za widokiem 3D (polityka globalna)**: *Czy strony są aktualizowane przy każdej zmianie modelu 3D*.
-   **Zezwalaj na zastępowanie strony (polityka globalna)**: *Czy strony [są aktualizowane](TechDraw_PageDefault/pl#Właściwości.md) przy każdej zmianie modelu 3D*.
-   **Aktualizuj stronę na bieżąco**: Utrzymuje strony rysunku w synchronizacji z modelem 3D w czasie rzeczywistym. Może to spowolnić czas odpowiedzi.
-   **Automatycznie rozmieszczaj widoki dodatkowe**: Automatyczne rozprowadzenie widoków pomocniczych dla [grupy rzutów](TechDraw_ProjectionGroup/pl.md).



### Etykiety

-   **Czcionka etykiety**: Nazwa domyślnej czcionki etykiet. Czcionka ta jest również używana dla nowych [wymiarów](#Wymiary.md), zmiana jej nie ma wpływu na wymiary już istniejące.
-   **Rozmiar etykiety**: Domyślny rozmiar tekstu etykiety.



### Zasady

-   **Grupa kąt projekcji**: [Grupa rzutów](TechDraw_ProjectionGroup/pl.md) będzie używać projekcji pierwszego *(standard europejski)* lub trzeciego *(standard amerykański)* kąta. Wyjaśnienie znajduje się na stronie [rzut wielu widoków](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews).
-   **Ukryta linia**: Styl *(ciągła, przerywana, itp.)* do zastosowania w ukrytych liniach.
-   **Wybór linii przekroju**: Standard dla linii sekcji, który kontroluje pozycję strzałek i symboli ({{Version/pl|1.0}}). Dostępne opcje to:
    -   *ANSI*
    -   *ISO*



### Plik

-   **Szablon domyślny**: Domyślny plik [szablonu](TechDraw_Templates.md) dla nowych stron.
-   **Katalog szablonów**: Katalog startowy dla przycisku narzędzia **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Wstaw nową stronę za pomocą szablonu](TechDraw_PageTemplate.md)**.
-   **Plik obrazka kreskowania**: Domyślnie [SVG](SVG.md) lub [bitmapa](bitmap.md) dla pliku **<img src="images/TechDraw_Hatch.svg" width=16px> [Kreskowanie powierzchni za pomocą pliku graficznego](TechDraw_Hatch.md)**.
-   **Plik grupy linii**: Alternatywny plik dla osobistych definicji [LineGroup](TechDraw_LineGroup.md).
-   **Katalog spawalniczy**: Domyślny katalog dla przycisku narzędzia **[<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Symboli spawalniczych](TechDraw_WeldSymbol.md)**.
-   **Plik PAT**: Domyślny plik definicji wzoru PAT dla **<img src="images/TechDraw_GeometricHatch.svg" width=16px> [Kreskowanie powierzchni za pomocą pliku graficznego](TechDraw_GeometricHatch.md)**.
-   **Nazwa wzoru**: Nazwa domyślnego wzoru PAT.
-   **Katalog symboli**: Alternatywna ścieżka do poszukiwania plików symboli SCG.



### Siatka

-   **Pokaż siatkę**: Domyślne ustawienie pokazywania siatki dla nowych stron. {{Version/pl|0.20}}
-   **Odstępy między liniami siatki**: Domyślna odległość między liniami siatki dla nowych stron. {{Version/pl|0.20}}



### Wybieranie

-   **Włącz tryb wielokrotnego wyboru**: Jeśli funkcja ta jest włączona, kliknięcie bez **Ctrl** nie usuwa istniejącego zaznaczenia. {{Version/pl|1.0}}



### Widoki domyślne 

-   **Użycie kierunku kamery 3D**: Jeśli zaznaczone, kierunek kamery 3d (lub kierunek normalny do wskazanej ściany) zostanie użyty jako kierunek widoku. Jeśli niezaznaczone, widoki będą tworzone jako widoki od przodu. {{Version/pl|1.0}}
-   **Zawsze pokazuj etykietę**: Jeśli zaznaczone, etykiety widoków będą wyświetlane nawet gdy ramki są wygaszone. {{Version/pl|1.0}}



### Przyciąganie

-   **Przyciąganie wyrównania widoku**: Jeśli zaznaczone, widoki będą przyciągane do wyrównania podczas ich przeciągania kursorem. {{Version/pl|1.0}}
-   **Współczynnik przyciągania widoków**: Tolerancja dla przyciągania widoków - jeśli widok jest w tym ułamku rozmiaru widoku do idealnego wyrównania, zostanie przyciągnięty do wyrównania. {{Version/pl|1.0}}



## Skala

<img alt="Preferencje skali" src=images/Preferences_TechDraw_Page_Scale.png  style="width:350px;">



### Skala 

-   **Skala strony**: Domyślna skala dla nowych stron.
-   **Wyświetl typ skali**: Domyślna skala dla nowych widoków.
-   **Wyświetl niestandardową skalę**: Domyślna skala dla widoków, jeśli opcja **Wyświetl typ skali** jest ustawiona na **Niestandardowa**.



### Dostosowanie rozmiaru 

-   **Vertex Scale**: Rozmiar punktu [wierzchołka](Glossary#V.md). Mnożnik szerokości linii.
-   **Center Mark Scale**: Rozmiar znaków środków. Mnożnik rozmiaru wierzchołka.
-   **Template Edit Mark**: Rozmiar [szablonu](TechDraw_Templates.md) pola uchwytu do klikania w mm *(zielone kropki)*.
-   **Skala symboli spawalniczych**: Mnożnik dla rozmiaru [symbolu spawalniczego](TechDraw_WeldSymbol.md).



## Wymiary

<img alt="Preferencje wymiarów" src=images/Preferences_TechDraw_Page_Dimensions.png  style="width:350px;">



### Wymiary 

-   **Standard i wygląd**: Norma stosowana dla wartości wymiarów. Różnica pomiędzy standardami przedstawiona jest na zdjęciu: ![\|500px\|Różnice pomiędzy wspieranymi normami. *([źródło ilustracji](images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))*](TechDraw_Dimension_standardization.png )

:   

    :   ISO Oriented - narysowany zgodnie z normą ISO 129-1, tekst jest obracany tak, aby był równoległy do stycznej linii wymiarowej.
    :   ISO Referencing - narysowany zgodnie z normą ISO 129-1, tekst jest zawsze poziomy, umieszczony powyżej najkrótszej możliwej linii odniesienia.
    :   ASME Inlined - sporządzony zgodnie z normą ASME Y14.5M, tekst jest poziomy, wstawiony w przerwę w linii wymiarowej lub łuku.
    :   ASME Referencing - sporządzony zgodnie z ASME Y14.5M, tekst jest poziomy, krótka linia odniesienia jest przymocowana do pionowego środka jednej strony.

-   **Zastosuj wartości globalne dla liczby miejsc dziesiętnych**: użyj liczby miejsc po przecinku z opcji [preferencje ogólne](Preferences_Editor/pl#Jednostki.md).
-   **Pokaż jednostki**: do wartości należy dołączyć specyfikację jednostek (mm, in, itp.).
-   **Alternatywne miejsca dziesiętne**: Liczba miejsc dziesiętnych, jeżeli nie wybrano opcji *Użyj globalnych ustawień odnośnie liczb miejsc po przecinku* i nie określono opcji *Format wymiaru*.
-   **Format wymiaru**: Format własny dla tekstu wymiarowego. Wykorzystuje specyfikację formatu [printf](https://en.wikipedia.org/wiki/Printf_format_string).
-   **Rozmiar czcionki**: rozmiar tekstu dla tekstu wymiarów.
-   **Skala tekstu tolerancji**: Ustawienie wielkości czcionki tolerancji. Mnożnik wymiaru **Rozmiar czcionki**.
-   **Symbol średnicy**: wymiary średnicy będą poprzedzone tym symbolem.
-   **Styl strzałki**: wybierz preferowany znacznik zakończenia linii wymiarowej.
-   **Rozmiar strzałki**: rozmiar znacznika końcowego w mm.
-   **Format Spec**: formatuje tekst wymiarowy. Używa [specyfikator formatu printf](https://en.wikipedia.org/wiki/Printf_format_string).
-   **Współczynnik zwiększenia odstępu - ISO**: Odstęp między punktem wymiarowym a początkiem linii pomocniczych dla wymiarów ISO. {{Version/pl|0.21}}
-   **Współczynnik zwiększenia odstępu - ASME**: Odstęp pomiędzy punktem wymiarowym a początkiem linii pomocniczych dla wymiarów ASME. {{Version/pl|0.21}}
-   **Odstępy między wierszami - ISO**: Odstępy między wierszem wymiaru a tekstem wymiaru dla wymiarów ISO. {{Version/pl|0.21}}.



### Narzędzia

-   **Narzędzie wymiarowania**: Wybierz rodzaj narzędzi wymiarowania dla paska narzędzi. Niezależnie od tego wyboru, wszystkie narzędzia są zawsze dostępne w menu i poprzez skróty. Opcje: {{Version/pl|1.0}}
    -   *Narzędzie pojedyncze*: [Jedno narzędzie](TechDraw_Dimension/pl.md) dla całego wymiarowania na pasku: Odległość, Odległość X / Y, Kąt, Promień. Pozostałe na liście rozwijanej.
    -   *Narzędzia oddzielne*: Pojedyncze narzędzia dla każdego typu wymiarowania.
    -   *Obydwa*: Zarówno \'Narzędzie pojedyncze\', jak i oddzielne narzędzia.
-   **Narzędzie wymiarowania w trybie średnicy / promienia**: Używając narzędzia [Wymiar](TechDraw_Dimension/pl.md) możesz wybrać jak chcesz wymiarować okręgi i łuki: {{Version/pl|1.0}}
    -   *Automatycznie*: Narzędzie będzie wymiarować promienie dla łuków i średnice dla okręgów.
    -   *Średnica*: Narzędzie będzie zawsze wymiarować średnice.
    -   *Promień*: Narzędzie będzie zawsze wymiarować promienie.



## Adnotacja

<img alt="Preferencje adnotacji" src=images/Preferences_TechDraw_Page_Annotation.png  style="width:350px;">



### Adnotacja 

-   **Powierzchnia cięcia przekroju**: Styl dla powierzchni cięcia przekroju. Dostępne są następujące opcje:
    -   *Ukryj*: Nie ma żadnej widocznej powierzchni.
    -   *Barwa bryły*: Obszar otrzymuje zestaw kolorów dla **Powierzchni przekroju**.
    -   *Kreskowanie SVG*: Powierzchnia jest [zakreskowana](TechDraw_Hatch/pl.md).
    -   *Kreskowanie PAT*: Powierzchnia jest [zakreskowana geometrycznie](TechDraw_GeometricHatch/pl.md).
-   **Pokaż linię przekroju w widoku źródłowym**: Jeśli zaznaczone, adnotacje przekrojów będą rysowane na widoku źródłowym. Jeśli odznaczone, na widoku źródłowym nie będzie linii przekroju, strzałek ani symboli. {{Version/pl|1.0}}
-   **Uwzględnij linię cięcia w adnotacji przekroju**: Jeśli zaznaczone, linia cięcia będzie rysowana na widoku źródłowym. Jeśli odznaczone, tylko znaczniki zmian, strzałki i symbole będą wyświetlane. {{Version/pl|1.0}}
-   **Znaczniki linii przekroju złożonego**: Pokaż znaki przy zmianach kierunku na liniach [przekroju złożonego](TechDraw_ComplexSection/pl.md). {{Version/pl|0.21}}
-   **Kształt konturu dla widoku szczegółów**: Kształt konturu dla [widoków szczegółów](TechDraw_DetailView.md). Dostępne opcje to:
    -   *Okrąg*
    -   *Kwadrat*
-   **Widok szczegółów pokazuje dopasowanie**: To pole wyboru kontroluje, czy wokół widoku szczegółowego ma być wyświetlany kontur. {{Version/pl|1.0}}.
-   **Pokaż podświetlenie źródła szczegółów**: To pole wyboru określa, czy wokół obszaru szczegółu w widoku źródłowym szczegółu ma być wyświetlane podświetlenie. {{Version/pl|1.0}}.
-   **Kształt dymka**: Domyślny styl zakończenia linii prowadzącej dymka, patrz [właściwości dymka](TechDraw_Balloon/pl#Właściwości.md).
-   **Koniec linii prowadzącej balonika**: Domyślny styl końców linii prowadzącej balonika.
-   **Długość zagięcia linii dymka**: Długość zagięcia linii prowadzącej balon.
-   **Trójkąt prostokątny balonika**: Jeśli *Zakończenie linii odniesienia balonika* ma postać *wypełnionego trójkąta*, trójkąt może uzyskać kierunek pionowy lub poziomy podczas przesuwania balonika.
-   **Automatyczne poziomowanie linii wiodącej**: Wymusza, aby ostatni segment [linii wiodącej](TechDraw_LeaderLine/pl.md) był poziomy.
-   **Typ widoku z przerwaniem**: Domyślny typ przerwania używany do oznaczania [widoków przerywanych](TechDraw_BrokenView/pl.md): <small>(v1.0)</small> 
    -   *Brak linii przerywanej*
    -   *Linia zygzak*
    -   *Linia pojedyncza*
-   **Pokaż znaki środka**: Umieszczaj znaki środka łuku w widoku.
-   **Drukuj znaki środka**: Umieszczaj znaki środka łuku na wydruku.



### Linie

-   **Standard linii**: Standard używany do rysowania linii przekroju w [widoku przekroju](TechDraw_SectionView/pl.md).
-   **Szerokość linii w grupie**: [LineGroup](TechDraw_LineGroup/pl.md) do ustawiania domyślnych szerokości linii.
-   **Styl ukrytej linii**: Styl ukrytych linii. {{Version/pl|1.0}}.
-   **Styl linii przekroju**: Styl linii sekcji.
-   **Styl podświetlenia szczegółu**: Styl linii kształtu konturu dla [widoki szczegółów](TechDraw_DetailView/pl.md).
-   **Styl linii środkowej**: Domyślny styl dla [linii środkowych](TechDraw_FaceCenterLine/pl.md).
-   **Styl linii przerywanej**: Domyślny styl dla linii używanych do oznaczania [widoków przerwania](TechDraw_BrokenView/pl.md). {{Version/pl|1.0}}
-   **Kształt elementu zakończenia linii**: Domyślny *(okrągły)* powinien być prawie zawsze właściwym wyborem. Płaskie lub kwadratowe nakładki są przydatne, jeśli planujesz użyć rysunku jako prowadnicy cięcia 1:1



## Kolory

<img alt="Preferencje kolorów" src=images/Preferences_TechDraw_Page_Colors.png  style="width:350px;">

Ustawienie domyślnych kolorów dla nowo utworzonych stron:

-   **Normalny**: Standardowy kolor linii.
-   **Wskazany**: Kolor wyboru wstępnego. Kolor, który jest używany do podświetlania obiektów po wskazaniu ich kursorem myszki.
-   **Wybrany**: Kolor dla wybranych obiektów.
-   **Tło**: Kolor tła strony.
-   **Wymiary**: Kolor linii wymiarowych i tekstu.
-   **Linia środka**: Kolor dla [linii środkowych](TechDraw_FaceCenterLine/pl.md).
-   **Podświetlenie szczegółu**: Kolor linii dla konturów [widoku szczegółu](TechDraw_DetailView/pl.md).
-   **Kolor siatki**: Kolor wszystkich siatek na stronie. {{Version/pl|0.20}}
-   **Szablon podkreślenia**: Kolor podkreślenia oznaczającego edytowalne teksty w szablonach. <small>(v1.0)</small> .
-   **Ukryta linia**: Kolor ukrytej linii. Kolor ten będzie używany do wszystkich rodzajów [ukrytych linii](#HLR_Parameters.md).
-   **Powierzchnia przekroju**: Kolor dla powierzchni przecięcia w [widoku przekroju](TechDraw_SectionView/pl.md). Stosuje się tylko wtedy, gdy opcja *Section Cut Surface* jest ustawiona na *Solid Color*.
-   **Linia przekroju**: Kolor dla linii ciecia w [widoku przekroju](TechDraw_SectionView/pl.md).
-   **Kreskowanie**: Kolor dla linii [kreskowania](TechDraw_Hatch.md).
-   **Wypełnienie wzorem**: Kolor wypełnienia dla [wzoru wypełnienia](TechDraw_GeometricHatch/pl.md).
-   **Wierzchołek**: Kolor wybieranego [wierzchołka](Glossary#V.md).
-   **Linia główna**: Kolor dla [linii głównych](TechDraw_LeaderLine/pl.md).
-   **Przezroczystość ścian**: Jeśli opcja zostanie zaznaczona, powierzchnie obiektów będą przezroczyste. W przeciwnym razie ustawiony kolor zostanie użyty jako kolor powierzchni.
-   **Jasne na ciemnym**: Jeśli opcja jest zaznaczona, tekst i linie będą miały jasny kolor. Używane, jeśli **Kolor strony** jest ciemny. W przypadku tej opcji zalecane są przezroczyste lub jasne ściany. {{Version/pl|0.21}}
-   **Monochromatyczny**: Jeśli zaznaczone, ustawiony kolor będzie używany dla całego tekstu i linii. {{Version/pl|0.21}}
-   **Kolor strony**: Kolor tła strony. {{Version/pl|0.21}}.



## HLR

<img alt="Ustawienia parametrów HLR" src=images/Preferences_TechDraw_Page_HLR.png  style="width:350px;">

HLR oznacza \"usunięcie ukrytej linii\".

-   **Użyj przybliżenia wielokąta**: Używa przybliżenia, aby znaleźć ukryte linie. Jest to szybkie, ale rezultatem jest zbiór krótkich linii prostych.
-   **Pokaż twarde linie**: Pokazuje krawędzie twarde i kontury *(widoczne linie są zawsze pokazane)*.
-   *Pokaż linie ciągłe*\': Pokazuje linie o gładkiej powierzchni. Gładka linia to linia wskazująca zmianę pomiędzy stycznymi powierzchniami, jak przy przejściu z płaskiej powierzchni na wyciągnięcie [1](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Pokaż linie szwu**: Pokazuje linie szwu. Linia szwu to granica pomiędzy powierzchniami stycznymi.
-   **Pokaż linie UV ISO**: Pokazuje linie ISO. ISO oznacza *izoparametryczne*. [Oto opis](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) czym są linie izoparametryczne *(w rzeczywistości krzywe)*.
-   **Licznik ISO**: Liczba linii ISO na krawędzi czołowej.



## Zaawansowane

<img alt="Ustawienia zaawansowane" src=images/Preferences_TechDraw_Page_Advanced.png  style="width:350px;">

-   **Wykrywaj ściany**: Jeśli opcja jest zaznaczona, środowisko pracy Rysunek Techniczny będzie próbować budować powierzchnie przy użyciu segmentów linii zwróconych przez algorytm usuwania ukrytych linii. Powierzchnie muszą być wykrywane w celu użycia [kreskowania](TechDraw_Hatching/pl.md), ale w złożonych modelach może wystąpić strata wydajności.
-   **Raportuj postęp**: Powoduje wyświetlanie komunikatów o postępie podczas budowania geometrii widoku. {{Version/pl|0.21}}
-   **Użyj nowego algorytmu wyszukiwania ścian**: Jeśli opcja jest zaznaczona, nowy algorytm wyszukiwania ścian będzie używany zamiast oryginalnego. {{Version/pl|0.21}}
-   **Automatyczna korekcja odniesień wymiarów**: Jeśli opcja ta jest zaznaczona, po zmianie modelu podejmowana jest próba aktualizacji odniesień wymiarów. {{Version/pl|0.21}}
-   **Pokaż krawędzie przekroju**: Zaznacza granicę przekroju wyciętego w funkcji [wygląd przekroju](TechDraw_SectionView/pl.md).
-   *Operacja złączenia przed przekrojem*: Wykonuje operację złączenia na kształcie wejściowym przed przetwarzaniem widoku przekroju.
-   **Przełącz środowisko pracy przy kliknięciu**: Jeśli zaznaczone, dwukrotne kliknięcie na stronie w drzewie automatycznie przełączy środowisko pracy na Rysunek Techniczny i strona zostanie uwidoczniona. {{Version/pl|1.1}}
-   **Obszar krawędzi**: Rozmiar obszaru zaznaczenia wokół krawędzi. Jednostka rozmycia wynosi około 0,1 mm, w zależności od aktualnego przybliżenia widoku.
-   **Obszar zaznaczenia**: Obszar zaznaczenia wokół znaczników środków. Jednostka rozmycia wynosi około 0,1 mm, w zależności od aktualnego przybliżenia widoku. Domyślną wartością jest 10. Wartości z zakresu 20-30 znacznie ułatwiają zaznaczanie krawędzi. Duże liczby spowodują nakładanie się z innymi elementami rysunku.
-   **Zezwalaj na nieprawidłowe krawędzie**: Zawiera w wynikach krawędzie o nieoczekiwanej geometrii, np. o zerowej długości.
-   **Sprawdzaj kształty**: Jeśli zaznaczone, kształty wejściowe będą sprawdzane pod kątem błędów przed użyciem i nieprawidłowe kształty będą pomijane. Może to być wolniejsze, ale zapobiega crashom. {{Version/pl|1.1}}
-   **Debugowanie przekroju**: Wyświetla wyniki pośrednie podczas przetwarzania widoków przekroju\'\'.
-   **Debudowanie błędnych kształtów**: Jeśli zaznaczone, kształty, które nie przeszły weryfikacji będą zapisywane do plików B-rep do dalszej analizy. {{Version/pl|1.1}}
-   **Debugowanie szczegółu**: Wyniki pośrednie podczas przetwarzania widoku szczegółów.
-   **Przejścia narzędzia do usuwania nakładających się na siebie krawędzi**: Liczba prób usunięcia nakładających się krawędzi zwróconych przez algorytm Hidden Line Removal. Wartość 0 oznacza brak szorowania. Wartości powyżej 2 są zazwyczaj nieproduktywne. Każda próba zwiększa czas wymagany do utworzenia rysunku. {{Version/pl|0.21}}
-   **Max SVG kafelki kreskowania**: Limit płytek SVG o rozmiarze 64x64 pikseli stosowany do zakreskowania pojedynczej powierzchni. Przy dużych skalach można popełnić błąd przy wielu kafelkach SVG, wtedy należy zwiększyć limit kafelków.
-   *Maksymalne segmenty linii kreskowania PAT*: Maksymalna liczba segmentów linii kreskowania stosowana przy kreskowaniu powierzchni o wzorze PAT.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/pl
