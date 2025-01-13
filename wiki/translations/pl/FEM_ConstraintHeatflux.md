---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintHeatflux
   Name/pl: MES: Obciążenie strumieniem ciepła
   MenuLocation: Model , Warunki brzegowe i obciążenia termiczne , Obciążenie strumieniem ciepła
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintHeatflux/pl



## Opis

Domyślnie, definiuje konwekcyjny strumień ciepła na powierzchni o temperaturze $T$ ze współczynnikiem przejmowania ciepła $h$ i z temperaturą otoczenia $T_{0}$. Konwekcyjny strumień ciepła *q* będzie spełniał zależność: $q=h(T-T_{0})$. Opcjonalne, może również definiować zwykły strumień ciepła na powierzchni.


{{Version/pl|1.0}}

: Może być również używany do definiowania strumienia ciepła od promieniowania na powierzchni. Spełnia on warunek: $q=\epsilon \sigma(T^{4}-T_{0}^{4})$, gdzie $\epsilon$ to emisyjność powierzchni zaś $\sigma$ to stała Stefana-Boltzmanna.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Obciążenie strumieniem ciepła](FEM_ConstraintHeatflux/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia termiczne → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Obciążenie strumieniem ciepła** z menu.
2.  Wciśnij przycisk **Dodaj**. W [widoku 3D](3D_view/pl.md) wybierz powierzchnie, do których to obciążenie ma być przypisane. Opcjonalnie, wciśnij przycisk **Usuń** aby usunąć wybrane powierzchnie z listy wskazań.
3.  Wybierz typ strumienia ciepła i wprowadź jego dane:
    -   *Konwekcja na powierzchni* (domyślny) - konwekcyjny strumień ciepła, wprowadź odpowiedni *Współczynnik przejmowania ciepła* i *Temperaturę otoczenia*

    -   
        {{Version/pl|1.0}}
        
        : *Promieniowanie powierzchni* - strumień ciepła od promieniowania, wprowadź *Emisyjność* powierzchni i *Temperaturę otoczenia*

    -   *Strumień ciepła na powierzchni* - ogólny strumień ciepła, wprowadź *Strumień ciepła na powierzchni* w Watach na jednostkę powierzchni (W/m\^2)



## Uwagi

-   Obciążenie strumieniem ciepła korzysta z następujących słów kluczowych CalculiX w zależności od wybranego trybu:
    -   [\*FILM](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html) dla *Konwekcji na powierzchni*

    -   
        {{Version/pl|1.0}}
        
        : [\*RADIATE](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node234.html) dla *Promieniowania powierzchni*

    -   [\*DFLUX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html) dla *Strumienia ciepła na powierzchni*





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/pl
