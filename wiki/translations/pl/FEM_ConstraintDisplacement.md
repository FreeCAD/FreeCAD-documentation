---
 GuiCommand:
   Name: FEM ConstraintDisplacement
|Name/pɬMES Warunek brzegowy przemieszczenia
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Warunek brzegowy przemieszczenia
   Workbenches: FEM_Workbench/pl
   Shortcut: 
   SeeAlso: FEM_tutorial/pl
---

# FEM ConstraintDisplacement/pl



## Opis

Tworzy warunek brzegowy MES przemieszczenia wybranego obiektu dla określonego stopnia swobody.



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> [Warunek brzegowy przemieszczenia](FEM_ConstraintDisplacement/pl.md)** lub wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Warunek brzegowy przemieszczenia**.
2.  W [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego ma być przyłożony warunek brzegowy. Może to być wierzchołek, krawędź lub ściana.
3.  Wciśnij przycisk **Dodaj**.
4.  Zaznacz właściwe pola do edycji.
5.  Ustaw wartości lub ({{Version/pl|0.21}}) podaj równanie dla przemieszczeń.



## Równania


{{Version/pl|0.21}}



### Ogólne

Dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solvera Elmer](FEM_SolverElmer/pl.md) istnieje możliwość zdefiniowania przemieszczenia jako formuły. W tym przypadku solver ustawia przemieszczenia zgodnie z wprowadzoną zmienną równania.

Załóżmy, że chcemy przeprowadzić [analizę ze zmiennością w czasie](FEM_SolverElmer_SolverSettings#Timestepping_(transient_analyses).md). Dla każdego kroku czasowego, przemieszczenie $d$ powinno być zwiększane o 6 mm:

$\quad
d(t)=0.006\cdot t$

wprowadź to w polu *Wzór*: ` Variable "time"; Real MATC "0.006*tx"`

Ten kod ma następującą składnię:

-   przedrostek *Variable* określa, że przemieszczenie nie jest stałą tylko zmienną
-   zmienną jest bieżący czas
-   wartości przemieszczenia są zwracane jako wartości *Real* (rzeczywiste zmiennoprzecinkowe)
-   *MATC* to przedrostek dla solvera Elmer oznaczający, że następujący kod jest równaniem
-   *tx* jest zawsze nazwą zmiennej w równaniach *MATC*, mimo że w naszym przypadku *tx* to *t*



### Obroty

Elmer korzysta tylko z pól warunku brzegowego **Przemieszczenie \***. Aby zdefiniować obroty, potrzebne jest równanie.

Przykładowo, jeśli ściana powinna być obrócona zgodnie z tym warunkiemː

$\quad
\begin{align}
d_{x}(t)= & \left(\cos(\phi)-1\right)x-\sin(\phi)y\\
d_{y}(t)= & \left(\cos(\phi)-1\right)y+\sin(\phi)x
\end{align}$

to należy wprowadzić jako **Przemieszczenie x** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(1)-sin(tx(0)*pi)*tx(2)`

a jako **Przemieszczenie y** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(2)+sin(tx(0)*pi)*tx(1)`

Ten kod ma następującą składnię:

-   mamy 4 zmienne - czas i wszystkie możliwe współrzędne (x, y z)
-   *tx* jest wektorem, *tx(0)* odnosi się do pierwszej zmiennej - czasu, podczas gdy *tx(1)* odnosi się do pierwszej współrzędnej - *x*
-   *pi* oznacza $\pi$ i zostało dodane aby po $t=1\rm\, s$ został przeprowadzony obrót o 180°



## Uwagi

Dla <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md):

-   To narzędzie korzysta ze słowa kluczowego \*BOUNDARY.
-   Blokowanie stopnia swobody jest wyjaśnione na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html>
-   Zadawanie wartości przemieszczenia dla stopnia swobody jest opisane na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/pl
