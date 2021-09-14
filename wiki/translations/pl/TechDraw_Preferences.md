# TechDraw Preferences/pl







{{TOCright}}

## Wprowadzenie

Ekran preferencji środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) znajduje się w [Edytorze preferencji](Preferences_Editor/pl.md), **Edycja → Preferencje → Rysunek Techniczny**.

Wszystkie ustawienia preferencji z etykietami pisanymi *kursywą* są wartościami domyślnymi dla nowo tworzonych obiektów rysunku. Nie mają one żadnego wpływu na już istniejące obiekty.

## Informacje ogólne 

<img alt="Preferencje ogólne" src=images/TechDraw_PreferencesGeneral.png  style="width:350px;">

#### Aktualizacje rysunków 


{{Version/pl|0.19}}

-   **Aktualizuj z 3D**: *Czy strony są aktualizowane przy każdej zmianie modelu 3D*. To jest globalne ustawienie zasad.
-   **Pozwól na zastąpienie strony**: *Czy strony [są aktualizowane](TechDraw_PageDefault#Properties.md) przy każdej zmianie modelu 3D*. To jest globalne ustawienie zasad.
-   **Aktualizuj stronę na bieżąco**: Utrzymuje strony rysunku w synchronizacji z modelem 3D w czasie rzeczywistym. Może to spowolnić czas odpowiedzi.
-   **Automatyczna alokacja widoków pomocniczych**: Automatyczne rozprowadzenie widoków pomocniczych dla [grupy rzutów](TechDraw_ProjectionGroup.md).

### Etykiety

-   **Czcionka etykiety**: Nazwa domyślnej czcionki etykiet. Czcionka ta jest również używana dla nowych [wymiarów](TechDraw_Preferences/pl#Wymiary.md), zmiana jej nie ma wpływu na wymiary już istniejące.
-   **Rozmiar etykiety**: Domyślny rozmiar tekstu etykiety.

### Zasady

-   **Grupa kąt projekcji**: [Grupa rzutów](TechDraw_ProjectionGroup.md) będzie używać projekcji pierwszego lub trzeciego kąta. Wyjaśnienie znajduje się na stronie [rzut wielu widoków](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews).
-   **Ukryta linia**: Styl *(ciągła, przerywana, itp.)* do zastosowania w ukrytych liniach.

### Plik

-   **Szablon domyślny**: Domyślny plik [szablonu](TechDraw_Templates.md) dla nowych stron.
-   \'\'\' Katalog szablonów \'\'\': Katalog startowy dla przycisku narzędzia **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Wstaw nową stronę za pomocą szablonu](TechDraw_PageTemplate.md)**.
-   **Plik obrazka kreskowania**: Domyślnie [SVG](SVG.md) lub [bitmapa](bitmap.md) dla pliku **<img src="images/TechDraw_Hatch.svg" width=16px> [Kreskowanie powierzchni za pomocą pliku graficznego](TechDraw_Hatch.md)**.
-   **Plik grupy linii**: Alternatywny plik dla osobistych definicji [LineGroup](TechDraw_LineGroup.md).
-   **Katalog spawalniczy**: Domyślny katalog dla przycisku narzędzia **<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Symboli spawalniczych](TechDraw_WeldSymbol.md)**. {{Version/pl|0.19}}
-   **Plik PAT**: Domyślny plik definicji wzoru PAT dla **<img src="images/TechDraw_GeometricHatch.svg" width=16px> [Kreskowanie powierzchni za pomocą pliku graficznego](TechDraw_GeometricHatch.md)**.
-   \'\'\'\' Nazwa wzoru \'\'\': Nazwa domyślnego wzoru PAT.

## Skala

<img alt="Preferencje dotyczące skali" src=images/TechDraw_PreferencesScale.png  style="width:350px;">

### Skala 

-   **Skala strony**: Domyślna skala dla nowych stron.
-   **Wyświetl typ skali**: Domyślna skala dla nowych widoków.
-   **Wyświetl niestandardową skalę**: Domyślna skala dla widoków, jeśli opcja **Wyświetl typ skali** jest ustawiona na **Niestandardowa**.

### Dostosowanie rozmiaru 

-   **Vertex Scale**: Rozmiar punktu [wierzchołka](Glossary#V.md). Mnożnik szerokości linii.
-   **Center Mark Scale**: Rozmiar znaków środków. Mnożnik rozmiaru wierzchołka.
-   **Template Edit Mark**: Rozmiar [szablonu](TechDraw_Templates.md) pola uchwytu do klikania w mm *(zielone kropki)*.
-   **Skala symboli spawalniczych**: Mnożnik dla rozmiaru [symbolu spawalniczego](TechDraw_WeldSymbol.md). {{Version/pl|0.19}}

## Wymiary

<img alt="Preferencje wymiarów" src=images/TechDraw_PreferencesDimensions.png  style="width:350px;">

### Wymiary 

-   **Standard i wygląd**: Norma stosowana dla wartości wymiarów. Różnica pomiędzy standardami przedstawiona jest na zdjęciu: ![\|500px\|Różnice pomiędzy wspieranymi normami. *([źródło ilustracji](images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))*](TechDraw_Dimension_standardization.png )

:   

    :   ISO Oriented - narysowany zgodnie z normą ISO 129-1, tekst jest obracany tak, aby był równoległy do stycznej linii wymiarowej.
    :   ISO Referencing - narysowany zgodnie z normą ISO 129-1, tekst jest zawsze poziomy, umieszczony powyżej najkrótszej możliwej linii odniesienia.
    :   ASME Inlined - sporządzony zgodnie z normą ASME Y14.5M, tekst jest poziomy, wstawiony w przerwę w linii wymiarowej lub łuku.
    :   ASME Referencing - sporządzony zgodnie z ASME Y14.5M, tekst jest poziomy, krótka linia odniesienia jest przymocowana do pionowego środka jednej strony.

-   **Zastosuj wartości globalne dla liczby miejsc dziesiętnych**: użyj liczby miejsc po przecinku z opcji [preferencje ogólne](Preferences_Editor/pl#Jednostki.md).
-   **Pokaż jednostki**: do wartości należy dołączyć specyfikację jednostek (mm, in, itp.).
-   **Alternatywne miejsca dziesiętne**: jeśli opcja Użyj globalnych miejsc dziesiętnych nie jest zaznaczona, należy użyć tej liczby miejsc po przecinku.
-   **Format domyślny**: Format własny dla tekstu wymiarowego. Wykorzystuje specyfikację formatu [printf](https://en.wikipedia.org/wiki/Printf_format_string).
-   **Rozmiar czcionki**: rozmiar tekstu dla tekstu wymiarów.
-   **Skala tekstu tolerancji**: Ustawienie wielkości czcionki tolerancji. Mnożnik wymiaru **[rozmiaru czcionki](TechDraw_Preferences/pl#Wymiary_2.md)**.
-   **Symbol średnicy**: wymiary średnicy będą poprzedzone tym symbolem.
-   **Styl strzałki**: wybierz preferowany znacznik zakończenia linii wymiarowej.
-   **Rozmiar strzałki**: rozmiar znacznika końcowego w mm.\* **Format Spec**: formatuje tekst wymiarowy. Używa [specyfikator formatu printf](https://en.wikipedia.org/wiki/Printf_format_string).

## Adnotacje

<img alt="Preferencje adnotacji" src=images/TechDraw_PreferencesAnnotation.png  style="width:350px;">

-   **Standard linii przekroju**: Wzorzec używany do rysowania linii przekroju w [widoku przekroju](TechDraw_SectionView/pl.md).
-   **Styl linii przekroju**: Styl dla linii przekroju.
-   **Powierzchnia cięcia przekroju**: Styl dla powierzchni cięcia przekroju. Dostępne są następujące opcje: {{Version/pl|0.19}}
    -   *Ukryj*: Nie ma żadnej widocznej powierzchni.
    -   *Barwa bryły*: Obszar otrzymuje zestaw kolorów dla **Powierzchni przekroju**.
    -   *Kreskowanie SVG*: Powierzchnia jest [zakreskowana](TechDraw_Hatch/pl.md).
    -   *Kreskowanie PAT*: Powierzchnia jest [zakreskowana geometrycznie](TechDraw_GeometricHatch.md).
-   **Grupa szerokości linii**: Narzędzie [LineGroup](TechDraw_LineGroup/pl.md) służy do ustawiania domyślnej szerokości linii.
-   **Widok szczegółowy Kształt konturu**: Kształt zarysu dla [widoku szczegółu](TechDraw_DetailView/pl.md).
-   **Styl wybranego detalu**: Styl linii kształtu konturu dla [widoku szczegółów](TechDraw_DetailView/pl.md). {{Version/pl|0.19}}
-   **Styl linii osi**: Domyślny styl dla [linii osi obiektu](TechDraw_FaceCenterLine.md).
-   **Kształt dymka**: Styl domyślny dla [adnotacji w dymku](TechDraw_Balloon.md).
-   **Koniec linii prowadzącej balonika**: Domyślny styl końców linii prowadzącej balonika.
-   **Długość zagięcia linii wiodącej balon**: Długość zagięcia linii prowadzącej balon.
-   **Trójkąt prostokątny balonika**: Jeśli *Zakończenie linii odniesienia balonika* ma postać *wypełnionego trójkąta*, trójkąt może uzyskać kierunek pionowy lub poziomy podczas przesuwania balonika.
-   **Automatyczne poziomowanie linii wiodącej**: Wymusza, aby ostatni segment [linii wiodącej](TechDraw_LeaderLine.md) był poziomy.
-   **Pokaż znaki środka**: Umieszczaj znaki środka łuku w widoku.
-   **Drukuj znaki środka**: Umieszczaj znaki środka łuku na wydruku.

## Kolory

<img alt="Preferencje kolorów" src=images/TechDraw_Preferences_Colors.PNG  style="width:350px;">

Ustawienie domyślnych kolorów dla nowo utworzonych stron:

-   **Normalny**: Standardowy kolor linii.
-   **Wskazany**: Kolor wyboru wstępnego. Kolor, który jest używany do podświetlania obiektów po wskazaniu ich kursorem myszki.
-   **Wybrany**: Kolor dla wybranych obiektów.
-   **Tło**: Kolor tła strony.
-   **Wymiary**: Kolor linii wymiarowych i tekstu.
-   **Linia środka**: Kolor dla [linii środkowych](TechDraw_FaceCenterLine.md).
-   **Podświetlenie szczegółu**: Kolor linii dla konturów [widoku szczegułu](TechDraw_DetailView.md). {{Version/pl|0.19}}
-   **Powierzchnia przezroczysta**: Jeśli opcja zostanie zaznaczona, powierzchnie obiektów będą przezroczyste. W przeciwnym razie ustawiony kolor zostanie użyty jako kolor powierzchni. {{Version/pl|0.19}}
-   **Ukryta linia**: Kolor ukrytej linii. Kolor ten będzie używany do wszystkich rodzajów [ukrytych linii](#HLR_Parameters.md).
-   **Powierzchnia przekroju**: Kolor dla powierzchni przecięcia w [widoku przekroju](TechDraw_SectionView.md). Stosuje się tylko wtedy, gdy opcja *Section Cut Surface* jest ustawiona na *Solid Color*.
-   **Linia przekroju**: Kolor dla linii ciecia w [widoku przekroju](TechDraw_SectionView.md).
-   **Kreskowanie**: Kolor dla linii [kreskowania](TechDraw_Hatch.md).
-   **Wypełnienie wzorem**: Kolor wypełnienia dla [wzoru wypełnienia](TechDraw_GeometricHatch.md).
-   **Wierzchołek**: Kolor wybieranego [wierzchołka](Glossary#V.md).
-   **Linia główna**: Kolor dla [linii głównych](TechDraw_LeaderLine.md).

## HLR

<img alt="Ustawienia parametrów HLR" src=images/TechDraw_PreferencesHLR.png  style="width:350px;">

HLR oznacza \"usunięcie ukrytej linii\".

-   **Użyj przybliżenia wielokąta**: Używa przybliżenia, aby znaleźć ukryte linie. Jest to szybkie, ale rezultatem jest zbiór krótkich linii prostych.
-   **Pokaż twarde linie**: Pokazuje krawędzie twarde i kontury *(widoczne linie są zawsze pokazane)*.
-   *Pokaż linie ciągłe*\': Pokazuje linie o gładkiej powierzchni. Gładka linia to linia wskazująca zmianę pomiędzy stycznymi powierzchniami, jak przy przejściu z płaskiej powierzchni na wyciągnięcie [1](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Pokaż linie szwu**: Pokazuje linie szwu. Linia szwu to granica pomiędzy powierzchniami stycznymi.
-   **Pokaż linie UV ISO**: Pokazuje linie ISO. ISO oznacza *izoparametryczne*. [Oto opis](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) czym są linie izoparametryczne *(w rzeczywistości krzywe)*.
-   **Licznik ISO**: Liczba linii ISO na krawędzi czołowej.

## Zaawansowane

<img alt="Ustawienia zaawansowane" src=images/TechDraw_PreferencesAdvanced.png  style="width:350px;">

-   **Wykryj powierzchnie**: Jeśli opcja jest zaznaczona, TechDraw będzie próbował budować powierzchnie przy użyciu segmentów linii zwróconych przez algorytm usuwania ukrytych linii. Powierzchnie muszą być wykrywane w celu użycia [kreskowania](TechDraw_Hatching.md), ale w złożonych modelach może wystąpić strata wydajności.
-   **Pokaż krawędzie przekroju**: Zaznacza granicę przekroju wyciętego w funkcji [wygląd przekroju](TechDraw_SectionView.md).
-   **Debugowanie sekcji**: Wyświetla wyniki pośrednie podczas przetwarzania widoków przekroju\'\'.
-   *Szczegóły dotyczące debugowania*: Wyniki pośrednie podczas przetwarzania widoku szczegółów
-   **Wykryj zwariowane krawędzie**: Zawiera w wynikach krawędzie o nieoczekiwanej geometrii, np. o zerowej długości.
-   *Bezpiecznik przed przekrojem*: Wykonuje operację z użyciem bezpiecznika na kształcie(-ach) wejściowym(-ych) przed przetwarzaniem widoku przekroju.
-   **Pokaż luźne Geometrie 2D**: Zawiera obiekty 2D w rzutach, np. luźne szkice.
-   **Obszar krawędzi**: Rozmiar obszaru zaznaczenia wokół krawędzi. Jednostka rozmycia wynosi około 0,1 mm, w zależności od aktualnego przybliżenia widoku.
-   **Obszar zaznaczenia**: Obszar zaznaczenia wokół znaczników środków. Jednostka rozmycia wynosi około 0,1 mm, w zależności od aktualnego przybliżenia widoku.
-   **Kształt zakończenia linii**: Ustawienie kształtu zakończenia linii. Wyjaśnienie opcji: <https://doc.qt.io/qt-5/qt.html#PenCapStyle-enum> .
-   **Max SVG kafelki kreskowania**: Limit płytek SVG o rozmiarze 64x64 pikseli stosowany do zakreskowania pojedynczej powierzchni. Przy dużych skalach można popełnić błąd przy wielu kafelkach SVG, wtedy należy zwiększyć limit kafelków.
-   *Maksymalne segmenty linii kreskowania PAT*: Maksymalna liczba segmentów linii kreskowania stosowana przy kreskowaniu powierzchni o wzorze PAT.

## Ustawienia ukryte 

\'\'\'Uwaga: \'\'\' Od wersji **0.19** wszystkie ustawienia są dostępne w menu Preferencje. Poniższe informacje dotyczą tylko wersji FreeCAD starszych niż 0.19:

Niektóre ustawienia preferencji są dostępne tylko poprzez [Edytor parametrów](Std_DlgParameter/pl.md), **Narzędzia → Edycja parametrów**.

### Preferencje/Mod/TechDraw/Dekoracje

-   **CenterMarkScale**: domyślny współczynnik skali dla znaczników środka.
-   **ShowCenterMarks**: domyślnie `True`/`False`.
-   **PrintCenterMarks**: `True`/`False` pokaż znaczniki środka podczas drukowania. {{Version/pl|0.19}}

### Preferencje/Mod/TechDraw/Generalne

-   **DefaultScale**: wstępne ustawienie skali strony {{VersionPlus/pl|0.19}}.
-   **EdgeFuzz**: promień wybierania dla krawędzi.
-   **MarkFuzz**: promień wybierania dla znaczników środka.
-   **SectionFuseFirst**: zabezpiecz obiekty źródłowe przed wykonaniem cięcia przekroju.
-   **EdgeEndCap**: kształt zakończeń krawędzi **0x00** zakończenie płaskie, **0x10** zakończenie kwadratowe, **0x20** zakończenie okrągłe *(Qt::PenCapStyle)* {{VersionPlus/pl|0.19}}.

### Preferencje/Mod/TechDraw/Format

-   **format przekroju**: styl linii przekroju 0-ASME 1-ISO

### Preferencje/Mod/TechDraw/Standardy

-   **WyrównaniePromienia**: Format wymiaru promienia 0-ISO *(wyrównany)* 1-ASME *(jednolity)*.





{{TechDraw Tools navi

}} 

[Category:Preferences](Category:Preferences.md)
