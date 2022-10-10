# <img alt="Ikonka FreeCAD dla Środowiska pracy Szkicownik " src=images/Workbench_Sketcher.svg  style="width   *64px;"> Sketcher Workbench/pl


{{TOCright}}

## Wprowadzenie

FreeCAD <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Środowisko pracy Szkicownik](Sketcher_Workbench/pl.md) służy do tworzenia geometrii 2D przeznaczonych do wykorzystania w Środowiskach pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Projekt części](PartDesign_Workbench/pl.md), <img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> [Arch](Arch_Workbench/pl.md) i innych. Ogólnie rzecz biorąc, rysunek 2D jest uważany za punkt wyjścia dla większości modeli CAD, ponieważ szkic 2D może być **wyciągany** do tworzenia kształtu 3D. Kolejne szkice 2D mogą być wykorzystywane do tworzenia następnych elementów detalu, takich jak kieszenie, grzbiety lub wytłoczki na górze uprzednio zbudowanych kształtów 3D. Wraz z operacjami logicznymi zdefiniowanymi w Środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/pl.md), Sketcher stanowi podstawę [konstrukcyjnej geometrii bryłowej](Constructive_solid_geometry.md) *(CSG)* metody budowania brył. Ponadto wraz z operacjami dostępnymi w <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> środowisku [Projekt części](PartDesign_Workbench/pl.md) Szkicownik stanowi również podstawę do metody tworzenia brył.

Środowisko pracy Szkicownik posiada **wiązania**, dzięki czemu kształty 2D mogą podążać za precyzyjnymi definicjami geometrycznymi pod względem długości, kątów i relacji *(poziomość, pionowość, prostopadłość itp.)*. Narzędzie do tworzenia wiązań oblicza wymagany zakres geometrii 2D i umożliwia przeprowadzenie interaktywnej eksploracji stopni swobody szkicu.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width   *450px;"> 
*W pełni związany szkic.*

## Podstawy szkicowania z wiązaniami 

Aby wyjaśnić, jak działa Szkicownik, przydatne może być porównanie go z \"tradycyjnym\" sposobem sporządzania projektu.

#### Kreślenie tradycyjne 

Tradycyjna metoda rysowania CAD pochodzi od dawnej [deski kreślarskiej](http   *//en.wikipedia.org/wiki/Drawing_board). [Rzuty prostopadłe *(2D)*](http   *//en.wikipedia.org/wiki/Multiview_orthographic_projection) są kreślone ręczenie z przeznaczeniem do tworzenia rysunków technicznych. Obiekty są rysowane precyzyjnie w zamierzonej skali lub wymiarze. Jeśli chcesz narysować poziomą linię o długości 100mm startującą w punkcie (0,0), musisz aktywować narzędzie linii, kliknąć na ekranie bądź wprowadzić współrzędne (0,0) dla pierwszego punktu, następnie wykonać kolejne kliknięcie lub wprowadzić współrzędnie dla drugiego punktu (0,100). Ewentualnie możesz narysować linię bez określanie jej pozycji i przesunąć ją później. Kiedy skończysz rysować geometrię, nadajesz jej wymiary.

#### Szkicowanie z więzami 

**Szkicownik** odchodzi od tej logiki. Obiekty nie muszą być rysowane dokładnie tak, jak zamierzasz, ponieważ zostaną później zdefiniowane przez wiązania. Obiekty mogą być rysowane luźno i tak długo, jak długo pozostają niezwiązane, mogą być modyfikowane. Są one w efekcie pływające i mogą być przesuwane, rozciągane, obracane, skalowane i tak dalej. Daje to dużą elastyczność w procesie projektowania.

#### Czym są wiązania 

Zamiast wymiarów, wiązania są stosowane w celu ograniczenia stopnia swobody obiektu. Na przykład, linia bez wiązań ma 4 [stopnie swobody](#Degrees_Of_Freedom/pl.md) *(w skrócie \"DOF\")*   * można ją przesuwać w poziomie lub w pionie, można ją rozciągać i obracać.

Wykorzystanie wiązania poziomego lub pionowego, lub wiązania kąta *(względem innej linii lub jednej z osi)*, ograniczy jej zdolność do obracania pozostawiając ją z 3 stopniami swobody. Zablokowanie jednego z punktów w relacji do układu współrzędnych usunie kolejne dwa stopnie. W końcu zastosowanie wiązania wymiaru usunie ostatni stopień swobody. Linia jest w wtedy uznawana za **w pełni ograniczoną więzami**.

Wiele obiektów może być ze sobą związanych. Dwie linie mogą być połączone poprzez jeden z ich punktów za pomocą wiązania punktów zbieżnych. Mogą być ustawiane między sobą pod kątem lub prostopadle. Linia może być styczna do łuku lub okręgu i tak dalej. Złożony szkic z wieloma obiektami będzie miał wiele różnych rozwiązań, a uczynienie go **w pełni ograniczonym** oznacza, że tylko jedno z tych możliwych rozwiązań zostało osiągnięte w oparciu o zastosowane ograniczenia.

Są dwa typy wiązań   * geometryczne i wymiarowe. Są one opisane dokładnej w poniższej sekcji [Narzędzia](#Narzędzia.md).

#### Do czego Szkicownik nie jest dobry 

Szkicownik nie jest przeznaczony do wykonywania planów 2D. Gdy szkice zostaną użyte do wygenerowania bryły, są one automatycznie ukrywane. Ograniczenia są widoczne tylko w trybie edycji szkicu.

Jeśli potrzebujesz stworzyć tylko widoki 2D do druku, a nie chcesz tworzyć modeli 3D, sprawdź Środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md). W przeciwieństwie do elementów szkicownika, szkice obiektów nie używają wiązań. Są to proste kształty zdefiniowane w momencie tworzenia. Zarówno środowisko Rysunek roboczy jak i Szkicownik mogą być używane do rysowania geometrii 2D i tworzenia brył 3D, chociaż ich preferowane zastosowanie jest inne.
Szkicownik jest zwykle używany razem z środowiskiem [Część](Part_Workbench/pl.md) i [Projekt części](PartDesign_Workbench/pl.md) do tworzenia brył. Środowisko Rysunek roboczy jest zwykle używane do wykonywania prostych rysunków planarnych na siatce, jak podczas rysowania architektonicznego planu piętra. W takich sytuacjach Środowisko Rysunek roboczy jest najczęściej używane razem ze Środowiskiem pracy [Architektura](Arch_Workbench/pl.md). Narzędzie [Draft2Sketch](Draft_Draft2Sketch.md) konwertuje obiekt środowiska Rysunek roboczy na obiekt Szkicownika i vice versa. Wiele narzędzi, które potrzebują elementu 2D jako wejścia do pracy z każdym typem obiektu wykonuje automatycznie konwersję wewnętrzną.

## Szkicowanie - schemat pracy 

Szkic jest zawsze dwuwymiarowy *(2D)*. Aby utworzyć bryłę, tworzony jest płaski szkic pojedynczego zamkniętego obszaru, a następnie zostaje albo wypełniony albo obracany, aby dodać trzeci wymiar. W ten sposób tworzona jest przestrzenna bryła z płaskiego szkicu.

Jeśli szkic posiada odcinki, które się krzyżują, miejsca, w których punkt nie znajduje się bezpośrednio na odcinku, lub miejsca, w których występują przerwy pomiędzy punktami końcowymi sąsiednich odcinków, wyciągnięcie lub wyciągnięcie przez obrót nie stworzą bryły. Czasami szkic, który zawiera przecinające się linie, będzie działał dla prostej operacji, takiej jak wyciągnięcie, ale późniejsze operacje, takie jak Linear Pattern, nie powiodą się. Najlepiej jest unikać krzyżowania linii. Wyjątkiem od tej reguły jest sytuacja, dla elementów konstrukcyjnych *(niebieskich)*.

Wewnątrz zamkniętego obszaru możemy mieć mniejsze powierzchnie nie zachodzące na siebie. Będą to puste przestrzenie, gdy zostanie utworzona bryła 3D.

Gdy szkic jest w pełni związany, jego elementy zmienią kolor na zielony, geometria konstrukcji pozostanie niebieska. Zazwyczaj jest on gotowy w tym miejscu i nadaje się do wykorzystania przy tworzeniu bryły przestrzennej. Jednakże, gdy okno dialogowe Szkic jest zamknięte, warto przejść do Środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Część](Part_Workbench/pl.md) i uruchomić funkcję **[<img src=images/Part_CheckGeometry.svg style="width   *16px"> [Sprawdź geometrię](Part_CheckGeometry/pl.md)**, aby upewnić się, że w Szkicu nie ma elementów, które mogą spowodować późniejsze problemy.

## Przybory

Wszystkie narzędzia Środowiska prascy Szkicownik znajdują się w menu głównym **Szkicownik**, które pojawia się po załadowaniu tego środowiska pracy.

### Informacje ogólne 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> [Utwórz szkic](Sketcher_NewSketch/pl.md)   * Tworzy nowy szkic na wybranej powierzchni lub płaszczyźnie. Jeśli podczas uruchamiania tego narzędzia nie zostanie wybrana żadna ściana, użytkownik zostanie poproszony o wybranie płaszczyzny z wyskakującego okna.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width   *32px;"> [Edycja szkicu](Sketcher_EditSketch/pl.md)   * Edytuj wybrany szkic. Spowoduje to otwarcie [Okna dialogowego Szkicownika](Sketcher_Dialog/pl.md).

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width   *32px;"> [Opuść szkic](Sketcher_LeaveSketch/pl.md)   * Zamyka tryb edycji Środowiska pracy Szkicownik.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width   *32px;"> [Widok szkicu](Sketcher_ViewSketch/pl.md)   * Ustawia widok modelu prostopadle do płaszczyzny szkicu.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width   *32px;"> [Zobacz przekrój](Sketcher_ViewSection/pl.md)   * Tworzy płaszczyznę przekroju, która tymczasowo ukrywa jakąkolwiek zawartość przed płaszczyzną szkicu.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width   *32px;"> [Mapuj szkic na płaszczyznę](Sketcher_MapSketch/pl.md)   * Nanosi szkic na uprzednio wybraną ścianę bryły.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width   *32px;"> [Zmień orientacje szkicu](Sketcher_ReorientSketch/pl.md)   * Umożliwia dołączenie szkicu do jednej z głównych płaszczyzn.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width   *32px;"> [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md)   * Sprawdź odchylenie różnych punktów i dopasuj je.

-   <img alt="" src=images/Sketcher_MergeSketch.svg  style="width   *32px;"> [Połącz szkice](Sketcher_MergeSketches.md)   * Łączy ze sobą dwa lub więcej szkiców.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width   *32px;"> [Odbicie lustrzane](Sketcher_MirrorSketch.md)   * Odbicie szkicu wzdłuż osi x, osi y, lub punktu początku układu współrzędnych.

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width   *32px;"> [Przerwij operację](Sketcher_StopOperation/pl.md)   * w trybie edycji przerywa bieżącą operację, niezależnie od tego, czy jest to rysowanie, ustawianie wiązań, itp.

### Geometria w szkicowniku 

Poniżej znajdują się narzędzia do tworzenia obiektów.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width   *32px;"> [Utwórz punkt na szkicu](Sketcher_CreatePoint/pl.md)   * Rysuje punkt.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width   *32px;"> [Utwórz linię na szkicu](Sketcher_CreateLine/pl.md)   * Rysuje odcinek linii między 2 punktami. Linie są nieograniczone pod względem pewnych wiązań.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width   *48px;"> [Utwórz łuk](Sketcher_CompCreateArc/pl.md)   * Jest to ikona menu na pasku narzędzi szkicownika, która zawiera następujące funkcje   *

   ** <img alt="" src=images/Sketcher_CreateArc.svg  style="width   *32px;"> [Utwórz łuk w szkicowniku](Sketcher_CreateArc/pl.md)   * Rysuje odcinek łuku od punktu środka, uwzględniając promień, oraz punkt początkowy i punkt końcowy.

   ** <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width   *32px;"> [Utwórz łuk podając 3 punkty na obwodzie](Sketcher_Create3PointArc.md)   * Rysuje odcinek łuku z dwóch punktów końcowych i innego punktu na obwodzie.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width   *48px;"> [Utwórz okrąg \...](Sketcher_CompCreateCircle.md)   * Jest to ikona menu na pasku narzędzi szkicownika, która zawiera następujące funkcje   *

   ** <img alt="" src=images/Sketcher_CreateCircle.svg  style="width   *32px;"> [Rysuje okrąg przez punkt środkowy i na obwodzie](Sketcher_CreateCircle/pl.md)   * Rysuje koło na podstawie punktu środkowego i promienia.

   ** <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width   *32px;"> [Rysuje okrąg podając 3 punkty na obwodzie](Sketcher_Create3PointCircle.md)   * Rysuje okrąg z trzech punktów na obwodzie.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width   *48px;"> [Utwórz krzywą stożkową](Sketcher_CompCreateConic/pl.md)   * Szkicownik oferuje poniższe sekcje o kształcie stożka. W przeciwieństwie do krzywych złożonych mogą być one używane z różnego rodzaju wiązaniami, takimi jak [stycznie](Sketcher_ConstrainTangent/pl.md), [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md), lub [prostopadle](Sketcher_ConstrainPerpendicular.md).

   ** <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width   *32px;"> [Elipsa przez środek](Sketcher_CreateEllipseByCenter/pl.md)   * Rysuje elipsę według punktu środkowego, głównego promienia i małego promienia.

   ** <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width   *32px;"> [Ellipsa przez 3 punkty](Sketcher_CreateEllipseBy3Points/pl.md)   * Rysuje elipsę według średnicy głównej *(2 punkty)* i punktu mniejszego promienia.

   ** <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width   *32px;"> [Łuk elipsy przez środek \...](Sketcher_CreateArcOfEllipse/pl.md)   * Rysuje łuk elipsy według punktu środkowego, głównego promienia, punktu początkowego i końcowego.

   **<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width   *32px;"> [Łuk hiperboli przez środek \...](Sketcher_CreateArcOfHyperbola/pl.md)   * Rysuje łuk hiperboli.

   **<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width   *32px;"> [Łuk paraboli](Sketcher_CreateArcOfParabola/pl.md)   * Rysuje łuk paraboli.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width   *48px;"> [Utwórz krzywą złożoną](Sketcher_CompCreateBSpline/pl.md)   * Jest to ikona menu na pasku narzędzi Szkicownika, która zawiera następujące polecenia   *

   ** <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width   *32px;"> [Krzywa złożona przez punkty kontrolne](Sketcher_CreateBSpline/pl.md)   * Rysuje krzywą złożoną za pomocą punktów kontrolnych.

   ** <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width   *32px;"> [Okresowa krzywa złożona przez punkty kontrolne](Sketcher_CreatePeriodicBSpline/pl.md)   * Rysuje okresową *(zamkniętą)* krzywą złożoną za pomocą punktów kontrolnych.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width   *32px;"> [Utwórz linię łamaną w szkicu](Sketcher_CreatePolyline/pl.md)   * Rysuje linię złożoną z wielu segmentów linii. Naciśnięcie klawisza **M** podczas rysowania polilinii przełącza pomiędzy różnymi trybami.

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width   *48px;"> [Komponent utwórz prostokąt](Sketcher_CompCreateRectangles/pl.md)   * Jest to menu z ikonkami na pasku narzędzi Szkicownika, które zawiera następujące polecenia   * {{Version/pl|0.20}}

   ** <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width   *32px;"> [Utwórz prostokąt na szkicu](Sketcher_CreateRectangle/pl.md)   * Rysuje prostokąt na podstawie 2 przeciwległych punktów.

   ** <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width   *32px;"> [Utwórz wyśrodkowany prostokąt](Sketcher_CreateRectangle_Center/pl.md)   * Rysuje prostokąt w oparciu o punkt centralny i punkt na brzegu. {{Version/pl|0.20}}

   ** <img alt="" src=images/Sketcher_CreateOblong.svg  style="width   *32px;"> [Utwórz zaokrąglony prostokąt](Sketcher_CreateOblong/pl.md)   * Rysuje zaokrąglony prostokąt na podstawie dwóch przeciwległych punktów. {{Version/pl|0.20}}

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width   *48px;"> [Utwórz wielokąt foremny \...](Sketcher_CompCreateRegularPolygon/pl.md)   * Jest to ikona menu na pasku narzędzi szkicownika, która zawiera następujące funkcje   *

   ** <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width   *32px;"> [Trójkąt](Sketcher_CreateTriangle.md)   * Rysuje zwyczajny trójkąt wpisany w okrąg o geometrii konstrukcyjnej.

   ** <img alt="" src=images/Sketcher_CreateSquare.svg  style="width   *32px;"> [Kwadrat](Sketcher_CreateSquare.md)   * Rysuje zwykły kwadrat wpisany w okrąg o geometrii konstrukcyjnej.

   ** <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width   *32px;"> [Pięciokąt](Sketcher_CreatePentagon.md)   * Rysuje pięciokąt foremny wpisany w okrąg o geomertii konstrukcyjnej.

   ** <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width   *32px;"> [Sześciokąt](Sketcher_CreateHexagon.md)   * Rysuje sześciokąt foremny wpisany w okrąg o geometrii konstrukcyjnej.

   ** <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width   *32px;"> [Siedmiokąt](Sketcher_CreateHeptagon.md)   * Rysuje siedmiokąt foremny wpisany w okrąg o geometrii konstrukcyjnej.

   ** <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width   *32px;"> [Ośmiokąt](Sketcher_CreateOctagon.md)   * Rysuje ośmiokąt foremny wpisany w okrąg o geometrii konstrukcyjnej.

   ** <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width   *32px;"> [Wielokąt foremny](Sketcher_CreateRegularPolygon/pl.md)   * Rysuje wielokąt foremny, wybierając liczbę boków i wybierając dwa punkty, środek i jeden róg.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width   *32px;"> [Utwórz rowek \...](Sketcher_CreateSlot.md)   * Rysuje owal, wybierając środek jednego półkola i punkt końcowy drugiego półkola.

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width   *48px;"> [Komponent zaokrąglenie](Sketcher_CompCreateFillets/pl.md)   * Jest to menu ikon na pasku narzędziowym Szkicownika, które zawiera następujące polecenia   *

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width   *32px;"> [Utwórz zaokrąglenie](Sketcher_CreateFillet/pl.md)   * Tworzy zaokrąglenie między dwiema liniami, które nie są równoległe.

   ** <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width   *32px;"> [Utwórz zaokrąglenie z zachowaniem wiązań](Sketcher_CreatePointFillet/pl.md)   * Tworzy zaokrąglenie pomiędzy dwoma liniami które nie są równoległe, zachowując ich *(wirtualny)* punkt przecięcia.

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width   *32px;"> [Przytnij krawędź](Sketcher_Trimming/pl.md)   * Przycina linię, okrąg lub łuk w odniesieniu do klikniętego punktu.

-   <img alt="" src=images/Sketcher_Extend.svg  style="width   *32px;"> [Rozszerz krawędź \...](Sketcher_Extend.md)   * Wydłuża linię lub łuk do linii granicznej, łuku, elipsy, łuku elipsy lub punktu w przestrzeni.

-   <img alt="" src=images/Sketcher_Split.svg  style="width   *32px;"> [Podziel](Sketcher_Split/pl.md)   * Dzieli linię lub łuk na dwie części, przekształca okrąg w łuk, zachowując większość ograniczeń. {{Version/pl|0.20}}

-   <img alt="" src=images/Sketcher_External.svg  style="width   *32px;"> [Geometria zewnętrzna](Sketcher_External/pl.md)   * Tworzy krawędź połączoną z geometrią zewnętrzną.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width   *32px;"> [Kalka techniczna](Sketcher_CarbonCopy/pl.md)   * Wykona kopie geometrii innego szkicu.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width   *32px;"> [Przełącz geometrię konstrukcyjną](Sketcher_ToggleConstruction/pl.md)   * Przełącza geometrię szkicu z / do trybu konstrukcyjnego. Geometria konstrukcji jest pokazana na niebiesko i jest pomijana poza trybem edycji szkicu.

### Wiązania w szkicowniku 

Wiązania służą do definiowania długości, ustalania reguł pomiędzy elementami szkicu oraz blokowania szkicu wzdłuż osi pionowej i poziomej. Niektóre z tych wiązań wymagają użycia [pomocy](Sketcher_helper_constraint.md).

#### Więzy geometrii 

Ograniczenia te nie są zależne od danych liczbowych.

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *32px;"> [32px](Sketcher_ConstrainCoincident.md) [Utwórz wiązanie zgodności \...](Sketcher_ConstrainCoincident/pl.md)   * Umieszcza punkt na *(zbieżny z)* jednym lub kilku innych punktach.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *32px;"> [Zwiąż punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md)   * Umieszcza punkt na innym obiekcie, takim jak linia, łuk lub oś.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width   *32px;"> [Utwórz wiązanie pionowe \...](Sketcher_ConstrainVertical/pl.md)   * Wyrównuje wybrane linie lub elementy polilinii do rzeczywistej orientacji pionowej. Przed zastosowaniem tego wiązania można wybrać więcej niż jeden obiekt.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width   *32px;"> [Utwórz wiązanie poziome](Sketcher_ConstrainHorizontal/pl.md)   * Wyrównuje wybrane linie lub elementy polilinii do rzeczywistej orientacji poziomej. Przed zastosowaniem tego wiązania można wybrać więcej niż jeden obiekt.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width   *32px;"> [Utwórz wiązanie równoległości](Sketcher_ConstrainParallel/pl.md)   * Wiąże dwie lub więcej linii, równolegle do siebie.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width   *32px;"> [Utwórz wiązanie prostopadłości \...](Sketcher_ConstrainPerpendicular/pl.md)   * Wiąże dwie linie prostopadle do siebie, lub też wiąże linię prostopadłą do punktu końcowego łuku.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width   *32px;"> [Utwórz styczną \...](Sketcher_ConstrainTangent/pl.md)   * Tworzy wiązanie styczne pomiędzy dwoma wybranymi elementami lub wiązanie współliniowe pomiędzy dwoma segmentami linii. Segment linii nie musi leżeć bezpośrednio na łuku lub okręgu, aby został związany ze styczną do tego łuku lub okręgu.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width   *32px;"> [Utwórz wiązanie równości](Sketcher_ConstrainEqual/pl.md)   * Powoduje, że dwie wybrane elementy są sobie równe. Jeśli są używane na okręgach lub łukach, ich promienie będą ustawione jako równe.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *32px;"> [Utwórz wiązanie symetrii \...](Sketcher_ConstrainSymmetric/pl.md)   * Powoduje symetryczne związanie dwóch punktów względem linii lub też związanie pierwszych dwóch wybranych punktów symetrycznie względem trzeciego wybranego punktu.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width   *32px;"> [Utwórz wiązanie zablokowania](Sketcher_ConstrainBlock.md)   * blokuje ruch krawędzi, to znaczy zapobiega zmianie aktualnego położenia wierzchołków. Szczególnie przydatne powinno być ustalenie pozycji B-splajnów. Patrz [temat na forum Block Constraint](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Wiązania wymiarów 

Są to wiązania ściśle powiązane z danymi liczbowymi, dla których można użyć [wyrażeń](Expressions/pl.md). Dane mogą być pobierane ze środowiska pracy [arkusza kalkulacyjnego](Spreadsheet_Workbench/pl.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width   *32px;"> [Utwórz wiązanie blokady odległości \...](Sketcher_ConstrainLock/pl.md)   * Powoduje związanie wybranego elementu poprzez ustawienie odległości pionowych i poziomych w stosunku do punktu początkowego, blokując w ten sposób lokalizację tego elementu. Odległości te można później edytować.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width   *32px;"> [Ustal poziomą odległość \...](Sketcher_ConstrainDistanceX/pl.md)   * Ustala poziomą odległość pomiędzy dwoma punktami lub punktami końcowymi linii. Jeśli wybrana jest tylko jedna pozycja, odległość jest ustawiana względem punktu początkowego.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width   *32px;"> [Ustal pionową odległość \...](Sketcher_ConstrainDistanceY/pl.md)   * Ustala pionową odległość pomiędzy dwoma punktami lub punktami końcowymi linii. Jeśli wybrana jest tylko jedna pozycja, odległość jest ustawiana względem punktu początkowego.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width   *32px;"> [Wiązanie odległości \...](Sketcher_ConstrainDistance/pl.md)   * Określa odległość wybranej linii przez związanie jej długości, lub określa odległość między dwoma punktami przez związanie odległości między nimi.

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width   *48px;"> [Komponent wiązanie promień średnica](Sketcher_CompConstrainRadDia/pl.md)   * Jest to menu ikonek na pasku narzędziowym wiązań Szkicownika, które zawiera następujące polecenia   *

   ** <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width   *32px;"> [Zwiąż promień](Sketcher_ConstrainRadius/pl.md)   * Określa promień wybranego łuku lub okręgu poprzez związanie promienia.

   ** <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width   *32px;"> [Średnica](Sketcher_ConstrainDiameter/pl.md)   * Definiuje średnicę wybranego łuku lub okręgu poprzez związanie średnicy.

   ** <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width   *32px;"> [Radiam](Sketcher_ConstrainRadiam/pl.md)   * Automatycznie definiuje promień / średnicę wybranego łuku lub okręgu *(waga dla bieguna B-spline, średnica dla pełnego okręgu, promień dla łuku)* {{Version/pl|0.20}}.

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width   *32px;"> [Ustaw kąt linii \...](Sketcher_ConstrainAngle/pl.md)   * Określa kąt wewnętrzny między dwiema wybranymi liniami.

#### Wiązania specjalne 

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width   *32px;"> [Wiązanie refrakcji](Sketcher_ConstrainSnellsLaw/pl.md)   * Wiąże dwie linie zgodnie z prawem załamania światła, aby symulować światło przechodzące przez interfejs.

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width   *32px;"> [Zwiąż do wewnątrz](Sketcher_ConstrainInternalAlignment.md)   * Wyrównuje wybrane elementy do wybranego kształtu *(np. linia staje się główną osią elipsy)*.

#### Narzędzia wiązań 

Następujące narzędzia mogą być wykorzystane do zmiany działania wiązań   *

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width   *32px;"> [Przełącza pasek narzędzi \... do trybu odniesienia](Sketcher_ToggleDrivingConstraint.md)   * Przełącza pasek narzędzi lub wybrane wiązania do/z trybu odniesienia.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width   *32px;"> [Aktywuj / dezaktywuj wiązanie](Sketcher_ToggleActiveConstraint.md)   * Włączenie lub wyłączenie już istniejącego wiązania. {{Version/pl|0.19}}

### Narzędzia szkicownika 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width   *32px;"> [Wybierz nie związane stopnie swobody](Sketcher_SelectElementsWithDoFs/pl.md)   * Podświetla na zielono geometrię z stopniami swobody *(DOFs)*, tzn. nie w pełni związaną.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width   *32px;"> [Zamknij kształt](Sketcher_CloseShape/pl.md)   * Tworzy zamknięty kształt, stosując wiązania zgodności względem punktów końcowych.

To narzędzie jest przestarzałe, nie będzie dostępne w przyszłych wydaniach ({{VersionPlus/pl|1.0}})

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width   *32px;"> [Połącz krawędzie](Sketcher_ConnectLines/pl.md)   * Połącz elementy szkicownika poprzez zastosowanie zbieżnych ograniczeń do punktów końcowych.

To narzędzie jest przestarzałe, nie będzie dostępne w przyszłych wydaniach ({{VersionPlus/pl|1.0}})

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width   *32px;"> [Wybierz powiązane wiązania](Sketcher_SelectConstraints/pl.md)   * Wybiera wiązania elementu rysunku w szkicowniku.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width   *32px;"> [Zaznacz powiązaną geometrię](Sketcher_SelectElementsAssociatedWithConstraints/pl.md)   * Wskaż elementy rysunku powiązane z wiązaniami.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width   *32px;"> [Wybierz zbędne wiązania](Sketcher_SelectRedundantConstraints/pl.md)   * Wybiera zbędne wiązania w szkicu.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width   *32px;"> [Wybierz wiązania konfliktowe](Sketcher_SelectConflictingConstraints/pl.md)   * Wybiera kolidujące ze sobą wiązania szkicu.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width   *32px;"> [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md)   * Umożliwia odtworzenie brakującej lub usunięcie niepotrzebnej geometrii wewnętrznej wybranej elipsy, łuku elipsy, hiperboli, paraboli lub krzywej złożonej.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width   *32px;"> [Wybierz odniesienie położenia](Sketcher_SelectOrigin/pl.md)   * Wybiera punkt początkowy szkicu.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width   *32px;"> [Wybierz oś pionową](Sketcher_SelectVerticalAxis/pl.md)   * Wybór osi pionowej szkicu.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width   *32px;"> [Wybierz oś poziomą](Sketcher_SelectHorizontalAxis/pl.md)   * Zaznacza poziomą oś szkicu.

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width   *32px;"> [Tworzy symetryczna geometrię \...](Sketcher_Symmetry/pl.md)   * Tworzy kopię wybranego elementu, symetrycznie względem wybranej linii.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width   *32px;"> [Tworzy proste kopie elementu \...](Sketcher_Clone/pl.md)   * Klonuje wybrany element w szkicowniku.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width   *32px;"> [Kopia](Sketcher_Copy/pl.md)   * Kopiuje element szkicownika.

-   <img alt="" src=images/Sketcher_Move.svg  style="width   *32px;"> [Przesuń](Sketcher_Move.md)   * Przesuwa wybraną geometrię, biorąc za punkt odniesienia ostatni wybrany punkt.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width   *32px;"> [Szyk prostokątny](Sketcher_RectangularArray/pl.md)   * Tworzy tablicę wybranych elementów szkicownika.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width   *32px;"> [Usuń wyrównanie osi](Sketcher_RemoveAxesAlignment/pl.md)   * Usuń wyrównanie osi, próbując jednocześnie zachować relację wiązań zaznaczenia {{Version/pl|0.20}}.

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width   *32px;"> [Usuń wszystkie geometrie](Sketcher_DeleteAllGeometry/pl.md)   * Usuwa całą geometrię ze szkicu.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width   *32px;"> [Usuń wszystkie wiązania](Sketcher_DeleteAllConstraints/pl.md)   * Usuwa wszystkie wiązania ze szkicu.

### Narzędzia szkicownika dla krzywych złożonych 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width   *32px;"> [Pokaż / ukryj stopnie krzywej złożonej](Sketcher_BSplineDegree/pl.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width   *32px;"> [Pokaż / ukryj ramkę kontrolną krzywej złożonej](Sketcher_BSplinePolygon.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width   *32px;"> [Pokaż / ukryj grzebień krzywizny krzywej złożonej](Sketcher_BSplineComb.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width   *32px;"> [Zwiększ / zmniejsz wielokrotność węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width   *32px;"> [Wyświetl / ukryj wagę punktu kontrolnego krzywej złożonej](Sketcher_BSplinePoleWeight.md), {{Version/pl|0.19}}

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width   *32px;"> [Konwertuj geometrie na krzywą złożoną](Sketcher_BSplineApproximate.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width   *32px;"> [Zwiększ stopień krzywej złożonej](Sketcher_BSplineIncreaseDegree.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width   *32px;"> [Zmniejsz stopień krzywej złożonej](Sketcher_BSplineDecreaseDegree.md) {{Version/pl|0.19}}

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width   *32px;"> [Zwiększyć liczebność węzłów](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width   *32px;"> [Zmniejsz liczbność węzłów](Sketcher_BSplineDecreaseKnotMultiplicity/pl.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width   *32px;"> [Wstaw węzeł](Sketcher_BSplineInsertKnot/pl.md), <small>(v0.20)</small> 

### Wirtualna przestrzeń szkicownika 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width   *32px;"> [Przełącz przestrzeń wirtualną](Sketcher_SwitchVirtualSpace/pl.md)   * Umożliwia ukrycie wszystkich wiązań szkicu i ponowne ich wyeksponowanie.

## Ustawienia

-   <img alt="" src=images/Preferences-general.svg  style="width   *32px;"> [Ustawienia](Sketcher_Preferences.md)   * Konfiguracja Środowiska pracy **Szkicownik**.

## Dobre praktyki 

Każdy użytkownik CAD z biegiem czasu rozwija swój własny sposób pracy, ale istnieją pewne przydatne ogólne zasady, którymi należy się kierować.

-   Seria prostych szkiców jest łatwiejsza do wykonania niż jeden złożony szkic. Na przykład, pierwszy szkic może być utworzony dla podstawowej funkcji 3D *(wyciągnięcie, albo wyciągniecie przez obrót)*, podczas gdy drugi może zawierać otwory lub wycięcia *(kieszenie)*. Niektóre szczegóły mogą zostać pominięte, które zostaną zrealizowane później jako funkcje 3D. Możesz wybrać unikanie zaokrągleń w szkicu, jeśli jest ich zbyt wiele, i dodać je jako funkcję 3D.
-   Zawsze twórz profil zamknięty, inaczej Twój szkic nie stworzy bryły, ale raczej zestaw otwartych ścian. Jeśli nie chcesz, aby niektóre obiekty zostały włączone do bryły, przekształć je w elementy konstrukcyjne za pomocą narzędzia **Tryb konstrukcji**.
-   Użyj funkcji automatycznych wiązań, aby ograniczyć liczbę wiązań, które musisz dodać ręcznie.
-   Z reguły najpierw należy zastosować ograniczenia geometryczne, potem ograniczenia wymiarowe, a następnie zablokować szkic jako ostatni. Ale pamiętaj   * reguły są tworzone po to, aby je łamać. Jeśli masz problemy z manipulowaniem szkicem, przydatne może być związanie najpierw kilku obiektów przed ukończeniem profilu.
-   Jeśli to możliwe, wyśrodkuj szkic do punktu początkowego *(0,0)* z wiązaniem blokady. Jeśli Twój szkic nie jest symetryczny, zlokalizuj jeden z jego punktów w punkcie początkowym lub wybierz ładne okrągłe liczby dla odległości blokady.
-   Jeśli masz możliwość wyboru między wiązaniem długości a wiązaniem poziomym lub pionowym, preferowane są te ostatnie. Ograniczenia odległości poziomej i pionowej są mniej obciążające obliczeniowo.
-   Ogólnie rzecz biorąc, najlepsze ograniczenia, których należy użyć, to   *
    Wiązania poziome i pionowe; Wiązania poziome i pionowe długości; Styczność punkt-punkt.
    Jeśli to możliwe, należy ograniczyć użycie następujących wiązań   *
    ogólne wiązanie długości, styczność krawędzi do krawędzi, ustalenie punktu do związania linii, wiązanie symetrii.
-   Jeśli masz wątpliwości co do poprawności szkicu po jego ukończeniu *(elementy zmieniają kolor na zielony)*, zamknij okno dialogowe Szkicownik, przejdź do środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Część](Part_Workbench/pl.md) i uruchom **[<img src=images/Part_CheckGeometry.svg style="width   *16px"> [Sprawdź geometrię](Part_CheckGeometry/pl.md)**.

## Poradniki

-   [Poradnik dla szkicownika](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=30104) według chrisb. Jest to 70-stronicowy dokument PDF, który służy za szczegółową instrukcję obsługi szkicownika. Wyjaśniono w nim podstawy użytkowania środowiska pracy Szkicownik i omówiono wiele szczegółów dotyczących tworzenia kształtów geometrycznych i każdego z ograniczeń.
-   [Podstawy Środowiska pracy Szkicownik](Basic_Sketcher_Tutorial/pl.md) dla początkujących.
-   [Szkicownik Mikro poradnik - Praktyki dotyczące wiązań](Sketcher_Micro_Tutorial_-_Constraint_Practices/pl.md)
-   [Szkicownik   * wymagania wobec szkicu](Sketcher_requirement_for_a_sketch/pl.md) Minimalne wymagania dotyczące szkicu i kompletne określenie szkicu.

## Tworzenie skryptów 

Strona [skrypty szkicownika](Sketcher_scripting.md) zawiera przykłady tworzenia wiązań przez skrypty środowiska Python.





{{Sketcher_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/pl
