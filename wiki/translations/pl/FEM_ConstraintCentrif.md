---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintCentrif
   Name/pl: MES Obciążenie siłą odśrodkową
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Obciążenie siłą odśrodkową
   Workbenches: FEM_Workbench/pl
   Shortcut: 
   Version: 0.20
   SeeAlso: 
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ConstraintCentrif/pl



## Opis

Definiuje obciążenie siłą odśrodkową bryły.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintCentrif.svg" width=16px> [Obciążenie siłą odśrodkową](FEM_ConstraintCentrif/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintCentrif.svg" width=16px> Obciążenie siłą odśrodkową** z menu.
2.  Podaj częstotliwość obrotów w Hz.
3.  Wciśnij przycisk **Dodaj** w oknie **Wybór geometrii odniesienia dla Solid** i w [widoku 3D](3D_view.md) wybierz bryłę, do której obciążenie ma być przypisane.
4.  Wciśnij przycisk **Dodaj** w oknie **Wybór geometrii odniesienia dla Edge** i w [widoku 3D](3D_view.md) wybierz krawędź, która ma stanowić oś obrotu.



## Uwagi

-   To narzędzia korzysta ze [słowa kluczowego \*DLOAD w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintCentrif/pl
