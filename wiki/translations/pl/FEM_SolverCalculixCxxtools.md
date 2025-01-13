---
 GuiCommand:
   Name: FEM SolverCalculixCxxtools
   Name/pl: Narzędzia CalculiX
   MenuLocation: Rozwiąż , Narzędzia CalculiX
   Workbenches: FEM_Workbench/pl
   Shortcut: **S** **X**
   SeeAlso: FEM_tutorial/pl
---

# FEM SolverCalculixCxxtools/pl



## Opis

[Narzędzia CalculiX](FEM_SolverCalculixCxxtools/pl.md) umożliwiają użycie solvera [CalculiX](https://en.wikipedia.org/wiki/Calculix). Mogą być używane do:

1.  Ustawiania parametrów analizy
2.  Wybierania ścieżki roboczej
3.  Uruchamiania solvera CalculiX



## Użycie

1.  Obiekt <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools jest tworzony automatycznie razem z <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [kontenerem analizy](FEM_Analysis/pl.md).
    Aby utworzyć go samodzielnie, skorzystaj z jednego z poniższych sposobów:
    -   Wciśnij przycisk **<img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> '''Narzędzia CalculiX'''**.
    -   Wybierz opcję **Rozwiąż → <img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> Narzędzia CalculiX** z menu.
    -   Wciśnij przycisk **S** a następnie **X**.
2.  Opcjonalnie, zmień właściwości obiektu <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools w [edytorze właściwości](Property_editor/pl.md).
3.  Dwukrotnie kliknij obiekt <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools.
4.  Wybierz **Typ analizy**.
5.  Wciśnij przycisk **Zapisz plik wejściowy .inp**.
6.  Wciśnij przycisk **Uruchom CalculiX**.



## Opcje

Wciśnij przycisk **Edytuj plik .inp** aby wyświetlić i ręcznie edytować plik wejściowy solvera CalculiX przed uruchomieniem analizy. W takim wypadku może być przydatne ustawienie właściwości **Split Input Writer** na {{True/pl}}.



## Właściwości

Domyślne właściwości można ustawić w menu **Edycja → Preferencje ... → MES → CalculiX**

-    **Analysis Type**:

    -   static - statyczna analiza naprężeń.
    -   frequency - analiza modalna *(wyznaczenie częstotliwości i postaci drgań własnych)*.
    -   thermomech - analiza termomechaniczna.
    -   check - bez obliczeń, przeprowadza sprawdzenie danych wejściowych.
    -   buckling - liniowa analiza wyboczeniowa. {{Version/pl|0.20}}

-    **Beam Reduced Integration**\- {{Version/pl|1.0}}:

    -   
        {{true/pl}}
        
        \- używa elementów belkowych ze zredukowanym całkowaniem (B31R lub B32R), które są wymagane w przypadku korzystania z przekroju rurowego i mogą umożliwić uzyskanie [dokładnych wyników w analizach z plastycznością](https://forum.freecad.org/viewtopic.php?t=61233)

    -   
        {{false/pl}}
        
        \- używa zwykłych elementów belkowych (z pełnym całkowaniem)

-    **Beam Shell Result Output 3D**: zwróć uwagę, że CalculiX wewnętrznie przekształca elementy 1D i 2D w elementy 3D

    -   
        {{true/pl}}
        
        \- wynikowa siatka będzie zawierała elementy 1D i 2D przekształcone w elementy 3D.

    -   
        {{false/pl}}
        
        \- wyniki dla elementów 1D i 2D będą uśrednione w węzłach oryginalnych elementów 1D lub 2D *(np. belka poddana czystemu zginaniu będzie miała zerowe naprężenia w węzłach z powodu uśredniania)*.

-    **Buckling Accuracy**\- {{Version/pl|1.1}}: definiuje dokładność wyznaczania wartości własnych wyboczenia. W większości przypadków domyślna wartość (0.01) jest wystarczająca, ale niekiedy konieczne jest jej obniżenie (np. do 0.0001) aby uchwycić pierwszą postać wyboczenia.

-    **Eigenmode High Limit**: wartości własne powyżej tego limitu nie będą wyznaczane; **Uwaga**: jeśli wartości własne modelu są wyższe od tego limitu, CalculiX zakończy analizę bez wyników.

-    **Eigenmode Low Limit**: wartości własne poniżej tego limitu nie będą obliczane.

-    **Eigenmodes Count**: liczba najniższych postaci własnych do wyznaczenia.

-    **Geometric Nonlinearity**:

    -   linear - przeprowadzona zostanie analiza liniowa jeśli model nie zawiera nieliniowego materiału.
    -   nonlinear - przeprowadzona zostanie analiza nieliniowa.

-    **Iterations Control parameter Cutb**: definiuje drugą linię [zaawansowanych parametrów iteracji solvera CalculiX](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Używane jeśli właściwość **Iterations Control Parameter Time Use** jest ustawiona na {{true/pl}}.

-    **Iterations Control Parameter Iter**: definiuje pierwszą linię [zaawansowanych parametrów iteracji solvera CalculiX](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Używane jeśli właściwość **Iterations Control Parameter Time Use** jest ustawiona na {{true/pl}}.

-    **Iterations Control Parameter Time Use**-   
        {{true/pl}}
        
        \- aktywuje **Iterations Control parameter Cutb** i **Iterations Control Parameter Iter**.

    -   
        {{false/pl}}
        

-    **Iterations Maximum**: maksymalna liczba przyrostów, po której analiza zostanie zatrzymana.

-    **Iterations User Defined Incrementations**:

    -   
        {{true/pl}}
        
        \- automatyczna kontrola inkrementacji będzie wyłączona przez parametr DIRECT.

    -   
        {{false/pl}}
        
        \- kontrola inkrementacji będzie automatyczna.

-    **Iterations User Defined Time Step Length**:

    -   
        {{true/pl}}
        
        \- aktywuje parametry **Time End** i **Time Initial Step**

    -   
        {{false/pl}}
        

-    **Material Nonlinearity**:

    -   linear - w analizie będą uwzględnione tylko liniowe właściwości materiału.
    -   nonlinear - uwzględnione będą nieliniowe właściwości materiału z obiektu **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=24px> [Nieliniowy materiał mechaniczny](FEM_MaterialMechanicalNonlinear/pl.md)**.

-    **Matrix Solver Type**: typ solvera do rozwiązania układu równań w analizie MES. Może znacząco wpłynąć na szybkość obliczeń i wymogi pamięci. Wybór zależy od danego modelu MES i dostępnego komputera.

    -   default - automatycznie wybiera solver do rozwiązywania macierzowego układu równań w zależności od dostępnych solverów *(zwykle jest to Spooles)*.

    -   
        {{Version/pl|1.0}}
        
        : pastix - jeden z najszybszych solverów (obok Pardiso), dostępny (i domyślny) w oficjalnych wersjach CalculiX od ccx 2.18, może nadal powodować okazjonalne problemy

    -   
        {{Version/pl|1.0}}
        
        : pardiso - jeden z najszybszych solverów (obok PaStiX), ale z zamkniętym kodem źródłowym, wymaga innego pliku wykonywalnego CalculiX (ccx_dynamic) i dodatkowych bibliotek, które nie są dostarczane z FreeCAD, bardziej niezawodny niż PaStiX

    -   spooles - solver bezpośredni ze wsparciem dla wielu rdzeni. Liczbę rdzeni należy ustawić we [właściwościach](FEM_Preferences/pl#CalculiX.md) jako *Ustawienia domyślne solvera → Liczba rdzeni CPU do użycia*.

    -   iterativescaling - solver iteracyjny z najniższymi wymaganiami pamięci, odpowiedni jeśli model składa się głównie z elementów 3D.

    -   iterativecholesky - solver iteracyjny z prekondycjonowaniem i niskimi wymaganiami pamięci, odpowiedni jeśli model składa się głównie z elementów 3D.

-    **Model Space**\- {{Version/pl|1.0}}: przełącza między analizami 3D i 2D, te drugie wymagają geometrii powierzchniowej na płaszczyźnie XY (po prawej stronie od osi Y w przypadku osiowosymetrycznym) z [definicją grubości](FEM_ElementGeometry2D/pl.md) (wartość ignorowana w przypadku osiowosymetrycznym) i odpowiednich warunków brzegowych (należy używać [warunku brzegowego przemieszczenia](FEM_ConstraintDisplacement/pl.md) ze stopniami swobody X i Y zamiast [warunku brzegowego utwierdzenia](FEM_ConstraintFixed/pl.md)) oraz obciążeniami działającymi w płaszczyźnie zadanymi na krawędzie

    -   3D - używane są trójwymiarowe elementy bryłowe/powłokowe/belkowe
    -   plane stress - używane są elementy 2D płaskiego stanu naprężeń
    -   plane strain - używane są elementy 2D płaskiego stanu odkształceń
    -   axisymmetric - używane są elementy 2D osiowosymetryczne

-    **Output Frequency**\- {{Version/pl|1.0}}: definiuje częstotliwość zapisywania wyników w przyrostach (domyślne ustawienie 1 oznacza, że wyniki zapisywane są co przyrost, podczas gdy ustawienie wartości 2 oznaczałoby zapis wyników co 2 przyrosty itd.), ta opcja jest szczególnie przydatna do analiz nieliniowych i stanu nieustalonego, pomaga zredukować liczbę obiektów w drzewie, ponieważ obecnie para obiektów wyników (CCX_Results i Pipeline_CCX_Results) jest tworzona dla każdej klatki wyników

-    **Split Input Writer**:

    -   
        {{false/pl}}
        
        \- zapisz wszystkie dane wejściowe do jednego pliku \*.inp file.

    -   
        {{true/pl}}
        
        \- podziel zapis danych wejściowych na więcej plików \*.inp - ułatwia ręczną edycję.

-    **Thermo Mech Steady State**:

    -   
        {{true/pl}}
        
        \- analiza termomechaniczna stanu ustalonego.

    -   
        {{false/pl}}
        
        \- analiza termomechaniczna stanu nieustalonego.

-    **Thermo Mech Type**\- {{Version/pl|1.0}}:

    -   coupled - sprzężona analiza termomechaniczna,
    -   uncoupled - niesprzężona analiza termomechaniczna,
    -   pure heat transfer - analiza czysto termiczna *(\*HEAT TRANSFER)*.

-    **Time End**: czas trwania kroku, używany gdy parametr **Iterations User Defined Incrementations** lub **Iterations User Defined Time Step Length** jest ustawiony na {{true/pl}}

-    **Time Initial Step**: początkowy przyrost czasu dla kroku, używany gdy parametr **Iterations User Defined Incrementations** lub **Iterations User Defined Time Step Length** jest ustawiony na {{true/pl}}.

-    **Time Maximum Step**\- {{Version/pl|1.0}}: maksymalny przyrost czasu dla kroku, używany gdy parameter **Iterations User Defined Incrementations** lub **Iterations User Defined Time Step Length** jest ustawiony na {{true/pl}}

-    **Time Minimum Step**\- {{Version/pl|1.0}}: minimalny przyrost czasu dla kroku, używany gdy parameter **Iterations User Defined Incrementations** lub **Iterations User Defined Time Step Length** jest ustawiony na {{true/pl}}

-    **Working Dir**: ścieżka do katalogu roboczego, który będzie używany do plików solvera CalculiX.



## Ograniczenia

Podczas uruchamiania solvera CalculiX można się spotkać z błędem **error 4294977295**. Oznacza to brak wystarczającej pamięci RAM. Istnieją dwa rozwiązania:

1.  zmniejszyć gęstość siatki, najlepiej przez pominięcie geometrii, która nie jest absolutnie niezbędna do analizy.
2.  dokupić pamięć RAM do komputera.



## Uwagi

Oryginalną dokumentację solvera CalculiX można znaleźć na stronie <http://dhondt.de/> w części \"ccx\".



## Tworzenie skryptów 





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/pl
