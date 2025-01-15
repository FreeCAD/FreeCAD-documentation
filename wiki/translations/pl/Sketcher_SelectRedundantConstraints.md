---
 GuiCommand:
   Name: Sketcher SelectRedundantConstraints
   Name/pl: Szkicownik: Wybierz zbędne wiązania
   MenuLocation: Szkic , Widok szkicu , Wybierz zbędne wiązania
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **P** **R**
   Version: 0.15
---

# Sketcher SelectRedundantConstraints/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> **Zaznacz nadmiarowe wiązania** wybiera zbędne wiązania w szkicu.

Jeśli takie wiązania istnieją w szkicu, [sekcja komunikatów Solvera w oknie dialogowym Szkicownika](Sketcher_Dialog/pl#Komunikaty_solvera.md) wyświetla następujący komunikat:

-   Wiązania nadmiarowe: (#, #, #)

Gdzie *(#, #, #)* to indeksy więzów. Kliknięcie podkreślonego tekstu spowoduje wybranie zbędnych wiązań.

Należy pamiętać, że szkic może mieć również nadmiarowe wiązania, jeśli wyświetlany jest jeden z innych [komunikatów solvera](Sketcher_Dialog/pl#Komunikaty_solvera.md).



## Użycie

1.  Narzędzie można wywołać na kilka sposobów:
    -   Kliknij podkreślony tekst w oknie dialogowym szkicownika, jak opisano powyżej.
    -   Wybierz z menu opcję **Szkic → Widok szkicu → <img src="images/Sketcher_SelectRedundantConstraints.svg" width=16px> Zaznacz nadmiarowe wiązania**.
    -   Użyj skrótu klawiaturowego: **Z**, następnie **P**, a potem **R**.
2.  Nadmiarowe ograniczenia zostaną zaznaczone.
3.  Opcjonalnie kliknij w pustym obszarze w [widoku 3D](3D_view/pl.md), aby usunąć zaznaczenie.



## Uwagi

-   Zbędne wiązania muszą zostać usunięte ze szkicu.
-   Zamiast proponowanych indeksów możliwe jest również usunięcie innych wiązań.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/pl
