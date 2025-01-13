---
 GuiCommand:
   Name: Sketcher BSplineInsertKnot
   Name/pl: Szkicownik: Wstaw węzeł krzywej złożonej
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Wstaw węzeł
   Workbenches: Sketcher_Workbench/pl
   Version: 0.20
   SeeAlso: Sketcher_BSplineKnotMultiplicity/pl, Sketcher_BSplineIncreaseKnotMultiplicity/pl, Sketcher_BSplineDecreaseKnotMultiplicity/pl
---

# Sketcher BSplineInsertKnot/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:24px;"> **Wstaw węzeł** wstawia węzeł do [krzywej złozonej](B-Splines/pl.md). Jeśli węzeł już istnieje przy określonym parametrze, jego krotność jest zwiększana o jeden.



## Użycie

1.  Wybierz krzywą złożoną.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:16px"> '''Wstaw węzeł krzywej złożonej'''**.

    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika krzywej złożonej → <img src="images/Sketcher_BSplineInsertKnot.svg" width=16px> Wstaw węzeł krzywej złożonej**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widok 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_BSplineInsertKnot.svg" width=16px> Wstaw węzeł** z menu podręcznego.
3.  Przesuń kursor do wybranej lokalizacji.
4.  Bieżąca pozycja jest oznaczona małym kółkiem i wskazana jest jej wartość parametru.
5.  Kliknij, aby wstawić węzeł lub kliknij istniejący węzeł, aby zwiększyć jego krotność.
6.  To narzędzie zawsze działa w trybie kontynuacji: opcjonalnie można kontynuować wstawianie węzłów i / lub zwiększanie krotności.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom narzędzie do tworzenia geometrii lub wiązań.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineInsertKnot/pl
