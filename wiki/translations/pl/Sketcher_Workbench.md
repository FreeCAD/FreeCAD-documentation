# <img alt="Ikonka FreeCAD dla Środowiska pracy Szkicownik " src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/pl






## Wprowadzenie

Dzięki środowisku pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> **Szkicownik** można tworzyć szkice 2D przeznaczone do wykorzystania w innych środowiskach pracy. Szkice 2D są punktem wyjścia dla wielu modeli CAD. Zazwyczaj definiują one kształt i ścieżkę dla operacji tworzenia kształtów 3D. Ostateczny kształt modelu może zależeć od kilku szkiców.

Wraz z operacjami logicznymi zdefiniowanymi w środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md), środowisko pracy Szkicownik, lub w skrócie \"Szkicownik\", stanowi podstawę [konstrukcyjnej geometrii brył](Constructive_solid_geometry/pl.md) *(CSG)* metody budowania brył. Wraz z operacjami środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md), stanowi również podstawę [edycji cech](Feature_editing/pl.md) metodologii tworzenia brył. Jednak wiele innych środowisk pracy również korzysta ze szkiców.

Środowisko pracy Szkicownik posiada **[wiązania](Sketcher_Workbench/pl#Wiązania.md)**, dzięki czemu kształty 2D mogą podążać za precyzyjnymi definicjami geometrycznymi pod względem długości, kątów i relacji *(poziomość, pionowość, prostopadłość itp.)*. Narzędzie do tworzenia wiązań oblicza wymagany zakres geometrii 2D i umożliwia przeprowadzenie interaktywnej eksploracji stopni swobody szkicu.

Szkicownik nie jest przeznaczony do tworzenia planów 2D. Po użyciu szkiców do wygenerowania bryły są one automatycznie ukrywane, a wiązania są widoczne tylko w trybie edycji szkicu. Jeśli potrzebujesz tworzyć tylko widoki 2D do druku i nie chcesz tworzyć modeli 3D, wypróbuj środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md).

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*W pełni związany szkic.*



## Wiązania

Zamiast wymiarów, wiązania są stosowane w celu ograniczenia stopnia swobody obiektu. Na przykład, linia bez wiązań ma 4 [stopnie swobody](#Degrees_Of_Freedom/pl.md) *(w skrócie \"DoF\")*: można ją przesuwać w poziomie lub w pionie, można ją rozciągać i obracać.

Wykorzystanie wiązania poziomego lub pionowego, lub wiązania kąta *(względem innej linii lub jednej z osi)*, ograniczy jej zdolność do obracania pozostawiając ją z 3 stopniami swobody. Zablokowanie jednego z punktów w relacji do układu współrzędnych usunie kolejne dwa stopnie. W końcu zastosowanie wiązania wymiaru usunie ostatni stopień swobody. Linia jest w wtedy uznawana za **w pełni ograniczoną więzami**.

Obiekty mogą być ze sobą związane. Dwie linie mogą być połączone przez jeden z ich punktów za pomocą wiązania punktu zbieżnego. Można ustawić kąt między nimi lub określić ich prostopadłość. Linia może być styczna do łuku lub okręgu itd. Złożony szkic z wieloma obiektami może mieć wiele różnych rozwiązań, a uczynienie go **w pełni związanym** może oznaczać, że tylko jedno z tych możliwych rozwiązań zostało osiągnięte na podstawie zastosowanych wiązań.

Są dwa typy wiązań: geometryczne i wymiarowe. Są one opisane dokładnej w poniższej sekcji [Narzędzia](#Narzędzia.md).



### Edycja wiązań 

Gdy utworzone jest [wiązanie konstrukcyjne](Sketcher_ToggleDrivingConstraint/pl.md) i gdy wybrana jest opcja **Spytaj o wartość po stworzeniu wiązania wymiaru** w [preferencjach](Sketcher_Preferences/pl#Wyświetlanie.md) *(domyślnie)*, otworzy się okno dialogowe do edycji jej wartości.

![](images/Sketcher_Edit_Constraint.png )

Można wprowadzić wartość liczbową lub [wyrażenie](Expressions/pl.md), a także można nazwać wiązanie, aby ułatwić jego użycie w innych wyrażeniach. Można również zaznaczyć pole wyboru **Odniesienie**, aby przełączyć wiązanie w [tryb odniesienia](Sketcher_ToggleDrivingConstraint/pl.md).

Aby edytować wartość istniejącego wiązania wymiarowego, wykonaj jedną z poniższych czynności:

-   Kliknij dwukrotnie wartość wiązania w [Widoku 3D](3D_view/pl.md).
-   Kliknij dwukrotnie wiązanie w [oknie dialogowym szkicownika](Sketcher_Dialog/pl.md).
-   Kliknij prawym przyciskiem myszy wiązanie w oknie dialogowym szkicownika i wybierz opcję **Zmień wartość** z menu kontekstowego.



### Zmiana położenia wiązań 

Ograniczenia wymiarowe można zmieniać w widoku 3D poprzez przeciąganie. Przytrzymaj lewy przycisk myszy nad wartością ograniczenia i przesuń kursor myszki. Symbole ograniczeń geometrycznych są pozycjonowane automatycznie i nie można ich przesuwać.



## Szkice profilowe 

Aby utworzyć szkic, który może być użyty jako profil do generowania brył, należy przestrzegać pewnych zasad:

-   Szkic musi zawierać tylko zamknięte kontury. Odstępy między punktami końcowymi, nawet najmniejsze, są niedozwolone.
-   Kontury mogą być zagnieżdżane, aby tworzyć puste przestrzenie, ale nie powinny przecinać się ani przecinać innych konturów.
-   Kontury nie mogą współdzielić krawędzi z innymi konturami. Należy unikać zduplikowanych krawędzi.
-   Połączenia T, czyli więcej niż dwie krawędzie dzielące wspólny punkt lub punkt dotykający krawędzi, są niedozwolone.

Reguły te nie mają zastosowania do geometrii konstrukcyjnej *(domyślny kolor niebieski)*, która nie jest wyświetlana poza trybem edycji lub jeśli szkic jest używany do innego celu. W zależności od środowiska pracy i narzędzia, które będzie używać szkicu profilu, mogą obowiązywać dodatkowe restrykcje.



## Pomoce kreślarskie 

Środowisko pracy Szkicownik ma kilka pomocy rysunkowych i innych funkcji, które mogą pomóc podczas tworzenia geometrii i stosowania wiązań.



### Tryby kontynuacji 

W [konfiguracji](Sketcher_Preferences/pl#Wyświetlanie.md) istnieją dwa tryby kontynuacji: **Tworzenie geometrii \"Tryb kontynuacji\"** i **Tworzenie wiązań \"Tryb kontynuacji\"**. Jeśli są one zaznaczone *(domyślnie)*, powiązane narzędzia uruchomią się ponownie po zakończeniu. Aby wyjść z narzędzia ciągłego, należy nacisnąć **Esc** lub prawy przycisk myszy. Czynność tę należy powtórzyć, jeśli narzędzie geometrii ciągłej zostało już wprowadzone. Narzędzie ciągłe można również zamknąć, uruchamiając inne narzędzie do tworzenia geometrii lub wiązań. Należy pamiętać, że naciśnięcie **Esc**, gdy żadne narzędzie nie jest aktywne, spowoduje wyjście z trybu edycji szkicu. Odznacz opcję **Klawisz Esc umożliwia wyjście z trybu edycji szkicu** w [konfiguracji](Sketcher_Preferences/pl#Ogólne.md), jeśli często nieumyślnie naciskasz **Esc** zbyt wiele razy.



### Wiązania automatyczne 

W szkicach z zaznaczoną opcją **Automatyczne wiązania** *(domyślnie)* kilka wiązań jest nakładanych automatycznie. Ikona proponowanego wiązania automatycznego jest wyświetlana obok kursora, gdy jest on prawidłowo umieszczony. Kliknięcie lewym przyciskiem myszy spowoduje zastosowanie tego wiązania. Jest to ustawienie dla każdego szkicu, które można zmienić w [oknie dialogowym](Sketcher_Dialog/pl#Wiązania.md) lub zmieniając [właściwość](Property_editor/pl.md) szkicu **Wiązania automatyczne**.

Następujące wiązania są stosowane automatycznie:

-   [wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md),

-   [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md),

-   [poziomo](Sketcher_ConstrainHorizontal/pl.md),

-   [pionowo](Sketcher_ConstrainVertical/pl.md),

-   [stycznie](Sketcher_ConstrainTangent/pl.md),

-    {{Version/pl|0.22}}: [wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md) *(punkt środkowy linii)*.



### Przyciąganie


{{Version/pl|0.21}}

Możliwe jest [przyciągnięcie](Sketcher_Snap/pl.md) do linii siatki i przecięć siatki, do krawędzi geometrii i punktów środkowych linii i łuków oraz do pewnych kątów. Należy pamiętać, że przyciąganie samo w sobie nie tworzy wiązań. Na przykład, tylko jeśli włączono [wiązania automatyczne](#Wiązania_automatyczne.md), przyciąganie do krawędzi utworzy wiązanie [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Ale samo wybranie punktu na krawędzi dałoby ten sam rezultat.



### Parametry wyświetlane na ekranie 


{{Version/pl|1.0}}

W zależności od wybranej opcji w [ustawieniach](Sketcher_Preferences/pl#Ogólne.md) można włączyć tylko wymiarowe parametry widoku lub zarówno wymiarowe, jak i pozycyjne parametry widoku. Parametry pozycyjne umożliwiają wprowadzenie dokładnych współrzędnych, na przykład środka okręgu lub punktu początkowego linii. Parametry wymiarowe umożliwiają wprowadzenie dokładnych wymiarów, na przykład promienia okręgu lub długości i kąta linii. Parametry w widoku nie są dostępne dla wszystkich narzędzi.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Określanie punktu środkowego okręgu z włączonymi parametrami pozycji.*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Wyznaczanie promienia okręgu z włączonymi parametrami wymiarowymi.*

Jeśli wartości zostaną wprowadzone i potwierdzone przez naciśnięcie **Enter** lub **Tab**, powiązane wiązania zostaną dodane automatycznie. Jeśli jednocześnie wyświetlane są dwa parametry, na przykład współrzędne X i Y punktu, możliwe jest wprowadzenie jednej wartości i wybranie punktu w celu zdefiniowania drugiej. W zależności od obiektu mogą być wymagane dodatkowe wiązania, aby w pełni go ograniczyć. Wiązania wynikające z parametrów w widoku mają pierwszeństwo przed tymi, które mogą wynikać z [wiązań automatycznych](Sketcher_Dialog/pl#Wiązania.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Łuk utworzony przez wprowadzenie wszystkich parametrów w widoku z automatycznie utworzonymi wiązaniami.*



### Wyświetlanie współrzędnych 

Jeśli opcja **Pokaż współrzędne obok kursora myszki podczas edycji** [preferencji](Sketcher_Preferences/pl#Wyświetlanie.md) jest zaznaczona *(domyślnie)*, parametry bieżącego narzędzia geometrii *(współrzędne, promień lub długość i kąt)* są wyświetlane obok kursora. Ta opcja jest wyłączona, gdy wyświetlane są parametry w widoku.



## Metody zaznaczenia 

Gdy szkic znajduje się w trybie edycji, można użyć następujących metod wyboru:



### Wybór elementu w widoku 3D 

Podobnie jak w innych obszarach FreeCAD, element można wybrać w oknie [widoku 3D](3D_view/pl.md) za pomocą jednego kliknięcia lewym przyciskiem myszy. Nie ma jednak potrzeby przytrzymywania klawisza **Ctrl** podczas wybierania wielu elementów. Przytrzymanie tego klawisza jest jednak możliwe i ma tę zaletę, że można błędnie kliknąć bez utraty zaznaczenia. W ten sposób można zaznaczać krawędzie, punkty i wiązania.



### Zaznaczanie obszarem w widoku 3D 

Zaznaczenie ramką w widoku 3D działa bez użycia narzędzia [Zaznacz obszar](Std_BoxSelection/pl.md) lub [Wybór elementów ramką zaznaczenia](Std_BoxElementSelection/pl.md):

1.  Upewnij się, że żadne narzędzie nie jest aktywne.
2.  Wykonaj jedną z następujących czynności:
    -   Kliknij w pustym obszarze i przeciągnij prostokąt od lewej do prawej, aby zaznaczyć elementy leżące całkowicie wewnątrz prostokąta.
    -   Kliknij w pustym obszarze i przeciągnij prostokąt od prawej do lewej, aby zaznaczyć również elementy, które dotykają lub przecinają prostokąt.

Można zaznaczać krawędzie i punkty w ramkach, ale nie można zaznaczać wiązań.



### Zaznaczanie połączonej geometrii w widoku 3D 


{{Version/pl|1.0}}

Dwukrotne kliknięcie krawędzi w widoku 3D spowoduje zaznaczenie wszystkich krawędzi bezpośrednio i pośrednio połączonych z tą krawędzią poprzez punkty końcowe. Nie ma potrzeby, aby krawędzie były połączone [więzem zbieżności](Sketcher_ConstrainCoincident/pl.md), punkty końcowe muszą mieć tylko te same współrzędne.



### Zaznaczanie w oknie dialogowym szkicownika 

Krawędzie i punkty można również wybierać z sekcji Elementy [okna dialogowego](Sketcher_Dialog/pl.md), a wiązania z sekcji Wiązania tego okna dialogowego.



## Kopiowanie, wycinanie i wklejanie 


{{Version/pl|1.0}}

Standardowe skróty klawiaturowe **Ctrl** + **C**, wycinania, **Ctrl** + **X**, **Ctrl** + **V** mogą być używane do kopiowania, wycinania i wklejania wybranej geometrii Szkicownika wraz z powiązanymi ograniczeniami. Narzędzia te są również dostępne w menu **Szkic → Narzędzia szkicownika**. Można ich używać w ramach tego samego szkicu, ale także między różnymi szkicami lub oddzielnymi instancjami FreeCAD. Ponieważ dane są kopiowane do schowka w postaci kodu Python, mogą być również wykorzystywane w inny sposób *(np. udostępniane na forum)*.



## Przybory

Narzędzia środowiska pracy szkicownika znajdują się w menu Szkic i/lub na kilku paskach narzędziowych. {{Version/pl|0.21}}: Prawie wszystkie paski narzędzi szkicownika są wyświetlane tylko wtedy, gdy szkic jest w trybie edycji. Jedynym wyjątkiem jest pasek narzędzi [szkicownika](#Pasek_narzędzi_szkicownika.md), który jest wyświetlany tylko wtedy, gdy żaden szkic nie jest w trybie edycji.

Niektóre narzędzia są również dostępne z menu kontekstowego [Widoku 3D](3D_view/pl.md), gdy szkic jest w trybie edycji, lub z menu kontekstowego [okna dialogowego szkicownika](Sketcher_Dialog/pl.md).


{{Version/pl|0.21}}

: Jeśli szkic jest w trybie edycji, pasek narzędzi **Konstrukcja** jest ukryty, ponieważ żadne z jego narzędzi nie może być wtedy użyte.



### Informacje ogólne 



#### Pasek narzędzi szkicownika 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Utwórz szkic](Sketcher_NewSketch/pl.md): Tworzy nowy szkic i otwiera [okno dialogowe szkicownika](Sketcher_Dialog/pl.md), aby go edytować.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edycja szkicu](Sketcher_EditSketch/pl.md): Edytuj wybrany szkic. Otwiera [Okna dialogowego Szkicownika](Sketcher_Dialog/pl.md) do edycji istniejącego szkicu.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Mapuj szkic na płaszczyznę](Sketcher_MapSketch/pl.md): Dołącza szkic do wybranej geometrii.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Zmień orientacje szkicu](Sketcher_ReorientSketch/pl.md): Umieszcza szkic na jednej z głównych płaszczyzn z opcjonalnym przesunięciem. Może być również używane do odłączania szkicu.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md): Potrafi analizować i naprawiać szkic, którego nie można już edytować lub który zawiera nieprawidłowe wiązania, a także dodawać brakujące wiązania zbieżne.

-   <img alt="" src=images/Sketcher_MergeSketch.svg  style="width:32px;"> [Połącz szkice](Sketcher_MergeSketches.md): Łączy ze sobą dwa lub więcej szkiców.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Odbicie lustrzane](Sketcher_MirrorSketch.md): Odbicie szkicu w poprzek ich osi X, osi Y, lub punktu początku układu współrzędnych.



#### Pasek narzędzi trybu edycji szkicownika 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Opuść szkic](Sketcher_LeaveSketch/pl.md): Kończy tryb edycji szkicu i zamyka [okno dialogowe](Sketcher_Dialog/pl.md) Szkicownka.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Widok szkicu](Sketcher_ViewSketch/pl.md): Wyrównuje [widok 3D](3D_view/pl.md) ze szkicem.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Zobacz przekrój](Sketcher_ViewSection/pl.md): Uaktywnia tymczasową płaszczyznę przekroju, która ukrywa wszelkie obiekty i części obiektów znajdujące się przed płaszczyzną szkicu.



#### Pasek narzędzi edycji szkicownika 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Przełącz widoczność siatki](Sketcher_Grid/pl.md): Włącza lub wyłącza siatkę w aktualnie edytowanym szkicu. Ustawienia można zmienić w powiązanym menu. {{Version/pl|0.21}}

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Przełącz przyciąganie](Sketcher_Snap/pl.md): Włącza lub wyłącza przyciąganie we wszystkich szkicach. Ustawienia można zmienić w powiązanym menu. {{Version/pl|0.21}}

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Konfiguruj kolejność renderowania](Sketcher_RenderingOrder/pl.md): Kolejność renderowania wszystkich szkiców można zmienić w powiązanym menu. {{Version/pl|0.21}}.



#### Pozostałe

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Przerwij operację](Sketcher_StopOperation/pl.md): Zatrzymuje aktualnie uruchomione narzędzie do tworzenia geometrii lub wiązań.



### Geometria w szkicowniku 

Poniżej znajdują się narzędzia do tworzenia obiektów.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Utwórz punkt na szkicu](Sketcher_CreatePoint/pl.md): Twotrzy punkt.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Utwórz polilinię](Sketcher_CreatePolyline/pl.md): Tworzy serię segmentów linii i łuków połączonych punktami końcowymi. Narzędzie ma kilka trybów.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Utwórz linię na szkicu](Sketcher_CreateLine/pl.md): Tworzy linię. {{Version/pl|1.0}}: Narzędzie ma trzy tryby.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz łuk:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Utwórz łuk przez środek](Sketcher_CreateArc/pl.md): Tworzy łuk na podstawie jego środka i punktów końcowych. {{Version/pl|1.0}}: Lub przez punkty końcowe i punkt wzdłuż łuku.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Utwórz łuk przez trzy punkty na obwodzie](Sketcher_Create3PointArc.md): Tworzy łuk na podstawie jego punktów końcowych i punktu wzdłuż łuku. <small>(v1.0)</small> : Jest to to samo narzędzie co [Utwórz łuk przez środek](Sketcher_CreateArc/pl.md), ale z innym trybem początkowym.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Utwórz łuk na podstawie elipsy](Sketcher_CreateArcOfEllipse/pl.md): Tworzy łuk elipsy według punktu środkowego, głównego promienia, punktu początkowego i końcowego.

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Utwórz łuk na podstawie hiperboli](Sketcher_CreateArcOfHyperbola/pl.md): Twotzy łuk hiperboli.

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Utwórz łuk na podstawie paraboli](Sketcher_CreateArcOfParabola/pl.md): Twotzy łuk paraboli.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Tworzy okrąg / elipsę:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Utwórz okrąg przez środek](Sketcher_CreateCircle/pl.md): Tworzy okrąg przez jego środek i punkt wzdłuż okręgu. {{Version/pl|1.0}}: Lub przez trzy punkty wzdłuż okręgu.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Utwórz okrąg przez trzy punkty](Sketcher_Create3PointCircle.md): Tworzy okrąg przez trzy punkty wzdłuż okręgu. <small>(v1.0)</small> : Jest to to samo narzędzie co [Utwórz okrąg przez środek](Sketcher_CreateCircle/pl.md), ale z innym trybem początkowym.

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Utwórz elipsę przez środek](Sketcher_CreateEllipseByCenter/pl.md): Tworzy elipsę według jej środka, punktu końcowego jednej z jej osi i punktu wzdłuż elipsy. {{Version/pl|1.0}}: Lub przez oba punkty końcowe jednej z jej osi i punkt wzdłuż elipsy.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Utwórz elipsę przez trzy punkty](Sketcher_CreateEllipseBy3Points/pl.md): Tworzy elipsę przez punkty końcowe jednej z jej osi i punkt wzdłuż elipsy. {{Version/pl|1.0}}: Jest to to samo narzędzie co [Utwórz elipsę przez środek](Sketcher_CreateEllipseByCenter/pl.md), ale z innym trybem początkowym.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz prostokąt:

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Utwórz prostokąt](Sketcher_CreateRectangle/pl.md): Tworzy prostokąt. {{Version/pl|1.0}}: Narzędzie ma cztery tryby. Zaokrąglone rogi i tworzenie kopii z przesunięciem są funkcjami opcjonalnymi.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Prostokąt wyśrodkowany](Sketcher_CreateRectangle_Center/pl.md): Tworzy wyśrodkowany prostokąt. {{Version/pl|1.0}}: Jest to to samo narzędzie co [Utwórz prostokąt](Sketcher_CreateRectangle/pl.md), ale z innym trybem początkowym.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Prostokąt zaokrąglony](Sketcher_CreateOblong/pl.md): Tworzy zaokrąglony prostokąt. Analogicznie.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz wielokąt foremny:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Trójkąt](Sketcher_CreateTriangle/pl.md): tworzy trójkąt równoboczny. {{Version/pl|1.0}}: Jest to to samo narzędzie co [Utwórz wielokąt foremny](Sketcher_CreateRegularPolygon/pl.md), ale z liczbą boków ustawioną na określoną wartość.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Kwadrat](Sketcher_CreateSquare/pl.md): Tworzy kwadrat. Analogicznie.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pięciokąt](Sketcher_CreatePentagon/pl.md): Tworzy pięciokąt foremny. Analogicznie.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Sześciokąt](Sketcher_CreateHexagon/pl.md): Tworzy sześciokąt foremny. Analogicznie.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Siedmiokąt](Sketcher_CreateHeptagon/pl.md): Tworzy siedmiokąt foremny. Analogicznie.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Ośmiokąt](Sketcher_CreateOctagon.md): Tworzy ośmiokąt foremny. Analogicznie.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Wielokąt foremny](Sketcher_CreateRegularPolygon/pl.md): Tworzy wielokąt foremny. Można określić liczbę boków.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz owal:

  - <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Utwórz szczelinę](Sketcher_CreateSlot/pl.md): Rysuje owal.

-   <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Utwórz szczelinę łukową](Sketcher_CreateArcSlot/pl.md): Rysuje owal na łuku. {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Tworzy krzywą złozoną:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Krzywa złożona przez punkty kontrolne](Sketcher_CreateBSpline/pl.md): Tworzy krzywą złożoną za pomocą punktów kontrolnych. {{Version/pl|1.0}}: Lub za pomocą węzłów.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Okresowa krzywa złożona przez punkty kontrolne](Sketcher_CreatePeriodicBSpline/pl.md): Tworzy okresową *(zamkniętą)* krzywą złożoną za pomocą punktów kontrolnych. {{Version/pl|1.0}}: To jest to samo narzędzie co [Krzywa złożona przez punkty kontrolne](Sketcher_CreateBSpline/pl.md), ale z innym trybem początkowym.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [Krzywa złozona przez węzły](Sketcher_CreateBSplineByInterpolation/pl.md): Tworzy krzywą złożoną przez węzły.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Okresowa krzywa złożona przez węzły](Sketcher_CreatePeriodicBSplineByInterpolation/pl.md): Tworzy okresową krzywą złożoną przez węzły.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md): Przełącza narzędzia do tworzenia geometrii do / z trybu konstrukcyjnego lub przełącza wybraną geometrię do / z geometrii konstrukcyjnej.



### Wiązania w szkicowniku 

Są to narzędzia do tworzenia [wiązań](#Wiązania.md). Niektóre z nich wymagają użycia [wiązań pomocniczych](Sketcher_helper_constraint/pl.md).

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Wiązanie wymiaru:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Wiązanie odległości](Sketcher_Dimension/pl.md): Jest kontekstowym narzędziem wiązań w środowisku pracy Szkicownika. Na podstawie bieżącego wyboru oferuje odpowiednie wiązania wymiarowe, ale także wiązania geometryczne. {{Version/pl|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md): Określa odległość poziomą między dwoma punktami lub punktami końcowymi linii. Jeśli wstępnie wybrano pojedynczy punkt, odległość jest określana względem początku szkicu.

  - <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md): Określa odległość pionową między dwoma punktami lub punktami końcowymi linii. Jeśli wstępnie wybrano pojedynczy punkt, odległość jest określana względem początku szkicu.

  - <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md): Określa długość prostej, odległość między dwoma punktami, odległość prostopadłą między punktem a prostą, lub <small>(v0.21)</small> , odległość między krawędziami dwóch okręgów lub łuków, lub między krawędzią okręgu lub łuku a prostą lub {{Version/pl|1.0}}, odległość między krawędziami dwóch łuków.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Zwiąż automatycznie promień / średnicę](Sketcher_ConstrainRadiam/pl.md): Określa promień łuków i okręgów z wagą krzywej złożonej oraz średnicę okręgów. 

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Wiązanie promienia](Sketcher_ConstrainRadius/pl.md): Określa promień okręgów i łuków oraz okręgów z wagą krzywej złożonej.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Wiązanie średnicy](Sketcher_ConstrainDiameter/pl.md): Określa średnicę okręgów i łuków.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Wiązanie kąta](Sketcher_ConstrainAngle/pl.md): Określa kąt między dwiema krawędziami, kąt linii z poziomą osią szkicu lub kąt apertury łuku kołowego.

  - <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Wiązanie blokady odległości](Sketcher_ConstrainLock/pl.md): Stosuje więzy [Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md) i [Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md) do punktów. Jeśli wybrany jest pojedynczy punkt, wiązania odnoszą się do początku szkicu. Jeśli wybrano dwa lub więcej punktów, wiązania odnoszą się do ostatnio wybranego punktu.

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Wiązanie zbieżności punktów (ujednolicone)](Sketcher_ConstrainCoincidentUnified/pl.md): Tworzy wiązanie zbieżności między punktami, ustala punkty na krawędziach lub osiach lub tworzy wiązanie koncentryczności. Łączy w sobie narzędzia wiązań [zbieżności](Sketcher_ConstrainCoincident/pl.md) i [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md): Tworzy wiązanie zbieżne między punktami lub wiązanie współosiowe.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Zwiąż punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md): Mocuje punkty na krawędziach lub osiach.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Wiązanie poziomo / pionowo:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Wiązanie poziomo / pionowo](Sketcher_ConstrainHorVer/pl.md): Wiąże linie lub pary punktów, aby były poziome lub pionowe, w zależności od tego, co jest najbliższe bieżącemu wyrównaniu. Łączy narzędzia [poziomo](Sketcher_ConstrainHorizontal/pl.md) i [pionowo](Sketcher_ConstrainVertical/pl.md). {{Version/pl|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Wiązanie poziome](Sketcher_ConstrainHorizontal/pl.md): Ustawia linie lub pary punktów jako poziome.

  - <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Wiązanie pionowe](Sketcher_ConstrainVertical/pl.md): Ogranicza linie lub pary punktów do pionu.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Wiązanie równoległości](Sketcher_ConstrainParallel/pl.md): Wymusza, aby linie były równoległe.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Wiązanie prostopadłości](Sketcher_ConstrainPerpendicular/pl.md): Wymusza, aby dwie linie były prostopadłe, dwie krawędzie lub krawędź i oś były prostopadłe na ich przecięciu. Wiązanie może również łączyć dwie krawędzie, wymuszając ich prostopadłość w miejscu połączenia.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Wiązanie styczności](Sketcher_ConstrainTangent/pl.md): Wymusza, aby dwie krawędzie lub krawędź i oś były styczne. Wiązanie może również łączyć dwie krawędzie, wymuszając ich styczność w miejscu połączenia. Jeśli wybrane zostaną dwie linie, staną się one współliniowe.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Wiązanie równości](Sketcher_ConstrainEqual/pl.md): Narzuca, aby krawędzie *(linie)* lub krzywizny miały jednakową długość *(krawędzie z wyjątkiem krzywych złożonych)*.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md): Wymusza symetrię dwóch punktów wokół prostej, osi lub wokół trzeciego punktu.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Wiązanie zablokowania](Sketcher_ConstrainBlock/pl.md): Blokuje krawędzie w miejscu za pomocą pojedynczego wiązania. Jest przeznaczony głównie dla krzywych złożonych.

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> \[\[Sketcher_ConstrainSnellsLaw/pl\|Wiązanie refrakcji\] (prawo Snell\'a)\]: Wiąże dwie linie zgodnie z prawem załamania światła, aby symulować światło przechodzące przez interfejs.

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Przełącz wiązania:

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md): Przełącza narzędzia do tworzenia wiązań wymiarowych między trybem konstrukcyjnym a trybem informacyjnym lub przełącza wybrane wiązania wymiarowe między tymi trybami.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Aktywuj / dezaktywuj wiązanie](Sketcher_ToggleActiveConstraint.md): Włącza lub dezaktywuje istniejące wiązania.



### Narzędzia szkicownika 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Tworzy zaokrąglenie / sfazowanie:

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Utwórz zaokrąglenie](Sketcher_CreateFillet/pl.md): Tworzy zaokrąglenie między dwiema krawędziami, które nie są równoległe. {{Version/pl|1.0}} Narzędzie może również tworzyć fazki.

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Utwórz sfazowanie](Sketcher_CreateChamfer/pl.md): Tworzy fazę między dwiema nierównoległymi krawędziami. Jest to to samo narzędzie co [Zaokrąglenie](Sketcher_CreateFillet/pl.md), ale z innym trybem początkowym. {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edytuj krawędź:

  - <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Przytnij krawędź](Sketcher_Trimming/pl.md): Przycina krawędź na najbliższych przecięciach z innymi krawędziami.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Podziel](Sketcher_Split/pl.md): Dzieli krawędź na dwie części z zachowaniem większości więzów.

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Rozszerz krawędź \...](Sketcher_Extend.md): Wydłuża lub skraca linię lub łuk do dowolnego miejsca lub do docelowej krawędzi lub punktu.

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometria zewnętrzna](Sketcher_External/pl.md): Rzutuje krawędzie i / lub wierzchołki należące do obiektów spoza szkicu na płaszczyznę szkicu. {{VersionMinus/pl|1.0}}

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Geometria zewnętrzna:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Utwórz geometrię zewnętrzną rzutowania](Sketcher_Projection/pl.md): Tworzy krawędzie rzutowania geometrii zewnętrznej. {{Version/pl|1.1}}

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Utwórz geometrię zewnętrzną przecięcia](Sketcher_Intersection.md): Tworzy krawędzie przecięcia geometrii zewnętrznej z płaszczyzną szkicu. {{Version/pl|1.1}}

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Kalka techniczna](Sketcher_CarbonCopy/pl.md): Kopiuje całą geometrię i wiązania z innego szkicu do aktywnego szkicu.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Wybierz odniesienie położenia](Sketcher_SelectOrigin/pl.md): Wybiera punkt początkowy szkicu.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Wybierz oś poziomą](Sketcher_SelectHorizontalAxis/pl.md): Zaznacza poziomą oś szkicu.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Wybierz oś pionową](Sketcher_SelectVerticalAxis/pl.md): Wybór osi pionowej szkicu.

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Przekształcanie w szyku](Sketcher_Translate/pl.md): Przekształca lub opcjonalnie kopiuje wybrane geometrie. {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Przemieszczenie biegunowe](Sketcher_Rotate/pl.md): Obraca lub opcjonalnie tworzy obrócone kopie wybranych elementów. {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Przekształcenie skali](Sketcher_Scale/pl.md): Skaluje lub opcjonalnie tworzy skalowane kopie wybranych elementów. {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Geometria odsunięcia](Sketcher_Offset/pl.md): Tworzy równoodległe krawędzie wokół wybranych krawędzi. {{Version/pl|1.0}}

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Tworzy symetryczna geometrię \...](Sketcher_Symmetry/pl.md): Tworzy kopię wybranego elementu szkicu, symetrycznie względem wybranej linii.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Usuń wyrównanie osi](Sketcher_RemoveAxesAlignment/pl.md): Usuwa wyrównanie osi wybranych krawędzi, zastępując wiązania [Poziomo](Sketcher_ConstrainHorizontal/pl.md) i [Pionowo](Sketcher_ConstrainVertical/pl.md) wiązaniami [Równolegle](Sketcher_ConstrainParallel/pl.md) i [Prostopadle](Sketcher_ConstrainPerpendicular/pl.md).

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Usuń wszystkie geometrie](Sketcher_DeleteAllGeometry/pl.md): Usuwa całą geometrię i wszystkie wiązania ze szkicu.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Usuń wszystkie wiązania](Sketcher_DeleteAllConstraints/pl.md): Usuwa wszystkie wiązania ze szkicu.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Kopiowanie w Szkicowniku: Zobacz akapit [Kopiuj, wycinaj i wklejaj](#Kopiowanie,_wycinanie_i_wklejanie.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Wycinanie w Szkicowniku: Zobacz akapit [Kopiuj, wycinaj i wklejaj](#Kopiowanie,_wycinanie_i_wklejanie.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Wklej w Szkicowniku: Zobacz [Kopiuj, wytnij i wklej](#Kopiowanie,_wycinanie_i_wklejanie.md).



### Narzędzia szkicownika dla krzywych złożonych 

-   <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:32px;"> [Konwertuj geometrie na krzywą złożoną](Sketcher_BSplineConvertToNURBS/pl.md) Konwertuje krawędzie na krzywą złożoną.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Zwiększ stopień krzywej złożonej](Sketcher_BSplineIncreaseDegree/pl.md) Zwiększa stopień *(kolejność)* krzywej złożonej.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Zmniejsz stopień krzywej złożonej](Sketcher_BSplineDecreaseDegree/pl.md) Zmniejsza stopień *(krotność)* krzywej złożonej.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Zwiększyć liczebność węzłów](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md) Zwiększa krotność węzła krzywej złożonej.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Zmniejsz liczbę węzłów](Sketcher_BSplineDecreaseKnotMultiplicity/pl.md) Zmniejsza krotność węzła krzywej złożonej.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Wstaw węzeł](Sketcher_BSplineInsertKnot/pl.md) Wstawia węzeł do krzywej złożonej lub zwiększa krotność istniejącego węzła.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Połącz krzywe](Sketcher_JoinCurves/pl.md) Tworzy krzywą złożoną poprzez połączenie dwóch istniejących krzywych złożonych lub innych krawędzi. {{Version/pl|0.21}}



### Widok szkicu 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Wybierz nie związane stopnie swobody](Sketcher_SelectElementsWithDoFs/pl.md): Zaznacza w szkicu nie w pełni związane elementy.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Wybierz powiązane wiązania](Sketcher_SelectConstraints/pl.md): Wybiera wiązania powiązane z elementami szkicu.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Zaznacz powiązaną geometrię](Sketcher_SelectElementsAssociatedWithConstraints/pl.md): Wybiera elementy szkicu powiązane z wiązaniami.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Wybierz zbędne wiązania](Sketcher_SelectRedundantConstraints/pl.md): Wybiera zbędne wiązania w szkicu.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Wybierz wiązania konfliktowe](Sketcher_SelectConflictingConstraints/pl.md): Wybiera kolidujące ze sobą wiązania szkicu.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Pokaż / ukryj okrąg pomocniczy dla łuków](Sketcher_ArcOverlay/pl.md): Pokazuje lub ukrywa okrągłe elementy pomocnicze *(wirtualne okręgi)* dla łuków we wszystkich szkicach. {{Version/pl|0.22}}

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Pokaż / ukryj warstwę informacyjną krzywej złożonej:

  - <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Pokaż / ukryj stopnie krzywej złożonej](Sketcher_BSplineDegree/pl.md) Pokazuje lub ukrywa wyświetlanie stopnia krzywej złożonej we wszystkich szkicach.

  - <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Pokaż / ukryj ramkę kontrolną krzywej złożonej](Sketcher_BSplinePolygon/pl.md) Pokazuje lub ukrywa wyświetlanie wielokąta kontrolnego krzywej złożonej we wszystkich szkicach.

  - <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Pokaż / ukryj grzebień krzywizny krzywej złożonej](Sketcher_BSplineComb/pl.md) Pokazuje lub ukrywa wyświetlanie grzebienia krzywizny krzywej złożonej we wszystkich szkicach.

  - <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Zwiększ / zmniejsz wielokrotność węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md) Pokazuje lub ukrywa wyświetlanie krotności węzła krzywej złożonej we wszystkich szkicach.

  - <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Wyświetl / ukryj wagę punktu kontrolnego krzywej złożonej](Sketcher_BSplinePoleWeight/pl.md) Pokazuje lub ukrywa wyświetlanie wag punktów kontrolnych krzywej złożonej we wszystkich szkicach.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md): Usuwa wewnętrzną geometrię elementów lub odtwarza brakującą geometrię wewnętrzną.

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Przełącz przestrzeń wirtualną](Sketcher_SwitchVirtualSpace/pl.md): Umożliwia ukrycie wszystkich wiązań szkicu i ponowne ich wyeksponowanie lub przełącza widoczną przestrzeń wirtualną.



### Narzędzia przestarzałe 

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Tworzy proste kopie elementu \...](Sketcher_Clone/pl.md): Klonuje wybrany element w szkicowniku. Nie dostępne dla {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Zamknij kształt](Sketcher_CloseShape/pl.md): Tworzy zamknięty kształt, stosując wiązania zgodności względem punktów końcowych.

To narzędzie jest przestarzałe, nie będzie dostępne od ({{VersionPlus/pl|0.21}})

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Utwórz zaokrąglenie z zachowaniem wiązań](Sketcher_CreatePointFillet/pl.md): Tworzy zaokrąglenie między dwiema nierównoległymi liniami, zachowując ich punkt narożny. Niedostępne w {{VersionPlus/pl|1.0}}

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Połącz krawędzie](Sketcher_ConnectLines/pl.md): Połącz elementy szkicu poprzez zastosowanie zbieżnych ograniczeń do punktów końcowych.

To narzędzie jest przestarzałe, nie będzie dostępne od ({{VersionPlus/pl|0.21}})

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Kopia](Sketcher_Copy/pl.md): Kopiuje element szkicu. Nie dostępne dla {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Przesuń](Sketcher_Move.md): Przesuwa wybraną geometrię, biorąc za punkt odniesienia ostatni wybrany punkt. Nie dostępne dla {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Szyk prostokątny](Sketcher_RectangularArray/pl.md): Tworzy tablicę wybranych elementów szkicownika. Nie dostępne dla {{VersionPlus/pl|1.0}}



## Ustawienia

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Ustawienia](Sketcher_Preferences.md): Konfiguracja Środowiska pracy Szkicownik.



## Dobre praktyki 

Każdy użytkownik CAD z biegiem czasu rozwija swój własny sposób pracy, ale istnieją pewne przydatne ogólne zasady, którymi należy się kierować.

-   Seria prostych szkiców jest łatwiejsza do wykonania niż jeden złożony szkic. Na przykład, pierwszy szkic może być utworzony dla podstawowej cechy 3D *(wyciągnięcie, albo wyciągniecie przez obrót)*, podczas gdy drugi może zawierać otwory lub wycięcia *(kieszenie)*. Niektóre szczegóły mogą zostać pominięte, które zostaną zrealizowane później jako cechy 3D. Możesz wybrać unikanie zaokrągleń w szkicu, jeśli jest ich zbyt wiele, i dodać je jako cechy 3D.
-   Zawsze twórz profil zamknięty, inaczej Twój szkic nie stworzy bryły, ale raczej zestaw otwartych ścian. Jeśli nie chcesz, aby niektóre obiekty zostały włączone do bryły, przekształć je w elementy konstrukcyjne za pomocą narzędzia **Tryb konstrukcji**.
-   Użyj funkcji automatycznych wiązań, aby ograniczyć liczbę wiązań, które musisz dodać ręcznie.
-   Z reguły najpierw należy zastosować ograniczenia geometryczne, potem ograniczenia wymiarowe, a następnie zablokować szkic jako ostatni. Ale pamiętaj: reguły są tworzone po to, aby je łamać. Jeśli masz problemy z manipulowaniem szkicem, przydatne może być związanie najpierw kilku obiektów przed ukończeniem profilu.
-   Jeśli to możliwe, wyśrodkuj szkic do punktu początkowego *(0,0)* z wiązaniem blokady. Jeśli Twój szkic nie jest symetryczny, zlokalizuj jeden z jego punktów w punkcie początkowym lub wybierz ładne okrągłe liczby dla odległości blokady.
-   Jeśli masz możliwość wyboru między wiązaniem długości a wiązaniem poziomym lub pionowym, preferowane są te ostatnie. Ograniczenia odległości poziomej i pionowej są mniej obciążające obliczeniowo.
-   Ogólnie rzecz biorąc, najlepsze ograniczenia, których należy użyć, to:
    Wiązania poziome i pionowe; Wiązania poziome i pionowe długości, styczność punkt-punkt.
    Jeśli to możliwe, należy ograniczyć użycie następujących wiązań:
    ogólne wiązanie długości, styczność krawędzi do krawędzi, ustalenie punktu do związania linii, wiązanie symetrii.
-   Jeśli masz wątpliwości co do poprawności szkicu po jego ukończeniu *(elementy zmieniają kolor na zielony)*, zamknij okno dialogowe Szkicownika, i użyj narzędzia <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;">. [sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md).



## Poradniki

-   [Poradnik dla szkicownika](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) według chrisb. Jest to ponad 80-cio stronicowy dokument PDF, który służy za szczegółową instrukcję obsługi szkicownika. Wyjaśniono w nim podstawy użytkowania środowiska pracy Szkicownik i omówiono wiele szczegółów dotyczących tworzenia kształtów geometrycznych i każdego z ograniczeń.
-   [Podstawy Środowiska pracy Szkicownik](Basic_Sketcher_Tutorial/pl.md) dla początkujących.
-   [Szkicownik Mikro poradnik - Praktyki dotyczące wiązań](Sketcher_Micro_Tutorial_-_Constraint_Practices/pl.md)
-   [Szkicownik: wymagania wobec szkicu](Sketcher_requirement_for_a_sketch/pl.md) Minimalne wymagania dotyczące szkicu i kompletne określenie szkicu.



## Tworzenie skryptów 

Strona [skrypty szkicownika](Sketcher_scripting.md) zawiera przykłady tworzenia wiązań przez skrypty środowiska Python.



## Przykłady

Aby uzyskać kilka pomysłów na to, co można osiągnąć za pomocą narzędzi środowiska Szkicownik, zajrzyj do: [przykładów](Sketcher_Examples/pl.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/pl
