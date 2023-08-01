---
- GuiCommand:
   Name: TechDraw LengthDimension
   Name/pl: Rysunek Techniczny: Wstaw wymiar długości
   MenuLocation: Rysunek Techniczny - Wymiary - Wstaw wymiar długości
   Workbenches: [Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso: [Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md), [Wstaw wymiar pionowy](TechDraw_VerticalDimension/pl.md)
---

# TechDraw LengthDimension/pl



## Opis

Narzędzie **Wstaw wymiar długości** dodaje wymiar liniowy do widoku. Wymiar może być odległością między dwoma punktami, długością prostej krawędzi, prostopadłą odległością między dwiema krawędziami lub prostopadłą odległością między punktem a krawędzią.

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width:220px;"> 
*Wymiar długości pobrany z dwóch punktów.*



## Użycie

1.  Wybierz punkty i / lub krawędzie, które definiują pomiar. Geometria może zostać wybrana w oknie [widoku 3D](3D_view/pl.md) *(pierwsze dwie opcje)* lub na rysunku *(wszystkie opcje)*:
    -   Wybierz dwa punkty.
    -   Wybierz pojedynczą krawędź prostą.
    -   Wybierz dwie krawędzie. Jeśli obie krawędzie są proste, muszą być równoległe. Spowoduje to utworzenie wymiaru prostopadłego, jeśli punkt końcowy jednej z krawędzi ma rzut prostopadły na drugą krawędź *(punkt wynikowy musi leżeć na rzeczywistej krawędzi)*. Jeśli możliwych jest wiele rozwiązań, używany jest punkt końcowy najbliższy rzutowanemu punktowi. Jeśli nie ma prawidłowego rzutowania prostopadłego, wymiar będzie odległością między najbliższymi punktami końcowymi krawędzi.
    -   Wybierz punkt i krawędź. Spowoduje to utworzenie wymiaru prostopadłego, jeśli punkt ma rzut prostopadły na rzeczywistą krawędź. W przeciwnym razie wymiar będzie odległością między punktem a najbliższym punktem końcowym krawędzi.
2.  Jeśli geometria została wybrana w widoku 3D: dodaj prawidłowy widok do zaznaczenia, wybierając go w oknie [widoku 3D](3D_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_LengthDimension.svg" width=16px> '''Wstaw wymiar długości'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_LengthDimension.svg" width=16px> Wstaw wymiar długości**.
4.  Wymiar zostanie dodany do widoku.
5.  Wymiar można przeciągnąć do wybranej pozycji.
6.  W razie potrzeby dodaj tolerancje zgodnie z opisem na stronie [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



### Wyświetlanie pomiarów 3D 

Wymiar będzie początkowo wyświetlał rzutowany pomiar *(tj. taki, jak pokazano na rysunku)*. W razie potrzeby i jeśli wymiar jest oparty na odniesieniach 3D, można go zmienić na rzeczywisty pomiar 3D, zmieniając jego właściwość **Typ pomiaru** na wartość {{Value|True}}. Aby oprzeć wymiar na odniesieniach 3D, wybierz geometrię z okna [widoku 3D](3D_view/pl.md) w czasie tworzenia lub użyj narzędzia <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;">. [Napraw odniesienia do wymiarów](TechDraw_DimensionRepair/pl.md), aby zaktualizować istniejące wymiary.



### Zmiana właściwości 

Aby zmienić właściwości obiektu wymiaru, kliknij go dwukrotnie na rysunku lub w oknie [widoku Drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](#Okno_dialogowe.md):



## Okno dialogowe 

![](images/TechDraw_DimensionDialog.png )

Okno dialogowe wymiaru oferuje następujące ustawienia:



### Tolerancja

-   **W teorii dokładnie**: Jeśli to pole jest zaznaczone, wymiar jest określony jako teoretycznie dokładny. W związku z tym nie powinien mieć żadnych tolerancji. Wymiar będzie wyświetlany z ramką wokół wartości: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">.

-   **Tolerancja symetryczna**: Jeśli to pole jest zaznaczone, tolerancja nadmierna i tolerancja niedostateczna są równe, a zanegowana wartość tolerancji nadmiernej jest używana jako tolerancja niedostateczna. Wyświetlany będzie symbol <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">, w przeciwnym razie będzie to <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-   **Powyżej tolerancji:**: Wielkość, o jaką wymiar może być większy.

-   **Poniżej tolerancji:**: Wielkość, o jaką wymiar może być mniejszy.



### Formatowanie

-   **Określenie formatu**: sposób formatowania wartości wymiaru. Domyślnie specyfikatorem jest {{Value|%.xf}}, gdzie {{Value|x}} to liczba miejsc dziesiętnych. Składnia formatowania znajduje się na stronie [tej strony Wikipedii](https://en.wikipedia.org/wiki/Printf_format_string). Istnieje również dodatkowy format {{Value|%w}}, który wyświetla określoną liczbę cyfr po separatorze dziesiętnym i usuwa końcowe zera. Na przykład {{Value|%.2w}} oznacza, że wypisane zostaną co najwyżej 2 cyfry po przecinku, a końcowe zera zostaną odcięte.

-   **Dowolny tekst**: Jeśli to pole jest zaznaczone, wymiar jest zastępowany zawartością pola \"Określenie formatu\".

-   **Określenie formatu górnej granicy tolerancji:**: Sposób formatowania wartości powyżej tolerancji. Domyślnie specyfikatorem jest {{Value|%.xf}}, gdzie {{Value|x}} to liczba miejsc po przecinku. Składnia formatowania znajduje się na stronie [tej strony Wikipedii](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Określenie formatu dolnej granicy tolerancji:**: Sposób formatowania wartości Poniżej tolerancji. Domyślnie specyfikatorem jest {{Value|%.xf}}, gdzie {{Value|x}} to liczba miejsc po przecinku. Składnia formatowania znajduje się na stronie [tej strony Wikipedii](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Dowolne sformułowanie tolerancji**: Jeśli opcja ta jest zaznaczona, tolerancje są zastępowane zawartością pól **Określenie formatu górnej granicy tolerancji** **Określenie formatu dolnej granicy tolerancji**.



### Styl wyświetlania 

-   **Odwróć groty**: Odwraca kierunek strzałek linii wymiarowej. Domyślnie znajdują się one wewnątrz linii wymiarowej / łuku i są skierowane na zewnątrz.

-   **Kolor**: Barwa dla linii i tekstu.

-   **Rozmiar czcionki**: Określa rozmiar tekstu.

-   **Styl rysunku**: Standard *(i jego styl)*, zgodnie z którym wymiar jest rysowany. Zobacz właściwość [**Standard i styl**](#Widok.md), aby uzyskać szczegółowe informacje.



### Linia

-   **Zastąp kąty**: Jeśli opcja jest zaznaczona, zwykłe kąty dla linii wymiarowej i linii przedłużenia zostaną zastąpione określonymi wartościami.

-   **Kąt linii wymiarowej**: Zastępuje wartość kąta linii wymiarowej względem osi X widoku *(w stopniach)*.

-   **Użyj wartości domyślnych**: Ustaw kąt linii wymiarowej na zwykły kąt.

-   **Użyj z wyboru**: Ustaw kąt linii wymiarowej tak, aby odpowiadał kątowi wybranej krawędzi *(lub 2 wierzchołków)* w widoku.

-   **Kąt linii przedłużenia**: Zastąp wartość kąta linii przedłużenia z osią X widoku *(w stopniach)*.

-   **Użyj wartości domyślnych**: Ustaw kąt linii przedłużającej na zwykły kąt.

-   **Użyj z wyboru**: Ustaw kąt linii rozszerzenia tak, aby odpowiadał kątowi wybranej krawędzi *(lub 2 wierzchołków)* w widoku.



## Ograniczenia

Obiekty wymiarów są podatne na \"[problem z nazewnictwem topologicznym](Topological_naming_problem/pl.md)\". Oznacza to, że jeśli zmodyfikujesz geometrię 3D, ściany i krawędzie modelu mogą zostać wewnętrznie przemianowane. Jeśli wymiar jest dołączony do krawędzi, która jest następnie modyfikowana, wymiar może zostać uszkodzony. Ogólnie rzecz biorąc, nie jest możliwe zsynchronizowanie rzutowanych wymiarów 2D z rzeczywistymi obiektami 3D.

Dlatego zaleca się dodawanie wymiarów, gdy model 3D nie jest już modyfikowany.



### Obejście

Jeśli chcesz zachować widok Rysunku Technicznego z wymiarami, które nie ulegną uszkodzeniu, musisz zwymiarować obiekt, który się nie zmieni:

-   Utwórz nieparametryczną kopię obiektu, który chcesz rzutować za pomocą narzędzia <img alt="" src=images/Part_SimpleCopy.svg  style="width:16px;"> [Utwórz prostą kopię](Part_SimpleCopy/pl.md).
-   Wybierz tę kopię, a następnie użyj narzędzia [Wstaw widok](TechDraw_View/pl.md) i dodaj żądane wymiary.
-   Jeśli oryginalny model 3D zostanie zmodyfikowany, modyfikacje nie wpłyną na prostą kopię, ani na wymiary w widoku rysunku technicznego.

Zobacz [Wymiar przestrzenny](TechDraw_LandmarkDimension/pl.md) aby zapoznać się z innym podejściem do ominięcia problemu nazewnictwa topologicznego.



## Uwagi

-   **Wybór krawędzi**. Krawędzie mogą być trudne do zaznaczenia. Obszar zaznaczenia krawędzi można dostosować, zmieniając preferencję [Wykrywanie krawędzi](TechDraw_Preferences/pl#Zaawansowane.md).
-   **Miejsca dziesiętne**. Wymiary domyślnie używają globalnego ustawienia miejsc dziesiętnych. Można to zmienić poprzez [ustawienia](TechDraw_Preferences/pl#Wymiary.md) lub zmieniając właściwość Określenie formatu.
-   **Wiele obiektów**. Widoki mogą zawierać wiele obiektów 3D jako źródło. Wymiary mogą być stosowane do geometrii z dowolnych obiektów w widoku *(np. od Object1.Vertex0 do Object2.Vertex3)*.



## Właściwości



### Dane


{{Properties_Title|Podstawowe}}

-    **Odniesienie 2D|LinkSubList**: Obiekt*(y)* widoku rysunku 2D, na którym oparty jest pomiar. Używane, jeśli parametr **Typ pomiaru** ma wartość {{Value|Projekcja}}.

-    **Odniesienie 3D|LinkSubList**: Obiekt(y) 3D, na których oparty jest pomiar. Używane, jeśli parametr **Typ pomiaru** ma wartość {{True/pl}}.

-    **Typ|Enumeration**: Długość, promień, średnica itp. Zwykle nie są używane przez użytkownika końcowego.

-    **Typ pomiaru|Wyliczenie**: Sposób wykonania pomiaru.

:   

    :   True - w oparciu o geometrię 3D.
    :   Projected - na podstawie rysunku 2D Widok geometrii.

-    **W teorii dokładnie|Bool**: Określa teoretycznie dokładny *(lub podstawowy)* wymiar.

:   

    :   
        {{FALSE/pl}}
        
        \- domyślnie wspólny wymiar, ewentualnie z tolerancjami.

    :   
        {{TRUE/pl}}
        
        \- jest to wartość teoretyczna. Jako taka, nie powinna zawierać żadnych tolerancji. Wymiar będzie wyświetlany w ramce otaczającej wartość: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-    **Tolerancja symetryczna|Bool**: Jeżeli tolerancja nadmiarowa i niedomiarowa są równe. Wtedy zanegowana wartość tolerancji nadmiarowej jest używana jako tolerancja niedomiarowa.

:   

    :   
        {{TRUE/pl}}
        
        \- zanegowana wartość **Powyżej tolerancji:** jest używana jako **Poniżej tolerancji:**. Wyświetlana wartość to <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">.

    :   
        {{FALSE/pl}}
        
        \- the **Poniżej tolerancji:** zostaje wzięty pod uwagę. Wyświetlany będzie <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-    **Powyżej tolerancji|QuantityConstraint**: Wartość, o jaką wymiar może być większy.

-    **Poniżej tolerancji|QuantityConstraint**: Wartość, o jaką wymiar może być mniejszy.

-    **Odwrotny|Bool**: Określa, czy wymiar reprezentuje wartość zwykłą czy odwróconą.

:   

    :   
        `False`
        
        \- używana jest zwykła wartość. Dla długości jest to liczba dodatnia, dla kąta wartość skośna *(0° - 180°)*.

    :   
        `True`
        
        \- używana jest wartość odwrócona. W przypadku długości jest to liczba ujemna, w przypadku kąta wartość odbicia *(180° - 360°)*.

-    **X|Distance**: Poziome położenie tekstu wymiaru względem widoku.

-    **Y|Distance**: Pionowe położenie tekstu wymiaru względem widoku.

-    **Zablokuj pozycję|Bool|Ukryte**: Blokuje pozycję tekstu wymiaru, gdy opcja ta ma wartość `True`.

-    **Obrót|Angle|Ukryte**: Tylko do odczytu.

-    **Typ skali Type|Enumeration|Ukryte**: Tylko do odczytu.

-    **Skala|FloatConstant|Ukryte**: Tylko do odczytu.

-    **Podpis|String|Ukryte**: Nieużywane.


{{Properties_Title|Format}}

-    **Określenie formatu|String**: Sposób formatowania wartości wymiaru. Zobacz [Formatowanie](#Formatowanie.md).

-    **Określenie formatu górnej granicy tolerancji|String**: Podobnie jak **Określenie formatu**, ale dla przekroczenia tolerancji.

-    **Określenie formatu dolnej granicy tolerancji|String**: Jak **Określenie formatu**, ale dla zaniżonych tolerancji.

-    **Dowolny|Bool**: Czy wymiar jest zastępowany zawartością pola **Określenie formatu**.

:   

    :   
        {{FALSE/pl}}
        
        \- zawartość pola **Określenie formatu** jest używana do formatowania rzeczywistej wartości wymiaru.

    :   
        {{TRUE/pl}}
        
        \- zawartość pola **Określenie formatu** będzie wyświetlana jako tekst zamiast wartości wymiaru.

-    **Dowolne sformuowanie tolerancji|Bool**: Podobnie jak **Dowolny**, ale dla tolerancji.


{{Properties_Title|Zastąp}}

-    **Zastąp kąty|Bool**: Czy kierunek linii wymiarowych i przedłużających jest nadpisywany.

:   

    :   
        `False`
        
        \- kierunki są obliczane jak zwykle.

    :   
        `True`
        
        \- kierunki są nadpisywane przez wartości właściwości LineAngle i ExtensionAngle.

-    **Kąt linii|Angle**: kąt linii wymiarowej z osią X widoku *(w stopniach)*.

-    **Kąt linii pomocniczej|Angle**: kąt linii przedłużenia z osią X widoku *(w stopniach)*.


{{Properties_Title|Odniesienia}}

-    **Zapisana geometria|TopoShapeList|Hidden**: Geometria odniesienia. {{Version/pl|0.21}}



### Widok


{{TitleProperty|Podstawa}}

-    **Zachowaj etykietę|Bool**: Nieużywane.

-    **Kolejność na stosie|Integer**: Nakładanie się lub niedopasowanie względem innych obiektów rysunku. {{Version/pl|0.21}}


{{Properties_Title|Format wymiaru}}

-    **Rozmiar grotu|Length**: Rozmiar strzałek wymiaru. {{Version/pl|0.21}}

-    **Kolor|Color**: Kolor linii i tekstu.

-    **Odwróć groty|Bool**: Wartością domyślną jest *wewnątrz* linii wymiarowej / łuku, co oznacza strzałki skierowane *na zewnątrz*. Jeśli strzałki są umieszczone *na zewnątrz* linii wymiarowej/łuku, strzałki są skierowane *do wewnątrz* linii wymiarowej/łuku.

:   

    :   
        {{FALSE/pl}}
        
        \- Umożliwia automatyczne wybieranie kierunku strzałek zgodnie z powyższą regułą.

    :   
        {{TRUE/pl}}
        
        \- Nadpisuje automatycznie wybrany kierunek i wymusza kierunek przeciwny.

-    **Czcionka|Font**: Nazwa czcionki używanej dla tekstu wymiaru.

-    **Rozmiar czcionki|Length**: Określa rozmiar tekstu.

-    **Współczynnik odstępu ASME|Float**: Umożliwia dostosowanie odstępu między punktami wymiaru a początkiem linii rozszerzenia. Wartość odstępu jest pomnożona przez szerokość linii. {{Version/pl|0.21}}

-    **Współczynnik odstępu  ISO|Float**: Umożliwia dostosowanie odstępu między punktami wymiaru a początkiem linii rozszerzenia. Wartość odstępu jest pomnożona przez szerokość linii. {{Version/pl|0.21}}

-    **Współczynnik odstępu między wierszami|Float**: Dostosowuje odstęp między tekstem wymiaru a linią wymiaru. Odstęp jest równy tej wartości pomnożonej przez szerokość linii. {{Version/pl|0.21}}

-    **Szerokość linii|Length**: Określa grubość linii wymiarowej.

-    **Zakres renderowania|Enumeration**: Właściwość raczej uniwersalna określająca ile miejsca może zająć rysunek wymiarowy:

:   

    :   None - żadne linie ani strzałki nie są rysowane, wyświetlana jest tylko sama wartość wymiaru.
    :   Minimal - dla długości i kątów rysowana jest pojedyncza linia łącząca wartość wymiaru i wirtualną linię przedłużenia punktu końcowego. Sama linia pomocnicza nie jest dodawana.
    :   Średnice są renderowane w zgodnie z zakresem Confined, promienie następujące po Reduced zasięgu.
    :   Confined -dla długości i kątów rysowana jest dwukierunkowa linia *(lub łuk)* łącząca \"wirtualne linie pomocnicze\" punktu początkowego i końcowego, chociaż same linie pomocnicze nie są dodawane.

Średnice są rysowane za pomocą minimalnej pojedynczej linii od wartości wymiaru do najbliższego punktu na okręgu, promienie jak w przypadku Reduced.

:   

    :   Reduced - dla długości i kątów rysowana jest pojedyncza linia łącząca wartość wymiarową i linię przedłużenia punktu końcowego wraz z samą linią przedłużenia.
    :   Średnice są rysowane za pomocą linii pojedynczej od środka do najbliższego punktu na okręgu, promienie za pomocą minimalnej linii pojedynczej od wartości wymiarowej do najbliższego punktu łuku.
    :   Normal - jest to wartość domyślna. Dla długości i kątów rysowana jest podwójna linia *(lub łuk)* łącząca \"linie przedłużające\" punktu początkowego i końcowego, a także same linie przedłużające.
    :   Średnice są rysowane jako podwójne linie przechodzące przez środek i łączące najbliższe i najdalsze punkty na okręgu.
    :   Promienie są rysowane jako pojedyncza linia prowadząca od środka do najbliższego punktu łuku.
    :   Expanded - Tylko średnice obsługują tę wartość, renderując je w sposób podobny do długości w poziomie lub w pionie. Inne typy wymiarów są renderowane jak w przypadku zakresu Normal.

-    **Standard i styl|Enumeration**: Określa standard *(i jego styl)*, zgodnie z którym wymiar jest rysowany:

:   

    :   <img alt="Różnice między obsługiwanymi standardami" src=images/TechDraw_Dimension_standardization.png  style="width:500px;">
    :   ISO Oriented - obiekty są rysowane zgodnie z normą ISO 129-1, tekst jest obrócony tak, aby był równoległy do stycznej linii wymiarowej.
    :   ISO Referencing - obiekty są rysowane zgodnie z normą ISO 129-1, tekst jest zawsze poziomy, nad najkrótszą możliwą linią odniesienia.
    :   ASME Inlined - obiekty są rysowane zgodnie ze standardem ASME Y14.5M, tekst jest poziomy, wstawiany w przerwie w obrębie linii wymiarowej lub łuku.
    :   ASME Referencing - obiekty są rysowane zgodnie z ASME Y14.5M, tekst jest poziomy, krótka linia odniesienia jest dołączona do pionowego środka jednej strony.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wymiar długości** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Distance"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LengthDimension/pl
