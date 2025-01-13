---
 GuiCommand:
   Name: Sketcher Symmetry
   Name/pl: Szkicownik: Odbicie lustrzane
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Odbicie lustrzane
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **S**
   Version: 0.16
   SeeAlso: Sketcher_MirrorSketch/pl
---

# Sketcher Symmetry/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Symmetry.svg  style="width:24px;"> **Odbicie lustrzane** tworzy lustrzane kopie wybranych elementów.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Wybierz jedną lub więcej krawędzi i / lub punktów.
2.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Sketcher_Symmetry.svg" width=16px> '''Odbicie lustrzane'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_Symmetry.svg" width=16px> Odbicie lustrzane**.
    -   Skrót klawiaturowy: **Z**, a następnie **S**.
3.  Kursor zmienia się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry symetrii** ({{Version/pl|1.0}}) jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
5.  Opcjonalnie naciśnij klawisz **U** lub zaznacz pole wyboru **Usuń oryginalne geometrie**, aby zachować tylko elementy transformacji lustrzanej. {{Version/pl|1.0}}
6.  Opcjonalnie naciśnij przycisk **J** lub zaznacz pole wyboru **Utwórz wiązania symetrii**, aby dodać [Wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md) pomiędzy każdym oryginalnym i punktem transformacji lustrzanej. {{Version/pl|1.0}}
7.  Wybierz linię lub oś szkicu, aby zdefiniować linię symetrii, lub punkt, aby zdefiniować punkt symetrii.
8.  Tworzone są kopie lustrzane. Przetwarzane są również wiązania powiązane z wybranymi elementami.
    -   Jeśli wybrano opcję **Utwórz wiązania symetrii**, dodawane są wiązania symetryczne.
    -   Jeśli wybrano opcję *Usuń oryginalną geometrię*, oryginalna geometria zostanie usunięta.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Symmetry/pl
