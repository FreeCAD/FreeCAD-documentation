# <img alt="Ikonka FreeCAD dla Środowiska pracy Arkusz Kalkulacyjny" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/pl

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> **Arkusz Kalkulacyjny** pozwala tworzyć i edytować arkusze kalkulacyjne, używać danych z arkusza kalkulacyjnego jako parametrów w modelu, wypełniać arkusz kalkulacyjny danymi pobranymi z modelu, wykonywać obliczenia i eksportować dane do innych aplikacji arkuszy kalkulacyjnych, takich jak LibreOffice czy Microsoft Excel.




<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Arkusz kalkulacyjny z komórkami wypełnionymi tekstem i ilościami*

## Przybory

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Utwórz arkusz](Spreadsheet_CreateSheet/pl.md): tworzy nowy arkusz kalkulacyjny.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Importuj arkusz](Spreadsheet_Import/pl.md): wczytuje plik CSV do arkusza kalkulacyjnego.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Eksportuj arkusz](Spreadsheet_Export/pl.md): zapisuje pliku CSV na podstawie arkusza kalkulacyjnego.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Scal komórki](Spreadsheet_MergeCells/pl.md): łączy wybrane komórki.

-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Podziel komórkę](Spreadsheet_SplitCell/pl.md): rozdziela poprzednio scalone komórki.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Wyrównaj do lewej](Spreadsheet_AlignLeft/pl.md): wyrównuje treść wybranych komórek do lewej.

-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Wyśrodkuj w poziomie](Spreadsheet_AlignCenter/pl.md): wyrównuje treść wybranych komórek do środka w poziomie.

-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Wyrównaj do prawej](Spreadsheet_AlignRight/pl.md): wyrównuje treść wybranych komórek do prawej.

-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Wyrównaj do góry](Spreadsheet_AlignTop/pl.md): wyrównanie zawartości wybranych komórek w górę.

-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Wyśrodkuj w pionie](Spreadsheet_AlignVCenter/pl.md): wyrównuje treść wybranych komórek do środka w pionie.

-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Wyrównaj w dół](Spreadsheet_AlignBottom/pl.md): wyrównuje treść wybranych komórek do dołu.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Pogrubienie](Spreadsheet_StyleBold/pl.md): ustawia pogrubienie treści wybranych komórek.

-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Kursywa](Spreadsheet_StyleItalic/pl.md): ustawia treść wybranych komórek na kursywę.

-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Podkreślenia](Spreadsheet_StyleUnderline/pl.md): ustawia treść wybranych komórek jako podkreśloną.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Ustaw alias](Spreadsheet_SetAlias/pl.md): ustawia alias dla wybranej komórki.

-   Przyciski **Czarny** oraz **Biały** ustawia kolory czcionki i tła dla wybranych komórek.

## Ustawienia

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width:32px;"> [Ustawienia](Spreadsheet_Preferences/pl.md): preferencje dla środowiska pracy Arkusz Kalkulacyjny. {{Version/pl|0.20}}

## Wstawianie i usuwanie wierszy i kolumn 

Wiersze i kolumny można wstawiać i usuwać, klikając prawym przyciskiem myszy nagłówek wiersza lub kolumny i wybierając odpowiednią opcję z menu podręcznego. Możliwe jest zaznaczenie najpierw wielu wierszy lub kolumn. Można to zrobić, przytrzymując klawisz **Ctrl** podczas zaznaczania nagłówków lub przytrzymując lewy przycisk myszy i przeciągając.

W programie FreeCAD w wersji 0.19 i wcześniejszych wiersze są wstawiane nad zaznaczonymi wierszami, a kolumny po lewej stronie zaznaczonych kolumn. W programie FreeCAD w wersji 0.20 można określić kierunek wstawiania.

Należy pamiętać, że usunięcie wierszy lub kolumn z danymi może spowodować zepsucie arkusza kalkulacyjnego i Twojego modelu, jeśli opiera się on na arkuszu. W takim przypadku użytkownik nie jest ostrzegany.

## Wycinanie i kopiowanie-wklejanie komórek 

W komórkach arkuszy kalkulacyjnych programu FreeCAD można wykonywać operacje wycinania i kopiowania-wklejania. Do tych operacji można używać standardowych skrótów klawiszowych: **Ctrl** + **X**, **Ctrl** + **C** i **Ctrl** + **V**. Aby zaznaczyć wiele komórek, przytrzymaj klawisz **Ctrl** podczas zaznaczania lub przytrzymaj lewy przycisk myszy i przeciągnij, aby zaznaczyć prostokątny zakres komórek.

Operacje wycinania i kopiowania zapisują zawartość i właściwości komórek w Schowku. Operacja wklejania powoduje zapisanie danych w taki sposób, że zawartość lewej górnej komórki zapisanych danych jest umieszczana w aktywnej komórce. Pozostała przechowywana zawartość jest umieszczana względem tej komórki. Formuły są odpowiednio aktualizowane.

Należy pamiętać, że usunięcie komurek z danymi może spowodować zepsucie arkusza kalkulacyjnego i Twojego modelu, jeśli opiera się on na arkuszu. W takim przypadku użytkownik nie jest ostrzegany.

W programie FreeCAD w wersji 0.19 i wcześniejszych występuje błąd, który może powodować zawieszanie się programu FreeCAD, jeśli wklejany jest zakres komórek inny niż prostokątny. Zaleca się zapisanie pracy przed wykonaniem jakichkolwiek operacji wklejania.

## Właściwości komórek 

Właściwości komórki arkusza kalkulacyjnego można edytować, klikając komórkę prawym przyciskiem myszy i wybierając z menu podręcznego polecenie **Właściwości ...**. Zostanie wyświetlone następujące okno dialogowe:

![](images/SpreadsheetCellPropDialog.png )

Zgodnie z informacjami na kartach można zmieniać następujące właściwości:

-   Kolor: kolor tekstu i kolor tła
-   Wyrównanie: wyrównanie tekstu w poziomie i w pionie
-   Styl: styl tekstu: pogrubienie, kursywa, podkreślenie
-   Jednostki: Wyświetl jednostki dla tej komórki. Proszę przeczytać sekcję [Jednostki](#Jednostki.md) poniżej.
-   Alias: Definiuje [alias](Spreadsheet_SetAlias/pl.md) dla tej komórki. Można go używać w formułach komórek, a także w ogólnych [wyrażeniach](Expressions/pl.md). Więcej informacji na ten temat znajduje się w sekcji [Dane arkusza kalkulacyjnego w wyrażeniach](#Dane_arkusza_kalkulacyjnego_w_wyra.C5.BCeniach.md).

## Wyrażenia w komórkach 

Komórka arkusza kalkulacyjnego może zawierać dowolny tekst, cyfry lub wyrażenie. Wyrażenia muszą zaczynać się od znaku równości \"=\".

Wyrażenia komórek mogą zawierać liczby, funkcje, odwołania do innych komórek i odwołania do właściwości modelu *(ale przeczytaj akapit [Obecne ograniczenia](#Obecne_ograniczenia.md) poniżej)*. Do komórek odwołujemy się za pomocą ich adresu utworzonego z indeksu kolumny *(wielka litera)* i wiersza *(liczba)*, np B4, lub przez jej [alias](Spreadsheet_SetAlias/pl.md).

**Uwaga:** Wyrażenia komórek są traktowane przez FreeCAD jak kod programowania. Dlatego podczas edycji zawartości komórki można zauważyć, że nie jest ona zgodna z ustawieniami wyświetlania:

-   Separatorem miejsc dziesiętnych jest zawsze kropka. Ale przy wprowadzaniu wartości można również używać przecinków.
-   Liczba wyświetlanych miejsc po przecinku może się różnić od Twoich [ustawień w preferencjach](Preferences_Editor#Jednostki.md).

Odwołania do obiektów w modelu wyjaśniono w sekcji [Odniesienia do danych CAD](#Odniesienia_do_danych_CAD.md) poniżej. Używanie wartości komórek arkusza kalkulacyjnego do definiowania właściwości modelu wyjaśniono w sekcji [Dane arkusza kalkulacyjnego w wyrażeniach](#Dane_arkusza_kalkulacyjnego_w_wyra.C5.BCeniach.md) poniżej. Więcej informacji na temat wyrażeń i dostępnych funkcji można znaleźć na stronie [Wyrażenia](Expressions/pl.md).

## Interakcja między arkuszami kalkulacyjnymi a modelem CAD 

Dane znajdujące się w komórkach arkusza kalkulacyjnego mogą być wykorzystywane w wyrażeniach parametrów modelu CAD. W ten sposób arkusz kalkulacyjny może być używany jako źródło wartości parametrów używanych w całym modelu, efektywnie gromadząc wartości w jednym miejscu. Gdy wartości są zmieniane w arkuszu kalkulacyjnym, zostają one przekazane do całego modelu.

Podobnie, właściwości obiektów modelu CAD mogą być używane w wyrażeniach w komórkach arkusza kalkulacyjnego. Pozwala to na wykorzystanie w arkuszu kalkulacyjnym właściwości obiektu, takich jak objętość czy powierzchnia. Jeśli nazwa obiektu w modelu CAD zostanie zmieniona, zmiana ta zostanie automatycznie przeniesiona do wszystkich odwołań w wyrażeniach arkusza kalkulacyjnego używających zmienionej nazwy.

W dokumencie może być używany więcej niż jeden arkusz kalkulacyjny. Arkusz kalkulacyjny można zidentyfikować, używając jego nazwy lub etykiety.

FreeCAD automatycznie przypisuje unikalną nazwę do arkusza kalkulacyjnego podczas jego tworzenia. Nazwy te są zgodne z wzorcem `Arkusz kalkulacyjny`, `Arkusz kalkulacyjny001`, `Arkusz kalkulacyjny002` i tak dalej. Nazwy tej nie można zmienić ręcznie i nie jest ona widoczna we właściwościach arkusza kalkulacyjnego. Można jej użyć do odwołania się do arkusza kalkulacyjnego w [wyrażeniach](Expressions/pl.md) *(zobacz sekcję [Dane arkusza kalkulacyjnego w wyrażeniach](#Dane_arkusza_kalkulacyjnego_w_wyra.C5.BCeniach.md) poniżej)*.

Etykieta arkusza kalkulacyjnego jest automatycznie ustawiana na nazwę arkusza podczas jego tworzenia. W przeciwieństwie do nazwy, etykietę można zmienić, np. w panelu właściwości lub za pomocą polecenia **Zmień nazwę** w menu podręcznym. Domyślnie FreeCAD nie akceptuje zduplikowanych etykiet, ale istnieje [preferencja](Preferences_Editor/pl#Dokument.md), aby to zmienić. Do arkuszy kalkulacyjnych ze zduplikowanymi etykietami w tym samym dokumencie nie można odwoływać się za pomocą ich etykiety.

FreeCAD sprawdza, czy nie występują zależności cykliczne. Zobacz sekcję [obecne ograniczenia](#Obecne_ograniczenia.md).

### Odniesienia do danych CAD 

Jak wskazano powyżej, w wyrażeniach arkusza kalkulacyjnego można odwoływać się do danych z modelu CAD.

W poniższej tabeli przedstawiono kilka przykładów przy założeniu, że model ma cechę o nazwie \"MyCube\":

++++
| Dane CAD                                         | Komórka w arkuszu                                        | Rezultat                       |
+==================================================+==========================================================+================================+
| Długość parametryczna sześcianu środowiska Część |                                           | Długość z jednostkami mm       |
|                                                  | {{Incode|<nowiki>=MyCube.Length</nowiki>}}               |                                |
|                                                  |                                                       |                                |
++++
| Objętość sześcianu                               |                                           | Objętość w mm³ bez jednostek   |
|                                                  | {{Incode|<nowiki>=MyCube.Shape.Volume</nowiki>}}         |                                |
|                                                  |                                                       |                                |
++++
| Typ kształtu sześcianu                           |                                           | String: Solid                  |
|                                                  | {{Incode|<nowiki>=MyCube.Shape.ShapeType</nowiki>}}      |                                |
|                                                  |                                                       |                                |
++++
| Etykieta sześcianu                               |                                           | String: MyCube                 |
|                                                  | {{Incode|<nowiki>=MyCube.Label</nowiki>}}                |                                |
|                                                  |                                                       |                                |
++++
| Współrzędna X środka masy sześcianu              |                                           | Współrzędna w mm bez jednostek |
|                                                  | {{Incode|<nowiki>=MyCube.Shape.CenterOfMass.x</nowiki>}} |                                |
|                                                  |                                                       |                                |
++++

### Dane arkusza kalkulacyjnego w wyrażeniach 

Aby użyć danych arkusza kalkulacyjnego w innych częściach programu FreeCAD, zwykle tworzy się [Wyrażenie](Expressions/pl.md), które odnosi się do arkusza kalkulacyjnego i komórki zawierającej dane, których chcesz użyć. Arkusze kalkulacyjne można identyfikować na podstawie nazwy lub etykiety, a komórki na podstawie adresu lub aliasu. Autouzupełnianie jest dostępne dla wszystkich form odwołań.

++++
|                       | Arkusz kalkulacyjny według nazwy                    | Arkusz kalkulacyjny według etykiety                    |
+=======================+=====================================================+========================================================+
| Komórka według adresu |                                      |                                         |
|                       | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                       |                                                  |                                                     |
++++
| Komórka według aliasu |                                      |                                         |
|                       | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                       |                                                  |                                                     |
++++


<div class="mw-collapsible mw-collapsed">

Zalecanym sposobem odwoływania się do danych arkusza kalkulacyjnego jest używanie etykiety arkusza i nazwy aliasu komórki. Bardziej szczegółowe omówienie zalet i wad poszczególnych trybów adresowania znajduje się w rozwiniętej sekcji poniżej.


<div class="mw-collapsible-content">

Użycie etykiety arkusza kalkulacyjnego ma tę zaletę, że można ją dowolnie zmieniać, aby opisywała zawartość arkusza. Łatwiej jest również zidentyfikować używany arkusz kalkulacyjny, ponieważ tekst w wyrażeniu odpowiada etykiecie widocznej w widoku modelu i właściwości. Jeśli zdecydujesz się zmienić etykietę arkusza kalkulacyjnego, istniejące odwołania do zawartości arkusza zostaną zaktualizowane, więc nie zepsujesz swoich wyrażeń, zmieniając nazwę arkusza. Wewnętrzna nazwa arkusza kalkulacyjnego nie jest dostępna nigdzie poza edytorem wyrażeń, więc jeśli użyjesz wewnętrznej nazwy, a później zmienisz nazwę arkusza kalkulacyjnego, możesz mieć problem z odnalezieniem źródła danych wyrażenia.

Pamiętaj, że podczas tworzenia nowego arkusza kalkulacyjnego nazwa i etykieta są takie same, więc łatwo jest przypadkowo użyć nazwy arkusza zamiast etykiety. Prostym sposobem na uniknięcie takiej sytuacji jest nadanie arkuszowi sensownej nazwy przed rozpoczęciem używania go w wyrażeniach.

Chociaż w wyrażeniu można użyć numeru wiersza i kolumny w celu odwołania się do komórki, najlepszą praktyką jest nadanie komórce nazwy aliasu i użycie jej. Zobacz [Właściwości komórki](#Właściwości_komórki.md) powyżej, jak ustawić alias. Na przykład, jeśli dane w komórce B1 zawierają parametr długości obiektu, nazwa aliasu `MyObject_Length` pozwoli na odwołanie się do tej wartości jako `<<MyParams>>.MyObject_Length` zamiast `Spreadsheet.B1`. Oprócz tego, że nazwy aliasów są o wiele łatwiejsze do odczytania i zrozumienia, można je również o wiele łatwiej zmienić, jeśli zdecydujemy się na zmianę struktury arkusza kalkulacyjnego. Używanie aliasów ma również tę zaletę, że łatwiej jest sprawdzić, które komórki są używane do sterowania innymi częściami dokumentu. Zauważ, że FreeCAD automatycznie dostosowuje odniesienia do pozycji w wyrażeniach, jeśli wstawiasz lub usuwasz wiersze i kolumny w arkuszu kalkulacyjnym, więc nawet jeśli używasz numerów wierszy i kolumn w wyrażeniu, możesz wstawiać wiersze i kolumny bez naruszania odniesień do otaczających komórek.


</div>


</div>

### Modele złożone i przeliczanie 

Edycja arkusza kalkulacyjnego powoduje ponowne obliczenie modelu 3D, nawet jeśli wprowadzone zmiany nie mają wpływu na model. W przypadku złożonego modelu ponowne obliczanie może trwać bardzo długo, a konieczność czekania po każdej edycji jest oczywiście dość irytująca.

Oto trzy rozwiązania, jak sobie z tym poradzić:

1.  Tymczasowo pomiń ponowne przeliczenie:
    -   W oknie [widoku drzewa](Tree_view/pl.md) kliknij prawym przyciskiem myszy dokument <img alt="" src=images/Document.svg  style="width:24px;"> zawierający arkusz kalkulacyjny.
    -   Z menu podręcznego wybierz opcję **Pomiń przeliczanie**.
    -   Rozwiązanie to ma dużą wadę. Nowe wartości wprowadzone w arkuszu kalkulacyjnym nie zostaną wyświetlone do czasu ponownego przeliczenia dokumentu. Zamiast tego wyświetlany jest komunikat `#OCZEKIWANIE`.
    -   Możesz dokonać przeliczenia ręcznie, używając polecenia [Odświerz](Std_Refresh/pl.md), lub wyłączyć opcję **Pomiń przeliczanie** po zakończeniu edycji.
2.  Użyj makra, aby automatycznie pomijać ponowne obliczenia podczas edycji arkusza kalkulacyjnego:
    -   Pobierz i uruchom makrodefinicję [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   To rozwiązanie pozwala zaoszczędzić kilka kroków w porównaniu z pierwszym rozwiązaniem, ale ma też wspomnianą wadę.
3.  Umieść arkusz kalkulacyjny w osobnym pliku [FreeCAD](File_Format_FCStd/pl.md):
    -   Możesz odwoływać się do danych arkusza kalkulacyjnego z zewnętrznego pliku **.FCStd** za pomocą takiej składni: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   Zaletą umieszczenia arkusza kalkulacyjnego w innym pliku w stosunku do wyłączenia ponownych obliczeń jest to, że ponownie przeliczany będzie sam arkusz.
    -   Wadą jest to, że model nie będzie automatycznie przeliczany po wprowadzeniu zmian w arkuszu kalkulacyjnym.
    -   W sytuacji, gdy najpierw otwieramy plik arkusza kalkulacyjnego, zmieniamy jedną lub więcej wartości, a następnie otwieramy plik modelu, nie ma żadnych informacji o konieczności ponownego przeliczenia modelu. Jeśli jednak otwarte są oba pliki, po użyciu przycisku [Odświerz](Std_Refresh/pl.md) zostanie poprawnie zaktualizowany model po zmianach w pliku arkusza kalkulacyjnego.

## Jednostki

W arkuszu kalkulacyjnym z wartościami komórek jest związane pojęcie wymiaru *(jednostki)*. Liczba wprowadzona bez przypisanej jej jednostki nie ma określonego wymiaru. Jednostka powinna być wprowadzona bezpośrednio po wartości liczby, bez odstępów. Jeśli liczba ma przypisaną jednostkę, będzie ona używana we wszystkich obliczeniach. Na przykład pomnożenie dwóch długości z jednostką mm daje pole powierzchni z jednostką mm².

Jeśli komórka zawiera wartość reprezentującą wymiar, należy ją wpisać wraz z odpowiadającą jej jednostką. Chociaż w wielu prostych przypadkach można się obejść bez podawania wartości bezwymiarowej, nie należy podawać jednostki. Jeśli wartość reprezentująca wymiar zostanie wprowadzona bez powiązanej z nią jednostki, pewne sekwencje operacji powodują, że FreeCAD zgłasza niezgodność jednostek w wyrażeniu, podczas gdy wydaje się, że wyrażenie powinno być poprawne. *(Można to lepiej zrozumieć, przeglądając [ten wątek](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) na forum FreeCAD)*.

Jednostki wyświetlane dla wartości komórki można zmienić za pomocą okna dialogowego właściwości [zakładka jednostki](#W.C5.82a.C5.9Bciwo.C5.9Bci_kom.C3.B3rek.md) *(powyżej)*. Nie zmienia to wartości zawartej w komórce, a jedynie konwertuje istniejącą wartość na potrzeby wyświetlania. Wartość używana do obliczeń nie ulega zmianie, a wyniki formuł wykorzystujących tę wartość pozostają niezmienione. Na przykład komórka zawierająca wartość {{value|5.08cm}} może zostać wyświetlona jako {{value|2cale}} po zmianie wartości na karcie Jednostki na \"cale\".

Liczby bezwymiarowej nie można zmienić na liczbę z jednostką za pomocą okna dialogowego właściwości komórki. Można wprowadzić ciąg jednostek i zostanie on wyświetlony, ale komórka nadal będzie zawierać liczbę bezwymiarową. Aby zmienić wartość bezwymiarową na wartość z wymiarem, należy ponownie wprowadzić samą wartość wraz z przypisaną jej jednostką.

Niekiedy może być wskazane usunięcie wymiaru z wyrażenia. Można to zrobić, mnożąc przez 1 z jednostką odwrotną.

## Importowanie i eksportowanie 

### Format CSV 

Arkusze kalkulacyjne FreeCAD mogą być importowane i eksportowane do formatu [CSV](https://en.wikipedia.org/wiki/Comma-separated_values), który może być również odczytywany i zapisywany przez większość innych aplikacji arkuszy kalkulacyjnych, takich jak Microsoft Excel czy LibreOffice Calc. Więcej informacji na ten temat można znaleźć na stronach [Import](Spreadsheet_Import/pl.md) i [Eksport](Spreadsheet_Export/pl.md).

### Format XLSX 

Arkusze kalkulacyjne w formacie Excel XLSX można importować za pomocą polecenia [Importuj](Std_Import/pl.md) lub polecenia [Otwórz](Std_Open/pl.md). Obsługiwane są następujące funkcje:

-   Wszystkie funkcje, które są dostępne także w arkuszu kalkulacyjnym FreeCAD. Inne funkcje powodują wystąpienie błędu w odpowiedniej komórce po zaimportowaniu.
-   Nazwy aliasów dla komórek.
-   Więcej niż jeden arkusz w arkuszu kalkulacyjnym Excel. W takim przypadku dla każdego arkusza Excela tworzony jest jeden arkusz kalkulacyjny FreeCAD.

Inne funkcje nie są importowane do arkusza kalkulacyjnego FreeCAD.

## Wydruki

Aby zachować ustawienia strony niezbędne do drukowania, arkusze kalkulacyjne FreeCAD można drukować, wstawiając je do obiektu [widok Arkusza Kalkulacyjnego](TechDraw_SpreadsheetView/pl.md).

## Obecne ograniczenia 

FreeCAD sprawdza zależności cykliczne podczas ponownych obliczeń. Z założenia sprawdzanie to zatrzymuje się na poziomie obiektu arkusza kalkulacyjnego. W konsekwencji nie powinieneś mieć arkusza kalkulacyjnego zawierającego zarówno komórki, których wartości są używane do określania parametrów modelu, jak i komórki, których wartości wykorzystują dane wyjściowe z modelu. Na przykład nie można mieć komórek określających długość, szerokość i wysokość obiektu, a także innej komórki, która odwołuje się do całkowitej objętości wynikowego kształtu. Ograniczenie to można obejść, mając dwa arkusze kalkulacyjne: jeden używany jako źródło danych dla parametrów wejściowych do modelu, a drugi używany do obliczeń opartych na danych wynikowych geometrii.

## Łączenie komórek 


{{Version/pl|0.20}}

Istnieje możliwość łączenia zawartości komórek z innymi komórkami arkusza kalkulacyjnego. Może to być przydatne podczas pracy z dużymi tabelami lub w celu pobrania zawartości komórki z innego arkusza kalkulacyjnego.

### Tworzenie powiązań 

Aby na przykład powiązać zakres komórek A3-C4 z zakresem komórek B1-D2:

1.  Zaznacz zakres komórek A3-C4.
2.  Kliknij prawym przyciskiem myszy i wybierz **Powiąż ...** z menu podręcznego.
3.  Zostanie otwarte okno dialogowe **Powiąż komórki arkusza kalkulacyjnego**.
4.  Ustaw zakres B1-D2 w polu **Do komórek**:
    ![](images/Spreadsheet_binding-dialog.png )
5.  Naciśnij przycisk **OK**.
6.  Związane komórki mają niebieską obwódkę, aby wyróżnić to powiązanie.
7.  Jeśli teraz wpiszesz coś w komórce C1, to to samo pojawi się natychmiast w komórce B3.

![](images/Spreadsheet_binding-result.png ) 
*Arkusz kalkulacyjny może teraz wyglądać następująco*

### Modyfikacja powiązań 

1.  Kliknij prawym przyciskiem myszy powiązaną komórkę (nie trzeba zaznaczać całego powiązanego zakresu) i wybierz z menu kontekstowego polecenie **Powiąż ...**.
2.  Otworzy się okno dialogowe **Powiąż komórki arkusza kalkulacyjnego**.
3.  Zmień jedną lub więcej opcji. Zwróć uwagę, że nie można zmienić zakresu komórek **Powiąż komórki**, czyli powiązanego zakresu komórek.
4.  Naciśnij przycisk **OK**.

### Usuwanie powiązań 

1.  Kliknij prawym przyciskiem myszy wiązaną komórkę (nie trzeba zaznaczać całego wiązanego zakresu) i wybierz z menu kontekstowego polecenie **Powiąż ...**.
2.  Otworzy się okno dialogowe **Powiąż komórki arkusza kalkulacyjnego**.
3.  Naciśnij przycisk **Usuń powiązanie**.

### Uwagi

-   Opcji **Ukryj zależność powiązania** można użyć, aby uniknąć problemów z cyklicznymi zależnościami między arkuszami kalkulacyjnymi. Zaznaczenie jej jest konieczne, gdy na przykład komórki w *Arkuszu kalkulacyjnym A* są powiązane z komórkami w *Arkuszu kalkulacyjnym B*, a komórki w *Arkuszu kalkulacyjnym B* są powiązane z innymi komórkami w *Arkuszu kalkulacyjnym A*. Opcji tej należy używać z rozwagą:
    -   Ukrywanie zależności może być niebezpieczne, ponieważ uszkodzone zależności mogą spowodować uszkodzenie pliku FreeCAD. Na przykład, gdy usuniesz arkusz kalkulacyjny, nie zostaniesz ostrzeżony o ukrytych zależnościach.
    -   Gdy otworzysz dokument z arkuszem kalkulacyjnym zawierającym ukrytą zależność, arkusz zostanie oznaczony do ponownego przeliczenia. Dzieje się tak dlatego, że zależności cyklicznej nie można obliczyć ponownie w sposób automatyczny. Aby ponownie obliczyć, należy użyć narzędzia [Odśwież](Std_Refresh/pl.md).
-   Wiązanie komórek ma funkcję sprawdzania zakresu i ostrzega o niedopasowanych zakresach. Na przykład powiązanie komórek 1x3 z komórkami 3x2 nie działa, ponieważ nie wiadomo, które 3 komórki z pierwotnych 6 komórek powinny zostać użyte.
-   Nie można zmienić zakresu komórek w istniejącym powiązaniu. Należy najpierw usunąć powiązanie z komórek, a następnie utworzyć nowe.
-   Nie można jeszcze zmienić koloru ramki wskazującej powiązanie.

## Tabela konfiguracji 


{{Version/pl|0.20}}

Za pomocą Arkuszy kalkulacyjnych można tworzyć tabele konfiguracyjne zawierające zestawy wstępnie zdefiniowanych parametrów modelu, a następnie dynamicznie zmieniać konfigurację, która ma być używana. Aby dowiedzieć się więcej na temat działania tej funkcji, zobacz [ten post na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183).


<div class="mw-collapsible mw-collapsed toccolours">

Rozwiń tę sekcję, aby zapoznać się z krótkim przewodnikiem po tworzeniu tabeli konfiguracyjnej.


<div class="mw-collapsible-content">

1.  W nowym dokumencie najpierw utwórz [Część](Std_Part.md) środowiska pracy Część, następnie utwórz [sześcian](Part_Box/pl.md), [walec](Part_Cylinder/pl.md) i arkusz kalkulacyjny.
2.  Sześcian i walec są automatycznie umieszczane w kontenerze [Część](Std_Part/pl.md). Umieść w nim także arkusz kalkulacyjny.
3.  W arkuszu kalkulacyjnym wprowadź zawartość w sposób przedstawiony poniżej. Ustaw aliasy dla komórek B2 jako {{Value|szerokość}}, C2 jako {{Value|długość}} i D2 jako {{Value|promień}}:
    ![](images/Spreadsheet_configuration_table_screenshot_4.png )
4.  Powiąż [wyrażeniem](Expressions.md) komórki {{Value|Spreadsheet.szerokość}} i {{Value|Spreadsheet.długość}} do właściwości sześcianu **Szerokość** i **Długość**, odpowiednio:
    ![](images/Spreadsheet_configuration_table_screenshot_2.png )
5.  Powiąż wyrażenie {{Value|Spreadsheet.promień}} z właściwością **Promień** walca. Zmień także wartość **Wysokość** walca na {{Value|5 mm}}, tak aby był on niższy niż sześcian.
6.  Kliknij prawym przyciskiem myszy komórkę A2 w arkuszu kalkulacyjnym i wybierz z menu kontekstowego polecenie **Tabela konfiguracji ...**.
7.  Zostanie otwarte okno dialogowe **Ustawienia tabeli konfiguracji**.
8.  Wprowadź następujące dane:
    ![](images/Spreadsheet_configuration_table_screenshot_5.png )
9.  Naciśnij przycisk **OK**.
10. Do kontenera [Część](Std_Part.md) jest dodawana nowa właściwość o nazwie **Konfiguracja**, która umożliwia wybór konfiguracji, jak pokazano poniżej:
    ![](images/Spreadsheet_configuration_table_screenshot_6.png )

Za pomocą [Łącza](Std_LinkMake/pl.md) lub funkcji [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md) można utworzyć instancję [zmienną](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183&p=532130#p532130) obiektu konfigurowalnego, wykonując następujące czynności:

1.  Utwórz [Łącze](Std_LinkMake/pl.md) do kontenera [Część](Std_Part/pl.md) i ustaw jego właściwość **Kopiuj łącze przy zmianie** na wartość {{Value|Włączone}}.
2.  Przenieś łącze w nowe miejsce, zmieniając jego **Umiejscowienie** tak, aby łatwiej było je odróżnić od oryginalnego obiektu.
3.  Wybierz inną **Konfigurację** dla łącza, aby utworzyć jego wersję wariantową.

Podobne kroki dotyczą funkcji [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md), z tą różnicą, że jego właściwość do aktywowania instancji wariantu nazywa się **Kopiuj łącze przy zmianie**.


</div>


</div>

## Podstawy pisania skryptów 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/pl
