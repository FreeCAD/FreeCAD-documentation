---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintTemperature
   Name/pl: MES: Warunek brzegowy temperatury
   MenuLocation: Model , Warunki brzegowe i obciążenia termiczne , Warunek brzegowy temperatury
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintTemperature/pl



## Opis

Definiuje warunek brzegowy temperatury lub, opcjonalnie, skupiony strumień ciepła.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Warunek brzegowy temperatury](FEM_ConstraintTemperature/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia termiczne → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Warunek brzegowy temperatury** z menu.
2.  Wciśnij przycisk **Dodaj**.
3.  W [widoku 3D](3D_view/pl.md) wybierz obiekty, do których warunek brzegowy ma być przypisany. Mogą to być wierzchołki, krawędzie lub ściany. Opcjonalnie, wciśnij przycisk **Usuń** i kliknij na obiektach, które chcesz usunąć z zaznaczenia.
4.  Wybierz typ obciążenia i podaj jego wartość:
    -   *Temperature* (domyślne) - warunek brzegowy temperatury, wprowadź wartość parametru *Temperatura* (K)
    -   *CFlux* - obciążenie skupionym strumieniem ciepła, wprowadź wartość parametru *Skupiony strumień ciepła* (mW) - ta wartość zostanie podzielona przez liczbę węzłów odpowiadających wskazanemu obiektowi geometrycznemu aby uzyskać całkowity strumień ciepła o zadanej wartości dla tego obiektu



## Uwagi

-   Warunek brzegowy temperatury korzysta ze słowa kluczowego \*BOUNDARY w CalculiX. Jest to opisane na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>
-   Opcja **Skupiony strumień ciepła** korzysta ze słowa kluczowego \*CFLUX w CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node168.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/pl
