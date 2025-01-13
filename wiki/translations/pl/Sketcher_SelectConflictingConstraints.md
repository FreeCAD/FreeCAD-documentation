---
 GuiCommand:
   Name: Sketcher SelectConflictingConstraints
   Name/pl: Szkicownik: Wybierz wiązania konfliktowe
   MenuLocation: Szkic , Widok szkicu , Wybierz wiązania konfliktowe
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **P** **C**
   Version: 0.15
---

# Sketcher SelectConflictingConstraints/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:24px;"> **Wybierz wiązania konfliktowe** wybiera konfliktowe wiązania w szkicu.

Jeśli takie wiązania istnieją w szkicu, [sekcja komunikatów Solvera w oknie dialogowym Szkicownika](Sketcher_Dialog/pl#Komunikaty_solvera.md) wyświetla następujący komunikat:

-   Wiązania nadmierne: (#, #, #)

Gdzie *(#, #, #)* to indeksy więzów. Kliknięcie podkreślonego tekstu spowoduje wybranie zbędnych wiązań.



## Użycie

1.  Narzędzie można wywołać na kilka sposobów:
    -   Kliknij podkreślony tekst w oknie dialogowym szkicownika, jak opisano powyżej.
    -   Wybierz z menu opcję **Szkic → Widok szkicu → <img src="images/Sketcher_SelectConflictingConstraints.svg" width=16px> Wybierz wiązania konfliktowe**.
    -   Użyj skrótu klawiaturowego: **Z**, następnie **P**, a potem **C**.
2.  The conflicting constraints are selected.
3.  Opcjonalnie kliknij w pustym obszarze w [widoku 3D](3D_view/pl.md), aby usunąć zaznaczenie.



## Uwagi

-   Konfliktowe wiązania muszą zostać usunięte ze szkicu.
-   Zamiast proponowanych indeksów możliwe jest również usunięcie innych wiązań.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectConflictingConstraints/pl
