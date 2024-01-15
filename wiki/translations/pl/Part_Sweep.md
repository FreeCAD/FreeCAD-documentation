---
 GuiCommand:
   Name: Part Sweep
   Name/pl: Część: Wyciągnięcie po ścieżce
   MenuLocation: Część , Wyciągnięcie po ścieżce
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_Loft/pl
---

# Part Sweep/pl



## Opis

Narzędzie <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Wyciągnięcie po ścieżce](Part_Sweep/pl.md) jest używane do tworzenia powierzchni, powłoki lub bryły z jednego lub więcej profili *(przekrojów)* rozmieszczonych wzdłuż ścieżki.

Narzędzie **Wyciągnięcie po ścieżce** środowiska pracy Część jest podobne do narzędzia <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Wyciągnięcie przez profile](Part_Loft/pl.md) z dodatkiem ścieżki do definiowania rzutu pomiędzy profilami.

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*Bryła wygenerowana z pojedynczego profilu ''(A)'' rozmieszczonego wzdłuż linii grzbietu ''(B)''.*



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Sweep.svg" width=16px> '''Wyciągnięcie po ścieżce ...'''**.
    -   Wybierz opcję z menu **Część → <img src="images/Part_Sweep.svg" width=16px> Wyciągnięcie po ścieżce ...**.
2.  Otworzy się [panel zadań](Task_panel/pl.md) Wyciągnięcie po ścieżce.
3.  Na liście *Dostępne profile* po lewej stronie wybierz profil i kliknij strzałkę w prawo, aby umieścić go na liście *Wybrane profile* po prawej stronie.
4.  Powtórz, jeśli wymagany jest więcej niż jeden profil.
5.  Strzałki w górę i w dół zmieniają kolejność listy po prawej stronie. Nie ma to jednak wpływu na wynik. Położenie profili wzdłuż linii grzbietu określa kolejność ich użycia.
6.  Kliknij przycisk **Ścieżka wyciągnięcia**, a następnie wybierz jeden z trybów wyboru:
    -   *Wybór ścieżki*: wybierz jedną lub więcej sąsiadujących krawędzi w oknie [widoku 3D](3D_view/pl.md) *(naciśnij **CTRL** dla wielokrotnego wyboru)* i kliknij **Gotowe**. Przeciągnięcie zostanie wygenerowane tylko wzdłuż wybranych krawędzi.
    -   *Pełny wybór ścieżki*: przełącz się do [Widoku drzewa](Tree_view/pl.md), wybierz obiekt, który ma być użyty jako grzbiet, przełącz się z powrotem do panelu zadań i kliknij **Gotowe**. Przeciągnięcie zostanie wygenerowane wzdłuż wszystkich ciągłych krawędzi znalezionych w obiekcie.
7.  Zdefiniuj opcje [Utwórz bryłę](#Utwórz_bryłę.md) i [Wektor Freneta](#Wektor_Freneta.md).
8.  Kliknij **OK**.



### Akceptowana geometria 

-   **Profile**: mogą być punktem *(wierzchołkiem)*, linią *(krawędzią)*, konturem lub ścianą. Krawędzie i kontury mogą być otwarte lub zamknięte. Istnieją różne [ograniczenia](#Ograniczenia.md), patrz poniżej.

-   **Ścieżka**: może być linią *(krawędzią)* lub serią linii połączonych, linią złożoną lub różnymi elementami pierwotnymi środowiska Część, elementami środowiska Rysunek Roboczy, lub szkicem. Ścieżka może być otwarta lub zamknięta.

-   Obiekty typu[odnośnik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów oraz kontenery typu [część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako profile i ścieżki. {{Version/pl|0.20}}



## Opcje



#### Utwórz bryłę 

Jeśli opcja **Utwórz bryłę** jest ustawiona na wartość {{True/pl}} *(wybrana)*, FreeCAD utworzy bryłę, pod warunkiem, że profile mają geometrię zamkniętą. Jeśli opcja jest ustawiona na wartość {{False/pl}}, zostanie utworzona powierzchnia lub powłoka dla profili otwartych lub zamkniętych.



#### Wektor Freneta 

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;"> Opcja **Wektor Freneta** kontroluje, w jaki sposób orientacja profilu zmienia się podczas podążania wzdłuż ścieżki przeciągania. Jeśli opcja ta ma wartość {{False/pl}} *(nie została wybrana)*, orientacja profilu jest utrzymywana na stałym poziomie od punktu do punktu. Wynikowy kształt ma minimalne możliwe skręcenie. Nieintuicyjnie, gdy profil jest przemieszczany wzdłuż spirali, powoduje to powolne pełzanie *(obracanie)* orientacji profilu podczas przemieszczania się wzdłuż ścieżki. Ustawienie opcji **Wektor Freneta** na wartość {{True/pl}} zapobiega takiemu pełzaniu.

Jeśli opcja **Wektor Freneta** ma wartość {{true/pl}}, orientacja profilu jest obliczana na podstawie wektorów lokalnej krzywizny i styczności ścieżki. Utrzymuje to orientację profilu spójną podczas przeciągania wzdłuż spirali *(ponieważ wektor krzywizny prostej spirali jest zawsze skierowany do jej osi)*. Jednakże, gdy ścieżka nie jest spiralą, wynikowy kształt może czasami mieć dziwnie wyglądające skręcenia. Więcej informacji na ten temat można znaleźć na stronie [Formuły Freneta Serreta](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).



#### Przejście

Opcja \"Przejście\" ustawia styl przejścia Przeciągnięcia na niestycznych połączeniach na ścieżce. Właściwość nie jest widoczna w panelu zadań i można ją znaleźć w [Edytorze własciwości](Property_editor/pl.md) po utworzeniu przeciągnięcia.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Wyciągnięcia po ścieżce** wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Przeciągnięcie}}

-    **Profile|LinkList**: lista używanych profili.

-    **Kręgosłup|LinkSub**: kręgosłup *(ścieżka)*, wzdłuż którego ma przebiegać trasa.

-    **Bryła|Bool**: przyjmuje wartości {{True/pl}} lub {{False/pl}} *(domyślnie)*. Wartość {{True/pl}} oznacza utworzenie bryły.

-    **Frenet|Bool**: przyjmuje wartości {{True/pl}} lub {{False/pl}} *(domyślnie)*. Wartość {{True/pl}} oznacza użycie algorytmu Frenet.

-    **Przejście|Enumeration**: tryb przejścia. Dostępne opcje to \'*\'Przekształcenie*, *Ostry narożnik* lub *Zaokrąglony narożnik*.



## Ograniczenia



### Wierzchołek lub punkt 

Wierzchołek lub punkt może być użyty tylko jako pierwszy i / lub ostatni profil. Na przykład:

-   Nie można wykonać przeciągnięcia od okręgu do punktu, do elipsy.
-   Można jednak przejść od punktu do okręgu, przez elipsę do innego punktu.



### Profile

Podczas jednego cyklu przeciągania wszystkie profile *(linie, polilinie itp.)* muszą być otwarte lub zamknięte. Przykładowo:

-   Program FreeCAD nie może przeciągać między okręgiem środowiska Część a linią środowiska Część.



### Szkic

-   Profil można utworzyć za pomocą szkicu. Jednak tylko prawidłowe szkice będą dostępne do wyboru w panelu zadań.
-   Szkic musi zawierać tylko jedną otwartą lub zamkniętą polilinię lub linię *(może to być wiele linii, jeśli wszystkie te linie są połączone w taki sposób, że stanowią jedną polilinię)*.



### Obiekty środowiska Rysunek Roboczy 

Profil może być obiektem środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).
Następujące obiekty mogą być poprawnymi profilami:

-   punkt,
-   Linia, Polilinia,
-   krzywa złożona, krzywa Béziera,
-   okrąg, elipsa,
-   prostokąt, wielokąt.



### Obiekty środowiska Część 

Profil może być obiektem środowiska pracy Część utworzonym za pomocą narzędzia [Utwórz geometrię pierwotną](Part_Primitives/pl.md).
Następujące obiekty mogą być prawidłowymi profilami:

-   punkt *(wierzchołek)*,
-   linia *(krawędź)*,
-   spirala,
-   okrąg, elipsa,
-   wielokąt foremny,
-   płaszczyzna.



## Odnośniki internetowe 

-   Ponieważ funkcja ta jest często używana do tworzenia gwintów dla śrub, powinieneś zobaczyć stronę [Przewodnik: Tworzenie gwintów](Thread_for_Screw_Tutorial/pl.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/pl
