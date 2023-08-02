---
- GuiCommand:
   Name: Part Sweep
   Name/pl: Część: Wyciągnięcie po ścieżce
   MenuLocation: Część -> Wyciągnięcie po ścieżce
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_Loft/pl
---

# Part Sweep/pl



## Opis

Narzędzie <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Wyciągnięcie po ścieżce](Part_Sweep/pl.md) jest używane do tworzenia powierzchni, powłoki lub bryły z jednego lub więcej profili *(przekrojów)* rzutowanych wzdłuż ścieżki.

Narzędzie **Wyciągnięcie po ścieżce** środowiska pracy Część jest podobne do narzędzia <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Wyciągnięcie przez profile](Part_Loft/pl.md) z dodatkiem ścieżki do definiowania rzutu pomiędzy profilami.

![](images/Part_Sweep_simple.png ) 
*Bryła wykonana metodą przeciągnięcia wygenerowana z pojedynczego profilu ''(A)'' rzutowanego wzdłuż ścieżki ''(B)''.*



## Użycie

1.  Naciśnij przycisk **<img src="images/Part_Sweep.svg" width=16px>. '''Narzędzie do wyciągnięcia po ścieżce'''**. Otworzy się okno parametrów **Parametry wyciągnięcia** w [panelu zadań](Task_panel/pl.md).
2.  W lewej kolumnie **Dostępne profile** *(poprzednio w wersji 0.16 wierzchołek / Krawędź / Kontur / Ściana)* kliknij w element, który ma być użyty jako profil do przeciągania, a następnie kliknij strzałkę w prawo, aby umieścić go w prawej kolumnie *Wybrane profile* *(poprzednio w wersji 0.16 Przemiatanie)*. Powtarzaj czynność, jeśli potrzebujesz więcej niż jednego profilu. Użyj strzałek w górę i w dół, aby zmienić kolejność na liście wybranych profili.
3.  Kliknij na przycisk **Ścieżka wyciągnięcia**, następnie wybierz jeden z trybów selekcji:
    -   *Wybór pojedynczego segmentu*: zaznacz jedną lub więcej sąsiadujących krawędzi w oknie [widoku 3D](3D_view/pl.md) *(naciśnij **CTRL** dla wielokrotnego wyboru)* i kliknij przycisk **Zakończ**. Przeciągnięcie zostanie wygenerowane tylko wzdłuż wybranych krawędzi.
    -   *Pełny wybór ścieżki*: przełącz się na zakładkę Model, w drzewie wybierz obiekt 2D, który ma być użyty jako ścieżka, przełącz się z powrotem na [Panel zadań](Task_panel/pl.md) i kliknij przycisk **Zakończ**. Ścieżka zostanie wygenerowana wzdłuż wszystkich sąsiadujących krawędzi obiektu 2D.
4.  Zdefiniuj opcje [Utwórz bryłę](#Utw.C3.B3rz_bry.C5.82.C4.99.md) i [Wektor_Freneta](#Wektor_Freneta.md).
5.  Kliknij w przycisk **OK**



### Akceptowana geometria 

-   **Profile**: mogą być punktem *(wierzchołkiem)*, linią *(krawędzią)*, konturem lub ścianą. Krawędzie i kontury mogą być otwarte lub zamknięte. Istnieją różne [profile ograniczenia i komplikacje](Part_Sweep/pl#Ograniczenia_i_komplikacje_profilu.md), zobacz poniżej, jednakże profile mogą pochodzić z elementów pierwotnych środowiska pracy Część, elementów środowiska pracy Rysunek Roboczy i Szkiców.

-   **Ścieżka**: może być linią *(krawędzią)* lub serią linii połączonych, linią złożoną lub różnymi elementami pierwotnymi środowiska Część, elementami środowiska Rysunek Roboczy, lub szkicem. Ścieżka jest często wybierana bezpośrednio z głównego okna modelu, jednak może być również wybrana z panela [Widok drzewa](Tree_view/pl.md) *(zakładka Model w oknie [widoku połączonego](Combo_view/pl.md))*. Ścieżka może być albo całym odpowiednim kształtem, albo odpowiednim elementem bardziej zaawansowanego kształtu *(na przykład, krawędź <img alt="" src=images/Part_Box.svg  style="width:24px;"> [sześcianu](Part_Box/pl.md) może być wybrana jako ścieżka)*.
    Ścieżka może być otwarta lub zamknięta, a zatem będzie tworzyła albo otwarte albo zamknięte Przeciągnięcie. Zamknięta ścieżka, taka jak Okrąg środowiska Część, spowoduje zamknięcie Przeciągnięcia. Na przykład pociągnięcie mniejszego okręgu wokół ścieżki z większego okręgu utworzy torus.

-   Obiekty typu[odnośnik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów oraz kontenery typu [część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako profile i ścieżki. {{Version/pl|0.20}}



## Właściwości



### Bryła

Jeśli opcja **Utwórz bryłę** jest *(wybrana)* ustawiona na wartość {{True}}, FreeCAD tworzy bryłę, pod warunkiem, że profile mają geometrię zamkniętą. Jeśli opcja jest ustawiona na wartość {{False/pl}}, program FreeCAD tworzy powierzchnię lub *(jeśli jest więcej niż jedna powierzchnia)* powłokę dla profili otwartych lub zamkniętych.



### Wektor Freneta 

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;"> Opcja **Wektor Freneta** kontroluje, w jaki sposób orientacja profilu zmienia się podczas podążania wzdłuż ścieżki przeciągania. Jeśli opcja ta ma wartość {{False/pl}} *(nie została wybrana)*, orientacja profilu jest utrzymywana na stałym poziomie od punktu do punktu. Wynikowy kształt ma minimalne możliwe skręcenie. Nieintuicyjnie, gdy profil jest przemieszczany wzdłuż spirali, powoduje to powolne pełzanie *(obracanie)* orientacji profilu podczas przemieszczania się wzdłuż spirali. Ustawienie opcji **Wektor Freneta** na wartość {{True/pl}} zapobiega takiemu pełzaniu.

Jeśli opcja **Wektor Freneta** ma wartość {{true}}, orientacja profilu jest obliczana na podstawie wektorów lokalnej krzywizny i styczności ścieżki. Utrzymuje to orientację profilu spójną podczas przeciągania wzdłuż spirali (ponieważ wektor krzywizny prostej spirali jest zawsze skierowany do jej osi). Jednakże, gdy ścieżka nie jest spiralą, wynikowy kształt może czasami mieć dziwnie wyglądające skręcenia. Więcej informacji na ten temat można znaleźć na stronie [Formuły Freneta Serreta](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).



### Przejście

Opcja **Przejście** ustawia styl przejścia Przeciągania w miejscu połączenia na ścieżce, jeśli ścieżka nie definiuje przejścia w narożniku *(na przykład gdy ścieżka jest polilinią)*. Właściwość ta nie jest widoczna w oknie [Panelu zadań](Task_panel/pl.md) i można ją znaleźć we właściwościach po utworzeniu przeciągnięcia.



## Ograniczenia i komplikacje profilu 

-   Wierzchołek lub punkt
    -   Wierzchołek lub punkt może być użyty tylko jako pierwszy i / lub ostatni profil na liście profili.
        -   Na przykład.
            -   Nie można przeciągnąć punktu z okręgu do elipsy.
            -   Można jednak przeciągnąć punkt do okręgu, elipsy do innego punktu.
-   Otwarte i zamknięte profile geometrii nie mogą być mieszane w jednym przeciągnięciu.
    -   W jednym przejściu wszystkie profile *(linie, kontury itp.)* muszą być albo otwarte, albo zamknięte.
        -   Na przykład
            -   FreeCAD nie może przeciągać pomiędzy jednym okręgiem środowiska Część i jedną domyślną linią środowiska Część.
-   Funkcje środowiska Rysunek Roboczy.
    -   Cechy środowiska Rysunek Roboczy mogą być bezpośrednio użyte jako profil w FreeCAD 0.14 lub nowszym.
        -   Na przykład następujące elementy środowiska Rysunek Roboczy mogą być użyte jako profile w funkcji Przeciągnięcia środowiska Część.
            -   wielokąt.
            -   punkt, linia, kontur,
            -   krzywa złożona, krzywa Beziera,
            -   okrąg, elipsa, prostokąt.
-   Szkice środowiska Projekt Części.
    -   Profil może zostać utworzony za pomocą szkicu. Jednak tylko prawidłowy szkic zostanie wyświetlony na liście i będzie dostępny do wyboru.
    -   Szkic musi zawierać tylko jedną otwartą lub zamkniętą linię lub polilinię *(może być wiele linii, jeśli wszystkie te linie są połączone tak jak są, wtedy jest to pojedyncza polilinia)*.
-   Środowisko pracy Część.
    -   profil może być prawidłowym elementem geometrycznym środowiska Część, który można utworzyć za pomocą narzędzia [Bryły pierwotne](Part_Primitives/pl.md) środowiska Część.
        -   Na przykład następujące geometryczne elementy pierwotne środowiska Część mogą być prawidłowym profilem
            -   punkt *(Wierzchołek)*, linia *(Krawędź)*,
            -   helisa, spirala,
            -   okrąg, elipsa,
            -   wielokąt foremny,
            -   płaszczyzna *(ściana)*.



## Odnośniki internetowe 

-   Ponieważ funkcja ta jest często używana do tworzenia gwintów dla śrub, powinieneś zobaczyć stronę [Przewodnik: Tworzenie gwintów](Thread_for_Screw_Tutorial/pl.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/pl
