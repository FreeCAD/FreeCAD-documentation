---
 TutorialInfo:l
   Topic:  Drafting
   Level:  początkujący
   Time:  30 minut
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei and vocx
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/viewtopic.php?f=36&t=43651 Zaktualizowany projekt samouczka
---

# Draft tutorial/pl







## Wprowadzenie

Ten poradnik został pierwotnie napisany przez Drei i został zaktualizowany i odnowiony przez vocx.

Ten poradnik ma na celu zapoznanie czytelnika z podstawowym przepływem pracy środowiska pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md).

Czytelnik przećwiczy:

-   tworzenie linii, łuków i wielokątów,
-   korzystanie z płaszczyzn roboczych,
-   tworzenie wymiarów, tekstu i ciągów kształtów,
-   tworzenie rysunków technicznych.

Ten samouczek używa notacji {{Value|(x, y, z)}} do oznaczania współrzędnych wymaganych do zdefiniowania punktów w obiekcie. Domyślną jednostką są milimetry {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Rysunek końcowy zawierający różne obiekty środowiska Rysunek Roboczy.*



## Sposób postępowania 

1\. Uruchom FreeCAD, utwórz nowy pusty dokument za pomocą opcji z menu **Plik → [<img src=images/Std_New.svg style="width:16px"> [Nowy](Std_New/pl.md)**.

:   1.1. Przełącz się do środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) z [selektora środowisk pracy](Std_Workbench.md), lub menu **Widok → Środowiska pracy → [<img src=images/Workbench_Draft.svg style="width:16px"> Rysunek Roboczy**.
:   1.2. Upewnij się, że rozumiesz jak używać [edytora właściwości](Property_editor/pl.md), w szczególności zakładek **Dane** i **Widok** do zmiany właściwości. Podczas zmiany właściwości może być konieczne wykonanie **<img src="images/Std_Refresh.svg" width=16px> [odświeżenia](Std_Refresh/pl.md)**, aby zobaczyć rezultat w oknie [widoku 3D](3D_view/pl.md).
:   1.3. Ponieważ obiekty środowiska Rysunek Roboczy są płaskimi kształtami, lepiej oglądać je od góry. Użyj **[<img src=images/Std_ViewTop.svg style="width:16px"> [widoku od góry](Std_ViewTop/pl.md)**, aby ustawić [widok 3D](3D_view/pl.md).
:   1.4. Chociaż siatka nie jest używana w tym samouczku, jest pomocna w pozycjonowaniu elementów geometrycznych. Użyj narzędzia **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Wybór płaszczyzny roboczej](Draft_SelectPlane/pl.md)**, aby ustawić zarówno płaszczyznę roboczą, jak i siatkę, a następnie pokazać i ukryć siatkę za pomocą narzędzia **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md)**.



## Pasek narzędzi przyciągania 

2\. Pasek narzędzi [przyciągania](Draft_Snap/pl.md) jest zwykle aktywowany po przejściu do środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).

:   2.1. Aby upewnić się, że zawsze tam jest, przejdź do [ustawień](Draft_Preferences/pl.md), **Edycja → Preferencje → Rysunek Roboczy → Zakładka Siatka i przyciąganie**.
:   2.2. Sprawdź, czy pasek narzędzi **Pokaż narzędzia przyciągania** jest aktywny.

W tym samym oknie można również zmienić widoczność i właściwości siatki środowiska Rysunek Roboczy.



## Płaszczyzny robocze 

Większość obiektów środowiska Rysunek Roboczy to płaskie kształty, więc są one naturalnie oparte na **płaszczyźnie roboczej**. Płaszczyzna robocza może być jedną z głównych globalnych płaszczyzn współrzędnych XY, XZ i YZ lub może być płaszczyzną równoległą do nich z dodatnim lub ujemnym przesunięciem, lub może być płaszczyzną zdefiniowaną przez powierzchnię obiektu bryłowego.

3\. Naciśnij przycisk **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Wybierz płaszczyznę](Draft_SelectPlane/pl.md)**, lub przejdź do menu **Narzędzia → [<img src=images/Draft_SelectPlane.svg style="width:16px"> [Wybierz płaszczyznę](Draft_SelectPlane/pl.md)**, aby otworzyć [panel zadań](Task_panel/pl.md) płaszczyzny roboczej.

:   3.1. Naciśnij **[<img src=images/Std_ViewTop.svg style="width:16px"> Góra (XY)**.

Przed naciśnięciem przycisku można również zmienić wartość odsunięcia w milimetrach, a także odstępy siatki, linie główne i promień przyciągania.



## Linie i łuki 

4\. Będziemy tworzyć łuki i linie.

:   4.1. Naciśnij **[<img src=images/Draft_Arc.svg style="width:16px"> [Łuk](Draft_Arc.md)**.
:   4.2. Ustaw **Środek** na {{Value|(0, 0, 0)}} i naciśnij klawisz **Enter**.
:   4.3. Ustaw **Promień** na {{Value|30 mm}} i naciśnij **Enter**.
:   4.4. Ustaw **Kąt początkowy** na {{Value|60.0°}} i naciśnij **Enter**.
:   4.5. Ustaw **Kąt otwarcia** na {{Value|60.0°}} i naciśnij **Enter**.
:   4.6. Powtórz tę samą procedurę dla drugiego łuku o promieniu {{Value|25 mm}}, pozostałe właściwości są takie same.

5\. Utworzymy teraz profil zamknięty, wiążąc łuki liniami.

:   5.1. Naciśnij **[<img src=images/Draft_Line.svg style="width:16px"> [Linia](Draft_Line/pl.md)**.
:   5.2. Na pasku narzędzi [przyciągania](Draft_Snap/pl.md) upewnij się, że aktywna jest tylko opcja **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md)** oraz tylko **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md)**. Po przesunięciu kursora na łuk i zbliżeniu do jednego z jego punktów końcowych, powinna pojawić się ikona <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> [24px](Draft_Snap_Endpoint.svg.md) [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md). Ponadto punkt docelowy jest wyróżniony dużą białą kropką. Kliknij, aby wybrać ten punkt.
:   5.3. Przesuń kursor do najbliższego punktu końcowego drugiego łuku, aby połączyć oba łuki.
:   5.4. Powtórz proces dla drugiej strony łuku, aby zamknąć profil.

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Profil zamknięty utworzony przez dwa łuki i dwie linie.*



## Łączenie lub montaż 

Mamy teraz kilka obiektów w [widoku drzewa](Tree_view/pl.md), które tworzą zamknięty profil. Jednak profil ten nadal składa się z rozłącznych obiektów. Każdy z nich może być edytowany i przenoszony niezależnie od pozostałych. Możliwe jest kontynuowanie pracy z elementami w ten sposób, ale możliwe jest również połączenie ich w jeden obiekt.

6a. Należy pamiętać, że połączenie obiektów w jeden obiekt spowoduje utworzenie obiektu, który nie jest już parametryczny, więc ich właściwości nie mogą być dalej modyfikowane. 6a.1. Zaznacz wszystkie cztery obiekty w oknie [widoku drzewa](Tree_view/pl.md) lub przytrzymując **Ctrl** i wybierając je w oknie [widoku 3D](3D_view/pl.md).

:   6a.2. Po zaznaczeniu tych obiektów kliknij **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Ulepsz](Draft_Upgrade/pl.md)**.

Ulepszy to cztery obiekty w jeden {{Value|polilinię}}.

6b. Jeśli chcesz zachować parametryczną naturę obiektów, możesz zamiast tego utworzyć złożenie.

:   6b.1. Przejdź do środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).
:   6b.2. Po zaznaczeniu tych obiektów, kliknij na **[<img src=images/Part_Compound.svg style="width:16px"> [Utwórz kształt złożony](Part_Compound/pl.md)**.



## Prostokąty, okręgi i wielokąty 

7\. Narysujemy prostokątną ramkę. *(Przełącz się z powrotem do środowiska <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md))*.

:   7.1. Utwórz **[<img src=images/Draft_Rectangle.svg style="width:16px"> [Prostokąt](Draft_Rectangle/pl.md)**.
:   7.2. Wprowadź wartości pierwszego punktu {{Value|(-100, -60, 0)}} i naciśnij **Enter**.
:   7.3. Upewnij się, że opcja **Relatywnie** jest odznaczona, ponieważ będziemy używać jednostek bezwzględnych. Możesz nacisnąć **R** na klawiaturze, aby szybko włączyć lub wyłączyć tę opcję.
:   7.4. Wprowadź wartości dla drugiego punktu {{Value|(140, 90, 0)}} i naciśnij **Enter**.

Utworzony zostanie prostokąt. Przejdź do [edytora właściwości](Property_editor.md), aby zmienić jego właściwości. Jeśli nie chcesz, aby prostokąt tworzył ścianę, ustaw właściwość **Utwórz ścianę** na wartość {{FALSE/pl}}. Jeśli chcesz utworzyć ścianę, ale widzieć tylko przewody tego obiektu, ustaw **Utwórz ścianę** na {{TRUE/pl}}, ale ustaw **Tryb wyświetlania** na {{Value|Szkieletowy}}.

8\. Narysujemy okrąg.

:   8.1. Naciśnij przycisk **[<img src=images/Draft_Circle.svg style="width:16px"> [Okrąg](Draft_Circle/pl.md)**.
:   8.2. Wprowadź wartości środka {{Value|(0, 0, 0)}} i naciśnij **Enter**.
:   8.3. Ustaw promień na {{value|15 mm}} i naciśnij **Enter**.

9\. Narysujemy wielokąt foremny.

:   9.1. Naciśnij **[<img src=images/Draft_Polygon.svg style="width:16px"> [Wielokąt](Draft_Polygon/pl.md)**.
:   9.2. Wprowadź wartości położenia środka {{Value|(0, 0, 0)}} i naciśnij **Enter**.
:   9.3. Ustaw liczbę boków na {{Value|6}} i naciśnij **Enter**.
:   9.4. Ustaw promień na {{Value|50 mm}} i naciśnij **Enter**.

Ponownie, jeśli chcesz, możesz zmienić właściwości **Utwórz ścianę** i **Tryb wyświetlania** w [edytorze właściwości](Property_editor/pl.md).

Prostokąt, okrąg, wielokąt i większość innych obiektów utworzonych za pomocą środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) współdzielą wiele danych i właściwości widoku, ponieważ wywodzą się z tej samej klasy bazowej, [Część: Część na obiekt 2D](Part_Part2DObject/pl.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Dodano prostokąt, okrąg i wielokąt.*



## Szyki

Szyki są używane do powielania obiektu kilka razy w kierunku prostopadłym *(X, Y, Z)*, wokół osi obrotu lub wzdłuż ścieżki.

10\. Utworzymy szyk biegunowy.

:   10.1. Wybierz obiekt {{Value|Polilinia}}, który został wcześniej utworzony za pomocą narzędzia **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Ulepsz](Draft_Upgrade/pl.md)** lub obiekt {{Value|Kształt złożony}} utworzony za pomocą narzędzia **[<img src=images/Part_Compound.svg style="width:16px"> [Utwórz kształt złożony](Part_Compound.md)** środowiska Część.
:   10.2. Naciśnij przycisk **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Szyk biegunowy](Draft_PolarArray/pl.md)**.
:   10.3. Ustaw kąt biegunowy na {{Value|360°}}.
:   10.4. Ustaw liczbę elementów na {{Value|4}}.
:   10.5. Wprowadź wartości środka obrotu {{Value|(0, 0, 0)}} i naciśnij **Enter**.

Obiekt tablicy pokazuje kopie obiektu wokół punktu odniesienia położenia.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Szyk biegunowy małego profilu wyśrodkowanego wokół punktu odniesienia położenia.*



## Wymiary

Wymiary liniowe działają najlepiej przy użyciu odpowiednich metod [przyciągania](Draft_Snap/pl.md) do wybierania punktów i krawędzi do pomiaru. Można je jednak również utworzyć, określając współrzędne bezwzględne.

11\. Tworzenie wymiarów dla różnych obiektów.

:   11.1. Naciśnij **[<img src=images/Draft_Dimension.svg style="width:16px"> [Dimension](Draft_Dimension/pl.md)**.
:   11.2. Wybierz pierwszy punkt. W tym poradniku pierwszym punktem będzie zawsze początek {{Value|(0, 0, 0)}}.
:   11.3. Na pasku narzędzi [przyciągania](Draft_Snap/pl.md) upewnij się, że narzędzie **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md)** jest aktywne i wybrano tylko funkcję **[<img src=images/Draft_Snap_Midpoint.svg style="width:16px"> [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md)**. Gdy przesuniesz wskaźnik do górnej krawędzi wielokąta, <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> powinna pojawić się ikona [Punkt środkowy](Draft_Snap_Midpoint/pl.md). Kliknij, aby wybrać ten punkt.
:   11.4. Przesuń kursor w prawo, aby określić położenie wymiaru, a następnie kliknij, aby ustawić ostateczne położenie, około {{Value|(100, 20, 0)}}. Wymiar automatycznie wyświetli wartość długości zmierzoną między dwoma punktami.
:   11.5. Wybierz obiekt wymiaru w [widoku drzewa](Tree_view/pl.md), a następnie w [edytorze właściwości](Property_editor.md) zmień **Rozmiar czcionki** na {{Value|6 mm}}, ustaw **Linie pomocnicze** na {{Value|45 mm}}, a **Wyświetlaj jednostki** na {{FALSE/pl}}.

12\. Powtórz ten proces dla dwóch łuków profilu zamkniętego. Pierwszy punkt pomiaru nadal będzie początkiem, dla drugiego punktu użyj <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md) łuku.

13\. Powtórz ten proces dla okręgu znajdującego się w środku. Pierwszy punkt pomiaru nadal będzie punktem początkowym. Aby wybrać drugi punkt, upewnij się, że narzędzie **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Włącz / wyłącz przyciąganie](Draft_Snap_Lock/pl.md)** jest aktywne, i wybrano tylko funkcję **[<img src=images/Draft_Snap_Angle.svg style="width:16px"> [Przyciągnij do kąta](Draft_Snap_Angle/pl.md)**. Gdy przesuniesz kursor do górnej części okręgu, powinna pojawić się ikona <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Przyciągnij do kąta](Draft_Snap_Angle/pl.md). Kliknij, aby zaznaczyć ten punkt. Następnie przesuń kursor w prawo i kliknij, aby ustalić wymiar.

Pamiętaj, aby dostosować **Rozmiar czcionki** i inne właściwości, aby poprawnie zobaczyć wymiar.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Wymiary mierzące pionową odległość od punktu odniesienia położenia do górnej krawędzi okręgu, łuku i wielokąta.*



## Adnotacje wieloliniowe i kształt z tekstu 

14\. Obiekty tekstowe są prostymi figurami płaskimi, które są tworzone w oknie [widoku 3D](3D_view/pl.md), ale nie mają pod spodem rzeczywistego \"[kształtu](Shape/pl.md)\". Oznacza to, że nie mogą być używane w złożonych operacjach z kształtami, takich jak wyciągnięcia lub operacje logiczne.

:   14.1. Naciśnij przycisk **[<img src=images/Draft_Text.svg style="width:16px"> [Adnotacja wieloliniowa](Draft_Text/pl.md)**.
:   14.2. Wybierz punkt odniesienia w oknie [widoku 3D](3D_view/pl.md). Na pasku narzędzi [przyciągania](Draft_Snap/pl.md) upewnij się, że narzędzie **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md)** jest aktywne i wybrano tylko funkcję **[<img src=images/Draft_Snap_Midpoint.svg style="width:16px"> [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md)**. Przesuń kursor do górnej krawędzi najwyższego łuku, tak aby <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> pojawi się ikona [Przyciągnij do punktu środkowego](Draft_Snap_Midpoint/pl.md). Kliknij, aby wybrać ten punkt.
:   14.3. Wpisz wymagany **Tekst** i naciśnij **Enter** raz, aby rozpocząć nową linię. W razie potrzeby dodaj więcej linii tekstu.
:   14.4. Gdy zakończysz edycję, naciśnij **Enter** dwa razy.
:   14.5. Zaznacz obiekt tekstowy w oknie [widoku drzewa](Tree_view/pl.md), a następnie w oknie [edytora właściwości](Property_editor/pl.md) zmień wartość własciwości **Rozmiar czcionki** na {{Value|6 mm}}, a właściwość **Wyrównanie poziome** na {{Value|Wyśrodkowane}}.

15\. Obiekty **Kształt z tekstu** to kształty wykonane z pierwotnych polilini, które podążają za liniami wskazanymi przez określoną czcionkę. Oznacza to, że obiekty te mają prawdziwy \"[kształt](Shape/pl.md)\" pod spodem, a zatem mogą być używane w złożonych operacjach, takich jak wyciągnięcia i operacje logiczne.

:   15.1. Naciśnij przycisk **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Kształt z tekstu](Draft_ShapeString/pl.md)**.
:   15.2. Przesuń kursor do żądanego miejsca w oknie [widoku 3D](3D_view/pl.md) nad regularnym wielokątem i kliknij raz. Spowoduje to ustalenie punktu bazowego dla Kształtu z tekstu. Współrzędne można również wprowadzić ręcznie, na przykład {{Value|(-20, 65, 0)}}.
:   15.3. Wprowadź żądany **Ciąg znaków** i wybierz odpowiednią **Wysokość**.
:   15.4. Jeśli nie ma domyślnego pliku czcionki, należy kliknąć wielokropek **...**, aby otworzyć okno dialogowe umożliwiające wybranie lokalizacji czcionki w systemie.
:   15.5. Po określeniu prawidłowego pliku czcionki można kliknąć **OK** lub nacisnąć **Enter**.

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Dodano obiekty Adnotacja wieloliniowa i Kształt z tekstu.*

Aby wytłaczać litery i grawerować je na bryłach, zobacz poradnik [Poradnik: Rysunek Roboczy kształt z tekstu](Draft_ShapeString_tutorial/pl.md).



## Tworzenie rysunku technicznego 

W obecnej formie stworzone przez nas obiekty można zapisać, wyeksportować do innych formatów, takich jak [SVG](SVG.md) lub [DXF](DXF.md), lub wydrukować.

Jeśli chcesz, możesz utworzyć rysunek techniczny, aby wyświetlić te obiekty wraz z dodatkowymi informacjami, takimi jak ramka.

Zanim cokolwiek zrobisz, ukryj siatkę Rysunku Roboczego naciskając **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md)**.

16\. Przejdź do środowiska pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Roboczy](TechDraw_Workbench/pl.md).

:   16.1. Utwórz standardową stronę naciskając **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [Wstaw nową domyślną stronę rysunku](TechDraw_PageDefault/pl.md)**.
:   16.2. W oknie [widoku drzewa](Tree_view/pl.md) zaznacz wszystkie utworzone obiekty z wyjątkiem strony, a następnie naciśnij **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [Wstaw aktywny widok](TechDraw_ActiveView/pl.md)**. Naciśnij **OK** z domyślnymi opcjami. Utworzenie widoku na stronie może potrwać kilka sekund.
:   16.3. Wybranie obiektu strony w oknie [widoku drzewa](Tree_view/pl.md) spowoduje automatyczne wyświetlenie strony w oknie głównym. Po wybraniu strony przejdź do [edytora właściwości](Property_editor/pl.md) i zmień właściwość **Skala** na {{Value|0.75}}.
:   16.4. Rozwiń obiekt Strona w oknie [widoku drzewa](Tree_view/pl.md), aby wybrać obiekt AktywnyWidok. Po wybraniu tego widoku przejdź do [edytora właściwości](Property_editor/pl.md) i zmień właściwość **Typ skali** na {{Value|Strona}}.
:   16.5. Ponownie oblicz model używając narzędzia **[<img src=images/Std_Refresh.svg style="width:16px"> [Przelicz](Std_Refresh/pl.md)** lub naciskając **F5**.
:   16.6. Ukryj ramki obiektów naciskając **[<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md)**.

Dowiedz się więcej o środowisku pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) czytając poradnik [Podstawy dla środowiska pracy Rysunek Techniczny](Basic_TechDraw_Tutorial/pl.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*Strona Rysunku Technicznego z rzutem kształtów utworzonych za pomocą środowiska Rysunek Roboczy.*

Rysunek Techniczny działa najlepiej z obiektami, które mają [kształt topologiczny](Part_TopoShape/pl.md). Ponieważ niektóre obiekty ze środowiska Rysunek Roboczy, takie jak [Adnotacja wieloliniowa](Draft_Text/pl.md) i [Wymiary](Draft_Dimension/pl.md), nie mają takich \"[kształtów](Shape/pl.md)\", niektóre operacje środowiska Rysunek Techniczny nie działają z tymi elementami.

Narzędzia takie jak **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [Wstaw aktywny widok](TechDraw_ActiveView/pl.md)**, **[<img src=images/TechDraw_DraftView.svg style="width:16px"> [Wstaw obiekt środowiska Rysunek Roboczy](TechDraw_DraftView/pl.md)**, oraz **[<img src=images/TechDraw_ArchView.svg style="width:16px"> [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md)** działają poprzez odbieranie wewnętrznego obrazu SVG, który jest generowany przez wewnętrzne funkcje środowiska Rysunek Roboczy. Dlatego środowisko pracy Rysunek Techniczny nie ma dużej kontroli nad sposobem wyświetlania tych widoków. Większa integracja tych dwóch środowisk pracy jest w toku.



## Uwagi końcowe 

Środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) pod wieloma względami jest podobne do środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md), ponieważ oba są przeznaczone do tworzenia kształtów 2D. Główna różnica polega na sposobie, w jaki każde ze środowisk pracy obsługuje układy współrzędnych i sposób pozycjonowania obiektów. W Rysunku Roboczym obiekty są swobodnie pozycjonowane w globalnym układzie współrzędnych, zazwyczaj przyciągając swoje punkty do siatki lub innych obiektów. W Szkicowniku **[obiekt szkicu](Sketch/pl.md)** definiuje lokalny układ współrzędnych, który służy jako odniesienie dla wszystkich elementów geometrycznych w tym szkicu. Co więcej, szkic opiera się na *wiązaniach* w celu zdefiniowania ostatecznej pozycji jego punktów.

-   Środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) jest przeznaczone dla rysunków 2D, które nadają się do rysowania na siatce. Środowisko pracy [Architektura](Arch_Workbench/pl.md) opiera się głównie na narzędziach zdefiniowanych w środowisku [Rysunek Roboczy](Draft_Workbench/pl.md).

-   Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) jest przeznaczone do rysunków 2D, które wymagają precyzyjnych relacji między punktami. Nie opiera się ono na siatce, ale na regułach pozycjonowania *(wiązaniach)* w celu określenia, gdzie zostaną umieszczone punkty i krawędzie. [Szkicownik](Sketcher_Workbench/pl.md) jest najczęściej używany razem ze środowiskiem [Projekt Części](PartDesign_Workbench/pl.md) do tworzenia brył.

-   Możliwe jest przekształcenie obiektu środowiska Rysunek Roboczy w [Szkic](Sketch/pl.md) i na odwrót, przy użyciu narzędzia **[<img src=images/Draft_Draft2Sketch.svg style="width:16px"> [Rysunek roboczy do szkicu](Draft_Draft2Sketch/pl.md)**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft tutorial/pl
