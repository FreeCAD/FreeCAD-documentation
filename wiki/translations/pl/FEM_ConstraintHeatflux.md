---
 GuiCommand:
   Name: FEM ConstraintHeatflux
   Name/pl: MES: Obciążenie strumieniem ciepła
   MenuLocation: Model , Warunki brzegowe i obciążenia termiczne , Obciążenie strumieniem ciepła
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM ConstraintHeatflux/pl



## Opis

Definiuje konwekcyjny strumień ciepła na powierzchni o temperaturze *T* ze współczynnikiem przejmowania ciepła *h* i z temperaturą otoczenia *T~0~*. Konwekcyjny strumień ciepła *q* będzie spełniał zależność: ***q = h(T -T~0~)***. Opcjonalne, może również definiować zwykły strumień ciepła na powierzchni.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Obciążenie strumieniem ciepła](FEM_ConstraintHeatflux/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia termiczne → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Obciążenie strumieniem ciepła** z menu.
2.  W [widoku 3D](3D_view/pl.md) wybierz powierzchnie, do których to obciążenie ma być przypisane.
3.  Wprowadź wartość współczynnika przejmowania ciepła i temperatury otoczenia.



### Opcje

Domyślnie to narzędzie definiuje konwekcyjny strumień ciepła. Korzystając z opcji **Strumień ciepła na powierzchni** można zdefiniować wartość strumienia ciepła w Watach na jednostkę powierzchni (W/m\^2).



## Uwagi

-   Obciążenie strumieniem ciepła korzysta ze słowa kluczowego \*FILM w CalculiX. Jest to opisane na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>
-   Opcja **Strumień ciepła na powierzchni** korzysta ze słowa kluczowego \*DFLUX w CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/pl
