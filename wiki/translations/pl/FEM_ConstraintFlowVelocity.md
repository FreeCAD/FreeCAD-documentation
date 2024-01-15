---
 GuiCommand:
   Name: FEM ConstraintFlowVelocity
   Name/pl: MES: Warunek brzegowy prędkości przepływu
   MenuLocation: Model , Warunki brzegowe dla płynu , Warunek brzegowy prędkości przepływu
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintInitialFlowVelocity/pl
---

# FEM ConstraintFlowVelocity/pl



## Opis

Definiuje prędkość przepływu jako warunek brzegowy dla krawędzi w 2D lub powierzchni w 3D.



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> [Warunek brzegowy prędkości przepływu](FEM_ConstraintFlowVelocity/pl.md)** lub wybierz opcję **Model → Warunki brzegowe dla płynu → <img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> Warunek brzegowy prędkości przepływu**.
2.  Wybierz docelowe krawędzie lub ściany.
3.  Wciśnij przycisk **Dodaj**.
4.  Odznacz *nieokreślony* żeby aktywować wymagane pola do edycji.
5.  Wprowadź wartości prędkości lub (<small>(v0.21)</small> ) równanie.



## Równania


<small>(v0.21)</small> 

Jest możliwe definiowanie prędkości poprzez określenie profilu prędkości równaniem. W takim przypadku solver ustawia prędkości w różnych miejscach zgodnie z profilem.

Przykładowo, aby zdefiniować profil prędkości

$\quad
v_{x} (y)=6\left(y-1\right)\left(2-y\right)$

dla $y\in[1;2]$ (zakładając, że np. rura ma ścianę na y = 1 m i y = 2 m)

wprowadź to w polu *wzór*: ` Variable Coordinate 2; Real MATC "6*(tx-1)*(2-tx)"`

Ten kod ma następującą składnięː

-   przedrostek *Variable* wskazuje, że prędkość nie jest stałą, lecz zmienną
-   zmienna do obliczenia prędkości to*Coordinate 2*, co oznacza współrzędną y
-   wartości prędkości są zwracane jako *Real* (rzeczywiste liczby zmiennoprzecinkowe)
-   *MATC* to przedrostek dla solvera Elmer oznaczający, że kod jest równaniem
-   *tx* jest zawsze nazwą zmiennej w równaniach *MATC*, mimo że *tx* w naszym przypadku to tak naprawdę *y*

Zakres $y\in[1;2]$ dla *y* jest ustawiony, ponieważ *MATC* określa tylko zakres *tx*, w którym wynik jest dodatni. To zachowanie jest dość specyficzne, ale ma tę zaletę, że nie trzeba określać zakresu ręcznie.

Jest również możliwe używanie więcej niż jednej zmiennej. P̪rzykład można znaleźć w postaci definicji obrotów dla [warunku brzegowego przemieszczenia](FEM_ConstraintDisplacement#Rotations/pl.md).



## Uwagi

-   Każdy komponent wektora, który powinien być wynikiem solvera, musi być ustawiony na *nieokreślony*.
-   Jeśli docelowa powierzchnia lub krawędź nie jest zrównana z osiami kartezjańskiego układu współrzędnych, istnieje możliwość ustawienia opcji **Normalny do brzegu**.

    :   Jeśli opcja **Normalny do brzegu** jest zaznaczona, wektor normalny do wybranej krawędzi lub powierzchni jest X i będzie zorientowany na zewnątrz domeny siatki.
    :   Przykładowo, jeśli przepływ powietrza o prędkości 20 mm/s powinien być zadany na wlocie to z opcją **Normalny do brzegu** trzeba wprowadzić wartość -20 mm/s w polu *Prędkość x*.

-   Dla ściany z warunkiem braku poślizgu, ustaw wszystkie komponenty prędkości na 0.
-   Dla warunku symetrii, ustaw przepływ na (0, nieokreślony, nieokreślony) jeśli zaznaczona jest opcja **Normalny do brzegu**.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/pl
