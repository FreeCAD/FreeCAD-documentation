---
 GuiCommand:
   Name: Arch Wall
   Name/pl: Architektura: Ściana
   MenuLocation: 3D / BIM  , Ściana
   Workbenches: BIM_Workbench/pl
   Shortcut: **W** **A**
   SeeAlso: 
---

# Arch Wall/pl



## Opis

Narzędzie **Ściana** tworzy obiekt Ściany od podstaw lub na bazie dowolnego innego obiektu opartego na [kształcie](Part_Workbench/pl.md) lub [siatce](Mesh_Workbench/pl.md). Ściana może być budowana bez żadnego obiektu bazowego, wtedy zachowuje się jak objętość sześcianu, korzystając z właściwości długości, szerokości i wysokości. Gdy budowana jest na istniejącym kształcie, ściana może być oparta na:

-   Obiekt **liniowy 2D**, taki jak linie, krawędzie, łuki lub szkice, w którym możesz zmienić grubość, wyrównanie *(prawo, lewo lub wyśrodkowane)* i wysokość. Właściwość długości nie ma wpływu.
-   Płaska **powierzchnia**, w której możesz zmieniać tylko wysokość. Właściwości długości i szerokości nie mają wpływu. Jeśli płaszczyzna bazowa jest pionowa, ściana użyje właściwości szerokości zamiast wysokości, pozwalając na budowę ścian z obiektów przypominających przestrzeń lub studia masy.
-   **Bryła**, w której właściwości długości, szerokości i wysokości nie mają wpływu. Ściana po prostu używa podstawowej bryły jako swojego kształtu.
-   **Siatka**, w której podstawowa siatka musi być zamkniętą, trójwymiarową bryłą.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Ściany zbudowane z linii, polilinii, ściany, bryły i szkicu.*

Ściany mogą także mieć obiekty dodawane lub odejmowane. Obiekty dodawane to inne obiekty, których kształty są łączone w kształt tej ściany, podczas gdy odejmowane stanowią ubytki. Dodatki i odejmowania mogą być obsługiwane za pomocą narzędzi [Dodaj](Arch_Add/pl.md) i [Arch Remove](Arch_Remove/pl.md). Dodatki i odejmowania nie mają wpływu na parametry ściany, takie jak wysokość i szerokość, które nadal można zmieniać. Ściany mogą także mieć automatyczną wysokość, jeśli są one zawarte w obiekcie wyższego poziomu, takim jak [piętra](Arch_Floor/pl.md). Wysokość musi być ustawiona na 0, wtedy ściana przyjmie wysokość określoną w obiekcie nadrzędnym.

Kiedy kilka ścian powinno się przecinać, musisz umieścić je w [podłodze](Arch_Floor/pl.md), aby ich geometria się przecinała.



## Użycie



### Kreślenie ścian od podstaw 

1.  Jest kilka sposobów wywołania tego narzędzia:
    -   Wciśnij przycisk **<img src="images/Arch_Wall.svg" width=16px> [Ściana](Arch_Wall/pl.md)**.
    -   Wybierz opcję **3D/BIM → <img src="images/Arch_Wall.svg" width=16px> Ściana** z menu.
    -   Użyj skrótu klawiszowego: **W** a następnie **A**.
2.  Kliknij pierwszy punkt w widoku 3D lub wprowadź współrzędne.
3.  Kliknij drugi punkt w widoku 3D lub wprowadź współrzędne.



### Kreślenie ściany na wybranym obiekcie 

1.  Wybierz jeden lub więcej obiektów bazowej geometrii (obiekt środowiska Rysunek Roboczy, szkic itd.).
2.  Wywołaj narzędzie jak opisano powyżej.
3.  Dostosuj właściwości takie jak wysokość lub szerokość.



## Opcje

-   Ściany dzielą wspólne właściwości i zachowania wszystkich [Komponentów Architektonicznych](Arch_Component/pl.md).
-   Wysokość, szerokość i wyrównanie ściany można ustawić podczas rysowania, za pomocą panelu zadań.
-   Przyciągając ścianę do istniejącej ściany, obie ściany zostaną połączone w jedną. Sposób, w jaki są one łączone, zależy od ich właściwości: Jeśli mają one taką samą szerokość, wysokość i wyrównanie, oraz jeśli opcja \"Połącz szkice bazowe ścian, jeśli to możliwe\" jest włączona w preferencjach Architektury, rezultatem będzie jedna ściana oparta na szkicu złożonym z kilku segmentów. W przeciwnym razie, ta druga ściana zostanie dodana do pierwszej jako obiekt dodany.
-   Naciśnij **X**, **Y** lub **Z** po pierwszym punkcie, aby ograniczyć drugi punkt do wybranej osi.
-   Aby wprowadzić współrzędne ręcznie, po prostu wpisz liczby, a następnie naciśnij **Enter** między każdą składową X, Y i Z.
-   Naciśnij **R** lub kliknij pole wyboru, aby zaznaczyć / odznaczyć pole **Względnie**. Jeśli tryb relatywny jest włączony, współrzędne drugiego punktu są względne względem pierwszego. Jeśli nie, są one bezwzględne, pobrane z punktu odniesienia położenia (0,0,0).
-   Naciśnij **Shift** podczas rysowania, aby [ograniczyć](Draft_Constrain/pl.md) drugi punkt poziomo lub pionowo w stosunku do pierwszego.
-   Naciśnij **Esc** lub przycisk **Anuluj**, aby przerwać bieżące polecenie.
-   Podwójne kliknięcie na ścianie w widoku drzewa po jej utworzeniu pozwala wejść w tryb edycji i uzyskać dostęp i modyfikować jej obiekty dołączone i odejmowane.
-   Wielowarstwowe ściany można łatwo tworzyć, budując kilka ścian z tego samego punktu odniesienia. Ustawiając ich właściwość Wyrównanie na lewo lub prawo oraz określając wartość Odsunięcie, można efektywnie skonstruować kilka warstw ściany. Umieszczenie okna w takiej warstwie ściany spowoduje rozprzestrzenienie się otworu na inne warstwy ściany w oparciu o tę samą linię bazową.
-   Ściany mogą również korzystać z [Wielomateriałowej struktury](Arch_MultiMaterial/pl.md). Korzystając z wielu materiałów, ściana stanie się wielowarstwowa, korzystając z grubości określonych przez wiele materiałów. Każda warstwa o grubości zerowej będzie miała swoją grubość automatycznie określoną przez pozostałe miejsce określone przez Wartość Szerokość ściany, po odjęciu innych warstw.
-   Ściany mogą wyświetlać bloki zamiast pojedynczej bryły, przez włączenie ich właściwości **Utwórz bloki**. Rozmiar i przesunięcie bloków można skonfigurować za pomocą różnych właściwości, a liczba bloków jest automatycznie obliczana.



## Przyciąganie

1.  Wybierz jeden lub więcej obiektów geometrii bazowej *(szkic obiektu, szkic itp.)*.
2.  Naciśnij przycisk **<img src="images/Arch_Wall.svg" width=16px> '''Ściana'''** lub naciśnij klawisze **W**, a następnie **A**.
3.  Dostosuj potrzebne właściwości, takie jak wysokość lub szerokość.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Druga ściana przylegająca prostopadle do pierwszej.*



## Właściwości

Obiekty Ścian dziedziczą właściwości obiektów [Część](Part_Workbench/pl.md), a także posiadają następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Blok}}

-    **Wysokość Bloku**: Wysokość każdego bloku.

-    **Długość Bloku**: Długość każdego bloku.

-    **Liczba Zniszczonych**: Liczba zniszczonych bloków *(tylko do odczytu)*.

-    **Liczba Wystąpień**: Liczba wszystkich bloków *(tylko do odczytu)*.

-    **Połączenie**: Rozmiar spoiny, pusta przestrzeń między blokami.

-    **Twórz Bloki**: Włącza generowanie bloków.

-    **Odsunięcie Pierwszego**: Poziome przesunięcie pierwszej i każdej nieparzystej linii bloków.

-    **Odsunięcie Drugiego**: Poziome przesunięcie drugiej i każdej parzystej linii bloków.


{{TitleProperty|Komponent}}

Zobacz również: [Komponent](Arch_Component/pl#Właściwości.md).


{{TitleProperty|IFC}}

Zobacz również: [Komponent](Arch_Component/pl#Właściwości.md).


{{TitleProperty|Atrybuty IFC}}

Zobacz również: [Komponent](Arch_Component/pl#Właściwości.md).


{{TitleProperty|Ściana}}

-    **Wyrównanie**: Wyrównanie ściany na jej linii bazowej: Lewo, Prawo lub Środek. Kierunek pojedynczych krawędzi obiektu bazowego (szkicu/szkicu architektury) jest brany pod uwagę, dając większą kontrolę nad każdym segmentem ściany. Zobacz schemat poniżej. Łuki w szkicach są zawsze przeciwne do ruchu wskazówek zegara. Gdy zakrzywiony segment ściany jest wyrównany w lewo, wewnętrzna krawędź segmentu pasuje do łuku szkicu. Zobacz również **Nadpisywanie krawędzi**.

-    **Powierzchnia**: Powierzchnia całej ściany, podział na bloki nie ma znaczenia *(tylko do odczytu)*.

-    **Powierzchnia**: Powierzchnia całej ściany, podział na bloki nie ma znaczenia *(tylko do odczytu)*.

-    **Ściana**: Indeks ściany z obiektu bazowego do użycia. Jeśli wartość nie jest ustawiona lub wynosi 0, używany jest cały obiekt.

-    **Wysokość**: Wysokość ściany. Ignorowane, jeśli ściana oparta jest na bryle. Jeśli ustawiono na zero, a ściana znajduje się wewnątrz obiektu [Piętro](Arch_Floor/pl.md) z zdefiniowaną wysokością, ściana automatycznie przyjmie wartość wysokości piętra.

-    **Długość**: Długość ściany. Wartość może być edytowana jeśli ściana jest oparta na niezwiązanym szkicu z pojedynczą krawędzią lub na [polilinii](Draft_Wire/pl.md) z pojedynczą krawędzią, w innym wypadku wartość jest tylko do odczytu. {{Version/pl|1.0}} Wartość w przypadku właściwości będącej tylko do odczytu jest dokładniejsza. Jest oparta na medium ściany jeśli segmenty mają różne właściwości **Szerokość**, **Wyrównanie** i/lub **Odsunięcie**. Zauważ, że nadal mogą występować niedokładności jeśli ściana jest skomplikowana, np. ma przecięcia w kształcie litery T lub samoprzecięcia. W takich przypadkach zalecane jest użycie zamiast tego właściwości **Obszar poziomy** do dalszych obliczeń.

-    **Normalna**: Kierunek wyciągania dla ściany. Jeśli ustawiono na (0,0,0), kierunek wyciągania jest automatyczny.

-    **Odsunięcie**: Odległość między ścianą a jej linią bazową. Działa tylko, jeśli właściwość **Wyrównanie** jest ustawiona na Prawo lub Lewo. Kierunek pojedynczych krawędzi obiektu bazowego (szkicu/szkicu architektury) jest brany pod uwagę, dając większą kontrolę nad każdym segmentem ściany. Zobacz również **Zastąp Odsunięcie**.

-    **Nadpisywanie krawędzi**: *({{Version/pl|1.0}})* Wprowadzane są numery indeksowe krawędzi geometrii Bazowego obiektu ArchSketch / Szkic *(w trybie Edycji)*. Wybrane krawędzie są używane do tworzenia kształtu tej ściany kurtynowej architektury (zamiast domyślnego używania wszystkich krawędzi). Ignorowane, jeśli Bazowy szkic dostarczył wybrane krawędzie. AKTUALIZACJA przez ArchSketch: Narzędzie GUI \"Edytuj ścianę kurtynową\" jest dostępne w zewnętrznym <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [dodatku SketchArch](https://github.com/paullee0/FreeCAD_SketchArch), aby umożliwić użytkownikom interaktywny wybór krawędzi. \"Toponaming-Tolerant\", jeśli ArchSketch jest używany jako baza 
*(i zainstalowany jest dodatek SketchArch)*. Ostrzeżenie: Nie jest \'Toponaming-Tolerant\', jeśli używany jest tylko Szkic. *(Zobacz wątek na forum - <https://forum.freecad.org/viewtopic.php?t=73018&start=40#p756554>)*

-    **Nadpisz Szerokość**: Zastępuje atrybut **Szerokość**, aby ustawić szerokość każdego segmentu ściany. Ignorowane, jeśli obiekt bazowy udostępnia informacje o szerokości za pomocą metody getWidths() *(jeśli wartość wynosi zero, zostanie zastosowana wartość \"Szerokość\")*. AKTUALIZACJA przez ArchSketch: Narzędzie GUI \"Edytuj ścianę kurtynową\" jest dostępne w zewnętrznym <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [dodatku SketchArch](https://github.com/paullee0/FreeCAD_SketchArch), aby umożliwić użytkownikom interaktywny wybór krawędzi. \"Toponaming-Tolerant\", jeśli ArchSketch jest używany jako baza 
*(i zainstalowany jest dodatek SketchArch)*. Ostrzeżenie: Nie jest \"Toponaming-Tolerant\", jeśli używany jest tylko Szkic. *(Zobacz wątek na forum - <https://forum.freecad.org/viewtopic.php?t=73018&start=40#p756554>)*

-    **Zastąp Odsunięcie**: (<small>(v1.0)</small> ) Parametr ten zastępuje atrybut **Odsunięcie** w celu ustawienia odsunięcia każdego segmentu ściany. Ignorowane, jeśli obiekt Bazowy dostarcza informacji o przesunięciach za pomocą metody getOffsets() (jeśli wartość wynosi zero, zostanie zastosowana wartość \"Offset\"). AKTUALIZACJA przez ArchSketch: Narzędzie GUI \"Edytuj przesunięcie segmentu ściany\" jest dostępne w zewnętrznym dodatku<img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [SketchArch](https://github.com/paullee0/FreeCAD_SketchArch), aby umożliwić użytkownikom interaktywny wybór krawędzi. \"Toponaming-Tolerant\", jeśli ArchSketch jest używany jako Baza *(i zainstalowany jest dodatek SketchArch)*. Ostrzeżenie: Nie jest \"Toponaming-Tolerant\", jeśli używany jest tylko Szkic. Właściwość jest ignorowana, jeśli Base ArchSketch dostarczył wybrane krawędzie.

-    **Szerokość**: Szerokość ściany. Ignorowana jeśli ściana jest oparta o powierzchnię lub bryłę. Zobacz również **Nadpisz Szerokość**.

<img alt="" src=images/Sketch_vs_Wall.jpg  style="width:480px;">



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Ściana** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Tworzy obiekt `Wall` na podstawie podanego obiektu `baseobj`, który może być obiektem środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md), [Szkicownik](Sketcher_Workbench/pl.md), ścianą lub bryłą.
    -   Jeśli nie podano `baseobj`, można podać numeryczne wartości dla `length`, `width` *(grubości)* i `height`.
    -   Jeśli podano, `face` może być używane do podania indeksu twarzy z podstawowego obiektu, na którym ma być zbudowana ta ściana, zamiast używania całego obiektu.

-    `wyrównanie`może mieć wartość `"Center"`, `"Left"` lub `"Right"`.

-   Zwraca `None`, jeśli operacja się nie powiedzie.

Przykład:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Wall/pl
