---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ElementGeometry2D
   Name/pl: MES: Grubość powłoki
   MenuLocation: Model , Geometria elementu , Grubość powłoki
   Workbenches: FEM_Workbench/pl
   Shortcut: **C** **S**
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Wszystkie
}}
---

# FEM ElementGeometry2D/pl



## Opis

**ElementGeometry2D** jest używane do definiowania grubości elementów 2D (powłokowych i {{Version/pl|1.0}}: płaskiego stanu naprężeń/odkształceń), wszystkich lub należących do wybranej powierzchni.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Grubość powłoki](FEM_ElementGeometry2D/pl.md)**.
    -   Wybierz opcję **Model → Geometria elementu → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Grubość powłoki** z menu.
2.  Podaj grubość powłoki.
3.  Opcjonalnie, wciśnij przycisk **Dodaj** w panelu zadań a następnie kliknij na powierzchni, dla której chcesz przypisać grubość. Jeśli żadna powierzchnia nie zostanie wskazana, wszystkie pozostałe powierzchnie *(których grubości nie są zdefiniowane przy pomocy innych obiektów **Grubość powłoki 2D**)* będą automatycznie użyte.



## Ograniczenia

-   Obecnie analizy łączące elementy powłokowe z bryłowymi lub belkowymi nie są wspierane.



## Właściwości


**Grubość**

: Określa grubość elementów 2D.



## Uwagi

Do wyświetlania wyników z solvera CalculiX na siatce ze zwizualizowaną grubością, należy ustawić właściwość `Beam Shell Result Output 3D` w [solverze CalculiX](FEM_SolverCalculixCxxtools/pl.md) na wartość {{True/pl}}.

-   To narzędzie korzysta ze [słowa kluczowego \*SHELL SECTION w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node238.html) dla elementów powłokowych i [słowa kluczowego \*SOLID SECTION](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node239.html) dla elementów płaskiego stanu naprężeń/odkształceń.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/pl
