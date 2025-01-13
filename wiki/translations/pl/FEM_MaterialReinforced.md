---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MaterialReinforced
   Name/pl: MES Materiał zbrojony 
   MenuLocation:  Model , Materiały , Materiał zbrojony 
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM MaterialReinforced/pl



## Opis

Tworzy materiał o zbrojonej matrycy. Łączy materiał matrycy (np. beton) z materiałem zbrojenia (np. stal).



## Użycie

1.  Aby stworzyć nowy obiekt MaterialReinforced:
    -   Kliknij przycisk **<img src="images/FEM_MaterialReinforced.svg" width=16px> [Materiał zbrojony (beton)](FEM_MaterialReinforced/pl.md)** lub wybierz opcję **Model → Materiały → <img src="images/FEM_MaterialReinforced.svg" width=16px> Materiał zbrojony (beton)** z menu.
2.  Aby edytować istniejący obiekt MaterialReinforced:
    -   Kliknij na nim dwukrotnie w [widoku drzewa](Tree_view/pl.md).
3.  Wybierz materiał matrycy.
4.  Opcjonalnie, wciśnij przycisk **Edytuj** aby edytować jego właściwości. Następujące stałe materiałowe są wymaganeː moduł Younga, współczynnik Poissona, wytrzymałość na ściskanie oraz kąt tarcia.
5.  Wybierz materiał zbrojenia.
6.  Opcjonalnie, wciśnij przycisk **Edytuj** aby edytować jego właściwości. Granica plastyczności musi być zdefiniowana.



## Uwagi

-   W ustawieniach solvera CalculiX należy ustawić Material Nonlinearity na linear jeśli [Nieliniowy materiał mechaniczny](FEM_MaterialMechanicalNonlinear/pl.md) nie jest zdefiniowany.
-   Więcej informacji na temat tego narzędzia oraz przykład jego użycia można znaleźć na stronie [MES: Analiza betonu zbrojonego](Analysis_of_reinforced_concrete_with_FEM/pl.md).
-   Aby zapoznać się z samouczkiem wideo *(opartym na [poradniku FEM](FEM_tutorial/pl.md))*, który wykorzystuje to narzędzie, obejrzyj: [Poradnik FEM Materiał zbrojony](https://www.youtube.com/watch?v=SZTIqhfCSVc).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialReinforced/pl
