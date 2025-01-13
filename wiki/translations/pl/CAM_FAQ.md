# CAM FAQ/pl
## Ile osi środowisko pracy CAM wspiera? 

Obecnie, środowisko pracy CAM obsługuje frezowanie z wykorzystaniem do 3 osi. Na ten moment, funkcje związane z czwartą osią nie są oficjalnie dostępne, ale istnieją [eksperymentalne implementacje](CAM_fourth_axis/pl.md). 

## Czy środowisko pracy CAM wspiera toczenie? 

Obecnie środowisko pracy CAM nie wspiera operacji obróbki na tokarkach bezpośrednio, ale można zainstalować rozszerzenie [TurningAddon](https://github.com/dubstar-04/TurningAddon), które korzysta z biblioteki Pythona [LibLathe](https://github.com/dubstar-04/LibLathe). Więcej informacji można znaleźć w [tym wątku na forum](https://forum.freecad.org/viewtopic.php?t=30563). 

## Dlaczego wydaje się, że w niektórych przypadkach środowisko CAM zapewnia więcej niż jeden sposób określenia Operacji? 

Środowisko CAM zapewnia istniejące narzędzia do realizowania wielu operacji frezowania, a ponieważ FreeCAD jest programem open source, nic nie stoi na przeszkodzie aby dowolny użytkownik stworzył własną funkcjonalność do niego.

Podobnie jak z modelowaniem 3D, często dostępnych jest wiele metod, które mogą mieć przewagę dla różnych operacji Zadań. W niektórych przypadkach kombinacje operacji są używane do zapewnienia kompletnego frezowania materiału roboczego.

Jednym częstym przykładem jest to, że cięcie konturowe może być wygenerowane z krawędzi lub ścian. W niektórych przypadkach widoczna będzie przewaga jednej z tych form geometrii wejściowej nad drugą. 

## Dlaczego wykańczanie Operacji zmienia pozycję w przepływie pracy Zadania pokazywanym na liście Operacji? 

Wszystkie dodatki do Zadania\--wliczając modyfikacje i kopie operacji\--są dodawane na końcu przepływu pracy Zadania. Jeśli to zakłóca poprawną kolejność Zadania, należy dokonać zmiany kolejności w zakładce Workflow edytora Zadania. 

## Jaka jest różnica między Odległością odstępu i Bezpieczną wysokością? 

Informacje na ten temat można znaleźć na stronie [Wysokości i głębokości](CAM_Workbench/pl#Wysokości_i_głębokości.md). 

## Jakie jest typowe wykorzystanie Karty konfiguracji? 

[Karta konfiguracji](CAM_SetupSheet/pl.md) to dedykowany arkusz kalkulacyjny zawarty w Zadaniu, modyfikowany w widoku właściwości, dostępny wyłącznie z poziomu środowiska pracy CAM. Zapewnia on mechanizm dla bardziej zaawansowanych użytkowników, umożliwiając im konfigurowanie różnych aspektów swojego zadania za pomocą wartości i wyrażeń zawartych w [Karcie konfiguracji](CAM_SetupSheet/pl.md).

Aktualne wartości dla Głębokości, Wysokości i Kontrolerów Narzędziowych obejmują:

1.  Final Depth Expression --- OpFinalDepth
2.  Start Depth Expression --- OpStartDepth
3.  Step Down Expression --- Domyślnie OpToolDiameter. To wyrażenie jest używane w każdej operacji do obliczenia domyślnej wartości krokowego opadania w oparciu o średnicę narzędzia określoną w powiązanym kontrolerze narzędzi.
4.  Clearance Height Expression --- StartDepth+SetupSheet.ClearanceHeightOffset
5.  Clearance Height Offset Value --- Zawiera wartość używaną w wyrażeniach
6.  Safe Height Expression --- StartDepth+SetupSheet.SafeHeightOffset
7.  Safe Height Offset Value --- Zawiera wartość używaną w wyrażeniach
8.  Horizontal Rapid Value --- Dostarcza domyślną wartość używaną do początkowego wypełnienia wartości Szybkiego Ruchu Poziomego dla wszystkich kontrolerów narzędzi.
9.  Vertical Rapid Value --- Dostarcza domyślną wartość używaną do początkowego wypełnienia wartości Szybkiego Ruchu Pionowego dla wszystkich kontrolerów narzędzi.

To zapewnia wszechstronność. Przykładowo, zapewniane są domyślne wyrażenia, ale mogą one zostać nadpisane przez użytkownika. Modyfikacja może nawet redukować domyślne równanie do wartości odpowiedniej dla użytkownika. 

## Jakie jest typowe wykorzystanie Szablonów zadań? 

Szablony zadań pozwalają na zapisanie często używanych definicji Zadań z Zadania do użycia w kolejnych podobnie skonfigurowanych Zadaniach. 

## Ile obiektów podstawowych środowisko pracy CAM wspiera? 

Wsparcie jest tylko dla jednego obiektu podstawowego. Aby tworzyć ścieżki dla wielu brył w jednym Zadaniu, możesz utworzyć z nich kształt złożony i użyć go jako obiektu podstawowego dla Zadania. 

## Dlaczego Operacja nie tworzy użytecznych wyników? 

Istnieje wiele powodów, dla których pojedyncza Operacja może nie generować wyników.

Jednym częstym powodem jest to, że geometria narzędzia zdefiniowana w Kontrolerze narzędzia wybranym dla Operacji jest zbyt duża aby zmieścić się w geometrii wybranej na modelu 3D dla Operacji.

Miej na uwadze, że zwykle objawia się to jako gwałtowny ruch do miejsca rozpoczęcia Operacji, dopełniony gwałtownym ruchem w osi Z do geometrii wskazanej do zdefiniowana Operacji a następnie powrotem do wysokości gwałtownego przejścia.

Innym częstym błędem jest to, że operacja konturowa nie tworzy ścieżek gdy edytor operacji konturowej Cut Side jest ustawiony na \"Inside\", wartość domyślną a przełączanie widoczności modelu 3D pozwala je zauważyć. 

## Czy środowisko pracy CAM może wykonywać operacje frezowania powierzchni 3D? 

Tak, to środowisko zapewnia operacje frezowania 3D powierzchni. Wymagają one zainstalowania w ścieżce plików makr zewnętrznego modułu open source - OpenCamLibrary.

OpenCamLibrary nie jest zintegrowane z FreeCAD aby uniknąć naruszeń warunków licencji. 

## Co należy zrobić jeśli domyślne strategie Operacji nie są wystarczające? 

Dla operacji kieszeni, punkt początkowy domyślnie ustawiony jest na XYZ = 000 i zawsze jest aktywowany, ale może być również skonfigurowany w oknie widoku właściwości. Operacje kieszeni i frezowania powierzchni oferują jawne określenie trybu cięcia: Climb (wspinaczka) i Conventional (konwencjonalny) w zakładce Operacja.

Dla operacji typu konturowego, zakładka Operacja ma pole „Kierunek", które może być skonfigurowane jako CW (zgodnie z ruchem wskazówek zegara) lub CCW (przeciwnie do ruchu wskazówek zegara), co definiuje kierunek cięcia. Dla odniesienia:

1.  Cut Side = Outside, Cut Direction = CCW, cięcie w górę
2.  Cut Side = Outside, Cut Direction = CW, cięcie konwencjonalne
3.  Cut Side = Inside, Cut Direction = CW, cięcie konwencjonalne
4.  Cut Side = Inside, Cut Direction = CCW, cięcie w górę

Punkty startowe mogą być włączone i skonfigurowane w oknie widoku Właściwości.

W operacjach frezowania ścian można określić Material Allowance, pozwalając na nadcinanie dla dodatnich wartości i podcinanie dla ujemnych wartości.

W operacjach konturowych i kieszeni, dodatkowe odsunięcie ma ten sam cel.

Te pola wejściowe są cenne, umożliwiając funkcjonalności takie jak:

1.  Określenie przejazdów wstępnych, w połączeniu z polami wejściowymi Głębokości.
2.  Określenie nadmiaru dla operacji frezowania.
3.  Elementy mniejsze niż średnica narzędzia, które muszą być frezowane, mogą skorzystać z określenia cięcia konturu zewnętrznego z ujemną wartością Dodatkowego Odstępu.

Należy zachować ostrożność przy określaniu Material Allowance i Odstępów, aby uniknąć niepożądanych cięć w surowcu. 

## Co należy zrobić jeśli Operacja generuje więcej ruchów pionowych niż dane Zadanie zezwala? 

Operacje takie jak [Kieszeń 3D](CAM_Pocket_3D/pl.md), [Obróbka kieszeni](CAM_Pocket_Shape/pl.md) i [Powierzchnia](CAM_MillFace/pl.md), ale nie operacje konturowe, mają opcję konfiguracji utrzymywania narzędzia w dół, w zakładce Danych w Widoku właściwości. 

## Jak można zostawić zakładki żeby umocować obrobiony element? 

Środowisko pracy CAM zapewnia [Znacznik](CAM_DressupTag/pl.md) dokładnie w tym celu. 

## Czym jest Postprocessor? 

[Postprocesor](CAM_Post/pl.md) jest używany do przygotowania kodu wyjściowego dla kontrolerów CNC różnych obrabiarek, w ich dialekcie G-code. 

## Czy można zmodyfikować istniejący lub utworzyć własny Postprocesor? 

Postprocesory są skryptami Pythona i są zapisywane w ścieżce plików makr. Są przeznaczone do modyfikowania lub wykorzystywania jako szablon dla dalszego rozwoju postprocesorów. 

## Chcę korzystać tylko z jednego postprocesora\-- czy mogę ustawić go jako domyślny lub schować pozostałe opcje? 

Tak, [preferencje CAM](CAM_Preferences/pl.md) mają sekcję do postprocesorów gdzie można wybrać które mają być wyświetlane i ustawić domyślny. 

## Jak można ustawić jednostko metryczne/imperialne dla obiektu ścieżki? 

Jednostki modelu 3D są zdefiniowane w zakładce Edycja-\>Preferencje\...\>Ogólne-\>Jednostki.

Ustawienie Jednostki, które konfiguruje, jak docelowa frezarka interpretuje G-code Zadania, jest ustawiane w wyjściowym postprocesorze, który wstawia polecenie G20 lub G21 kodu G-code, aby wskazać odpowiednio cale lub milimetry.

Postprocesor jest również skonfigurowany dla Jednostki/sekundę lub Jednostki/minutę. Jeśli ustawiony na Jednostki/minutę, wewnętrzny dialekt kodu G w środowisku pracy CAM jest mnożony przez 60.

Niezgodności między modelem 3D a ustawieniami postprocesora są prawdopodobnymi przyczynami błędów w prędkości posuwu o czynnik 60 oraz błędów w odległości o czynnik 25.4. 

## Jak mogę zasymulować swoje strategie obróbki? 

Objętościowy symulator jest dostępny, pozwalając wyświetlić wyniki cięcia geometrii narzędzi w operacjach Zadania względem materiału obrabianego.

Jeśli linie ścieżki zakrywają wynik symulacji, ich widoczność powinna być wyłączona przed symulacją. 

## Jakie jest znaczenie kolorów linii ścieżek? 

Kolory linii ścieżek są definiowane w Edycja-\>Preferencje\...-\>CAM-\>GUI-\>Domyślne kolory CAM. Domyślne kolory to:

1.  Zielony dla normalnych ścieżek.
2.  Czerwony dla gwałtownych ścieżek.
3.  Żółty dla sondowanych ścieżek.


{{Top}}



## Jak można włączyć/wyłączyć widoczność linii ścieżek? 

Środowisko pracy CAM pozwala na kontrolowanie wyświetlania linii ścieżki poprzez przełączanie widoczności zadania, wybierając je w [widoku złożonym](Combo_view/pl.md). Widoczność poszczególnych operacji lub grup operacji jest następnie przełączana z widoku złożonym. 

## Jak można sprawdzić czy sekwencja G-code jest poprawna? 

Domyślnie wyjście postprocesora jest wyświetlane w oknie przed zapisaniem. To, wraz z symulatorem CAM, stanowi sposób na sprawdzenie zadania przed przetworzeniem go na maszynie CNC. Narzędzie do inspekcji kodu G pozwala na przeglądanie wewnętrznego kodu G-code CAM dla każdej operacji, umożliwiając śledzenie, czy wyjście postprocesora odzwierciedla to, co jest zdefiniowane w operacji.

Lista operacji w panelu widoku złożonego wyświetla kolejność, w jakiej operacje będą przetwarzane w zadaniu. Jeśli operacje są poprawne, ale nie w żądanej kolejności, można to dostosować, klikając dwukrotnie listę operacji i przeciągając operacje do właściwej lokalizacji, lub klikając dwukrotnie edytor zadania i wybierając zakładkę Workflow, a następnie używając strzałek w górę/w dół na wybranych operacjach, aby je posortować. 

## Dlaczego nie uzyskuję poprawnego wyjściowego kodu G-code z mojego postprocesora dla Operacji wstawianych używając polecenia Partial Command-\>Custom? 

Często polecenie Custom G-Code, ze względu na format będący zawsze w Jednostkach/sekundę, może powodować błędy rzędu 60 dla obrabiarek CNC operujących w Jednostkach/minutę. 

## Dlaczego zmiany wartości Umiejscowienia w Widoku właściwości zdają się nie działać poprawnie w środowisku pracy CAM? 

Funkcja Ścieżka również posiada właściwość Umiejscowienie. Zmiana wartości tej właściwości zmieni położenie funkcji w widoku 3D, chociaż sama informacja o Ścieżce nie zostanie zmodyfikowana. Transformacja jest czysto wizualna. Pozwala to na przykład stworzyć Ścieżkę wokół powierzchni, która ma określoną orientację w modelu, różniącą się od orientacji materiału skrawającego na maszynie CNC.

Jednakże, Złożenia Ścieżki mogą korzystać z Umiejscowienia swoich elementów podrzędnych (zobacz poniżej).

[skrypty dla środowiska Path](CAM_scripting/pl.md) 

## Dlaczego środowisko pracy CAM na moim komputerze zdaje się nie mieć funkcji, które widzę u innych użytkowników w postach na forum? 

Domyślnie eksperymentalne funkcje są ukryte w środowisku CAM. 

## Dlaczego filmiki na YouTube publikowane przez deweloperów środowiska pracy CAM wydają się nie być zgodne z tym środowiskiem? 

Środowisko pracy CAM zmieniło się znacząco między wersjami v0.16 i v0.17 i wszelkie filmiki opublikowane przed 01.01.2018 najprawdopodobniej zawierają informacje niezgodne z wersją v0.17 środowiska CAM. 

## Dlaczego łuki nie są okrągłe tylko zrobione ze zbiorów prostych linii? 

To tylko kwestia wyświetlania ścieżki. Można to zmienić w preferencjach: załaduj środowisko pracy CAM.

1.  otwórz Preferencje-\>CAM-\>Ustawienia dla zadania
2.  ustaw wartości dla *Domyślna tolerancja geometrii* i *Domyślna dokładność krzywej* na małe wartości, ale nie na 0, np. użyj 0.01mm.
3.  zatwierdź zmiany
4.  zrestartuj FreeCAD.


{{Top}}





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM FAQ/pl
